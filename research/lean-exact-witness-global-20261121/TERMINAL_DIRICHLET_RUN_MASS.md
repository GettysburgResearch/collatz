# The terminal Dirichlet measure is original-source occupation

**Status.** New written, source-qualified deductions from the exact
canonical Dirichlet boundary identity in PR175 at
`728389c2ad4796853948250a90188b0697483d92`, combined with this branch's
binary-run occupation theorem. No analytic statement here is installed
as a Lean axiom or represented as a new Lean declaration. The theorem
identifies the entire terminal energy measure, including the vanishing
killed-boundary remainder. It does not prove that its boundary mass is
zero or classify nontrivial periodic cycles.

The main identity is a convergence in ordinary total mass norm:

\[
\boxed{\left\|\mathfrak e_N-
 \frac1N\sum_{j=0}^{N-1}L^j(dF)\right\|_{\ell^1}
 \longrightarrow0.}
\tag{1}
\]

Here `dF` is one fixed finite measure on the original ordinary integer
sources, and `e_N` is the endpoint pushforward of the actual Dirichlet
energy. Thus the boundary coefficient has an unchanged-source
interpretation at the measure level. Its run-weighted mass diverges
whenever an escaping component exists.

## 1. Pinned data and notation

Use the nonperiodic positive odd ternary-unit domain `N` of the pinned
ordinary harmonic construction. A state in `N` may later enter a periodic
orbit. The ordinary odd map is

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}},
\]

and forward transport is killed on its first entry into any periodic
state. For a source `n`, let `τ(n)` be that killing time, with value
infinity on an escaping orbit. In particular `τ(n)≥1` for `n∈N`.

The imported positive reference and operators are

\[
\begin{gathered}
(La)(q)=\sum_{U(n)=q}a(n),\qquad L\nu=\nu,
\qquad0<\nu(q)\le A,\\
(\mathsf C f)(n)=\mathbf1_{\{\tau(n)>1\}}f(U(n)),\qquad
(Kf)(q)=\frac1{\nu(q)}\sum_{U(n)=q}\nu(n)f(n).
\end{gathered}
\tag{2}
\]

The inverse kernel `K` has row mass one, by `Lν=ν`. This holds also
when forward transport has a killed boundary. All sums below use the
retained domain unless another domain is specified.

Write `𝓡` for the canonical potential, to distinguish it from binary
run count. The finite positive immigration measure `d` satisfies

\[
g=d/\nu,\qquad
\mathcal R=\sum_{j\ge0}K^jg,\qquad0\le\mathcal R\le1,
\qquad\sum_qd(q)<\infty.
\tag{3}
\]

In particular its inverse tail is a genuine pure-potential tail:

\[
K^m\mathcal R(q)
=\sum_{j\ge m}K^jg(q)\downarrow0
\quad\text{for every fixed }q.
\tag{4}
\]

Every escaping ordinary component `𝒞` has a capacity and a forward
potential limit

\[
\nu(U^j x)\uparrow C_{\mathcal C}>0,\qquad
\mathcal R(U^j x)\longrightarrow
F_{\mathcal C}=\frac{D_{\mathcal C}}{C_{\mathcal C}}>0,
\qquad
D_{\mathcal C}=\sum_{x\in\mathcal C}d(x).
\tag{5}
\]

Extend `F` by zero on eventually killed states. It is constant on every
escaping component, and `0≤F≤1`. The following finite coefficient is the
exact boundary from PR175:

\[
b_\infty=\sum_q d(q)F(q)
=\sum_{\mathcal C\text{ escaping}}
 \frac{D_{\mathcal C}^2}{C_{\mathcal C}}
=\sum_{\mathcal C\text{ escaping}}C_{\mathcal C}F_{\mathcal C}^2.
\tag{6}
\]

All these inputs retain the pinned predecessor-population and canonical
envelope qualifications. The source proves, with the actual killed
boundary included, that

