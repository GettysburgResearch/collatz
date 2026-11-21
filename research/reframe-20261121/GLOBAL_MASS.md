# Global mass attempt: continuous weights, exact Green functions, and compression

**Full Collatz closure: OPEN.** The new results in this lane are proposed
paper proofs, with an exact rational replay for one compressed-weight
obstruction. They have not been formalized in Lean. They do not exclude an
actual nonperiodic component or a nontrivial positive cycle.

This pass stepped back from individual marked families. It attempted to
close the ordinary spectral route, first by a Hilbert-space renormalization
that preserves every hypothetical escape witness, then by an exact
source-dependent Green weight. The first attempt is ruled out for an entire
class of continuous ternary weights. The second produces a norm-one
contraction with an exact norm-loss identity, but necessarily loses
square-summability of the witness. A
compressed Green weight retains a concrete unresolved tail inequality;
substantial portions of its parameter range can be ruled out explicitly.

## 1. Source selection and inherited scope

| Frozen source | Interface used here |
|---|---|
| PR143, `41a408e5e617fb4e65142485f6f3ff3e6ef6c408`, `research/pressure-decay-20261031/PROOF.md`, PF-002 | The ordinary derivative operator, its nonperiodic fixed vectors, and the unit-circle eigenfamily |
| Same source, PF-003--005 and `ENERGY.md` | Positive all-one shadows; averaged pressure versus fixed-source spikes; the moment route |
| PR144, `df756794e1d8de5cabff148ef433df505e3b68b4`, `research/pressure-diagonal-20261031/PROOF.md` and `DISSIPATION.md` | The unresolved moment/dissipation estimate, including its treatment of repeated cycles |
| PR155, `92f499b9d340d1ff8cc643c3eef3477d61b477c1`, `research/gemini-dirichlet-global-20261120/FARKAS_DIRICHLET_AUDIT.md` | The ternary averaged factor `3^(alpha-1)/(2^alpha-1)` and the hidden-lift scope warning |
| PR162, `2279da37ac612dbe049777354cdedb3c0aa03282`, `research/creative-closure-20261120/analytic_flow.md` | Why raw Hardy fixed spaces and regularity do not isolate positive escape |
| PR169, `6cb9bfdc828f91576066b0e4a099d47d8144e915`, `research/certificate-renewal-20261121/FIXED_ENDPOINT_SUMMABILITY.md`, ES1--4 | Fixed-target all-time summability and the sharp fifth-power Green bound at exponent four |
| PR171, `2bd243b3e05eaa5543adeb2894637b053c9662ca`, `research/adaptive-closure-20261121/CRITICAL_NEGATIVE_MOMENT_INTERFACE.md` | The remaining arithmetic primitive-endpoint moment |
| PR183, `8659cf62ac685540cadeef320e596c852fbb0959`, `research/band-completion-20261121/mass/RENEWAL_ATTEMPT.md` | Actual source entrance mass is retained through the band; an endpoint count is not a source-mass loss |

The integrated research map and scoped errata were read. This is a targeted
use of the existing interfaces, not a new acceptance verdict on their entire
source packets. In particular the construction of a nonzero escape fixed
vector below uses PR143's inherited simple-orbit reciprocal budget. The new
operator obstruction itself does not use that budget, ordinary density,
external predecessor-density results, or a conjectural Collatz assertion.

### Ordinary map and state space

Throughout this note,

\[
\mathcal O^*=\{n\ge1:n\text{ odd},\ 3\nmid n\},\qquad
U(n)=\frac{3n+1}{2^{a(n)}},\quad a(n)=v_2(3n+1),\quad
d(n)=\frac3{2^{a(n)}}.
\]

The map `U` preserves `O*`. Removing positive odd multiples of three loses
no hypothetical nonperiodic orbit after its first odd step. We write
`J_q(n)=3^q/2^{A_q(n)}` for its actual derivative product, with `J_0=1`.

## 2. The global spectral attempt and its exact test

On ordinary source-indexed sequences put

\[
(Af)(n)=d(n)f(U(n)). \tag{G1}
\]

PR143 identifies a nonzero fixed vector on every hypothetical nonperiodic
merger component `C`:

\[
w_C(n)=\frac{\mathbf1_C(n)}n
\prod_{j\ge0}\frac{3U^j(n)}{3U^j(n)+1}.
\]

The credited reciprocal budget makes this product positive. It also gives
`0<w_C(n)<=1/n` on `C`. An integer clock on an aperiodic component satisfies
`h(U(n))=h(n)+1`, so `z^h w_C` is an eigenvector of `A` with eigenvalue `z`
for every `|z|=1`.

