# A finite minimum flux and subcritical arithmetic weights on the actual component

Date: 2026-11-23.

**Status.** Written deductions on one hypothetical escaping ordinary component,
retaining its source-qualified canonical harmonic flow. The new deductions are
the minimum decomposition (4), the component occupation identity (6), and the
arithmetic-progression and off-diagonal estimates (11)--(14). They do not prove
escape exclusion or exclude nontrivial cycles. No new Lean theorem is claimed
for the infinite measure arguments in this note.

The direct attack was to connect the real inverse-boundary information to the
late ordinary orbit through the attained pressure maximum of PR182. There is a
finite, exact connection: a whole path has one minimum of its coherent scale,
and the masses of these minima sum to the component capacity. This also gives
finite arithmetic comparison measures at exponents below one. Their upper
bounds are for specified actual measures, however; the transfer to the late
time law retains a height factor. Sections 5--6 keep that factor visible.

## 1. Inputs and the unchanged ordinary component

The sources used here are:

| Source | Pin and exact part used |
|---|---|
| PR180 | `fcdcdbadc6172e414f7282442a8a6b85587d7e70`, `research/high-variance-20261123/ANALYTIC_GLUING.md`: the whole ordinary path law, coherent scale, and common real boundary. |
| PR180 | Same pin, `research/source-clock-20261123/EXTENSIONS.md`: the positive lower information dimension under every fixed absolutely continuous path reweighting. This result is used as supplied, not reverified. |
| PR180 | Same pin, `research/astra-three-routes/pass2/ORBIT_MELLIN.md`, T-A3-401 and T-A3-403: the equal-depth-injective count and its Mellin consequence. The path-count estimate itself is not new here. |
| PR182 | `b78819e95ee7d39f02022de991b42217821e7590`, `research/closure-round2-20261123/SOURCE_CLOSURE.md`, Sections 2--3: an attained ordinary maximum of `r(n)=Lambda(n)/n`, simultaneously for every pressure parameter. |
| PR178 | `4e204f54136c79cf8c9393b34e3330594f99ae0a`, `research/global-closure-20261123/escape/PRESSURE_COLLISION_ATTACK.md`: the exact law being compared, and why a density norm must be retained. |
| PR185 | `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`, `research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md`, Theorem 4: the critical running-height lower bound. Its distinction between bounded-window duration and total low visits is retained. |

Let `E` be one escaping component of positive odd integers prime to three.
Write

\[
 U(n)=(3n+1)/2^{a(n)},\qquad
 0<\nu(n),\qquad \nu(q)=\sum_{Un=q}\nu(n).
\]

Retain the existing component clock `ell(Un)=ell(n)+1`, capacity `C>0`,
and whole path probability `Pi`. Its marginals and edges are

\[
 \Pi(Q_j=n)=\frac{\nu(n)}C\quad(\ell(n)=j),\qquad
 U(Q_j)=Q_{j+1},\qquad
 K_\nu(q,n)=\mathbf1_{Un=q}\frac{\nu(n)}{\nu(q)}.       \tag{1}
\]

In particular each level has total mass `C`, so `0<nu(n)<=C`.
Every whole path is an actual two-sided sequence of distinct ordinary states.
The coherent positive scale satisfies

\[
 \chi(Un)=\frac3{2^{a(n)}}\chi(n),\qquad
 y(n)=\frac n{\chi(n)}\in[a,b],\quad 0<a\le b<\infty.  \tag{2}
\]

Here `a,b` are component constants from the pinned construction. Its common
real backward limit is denoted `Z`. None of (1)--(2) is asserted for an
unqualified arbitrary flow or for a component containing a cycle.

## 2. Every whole path has one coherent-scale minimum

Because a whole path has distinct ordinary states, `Q_j -> infinity` as
`j -> +infinity` and as `j -> -infinity`: each finite set can contain only
finitely many entries. From `chi(n)>=n/b`, its coherent scale also tends to
infinity at both ends. It therefore attains a minimum at a finite clock.

That minimum is unique on the path. Indeed, for two clocks separated by
`h>=1` and actual total valuation `A>=h`, equality of the scales would give
`3^h=2^A`, which is impossible. This assertion concerns one path; different
states on the same component level can have the same coherent scale.

