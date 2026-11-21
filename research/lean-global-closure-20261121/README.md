# Lean attempts at universal Collatz closure

**Status: OPEN. No complete proof of Collatz is claimed.** This project targets
the universal closing step, with machine-checked intermediate results and
explicit hypotheses. The map is the ordinary shortcut map

\[
T(n)=n/2\quad(n\text{ even}),\qquad T(n)=(3n+1)/2\quad(n\text{ odd}).
\]

## Compiled results

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
