# Lean attempts at universal Collatz closure

**Status: OPEN. No complete proof of Collatz is claimed.** This project targets
the universal closing step, with machine-checked intermediate results and
explicit hypotheses. The map is the ordinary shortcut map

\[
T(n)=n/2\quad(n\text{ even}),\qquad T(n)=(3n+1)/2\quad(n\text{ odd}).
\]

## Compiled results

### Late-source composition — 22 November 2026

The [late synthesis](LATE_SOURCE_SYNTHESIS_20261122.md) incorporates the five
substantial branch updates that arrived during the first build. It connects
PR177's new uniform return cone to our actual all-word signed compiler in
Lean, and proves an unconditional odd-count bound for every multiplicative
return. The driver now contains 21 core compilation units.

The accompanying written proof establishes finite harmonic moments of every
positive power of the normalized Green deficit, with an explicit ordinary
mean rate, and a complete unchanged-source occupation bound. A separate
channel calculation identifies the correct sourcewise boundary trace and
proves that its unsubtracted fixed-radius replacement always diverges.
The analytic deductions retain their pinned harmonic and rigidity inputs.
The [source snapshot and scoped reviews](../../reports/lean-global-closure-20261121/nov22/late/)
separate the new deductions from imported results and actual executions.

### Global continuation — 22 November 2026

The [new global-step packet](GLOBAL_STEP_20261122.md) builds on the refreshed
145-PR inventory. It adds an exact signed carry compiler for arbitrary
supplied complete source words, and a universal affine rigidity theorem:
one sufficiently large actual merger certifies its entire binary parameter
class at the same two independent clocks. It also proves a pointwise clock
lower bound for every multiplication-by-five merger.

The accompanying written potential theorem and its all-exponent extension
exclude every nonzero fixed-period regularly varying profile of an excessive
inverse envelope, including the critical exponent one. Its finite positive-row algebra and signed-history lift have Lean
cores; the asymptotic and modular arguments remain written mathematics.
The complete common-rank stopping rule and the moving-target analytic
estimate remain open. No full Collatz proof is claimed.

That scientific checkpoint added three modules and compiled 19 core units.
The [actual published-checkout replay](../../reports/lean-global-closure-20261121/nov22/VALIDATION.md)
passed all 19 units and 126 axiom reports, including 55 new-module reports,
with only Lean's standard axioms. All five repository commands also passed.
The earlier 16-unit receipt below remains evidence for its exact older
scientific commit, not a replay of this continuation.

### Earlier literature and inverse continuation

The preceding [literature continuation](LITERATURE_CLOSURE_ATTEMPT.md) is a
separate written proof packet. Using the explicitly pinned PR180 population
and canonical-potential inputs, it proves the global weighted bound
`sum_(n<=X, nonperiodic odd unit) V(n)/n <= (5/c)*X^(39/40)` and consequently
`sum V(n)/n^2 <= 200/c`. The deduction has an independent written review;
it is not counted among the Lean compilations below. Its missing transfer
to an invariant component label's multiplicative five energy is explicit.
The same continuation records a typed certificate evaluator and exact
interval fusion, including the unbounded terminal case that remains open.

### Whole-repository continuation

The [wider attack](WIDE_CLOSURE_ATTEMPT.md) compares the current complete-witness,
ordinary-merger, and analytic routes after inventorying all 143 PRs. It adds
an exact normalized-quotient theorem and complete inverse continuation with
ternary carries; an iff characterizing the full canonical reserved-merger
menu; and an asynchronous complete-certificate compiler accepting arbitrary
actual parent-target phases. The arithmetic foundation was ported to core
Lean without changing its statements.

[MaximalReserve.lean](CollatzGlobalClosure/MaximalReserve.lean) further proves
that a single, uniquely selected maximal ternary reserve per source clock
retains every merger within the two source horizons. Its canonical leading
quotient is one or two; no scan over smaller reserves is needed.

The new [terminal reset](CollatzGlobalClosure/TerminalReset.lean) covers every
power-of-two source as a recursive case of the common multiset induction,
using the fixed certificate of three and preserving any supplied terminal
tail. It removes that infinite terminal family from the dispatch obligations;
the remaining nonterminal cases still need a complete selector.

The analytic continuation bounds the entire ordinary pressure tail beyond
its first positive period by `½(3/5)^q`, using the pinned PR144 population
identities. Its rational finite weighted kernel is separately formalized in
core Lean. The infinite trace application is a written deduction, and the
required upper bound on the moving core remains open.

All new formal sources can be compiled without Mathlib:

```sh
python -B build_wide.py --lean /path/to/lean-4.34.1/bin/lean \
  --output /fresh/wide-build --receipt /fresh/wide-build.json
```

The [published-checkout execution record](../../reports/lean-global-closure-20261121/wide/VALIDATION.md)
records the successful fresh build of all 16 core units, 71 axiom reports
using only Lean's standard axioms, and all five required repository checks
at the exact scientific commit.

