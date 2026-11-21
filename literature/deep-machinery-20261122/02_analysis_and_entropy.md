# Analytic machinery: mixing, entropy, populations, and the exceptional orbit

**Research briefing, 22 November 2026.** This is a literature-to-repository translation, not a proof of Collatz. Literature statements are separated from proposed interfaces. Recent preprints and repository analytic arguments retain their own evidence boundaries. No Lean project was rebuilt for this briefing.

## Read this first

The most promising analytic question is not whether Collatz looks random. It is whether a particular distribution, produced by the actual unresolved dynamics, remains sufficiently spread out after repeated selection and transport. Deep mixing theorems often describe a fresh ensemble. The repository needs estimates for the ensemble left after the difficult trajectories have been selected.

Three projects deserve priority:

1. **Audit the joint clock-and-offset mixing interface already attempted in PR180.** This is the most direct point of contact with Tao's strongest machinery. Verify the exact selected law, central-clock normalization, and conversion from weighted paths to distinct ordinary sources.
2. **Convert the new predecessor-population bounds into a quantitative contradiction contract.** A failed orbit would have many predecessors. An upper bound for the same failed set, with the same floor and source measure, could eliminate it. The missing estimate can be stated numerically instead of as “prove enough mixing.”
3. **Use finite inequality certificates to discover what extra state is necessary.** Krasikov–Lagarias provides a model for making large computations produce transparent inequalities. A band-survivor or retained-source adaptation would be new; merely increasing the classical exponent is less targeted.

The highest-risk, potentially high-value connections are entropy inverse theorems, entropy decrement, and sum–product/expander ideas. Their potential contribution is a structural description of failure to mix. None presently applies automatically to the selected return process.

## 1. The interface to the current repository

The shortcut map is

$$
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
$$

For odd positive inputs write

$$
U(x)=\frac{3x+1}{2^{a(x)}},\qquad a(x)=v_2(3x+1).
$$

The forced section is the set of odd positive integers satisfying

$$
(d+1)(x-2^d)\le70\,2^d,\qquad d=\lfloor\log_2x\rfloor.
$$

It has no defining condition modulo three. Every positive orbit reaches it. Its first positive return map is total, but the open return-descent assertion is that every marked input greater than one has some later marked return below itself. Returns can grow by arbitrarily large factors.

The current packets already go substantially beyond the original visit theorem:

| Repository interface | Current scoped result | What the analytic literature would still have to supply |
|---|---|---|
| PR173, `ForwardSection.lean` and `SectionDynamics.lean`, head `fa0c9e2a2851e6324391e39c17afcb5913185aec` | Forced actual entry; return-descent equivalence | A universal descent mechanism after entry |
| PR176, section README, head `3dbe5542fd6a5a1d63b354225d92391471c17002` | Exponentially many distinct marked predecessors in a controlled height range, with varying ordinary clocks | A survivor upper bound that beats that population on the same scale |
| PR180, `research/lean-forward-band-20261121/README.md`, head `cf91e46fa9fbadba3df7942202a5197c134d0ce0` | Written joint-clock mixing and a claimed uniform ordinary predecessor lower bound `cX/a` for `X≥Ca`; analytic theorem is not Lean formalized | Audit and then exploit this lower bound; it is not a survivor upper bound |
| PR183, `research/literature-closing-20261121/README.md`, head `cc046e189366e7e876fc283b80459e64faa9c486` | Written retained-source entrance renewal, first-return domination with an explicit residual, conditional recurrence criterion; four new Lean scripts at this head await compiler replay | Domination of the actual repeatedly transported packets, with the required finite moment |

This briefing does not rebrand the existing PR180 joint-clock argument as a newly proposed idea. The new contribution here is the external comparison, the audit contract, and the quantitative population-versus-survival test below.

## 2. Tao's machinery: strongest direct connection

### The literature result

