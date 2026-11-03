# Scenario and decision rules

## Business and roles

BrewByte operates two fictional coffee shops. Checkout depends on register devices. Online ordering depends on ORDER-01 and DB-01. GW-01 supports vendor administration. BKP-01 stores backups. Guest Wi-Fi should provide Internet access without access to checkout administration.

| Role | Responsibility |
|---|---|
| Business Owner | Owns business priorities, funding, and acceptance of material residual risk |
| IT Lead | Owns network, gateway, backups, and approved technical changes |
| Application Owner | Owns ordering and database services |
| Store Systems Owner | Owns register devices and secure retirement evidence |
| Vendor Coordinator | Owns vendor and partner access reviews |
| Store Operations Lead | Owns staff onboarding, offboarding, and store continuity procedures |

These are role labels, not real people. The Business Owner has the scenario's authority to accept material remaining risk. Technicians provide evidence and options.

## Classroom operating requirements

These are invented policy requirements for this exercise, not external mandates.

- Vendor administration requires a named account, MFA, explicit approval, and an enforced end time.
- Guest Wi-Fi must not reach checkout management interfaces.
- Departed staff access must be disabled when employment ends, and completion must be verified.
- The delivery partner should see only assigned delivery details needed for the service. Bulk access to customer profiles is outside the approved purpose.
- Audit logging must follow the approved baseline.
- Retirement requires evidence of custody, data handling, and credential/access removal.
- The online ordering service has an RTO of 60 minutes and an RPO of 60 minutes.
- High-priority confirmed findings require a response plan within one business day. A due date is a target for this fictional exercise, not proof the target is appropriate for every organization.
- Production changes require recorded approval, pre-change testing, a rollback plan, and post-change verification. Emergency work uses an authorized emergency route with documentation and follow-up.

## How to reason about the data

Inventory records declare what the organization knows. Missing evidence creates uncertainty. A retired status alone does not prove data erasure. A successful backup does not prove successful restoration. A vendor advisory indicates possible exposure, not that an incident occurred.

Use the asset ID to join records. Compare configuration using the pair (asset_id, setting). Current-only configuration entries for new devices are new observations, not changes to an existing baseline entry.

The change log is complete for recorded approvals during the comparison period. A difference with no matching approval requires investigation. CHG-105 is conditional: enabling support does not authorize disabling MFA or omitting an expiry.

Treat the domains as cooperating functions. External information and internal facts inform risk assessment. Assessment identifies weaknesses and remediation addresses them. Rehearsal and review test whether people and processes are ready.
