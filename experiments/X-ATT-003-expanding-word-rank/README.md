# X-ATT-003: expanding-word rank and the failed activation step

**Finite exact checks; proposed research, not a Collatz proof.**
The universal arguments are in
[PROOF.md](../../research/astra-tail-transport/expanding-word-rank/PROOF.md).
Parent: `73572fddd9b8b3cbd8fc03c3a992eb0735d0f62c`.

## Replay

From a checkout containing these additions:

```bash
python -B experiments/X-ATT-003-expanding-word-rank/run.py \
  --check experiments/X-ATT-003-expanding-word-rank/results/canonical.json
python -B experiments/X-ATT-003-expanding-word-rank/verify.py \
  experiments/X-ATT-003-expanding-word-rank/results/canonical.json --self-test
python -O -B experiments/X-ATT-003-expanding-word-rank/verify.py \
  experiments/X-ATT-003-expanding-word-rank/results/canonical.json --self-test
```

Only generator `--write` intentionally writes a report; `--check` and the
verifier do not. All predicates use explicit exceptions and remain active
under optimization. Standard library only; no external solver or source code
import is needed. The protocol is deterministic and bounded.

Semantic SHA-256:

    4b4ff957e4c782695a07f3127c52c5d12646f9077c3000748ff683da94886d9a

## Exact coverage

| Object | Count | Meaning |
|---|---:|---|
| Source census n=2..4096 | 4,095 | Exact full rho, every tied minimizer and legal-word tests. |
| Successful local certificates | 1,639 | Strict common-rank physical diagrams, not universal coverage. |
| UNRESOLVED sources | 2,456 | This narrow selector fails; not nonconvergence claims. |
| Binary words through length 16 | 131,070 | All words checked; admissible coefficients compared. |
| High-precision phase sources | 24 | K=1..8 with three valuation choices per K. |
| Physical phase positions | 672 | Exact phase identity, rank-theorem premises and shortcut replay. |
| Old quarter-unsafe module sources | 216 | Literal old A guard in the verifier. |
| Exhaustive phase rank positions | 60 | The K=1,2 subset minimizes over the entire proved finite dictionary. |
| Fixed-forward-clock source controls | 36 | K=1..12 and three depths; different sources for different K. |
| Forward-shadow positions | 234 | Physical replay and exact theorem-premise lower bounds. |
| Resealed corruptions rejected | 12 | Each changes payload semantics before recomputing the digest. |

The maximum full word length needed by the initial source census was 12.
The all-word layer census runs separately through 16. Large family positions
are NOT described as exhaustive rank enumeration: except for the labeled 60,
the proof supplies the universal comparison and code tests its exact premises.
No finite data establish infinitely many sources without the written formulas.

## Implementation separation

`run.py` constructs word coefficients by affine composition, prunes candidate
lengths dynamically, uses the old four-entry R_* formula and a closed-form A,
and constructs shadow congruences with modular inversion.

`verify.py` enumerates physical source residues, obtains each affine remainder
from actual source/endpoint iteration, and reconstructs seeded words by binary
lifting. It enumerates the full initial length cutoff without dynamic pruning,
computes R_* with a terminating scan of its unbounded index, iterates A
literally until the active mode changes, and finds shadow multipliers by a
separate bounded congruence search. It checks the negative primitive cycle
with rational arithmetic. It imports neither the generator nor any repository
module. The complete expected payload must match, not just an embedded hash.

Both programs were written by the same author. This is implementation
independence, not an independent mathematical review of ATT-201--206.

The 12 mutations cover status/rank scope, missing census coverage, changed
counts, examples, constants, phase sizes, exhaustive-scope labels, and removed
open obligations. Resealing does not make a changed report pass.

## Limits

The full-proof step fails: a minimizing word need not be physically legal.
The unbounded exit family and arbitrary finite forward-delay families are
retained. The count of successful local certificates cannot be extrapolated.
No full checkout validator, earlier heavy experiment, external formal build,
canonical promotion, workflow, or repository setting is part of this protocol.
