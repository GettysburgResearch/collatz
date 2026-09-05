# Second three-route pass — all three remain active

Agent: `astra-three-routes-02` (GPT-6 Pro), 2026-09-05, Asia/Jerusalem.
Frozen parent: PR #92 at `879343c33a7dca29128891cf6e10d9c7be1ba482`.

**PARTIAL RESEARCH. All new theorem-level statements are PROPOSED pending
independent mathematical review. No proof of Collatz, SC*, the nontrivial-cycle
exclusion, or an all-time survivor-bias estimate is claimed.** The pass extends
the existing PR #92; it does not narrow the portfolio or replace it by PR #91.

## Three substantive advances

| Route | What this pass supplies | What is still missing |
|---|---|---|
| [1. Orbitwise Mellin control](ORBIT_MELLIN.md) | A self-contained explicit equal-depth-injective bound 4X^(39/40), improved to O(X^(19/20)) with forward invariance; reciprocal budget 160m^(-1/40); bounded affine correction; a cofinal-time weakening of the original all-source bias target | Transfer from one orbit to its many-to-one inverse basin; a proved cofinal survivor-bias estimate |
| [2. Actual supercritical tails and complete echoes](SC_TAIL_AND_ECHO.md) | Every infinite orbit has an actual SC-infinite tail; SC* is equivalent to eventual periodicity; quantitative proximity to an orbit minimum; exact continuation interval/CRT compiler; an explicit rational countermodel to omitting integrality | SC* and ordinary nontrivial-cycle exclusion; universal arithmetic rejection of the remaining tuples |
| [3. Nonlinear rank profiles](NONLINEAR_PROFILE_RANKS.md) | Separate all-class proofs excluding arbitrary finite-valued univariate valuation profiles, not merely linear coefficients, for both fixed shortcut blocks and the adaptive whole-run macro | A genuinely interacting, vector/tree, infinite-feature, or differently grouped total rank mechanism |

The orbit-sparsity and qualitative reciprocal-summability ideas have prior art.
They are credited explicitly, not repackaged as a novel solution. The useful
project gain is the quantitative, locally proved interface and the sharper
SC*/cycle crosswalk. See [sources and review boundaries](SOURCES_AND_REVIEW.md).

## The new end-to-end interfaces

For an infinite positive orbit, the correction product is finite. Thus its
coefficient C_k=3^(q_k)/2^k tends to infinity, and a global minimum of C_k yields
one actual source with every future coefficient prefix at least one. Hence

    SC* <=> every positive orbit is eventually periodic;
    SC* + no nontrivial positive integer cycle => Collatz.

Neither premise of the second implication is proved. Unlike a universal FC*
exclusion, it does not demand that every first coefficient crossing descend.
This local proposed bridge does not change any canonical roadmap status.

For the original all-source H=64 mass target, Q_k/M_k<=69/200 at unboundedly
many times is sufficient. The orbitwise budget does not establish those times.
There is no hidden substitution of a sparse orbit for its much larger basin.

## Exact finite evidence

The separately structured implementations agree on:

    1,023 complete valuation cylinders; 3,069 ordinary lifted replays;
    64 exact negative-binomial bounds; six integer inequalities;
    257 source prefixes, 10,416 exact correction-product positions;
    convergence of every source in [1,64]; maximum time 71 at 54 and 55;
    12,449 first-crossing words through length 21;
    9,779 formal positive-displacement pairs;
    9,381 rejected by at most 2j further steps, versus 6,431 by the old echo;
    398 remaining formal pairs; zero positive-displacement integer sources;
    35,666 continuation constraints, including 4,238 with negative coefficient;
    one rational no-descent countermodel, preperiod 13 and period 30;
    36 exact nonlinear rank violations (nine profiles, four block modes);
    six resealed corrupt certificates rejected.

The finite words and ranks are regression evidence, not universal proofs.
Both implementations were authored in this session: implementation independence
is **not independent mathematical review**. Earlier X-ASTRA3-001 artifacts and
proofs are unchanged, and the earlier large inverse cone was not replayed here.

From the repository root:

```bash
python -B experiments/X-ASTRA3-002-three-routes/run.py \
  --check experiments/X-ASTRA3-002-three-routes/results/canonical.json
python -B experiments/X-ASTRA3-002-three-routes/verify.py \
  experiments/X-ASTRA3-002-three-routes/results/canonical.json --self-test
```

Semantic SHA-256:

    541017f8a517ee731791224129150e68543bd06c434de48e5ffa07e447aa2b68

## Review priorities

First reconstruct the two-lane cylinder/injective-endpoint count and the
uniformity of its constants. Then check that the correction product gives
actual coefficient-tail extraction, not merely arbitrarily long finite tails.
Check every sign in the continuation inequality and keep the same ordinary
displacement modulo the whole denominator. Finally audit the nonlinear profile
transport, fixed precision shifts, and the distinct proof for adaptive blocks.

All three routes remain active. The next offensive connection is to combine
quantitative orbit/source constraints with actual basin transport, while the
rank route must use a mechanism outside separate scalar valuation profiles.
