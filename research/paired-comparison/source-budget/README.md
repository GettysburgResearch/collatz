# Fixed-source merging: ternary splices and a common restart budget

**Exploratory research, PROPOSED. Collatz remains unresolved.** This packet
continues the fixed-original-source route from #130 and #133--136 on a new
branch from main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. It credits those
exact source interfaces without importing or promoting their branch histories.

The question is concrete: after an actual orbit reaches `H(C)=9C+2`, can a
new companion be kept below the **unchanged original source N**? A legal
comparison whose companion exceeds N cannot support least-source induction.

## Main results

| Result | What changes | Exact limit |
|---|---|---|
| [Ternary splice, TSB-001](TERNARY_SPLICE.md#tsb-001-a-two-odd-block-4z3-switch-at-the-actual-hard-exit) | At a first hard odd exit, `3^a` dividing `4N+3` gives an explicit companion `m=2^a(4N+3)/3^a-1`; `m<N` holds exactly for `a>=4`. | This is an initial-source guard: it cannot recur after an odd shortcut step, because the forward states are then units modulo three. |
| [Unbounded repaired classes, TSB-002](TERNARY_SPLICE.md#tsb-002-unbounded-first-runs-with-failed-old-root-order-repaired-by-tsb-001) | For every first odd-run length `r>=6`, CRT supplies whole classes where the old #135 companion exceeds N but the new companion is below N. The displayed original arm stays entirely above N. | The congruences describe precisely which unchanged inputs are covered; they are not forced on every input. |
| [One common restart rank, RSB-002](RESTART_BUDGET.md#rsb-002-one-common-exact-companion-height-ledger) | For a hard H return with run length s and output valuation `2k+epsilon`, the guard `3^(s+k)<=2^(s+2k+epsilon)` gives `0<=M_next-3<(3/4)(M-3)`. Arbitrary admitted switching retains `M<N`. | The normalizer ends in MERGE or FAILED_DEBT_GUARD. The guard is not proved universal. |
| [Sharp height obstruction, RSB-003/004](RESTART_BUDGET.md#rsb-003-sharp-one-restart-inflation-exponent) | One legal restart can increase the next canonical companion to order `N^(log_2 3)`. Arbitrarily long finite expanding runs can lose source order immediately. | These are different finite ordinary sources at different lengths, not an infinite ordinary counterexample. |
| [Alternative companion and all-clock control, TSB-003/004](TERNARY_SPLICE.md#tsb-003-an-independent-smaller-companion-beyond-the-new-valuation-guard) | A whole family has `6m<N` despite failure of both displayed source tests. The complete bank below 27 proves that no smaller-source merger occurs before its first ordinary descent. | A proof must permit ordinary descent and cannot infer complete coverage from these successful families. |

The contraction proof uses one ordinary integer quantity, `M-3`. It does not
combine #136's `D-2` rank with a reset companion clock. The exact affine ledger
in RSB-002 records the positive correction terms that a more general
amortized argument would still need to control.

### Small new certificate

For every integer `t>=0`,

    N=53439+82944t, m=42223+65536t, E=456536+708588t,
    T^8(N)=T^14(m)=E, 0<m<N.

The old odd-valuation companion is `76089+118098t>N`. Every positive-time
state on the eight-step original arm is above N, and `3|N`, so the new witness
also cannot be explained by a smaller pure ancestor of N.

## What would move this toward a full proof

A full fixed-source argument needs a finite smaller-source merger or an
ordinary descent for every `N>1`. This packet gives a new initial guard and a
terminating partial restart language. Its first missing theorem is coverage
at **FAILED_DEBT_GUARD** or at a failed initial source-order test, retaining
the same original N. A successful continuation must either produce a new
physical companion below N or justify a return with one compatible decreasing
quantity. The sharp inflation examples rule out restoring this merely by
allowing a fixed factor of slack in the next canonical companion.

No fixed-floor mass estimate, density result, stopping-time assumption, or
infinite ordinary realization is used. No full proof, divergent positive
orbit, or nontrivial positive cycle is asserted.

## Reproduce the evidence

From the repository root, using Python 3.11 or later:

```bash
python -S -B experiments/paired-comparison/source-budget/check_splices.py
python -S -B experiments/paired-comparison/source-budget/check_restarts.py
python -S -B experiments/paired-comparison/source-budget/verify_certificates.py experiments/paired-comparison/source-budget/certificates.json --self-test
python -S -B experiments/paired-comparison/source-budget/independent_checks.py
```

The same entry points support `-OO`; the mathematical checks are explicit
and remain active. The certificate file stores whole affine words and the
complete smaller-source bank for 27. The checker verifies all-parameter
parities and inequalities and rejects targeted corruptions. The larger
bounded input grids are regenerated, not mistaken for all-input proofs.

[Source pins and credits](SOURCES.json) identify prior claims by full SHA and
path. The publication report records separate proof reconstruction, finite
execution, and complete-checkout validation. In-session checking is not a
formal proof build or an acceptance decision for the project.
