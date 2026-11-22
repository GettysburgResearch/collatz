# Full-source Lp transport and an actual infinite-energy contact transfer

**Status: SOURCE-QUALIFIED written theorems, with an eleven-theorem Lean
arithmetic and quadratic core. Full Collatz remains OPEN.**

The positive result extends the last-contact source estimate to an entire
class of sources on the ordinary integer domain. In particular, the
canonical immigration seed gives full-source, all-frequency Abel and
Cesaro residue formulas in every finite `Lp`, with an explicit error for
truncating original source labels. The critical quadratic residue itself
was already identified in PR183; it is not claimed as new here.

The second result tests the missing stability of the contact operation on
the immigration reference alone. At the concrete, convergent root **17**, its actual inverse
first-contact probability law has **infinite quadratic density energy
relative to the canonical immigration seed**. The input atom has finite
energy. This obstruction uses infinitely many actual incomparable
predecessor branches, not an assumed escaping orbit or a generic graph.

The third result repairs that domain problem. A summable mixture of
**all future-contact layers**, together with the immigration seed, gives
one finite reference on the whole ordinary domain. Against that same
reference, the actual contact reset after any forward clock has a
uniformly bounded density for the original `n^-4` law, an explicit
`O(N^(-1/2))` original-source tail, and strong convergence in every
finite `Lp`. The limit retains exactly the escaping source mass; no
claim that it vanishes is made.

## 1. Exact inputs, maps, and prior ownership

| Source | Frozen head | Input used |
|---|---|---|
| PR185, `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md` | `276be8154f4e867acc0230466b34d9cb224aacf5` | Ordinary harmonic reference, canonical harmonic floor, finite immigration seed, bounded comparison. The same file is retained at the refreshed PR185 head `7889fc680f5ee22237732eccc172b1699ef565da`. |
| PR182, `research/lean-dyadic-descent-20261121/HARMONIC_CAPTURE_BRIDGE.md` | `9dacd610ba7735e89e2e29e4ab01795983317980` | Exact complete Green sum `S d = nu-lambda*h`, including time zero. |
| PR183, `research/profound-step-20261122/operator/WOLD_CHANNELS.md` and `transport/ASYNCHRONOUS_RESIDUE.md` | `68345f60a4f757acb42a69a4ac95910f8ce26163` | Actual clock lags, component capacities, finite-source quadratic residues, and original `n^-4` quadratic residue. |
| PR176, `research/lean-global-resolvent-20261121/overview/whole/ORDINARY_LAST_CONTACT_MEASURE.md` and `LAST_CONTACT_CHANNEL_INTEGRATION.md` | `c83a8459066d8223aefe7fc5f6b75faeea557345` | Almost-sure inverse contact, ordinary first-contact atoms, last-contact measure, and its `L2(eta)` source theorem. |
| PR180, `research/lean-critical-20261122/lean/PotentialCritical.lean` and the pinned `MarkedDensityPotential` dependencies | `cfe70e02f246119a55fb5bf8fd573f148d746beb` | Formal map conventions and the existing arithmetic style for cofinal ordinary inverse ladders. The new ladder ends at 17, and its purpose is the distinct contact-energy obstruction below. |

The infinite analytic premises keep their source qualifications, including
the upstream predecessor-population and canonical-envelope inputs. They
are not installed as Lean axioms.

Let

\[
U(n)=(3n+1)/2^{v_2(3n+1)}.
\]

Let `N` be the positive odd ternary units that are not themselves periodic.
The ordinary mass transport is

\[
(La)(q)=\sum_{n\in N:U(n)=q}a(n),
\qquad S=\sum_{j\ge0}L^j.
\tag{B1}
\]

Transport is killed on entering any periodic state. A source can visit a
retained target at most once. This operator does not exclude additional
cycles. On `N` the imported data satisfy

\[
L\nu=\nu,\qquad
h(q)=G(q)/q,\qquad
0<\gamma/q\le h(q)\le\nu(q)\le A,
\tag{B2}
\]

with fixed `gamma,A>0`. Define

\[
\lambda(q)=\frac{3q}{3q+1},\qquad
d(q)=\frac{h(q)}{3q+1}>0.
\]

