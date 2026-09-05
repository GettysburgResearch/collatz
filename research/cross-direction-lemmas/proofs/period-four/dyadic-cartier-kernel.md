# Dyadic characteristic-two reduction: Cartier product, solved scalar kernel, and transfer frontier

Date: 2026-07-22

Status: scratch-only theorem checkpoint.  The identities and kernel theorem
below hold for every `u`.  They do **not** by themselves prove the full
Newton-model conjecture: one explicitly displayed type-C transfer valuation
remains open.  The shared repository was not edited.

## 1. Set-up

Let

\[
 A_u(t)=\sum_{k=-u}^{u+1}(-1)^k q^{5\binom{k}{2}}
 {2u+1\brack u+k}_q t^{u+k}.
\]

Its derivative at `t=1`, divided by `(q;q)_u`, is the target quotient
`Q_u^(5)` up to a harmless sign.  Work in characteristic two and put

\[
 x=q+1,\qquad s=q^4=1+x^4.
\]

All powers of `q` and `s` below are units in the local Laurent-series ring.

## 2. Exact diagonal-product representation

Write `N=2u+1` and `v=u+k`.  The elementary identity

\[
 \binom{v-u}{2}=\binom v2-uv+\binom{u+1}{2}
\]

and the finite q-binomial theorem give

\[
 A_u(t)=q^{5\binom{u+1}{2}}
 \sum_{v=0}^{N}s^{\binom v2-uv}f_{u,v}t^v,                 \tag{1}
\]

where the coefficients `f_(u,v)` are defined by the centered product

\[
 F_u(z):=\sum_v f_{u,v}z^v
 =\prod_{i=-u}^{u}(1+zq^i).                                \tag{2}
\]

Indeed, the usual product has coefficient
`q^(binom(v,2))[N choose v]_q`; centering its indices subtracts `uv`,
while the remaining `4 binom(v,2)-4uv` is exactly the power of `s` in
(1).

Since differentiation in characteristic two retains precisely the odd
degrees, the numerator

\[
 H_u:=(q;q)_uQ_u^{(5)}\pmod2
\]

is, up to a monomial unit,

\[
 \boxed{H_u\doteq
 \sum_{v\text{ odd}}s^{\binom v2-uv}f_{u,v}.}              \tag{3}
\]

Here and below `doteq` means equality up to a power of `q`, which never
changes an `x`-adic order.

Reflection of the factors in (2) now gives the decisive type-C form

\[
 \boxed{F_u(z)=(1+z)\prod_{j=1}^u
 \bigl(1+(q^j+q^{-j})z+z^2\bigr).}                         \tag{4}
\]

This is an exact identity, not an approximation.

## 3. Exact elementary-symmetric/scalar decomposition

Put

\[
 h_j=q^j+q^{-j},\qquad
 E_{u,r}=e_r(h_1,\ldots,h_u).
\]

Choose the linear term from a set `R` of the quadratic factors in (4),
the quadratic term from a disjoint set `T`, and choose the central `z`
exactly when needed to make the total degree odd.  If `r=|R|`, the actual
odd degree is `r+1+2|T|` when `r` is even and `r+2|T|` when `r` is odd.
Now use the reflection `v -> 2u+1-v`: the exponent
`binom(v,2)-uv=-v(2u+1-v)/2` is reflection-invariant, and complementing
`T` among the `u-r` unused quadratic factors preserves the coefficient.
After this reflection the degrees are

\[
 a_r=2\lceil r/2\rceil
\]

before the `2|T|` contribution.  Consequently (3) becomes

\[
 \boxed{H_u\doteq\sum_{r=0}^u E_{u,r}
 K_{u-r,a_r;u}(s),}                                        \tag{5}
\]

where

\[
 K_{M,a;b}(s)=\sum_{t=0}^{M}{M\choose t}
 s^{\binom{a+2t}{2}-b(a+2t)}\quad\text{in }\mathbb F_2[s^{\pm1}]. \tag{6}
\]

Thus all of the diagonal deformation has been separated into a scalar
kernel depending only on `(M,a,b)`, and all dependence on the centered
q-lattice lies in the type-C elementary symmetric functions `E_(u,r)`.

