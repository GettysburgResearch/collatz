# Dense actual fibres without higher-rank thickening

Date: 2026-11-23.

**Status: a new source-qualified, source-preserving density theorem, with an elementary
finite geometry core checked in Lean. The actual ternary collision upper
bound, and Collatz, remain unproved.**

The main result is that almost every actual common real boundary point has
a tail-dense orbit in the full `2,3` solenoid under the **unthickened,
original sequence of coherent Collatz scales**. It uses the actual
boundary's upper local dimension one, not an auxiliary measure of large
dimension. The argument also proves divergence of the summed actual
conditional fibre masses in every nonempty open set. No `N^2` thickening
or vanishing `1/N^2` retained coefficient appears in these conclusions.

This is a topological and infinite-occupation conclusion. It does not
identify a time-average limit or the original ordinary endpoint residues.
The last sections test the literature's stronger entropy and invariance
mechanisms against those two remaining requirements.

## 1. Exact inputs and the unchanged source

The following are the source interfaces used here; the older corpus is not
revalidated in this packet.

| Input | Frozen checkpoint |
|---|---|
| Actual common boundary has upper local dimension one | PR180, `fcdcdbadc6172e414f7282442a8a6b85587d7e70`, `research/source-clock-20261123/BOUNDARY_OVERLAP.md`, (24) |
| Actual common path, conditional fibres, coherent scales, and the compact solenoid | PR175, `53ba1e1ffc46bf022433c2124a62682ad8dd4739`, `research/lean-global-closure-20261121/risk24/literature/HIGHER_RANK_BOUNDARY_ATTACK.md`, Sections 1--3 |
| Strict collision-exponent gap for every fixed actual stationary limit | Published `a436db7b85f37abafea25f42d6f34afed02a29c0`, `research/whole-source-20261123/COLLISION_CORE.md`, Sections 2--4 |
| Exact same-source injection after retaining total, carry quotient, and source quotient | PR182, `a7fd3ac9e5bff7412858df23d776bb847e9c1371`, `research/whole-repo-round3-20261123/ACTUAL_COLLISION.md` |
| Uniform counting of all ordinary visits in an initial interval | Same PR182 head, `research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md` |

Retain the canonical trace, positive floor, full-event selection, and
path-count qualifications of the pinned boundary packet. The following
application is conditional on that source-qualified construction; no
unqualified boundary existence theorem is substituted for it.

Fix one hypothetical escaping ordinary odd-unit source `p`, and retain

\[
 q_j=U^jp,\qquad a_j=v_2(3q_j+1),\qquad
 A_j=\sum_{i<j}a_i,\qquad
 \chi_j=3^j2^{-A_j}.                                      \tag{1}
\]

The common path probability is `P`, its common real boundary is `Z`, and
its boundary marginal is `mu`. Its compact support lies in
`[a,b] subset (0,infinity)`. The pinned dimension conclusion is

\[
 \overline d_\mu(z)
 :=\limsup_{r\downarrow0}\frac{\log\mu(B(z,r))}{\log r}
 =1\quad\text{for }\mu\text{-almost every }z.             \tag{2}
\]

This is an upper local dimension assertion. No lower local dimension or
uniform concentration bound is assumed.

Let `E_j` be the event that the common path passes through `q_j`. The
retained source comparison is

\[
 E_j\uparrow\Omega\quad\text{modulo a null set},\qquad
 p_j=\mathsf P(E_j)\uparrow1,\qquad p_0>0,\qquad
 \mu_j=\mathcal L(Z\mid E_j),\qquad \mu\ge p_j\mu_j.
                                                               \tag{3}
\]

The same path's physical intercept at that root is
`B_infinity=q_j-chi_j Z`. The positive ordinary product gives

\[
 \chi_j=\frac{q_j\Lambda_j}{p},\qquad
 \Lambda_j=\prod_{i<j}\frac{3q_i}{3q_i+1}
 \longrightarrow\Lambda_\infty>0.                       \tag{4}
\]

An escaping ordinary orbit has distinct states tending to infinity.
Consequently

