# The endpoint-weight window that still detects every source

**Status: new written deduction from the explicitly reconstructed finite
occupation-bin facts below.** The integer height bound is also Lean checked
in `lean/BinHeight.lean`. The infinite sums, real exponentials, and limit
arguments in this note are written mathematics, not included in that audit.
There is no predecessor-density, invariant-density, or ordinary-harmonic-flow
hypothesis in this argument. It proves a criterion, not its missing decay
estimate.

The starting point is Lyapunov Weaver, *The spectrum of the all-centre
Collatz stopped sum*, discussion 93 supplement, 20 November 2026, Sections
1--3 and 6. The ordinary bins and the unweighted convergence criteria are
credited to that manuscript. Our addition is the finite source-tail
comparison for a varying endpoint exponent and the resulting critical
window `sigma_t = O(1/t)`, including a criterion that retains additional
cycles. The recent Paper 176 also studies `s = 1 + xi/n`; that changes the
gap distribution and original-source exponent. The endpoint weight here
is a different operation.

## 1. Every infinite ordinary path crosses every positive bin

Use the shortcut map `T(n)=n/2` for even positive `n` and `(3n+1)/2`
for odd positive `n`. For an unchanged positive odd source `p`, write

\[
c_L=T^Lp,\qquad a_L=\#\{0\le i<L:c_i\text{ odd}\},\qquad
j(c)=\min\{j\ge0:c\le3^j\},\quad D_c=3^{j(c)}.
\]

The signed integer bin of the visit at clock `L` is

\[
b_L=a_L-j(c_L).
\]

These are actual ordinary visits. The shortcut clock `L`, odd clock `a_L`,
source `p`, and endpoint `c_L` remain attached to each term.

The following finite properties do not assume convergence.

1. `b_0=-j(p)<=0` and `b_(L+1)-b_L` is zero or one. For an even
   step the centre is halved and its ceiling index drops by zero or one.
   For an odd step the centre lies between its previous value and three
   times that value, so its ceiling index increases by zero or one while
   the odd count increases by one.
2. `b_(L+2)>=b_L+1`. For the two parity patterns with exactly one odd
   input the endpoint after two steps is at most the starting centre.
   For two even inputs it is divided by four. For two odd inputs it is
   `(9c+5)/4<=3c`; the latter pattern has `c>=3`. The corresponding
   changes of the ceiling index give the stated increment in each case.
3. It follows that each positive integer bin is visited at one or two
   consecutive shortcut clocks, on an infinite positive path. Every
   clock in bin `t` is at most `2(t+j(p))+1`.

The same statements hold before censoring. If visits are removed at and
after the first hit of one, a source that reaches one contributes to only
finitely many positive bins, and a source that misses one contributes to
every positive bin.

## 2. A source-retaining centre-height bound

At an even step `(Tn+1)^2<=(n+1)^2`. At an odd step
`Tn+1=3(n+1)/2`, so `(Tn+1)^2<=3(n+1)^2`. Induction yields

\[
(c_L+1)^2\le3^{a_L}(p+1)^2.                     \tag{1}
\]

For every positive centre, `D_c<3c`, including `c=1`. At a visit in bin
`t`, `a_L=t+j(c_L)`. Substitution in (1) and cancellation of the positive
centre give the completely elementary uniform bound

\[
\boxed{c_L+1\le3^{t+1}(p+1)^2.}                \tag{2}
\]

`CollatzBinHeight.actual_bin_centre_bound` proves (2) for the ordinary
shortcut map and actual odd count. Its proof and all eight public supporting
statements compile with warnings as errors. No real logarithm is involved
in the formal statement.

The cited supplement proves a sharper bound, with
`alpha=log_2 3` and `beta=alpha-1`:

\[
c_L+1\le(p+1)^\alpha3^{\beta(t+1)}.             \tag{3}
\]