Define the set of forward scale records

\[
 V=\{n\in E:\chi(U^h n)>\chi(n)\text{ for every }h\ge1\}.
\]

For `n in V`, let

\[
 b_*(n)=\mathbb P_n^{K_\nu}
       \{\chi(X_h)>\chi(n)\text{ for every }h\ge1\}.
                                                               \tag{3}
\]

This is a probability for the **actual ordinary inverse chain** from `n`.
It is not survival for independently sampled gaps. Let `M_n` be the event
that the unique minimum of the whole path occurs at state `n`. The future
from `n` is deterministic. Conditional on `Q_ell(n)=n`, the past has kernel
`K_nu`. Consequently

\[
 \boxed{\Pi(M_n)=\frac{\nu(n)}C b_*(n)\quad(n\in V),
 \qquad
 \sum_{n\in V}\nu(n)b_*(n)=C.}                         \tag{4}
\]

The last identity follows because the disjoint events `M_n` exhaust the
whole path probability. It is a finite mass identity over ordinary roots,
not a subtraction of two infinite level sums.

At the global pressure maximum `m` supplied by PR182, `chi(m)` is a global
minimum on `E`. Every other state of any actual path through `m` has a
different clock, hence a strictly larger scale. Thus

\[
 m\in V,\qquad b_*(m)=1,\qquad \Pi(M_m)=\nu(m)/C>0.      \tag{5}
\]

This identifies a concrete positive-mass part of the whole path law on
which **both** scale directions stay above the same ordinary root. More
generally the real boundary law is the countable mixture of its laws
conditional on the positive-mass `M_n`, with the weights in (4). The
previous fixed-reweighting information-dimension theorem applies to each
of those conditional laws. No limit-dependent reweighting has been used.

### The finite minimum source generates the whole late outgoing current

There is a useful operator form of (4), with a positive finite source.
Put

\[
 \sigma(n)=\mathbf1_{n\in V}\nu(n)b_*(n),\qquad
 \nu_+(n)=C\Pi\{Q_{\ell(n)}=n,\ \tau\le\ell(n)\},
 \qquad \nu_-(n)=\nu(n)-\nu_+(n),
\]

where `tau` is the unique minimum clock. Let `L` push ordinary masses
forward, `(Lf)(q)=sum_(Un=q) f(n)`. Once the minimum state is specified,
its entire future is deterministic. The minimum events are disjoint,
so summing their future contributions gives the exact identity

\[
 \boxed{\sum_n\sigma(n)=C,\qquad
 \nu_+=\sum_{j\ge0}L^j\sigma\le\nu,\qquad
 (I-L)\nu_+=\sigma,\qquad (L-I)\nu_-=\sigma.}           \tag{5a}
\]

All sums in the potential formula are nonnegative. At a fixed ordinary
vertex their total is bounded by `nu(n)`, so the subsequent difference
identities involve finite quantities.

Normalize the component clock so `ell(q_j)=j` on the original spine.
The event `E_j={Q_j=q_j}` has probability `nu(q_j)/C -> 1`, and
`Pi(tau>j) -> 0` because `tau` is a finite integer. Therefore

\[
 \boxed{\nu_+(q_j)\longrightarrow C,\qquad
        \nu_-(q_j)\longrightarrow0.}                   \tag{5b}
\]

Thus the entire limiting outgoing current is the ordinary Green
potential of the explicit finite minimum source `sigma`; the remaining
incoming current vanishes along that spine. This is not an inverse
resampling or a claim that the harmonic function `nu` itself is the
Green potential of a positive source. The latter would contradict its
harmonic equation. The two terms and their opposite source equations
in (5a) are retained separately.

## 3. Whole-component fractional occupation bounds

Put `theta=39/40`. A whole path is a set on which every `U^h` is injective:
`U^h(Q_j)=Q_(j+h)` and all entries are distinct. The existing elementary
equal-depth count therefore applies directly, without deleting an initial
piece of this two-sided path:

\[
 \#\{j\in\mathbb Z:Q_j\le X\}\le4X^\theta\quad(X\ge1).
\]

Normalize only the ordinary harmonic weights by `w(n)=nu(n)/C`. Tonelli
and (1) give the exact occupation identity

