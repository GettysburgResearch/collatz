# The exact unitary part of ordinary Collatz transport

**Status: written theorem conditional on the explicitly imported ordinary
harmonic reference; not a Lean theorem or a proof of Collatz.** The finite
clock algebra is separately formalized in `ClockLags.lean`. This note
identifies the unitary part of the actual transport operator, rather than
assuming that a spectral theorem removes it.

## 1. Literature motivation and the different operator used here

Neklyudov associates the shortcut map with operators on holomorphic
functions and relates hypothetical exceptional trajectories to special
fixed vectors. Béhani proves hypercyclicity for a related operator without
assuming Collatz. Those results motivate an operator approach, but neither
hypercyclicity nor the absence of particular eigenvectors decides ordinary
absorption. Here the weights are the ordinary harmonic flow constructed in
PR185, and the operator carries actual original-source masses.

The classical Wold decomposition says that an isometry splits into a
unitary part and unilateral shifts. Its unitary subspace is the intersection
of all its ranges. We use that statement as an organizing principle and
identify that intersection directly, including its measure and all clock
offsets. See Eisner--Farkas--Haase--Nagel, Theorem D.29, printed pp.500--501.

## 2. Exact hypotheses, map, and killed states

Let

\[
 U(n)=(3n+1)/2^{v_2(3n+1)}
\]

on positive odd integers. Let `N` be the positive odd ternary units that
are not themselves periodic. A point in `N` may eventually enter a cycle.
Transport is killed when it first leaves `N`. In particular this operator
alone does not exclude nontrivial cycles.

The source-qualified input is PR185 at
`276be8154f4e867acc0230466b34d9cb224aacf5`,
`research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`,
equations (14)--(15). It supplies an actual function on ordinary points,

\[
 0<\nu(q)\le A<\infty,\qquad
 \sum_{\substack{x\in N\\U(x)=q}}\nu(x)=\nu(q)\quad(q\in N).       \tag{W1}
\]

That source's population and canonical-envelope hypotheses remain attached
to this import. No measurable representative is evaluated at an ordinary
point by fiat, and no infinite analytic input is installed as a Lean axiom.
The results below hold for any deterministic countable system satisfying
(W1), with no repeated state before killing and with injective surviving
orbits. Those properties hold by the definition of `N`.

Write

\[
 (La)(q)=\sum_{U(x)=q}a(x),\quad
 \mathcal H=\ell^2(N,\nu),\quad
 (Sf)(x)=\begin{cases}f(Ux),&Ux\in N,\\0,&Ux\notin N.\end{cases}
\]

All terms in a parent sum belong to `N`. Cauchy--Schwarz on a parent fiber
and (W1) make the sums below well defined. Tonelli gives

\[
 \|Sf\|_\nu^2
 =\sum_{q\in N}|f(q)|^2\sum_{Ux=q}\nu(x)
 =\|f\|_\nu^2.                                               \tag{W2}
\]

Thus `S` is an isometry. Its adjoint is

\[
 (Pf)(q)=\frac1{\nu(q)}\sum_{Ux=q}\nu(x)f(x),\qquad
 P=S^*,\quad PS=I.                                          \tag{W3}
\]

For an actual source mass `a`, its density is `a/nu` and
`P^k(a/nu)=L^k a/nu`. Consequently the collision energy is exactly
`E_nu(a)=||a/nu||_nu^2`. This is a coisometry, not an assumed strict
contraction.

## 3. An integer coordinate on every escaping component

Fix an escaping ordinary component `C` and a reference ray
`q_j=U^j(q_0)`. Any `x` in this component has actual finite clocks `i,j`
with `U^i(x)=q_j`. Define

\[
 h_C(x)=j-i\in\mathbb Z.                                     \tag{W4}
\]

This is independent of the chosen meeting. Indeed two meetings `(i,j)` and
`(i',j')` give equality on the reference ray at clocks `i'+j` and `i+j'`;
its injectivity gives `j-i=j'-i'`. Moreover

\[
 h_C(Ux)=h_C(x)+1,\qquad
 h_C(x)=h_C(y)\ \Longleftrightarrow\
 U^k x=U^k y\text{ for some common }k.                        \tag{W5}
\]

The forward implication follows by synchronizing two finite meetings;
the reverse implication follows from (W4). These finite-clock facts are
the content of the Lean lag lemmas. They neither assert a meeting between
arbitrary components nor assume that any escaping component exists.

