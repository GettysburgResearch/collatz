# Review of the latest Collatz frontier

2026-11-24. **The full conjecture remains OPEN.** This is a source-pinned research review and a record of new deductions, not acceptance of entire branches. Exact heads and trees are in [SOURCE_HEADS.json](SOURCE_HEADS.json). Five GPT-6.2 Astra workers and the coordinating agent pursued separate mathematical and formalization tasks. Internal reconstruction is not an external referee report.

## What the latest work actually supplies

The source graph has several independent approaches. A complete proof could close any genuinely exhaustive route; it need not combine every packet. The current strongest connections are these:

| Source | Mathematical contribution relevant here | First unsupported global step |
| --- | --- | --- |
| PR146, `f431078244e868dc699fad011044f0d5e7f76437` | Exact basin and multiplier-five interfaces; growing intervals can synchronize at ordinary targets with controlled finite clocks. `WHOLE_INTERVAL_SYNCHRONIZATION.md` gives a median clock of order log-squared interval length and long blocks of failures conditional on a separating component. | No opposing upper bound on actual failure blocks, and no complete successful smaller-source construction. Random low-bit sampling is not a property of each fixed source. |
| PR173, `fa0c9e2a2851e6324391e39c17afcb5913185aec` | Every ordinary orbit has a bounded-time visit to the specified density-zero dyadic band. | A visit is not descent or a lower-rank merger. |
| PR174, `c92cd473de3b85ceb945702a726d2eb7350a6af8` | A dependency-free formal reduction to the named closure obligation. | The obligation remains a hypothesis of the convergence conclusion. |
| PR175, `67664c6bf555bf7f7fcec987acb79500071dce4b` | Unconditional orbitwise counting, finite correction products, cycle budgets, and exact mixed-place normalization. | Neither sparse orbit values nor a convergent reciprocal moment excludes that orbit. |
| PR176, `81095581a1dccb8b5d89ee2ea3e9ba4a7b447e0a` | Finite ordinary source repairs, all-gap occupation constraints, and generic-ray countercontrols. | No bound constructs repairs indefinitely at one fixed source. |
| PR177, `25bf9b95a9404998e8e55aa401773488cd3dd4b8` | Arbitrary nonintegral cycle templates cannot improve ordinary height in the stated displacement sense. Complete rational-center bounds follow from an explicit two-logarithm theorem and finite certificate. | Optimization over these templates is not a successful universal selector; integral improvements expose the unresolved cycle question. |
| PR178, `398b3a04da071e96362005792417bd5cf8cc6497` | Full numerical gcd exclusion for a family with unboundedly many specified coprime packets. | The factorization and coprimality structure do not cover arbitrary cycle words. |
| PR179, `27a2c7414fdb92eeca57ad552a9ab5c36d8430d8` | Finite-budget descent, unequal-prefix transport, and exact inverse ladders. | The successful budget is not available for every required source. |
| PR180, `7cfd911d35382d9d3bc988060ba88ade78a4267e` | Complete-carry and stationary identities, sharp random affine-model bounds, and a global parity resolvent. | A model law cannot replace the actual exceptional ordinary-source law. |
| PR181, `5f03d809b4495802971211ef13ff905f741d700d` | Unbounded charged descents and guarded repayment. | The repayment guard is not universally established. |
| PR182, `cbec52dde5bed390a693310dd04e911033ba0cc9` | An actual scalar, an exact triadic convergence criterion, fixed-source repetition bounds, all-reset phase bounds, and finite classification for supplied contracting rational phases. | Universal triadic membership, the low rational phase branch, and arbitrary irrational phases remain open. |
| PR183, `68345f60a4f757acb42a69a4ac95910f8ce26163` | Independent repeated cycle blocks, exact ordinary channels, and arbitrary carry transitions. | No finite block decomposition or channel estimate covers all ordinary trajectories. |
| PR184, `366dab89ee9548084ab9b5e4e90ff82abf287a20` | Physical band-to-merger transport and infinite successful smaller-source families. | All-source coverage and comparison with the original source are still required. |
| PR185, `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d` | Residual polynomial denominator growth, full-gcd warnings, and same-law critical collision bounds. | Numerical cancellation and the required opposite estimate for the original law remain unresolved. |
| PR186, `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493` | Literature interfaces and explicit research tasks. | A source guide is not a new closing theorem. |
| PR187, `099058f3f2602a48e109c964899f0a9a2a223338` | Every finite digit-weight L/P script is excluded at a fixed signed rational source. Subexponential ordinary escape forces superlinear actual-gap complexity. | Arbitrary schedules need not have the specified repetitions. |
| PR188, `beed685ab713923191ae40c9559bf7400298d2d3` | All-reset carry amortization and a full-gcd residue norm in the coprime-clock case. | No universal upper bound on canonical expansion or universal small norm. |
| PR189, `a0be70b1ffa075cbc50755ac76036108c028d120` | Strict stationary critical collision deficit; finite-window phase entropy and a better count for finite phase classes. | No lower collision dimension of the same ordinary-source limit; finite phase classes are an extra hypothesis. |
| PR190, `ba58227c5a047ff3859a148a5fdaac4fd1451e4c` | Written Mahler transcendence argument for binary uniform and primitive substitution scripts, including nonuniform substitutions. | Actual arbitrary itineraries are not known to have substitution structure. |
| PR191, `37b3916633cd32a0c173b20bb18ec3a7ec290a63` | Two-sided packing, noncoprime cyclotomic norm certificates, and a smaller physical shadow on the specified residue class. | A useful partition, quantitative norm bound, or residue coverage must still be supplied. |

