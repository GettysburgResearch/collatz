# What the forward section forces on a divergent orbit

**Status: the Fourier-cancellation theorem is formalized in `PhaseFrequency.lean`.
The interval-frequency and shrinking-section consequences below have written
proofs. No assertion here proves that a positive divergent Collatz orbit exists
or that none exists.**

## Ordinary map and clock

Use the shortcut Collatz map from PR 173, and write the ordinary odd orbit as

\[
x_{j+1}=\frac{3x_j+1}{2^{a_j}},\qquad
a_j=v_2(3x_j+1),\qquad x_j\in\mathbb N_{>0}\text{ odd}.
\]

The index `j` counts odd steps, rather than every shortcut step. Put

\[
\theta_j=\log_2x_j,\quad\alpha=\log_2 3,\quad
e_j=\log_2\!\left(1+\frac1{3x_j}\right).
\]

Then the exact identity is

\[
\theta_{j+1}=\theta_j+\alpha-a_j+e_j.\tag{1}
\]

This is the same identity used in the finite forward-section proof. Its
source is [PR 173 at the frozen head
`fa0c9e2a2851e6324391e39c17afcb5913185aec`](https://github.com/GettysburgResearch/collatz/blob/fa0c9e2a2851e6324391e39c17afcb5913185aec/research/lean-shell-cover/ForwardSection.lean).
The new result below uses (1) over all odd times of one fixed ordinary orbit.

## Fourier cancellation without an assumed growth rate

**Theorem PF-1.** Suppose `x_j` tends to infinity. For every nonzero integer
`k`,

\[
\lim_{N\to\infty}\frac1N\sum_{j=0}^{N-1}
  \exp(2\pi i k\log_2x_j)=0.\tag{2}
\]

The positive-frequency case is
`divergent_odd_fourier_mean`. Negative frequencies follow by conjugation; the
Lean theorem states the positive-frequency case explicitly. Neither a lower
growth rate nor convergence of `sum 1/x_j` is assumed.

**Proof.** Let `z_j=exp(2*pi*i*k*theta_j)` and
`r=exp(2*pi*i*k*alpha)`. The integer term in (1) disappears. Thus

\[
z_{j+1}=rz_j\exp(2\pi i k e_j),\qquad
d_j:=z_{j+1}-rz_j\longrightarrow0.
\]

The second assertion follows from `x_j -> infinity`, hence `e_j -> 0`, and
`|z_j|=|r|=1`. A direct telescoping sum gives

\[
(r-1)\sum_{j<N}z_j=z_N-z_0-\sum_{j<N}d_j.\tag{3}
\]

Divide (3) by `N`. The first term tends to zero because its norm is at most
`2/N`; the average of `d_j` tends to zero by Cesaro convergence. Finally
`r != 1`: otherwise `k*log_2 3` would be an integer. The frozen PR 173
integer-power separation theorem `grid_barrier`, applied with `N=4^k`, would
then assert `4^k+1 <= 4^k`. Therefore (2) follows.

The reusable theorem `mean_zero_of_rotation` formalizes (3) and this limiting
argument for any bounded complex sequence with a nontrivial asymptotic
rotation.

If an ordinary odd trajectory never repeats a value, it tends to infinity:
injectivity gives a finite preimage for each finite set of naturals. This is
the hypothesis of `nonrepeating_odd_fourier_mean`. The formal theorem
`odd_repeat_finite_range` proves that any repeat traps every later term in
the finite range before the second occurrence. Hence unboundedness of one
fixed trajectory implies injectivity and escape; this is used in
`unbounded_odd_fourier_mean`. Periodic trajectories are not covered.

## Fixed leading-digit windows have their rotation frequency

**Written consequence PF-2.** Under the same escape hypothesis, for every
fixed `0 <= a < b <= 1`,

\[
\frac{\#\{j<N:\{\log_2x_j\}\in[a,b)\}}N\longrightarrow b-a.\tag{4}
\]

Here braces mean fractional part. In particular, for each fixed `1 <= u <
v <= 2`, odd-orbit binary significands fall in `[u,v)` with frequency
`log_2(v/u)`. This is an odd-clock statement; the time spent at intervening
even values is not counted.

For completeness, (4) follows from (2) by approximating continuous periodic
functions uniformly by trigonometric polynomials, then bounding the indicator
of `[a,b)` above and below by continuous periodic functions with integrals
within any prescribed epsilon of `b-a`. Every nonconstant Fourier term of
the approximating polynomial has mean zero by (2), and its constant term
is its integral. The finitely many endpoints have zero limiting frequency
by the same upper approximations with arbitrarily small support.

This approximation argument is a written mathematical implication. It is not
an additional Lean theorem in this checkpoint.

## The forced shrinking section has zero orbit-time frequency

Recall the frozen section: an odd `x` is marked when, for `d=floor(log_2 x)`,

\[
(d+1)(x-2^d)\le70\,2^d.
\]

**Written consequence PF-3.** On a divergent ordinary odd trajectory,

\[
\lim_{N\to\infty}
\frac{\#\{j<N:x_j\text{ is marked}\}}N=0.\tag{5}
\]

At a marked point,

\[
0\le\{\log_2x\}\le
\log_2\!\left(1+\frac{70}{d+1}\right)\longrightarrow0
\]

as `x -> infinity`. Given any fixed epsilon in `(0,1)`, all sufficiently
late marked points therefore lie in the fixed phase interval `[0,epsilon)`.
Equation (4) bounds their upper frequency by epsilon. Let epsilon tend to
zero. This proves (5).

There is also a direct proof from (2) without using the full interval
criterion. For each integer `m >= 1`, the Fejer polynomial

\[
F_m(y)=\frac1{m+1}\left|\sum_{k=0}^{m}e^{2\pi iky}\right|^2
=1+2\sum_{k=1}^{m}\left(1-\frac{k}{m+1}\right)\cos(2\pi ky)
\]

is nonnegative and has orbit average tending to one by (2). For
`0 <= y <= 1/(6m)`, every cosine in the sum is at least `1/2`, so
`F_m(y) >= (m+2)/2 >= m/2`. All sufficiently late marked phases lie in that
interval. Their upper frequency is therefore at most `2/m`, and `m` is
arbitrary.

PR 173's bounded-visit theorem applies at every tail of the ordinary orbit,
so marked visits still occur infinitely often. If their odd clocks are
`j_1 < j_2 < ...`, (5) gives `r/j_r -> 0`, and hence `j_r/r -> infinity`.
The arithmetic mean of the gaps between the first `r` visits diverges. This
does not assert that each individual gap tends to infinity.

## Where the attempted completion stops

These theorems impose deterministic phase statistics on any hypothetical
nonperiodic orbit. They do not determine the valuations `a_j` in (1).
The exact size drift is

\[
\frac{\log_2 x_N-\log_2 x_0}{N}
=\log_2 3-\frac1N\sum_{j<N}a_j+\frac1N\sum_{j<N}e_j.
\]

Escape already makes the final average tend to zero. A contradiction would
follow from an eventually negative drift, for example from
`liminf (sum_{j<N} a_j)/N > log_2 3`. Fourier cancellation of the leading
phases supplies no such inequality: the valuations disappear identically
from the characters. Recovering a sufficient relation between the low-bit
valuation process and these leading phases is the first unsupported step.

The formal development makes a concrete version of this low-bit obstruction
explicit. Define

\[
L(x)=1+\mathbf1_{x\equiv1\pmod4}+\mathbf1_{x\equiv5\pmod8}.
\]

For odd `x`, `L(x) <= v_2(3x+1)`. On the odd residues `1,3,5,7 mod 8`, its
values are exactly `2,1,3,1`. The kernel-checked `lowBits_sum_bound` gives,
for every finite ordinary prefix,

\[
\sum_{j<N}L(x_j)\le\log_2x_0+N\log_2 3+\sum_{j<N}e_j.
\]

The theorem `lowBitsMean_eventually_le` consequently proves that for every
`epsilon>0`, on an escaping orbit,

\[
\frac1N\sum_{j<N}L(x_j)\le\log_2 3+\epsilon
\]

for all sufficiently large `N`. In particular, such an orbit cannot have
each of its four odd residues modulo eight occur with frequency `1/4`:
that would make the displayed average tend to `7/4`, strictly larger than
`log_2 3`. The strict comparison follows from `3^4=81<128=2^7`.

Thus the necessary obstruction is particularly concrete: any divergent
trajectory has uniform leading logarithmic phases, while its low three
bits must keep enough bias to defeat the displayed valuation threshold.
No independence of those two processes is asserted.

The inverse-log width of the forced section also depends on the point being
visited. Fixed-window equidistribution alone supplies no rate allowing that
moving width to be substituted in (4). Equation (5) is an upper-frequency
consequence, not a count of visits before a prescribed finite deadline and
not a convergence certificate.
