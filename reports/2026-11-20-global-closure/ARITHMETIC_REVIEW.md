# Independent review of the legal-block arithmetic lane

**Verdict: VERIFIED WITH A SOFTWARE SAFEGUARD FIX, at the exact pins below.**
The reviewer reconstructed GA-001--GA-005 and found no mathematical gap
in their stated finite-block and potential-obstruction conclusions. The
production checker initially permitted optimized Python to remove its
assertion gates. The author added an explicit rejection; normal replay
still reproduces the unchanged report. The corrected entry point was
tested to exit with status 1 under `-O`.

This is an independent agent reconstruction, not external peer review or
proof-assistant verification. No verdict here establishes a fixed ordinary
all-time source, convergence after a displayed block, or full Collatz.

## Exact reviewed content

| File | SHA-256 |
|---|---|
| `research/global-closure-20261120/arithmetic.md` | `ed2b9c627fe7b9000934ac6c0231f55f0cbafca1cbc6283b0d48b5758dc7860c` |
| `experiments/global_closure_arithmetic.py` | `5c928688397bd8b4f1d3b9b357e1646ec27cc8973c43a54abc3c714f84040269` |
| `reports/2026-11-20-global-closure/arithmetic-report.json` | `8d27838b5023b399736350d7659ba49cf62273f97e4261feaee5c779fe79336a` |

The pre-fix checker hash was
`2d0bd90ffe587c6740f3c0810fbbbddd3ed8d75d2fc21c282e7a86ee95011b77`.
The manuscript and production report did not change for this fix.

## Mathematical reconstruction

### GA-001: exact increasing-block clock and recharge account

For odd `n`, `B(n)=v2(n+1)-1` is nonnegative. Writing
`n=2^(b+1)u-1`, with `u` odd, gives the displayed formula
`U^j(n)=3^j 2^(b+1-j)u-1`. The first `b` sources are `3 mod4`,
so each has odd valuation exactly one. The last is `1 mod4`, so its
next valuation is at least two. Thus the lifetime is exact, including
the zero-clock endpoint.

At valuation one the clock drops by one; at valuation at least two the
source clock is zero and the next clock is its recharge. Summing these
actual one-step identities proves the finite accounting formula. No
estimate of the cumulative recharge sum is supplied or inferred.

### GA-002: even-residue count and restricted source set

The number of length-`L` binary strings ending in zero with exactly `r`
one-runs is `binom(L,2r)`, including leading zeros and the all-zero word.
The exponential binomial upper bound is valid because, for `k<=L/4`,
`3^(L/4-k)>=1`. Multiplication by the positive odd `3^i Q` permutes odd
residues, and subtraction by one maps them bijectively to even residues.

The admissible sources are only the odd residues of **bitlength exactly
L**, whose count is `2^(L-2)`. Bounding a bad subset by the bad count in
the entire residue space explains the factor `4` in the printed excluded
fraction. The proof does not presume equidistribution within that upper
half or independence across the `m` conditions. The strict margin for
`L=16m` and `L=16m^2` follows from `(27/16)^4>4` and `4^m>=4m`.
The exhaustive source search is therefore finite.

### GA-003: local legality, binary density, and uniform prime height

The construction uses `m=N+1`, so its `m` displayed states have exactly
the requested `N` valuation-one edges. The extra power of two is retained.
The separated trailing block of ones has a zero above it because
`3^i v-1` is even. This proves the run-count addition; taking a binary
suffix cannot increase the number of runs beyond that of the whole upper
block. The initial bitlength `17m` and bound `18m-1` for every state
follow directly from the chosen bitlength of `v`.

For the prime-height argument I reconstructed the exact affine identity

`2^d n_j = 3^d n_i + (3^d-2^d)`.

If a state has the largest `p`-valuation in a consecutive block, every
other state's full `p`-power divides its gcd with that state, hence divides
the corresponding **complete** `3^d-2^d` correction. Its binary prime
height is therefore less than `d log2(3)`. The maximum sum of distances
from one location in a block of `t` states is `t(t-1)/2`; with
`log2(3)<2` and `t<=r`, the printed `M+rt` bound is valid.

Partitioning into blocks of size `r=ceil(sqrt(m))` yields equation (16).
The inequalities `M/h<=9/8`, `h>=16m`, `1/r<=1/sqrt(m)`, and
`r<=sqrt(m)+1` give exactly `19/16` in equation (17). Both normalizations
are bounded by `Y/(mh)`. The proof is uniform over every **single shared**
set of at most `s` primes, including a set selected after observing the
whole segment. It does not permit selecting a different set at each
state.