The same inputs give `h>=delta*nu`, where `delta=exp(-200/3)`, and the
global antichain budget `sum_{q in B} nu(q)<=A` for every finite
reachability antichain `B`. Increasing unions extend that budget to
countable antichains. This budget is an additional imported fact, not a
consequence of the pointwise bound `nu<=A`. Its source-qualified
derivation uses `nu=h+SLd`, the canonical bound
`sum_{q in B}h(q)<=1/c`, and `||d||_1<=200/(3c)` from the pinned
harmonic-flow source. Each original atom of `Ld` hits an antichain at
most once, so `sum_{q in B}SLd(q)<=||Ld||_1<=||d||_1`. The stated
budget follows with the same `A=203/(3c)`; here `c>0` is the upstream
predecessor-population constant. PR176 also records this ordinary
antichain budget explicitly before constructing its last contacts.

The seed `d` has finite total mass. The precise already proved Green
identity is

\[
\boxed{S d(q)=\nu(q)-\lambda(q)h(q)<\nu(q).}
\tag{B3}
\]

The original sources in (B1)--(B3) are never replaced by endpoint weights.

## 2. An occupation-dominated source theorem in every finite Lp

Let `sigma` be any nonnegative finite source measure on `N` satisfying

\[
S\sigma(q)\le B\nu(q)\qquad(q\in N)
\tag{B4}
\]

for a finite `B>0`. This is an all-time occupation hypothesis on the
**unchanged** source measure. For `1<p<infinity`, take a possibly complex
`f` in `Lp(sigma)` and set `a=sigma*f`. Its total variation is finite by
Holder and finiteness of `sigma`.

Use the ordinary collision norm

\[
\|b\|_{\nu,p}^p
=\sum_{q\in N}\frac{|b(q)|^p}{\nu(q)^{p-1}}.
\tag{B5}
\]

For `0<r<1`, real frequency `theta`, and integer `J>=1`, put

\[
B_{r,\theta}a=\sum_{k\ge0}r^ke^{ik\theta}L^ka,
\qquad
C_{J,\theta}a=\frac1J\sum_{0\le k<J}e^{ik\theta}L^ka.
\]

### Theorem B1: complete-source bounds and uniform tails

\[
\boxed{
(1-r^p)\|B_{r,\theta}a\|_{\nu,p}^p
\le B^{p-1}\|f\|_{L^p(\sigma)}^p,
\qquad
J^{p-1}\|C_{J,\theta}a\|_{\nu,p}^p
\le B^{p-1}\|f\|_{L^p(\sigma)}^p.
}
\tag{B6}
\]

**Proof.** For a source `x` reaching `q`, let `k(x,q)` be its unique
retained hitting clock. Weighted Holder on the actual endpoint fiber gives

\[
\frac{|B_{r,\theta}a(q)|^p}{\nu(q)^{p-1}}
\le
\left(\frac{S\sigma(q)}{\nu(q)}\right)^{p-1}
\sum_{x\to q}\sigma(x)|f(x)|^p r^{p k(x,q)}.
\tag{B7}
\]

Empty fibers give zero. Substitute (B4), sum over targets, and retain each
original source. Before killing its endpoints are distinct, so its
geometric sum is at most `(1-r^p)^(-1)`. This proves the first bound.
Replacing `r^k` by `1_[k<J]` gives at most `J` endpoints per source and
proves the second. Increasing finite source sets and finite clocks prove
the same statements for the complete source, using nonnegative domination.
The same proof applies to every omitted source tail. QED.

In particular, the normalized **norms** are
`(1-r^p)^(1/p) ||B_{r,theta}a||_{nu,p}` and
`J^((p-1)/p) ||C_{J,theta}a||_{nu,p}`. Their differences for `f` and a
finite-source truncation are at most

\[
B^{1-1/p}\|f\mathbf1_{\text{omitted sources}}\|_{L^p(\sigma)},
\tag{B8}
\]

uniformly in `r`, `J`, and `theta`. No bound on the omitted sources'
meeting clocks is required. The finite real quadratic inequality behind
(B7) is `occupation_quadratic_bound` in the Lean module.

### Theorem B2: all-frequency Lp residues

For an escaping ordinary component `C`, PR183 supplies its capacity `C_C`
and an integer coordinate `h_C` satisfying `h_C(Ux)=h_C(x)+1`. Define

\[
A_C(\theta)=\sum_{x\in C}\sigma(x)f(x)e^{-i\theta h_C(x)}.
\]

Then

