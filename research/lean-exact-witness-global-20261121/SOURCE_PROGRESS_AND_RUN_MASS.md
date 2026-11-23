# Original-source run moments on the ordinary Collatz clock

**Status.** The main result below is a written deduction from the binary-run
occupation theorem in [BINARY_RUN_COMPACTNESS.md](BINARY_RUN_COMPACTNESS.md).
It retains each original integer source and transfers occupation to the
common shortcut clock. The finite integer clock estimate is kernel-checked
as `CollatzBinaryRunForcing.ordinary_clock_budget` in
[`lean/Collatz/BinaryRunForcing.lean`](lean/Collatz/BinaryRunForcing.lean).
The binary-run combinatorics, real asymptotics, and measure deductions here
are written proofs, not additional Lean theorems. The later comparison with
canonical harmonic flow retains the analytic qualifications of its pinned
sources. No convergence theorem or cycle classification is claimed.

## 1. The positive result

Write

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd},\end{cases}
\qquad
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}\quad(n\text{ odd}).
\]

Let `R(n)` be the number of maximal nonempty runs of one bits in the
ordinary binary expansion; set `R(0)=0`. Throughout, an **escaping** source
means a positive source whose orbit is not eventually periodic. A
deterministic orbit in the positive integers with this property has no
repeated state and eventually leaves every finite set. In particular its
states tend to infinity. This terminology includes no periodic orbit.

Put

\[
\kappa=\log_2 3,\qquad
\Phi_L(n)=\min\{4^{R(n)},4^L\}\quad(L\ge1).
\tag{1}
\]

### Theorem 1: ordinary occupation and divergence for the same source

For every escaping positive integer `x` and every integer `S≥1`,

\[
\liminf_{N\to\infty}\frac1N
 \#\{0\le t<N:R(T^t x)>S\}
\ge\frac{4^{-S}}{\kappa}.
\tag{2}
\]

For every fixed integer `L≥1`,

\[
\liminf_{N\to\infty}\frac1N
 \sum_{t=0}^{N-1}\Phi_L(T^t x)
\ge 4+\frac3\kappa(L-1).
\tag{3}
\]

Consequently,

\[
\boxed{\displaystyle
\frac1N\sum_{t=0}^{N-1}4^{R(T^t x)}\longrightarrow+\infty.}
\tag{4}
\]

These are observations of the original source at consecutive shortcut
times. No new source distribution, inverse random path, or independently
sampled endpoint enters (2)--(4).

### Proof: a deterministic clock conversion

First let `x=q_0` be odd. Set

\[
q_j=U^j(q_0),\qquad a_j=v_2(3q_j+1),\qquad
A_N=\sum_{j=0}^{N-1}a_j.
\tag{5}
\]

Then `a_j≥1` and `T^{A_N}(q_0)=q_N`. Multiplying the actual odd-step
identities gives

\[
2^{A_N}q_N=q_0\prod_{j=0}^{N-1}(3+1/q_j)\le q_0\,4^N.
\tag{6}
\]

Since `q_N≥1`, this proves the all-positive bound

\[
A_N\le2N+\log_2q_0.
\tag{7}
\]

The exact integral version is already formalized. A signed trace from
`(n : Int)` with gap list `word` and `n<2^ell` satisfies

\[
\operatorname{total}(\texttt{word})
 <2\operatorname{length}(\texttt{word})+\ell.
\tag{8}
\]

This is `CollatzBinaryRunForcing.ordinary_clock_budget`, derived from
`CollatzSignedShadow.cleared_magnitude`; an actual positive odd trace is
an instance. The factor two in (7) alone is sufficient for divergence.

For the sharper constant in (2), take logarithms in the exact equality
in (6):

\[
A_N=N\kappa+\log_2(q_0/q_N)
 +\sum_{j<N}\log_2\left(1+\frac1{3q_j}\right).
\tag{9}
\]

An escaping orbit has `q_j→∞`. The last summands therefore tend to zero,
so their Cesàro average tends to zero. Also `q_N≥1`. Hence

\[
\limsup_{N\to\infty}\frac{A_N}{N}\le\kappa.
\tag{10}
\]