Tao's theorem says that for every prescribed function `f(n)→∞`, the orbit minimum is below `f(n)` for logarithmically almost all starts. His Proposition 1.17 gives arbitrarily large polynomial decay in the depth for primitive Fourier coefficients of a specific random Syracuse offset modulo `3^r`. Sections 5–7 use first-passage transport, a convolution splitting, collision estimates, and a two-dimensional renewal process. These are ensemble statements, with their probability laws specified. The corrected version is arXiv:1909.03562v7, 16 July 2026; its main theorem is unchanged. [A01]

**Plain-language mechanism.** Start with many initial values rather than one. After enough steps, their additive offsets forget fine details of where they began. That makes it possible to pass from one height range to a lower one without resetting the distribution to an unjustified uniform law.

### Proposed translation and audit contract

For an actual valuation word `a_1,…,a_r`, put `A=a_1+…+a_r`. The exact affine identity is

$$
U^r(n)=3^r2^{-A}n+F_r(a_1,\ldots,a_r).
$$

The multiplier depends on `A`; the additive term depends on the whole word. Therefore forgetting `A` can discard the information needed to locate an ordinary source within a prescribed height interval. Conversely, conditioning on `A` changes the law of the word. A proof that the unconditioned offset mixes does not establish that the offset mixes after conditioning on its clock.

This is precisely why PR180's new argument matters. Its advertised use of a stronger nonnegative renewal estimate, rather than a marginal-only implication, should be checked at the following narrow points:

- Specify the joint distribution of `(A,F_r mod 3^s)` before and after all path selections.
- At a central total `|A-2r|≤√r`, retain its probability, typically of order `r^(-1/2)` in the independent geometric model. An absolute error that tends to zero may still swamp that cell.
- If Fourier inversion introduces a sum over `3^s` frequencies, retain that factor or the compensating collision-entropy estimate. Superpolynomial decay in `r` cannot blindly pay an exponential number of frequencies.
- Preserve every factor introduced by clock truncation, inverse integrality, source-height selection, and removal of periodic duplicate paths.
- Finally count distinct positive ordinary integers. A total weight of legal words is not yet a count of distinct sources.

These are proposed review obligations, not allegations that the current packet fails them. The benefit is a reusable theorem interface that subsequent agents can import without redoing the entire analytic proof.

### What this does not give

Even an excellent population theorem can feed a hypothetical failed target with many predecessors. That is useful, but compatible with failure unless another estimate makes that population impossible. Better mixing of a random inverse construction does not force the target itself to descend.

**First useful task.** Extract a short statement for the joint selected law with all constants and quantifiers. Verify it independently against Tao v7 and PR180's exact frozen source. Make the distinction between marginal mixing, joint mixing, and mixing conditional on one clock explicit.

**Stop rule.** Stop any proposed shortcut at the first place it replaces a selected law by the fresh geometric law without a proved comparison. That replacement is the hard theorem, not notation.

**Priority: very high.** This is a direct match to an active repository interface and has a narrow, reviewable output.

## 3. What the 2026 predecessor-density results change

### Source-qualified recent literature

Mazur's September 2026 predecessor paper states that each fixed positive target not divisible by three has a predecessor set of positive lower natural density. The target need not be known to converge. Constants may depend on the target. The companion page exposes formal statements and verification records; this briefing inspected the statement and paper, not a fresh build. [A03]

Lau's **version 2** gives an explicit refinement. With

$$
D_A=2^{2^{2^{163}}},\qquad c(t)=D_A^{-1}t^{-25/11},
$$

Theorem 1.3 states that for every cutoff `N`, at least `floor(c(t)N)` odd starts below `N` reach a prescribed positive target `t`, `3∤t`, within the stated logarithmic ordinary-clock budget. Corollary 1.6 deduces that density-one convergence to one would imply universal convergence. The source reports a Lean formalization; no independent replay is claimed here. [A04]

