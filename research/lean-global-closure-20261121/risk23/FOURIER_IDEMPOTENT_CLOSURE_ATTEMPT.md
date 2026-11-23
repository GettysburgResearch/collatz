# A direct Fourier-idempotent attack on the full basin

**23 November 2026. Status: full closure not obtained.**

This attempt targets every positive integer, including hypothetical cycles and
escaping components. It replaces the earlier finite-dimensional Mahler target
by finite Fourier-measure regularity. The regularity implication was attacked
directly. An exact positive-integer countertest shows that neither one shortcut
pullback nor one fully odd-accelerated pullback preserves the proposed
regularity, even when the latter retains dyadic invariance and the anchor at
one. The actual all-time basin fixed point has not been proved regular.

No new Lean compilation is claimed by this note. The analytic arguments are
written proofs; the companion script checks exact integer identities and the
finite algebra in the displayed boundary residue.

## 1. Latest inputs and the genuinely different closing target

The own-branch baseline is
`8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`. The following peer inputs were
read at their pinned objects:

* PR178 `7e4569476e152f6b8537bdc1711df595ec1ffd89`,
  `research/whole-repo-synthesis-20261122/arithmetic/WHOLE_WORD_MERGER_ATTEMPT.md`.
  Its whole-word inverse reservoir supplies a favorable size comparison only
  after the different inverse word is integral. No regularity of a basin
  indicator follows from that comparison.
* PR178 `9d4ae09cd50ccd54036141edc3938d2cabe786fd`,
  `research/deep-machinery-20261122/mahler/MIXED_DILATION_ATTEMPT.md`.
  This already gives the exact two-scale equations, the unbounded ternary
  root-of-unity ladder, and the eventual-periodicity consumer. Those results
  are not counted as new here.

Write

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd},\end{cases}
\qquad
a(n)=1_{\{T^j(n)=1\text{ for some }j\ge0\}}\quad(n>0).
\]

Define the **symmetric** extension by

\[
b(0)=1,\qquad b(n)=a(|n|)\quad(n\ne0).
\]

The choice at zero is only a finite coefficient adjustment. It makes the
expected solution particularly simple: if Collatz holds, every coefficient
of `b` is one and its Fourier measure is the unit atom at angle zero.

For `0<r<1`, use normalized circle measure and set

\[
K_r(\theta)=1+2\sum_{n\ge1}a(n)r^n\cos(n\theta),
\qquad
M(r)=\frac1{2\pi}\int_{-\pi}^{\pi}|K_r(\theta)|\,d\theta.
\tag{1}
\]

The proposed closing estimate is

\[
\boxed{\sup_{0<r<1}M(r)<\infty.}
\tag{2}
\]

This is not asserted. It is a precise sufficient estimate on the actual
all-time basin, with no fixed source clock, bounded word language, or
distributional replacement for an ordinary starting integer.

## 2. Why estimate (2) would prove the full conjecture

### 2.1. The measure criterion

For any bounded two-sided sequence `b`, a bound of the form (2) is equivalent
to the existence of a finite complex measure `mu` on the circle whose
Fourier coefficients are `b`.

In one direction, `K_r` is convolution of `mu` with the positive Poisson
kernel, whose normalized integral is one, so `M(r)<=||mu||`.
In the other direction, the measures `K_r(theta)dtheta/(2 pi)` have bounded
total variation. Weak-star compactness along `r` tending to one produces a
finite measure. Testing against each character gives its `n`th coefficient
as `b(n)`, because `r^|n| b(n)` tends to `b(n)`. Uniqueness follows from
density of trigonometric polynomials among continuous functions.

Because `b` only takes the values zero and one, such a measure satisfies
`mu*mu=mu`. Cohen's idempotent theorem then puts the support of `b` in the
coset ring of the discrete group of integers. On this group, every such
set is periodic outside a finite set: nontrivial subgroup cosets are
arithmetic progressions, the remaining subgroup is `{0}`, and finite
Boolean combinations preserve this description.