No reciprocal summability estimate or growth rate for `q_N` is used.

Theorem D of `BINARY_RUN_COMPACTNESS.md` states that, for each `S≥1`,
every sufficiently late block of `4^S` consecutive odd indices contains
some `j` with `R(q_j)>S`. Thus

\[
\liminf_{N\to\infty}\frac1N
 \#\{0\le j<N:R(q_j)>S\}\ge4^{-S}.
\tag{11}
\]

At a shortcut time `t`, choose `N` with `A_N≤t<A_{N+1}`. The odd visits
with indices `j<N` all occur at distinct shortcut times less than `t`.
Therefore the shortcut count through time `t` is at least the count on
the left of (11). Moreover `t/N≤A_{N+1}/N`, whose limsup is at most
`κ` by (10). This proves (2) for odd sources. Any positive source has
an odd part reached after finitely many initial halvings; that fixed
clock shift changes neither density nor the lower Cesàro bound for a
bounded observable. Thus (2) holds for every escaping positive source.

For every positive integer `n`, `R(n)≥1` and the finite identity

\[
\Phi_L(n)
 =1+3\sum_{s=0}^{L-1}4^s\mathbf1_{\{R(n)>s\}}
 =4+3\sum_{s=1}^{L-1}4^s\mathbf1_{\{R(n)>s\}}
\tag{12}
\]

holds. Apply (2) to the finitely many levels `1≤s<L` to obtain (3).
Since `4^{R(n)}≥Φ_L(n)` for every `L`, (3) with arbitrarily large fixed
`L` proves (4). The argument exchanges no infinite series with a signed
limit. Using only (7) instead of (10) gives the weaker but sufficient
lower bounds `4^{-S}/2` in (2) and `4+3(L-1)/2` in (3). ∎

## 2. An unchanged original-source measure

Let `a(x)≥0` be any finite atomic measure on the positive integers, and
write

\[
M=\sum_{x\ge1}a(x)<\infty,\qquad
e=\sum_{x\text{ escaping}}a(x).
\tag{13}
\]

Its common-shortcut-time pushforward is

\[
\mu_t(y)=\sum_{\substack{x\ge1\\T^t x=y}}a(x).
\tag{14}
\]

Collisions add the masses of the original sources. For every nonnegative
observable `f`, including an unbounded one in the extended sense,

\[
\sum_y f(y)\mu_t(y)=\sum_x a(x)f(T^t x).
\tag{15}
\]

This is just a regrouping of nonnegative terms according to their
deterministic image. The same source mass is used at all times.

### Theorem 2: a positive escaping atom forces the transported moment

For every fixed `L≥1`,

\[
\liminf_{N\to\infty}\frac1N\sum_{t<N}
 \sum_y\Phi_L(y)\mu_t(y)
\ge 4M+\frac3\kappa(L-1)e.
\tag{16}
\]

If `e>0`, then

\[
\boxed{\displaystyle
\frac1N\sum_{t<N}\sum_y4^{R(y)}\mu_t(y)
\longrightarrow+\infty.}
\tag{17}
\]

**Proof.** Subtract the constant baseline `4M` using (12). For a finite
set of escaping original sources, apply (3), multiplied by the original
source masses, and sum the finitely many resulting lower bounds. The
remaining terms are nonnegative. Increasing these finite subsets gives
(16). Now increase the fixed truncation level `L` to deduce (17).
Equivalently, any one escaping atom of mass `w>0` already contributes
at least `w` times the divergent average in (4). ∎

The hypothesis `e>0` is equivalent to the presence of a positive escaping
atom because the state space is countable. Taking a measure positive at
every positive integer makes this an obstruction to any escaping orbit.
For example, take

\[
a(x)=2^{-x}\quad(x\ge1).
\tag{18}
\]

Then `M=1` and `Σ_x x a(x)=2`. The untruncated moment is finite at every
individual time, as follows from the elementary bound

\[
\boxed{4^{R(n)}\le3n+1.}
\tag{19}
\]

Indeed, the least integer with `r` one-runs has a single one in each run,
a single zero between runs, and no final zero. Its value is
`1+4+⋯+4^{r-1}=(4^r-1)/3`. Also `T(n)≤2n` for every positive `n`, so
`T^t(x)≤2^t x`. Consequently (18) satisfies

