# Exact factorization of the ordinary and critical harmonic kernels

**Status:** complete written operator deduction from the retained-path
occupation bound and the strict-Green theorem in
`STRICT_GREEN_VOLTERRA.md`. The statements here are not Lean declarations.
They do not assert a spectral gap or Collatz convergence.

The strict-Green inverse does more than identify the previously
constructed canonical pair of functions. It identifies the entire
ordinary and critical stationary kernel spaces, on their exact maximal
domains. At the critical parameter it is an order isomorphism of their
positive cones. The unsmoothed transport is allowed to be unclosable
throughout the argument.

## 1. Space, maximal domains, and the bounded column

Let `N` be the positive odd ternary units that are not themselves
periodic under the actual accelerated Collatz map `U`. Forward transport
is killed on first entering a periodic state. Put

\[
\theta=\frac{39}{40},\qquad \theta<s\le1,\qquad
X_s=\ell^1(\mathcal N,n^{-s}),\qquad
\omega(n)=\frac1{3n+1},\qquad (Da)(n)=\omega(n)a(n).
\]

All spaces and operators in this note may be complex. Define the maximal
ordinary transport domain by

\[
\begin{split}
\mathcal D(L)=\{a\in X_s:;&
 \sum_{U(n)=q}|a(n)|<\infty\text{ for every }q\in\mathcal N,\\
&q\longmapsto\sum_{U(n)=q}a(n)\text{ belongs to }X_s\}.
\end{split}
\tag{1}
\]

On this domain, `(La)(q)=sum_(Un=q)a(n)`. It is a linear domain;
no closedness, closability, or Banach graph-domain property is assumed.

The unweighted space `ell^1(N)` is contained in `D(L)`, because a source
has at most one retained forward image, so ordinary transport is a
contraction on that unweighted space. Also

\[
\|Da\|_{\ell^1}
=\sum_n |a(n)|n^{-s}\frac{n^s}{3n+1}
\le\frac13\|a\|_s.
\tag{2}
\]

Thus `D:X_s->ell^1(N)` is bounded, and in particular

\[
\boxed{D(X_s)\subseteq\mathcal D(L).}
\tag{3}
\]

Set `B=LD`. It is a bounded operator `X_s->X_s`, also taking values
in unweighted `ell^1`. The exact weighted column is

\[
B\delta_n=
\begin{cases}
\omega(n)\delta_{U(n)},&U(n)\in\mathcal N,\\
0,&\text{otherwise}.
\end{cases}
\]

Since a retained target is a positive integer,

\[
\frac{\|B\delta_n\|_s}{\|\delta_n\|_s}
=\frac{n^s}{3n+1}\,U(n)^{-s}\le\frac13
\]

for a retained column; a killed column has ratio zero. Hence

\[
\boxed{\|B\|_{X_s\to X_s}\le\frac13,
\qquad \|Ba\|_{\ell^1}\le\frac13\|a\|_s.}
\tag{4}
\]

For `z in C`, define the physically weighted transport

\[
(T_za)(q)=\sum_{U(n)=q}(1-z\omega(n))a(n)
\]

on its own natural maximal domain: its parent sums must converge
absolutely and its output must belong to `X_s`. By definition this is
equivalent to `(I-zD)a in D(L)`. Equation (3) and linearity of `D(L)`
give

\[
(I-zD)a\in\mathcal D(L)
\quad\Longleftrightarrow\quad a\in\mathcal D(L).
\]

Therefore

\[
\boxed{\mathcal D(T_z)=\mathcal D(L),\qquad
T_z=L-zB\text{ on that domain}.}
\tag{5}
\]

This proof does not invert `I-zD`. That multiplier can vanish at a
coordinate, for example when `z=3n+1`; (5) remains valid.

## 2. The strict Green correction maps into the transport domain

Use the strict Green operator and its entire inverse from the companion
theorem:

\[
K=SLD=\sum_{j\ge1}L^jD,\qquad
R(z)=(I+zK)^{-1},\qquad
\|K\|\le A_s:=\frac{5s}{3(s-\theta)}.
\tag{6}
\]

The sum in (6) has the exact physical-path kernel

\[
Ka(q)=\sum_{n\prec q}\omega(n)a(n),
\]

where `n≺q` means a positive retained hitting depth. Each source-target
pair has at most one such depth.

For `a>=0`, nonnegative summation removes the one-step term when the
Green column is shifted:

\[
LKa=Ka-Ba.
\tag{7}
\]

This is a domain statement as well as a formal identity. The right side
is nonnegative and bounded above by `Ka`; hence it is pointwise finite
and belongs to `X_s`. For arbitrary complex `a`, apply this argument to
`|a|`. It shows absolute convergence of every parent sum for `Ka`,
since `L|Ka|<=LK|a|<=K|a|`. Fubini is then justified and gives (7).
Consequently

\[
\boxed{K(X_s)\subseteq\mathcal D(L),\qquad
LK=K-B\text{ on all }X_s,\qquad \|LK\|\le A_s.}
\tag{8}
\]

In particular `K` is bounded into the algebraic graph domain equipped
with `||a||_s+||La||_s`, with bound `2A_s`. Completeness of that graph
norm is neither asserted nor needed.

## 3. Domain automorphisms and the right factorization

Write `F_z=I+zK`. Equation (8) implies
`F_z(D(L)) subset D(L)`. The inverse satisfies the bounded-operator
identity

\[
R(z)=I-zKR(z).
\tag{9}
\]

