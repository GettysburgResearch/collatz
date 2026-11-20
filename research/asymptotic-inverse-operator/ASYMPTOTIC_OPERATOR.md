# Exact asymptotic operator blocks and the missing boundary compactness

**Status: DERIVED, source-qualified structural theorem, independently audited. No forward escape
exclusion or Collatz proof is claimed.**

This note computes an operator limit rather than merely asking for an
unspecified contraction. Every escaping component, if one exists, forces
infinitely many asymptotic eigenvalues approaching one. Every finite power
of the operator has essential norm one even if all ordinary orbits are
eventually periodic. Thus a finite-power norm estimate cannot supply the
missing conclusion.

## 1. Inputs and normalization

Let `S` be the positive odd integers not divisible by three. Write

\[
U(x)=\frac{3x+1}{2^{a(x)}},\qquad
J(x)=\frac3{2^{a(x)}},\qquad
c(x)=\frac{3x}{3x+1}.
\]

Use the finite, positive ordinary harmonic trace `H` satisfying

\[
H(t)=\sum_{Ux=t}J(x)H(x).
\tag{1}
\]

Nonunit children have zero trace and are omitted. The source packet gives
the additional facts needed below:

1. `H(t) <= C t` at ordinary targets whose forward orbit is not eventually
   periodic, with an absolute constant.
2. On every ordinary orbit that is not eventually periodic,
   \[
   r(x):=\prod_{j\ge0}c(U^jx)>0,
   \qquad r(U^jx)\longrightarrow1.
   \tag{2}
   \]
   Uniform simple-orbit reciprocal summability supplies (2).
3. Every bounded positive orbit is eventually periodic. This last fact
   follows directly from integrality and deterministic iteration.

The harmonic trace and reciprocal summability are source-qualified inputs,
not established by a finite matrix experiment here. The operator argument
below is elementary once they are given.

Put

\[
m(x)=\frac{H(x)}x,
\qquad
P(t,x)={\bf1}_{Ux=t}\frac{J(x)H(x)}{H(t)}.
\tag{3}
\]

Equation (1) makes `P` a Markov kernel. It runs backwards along ordinary
integer edges. Consider it as an operator on the Hilbert space
`l^2(S,m)`.

## 2. Contraction and the exact adjoint

The unique forward parent of `x` gives

\[
(mP)(x)=c(x)m(x).
\tag{4}
\]

Jensen's inequality and nonnegative summation imply

\[
\|Pf\|_m^2\le\sum_xc(x)m(x)|f(x)|^2\le\|f\|_m^2.
\tag{5}
\]

The first inequality is interpreted first for finitely supported
functions and then by completion. Its adjoint is especially simple:

\[
P^*f(x)=c(x)f(Ux).
\tag{6}
\]

Write `r_n(x)=prod_{j<n}c(U^jx)`. Iteration gives

\[
(P^*)^nf(x)=r_n(x)f(U^nx).
\tag{7}
\]

The positive contractions `(P*)^n P^n` decrease in operator order, so they
have a strong operator limit `A`. Existence of this limit uses no Collatz
conclusion.

The powers `P^n` tend weakly to zero unconditionally. Indeed for two
finitely supported test functions, a forward image from an orbit that is not eventually periodic eventually
leaves the second support, while the coefficient from an eventually periodic source
tends to zero because its product `r_n` does. The contraction bound and
density of finitely supported functions extend this to arbitrary vectors.
Also (5) is strictly below `||f||^2` for each nonzero `f`, because every
`c(x)<1`. Thus there are no eigenvectors of `P` with eigenvalue of modulus
one. These facts still do not imply strong stability.

## 3. Conservative boundary mass and clock classes

Fix an escaping merger component `C`: two states are in the same merger
component when their forward orbits eventually meet, with possibly
different clocks. Let `y_j=U^j(y_0)` be a spine. Define

\[
b(x)=r(x)m(x)\quad(x\in C).
\tag{8}
\]

The identity `r(x)=c(x)r(Ux)`, together with (1), gives exact
conservation:

\[
b(t)=\sum_{Ux=t}b(x).
\tag{9}
\]