\[
 \boxed{\sum_{n\in E}w(n)f(n)
       =\mathbb E_\Pi\sum_{j\in\mathbb Z}f(Q_j)}
       \quad(f\ge0).                                   \tag{6}
\]

In particular, although `sum_E w(n)=infinity`,

\[
 0<w(n)\le1,\qquad
 W(X):=\sum_{\substack{n\in E\\n\le X}}w(n)
       \le4X^\theta.                                   \tag{7}
\]

For every `s>theta`, define the **weighted occupation measure**

\[
 \tau_s=\sum_{n\in E}w(n)n^{-s}\delta_n,
 \qquad S_s=\tau_s(E).
\]

It is finite and nonzero. If `m_0=min E`, the counting-integral identity
gives

\[
 \boxed{0<S_s\le\frac{4s}{s-\theta}m_0^{\theta-s},
 \qquad
 \sum_{n>X}w(n)n^{-s}
       \le\frac{4s}{s-\theta}X^{\theta-s}.}             \tag{8}
\]

The orbitwise Mellin integration behind (8) is inherited. The point here
is its exact integration over the unchanged whole component using (6).
In particular this supplies a finite comparison measure for
`theta<s<1`, which is outside the `s>1` range obtained by bounding the
unweighted pressure atoms by `n^(-s)`.

**These measures are not claimed to be pressure eigenmeasures.** Their
weights are `nu(n)n^(-s)/C`, not `r(n)^s`. No invariant or conformal
identity is inferred for `tau_s` from its finiteness.

## 4. Arithmetic-progression tails, including the endpoint s=1

Here is an actual off-diagonal arithmetic upper bound for these measures.
The proof uses both the weight bound `w<=1` and the whole-component count
(7); it does not replace the ordinary states by Haar samples.

Fix an integer modulus `Q>=1` and a residue class `a mod Q`. Count only
ordinary states at least `Q`, and put

\[
 N_{a,Q}(X)=
 \sum_{\substack{n\in E,\ Q\le n\le X\\n\equiv a\pmod Q}}w(n).
\]

For `X>=Q`, counting ordinary integer positions and using (7) give

\[
 N_{a,Q}(X)\le\min(2X/Q,4X^\theta).                    \tag{9}
\]

For `theta<s<1`, write

\[
 \beta_s=\frac{s-\theta}{1-\theta}\in(0,1),\qquad
 A_s=4s\,2^{-\beta_s}
       \left(\frac1{1-s}+\frac1{s-\theta}\right).
                                                               \tag{10}
\]

**Arithmetic tail theorem.** Uniformly over every residue class,

\[
 \boxed{\sum_{\substack{n\in E,\ n\ge Q\\n\equiv a\pmod Q}}
               w(n)n^{-s}\le A_s Q^{-\beta_s}.}         \tag{11}
\]

To prove it, integrate (9) against `s X^(-s-1) dX`. The two terms in
the minimum meet at `X_*=(2Q)^(1/(1-theta))`. Splitting there gives

\[
 \frac{2s}{Q(1-s)}X_*^{1-s}
       +\frac{4s}{s-\theta}X_*^{\theta-s}
 =A_sQ^{-\beta_s}.
\]

We discarded only the nonnegative lower-end subtraction from the first
integral. All series are nonnegative, so the integration is justified by
Tonelli.

At `s=1` the first integral is logarithmic rather than a power. The same
split proves the separate, finite endpoint estimate

\[
 \boxed{\sum_{\substack{n\in E,\ n\ge Q\\n\equiv a\pmod Q}}
             \frac{w(n)}n
 \le\frac{2(1+\log2+\theta\log Q)}{(1-\theta)Q}.}       \tag{12}
\]

The lower cutoff `n>=Q` is material: a full residue class can retain a
fixed ordinary atom at every precision.

For an ordinary atomic measure `sigma`, let

\[
 \mathcal O_Q(\sigma)=
 \sum_{\substack{n\ne k\\Q\mid n-k}}
       \sigma(\{n\})\sigma(\{k\}).
\]

In each unequal congruent pair, the larger integer is at least `Q`.
Order the pair, apply (11) to the larger factor, and sum the smaller
factor. This gives