\[
\sum_y4^{R(y)}\mu_t(y)
\le3\cdot2^t\sum_x x2^{-x}+\sum_x2^{-x}
=6\cdot2^t+1<\infty.
\tag{20}
\]

This example rules out an artificial divergence caused by an infinite
moment at time zero or at every finite time. It supplies no uniform or
Cesàro upper bound.

The exact closing interface is now concrete: a finite liminf of the
Cesàro averages in (17), for one fixed everywhere-positive original
measure such as (18), would exclude every escaping orbit. No refreshed
source listed below proves that bound. A bounded liminf is sufficient;
an all-time bound is not required. This would exclude escape only, with
the classification of periodic orbits still a separate task.

## 3. Killing cycles without changing escaping atoms

Let `τ_per(x)` be the first shortcut time when the orbit of `x` lies on
any periodic orbit, and put `τ_per(x)=∞` for an escaping source. Define

\[
\mu_t^{\rm per}(y)=
\sum_{\substack{x\ge1\\t<\tau_{\rm per}(x)\\T^t x=y}}a(x).
\tag{21}
\]

This definition removes every periodic orbit, including a hypothetical
nontrivial one. It is a mathematical definition, not an effective cycle
recognition algorithm. Every escaping original atom survives unchanged.
For each fixed `L`, the contribution of the eventually periodic sources
to the `Φ_L` moment tends to zero: it is bounded by

\[
4^L\sum_{x\text{ eventually periodic}}
 a(x)\mathbf1_{\{t<\tau_{\rm per}(x)\}},
\tag{22}
\]

which tends to zero by finite-measure approximation. Each fixed term
eventually vanishes, and the total tail mass is arbitrarily small.
Thus (16) is replaced by

\[
\liminf_{N\to\infty}\frac1N\sum_{t<N}
 \sum_y\Phi_L(y)\mu_t^{\rm per}(y)
\ge\left(4+\frac3\kappa(L-1)\right)e,
\tag{23}
\]

and (17) still follows when `e>0`.

Killing only on arrival at one also preserves the escaping-source lower
bound, but a hypothetical nontrivial cycle would survive. It is therefore
incorrect to identify all surviving sources in that version with
escaping sources.

For infinitely supported `a`, no converse to (17) is asserted: bounded
observables in (22) can be handled by finite-measure approximation,
whereas unbounded excursion moments require additional control. If `a`
has finite support and no escaping atom, its finitely many orbits lie in
a finite union of finite preperiods and cycles, so the un-killed moment
is bounded. In the version (21) it is eventually zero.

## 4. A run-weighted version of the ordinary collision obstruction

This section uses the source-qualified harmonic flow of PR185. Its
domain consists of positive odd ternary units which are not themselves
periodic; transport is killed when a periodic state is first reached.
On this domain let

\[
(Lf)(q)=\sum_{U(n)=q}f(n),\qquad
L\nu=\nu,\qquad0<\nu(q)\le A.
\tag{24}
\]

For an original atomic measure `b`, write `b_k=L^k b`, and define the
nonnegative run-weighted collision energy

\[
\mathcal E_{\nu,R}(b_k)
=\sum_q\frac{4^{R(q)}b_k(q)^2}{\nu(q)}.
\tag{25}
\]

If `b` has an escaping atom `x` of mass `w>0`, then at `q_k=U^k(x)`
one has `b_k(q_k)≥w`. Hence

\[
\mathcal E_{\nu,R}(b_k)
\ge\frac{w^2}{A}4^{R(q_k)}.
\tag{26}
\]

The accelerated occupation theorem therefore gives

\[
\frac1N\sum_{k<N}\mathcal E_{\nu,R}(b_k)
\longrightarrow+\infty.
\tag{27}
\]

Equation (27) is an accelerated-clock statement, because `ν` is defined
on odd units. It is separate from the common-shortcut-clock linear
moment theorem (17); no reference measure on even states is silently
introduced.

PR185's established collision estimate contracts the unweighted energy
`Σ_q b_k(q)^2/ν(q)`. It does not contract (25). By (19), an upper bound
on the height-weighted energy

