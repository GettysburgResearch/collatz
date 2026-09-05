# Fifth all-route attack: unsafe moment loss, compulsory rank excursions, and switch repayment

Agent: `astra-three-routes-05` (GPT-6 Pro). Date: 2026-09-05.
Frozen parent: `6266bd8f73ce2f8488c02fbe29f34fd2b4f289bc`, existing PR #92.

**All new theorem-level claims are PROPOSED pending independent mathematical
review. A full end-to-end proof was attempted along every route but was not
obtained.** The unsafe supersolution, complete merging cover, and total rank
selector remain OPEN. All earlier packets and their proof statuses are preserved.

The pass tests three actual finishing mechanisms, not just another finite-depth
trend. A rank-adapted operator extension is disproved on all-source arithmetic
families; a resource-capped two-sided proof search receives an all-diagram lower
bound and a matching-scale successful family; and a computable unbounded switch
rule proves repayment for a genuinely unsafe growing prefix. All use the same
moving-envelope integer rank R from the parent.

## Read the three full attempts

| Route | New proved partial result / exact obstruction | Missing finishing theorem |
|---|---|---|
| [1. Rank moments and unsafe transport](RANK_MOMENTS.md) | Sharp square-root rank counting; summable rank weights; distribution-free safe resolvent; one unsafe step destroys a finite rank moment; every summable monomial height/rank supersolution fails | An actual unsafe-return weight or aggregate estimate, not a safe-region bound |
| [2. All-diagram rank barriers](MERGING_BARRIERS.md) | Every lower-rank merger from an odd multiple of3 must pass one compulsory high-rank state; infinite CRT families attain that cost scale and repay | Complete physical merging cover with genuinely adequate unbounded resources |
| [3. Unsafe switching repayment](UNSAFE_REPAYMENT.md) | A total guarded rule for arbitrarily many alternating modes3 and1, all unsafe, followed by exact quarter-rank repayment | Proved coverage/totality for all remaining inputs, not just the successful guard |

## New shared quantitative facts

For R=R_* of the parent and X>=1,

    floor(sqrt(X))-1 <= #{n>=2:R(n)<=X} <9sqrt(X),
    sum R(n)^(-s)<infinity iff s>1/2,
    sum 1/R(n)<=55/6.

Thus rank balls can be enumerated completely without scanning all integers up
to their largest possible source. The exact rank<=2^24 ball has10,195 members
and maximum source14,348,908. No orbit-convergence claim is inferred from this
rank census.

For arbitrary nonnegative input mass with finite R^p moment, the safe kernel
has norm at most4^(-p). However the induced unsafe operator sends the explicit
finite-moment input1_U/R^2 to infinite first rank moment. This uses ordinary
sources 3^e, e=4 mod16, and does NOT say their individual orbits diverge.

For an odd n with H=v3(n)>=1, every lower-rank merging diagram has peak rank at
least((3n-1)/2)^2. On n=3^H that is quadratic in starting rank. On the supplied
CRT repayment family the optimal peak lies between((3n-1)/2)^2 and
((3n+1)/2)^2, an interval of width3n. A fixed relative-rank search cap is therefore
not a complete end-to-end strategy.

For every K>=1 and L>=K+4, infinitely many ordinary n>=11 realize

    (111010)^K 0^L,
    n=10 mod243,
    v2(17n+73)=6K,

with an odd final endpoint. Every one of the first2K A-sources is unsafe, the
rank after those cycles exceeds(81/64)^(2K)R(n), and the final same rank is
less than R(n)/4. K is computed from n, not supplied by an oracle. This is
unbounded mode-switch repayment, not repeated alignment in a single mode.

## Evidence, not extrapolation

The new standard-library generator and independently written verifier cover:

    6 complete rank balls, with direct interval comparison through rank 2^16;
    1,311 arbitrarily weighted safe sources and9 moment-transport rows;
    8 infinite-family moment-spike samples;
    45 rank-barrier/repayment CRT samples,855 positions,405 reverse-ray checks;
    96 unsafe-switch samples,1,728 A-modules,1,632 unsafe source positions;
    5 actual unsafe power-weight failures;
    10 resealed corrupt reports rejected.

The all-parameter conclusions are the written proofs, not the samples. Both
programs were written by the same author: implementation independence is not
independent mathematical review. The verifier passes with Python -O because
checks raise explicit exceptions rather than removable assertions.

From the repository root:

```bash
python -B experiments/X-ASTRA3-005-rank-budget/run.py \
  --check experiments/X-ASTRA3-005-rank-budget/results/canonical.json
python -B experiments/X-ASTRA3-005-rank-budget/verify.py \
  experiments/X-ASTRA3-005-rank-budget/results/canonical.json --self-test
```

Semantic SHA-256:

    1dc5510f205dd8b4a106a636af68ef8a7252a867fc1e4c10310d93e54567fb5d

## End-to-end boundaries

A positive summable strict unsafe inverse supersolution would prove Collatz;
the tested whole power-weight class cannot supply it. A lower-rank merging
diagram for every possible exceptional component minimum would prove Collatz;
a universal diagram/rank-resource bound is not supplied. A total contracting
selector would prove Collatz; the new guarded selector returns UNRESOLVED
outside its certified family. These are three precise places where the attempted
full proofs stop. None is hidden in the finite certificates.

The older SC/cycle split, fixed-floor signed-boundary target, finite-record
clock, and other rank constructions remain active and unchanged. See
[SOURCES_AND_REVIEW.md](SOURCES_AND_REVIEW.md) for exact provenance and adversarial
review points. No broad external novelty claim is made.