\[
\mathcal D(f)=\sum_n\nu(n)|f(n)-\mathsf C f(n)|^2,
\qquad
\mathsf A_N=\frac1N\sum_{j<N}\mathsf C^j,
\qquad
N\mathcal D(\mathsf A_N\mathcal R)\longrightarrow b_\infty.
\tag{7}
\]

The energies in (7) are finite. Applying an ergodic theorem to `𝓡`
itself in `ℓ²(ν)` is not an input: that membership has not been proved.

## 2. Terminal energy and the killed remainder

For `N≥1`, define a nonnegative measure on actual retained terminal
states by

\[
\boxed{\mathfrak e_N(q)=\frac1N
 \sum_{\substack{n\in\mathcal N\\U^N(n)=q}}
 \nu(n)\left|\mathcal R(q)-\mathcal R(n)\right|^2.}
\tag{8}
\]

Only sources with `τ(n)>N` occur in this sum. They are pushed to their
actual endpoint after exactly `N` odd steps. Colliding source
contributions add without being discarded.

The pointwise telescoping identity

\[
(I-\mathsf C)\mathsf A_N\mathcal R
=\frac{\mathcal R-\mathsf C^N\mathcal R}{N}
\tag{9}
\]

and nonnegative regrouping give the exact decomposition

\[
\boxed{
N\mathcal D(\mathsf A_N\mathcal R)
=\|\mathfrak e_N\|_1+\zeta_N,
\qquad
\zeta_N=\frac1N\sum_{\tau(n)\le N}\nu(n)\mathcal R(n)^2\ge0.}
\tag{10}
\]

The second term is essential: a source killed by time `N` contributes
`ν(n)𝓡(n)²/N` to the full energy and has no retained endpoint. Finiteness
of (7) makes both terms in (10) finite. In particular

\[
\limsup_N\|\mathfrak e_N\|_1\le b_\infty.
\tag{11}
\]

For each fixed retained target, harmonicity also gives
`0≤e_N(q)≤ν(q)/N`, since the difference of two values in `[0,1]`
has square at most one.

## 3. A physical inverse-prefix lower bound

Fix an escaping component and an actual ray
`q_j=U^j(q_0)`. Let `0≤j<N`. The prescribed inverse prefix from `q_j`
back to `q_0` has probability

\[
\Pr_{q_j}\{X_j=q_0\text{ along that prefix}\}
=\frac{\nu(q_0)}{\nu(q_j)}.
\tag{12}
\]

This is the telescoping product of actual harmonic transition
probabilities. The source's forward orbit is deterministic, so the
prefix is an actual unique path; it is not sampled from a geometric gap
law. At `j=0`, the event has probability one.

Equivalently, (8) can be written

\[
\mathfrak e_N(q)=\frac{\nu(q)}N
 \mathbb E_q\bigl[(\mathcal R(q)-\mathcal R(X_N))^2\bigr].
\tag{13}
\]

Restrict this nonnegative expectation to the event (12), use the Markov
property for the remaining `N-j` steps, and apply Jensen to the
probability row at `q_0`. This proves

\[
\boxed{\mathfrak e_N(q_j)\ge
\frac{\nu(q_0)}N
 \bigl(\mathcal R(q_j)-K^{N-j}\mathcal R(q_0)\bigr)^2.}
\tag{14}
\]

The row-mass-one hypothesis is used precisely in Jensen's step.
Boundedness of `𝓡` makes every conditional expectation finite. The
restriction `j<N` retains a strictly positive remaining horizon; no
limit in which the horizon is silently set to zero is taken.

Choose `ε>0` with `2ε<F_𝒞`. Equations (4)--(5) supply fixed `J,K`
such that

\[
\mathcal R(q_j)\ge F_{\mathcal C}-\varepsilon\ (j\ge J),
\qquad K^k\mathcal R(q_0)\le\varepsilon\ (k\ge K).
\]

Therefore

\[
\mathfrak e_N(q_j)\ge
\frac{\nu(q_0)(F_{\mathcal C}-2\varepsilon)^2}{N}
\qquad(J\le j\le N-K).
\tag{15}
\]

