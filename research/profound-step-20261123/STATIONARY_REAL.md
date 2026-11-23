# Actual stationary affine series: a renewal identity, critical divergence, and rational atoms

Date: 2026-11-23.

**Status: written actual-source deductions and a literature-driven closing
attempt. No escape exclusion or complete Collatz proof.** This note works
with the stationary gap lift of an actual ordinary time-limit law constructed
in the preceding checkpoint. It proves a finite logarithmic renewal identity,
a fluctuation-controlled lower-tail bound for its real partial sums, and a
classification of every atom of its ternary factor. It also gives a finite
version on one unchanged ordinary word, with the error at its artificial
periodic seam retained explicitly.

The attempt to reconstruct a recurrent affine law from the intrinsic
minimum source is carried to its exact stopping-time and change-of-law
residual. A selected minimum has no later descending ladder time. Localizing
a uniform actual time sample near that minimum costs a factor of order the
time-window length, uniformly over the inverse clock. Neither fact is
silently replaced by the hypotheses of an independent affine recursion.

## 1. Sources and the unchanged stationary lift

The repository inputs are:

| Source | Exact use |
|---|---|
| PR180, `a436db7b85f37abafea25f42d6f34afed02a29c0`, `research/whole-source-20261123/COLLISION_CORE.md`, Sections 2--4 and 9 | Actual ordinary stationary gap lift, exact ternary coding, its mean bound, and the previously written finite-real-series obstruction. |
| Same pin, `research/whole-source-20261123/BOUNDARY_DESCENT.md`, (4)--(5b) | The finite minimum source `sigma`, whole ordinary path probability `Pi`, and `nu_+=sum L^j sigma`. |
| Same pin, `research/high-variance-20261123/ANALYTIC_GLUING.md` | Coherent scale `chi`, component capacity, and the increasing actual spine events. |
| PR182, `a7fd3ac9e5bff7412858df23d776bb847e9c1371`, `research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md` | New global separated-visit count and positive correction product. No new critical counting theorem is claimed here. |
| PR175, `53ba1e1ffc46bf022433c2124a62682ad8dd4739`, `research/lean-global-closure-20261121/risk24/literature/HIGHER_RANK_BOUNDARY_ATTACK.md` | The distinction between actual endpoint laws and dyadically thickened solenoid measures is retained. |
| PR177, `aaa132e904e4e6d0b438e963f76d72d79e2c7f34`, `research/lean-exact-witness-global-20261121/ATOMIC_EXCLUSION_CONTINUATION.md` | Its pressure remainder and continuous-profile classification are not substituted for a stationary real realization. |

Fix one escaping positive odd ternary-unit source and its actual orbit

\[
 q_j=U^j(q_0),\qquad 2^{g_j}q_j=3q_{j-1}+1,\qquad
 \ell=\log_2 3.
\]

Fix a subsequential weak limit `mu` of the unchanged ordinary time laws.
The preceding construction supplies a stationary law `eta` on positive
integer sequences, with shift `S` and coordinates `G_i`, such that

\[
 \mathbb E_\eta G_1\le\ell,\qquad
 z(\omega)=\sum_{i\ge1}3^{i-1}2^{-(G_1+\cdots+G_i)}
       \quad\hbox{in }\mathbb Z_3^\times,\qquad
 z_*\eta=\mu.                                           \tag{1}
\]

The stationary law is extracted from actual reversed past words. It is
not assumed independent or ergodic. Only in the previously proved
maximum-Shannon equality case is it forced to be geometric iid.

Use the same finite words to define real quantities

\[
 D_i=\log3-G_i\log2,\quad S_k=D_1+\cdots+D_k,\quad
 R_m=\frac13\sum_{k=1}^m e^{S_k}>0,\quad
 h(x)=\log\left(1+\frac1{3x}\right).                     \tag{2}
\]

The notation `S_k` for the real partial sum is distinct from the shift `S`.
The real limit `R_infinity` is allowed to be infinity. Ternary convergence
in (1) does not assert real convergence.

## 2. The exact finite logarithmic renewal identity

For every stationary law with `E G_1<infinity`, put

\[
 L_m=\mathbb E\log R_m,\qquad
 d=\log3-(\log2)\mathbb E G_1.
\]

All terms in the following identities are finite. Indeed,

\[
 R_m\ge2^{-G_1},\qquad
 R_m\le\sum_{i=1}^m\frac{3^{i-1}}{2^i}=(3/2)^m-1.
                                                               \tag{3}
\]