## 4. Solved scalar-kernel theorem

The scalar kernel has an unexpectedly rigid order.

> **Theorem.**  For every `M>=0`, every even integer `a`, and every integer
> `b`,
> \[
> \boxed{\operatorname{ord}_{s=1}K_{M,a;b}(s)=M.}           \tag{7}
> \]
> Its normalized leading coefficient is one in `F_2`.

It is useful to prove the slightly more general statement

\[
 \sum_{t=0}^{M}{M\choose t}s^{2t^2+Bt+C},\qquad B\text{ odd},          \tag{8}
\]

whose order at one is `M`.  Formula (6) has precisely this shape because
`a` is even.

Write the binary expansion `M=sum_i L_i`, where the `L_i` are distinct
powers of two.  Lucas's theorem restricts `t` in (8) to subset sums of the
`L_i`.  Apart from the unit `s^C`, the resulting sum is

\[
 \sum_{S}\prod_{i\in S}A_i
             \prod_{i<j\in S}B_{ij},                       \tag{9}
\]

with

\[
 A_i=s^{L_i(2L_i+B)},\qquad B_{ij}=s^{4L_iL_j}.             \tag{10}
\]

Put `z=s+1`.  Since `2L_i+B` is odd,

\[
 \operatorname{ord}_z(1+A_i)=L_i.                          \tag{11}
\]

If every interaction `B_(ij)` in (9) is replaced by one, the sum factors
as `prod_i(1+A_i)` and has order `sum_i L_i=M`, with leading coefficient
one.

Expand every interaction as `1+(1+B_(ij))`.  A nonempty interaction graph
`G`, with incident vertex set `V(G)`, contributes order at least

\[
 \sum_{ij\in E(G)}4L_iL_j+\sum_{i\notin V(G)}L_i.           \tag{12}
\]

For distinct positive powers of two,
`4L_iL_j>L_i+L_j`.  Summing this strict inequality over the edges shows
that (12) is strictly larger than `sum_i L_i=M`.  Hence no interaction
term can alter the unique order-`M` term.  This proves (7).

Because `s+1=x^4`, every scalar state in (5) therefore contributes the
known factor

\[
 \operatorname{ord}_x K_{u-r,a_r;u}=4(u-r).                \tag{13}
\]

## 5. Exact one-parameter transfer recurrence

Define the odd and even phase states

\[
 \begin{aligned}
 O_u(c)&=\sum_{v\text{ odd}}s^{\binom v2+cv}f_{u,v},\\
 E_u(c)&=\sum_{v\text{ even}}s^{\binom v2+cv}f_{u,v}.
 \end{aligned}                                             \tag{14}
\]

Then `H_u` is the state `O_u(-u)` up to a q-unit.  Multiplication by the
last factor `1+h_u z+z^2` in (4) gives the exact two-state recurrence

\[
 \boxed{\begin{aligned}
 O_u(c)&=O_{u-1}(c)+h_us^cE_{u-1}(c+1)
                 +s^{2c+1}O_{u-1}(c+2),\\
 E_u(c)&=E_{u-1}(c)+h_us^cO_{u-1}(c+1)
                 +s^{2c+1}E_{u-1}(c+2).
 \end{aligned}}                                            \tag{15}
\]

The palindromicity of `F_(u-1)`, whose degree is `2u-1`, eliminates the
even state.  Reindexing the middle term by `v -> 2u-1-v` gives the
termwise odd-state identity

\[
 O_u(c)=\sum_{v\text{ odd}}f_{u-1,v}s^{\binom v2+cv}
 \left(1+s^{2v+2c+1}
 +h_us^{(u-v)(2u+2c-1)}\right).                             \tag{16}
\]

This is the smallest exact induction frontier now known: there is only one
phase family, and the bracket is explicit.  Its coarse order is transparent:
it has `x`-order two when `u` is odd and at least four when `u` is even.
The exceptional cancellation at `u=2r` with `r` odd is exactly the source
of the later `4,8,16,...` clusters; it is no longer hidden inside a
Gaussian polynomial.

Exact state scans suggest the stronger uniform invariant

