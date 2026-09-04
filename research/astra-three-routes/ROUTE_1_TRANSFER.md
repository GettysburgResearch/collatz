# Route 1 — eliminate nonresonant excursions exactly

**Agent:** `astra-three-route-01` (GPT-6 Pro). **Date:** 2026-09-05.

**Status:** New claims `T-ATR-101` through `T-ATR-104` are **PROPOSED pending independent review**. Complete elementary proofs follow. Neither a fixed-floor exceptional power saving nor Collatz convergence is claimed. In this file, absorption means reaching **1 or an explicitly retained resonance set**, not reaching 1 alone.

## 1. T-ATR-101: an exact ordinary first-return map and its entire inverse fan

Use the one-division shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

Let

\[
H=\{n\ge4:n\equiv1\pmod3\}.
\]

Kill an orbit when it reaches 1. For `n in H`, let `R(n)` be its first positive-time visit to `H union {1}`. This visit always exists and has the following exact formula:

\[
\begin{array}{c|c|c}
\text{source}&R(n)&\text{shortcut length }\ell_R(n)\\\hline
n\equiv0\pmod4&n/4&2\\
n\text{ odd},\ n+1=2^a u,\ u\text{ odd}&(3^a u-1)/2&a+1\\
n\equiv2\pmod4,\ n/2+1=2^a u,\ u\text{ odd}&(3^a u-1)/2&a+2
\end{array}
\tag{1}
\]

The only source in `H` returning to 1 is 4. Furthermore,

\[
\ell_R(n)\le\lfloor\log_2(2n+1)\rfloor+2.
\tag{2}
\]

### Proof and ordinary coverage

For an odd number `m=2^a u-1`, the next `a` shortcut steps are odd steps and

\[
T^i(m)=3^i2^{a-i}u-1\quad(0\le i\le a).
\]

At time `a` the value is even and is 2 modulo 3; dividing it by 2 gives `(3^a u-1)/2`, which is 1 modulo 3. Every intermediate state after the first odd step is 2 modulo 3. For an even source in `H`, its first half is 2 modulo 3. If that half is even, the second half is already in `H union {1}`. Otherwise apply the odd-run identity. This proves both the formulas and the **first**-return property. The bound (2) follows from `a<=log_2(m+1)` in each case. Substitution shows that only the two-even-step case at `n=4` returns to 1.

Every positive integer reaches `H union {1}`: first strip its powers of 2 to obtain an odd `m`. If `m=1`, stop; otherwise the displayed odd-run formula reaches `H`. Thus termination of `R` on all of `H` is equivalent to Collatz. No compactness or infinite parity realization is involved.

### Exact inverse fan

Fix `y in H` and write

\[
h=h(y)=\nu_3(2y+1)\ge1,\qquad
u=u(y)=\frac{2y+1}{3^h},\qquad 3\nmid u,
\]

where the symbol `u` is used below for this odd positive integer. Put

\[
z_j=2^j3^{h-j}u-1\quad(0\le j\le h),\qquad
B=2^{h+1}u-1,\qquad k=k(y)=\nu_3(B).
\]

Then **all** inverse first-return sources are

\[
\boxed{R^{-1}(y)=\{2z_j:0\le j<h\}\ \cup\ \{z_h:\ k\ge1\}.}
\tag{3}
\]

These sources are distinct positive integers in `H`.

Indeed, the first inverse step from `y` must be its even preimage `2y=z_0`, in residue class 2. At a class-2 node `z_j`, the even predecessor `2z_j` is in `H`, while its odd predecessor is `z_(j+1)`. The latter remains class 2 until `j+1=h`. The terminal `z_h` is class 1 exactly when `k>=1`, and otherwise is class 0. From class 0 all backward steps remain class 0, so no further first-return source in `H` is hidden there. Source 1 cannot occur for `y>=4`. The even exits are distinct because `z_(j+1)+1=(2/3)(z_j+1)`; the terminal odd exit is different from every even exit. This proves completeness, not just inclusion.

## 2. T-ATR-102: an explicit summable weight with a global charged bound

Define

\[
P(y)=\frac{(2y+1)^2}{3^{h(y)}}=3^{h(y)}u(y)^2\in\mathbb N,
\qquad V(y)=\frac1{P(y)}.
\tag{4}
\]

This differs from PR #90's affine form `n+1`: the induced fan singles out **`2n+1`**. On `H`,

\[
2y+1\le P(y)\le\frac{(2y+1)^2}{3},\qquad P(y)\ge9.
\tag{5}
\]

The positive weight is summable, with

\[
\sum_{y\in H}V(y)\le\frac23.
\tag{6}
\]

