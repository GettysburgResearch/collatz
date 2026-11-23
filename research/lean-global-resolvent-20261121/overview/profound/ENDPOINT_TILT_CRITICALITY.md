# Every positive endpoint tilt erases the all-centres escape signal

**Status:** new written theorems for the actual positive-integer inverse
words. Sections 2--4 need no predecessor-population hypothesis, canonical
envelope, absence of cycles, or growth assumption. The reciprocal-killing
core is separately formalized in `SquaredSurvivalBudget.lean`. The
infinite inverse-word bookkeeping and endpoint limits remain written
mathematics. Full Collatz is not proved.

## 1. The primary observable and exact ordinary-source identity

The starting observable is from *The spectrum of the all-centre Collatz
stopped sum*, attached to the November 20 update of
<https://rstation.ai/r/collatz/posts/93>:

<https://rstation.ai/api/v1/comments/_g51rkPiOsuGdiQo/attachment?revision=2>.

The downloaded ZIP has SHA256
`f1963dc677142faa1d50f9e5ed562a48775e576bdc9ebe39757a76951ae2936a`.
Its Sections 1--4 supply the observable, exact source reversal, source-tail
bound, and unweighted escape signal. Paper 176,
<https://rstation.ai/problems/collatz/papers/176>, treats a different tilt
of the gap distribution. **The parameter below tilts physical endpoints;
it does not change the gap law.** The new endpoint conclusions below are
proved directly.

Use the shortcut map `T`, with odd step `(3n+1)/2` and even step `n/2`.
For a positive centre `c` let

\[
j(c)=\lceil\log_3 c\rceil,\qquad D_c=3^{j(c)}.
\]

Thus `c <= D_c < 3c`, with `D_1=1`. Let `S_n(c)` sum the squared gains
`(3^n/2^L)^2` of every legal inverse shortcut word of length `L` ending
immediately on its `n`th odd inverse. Different visits and words retain
their multiplicity. For real `sigma>=0` and integer `t>=1`, define

\[
W_t^{(\sigma)}
=\sum_{c\ge1}c^{-\sigma}D_c^{-2}S_{t+j(c)}(c).
\tag{1}
\]

At `sigma=0` this is the source's `W_t`.

Fix an original positive odd source `p`. Write

\[
q_n=U^n(p),\quad
e_n=v_2(3q_{n-1}+1)\ (n\ge1),\quad
f_n(p)=\prod_{i<n}\frac{3q_i}{3q_i+1},\quad f_0=1.
\tag{2}
\]

At shortcut time `L`, put `c_L=T^L(p)` and let `n_L` be the number of
odd inputs in the first `L` steps. The exact affine product identity is

\[
c_L=3^{n_L}2^{-L}\frac{p}{f_{n_L}(p)}.
\tag{3}
\]

Reversing a word ending on an odd inverse gives exactly one such pair
`(p,L)`, with `L>=1`. Its bin is `t_L=n_L-j(c_L)`, and its contribution
to (1), when `t_L=t`, is exactly

\[
c_L^{-\sigma}9^t4^{-L}
=\frac{f_{n_L}(p)^2}{p^2}
  \left(\frac{c_L}{D_{c_L}}\right)^2c_L^{-\sigma}.
\tag{4}
\]

Accordingly (1) is the sum of (4) over the same original sources and all
their visits in the indicated bin. All sums are nonnegative, so Tonelli
applies without an assumed independence or clock distribution.

## 2. Uniform control by the unchanged original source

The bin condition is equivalent to

\[
3^t\frac p{f_{n_L}(p)}\le2^L
  <3^{t+1}\frac p{f_{n_L}(p)}.
\tag{5}
\]

Since `j(c)>=0`, every visit in a positive bin has `n_L>=t` and hence
`f_(n_L)<=f_t`. Summing `9^t 4^(-L)` over all integer lengths satisfying
the lower bound in (5), even if some of those lengths are not visits,
gives the source-wise estimate

\[
0\le W_{p,t}^{(\sigma)}\le W_{p,t}^{(0)}
\le\frac{4f_t(p)^2}{3p^2}\le\frac4{3p^2}.
\tag{6}
\]