**Why this is consequential.** An exceptional orbit cannot simply be dismissed as a rare seed. Its entire ancestor basin must also fail. A positive-density ancestor theorem makes that basin visible to a density argument.

**Why this still does not solve Collatz.** “Almost all reach a threshold tending to infinity” and “almost all reach one” are different statements. The threshold cannot be frozen by substituting a constant into a theorem that requires divergence. Likewise, knowing a positive fraction converges does not imply the remaining fraction shrinks under repeated descent unless transport is controlled.

### An original quantitative bridge: compare the rates, not just the words

The following deduction is an original interface calculation. It is conditional on the stated external or repository population theorem, and it proposes an unproved survivor bound.

Suppose a least nonconvergent positive integer `m` exists. It is odd, because an even `m` immediately halves below itself. Choose a positive odd target `q` on its shortcut orbit with

$$
m\le q\le2m,\qquad3\nmid q.
$$

If `3∤m`, take `q=m`; otherwise take the next odd iterate if needed. One shortcut odd step produces a ternary unit at most `2m`; stripping any additional powers of two preserves the unit condition and cannot fall below `m` without contradiction.

Every predecessor of `q` fails to reach one, and every value on each such orbit is at least `m`. Otherwise a smaller positive input would fail, contradicting minimality. Hence a lower bound on predecessors of `q` becomes a lower bound for the **fixed-floor survivor set**

$$
E_m=\{n>0:\min_{j\ge0}T^j(n)\ge m\}.
$$

Lau v2 therefore implies, for natural and consequently logarithmic lower density,

$$
\underline d(E_m)\ge D_A^{-1}(2m)^{-25/11}.
$$

Now propose an upper bound

$$
\overline d_{\log}(E_M)\le C M^{-\beta}\qquad(M\ge M_0).
\tag{OPEN-FLOOR}
$$

If `β>25/11`, these estimates contradict each other for all sufficiently large `m`; an explicit finite range would remain. Conditional on PR180's stronger uniform predecessor statement `cX/q`, the analogous threshold is `β>1`.

This identifies a concrete ambition for stronger analytic machinery: a **power-saving tail in the fixed floor**, not merely a power saving in the initial cutoff. Those are different variables. Tao's fixed-floor estimate is of logarithmic order in the floor, which is too weak for this comparison. [A01, Theorem 3.1] To apply its odd-start formulation to $E_M$, use threshold $M-1$ and strip initial powers of two; summing the resulting geometric source weights changes only an absolute constant.

The enormous value of `D_A` matters to an effective final cutoff. For research triage, the exponent mismatch already shows why the currently cited results do not combine automatically. If a proposed estimate depends on `M` through an unspecified constant that can grow arbitrarily fast, it does not meet `(OPEN-FLOOR)`.

**First useful task.** Derive the weakest uniform tail bound needed from the precise population theorem one is willing to import. Keep the floor `M`, starting cutoff `X`, and available clock separate on every line.

**Stop rule.** Reject an argument that substitutes a moving floor `M=M(X)→∞` for a bound at one fixed hypothetical least counterexample and then changes the order of limits.

**Priority: very high.** This produces a precise closing target while preserving the conditional status of the new density literature.

## 4. New natural-density work: useful, but distinguish its targets

Shaik's October 2026 manuscript states natural-density-one descent to

$$
(\log n)^{A_{\rm FP}}U(n),\qquad A_{\rm FP}\approx9.9911,
$$

for prescribed positive `U(n)→∞`, with ordinary and shortcut logarithmic time estimates and control of the maximum height using another prescribed diverging function. Its proof is organized around finite parity counts and first passages counted among the original sources. It does not state descent below an arbitrary diverging threshold without the polylogarithmic factor. The paper and exposed theorem declarations were inspected; its formalization was not rebuilt here. [A05]