By moving the fixed anchor `q_0` a finite distance forward, `ν(q_0)`
can be made arbitrarily close to `C_𝒞`. Only a fixed number of initial
and terminal sites of an `N`-site ray segment are then omitted.

## 4. The full measure comparison

Choose one reference state `o_𝒞` in each escaping component, and put

\[
\pi_N^{\mathcal C}=\frac1N\sum_{j<N}\delta_{U^j o_{\mathcal C}},
\qquad
\mathfrak m_N=\sum_{\mathcal C\text{ escaping}}
 C_{\mathcal C}F_{\mathcal C}^2\pi_N^{\mathcal C}.
\tag{16}
\]

These are actual forward occupation measures, with
`||m_N||₁=b_∞`. Each ray is injective, and rays in different components
are disjoint.

### Theorem 1: convergence to the boundary-ray occupation measure

\[
\|\mathfrak e_N-\mathfrak m_N\|_1\longrightarrow0,
\qquad
\|\mathfrak e_N\|_1\longrightarrow b_\infty,
\qquad \zeta_N\longrightarrow0.
\tag{17}
\]

**Proof.** If `b_∞=0`, (10)--(11) already give all three conclusions.
Otherwise choose finitely many escaping components carrying all but an
arbitrarily small amount of the summable coefficient (6).

In each chosen component, first move a fixed anchor forward on its
reference ray and then choose `ε` small. The coefficient
`ν(q_0)(F_𝒞-2ε)²` in (15) can be made arbitrarily close from below to
`C_𝒞F_𝒞²`. If the new anchor is `s` steps past `o_𝒞`, increase the
fixed `K` to at least `s+1`. Then (15) applies to all but a fixed
number of the first `N` sites of the reference ray. At every such site,
`m_N` has mass exactly `C_𝒞F_𝒞²/N`.

Thus the total overlap obeys

\[
\liminf_N\sum_q\min\{\mathfrak e_N(q),\mathfrak m_N(q)\}
\ge\sum_{\mathcal C\text{ in the finite set}}
 C_{\mathcal C}F_{\mathcal C}^2,
\tag{18}
\]

after letting the finitely many anchor and `ε` errors tend to zero.
Exhausting the component set makes the right side `b_∞`. The overlap
is bounded above by both total masses; (11) and `||m_N||₁=b_∞`
therefore force its limit and `||e_N||₁` to equal `b_∞`. Finally use

\[
\|\mathfrak e_N-\mathfrak m_N\|_1
=\|\mathfrak e_N\|_1+\|\mathfrak m_N\|_1
 -2\sum_q\min\{\mathfrak e_N(q),\mathfrak m_N(q)\}.
\]

This proves the first two statements. The exact decomposition (10) and
the total limit (7) then prove `ζ_N→0`. The killed-boundary term has
been removed by a proved mass squeeze, not by dropping it at the outset. ∎

### Theorem 2: the same fixed original sources generate the energy

Define `a(q)=d(q)F(q)`. This is a finite nonnegative measure supported
on escaping sources, and its complete mass in a component is

\[
a(\mathcal C)=D_{\mathcal C}F_{\mathcal C}
=C_{\mathcal C}F_{\mathcal C}^2.
\tag{19}
\]

Then (1) holds.

**Proof.** For each original source `x∈𝒞`, its forward ray and that of
`o_𝒞` meet after some finite clocks `r_x,s_x`. Their length-`N`
occupation measures differ in `ℓ¹` by at most

\[
\min\left(2,\frac{2(r_x+s_x)}N\right).
\tag{20}
\]

The estimate comes from deleting their finite initial paths and
aligning the common tail; a fixed clock offset changes only finitely
many endpoints. Apply this first to a finite collection of original
sources. The bound tends to zero for every source in that collection.
The remaining source labels have total mass as small as desired, and
their norm contribution is at most twice that mass. Therefore