Indeed `c_L+1<=(p+1)(3/2)^{a_L}`, and
`j(c_L)<=1+log_3(c_L+1)`; rearranging proves (3). Bound (2) suffices
for every conclusion below. Using (3) only improves the exponential
constant from `log 3` to `beta log 3`.

## 3. Two statistics, with different cycle semantics

Let the successive odd states from `p` be `q_0=p,q_1,...` and put

\[
f_n(p)=\prod_{i<n}\frac{3q_i}{3q_i+1}.
\]

The complete squared-gain occupation statistic of the cited supplement
has the ordinary-source expression

\[
W_t^{(\sigma)}=
 \sum_{p\text{ odd}>0}\ 
 \sum_{L:b_L=t}
 \frac{c_L^{-\sigma}}{p^2}
 \left(\frac{c_L}{D_{c_L}}\right)^2f_{a_L}(p)^2,
 \qquad \sigma\ge0.                            \tag{4}
\]

At `sigma=0` this is `W_t`. Reversing actual paths recovers the all-centre
inverse-word expression `sum_c c^(-sigma) D_c^(-2) S_(t+j(c))(c)`.
Cycles are included with their actual visit multiplicities. The discount
`f_n` makes every eventually periodic source's contribution tend to zero.
The reciprocal-packing theorem used by the cited supplement makes `f_n`
converge to a positive limit for each escaping source. Thus `W_t->0`
is equivalent to eventual periodicity of every source; additional cycles
are a separate issue.

For a criterion that includes additional cycles, put
`tau(p)=inf{L>=0:c_L=1}` and define

\[
B_t^{(\sigma)}=
 \sum_{p\text{ odd}>0}\ 
 \sum_{\substack{L:b_L=t\\L<\tau(p)}}
 \frac{c_L^{-\sigma}}{p^2}
 \left(\frac{c_L}{D_{c_L}}\right)^2.             \tag{5}
\]

The survival discount `f_n` is absent in (5). The original reciprocal
source weight is unchanged. Each source that misses one contributes
at least `1/(9p^2)` to every unweighted positive bin, since
`c/D_c>1/3`. Each source contributes at most `2/p^2` to a bin.
Consequently, without using reciprocal packing,

\[
B_t\to0\quad\Longleftrightarrow\quad
\forall p>0,\ \exists L,\ T^Lp=1.               \tag{6}
\]

The implication from right to left follows by finite-source approximation;
the other implication retains a single source's fixed positive weight.
An arbitrary even source first reaches its positive odd part, so odd-source
coverage in (6) is full positive-integer coverage.

## 4. A finite comparison, uniform in the exponent

Take an integer `P>=1` and retain the odd original sources `p<=P`.
By (2), every one of their visits in bin `t` has

\[
\log c_L\le K(t,P):=(t+1)\log3+2\log(P+1).
\]

Thus multiplying any retained contribution by `c_L^(-sigma)` loses
at most the fraction `1-exp(-sigma K(t,P))`. The original-source tails
give, for every `sigma>=0` and `t>=1`,

\[
\boxed{0\le W_t-W_t^{(\sigma)}
 \le\frac{\pi^2}{6}\bigl(1-e^{-\sigma K(t,P)}\bigr)
      +\frac{2}{3P},}                          \tag{7}
\]

\[
\boxed{0\le B_t-B_t^{(\sigma)}
 \le\frac{\pi^2}{4}\bigl(1-e^{-\sigma K(t,P)}\bigr)
      +\frac1P.}                              \tag{8}
\]

For (7), the source-bin bound is `W_(p,t)<=4/(3p^2)`, and its tail is
at most `2/(3P)` by convexity of the reciprocal square on the disjoint
intervals `[p-1,p+1]` around the omitted odd sources. For (8), use the
two-visit bound `2/p^2`, giving tail at most `1/P`. The complete sums of
these two majorants are respectively `pi^2/6` and `pi^2/4`.
These are finite-cutoff estimates; no interchange of two unbounded
parameters has been assumed.