**Proposed use.** Its original-source bookkeeping is especially relevant to the repository's unsafe-transport problem. An agent should compare the exact mechanism that prevents repeated first-passage failures from being overcounted with the marked-return packets in PR183. The desired output is a finite pullback inequality for the actual source set, not a blanket invocation of “natural density.”

The main obstruction is that a repeated return packet is selected by its entire previous history. A finite-horizon theorem for most sources can leave a small set that contains every unresolved component. The question is whether the error can be made summable in an induction that preserves those same sources, or whether a structural alternative handles the remaining set.

A separate 2026 lead, Luo–Kolpakov–al-Jammas, advertises natural-density almost-boundedness through ternary residue mixing. The available search index exposed an abstract, but the full SSRN paper returned an access error in this run. It belongs on the **read-and-audit queue**, not among the inputs certified by this briefing. In particular, its conclusion should not be strengthened to density-one convergence to one. [A15]

**Priority: high for a targeted comparison; no automatic import.** Ask for a theorem-level explanation of how endpoint selection and original-source counting interact.

## 5. Krasikov–Lagarias: deep enough to be useful, concrete enough to certify

### The established result

Krasikov–Lagarias uses systems of difference inequalities indexed by ternary residue classes. A feasible positive solution of an associated linear program yields exponential growth in a logarithmic variable, hence a power-law lower bound for ordinary predecessor counts. Their Theorem 6.1 gives at least `X^0.84` predecessors of each fixed positive ternary-unit target for sufficiently large `X`. Theorem 2.2 is the reusable certificate interface. This is a historical verified baseline, not a claim about the best bound in November 2026. [A02]

**Plain-language mechanism.** Rather than guess that a large inverse tree grows quickly, assign weights to residue classes and prove that every legal branching step supplies enough weighted mass. A finite table of inequalities certifies an infinite family of inputs.

### Proposed translation

The attractive transplant is the certification architecture, not the particular exponent. A marked-survivor calculation could track states such as

$$
(\text{ternary residue},\ \text{binary precision},\ \text{clock budget},\ \text{height bin}).
$$

An admissible state must represent all ordinary inputs to which its inequality is applied. Transfers must include overflow states, unresolved guards, collisions, and paths leaving the displayed band. The lower-population and upper-survivor problems have opposite inequality directions, so the existing program cannot simply be relabelled.

One concrete experiment is to construct a small exact system for a **fixed floor** and a bounded precision. Ask whether a positive vector gives a contraction for all transitions, with an explicit boundary term for states requiring more precision. If it fails, obtain a dual obstruction identifying a collection of states that cannot be paid for with the chosen features. That obstruction can show an agent which additional carry or history coordinate is necessary.

The result of an optimization program is not automatically a proof. Export rational coefficients, verify every inequality independently, prove the abstraction covers the infinite integer domain, and retain boundary leakage. A numerical eigenvalue below one for a truncated matrix is especially unconvincing if the missing states are exactly the long rising excursions.

**First useful task.** Produce a tiny certificate where the arithmetic interpretation is completely explicit. Make the checker independent of the optimizer. Then enlarge the state space only to resolve a specific uncovered transition.

**Stop rule.** If every promising contraction disappears when overflow is retained, report that obstruction instead of renormalizing the truncated matrix.

**Priority: high.** It connects naturally to the repository's formal verification culture and can yield useful negative results.

## 6. Entropy inverse theorems: classify a failure of spreading

### The established machinery

Hochman's inverse theorem studies probability measures whose entropy grows very little after convolution. In its real-line formulation, most scales then have a special structure: one measure is nearly uniform locally, or the other is nearly atomic. His self-similar application relates dimension loss to extremely close cylinder maps. The theorem requires actual convolution of specified probability measures and quantitative scale hypotheses. It is not a theorem about arbitrary correlated sums. [A09]

**Plain-language mechanism.** Adding two independent clouds usually spreads them out. If it does not, there must be a reason. The theorem identifies what that reason looks like across many scales.

### Proposed translation