\[
\left\|\frac1N\sum_{j<N}L^j(dF)-\mathfrak m_N\right\|_1
\longrightarrow0.
\tag{21}
\]

Combining (21) with Theorem 1 proves (1). No common bound on all
original-source meeting clocks is needed. All original masses are
retained through their actual endpoint collisions. ∎

## 5. Binary-run occupation of the canonical energy

Write `r(n)` for the number of maximal nonempty runs of one bits in the
binary expansion of a positive integer. For `L≥1`, define the bounded
observable

\[
\Phi_L(n)=\min(4^{r(n)},4^L)
=1+3\sum_{s=0}^{L-1}4^s\mathbf1_{\{r(n)>s\}}.
\tag{22}
\]

The binary-run theorem in
[BINARY_RUN_COMPACTNESS.md](BINARY_RUN_COMPACTNESS.md) gives, on every
escaping odd ray,

\[
\liminf_{N\to\infty}\frac1N
 \#\{0\le j<N:r(U^j x)>s\}\ge4^{-s}
\qquad(s\ge1).
\tag{23}
\]

At level zero, the frequency is one because every positive state has
at least one run. Applying (23) to the finitely many terms of (22),
with no interchange of an infinite sum and a limit, yields

\[
\liminf_N\frac1N\sum_{j<N}\Phi_L(U^j x)\ge1+3L.
\tag{24}
\]

Apply (24) to a finite collection of original atoms of `dF`, and then
increase that collection using nonnegativity and its total mass (6).
Since `Φ_L≤4^L`, the measure comparison (1) transfers the resulting
bound to the actual energy measure:

\[
\boxed{\liminf_{N\to\infty}\sum_q\Phi_L(q)\mathfrak e_N(q)
\ge(1+3L)b_\infty\qquad(L\ge1).}
\tag{25}
\]

This is a frequency-weighted conclusion. It does not assert eventual
avoidance of every low-run state.

If an escaping component exists, then `b_∞>0` by (5)--(6). First take
the large-`N` limit for each fixed `L` in (25), then increase `L`.
Because `4^{r(q)}≥Φ_L(q)`,

\[
\boxed{\sum_q4^{r(q)}\mathfrak e_N(q)\longrightarrow+\infty.}
\tag{26}
\]

Equivalently, in terms of unchanged physical source labels,

\[
\boxed{\frac1N\sum_{\tau(n)>N}\nu(n)\,
4^{r(U^N n)}
\left|\mathcal R(U^N n)-\mathcal R(n)\right|^2
\longrightarrow+\infty.}
\tag{27}
\]

The sums in (26)--(27) are extended nonnegative sums. Their finiteness
at any individual `N` is not claimed. In contrast their unweighted
versions have the finite limit `b_∞` by Theorem 1.

This section uses the common **accelerated odd clock** of PR175's
Dirichlet operator. The common shortcut-clock theorem for an original
atomic measure is separately proved in
[SOURCE_PROGRESS_AND_RUN_MASS.md](SOURCE_PROGRESS_AND_RUN_MASS.md).
No source-dependent initial projection or clock change is made here.

## 6. The actual contact-reset limit of this same measure

The latest PR180 constructs the actual first-contact operator `Π`,
including depth-zero contact, and the measure `η₀=ν 1_{Λ₀}` on all
ordinary last contacts. For each escaping component write
`η_𝒞=η₀ 1_𝒞`. Its pinned input supplies

\[
\Pi\delta_{U^j x}\longrightarrow\eta_{\mathcal C}/C_{\mathcal C}
\quad\text{in }\ell^1\quad(x\in\mathcal C).
\tag{28}
\]

The operator `Π` is an `ℓ¹` contraction on signed measures because its
rows are probability measures. Finite-source approximation, followed by
the norm bound two for differences of probabilities, applies (28) to the
fixed finite source `dF`. Cesàro averaging and (19) give

\[
\Pi\left(\frac1N\sum_{j<N}L^j(dF)\right)
\longrightarrow
\sum_{\mathcal C}F_{\mathcal C}^2\eta_{\mathcal C}
=F^2\eta_0
\quad\text{in }\ell^1.
\tag{29}
\]

