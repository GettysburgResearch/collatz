# Full-cycle arithmetic after multiplicative expansion

Date: 23 November 2026. **Status: a direct closing attempt with an exact
all-period rational control. No unrestricted positive integer-cycle
exclusion is proved.** No historical novelty claim is made for the
elementary valuation criterion below.

The unchanged target is the complete numerical condition

\[
D=2^A-3^p>0,\qquad
C(w)=\sum_{i=0}^{p-1}2^{d_i}3^{p-1-i},\qquad D\mid C(w).
\tag{1}
\]

Every actual primitive positive integer cycle of shortcut length A
supplies A distinct rotations to that same zero fibre. The desired
strict count `N_0(A,p)<A` remains open. No proper denominator factor,
polynomial gcd, or independently resampled carry replaces (1).

## 1. The literature input actually tested

The external input is Lyapunov Weaver, *Polynomial multiplicative expansion in
Collatz orbit sets*, rStation Paper 144/v1 (14 November 2026):
<https://rstation.ai/problems/collatz/papers/144>.
Corollary 2 gives `|BB|>=p^(5/4)/32` for an actual p-state odd cycle B;
Theorem 12 gives `E_times(B)=O(p^3/log(2p))`. This pass reconstructs only
its fixed-class incidence argument and cycle specialization. Its
trajectory, sample, and local Sidon results are not new work of this
checkpoint, and its complete energy proof was not independently reviewed.

For the reconstruction, retain a division class of t sources and use
the lines

\[
v=\frac{3c}{2^a b}u+\frac{c}{2^a},\qquad (b,c)\in B^2.
\]

Their incidences at `(bx,c U(x))` lie in `BB x BB`. The intercept then
slope recovers `(b,c)`, so the lines are distinct. With `M=|BB|`, the
Szemeredi--Trotter inequality with the conservative constant four gives

\[
t p^2\le4(M^{4/3}p^{4/3}+M^2+p^2)
\le12M^{4/3}p^{4/3}.
\tag{2}
\]

The second comparison uses `p<=M<=p^2`. In a nontrivial integer cycle,
the total division exponent is less than `7p/4`, because each state is
at least three and `(10/3)^4<2^7`. Thus more than `p/4` edges have
division exponent one, and (2) gives the stated cycle bound with slack.
This is a reconstruction of the cited input, not a separate advance.

**The exact proposed consumer.** If full numerical cancellation forced
the ordinary cycle set to have

\[
|BB|<p^{5/4}/32,
\tag{3 — OPEN}
\]

the incidence bound would close that candidate. A suitable lower bound
on the actual multiplicative energy could similarly conflict with the
source-qualified energy estimate. Neither condition has been obtained
from (1).

The new PR175 residual-degree theorem gives a superpolynomial
*polynomial* denominator. It does not bound the cardinality of the
ordinary product set. Linear recurrence or Fourier rank is not a
product-cardinality bound. Its Hankel continuation also records that
the natural integral normalization pays the maximum cycle height;
the polynomial bound on the minimum does not remove that cost.

## 2. A useful valuation criterion

Let `d` be a positive odd integer and let

\[
0<n_0<n_1<\cdots<n_{p-1}
\]

be positive odd integers such that

\[
v_2(n_0+d)>v_2(n_1+d)>\cdots>v_2(n_{p-1}+d).
\tag{4}
\]

Then the set of these integers is **multiplicatively Sidon**: equality
`n_i n_j=n_k n_l` implies equality of the unordered pairs of indices,
allowing repeated indices.

Proof. Cancel any common index in the two pairs, using positivity. If
the pairs were different, their remaining largest index L could not
occur twice on its side: its square is larger than a product of two
smaller positive states. Thus the largest index occurs exactly once,
on one side, with every other index smaller. Put `s=v_2(n_L+d)`.
For every smaller index j, (4) gives

\[
n_j\equiv-d\pmod {2^{s+1}},\qquad
n_L\equiv2^s-d\pmod {2^{s+1}}.
\]

The product containing the largest state is therefore
`d^2-d*2^s` modulo `2^(s+1)`, whereas the other product is `d^2`.
Since d is odd these differ, a contradiction. This also handles a
repeated smaller index. Square versus square is already covered by
strict monotonicity. This proves the criterion.

## 3. Every positive one-rise rational cycle attains maximal products

Fix integers `p>=2` and `A>p` with `2^A>3^p`. Use the primitive
shortcut word

\[
w=1^p0^{A-p},\qquad
D=2^A-3^p,\quad C=3^p-2^p,\quad t=C/D.
\tag{5}
\]

Its p odd states are

\[
x_i=(3/2)^i(t+1)-1\quad(0\le i<p).
\tag{6}
\]

Put `h=2^(A-p)-1`, which is positive and odd. Their common-denominator
numerators are exactly

\[
N_i=D x_i=2^{p-i}3^i h-D.
\tag{7}
\]

These are positive odd integers and strictly increase:

\[
N_0=C>0,\qquad
N_{i+1}-N_i=2^{p-i-1}3^i h>0.
\tag{8}
\]