Consequently `b(y_j)` is increasing. It is positive and bounded above by
the linear trace bound. Let

\[
b_C=\lim_{j\to\infty}b(y_j)>0.
\tag{10}
\]

The limit is independent of the chosen spine because any two spines in
the component have a common tail. By (2), `m(y_j) -> b_C` as well.

For `x` in `C`, choose a meeting `U^q(x)=y_j` and define its synchronous
level by `ell(x)=j-q`. This integer does not depend on the meeting chosen:
a different meeting advances both clocks by the same amount because the
spine has no repetitions. Let `C_l={x:ell(x)=l}`. Then

\[
\ell(Ux)=\ell(x)+1,
\qquad
\sum_{x\in C_l}b(x)=b_C\quad(l\in\mathbb Z).
\tag{11}
\]

For the second assertion, for sufficiently large `j` take all predecessors
of `y_j` at depth `j-l`. Their total `b`-mass is `b(y_j)` by repeated
use of (9). These sets increase with `j` and exhaust `C_l`. Monotone
convergence proves (11), including the countably infinite predecessor
levels. All levels are nonempty because every unit target has a positive
unit predecessor.

Conservation, the component mass, and backwards spine concentration are
already in the source packet. Equation (11) records the entire level
mass for the operator calculation.

## 4. Computing the strong asymptotic limit

For each escaping component and integer level define

\[
v_{C,l}(x)=r(x){\bf1}_{x\in C_l}.
\tag{12}
\]

These vectors have disjoint supports and belong to `l^2(S,m)`, since

\[
\|v_{C,l}\|_m^2
=\sum_{x\in C_l}m(x)r(x)^2
=\sum_{x\in C_l}b(x)r(x)\le b_C.
\tag{13}
\]

**Theorem A.** The strong limit is exactly the orthogonal block sum

\[
Af=\sum_{C\ \mathrm{escaping}}\sum_{l\in\mathbb Z}
       \frac{\langle f,v_{C,l}\rangle_m}{b_C}\,v_{C,l}.
\tag{14}
\]

It is zero on all eventually periodic basins. Each displayed block is rank one.
Its nonzero eigenvalue is

\[
\lambda_{C,l}=\frac1{b_C}\sum_{x\in C_l}b(x)r(x),
\qquad 0<\lambda_{C,l}<1.
\tag{15}
\]

**Proof.** For a point indicator `1_x`, the function `P^n 1_x` is
supported only at `U^n x`, with value

\[
(P^n1_x)(U^nx)=\frac{m(x)r_n(x)}{m(U^nx)}.
\tag{16}
\]

On an eventually periodic basin, `r_n(x)` tends geometrically to zero after the cycle
is reached, and `m(U^nx)` ranges over finitely many positive values.
Thus the squared norm tends to zero.

On an escaping component, `r_n(x)->r(x)` and
`m(U^nx)->b_C`. Two sources have equal-clock collisions precisely when
they lie in the same synchronous level. In that case their forward
images agree for every sufficiently large clock, and

\[
\lim_n\langle P^n1_x,P^n1_z\rangle_m
=\frac{b(x)b(z)}{b_C}.
\tag{17}
\]

For distinct levels or components the inner product is zero at every
clock. These formulas establish (14) on finitely supported vectors.
The block sum is bounded by one, by (13), so density and the existence of
the strong asymptotic limit extend the equality to the entire space.
The strict bounds in (15) follow from (11) and `0<r(x)<1`.

## 5. Compactness is an exact boundary condition

For `l>=0` the level `C_l` contains `y_l`. Thus

\[
1\ge\lambda_{C,l}
\ge\frac{b(y_l)r(y_l)}{b_C}\longrightarrow1.
\tag{18}
\]

The associated normalized vectors are orthonormal. Hence if any ordinary
escaping component exists,

\[
\|A\|_{\rm ess}=1,
\qquad A\text{ has infinite rank},
\tag{19}
\]

and one is in its essential spectrum, though it is not an eigenvalue.
Conversely, if no such component exists, (14) gives `A=0`. Therefore