Put `S_{C,h}={x in C:h_C(x)=h}`. Every integer `h` occurs: positive
coordinates lie on the reference ray, and (W1) supplies a predecessor at
every inverse depth for negative coordinates.

Along the reference ray, (W1) gives
`nu(q_{j+1})>=nu(q_j)>0`. The uniform upper bound gives a finite positive
limit

\[
 C_C=\lim_{j\to\infty}\nu(q_j)\in(0,A].                      \tag{W6}
\]

The limit is independent of the chosen ray because rays in the same
ordinary component eventually coincide with a finite clock offset.

## 4. The mass of every synchronous class is exactly its component capacity

Fix `h in Z`. For `r>=max(h,0)` define the actual inverse front

\[
 F_r=\{x\in N:U^{r-h}x=q_r\}.
\]

The exponent is a nonnegative integer. The sets `F_r` increase with `r`,
their union is exactly `S_{C,h}`, and repeated (W1) gives
`sum_{x in F_r}nu(x)=nu(q_r)`. Monotone convergence therefore proves

\[
 \boxed{\sum_{x\in S_{C,h}}\nu(x)=C_C\quad\text{for every }h\in\mathbb Z.}
                                                                    \tag{W7}
\]

Each class has finite positive mass; the whole escaping component has
infinite mass. This is why replacing the reference by a finite measure
would change the problem.

## 5. Complete identification of the Wold unitary part

Let `H_u=intersection_{k>=0} ran(S^k)`. A vector in `H_u` is zero at every
source that is eventually killed: choose a larger power than that source's
lifetime. It is constant on every `S_{C,h}`: write it as `S^k g` after any
particular synchronous merger time in (W5).

Conversely, suppose a square-summable function is zero at the eventually
killed points and constant, with value `b_{C,h}`, on each `S_{C,h}`.
Equation (W7) gives its norm as `sum_{C,h} C_C |b_{C,h}|^2`. For every
`k`, the function with class values `b_{C,h-k}` has the same finite norm,
and applying `S^k` gives the original function. It therefore belongs to
every range. This proves the exact description

\[
 \boxed{\mathcal H_u\simeq
 \bigoplus_{C\ \mathrm{escaping}}\ell^2(\mathbb Z,C_C).}       \tag{W8}
\]

In these coordinates `S b(h)=b(h+1)` and `P b(h)=b(h-1)`. There is one
bilateral shift for each ordinary escaping component. The orthogonal
complement is the unilateral-shift part from Wold's theorem.

For a finite-energy mass `a`, put
`A_{C,h}=sum_{x in S_{C,h}}a(x)`. Cauchy--Schwarz and (W7) make this
sum absolutely convergent when interpreted for signed or complex masses.
The orthogonal projection of `a/nu` onto `H_u` has the explicit class value

\[
 (\Pi_u(a/\nu))(x)=A_{C,h}/C_C\quad(x\in S_{C,h}).             \tag{W9}
\]

It vanishes on eventually killed points. In particular

\[
 \|\Pi_u(a/\nu)\|_\nu^2
 =\sum_{C,h}\frac{|A_{C,h}|^2}{C_C}.                         \tag{W10}
\]

This reconstructs PR185's fixed-time synchronous energy limit and gives
it an exact operator meaning. It adds no assertion that the right side is
zero. Strong decay `P^k f -> 0` for every `f` is equivalent to absence of
these bilateral summands. In this killed domain that excludes escapes,
while cycle exclusion remains separate.

## 6. The complete boundary-frequency formula

For a finitely supported complex mass `a`, let

\[
 B_{r,\theta}a=\sum_{k\ge0}r^k e^{ik\theta}L^k a,
 \qquad 0<r<1.
\]

The series converges in collision norm because `P` is a contraction.
Define the component amplitude

\[
 A_C(\theta)=\sum_{x\in C}a(x)e^{-i\theta h_C(x)}.
\]

Then

\[
 \boxed{\lim_{r\uparrow1}(1-r^2)\mathcal E_\nu(B_{r,\theta}a)
 =\sum_{C\ \mathrm{escaping}}\frac{|A_C(\theta)|^2}{C_C}.}     \tag{W11}
\]

