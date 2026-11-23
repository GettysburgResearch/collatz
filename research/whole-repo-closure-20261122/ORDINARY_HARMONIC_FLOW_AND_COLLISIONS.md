# An ordinary harmonic reference with exact retained-source collision accounting

**Status: source-qualified written analytic deductions. These are not Lean declarations and do not prove Collatz convergence.**

This packet combines the newest canonical-potential comparisons with the actual ordinary inverse tree. It constructs a canonical ordinary harmonic flow, compares its path law with the critical inverse Doob law, and proves a uniform collision-energy contraction for unchanged original source masses. It also computes the exact surviving one-atom energy, so the remaining obstruction is stated quantitatively.

The harmonic reference has **infinite total mass**, provably even on a known convergent predecessor basin. A finite-reference estimate cannot be inferred from its collision contraction.

## 1. Frozen inputs and the domain

The repository is `GettysburgResearch/collatz`. The dependency ledger is `SOURCES.json` beside this note. The relevant exact source heads are:

| PR | Commit | Used result |
|---|---|---|
| 175 | `2bc2ad37b490a5aea63658eaf657bc048da4532e` | Canonical antichain and moment bounds, the corrected finite-chain count, and actual-path multiplicative corrections. |
| 176 | `41dc0ff039c13eeaf7f130c56a290212c00bcdef` | Common domination of all finite-depth and Abel densities by the finite canonical envelope; critical limits and their comparison. |
| 180 | `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d` | Canonical stationary normalization and the every-ordinary-point comparison between the least envelope and its harmonicization. |
| 186 | `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493` | The retained-source collision interface and its finite-reference qualification; research guidance, not an extra analytic hypothesis. |

The earlier ordinary harmonic correction is recorded in PR185's `CANONICAL_FINITE_SPINE_CONCENTRATION.md`. The proof below reconstructs that correction and supplies its quantitative comparison, exact change of path law, and collision consequences.

Let

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}
\]

on positive odd integers. Write `N` for the positive odd ternary units that are **not themselves periodic**. A state in `N` may later enter a cycle. Every unit predecessor of a state in `N` also belongs to `N`.

All operators in this note use this domain. Forward transport is killed when a source first leaves `N`, that is, when it first enters any periodic odd orbit. This is a mathematical separation of escape from cycles; it is not a procedure for deciding periodicity, and it does not rule out a nontrivial cycle.

For `q` in `N`, define

\[
\operatorname{Pred}(q)=\{n\in N:U^j(n)=q\text{ for some }j\ge0\},
\qquad
(Lf)(q)=\sum_{\substack{n\in N\\U(n)=q}}f(n).
\tag{1}
\]

This `L` is ordinary inverse counting, with no slope coefficient.

### Imported quantitative hypotheses

Let `c>0` be the constant in the source-qualified uniform unit-predecessor population. Let `V` be the canonical least excessive majorant of the unit indicator for

\[
(PF)(q)=\sum_{2^e q\equiv1\ (3)}\frac3{2^e}
 F\left(\frac{2^eq-1}{3}\right),
\]

and let `G=lim_j P^jV`. The pinned proofs supply `PG=G`, a constant `gamma>0` with `G>=gamma` on units, and `G<=V`. Put

\[
H(q)=\frac{V(q)}q,\qquad h(q)=\frac{G(q)}q,
\qquad \theta=\frac{39}{40}.
\]

On `N` the following inputs are used:

\[
0<h\le H\le\frac1c,
\qquad
\sum_{q\in A}H(q)\le\frac1c
\tag{2}
\]

for every finite reachability antichain `A`, and

\[
\sum_{q\in N}\frac{H(q)^p}{q^s}
\le\frac{5s}{c^p(s-\theta)}
\qquad(p\ge1,\ s>\theta).
\tag{3}
\]

The finite-chain count in PR175 supplies, without the population hypothesis,

\[
\#\{n\in C:n\le X\}\le5X^\theta
\tag{4}
\]

for any finite collection `C` of distinct nonperiodic unit states on one actual forward path. Therefore, if all its states are at least `m>=1`,

\[
\sum_{n\in C}\frac1n
\le\int_m^\infty5t^{\theta-2}\,dt
=200m^{-1/40}.
\tag{5}
\]

Set

