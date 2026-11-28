# Source refresh during the nine-hour pass

This is a focused record of primary sources that changed the research choices,
not an exhaustive literature survey. Dates are publication or revision dates
reported by the sources. The original conjecture remains unresolved here.

## A prior result changes the mass-gain claim

[Weaver 202/v1](https://rstation.ai/problems/collatz/papers/202), dated
November 22, already disproves universal inverse-logarithmic lower bounds
for sibling density and for the gain at a first odd doubling. Its Theorem 1
allows `2^s 3^k ≤ (log Y)^P` for every fixed `P`, and has constant-factor
two-sided estimates, a positive proportion of the specified progression,
and synchronized disjoint subfamilies. Root read its complete proof and
scope section. The first indication of an inverse-log refutation in this
pass was therefore a rediscovery, and is not presented as a new solution.

The new [polynomial-budget deduction](../../research/astra-global-rigidity-20261128/mass/POWER_SMALL_SIBLING_DENSITY.md)
instead allows `2^s 3^k ≤ Y^ε`, at the cost of `exp(O(sqrt(log Y)))` upper
factors. The distinct input is the uniform limiting landing-set majorant
in [Weaver 102/v1, Theorem 1](https://rstation.ai/problems/collatz/papers/102).
The proof explicitly retains that analytic premise and the fixed-total and
signed-column inputs of [Paper 200/v2](https://rstation.ai/problems/collatz/papers/200).
These rStation sources are treated as supplied, unrefereed mathematical
inputs; reviewing their interfaces does not constitute a formal verification
of their entire dependency chain. The fixed-positive-main-density question
remains outside these small-gain constructions.

## Very large individual computations

Andreas-Stephan Elsenhans's [*Numerical verification of the Collatz conjecture
for billion digit random numbers*](https://link.springer.com/article/10.1007/s40993-026-00811-5)
was published in *Research in Number Theory* on November 24. Root read the
algorithmic and complexity sections. The method composes exact affine
standard polynomials efficiently and supports enormous individual checks.
The quasilinear bit-complexity statement in Theorem 5.8 assumes the starting
integer belongs to the specified class with linearly bounded stopping time.
It does not prove that every integer belongs to that class. This is useful
for future unusually large certificates, but it does not supply the missing
universal descent theorem. This pass therefore kept its main effort on the
structural obstructions rather than starting a large random scan.

## Measure rigidity and the parity gap

[Paper 170/v1](https://rstation.ai/problems/collatz/papers/170), dated
November 18, establishes the stated approximate multiplication-by-two and
multiplication-by-three invariances for averaged binary windows, then applies
Rudolph's measure-rigidity theorem. Root also read its counterexamples and
the lower-digit dependence formula. Biased independent parity laws can have
Lebesgue binary-window limits for every bias strictly between zero and one.
The actual next parity depends on all lower digits, not merely on a bounded
window. Thus window equidistribution alone supplies no upper bound below the
critical density of odd steps, and positive entropy for a particular integer
orbit is a separate missing premise. This blocks a tempting attempt to turn
the solenoid/window results of this packet directly into descent.

## Arithmetic tools and their boundaries

[Paper 138/v1](https://rstation.ai/problems/collatz/papers/138), dated
November 13, already develops positive shifted carries, prime-power return
constraints and multiplicative-rank growth. Its related mechanism is credited
in the independent-sibling note. Rank growth is compatible with known
terminating controls and does not itself limit cumulative prime transport.

The moving-coefficient cycle argument uses Grieve and Wang's published
[*Greatest common divisors with moving targets and consequences for linear
recurrence sequences*](https://arxiv.org/pdf/1902.09109), especially Theorem
1.2 and the fixed-character alternative in its proof. Root checked the
positive fixed degrees, coprimality, nonzero constant term, small coefficient
heights, and the exceptional-subgroup condition in this application. The
number of sparse terms remains fixed. The result supplies no uniform bound
when that number grows with the clock.

The November 23 [Chudnovsky preprint](https://arxiv.org/html/2611.30820v1)
was read for its stated rational-logarithm estimate and reported formal
endpoint. Its full ancillary Lean project was not rebuilt here. The
geometric-return application in checkpoint 6 consequently keeps that recent
estimate as an explicit conditional premise; its appearance in a repository
with separately checked Lean files does not certify the external theorem.

## A sharply stated counting question

Polson and Sokolov's *On the Collatz Conjecture*, edition 1, records the
near-maximal correction-word question R9 and the untruncated cocycle
question R8 in its [exact November 10 source](https://github.com/VadimSokolov/collatz/blob/5840497a23fc0d64127b850aea68862d7c93f2b7/book/chapters/ch10h_ratchets.tex),
tag `v1.4.0`. Root retrieved that complete file and independently checked
the word definition, forced last exponent, pressure normalization and
question statements; a second agent did the same. The near-one rate in
checkpoint 8 is a new deduction relative to that exact source. The depth
model and proposed epsilon-log-inverse-epsilon scale belong to the book.
A targeted search found no additional result resolving that question;
this is not an exhaustive priority certification. The proof uses no
unverified density or number-theory premise from other chapters.

## First coefficient-crossing restrictions

De Jesús's [November 25 revision](https://hexagonmath.org/2611.00459v4)
gives restrictions on the first coefficient crossing in a putative
non-descending orbit. Root read the primary PDF's relevant proofs and
scope, including the finite odd-run regime, restart reductions, the
repeated-110 family and a square-prefix restriction. These can exclude
structured first crossings; they do not bound every crossing's complexity.
The claimed verification status of that unrefereed source was not treated
as an independent Lean rebuild, and none of its numerical thresholds is
used as a premise of the near-maximal entropy proof.

## Full word limits and concurrent arithmetic comparison

The same exact Polson–Sokolov source now supplies the questions answered by
checkpoint9: the full M4 count formula and both parts of R8, retaining the
R9 expansion. Kingman's scalar subadditive theorem is used with explicit
boundedness hypotheses; root read the original paper's primary statement
and Steele's author-hosted proof. The new critical transition argument is
proved directly and does not invoke a random-environment wetting theorem.

Root opened [Weaver160/v1](https://rstation.ai/problems/collatz/papers/160)
and [Weaver163/v1](https://rstation.ai/problems/collatz/papers/163), including
the latter's higher-order cancellation fixture and stated unrestricted-cost
question. Those are the precise antecedents of the new product arguments.
The pair theorem and bounded-division all-order theorem are credited.
Root also read [Paper137 Lemma4](https://rstation.ai/problems/collatz/papers/137)
for the earlier maximal-coefficient gcd criterion.

A GitHub refresh froze PR212 at 0172f15109b8749c14fed272e733c97a5a0f7d24,
PR214 at be010b2874b88267e710666d3c5f963a0c994356, and PR215 at
121054cf6569859585ede5c2d6e024eb2d97bbc5. Main remained
ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a. Their current front-door metadata
was read; this is not a review of all their new proofs. In addition, root
read PR215's complete moving-sparse-sum, moving-template and moving-residue
notes at d444e332d111115daa650c58a917dd46dacd4c1e. That prior publication
changes the attribution of the overlapping checkpoint7 method, as now
explained in `MOVING_FULL_MODULUS.md` and the checkpoint9 review.

## Checkpoint 10: native counts and full measures

The fixed-even-budget argument uses the rational S-adic Subspace Theorem
in the form of Theorem 5 of Varju's
[*On the multiplicative group generated by two primes in Z/QZ*](https://arxiv.org/pdf/2104.04367v2).
Root read that primary statement, including its integer-vector formulation
and finite exceptional-subspace conclusion. The original 1977 DOI could
not be retrieved. This is an external classical theorem, not one of the
finite Lean lemmas in the packet.

Root re-read the actual finite-source comparison and certified-stage rank
bounds in [Weaver102](https://rstation.ai/problems/collatz/papers/102),
the unit floor and finite ternary densities in
[Paper200](https://rstation.ai/problems/collatz/papers/200), and the prior
finite forward-orbit containment in
[Paper202](https://rstation.ai/problems/collatz/papers/202).
The new full-measure deductions retain these as explicit premises.
Paper200's earlier unbounded excess and Paper202's earlier containment are
credited directly; neither is claimed as new here. Root also read the
pinned PR193 canonical inverse-path construction and PR213's strict
no-return floor where the new acquisition and stopped-law arguments use
them. The exact book source above asks for an upper bound in R6; failure
of a matching two-sided fair-coin rate is not a disproof of that question.

A further November 28 search opened the abstract of
[*Collatz orbits of almost all primes attain almost bounded values*](https://aixiv.online/abs/2611.01542).
The catalog's word "proves" refers to a partial result, not universal
Collatz convergence. Its reported Lean package has not been rebuilt here,
and none of checkpoint10 depends on that claim. The same refresh opened
[Paper227](https://rstation.ai/problems/collatz/papers/227), whose sparse
sufficient-set construction is already credited in `PRIME_MIDPOINTS.md`,
and [Paper231](https://rstation.ai/problems/collatz/papers/231), which states
a large finite completeness interval for paradoxical sequences with
explicit record-table and census inputs. That finite computational claim
has not been replayed in this pass and does not cover all lengths.

## Checkpoint 11: exact antecedents and broader recent work

Root opened [Weaver114/v1, section 2](https://rstation.ai/problems/collatz/papers/114/v1), which already proves the near-dyadic crossing for every separation of repeated reduced clocks. That priority is explicit in the new all-sublap notes. Root also read [Weaver191/v2](https://rstation.ai/problems/collatz/papers/191/v2), including its actual finite-source record estimates, for the lifetime-deficit deduction. The compressed-parity argument reuses the primary rational S-adic statement in Varju's Theorem 5 cited above. The new denominator consequences use Corvaja and Zannier's [primary paper, Corollary 1](https://arxiv.org/pdf/math/0311030), whose multiplicative-independence hypothesis is checked separately at each application.

For the full-mark results, root read the complete native-transfer and Mellin-rigidity notes and the Rajchman statement at PR215 commit `121054cf6569859585ede5c2d6e024eb2d97bbc5`. Root also opened [Weaver124's counted fusion theorem](https://rstation.ai/problems/collatz/papers/124). These remain identified analytic inputs. The row-resolved theorem and the independent-convolution deduction do not constitute an independent rebuild of all earlier source results.

The recent prime-start preprint was examined beyond its catalog entry. Root downloaded the primary [paper at Zenodo 24286158](https://zenodo.org/records/24286158) and the [supplied Lean archive at Zenodo 24286141](https://zenodo.org/records/24286141), checked the archive's published MD5, and read the final theorem definitions, their audit equalities, the build script and the dependency pins. The five final statements have genuine positive-orbit minima and the stated weighted prime/rough-number quantifiers. The author reports a Lean and lean4lean check. This pass has **not** replayed that project: it requires a distinct Lean/Mathlib release and substantially more dependency storage. No result in this checkpoint takes the new prime theorem as a premise. Its conclusion concerns almost all starts in specified arithmetic populations, not every positive integer.

Root also downloaded the primary [November 8 Noubissie preprint](https://arxiv.org/abs/2611.11341), *On quantitative aspects of ideal membership certificate and GCD inequality for polynomials evaluated at almost units*. Its Theorem 9 bounds the number and degree of exceptional hypersurfaces in a quantitative small-gcd statement. It does not bound the maximum height of points on those exceptions. In the difficult native rotation problem, a long arc's additive carry can have height proportional to the entire clock and need not be an almost S-unit. Neither inserting that carry as a new coordinate nor quoting a finite number of exceptional hypersurfaces supplies the missing uniform transversality. The preprint is being assessed as a possible tool; it is not a new certified premise of a claimed cycle exclusion.

For the unrestricted higher-product question, root read the primary statements and qualifications in Fuchs's [*Polynomial-exponential equations involving multi-recurrences*](https://math.sbg.ac.at/fuchsc/publ/peeimr4.pdf). Its integral-root classifications require dominance, simple-root and comparable-parameter hypotheses. Slow coefficients and several competing scales in the remaining product problem do not automatically satisfy them. The previous failed algebraic-norm shortcut is not repaired merely by citing that classification.

## Checkpoint 12: native records, simultaneous tails and source dependence

Root read [Weaver211/v1, Theorem2 and section2.3](https://rstation.ai/problems/collatz/papers/211/v1) for the existing bounded-discrepancy first-visitor construction and its inverse-offset envelope. Its (J) premise remains in the first sharpness proof. The new balanced-block route instead uses [Weaver127/v1, Theorem5 and Corollary8](https://rstation.ai/problems/collatz/papers/127/v1), the finite-policy construction through equation(4) of [PR215's pinned entropy-transfer note](https://github.com/GettysburgResearch/collatz/blob/121054cf6569859585ede5c2d6e024eb2d97bbc5/research/astra-nine-hour-20261128/machinery/phase4/TILTED_ENTROPY_TRANSFER.md), and Leen's qualitative tilted absolute-continuity input. Root retrieved [Leen's primary TeX](https://zenodo.org/api/records/23268832/files/tilted-syracuse-laws.tex/content), SHA-256 `3855fc67c0c30c0e8e78af3de93fd85279d4376f2cb7c1e5d63d24433ce70afc`, and read Theorem B(a), the interval proof and its explicit formalization boundary. The author reports a kernel-checked general criterion in a separate development; its interval certificate and continuity specialization are written inputs. This pass has not rebuilt that external formal development.

For the signed shared-block arguments, root opened [Bilu's primary survey, Theorems2.3 and2.3′](https://www.numdam.org/item/AST_2008__317__1_0.pdf), including the fixed-place S-integer normalization, and [Weaver173/v1](https://rstation.ai/problems/collatz/papers/173/v1). Root also read PR212's complete six-mismatch, eight-near-circuit and odd-rotation-complexity proofs at commit `505d3fe782922904e86477990cc5d41e9110edda`; these antecedents are directly credited. This checkpoint's independent-valley result does not claim an all-profile rotation exclusion.

For the clock and rectangle deductions, root read the exact first-hit row law and [PR146's growing-additive-gap comparison](https://github.com/GettysburgResearch/collatz/blob/0410811710af2f7da71522ec67233528048adb9a/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md) at its pinned source. The actual-source crop, all finite residues, early-hit removal and common component are retained. These conclusions do not assume independence of the four corrected marks.

A read-only concurrent refresh recorded PR212 at `21f5cfef697de0941200286abaef2f8373d6915a`, PR214 at `d020c998fa1eb361182ae520bf1af3148afffb8b`, and PR215 at `5845a208956bce43b80cf6b4adbadb849d35c15d`. Main remained `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Root read their front-door descriptions, and separately read PR212's multiplier Bernoulli joining and full `RAW_LANDING_MOMENTS.md` / `ALL_SCALE_FIBRE_DENSITY.md` notes, the latter two at `e55fb7cac646013f143b563014ae97b105bc7547`. The multiplier independence transfers to ordinary sources only before the binary resolution horizon. It does not independently control postcritical native hit clocks. Root also read PR215's full `UNTRIMMED_RENYI_ENERGY.md`. The overlapping complete-measure moment conclusions are explicitly credited; their sharp logarithmic growth is stronger in the stated order range than this packet's unspecified polynomial-logarithmic bound.

The downloaded prime-start Lean package's manifest was checked against all 128 listed files, including their sizes and SHA-256 digests. The manifest hash is `26ef6c98b2280ec5255bbe8118132bc16d6eb63dd5ffa5bd786d94fd9e97a23e`. This validates the archive against its own supplied manifest, not the external theorem or an independent compiler build.

For the remaining arbitrary-order product problem, root read [Corvaja--Zannier, *S-unit points on analytic hypersurfaces*, Theorem1 and its proof](https://numdam.org/item/10.1016/j.ansens.2004.09.003.pdf). Its analytic substitution requires the total coordinate height to be controlled by the logarithm of the reciprocal of the largest small coordinate. Unbounded slower variables in the remaining native product problem do not automatically satisfy that uniform condition. The fixed-order result is not upgraded by citing this theorem without that hypothesis.

## Checkpoint 13: the precise native rotation question

Root opened [Wren218/v3, section7](https://rstation.ai/problems/collatz/papers/218) and the exact [Armstrong explicit-rate question](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/questions/rotation-distance-growth.md). Wren attributes the native odd-clock question to Armstrong; its shortcut-clock bounds do not transfer unchanged. Root separately fetched the complete [qualitative finite-exceptions question](https://github.com/stgoa/collatz/blob/d99505da4bc51849169cce0a7a46f0fce302afd0/areas/cycles/questions/rotation-distance-finite-exceptions.md), which explicitly accepts an ineffective proof for every fixed bound, and the complete related mismatch-chain Ridout criterion. The new theorem answers that qualitative assertion while retaining an ineffective threshold; it does not supply the explicit diverging function requested by the first question. The prior six-mismatch and eight-near-circuit work in PR212 remains directly credited.

The proof uses the classical Subspace Theorem in [Bilu, Theorems2.3 and2.3′](https://www.numdam.org/item/AST_2008__317__1_0.pdf), with fixed rational forms and rational S-integer points. Root re-read both normalizations and the corresponding discussion in [Weaver173/v1, section2](https://rstation.ai/problems/collatz/papers/173/v1). The slope-sequence and finite-translate method is credited to that antecedent. The new ternary valuation grouping, movable endpoint choice and chronological real product are reconstructed in the review. Neither this external theorem nor the general two-logarithm minimum bound is Lean-formalized in the packet.

## Checkpoint 14: precise transcendence and substitution precedence

Root read Weaver173's finite graph and short-phase argument directly in [§3 of v1](https://rstation.ai/problems/collatz/papers/173/v1), and checked the algebraic-coefficient fixed-place Subspace Theorem against the primary formulation already recorded above. The [earlier post6](https://rstation.ai/r/collatz/posts/6) has both an unrestricted finite-ratio threshold and, in its later discussion, a frequency-sensitive criterion covering every finite ratio when the frequency exists below the critical value. Its all-Sturmian consequence therefore predates this packet. The new algebraic statement removes the finite-ratio and frequency restrictions simultaneously; it retains Weaver173's rational theorem as a separate input. The [De Jesús v2 primary record](https://hexagonmath.org/2611.00108v2) describes characteristic Sturmian words and their shifts in its specified slope interval. That record and abstract were inspected for precedence; its external Lean development was not built here.

For the substitution theorem, root read Theorem 1 of the primary [Christol–Kamae–Mendès France–Rauzy paper](https://www.numdam.org/item/10.24033/bsmf.1926.pdf), using a downloaded PDF and extracted text when the web text endpoint failed. The PDF SHA-256 is `ca6bc2485bca42d07fd0a47084f2f282fb58427872f279296d2665bcd824cf40`. The [author's IBM publication record for Cobham](https://research.ibm.com/publications/on-the-base-dependence-of-sets-of-numbers-recognizable-by-finite-automata) states the base-independence conclusion; the original paper's full text was not retrieved. Root also read the relevant auxiliary-function and height-comparison portions of [Flicker's classical Mahler paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/93A86BEDCE91224C8E94E1E18D37A37B/S144678870001209Xa.pdf/algebraic-independence-by-a-method-of-mahler.pdf). The packet claims a specific uniform subshift application, not a new general Mahler method. [Weaver16 v3](https://rstation.ai/problems/collatz/papers/16) already excludes aperiodic positive rational automatic and primitive substitution fixed words in its stated scope. The new approximation bound is uniform over the whole subshift and varying algebraic approximants of each fixed degree.

The matching-mass result is compared with [Weaver174](https://rstation.ai/problems/collatz/papers/174), whose stated concentration inequalities concern constant-exponent-one groups and selected individual falls. Here each matching interval may have an arbitrary internal native word and compares distinct phases. The narrow rational comparison uses the exact PR212 construction and keeps its limitations explicit. No result of another active PR is merged or silently counted as a new theorem of this pass.

## Checkpoint 15: marked mixing, exact denominators and current neighboring work

Root directly read [Weaver–Wren48 v2, §8](https://rstation.ai/problems/collatz/papers/48), especially (60), the pair-total conditioning before (63), and (65)–(69). The source permits the specified fractional excess ternary precision and uses counting mass-vector norms; its lifting map has norm one. The new path-minimum extension is proved in this packet rather than claimed as an existing scalar theorem. Root also read [Weaver9 v2, Proposition13, formula (38), and AppendixB formula (B3)](https://rstation.ai/problems/collatz/papers/9), and [Weaver211 v1, TheoremA.1 and its (J) qualification](https://rstation.ai/problems/collatz/papers/211). The ordinary bridge, basin density and counted coalescence interfaces remain those already identified in the packet. The exact terminal-mark argument preserves their scope.

The entire [PR212 independent-clock construction at 505d3fe](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/INDEPENDENT_CLOCKS.md) was read, including the complete numerical denominator, physical realization, prime-marker primitivity, and both parameter diagonals. The inverse-mismatch upper order and shaped diffuse template explicitly use that construction. Its earlier narrow examples are not recast as new examples meeting every ordinary-height restriction.

The [05:44 UTC metadata snapshot](checkpoint15/source-refresh.json) records PR211 at 4b44cded, PR212 at 42a7493a and PR215 at 4f33ecc2. Their current opening reports were read. PR215's body still named its prior 5845a208 checkpoint while its actual head was newer; the snapshot preserves the actual head. These metadata checks do not independently verify the newly advertised proofs or import their formal counts. Both neighboring heads were fetched for the research lanes to inspect. No neighboring branch or main was modified.