Split an inverse valuation word into blocks. The affine composition law gives an offset of the form

$$
F_{r+s}=F_s(\text{last block})+3^s2^{-A_s^{\rm last}}F_r(\text{first block}),
$$

where $A_s^{\rm last}$ is the valuation sum of the last $s$ steps. These are the additive offsets in the forward affine formula, even when the words were generated by an inverse construction.

with the order fixed by one's convention. Under an independent block model, conditioning on the multiplier can expose a genuine convolution. Under actual survivor selection, the blocks may become correlated. The first task is to measure or prove a bound on that correlation, not to cite the inverse theorem prematurely.

A useful exploratory object is the distribution of exact offsets of legal inverse words that satisfy all current guards and have not yet obtained a smaller merger partner. If its scale entropy stays low, ask whether the concentration corresponds to a common carry, repeated affine map, near-cycle relation, or one arithmetic residue tower. Such structure might permit a deterministic certificate. If entropy grows, ask whether it gives enough ordinary source diversity to beat the required survivor bound.

This is a prospective **dichotomy**, not a completed reduction. A successful version would say: either a selected packet expands in an explicitly useful sense, or every nonexpanding packet falls into a finite or otherwise manageable family of arithmetic obstructions. The latter family must still be handled. Full Hausdorff dimension or full entropy dimension alone does not imply every integer is covered.

The ambient space also matters. Hochman's quoted theorem is over the real line. The repository needs ternary residue laws coupled to binary valuation and real height. A faithful transplant needs a suitable finite-ring or local-field entropy theorem, or a justified real embedding at each finite scale. “Both contain powers of two and three” is not that bridge.

**First useful task.** For exact bounded inverse words, compute block mutual information and offset collision counts before and after survivor selection. Look for stable concentration mechanisms. Use the experiment to formulate a lemma, not to announce random behavior.

**Stop rule.** If the selection makes one block nearly determine the other, abandon an independence-based convolution proof for that selection or refine the conditioning explicitly.

**Priority: medium; potentially high upside.** A structure theorem for the exceptional packet would address a real weakness of average estimates.

## 7. Entropy decrement and multiplicative correlations: a long shot with a precise question

### The established machinery

Tao's logarithmically averaged two-point Chowla theorem proves cancellation for products of the Liouville function on distinct affine forms. Its entropy-decrement step finds a scale with small mutual information between a block process and a residue variable. Multiplicativity, approximate stationarity, and number-theoretic correlation estimates are integral to the proof. This is a different use of entropy from the collision-entropy step in his Collatz paper. [A10]

**Plain-language mechanism.** Two kinds of information cannot keep revealing a substantial new amount about one another at every scale, because the total information budget is limited. At some scale, they become sufficiently weakly dependent to permit averaging.

### Proposed translation

The natural Collatz question is whether the leading binary phase and the trailing binary digits can remain strongly correlated forever on an escaping orbit or on a persistent survivor packet. The phase determines proximity to the band. The trailing digits determine how much division by two the next odd step provides. The repository has substantial phase information; it lacks the needed valuation control.

Define the variables before trying to apply the analogy. For example, under a precisely specified source law, let `X_h` record an orbit block together with band-height information and let `Y_h` record a residue modulo `2^h`. One would seek a genuine scale relation forcing persistent mutual information to consume an impossible entropy budget. The law must be consistent across scales, and all survivor conditioning must remain visible.

There is no current reason that these variables satisfy the approximate stationarity or multiplicative covariance used in Chowla. The basin indicator is not known to be a multiplicative function. A theorem averaging `λ(an+b)` over ordinary integers cannot be substituted for a statement about valuations along one deterministic Collatz trajectory. The exact identity `v_2(3x+1)` is local in the trailing digits; it does not acquire probabilistic independence because the leading phase is equidistributed.