\[
\delta_m=\exp\left(-\frac{200}{3}m^{-1/40}\right),
\qquad \delta=\delta_1.
\tag{6}
\]

The source-qualified status of (2)--(3), including their population and finite-envelope inputs, is retained. These are not new axioms or independently formalized facts in this packet.

## 2. A comparable ordinary harmonic flow

For an actual odd edge `U(n)=q`, let

\[
\lambda(n)=\frac{3n}{3n+1}.
\]

Dividing `PG=G` by the target gives the exact identity

\[
h(q)=\sum_{U(n)=q}\lambda(n)h(n)=L(\lambda h)(q).
\tag{7}
\]

For a path of length `k` write

\[
\Lambda_k(n)=\prod_{i=0}^{k-1}\lambda(U^i n).
\]

Every path ending in `N` is injective. By (5) and `log(1+x)<=x`,

\[
\delta\le\Lambda_k(n)\le1,
\tag{8}
\]

and `delta_m` replaces `delta` when all its states are at least `m`. Iterating (7) yields

\[
h(q)=\sum_{U^k(n)=q}\Lambda_k(n)h(n).
\tag{9}
\]

Define the nonnegative immigration

\[
d(n)=(1-\lambda(n))h(n)=\frac{h(n)}{3n+1}.
\]

By (3),

\[
D:=\sum_{n\in N}d(n)
\le\frac13\sum_{n\in N}\frac{h(n)}n
\le\frac{200}{3c}.
\tag{10}
\]

Equation (7) gives `Lh=h+Ld`, so `L^kh` increases with `k`. Define

\[
\nu(q)=\lim_{k\to\infty}L^kh(q).
\tag{11}
\]

Equation (9) and (8) show immediately that this limit is finite and

\[
\boxed{h(q)\le\nu(q)\le\delta^{-1}h(q).}
\tag{12}
\]

There is also the explicit source-sum formula

\[
\boxed{
\nu(q)=h(q)+\sum_{j\ge1}L^jd(q)
=\lambda(q)h(q)+\sum_{n\in\operatorname{Pred}(q)}d(n).
}
\tag{13}
\]

Indeed a fixed source can hit a nonperiodic target at only one depth. Tonelli thus identifies the Green sum with the single sum over distinct ordinary predecessors. Formula (10) gives the useful absolute bound

\[
\boxed{0<\nu(q)\le A:=\frac{203}{3c}.}
\tag{14}
\]

Monotone convergence in the nonnegative parent sum gives

\[
\boxed{L\nu=\nu.}
\tag{15}
\]

In fact `nu` is the least nonnegative `L`-excessive majorant of `h`: if `w>=h` and `Lw<=w`, then `L^kh<=w` for every `k`, so `nu<=w`. No arbitrary normalization or ordinary-point representative is chosen.

### Uniform comparison on a high-floor component

If an entire ordinary component has least positive odd unit `m`, then every inverse history in that component remains at least `m`. Consequently

\[
\boxed{1\le\frac{\nu(q)}{h(q)}\le\delta_m^{-1}}
\tag{16}
\]

for every nonperiodic unit `q` in that component. A growing minimum on a **forward suffix** cannot be substituted for `m`: inverse ancestors can still include the original low source. More generally, (16) is valid at a root if its whole unit-predecessor set lies above `m`.

### The reference has infinite total mass

For any fixed `q` in `N`, the inverse-depth levels `{n:U^j(n)=q}` are disjoint as `j` varies, by nonperiodicity. Each has `nu`-mass `L^jnu(q)=nu(q)>0`. Therefore

\[
\sum_{n\in\operatorname{Pred}(q)}\nu(n)=\infty.
\tag{17}
\]

Such a target exists unconditionally: `5` is an odd unit and `U(5)=1`, so it is nonperiodic. Thus `nu` is a positive sigma-finite reference of **infinite** total mass even on a known convergent predecessor basin.

## 3. Global moments and a common reference for the critical family

For a finite reachability antichain, the predecessor sets in (13) are disjoint. Equations (2), (10), and (13) give

\[
\sum_{q\in A_0}\nu(q)\le\frac1c+D\le A.
\tag{18}
\]

Combine this with (4). In a finite set of states below `X`, partition by the length of a longest reachability chain ending at the state. Each part is an antichain, and there are at most `5X^theta` parts. Since `nu<=A`, for every `p>=1`,

