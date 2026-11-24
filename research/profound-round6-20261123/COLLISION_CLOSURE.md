# Actual collision packing and the missing convergence rate

Date: 23 November 2026. Parent: `afe6f4d1a661b377c9daa4623bdd732ba478386b`.

**Status: PROVED finite source-packing theorem, with its integer and
rational-probability core checked in `CollisionClosure.lean`; written
mesoscopic comparison theorem; source-qualified application of PR180.
The actual stationary collision upper and full Collatz remain OPEN.**

The latest PR180 result changes which proposed closing step is viable.
Its critical iid geometric gap law has exact order-two dimension about
`0.70516`, although its Shannon dimension is about `0.94996`. A collision
upper with the latter exponent therefore cannot follow from the
stationary mean and entropy hypotheses that still permit this law.
One must first use its realization by the same ordinary source.

This note supplies a finite order-two upper at that source, retaining
every occurrence and the ordinary diagonal. It then quantifies the
unproved transfer from that empirical law to its stationary limit.
In particular, a fast comparison between two finite actual laws does
not supply a fast comparison of either law with the limiting model.
No new generic symbolic counterexample is needed for this distinction.

## 1. Frozen sources and the actual remaining hypothesis

PR180 was refreshed to head
`7cfd911d35382d9d3bc988060ba88ade78a4267e`, tree
`c2269ed9ddf0380f733be5d1d521e2a482984ba8`.
The following files were inspected at that head.

| Path within PR180 | Blob and inspected scope |
|---|---|
| `research/closing-step-20261123/COLLISION_CLOSURE.md` | `6e3bb90eb3733b58274f9742ffdd7a86ef84945c`: full-clock/full-carry coding, the conditional-mean carry correction, weighted squared-word tilt, and the exact geometric order-two exponent. |
| `research/closing-step-20261123/TILTED_MOMENT_OBSTRUCTION.md` | `a49031a2d4966b510c93f3af790465c811c7de1d`: original-law logarithmic carry control does not imply squared-word tilted carry moments, even for bounded stationary ergodic gaps. |
| `research/closing-step-20261123/FOURIER_BRIDGE.md` | `2fe3127e8d4882ae332541f76cfc17bbcee8079f`: random-model regularity and its explicit fixed-root, growing-frequency boundary. |
| `research/whole-source-20261123/COLLISION_CORE.md` | `d94a3c4153c7d02802f50bd3a1136c71f6936dca`: actual backward-gap lift, global mean bound, strict collision-exponent gap, and order of limits. |
| `research/profound-step-20261123/STATIONARY_REAL.md` | `2dacbd99dc90ca4b7dc324a59c492f42eb963a1e`: stationary real-series exclusion and the unproved real tightness of the actual code. |
| `research/profound-step-20261123/ENTROPY_ARITHMETIC.md` | `4530ed36c4f3ff6c9cf21149989e97cb94eb1714`: ordinary-source arithmetic and the critical iid alternative. |

