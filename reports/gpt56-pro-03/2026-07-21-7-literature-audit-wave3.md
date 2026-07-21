# Agent report — literature audit wave 3

```text
Agent: gpt56-pro-03
Issue: #7
Branch: agent/gpt56-pro-03/4-literature-audit
Date: 2026-07-21
```

## Starting hypothesis

The repository had acquired enough new mathematics that the literature layer needed another live pass. The main question was no longer only novelty matching: several branches appeared to converge on a precise ordinary-versus-completion obstruction, and existing literature might either collapse parts of the work to known theory or sharpen the remaining target.

## Repository snapshot reviewed

- PR #3: connector/Hensel counter-stack sessions through the exact 256-transition stage and information-surplus theorem;
- PR #16: fixed survivor measures, reciprocal phase chain, completion-height carry rigidity, and proposed all-depth weighted EQ;
- PR #19: exact H cylinders, carries, ghosts, survivor counting, and bounded-representative formulation;
- PR #20: repetition rigidity, chart criticality, demand-tree isometry, active finite cylinders, and ghost stages;
- issue #21 / Foundry branch: strictly causal parity-digit closure equations;
- issue #4 branch: latest density-one EQ and symbolic-amplifier ledger;
- PR #3's critical-particle and ordinary-spine formulations.

## New results and connections

### 1. Foundry contraction crosswalk

Bernstein--Lagarias's isometric parity conjugacy turns the Foundry equation into a strict contraction fixed-point problem. Strict causality gives a `1/2`-Lipschitz map, so Banach's theorem supplies existence and uniqueness immediately. The self-contained flip proof remains useful; the native research content begins at ordinary integrality and operator classification.

Added:

- `LIT-KTHM-0028`;
- `LIT-KTHM-0029`;
- `causal-foundry-and-padic-automata.md`.

### 2. Explicit logarithm hidden in PR #3

The quadratic moving bulk

```text
u_m=(3^(-7*2^m)-1)/2^(m+2)
```

is the divided exponential for

```text
u_infinity=-(7/4)log_2(3).
```

The exact approximation is `v_2(u_m-u_infinity)=m+1`. Mahler's p-adic Hermite--Lindemann theorem makes the nonzero limit transcendental. This gives the counter-stack program an explicit target constant and standard log algorithms, while preserving the central distinction between generating new digits forward and preloading the completed ghost.

Added:

- `LIT-KTHM-0030`;
- `padic-logarithm-stage-bulk.md`.

### 3. H ghosts as a separated countable IFS

The recursive exact-cylinder map defines pairwise disjoint `2`-adic branches with contraction exponents `3r+2`. The residue count obeys

```text
N(K)=N(K-2)+N(K-3),
```

so its growth is controlled by the plastic constant `rho`, and the ghost-set dimension is

```text
log_2(rho)=0.405685...
```

This yields the proposed sharper ordinary-survivor bound

```text
O(X^(log_2 rho)),
```

subject to independent verification of the branch orientation. It would supersede the current stretched-exponential upper bound in the H packet.

Added:

- `LIT-KTHM-0031`.

### 4. PR #16 as deterministic nonarchimedean Erdős--Kahane

The all-depth EQ proof uses the classical methodological chain “large Fourier coefficient implies many near-integral phases,” but replaces generic parameter transversality by exact integral carries and an ordinary height contradiction. Existing real self-similar Fourier theorems remain non-applicable as black boxes.

A reading-level audit found the chain coherent. No status is promoted. The review order is:

```text
L-9309 -> T-9307 -> T-9308
L-9310 -> T-9311
then T-9312.
```

Highest-risk interfaces:

- zero-carry modulus and terminal indexing;
- mirror/survivor sign and digit order;
- complete lift-digit bijection;
- exact removal of powers of `64`.

Added:

- `erdos-kahane-carry-rigidity.md`;
- wave-3 claim map and live review.