The genuinely useful possibility is methodological: construct an information budget for the **joint** leading/trailing process, with an alternative that yields an arithmetic obstruction. This would be a new theorem, not an application of Chowla's conclusion.

**First useful task.** Prove one nontrivial consistency or covariance identity for the proposed `(X_h,Y_h)` laws. If none survives the first return selection, redesign the law before pursuing the entropy calculation.

**Stop rule.** Do not continue a proof that needs the unknown valuation sequence to be stationary or independent as an initial hypothesis.

**Priority: speculative.** The question is aligned with the gap, but the missing structural bridge is substantial.

## 8. Sum–product and expansion: useful warnings and a possible structural tool

### Three different theorems, three different hypothesis sets

| Machinery | Established statement in brief | Direct mismatch with the Collatz application |
|---|---|---|
| Bourgain–Katz–Tao sum–product | A set of intermediate size in a prime field must expand under addition or multiplication. [A11] | `Z/3^rZ` is a ring with ideals, not a prime field; a survivor set is not known to be stable under the required operations. |
| Bourgain–Gamburd expansion | Fixed generators of a non-elementary subgroup of `SL_2(Z)` yield an expander family after suitable prime reductions. [A12] | Collatz branch maps are affine, hence represented by upper-triangular matrices preserving a common point at infinity. The quoted non-elementary hypothesis is unavailable. |
| Breuillard–Varjú affine walks | For `x_{k+1}=a x_k+b_k` over a prime field with independent noise, strong mixing holds for most multipliers; sharper cutoff results carry further qualifications, including GRH in the stated theorem. [A13] | The multiplier is prescribed, the moduli are prime powers, and the “noise” of an actual selected orbit is neither fresh nor independent. |

**Plain-language mechanism.** Addition and multiplication tend to destroy different kinds of structure. A set that resists both must be unusually organized. Expansion translates this inability to remain organized into rapid spreading of a random walk.

### Proposed translation

The plausible application is to a **family of legal inverse transformations**, not directly to the deterministic forward map. One might prove that a packet of inverse words cannot concentrate simultaneously in too few ternary residues and too few real-height bins, unless its affine maps share a rigid relation. Such a relation could become an exact merger or cycle constraint.

Before looking for a giant theorem, write the actual branch matrices. If they remain triangular after every permitted change of coordinates, invoking a semisimple-group expansion theorem is a category error. Embedding the matrices into a larger group does not help unless the larger random walk is generated by legal operations that retain the Collatz arithmetic interpretation.

At prime powers, test concentration in ideals such as `3^j Z/3^r Z`. These are genuine algebraic obstructions to naive finite-field intuition. An adapted sum–product theorem must state how such concentration is excluded or incorporated. Likewise, a theorem valid for most multipliers cannot justify one specified multiplier merely because it appears generic numerically.

A productive negative result would show that all offset packets allowed by a particular finite abstraction lie in a structured affine family, so that this abstraction cannot yield a spectral gap. A productive positive result would exhibit a precise legal branching operation that breaks that structure while preserving ordinary source height and injectivity.

**First useful task.** Build the smallest exact finite model of the permitted inverse operations, identify its invariant quotients and ideals, and test whether a proposed expansion estimate survives them. This is a diagnostic, not evidence of global mixing.

**Stop rule.** Stop at any appeal to “noncommutativity” without checking non-elementarity/Zariski density, or to “randomness” without specifying the independent variables.

**Priority: low-to-medium.** Potentially valuable for classifying structured obstructions; an immediate expander proof of Collatz is not supported.

## 9. Leading-digit equidistribution and random models: useful control cases

Lagarias–Soundararajan gives a quantitative finite-horizon Benford result for most initial seeds, with `X≥2^N`: the first `N` shortcut iterates have small leading-digit discrepancy except for a controlled fraction of starts. Its quantifiers concern many seeds at a specified horizon. They do not give an infinite-time theorem for an arbitrary fixed seed. [A07]