Thus the negative part of `log R_m` is bounded by the integrable
`G_1 log2`, and its positive part has a deterministic finite upper bound.
Also `h(R_m)<=G_1 log2+log(4/3)`.

The finite real series obeys

\[
 R_{m+1}=2^{-G_1}(1+3R_m\circ S).
\]

Take logarithms and use stationarity only after verifying (3). This gives
the exact identity

\[
 \boxed{L_{m+1}-L_m=d+\mathbb E h(R_m),\qquad
        L_1=-(\log2)\mathbb E G_1.}                     \tag{4}
\]

Consequently

\[
 \boxed{\sum_{k=1}^m\mathbb E h(R_k)
       =L_{m+1}-L_1-md.}                               \tag{5}
\]

No independence, mixing rate, logarithmic moment of `R_infinity`, or
exchange of a time limit with a resolution limit enters (4)--(5).

Since `R_k` increases, `h(R_k)` decreases. For every `H>0`, (5) gives

\[
 \boxed{\eta\{R_m\le H\}
 \le\frac{L_{m+1}-L_1-md}{m h(H)}.}                     \tag{6}
\]

This is a distributional estimate on the same stationary gap law used
to generate the actual ternary time limit.

## 3. The conditionally critical branch and an explicit iid rate

Let `I` be the invariant sigma-algebra of the stationary shift, and put
`bar_g=E[G_1|I]`. A **conditionally critical** law means

\[
 \bar g=\ell\quad\eta\hbox{-almost surely}.             \tag{7}
\]

An ergodic law of mean `ell` has this property. A nonergodic law whose
overall mean equals `ell` need not have it; mixtures of opposite drifts
are not included silently.

Under (7), define

\[
 M_n^+=\max(0,S_1,\ldots,S_n).
\]

Since `R_(m+1)<=(m+1)e^(M_(m+1)^+)/3`, equation (6) becomes

\[
 \boxed{\eta\{R_m\le H\}
 \le\frac{\log(m+1)+\mathbb E M_{m+1}^+}
              {m\log(1+1/(3H))}.}                     \tag{8}
\]

The numerator divided by `m` tends to zero. Birkhoff's theorem gives
`S_n/n -> 0` almost surely under (7), and therefore
`M_n^+/n -> 0` almost surely: discard a fixed finite prefix, then use
`|S_k|<=epsilon*k` on the remaining indices. The needed passage to
expectations does not assume uniform integrability of an unbounded
maximum. Here `G_i>=1`, so

\[
 0\le M_n^+/n\le\log(3/2)
\]

deterministically. Dominated convergence gives `E M_n^+=o(n)`.
Thus

\[
 \boxed{R_m\longrightarrow\infty\text{ in probability,
 and hence almost surely by monotonicity, under (7).}}    \tag{9}
\]

In the actual maximum-Shannon case, the previous checkpoint forces

\[
 \eta=\gamma_\ell^{\otimes\mathbb N},\qquad
 \gamma_\ell(k)=\ell^{-1}(1-\ell^{-1})^{k-1}.
\]

Then the `D_i` are iid of mean zero and variance

`s_D^2=(log2)^2 ell(ell-1)`.

The elementary square-integrable martingale maximal inequality gives
`E M_n^+<=2s_D sqrt(n)`. It may also be checked by stopping the centered
sum at its first crossing of `t`, obtaining
`P(M_n^+>=t)<=n s_D^2/t^2`, and integrating this bound after splitting
at `t=s_D sqrt(n)`. Therefore the actual equality-case lift obeys

\[
 \boxed{\eta\{R_m\le H\}
 \le\frac{\log(m+1)+
       2(\log2)\sqrt{\ell(\ell-1)(m+1)}}
       {m\log(1+1/(3H))}.}                             \tag{10}
\]

In particular the right side is `O_H(m^(-1/2))` for fixed `H`.
This applies only to the equality case where independence was proved;
it is not an iid estimate imposed on another actual stationary lift.

## 4. Full drift classification and the exact residual correction

The same variables have a precise nonergodic classification. Set

\[
 \bar d=\log3-(\log2)\bar g.
\]

Birkhoff gives `S_n/n -> bar_d`. If `bar_d<0`, the exponential series
in (2) converges. If `bar_d>0`, it diverges exponentially and
`log R_m/m -> bar_d`. On `bar_d=0`, condition on that invariant set
and apply Section 3. Consequently

