# R-9807 -- Native special-vector phase allocation has an exact ceiling

Claim ID: `R-9807`
Title: The summed native Pade vector has no hidden staggered cancellation and equal allocation is uniquely optimal
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-p`
Reviewing agents: `gpt56-synthesis-01-wave12-cold-review`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `PR20/L-9408`, `PR20/L-9411`, `PR20/T-9416`
Scope: the scalar phasewise root-product Pade family, for every displayed period `r`; the period-ten consequence is a method-closure statement
Refuted route: exploiting the native special coefficient vector solely by unequal phase allocation in one scalar root product
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Use the arbitrary-allocation root-product family of `PR20/L-9411`.  Thus

\[
 T={64\over81},\qquad \lambda=T^{9S},\qquad R=\lambda^r,
 \qquad Z=T^\zeta,
\]

and the phase constants are

\[
 C_j=T^{\gamma_j},\qquad
 \gamma_j=j+9A_j(W)+9mj,qquad 0\le j<r.
\]

The exponents `gamma_j` strictly increase.  Moreover

\[
 \boxed{\zeta-\gamma_{r-1}=1+9(S+m)>0.}                 \tag{1}
\]

Choose arbitrary integers `n_j>=0`, put

\[
 D=\sum_{j=0}^{r-1}n_j\ge1,
\]

and let

\[
 \mathcal C
 =\bigcup_{l=0}^{r-1}
   \{r(D+t)+l:0\le t<n_l\}.                         \tag{2}
\]

For `N>=D`, the phase contribution to the error coefficient is

\[
 \Gamma_{j,N}
 =C_jR^{N(N-1)/2}(Z\lambda^j)^N
  \prod_{c\in\mathcal C}(1-\lambda^{c-rN-j}),       \tag{3}
\]

and the native special-vector coefficient is

\[
 a_N=\sum_{j=0}^{r-1}\Gamma_{j,N}.                  \tag{4}
\]

Define, whether or not the corresponding product has a zero factor,

\[
 \Phi_j(N)=\gamma_j+\zeta N+9S\left\{
 {rN(N-1)\over2}+jN
 +\sum_{c\in\mathcal C}\min(0,c-rN-j)
 \right\}.                                         \tag{5}
\]

## Theorem 1 -- the combined zero window is exactly the minimum allocation

Put `u=N-D`.  Then

\[
 \boxed{\Gamma_{j,N}=0\iff u<n_j.}                 \tag{6}
\]

For every active phase `u>=n_j`, one has

\[
 \boxed{v_2(\Gamma_{j,N})=6\Phi_j(N).}             \tag{7}
\]

If `i<j` are both active at the same block, then

\[
 \boxed{
 \Phi_j(N)-\Phi_i(N)
 \ge \gamma_j-\gamma_i+9S(j-i)(N-D)>0.
 }                                                   \tag{8}
\]

Consequently, if

\[
 J_N=\{j:n_j\le N-D\},\qquad j_N=\min J_N,
\]

then, whenever `J_N` is nonempty,

\[
 \boxed{
 a_N\ne0,
 \qquad v_2(a_N)=6\Phi_{j_N}(N).
 }                                                   \tag{9}
\]

In particular, with

\[
 s=\min_j n_j,
\]

the combined special-vector error has exactly `s` zero blocks:

\[
 \boxed{
 a_D=\cdots=a_{D+s-1}=0,
 \qquad a_N\ne0\quad(N\ge D+s).
 }                                                   \tag{10}
\]

Thus unequal allocation cannot create even one extra cancellation by summing
the native phase vector.  This closes the staggered transition strip left
open in `L-9884`.

### Proof

Every root in (2) has a unique residue `l` modulo `r`.  Hence
`rN+j` belongs to `mathcal C` exactly when

\[
 j=l,\qquad N=D+t,\qquad 0\le t<n_j,
\]

which proves (6).

If no factor vanishes, a factor with positive exponent is a `2`-adic unit,
whereas

\[
 v_2(1-\lambda^d)=v_2(\lambda^d)=54Sd
 \qquad(d<0).
\]

Extracting all negative powers proves (7).

For fixed `c`, the function

\[
 j\longmapsto\min(0,c-rN-j)
\]

decreases by at most one at each step.  Therefore, for `i<j`,

\[
 \min(0,c-rN-j)-\min(0,c-rN-i)\ge-(j-i).
\]

There are exactly `D` roots.  Substitution in (5) proves the weak inequality
in (8), and strictness follows from `gamma_j>gamma_i`.  The least active
phase is therefore unique, so it cannot cancel in (4).  This proves (9),
and (6) and (9) give (10). **QED**

## Theorem 2 -- one explicit term controls the evaluated error

For every fixed phase, its nonzero exponents strictly increase after
activation:

\[
 \boxed{
 \Phi_j(N+1)-\Phi_j(N)
 \ge\zeta+9S\{r(N-D)+j\}>0
 }                                                   \tag{11}
\]

for `N>=D+n_j`.

The first-active exponent of a phase with a larger allocation is strictly
larger.  Precisely, if

\[
 x=n_i,\qquad y=n_j=x+h,qquad h\ge1,
\]

then

\[
 \boxed{
 \Phi_j(D+y)-\Phi_i(D+x)>0.
 }                                                   \tag{12}
\]

Let

\[
 j_*=\min\{j:n_j=s\},\qquad N_*=D+s.               \tag{13}
\]

Then `(j_*,N_*)` is the unique least-valuation term among every nonzero
`Gamma_(j,N)` in the full evaluated error.  Hence

\[
 \boxed{
 v_2\!\left(\sum_{N\ge D}a_N\right)
 =6\Phi_{j_*}(N_*).
 }                                                   \tag{14}
\]

The arbitrary-allocation denominator is a `2`-adic unit.  Therefore, for the
Pade pair `(A_{\mathbf n},B_{\mathbf n})` of `PR20/L-9411`,

\[
 \boxed{
 v_2\!\left(
 F(1)-{A_{\mathbf n}(1)\over B_{\mathbf n}(1)}
 \right)
 =6\Phi_{j_*}(N_*).
 }                                                   \tag{15}
\]

### Proof

Increasing `N` by one decreases each truncated root contribution in (5) by
at most `r`.  Their total loss is therefore at most `rD`, while the base term
gains `rN+j`.  This proves (11).

For (12), compare the thresholds at the two first-active blocks.  Their
difference is

\[
 \delta=rh+j-i\ge r-(r-1)=1.
\]

Each of the `D` truncated root contributions can decrease by at most `delta`.
Writing `N=D+x`, the remaining base contribution after this worst possible
loss is exactly

\[
 \delta x+{rh(h-1)\over2}+jh\ge0.                  \tag{16}
\]

Thus

\[
 \Phi_j(D+y)-\Phi_i(D+x)
 \ge\gamma_j-\gamma_i+\zeta h.
\]

By (1), the right side is at least

\[
 \zeta-\gamma_{r-1}>0,
\]

which proves (12).  Equation (8) orders phases whose allocations tie, while
(11) orders every later term within one phase.  Thus `(j_*,N_*)` is the
unique global minimum.  The terms tend quadratically to infinity in
`2`-adic valuation, so the unique minimum controls the convergent evaluated
sum, proving (14).

Finally, the constant term of `B_{\mathbf n}(1)` is one.  Every other
monomial contains `Z^k` with `k>=1`; the root-exponent nonnegativity proved in
`PR20/L-9411` shows that it has strictly positive `2`-adic valuation.
Therefore `v_2(B_{\mathbf n}(1))=0`, and (15) follows. **QED**

## Theorem 3 -- closed endpoint formula

At the unique controlling endpoint, the negative roots are exactly

\[
 \{r(D+t)+l:0\le t<s,\ 0\le l<r\}
 \ \cup\
 \{r(D+s)+l:0\le l<j_*\}.                         \tag{17}
\]

Consequently, define

\[
 \boxed{
 K_r(D,s,j)
 ={1\over2}\left\{
 rN(N-1)+2jN-r^2s^2-rs-2rsj-j(j+1)
 \right\},
 \quad N=D+s.
 }                                                   \tag{18}
\]

Then

\[
 \boxed{
 \Phi_{j_*}(N_*)
 =\gamma_{j_*}+\zeta(D+s)+9S K_r(D,s,j_*).
 }                                                   \tag{19}
\]

For equal allocation `n_j=n`, one has `D=rn`, `s=n`, `j_*=0`, and (18)
reduces exactly to

\[
 K_r(rn,n,0)
 ={n\{nr(r^2+r+1)-r^2-2r\}\over2}
 =L_{r,n}.                                          \tag{20}
\]

### Proof

At `N=D+s`, every root with `t<s` is negative.  A root with `t=s` is
negative precisely when `l<j_*`; it exists there because minimality of
`j_*` among the phases with allocation `s` forces `n_l>s`.  Every remaining
root has positive exponent.  Summing (17) gives

\[
 \sum_{c\in\mathcal C}\min(0,c-rN_*-j_*)
 =-{r^2s^2+rs+2rsj_*+j_*(j_*+1)\over2}.            \tag{21}
\]

Equations (5), (18), and (21) prove (19); direct substitution proves (20).
**QED**

## Corollary -- exact special-vector allocation functional

Let `D` tend to infinity through allocation vectors for which

\[
 {n_j\over D}\longrightarrow p_j,
 \qquad p_j\ge0,
 \qquad\sum_jp_j=1,
\]

and put `p=min_j p_j`.  Equations (18)--(19) give the exact quadratic error
shape, in the normalization used by `PR20/T-9416`,

\[
 \boxed{
 {\Phi_{j_*}(N_*)\over 9SrD^2}
 \longrightarrow
 e_{\rm sp}(p)
 ={1+2p-(r-1)p^2\over2}.
 }                                                   \tag{22}
\]

Together with the raw denominator-height shape of `PR20/L-9411`,

\[
 h(\mathbf p)={1+\sum_jp_j^2\over2},               \tag{23}
\]

the actual native special-vector error has the pre-reduction functional

\[
 \boxed{
 \sigma_{\rm sp}(\mathbf p)
 ={1+2p-(r-1)p^2\over1+\sum_jp_j^2}.
 }                                                   \tag{24}
\]

It satisfies

\[
 \boxed{
 \sigma_{\rm sp}(\mathbf p)
 \le {r^2+r+1\over r(r+1)},
 }                                                   \tag{25}
\]

with equality only at equal allocation `p_j=1/r`.  Thus `T-9416`'s
phase-allocation ceiling is not merely a worst-individual-phase guarantee:
it is the exact asymptotic functional of the summed native coefficient
vector.

For `r=1`, necessarily `p_0=p=1`, so (24)--(25) both equal `3/2` and
the equality assertion is immediate.  Assume henceforth that `r>=2`.
Convexity gives

\[
 \sum_jp_j^2\ge p^2+{(1-p)^2\over r-1},
\]

so (24) is at most

\[
 f_r(p)
 ={(r-1)\{1+2p-(r-1)p^2\}\over r-2p+rp^2}.
\]

Since `0<=p<=1/r` and

\[
 f_r'(p)
 ={2(r-1)(r+1-r^2p-p^2)\over(r-2p+rp^2)^2}>0,
\]

the maximum occurs at `p=1/r`; the equality conditions force every
coordinate to equal `1/r`.

For period ten, the best raw-height benchmark in the entire scalar
root-product allocation class is therefore

\[
 \boxed{
 \mu_{10}^{\rm root}
 ={1\over\log_{64}81}\left(1+{1\over110}\right)
 =0.954998217905888\ldots<1.
 }                                                   \tag{26}
\]

This does not settle the period-ten value.  It proves that tailoring only the
phase allocation to the special native coefficient vector cannot exploit the
dimension-ten gap in the imported Vaananen--Wallisser theorem.  A successful
native proof must use a construction outside one scalar root product, or a
quadratic reduced-height saving.

## Dependency and scope audit

- `PR20/L-9408` supplies `gamma_j`, `zeta`, and identity (1).
- `PR20/L-9411` supplies the exact root set, phase product, denominator, and
  raw height shape.
- `PR20/T-9416` is context for (25), but the optimization is repeated above.
- The proof is finite valuation geometry plus the ultrametric inequality.  No
  external transcendence theorem and no large computation is used.
- The result applies to every positive word and every displayed period, not
  only period ten.
- It does not cover Hermite--Pade systems, several independent root products,
  polynomial multipliers, adjacent-order determinants, resultants, or
  systematic numerator/denominator gcd savings.
- The bound in (26) is a raw/pre-reduction height benchmark.  It is not an
  upper bound on what a quadratic reduced-height factor could accomplish.
- No irrationality theorem and no Collatz conclusion is claimed.

## Bounded replay

An independent temporary exact-exponent replay checked equations (6)--(12)
and (18)--(19) for every nonzero allocation with

```text
1 <= r <= 7,
0 <= n_j <= 3.
```

It covered 21,837 allocation vectors.  The replay is supporting evidence;
the proof above is universal.