\[
\boxed{
\lim_{r\uparrow1}(1-r^p)\|B_{r,\theta}a\|_{\nu,p}^p
=\lim_{J\to\infty}J^{p-1}\|C_{J,\theta}a\|_{\nu,p}^p
=\sum_{C\text{ escaping}}
\frac{|A_C(\theta)|^p}{C_C^{p-1}}.
}
\tag{B9}
\]

Both limits are uniform in `theta`.

**Proof.** For finitely many sources, select a common forward tail after
all meetings in each component. Beyond finitely many initial states the
Abel mass at clock-coordinate `l` equals

\[
r^le^{il\theta}
\sum_{x\in C}a(x)r^{-h_C(x)}e^{-i\theta h_C(x)}.
\]

The normalized geometric mean of `nu(q_l)^(1-p)` converges to
`C_C^(1-p)`, since `nu(q_l)` increases to `C_C>0`. The amplitude converges
uniformly in frequency. The finite initial contribution vanishes. For the
Cesaro expression, the interior of the common tail has the complete
amplitude; only a bounded number of endpoint clocks are incomplete.
Those errors vanish after division by `J`. Eventually killed finite
source orbits contribute only finitely many targets and also vanish.

For the complete source, its component mass satisfies

\[
\sigma(C)=\lim_i S\sigma(U^i q)\le B C_C,
\tag{B10}
\]

because those increasing predecessor domains exhaust `C`. Componentwise
Holder therefore bounds the right side of (B9) by
`B^(p-1) ||f||_Lp(sigma)^p`. Applying this bound and (B8) to the omitted
source tail passes the finite-source result to the limit uniformly in
frequency and the clock/discount parameter. The normalized norms are
uniformly bounded by (B6), so convergence of those norms also passes to
their p-th powers uniformly. QED.

At zero frequency, a nonnegative source retains its complete ordinary
component mass. This is no vanishing theorem. It extends PR183's
quadratic source class and PR176's `L2(eta)` boundary argument to
occupation-dominated sources and every finite `p>1`.

## 3. Application to the entire original n^-4 law

By (B3), **sigma=d and B=1** satisfy the theorem on the whole ordinary
domain, including convergent preperiods. The same canonical seed
`a0(q)=h(q)/q=(3+1/q)d(q)` used by PR182 also belongs to this class.

The original positive integers need not start in `N`. Let `pi(n)` be the
first odd ternary unit on the actual trajectory: remove the initial
powers of two, and, only if that odd part is divisible by three, take one
accelerated odd step. Delete sources whose projected unit is periodic,
in accordance with the fixed killing convention. Retain the original law

\[
a(q)=\sum_{n\ge1:\,\pi(n)=q}n^{-4},\qquad q\in N.
\tag{B11}
\]

An explicit reference allocation preserves these original labels. Namely,

\[
\sum_{\pi(n)=q}n^{-2}\le\frac7{q^2}.
\tag{B12}
\]

To check it, write `n=2^k b` with `b` odd. The sources with unit odd part
contribute `(4/3)q^(-2)`. Any remaining `b` is at least three and has
`3b+1=2^e q`, `e>=1`; consequently
`b >= (3/10)2^e q`. Bounding by all positive exponents, even those with
the wrong ternary or parity condition, gives

\[
\sum_{\pi(n)=q}n^{-2}
\le\frac43\left(1+\frac{100}{9}\sum_{e\ge1}2^{-2e}\right)q^{-2}
=\frac{508}{81}q^{-2}<7q^{-2}.
\]

On the other hand (B2) gives

\[
d(q)\ge\frac{\gamma}{q(3q+1)}\ge\frac{\gamma}{4q^2}
\ge\frac\gamma{28}\sum_{\pi(n)=q}n^{-2}.
\tag{B13}
\]

Apply Holder on each complete projection fiber, with allocated reference
`(gamma/28)n^(-2)`. For every finite `p>1`,

\[
\boxed{
\sum_q\frac{a(q)^p}{d(q)^{p-1}}
\le(28/\gamma)^{p-1}\zeta(2p+2).
}
\tag{B14}
\]

If `a_N` retains original labels `n<=N`, precisely the same argument gives

\[
\boxed{
\sum_q\frac{|a(q)-a_N(q)|^p}{d(q)^{p-1}}
\le\frac{(28/\gamma)^{p-1}}{2p+1}N^{-(2p+1)}.
}
\tag{B15}
\]