\[
\sum_{\substack{q\in N\\q\le X}}\nu(q)^p\le5A^pX^\theta.
\]

Nonnegative Mellin integration consequently proves

\[
\boxed{
\sum_{q\in N}\frac{\nu(q)^p}{q^s}
\le\frac{5sA^p}{s-\theta}
\qquad(p\ge1,\ s>\theta).
}
\tag{19}
\]

In particular `sum nu(q)/q<=200A=40600/(3c)`. These are weighted moments, consistent with (17).

Write `chi` for PR180's exact normalization constant `(ess inf D)^(-1)`, to distinguish it from the path correction. Its every-ordinary-point comparison is `V<=2 chi G`; hence

\[
\delta\nu(q)\le H(q)\le2\chi\nu(q).
\tag{20}
\]

PR176 gives `D_s<=2V` for `s>=1`, and `F_r<=(1-r)+2rV` for the actual Abel family. Thus, at every `q` in `N`,

\[
\frac{D_s(q)}q\le4\chi\nu(q),\qquad
\frac{F_r(q)}q\le(\gamma^{-1}+4\chi)\nu(q)
\quad(s\ge1,\ 0<r<1).
\tag{21}
\]

The second bound uses `h(q)>=gamma/q` and `nu>=h`. This supplies one actual ordinary harmonic reference for all those finite-depth and discounted families, uniformly in the moving target. It does not assert that this reference is uniformly small on marked targets.

## 4. Exact change of inverse path law

Define two genuine inverse Markov kernels on `N`:

\[
K_h(q,n)=\mathbf1_{U(n)=q}\frac{\lambda(n)h(n)}{h(q)},
\qquad
K_\nu(q,n)=\mathbf1_{U(n)=q}\frac{\nu(n)}{\nu(q)}.
\tag{22}
\]

Their row sums are one by (7) and (15). Let `P_h^q` and `P_nu^q` be their laws on infinite inverse paths `N_0=q,N_1,...`. Write

\[
\Lambda_j=\prod_{i=1}^j\lambda(N_i),\qquad
r(q)=\frac{\nu(q)}{h(q)}.
\]

All inverse paths are simple. The decreasing product has a limit `Lambda_infinity>=delta>0`. Telescoping the transition weights gives

\[
\mathbb E_h^q[\Lambda_j^{-1}]
=\frac{L^jh(q)}{h(q)}.
\]

Bounded convergence and (11) yield the exact normalization

\[
\boxed{r(q)=\mathbb E_h^q[\Lambda_\infty^{-1}].}
\tag{23}
\]

The full change of path law is

\[
\boxed{
\frac{d\mathbb P_\nu^q}{d\mathbb P_h^q}
=\frac1{r(q)\Lambda_\infty}.
}
\tag{24}
\]

To verify it, condition the right side on a path prefix of length `j`. The Markov property and (23) give the conditional density

\[
\frac{r(N_j)}{r(q)\Lambda_j},
\]

which is exactly the product of the ratios `K_nu/K_h` along that prefix. Cylinder probabilities therefore agree with the stated law. All products are bounded by (8), so no unproved critical-limit interchange is used.

If the whole predecessor domain is above `m`, then `1<=r(q)<=delta_m^(-1)` and `delta_m<=Lambda_infinity<=1`. The density in (24) is at least `delta_m`, so the total-variation distance, in the convention `sup_B |P(B)-Q(B)|`, satisfies

\[
\boxed{
\|\mathbb P_\nu^q-\mathbb P_h^q\|_{\rm TV}
\le1-\delta_m
\le\frac{200}{3}m^{-1/40}.
}
\tag{25}
\]

The same bound holds for every finite-depth marginal. This is an approximation of two inverse laws on the same physical predecessor tree. It is not a statement that the forward source is randomly resampled.

## 5. Exact retained-source transport and collision contraction

Let `a>=0` be an original source mass on `N`, and let

\[
b_k(q)=L^ka(q)=\sum_{\substack{x\in N\\U^k(x)=q}}a(x).
\tag{26}
\]

The endpoint in `N` implies the path has not entered a periodic state earlier. Telescoping the ordinary harmonic kernel gives the **exact** identity

\[
\boxed{\nu(q)K_\nu^k(a/\nu)(q)=b_k(q).}
\tag{27}
\]

