# Literature suite protocol

This directory is a reusable theorem-and-source layer, not a second native claim ledger.

## Identity and provenance

Native claim IDs must be branch-qualified until integration:

- `PR3/...` — draft PR #3, branch `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`;
- `CLAUDE/...` — issue-#4 symbolic-rewrite branch;
- `TERM/...` — draft PR #6 termination-frontier packet.

Imported results use `LIT-KTHM-####`. They record known mathematics and may be dependencies of native claims, but they do not receive `PROVED` or `INDEPENDENTLY_VERIFIED` statuses from the repository claim ladder.

## Required fields for an imported theorem

Every file under `imported-theorems/` contains:

- exact source and inspection level;
- self-contained definitions and quantified statement;
- proof status (`RECONSTRUCTED`, `BLACK BOX`, or `PROOF SKETCH`);
- complete proof when short enough;
- branch-qualified native mappings;
- hypotheses and non-applications;
- remaining verification notes.

## Citation discipline

A source may enter `SOURCE_LEDGER.md` only after at least one of the following was inspected:

- `FULL TEXT` — article/report text was opened;
- `OFFICIAL ABSTRACT/HTML` — publisher or institutional page was opened;
- `METADATA` — stable bibliographic metadata was opened;
- `SECONDARY CONFIRMATION` — used only when clearly labeled and never as sole support for a load-bearing theorem.

A plausible citation not actually located belongs in `UNVERIFIED.md`, not in `references.bib`.

## Verdict discipline

“No exact antecedent found” is recorded as **POSSIBLY NOVEL FORMULATION**, never as proof of novelty. A thematic resemblance is not a theorem application. A source theorem and the repository reduction to it are audited separately.

## Mechanical validation

Run:

```bash
python3 literature/check_literature.py
```

The checker verifies citation keys, local Markdown links, imported-theorem IDs, absence of stale Deep Research citation artifacts, and use of the conservative novelty vocabulary.