The candidate was to choose a Hilbert weight

\[
\rho(n)=n^s V(n),\qquad s<1,\qquad
V:\mathbb Z_3^\times\longrightarrow(0,\infty)
\text{ continuous}. \tag{G2}
\]

Compactness bounds `V` above and away from zero. Hence all those hypothetical
eigenvectors remain in `ell^2(rho)`, since their weighted squared magnitudes
are at most a constant times `n^(s-2)`. This includes every positive weight
depending on finitely many ternary digits.

If this renormalization made `A` hyponormal, its eigenvectors at distinct
eigenvalues would be orthogonal. Indeed `T*T-TT*>=0` implies
`||(T*-conj(z))f||<=||(T-z)f||`; an eigenvector of `T` is therefore an
eigenvector of `T*` with the conjugate eigenvalue. The unit-circle family
would contradict separability. Thus the candidate really would exclude
nonperiodic components if its operator hypothesis held. It would still
leave positive-cycle exclusion as a separate task.

Under the unitary map `f(n) -> sqrt(rho(n)) f(n)`, the operator becomes

\[
(Wf)(n)=\lambda_n f(U(n)),\qquad
\lambda_n=d(n)\sqrt{\rho(n)/\rho(U(n))}.
\]

For an ordinary target `t`, let

\[
D_\rho(t)=\sum_{U(n)=t}\lambda_n^2.
\]

Then `W*W` is multiplication by `D_rho`, while `WW*` is the rank-one
matrix `(lambda_n lambda_m)` on each inverse fiber. Consequently the exact
hyponormality test is

\[
H_\rho(t):=\sum_{U(n)=t}\frac{\lambda_n^2}{D_\rho(n)}\le1
\quad\text{for every }t\in\mathcal O^*. \tag{G3}
\]

For completeness, Cauchy--Schwarz proves sufficiency on each fiber.
Necessity follows by testing finite fiber vectors
`f(n)=lambda_n/D_rho(n)`: if the finite sum is `S`, the commutator form is
`S-S^2`. An infinite sum greater than one has a finite partial sum greater
than one.

## 3. New obstruction: no positive continuous ternary renormalization works

**GM1 — PROPOSED, complete paper proof.** For every `s<1` and every `V` in
`(G2)`, the actual ordinary operator `W` fails `(G3)` at arbitrarily large
positive ordinary targets. It is not hyponormal.

### Ternary inverse operator

Put `alpha=2-s>1`. For a continuous function on ternary units define

\[
(P_\alpha\phi)(\zeta)=
\sum_{\substack{a\ge1\\2^a\zeta\bmod9\in\{4,7\}}}
\left(\frac3{2^a}\right)^\alpha
\phi\left(\frac{2^a\zeta-1}{3}\right). \tag{G4}
\]

The congruence guard says exactly that the inverse child is a ternary
unit. There are two allowed exponent classes modulo six at every target.
The series converges uniformly, so `P_alpha` preserves continuity and
strict positivity.

Let `mu` be normalized additive Haar measure restricted to
`Z_3^times`. Each allowed inverse branch is the inverse of

\[
u\longmapsto 2^{-a}(3u+1).
\]

This affine map scales that measure by `1/3`. Therefore, exactly,

\[
\int P_\alpha\phi\,d\mu
=\Lambda_\alpha\int\phi\,d\mu,
\qquad
\Lambda_\alpha=\frac{3^{\alpha-1}}{2^\alpha-1}. \tag{G5}
\]

This is an identity of the stated Haar integrals. It makes no claim that
an ordinary transported source population has Haar-distributed hidden lifts.

Set `D=P_alpha V/V`. For an ordinary legal inverse child
`n=(2^a t-1)/3`, the exact edge weight is

\[
\lambda_n^2=
\left(\frac3{2^a}\right)^\alpha
\left(1-\frac1{2^a t}\right)^s\frac{V(n)}{V(t)}. \tag{G6}
\]

Every ternary unit `zeta` admits positive odd integers `t_k` tending to
`zeta` ternarily and to infinity in ordinary size. For such a sequence,
fixed branches in `(G6)` converge and the geometric tails are uniformly
bounded. In addition `D_rho` is uniformly bounded away from zero: two
legal exponents occur among `1,...,6`, and their factors in `(G6)` have a
common positive lower bound. It follows that

\[
D_\rho(t_k)\longrightarrow D(\zeta),\qquad
H_\rho(t_k)\longrightarrow
\frac{P_\alpha(V/D)(\zeta)}{V(\zeta)}. \tag{G7}
\]

