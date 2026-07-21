# Literature layer

This directory separates five kinds of durable knowledge that should not be conflated:

1. **source metadata** — what was actually located and inspected;
2. **claim mappings** — what a source proves relative to a branch-qualified repository claim;
3. **atomic imports** — self-contained theorem statements and proofs or explicitly labeled black-box uses;
4. **topic notes** — useful neighboring theories, including non-applications;
5. **unverified items** — missing references, missing theorem hypotheses, and searches that did not confirm an attribution.

## Verdict vocabulary

| Verdict | Meaning |
|---|---|
| `KNOWN — EXACT` | The located result is essentially the same theorem after a transparent notation change. |
| `KNOWN — COROLLARY` | The repository claim follows by a short derivation, supplied or precisely described. |
| `PARTIAL OVERLAP` | A located result supplies a component but not the complete repository claim. |
| `FOLKLORE / STANDARD` | The result is standard and a proof or source is supplied. |
| `POSSIBLY NOVEL FORMULATION` | No exact antecedent was found after a documented search. This is not a novelty claim. |
| `UNVERIFIED` | A bibliographic item, theorem attribution, or reduction could not be confirmed. |
| `MISAPPLIED / HYPOTHESES FAIL` | The cited theorem does not imply the repository statement under the presently written hypotheses. |

## Import-note standard

Each file in `imported-theorems/` records:

- a stable local `KTHM-####` identifier;
- an exact statement and definitions;
- proof status;
- a complete proof when short, otherwise a black-box theorem with source location;
- branch-qualified mappings;
- dependency and gap audits;
- explicit non-applications.

`KTHM` identifiers are literature-layer identifiers only. They do not compete with repository `T-####` or `L-####` IDs.

## Citation rule

A BibTeX key appears only if the corresponding item was located through an official publisher, stable institutional record, DOI landing page, or primary preprint. Inspection level is recorded in `SOURCE_LEDGER.md`. An abstract-level inspection never supports a detailed proof attribution.

## Branch qualification

The suite intentionally uses `PR3/...`, `CLAUDE/...`, and `TERM/...`. An integrator may later replace these with canonical IDs, but provenance must remain recoverable.

## Validation

Run:

```bash
python3 scripts/check_literature.py
```

The checker verifies local Markdown links, citation-key resolution, import-ID uniqueness, branch qualification in claim maps, and the absence of citation placeholders.