The primary text inspected is Green--Sanders, *A quantitative version of
the idempotent theorem in harmonic analysis*, Annals of Mathematics 168
(2008), Theorem 1.1. Its hypothesis is a **finite measure**, not merely a
bounded sequence of coefficients. The quantitative bound on coset
complexity does not remove that hypothesis.

<https://annals.math.princeton.edu/wp-content/uploads/annals-v168-n3-p09.pdf>

### 2.2. The arithmetic consumer

The basin has the exact relations

\[
a(2n)=a(n),\qquad a(2n+1)=a(3n+2).
\tag{3}
\]

As already proved in the pinned Mahler note, any eventually periodic
sequence satisfying (3) is constant on the positive integers. Here is the
short consumer, to keep the logical dependency explicit. For an eventual
period `m`, let `lambda` give the eventual residue values. Doubling removes
all factors of two from the period. With the period odd, every residue
has arbitrarily large odd representatives, and the odd relation gives
`lambda(3x+1)=lambda(x)`. This removes every factor of three. With
`gcd(m,6)=1`, the two affine compositions give

\[
\lambda(6x+1)=\lambda(x)=\lambda(6x+2).
\]

Since `6x` runs over every residue, `lambda` is constant. Finally,
`a(2^j n)=a(n)` transports this eventual constancy back to each positive
integer. Since `a(1)=1`, the constant is one.

Consequently, (2) would prove the full conjecture. Conversely, the full
conjecture makes `K_r` the positive Poisson kernel, so `M(r)=1`. Thus (2)
is an exact analytic closing target, not an independently established
theorem about the basin. Bell--Lagarias already gives the related
rationality/Collatz equivalence; no priority over that work is claimed.

<https://www.impan.pl/shop/publication/transaction/download/product/82190>

## 3. Attempting a norm estimate: the integer operator and its boundary

First try the shortcut pullback on all integer Fourier coefficients:

\[
(Cf)(n)=f(T(n)),\qquad n\in\mathbb Z.
\]

For a point measure whose coefficients are `f(n)=exp(i n theta)`, its image
has the four-atom representation

\[
\frac12\delta_{\theta/2}
+\frac12\delta_{\theta/2+\pi}
+\frac{e^{i\theta/2}}2\delta_{3\theta/2}
-\frac{e^{i\theta/2}}2\delta_{3\theta/2+\pi}.
\tag{4}
\]

The first pair retains the even indices; the second pair retains the odd
indices and supplies the affine `+1`. Thus the full-integer operator has
norm at most two on Fourier measures, and for a generic angle the four
atoms are distinct and the norm is exactly two. This calculation supplies
no contraction.

More seriously, (4) is **not the operation on the symmetric extension in
(1)**. Negative integers under the `3x+1` map are the reflection of the
positive `3x-1` map. Reflecting the positive output of `C` instead amounts
to taking separate positive and negative frequency pieces. That
projection is not a bounded operation on finite measures. The next
section computes the resulting failure explicitly, using only positive
ordinary integers.

## 4. An exact one-step regularity failure

### 4.1. A shortcut step already creates logarithmic divergence

Begin with

\[
h(n)=1_{5\mid n}\qquad(n\in\mathbb Z).
\]

Its Fourier measure is the probability measure equally supported on the
five fifth roots of unity. It is a zero-one sequence, is symmetric, and
satisfies `h(2n)=h(n)`.

For a positive integer `n`, direct modular arithmetic gives

\[
h(T(n))=1\quad\Longleftrightarrow\quad n\equiv0\text{ or }3\pmod {10}.
\tag{5}
\]

Reflect this positive output to negative indices, and set its zero
coefficient to one. Its positive generating series, including zero, is

\[
G(z)=\frac{1+z^3}{1-z^{10}},
\qquad
L_r(\theta)=2\operatorname{Re}G(re^{i\theta})-1.
\tag{6}
\]