This table is a scoped synthesis of the inspected frontier, not a claim that every file or historical declaration on all twenty branches was recompiled. Fresh formalization scope is recorded separately.

## Reconstruction of the newest analytic and symbolic arguments

### PR182 round 12 and PR188: retain the complete carry and original clock

The canonical digit and physical gap have the exact relation

`a_i + c_(i+1) = b_i + 3 c_i`.

Telescoping retains the endpoint carry. Combining this with the literal physical product gives

`log₂ q_n + 2 Σ_(i<n)c_i = n log₂3 − Σ_(i<n)b_i + c_n − c_0 + log₂(q_0 E_n)`.

These are source-preserving statements. A large terminal carry can temporarily make ordinary height much larger than the canonical multiplier, so dropping it pointwise is invalid. PR182's logarithmic correction is a valid way to absorb it. The new occupation argument instead isolates exceptional clocks: their accumulated carry more than triples. This transfers the original counting function up to only a double-logarithmic number of exceptions, without using a fresh distribution.

The contracting rational-phase classifier in R12-3 retains guards even when the supplied scalar is false. Its periodic affine comparison bounds normalized height, the cubic guard restores ordinary height, and an actual repeated state gives a finite equality decision. The finite confined graph classifies cycles within its bound; it does not assert that every path stays inside the graph. The phase-dependent bound is not uniform over all rational phases.

### PR189: order of limits and attribution are part of the statement

PR189's later attribution correction at `a390a1a4c75ee95db98b4b683d17c503f4e4a118` credits the strict stationary collision deficit to PR180's `research/whole-source-20261123/COLLISION_CORE.md`, sections 3–4, equations (16)–(17), at the pinned PR180 head. PR189 independently rederives that theorem; it is not counted here as a new advance of PR189. The correction changes only its README, leaving the Lean source unchanged.

The stationary extraction uses tightness from bounded mean gaps. Entropy below the critical Shannon maximum gives a strict exponent deficit. Equality forces the nonuniform iid geometric distribution, whose collision entropy is strictly smaller. This proves a strict deficit for each extracted stationary law, but supplies no uniform deficit or convergence rate across all laws. The missing lower collision dimension cannot be inferred from ordinary integrality alone by replacing the law with a convenient random model.

The finite-window argument is stronger in a different direction. Conditional relative entropy counts the forbidden transition `b=1, c=0, c'>0` in the actual canonical-word law. Disjoint edges justify the product-reference support loss. The reference law is only an entropy comparison, not a proposed orbit law. The carry and canonical complexities remain distinct.

### PR190: nonvanishing must be checked at the moving physical point

