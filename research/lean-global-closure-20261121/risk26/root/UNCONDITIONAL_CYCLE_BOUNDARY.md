# An unconditional budget for every positive cycle and escape boundary

23 November 2026. **Written reconstruction and cross-source deduction;
not Lean formalized. Collatz remains OPEN.** The global counting theorem
already proved in PR182 supplies the entire defect budget needed by the
cycle-resolvent construction in PR180. Its predecessor-density hypothesis
`P` is unnecessary for that conclusion. A uniform tail bound by the cycle
minimum follows as well.

This is an application of the existing global count, not a claim to have
discovered that count or its reciprocal-moment consequence. The additional
step is to apply it to the union of **all** positive periodic points and
carry the resulting unconditional budget through the operator construction.
The construction cancels poles; it does not show that the cycles creating
them are absent.

## 1. Exact inputs and maps

Use the shortcut map `T(n)=n/2` for even `n`, and `(3n+1)/2` for odd
`n`, and the accelerated odd map

\[
 U(n)=(3n+1)/2^{v_2(3n+1)}.
\]

The inputs reconstructed for this note are:

| Pin | Claim used |
|---|---|
| PR182, `a7fd3ac9e5bff7412858df23d776bb847e9c1371`, `research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`, §§1–6 | Uniform count and reciprocal moment for any forward-invariant set of positive odd integers on which `U` is injective; the statement explicitly includes all positive odd periodic points |
| PR180, `7cfd911d35382d9d3bc988060ba88ade78a4267e`, `research/closing-step-20261123/GLOBAL_CONSTRUCTION.md`, §§1–3 | Meromorphic resolvent on `|z|<2`, exact classification of its simple finite-rank poles by actual positive cycles |
| Same PR180/head, `research/closing-step-20261123/CYCLE_RESOLVENT_BRIDGE.md`, §§1–4 | Grouped Blaschke construction, originally supplied with a source-qualified predecessor-density budget |

Put

\[
 \theta=H_2(\log_3 2)<1.
\]

The first input supplies one absolute constant `C` such that

\[
 F_S(X):=\#(S\cap[1,X])\le
 C\frac{X^\theta}{\sqrt{1+\log X}}                 \tag{UB1}
\]

for every such injective forward-invariant set `S`. Its elementary proof
uses one common odd-step clock for all sources being charged. Thus it
continues to apply to a union of disjoint cycles; no predecessor basin is
substituted for the set. No numerical optimization of `C` is asserted.

## 2. The budget holds simultaneously for all cycles

Index primitive positive odd cycles once each by `Cyc`. For a cycle `c`,
let `p_c` be its number of odd states, `A_c` the sum of its positive gaps,
and `m_c` its minimum. Define

\[
 \delta_c=A_c\log2-p_c\log3
 =\sum_{x\in c}\log\left(1+\frac1{3x}\right)>0.    \tag{UB2}
\]

The equality is the product of the actual odd transition identities.
Distinct primitive cycles have disjoint states. On the union of their
odd states, `U` is a permutation. Hence (UB1) applies to this union with
the **same** constant `C`.

For `M>=1`, the subunion of cycles with `m_c>=M` also satisfies the
hypotheses and contains only states at least `M`. Tonelli gives

\[
 \begin{aligned}
 \sum_{m_c\ge M}\delta_c
 &\le\frac13\sum_{x\in\cup_{m_c\ge M}c}\frac1x\\
 &=\frac13\int_M^\infty\frac{F_S(t)}{t^2}\,dt\\
 &\le \frac{C}{3(1-\theta)}
       \frac{M^{\theta-1}}{\sqrt{1+\log M}}
 =:L(M).                                         \tag{UB3}
 \end{aligned}
\]

In particular `sum_c delta_c <= L(1)<infinity`. This is unconditional
within the reconstructed elementary count. It does not require `P`,
Tao's almost-all theorem, a predecessor-population estimate, or any
uninspected large computation. Positivity justifies all infinite
rearrangements.

## 3. All cycle poles admit one bounded holomorphic cancellation factor

Set `w=z/2` and `a_c=3^{p_c}/2^{A_c}=exp(-delta_c)`, so `0<a_c<1`.
The roots corresponding to cycle `c` satisfy `w^{A_c}=a_c`. Their
Blaschke mass is

\[
 A_c(1-a_c^{1/A_c})\le\delta_c.
\]

For each complete root group define

\[
 \beta_c(w)=\frac{a_c-w^{A_c}}{1-a_cw^{A_c}}.
\]

On `|w|<1`, `|beta_c(w)|<=1`, and on `|w|<=r<1`,

\[
 |1-\beta_c(w)|
 \le(1-a_c)\frac{1+r^{A_c}}{1-r^{A_c}}
 \le\delta_c\frac{1+r}{1-r}.                      \tag{UB4}
\]

Consequently

\[
 \mathcal B(w)=\prod_{c\in\mathrm{Cyc}}\beta_c(w)   \tag{UB5}
\]

converges normally on the unit disk and is not identically zero:

\[
 |\mathcal B(w)|\le1,\qquad
 \mathcal B(0)=\exp\left(-\sum_c\delta_c\right)
 \ge e^{-L(1)}>0.
\]

At a point in the disk, only finitely many root groups vanish, and the
remaining product is nonzero there. Its zero multiplicity is the number
of groups containing that point, with their simple multiplicities.