\[
\boxed{
A\text{ compact}
\iff A=0
\iff P^n\longrightarrow0\text{ strongly}
\iff\text{every positive ordinary orbit is eventually periodic}.
}
\tag{20}
\]

The quantification over positive odd units suffices: every odd nonunit
maps to a unit in one odd step, and every positive integer has an odd
part. This criterion does not exclude nontrivial positive cycles.

## 6. Why no finite-power operator norm can prove (20)

**Theorem B.** For every fixed integer `n>=1`,

\[
P^n(P^*)^n-I\text{ is compact},
\qquad
\|P^n\|_{\rm ess}=\|P^n\|=1.
\tag{21}
\]

This statement is unconditional given the positive harmonic kernel;
it holds whether or not any orbit escapes.

**Proof.** Equation (7) and the deterministic forward parent give

\[
P^n(P^*)^nf(t)=d_n(t)f(t),
\qquad
d_n(t)=\sum_{U^nx=t}P^n(t,x)r_n(x).
\tag{22}
\]

Thus `d_n(t)` is an inverse-law average of the finite reciprocal product,
and lies in `(0,1]`. Every legal inverse step satisfies

\[
I_a(y)\ge\frac23(y+1)-1.
\]

Every intermediate state of an `n`-step inverse word from `t` therefore
is at least `(2/3)^n(t+1)-1`. For fixed `n`, all its factors `c(x)` approach
one uniformly over every inverse word as `t->infinity`. Hence
`d_n(t)->1`. A diagonal multiplier tending to zero is compact on the
countable weighted Hilbert space, proving the first assertion of (21).
In the Calkin algebra, the image of `P^n` consequently has product with
its adjoint equal to the identity, and has norm one. The contraction
bound gives the ordinary norm assertion as well.

The same conclusion can be seen without Calkin terminology: normalized
point indicators at distinct targets are orthonormal; their adjoint
images under `(P*)^n` have disjoint supports and norms tending to one.
Every compact operator sends that orthonormal sequence to zero in norm.

Consequently `lim_n ||P^n||=0` is not an available route even if Collatz
is true. Strong-limit compactness in (20) is a genuinely different,
nonfinite boundary assertion. Compactness does not pass automatically
through a decreasing strong limit of noncompact operators.

## 7. Exact failure of uniform physical truncations

Let `Q_M` be the orthogonal projection onto states `x <= M`. Its rank is
finite. For every finite integer `M >= 0` and `n >= 1`,

\[
\boxed{\|P^n(I-Q_M)\|=\|(I-Q_M)P^n\|=1.}
\tag{23}
\]

Thus even a time schedule `n=n(M)`, with each value finite, cannot make
either of these tails small in operator norm. This is an unconditional
obstruction to uniform truncation estimates, not evidence for escape.

Here is an explicit bound proving the assertion without computing the
harmonic trace. Put

\[
L_n(t)=(2/3)^n(t+1)-1.
\]

When `L=L_n(t)>0`, every factor in an inverse path obeys
`c(x)>=3L/(3L+1)`. Consequently

\[
d_n(t)\ge\left(\frac{3L}{3L+1}\right)^n
       \ge 1-\frac{n}{3L+1}.
\tag{24}
\]

The last step is Bernoulli's inequality. Let `e_t=1_t/sqrt(m(t))` be
the normalized point indicator. Equation (22) gives
`||(P*)^n e_t||^2=d_n(t)`. If `L_n(t)>M`, every state in the support of
`(P*)^n e_t` exceeds `M`. Therefore

\[
\|(I-Q_M)(P^*)^ne_t\|^2=d_n(t)\longrightarrow1
\quad(t\to\infty).
\]

Taking adjoints proves the first equality in (23). For the other one,
choose `t>M`; then `(I-Q_M)e_t=e_t`, so
`||(P*)^n(I-Q_M)e_t||^2=d_n(t)->1`. The contraction bound supplies the
matching upper bounds. There are arbitrarily large odd unit targets,
so the witnesses exist within the actual arithmetic state space.

Likewise, each finite-time positive operator `A_n=(P*)^nP^n` has
essential norm one. Any approximation of `A_n` by a finite-rank
operator consequently has operator-norm error at least one. There is
no uniform exchange of the physical truncation limit with the strong
asymptotic limit.