The same reasoning bounds `D_rho` above, so all the displayed ordinary
operators and inverse-fiber forms are bounded.

### Equality forced by the integral test

Suppose `(G3)` held outside a finite set. Then `(G7)` gives

\[
P_\alpha(V/D)\le V.
\]

Integrating and using `(G5)` gives

\[
\Lambda_\alpha\int V/D\,d\mu\le\int V\,d\mu,
\qquad
\int VD\,d\mu=\Lambda_\alpha\int V\,d\mu.
\]

Weighted Cauchy--Schwarz, or Jensen under the probability measure
`V dmu / integral(V)`, gives the reverse inequality

\[
\int V/D\,d\mu\ge
\frac{(\int V\,d\mu)^2}{\int VD\,d\mu}
=\frac{\int V\,d\mu}{\Lambda_\alpha}.
\]

Equality is forced. Its equality condition makes `D` constant almost
everywhere, and continuity and full support make it constant everywhere:

\[
P_\alpha V=\Lambda_\alpha V. \tag{G8}
\]

At the ternary unit `zeta=-1`, the legal branch `a=1` fixes `-1`. Its
single positive contribution in `(G8)` gives

\[
\Lambda_\alpha V(-1)\ge(3/2)^\alpha V(-1).
\]

But

\[
\frac{(3/2)^\alpha}{\Lambda_\alpha}
=3(1-2^{-\alpha})>1\qquad(\alpha>1),
\]

a contradiction. This proves GM1.

The point `-1` is used only to contradict an equation forced on a compact
continuous limit. The failed hyponormality is genuinely ordinary: some
limit value in `(G7)` exceeds one, its large positive approximants violate
`(G3)`, and a finite subset of each violating inverse fiber gives an
explicit negative commutator form. No negative orbit is being asserted to
be a positive counterexample.

## 4. Why column normalization gives an isometry but loses the witness

Define

\[
(Bf)(n)=\frac{\lambda_n}{\sqrt{D_\rho(U(n))}}f(U(n)). \tag{G9}
\]

Its inverse-column squared weights sum to one, so `B*B=I`. For the weight
class `(G2)`, each parent has two uniformly positive squared weights at
exponents at most six. Thus every normalized edge probability is bounded
by `1-delta` for some `delta>0` independent of the ordinary target.

The formula for `B^q` along one forward path gives

\[
|(B^q f)(n)|\le(1-\delta)^{q/2}\|f\|_2.
\]

If `f` belonged to every range of `B^q`, its isometric preimages would have
norm `||f||`, and the displayed bound would force every coordinate to be
zero. Thus `B` is a pure isometry, unconditionally, and has no nonzero
unit-circle eigenvector.

This does not contradict a hypothetical escape eigenvector of `W`.
The formal gauge needed to turn it into an eigenvector of `B` satisfies
`g(U(n))=sqrt(D_rho(U(n)))g(n)`. On a nonperiodic component this relation
can be solved algebraically. But for any nonzero formal unit-circle
eigenvector `f` of `B`, the total squared mass on every inverse level of a
fixed target `t` is exactly `|f(t)|^2`. Those inverse levels are pairwise
disjoint, since otherwise `t` would be periodic. Hence its squared norm
is infinite. The normalization has conserved each inverse cutset's mass;
it has not annihilated a positive ordinary component.

## 5. Fixed-target Green decay is already available

To avoid confusing the compact operator in `(G4)` with actual source
accounting, write the ordinary inverse operator as

\[
(\mathcal P_\alpha f)(t)=
\sum_{\substack{n\in\mathcal O^*\\U(n)=t}}d(n)^\alpha f(n).
\]

Its `q`th inverse column is

\[
\mathcal P_\alpha^q1(t)=\sum_{U^q(n)=t}J_q(n)^\alpha.
\]

For every `alpha>1`, put `C_alpha=sum_(n in O*) n^(-alpha)` and

\[
G_\alpha(t)=\sum_{q\ge0}\mathcal P_\alpha^q1(t).
\]

The first-hit/cycle proof of PR169 ES1 extends verbatim to give

\[
G_\alpha(t)\le
\frac{C_\alpha t^\alpha}
 {1-(3t/(3t+1))^\alpha}
\le C_\alpha t^\alpha(3t+1)
\le4C_\alpha t^{\alpha+1}. \tag{G10}
\]