They obey the actual numerator equations

\[
3N_i+D=2N_{i+1}\quad(i<p-1),\qquad
3N_{p-1}+D=2^{A-p+1}N_0.
\tag{9}
\]

Because all N_i and D are odd, the displayed powers of two are exact.
Thus the rational shortcut trajectory is legal: it has p successive
odd steps and then A-p halvings. Its least odd period is p, since
the odd states are distinct; its least shortcut period is A, also
visible from the unique cyclic run of ones and unique cyclic run of
zeros. All shortcut states are at least t: the odd states increase,
and the final even chain descends from `2^(A-p)*t` to t.

The shifted valuations in (7) are

\[
v_2(N_i+D)=p-i.
\tag{10}
\]

Apply the criterion with `d=D`. Scaling by the same nonzero D preserves
all multiplicative equalities. Hence the *entire* odd-state set B of
this rational cycle satisfies

\[
\boxed{|BB|=\frac{p(p+1)}2,
\qquad E_\times(B)=2p^2-p.}
\tag{11}
\]

The energy count is exact: each square has one ordered representation;
each product of two different states has two. Thus the energy is
`p+4*p*(p-1)/2`. No finite enumeration or probabilistic genericity is
used in (11).

This general argument supersedes the first test family `A=5p`, where
smallness of t alone also rules out product collisions. The theorem
does not require the rational cycle to have a small minimum.

## 4. Arbitrarily high, arbitrarily long nonintegral controls

For every real floor `H>=1` and every requested period lower bound P,
there is a cycle (5) with `p>P`, all its shortcut states above H, and
its entire odd-state set satisfying (11). Its full denominator does
not divide its carry.

Here is an all-parameter existence proof, not a claim inferred from
the examples. The number `alpha=log_2(3)` is irrational by unique
factorization. Density of its positive multiples modulo one supplies
arbitrarily large p and `A=ceil(p alpha)` with

\[
1+\frac1{4H}<\frac{2^A}{3^p}<1+\frac1{2H}.
\tag{12}
\]

Choose such p also satisfying
`(2/3)^p<1/2` and `2^p>4H+1`. Then

\[
t=\frac{1-(2/3)^p}{2^A/3^p-1},\qquad H<t<4H.
\tag{13}
\]

The whole rational shortcut cycle is therefore above H. But

\[
t+1=\frac{2^p(2^{A-p}-1)}D,
\qquad v_2(t+1)=p.
\tag{14}
\]

If t were an ordinary integer, (14) would force the positive integer
`t+1` to be at least `2^p`, contradicting (13) and `2^p>4H+1`.
Consequently `D` does not divide C. The reduced denominator remains
nontrivial; no proper-factor or unreduced-denominator shortcut is used.

For completeness, the density fact here has an elementary proof.
Pigeonhole among finitely many fractional parts gives a nonzero signed
integer q with `0<{q alpha}<epsilon`. The finite set of multiples of
this small positive fractional part up to its last value below one has
all circular gaps at most epsilon. Translate this finite net by
`{M alpha}` and take M sufficiently large that every integer index
`M+jq` exceeds P. Every open interval longer than epsilon is hit at
an index above P. Taking epsilon smaller than the interval corresponding
to (12) proves the required arbitrarily late visits.

## 5. What this resolves about the attempted bridge

The incidence proof is insensitive to the nonzero additive constant:
for `3n+d`, replace the line intercept in Section 1 by `dc/2^a`.
After multiplying a rational cycle by its common odd denominator,
the same argument therefore applies to its positive odd numerator
cycle. Product cardinality and multiplicative energy themselves are
unchanged by the common scaling.

Thus the strong product-growth input is compatible with every feature
of the high controls proved here: literal cyclic legality, primitivity,
unbounded period, any prescribed positive floor, and even the largest
possible product set and smallest possible energy. This is why neither
cyclic closure nor real positivity can supply a small-product or
large-energy contradiction.

**First remaining inference.** One must use the specific equality of
the reduced denominator to one to force an additional restriction,
or transfer product growth into the actual complete carry zero fibre
by a proved arithmetic inequality. The new residual degree and the
available incidence theorem do not give that transfer. This result
does not rule out an argument that genuinely uses full integrality.

The pass also tested the fixed-rank unit-equation compression, the
full-rank Hankel norm, and normalized coefficient differences against
this same goal. The unit-equation theorem leaves rank uncontrolled;
the determinant retains the wrong-conjugate possibility; reducing
archimedean variation reintroduces finite-place normalization costs.
No new rank upper bound, distinguished-fibre gcd bound, or strict
zero-fibre count was obtained. No Lean wrapper was added for those
unproved implications.

`check_cycle_product_control.py` replays the displayed rational family
and high controls in exact arithmetic, including all word parities,
exact gaps, shifted valuations, full gcd reduction and product counts
on the stated small cases. The unbounded results are supplied by the
proofs above. `SOURCES.json` records the inspected source pins and the
limited scope of each literature use.