The integral bound for the final decreasing source series is valid for
every integer `N>=1`. Combining (B6), (B8), and (B15) controls the omitted
original sources uniformly over **all** discounts, clocks, and
frequencies. No original atom is replaced by a power of its current
endpoint. At `p=2`, PR183 already proved the original-source residue and
has a sharper total constant; (B14) does not claim to improve that
constant. The new addition is the general source class, all finite `p`,
and their common allocation argument.

## 4. Why actual contact transfer does not preserve this source class

Let

\[
\mathcal C_2=\{q\in N:V(q)\le2\}
\]

and use the ordinary inverse Markov kernel

\[
K_\nu(q,x)=\mathbf1_{U(x)=q}\frac{\nu(x)}{\nu(q)}.
\tag{B16}
\]

The pinned first-contact theorem says that its first visit to `C2` is
almost surely finite from every root. Write `Gamma(q)` for the support of
that first-contact law. When `q` is outside `C2`, every `x` in `Gamma(q)`
has one actual path to `q`, with all subsequent states through `q`
outside `C2`. Nonperiodicity gives a unique hitting depth. Telescoping
the inverse probabilities gives the exact atom

\[
\boxed{\mu_q(x)=\nu(x)/\nu(q)\quad(x\in\Gamma(q)).}
\tag{B17}
\]

### Every noncontact root has infinitely many first contacts

Every odd unit `q` has infinitely many positive odd unit parents: the
two admissible exponents modulo six repeat indefinitely. Parents from
different exponents are distinct. They are incomparable before reaching
`q`: a trajectory hitting two distinct parents would revisit `q`, contrary
to its nonperiodicity.

The first inverse step into each parent branch has strictly positive
probability by (B2). Almost-sure contact, applied within that branch,
supplies a first-contact endpoint there. Different parent branches give
different endpoints. Therefore

\[
q\notin\mathcal C_2\quad\Longrightarrow\quad
\Gamma(q)\text{ is infinite}.
\tag{B18}
\]

This argument concerns actual integers and the genuine first-contact law;
there is no appeal to an abstract completion or to infinite paths having
ordinary realizations.

### Every first-contact atom has a uniformly positive immigration cost

For every `x` in `N`, not merely contact states, (B2) implies

\[
\boxed{
\frac{\nu(x)^2}{d(x)}
=(3x+1)\frac{\nu(x)^2}{h(x)}
\ge(3x+1)h(x)\ge3\gamma.
}
\tag{B19}
\]

Consequently (B17)--(B19) give

\[
\boxed{
\sum_{x\in\Gamma(q)}\frac{\mu_q(x)^2}{d(x)}=\infty
\quad(q\notin\mathcal C_2).
}
\tag{B20}
\]

For any `J` selected distinct contacts, the partial sum is at least
`3 gamma J / nu(q)^2`. This is an explicit infinite-support failure of
the quadratic domain, despite `mu_q` being a probability measure.

More generally the canonical contact comparison
`nu(x)<=2/(delta*x)` and `h(x)>=delta*nu(x)`, with
`delta=exp(-200/3)`, gives on `Gamma(q)`

\[
3^{p-1}\gamma x^{p-2}
\le\frac{\nu(x)^p}{d(x)^{p-1}}
\le2\,4^{p-1}\delta^{-p}x^{p-2}.
\tag{B21}
\]

Thus (B20) holds for every `p>=2` after replacing the square by the
p-th power and the denominator by `d^(p-1)`. For `1<p<2`, finiteness
depends on the actual contact-height sum `sum x^(p-2)`; no general
finiteness claim in that range is made.

## 5. The obstruction already occurs at the convergent root 17

The actual odd steps are

\[
7\longmapsto11\longmapsto17.
\]

Both gaps equal one. The inverse excessive inequality for the canonical
majorant, and `V>=1`, give

\[
V(17)\ge\frac32V(11)\ge\frac94V(7)\ge\frac94>2.
\tag{B22}
\]

Hence `17` is outside the contact set. It is nevertheless in the known
basin: its shortcut path is

\[
17,26,13,20,10,5,8,4,2,1.
\]

An explicit infinite family of unit parents is

\[
p_j=\frac{34\,64^j-1}{3},\qquad
3p_j+1=17\,2^{6j+1},\qquad U(p_j)=17.
\tag{B23}
\]

Equivalently `p_0=11`, `p_(j+1)=64p_j+21`. They are strictly increasing
positive odd units, and all reach the certified basin of 17. The Lean
module checks this family, its actual odd transition, the path from 17,
and the finite consequence (B22).