This is an explicit rational function, so its boundary behavior can be
computed without Cohen's theorem. At the tenth roots
`zeta_k=exp(2 pi i k/10)`, its simple-pole coefficients are

\[
A_k=\frac{1+\zeta_k^3}{10},
\qquad
G(z)=\sum_{k=0}^9\frac{A_k}{1-z/\zeta_k}.
\]

A nonzero imaginary part of `A_k` contributes a conjugate-Poisson term
to `L_r`, with a `1/theta` absolute-integral divergence near that root.
Separating disjoint small arcs around the ten roots gives the exact
leading asymptotic

\[
\frac1{2\pi}\int_{-\pi}^{\pi}|L_r(\theta)|\,d\theta
=\frac{2}{5\pi}\cot\!\left(\frac\pi{10}\right)
  \log\frac1{1-r}+O(1).
\tag{7}
\]

For completeness, the local contribution is
`(2/pi)|Im A_k| log(1/(1-r))+O(1)`. The real part contributes only bounded
Poisson mass; all other poles are bounded on that arc. Summing uses
`sum_k |sin(3 pi k/5)|=2 cot(pi/10)`.

The anchored variant

\[
c(0)=1,\qquad c(n)=1-1_{5\mid n}\quad(n\ne0)
\tag{8}
\]

starts from the finite real measure
`delta_0 - uniform_fifth_roots + normalized_Lebesgue_measure`.
It has `c(1)=c(2)=1` and dyadic invariance. Its symmetrized shortcut
output has the same logarithmic coefficient in (7): complementing adds
only a Poisson kernel and a constant. Thus anchoring at one does not
repair the one-step norm estimate.

### 4.2. Restoring all dyadic invariance does not repair the estimate

Let `odd(n)` remove all powers of two from a positive integer, and let

\[
U(q)=\frac{3q+1}{2^{v_2(3q+1)}}\qquad(q>0\text{ odd}).
\]

Instead of a shortcut step, apply the actual fully odd-accelerated map:

\[
d(n)=c(U(\operatorname{odd}(n)))
=1-1_{\operatorname{odd}(n)\equiv3\ (5)}
\quad(n>0),\qquad d(0)=1.
\tag{9}
\]

The congruence follows because division by any power of two preserves
divisibility by five. Both `d(2n)=d(n)` and `d(1)=d(2)=1` now hold
exactly. Nonetheless its symmetric extension is not a finite Fourier
measure. There are two independent proofs.

**Nonperiodicity proof.** Write
`e(n)=1_{odd(n)=3 mod 5}` for positive `n`. If it had an eventual period,
doubling transports it to a period on all positive inputs and removes
the period's powers of two. Let `m` be the remaining odd period. On odd
inputs `e(n)=1` exactly when `n=3 mod 10`. Comparing such an `n` with
`n+2m` forces `5|m`. But `e(6)=e(3)=1`, while `6+m` is odd and equals
one modulo five, so `e(6+m)=0`, a contradiction. Cohen's theorem therefore
excludes a finite Fourier measure for the symmetric `e`, and hence for
the symmetric `d`.

**Explicit nonreal boundary residue.** Unique extraction of the odd part
gives the positive generating series

\[
E(z)=\sum_{j\ge0}\frac{z^{3\cdot2^j}}{1-z^{10\cdot2^j}}.
\tag{10}
\]

Put `zeta=exp(2 pi i/5)`. Then

\[
\begin{split}
\lim_{r\uparrow1}(1-r)E(r\zeta)
&=\frac1{10}\sum_{j\ge0}2^{-j}\zeta^{3\cdot2^j}\\
&=\frac{8\zeta^3+4\zeta+2\zeta^2+\zeta^4}{75}
=:A.
\end{split}
\tag{11}
\]

Interchanging limit and sum is justified explicitly: for `p=2^j`,

