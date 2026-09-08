# Critical rank tails under actual Collatz transport

**PROPOSED pending independent mathematical review. No complete Collatz proof.**

This research attempt follows the Reviewer D audit but is not part of that
review and assigns no new canonical status. It uses the moving rank R_* from
PR92, not the different P-rank from PR90/91. The starting question is whether
an analytic proof can tolerate the unsafe spikes that destroy first moments.

## Main results of this attempt

Write w(n)=1/R_*(n)^2, kill at 1, and let F_k(Y) be the actual total w-mass of
sources whose k-th shortcut endpoint has rank greater than Y.

| Claim | Proposed result | Boundary |
|---|---|---|
| ATT-001 | For every ordinary cutoff N>=2, `1/(9N^2) <= sum_(n>N) w(n) <=43/N^2`. | Source-height tail, not just a rank-sublevel estimate; the exponent is sharp. |
| ATT-002 | For every fixed k>=1, `F_k(Y)=Theta_k(1/Y)`. All moments of order 0<s<1 are finite, while the first moment is infinite. Moreover `sup_Y YF_k(Y)=Theta((9/4)^k)` with explicit constants for k>=6. | The input first rank moment is finite. The tail norm's growth is not an individual divergent orbit or a failure of uniform tightness. |
| ATT-003 | The total maximal repeated-word module obeys `A(n)+5 <=(n+5)^(9/4)` for every n>1. | All active modes and repetition counts; improves the previous coarse cubic bound but is not descent. |
| ATT-004 | One actual quarter-unsafe return H sends `f<=C/R_*^2` to a distribution with tail `<=200 C Y^(-4/9)`. Its s-th rank moment is finite for s<4/9; in particular the 1/3-moment is <=602 C. | Covers every source and every intervening safe excursion. The output envelope needed for iteration has NOT been proved. |
| ATT-005 | For the same full-support unsafe input, `sup_Y Y sum_(R_*>Y) Hf = infinity`. A completely explicit infinite family also refutes `R_*(A(n)) <= C R_*(n)^2` for every fixed C. | This is stronger than merely infinite first moment; it does not refute the fractional output estimate. |
| ATT-006 | Uniform tail defect equals the input mass of divergent basins; limiting finite-ball Cesaro occupation equals the input mass of nontrivial-cycle basins. | Both vanishing conditions together are equivalent to Collatz. Neither vanishing theorem is established here. |

Read [PROOF.md](PROOF.md) for complete arguments and the exact failed
completion. Read [sources and claim boundaries](SOURCES_AND_STATUS.md) before
comparing with earlier programs. The [experiment](../../experiments/X-ATT-001-critical-tails/README.md)
contains two separately implemented finite checks and a canonical report.

## The explicit clock-change family

For every even j>=2, set

```
t=2^j, M=3^t, n=4M-5, a=j+4,
m=(M-1)/2^(j+2), y=(3^a m-1)/2.
```

The actual module and induced unsafe return both send n to y. Both endpoints
are unsafe, and

```
R_*(n)=16M,
R_*(y)=(y+5)^2/9,
R_*(y)/R_*(n)^2 > (9/4)^a/1152.
```

The ordinary inputs are explicit integers, not merely CRT-compatible prefixes.
Their continuation is not assumed convergent or divergent. At j=2 the path is

```
319 -> 479 -> 719 -> 1079 -> 1619 -> 2429 -> 3644 -> 1822.
```

At fixed clocks these witnesses prove sharp growth of the weak rank moment.
At the unbounded input-dependent clock they disprove a critical output tail
bound. Both facts can hold even if every input eventually converges.

## What this adds, and what it does not

The input rank, total acceleration, rank-fiber enumeration, safe induced map,
and earlier first-moment explosion are credited to PR92. The additions are the
source-height tail, exact fixed-clock moment threshold and sharp clock rate,
the improved uniform module ceiling, a positive fractional output-domain
estimate, and the explicit weak-critical failure family. The general
escape/occupation decomposition is elementary and carries no priority claim.

The proof attempt stops at re-entry: one output estimate does not regenerate
its own input hypotheses. A cycle obstruction also remains independently
necessary. Neither the existence of many partial rank reductions nor the
finite mass enclosures solves those problems.

## Reproduction

From a repository checkout:

```bash
python -B experiments/X-ATT-001-critical-tails/run.py --check experiments/X-ATT-001-critical-tails/results/canonical.json
python -B experiments/X-ATT-001-critical-tails/verify.py experiments/X-ATT-001-critical-tails/results/canonical.json --self-test
python -O -B experiments/X-ATT-001-critical-tails/verify.py experiments/X-ATT-001-critical-tails/results/canonical.json --self-test
```

Both implementations were authored in this research session. Their agreement
is implementation independence, not an independent mathematical review.
The [publication handoff](../../reports/astra-tail-transport-01/2026-09-07-attempt.md)
records the actual tool and execution boundary.
