# Sources, status, and independent-review handoff

Author: `astra-tail-transport-04`. Date: 2026-09-09 (Asia/Jerusalem).
All ATT-301--306 results are PROPOSED pending independent mathematical review.
Q-ATT-301 is OPEN. No complete Collatz proof is submitted by this packet.

## Exact sources

Research parent and intended publication branch:

```text
PR105: 912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe
Tree:  16da7fca7ad5f91e3d9d25f7ba6d5e42b2e59cdc
Branch: agent/astra-tail-transport-01/critical-tails
```

The parent file `research/astra-tail-transport/expanding-word-rank/PROOF.md`
has Git blob `857e8aff7b6e56c96c1119e7f4813d6aa2765a67`.

- ATT-201 supplies the precise rho dictionary and original computability bound;
  the required finite cutoff is rederived here.
- ATT-202 supplies the earlier word-count constant and loose rank spectrum.
  The word-count argument is reproduced. The new progression-modulus/small-source
  count improves the spectrum, not the definition of the rank.
- ATT-204 supplies the unique all-word minimizer under h>=13 and 2^h>2176u.
  This is an explicit source-qualified dependency of the LARGE rho equalities
  in ATT-305, and is still proposed. The inverse diagrams and ordinary-value
  decreases have independent elementary proofs here.
- ATT-205/206 supply the earlier activation/forward-delay obstructions. They
  remain true within their original orders and quantifiers. A smaller ordinary
  witness need not have a smaller rho, so the new reverse construction does not
  refute them or erase the old unresolved boundary.

Main first observed in this session:
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Its AGENTS.md was fetched and followed.
This research remains a child of the frozen PR105 head, not a rebase onto main.
A final readback records subsequent movement rather than incorporating it
silently. Reviewer D's review files, old A/B assignments, all source proofs,
canonical statuses, settings and workflows are untouched.

## Attribution and novelty boundary

Finite parity-cylinder bijectivity, affine composition, well-ordering of the
positive integers, positive summation and ordinary inverse Collatz formulas
are elementary background, not claimed discoveries. The 111010 arithmetic
phase was already in the PR92 source and in the parent; its existence is not new.
The contributions claimed here are the uniform LOW-RANK reverse implication,
its exact positive-orbit representation and batch algorithm, the sharper complete
infinite-dictionary spectrum, and the exact scope of the resulting normalizer.
No comprehensive external novelty survey is claimed.

External searches confirmed the reported September 8 Navier--Stokes announcement
and inspected an abstract of Applegate--Lagarias, The 3x+1 Semigroup,
arXiv:math/0411140. Neither is a mathematical premise. In particular abstract
semigroup products are not treated as physical Collatz paths. No external paper,
Lean formalization or binary certificate is redistributed or claimed replayed.

## Attempted full-proof argument and the precise failure

The valid chain is: low word component -> positive smaller ancestor -> strict
ordinary-value normalization -> one explicit residual class. The attempted
next step was that forward motion followed by normalization must give genuine
progress after a bounded amount of forward lookahead. ATT-306 refutes that
step with ordinary finite CRT families for every prescribed horizon.

A zero signed-clock normalization loop is not a positive Collatz cycle. No
argument here proves that helpful noncanceling progress eventually occurs for
every residual. The complete finite normalizer may return RESIDUAL, and its
residual contains every 3 mod12 source. A finite core patch cannot make that
particular rule universal. A new successful selector or another all-source
argument is still required.

## Computation and publication

The canonical finite report has semantic SHA-256
`a6f7d63e6c6f54f0d0078d02768ebc56226880f436f3365bbaef0e738d7cf75f`.
Two differently structured implementations reconstruct the complete payload.
Normal and optimized verifier modes reject twelve resealed corruptions.
Same-author implementation independence is not independent mathematical review.

The direct command `git ls-remote https://github.com/GettysburgResearch/collatz.git HEAD`
failed with `Could not resolve host: github.com` at the 2026-09-09T00:01:28Z
local environment check. No authenticated complete checkout was available for
`tools/validate.py`. Standalone checks and fresh-directory replay are not a
repository-wide validator run. API publication and exact blob readback are
separate integrity evidence, recorded in the delivery receipt.

## Review priorities

1. Low-rank forcing e>=q; positivity of the smaller integer; cylinder legality.
2. Completeness of the positive-ancestor representation and the batch clock bound.
3. Both terms in the AP count, treatment of long-word rounding, all constants,
   and the exact half-power summability endpoint.
4. Positive interchange and source-height tail estimates for the full dictionary.
5. Distinguish ordinary-value descent, rho descent, and unabsorbed physical clocks.
6. Exact odd-family congruences and the separately sourced global-rank equalities.
7. Residual classification, all-depth symbolic shortcut for multiples of three,
   clock-zero echoes, and the lack of a total successful residual selector.