The input atom `delta_17` has finite immigration density energy
`1/d(17)`. Its actual inverse first-contact law has infinite energy by
(B20). Therefore the contact operator is **not a bounded operator from
this full-source L2(d) class to itself**. It does not even take this
particular finite-support input into that class.

This is not a counterexample to the forward estimates (B6), nor to
PR176's boundary `L2(eta)` estimate. They use different source measures
and operations. It is the specific missing domain check in an attempted
iteration that would alternate the forward source bound with a
first-contact reset while keeping the same finite source norm.

## 6. Escaping last contacts and the exact regularity boundary

The same argument applies to PR176's canonical last-contact measure
`eta=nu 1_Lambda`. If an escaping component exists, choose any sufficiently
late point on its forward ray so that its whole future avoids `C2`.
Every first contact behind that point is a last contact, and (B18)
supplies infinitely many of them in the same component. Thus

\[
\boxed{
\text{an escaping component exists}
\quad\Longrightarrow\quad
\sum_x\frac{\eta(x)^2}{d(x)}=\infty.
}
\tag{B24}
\]

In contrast, the existing result gives
`sum eta(x)^2/nu(x)=sum eta(x)<infinity`. Finiteness of the boundary
mass and finiteness of immigration density energy are different facts.
The precise switch of reference contributes a cost bounded below at
each contact, and the actual branching makes their number infinite.

Since `eta=0` when there are no escaping components, finite immigration
energy of this particular boundary measure is equivalent, under the
stated analytic inputs, to absence of escaping orbits. It is **not**
established here. The concrete example at 17 shows why a general
first-contact boundedness theorem cannot prove it.

The all-frequency source theorem supplies valid global bounds and complete
source tails; its nonnegative zero-frequency residue still records
escaping component mass. The arithmetic contact obstruction identifies
why a tempting norm-preserving reset fails even in a known convergent
basin. Neither result excludes nontrivial cycles or proves universal
convergence.

## 7. A finite reference that supports every actual forward/contact clock

The obstruction in Section 5 concerns the particular reference `d`.
It can be repaired without an additional path-count exponent or an
assumption that escape is absent. The following construction includes
last contacts in convergent components as well as escaping ones.

### Contact layers and one occupation-dominated reference

For any `q` in `N`, let

\[
\ell(q)=\#\{k\ge1:U^kq\text{ is retained in }N,
                         \ V(U^kq)\le2\}.
\tag{B25}
\]

This counts **strict future** contacts, whether or not `q` is itself a
contact. Every retained forward path has distinct integer states.
Along it `nu` is nondecreasing. If `x` is a future contact of `q`, then

\[
\delta\nu(q)x\le\delta\nu(x)x\le V(x)\le2.
\]

There are at most `2/(delta*nu(q))` distinct positive integers of that
height. In particular the count is finite, and

\[
\boxed{\ell(q)\le\frac2{\delta\nu(q)}.}
\tag{B26}
\]

No effective test for the infinite-future predicate in (B25) is asserted.
Define the contact layers and their measures by

\[
\Lambda_j=\{x\in\mathcal C_2:\ell(x)=j\},
\qquad \eta_j=\nu\mathbf1_{\Lambda_j},\qquad j\ge0.
\tag{B27}
\]

If two distinct contacts are comparable, the earlier one's strict
future contains the later contact and all its strict future contacts.
Their counts therefore differ. Each `Lambda_j` is a global reachability
antichain. Consequently

\[
\sum_x\eta_j(x)\le A,
\qquad
\boxed{S\eta_j(q)=\nu(q)\mathbf1_{\{\ell(q)\le j\}}.}
\tag{B28}
\]

For the Green identity, first contact from `q` hits layer `ell(q)`
almost surely. Every inverse parent `x` of a contact `y` has
`ell(x)=ell(y)+1`. After taking that one inverse step, apply the same
almost-sure first-contact theorem from its endpoint to reach the next
layer. Each inverse parent of a nonperiodic state is nonperiodic, so the
theorem remains applicable, including in convergent components. Repeating
this procedure finitely many times reaches every prescribed layer
`j>=ell(q)` almost surely. Layers below `ell(q)` cannot be reached.
The inverse paths to any one layer are disjoint hitting events, with
telescoping probabilities `nu(x)/nu(q)`. Summing those probabilities
gives (B28). This finite repeated-contact argument supplies no bound on
the hitting time.