The detailed [inverse](INVERSE_CARRY_CONTINUATION.md),
[certificate](ASYNC_CLOSURE_ATTEMPT.md), and
[analytic](FULL_SOURCE_TRACE_ATTEMPT.md) notes retain exact input commits,
proofs, failed completions, and the first unproved global step. These results
do not supply a full Collatz proof.

### The new forced dyadic section

The [band attack](BAND_ATTACK.md) builds on PR173 at
`fa0c9e2a2851e6324391e39c17afcb5913185aec`, which proves that every ordinary
positive orbit reaches a shrinking odd band above a power of two.
The new results include exact offset-descent and certificate transfers;
an infinite, much thinner marked family with no descent through its binary
exponent clock; and a cofinal first-return construction that simultaneously
increases size and trailing-one depth by arbitrary amounts. It rules out
every coordinatewise monotone strict return rank based on those two quantities,
even after a finite exception range. A separate cofinal construction has
distinct marked endpoints with identical binary exponent and trailing-one
depth, while the entire intervening path stays above the cutoff. The
[return-path composition](CollatzGlobalClosure/SectionFeatureRanks.lean)
therefore excludes **every function of binary exponent and trailing-one depth** as a strict
every-return rank, without a monotonicity assumption. Every fixed finite
odd-source parity prefix also occurs cofinally inside the marked set.

The [reset proof](SECTION_RESET_RETURNS.md) and
[offset attempt](BAND_OFFSET_ATTEMPT.md) give the constructions and the exact
remaining obligations. Ordinary descent below a mark must not be substituted
for descent among marked returns: the next marked visit can overshoot.
The source's universal variable-return descent criterion remains open.
The follow-on [segment-minimum attempt](SEGMENT_MINIMUM_ATTEMPT.md) records
the remaining ordinary-height and certificate-window gaps. The
[published-checkout execution record](../../reports/lean-global-closure-20261121/band/VALIDATION.md)
records all 17 fresh compilation units and the complete repository gate.

### Exact cost of preserving a parity prefix

[`CollatzGlobalClosure/SiblingRigidity.lean`](CollatzGlobalClosure/SiblingRigidity.lean)
proves an unbounded rigidity theorem for ordinary affine mergers. If
`x=2^a n+c` shares the first `k` parity steps of `n`, merges with its
`k`-step endpoint at clock `k+a`, and has the same total odd count `p>0`,
then

\[
3^p c=(2^a-1)C,\qquad 2\cdot3^{p-1}\mid a.
\]

Here `C` is the genuine prefix offset. For `a>0` and `c≥0`, the additional
clock is at least `2·3^(p−1)` and the image is at least
`2^(2·3^(p−1))*n`. The file proves the ordinary prefix facts, the ternary
unit property of `C`, and the exact order implication using Mathlib's
proved lifting-the-exponent theorem. The
[scope and proof](SIBLING_RIGIDITY.md) specify every guard. This explains
the exponential clock cost within that family; it does not exclude a
construction that switches parity cells or changes odd counts.

### An obstruction valid at every finite window width

[`CollatzGlobalClosure/LocalProfileObstruction.lean`](CollatzGlobalClosure/LocalProfileObstruction.lean)
constructs, for **every** binary window width and **every** size threshold,
positive odd integers `n > m > 1`, with `n` above that threshold, satisfying

\[
3n+1=4m,\qquad H_r(n)=H_r(m).
\]

Here `H_r` records the entire zero-padded binary-window histogram of width
`r+1`. It follows that **any function** of one fixed-width histogram,
including a nonlinear function with an arbitrary preordered codomain,
cannot be a strict rank for every accelerated odd Collatz step. Arbitrarily
many small exceptions do not fix this obstruction. This is a constructive
infinite-family theorem, independent of numerical synthesis searches.
The [construction and scope](LOCAL_PROFILE_OBSTRUCTION.md) retain the
distinction from ranks that depend on positions or on blocks of steps.

### Deterministic relative parity

[`CollatzGlobalClosure/RelativeParityBarrier.lean`](CollatzGlobalClosure/RelativeParityBarrier.lean)
proves, for every positive orbit that never hits one and every clock `t`,

\[
2^{4t}\le 2^{7p_t}n^4,
\]

where `p_t` counts its actual odd inputs before clock `t`. This covers both
divergence and hypothetical nontrivial cycles. It then proves a finite
source-relative convergence certificate and the exact equivalence

\[
\texttt{ForwardFiveClosure}\iff\texttt{RelativeBudgetReturns}.
\]

The right-hand statement is **not proved**. It is a defined proposition,
not a new axiom. The [proof note](RELATIVE_PARITY_ROUTE.md) gives its complete
quantifiers, the elementary estimates, and the first unsupported step in
the attempted deterministic completion. No novelty claim is made for the
elementary parity estimate.

### Exact endpoint construction