\[
 \boxed{\chi_j\longrightarrow\infty,\qquad
         0<\chi_{j+1}\le\tfrac32\chi_j.}                \tag{5}
\]

Only the two properties in (5) and the actual dimension statement (2)
are needed for the new density argument. Large downward jumps are allowed.

## 2. Every sufficiently small interval contains an avoidance hole

We first prove a deterministic statement that makes no Collatz or measure
assumption.

**Lemma 1 (bounded upward jumps give uniform holes).** Let
`lambda_j>0`, `lambda_j -> infinity`, and
`lambda_(j+1)<=L lambda_j` for one fixed `L>=1`. Let `J` be a nonempty
open arc of the circle. For every fixed tail index `N` and bounded closed real
interval `K`, the closed avoidance set

\[
 F_{N,J}=\{z\in K:\lambda_jz\bmod1\notin J
                     \text{ for every }j\ge N\}          \tag{6}
\]

has upper box dimension strictly less than one. The dimension deficit
depends on `L` and on an interval contained in `J`, but not on `N` or `K`.

**Proof.** Choose a real interval `(c,c+eta)` projecting into `J`, with
`0<eta<1`. Let `I=(u,v)` have width `w=v-u` sufficiently small that
`lambda_N<4/w`. Choose the first `j>=N` with `lambda_j>=4/w`.
It exists because the scales tend to infinity and satisfies `j>N`.
Minimality and the bounded upward jump give

\[
 \frac4w\le\lambda_j<\frac{4L}{w}.                       \tag{7}
\]

This is a first crossing, not a monotonicity assertion about the scales.

The image interval `lambda_j I` has width at least four. Put

\[
 k=\lfloor\lambda_j u-c\rfloor+2.
\]

The two floor inequalities imply

\[
 \lambda_j u+1<k+c\le\lambda_j u+2,
 \qquad k+c+\eta<\lambda_j u+3<\lambda_jv.               \tag{8}
\]

Thus

\[
 H=\left(\frac{k+c}{\lambda_j},
          \frac{k+c+\eta}{\lambda_j}\right)\subset I
\]

is disjoint from `F_(N,J)` and has length

\[
 |H|=\frac\eta{\lambda_j}>\frac{\eta}{4L}|I|.           \tag{9}
\]

In particular the hole exists in **every** sufficiently small real
interval, not only in intervals centred on the avoidance set.

For completeness, turn this into the required dimension estimate. Choose
an integer `h>=1` such that `B=2^h>32L/eta`. Every sufficiently small
dyadic parent interval has an open hole of length greater than eight of
its depth-`h` children. At least one closed child lies inside that hole,
so that child misses `F_(N,J)`. If `n_m` is the number of dyadic cells of
length `2^-m` meeting the bounded avoidance set, then, for all sufficiently
large `m`,

\[
 n_{m+h}\le(B-1)n_m.                                    \tag{10}
\]

Half-open dyadic cells can be used for counting; the discarded child's
closure lies inside the hole, so dyadic endpoints cause no problem.
Iteration, with the finitely many intermediate levels absorbed in a
constant, gives

\[
 \overline{\dim}_{\rm B}F_{N,J}
 \le d_J:=\frac{\log(B-1)}{\log B}<1.                   \tag{11}
\]

This proves the lemma. `square`

The factor four and the choice `32L/eta` are convenient slack constants.
No quantitative optimization is used later.

## 3. Upper local dimension one annihilates these avoidance sets

The required implication uses upper local dimension exactly as supplied
by the source packet. It does not replace it by lower local dimension.

**Lemma 2 (a direct restriction argument).** Suppose a finite Borel
probability `mu` on a bounded interval has upper local dimension one
almost everywhere. Every bounded Borel set `F` with upper box dimension
less than one has `mu(F)=0`.

**Proof.** Suppose instead `mu(F)>0`, and normalize its restriction:
`nu=mu|F/mu(F)`. Choose

\[
 \overline{\dim}_{\rm B}F<s<t<1.
\]