Unlike the critical `h`-kernel identity, (27) has no multiplicative correction on the original atom. It retains the source, the depth, and every collision exactly.

Define

\[
\mathcal E_\nu(a)=\sum_{q\in N}\frac{a(q)^2}{\nu(q)}.
\]

If this is finite, Jensen's inequality for the probability row `K_nu(q,.)` and Tonelli imply

\[
\boxed{\mathcal E_\nu(b_k)\le\mathcal E_\nu(a)
\qquad(k\ge0).}
\tag{28}
\]

Indeed, for `f=a/nu`,

\[
\begin{aligned}
\sum_q\nu(q)(K_\nu f(q))^2
&\le\sum_q\sum_{U(n)=q}\nu(n)f(n)^2\\
&\le\sum_n\nu(n)f(n)^2.
\end{aligned}
\]

The second inequality accounts for sources that leave `N` and are killed. Iteration proves (28).

The exact original-source pair expansion is

\[
\boxed{
\mathcal E_\nu(b_k)=
\sum_{x,y\in N}
\frac{a(x)a(y)\,
\mathbf1_{\{U^k(x)=U^k(y)\in N\}}}{\nu(U^k(x))}.
}
\tag{29}
\]

In (29), the summand is defined to be zero when its indicator is zero. Nonnegative summation justifies the expansion without truncating the source pair set or replacing it by independent samples.

### Exact one-step dissipation

For `b>=0` of finite energy and `f=b/nu`,

\[
\begin{aligned}
\mathcal E_\nu(b)-\mathcal E_\nu(Lb)
={}&\sum_{\substack{n\in N\\U(n)\notin N}}\nu(n)f(n)^2\\
&+\frac12\sum_{q\in N}
\sum_{\substack{U(n)=q\\U(m)=q}}
\frac{\nu(n)\nu(m)}{\nu(q)}(f(n)-f(m))^2.
\end{aligned}
\tag{30}
\]

This is the countable probability-row variance identity. All right-hand terms are nonnegative and their sum is at most the initial finite energy. The first term records actual killing; the second records the exact unequal-density collision loss.

### A concrete finite, positive source seed

Take the original source mass

\[
a_0(n)=\frac{h(n)}n=\frac{G(n)}{n^2}.
\]

It is positive at every state of `N`, and (3) gives

\[
\sum_n a_0(n)\le\frac{200}{c}.
\]

Since `nu>=h`,

\[
\mathcal E_\nu(a_0)
\le\sum_n\frac{h(n)}{n^2}
\le\frac{10}{c(2-39/40)}
=\frac{400}{41c}.
\]

Consequently the actual unchanged-source fibers satisfy the global bound

\[
\boxed{
\sum_q\frac{(L^ka_0(q))^2}{\nu(q)}\le\frac{400}{41c}
\quad\text{for every }k\ge0.
}
\tag{31}
\]

Also, (12) gives the uniform comparison

\[
\sum_q\frac{(L^ka_0(q))^2}{h(q)}
\le e^{200/3}\frac{400}{41c}.
\tag{32}
\]

These are actual all-time collision bounds. Their references `nu` and `h` are not finite measures.

## 6. The exact energy retained by an escaping source

Suppose an actual source `x` never enters a periodic orbit. Its unit odd orbit `q_k=U^k(x)` is injective. From `Lnu=nu`,

\[
\nu(q_{k+1})\ge\nu(q_k)>0.
\]

The uniform upper bound (14) makes the limit

\[
C_{\mathcal C}=\lim_{k\to\infty}\nu(q_k)
\]

finite and positive. It depends only on the ordinary escaping component: two sources in that component have forward tails meeting after possibly different finite clocks, and finite clock offsets do not change the limit.

For a single original atom of mass `w>0`, the energy is exactly

\[
\boxed{
\mathcal E_\nu(L^k(w\delta_x))
=\frac{w^2}{\nu(q_k)}
\longrightarrow\frac{w^2}{C_{\mathcal C}}>0.
}
\tag{33}
\]

Its cumulative dissipation telescopes to

\[
\sum_{k\ge0}\left(
\mathcal E_\nu(L^k(w\delta_x))-
\mathcal E_\nu(L^{k+1}(w\delta_x))\right)
=w^2\left(\frac1{\nu(x)}-\frac1{C_{\mathcal C}}\right).
\tag{34}
\]