The standalone exact checker `verify_operator_controls.py` verifies
(24) on finitely many complete capped inverse trees and checks rational
shift controls with opposite asymptotic behavior. The proof of (24)
for all legal inverse exponents is the algebraic argument above; the
finite replay is not a substitute for that proof.

## 8. Relation to established weighted-shift theory

The general Hilbert-space mechanism is established theory. Under the
unitary change of coordinates `f(x) -> sqrt(m(x)) f(x)`, the operator
`P*` is a weighted shift on the reversed functional graph, with edge
weight

\[
\alpha_x=c(x)\sqrt{m(x)/m(Ux)}.
\]

On an escaping component this graph is a rootless directed tree.
Gehér's Proposition 3.3 in *Asymptotic behaviour and cyclic properties
of weighted shifts on directed trees* computes the asymptotic limit of
the adjoint of such a shift as rank-one blocks on generation classes.
Its infinite products telescope here to

\[
\prod_{j=0}^{\infty}\alpha_{U^jx}
  =r(x)\sqrt{m(x)/b_C}.
\]

This gives precisely (14), after returning to the weighted space.
The arithmetic inputs identify those products and normalize their
level masses; the rank-one block mechanism is not new general operator
theory.

The compactness dichotomy also specializes Gehér's Theorem 1 in
*Positive operators arising asymptotically from contractions*: a
nonzero compact asymptotic limit of a contraction is a finite-rank
projection and comes from an isometric part. The strict inequality in
(5) rules out that part here. The direct proof above records why the
noncompact alternative corresponds to ordinary escaping components.

Primary references:

- György Pál Gehér, *Asymptotic behaviour and cyclic properties of
  weighted shifts on directed trees*, Journal of Mathematical Analysis
  and Applications 440 (2016), 14–32, Proposition 3.3 and equation (3.1).
  [arXiv:1401.5927](https://arxiv.org/abs/1401.5927),
  [DOI](https://doi.org/10.1016/j.jmaa.2016.03.019).
- György Pál Gehér, *Positive operators arising asymptotically from
  contractions*, Acta Scientiarum Mathematicarum (Szeged) 79 (2013),
  273–287, Theorem 1 and Proposition 1.
  [arXiv:1407.1278](https://arxiv.org/abs/1407.1278).

The arithmetic finite-power and physical-truncation estimates (21)–(24)
are included as an explicit Collatz interface. Their usefulness is to
rule out a tempting closure argument. They do not establish the
compactness required in (20).

## 9. Audit boundary and relation to the existing packet

The finite tests and null real supports already available in PR #145
do not prove the compactness in (20). The packet's moving-root spine law
actually describes the persistent rank-one mass that appears in (14).
It is compatible with all fixed-root inverse empirical laws. Its
finite harmonic-test constructions likewise do not provide an estimate
on this strong asymptotic limit.

No argument here establishes compactness of `A`, and no numerical
finite-clock computation could determine it by (21) alone. This is a
structural classification and an obstruction to finite-power norm
approaches, not a completed closure argument.

All repository inputs were inspected at PR #145,
`dd245a712f985909f541590e3f6c179b7ba011e4`:

- `research/native-pressure-20261118/INVERSE-CHAIN.md`;
- `research/native-pressure-20261118/EVERY-DEPTH.md`;
- `research/native-pressure-20261118/ORDINARY-DENSITIES.md`;
- `research/critical-orbit-mellin/SPINE_CLOCK_PROFILE.md`;
- `research/critical-orbit-mellin/HARMONIC_OFFSET_CONE.md`;
- `research/critical-orbit-mellin/STATIONARY_ZERO_FLUX.md`;
- `research/critical-orbit-mellin/TWO_SCALE_TEST.md`;
- `research/unrestricted-cycle-denominator/FINITE_HARMONIC_TESTS.md`.

Conservative component masses and backwards spine concentration are
credited to these sources and their cited canonical-trace antecedents.
No novelty claim is made for general Hilbert-space asymptotic contraction
theory or for the elementary strong-limit existence argument.