In particular every quantity in (1) is finite and bounded by `pi^2/6`.
The omitted sources above an integer cutoff `P>=1` contribute at most
`2/(3P)`, uniformly in `t` and in `sigma>=0`. This is the same original
source-tail control as in the primary observable.

## 3. Positive endpoint tilt always gives a zero limit

### Theorem 1

For every fixed real `sigma>0`,

\[
\boxed{W_t^{(\sigma)}\longrightarrow0\quad(t\to\infty).}
\tag{7}
\]

This is unconditional for the ordinary positive-integer dynamics.

**Proof.** Fix an original odd `p`. An orbit of a deterministic map on
positive integers either eventually repeats or has distinct states
tending to infinity.

In the first case it eventually enters a cycle. A positive odd state is
visited repeatedly on that cycle, and its factor `3q/(3q+1)` is strictly
less than one. Thus `f_t(p)->0`, and (6) proves the source's contribution
tends to zero.

In the second case `c_L->infinity`. Every positive-bin visit has
`L>=n_L>=t`. Therefore the endpoint weight `c_L^(-sigma)` tends to zero
uniformly over all visits in bin `t`. Multiplying the unweighted bound
in (6) by `sup_(L>=t)c_L^(-sigma)` proves the same source-wise limit.

Finally use the summable dominating sequence `4/(3p^2)` from (6) over
the actual odd sources. This proves (7), including when hypothetical
escaping orbits or nontrivial positive cycles exist. QED.

### Why zero is the critical endpoint exponent

For each fixed `t`, monotone convergence gives

\[
W_t^{(\sigma)}\uparrow W_t^{(0)}\qquad(\sigma\downarrow0).
\tag{8}
\]

At exponent zero, the primary source's packing argument retains a
different conclusion. On any escaping odd source `p`, it proves
`f_infinity(p)>0`; set `Phi(p)=p/f_infinity(p)<infinity`. The bin clock
has increments zero or one. At length
`ceil(log_2(3^t Phi(p)))` it is at least `t`, by (5), so some visit in bin
`t` occurs by that length. The corresponding single term is at least

\[
W_t^{(0)}\ge\frac1{4\Phi(p)^2}>0\qquad(t\ge1).
\tag{9}
\]

The no-skip assertion follows directly from the actual shortcut step:
an even step lowers `j(c)` by zero or one; an odd step raises it by zero
or one while increasing `n_L` by one. The initial bin is `-j(p)<=0`.

Thus, if an escape exists, the two limits in (7)--(8) cannot be
interchanged. The new theorem does not need the packing input, but this
comparison with the untilted signal does. The primary source receives
credit for (9) and its stronger oscillation theorem; no new oscillation
claim is made here.

## 4. One extra endpoint power gives a finite all-time budget

### Theorem 2

The actual all-centres series has the unconditional bound

\[
\boxed{
\sum_{t\ge1}W_t^{(1)}\le\frac{4\pi^2}{7}.
}
\tag{10}
\]

In particular this includes all repeated cycle visits with their genuine
gain factors; no trajectory is killed for this statement.

**The reciprocal killing telescope.** For every real `q>=1`,

\[
1-\left(\frac{3q}{3q+1}\right)^2-\frac7{16q}
=\frac{(q-1)(33q+7)}{16q(3q+1)^2}\ge0.
\tag{11}
\]

Since `f_(n+1)=f_n 3q_n/(3q_n+1)`, multiplication by `f_n^2` and a
finite telescope give

\[
\frac7{16}\sum_{n<N}\frac{f_n(p)^2}{q_n}+f_N(p)^2\le1.
\]

Increasing `N` proves, with no condition on the orbit,

\[
\boxed{\sum_{n\ge0}\frac{f_n(p)^2}{q_n}\le\frac{16}{7}.}
\tag{12}
\]

**The shortcut indexing.** In the `n`th odd gap, `n>=1`, the endpoints
after the odd step and subsequent halvings, including the terminal odd
endpoint, are

\[
2^{e_n-1}q_n,\ 2^{e_n-2}q_n,\ldots,\ q_n.
\]

At every one of those endpoints the number of odd inputs already
consumed is exactly `n`; the survival product is `f_n`, not `f_(n-1)`.
The reciprocal sum over this block is

\[
\frac1{q_n}\sum_{k=0}^{e_n-1}2^{-k}<\frac2{q_n}.
\tag{13}
\]