The coordinator reconstructed the formal series telescoping, substitution equation, weighted finite-state argument and the moving-point nonvanishing split in `README.md` and `PRIMITIVE_MORPHISMS.md`. The important safeguards are:

- A first differing binary symbol supplies a unique term of lowest 2-adic valuation. In the unequal-image case one compares periodic image words, so a proper-prefix relation does not invalidate regularity.
- Algebraicity implies a polynomial-coefficient recurrence. Normalization by the current rational prefix weight gives finitely many local tuples; eventual recurrence identities then yield a constant-coefficient recurrence and a finite deterministic state. This supplies transcendence of the required weighted specializations.
- Formal nonzero auxiliary series need not remain nonzero along a monomial orbit. The proof separately handles distinct transverse ratios, irrational Perron weights, and constant-ratio specializations.
- Height propagation stays inside one fixed number field under the temporary algebraicity hypothesis. The auxiliary order grows faster than its degree, while the relevant iterate heights have the same substitution growth scale.

This is a written reconstruction of the displayed argument. The infinite transcendence theorem is not formalized by `MahlerCore.lean`, which supplies finite affine and substitution identities. No extension to arbitrary larger-alphabet automatic sequences or arbitrary ordinary trajectories is inferred.

### PR191: cancellation and the shadow residue are genuine hypotheses

The two-sided packing argument uses both common future binary congruence and common past ternary congruence. Cyclic extrema compare the full range of carries and states. A common prefix/suffix factor cancels only after both sides carry that factor. The new rotation argument applies the same principle to two whole-period rotations, without assuming an equal-clock block dictionary.

For the noncoprime norm, cyclotomic factors may share primes. The displayed product divisibility is justified prime by prime by `min(c, Σd_j) ≤ Σ min(c,d_j)`; it is not a pairwise-coprime argument. Zero determinant components remain explicitly ineffective. They cannot be discarded from the whole denominator.

The smaller L/P shadow is integral only on its specified class `83 | q+7`. Its literal first gap is one, so the entire continued shadow cannot reach the ordinary fixed point. The comparison with the least nonconverger uses the minimum over block boundaries to control intermediate states. It does not justify applying the same comparison at a minimum restricted to one scalar phase, or outside the residue class.

## New deduction boundaries

The new carry occupation and critical-word separation proofs are in the scientific packet. The latter use only the scalar identities, finite ordinary endpoint residues, and an elementary harmonic bound; they do not require a stationary law, an entropy limit, Matveev, or a conjectural distribution.

The new rotational exclusion has an elementary divisibility theorem and a separately source-qualified uniform two-power gap. The coordinator checked Matveev's original Corollary 2.3, equations (2.4), (2.6), printed page 1219: specialize to two logarithms over the rationals and use the permitted constant `2^(6n+20)`. With `n=2`, `(log 2)(log 3)<1`, and `B*=max(A,p)`, the stated weaker constant `5·10^9` is valid. The finite Farey certificate and all bounded comparisons are replayable. This imported analytic theorem is not made a Lean axiom or presented as a newly formalized result.