For all sufficiently large `m`, at most `C 2^(sm)` dyadic cells of mesh
`2^-m` meet `F`. The `nu`-mass of cells whose individual `nu`-mass is
smaller than `2^(-tm)` is therefore at most

\[
 C2^{-(t-s)m}.
\]

These bounds are summable. Borel--Cantelli gives, for `nu`-almost every
`z`, eventual lower bounds `nu(D_m(z))>=2^(-tm)` for the containing
dyadic cells. Each such cell is inside `B(z,2^(1-m))`. Interpolating
between consecutive dyadic radii yields

\[
 \overline d_\nu(z)\le t<1\quad\nu\text{-almost surely}.
\]

Since `mu(B)>=mu(F)nu(B)`, division by the negative number `log r`
gives `overline d_mu<=overline d_nu` at these points. Also `nu<<mu`,
so the hypothesis `overline d_mu=1` holds `nu`-almost surely. This is
a contradiction. `square`

**Theorem 3 (tail density for the actual scale sequence).** Under (2)
and (5), for `mu`-almost every `z`, every tail of

\[
 \{\chi_j z\bmod1:j\ge0\}
\]

is dense in the circle. The assertion holds simultaneously after dividing
every scale by any positive member of a fixed countable set.

**Proof.** Apply Lemma 1 with `lambda_j=chi_j/c`, `L=3/2`, to each
fixed `c>0`. Lemma 2 annihilates every avoidance set. Take the countable
union over tail indices, a countable arc basis, and the specified values
of `c`. `square`

There is no appeal here to an equidistribution theorem, to Haar measure,
or to a random model for the valuation sequence.

## 4. Tail density in the full unthickened solenoid

Retain the exact compact group from the higher-rank packet:

\[
 X_6=(\mathbb R\times\mathbb Q_2\times\mathbb Q_3)
       /\operatorname{diag}\mathbb Z[1/6],\qquad
 \iota(t)=[(t,0,0)].                                    \tag{12}
\]

For `k>=0`, let `pi_k:X_6->R/Z` be the character indexed by `6^-k`.
Then `pi_k iota(t)=t/6^k mod 1`, and
`pi_k=6 pi_(k+1)`. These inverse-limit circle factors generate the
topology: every nonempty open subset of `X_6` contains a cylinder
`pi_k^-1(J)` for some nonempty open circle arc `J`. Indeed finitely
many character constraints can be expressed at the largest denominator,
and the resulting open circle set contains a nonempty arc.

Apply Theorem 3 with all `c=6^k` and reflect the arcs to accommodate
the minus sign. We obtain

\[
 \boxed{\text{For }\mu\text{-almost every }Z,
  \{\iota(-\chi_jZ):j\ge N\}\text{ is dense in }X_6
  \text{ for every }N.}                                \tag{13}
\]

These are the actual physical fibre classes, because subtracting the
diagonal integer `q_j` gives

\[
 [(B_\infty,q_j,q_j)]
 =[(B_\infty-q_j,0,0)]
 =\iota(-\chi_jZ).                                     \tag{14}
\]

This is precisely the original sequence; no extra powers of two or three
have been inserted. Every fixed conditional boundary law `mu_j` is
absolutely continuous with respect to `mu` by (3), so the same almost
sure assertion holds after any one such conditioning.

### Infinite occupation in the original conditional fibre laws

Define the actual moving-root fibre law

\[
 \kappa_j=(z\mapsto\iota(-\chi_jz))_*\mu_j.             \tag{15}
\]

On the common path space, (3) implies that almost every path belongs to
`E_j` for all sufficiently large `j`. Equation (13) says its fibre visits
every nonempty open set `V` infinitely often. Tonelli's theorem now gives

\[
 \boxed{
 \sum_{j\ge0}p_j\kappa_j(V)
 =\mathbb E\sum_{j\ge0}
     \mathbf1_{E_j}\mathbf1_{\{\iota(-\chi_jZ)\in V\}}
 =\infty.}                                             \tag{16}
\]

In particular `sum_j kappa_j(V)=infinity`. Both the root index and the
conditional fibre laws in this assertion are the retained ones.