For finite support the limit is uniform in `theta`. To prove it directly,
choose, in each surviving component touched by the support, a common ray
after all initial meetings. At its sufficiently late point of coordinate
`l`, the mass is exactly

\[
 r^l e^{il\theta}
 \sum_{x\in C}a(x)r^{-h_C(x)}e^{-i\theta h_C(x)}.
\]

There are only finitely many transient points outside these common tails.
Their normalized contribution tends to zero. On each ray the elementary
Abelian mean
`(1-r^2)sum_{l>=l_0}r^{2l}/nu(q_l)` tends to `1/C_C`.
The finite amplitude converges uniformly on the circle. This proves (W11)
without invoking a spectral-gap premise.

There is a useful complete-source extension. If

\[
 \sum_x |a(x)|/\sqrt{\nu(x)}<\infty,                         \tag{W12}
\]

the same formula and uniform convergence hold. For a singleton on an
injective surviving segment, monotonicity of `nu` bounds the normalized
Abel energy by `|a(x)|^2/nu(x)`. The same bound holds before killing.
The triangle inequality makes the normalized norm of any omitted tail
at most `sum_tail |a(x)|/sqrt(nu(x))`, uniformly in `r,theta`.
Finite-support approximation now proves the assertion. Since `nu<=A`,
(W12) also implies absolute summability of `a`, so every component
amplitude is well defined and continuous.

For nonnegative `a`, at `theta=0` all source masses in one ordinary
component add, irrespective of their meeting clocks:

\[
 \mathcal R_a(0)=\sum_C\frac{a(C)^2}{C_C}.                    \tag{W13}
\]

Integrating (W11) over the circle gives (W10), by orthogonality of the
integer lag characters. At other frequencies phases can cancel; at zero
frequency positivity prevents this. The transport companion proves (W12)
for the projection of the original full-support weights `n^{-4}`, as well
as the exact Cesaro version and a separate cycle pole.

## 7. What the literature-inspired attack did and did not close

The construction identifies the entire possible escape contribution of
the actual operator: its Hilbert subspace, class masses, projection, and
boundary-frequency residue. A fixed surviving positive source cannot
disappear from these formulas. General weak stability or absence of
unit-circle eigenvectors would not remove a bilateral shift; it is weakly
stable and has continuous spectrum. A theorem about generic vectors of a
different holomorphic operator likewise supplies no such removal.

The requested global step is now an actual **zero-residue estimate** for
the full positive source, together with the cycle condition retained in
the transport companion. A bound of order `(1-r^2)^{-1}` for the squared
resolvent norm is already compatible with positive (W13); a little-oh
bound would remove it. Neither Wold decomposition nor (W1) proves that
little-oh statement. No such estimate is claimed here.

## Sources and verification boundary

- M. Neklyudov, *Functional analysis approach to the Collatz conjecture*,
  arXiv:2106.11859v9, 1 June 2022, especially Lemma 2.4, Proposition 4.2,
  and Corollary 4.14. [Primary PDF](https://arxiv.org/pdf/2106.11859v9).
  Read directly; its holomorphic operators are not identified with (W3).
- V. Behani, *Linear dynamics of an operator associated to the Collatz
  map*, Proc. AMS 152 (2024), 1191--1206, DOI
  [10.1090/proc/16627](https://doi.org/10.1090/proc/16627).
  [Primary preprint](https://arxiv.org/pdf/2303.03203v1), read directly.
  Its theorem is motivation and a scope check, not a closure input.
- T. Eisner, B. Farkas, M. Haase, R. Nagel, *Operator Theoretic Aspects of
  Ergodic Theory*, GTM272, Springer 2015, Theorem D.29.
  [Author-hosted text](https://www.math.uni-leipzig.de/~eisner/book-EFHN.pdf),
  April 2016 version, inspected at the theorem. The standard Wold statement
  is credited here; (W4)--(W13) are reconstructed for the ordinary system.
- PR185 at the full SHA above supplies (W1) with its displayed quantitative
  population and canonical-envelope prerequisites. PR186 at
  `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493` supplied the literature field
  guide. Neither source is promoted to a fully formalized theorem.

Only the exact finite-clock declarations of `ClockLags.lean` are included
in the Lean audit. The Hilbert-space, infinite-sum, and boundary-limit
arguments in this note are written proofs with the displayed hypotheses.
