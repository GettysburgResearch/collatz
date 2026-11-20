# Independent narrow review: prime-support peak bounds P13

**Verdict: VERIFIED at the two exact file hashes below, for P13a--P13f and
its stated finite-source/cycle scope.** No mathematical correction was needed.
This is an independent AI proof reconstruction with a separately implemented
finite check, not human peer acceptance or formal proof-assistant verification.

## Frozen objects and scope

Author files are retained in
`research/allhands-global-closure-20261120/`:

| File | SHA-256 |
|---|---|
| `PRIME_SUPPORT_PEAKS.md` | `9bafb9167ae3c939d3d2d839b6ee02bde0720c0ec7492ae46ebdf15dba834edf` |
| `check_prime_support_peaks.py` | `103c19a367e3d79afe43c80300f1ad15ac8ef199ea7a64aa5be962ac7ac9adac` |

I read both files. The parent had already reconstructed P1--P12. My review
concentrates on the new maximum-deletion strengthening, its exact return
cost, and the claims

\[
\max_j n_j\le\max\{4^s n_0,(s+1)^{64s}\},\qquad
\max n<(s+1)^{64s}\text{ on a cycle}.                       \tag{R1}
\]

The prime-power tail mechanism is credited to Paper138 by the author. I did
not perform an independent literature-priority audit or rebuild external
formalizations. The argument reviewed here is elementary and complete using
the displayed ordinary affine identity.

## 1. Exact return cost

For an actual odd-clock return from index `i` to `j`, put `d=j-i` and
`A=sum_{i<=l<j} v2(3n_l+1)`. The affine numerator obeys

\[
0<C<3^d2^{A-d},\qquad
\gcd(n_i,n_j)\mid C.
\]

The strict bound follows immediately from the section-2 identity
`C/2^A <= (3/2)^d-1`. Consequently a common divisor `q` of the endpoints
satisfies

\[
\log_2q<d\log_2 3+(A-d).
\]

Every edge's cost `log2(3)+(a_l-1)` is positive. Costs of consecutive returns
to one prime-power level therefore sum to at most the cost of the whole
original window: their interiors are disjoint, and omitted intervals have
nonnegative cost. This uses actual original gaps, not compressed time on a
selected subsequence.

## 2. Cost and deletion at a peak

The window has `2s+1` states ending at a maximum and `2s` actual transitions.
Since

\[
2^A n_{\rm end}=n_{\rm start}
       \prod_{l}(3+1/n_l)\le n_{\rm end}4^{2s},
\]

its total exponent satisfies `A<=4s`; hence
`V=2s log2(3)+(A-2s)<6s`. No bound on any individual exponent is assumed.

Delete one coordinate maximizer for each prime. Different primes can choose
the same point; at most `s` points are removed, so `m>=s+1` remain. Whenever
a positive level for a prime was occupied, its maximizer is among the deleted
points. If `r` original points lie above that level, at most `r-1` retained
points do. The original consecutive returns charge these `r-1` occurrences
against `V`, proving the boundary-free retained tail

\[
R_{p,Y}(h)\le\min(m,V/h).
\]

Deletion is solely a counting operation. This distinction is correctly kept
in the author's statement and checker.

## 3. Layer integration and numerical inversion

When `M>=max(6,2s)`, one has `Mm>=6(s+1)>6s>V`. Thus

\[
\int_0^M\min(m,V/h)\,dh
 =V(1+\ln(Mm/V)).
\]

The right side is increasing in `V` for `V<Mm`, because its derivative is
`ln(Mm/V)>0`. Replacing `V` by `6s` is legal. Also `m<=2s+1<=3s`, so the
result is at most `6s(1+ln M)` for each prime. Every retained state's height
is at least `M-2s`. Summing over the support therefore yields

\[
(s+1)(M-2s)\le6s^2(1+\ln M),
\]

and hence `M<8s+6s ln M<8s+5s log2 M`. The latter conversion uses
`6 ln2<5`.

At `B=64s log2(s+1)`, writing `L=log2(s+1)>=1` gives
`log2 B<=6+2L` and `8s+5s log2 B<=48sL<B`. For `M>=B`, the derivative
of `M-5s log2 M` is positive. This proves `M<B`; the smaller excluded
cases satisfy it directly. The inversion is universal algebra, not an
extrapolation from the numerical checks.

## 4. Finite-source and cycle domains

If the peak occurs before odd-clock index `2s`, bounded upward increments
instead give `n_max<4^s n_0`. Otherwise the last `2s+1` states are available.
This proves the first inequality in (R1). A source term is necessary: a
one-state prefix can contain an arbitrarily large prime while using only
one prime in its support.

For a cycle, unroll as many copies as needed before a maximum. The affine
numerator remains positive for returns to a repeated state, so the same
proof applies and the source alternative disappears. This verifies the
second inequality in (R1). It does not exclude every nontrivial cycle below
the finite bound.

A prime support of size at most `s` implies multiplicative rank at most `s`;
the converse is false. For example `{15,225}` has rank one but prime support
`{3,5}`. This is only an algebraic scope illustration, not a claimed Collatz
trajectory. The note correctly restricts its improvement to the prime-support
subclass and does not claim a better theorem for arbitrary rank.

## 5. Independent execution

I implemented `review_prime_support_independent.py` without importing author
code. It uses a bit operation to recover the exact odd-step exponent,
independently expands each relevant affine numerator, and deliberately deletes
the **last** prime-coordinate maximizer instead of the author's first.
Repeated visits to the actual fixed point `1` are kept in the trajectories.

Both normal and optimized executions completed with exit zero; their complete
JSON reports are byte-identical. Executed coverage:

* 70 ordinary sources and 5,600 literal odd edges;
* 1,317 peak-ending windows;
* 7,968 boundary-free prime-power tail checks;
* 1,234 independent affine return expansions and costs;
* 359 finite-source boundary checks;
* eight exact inversion checks at `s=2^r-1`, `1<=r<=8`, where
  `B=64sr` is an integer;
* a rational series enclosure of `ln2` proving the numerical conversion
  constants and derivative sign without floating-point logarithms.

The exact negative control `3 -> 5` has total return cost `3`, whereas its
single occurrence of the prime power `5` exceeds that cost. Thus omitting the
maximum deletion would give a false boundary-free tail, even on a literal
ordinary peak window. No hypothetical nontrivial cycle was used.

Independent checker SHA-256:
`504b6135872f30f1b94df629a4658f9f502d27646724c6c5dadfa65c237d5a84`.

The identical execution output is retained once as
`prime-support-independent-report.json`. The packet execution receipt
records the comparison with the optimized run.

The author checker was inspected, not rerun by me; the independent executions
above are a different and narrower coverage record. They do not validate the
author's reported counts by substitution. No repository-wide validation or
external Lean build is claimed by this review.

## Remaining limitation

The result bounds height under a bound on the actual prime support. It does
not supply an upper bound on the support created by an escaping orbit, nor
a lower-energy contradiction, nor control of prime divisors of shifted values
`n_j+1`. Its connection to a full Collatz proof remains open exactly where the
author states it. The review verdict does not extend to later file revisions.
