# Directed and source-witness induction

**Status: OPEN for the full Collatz theorem and the original residue implication.**

This checkpoint supplies executable search methods and Lean-checked soundness
theorems. It does not supply a complete recursive rule cover. In particular,
the propositions `Complete`, `ClockComplete`, and `EnergyComplete` remain
explicit hypotheses of the respective global closing theorems.

## The global target

The foundation theorem `deep_reverse_generates`, already imported and pinned
in this packet, reduces the global conclusion to

\[
n\equiv9\pmod {18},\qquad B(3n)\Longrightarrow B(n).
\]

Here `B(n)` means that the ordinary shortcut orbit of `n` reaches 1. The
target comprises 80 odd residue classes modulo 1440, each representing an
unbounded arithmetic progression. A proof may activate additional comparison
or convergence classes, but it must close every dependency it activates.

The new Lean theorems use this existing reverse-cover theorem without
reasserting its source results as new. The original arbitrary-tuple statement
is connected to full convergence by the existing
`CollatzWitness.original_iff_collatz` theorem.

## D1: a simultaneous directed induction

`Collatz.DirectedInduction` distinguishes the propositions

\[
F_q(n): B(n)\to B(qn),\qquad
R_q(n): B(qn)\to B(n),\qquad B(n).
\]

The `Kind` type allows arbitrary natural factors; the present searches use
3 and 5. A rank may depend on the direction and on the normalized input.
`oddCore` removes the entire power of two. Its positivity, oddness, component
equivalence and factorization are proved in Lean.

Removing powers of two is normalization and need not strictly decrease a
periodic rank. Every recursive query is subsequently required to be active
and strictly smaller under the common natural-number rank. This prevents
an implicit cycle between the convergence and comparison systems.

The affine path kernel checks ordinary doubling and shortcut links, directed
multiplication queries, joins between the known and desired arms, and
convergence terminals. Reversing the desired arm reverses the direction of
its comparison queries. A convergence terminal consumes a lower-ranked
convergence fact; it is not a free reset to 1.

| ID | Lean theorem | Scope |
|---|---|---|
| D1 | `oddCore_spec`, `oddCore_factor` | Complete dyadic normalization and preservation of each directed claim. |
| D2 | `oddCore_upper_bound`, `weighted_upper_bound`, `affine_tail` | Unbounded-valuation rank bounds and exact tail guards. |
| D3 | `step_sound`, `path_sound`, `certificate_sound` | Soundness of the actual directed affine proof operations. |
| D4 | `close`, `complete_of_certificates` | Well-founded induction from an explicitly complete active rule system. |
| D5 | `collatz_of_complete_deep` | Full convergence if that system covers every deep reverse-tripling input. |

No weight vector or finite table is asserted to satisfy D4's hypotheses.

### Why the numerical rank search was changed

The candidate search eventually supplied whole-progression paths with complete
dependency availability. That did not imply a well-founded proof program.
Exact rank analysis exposed selected multiplicative gain cycles.

For example, under ranks indexed by odd residues modulo 144, one selected
pair used a convergence rule on `1440t+283` querying `2160t+425`, and another
on `1440t+281` querying the odd part of `2160t+422`. Their selected rank types
formed a cycle with slope product `(3/2)(3/4)=9/8`. The second type is obtained
on an actual unbounded odd-parameter branch. This excludes that selected
type-weight policy; it does not exclude other paths or more detailed ranks.

The search also produced literal ordinary backtracking pairs. Such pairs
cannot both be justified as strict recursive descent. Increasing a residue
modulus does not by itself remove that logical defect.

The new source-witness route addresses a different quantity: the full known
certificate, rather than the magnitude of the integer indexing a comparison.

## S1: exact transformations of a supplied witness

`Collatz.SourceWitness.Trace s d xs` means that `xs` lists the successive
ordinary states before endpoint `d`, starting at `s`. The theorem `trace_peel`
removes such a prefix from any supplied hitting-time witness. It explicitly
requires that the removed prefix has not already visited 1.

This guard matters. A path in the undirected ordinary graph need not be a
prefix of the supplied forward witness, and subtracting steps after an early
hit would be invalid. The finite affine search records parameter-zero
exceptions separately. A candidate with such an exception is not an
unconditional full-cell theorem until the exceptional input is discharged.

Suppose the parent known source and child known source have forward prefixes
`old` and `new` to the same endpoint. If

\[
|\mathrm{new}|<|\mathrm{old}|,
\]

then `clock_replacement` constructs a child hitting witness strictly shorter
than the supplied parent witness. The child integer is allowed to be larger.
The target-side prefixes separately transfer the child conclusion back to
the desired parent conclusion.

`one_query_clock` proves the resulting rule. `close_clock` and
`collatz_of_clock_complete` prove termination of a complete such program by
strong induction on the supplied certificate length. The program coverage
remains a separate obligation.

## E1: a natural-number rank permitting longer replacements

For a finite ordinary witness prefix, define

\[
E_C([x_0,\ldots,x_{k-1}])=\sum_{i<k}C^{x_i}.
\]

If an inserted prefix has fewer than `C` values and each inserted value is
strictly below a removed peak `p`, then

\[
E_C(\mathrm{inserted})
\le |\mathrm{inserted}|C^{p-1}
< C^p
\le E_C(\mathrm{removed}).
\]

The zero-peak edge case is handled separately in Lean. A common witness
suffix cancels exactly. The stronger exported lemmas also allow different
removed dominators for different inserted values, permutation, and
cancellation of a shared finite multiset.

