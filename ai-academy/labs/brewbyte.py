"""Small public worked examples. Fixtures do not measure real LLM quality."""
from __future__ import annotations

import csv
import hashlib
import html
import json
import math
import re
import sqlite3
import statistics
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
MAX_INPUT = 4000
ROLES = {'public': {'public'}, 'staff': {'public', 'staff'},
         'manager': {'public', 'staff', 'manager'}}


def load_csv(name):
    with (DATA / name).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def validate_text(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError('A nonempty text string is required')
    if len(text) > MAX_INPUT:
        raise ValueError('Request exceeds the input limit')
    return text.strip()


def route(text):
    text = validate_text(text).lower()
    if 'payment' in text or 'charged' in text:
        return 'billing'
    if 'login' in text or 'password' in text:
        return 'account'
    return 'service'


def clean_tickets(rows):
    accepted, rejected, duplicates, seen = [], [], [], set()
    for row in rows:
        key = row.get('ticket_id', '')
        if key in seen:
            duplicates.append(dict(row))
            continue
        if not key.startswith('SYN-T'):
            rejected.append({'row': dict(row), 'reason': 'invalid ticket identifier'})
            continue
        seen.add(key)
        try:
            text = validate_text(row.get('description'))
            amount = float(row.get('amount', ''))
            if not math.isfinite(amount) or amount < 0:
                raise ValueError('invalid amount')
        except (TypeError, ValueError) as exc:
            rejected.append({'row': dict(row), 'reason': str(exc)})
            continue
        accepted.append({**row, 'description': text, 'amount': amount})
    assert len(accepted) + len(rejected) + len(duplicates) == len(rows)
    return accepted, rejected, duplicates


def binary_metrics(truth, predictions):
    if len(truth) != len(predictions) or not truth:
        raise ValueError('Equally sized nonempty sequences required')
    if any(x not in (0, 1) for x in [*truth, *predictions]):
        raise ValueError('Binary labels must be zero or one')
    tp = sum(y == p == 1 for y, p in zip(truth, predictions))
    fp = sum(y == 0 and p == 1 for y, p in zip(truth, predictions))
    fn = sum(y == 1 and p == 0 for y, p in zip(truth, predictions))
    tn = len(truth) - tp - fp - fn
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return dict(n=len(truth), tp=tp, fp=fp, fn=fn, tn=tn,
                precision=precision, recall=recall,
                f1=2*precision*recall/(precision+recall) if precision+recall else 0.0)


EMAIL = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')


def scrub(text):
    """Email-pattern demonstration only. Not an anonymization guarantee."""
    return EMAIL.sub('[EMAIL]', text)


def verify_manifest():
    expected = json.loads((DATA / 'manifest.json').read_text(encoding='utf-8'))
    return {name: hashlib.sha256((DATA / name).read_bytes()).hexdigest() == digest
            for name, digest in expected.items()}


def fixture_summary(text):
    """Deterministic schema fixture. Does not generate or understand text."""
    text = validate_text(text)
    return {'category': route(text), 'summary': scrub(text)[:180],
            'needs_review': True, 'backend': 'deterministic-fixture'}


def policies_for(role):
    if role not in ROLES:
        raise PermissionError('Unknown role')
    policies = json.loads((DATA / 'policies.json').read_text(encoding='utf-8'))
    return [p for p in policies if p['access'] in ROLES[role]]


def retrieve(query, role='public', k=3):
    """Permission-filtered lexical baseline; not embedding search or a full RAG."""
    query = validate_text(query)
    if not isinstance(k, int) or not 1 <= k <= 5:
        raise ValueError('k must be between one and five')
    terms = set(re.findall(r'[a-z]+', query.lower()))
    candidates = policies_for(role)  # Restrict before ranking/context assembly.
    scored = []
    for policy in candidates:
        words = set(re.findall(r'[a-z]+', policy['text'].lower()))
        overlap = len(terms & words)
        if overlap:
            scored.append((overlap, policy['id'], policy))
    return [p for _, _, p in sorted(scored, key=lambda t: (-t[0], t[1]))[:k]]


def safe_tool(name, *, role):
    if role not in ROLES:
        raise PermissionError('Unknown role')
    if name != 'read_policy':
        raise PermissionError('Only the read_policy tool is permitted')
    return {'tool': name, 'mode': 'read-only', 'role': role}


def correlate(events):
    """Toy per-user correlation over this one-hour fixture, not a production detector."""
    groups = defaultdict(list)
    for event in events:
        groups[event['user']].append(event)
    findings = []
    for user, group in sorted(groups.items()):
        failed = [e for e in group if e['outcome'] == 'failure']
        if len(failed) >= 3:
            findings.append({'user': user, 'event_ids': [e['event_id'] for e in failed],
                             'hypothesis': 'Repeated failures require investigation',
                             'confirmed_compromise': False, 'action': 'review-only'})
    return findings


def security_report():
    rows = []
    for case in json.loads((DATA / 'security-cases.json').read_text(encoding='utf-8')):
        try:
            if case['kind'] == 'tool':
                safe_tool(case['input'], role=case['role'])
                allowed = True
            elif case['kind'] == 'render':
                allowed = '<script' not in html.escape(case['input'])
            else:
                docs = retrieve(case['input'], role=case['role'])
                allowed = all(p['access'] in ROLES[case['role']] for p in docs)
            passed = allowed == case['expected_allowed']
        except PermissionError:
            passed = not case['expected_allowed']
        rows.append({'id': case['id'], 'passed': passed})
    return {'scope': 'deterministic tool, rendering and retrieval boundaries only',
            'cases': rows, 'passed': sum(r['passed'] for r in rows), 'n': len(rows)}


def ml_demo():
    """Real classical models; chronological split, fitted preprocessing in pipelines."""
    import pandas as pd
    from sklearn.cluster import KMeans
    from sklearn.dummy import DummyRegressor, DummyClassifier
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    from sklearn.pipeline import make_pipeline
    from sklearn.linear_model import LinearRegression, LogisticRegression
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_absolute_error, f1_score
    frame = pd.read_csv(DATA / 'sales.csv')
    cut = int(len(frame)*0.8)
    features = ['product', 'location', 'weekend', 'day_index']
    x, y = frame[features], frame['units']
    # Source data are date-ordered; same-date records remain on one side of the split.
    split_day = frame.iloc[cut]['day_index']
    train = frame['day_index'] < split_day
    test = ~train
    def preprocess():
        return ColumnTransformer([
            ('categories', OneHotEncoder(handle_unknown='ignore', sparse_output=False),
             ['product', 'location']),
            ('numeric', StandardScaler(), ['weekend', 'day_index'])])
    result = {}
    for name, estimator in [
        ('dummy', DummyRegressor()), ('linear', LinearRegression()),
        ('tree', DecisionTreeRegressor(max_depth=5, random_state=42)),
        ('forest', RandomForestRegressor(n_estimators=40, max_depth=8, random_state=42))]:
        pipeline = make_pipeline(preprocess(), estimator)
        pipeline.fit(x[train], y[train])
        result[name+'_mae'] = float(mean_absolute_error(y[test], pipeline.predict(x[test])))
    high_demand = (y >= 50).astype(int)
    for name, estimator in [('dummy', DummyClassifier(strategy='most_frequent')),
                             ('logistic', LogisticRegression(max_iter=500))]:
        pipe = make_pipeline(preprocess(), estimator)
        pipe.fit(x[train], high_demand[train])
        result[name+'_f1'] = float(f1_score(high_demand[test], pipe.predict(x[test]), zero_division=0))
    # Exploratory training-set clusters, never evaluated as verified labels.
    transformed = preprocess().fit_transform(x[train])
    clusters = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(transformed)
    result['exploratory_cluster_sizes'] = {str(k): int(v) for k,v in Counter(clusters).items()}
    result['n_train'], result['n_test'] = int(train.sum()), int(test.sum())
    result['scope'] = 'synthetic chronological demonstration; no universal performance claim'
    return result


def run(module):
    if module == 1:
        return {'prompt': 'Summarize using only the request. Return category, summary, needs_review.',
                'fixture_example': fixture_summary('I was charged twice for a latte.'),
                'next': 'Collect genuine model outputs before evaluating prompting quality.'}
    if module == 2:
        return fixture_summary('My login does not work. Contact SYN-7@example.invalid')
    if module == 3:
        raw = load_csv('tickets-dirty.csv')
        good, bad, duplicate = clean_tickets(raw)
        con = sqlite3.connect(':memory:')
        con.execute('CREATE TABLE tickets (category TEXT, amount REAL)')
        con.executemany('INSERT INTO tickets VALUES (?,?)', [(r['category'], r['amount']) for r in good])
        sql = dict(con.execute('SELECT category, COUNT(*) FROM tickets GROUP BY category'))
        con.close()
        return {'raw': len(raw), 'accepted': len(good), 'rejected': len(bad),
                'duplicates': len(duplicate), 'sql_counts': sql,
                'python_counts': dict(Counter(r['category'] for r in good)),
                'median_amount': statistics.median(r['amount'] for r in good)}
    if module == 4:
        return ml_demo()
    if module == 5:
        rows = load_csv('tickets.csv')
        heldout = rows[int(len(rows)*.8):]
        return {'scope': 'fixed keyword baseline on held-out synthetic tickets; no ML tuning',
                **binary_metrics([int(r['escalate']) for r in heldout],
                                 [int('urgent' in r['description'].lower()) for r in heldout])}
    if module == 6:
        return {'scrubbed': scrub('Email SYN-person@example.invalid about the request.'),
                'manifest': verify_manifest(), 'limits': 'email patterns only; no anonymity guarantee'}
    if module == 7:
        return fixture_summary('Please summarize the payment issue without inventing facts.')
    if module == 8:
        return {'backend': 'lexical baseline', 'public': retrieve('refund manager policy', 'public'),
                'manager': retrieve('refund manager policy', 'manager')}
    if module == 9:
        return security_report()
    if module == 10:
        events = load_csv('events.csv')
        return {'events': len(events), 'review_only_findings': correlate(events)}
    if module == 11:
        return {'risk_example': {'id': 'SYN-R01', 'risk': 'Cross-role policy disclosure',
                'owner': 'Application owner', 'control': 'Filter candidates before context',
                'evidence': 'tests/test_core.py', 'residual': 'Model and indexing changes need retesting',
                'trigger': 'Role or ingestion change'},
                'task': 'Create ten application-specific risks; do not copy this as a full assessment.'}
    if module == 12:
        return {'core': 'python -m unittest discover -s ai-academy/tests -v',
                'build': 'python ai-academy/tools/build_course.py --check',
                'api': 'optional FastAPI scaffold; fixture backend; localhost only',
                'cloud': 'not executed by this demonstration', 'scope': 'pilot release'}
    raise ValueError('Module must be between one and twelve')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('module', type=int)
    print(json.dumps(run(parser.parse_args().module), indent=2))