### What observable has become dense

The conclusion concerns the compact class of the **pair of the real
intercept and its ordinary root**, as in (14). It is not a density
statement for `q_j mod 3^m`.

For example, represent `iota(-chi_jZ)` with real coordinate in `[0,1)`.
Subtracting the diagonal integer `floor(-chi_jZ)` gives

\[
 \bigl(\{-\chi_jZ\},-\lfloor-\chi_jZ\rfloor,
                           -\lfloor-\chi_jZ\rfloor\bigr).
                                                               \tag{17}
\]

The resulting ternary coordinate includes the unbounded integer part of
the real scaling. It is not `q_j`. In the original representative the
same effect is the diagonal shift by `floor(B_infinity)`. Thus a compact
cylinder cannot simply be relabelled as an original endpoint residue
condition. The missing integer part is exactly the type of source/carry
information retained in the latest PR182 boxes.

## 5. Frequency is a separate assertion

The proof establishes infinitely many visits on each actual path and
divergence of the summed actual fibre masses. It proves neither a positive
liminf time frequency nor a positive limsup time frequency, and it does
not identify a Cesaro limit as Haar. A tail-dense sequence can have zero
frequency in an open set. The proof used only bounded upward jumps and
the occurrence of arbitrarily large scales; it does not compare elapsed
ordinary time with the number of scales crossed.

The almost sure avoidance argument is nevertheless stronger than a
support statement for one enlarged measure: any proposed contradiction
that confines a positive portion of the actual common boundary to an
eventual proper closed solenoid subset would now close immediately. No
such confinement is obtained from the current real whole-cone floor.

## 6. A second exact constraint: scale phase and the critical iid branch

Put `ell=log_2 3`. Since `A_j` is an integer,

\[
 \log_2\chi_j=j\ell-A_j,
 \qquad \log_2\chi_j\bmod1=j\ell\bmod1.                \tag{18}
\]

The phase is therefore the fixed irrational rotation by `ell`, regardless
of the gap choices. Irrationality follows from unique factorization:
`ell=r/s` with positive integers would imply `2^r=3^s`.

The preceding collision theorem distinguishes a finite Shannon-deficit
branch from the entropy-equality branch. In the equality branch, the
stationary two-sided gap process is the iid positive geometric process
with mean `ell`. Consider any joint empirical limit of that process and
the phase in (18), along the same chosen time subsequence. Compactness of
the phase and the already proved tightness of fixed gap blocks preserve
the gap marginal. Deleting an endpoint preserves joint stationarity.
The phase marginal is Haar, by the elementary irrational-rotation
equidistribution theorem.

**Proposition 4 (the phase cannot correlate with an iid limiting gap
process).** Every stationary joining of a Bernoulli gap shift with the
irrational rotation by `ell` is their product.

**Proof.** Let `theta` denote the circle coordinate. For a nonzero integer
`k`, put

\[
 f_k(\omega)=\mathbb E[e^{2\pi i k\theta}\mid\omega].
\]

Joint invariance makes `f_k` an `L^2` eigenfunction of the Bernoulli shift
with eigenvalue `exp(2 pi i k ell)` (or its inverse under the reverse-shift
convention). This eigenvalue is not one. Bernoulli mixing follows first
for finite cylinder functions by independence and then for all `L^2`
functions by approximation. Mixing excludes every nonconstant eigenfunction:
its correlation with its shifted copy would have constant modulus rather
than tending to the product of means. Hence `f_k=0` for every `k!=0`.
Uniqueness of circle Fourier coefficients makes the conditional phase law
Haar almost surely, which is the product assertion. `square`

The actual integer clock has a stronger, finite-modulus consequence. Use
forward time: `omega_i=a_(j+i)` at time `j`, so the next edge gap is
`omega_0` and the shift is `(S omega)_i=omega_(i+1)`. Fixed initial
boundary coordinates in these empirical two-sided windows have vanishing
proportion and do not change the limits. Put