\[
 \operatorname{ord}_xO_u(c)=\operatorname{ord}_xE_u(c)
 =W_2(u)+m_u                                                   \tag{17}
\]

for every integral `c`, where

\[
 m_u=u+\lfloor u/2\rfloor
 +2\left(2^{\nu_2(\lfloor u/2\rfloor+1)}-1\right).          \tag{18}
\]

Formula (17) is verified broadly but is **not claimed as a theorem here**.
Proving it from (15) or (16) would settle the mod-two half of the dyadic
Newton criterion.

## 6. Dickson structure of the remaining type-C state

Let `y=q+q^(-1)`.  In characteristic two,

\[
 h_j=D_j(y),\qquad D_{2j}(y)=D_j(y)^2,                       \tag{19}
\]

where `D_j` is the Dickson/Chebyshev polynomial determined by
`D_0=0`, `D_1=y`, `D_(j+1)=yD_j+D_(j-1)`.  For odd `j`,

\[
 D_j(y)=y\,U_j(y^2),\qquad U_j(0)=1.                         \tag{20}
\]

Therefore

\[
 \boxed{\operatorname{ord}_x h_j=2^{\nu_2(j)+1}.}           \tag{21}
\]

This gives a recursive Frobenius split of the elementary generating
polynomial:

\[
 \prod_{j=1}^u(1+h_jz)
 =\left(\prod_{j=1}^{\lfloor u/2\rfloor}(1+h_j^2z)\right)
  \left(\prod_{j\le u,\ j\text{ odd}}(1+yU_j(y^2)z)\right). \tag{22}
\]

The monomial shadow

\[
 \prod_{j=1}^u\left(1+y^{2^{\nu_2(j)}}z\right)              \tag{23}
\]

reproduces the exact leading order and leading bit of every tested
`E_(u,r)`.  For the complete block `u=2^k-1`, (23) gives the particularly
simple profile

\[
 \operatorname{ord}_yE_{2^k-1,r}=2^{k-1}s_2(r).             \tag{24}
\]

Equations (23)--(24) remain a proved target only after the required strict
unit-perturbation induction is supplied; they are recorded here as the
most structured route into (17), not as completed theorems.

## 7. Binary arithmetic of the Newton cluster model

Let `n=floor(u/2)` and

\[
 \mathcal E(n)=\{e=2^r\ge4:n\bmod e\ge e/2-1\}.             \tag{25}
\]

This is the same set as the one in the Newton checkpoint.  It obeys the
exact recurrences

\[
 \begin{aligned}
 \mathcal E(2a)&=\{4\cdot2^j:\text{bit }j\text{ of }a\text{ is }1\},\\
 \mathcal E(2a+1)&=\{4\}\cup\{2e:e\in\mathcal E(a)\}.
 \end{aligned}                                              \tag{26}
\]

The first line follows by dividing the defining inequality by two; the
second follows in the same way, with the `e=4` case separated.  Immediate
induction gives

\[
 |\mathcal E(n)|=s_2(n),\qquad
 \sum_{e\in\mathcal E(n)}e
 =2n+2\left(2^{\nu_2(n+1)}-1\right).                        \tag{27}
\]

The largest member is the least power of two strictly greater than `n+1`.
Consequently, for `d` the least power of two above `u`, this largest member
equals `d` exactly at `u=d-2,d-1`.  Those two families are already closed
by the independent boundary theorem.

## 8. What is proved and what remains

Proved here for all orders:

1. the characteristic-two diagonal product (1)--(4);
2. the elementary-symmetric/scalar separation (5)--(6);
3. the complete scalar-kernel order theorem (7);
4. the exact one-parameter transfer recurrences (15)--(16);
5. the Dickson/Frobenius structure and individual orders (19)--(22);
6. the binary cluster recurrences and formulas (26)--(27).

Still open:

1. prove the uniform transfer valuation (17), equivalently the first odd
   Taylor coefficient formula for `Q_u^(5)`;
2. lift the transfer one level to mod four through degree `m_u-d`.

The first remaining item is now a finite-characteristic transfer theorem,
not an unstructured finite-Jacobi cancellation problem.