### 5. PR #20 and p-adic stammering methods

The repetition theorem is a specialized product-formula argument: an eventually periodic approximant has small global height but agrees to very high `2`-adic precision. Ridout and Adamczewski--Bugeaud supply the natural next literature for fractional powers and symmetric patterns, but no source is directly applicable without a native rational-base reduction.

Added:

- `completion-height-principle.md`.

### 6. PR #3's critical particle as a size-biased spine

The mass-conserving particle tree and Doob endpoint law are an exact deterministic spine construction. Lyons--Pemantle--Peres and Hardy--Harris supply many-to-one, martingale, entropy, and spine-change tools. They do not solve marked ordinary closure.

Added:

- `LIT-KTHM-0032`;
- `collatz-spine-many-to-one.md`.

## Cross-program conclusion

Foundry, PR #3, PR #19, and PR #20 all now have the exact form

```text
infinite directive
 -> one unique point in Z_2
 -> ordinary integer iff least representatives or new blocks eventually stabilize.
```

PR #16 and PR #20 independently produce the same criticality constant

```text
1/(log_64(81)-1)=17.654847...
```

through different completion-height arguments. This is meaningful cross-validation of structure, not proof verification.

The common next theorem should be an adaptive completion-height result for finite control plus one unbounded counter/stack. Existing results handle fixed or repeated approximants; the final directive changes with the same state that generates its height.

## Mathematical-quality assessment

The strongest work is research-grade in conception and proof organization:

- exact quantified claims rather than motivational prose;
- explicit dependency and gap audits;
- self-correction when counterexamples appear;
- independent branches converging on the same constants and completion boundary;
- reductions that materially narrow the full problem.

The project is not yet at publication-grade validation as a whole:

- most central theorems are author-proposed and unreviewed;
- notation and claim spaces remain fragmented;
- several chains are long enough that one indexing or sign error could invalidate downstream conclusions;
- no branch crosses the ordinary-integer stabilization barrier.

The best current claims have credible publication potential after independent reconstruction. The work has genuine relevance to the full problem because it isolates a necessary and sufficient final obstruction and supplies multiple attacks on it. It does not yet provide evidence that the obstruction is close to being crossed.

## Files added

- `literature/LIVE_REPO_REVIEW_WAVE3.md`
- `literature/SOURCE_LEDGER_WAVE3.md`
- `literature/references-wave3.bib`
- `literature/check_literature_wave3.py`
- `literature/claim-maps/WAVE3.md`
- `literature/imported-theorems/LIT-KTHM-0028-*` through `0032-*`
- five wave-3 topic notes
- this report

## Validation status

The wave-3 checker was added to validate IDs, required files, bibliography-key uniqueness, stale citation artifacts, and load-bearing theorem markers. The GitHub connector does not execute repository code; a reviewer or CI should run:

```bash
python3 literature/check_literature.py
python3 literature/check_literature_wave2.py
python3 literature/check_literature_wave3.py
```

## Recommended next actions

1. Independently reconstruct PR #16's all-depth EQ chain before further extension.
2. Add the logarithm identification to PR #3 and redesign its bulk generator around explicit log digits.
3. Independently prove the H IFS recurrence and replace the weaker count if it passes.
4. Extend PR #20's exact-repeat theorem to fractional powers or symmetric patterns.
5. Classify small finite-state Foundry operators through van der Put coefficients.
6. Create one cross-program completion-height packet after repository consolidation.

## Candidate counterexamples

None proposed or promoted.

## Potential errors / unresolved doubts

- The H-IFS branch orientation and finite-prefix-to-infinite-map crosswalk require independent checking before use.
- The exact valuation of the PR #3 logarithmic approximation should be independently recomputed.
- The PR #16 chain has not received a full independent proof reconstruction.
- Mahler's transcendence theorem identifies the completed logarithm but says nothing about digit-generation complexity.
- No literature result found supplies ordinary integrality of any selected completion point.