This is a rank in the natural numbers, with ordinary well-founded induction.
It does not require an imported ordinal or multiset-termination axiom.

| ID | Lean theorem | Scope |
|---|---|---|
| E1 | `prefixEnergy_replacement_lt_with_suffix` | Strict energy decrease below a removed peak, for an arbitrary shared suffix. |
| E2 | `prefixEnergy_cancelled_replacement_lt` | Exact multiset cancellation followed by energy decrease. |
| E3 | `energy_replacement` | Constructs the transformed supplied hitting witness and proves its whole energy decreases. |
| E4 | `one_query_energy` | Soundness of a one-query comparison rule with this witness transformation. |
| E5 | `close_energy`, `collatz_of_energy_complete` | Global conclusion from a complete energy-decreasing rule system. |

Clock decrease and energy decrease are **different induction orders**. A
rule that decreases only length is not silently combined with a rule that
may increase length but decreases energy. Each reported search system is
closed separately.

## Finite search scope

The reusable search packet lives in [`search/`](search/). It reconstructs
ordinary affine paths and exact query dependencies with integer arithmetic.
Its arithmetic replays are separate from the Lean kernel proofs above.

An initial replay of 738 accepted records found 137 ordinary mergers,
188 forward-consumption rules, 386 peak-replacement rules and 27 additional
length-only rules. In that screened energy program the maximum inserted
multiset length was eight, so `C=9` sufficed. Dependency closure still covered
only five of the 80 required reverse-tripling classes.

The later generators target the witness rank directly. Their finite search
boundary has an algebraic justification, not just an arbitrary word cutoff.
For a positive-slope affine form `at+b`, every legal whole-cell ordinary
forward move decreases the 2-adic valuation of `a` by one. Its forward path
therefore has a unique endpoint with odd slope. Legal inverse moves build a
tree above that frontier.

For strict source-clock consumption, the child source must lie at a smaller
depth than the parent in this tree. For peak-energy replacement, every
inserted-prefix slope must be no larger than a removed-prefix maximum slope
on an unbounded parameter tail. The fixed odd part of the slope after
removing powers of both 2 and 3 gives a lower bound `g*2^depth` on inverse
nodes. This yields a finite depth bound for that grammar.

These completeness statements concern **whole-cell ordinary affine paths
with one normalized comparison query and the specified prefix rank**.
They do not cover arbitrary witness transformations, unrestricted adaptive
trees, multiple-query energy bounds, or exponent-parameterized schemas.

Binary refinement preserves both child cells. The search checkpoint records
every unresolved branch; a processed-cell budget is never interpreted as
coverage. Reproduction receipts report the exact counts, semantic hashes,
parameter exceptions and open frontier.

## First unsupported global inference

The missing step is a complete dependency-closed rule family for all
`n ≡ 9 (mod 18)` with a single valid induction order, including its finite
exceptional inputs. Neither candidate availability, successful local prefix
checks, finite search exhaustion in a restricted grammar, nor a collection
of known convergent examples supplies that statement.

Consequently no `Complete`, `ClockComplete`, or `EnergyComplete` witness is
defined here. The global closing theorems retain their hypotheses, and no
`sorry`, `sorryAx`, custom axiom, or native-decide shortcut fills the gap.

## Sources and validation boundary

The ordinary foundation and deep reverse cover have the unchanged source
pins given in the packet README. This pass also examined:

- PR180, commit `995ae97b10e851e4f91f7c74395a5b28bcacfebc`,
  `research/lean-ordinary-closure-20261121/lean/Collatz/JointDescent.lean`,
  for the earlier symmetric affine comparison kernel and conditional search.
- PR176, commit `d2303ea3144ba652d089c1ec38ad3879c3ea5ef7`,
  `research/lean-global-resolvent-20261121/MIXED_CERTIFICATE_DESCENT.md`,
  for the source-certificate multiset approach. The present energy inequalities
  and source-witness transport are proved directly in Lean core.

Actual build and axiom output, pinned source hashes, and repository execution
receipts belong in
[`reports/lean-exact-witness-global-20261121/`](../../reports/lean-exact-witness-global-20261121/).
Successful repository validation is not presented as proof of any unfilled
global hypothesis.

## Follow-on exponent-word search

The next checkpoint ranks accelerated source exponents instead of ordinary
source values. Its common rank is `sum (15^a)` over the complete supplied
source word. A high first exponent can be replaced by at most fourteen
strictly smaller exponents; an arbitrary inherited tail cancels from the
rank comparison. The generic inequality is an instance of
`CollatzWitnessEnergy.prefixEnergy_replacement_lt_with_suffix`.

The complete derivation and exact finite grammar are in
[`gap-search/high/README.md`](gap-search/high/README.md). Its 8,147 rules
include 7,916 numerically expanding child maps. Its ternary guard union is
`5950/531441`, so it does not cover the high-first-gap branch. That fraction
does not measure progress on the full theorem.

[`gap-search/low/LOW_GAP_DISPATCH.md`](gap-search/low/LOW_GAP_DISPATCH.md)
checks the low-gap transitions with a shared unknown final valuation. The
rank difference is a polynomial of degree one in `15^δ`, with nonnegative
coefficient and positive value at `δ=0`. This proves decrease for every
`δ≥0`, not merely a list of sampled valuations. Its 87 fixed-cell rules
leave the global state program incomplete; `n=288t+9` is one explicitly
uncovered cell of the tested grammar.

The two catalogues have a compatible source-gap rank. A complete combined
cover, all required auxiliary states, and finite entrance cases still need
proof. The arithmetic implementations of these source/target splices have
not been formalized in Lean in this checkpoint.