\[
 \boxed{\{R_\infty<\infty\}=\{\bar g>\ell\}
       \quad\text{modulo null sets},\qquad
 \frac{\log R_m}{m}\longrightarrow(\bar d)_+.}         \tag{11}
\]

The convergence of the normalized logarithms also holds in `L^1`.
Their positive parts are bounded by `log(3/2)+o(1)`, while their negative
parts are bounded by `G_1 log2/m`. This explicitly handles the otherwise
unbounded lower logarithmic tail.

Extend `h` by `h(infinity)=0`. It decreases along `R_m` and is dominated
by the integrable `h(R_1)`. Divide (5) by `m`, use (11), and then use
monotone convergence of the expectations (or dominated convergence).
The exact residual is

\[
 \boxed{\mathbb E h(R_\infty)
       =\mathbb E\big[(\bar g\log2-\log3)_+\big].}     \tag{12}
\]

For the actual lift in (1), its total mean bound therefore implies

\[
 \mathbb E h(R_\infty)
 \le\mathbb E\big[(\log3-\bar g\log2)_+\big].          \tag{13}
\]

The strictly contracting components can carry finite real series, but
their positive correction must be paid by the expanding components.
Merely knowing the overall critical mean does not remove this residual.
This is why the conditional qualification in (7) matters.

## 5. Atoms of the same ternary factor are exactly rational-cycle components

The next result concerns the actual stationary ternary factor in (1),
not the separate canonical real boundary.

**Atomic classification.** For any stationary positive-gap process, every
atom of its ternary series factor belongs to a rational Syracuse cycle.
Its atomic part is a mixture of the uniform phase laws of such cycles.
On a cycle of odd length `h` and total gap `A`, the conditional gap mean
is `A/h`. Positive cycles have `A/h>ell`, and negative cycles have
`A/h<ell`.

Here the rational map is `U(x)=(3x+1)/2^(v_2(3x+1))` on rational
2-adic units with denominator prime to three. Rational cycles are not
asserted to be integer cycles.

**Proof.** Let `z` be an atom. Poincare recurrence to the positive-measure
event `{z(omega)=z}` supplies a finite return of positive length `h`.
For its actual gap prefix, with partial sums `A_i` and total `A`, the
finite affine identity gives

\[
 (2^A-3^h)z=C,\qquad
 C=\sum_{i=1}^h3^{i-1}2^{A-A_i}>0.                     \tag{14}
\]

The denominator is nonzero and odd. The last summand of `C` is odd and
all earlier summands are even, so `C` is odd. Its first summand is a
ternary unit and all later summands are divisible by three. Thus every
atom is already a rational 2-adic and ternary unit. No phase clearing
dyadic denominators is needed.

Let `A_mu` be the countable set of atoms. The identity

\[
 z(S\omega)=(2^{G_1}z(\omega)-1)/3                     \tag{15}
\]

shows that conditional on an atom and on a gap of positive conditional
probability, the shifted factor is another atom. Hence the event
`{z in A_mu}` is forward invariant modulo null sets, and stationarity
makes it invariant modulo null sets. On this event both terms in (15)
are rational 2-adic units. It follows that

`G_1=v_2(3 z(S omega)+1)` and `U(z(S omega))=z(omega)`.

Consequently the finite atomic factor measure is invariant under the
deterministic rational map `U`. Each positive-mass atom is recurrent
under this map, hence periodic. Within a deterministic cycle the preceding
periodic vertex is unique; the gaps on the atomic event are therefore
the repeated cycle gaps, with uniform phase under stationarity.

Finally the sign of (14) is the sign of `2^A-3^h`. Cyclic rotation gives
the same denominator and positive carries, so every point of one cycle
has that same sign. This proves the assertions about its conditional mean.
`A/h` is rational whereas `ell` is irrational. QED.

The rational part of the factor is countable, so any rational point of
positive measure is an atom; the theorem describes all its mass. In
particular

\[
 \boxed{\text{Every conditionally critical component in (7) has a
 nonatomic ternary factor.}}                           \tag{16}
\]

Nonatomicity is weaker than the missing critical collision-dimension
lower bound. A noncritical component can retain a rational-cycle atom;
the mere overall mean inequality in (1) does not eliminate mixtures of
components of different drift. No such elimination is inferred here.

## 6. A finite version on the unchanged ordinary word

