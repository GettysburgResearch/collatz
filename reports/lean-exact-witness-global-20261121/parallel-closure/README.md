# Checkpoint fourteen: exact scope and execution

**Full Collatz, the original residue implication, and `FloorIntervalStep` remain OPEN.**

Parent published head: `e4ca639326bac73da8c2a698dec8a749e5efbe68`.
The final published commit and exact tree are recorded on PR177 after the
remote write is read back. This report does not substitute a local commit
for an unconfirmed remote publication.

## New results and proof levels

* `BinaryRunClock.lean`: 19 new public theorems. It defines the genuine binary
  run count and proves its dyadic invariance, exact valuation bound, a finite
  multiplication-transducer estimate, the all-prefix ordinary-clock bound,
  and the source-height ceiling. Every claim in this module is kernel checked.
* `ContextSurgery.lean`: 16 new public theorems. Exact unbounded affine carry
  semantics preserve the supplied complete tail. Lower-grade completion and
  a target-aware early exit consume the original interval hypothesis. An
  all-length inverse-tree theorem refutes a particular gap-three regrowth
  strategy. Universal carry completeness is not asserted.
* `ARITHMETIC_CYCLE_CONTINUATION.md`: written deductions of finite sparse
  endpoint pairs, uniform occupation with an explicit finite-core term,
  cycle moment properness, and ordinary-clock moment consequences. These
  use the already pinned published ESS theorem and its sparse-return proof.
* `ENERGY_TRANSPORT_CONTINUATION.md`: written uniform two-parameter profiles
  for both finite-Green energy directions, the complete potential, and every
  omitted tail. The actual canonical hypotheses, original source charges,
  killed paths, and same-component cross terms are retained. No zero-escape
  or sibling-current estimate is claimed.

## Focused Lean execution

The complete output and source identities are in
[checkpoint-fourteen.json](checkpoint-fourteen.json).

* Lean 4.34.1, compiler `5045d0056413266e57c625dcd7c365b10e377c52`.
* Core only; no Mathlib or external Lean package.
* Incremental aggregate build: **47 jobs**. The two new modules were also
  separately compiled with `-DwarningAsError=true`.
* Expanded dependency audit: **308 declarations**, of which **11** use no
  axioms. All other dependencies are confined to `propext`,
  `Classical.choice`, and `Quot.sound`.
* **35 new public theorems**. No admitted proof, custom conjectural
  assumption, or native-decision step was introduced.
* **43 preexisting Lean sources** were hash-matched to checkpoint thirteen.
  Their compiled dependencies were reused; this is not a fresh rebuild of
  the old proof packet. There are 47 current Lean source files, including
  the aggregate and audit files.

The separate complete-checkout default repository gate is run on the final
clean commit before publication. Its exact commit/tree and receipt digest
are included in the PR publication report. The broader regression bundle
was not repeated: the new modules and current structural gate are the
relevant checks for this checkpoint. Repository integrity is not a proof
of the written infinite mathematical arguments.

## Independent internal review

The principal researcher independently reconstructed the sparse-pair and
finite-window proofs, the complete carry consumers, and the source-wise
BV/physical-pulse energy proof. A second researcher independently reviewed
arithmetic AP1–AP9, including partial ordinary halving blocks and the
primitive-cycle clock conversion. The energy proof also received an
independent review of both signs, all finite Green depths, original-charge
exhaustion, killed components, and same-component coalescence. No missing
uniformity was found in these stated claims.

The carry module and note received another independent review. One wording
issue was corrected: its coefficientwise carry guard is sufficient, not
necessary for one isolated numerical edge. The formal theorem always had
the correct sufficient direction. The 77 inverse-tree claim is proved by
arbitrary word induction, not a bounded search. These are scoped internal
reviews, not external peer review.

| Final reviewed source | SHA-256 |
|---|---|
| `ARITHMETIC_CYCLE_CONTINUATION.md` | `a3c9113198564e4dac212782d5b6d3c270635c1fc9fe9a1e33cac75e5a8b7fc8` |
| `ENERGY_TRANSPORT_CONTINUATION.md` | `d1ae599da67c9fb8d0a3930a7aee09f20cbe4b5f8dff23326efef7e8e885b1a0` |
| `WITNESS_CLOSURE_CONTINUATION.md` | `08c0da9935c70f090eb759652e6dae890e31e3da6e1f1144bd401dda6448dde9` |
| `lean/Collatz/BinaryRunClock.lean` | `0a3bce12fd66cd4c13040f054b60f7626c653da1e77dcc837de8977531c041e3` |
| `lean/Collatz/ContextSurgery.lean` | `c9e8e0187c42a14f06b0951a8b88baa1d0c7ea681b06c5782419002b9356a593` |

## Source continuity and remaining inference

[SOURCES.json](SOURCES.json) pins 11 selected current repository sources and
two primary literature records. The comparable-growth Corvaja–Zannier
cycle attempt was not promoted as new progress because PR183 already
proves a stronger fixed-block positive-cycle theorem.

The arithmetic result imposes complexity on unresolved orbits; it does not
force a low-complexity return on every such orbit. The exact energy profile
shows why no finite-Green diagonal can discard the moving cutoff under
escape; it does not eliminate the escaping coefficient. The witness program
preserves all required source and target resources, but a proof of universal
successful completion is still absent. None of these missing conclusions
is a formal premise disguised as a new theorem.