The earlier escape measure is `eta=eta_0 1_E`, where `E` is the escaping
domain. In general `eta_0` also contains convergent last contacts.

Choose the positive decreasing weights

\[
c_j=\frac1{\sqrt{j+1}}-\frac1{\sqrt{j+2}},
\qquad \sum_{j\ge0}c_j=1,
\qquad c_j\ge\frac1{2(j+2)^{3/2}}.
\tag{B29}
\]

The sum telescopes. Monotonicity and the lower bound follow, for
example, by writing `c_j=(1/2) integral_{j+1}^{j+2} t^(-3/2) dt`.
Put

\[
\boxed{\kappa=3\delta/4,\qquad
\sigma_*=d+\kappa\sum_{j\ge0}c_j\eta_j.}
\tag{B30}
\]

This is one finite reference, strictly positive everywhere on `N`, with
total mass at most `||d||_1+kappa*A`. Equations (B3) and (B28), and
`lambda*h >= (3/4)delta*nu`, give

\[
\boxed{
S\sigma_*(q)=\nu(q)-\lambda(q)h(q)
       +\frac{\kappa\nu(q)}{\sqrt{\ell(q)+1}}
\le\nu(q).}
\tag{B31}
\]

The square-root term follows by summing the telescoping tail
`sum_{j>=ell(q)}c_j=1/sqrt(ell(q)+1)`. As a local cross-check, every
inverse parent `x` of `q` satisfies
`ell(x)=ell(q)+1_C2(q)`. Harmonicity therefore shows that
`F(q)=nu(q)/sqrt(ell(q)+1)` obeys
`(I-L)F=sum_j c_j eta_j`. The repeated-contact argument above establishes
the complete Green identity, so no unproved zero-boundary remainder is
being inferred merely from this local equation.

All interchanges here are nonnegative sums. Thus Theorems B1--B2 apply
to `sigma_*` with **B=1**. Since `sigma_*>=d`, all original-source
estimates in Section 3 remain valid in this reference as well.

### First contact stays in one layer, with a uniform original-atom bound

Let `mu_q` be the actual first-contact probability law, now including
time zero: when `q` is a contact, `mu_q=delta_q`. Every first-contact
endpoint `x` has

\[
\ell(x)=\ell(q).
\tag{B32}
\]

Indeed the path from `x` to `q` has no intervening contact; if the path
has positive length, `q` is not a contact either. This also covers the
zero-length path. Telescoping still gives `mu_q(x)=nu(x)/nu(q)` on its
support. Therefore

\[
\boxed{\mu_q\le D(q)\sigma_*,\qquad
D(q)=\frac1{\kappa c_{\ell(q)}\nu(q)}.}
\tag{B33}
\]

Along a retained forward path the strict future contact count cannot
increase, while `nu` cannot decrease. Since `c_j` decreases with `j`,

\[
D(U^kq)\le D(q)
\qquad\text{whenever }U^kq\in N.
\tag{B34}
\]

In particular the same bound from the **original** atom controls its
contact law after every forward clock. By (B2), (B26), and (B29),

\[
D(q)\le D_0q^{5/2},\qquad
D_0=\frac{2}{\kappa\gamma}
       \left(2+\frac2{\delta\gamma}\right)^{3/2}.
\tag{B35}
\]

This follows from `ell(q)+2 <= (2+2/(delta*gamma))q` and
`1/nu(q)<=q/gamma`. The elementary distinct-integer count in (B26)
suffices; the sharper `39/40` physical-path count is not an input.
The formerly problematic atom at 17 now has a finite bound (B33),
because its contact layer is explicitly present in `sigma_*`.

### The original n^-4 source has a bounded reset density at every clock

For a nonnegative source `b`, define the genuine inverse contact reset

\[
\Pi b=\sum_{q\in N}b(q)\mu_q.
\]

It preserves total mass on `N`. Apply the actual forward operator first,
with killing at periodic states as before, and write

\[
b_k=\Pi L^k a,\qquad b_{k,N}=\Pi L^k a_N.
\tag{B36}
\]

For the projection in Section 3, `pi(n)<=2n`: a unit odd part is at
most `n`, and a nonunit odd part `b` projects to
`(3b+1)/2^e <= 2b`. Each surviving original atom `n^-4`, still bearing
its original label, therefore contributes at most
`D_0 2^(5/2)n^(-3/2) sigma_*` to every `b_k`. Set