Contractivity of `Π` and (1) therefore prove the new identification

\[
\boxed{\Pi\mathfrak e_N\longrightarrow F^2\eta_0
\quad\text{in }\ell^1,\qquad
\|F^2\eta_0\|_1=b_\infty.}
\tag{30}
\]

PR180's finite reference `σ_*` contains `κ c_0 η₀`, with positive
constants `κ,c_0`. Thus this particular limiting measure has bounded
density `F²η₀/σ_*≤1/(κ c_0)`. No uniform `Lp` bound or `Lp`
convergence for the whole family `Πe_N` is inferred from its `ℓ¹`
convergence. The reset forgets the inverse contact depth. In particular
(30) is not a stationarity assertion for the different iterated operator
`Q=ΠL`, whose clock behavior is analyzed in PR180's `CONTACT_CLOCK.md`.

## 7. Exact remaining arithmetic estimate

The existing unweighted estimate (7) permits positive boundary mass,
and Theorem 2 identifies exactly which original measure accounts for it.
The original-source run theorem now forces that canonical endpoint
energy to accumulate unbounded run weight, as in (27).

A finite liminf upper bound for the **same** run-weighted expression
(27) would therefore give `b_∞=0` and exclude every escaping component.
Neither PR175's unweighted `O(1/N)` estimate, PR180's finite reference
for the specified forward/contact compositions, nor PR185's induced
contact-return contraction proves such a bound. The latter contraction
kills a source at its final contact even when its ordinary future
escapes; (30) retains the corresponding positive canonical boundary.

The source-floor theorem provides a different arithmetic interface. A
physical target return into its paid cone descends below the original
target, and that implication is already compiled. It does not establish
the return, nor bound the run-weighted energy (27). Its chosen known
source has a literal certificate to one; a hypothetical escaping target
would be in a different ordinary component. The componentwise harmonic
identities alone provide no comparison between their potential values
merely from their numerical proximity.

Thus the new result is the source-preserving measure identity (1), the
proved disappearance of the killed remainder, and the canonical
run-weighted divergence (25)--(27), with the actual reset limit (30).
No missing upper bound, cap-return coverage, or periodic-orbit exclusion
has been supplied as an assumption to a claimed global conclusion.

## Frozen source ledger

- PR175, `728389c2ad4796853948250a90188b0697483d92`:
  `research/lean-global-closure-20261121/LITERATURE_DIRICHLET_BOUNDARY.md`,
  especially its exact total boundary limit and canonical component data.
  Its upstream analytic qualifications are retained throughout.
- PR180, `ab3973099f0d285bbe88972382ad599bb02cd460`:
  `research/lean-joint-20261122/ORDINARY_BOUNDARY.md` and
  `CONTACT_CLOCK.md`, for the actual first-contact law, finite reference,
  and distinction between one reset after forward transport and repeated
  resets.
- PR185, `53f01ca5b443ef57ef2160b4996dbb2cc87f7395`:
  `research/multiple-attacks-20261122/CONTACT_RETURN_FINITE_REFERENCE.md`,
  `CONTACT_EXIT_ACCOUNTING.md`, and `STOPPED_MIXING_INTERFACE.md`, for
  the current induced contact contraction and its retained terminal exit.
  The PR description still naming `7889fc...` was not used as the latest
  science snapshot.
- This branch, checkpoint 11 `8ef9bf0d828fc533721dee1f90c5d78fac80ad39`:
  `BINARY_RUN_COMPACTNESS.md`, `SOURCE_PROGRESS_AND_RUN_MASS.md`, and
  `ROOTED_SOURCE_FLOOR.md`, with the formal clock, source-growth, and
  floor interfaces in their explicitly identified Lean modules.

The overlap squeeze and the finite-level run identity were also checked
independently by the certificate lane. No bounded numerical experiment or
new formal audit is needed to substantiate the written measure proof.