\[
0\le\frac{(1-r)r^{3p}}{1-r^{10p}}
=\frac{r^{3p}}{\sum_{l=0}^{10p-1}r^l}
\le\frac1{3p+1}.
\]

The geometric denominator `1-1/16` in (11) comes from the four-cycle
`3,1,2,4` of `3*2^j` modulo five. Crucially,

\[
\operatorname{Im}A
=\frac{\sin(2\pi/5)-2\sin(\pi/5)}{25}
=\frac{2\sin(\pi/5)(\cos(\pi/5)-1)}{25}<0.
\tag{12}
\]

If the symmetric `e` were the Fourier coefficients of a finite measure,
the measure would be real, by uniqueness and the real symmetric
coefficients. The radial residue of its Cauchy transform at a unit-circle
point is its atom at that point, hence real. This last assertion follows
directly from dominated convergence: the relevant kernel is
`(1-r)/(1-r exp(i x))`, whose absolute value is at most one and whose
limit is one at `x=0` and zero elsewhere. Equation (12) is a contradiction.

This second proof locates an actual noncancelling boundary term, rather
than merely citing an abstract obstruction. It also proves divergence of
the symmetric Abel norms without using the idempotent theorem.

Neither `c` nor `d` is claimed to be the basin indicator. For example,
`d(3)=0` and `d(T(3))=d(5)=1`, so full odd-edge invariance fails. This is
therefore a counterexample to the attempted **regularity propagation**,
not a counterexample to Collatz or to regularity of its actual fixed point.

## 5. Finite defects cannot simply be discarded

There is also an actual inverse-orbit control inside the positive `3x+1`
map. Let `v(n)` indicate whether `n` ever reaches three. Since
`3 -> 5 -> 8 -> 4 -> 2 -> 1 -> 2`, one has `v(3)=1`, `v(1)=0`, and

\[
v(2n)=v(n),\qquad v(n)-v(T(n))=1_{n=3}.
\tag{13}
\]

Thus its functional equation has just one finite source defect. If the
symmetric Abel norms for `v` were bounded, Cohen would imply eventual
periodicity. The arithmetic consumer in Section 2 only uses the branch
identities at sufficiently large inputs, so the single defect would not
affect it. Dyadic invariance would then make `v` constant everywhere,
contradicting its values at one and three. Its norms are consequently
unbounded.

This does not settle the homogeneous basin equation. It does rule out
treating a finite inhomogeneous polynomial as automatically harmless in
the proposed norm estimate. Bell--Lagarias independently establishes the
natural-boundary result for this ancestor series; the Fourier-measure
argument here identifies the stronger regularity input being tested.

## 6. Exact outcome and the remaining closing step

The proposed heavy theorem applies cleanly after a bound on the **actual
all-time symmetric basin**. The remaining claim is precisely (2).

The attempted proof by propagating a finite Fourier measure through
actual Collatz pullbacks fails already on explicit dyadically invariant,
zero-one data anchored at one. Fully odd-accelerated pullback retains
those properties and still creates the nonreal residue (11)--(12).
The whole-word source reservoir does not supply a cancellation of that
type; its unclosed integrality condition is a different obligation.

A valid continuation would have to use the complete homogeneous fixed
point together with its actual basin selection to prove (2), or replace
(2) by a different analytic rigidity premise and then establish that
premise. No such step was obtained here. In particular, bounded
coefficients, Hadamard idempotence, dyadic invariance, the anchor at
`{1,2}`, and a bounded norm of the input measure are not enough for the
regularity propagation that this attack first attempted.

## Reproduction

Run `python check_fourier_interface.py` to write
`fourier-interface-checks.json`. The script checks the modular formulas
and accelerated formula on a finite range, the four-cycle of exponents,
and the exact rational weights in (11). Optional high-precision numerical
values are explicitly labeled as numerical sanity checks. The infinite
norm conclusions and interchange of limits are proved above; they are
not inferred from that finite computation.