Strict geometric growth gives the translated-interval bound for real
widths, including the singleton case of width zero. It is a statement
about this finite set of ordinary orbit states, not its predecessor basin.

### GA-004: pairwise coprimality and exclusion of small primes

Every potential common prime divisor of two constructed states divides
one of the correction factors in `Q_m`, whereas each state is `-1 mod Q_m`.
This proves pairwise coprimality. The odd-number product in `Q_m` includes
every odd prime at most `2m-1`, and all states are odd, proving the small-
prime exclusion without factoring them.

The height bound uses
`Q_m<2^(m(m-1))(2m)^m<=2^(2m^2-m)`, valid for `m>=2`.
The same separated binary suffix proves the run bound. Each prime can
divide at most one displayed state, so at most `s` states have positive
height from a shared `s`-prime set. The growth per edge is less than a
factor of two, and `x0>=16m^2+m-2`; hence
`M/x0<1+1/(16m)`. These give all three uniform prime-set conclusions.
No factorization or claim about the unobserved future is required.

### GA-005: a fixed cost can create an arbitrarily large clock

The equations `3z+1=8x`, `x` odd, and the valuations of `z+1` and `x+1`
prove the exact valuation-three reset and recharge `m-1`. The ordinary
height ratio is strictly between 1 and 4. With `u=1`, both endpoints
have exactly two one-runs and their popcounts differ by exactly one.

Thus the `mu` term in the proposed potential cancels, the `nu` term is
constant, and the logarithmic term has magnitude less than `2|kappa|`.
Every fixed positive coefficient on `B` is defeated for sufficiently
large `m`. This refutes only the specified additive class and individual-
reset charging rules. It does not refute nonlinear potentials or a
multi-step bound on accumulated recharges.

## Separate computation and actual execution scope

The review checker
[`arithmetic-independent-check.py`](arithmetic-independent-check.py)
does **not import the production module**. It uses string-based run
counting, literal repeated halving, and a different deterministic candidate
sequence for new ordinary sources. Its exact result is saved in
[`arithmetic-independent-report.json`](arithmetic-independent-report.json).

| Independent check | Executed scope |
|---|---:|
| Complete even-string count | Lengths 1--16; 65,535 words |
| Exact bad-set union margins | 63 values, `m=2,...,64` |
| Clock account on arbitrary odd starts | 2,048 starts, 32 edges each; 65,536 prefix checks |
| Newly constructed legal blocks | 14 blocks; `m=2,3,4,7,11,17,25` in both regimes |
| Literal block edges | 124 |
| Full distinct-state gcd/affine comparisons | 1,044 |
| Selected-prime maximum-valuation block checks | 240, using 12 specified primes |
| Recharge families | 268, with `u=1,3,5,11` |
| Literal recharge edges | 13,952 |
| Largest independently constructed state | 10,617 bits |

The selected-prime checks do not exhaust all prime sets. The uniform
prime-set conclusion is supported by the separately reconstructed written
gcd argument. Likewise, finite construction does not substitute for the
entropy proof guaranteeing a source for every requested finite length.

Hashes of these review artifacts:

- Independent checker:
  `88dddc07178f8ccabb53b211d8b1f61950953da035a36b03de47391a75a1bbdd`.
- Independent report:
  `4d40719a60f0e995c27aee8dfc449ccaab9528ba6e9d5d27adba649dd053abf3`.

Commands actually executed after the production safeguard fix:

```bash
python -X utf8 -B experiments/global_closure_arithmetic.py --compare reports/2026-11-20-global-closure/arithmetic-report.json
python -O -X utf8 -B experiments/global_closure_arithmetic.py --compare reports/2026-11-20-global-closure/arithmetic-report.json
python -X utf8 -B reports/2026-11-20-global-closure/arithmetic-independent-check.py --output reports/2026-11-20-global-closure/arithmetic-independent-report.json
python -O -X utf8 -B reports/2026-11-20-global-closure/arithmetic-independent-check.py --compare reports/2026-11-20-global-closure/arithmetic-independent-report.json
```

The first command passed exact regeneration. The second exited 1 with
`verification requires assertions; optimized Python is not supported`,
as intended. Both independent-checker executions passed; its verification
gates are explicit exceptions and remain active under optimized Python.

## Final scope boundary

GA-003/004 construct arbitrarily long exact ordinary segments, with a
different source for each requested length. Their local constraints
coexist, but no fixed ordinary source is proved to support all such blocks.
GA-005 defeats a specific simple way to pay for resets, while a useful
global accumulated-recharge estimate remains open. No complete cycle
denominator exclusion is claimed. The manuscript preserves these limits.