Indeed the first-hit derivative from `n` to `t` is at most `t/n`. A
nonperiodic target is visited at most once. At a periodic target the
derivative around its positive cycle is at most `3t/(3t+1)`, so later
visits form a convergent geometric series. Tonelli includes all sources
and all visits. Thus each fixed inverse column tends to zero with depth;
this pointwise fact is not a new closure result here.

The sharp per-source telescoping estimate in PR169 ES3 likewise extends
to

\[
\sum_{q\ge0}\frac{J_q(n)^\alpha}{U^q(n)^{\alpha+1}}
\le\frac{1}{[1-(3/4)^\alpha]n^\alpha}. \tag{G11}
\]

For clarity, `V_q=J_q(n)^alpha/U^q(n)^alpha` obeys
`V_q-V_(q+1)=V_q[1-(3t/(3t+1))^alpha]` at `t=U^q(n)`.
Concavity of `1-(1+u)^(-alpha)` implies

\[
t[1-(3t/(3t+1))^\alpha]\ge1-(3/4)^\alpha\quad(t\ge1).
\]

Telescoping proves `(G11)`; equality holds at source one. Summing it over
sources gives a finite all-time Green sum with endpoint denominator
`t^(alpha+1)`. At exponent four this is precisely the previously credited
fifth-power mechanism. It does not control the missing smaller endpoint
denominator of the global moment.

### An exact positive weight that really is contractive

Tonelli gives the ordinary resolvent identity

\[
\mathcal P_\alpha G_\alpha=G_\alpha-1. \tag{G12}
\]

At `alpha=2`, choosing the Hilbert weight `rho=G_2` therefore makes `A`
a contraction with each incoming column strictly less than one:

\[
D_\rho(t)=1-1/G_2(t)<1.
\]

In fact its exact norm identity is

\[
\|Af\|_{\ell^2(G_2)}^2
=\|f\|_{\ell^2(G_2)}^2-\|f\|_{\ell^2}^2.
\]

Thus every nonzero vector's norm strictly decreases. There is no uniform
contraction margin: the positive all-one paths make `G_2` unbounded, so
the supremum of the incoming column sums `1-1/G_2(t)` is exactly one.

The Green norm is also exactly `sum_(q>=0) ||A^q f||_2^2`, by Tonelli.
Every coordinate vector has finite Green norm by `(G10)`, so the original
operator's powers tend to zero on a dense set of finitely supported
vectors. This does not imply strong stability on all of `ell^2`: the
positive all-one paths make `||A^q|| >= (3/2)^q`, so the missing uniform
power bound is false, unconditionally.

There is no speculative normality step here. The obstruction is exactly
membership of the original witness. If `Av=zv`, `|z|=1`, and the orbit of
`n_0` is injective, then `G_2(U^q n_0)>=J_q(n_0)^2`, while
`|v(U^q n_0)|=|v(n_0)|/J_q(n_0)`. Consequently

\[
G_2(U^q n_0)|v(U^q n_0)|^2\ge|v(n_0)|^2
\quad\text{for every }q. \tag{G13}
\]

Its norm in this new space is infinite. More generally, every strictly
positive ordinary weight with `mathcal P_2 rho<=rho` has this same loss:
iterate its single-path contribution to obtain
`rho(U^q n_0)>=J_q(n_0)^2 rho(n_0)`. Thus changing the Green forcing to
another positive source function cannot fix the integrability issue while
retaining the same diagonal contraction argument.

## 6. A concrete attempt to compress the Green weight

Instead take

\[
\rho_\theta(t)=G_\alpha(t)^\theta,\qquad 0<\theta<1,
\]

and use the weighted `ell^alpha` norm. By `(G10)`, every original escape
witness bounded by `1/n` remains summable whenever

\[
(\alpha+1)\theta<\alpha-1. \tag{G14}
\]

The desired contraction inequality is the explicit ordinary inequality

\[
\boxed{\quad
\sum_{U(n)=t}d(n)^\alpha
\left(\frac{G_\alpha(n)}{G_\alpha(t)}\right)^\theta\le1.
\quad} \tag{G15}
\]

Concavity alone does not prove it. The available bound is only

\[
\mathcal P_\alpha(G_\alpha^\theta)(t)
\le [\mathcal P_\alpha1(t)]^{1-\theta}
      [G_\alpha(t)-1]^\theta,
\]

and the incoming unweighted factor exceeds one in some residue classes.

### GM2: positive ordinary shadows exclude a full parameter range

**GM2 — PROPOSED, complete paper proof.** Inequality `(G15)` cannot hold
outside any fixed finite range if

\[
\theta<\frac{\alpha\log(3/2)}{(\alpha+1)\log3}. \tag{G16}
\]

