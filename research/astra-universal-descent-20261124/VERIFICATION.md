# Verification and proof boundaries

## Checkpoint 1: executed formal checks

The exact execution receipt is
[CHECKS.json](../../reports/astra-universal-descent-20261124/checkpoint1/CHECKS.json).
It records **23 public theorem declarations**, all accepted by official
Lean 4.34.1 (release commit
`5045d0056413266e57c625dcd7c365b10e377c52`), with warnings treated as errors.
All transitive axiom lists are subsets of
`propext`, `Classical.choice`, and `Quot.sound`.
No `sorryAx` or custom mathematical axiom appears.

| Source | Public theorems | SHA-256 |
|---|---:|---|
| CycleCore.lean | 8 | `16452b97967d2279eb25dabfc4fa52df50d3b475d2a7cab85a46ba25d2f6c81b` |
| EscapeCore.lean | 5 | `94c242425386d2273f74ec08164d91614df394ba482b6966b5dc4fbc714b9d73` |
| ShadowCore.lean | 10 | `e3902fa437b78b123d5cec2f73d04b68604fbfcf8b2eb2c674b161bf1a4cda16` |

The checker copies each unaltered module into the supplied output directory,
appends only `#print axioms` queries for all its public theorem names, and
compiles that copy. Both original and audited-copy hashes are recorded.
The proof sources import only `Std`; no Mathlib package or other project
theorem is required.

### What these checks establish

- `ShadowCore.guarded_certificate` proves the complete guarded smaller
  partner statement, with positivity, strict size decrease and the exact
  ordinary iteration. Its guard is a hypothesis.
- `EscapeCore` proves the affine remainder envelope, the translated
  interval inequality, and deterministic residual-clock/inverse-fiber
  injectivity. The asymptotic counting and synchronization theorem is a
  written proof.
- `CycleCore` proves finite cut arithmetic, divisibility of differences
  for a shared scaled shortcut word, and the resulting two-point
  packing inequality. Selection of the repeated word, analytic bounds,
  and all-word denominator conclusions remain written proofs.

This is ordinary Lean compilation and transitive axiom inspection.
No independent alternative kernel replay is claimed. No formal theorem
here states unconditional universal Collatz convergence.

## Finite controls actually executed

The three programs ran successfully in both normal Python and optimized
Python (`-O`), with identical stdout. Arithmetic assertions in the two
assertion-based author drafts were replaced with explicit exceptions
before this execution, so optimization does not disable their checks.

| Program | Coverage |
|---|---|
| cycle_check.py | Three ordinary/rational controls; 179 primitive positive cyclic words through shortcut period 10; 4,384 exact integer comparisons |
| shadow_check.py | 63 unbounded-family instances; 2,188 bounded competing diagrams, including 329 first-tier cases; 38 immediate-endpoint inversions; six finite ordinary budgets |
| escape_check.py | Every window offset modulo 2^k for k=8,12,16; exact maximum signature counts 130, 1,540, 19,283 |

The finite controls test the formulas and implementations. They do not
establish an unbounded theorem by exhaustion.

## Independent mathematical inspection

The three agents authored distinct lanes and cross-inspected specific
arguments. These were independent reconstructions within this session,
not external peer review.

- The cycle agent checked the translated counting recurrence, residual
  clock ceilings, critical logarithmic gain, inverse-fiber selection and
  collision conditioning in the escape note. It required the explicit
  inherited `m<=M` condition; the text includes it.
- The shadow agent checked the two-sided reduced-denominator proof:
  common denominator, integer spacing, rounded choice of windows and
  the full-cycle product identity.
- The escape agent checked the partner construction, sign and parity
  boundaries, and exact competing-word reconstruction. It requested a
  bundled positive certificate; that is now `guarded_certificate`.
- The root independently reconstructed the positive partner arithmetic,
  the two-sided integer inequality, and the finite-clock counting
  induction. It also checked that the finite interval enumeration
  includes every window offset rather than only aligned blocks.

The formal receipts bind exact Lean and replay bytes. The prose review
statements concern the associated checkpoint text and do not transfer to
future changes.

## Reproduce

From the repository root with Lean 4.34.1 installed:

```sh
python -B research/astra-universal-descent-20261124/check.py \
  --lean /absolute/path/to/lean-4.34.1-linux/bin/lean \
  --out /absolute/path/outside/the/packet/checks
```

Then, in a clean complete checkout:

```sh
python -X utf8 -B tools/validate.py \
  --receipt /absolute/path/outside/the/checkout/integrity.json
```

Repository integrity is separate from Lean checking and mathematical
correctness. A head-bound integrity receipt is recorded with the
publication checkpoint; it is not evidence for a universal theorem.

