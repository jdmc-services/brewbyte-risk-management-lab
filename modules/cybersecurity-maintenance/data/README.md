# Data guide

All records are synthetic classroom fixtures. Product versions are invented labels. Never use these advisories as real product intelligence. Dates use YYYY-MM-DD. Event timestamps include the Eastern Time UTC offset. Semicolons separate multiple IDs within a single CSV field.

| File | Records | Purpose and key |
|---|---:|---|
| [asset-inventory-baseline.csv](asset-inventory-baseline.csv) | 10 | Approved comparison snapshot on October 20. One row per asset_id. |
| [asset-inventory-current.csv](asset-inventory-current.csv) | 12 | Observed inventory on November 3 at 08:00 ET. Includes retired assets. |
| [configuration-baseline.csv](configuration-baseline.csv) | 9 | Approved settings. Key is asset_id plus setting. |
| [configuration-current.csv](configuration-current.csv) | 11 | Observed settings at the current snapshot. Same compound key. |
| [approved-changes.csv](approved-changes.csv) | 5 | Recorded approvals and implementation claims. Conditions appear in record_note. |
| [business-changes.csv](business-changes.csv) | 6 | Changes to operations, people, and relationships. |
| [access-review.csv](access-review.csv) | 6 | Account states and scope. Account IDs are fictional labels, not credentials. |
| [vulnerability-findings.csv](vulnerability-findings.csv) | 7 | Mixed confirmed, unconfirmed, and closed findings. |
| [backup-and-recovery.csv](backup-and-recovery.csv) | 5 | Backup outcomes and restore evidence; estimates are explicitly labeled. |
| [incident-timeline.csv](incident-timeline.csv) | 8 | Later tabletop events. The cause of the simulated outage is unknown. |
| [vendor-advisories.md](vendor-advisories.md) | 2 advisories | One relevant and one unrelated fictional bulletin. |

## Field definitions

**Inventory:** asset_id is the stable join key; hostname is the human-readable name; business_role explains its service; location is a fictional site; product and version support advisory matching; owner_role identifies accountability; criticality is business importance; network_zone groups intended network use; private_ip is a private illustrative address; lifecycle_state records Active or Retired. Unassigned ownership is a gap for review.

**Configuration:** setting names the control or property; value is the approved or observed state. These tables contain observations, not commands.

**Approvals:** change_id is a stable reference; approved_date records the decision; change_type selects inventory or configuration; setting_or_field and approved_value identify the approved state; implementation_state describes recorded execution; approver_role and record_note give accountability and conditions. Completed describes the recorded implementation, not a guarantee that every condition was met.

**Business changes:** event_id identifies a business event; date is its recording date; change_description explains the event; related_assets lists relevant asset IDs; responsible_role owns the business process.

**Access review:** account_type identifies staff, vendor, service, or partner use; purpose describes the intended role; employment_or_contract_state gives business context; enabled describes account state; privilege_scope describes permissions; mfa records the observed authentication control; access_expiry records the enforced end time or its absence; last_review_date and review_owner_role identify review context. A service account with not-applicable MFA is not automatically defective; evaluate workload identity, privilege, and credential management separately.

**Findings:** finding_id is the unique record; discovered_date is the discovery date; finding_description describes the observation; validation_state separates evidence from suspicion; exposure describes reachability/context; business_impact gives a consequence; existing_control is a relevant safeguard; fix_available describes an option; due_date is a fictional target; status tracks current disposition. A severity score is deliberately omitted so you must justify priority.

**Recovery:** activity distinguishes a backup job, restore test, or estimate; result labels the evidence; duration_minutes means observed restore duration or an explicitly labeled estimate; for backup jobs it means job runtime. data_age_minutes means the recovery point's age at restoration or a hypothetical estimate. Zero on a backup job only describes its snapshot and does not prove recovery within RPO at an arbitrary outage time. evidence_note limits interpretation.

**Incident timeline:** time_et orders observations; source is a role or source system; related_assets gives context; observation describes only what the exercise establishes. A hypothesis is not a confirmed cause.

## Important joins

Use asset_id across inventory, configurations, approvals, findings, and recovery records. related_assets may contain several IDs. The access-review file does not use a direct asset key: use the stated purpose and scenario to connect accounts to services.