\[
\sum_q\frac{(3q+1)b_k(q)^2}{\nu(q)}
\tag{28}
\]

would control (25), but the supplied results do not provide such a
finite-reference estimate. The run weight in (25) can be much smaller
than height and supplies a more specific observable to test.

## 5. What critical spikes say about an original source

The finite-spike theorem in PR185 says the following, with its imported
analytic assumptions retained. Fix `B>0`, `η>0`, and `0<γ<1`. For all
sufficiently large odd units `q`,

\[
V_k(q)\ge\eta\frac q{\log(q+2)},\qquad k\le(\log q)^B
\tag{29}
\]

forces an actual predecessor

\[
U^j(n)=q,\qquad1\le j\le k+1,\qquad
n<\exp((\log q)^\gamma)<q.
\tag{30}
\]

The conclusion is smaller than the moving target `q`, not necessarily
smaller than an original source or a whole-component minimum `m`.
There is a direct quantitative reason that a single retained original
leaf does not automatically supply that stronger conclusion.

For an actual path `U^j(m)=q` with total dyadic exponent `A_j`, write

\[
q=\omega m+\beta,\qquad
\omega=3^j2^{-A_j},\quad\beta\ge0.
\tag{31}
\]

Thus `ω/q≤1/m`. Suppose a single stopped leaf of value `v`, with a
specified absolute bound `0≤v≤H` and `H>0`, supplies the spike in (29):

\[
\omega v\ge\eta\frac q{\log(q+2)}.
\tag{32}
\]

Then

\[
\log(q+2)\ge\frac{\eta m}{H}.
\tag{33}
\]

For `q≥2`, `log(q+2)≤2 log q`, so `log q≥ηm/(2H)`.
To put the cutoff in (30) at most `m`, so that its strict conclusion
forces `n<m`, one needs `log q≤(log m)^{1/γ}`. These conditions are incompatible whenever

\[
\frac{\eta m}{2H}>(\log m)^{1/\gamma}.
\tag{34}
\]

For fixed `H,η,γ`, (34) holds for all sufficiently large `m`. A bounded
obstacle leaf has `H=1`; a contact leaf with `V(m)≤2` has `H=2`. An
arbitrary retained subtree has its actual value, and its value must not
be replaced by either constant. Equations (31)--(34) concern only a
single bounded-value original leaf. They do not exclude a stronger
theorem using a collective cutset, nor assert that (30) can never find
a smaller source. They show exactly why the displayed spike bound does
not by itself certify strict original-source progress.

The latest PR176 last-contact representation also retains old sources
at growing distances. It supplies a finite measure `η_Λ` on actual
last-contact sources and, on post-contact escaping states,

\[
\nu(q)=\sum_{\substack{x\in\Lambda\\x\to q}}\eta_\Lambda(x),
\qquad\sum_x\eta_\Lambda(x)\le A.
\tag{35}
\]

For sufficiently large `q`, at the native inverse clock

\[
\ell(q)=\left\lfloor
\frac{\log q-3\log\log(q+2)}{\log(3/2)}
\right\rfloor,
\tag{36}
\]

every physical path `U^j(x)=q`, `j<ℓ(q)`, satisfies

\[
x+1\ge(q+1)(3/2)^{-\ell(q)}\ge\log(q+2)^3.
\tag{37}
\]

Indeed `U(n)+1≤(3/2)(n+1)` at every odd step. Along a fixed escaping
spine `q_i=U^i(q_0)`, a fixed original source's distance to `q_i` has
the form `i-s_x`, whereas

\[
i-\ell(q_i)\ge
\frac{3\log\log(q_i+2)-\log(q_0+1)}{\log(3/2)}\longrightarrow\infty.
\tag{38}
\]

Thus that fixed source eventually lies outside the native clock.
New short-front sources in (37) have growing heights; freshness alone
does not put them below a fixed original minimum. The quantitative
source-qualified upper bound already available is

\[
\nu(q)p_{\ell(q)}^\nu(q)
\le\frac{16}{\delta\log(3/2)\log(q+2)^2},
\qquad\delta=e^{-200/3}.
\tag{39}
\]