\[
 \theta_j=\{j\ell\},\qquad
 K_j=\lfloor j\ell\rfloor-A_j=\lfloor\log_2\chi_j\rfloor.
                                                               \tag{19}
\]

Then the exact forward update is

\[
 K_{j+1}-K_j=\lfloor\theta_j+\ell\rfloor-a_j,
 \qquad \theta_{j+1}=\{\theta_j+\ell\}.                 \tag{20}
\]

**Proposition 5 (uniform finite residues of the global scale clock).**
Fix any integer `m>=1`. In the critical iid branch, every joint limit
along the selected ordinary time subsequence of the two-sided gap process,
`theta_j`, and `K_j mod m` is

\[
 \boxed{\eta\otimes m_{\mathbb R/\mathbb Z}
                    \otimes\operatorname{Unif}(\mathbb Z/m\mathbb Z).}
                                                               \tag{21}
\]

In particular the scale-clock residue is independent of the entire limiting
gap process, as well as of the phase. This assertion has fixed `m`.

**Proof.** Write `k=K mod m` using its representative in `{0,...,m-1}`
and encode the two compact coordinates by

\[
 \beta=(k+\theta)/m\pmod1.
\]

The factor `m beta mod 1` is `theta`. The coordinate conversion uses
representatives and is discontinuous only at `theta=0`, or at the finitely
many beta points `r/m`. Those sets have zero mass in every limit under
consideration because its projected phase law is Haar. Weak-limit
coordinate transport is therefore valid in both directions. Equations
(20) become the continuous
circle skew update

\[
 T(\omega,\beta)=
 \left(S\omega,\beta+\frac{\ell-\omega_0}{m}\right).
                                                               \tag{22}
\]

The gap coordinate has the product discrete topology. Therefore the
endpoint-deletion argument for empirical laws gives `T`-invariance of
any such limit. Its projection to `(omega,m beta)` is the product in
Proposition 4.

Let `lambda_0=eta tensor Haar_beta`. It is `T`-invariant: conditionally
on every gap sequence, the beta map is a circle translation. We show
that `lambda_0` is ergodic. Bounded finite cylinder functions of the gaps times
circle Fourier characters form a dense subspace of `L^2(lambda_0)`.
For two such functions, integration in beta makes their correlation zero
unless their Fourier indices agree. At a common index `r`, the phase
accumulated over `n` steps is

\[
 \exp\left(\frac{2\pi i r n\ell}{m}\right)
 \prod_{j=0}^{n-1}\exp\left(-\frac{2\pi i r\omega_j}{m}\right).
                                                               \tag{23}
\]

If `m` does not divide `r`, the geometric distribution gives

\[
 \left|\mathbb E_\eta e^{-2\pi i r\omega_0/m}\right|<1,
\]

because it assigns positive mass to every positive integer, whose phases
are not all equal. All but a fixed number of the factors in (23) involve
gap coordinates outside the two finite cylinder functions. Independence
bounds the correlation by a constant times this strict factor to the
power `n-O(1)`, so it tends to zero.

If `r=hm` with `h!=0`, the product over integer gaps in (23) is one.
The two cylinder functions become independent for all sufficiently large
`n`, and the remaining phase is `exp(2 pi i h n ell)`, whose Cesaro
mean is zero by irrationality. At `r=0` the correlation tends to the
product of means by Bernoulli mixing. Taking Cesaro averages and then
using `L^2` approximation proves ergodicity of `T` under `lambda_0`.

Finally, any joint invariant lift of the already fixed base law
`eta tensor Haar_theta` is absolutely continuous with respect to
`lambda_0`, with density at most `m`: over each base point there are
exactly `m` beta values, and uniform counting gives weight `1/m` to each.
Invariance of the lift and of `lambda_0` makes that density invariant.
Ergodicity forces it to be the constant one. Converting beta back to
`(theta,k)` proves (21). `square`

This controls every fixed profinite observation of the **global** scale
clock. It does not make the total gap of a window independent of that
same window: `A_(j+m)-A_j` is still a deterministic function of its gap
word. In particular it supplies no independence between the PR182 source
quotient and the word in its source box.