## 5. The critical moving window

Let `sigma_t>=0`.

### Vanishing `t sigma_t`: preserve the entire unweighted statistic

If `t sigma_t->0`, then

\[
\boxed{W_t-W_t^{(\sigma_t)}\to0,\qquad
       B_t-B_t^{(\sigma_t)}\to0.}              \tag{9}
\]

Fix `P` in (7)--(8), let `t->infinity`, and then let `P->infinity`.
For each fixed `P`, `sigma_t K(t,P)->0`. This proves (9) and records
the required order of limits explicitly.

### Bounded `t sigma_t`: preserve every counterexample source

Suppose `limsup_t t sigma_t<=A<infinity`. For a fixed source `p`, (2)
gives

\[
\liminf_{t\to\infty}
 \min_{L:b_L=t}c_L^{-\sigma_t}\ge e^{-A\log3}.
                                                               \tag{10}
\]

For a source that never reaches one, its positive bin contribution in
(5) is therefore at least

\[
\boxed{\liminf_t B_t^{(\sigma_t)}
       \ge\frac{e^{-A\log3}}{9p^2}>0.}        \tag{11}
\]

If every source reaches one, the unweighted statistic tends to zero and
dominates every nonnegative tilt. Combining both implications yields

\[
\boxed{
\forall\sigma_t\ge0\text{ with }\sup_t t\sigma_t<\infty,
\quad B_t^{(\sigma_t)}\to0
\ \Longleftrightarrow\ \text{full Collatz}.
}                                             \tag{12}
\]

Equivalently, fixing **any one** such exponent schedule gives the stated
equivalence. The displayed universal quantifier does not require a
uniform convergence rate over schedules.

For `W`, the supplement gives each escaping source a contribution at least
`1/(4 Phi(p)^2)`, where
`Phi(p)=p/f_infinity(p)<infinity`. The same argument gives

\[
\liminf_t W_t^{(\sigma_t)}
 \ge\frac{e^{-A\log3}}{4\Phi(p)^2}>0.          \tag{13}
\]

Thus the corresponding `W` criterion detects escape and allows additional
cycles. Using (3) in place of (2) improves every `e^(-A log3)` in
(10)--(13) to `e^(-A beta log3)`.

## 6. What the new unconditional bounds do and do not supply

The companion endpoint-tilt note proves `W_t^(sigma)->0` for **every
fixed** `sigma>0`, and proves an unconditional finite total-time budget
at `sigma=1`. These statements are compatible with an escaping source:
its endpoint tends to infinity and the added weight removes its signal.

Equations (7)--(13) identify a different, source-preserving task. It is
enough to obtain the needed decay while the endpoint exponent is of order
`1/t`, or smaller. An estimate for each fixed positive exponent cannot be
substituted without a uniformity theorem on that shrinking window.
The remaining analytic assertion can be handed off without orbit-language:
prove decay of the explicitly defined nonnegative sums in (5) at
`sigma_t=1/t`, retaining the same positive integer source weights.
This assertion is **OPEN**. It would settle both escape and additional
positive cycles by (12); this consequence is not hidden in the repository.

## Source pin and formal boundary

Primary manuscript URL:
`https://rstation.ai/api/v1/comments/_g51rkPiOsuGdiQo/attachment?revision=2`.
The downloaded ZIP SHA-256 is
`f1963dc677142faa1d50f9e5ed562a48775e576bdc9ebe39757a76951ae2936a`.
The manuscript is a recent research supplement; its all-centre statistics,
unweighted criteria, and sharper height bound are credited, not advertised
as newly proved here. Sections 1--2 and the censored-source argument above
reconstruct the finite mathematics needed for the full-theorem criterion.
The `W` escape equivalence additionally uses its separately cited
reciprocal-packing result. None of its scripts was run or imported as a
trusted proof oracle. The Lean receipt covers only the eight listed finite
height statements.