These disjoint blocks partition all shortcut times `L>=1`. Combining
(12)--(13) proves

\[
\sum_{L\ge1}\frac{f_{n_L}(p)^2}{c_L}
\le2\sum_{n\ge1}\frac{f_n(p)^2}{q_n}
\le\frac{32}{7}.
\tag{14}
\]

Now sum (4) with `sigma=1` over all positive bins. Each physical visit
belongs to only one bin. Dropping the restriction to positive bins and
using `(c/D_c)^2<=1` gives a bound of `32/(7p^2)` for this source.
Tonelli and `sum_(p positive odd)p^(-2)=pi^2/8` prove (10). QED.

Equations (11)--(12), including the finite remainder, summability, and
complete bound, are the scope of `SquaredSurvivalBudget.lean`. The
translation (13)--(14) and the inverse-word/source correspondence are
not claimed to be formalized in that module.

## 5. Exact comparison with the canonical ordinary Green budget

This section additionally uses the source-qualified canonical data of
PR185 `276be8154f4e867acc0230466b34d9cb224aacf5` and PR182
`9dacd610ba7735e89e2e29e4ab01795983317980`,
`research/lean-dyadic-descent-20261121/HARMONIC_CAPTURE_BRIDGE.md`.
Its domain `N` consists of nonperiodic positive odd ternary units, with
ordinary transport killed on entering any periodic state. Write

\[
a_0(x)=G(x)/x^2,\quad G(x)\ge\gamma>0,\quad
b_n=L^na_0,\quad R=\sum_{n\ge0}b_n\le4\nu,
\quad\sum_{q\in N}\frac{\nu(q)}{q^s}
\le\frac{5sA}{s-39/40}.
\tag{15}
\]

For an odd target `q` in `N`, let `S_n^u(q)` retain only odd unit
sources. The exact inverse identity and the original source floor give

\[
\boxed{
\frac{S_n^u(q)}{q^2}
=\sum_{U^nx=q}\frac{f_n(x)^2}{x^2}
\le\frac{b_n(q)}\gamma.
}
\tag{16}
\]

There is no extra `delta` loss: `f_n<=1` and `G(x)>=gamma` directly
dominate each unchanged source atom by `a_0(x)/gamma`.

An odd nonunit source becomes a unit after its first odd step. Grouping
these sources by that next unit `y`, their squared initial gains sum to
at most `12/5`, since the allowed exponents form one parity class and
`sum_(e odd, e>=1)9·4^(-e)=12/5`. Thus, for `n>=1`,

\[
\frac{S_n(q)}{q^2}
\le\frac1\gamma\left[b_n(q)+\frac{12}{5}b_{n-1}(q)\right].
\tag{17}
\]

This includes all odd original sources reaching the specified target.
It does not extend the killed harmonic reference to periodic states.

For `s>39/40`, (15)--(17) and `D_q>=q` give the actual adaptive-depth
bound

\[
\boxed{
\sum_{t\ge1}\sum_{q\in N}
q^{-s}D_q^{-2}S_{t+j(q)}(q)
\le\frac{68sA}{\gamma(s-39/40)}.
}
\tag{18}
\]

The target-dependent depth is retained. Its sum is bounded by the
complete Green sum at that same target; no time or source is resampled.
For `s=1`, Theorem 2 is a much stronger population-free bound and also
includes periodic and even centres. The role of (18) is to identify
precisely how the current canonical moment estimate enters the same
observable.

## 6. The obstruction located by these results

The known Green moment pays a positive spatial power in (18). Such a
power cannot be silently removed: Theorem 1 proves that **every** fixed
positive endpoint power already destroys the escape signal, independently
of whether an escape exists. Theorem 2 quantifies this for the reciprocal
endpoint cost by a finite budget valid even with cycles.

These estimates therefore locate the missing ordinary endpoint control at
the zero-power boundary. They establish no uniformity as the endpoint
exponent tends to zero while the bin moves. That joint regime requires a
separate argument retaining the original source; it is not supplied by
fixed-exponent dominated convergence or by (10).

The censored statistic `B_t` in the external supplement has different
per-visit weights and retains nontrivial cycles. It is not substituted
for `W_t` anywhere in this proof. No bound above is asserted for that
different observable without its corresponding source calculation.
