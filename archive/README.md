# Backstage archive

This area indexes provenance and integration evidence that must remain durable but should not be the public front door.

The archive contains or points to:

- immutable dated integration snapshots;
- exact-SHA review coverage and frozen PR-head inventories;
- lifecycle and recommended-action ledgers;
- machine-readable registries and alias tables;
- previous handoffs, owner decisions, and proof-import plans;
- historical process documents whose language reflects the repository state at the time.

These records are essential for auditors and integrators. They are not the best place for a newcomer to learn the mathematics.

## Current front-stage documents

- [`../README.md`](../README.md)
- [`../START_HERE.md`](../START_HERE.md)
- [`../CURRENT_KNOWLEDGE.md`](../CURRENT_KNOWLEDGE.md)
- [`../FRONTIERS.md`](../FRONTIERS.md)
- [`../AGENTS.md`](../AGENTS.md)

## Integration archive

See [`integration/README.md`](integration/README.md).

## Machine metadata

The machine registry remains at [`../claims/registry/`](../claims/registry/) with its index at [`../claims/registry.json`](../claims/registry.json). It is retained in place to preserve stable paths and exact historical links. Human-readable mathematics lives under [`../research/integrated/`](../research/integrated/README.md).

## Historical-language rule

A dated snapshot may say that a PR was open, draft, or unmerged because that was true at its observation time. Such text is historical evidence, not current status. Current status is stated only in the root front-stage documents and the active registry.

Do not rewrite a frozen snapshot to make later activity appear reviewed or accepted earlier. Add a new dated record or update the current front-stage synthesis instead.