There is a way to retain a completely explicit finite source rather
than infer a moving-resolution statement from weak convergence.
Fix its actual first `N` gaps. Put

\[
 T_j=j\log3-A_j\log2=\log\chi_j,\qquad
 d_N=T_N/N,\qquad B_j=T_j-jd_N\quad(0\le j\le N),
\]

and define the bridge oscillation

\[
 V_N=\max_{0\le j\le N}B_j-\min_{0\le j\le N}B_j.
                                                               \tag{17}
\]

Assume `T_N>=0`. This is the finite coefficient condition
`2^(A_N)<=3^N`; it holds for every prefix of the pressure-maximum
source and eventually for any escaping source.

Periodize **these supplied gaps only**, and choose the phase uniformly
from `1,...,N`, reading backwards. Call this auxiliary stationary finite
word law `rho_N`. Its mean logarithmic drift is exactly `d_N>=0`.
Its centered backward partial sums are differences of two values of
the periodically extended bridge `B_j`. They are therefore at most
`V_N`, at every length.

Apply (5)--(6) to this specified finite periodic law. For any `m>=1`,

\[
 L_{m+1}-L_1-md_N
 \le\log(m+1)+\mathbb E\max_{k\le m+1}S_k-(m+1)d_N
 \le\log(m+1)+V_N.
\]

Thus

\[
 \boxed{\rho_N\{R_m\le H\}
 \le\frac{\log(m+1)+V_N}{m\log(1+1/(3H))}.}            \tag{18}
\]

When `1<=m<=N`, exactly the phases `j=m,...,N` avoid the artificial
seam. On these phases the word and its real sum are literal past words
of the original orbit. Therefore the following inequality is entirely
about its actual finite words:

\[
 \boxed{\frac1N\#\{m\le j\le N:R_{m,j}\le H\}
 \le\frac{\log(m+1)+V_N}{m\log(1+1/(3H))},}            \tag{19}
\]

where

\[
 R_{m,j}=\sum_{i=1}^m3^{i-1}
       2^{-(g_j+\cdots+g_{j-i+1})}.
\]

No assumption that the actual gap word is periodic was made. The
periodic completion is only an auxiliary averaging device, and (19)
counts exactly the phases that do not use it.

The exact ordinary affine remainder is

\[
 \boxed{0<R_{m,j}=q_j-3^m2^{-(A_j-A_{j-m})}q_{j-m}<q_j.} \tag{20}
\]

For example, combining (19)--(20) gives the valid finite consequence

