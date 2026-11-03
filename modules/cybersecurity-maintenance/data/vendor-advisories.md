# Fictional vendor advisories

These notices are invented for this exercise. They are not CVEs or real vendor guidance.

## BB-ADV-01: BrewGate remote support authorization weakness

- Issued: November 3, 2026, 07:30 ET.
- Product: BrewGate.
- Affected version: 2.0.
- Fictional corrected version: 2.1.
- Condition: affected remote-support interfaces can permit unauthorized administrative actions when reachable by an attacker.
- Potential consequence: configuration changes and service interruption.
- Suggested response: confirm product/version and exposure, restrict unnecessary remote support, validate approval conditions, test the corrected build, schedule authorized deployment, and verify afterward.
- Exploitation at BrewByte: unknown. A match does not prove a breach.

## BB-ADV-02: RoastLedger export error

- Issued: November 3, 2026, 07:45 ET.
- Product: RoastLedger.
- Affected version: 7.0.
- Fictional corrected version: 7.1.
- Condition: a malformed export request can interrupt the reporting service.
- Suggested response: determine whether RoastLedger exists in the environment before assigning corrective work.
- Inventory coverage: the supplied inventory is the authoritative exercise snapshot. Explain any assumptions if claiming a product is absent.