\[
 \boxed{\mathcal O_Q(\tau_s)\le2S_s A_sQ^{-\beta_s},
 \qquad
 \mathcal O_Q(\tau_s/S_s)\le(2A_s/S_s)Q^{-\beta_s}.}     \tag{13}
\]

In particular the endpoint measure has

\[
 \boxed{\mathcal O_Q(\tau_1)
 \le\frac{4S_1(1+\log2+\theta\log Q)}{(1-\theta)Q}.}    \tag{14}
\]

This is an upper estimate on the actual ordinary weighted component,
with an exponent arbitrarily close to one below the endpoint and a
logarithmic loss at the endpoint. Its ordinary diagonal remains positive.

## 5. Transfer to the original time law: exact retained factor

Let `q_j=U^j(q_0)` be the unchanged original escaping orbit, `N=M+1`,
`v_j=nu(q_j)`, and

\[
 \pi_M=\frac1N\sum_{j=0}^M\delta_{q_j},\qquad
 H_M=\max_{0\le j\le M}q_j.
\]

The literal density relative to the normalized weighted occupation
measure is

\[
 \frac{\pi_M(\{q_j\})}{(\tau_s/S_s)(\{q_j\})}
       =\frac{CS_s q_j^s}{Nv_j}.
                                                               \tag{15}
\]

Since `v_0<=v_j<=C`, its maximum lies between
`S_s H_M^s/N` and `(C/v_0)S_s H_M^s/N`. Applying the one-density
version of the progression estimate therefore gives the valid bound

\[
 \boxed{\mathcal O_Q(\pi_M)
       \le\frac{2CA_s}{v_0}\frac{H_M^s}{N}Q^{-\beta_s}}
       \quad(\theta<s<1).                               \tag{16}
\]

For `s=1`, replace `A_s Q^(-beta_s)` by the right side of (12).
The ordinary diagonal of `pi_M` is exactly `1/N`.

Thus passing below pressure exponent one supplies finite measures and
new arithmetic tail bounds, but it does **not** remove the actual time
law's height factor. For the moving inverse endpoint law `zeta_(M,r)`,
the pointwise density on an endpoint `n` with `U^r n=q_(r+j)` is exactly

\[
 \frac{CS_s n^s}{Nv_{r+j}}.
\]

For `r>=1`, the ordinary inverse support is unbounded, so this density
has infinite supremum. A global maximum-density transfer at such a clock
is unavailable even though (11)--(14) remain valid for `tau_s`.

The critical running-height exponent from PR185 is
`theta_0=0.949955527188...<theta=39/40`. It gives
`H_M >= c N^(1/theta_0)(log N)^(1/(2theta_0))` for large `N`.
Consequently, for every fixed `s>theta`, the factor `H_M^s/N` in (16)
diverges. Taking `M -> infinity` first at a fixed modulus does not
produce a bound on an actual stationary time limit. This is a statement
about the displayed comparison bound, not a lower bound on the true
off-diagonal collisions.

## 6. What the minimum decomposition makes available for the closing step

The new decomposition has a finite ordinary accounting unit:
`nu(n)b_*(n)`. Its total is exactly `C`, and at the global pressure
maximum it is the full weight `nu(m)`. Its ordinary forward Green
potential is exactly the outgoing current `nu_+`, which tends to `C`
along the original future spine. One can therefore condition at
an actual minimum, use the existing inverse-boundary information there,
and sum back with no missing capacity factor. Equations (6)--(14) also
give explicit arithmetic upper bounds for a family of measures on the
whole same component, including a finite weight at exponent one.

They have not supplied an upper bound for the late stationary time law.
In particular, a path's minimum occurs at a finite random clock. Its
future eventually merges with the deterministic original spine, while
its boundary randomness lies in the earlier inverse tree. The exact
weights in (4) do not by themselves impose residue anti-concentration
on that future spine. The comparison (15) quantifies the remaining
change of law, and the height factor in (16) cannot be silently discarded.

A successful use of this route would need a **bilinear** estimate that
uses which large-density ordinary atoms share a residue, or an actual
arithmetic relation transporting the minimum-conditioned boundary law
through the deterministic future without this loss. Neither identity
is asserted here. The new stationary strict collision lower bound in
the sibling lane makes that target precise, but the matching same-limit
upper remains unproved. Full Collatz is unresolved in this packet.