[`CollatzGlobalClosure/EndpointSteering.lean`](CollatzGlobalClosure/EndpointSteering.lean)
proves the full ordinary lift identity

\[
T^k(n+2^k3^p t)=T^k(n)+3^{p+\operatorname{odds}(k,n)}t.
\]

It gives the exact inequality and divisibility condition for a prescribed
endpoint, constructs the source from them, and proves positivity under an
explicit positive-source guard. The [endpoint note](ENDPOINT_STEERING.md)
and [inverse-tree attempt](INVERSE_TREE_ATTEMPT.md) explain the proposed
adaptive construction. Its all-precision depth bound is open.

## Attempts at the full closing step

The [global-attempt record](GLOBAL_ATTEMPTS.md) separates the proved
statements from the remaining universal targets. The
[fixed-clock synthesis](FIXED_CLOCK_SYNTHESIS.md) seeks an ordinary rank
decreasing under a fixed even iterate `T^q` at every input greater than two.
Its finite carry transducers handle arbitrary binary lengths. An exact
global verifier rejected candidates that passed their initial concrete
constraints. No global rank certificate was obtained.

The search code is exploratory, and the floating-point infeasibility and
timeout results are not Lean theorems. None of the compiled results imports
the search outputs as a proof premise.

## Build

The project pins Lean **4.34.1** and mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`. From this directory:

```sh
lake exe cache get Mathlib/Tactic.lean Mathlib/FieldTheory/Finite/Basic.lean Mathlib/Data/Nat/Digits/Lemmas.lean Mathlib/NumberTheory/Multiplicity.lean
lake build
```

For a receipt-producing direct build of the new band continuation, including
the exact frozen source files, use an installed Lean binary and the pinned
mathlib checkout:

```sh
python build_band.py --lean /path/to/lean --mathlib /path/to/mathlib4 --output /tmp/collatz-band-fresh --receipt /tmp/collatz-band-build.json --full
```

The output directory must not already contain compiled project modules.
The new dependencies include mathlib's logarithm, factorization, and
Diophantine-approximation files; obtain their cache with `lake exe cache get`
if it is not already present.

`lakefile.toml` treats warnings as errors. The relative-parity, endpoint,
and rigidity declarations and the two principal profile theorems print
their axiom dependencies. Only Lean's standard
`propext`, `Classical.choice`, and `Quot.sound` occur. The source contains
no `sorry`, custom axiom, `native_decide`, or unsafe proof mechanism.
The actual package execution is recorded in
[`checkpoint-build.json`](../../reports/lean-global-closure-20261121/checkpoint-build.json)
and [`checkpoint2-build.json`](../../reports/lean-global-closure-20261121/checkpoint2-build.json),
followed by the complete four-module build in
[`checkpoint3-build.json`](../../reports/lean-global-closure-20261121/checkpoint3-build.json).
This execution proves the stated implications; it does not establish their
open universal hypothesis.

The final [clean-checkout validation record](../../reports/lean-global-closure-20261121/VALIDATION.md)
records a fresh build of every project proof module at the published
scientific commit and the separate five-command repository gate.

## Earlier source interfaces considered

These are exact investigation pins, not unproved premises imported into the
Lean kernel. Older work is not re-audited by this checkpoint.

| Source | Exact head | Interface used for the research attempt |
|---|---|---|
| [PR146](https://github.com/GettysburgResearch/collatz/pull/146) | `f431078244e868dc699fad011044f0d5e7f76437` | Whole-interval synchronization; certified terminal sources; finite directed five-closure interface |
| [PR173](https://github.com/GettysburgResearch/collatz/pull/173) | `8596fdfd4d6378b57f83d843e94a206f45604b1b` | Lean predecessor fans in narrow multiplicative shells |
| [PR171](https://github.com/GettysburgResearch/collatz/pull/171) | `2bd243b3e05eaa5543adeb2894637b053c9662ca` | Paired section recurrence and the distinction between Haar recurrence and supplied ordinary sources |
| [PR164](https://github.com/GettysburgResearch/collatz/pull/164) | `9582df78eb4d768eb748d3cf367ba97582308a52` | Witness-relative rewrites for the direct `27m -> 9m` closure problem |
| [PR172](https://github.com/GettysburgResearch/collatz/pull/172) | `b22d94240f3d44a04231508e5dfe9a4947a57125` | Prior pass's global certificate attempts and explicit remaining obligations |

The active universal attempts are deterministic relative parity, adaptive
endpoint steering for synchronized intervals, and a rank that retains
nonlocal binary/ternary structure. An incomplete search or a conditional
closing lemma will not be labeled a proof of the full theorem.

A late source refresh also considered PR173's new five-block criterion at
`cccf14d13250d3f98ef9b01ddbd304d11294e603` and the current descriptions of
PRs174,176,177,179,180. These newer interfaces are recorded in
`GLOBAL_ATTEMPTS.md`; they are not additional hypotheses of the Lean files.