To see this, enlarge the sum to all `h>=1,u>=1`, obtaining
`sum 3^(-h) sum u^(-2)<=1`. The enlarged sum includes the excluded pair `(h,u)=(1,1)`, of weight `1/3`, so subtract it. We used only `sum u^(-2)<=2`. More quantitatively, if `M>=4` and `J=floor(log_3(2M+1))`, then

\[
\sum_{\substack{y\in H\\y\ge M}}V(y)
\le\frac{2J+3}{2M+1}.
\tag{7}
\]

For `1<=h<=J`, use `sum_(u>=A)u^(-2)<=2/A` with `A=(2M+1)/3^h`; each `h` contributes at most `2/(2M+1)`. For `h>J`, the full sum is at most `3^(-J)<=3/(2M+1)`.

Let the killed inverse operator be

\[
(Kf)(y)=\sum_{\substack{x\in H\\R(x)=y}} f(x),\qquad y\in H.
\]

Set

\[
Q(y)=\max\left\{1,\frac{3^{h(y)+k(y)}}{4^{h(y)}}\right\}.
\tag{8}
\]

The global inequality is

\[
\boxed{KV(y)\le\frac12 Q(y)V(y)\quad(y\in H).}
\tag{9}
\]

### Exact evaluation before estimation

Formula (3) gives

\[
KV(y)=
\sum_{j=0}^{h-2}\frac{3}{(2^{j+2}3^{h-j}u-3)^2}
+\begin{cases}
1/(3B^2),&k=0,\\
4\,3^k/(3B^2),&k\ge1.
\end{cases}
\tag{10}
\]

The sum is empty for `h=1`. For `j<=h-2`, the valuation of `2(2z_j)+1` is exactly 1. At the last even exit, `2(2z_(h-1))+1=3B`; if the terminal odd exit exists, its affine form is `B`. Their combined weights give the second term of (10).

For `h>=2`, each `M_j=2^(j+2)3^(h-j)u` in the first sum is at least 36, so `M_j-3 >= (11/12)M_j`. Summing the resulting geometric series gives

\[
\frac{\text{first sum}}{V(y)}
\le\frac{48}{605}(3/4)^h-\frac{108}{605}3^{-h}
<\frac{27}{605}<\frac1{20}.
\tag{11}
\]

Also `2^(h+1)u>=8` for every `y in H`: if `h=1`, the excluded small values and `3`-unit condition give `u>=5`. Consequently
`B>=(7/8)2^(h+1)u`. In both cases of the boundary term,

\[
\frac{\text{boundary}}{V(y)}
\le\frac{64}{147}(3/4)^h3^k.
\tag{12}
\]

Combining (11), (12), and

\[
\frac1{20}+\frac{64}{147}=\frac{1427}{2940}<\frac12
\]

proves (9). For `h=1`, omit the first sum and use the same bound. These are rational inequalities; no floating-point logarithm determines a branch.

## 3. T-ATR-103: resonance entrance, finite-time mass loss, and exact density

Define the retained resonance set and its complement in `H`:

\[
\mathcal R=\{y\in H:3^{h(y)+k(y)}>4^{h(y)}\},\qquad
G=H\setminus\mathcal R.
\tag{13}
\]

Because each inverse term is nonnegative, (9) implies for every actual edge `x -> y` in `H`:

\[
\boxed{P(y)\le\frac12Q(y)P(x).}
\tag{14}
\]

Thus **arrival at a nonresonant endpoint halves an integer rank**, regardless of whether the source was resonant.

### Deterministic entrance bound

Starting from `x in G`, let `b=floor(log_2 P(x))`. The orbit enters `mathcal R union {1}` in at most `b+1` applications of `R`, and in at most

\[
\boxed{(b+1)(b+2)}
\tag{15}
\]

shortcut steps. Otherwise (14) would force a positive integer rank below 1. Until entrance, (5) and (14) bound every hard-state source by its initial rank; (2) therefore bounds each intervening block by `b+2` shortcut steps. Every nonconvergent orbit must consequently visit `mathcal R` infinitely often. This is a restriction on every possible counterexample, not an exclusion of all such counterexamples.

### All-source weighted loss before resonance

Let `K_GG` mean the inverse operator restricted to sources and endpoints both in `G`. Then `K_GG V_G <= V_G/2`. Nonnegative summation gives, for every integer `t>=0`,

\[
\boxed{
\sum_{\substack{x\in G\\x,Rx,\ldots,R^t x\in G}}V(x)
\le\frac23\,2^{-t}.}
\tag{16}
\]

Indeed the left side is `sum_(y in G) (K_GG^t V_G)(y)`. This treats **all ordinary sources** and arbitrary `t`, but kills on entering **resonance or 1**. It is not a bound for the set of sources avoiding 1 alone and does not instantiate PR #88's fixed-floor power-saving hypothesis.

### Density of the retained set

For `h>=1`, let `K_h` be the least nonnegative integer such that `3^(h+K_h)>4^h`. In fact `K_h>=1`. The exact natural density in all positive integers is