Thus strict positive losses can have a finite total while a positive energy remains. Formula (28) alone cannot exclude this behavior.

### Exact asymptotic formula for multiple original sources

Among escaping sources, define synchronous equivalence by

\[
x\sim y\quad\Longleftrightarrow\quad
U^j(x)=U^j(y)\text{ for some common }j\ge0.
\]

This is finer than ordinary component equivalence: sources meeting only at different clocks need not belong to the same synchronous class. Let `S` range over these classes, and let `C(S)` be their ordinary component. For a finite nonnegative source mass `a` of finite energy,

\[
\boxed{
\lim_{k\to\infty}\mathcal E_\nu(L^ka)
=\sum_S\frac{\left(\sum_{x\in S}a(x)\right)^2}{C_{C(S)}}.
}
\tag{35}
\]

For finitely supported `a`, choose a time after every eventual synchronous collision among its escaping sources and after every nonescaping support point has entered a periodic orbit. Thereafter each synchronous class contributes exactly one atom of its total original mass, different classes have distinct endpoints, and (33) proves (35).

For general finite `a` of finite energy, approximate by its restrictions to increasing finite sets. The omitted `L^2(nu)` energy tends to zero. Contraction (28) bounds the propagated omitted norm uniformly in `k`, and

\[
|\|f\|_2^2-\|g\|_2^2|
\le(\|f\|_2+\|g\|_2)\|f-g\|_2
\]

makes the finite-support energy limits uniformly Cauchy. On the right, the partial class masses increase, so nonnegative convergence gives precisely (35). No endpoint independence or change of source weights is used.

For the positive seed `a_0`, (35) would vanish exactly when no source in `N` escapes. This is a characterization of the remaining energy decay, not a proof that it vanishes. Periodic orbits have already been killed by the definition of the domain and require their separate treatment.

## 7. Testing the finite-reference and five-energy extensions

The new harmonic reference fixes the slope correction in actual transport, but a change to the finite source measure `a_0` has an explicit cost:

\[
\frac{\nu(q)}{a_0(q)}
=q\frac{\nu(q)}{h(q)}\in[q,\delta^{-1}q].
\tag{36}
\]

Therefore

\[
\sum_q\frac{b_k(q)^2}{a_0(q)}
=\sum_q\frac{\nu(q)}{a_0(q)}\frac{b_k(q)^2}{\nu(q)}
\]

requires a height-weighted energy estimate. Dropping the factor in (36) would silently replace the finite-reference problem by a different norm. The moment bounds (19) describe the reference, not the moving source-fiber energy, and do not pay this factor.

Likewise, `nu` is an ordinary harmonic flow, not an invariant component label. Its forward limit `C_C` is an invariant label on escaping components, but it is not bounded by a uniform constant times the local `nu(q)`. The pinned fixed-basin sublinearity and (12) give `nu(n)->0` along unbounded predecessors of a fixed target, whereas the positive component capacity is unchanged. Even the simpler bound that a fixed future value be uniformly charged to every ancestor is false on a known convergent example: `nu(5)>0`, while `nu(n)->0` through unbounded unit predecessors of 5.

The high-floor comparison (16) compares `nu` with `h` **at the same node**. It does not control mass from branches that join later, compare different ordinary components, or create a finite five-defect energy for an invariant label. The covariance of the canonical inverse construction remains componentwise.

The exact remaining estimate is consequently one of the following substantive additions: a genuine height-weighted or finite-reference collision bound retaining each original atom; a proved vanishing of the energy in (35); or an arithmetic charging estimate that makes the invariant label's five-energy finite. None follows from (25), (28), or the stationary almost-everywhere normalization alone.

## 8. Scope of this checkpoint

The new proved statements are the comparable ordinary harmonic reference (11)--(16), its global moments (19), its uniform domination of the critical family (21), the exact bounded path-law change (23)--(25), unchanged-source transport (27), collision contraction and dissipation (28)--(32), and the asymptotic energy calculation (33)--(35).

Every infinite sum in these deductions is nonnegative or is dominated by a displayed finite bound. The cycle exclusion, moving-target critical decay, finite-reference height cost, and five-energy bound remain unproved. No full Collatz theorem, ordinary limit uniqueness, or finite total invariant measure is asserted.