There are finitely many cycles with `m_c<M`, because their distinct
minima are positive odd integers below `M`. Let `B_{<M}` be their finite
product. Telescoping products, using that each factor has modulus at
most one, gives the useful quantitative strengthening

\[
 \boxed{\sup_{|w|\le r}
 |\mathcal B(w)-\mathcal B_{<M}(w)|
 \le\frac{1+r}{1-r}L(M).}                         \tag{UB6}
\]

This is a bound for the exact mathematical finite product. It is not an
algorithm deciding which small integers are periodic: an escaping orbit
starting below `M` need not be recognized in finite time by following it.

For the actual operator on

\[
 X=\{f:\mathbb N_{>0}\to\mathbb C:
       \sup_n|f(n)|/n<\infty\},\qquad
 Kf(n)=3^{-\mathbf1_{n\text{ odd}}}f(Tn),
\]

PR180's pole classification now gives the unconditional conclusion

\[
 \boxed{\mathcal B(z/2)(I-zK)^{-1}
        \text{ is operator-norm holomorphic for }|z|<2.} \tag{UB7}
\]

Indeed every pole there is simple and comes from an actual positive
cycle, and (UB5) has a zero at each such pole. This uses the separately
reconstructed PR180 operator theorem; (UB1) alone is not an operator
theorem. The existence of the factor is valid even if unknown cycles
exist. Neither (UB7) nor the tail estimate proves outer continuation.

## 4. The same count makes the escaping scalar boundary unconditional

Let `x_i=U^i(n)` be one escaping positive odd orbit, with gap sums `A_i`
and `A_0=0`. The states are distinct, and their set is forward invariant
with injective `U`. Let `M=min_i x_i`, an attained positive integer.
Define the actual rational approximants

\[
 E_i=\frac{2^{A_i}x_i}{3^i}.
\]

The odd transition law gives both exact identities

\[
 E_{i+1}=E_i+\frac{2^{A_i}}{3^{i+1}},\qquad
 E_i=n\prod_{j<i}\left(1+\frac1{3x_j}\right).      \tag{UB8}
\]

By (UB1), the correction sum is at most `L(M)`. Thus `E_i` increases
to a finite real `E_infinity` with

\[
 n<E_\infty\le n e^{L(M)},\qquad
 0<\sum_{i\ge0}\frac{2^{A_i}}{3^{i+1}}
   =E_\infty-n\le n(e^{L(M)}-1).                  \tag{UB9}
\]

There is no predecessor-density premise in this statement either. For
the fixed shortcut forcing series

\[
 B_n(z)=\sum_{j\ge0}
       \frac{e_j(n)}{3^{p_{j+1}(n)}}z^j,
\]

the nonzero terms at `z=2` are exactly the summands in (UB9). Meanwhile
the same rational partial sums converge to `-n` in `Q_2`, because
`E_i=2^{A_i}x_i/3^i ->0` there. Therefore

\[
 B_n(2)>0\text{ in }\mathbb R,
 \qquad B_n(2)=-n\text{ in }\mathbb Q_2.           \tag{UB10}
\]

These are two different completions and not a contradiction. A valid
arithmetic gluing theorem for this exact coefficient sequence would be
decisive. Positivity or convergence at both places does not supply it.

The tail is also controlled by the actual future floor
`M_i=min_{j>=i}x_j`, which tends to infinity:

\[
 0<E_\infty-E_i\le E_i(e^{L(M_i)}-1).             \tag{UB11}
\]

This follows by applying the same count to the injective future ray.
There is no asserted rate of growth of `M_i` in `i`.

## 5. What the arithmetic rationality literature still requires

Bost--Chambert-Loir, *Analytic curves in algebraic varieties over number
fields*, arXiv:math/0702593v3, Theorems 7.8–7.9 and Example 7.10, were
read at the primary text: <https://arxiv.org/pdf/math/0702593>.
The general algebraicity/rationality criterion needs positive adelic
capacity; its degree-zero variant in Theorem 7.8 additionally assumes
algebraicity and a boundary condition. Finite scalar boundary sums do
not verify those hypotheses.

For an escaping ray whose shortcut odd frequency has a limit `rho`,
the nonzero coefficients of `B_n` have archimedean radius `3^rho`
and 3-adic radius `3^{-rho}`. At the critical value
`rho=log_3 2`, these are `2` and `1/2`, with product exactly one.
All other finite-place radii are one. Thus the disks provided by the
coefficient growth give no strict adelic-capacity surplus. Without a
frequency limit the two radii involve the liminf and limsup on odd
indices and their product is at most one. These statements concern
Taylor radii, not a proof that no larger meromorphic domains exist.

The scalar value and operator assertions must also remain separate.
PR180 exhibits the actual powers-of-two coordinates
`(3-z^2)B_{2^k}(z)=z^k`; in the stated weighted sup norm they obstruct
meromorphic continuation across every point of `|z|=2`. A construction
of larger scalar domains therefore cannot simply be replaced by a
uniform continuation assertion in `X`.

## 6. Remaining central step

This deduction removes a real external hypothesis from a construction
that treats **every** positive cycle, and supplies uniform floor tails.
It does not exclude even one new primitive positive cycle. Summability
of positive defects permits infinitely many small defects. The first
open step in a cycle-exclusion argument is still a full numerical
divisibility obstruction for actual positive-gap words, or another
argument proving that the cancellation factor has only the known-cycle
zeros. On the escape side, it is a source-specific arithmetic
continuation or an equivalent ordinary-source contradiction, retaining
the exact coefficients of `B_n`.