The new run-occupation theorem gives no lower bound for this inverse
contact probability. It constrains the same forward source at actual
times, while (39) counts which original contacts reach a moving target
within a prescribed inverse horizon.

## 6. Comparison with the refreshed global results

The following inputs were read at the frozen revisions below. Their
analytic dependencies remain those stated in the source files.

| Input | What it supplies | Why it does not supply the upper bound for (17) |
|---|---|---|
| PR175, all-exponent addendum | Excludes nonzero finite-period regularly varying leading profiles for a positive excessive function. | No such asymptotic profile or upper bound is established for the transported run moment. |
| PR176, last-contact measure | A finite original boundary measure, exact component capacities, and the native-clock upper bound (39). | The forward trajectories of its escaping atoms retain their mass. Finite boundary mass does not bound the values of `4^R` along those trajectories. |
| PR178, ordinary mass | Under its predecessor-population input, escape forces a future-minimum mass of order `X log X` and a reciprocal version of order `(log X)^2`. | These are lower bounds on differently weighted ordinary-source populations; no opposite upper bound for a common-time run moment is supplied. |
| PR182, canonical escape label | A bounded invariant component label, and polynomial-phase rigidity under its stated approximation hypothesis. | The run observable is unbounded and is not invariant. Its bounded truncations are not invariant either, and the required approximation statement is not proved. |
| PR185, harmonic flow and collisions | A bounded positive ordinary harmonic reference, unweighted collision contraction, and global reference moments. | Those bounds do not control the run-weighted energy (25), or the run moment of the moving image of one original atom. |
| PR185, finite spikes | The physical predecessor conclusion (30) in a finite inverse horizon. | The cutoff is measured relative to the moving target. Equations (31)--(34) expose the distinction from strict progress below an original source. |

A concrete distinction between future minimum and run complexity is
useful here. For

\[
u_r=\frac{4^r-1}{3}\quad(r\ge1),
\tag{40}
\]

the binary expansion has `r` one-runs, but `3u_r+1=4^r`, so `U(u_r)=1`.
Thus the future minimum is one while `4^{R(u_r)}=4^r` is arbitrarily
large. A bound on a fixed power of future minimum cannot be substituted
pointwise for the required run weight.
If the domain is restricted to odd ternary units, take `r≡1 (mod 3)`;
then `u_r≡1 (mod 3)` and the same counterexample family remains infinite.

### Frozen source ledger

- PR175, `54b5a324f55d97925ecb8100aa15ce7b08a12093`:
  `research/lean-global-closure-20261121/ADDENDUM_ALL_EXPONENTS.md` and
  `GLOBAL_STEP_20261122.md`.
- PR176, `c83a8459066d8223aefe7fc5f6b75faeea557345`:
  `research/lean-global-resolvent-20261121/overview/whole/ORDINARY_LAST_CONTACT_MEASURE.md`.
- PR178, `f464ddf2af6e340054673fdd6f5b28aba0310c10`:
  `research/global-synthesis-20261122/ORDINARY_MASS.md`.
- PR182, `9dacd610ba7735e89e2e29e4ab01795983317980`:
  `research/lean-dyadic-descent-20261121/CANONICAL_ESCAPE_LABEL.md`.
- PR185, `276be8154f4e867acc0230466b34d9cb224aacf5`:
  `research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`.
- PR185, `7889fc680f5ee22237732eccc172b1699ef565da`:
  `research/profound-closure-20261122/FINITE_SPIKES_FORCE_SMALL_ANCESTORS.md`
  and `POLYLOGARITHMIC_INVERSE_HORIZONS.md`.
- This checkpoint: `BINARY_RUN_COMPACTNESS.md`,
  `lean/Collatz/SignedShadow.lean`, and
  `lean/Collatz/BinaryRunForcing.lean`.

The new conclusion is (17) on the common ordinary clock, together with
the explicitly cycle-killed version (23) and the accelerated energy
consequence (27). It uses the unchanged original source even when other
sources collide with it. A proved finite liminf of that same transported
run moment would exclude escape; none of the refreshed analytic inputs
establishes that bound, and none of these arguments classifies all cycles.
