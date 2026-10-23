"""Offline structure, local-link, notebook and content-hygiene checks."""
import ast
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set(); self.h1=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1': self.h1+=1
        if 'id' in a:self.ids.add(a['id'])
        for attr in ['href','src']:
            if attr in a:self.links.append(a[attr])


def main():
    course=json.loads((ROOT/'source/course.json').read_text(encoding='utf-8'))
    assert [m['id'] for m in course['modules']]==list(range(1,13))
    for m in course['modules']:
        assert len(m['weeks'])==4
        for field in ['objectives','alignment','project','acceptance','security','resources']:
            assert m[field],(m['id'],field)
        for w in m['weeks']:
            assert len(w['concept'].split())>=35,(m['id'],w['week'],'insufficient concept explanation')
            assert len(w['practice'].split())>=20,(m['id'],w['week'],'missing independent practice')
    pages=list(ROOT.rglob('*.html'))+[ROOT.parent/'index.html']; errors=[]
    for path in pages:
        parser=Links();parser.feed(path.read_text(encoding='utf-8'))
        if parser.h1!=1:errors.append(f'{path}: expected one primary heading')
        for link in parser.links:
            parts=urlsplit(link)
            if parts.scheme or parts.netloc:continue
            dest=(path.parent/unquote(parts.path)).resolve() if parts.path else path
            if dest.is_dir():dest/= 'index.html'
            if not dest.exists():errors.append(f'{path.name} -> {link}')
            elif parts.fragment and dest.suffix=='.html':
                target=Links();target.feed(dest.read_text(encoding='utf-8'))
                if parts.fragment not in target.ids:errors.append(f'Missing anchor {link} in {path}')
    notebooks=list(ROOT.glob('modules/*/lab.ipynb'))
    assert len(notebooks)==12
    for path in notebooks:
        nb=json.loads(path.read_text(encoding='utf-8'));assert nb['nbformat']==4
        for cell in nb['cells']:
            if cell['cell_type']=='code':
                assert cell['outputs']==[] and cell['execution_count'] is None
                ast.parse(''.join(cell['source']),filename=str(path))
    for path in ROOT.rglob('*.py'):
        ast.parse(path.read_text(encoding='utf-8'),filename=str(path))
    # Real-world identifiers are prohibited. Synthetic reserved-domain emails are allowed.
    for path in ROOT.rglob('*'):
        if path.is_file() and path.suffix in ['.md','.json','.csv','.html','.py']:
            text=path.read_text(encoding='utf-8')
            if re.search(r'\bgh[pousr]_[A-Za-z0-9]{20,}\b|\bsk-[A-Za-z0-9]{24,}\b',text):
                errors.append(f'Possible credential in {path}')
    if errors:raise SystemExit('\n'.join(errors))
    print(f'PASS: 12 modules, 48 lessons, {len(pages)} HTML pages, 12 notebooks, local links and syntax. External URLs not network-tested.')


if __name__=='__main__':main()
