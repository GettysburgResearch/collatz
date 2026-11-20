# A local prime-support barrier at ordinary height peaks

**Status: PROPOSED.** The elementary statements below have complete written
proofs and a bounded exact-integer replay. They do not resolve Collatz.

The useful new synthesis is a maximum-height bound, obtained by placing the
known prime-power return budget in a short backward window of an actual
height peak. The number of primes in a support is denoted by `s`; this is
not interchangeable with the multiplicative rank of the states.

## 1. Map and source comparison

Use the accelerated map on positive odd integers

\[
U(n)=(3n+1)/2^{v_2(3n+1)},\qquad n_{j+1}=U(n_j),
\quad x_j=\log_2 n_j.
\]

Every upward increment of `x` is at most one. Repeated states are allowed
in the finite statements; a cyclic segment is literally unrolled before
applying them. All primes and valuations belong to actual ordinary
integer states.

Frozen repository inputs:

* PR154, `fe40bb6f88e8094290ef01207d9bf7c4798d35d0`,
  `research/structural-reset-20261120/adelic/PRIME_HEIGHT_ESCAPE.md`,
  ADEL-001--007: ordinary gcd control, prime-height dispersion and an
  elementary bounded-prime-support cycle consequence.
* PR153, `eb04a5d79020cefa0ba46794095b5766c5ff66a4`,
  `research/fixed-integer-descent/arithmetic.md`, RC-1--5: finite cores for
  bounded binary one-run count. A run-cap exit is not descent.
* PR156, `c5cb84502c7289705d59a8781a65fd845b9b6b14`,
  `research/global-rigidity-20261120/SHIFTED_LINEARIZATION.md`: its
  algebraicity and power-saving requirements remain open.

Related primary manuscripts, inspected 2026-11-20:

* [Paper137](https://rstation.ai/problems/collatz/papers/137), v1,
  Theorem 2: the stronger parameter of multiplicative rank gives an
  elementary maximum-height bound with logarithm `O(r^2)`.
* [Paper138](https://rstation.ai/problems/collatz/papers/138), v1,
  Sections 2--3 and Theorem 7: consecutive prime-power returns, deletion
  of coordinate maxima, valuation tails, entropy, and relative cofactor
  dispersion. The tail mechanism in Section 2 below is **credited prior
  work**, rederived here with a convenient coarse constant.
* [Paper159](https://rstation.ai/problems/collatz/papers/159), v1,
  Lemmas 5--6: source-uniform rank/energy bounds obtained by first paying
  costly returns. Those results do not provide an incompatible energy
  lower bound for a hypothetical exceptional orbit.

The result below concerns a prime pool of size `s`, a more restrictive
condition than rank at most `s`. In that subclass it replaces the
elementary `exp(O(s^2))` maximum-height scale by `exp(O(s log(s+1)))`.
No exhaustive novelty assertion, new unit-equation finiteness principle,
or improvement to the cited general-rank theorem is claimed.

## 2. A convenient ordinary return budget

For `i<j`, put `d=j-i`, let `a_l=v2(3n_l+1)`, and write the actual
affine identity

\[
2^A n_j=3^d n_i+C,\qquad
C=\sum_{t=0}^{d-1}3^{d-1-t}2^{A_t}>0.
\]

Every remaining valuation is at least one, so

\[
C/2^A\le (3/2)^d-1<(3/2)^d.
\]

Also `2^A n_j/n_i=prod(3+1/n_l)<=4^d`. Since the gcd of the
endpoints divides `C`,

\[
\boxed{\gcd(n_i,n_j)n_j<6^d n_i.}                 \tag{P1}
\]

Thus

\[
\log_2\gcd(n_i,n_j)<x_i-x_j+3d.                 \tag{P2}
\]

This deliberately rounds `log2(6)` up to 3. For a common divisor `q`
at selected positions `i_0<...<i_r`, multiplying (P1) gives the exact
integer certificate

\[
\boxed{q^r n_{i_r}<6^{i_r-i_0}n_{i_0}.}          \tag{P3}
\]

There is no bound on individual division exponents, no discarded
intermediate state, and no claim that the selected positions form a new
trajectory.

For one prime `p`, let `y_j=v_p(n_j) log2(p)` in a block of `N` states
starting at index zero. Define

\[
R_p(h)=\#\{0\le j<N:y_j>h\},\qquad
K=x_0+3(N-1).
\]

Consecutive positions in this set have gcd logarithm greater than `h`.
Summing (P2), and using `x_i<=x_0+i` and `x_j>=0`, proves

\[
R_p(h)\le\min\{N,1+K/h\}\qquad(h>0).            \tag{P4}
\]

The additive one is essential: a prime power that occurs only once has
no return to charge. This is the familiar boundary term in the cited
prime-power method, not a new return theorem.

## 3. The peak-window inequality

Suppose `n_k` is a maximum of a finite prefix and put

\[
M=\log_2 n_k\ge8,\qquad N=\lceil M/2\rceil.
\]

Assume there are at least `N-1` preceding transitions, and consider the
last `N` states ending at this occurrence of the maximum. Let `S` be the
union of their prime divisors and `s=|S|`. The set is chosen after seeing
the whole window, but is shared by all its states.

Every state in this window has logarithmic height at most `M`. Bounded
upward increments also give

\[
x_j\ge M-(N-1)>M/2.                              \tag{P5}
\]

Consequently its accumulated height `W` satisfies

\[
W>NM/2\ge M^2/4.                                \tag{P6}
\]

The initial height of this window is at most `M`, so its return budget
has `K<M+3M/2=(5/2)M`. For any prime `p`, layer integration and (P4)
give

\[
\begin{aligned}
\sum_{j<N}y_j
 &=\int_0^M R_p(h)\,dh\\
 &\le 8N+\int_8^M(1+K/h)\,dh\\
 &\le 7M+\tfrac52M\ln M.                         \tag{P7}
\end{aligned}
\]

At `M=8` the integral is zero. For the last line, use
`N<=M/2+1<=3M/4`, and discard favorable terms. All quantities are
nonnegative and the support of each `y_j` lies in `[0,M]`.

Since the entire factorization of every window state uses `S`, summing
(P7) over its `s` primes and comparing with (P6) gives

\[
\boxed{M<28s+10s\ln M
       <28s+7s\log_2 M.}                         \tag{P8}
\]

In particular, every such peak window has the explicit support lower
bound

\[
\boxed{s>\frac{M}{28+7\log_2 M}.}               \tag{P9}
\]

This is a local statement at the actual peak, uniform in the source,
the actual primes, and all division exponents. The window has only
`ceil(M/2)` states.

### An explicit height bound

For `s>=1` put `L=log2(s+1)>=1` and `B=128sL`. At `M=B`,

\[
\log_2 B=7+\log_2s+\log_2 L\le7+2L,
\]

and hence

\[
28s+7s\log_2B\le s(77+14L)\le91sL<B.
\]

The function `M-7s log2 M` is increasing for `M>=B`, because its
derivative is `1-7s/(M ln2)>0`. Thus (P8) is impossible for `M>=B`.
We conclude

\[
\boxed{M<128s\log_2(s+1),\qquad
       n_k<(s+1)^{128s}.}                         \tag{P10}
\]

The coarse case `M<8` satisfies the same upper bound automatically.
The constants are explicit and intentionally conservative.

## 4. A finite-source barrier and an unconditional cycle corollary

**P11.** Suppose every state of a finite positive odd prefix uses primes
from one set of cardinality at most `s>=1`. Then

\[
\boxed{\max_j n_j\le
\max\{n_0^2,(s+1)^{128s}\}.}                     \tag{P11}
\]

**Proof.** Take an occurrence of its maximum, with logarithmic height
`M`. If `M<8`, use the explicit constant. Otherwise use the preceding
peak argument whenever `k>=ceil(M/2)-1`. If that many predecessors do
not exist, `k<ceil(M/2)-1<M/2`, so bounded upward increments give
`M<=x_0+k<x_0+M/2`, or `M<2x_0`. This is the other alternative. QED.

The same proof allows a *different* prime pool at different peaks: if
`M>max(8,2 log2 n0)`, the actual last `ceil(M/2)` states ending at a
record must collectively contain more than the number in (P9).
No global fixed prime pool is required for this local statement.

**P12.** Every positive odd cycle whose complete prime support has
cardinality at most `s>=1` satisfies

\[
\boxed{\max n<(s+1)^{128s}.}                     \tag{P12}
\]

**Proof.** Unroll enough copies of the actual cycle before an occurrence
of its maximum to supply the required `ceil(M/2)-1` predecessors. The
same gcd identities hold across repeated states; their positive affine
numerator remains positive. The peak argument applies without a source
alternative. The cycle `{1}` is immediate. QED.

This makes every fixed prime-support class effectively finite without
specifying which primes constitute it: every state is below the displayed
integer cutoff. It does not prove that the finite class contains no
nontrivial cycle. The source's general-rank maximum-height theorem and
its sharper cycle-period/ minimum restrictions retain their own scope.

### P13: remove the large-source square by deleting boundary maxima

The exact total return cost improves the finite-source alternative. The
following argument explicitly uses the maximum-deletion mechanism of
Paper138, Section 2.

Take `2s` steps ending at a maximum, so the window has `2s+1` states.
All its logarithmic heights are at least `M-2s`. If `A` is its actual
total division exponent, telescoping at a maximum gives `A<=4s`.
Therefore its total logarithmic return cost, in base two, is

\[
V=2s\log_2 3+(A-2s)<6s.                          \tag{P13a}
\]

For each prime in the support, delete one window point where its
valuation is maximal. At most `s` points are deleted, leaving a set `Y`
of `m>=s+1` actual window points. At every positive prime-height level,
at least one original occurrence has been deleted. The consecutive
original return intervals have disjoint interiors and their costs sum
to at most `V`. Hence on `Y` the boundary-free tail is

\[
\#\{j\in Y:v_p(n_j)\log_2p>h\}\le\min(m,V/h).
                                                               \tag{P13b}
\]

This is a counting deletion only. The points of `Y` are not declared a
new trajectory, and all omitted divisions remain in `V`.

Assume `M>=max(6,2s)`; the other cases satisfy the final bound directly.
Since `m>=s+1`, we have `Mm>6s>V`. Integration gives

\[
\sum_{j\in Y}v_p(n_j)\log_2p
 \le V\{1+\ln(Mm/V)\}
 \le6s\{1+\ln M\}.                              \tag{P13c}
\]

For the last inequality, the function `v(1+ln(Mm/v))` is increasing for
`0<v<Mm`, so replace `V` by `6s`; also `m<=2s+1<=3s`, hence
`Mm/(6s)<=M/2<M`. Summing over at most `s` primes yields

\[
(s+1)(M-2s)\le6s^2(1+\ln M),
\quad M<8s+6s\ln M<8s+5s\log_2M.               \tag{P13d}
\]

Put `B=64s log2(s+1)` and `L=log2(s+1)>=1`. Then
`log2 B<=6+2L`, and

\[
8s+5s\log_2B\le s(38+10L)\le48sL<B.
\]

The same monotonicity argument as before excludes `M>=B`. A finite
prefix whose maximum occurs before step `2s` instead has
`n_max<4^s n_0`. Cyclic unrolling supplies all the predecessors for a
cycle. Thus the sharpened conclusions are

\[
\boxed{\max_j n_j\le
\max\{4^s n_0,(s+1)^{64s}\}}
\quad\text{for a finite S-supported prefix},                  \tag{P13e}
\]

\[
\boxed{\max n<(s+1)^{64s}}
\quad\text{for an S-supported cycle}.                         \tag{P13f}
\]

The finite-source inequalities (P11) and (P13e) are both available;
neither is substituted for the source-independent local assertion
(P9). The leading asymptotic scale is the point of the construction,
not optimization of its explicit constants.

## 5. The attempted global bridge

The peak theorem strengthens a complexity requirement on one actual
ordinary orbit. A hypothetical escape must repeatedly form windows
whose prime support grows at least on the scale

\[
\frac{\log n_{\rm peak}}{\log\log n_{\rm peak}}.
\]

This does not conflict with the size or factorization budget of a window
of `O(log n_peak)` ordinary states. Bounded growth of each state permits
that many new prime factors. A deterministic orbit being generated from
one finite input does not bound the primes that may appear, nor their
Kolmogorov information; no entropy-independence assumption is made here.

Three further closing attempts do not supply that missing upper bound:

1. **Binary runs.** The PR153 core theorem forces high run count but
   supplies no upper bound on prime support. A cap exit can increase the
   value. These two growth requirements are compatible.
2. **Multiplicative energy.** Paper159 bounds energy above. Distinct
   Collatz states supply no opposing large-energy lower bound. The
   tautological diagonal lower bound is of order `N^2` and is compatible
   with its subcubic upper estimate.
3. **The shifted smooth part.** PR156 uses factors of `n_j+1`, whereas
   (P1)--(P12) concern factors of `n_j`. A valuation-one step transports
   `n_j+1` by multiplication by `3/2`, so the positive unshifted gcd
   correction is absent there. Applying (P4) to `n_j+1` would be an
   unsupported substitution. The needed algebraicity of its real limit
   and all-future power saving remain open.

The first unsupported implication toward full Collatz is therefore an
upper bound preventing the local prime-support creation in (P9), or a
different ordinary descent mechanism that uses that creation. No such
upper bound or descent is proved here. Cycles with unbounded support
remain a separate unresolved class.

## 6. Finite evidence

`check_prime_support_peaks.py` replays literal positive odd trajectories,
factors the declared finite states, and verifies (P1), (P3), discrete
prime-height threshold charges, and integer versions of the peak-window
floor and support bound. It also checks the final finite-source bound.
It uses exact integers and rational comparisons, not floating-point
logarithms. The checker rejects negative/zero/even sources and a
deliberately corrupted edge. The proof is the argument above; these
finite checks do not certify arbitrary sources or nontrivial cycles.

The completed normal and `-OO` executions produced byte-identical JSON
payloads. Coverage was 1,045 sources, 26,301 literal odd edges, 306,559
short affine-return checks, 26,005 prime-power return checks, 19,778
discrete prime-height threshold checks, 1,864 peak windows, 2,284
source-boundary alternatives, 10,917 exact peak-cost windows, and 85,170
boundary-free valuation-tail checks. Seven negative controls passed.
The largest source was 531,441 and the largest encountered state had
29 bits. The actual root fixed point was the only cycle fixture.

Run without altering the preserved report:

```bash
python -B check_prime_support_peaks.py --output /tmp/prime-support-normal.json
python -OO -B check_prime_support_peaks.py --output /tmp/prime-support-optimized.json
```
