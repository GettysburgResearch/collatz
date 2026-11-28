# The critical one-copy gap needs no orbit-packing theorem

**A dependency reduction for the existing critical-grade consumer.** The exact cycle-mixture formula in [CRITICAL_GRADE_TAIL.md](../arithmetic/CRITICAL_GRADE_TAIL.md) uses a uniform orbit-packing input. Its sufficient one-quantile lower-bound criterion does not need that input: an elementary finite inequality after the true minimum already gives the same strict upper gap. This note supplies that inequality. It does not prove the required lower bound.

Use the native shortcut map, its global minimum \(m(n)\), and the first date \(\tau(n)\) attaining it. Put
\[
 \delta_1=\log2-\tfrac12\log3,\quad \mu=1/\delta_1,\quad
 h=\lfloor\mu\log X\rfloor,\quad
 W_X(n)=\frac{2(a_h(n)-h/2)}{\sqrt h},
\]
where \(a_j(n)\) counts odd departures before date \(j\). The clock variance is the same as in the companion note:
\[
 \sigma^2=\frac{2(\log3)^2}{\log^3(4/3)}.
\]
We import only the natural minimum-clock limit and its joint known-basin label from [Leen's original manuscript](https://doi.org/10.5281/zenodo.23269488), source SHA-256 `211bc4fe107b3821e510486be28cf53f69751f71394582822faf385d09561e37`, until the final positive-predecessor upgrade. No height-process theorem, phase theorem, cycle classification, or uniform orbit-packing estimate is required for the upper bound below.

## 1. A finite postminimum count inequality

Start at an actual positive global minimum \(m\), and follow its next \(t\) steps. Every state is at least \(m\). If \(b_t\) is the number of odd departures and the endpoint is \(y\), the exact product gives
\[
 2^t\frac ym
   =\prod_{j<t,\ T^j(m)\ \mathrm{odd}}
       \left(3+\frac1{T^j(m)}\right)
   \le(3+1/m)^{b_t}.
\]
Since \(y\ge m\),
\[
 \boxed{\quad b_t\ge\beta_m t,\qquad
 \beta_m=\frac{\log2}{\log(3+1/m)}.\quad}                 \tag{1}
\]
In particular \(b_t\ge t/2\). Every positive global minimum is odd; an even one would immediately halve to a smaller value. Hence on the bad event \(m>1\), one has \(m\ge3\) and
\[
 b_t\ge\beta_3t,\qquad \beta_3=\frac{\log2}{\log(10/3)}>1/2.
\]
This is a finite deterministic inequality on every such future, including a hypothetical escaping future. It assumes no distribution of its parity bits. The elementary oddness statement is among the five audited roots of [NativeMinimum.lean](NativeMinimum.lean); the logarithmic product inequality (1) remains a written proof.

## 2. The preminimum correction needs only distinctness

Define
\[
 C_j(n)=\sum_{i<j,\ T^i(n)\ \mathrm{odd}}
       \log\left(1+\frac1{3T^i(n)}\right).
\]
For \(j\le\tau(n)\), the departed states are distinct. Otherwise a cycle would have begun before the first global minimum and that minimum would already have occurred. Therefore
\[
 0\le C_j(n)\le\frac13\sum_{k=1}^j\frac1k
       \le\frac{1+\log h}{3}\qquad(1\le j\le\min(h,\tau(n))). \tag{2}
\]
The empty sum at \(j=0\) is zero. The exact native identity is
\[
 \log T^j(n)=\log n+a_j(n)\log3-j\log2+C_j(n).             \tag{3}
\]
Set, for \(h\ge1\),
\[
 \epsilon_X=
 \frac{2[\delta_1+(1+\log h)/3]}{\log3\sqrt h}\longrightarrow0.
\]
If \(\tau(n)>h\), equations (2)–(3), \(T^h(n)\ge1\), and \(n\le X\) give the uniform bound
\[
                              W_X(n)\ge-\epsilon_X.         \tag{4}
\]
Thus every fixed strictly negative grade event is postminimum for all sufficiently large cutoffs. This conclusion uses a logarithmic harmonic-sum bound, not a uniform reciprocal sum over an entire orbit.

## 3. A deterministic Gaussian-clock comparison on every bad source

Write
\[
 Z_X(n)=\frac{\tau(n)-h}{\sigma\sqrt{\log X}},\qquad
 c_X=\frac{2\delta_1\sigma\sqrt{\log X}}{\log3\sqrt h}
       \longrightarrow1,
\]
and
\[
 r_*=
 \frac{\log2-\beta_3\log3}{\delta_1}\in(0,1).
\]
Suppose \(\tau(n)\le h\) and \(m(n)>1\). Split the grade at \(\tau\), use (3) there, and apply (1) to the remaining \(h-\tau\) steps. The nonnegative terms \(\log(X/n)\) and \(\log m\) can be dropped. Equations (1)–(2) then give
\[
\begin{aligned}
 W_X(n)
 &\ge\frac{2\delta_1(\tau-h)}{\log3\sqrt h}
       +\frac{2(\beta_3-1/2)(h-\tau)}{\sqrt h}
       -\epsilon_X\\
 &=\boxed{\ c_Xr_*Z_X(n)-\epsilon_X\ }.                    \tag{5}
\end{aligned}
\]
This is uniform in the positive source \(n\le X\). The same constant \(r_*\approx0.42170026\) appears in the companion cycle argument, but (5) requires no eventual periodicity.

For \(z>\epsilon_X\), (4)–(5) give the literal event inclusion
\[
 \{m>1,\ W_X\le-z\}
 \subseteq
 \left\{m>1,\ Z_X\le\frac{-z+\epsilon_X}{c_Xr_*}\right\}. \tag{6}
\]
There is no claim about a fresh postminimum random walk.

## 4. The same strict upper gap with fewer analytic inputs

Let \(B=\{n:m(n)=1\}\) have natural density \(b\). The imported joint clock law gives
\[
 \Pr(B,Z_X\le t)\to b\Phi(t),\qquad
 \Pr(B^c,Z_X\le t)\to(1-b)\Phi(t).
\]
The second statement follows also by subtracting the first from the unconditional clock limit.

On \(B\), the future after the minimum is the known two-cycle. Its odd count differs from half its length by at most one-half. Equations (2)–(3), together with tightness of \(\log(X/n)\), therefore give \(W_X=c_XZ_X+o_{\Pr}(1)\) on already-entered known-basin sources. By (4), a fixed strictly negative threshold discards the other sources. Consequently
\[
 \Pr(B,W_X\le-z)\longrightarrow b\Phi(-z).
\]
Using (6) and Gaussian continuity proves, for every fixed \(z>0\),
\[
\boxed{
 b\Phi(-z)\le\liminf_X\Pr(W_X\le-z)
 \le\limsup_X\Pr(W_X\le-z)
 \le b\Phi(-z)+(1-b)\Phi(-z/r_*).
}                                                            \tag{7}
\]
In particular the upper gap from the fair Gaussian coefficient is at least
\[
 (1-b)\,[\Phi(-z)-\Phi(-z/r_*)]>0\qquad\text{if }b<1.
\]
A matching lower bound \(\liminf_X\Pr(W_X\le-z)\ge\Phi(-z)\) still forces \(b=1\). The named positive-predecessor theorem then upgrades that density-one conclusion to full Collatz, as in the companion note. The same full-law stationary transfer converts this into its existing one-copy relative selector estimate.

The exact cycle-mixture formula remains stronger descriptive information and retains its orbit-packing input. Formula (7) is a sufficient upper-gap theorem with fewer dependencies. It does not assert that the full negative-tail limit exists without the extra input, and it does not prove the missing lower estimate.

## 5. Finite native product kernel

The arithmetic lane's [MinimumProduct.lean](../arithmetic/MinimumProduct.lean) freshly certifies four roots: the native one-step cap, its finite-prefix product, cancellation at a supplied finite minimum, and the specialization
\[
                         2^t3^{a_t}\le10^{a_t}
\]
when the supplied minimum is at least three. The general denominator-cleared minimum bound is \(2^t m^{a_t}\le(3m+1)^{a_t}\); taking logarithms gives (1). The source and a separate root/type/axiom audit completed under Lean 4.34.1 with only `Quot.sound` and `propext`, reusing the pinned dependencies. The [receipt](../../../reports/astra-collision-factor-bridge-20261128/arithmetic/minimum-product-lean.json) pins source SHA-256 `e2874bd79b99bafef976cfbdaa20b7910ff51055c6ff7ff66abef19973da8f1a`. The Gaussian limits, probability event comparisons, stationary transfer, and convergence implication remain written deductions with the stated external inputs; no cold rebuild or independent LeanChecker replay is claimed.