Kontorovich–Lagarias explicitly separates rigorous finite parity facts from stochastic predictions of long-time behavior. Their random models are valuable because they make detailed predictions that can be tested, while clearly identifying which independence assumptions belong to the model. [A08]

Gonçalves–Greenfeld–Madrid extends Tao's strategy to a family of generalized Collatz maps under explicit arithmetic and drift hypotheses, and isolates a renewal-process theorem. This is a source for modular proof architecture and control examples; it remains an almost-all conclusion. [A14]

**Proposed use.** Every proposed statistical closure mechanism should be run through a control map where the argument's assumptions can be checked and nonconvergence is possible. If it would prove all trajectories converge for an expansive control system merely because its phases are well distributed, it is missing a drift or integrality hypothesis.

For the actual band problem, phase information has a particularly sharp limitation:

$$
\log_2U(x)-\log_2x=\log_23-a(x)+\log_2(1+1/(3x)).
$$

Reducing modulo one removes the integer `a(x)`. That integer is exactly what controls the sign of the large-scale drift. Therefore improving phase equidistribution alone does not recover the missing height information. A useful new theorem must couple phase to valuation, reconstruct accumulated division, or obtain an independent descent/merger certificate.

**First useful task.** When an agent proposes a phase-based argument, require an explicit line recovering a bound for `Σa(x_j)` or a smaller ordinary merger. If it supplies neither, the argument has not yet reached the global obstruction.

## 10. A short handoff queue for agents

| Task | Deliverable | Evidence that would count as progress |
|---|---|---|
| A-T1: joint-law audit | A theorem contract for PR180 with precise random variables, normalization, central-clock floor, and distinct-source count | Either an independently reconstructed implication or a specific unsupported estimate with its required strength |
| A-T2: quantitative population/survival interface | A formal statement of `(OPEN-FLOOR)` sufficient under Lau v2 or the stronger PR180 population hypothesis | Correct floor/cutoff order, ordinary-map conversion, and explicit finite-range implication |
| A-T3: selected-packet entropy | Exact block laws and collision/mutual-information computations retaining all guards | A stable concentration mechanism or a provable convolution/decoupling lemma |
| A-T4: finite inequality architecture | Rational certificate or dual obstruction for a modest state space | Full treatment of overflow, collisions, and source weights; no truncated-matrix renormalization |
| A-T5: compare natural-density first passages | A source-preserving pullback inequality extracted from Shaik's exact statement | A real improvement over the already derived PR183 first-return bound, with repeated-return assumptions stated |
| A-T6: structured obstruction search | Legal affine transformations and their invariant quotients/ideals | A verified reason an expansion theorem does or does not apply, rather than a thematic analogy |

The most valuable negative outcome is a clean theorem that a proposed abstraction cannot carry the desired conclusion. It should preserve the actual obstructing family and say which additional information a future proof must retain.

## Sources and inspection scope

Source IDs are stable within this briefing. The consolidated [source manifest](SOURCES.json) records URLs, theorem locations, versions, and evidence scope. Statements above are paraphrased narrowly; the repository translations and proposed tasks are original analysis.