Because `KR(z)` takes all of `X_s` into `D(L)`, (9) gives
`R(z)(D(L)) subset D(L)` as well. Thus

\[
\boxed{F_z:\mathcal D(L)\longrightarrow\mathcal D(L)
\text{ is a bijection with inverse }R(z).}
\tag{10}
\]

All expressions in the following calculation are now defined. For
`a in D(L)`, (8) yields

\[
\begin{aligned}
(I-L)(I+zK)a
&=a-La+zKa-zLKa\\
&=a-La+zBa\\
&=(I-T_z)a.
\end{aligned}
\]

Hence the exact operator statement is

\[
\boxed{I-T_z=(I-L)(I+zK)
\quad\text{on the common maximal domain }\mathcal D(L).}
\tag{11}
\]

It follows immediately that

\[
\boxed{
\ker(I-T_z)=R(z)\ker(I-L),\qquad
\operatorname{Ran}(I-T_z)=\operatorname{Ran}(I-L).}
\tag{12}
\]

The kernel equality is an isomorphism of linear spaces; either dimension
may be infinite. The range equality is equality of actual subsets of
`X_s`, not merely equality after closure. More generally, the equation
`(I-T_z)a=b` is equivalent to `(I-L)u=b` through `u=F_z a`.

Equation (11) is a **right factorization**. It is not a conjugacy
`T_z=F_z^(-1) L F_z`, and it proves no equality of the whole spectra of
the two transports. In particular, an entire inverse for `I+zK` is not
an inverse for `I-L` or for `I-T_z`.

## 4. An order isomorphism at the critical parameter

At `z=1`, write

\[
\lambda(n)=1-\omega(n)=\frac{3n}{3n+1},\qquad T=T_1.
\]

The retained actual-path estimate used in the companion theorem gives

\[
\delta\le\prod_{i=0}^{k-1}\lambda(U^i n)\le1,
\qquad \delta=\exp(-200/3),
\tag{13}
\]

on every retained finite path. This is a physical path bound, with no
random replacement of the states.

For a finite source mass `eta>=0`, let `S_T eta=sum_(j>=0)T^j eta`.
The positive critical path kernel is dominated by the ordinary kernel,
so `S_T:ell^1->X_s` is bounded with norm at most
`C_s=5s/(s-theta)`. Exact source-path coefficients give

\[
\boxed{R(1)=I-S_TB\text{ on }X_s.}
\tag{14}
\]

Indeed, the coefficient of `S_TB` from `n` to `q` is
`omega(n)` times the product of `lambda` over the interior states of
the unique strictly positive path. This is precisely the negative
off-diagonal term in the strict-Green inverse. The source `Ba` is in
unweighted `ell^1` by (4), so the countable sums are absolutely
controlled even when `a` has infinite unweighted total mass.

In particular the special positive-parameter bound improves to

\[
\boxed{\|R(1)\|\le1+A_s.}
\tag{15}
\]

Now let `nu>=0` belong to `X_s` and satisfy `Lnu=nu`. Every iterate
`T^k nu` is well defined, nonnegative and bounded above by `nu`.
Actual inverse-path expansion and (13) give

\[
\delta\nu\le T^k\nu\le\nu.
\]

Moreover `Tnu=nu-Bnu<=nu`, so the sequence decreases. Its norm and
pointwise limit exist by domination by `nu in X_s`. The finite identity

\[
\nu-T^k\nu=\sum_{j=0}^{k-1}T^jB\nu
\]

and (14) identify the limit exactly as `R(1)nu`. Thus

\[
\boxed{\delta\nu\le R(1)\nu\le\nu
\quad(\nu\ge0,\ L\nu=\nu,\ \nu\in X_s).}
\tag{16}
\]

Conversely, if `h>=0` is in `X_s` and `Th=h`, then (11) shows that
`nu=(I+K)h` is ordinary harmonic, and it is positive because `K` is
positive. Consequently

\[
\boxed{
I+K:\ker(I-T)\cap X_s^+\ \longleftrightarrow\
\ker(I-L)\cap X_s^+
\text{ is an order isomorphism},}
\tag{17}
\]

with inverse `R(1)` and comparison `h<=nu<=delta^(-1)h`.
Positivity in (16)–(17) concerns these harmonic cones. The inverse is
not asserted positive on every positive input in `X_s`.

## 5. Escape labels are preserved, with their physical sources

Let `E` be the set of nonperiodic states whose forward orbit never
enters a periodic orbit. This is a mathematical predicate, not a
recognition algorithm. If `n` reaches `q`, then `n in E` if and only
if `q in E`. Therefore multiplication `P_E a=1_E a` commutes with
the physical-path kernel `K`, and hence with every `F_z` and `R(z)`.

The same statement holds for any union of ordinary components. In
particular, for an ordinary positive harmonic flow `nu`,

\[
\boxed{
R(1)(\nu\mathbf1_E)=(R(1)\nu)\mathbf1_E
\ge\delta\nu\mathbf1_E.}
\tag{18}
\]

A nonzero escaping harmonic sector is therefore carried to a nonzero
critical sector. The weighted-space correction and its entire inverse
do not merge different ordinary components or turn a surviving original
source into an absorbed one.

The contact-return finite reference gives additional quantitative
control on visits before the last contact; its terminal escape flux
is accounted for separately in `CONTACT_EXIT_ACCOUNTING.md`.
Equations (12), (16), and (18) explain the exact result of combining the
two attacks: the correction interface is fully invertible, while the
stationary channel that a convergence argument must eliminate remains
present with a uniform positive comparison.