\[
K=2^{5/2}D_0,\qquad M=K\zeta(3/2).
\]

Nonnegative summation and the elementary decreasing-series tail give

\[
\boxed{0\le b_k\le M\sigma_*,\qquad
0\le b_k-b_{k,N}\le2K N^{-1/2}\sigma_*}
\quad(k\ge0,\ N\ge1).
\tag{B37}
\]

There is no restriction on the forward clock `k`. Collisions retain
all contributing original labels. Also
`||b_k-b_{k,N}||_1 <= sum_{n>N}n^(-4) <= 1/(3N^3)`. Combining this
mass bound with (B37) proves, for every finite `p>=1`,

\[
\boxed{
\sum_x\frac{|b_k(x)-b_{k,N}(x)|^p}{\sigma_*(x)^{p-1}}
\le\frac{(2K)^{p-1}}3 N^{-(p+5)/2}.}
\tag{B38}
\]

In particular `sum b_k^p/sigma_*^(p-1) <= M^(p-1)zeta(4)`.
These are bounds for the specified original-source family, not a claim
that `Pi` is bounded on every function in `Lp(sigma_*)`, or that
arbitrarily many alternating resets obey the same estimate.

### Strong finite-Lp convergence in the same reference

For an escaping component `C`, let `a(C)` be its complete original
projected source mass, and retain PR183's capacity `C_C`. Define

\[
\boxed{
b_\infty=
\sum_{C\text{ escaping}}\frac{a(C)}{C_C}\,
                           \eta_0\mathbf1_C.}
\tag{B39}
\]

This formula is now the limit of the **actual** compositions (B36).
For a fixed surviving source in `C`, its forward path eventually has
no further contacts. PR176's ordinary first-contact law then converges
in total variation to `eta_0 1_C/C_C`; the proof uses its increasing
ancestor sets and `nu(U^kq) -> C_C`. A source entering a periodic orbit
is eventually killed and contributes zero. Summing over the unchanged
original labels, dominated by `2n^-4`, yields

\[
\|b_k-b_\infty\|_1\longrightarrow0.
\tag{B40}
\]

The limit obeys `0<=b_infinity<=M sigma_*` by (B37). For
`f_k=b_k/sigma_*` and `f_infinity=b_infinity/sigma_*`, both densities
lie between zero and `M`. Consequently, for every finite `p>=1`,

\[
\boxed{
\|f_k-f_\infty\|_{L^p(\sigma_*)}^p
\le M^{p-1}\|b_k-b_\infty\|_1\longrightarrow0.}
\tag{B41}
\]

The original-label truncation bound (B38) is uniform in the entire
convergent family and passes to its limit. By (B6) and (B31), the
strong convergence (B41) also passes through subsequent normalized
forward Abel and Cesaro transforms, uniformly in their frequencies,
discounts, and clocks. Here (B6) gives the assertion for `p>1`; for
`p=1`, the same assertion follows directly from the triangle inequality
and `||L^j z||_1<=||z||_1`. This statement concerns the explicitly specified
composition; a reset is not a replacement of the original forward
resolvent or its clock phases.

The limit has total mass `sum_{C escaping} a(C)`. Since every actual
escaping integer has positive original source weight, it is zero
exactly when there are no escaping components. The theorem establishes
the common finite reference, uniform densities, tails, and strong
limit; it does **not** establish that this remaining mass is zero.
The reset reuses contact endpoints and omits its inverse hitting
depths. A finite reference for its output therefore supplies no
ordinary-state recurrence theorem. In particular `Pi b_infinity =
b_infinity`, because the limit is supported on contacts. Nontrivial
cycles remain outside the killed domain, as throughout this note.

## 8. Lean scope

`lean/OrdinaryBoundary.lean` has eleven audited public theorems:

- Four statements for the infinite ordinary parent family of 17.
- The explicit convergent shortcut path, the two gap-one edges, and their
  canonical majorant inequality.
- The finite occupation-dominated quadratic inequality.
- The pointwise immigration energy floor, its finite-cardinality sum,
  and the resulting nonsummability of a sequence with that positive floor.

The module imports the existing pinned `MarkedDensityPotential` chain and
standard Mathlib finite-sum/infinite-sum material. All eleven compiled
with Lean 4.34.1 and warnings as errors, using only standard axioms.
The general Lp theorem, infinite contact-support construction, and their
analytic applications remain the written deductions above.