Also, the dilation `z -> 2^K z` does not depend continuously on `K` in
the profinite topology. Fixed-modulus clock equidistribution consequently
does not identify the evolving real scenery or give a growing-modulus
estimate. The unbounded integer scale remains outside the fixed-resolution
joining conclusion. A causal disintegration for the full solenoid fibre
has not been established.

## 7. Literature tested against the missing same-law upper bound

The inspected primary sources give several genuine routes to stronger
regularity. Their hypotheses identify exactly which extra structure is
needed from the actual source.

### 7.1 Higher-rank measure rigidity

Einsiedler--Lindenstrauss, *Rigidity properties for commuting automorphisms
on tori and solenoids*, ETDS 42 (2022), 691--736, Theorem 1.2, classifies
ergodic jointly invariant probabilities for the relevant totally
irreducible non-virtually-cyclic action: positive action entropy forces
Haar. [Primary published PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B5B7471AB9A282B5B179E35040809159/S0143385721000742a.pdf/div-class-title-rigidity-properties-for-commuting-automorphisms-on-tori-and-solenoids-div.pdf),
DOI `10.1017/etds.2021.74`.

The actual unthickened measures obey only

\[
 \sigma_{j+1}=(T_3T_2^{-a_j})_*\sigma_j,
 \qquad\sigma_j=(\iota(-\chi_j\cdot))_*\mu.             \tag{24}
\]

This state-dependent cocycle is not separate invariance. The fresh PR175
packet obtains joint invariance and a positive Haar component after an
explicit averaging of `N^2` powers of two. It retains the unthickened
conditional law with coefficient at least `p_0/N^2`, which tends to zero.
The new theorem (13) bypasses that coefficient loss for density, but
does not create the missing unthickened invariance or endpoint label.

### 7.2 Entropy inverse theorems and the exact source boxes

