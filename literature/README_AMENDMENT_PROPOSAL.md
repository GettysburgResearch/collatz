# Proposed README amendment — not yet applied

## Why a README change is warranted

The repository now routinely imports external theorems, uses the same theorem names for distinct hypotheses, and receives live counterexamples in PR review. The existing README has excellent native-claim discipline but no stable protocol for:

- inspection level of external sources;
- separating the source theorem from the native reduction;
- identifying analogy versus application;
- assigning imported theorem IDs;
- reacting when a reviewer supplies an explicit counterexample to a live claim.

Without a short stable rule, every branch can repeat the same Cobham/SML/Mahler/Fourier ambiguity, and a false theorem may remain described as “closed” after review.

## Suggested text

```markdown
## External results and live-claim correction

1. Imported external results use stable IDs `LIT-KTHM-####` and live under
   `literature/imported-theorems/`.
2. Every external citation records what was actually inspected: full text,
   abstract/metadata, or secondary exposition.
3. Every application separates:
   - the exact external theorem;
   - the repository-side reduction establishing its hypotheses;
   - the native conclusion;
   - non-applications and scope limits.
4. A thematic analogy is not a theorem dependency.
5. A literature match does not promote a native claim's proof status.
6. “No exact antecedent found” may be recorded only as
   `POSSIBLY NOVEL FORMULATION`, never as proof of novelty.
7. Until claim ledgers are integrated, external maps must use branch-qualified
   native IDs.
8. When a concrete counterexample to a stated claim is supplied in review, the
   author must mark the claim `REFUTED`, narrow/replace it, or give a complete
   rebuttal before the PR describes that path as closed.
9. Any downstream claim depending on a refuted statement must receive an
   explicit dependency audit.
```

## Separate live index

Do **not** put the changing program dashboard in README. Create a top-level `RESEARCH_INDEX.md`, maintained by an integrator, with:

- active issue/PR and branch;
- agent owner;
- native namespace;
- one-sentence target;
- strongest admitted result;
- central unresolved interface;
- known overlaps/conflicts;
- last update.

The README should remain stable governance; the index may change daily.