The conclusion also holds after multiplying `rho_theta` by any positive
factor bounded above and away from zero, including any finite correction.

For every `q`, the positive unit source
`m_q=6*2^q-1` has an actual all-valuation-one path to `t_q=6*3^q-1`.
Every point is a ternary unit, and the entire path tends to infinity in
ordinary size as `q` grows. If the column inequality held along this
path, its single-path contribution would give

\[
\rho_\theta(t_q)\ge(3/2)^{\alpha q}\rho_\theta(m_q)
\ge(3/2)^{\alpha q}.
\]

But `(G10)` bounds the left side by a constant times
`3^((alpha+1)theta q)`. Condition `(G16)` contradicts that bound.
Bounded positive factors only change the constants.

For `1<alpha<=log(3)/log(2)`, the entire sufficient summability range
`(G14)` lies inside `(G16)`. Thus the low-exponent compression route is
ruled out, including finite corrections to the weight.

### GM3: the unmodified square-pressure compression fails even earlier

At `alpha=2`, the unconditional summability range is `theta<1/3`.
In fact the unmodified weight fails global contraction for every
`0<theta<=1/2`, at the known ordinary target `11`.

The source `7` is a ternary unit, `U(7)=11`, and `d(7)^2=9/4`.
Also `G_2(7)>=1`. The exact source calculation below proves

\[
G_2(11)\le\frac{84589185}{16777216}<\frac{81}{16}. \tag{G17}
\]

Therefore its one inverse edge already gives

\[
\sum_{U(n)=11}d(n)^2
 \left(\frac{G_2(n)}{G_2(11)}\right)^\theta
\ge\frac94 G_2(11)^{-\theta}>1
\qquad(0<\theta\le1/2).
\]

The target `11` is nonperiodic because its actual tail is
`11,17,13,5,1`; hence sources contribute at most one visit to it.
Among positive odd ternary units at most `63`, the sources reaching it
have `(source, first-hit clock, total valuation)` equal to

\[
(7,1,1),(11,0,0),(19,2,4),(25,3,6),(29,1,3),
(37,2,5),(43,5,10),(49,3,7),(59,6,12).
\]

Every other source in that finite set reaches one before visiting `11`.
The sum of their squared derivatives is `68729473/16777216`.
For all remaining odd sources, the first-hit estimate gives the rigorous
tail bound

\[
121\sum_{\substack{n>63\\n\text{ odd}}}n^{-2}
\le\frac{121}{128}.
\]

For example this follows by integrating on the disjoint intervals
`[n-1,n+1]` and using convexity of `x^(-2)`. Adding the two rational
bounds gives `(G17)`. The exact replay and all finite classifications are
in [global_mass_green_certificate.py](global_mass_green_certificate.py).
No floating-point comparison or unbounded convergence test is used.

### The exact tail assertion still open after these tests

For square pressure, GM2 rules out eventual contraction whenever

\[
0<\theta<\theta_*:=\frac{2\log(3/2)}{3\log3}.
\]

The remaining interval `theta_*<=theta<1/3` is nonempty. GM3 rules out
the unmodified weight as a contraction on the entire state space even
there, but it does not rule out an eventual inequality after a finite
range, nor a sufficiently height-dependent modification.

The concrete unfinished assertion is to prove, or refute, `(G15)` for
all sufficiently large ordinary targets for some `theta` in that interval.
If the cutoff's finite states were separately certified to converge, the
inequality together with `(G14)` would exclude a nonperiodic component:
such a component avoids that finite set, and iteration of one positive
path would contradict the finite weighted norm exactly as in `(G13)`.
No such eventual inequality has been established. Positive-cycle
exclusion would still be needed for full Collatz.

## 7. Outcome of the global closure attempt

The ordinary-source route supplies substantially more structure than a
finite residue average: actual Green functions are finite at every target,
their uncompressed weights give exact contractions, and the compressed
weights have an explicit ordinary inverse-column test. Nevertheless the
proof has not obtained a coercive estimate while preserving the original
fixed-source witness in its function space.

GM1 excludes the entire bounded continuous ternary Hilbert renormalization
attempt. Column normalization and exact Green weighting both explain
their loss of integrability by a direct mass calculation. GM2 and GM3
then test a specific arithmetic alternative, rather than assuming its
regularity or contraction. These are structural progress and failed
strengthenings, not a proof of the full theorem. The marked entrance mass
from PR183 remains compatible with the unresolved mass on moving targets;
no step here converts it into actual mass lost at one.
