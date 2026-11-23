# Independent review of the finite weighted-collision Lean core

Date: 2026-11-23. Reviewer: `global_construction`.

**Verdict: VERIFIED for the three stated finite algebraic theorems.**
The complete joint injection is an explicit hypothesis of the collision
theorem. The carry theorem recovers the full natural-number carry; it does
not itself decode a gap word or discharge that injection hypothesis.
Neither countable collision transport, the probabilistic moment estimates,
nor a universal ordinary Collatz conclusion is formalized by these files.
No source change is requested.

## Exact reviewed artifacts

Paths below are relative to the repository root. The source and audit
hashes agree with the successful compilation receipt and the files read
for this review.

| Artifact | SHA256 |
|---|---|
| `research/closing-step-20261123/lean/WeightedCollision.lean` | `10ca5db21199dec6ac8dd3059c573bd7cd952b8bbbaaf114649975fc4141a3ee` |
| `research/closing-step-20261123/lean/WeightedCollisionAudit.lean` | `0aa063cadeb387fdd3bfd447e1c0eb2389dd56db576a5fe5198da38f72b06048` |
| `research/closing-step-20261123/check_lean.py` | `384b0ee481acbbb5b2c6eebbdaad61a7a9e90b2ded6eb08b08e7a2f4b54c2382` |
| `research/closing-step-20261123/reports/weighted-collision-lean-check.json` | `85ffcb3d43bd798bea9250c6f8f05d1f579718ef286b4234c50ecda27e9dee34` |
| `research/closing-step-20261123/reports/weighted-collision-lean-build.log` | `bc9b088847313beced2d6757776cef0ee255f604289d43e9329bc33233499aa6` |

This is an independent source-and-receipt review. The already successful
fresh compilation was inspected, rather than repeating the same build.
The written collision argument was separately reviewed in
`GLOBAL_REVIEW_COLLISION.md`, against the exact note hash recorded there.

## 1. Weighted Cauchy--Schwarz

`weighted_sum_cauchy` states, for a finite set `s`, real weights `w`, and
strictly positive real penalties `L` on `s`,

\[
 \left(\sum_{i\in s}w_i\right)^2
 \le \left(\sum_{i\in s}L_i^{-1}\right)
             \left(\sum_{i\in s}L_iw_i^2\right).
\]

The proof supplies the required nonnegative inverse and weighted-square
terms to Mathlib's finite Cauchy--Schwarz inequality. The pointwise square
bound is the identity `w_i^2 = L_i^-1 * (L_i*w_i^2)`, justified using
`L_i != 0`. No nonnegativity assumption on `w_i` is needed for this
algebraic result. In a probability application the weights are, of course,
nonnegative. The empty finite set is included correctly.

## 2. Complete-label collision inequality

`labelled_collision_bound` uses finite types of objects `I`, labels `B`,
and residues `R`. Its hypotheses are exactly strict positivity of every
`L b` and injectivity of

\[
                 i\longmapsto (\operatorname{box}(i),
                                \operatorname{residue}(i)).
\]

Its conclusion retains every cross-label contribution on the left:

\[
 \sum_r\left(\sum_{i:\,r(i)=r}w_i\right)^2
 \le \left(\sum_bL_b^{-1}\right)
                 \sum_i L_{\operatorname{box}(i)}w_i^2.
\]

I checked the two nontrivial bookkeeping steps directly:

1. Within a fixed residue fiber, equality of labels gives equality of
   the complete ordered pair and therefore equality of objects. The
   inverse-penalty sum can consequently be rewritten over the image of
   the label map, with no multiplicity discarded. Nonnegativity then
   bounds it by the sum over all labels.
2. After the fiberwise weighted inequality, the final interchange of the
   two finite sums counts each original object in its unique residue
   fiber. It does not replace a residue mass by the mass of one selected
   object or by a diagonal term.

The theorem permits signed real weights, which is a harmless algebraic
strengthening. The term "collision" has its probability meaning after
specializing to nonnegative weights. Finiteness is genuine: the
countable gap-word law and its monotone limiting argument remain in the
written proof, not in this module. The source documentation and receipt
say so explicitly.

## 3. Complete quotient/residue carry recovery

`complete_carry_recovery` assumes, for natural numbers `M A z C D`, that
the quotients `C/M` and `D/M` agree and that both remainders equal
`(2^A*z) % M`. The proof first equates the remainders and then applies
Euclidean division `C % M + M*(C/M) = C` and its counterpart for `D`.
Thus it recovers the **full** carry `C = D`, rather than merely equality
modulo `M`.

This is the required quotient/remainder component when specializing to
`M=3^m`, retaining the binary clock `A` and an endpoint residue `z`.
The theorem is valid even for `M=0` under Lean's natural-number division
conventions; excluding that case is unnecessary. Its hypotheses already
provide both remainders, so it does not assert invertibility of `2^A`
or prove the chronological carry recurrence. In particular, word
recovery from a complete carry and the last gap from the total clock
remain separate steps in the written joint-injection proof.

## 4. Compilation, dependency, and axiom scope

The checker verifies Lean version `4.34.1`, compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`. It rejects modified tracked
Mathlib source files, records the compiler binary and direct imported
source hashes, and compiles the new module followed by its audit into a
fresh temporary output directory placed first on `LEAN_PATH`. Existing
pinned Mathlib build dependencies are reused. The receipt does not claim
that every dependency was rebuilt or independently attested.

The theorem inventory is checked against the three declarations above.
The audit imports the freshly compiled module and prints the axioms for
all three fully qualified names. The checker requires the exact expected
audit list, rejects nonzero compiler exits and axioms outside the standard
allowlist, and verifies that the two Lean sources did not change during
compilation. Compilation uses warnings as errors. I found no `sorry`,
custom axiom, unproved declaration, or native computation shortcut in the
reviewed Lean sources.

The build log records:

| Theorem | Reported axiom dependencies |
|---|---|
| `weighted_sum_cauchy` | `propext`, `Classical.choice`, `Quot.sound` |
| `labelled_collision_bound` | `propext`, `Classical.choice`, `Quot.sound` |
| `complete_carry_recovery` | `propext` |

The successful receipt matches the log and current source hashes. Its
scope description accurately states finite weighted collision transport
with all labels retained, plus full quotient/residue carry recovery,
and explicitly excludes an infinite collision estimate or universal
closure.

## 5. Consequence for the research packet

The finite inequality supporting the written collision argument now has
a checked Lean proof, with the crucial decoding premise visible in its
type. The elementary full-carry recovery step is also checked. This
does not change the open status of the ordinary-source hypothesis or
promote the written Shannon/Renyi conclusions into Lean theorems.