- **A01.** Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), e12; corrected [arXiv:1909.03562v7](https://arxiv.org/html/1909.03562v7), 16 July 2026. Inspected Theorem 1.3, Proposition 1.17, Remark 1.16, Theorem 3.1, and Sections 6–7.
- **A02.** Ilia Krasikov and Jeffrey C. Lagarias, *Bounds for the 3x+1 Problem using Difference Inequalities*, Acta Arithmetica 109 (2003), 237–258; [arXiv:math/0205002](https://arxiv.org/pdf/math/0205002). Inspected Proposition 2.1 and Theorems 2.2, 5.1, 6.1; no new replay of their optimization certificates.
- **A03.** Lech Mazur, *Positive Lower Density of Collatz Predecessors*, version 1.0, 6 September 2026. [Paper](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf) and [formal statement](https://www.proofatlas.ai/proofs/artifact.collatz.predecessors_positive_lower_density.v001.html). Inspected theorem and fixed-target counting argument; source-qualified, not independently rebuilt.
- **A04.** Kenny Lau, *Explicit positive lower density for the Collatz Conjecture*, [Hexagon 2610.00249v2](https://hexagonmath.org/pdf/2610.00249v2), 14 October 2026. Inspected Theorem 1.3, Corollary 1.6, and the overview of legal words, source distinctness, selected census, and seed construction; no Lean replay.
- **A05.** Idris Ali Shaik, *Polylogarithmic Descent for Almost All Collatz Orbits in Natural Density*, manuscript v4.0.2, 4 October 2026. [Full text](https://shaikidris.github.io/polylog/paper/). Inspected Theorem 1.1 and the stated source-counting organization; no full independent proof audit or Lean replay.
- **A07.** Jeffrey C. Lagarias and K. Soundararajan, *Benford's Law for the 3x+1 Function*, J. London Math. Soc. 74 (2006), 289–303. [Author preprint](https://arxiv.org/pdf/math/0509175). Inspected Theorem 2.1 and its quantifiers.
- **A08.** Alex V. Kontorovich and Jeffrey C. Lagarias, *Stochastic Models for the 3x+1 and 5x+1 Problems*, in *The Ultimate Challenge* (2010). [Author preprint](https://arxiv.org/pdf/0910.1944). Inspected model/rigorous-result separation and Sections 2–3; used as an author-written source on model scope.
- **A09.** Michael Hochman, *On self-similar sets with overlaps and inverse theorems for entropy*, Annals of Mathematics 180 (2014), 773–822. [Author preprint](https://arxiv.org/pdf/1212.1873). Inspected Theorem 2.7 and surrounding definitions; no claim of an automatic finite-ring extension.
- **A10.** Terence Tao, *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations*, Forum of Mathematics, Pi 4 (2016), e8. [Author preprint](https://arxiv.org/pdf/1509.05422). Inspected Theorem 1.2 and Lemma 3.2; methodological connection only.
- **A11.** Jean Bourgain, Nets Katz, and Terence Tao, *A sum-product estimate in finite fields, and applications*, GAFA 14 (2004), 27–57. [Author preprint](https://arxiv.org/pdf/math/0301343). Inspected Theorem 1.1 and prime-field assumptions.
- **A12.** Jean Bourgain and Alex Gamburd, *Uniform expansion bounds for Cayley graphs of SL₂(Fp)*, Annals of Mathematics 167 (2008), 625–642. [Publisher PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v167-n2-p07.pdf). Inspected Theorem 1; the affine Collatz matrices do not meet its non-elementarity hypothesis.
- **A13.** Emmanuel Breuillard and Péter P. Varjú, *Cut-off phenomenon for the ax+b Markov chain over a finite field*, Probability Theory and Related Fields 184 (2022), 85–113. [Author preprint](https://arxiv.org/pdf/1909.09053). Inspected Theorem 1 and the qualified cutoff discussion; do not erase “most multipliers” or GRH from the relevant statements.
- **A14.** Felipe Gonçalves, Rachel Greenfeld, and José Madrid, *Generalized Collatz Maps with Almost Bounded Orbits*, Indiana University Mathematics Journal 74 (2025), no. 1. [Author preprint](https://arxiv.org/pdf/2111.06170). Inspected the generalized result's scope and Theorem 1.9 renewal interface; not used to assert pointwise convergence.
- **A15.** Yi Den Luo, Alexander Kolpakov, and Humam al-Jammas, *Ternary Residue Mixing and Natural Density Descent for the Collatz Map*, SSRN 7434138, manuscript dated 1 August 2026, posted September 2026. [Source landing page](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7434138). Abstract/metadata retrieved; full-text access failed. This is an audit lead only.