\[
\boxed{d(\mathcal R)=\sum_{h\ge1}3^{-h-K_h}.}
\tag{17}
\]

For fixed `h`, resonance is the single congruence
`u == 2^(-h-1) (mod 3^K_h)`, hence one residue for `y` modulo `3^(h+K_h)`. This automatically has valuation exactly `h` because that `u` is a 3-unit. The classes for distinct `h` are disjoint. The union of all omitted classes with `h>J` is contained in `2y+1 == 0 (mod 3^(J+1))`. Therefore finite-union densities converge to (17), and the truncation error is at most `3^(-J-1)`.

At `J=32`, exact rational arithmetic encloses this density between

\[
\frac{5928117868465419442}{36472996377170786403}
\quad\text{and}\quad
\frac{5928117868465426003}{36472996377170786403}.
\]

It is approximately `0.162534435261698`, measured against **all positive integers**, not against `H`. Density alone supplies no contradiction to infinite visits.

## 4. T-ATR-104: an exact resonance-return operator with a certified truncation tail

Rows in every block below denote **endpoints**, and columns denote **sources**. For example, `K_GmathcalR` takes a function on resonant sources to its contribution at nonresonant endpoints.

The weighted supremum norm `||f||_V = sup_(y in G) |f(y)|/V(y)` gives

\[
\|K_{GG}\|_V\le\frac12,\qquad
(I-K_{GG})^{-1}=\sum_{t\ge0}K_{GG}^t,\qquad
\|(I-K_{GG})^{-1}\|_V\le2.
\tag{18}
\]

The series identity follows directly from the geometric norm bound.

Let `S` be first positive return from `mathcal R` to `mathcal R union {1}`, killed on 1. It is everywhere defined: an initial nonresonant excursion terminates by (15). Its exact inverse operator is

\[
\boxed{
K_{\rm eff}=K_{\mathcal R\mathcal R}
+K_{\mathcal RG}(I-K_{GG})^{-1}K_{G\mathcal R}.}
\tag{19}
\]

Every inverse first-return path either is a direct resonant-to-resonant edge or has one or more nonresonant interior states. Expanding (19) enumerates exactly those alternatives. Deterministic forward dynamics prevents duplicate counting of a source with two different first-return paths. No infinite safe excursion is omitted.

There is also an explicit error bound. For `0<=f<=C V` on `mathcal R`, define

\[
K_{\rm eff}^{(L)}=K_{\mathcal R\mathcal R}
+\sum_{t=0}^{L-1}K_{\mathcal RG}K_{GG}^tK_{G\mathcal R},\qquad L\ge0.
\]

Then, pointwise at every resonant endpoint,

\[
\boxed{
0\le (K_{\rm eff}-K_{\rm eff}^{(L)})f(y)
\le C2^{-L}K_{\mathcal RG}V_G(y)
\le C2^{-L-1}Q(y)V(y).}
\tag{20}
\]

Indeed `K_GmathcalR f <= (C/2)V_G`, because at a nonresonant endpoint the full incoming `V`-mass is at most `V/2`. Apply `K_GG^t`, sum the geometric tail starting at `t=L`, and then apply the finite incoming row `K_mathcalR G`. The last inequality follows from (9).

Choosing

\[
L(y)\ge\lceil\log_2 Q(y)\rceil+m
\]

makes the tail at most `C2^(-m-1)V(y)`. All such depth choices can be made by exact comparisons of integers. This is an **adaptive all-excursion truncation theorem**, not a fixed-block extrapolation.

## 5. The remaining end-to-end target

A positive summable `w` on `mathcal R` with

\[
K_{\rm eff}w<w
\tag{21}
\]

would prove Collatz. If an exceptional set exists, its intersection with `mathcal R` is nonempty and forward/backward invariant under `S`. Summing (21) over that intersection contradicts conservation of its finite positive mass. Alternatively, a well-founded rank decreasing under all resonant returns would suffice.

The positive-mass criterion itself is credited to PR #90, rather than renamed as a new general theorem. The new result here is the explicit induced fan, nonresonant contraction, and the error-controlled elimination (19)-(20).

The unmodified `V` is **not** the missing supersolution: `R(13)=10`, both states are resonant, and `V(13)=1/27 > 1/147=V(10)`. Thus even one direct incoming term violates nonexpansion at 10. A useful next certificate must redistribute mass across, or amortize, resonant excursions. Equation (20) currently applies to trial functions bounded by `C V`; extending it to an unbounded correction factor requires its own proved envelope.

The imported `0.901` exponent race remains an alternative closing target, but no fixed-floor exceptional estimate with that exponent is established here. More than half the hard-state space has been eliminated in one exact sense; the remaining resonance process is still an infinite arithmetic problem.
