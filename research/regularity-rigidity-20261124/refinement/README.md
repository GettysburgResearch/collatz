# Central paired fibers, simultaneous localization and verified ordinary attachment

24 November 2026. **Collatz remains OPEN.** This continuation improves the
paired renewal count, gives two constant-clock routing constructions,
corrects an overly broad possible use of the filtered-state hypothesis,
and repairs and extends the Lean core. Three GPT-6.2 Astra agents developed
and cross-reviewed the work; the coordinator reconstructed the new
arguments and independently replayed the delivered finite checks.

## The strongest new counting statement

Let N_(e,p)(q) count complete ratio-five marked inverse words at common
shortcut clock e and odd count p, with real affine offset at most 1/2.
Put G=2^e/3^p. Under the precise marked-return inputs pinned in the proof,
there are fixed D,C,c>0 such that, for every sufficiently large H, one row
satisfies

\[
 H\le e\le DH,\qquad |2p-e|\le C\sqrt H,
\]

and at least c·3^p/H unit classes modulo 3^(p+1) each have

\[
 N_{e,p}(q)\ge cG/H.
\]

For every positive odd ordinary representative of any such class, all
these words decode to distinct positive odd ternary-unit starts in
[qG/2,qG], with T^e(x)=q and T^e(5x)=5q. The two arms have the same p.
The result retains the bounded real offset throughout the probability
argument and does not use Tao's fine-scale mixing or an external one-arm
inverse floor. It strengthens the earlier PF2 in its clock window,
balance width, cell fraction and inverse multiplicity.

[Full proof and exact inputs](LOCAL_FIBER_ROWS.md) ·
[Independent crossreview](../../../reports/regularity-rigidity-20261124/LOCAL_FIBER_CROSSREVIEW.md)

**Late source intake and credit.** PR193 advanced during this pass and
independently proved a central `1/H` bank with bounded real offsets and
many interior marks. After one fixed padded A-block, its bank and the
carry ceiling here also imply the many-cell statement above. The frozen
proof is an independent derivation, not a claim to the first central
polynomial bank. PR193 additionally routes a dense short-interval pattern
into every prescribed ordinary pair, while allowing the source height
and suffix clock to be arbitrarily large. The controlled-clock coarse
localization below addresses a different quantifier.
[Exact refreshed sources and the short second derivation](../../../reports/regularity-rigidity-20261124/LATEST_INTAKE.md)

## Localization, exact target tests and the missing step

At one adjusted physical clock and odd count, the good fine cells can be
placed in **every** prescribed coarse ternary class simultaneously.
The elementary construction adds 119 clocks and four odd inputs per
four digits of precision. A completely replayed four-A certificate adds
88 clocks and eight odd inputs per eight digits. Precision k=o(H) retains
the near-linear exponential order; k=O(log H) retains polynomial pressure.

The 88-clock certificate enumerates all 47,905 compositions in its grammar,
covers all 13,122 fine unit classes modulo 3^9, and replays 26,244 literal
arm paths. The 119-clock route has a separate Lean theorem for every
positive odd ordinary ternary-unit target; its finite 243-residue
certificate is evaluated by the Lean kernel.

[88-clock proof and certificate](FIXED_CLOCK_ROUTER.md) ·
[Exact checker](check_fixed_clock_router.py) ·
[Independent second reconstruction](../../../reports/regularity-rigidity-20261124/FOUR_A_CROSS_REVIEW.md)

For a supplied ordinary q, the exact complete paired count also has a
finite arithmetic description. If C_(e,p) is the set of legal odd-start
word carries, count C such that C and 5C both belong to C_(e,p),
0<C<=2^(e-1), and 2^e q-C is divisible by 3^p but not by 3^(p+1).
This retains the same target and the second arm. A scalar floor alone
does not control this intersection.

The state-filtered hypothesis FS cannot be assumed for every integral
menu. Every bounded-offset relative state satisfies
D>−5·3^(k_+)B. The actual state (k,D)=(0,−4) therefore has no rows with
B=1/2, although it occurs at an exactly balanced positive ordinary pair
with both terminal values units. The conditional common-suffix implication
survives for a suitable selected menu; existence of enough admissible
prefixes remains open.

[Exact carry characterization, counterexample and narrow review](PAIRED_FIBER_AUDIT.md) ·
[Finite controls](FIBER_CONTROLS.json)

The main gap is unchanged in its quantifier: **the fine class of one
specified ordinary q must carry enough complete paired words along
arbitrarily large balanced rows**. Favorable fine classes in the new
theorem may change with H. Even that missing lower bound would need an
opposing bound for genuine failed comparisons, or another global
mechanism, to settle Collatz.

## Independent analytic review and finite-state improvement

The review reconstructs the stopped occupation estimate, reverse-prefix
domination, exact use of Tao's published proposition, shell discrepancy,
polynomial phase cancellation and approximate-coloring countermodel.
Its verdicts retain each stated source hypothesis and do not certify
neighboring claims or the whole repository.

The new finite-state theorem gives decorrelation from varying base-B
digit automata whenever

\[
 S^4B^{2S}=o(\log\log X).
\]

This improves the previous S^2=o(log log log X) range. The proof uses a
uniform product-chain meeting-time bound and the existing ordinary label
estimates. It does not construct a classifier of an invariant basin.
The exact finite-chain checker covers 746 binary tables and three larger
examples; it explicitly rejects optimized Python rather than dropping
its assertions.

[New finite-state proof](AUTOMATON_COUPLING.md) ·
[Original analytic claims reviewed](../../../reports/regularity-rigidity-20261124/REVERSE_AND_RIGIDITY_REVIEW.md)

PR195 had already improved the stationary entropy deficit to O(log k)
and proved a nearly Haar **upper** cylinder bound at each positive
ordinary target. This checkpoint independently reconstructs those
earlier estimates and records a direct uniform upper-exponent corollary;
it does not present the entropy result as new.

[Prior result, source credit and exact direction of the estimate](STATIONARY_CYLINDER_BOUNDS.md)

## Formal evidence and execution

The original 19 theorem signatures are unchanged. Seven modules now
compile with Lean 4.34.1 and Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612,
with warnings as errors and automatic implicit arguments disabled.
All 46 theorem declarations, including eight private helpers, report
only subsets of propext, Classical.choice and Quot.sound. Four new
modules provide the ordinary paired-family decoder and cardinality
ceiling, the relative-state exclusion, finite mass splitting and the
119-clock paired route. The renewal and asymptotic estimates remain
written proofs with their named inputs.

[Repair and formal scope report](../../../reports/regularity-rigidity-20261124/LEAN_REPLAY.md) ·
[Compiler receipt](../../../reports/regularity-rigidity-20261124/LEAN_RECEIPT.json) ·
[Reproducible Lean runner](../replay_lean.py) ·
[Original five controls replay](replay_controls.py) ·
[Source and evidence manifest](../../../reports/regularity-rigidity-20261124/MANIFEST.json)

The coordinator's fresh Lean replay reproduced the worker receipt
byte-for-byte. All five existing JavaScript controls matched their
published data, the new fixed-target carry controls matched their
canonical JSON, and the finite automaton checker matched the reviewed
exact rational output. A repository integrity receipt is separate
evidence from these mathematical checks.