\[
 \frac{\#\{0\le j\le N:q_j\le H\}}{N+1}
 \le\frac m{N+1}+\frac N{N+1}
       \frac{\log(m+1)+V_N}{m\log(1+1/(3H))}.           \tag{21}
\]

Its purpose is source accounting, not a claimed improvement over the
new global integer orbit count. More directly, if `V_N=o(N)`, one can
choose `m_N=o(N)` with `V_N+log N=o(m_N)`; then the actual real past
sums `R_(m_N,j)` leave every fixed bounded interval for all but a
vanishing fraction of the original time sample. The oscillation term
in (19), rather than an unspecified stationary convergence rate, is
the exact remaining quantitative input. If the original Cesaro gap
mean exists, Birkhoff-style prefix algebra gives `V_N=o(N)` directly
from `T_j/j` having a limit; no ergodic assumption is needed for that
deterministic statement.

Inequality (20) does not bound the partial sums by a fixed `H` under
the time sample: its bound is the moving ordinary height `q_j`.
At fixed `m`, the actual empirical word laws do converge to the
chosen stationary law, but this alone supplies no rate at growing
`m`. Neither issue is suppressed in (19)--(21).

## 7. Trying to reconstruct the stationary real law from the minimum source

The earlier exact source is

\[
 \sigma(n)=\nu(n)b_*(n)\mathbf1_{n\in V},\qquad
 \sum_n\sigma(n)=C,\qquad
 \nu_+=\sum_{j\ge0}L^j\sigma,\qquad \nu_+(q_j)\to C.
                                                               \tag{22}
\]

The selected roots `n in V` obey
`chi(U^k n)>chi(n)` for every `k>=1`. Thus, under the actual finite
minimum-source law, the first strict descending ladder time of
`log chi(U^k n)-log chi(n)` is **infinity with probability one**.
There is no recurrent ladder chain at which to perform a stationary
contractive reconstruction from this source.

This failure can also be quantified before taking a limit. In the whole
path law `Pi`, let `tau` be the unique minimum clock and
`E_j={Q_j=q_j}`. Write `p_j=Pi(E_j)`, so `p_j` increases to one and
`p_0>0`. Choose `J` uniformly from `0,...,N`, and conditional on `J=j`
sample the whole path from `Pi(.|E_(r+j))`. The endpoint `Q_J` then
has precisely the original moving inverse law `zeta_(N,r)`.

For any fixed nonnegative integer `L`, this unchanged joint law satisfies

\[
 \boxed{\mathbb P_{N,r}\{|J-\tau|\le L\}
 \le\frac{2L+1}{p_0(N+1)}\qquad\text{for every }r\ge0.} \tag{23}
\]

Indeed its density relative to the product of uniform time and `Pi`
is at most `1/p_0`. For each whole path at most `2L+1` sampled
indices lie in the specified interval about its minimum. This proves
the uniform estimate without any rate for `p_j -> 1`.

If a proposed reweighting `Q_(N,r)` gives that event probability at
least a fixed `rho>0`, binary data processing gives, whenever the
right side of (23) is below one,

\[
 \boxed{D_{\rm KL}(Q_{N,r}\Vert\mathbb P_{N,r})
 \ge\rho\log\frac{p_0(N+1)}{2L+1}-\log2.}             \tag{24}
\]

The bound includes infinite relative entropy. Thus the finite minimum
source cannot be substituted for a typical endpoint using a fixed
absolutely continuous change of law with a controlled information
cost. Its mass is finite and positive, but its clock neighborhood has
vanishing frequency in the actual late time sample. Equations
(22)--(24) retain both facts.

## 8. Primary literature and the exact applicability boundary

Two primary sources were inspected at their actual statements:

- Sara Brofferio, Dariusz Buraczewski and Ewa Damek,
  [*On solutions of the affine recursion and the smoothing transform in
  the critical case*](https://sbroffer.perso.math.cnrs.fr/articoli/proc-BBD13.pdf),
  Theorem 1.6 and Section 3.2, especially (3.2)--(3.4) and Proposition 3.5.
  The driver consists of iid affine maps. The critical invariant Radon
  law is reconstructed from a contracting chain at descending ladder
  times; its occupation formula retains the ladder-cycle length. The
  inspected theorem also imposes aperiodicity and explicit logarithmic
  moments. The actual law (22) has a deterministic future from its
  sampled root and an infinite first descending ladder time. Its Green
  formula therefore does not verify that theorem's hypotheses.
- Giles Atkinson,
  [*Recurrence of Co-Cycles and Random Walks*](https://doi.org/10.1112/jlms/s2-13.3.486),
  JLMS, 1976, pp. 486--488. The complete published paper is reproduced
  in Appendix A, printed pp. 89--91, of the author's
  [Warwick thesis](https://wrap.warwick.ac.uk/id/eprint/136838/1/WRAP_Theses_Atkinson_1976.pdf).
  The theorem concerns an integrable real cocycle over an ergodic
  probability-preserving automorphism and identifies zero mean with
  recurrence. It does not make every deterministic sequence generic
  for that measure recurrent. Sections 2--4 above use direct finite
  logarithmic identities and the conditional ergodic theorem, keeping
  that distinction explicit.

The derivations (4)--(24) do not import an unverified renewal-rate,
independence, or Markov-modulation hypothesis. In particular the rational
atom classification and finite periodization calculation need no iid
recursion theorem.

## 9. Outcome of the direct completion attempt

The same stationary critical law now has an explicit real lower-tail
estimate, an exact nonergodic correction balance, and a nonatomic ternary
factor. The finite word version retains the actual source and exposes
the precise fluctuation residual `V_N`. The minimum-source reconstruction
has been tested at its first ladder time and at its actual time-sampling
cost, rather than assumed recurrent because its total source mass is finite.

These facts still do not force a finite real realization for an actual
stationary gap lift or the missing critical collision upper bound.
Nonatomicity alone supplies no collision exponent, and (20) carries a
moving height. No law-changing limit or missing arithmetic comparison
has been promoted to a theorem. Full escape exclusion and the separate
positive-cycle problem remain open in this checkpoint.

No new Lean declaration is claimed for the measure-theoretic arguments
in this note. The preceding stationary sequence core is reused only
with its already stated scope; no generic wrapper was added in place
of the unresolved arithmetic construction.