Hochman, *On self-similar sets with overlaps and inverse theorems for
entropy*, Annals 180 (2014), 773--822, develops entropy inverse theorems
for convolutions and proves strong separation consequences for dimension
drop in self-similar measures.
[Primary article and PDF](https://annals.math.princeton.edu/2014/180-2/p07).
Shmerkin, *On Furstenberg's intersection conjecture, self-similar measures,
and the Lq norms of convolutions*, Annals 189 (2019), 319--391, supplies
an inverse theorem directly sensitive to `Lq` concentration.
[Primary article](https://annals.math.princeton.edu/2019/189-2/p01).

For an actual length-`m` word of total `A`, PR182 retains

\[
 2^Aq=3^mp+C_w,
 \qquad k=\lfloor C_w/3^m\rfloor,
 \qquad l=\lfloor p/2^A\rfloor.                         \tag{25}
\]

Within a fixed `(A,k,l)` box, the endpoint residue determines the word,
the source and its unique ordinary occurrence. Consequently the within-box
collision is just the ordinary diagonal. The exact whole-law upper bound
still has the form

\[
 \operatorname{Col}\le
 \left(\sum_{\mathcal B}
     \sqrt{\sum_{j\in\mathcal B}t_j^2}+\tau\right)^2,   \tag{26}
\]

where `t_j` are the original retained weights and `tau` is the original
omitted mass. This is a dependent mixture over actual source boxes.
It is not an independent additive convolution to which an entropy or
`Lq` flattening theorem can directly be applied. Neither (13) nor (18)
has yet supplied the required distribution of the quotient labels in
(25). That is the first missing step in this route, before applying an
inverse theorem.

The contemporary primary manuscript [*A power improvement for uniform
Collatz interval compression*, rStation paper 28, version 3](https://rstation.ai/problems/collatz/papers/28)
also tests this distinction. Its Section 7.10 entropy amplification concerns
iid critical geometric words and the **canonical source modulo powers of
three jointly with the canonical endpoint modulo powers of two**. The
actual source differs from its canonical representative by the source
quotient in (25). The retained individual-orbit law is not the iid word
law, and that quotient is not independent of the word. Its stated
translated compression bound is therefore not silently imported as the
missing actual endpoint collision estimate here.

### 7.3 Scenery normality

Hochman--Shmerkin, *Equidistribution from fractal measures*, Invent.
Math. 202 (2015), 427--479, Theorem 1.1, proves normality from a nontrivial
ergodic scenery distribution with the specified spectral nonresonance.
[Primary author PDF](https://math.huji.ac.il/~mhochman/preprints/normality.pdf).

The actual boundary has (2) and positive lower information dimension.
These do not by themselves supply one ergodic scenery distribution or
the theorem's spectral exclusion. The exact phase (18) is useful data,
but its product joining in Proposition 4 is with the stationary gap
process, not with an already established scenery process. Applying the
normality theorem at this point would assume that missing identification.

### 7.4 Zero real drift and invariance principles

Avila--Viana, *Extremal Lyapunov exponents: an invariance principle and
applications*, Invent. Math. 181 (2010), 115--178, Theorem B, obtains
one-sided measurability of invariant disintegrations for smooth fibre
cocycles under a nonnegative smallest fibre exponent; applying the inverse
version gives the corresponding opposite direction under a nonpositive
largest exponent.
[Primary author PDF](https://w3.impa.br/~viana/out/extremal.pdf),
DOI `10.1007/s00222-010-0243-1`.

In the critical iid gap branch, the real multiplicative drift of
`3/2^a` is zero. This suggests trying to force a causal disintegration,
then independence of the next gap, and finally stationary abelian-action
rigidity. Two precise hypotheses remain absent. First, the actual compact
fibre `X_6` is not a smooth real manifold fibre and has nonzero nonarchimedean
expansion. Second, the real lift is not a tight invariant probability:
`chi_j Z -> infinity` almost surely because `Z>=a>0` and (5).
Passing to a real compactification places that escaping mass at infinity;
it does not recover a finite real fibre law. Unbounded gaps also require
care with derivative hypotheses. No invariance principle is invoked
without resolving these requirements.

Brofferio, *The Poisson boundary of random rational affinities*, Ann.
Inst. Fourier 56 (2006), 499--515, gives a compatible warning rather than
the missing implication: for iid rational affine walks with the stated
moment assumptions, boundary factors occur at places of negative drift.
The critical real place is not a contracting factor in that description.
[Primary published PDF](https://www.numdam.org/article/AIF_2006__56_2_499_0.pdf),
DOI `10.5802/aif.2191`.

## 8. The precise remaining quantitative target

The prior original-source theorem supplies, for every fixed ternary weak
limit `rho` of ordinary time laws, a process-dependent `delta>0` such that

\[
 \operatorname{Col}_m(\rho)
 \ge \exp\bigl(-m(\Phi(\log_2 3)-\delta)+O(1)\bigr).    \tag{27}
\]

It does not assume existence of a Renyi entropy rate. Thus an upper bound

\[
 \operatorname{Col}_m(\rho)
 \le \exp\bigl(-m\Phi(\log_2 3)+o(m)\bigr)             \tag{28}
\]

for that same fixed actual limit would already contradict escape. The
new theorem proves full tail density of actual compact fibres, but it
does not prove (28), control the quotient sum in (26), or identify those
compact fibres with the original residue law `rho`.

The concrete new exclusion is therefore: a positive common-boundary
portion of an escaping ordinary component cannot remain eventually in a
proper closed solenoid set. The first unproved bridge to (28) remains
quantitative distribution of the original source/carry labels, or an
actual arithmetic confinement contradicting (13). No such bridge, and
no proof of Collatz, is asserted in this packet.

## 9. Formalization boundary

`lean/ScaleAvoidance.lean` checks the all-depth first-crossing estimate,
the explicit floor-selected interval hole, and iteration of the finite
covering recurrence. These are the deterministic geometry used in Lemma 1.
The measure restriction/Borel--Cantelli argument, inverse-limit topology,
actual source identifications, joining proof, and literature hypothesis
checks remain written mathematics. They are not introduced as Lean axioms.
The replay script and report identify the exact compiler, Mathlib revision,
source bytes and public theorem axioms.