All links to this snapshot can be formed from the
[frozen PR180 tree](https://github.com/GettysburgResearch/collatz/tree/7cfd911d35382d9d3bc988060ba88ade78a4267e).
This note does not extend a review verdict to later heads.

The distinction between global and componentwise mean is material.
For the actual stationary gap law, the source currently proves

\[
 \mathbb E G\le\ell,\qquad \ell=\log_2 3.                 \tag{1}
\]

For a possibly nonergodic law, the new carry correction is

\[
 \mathbb E\bigl[(\mathbb E[G\mid\mathcal I]\log2-\log3)_+\bigr].
                                                               \tag{2}
\]

Vanishing of (2) requires the stronger componentwise condition
`E[G | I] <= ell`. It is not a consequence of (1) in the inspected
source. This lane does not assume it silently.

## 2. An untrimmed finite collision upper at the original source

Let `q_0,...,q_(N-1)` be **distinct positive ordinary integers** from
one orbit, with `N>=1`. For odd acceleration these are the actual odd
states, not freely selected representatives of residue classes. Put

\[
 H_N=\max_{0\le j<N}q_j,\qquad
 \pi_N=\frac1N\sum_{j=0}^{N-1}\delta_{q_j},\qquad Q\ge1.
\]

For any probability law `nu` on the integers or on `Z_3`, define

\[
 \operatorname{Col}_Q(\nu)
   =\sum_{r\bmod Q}\nu(r+Q\mathbb Z)^2,                    \tag{3}
\]

where `Q=3^m` for the `Z_3` interpretation. The two draws in (3) are
independent draws from the same empirical law; no stochastic hypothesis
on the underlying orbit is made.

**Theorem 1 (complete pair count).** With
`L_(N,Q)=floor(H_N/Q)+1`,

\[
 \boxed{\quad
 \frac1N\le\operatorname{Col}_Q(\pi_N)
       \le\frac{L_{N,Q}}N
       \le\frac{H_N/Q+1}{N}.
 \quad}                                                    \tag{4}
\]

**Proof.** Keep every ordered pair `(i,j)` with
`q_i == q_j (mod Q)`, and send it to

\[
       (q_i,\lfloor q_j/Q\rfloor).                         \tag{5}
\]

There are at most `N L_(N,Q)` possible images. The first source fixes
the residue of the second; its complete quotient in (5) then recovers
the second integer exactly. Distinctness of the ordinary states recovers
both indices. Thus (5) is injective and the collision-pair count is at
most `N L_(N,Q)`. Dividing by `N^2` proves the upper bound. All `N`
ordinary diagonal pairs are present, proving the lower bound. No pair
is removed because of a large carry, atypical gap word, or source cell.

If `Q>H_N`, equality holds on the left: congruent ordinary states
below `Q` are equal, so every collision is a diagonal pair.

The ordinary quotient in (5) is retained until the count is complete.
It is not replaced by a uniform distribution. This direct endpoint
count coexists with the full affine identity

\[
       2^Aq=3^mp+C
\]

used in the earlier source/carry boxes: it does not discard `p`, `A`,
or `C` from an asserted decoding theorem. Instead it bounds **all**
boxes and their cross-collisions together by the actual endpoint height.
The price of that unconditional finite bound is precisely `H_N`.

The Lean module proves the injective count for an arbitrary finite
set of ordinary naturals, its normalized rational collision bound,
and the exact diagonal identity below one modulus. Applying it to
the set of distinct actual orbit states gives (4). It does not
formalize stationary limits or the analytic arguments below.

## 3. Quantitative obstruction to transferring the upper to a limit

Fix any probability measure `mu` on `Z_3`. It may, in particular, be
a stationary residue limit of these same actual prefixes. Use total
variation normalized as half the `l^1` distance and set

\[
 \varepsilon_{N,m}
   =\|\pi_N\bmod3^m-\mu\bmod3^m\|_{\rm TV}.
\]

**Theorem 2 (same-source discrepancy).** For every `N,m`, with
`Q=3^m`,

\[
 \boxed{
 \varepsilon_{N,m}\ge\frac1{\sqrt2}
   \left(\sqrt{\operatorname{Col}_Q(\mu)}
       -\sqrt{\frac{\lfloor H_N/Q\rfloor+1}{N}}\right)_+.
 }                                                         \tag{6}
\]

**Proof.** If `p,q` are two finite probability vectors and their
total variation distance is `delta`, the positive and negative parts
of `p-q` each have total mass `delta`. Consequently

\[
 \|p-q\|_2^2\le2\delta^2.
\]

The triangle inequality therefore gives

\[
 \sqrt{\operatorname{Col}_Q(\mu)}
 \le\sqrt{\operatorname{Col}_Q(\pi_N)}
       +\sqrt2\varepsilon_{N,m}.
\]

Insert (4) and rearrange. This is an inequality for the full empirical
law and full limiting law, not for typical-set restrictions.

Here is the resulting scale restriction. Suppose, along one fixed
subsequence `N_i -> infinity`, that

\[
 H_{N_i}\le N_i^{\beta+o(1)},\qquad
 \operatorname{Col}_{3^m}(\mu)\ge c\,3^{-dm}
 \quad\text{for all sufficiently large }m,                 \tag{7}
\]

where `c>0` and `0<d<1`. For a fixed `kappa>0`, put
`m_i=floor(kappa log_3 N_i)` and `Q_i=3^(m_i)`.
If

\[
       \kappa d<1,
       \qquad \beta<1+\kappa(1-d),                         \tag{8}
\]

then

\[
 \boxed{
 \varepsilon_{N_i,m_i}
    \ge\left(\sqrt{c/2}-o(1)\right)Q_i^{-d/2}.
 }                                                         \tag{9}
\]

Indeed, the ratio of the packing upper in (4) to `c Q_i^(-d)`
is at most

\[
 c^{-1}\left(\frac{H_{N_i}}{N_i}Q_i^{d-1}
                    +\frac{Q_i^d}{N_i}\right)=o(1)
\]

by (8). Equation (6) proves (9).

Conversely, a comparison
`epsilon_(N_i,m_i)=o(Q_i^(-d/2))` at such a growing scale can only
hold if `beta >= 1+kappa(1-d)`, provided `kappa d<1`.
If a claimed rate `epsilon_(N_i,m_i) <= N_i^(-gamma+o(1))`
is available for **every fixed** `0<kappa<1/d`, optimization gives

\[
 \boxed{
       \beta\ge1+\frac{1-d}{d}\min\{1,2\gamma\}.
 }                                                         \tag{10}
\]

The quantifier over growing scales in this last statement is essential.
Convergence at each fixed modulus supplies none of these rates.

## 4. What the new sharp geometric result implies

At the frozen PR180 head, iid geometric gaps with mean `1<b<2`
give the sharp untrimmed ternary estimate

\[
 (2b-1)^{-m}\le\operatorname{Col}_{3^m}(\mu_b)
          \le C_b\sqrt m\,(2b-1)^{-m}.                    \tag{11}
\]

This uses the squared-word tilt, whose mean is
`b^2/(2b-1)`, together with a full-carry moment under that tilted law.
It is an exact random-model result, not a claim that the actual
ordinary source samples that model.

In the critical alternative `b=ell`, define

\[
 d_* =\frac{\log(2\ell-1)}{\log3}
       =0.7051555980\ldots,
 \qquad \frac1{d_*}=1.4181267267\ldots.                    \tag{12}
\]

The Shannon value is

\[
 \theta=\frac{\ell\log\ell-(\ell-1)\log(\ell-1)}{\log3}
         =0.9499555272\ldots.
\]

Thus an order-two upper `exp(o(m)) 3^(-theta m)` is incompatible
with (11) for this law. Using it to close the actual-orbit argument
requires an additional ordinary-source exclusion of the critical
iid alternative. Shannon entropy loss `o(m)` does not provide it.

Applying (9) with `c=1,d=d_*` gives a more explicit test. Whenever
`beta<1/d_*`, there is a nonempty interval

\[
 \max\left\{0,\frac{\beta-1}{1-d_*}\right\}
        <\kappa<\frac1{d_*}
\]

on which a putative critical iid limit necessarily has discrepancy
at least `(1/sqrt(2)-o(1)) Q_i^(-d_*/2)` from the actual finite law.
For instance, a rate at least `N_i^(-1/2+o(1))` at all these scales
would force the stronger height exponent `beta>=1.4181267...`.
This is conditional on that specified rate; it is not a new
unconditional height lower bound.

The general strict collision-exponent gap in PR180's
`COLLISION_CORE.md` can also be inserted into (6)--(10), with its
process-dependent exponent. No iid replacement is required for
Theorems 1 and 2 or for that application.

### Fast finite flows preserve this obstruction

The inspected PR178 source
`research/central-step-20261123/stationary/FAST_EQUIVALENT_FLOW.md`,
head `c91b80a3156e640ad471cf30c47721145ae21eb1`, blob
`39ccf195e42ee17121ff856c45541e70e05d393f`, gives an equivalent
actual inverse flow with `O(1/N)` total-variation error.
If such a flow is `zeta_N`, then contraction under projection and
the triangle inequality give, uniformly in `m`,

\[
 \|\zeta_N\bmod3^m-\mu\bmod3^m\|_{\rm TV}
 \ge \varepsilon_{N,m}-O(1/N).                             \tag{13}
\]

Since `kappa d<1` in (8), the correction in (13) is negligible
against `Q_i^(-d/2)`. The lower bound (9) therefore survives this
faster clock normalization. The `O(1/N)` estimate compares two
finite laws from the same source; it does not estimate either
law's error relative to `mu` at growing resolution.

## 5. Literature consumers checked, and why they do not yet close

**Shmerkin's order-q inverse theorem.**
[Shmerkin, *On Furstenberg's intersection conjecture, self-similar
measures, and the Lq norms of convolutions*, Annals of Mathematics
189 (2019), Theorem 2.1](https://annals.math.princeton.edu/wp-content/uploads/annals-v189-n2-p01-s.pdf)
was read in its original statement. It applies to an actual convolution
of discretized probability measures whose `L^q` norm fails to flatten,
and extracts regular subsets with a scale-by-scale branching
alternative. The discussion before the theorem explicitly accounts
for subsets of exponentially small mass. This is relevant to the
untrimmed collision target. However, the actual gap-selected affine
code has not been represented as the required convolution of the
same source law; full clock, carry, and conditional dependence cannot
be suppressed to create that hypothesis. The theorem is not applied
here, and no rigidity conclusion for the actual Collatz measure is
claimed.

**Stationary Renyi rates.**
[Wu, Li, Xu and Han, *Renyi Entropy Rate of Stationary Ergodic
Processes*](https://arxiv.org/abs/2207.07554), published in IEEE
Transactions on Information Theory 70 (2024), was inspected at the
primary abstract and publication record level. It distinguishes
classes with controlled Renyi rates and Markov approximation from
general stationary ergodic processes, where the proposed continuity
to Shannon entropy can fail. No theorem from its uninspected full
proof is imported. PR180's exact critical geometric calculation is
already sufficient for the specific Shannon/order-two separation
used in this note.

**Critical real affine recursions.**
[Brofferio, Buraczewski and Damek, *On the invariant measure of the
random difference equation in the critical case*, Annales de
l'Institut Henri Poincare 48 (2012), 377--395](https://www.numdam.org/article/AIHPB_2012__48_2_377_0.pdf)
was read for the introduction and Theorem 1.1 hypotheses. Critical
iid coefficients describe a random affine recursion with zero mean
logarithmic multiplier and an invariant Radon, rather than probability,
measure under the stated nondegeneracy and moment assumptions.
For geometric gaps at mean `ell`, the model coefficients
`A=3/2^G,B=1/2^G` fit the zero-drift setup. A fixed ordinary orbit
whose finite block frequencies are iid need not be a typical random
sample for an unbounded real recurrence observable. The missing
actual-source real tightness in `STATIONARY_REAL.md` is therefore
not discharged by this literature result.

## 6. First unsupported step and formal scope

The finite upper (4) is unconditional for distinct ordinary source
states. Its conversion into an upper for the stationary law requires
a comparison at `m` growing with `log N`, with error on the square-root
collision scale. The first unsupported step is precisely that
source-conditioned comparison, or a different argument controlling
the full stationary collision without it. Fixed-modulus weak
convergence, typical-set entropy estimates, and a fast replacement
of one finite actual flow by another do not supply this step.

No convergence rate or ordinary height upper has been proved here.
The conditions of (7)--(10) are displayed to test proposed transfers,
not introduced as a new name for a proved closure hypothesis.

`CollisionClosure.lean` was checked with Lean `4.34.1`, mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`, one worker, and
`-DwarningAsError=true`. Its substantive declarations are
`source_eq_of_residue_and_quotient`,
`orderedResidueCollisions_card_le`,
`residueCollision_le_of_height`, and
`orderedResidueCollisions_eq_diagonal` in namespace
`CollatzShell.CollisionClosure`. The normalized formal statement
uses rational probabilities, which are exact for finite uniform
empirical laws. The measure-theoretic limit, total-variation theorem,
asymptotic corollaries, and literature transfers are written arguments,
not claimed as Lean formalizations. No bounded experiment is used
as evidence for an all-depth assertion.