Primary source: E. M. Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II*, Izvestiya: Mathematics 64:6 (2000), 1217–1269, [DOI](https://doi.org/10.1070/IM2000v064n06ABEH000314), [publisher PDF](https://www.mathnet.ru/links/ece4aa0032f96dfaf141673d5dc77324/im314_eng.pdf).

No argument here forces every exceptional orbit to remain within a small number of critical mechanical fragments, and no argument forces every possible cycle to have a long repeated cyclic factor. These are the exact remaining coverage gaps after the new exclusions.

## Work arriving during this pass: PR192 and PR193

The fixed final comparison cutoff is PR192 at `be783656f0e889fe0d5318a2f7a9140099cb94b5` and PR193 at `52beff703fd3ce798c430e5af8199eb58d41bf93`. Their earlier scientific pins and later verification/extension deltas are distinguished in the review addenda. These are two additional sources beyond the initial twenty-PR table.

### PR192: finite canonical words are fully realized, while infinite sources remain distinct

The independent reconstruction of `PHASE_SEPARATION.md`, PS1–PS6, is in [ADDENDUM_PR192.md](ADDENDUM_PR192.md). Extreme digit runs give actual normalized-height inequalities and phase separation. More decisively for the symbolic interface, every finite length-m canonical word occurs at a positive ordinary source first reaching 1 after exactly m+2 accelerated odd steps. A terminal two-step scalar fiber supplies every required ternary residue; the backward construction keeps all ordinary positivity and parity guards.

This rules out a universal forbidden finite canonical word across all positive sources. It does not rule out a restriction conditioned on the source, its height, its carries, or a hypothetical failure to converge. Passing to longer words changes the realizing source. It supplies neither one ordinary realization of an arbitrary infinite word nor a bounded sequence of realizing source heights.

The new square-root edit exclusion in this packet keeps the starting source fixed. Its cubic example has bounded runs of extreme digits, so it is not merely another application of PR192's endpoint-run exclusion. Conversely the far-from-critical phase examples in PR192 need not fall within the mechanical approximation class. The two restrictions do not jointly exhaust all actual phase words.

The [cycle review](PR192_CYCLE_REVIEW.md) reconstructs `CYCLE_FACTORS.md` §§1–4 with its explicitly imported PR185 inputs. The surviving evaluated polynomial grows faster than every fixed power of the odd count. This still precedes numerical cancellation with the evaluated numerator. The exceptional cyclotomic split and examples where all component norms are simultaneously divisible reinforce that exact boundary. Our rotational divisor is a divisor of the true reduced denominator, but needs a useful complementary carry difference. Neither result provides such a saving for every possible primitive word.

PR192's later commit contains a successful fresh-source formal receipt after a documented visibility port. It includes ten new declarations and five selected upstream reports. This source record was inspected; its execution is not counted among the 83 declarations freshly checked by this packet.

### PR193: an interval bound cannot select its least unresolved source

The [PR193 addendum](ADDENDUM_PR193.md) reconstructs the exact cyclic complexity inequality and the source-preserving finite synchronization argument. An arbitrary translated interval of length L has at most O(L^theta/sqrt(log(2L))) terminal fibers at a common O(log-squared L) odd clock. Every source except the least in its fiber has an actual smaller partner in that interval. The finite proof keeps the same ordinary dynamics, translation-independent interval contraction, and the necessary remaining clock budget.

The exceptional fiber representatives cannot be erased by taking larger intervals: a specified source can remain a representative. Our half-size selector handles a fixed source in one explicit congruence class, but no argument puts every representative into that class. This is exactly the missing universal step. The new two-anchor obstruction further shows that a search with a fixed excess budget on a fixed initial forward horizon can miss an existing smaller witness. The positive construction crosses it at the next clock, so the obstruction is not an all-time failure.

PR193's cycle inequality retains the true reduced denominator d and factor complexity P(k). With d=1 and P(k)<A, its asymptotic repeated-factor threshold agrees with the coefficient 1-log(2)/log(3) in our rotational bound. Its finer scale dependence and our exact pairwise divisor are different statements; the shared asymptotic consequence is not counted twice.

At the final head, `HIGH_COMPLEXITY_CONTROLS.md` constructs primitive positive rational cycles having arbitrarily high minimum, integrality at any prescribed finite set of primes, and logarithmic-length factor saturation. Their actual reduced denominators are exponentially large. These examples cannot be ordinary counterexamples, but they show why positivity, high minimum, and a finite collection of local tests cannot force the desired long repeated factor. `SHADOW_COVERAGE_LIMIT.md` also gives a positive relative density of failures for its specific first-endpoint odd-excess budget; it does not exclude later targets. The review separates both results from new Lean compilation.

## A concrete closing obligation after synthesis

For every positive n>1, constructing a positive m<n and actual finite clocks s,t with T^s(m)=T^t(n) would prove Collatz by strong induction. The explicit successful cells, interval fiber compression, and full finite inverse layers are useful parts of this objective. They still leave a prescribed least unresolved source untreated. A proof needs pointwise coverage, rather than another estimate permitting even one such source.

The two other routes are likewise precise: an incompatible upper condition on every fixed nonperiodic actual word, or a full numerical denominator obstruction for every primitive positive nonstandard cycle together with control of divergence. The new necessary conditions and source-qualified exclusions do not discharge any of these universal statements.
