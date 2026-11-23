# Independent review of the two numen arguments

Date: 2026-11-23. Reviewer: ordinary-pressure research agent, not the author
of the two reviewed notes. **Result: the stated constructions and the
two-place classification pass the written reconstruction below.**

Reviewed byte bindings:

| File | SHA-256 |
|---|---|
| NUMEN_INVERSE_FIBER.md | `0d51c889a7cf9b80310ff1d524d9c8d49f23b2de26adfdfb2d904475c1347b5c` |
| TWO_PLACE_NUMEN_CLASSIFICATION.md | `ed208f5ad73cf2f566973d72a5a75b2addfc487973978a4c7cc5e3c7b093d9d7` |

Publication-binding update: I reread the complete current classification
note after the initial review. Its finite-segment wording now specifies
"at most r vertices" rather than the ambiguous "length is at most r".
That is a minor clarification of the deletion argument already reviewed;
the conclusions and proof remain valid. The second hash above binds the
reread current bytes. No finite-control replay was needed for this wording
change.

These are written infinite proofs. This review is not a Lean proof, an
audit of every cited literature result, or a proof of Collatz. The reviewer
read PR177's elementary orbit-cylinder argument before receiving the review
task, and independently opened the primary dissertation during this review.

## 1. The growing inverse fibers

The series normalization is consistent: a one at binary position d gives
the term 2^(-d-1), with the next one acquiring an additional factor 3.
Consequently the displayed functional equations for the numen hold, and
the finite value at input 2 is 1/4.

For an odd unit root, the legal gap table is correct. Integrality and
unit output reduce to the two target residues 4 and 7 modulo 9. Every
selected e is at least 3, so the next ordinary state strictly exceeds the
current one. Its forward odd image is exactly the current state, because
the latter is odd and the displayed power of 2 is therefore its exact
valuation. The recurrence has the inverse, not forward, orientation.

The rational identity `q0-S_k=3^k q_k/2^A_k` follows by substitution.
All q_k are 3-units, giving exactly valuation k; this proves the 3-adic
limit at the specified ordinary integer. The real upper bound 1/5 follows
from A_i>=3i, independently of this limit.

The irrationality argument is valid. Eventual periodicity of binary
digits with infinitely many ones implies eventual periodicity of the
gap sequence after an appropriate one-boundary. The repeated inverse
block has an affine fixed point in Z3 because its denominator is a unit
modulo 3. Iteration would make the fixed rational difference from that
point divisible by arbitrarily large powers of 3, forcing exact equality.
That contradicts strict ordinary growth. The first distinct branch choice
gives a distinct next one-position, proving injection of the full binary
choice space and hence the continuum cardinality.

The additional surjectivity statement onto all ternary units also holds.
The same residue recursion works for arbitrary Z3 units without a real
ordering claim; conversely the first series term is a ternary unit and
all subsequent terms are divisible by 3. The domain excludes finite
binary expansions, as required.

## 2. The correction involving both completions

The positive-odd-root restriction in the final note is essential for the
odd-edge formulation and is correctly stated. With an even root, the
first displayed power of 2 would need an initial dyadic adjustment before
being called the exact odd-step valuation. A positive odd root in the
image is automatically a 3-unit.

For an arbitrary code in that root's fiber, the normalized tail is a
3-adic unit. Its independently defined rational expression has only a
power of 3 in the denominator, so 3-adic integrality implies ordinary
integer integrality. The inverse recurrence preserves positivity from
the initial positive integer and gives odd tails. Thus the series is an
actual ordinary inverse path before any real limiting argument is used.

The use of PR177's cylinder estimate on a tail of a simple inverse path
is justified. Its low-total part counts one exact dyadic cylinder per
gap word; its high-total part needs only injectivity of the r-step map
on the selected starting states. It does not require the collection to
be a complete forward orbit. Removing the first r inverse vertices makes
that injectivity exact. Paying at most r extra vertices gives
`N(X)<=r+4 X^(39/40)<=5 X^(39/40)`. The integral of that bound against
X^(-2) is exactly 200. It applies to separated visits as stated.

The real remainder is the original root times the product of
`3q_i/(3q_i+1)` over the inverse states. The reciprocal budget therefore
gives a lower bound `q exp(-200/3)` on every simple inverse path. No change
of source or probability law occurs.

The repetition alternatives are exhaustive. Any repeated inverse state
puts that state and the original root on one actual forward cycle. Once
the inverse path exits that cycle, it cannot reach any cycle farther
backward: a cycle's deterministic forward images stay on that cycle.
Thus an exited tail is simple. The finite product through indices
1,...,J-1 correctly precedes the tail bound which includes q_J.

An inverse path that remains on its cycle has periodic odd gaps and a
strictly decreasing product per full lap, so its real remainder tends to
zero. Conversely every nonperiodic root or eventual cycle exit has a
strictly positive remainder. Repeating gaps from the initial root gives
a purely periodic binary code from its first digit, not merely eventual
periodicity. This proves exactly the claimed equality classification.

## 3. The specific source correction

I independently opened <https://arxiv.org/pdf/2412.02902>, identified its
v1 marker, and read the relevant displayed hypotheses and proof of
Theorem 2.7 on printed page 76, Corollary 2.3 on printed page 73, and
the definition of contracting on printed page 60. For the shortcut 3x+1
map, that contracting condition refers to the slope of the zero branch,
which is 1/2; it is not a missing requirement that both branches contract
in the real metric.

The theorem has no additional same-real-value hypothesis. The proof uses
the existence of a rational code for a periodic integer value to infer
that the particular code already under discussion is rational. The
root-1 increasing inverse construction is a counterexample to precisely
that inference and the theorem as printed: its value is on the known
cycle while its code is irrational. The construction therefore tests the
theorem's actual hypotheses, not a weaker paraphrase of it.

This review does not assess the thesis's general Fourier or Tauberian
theorems. Nor does it infer that every result using its numen formalism
is invalid. The corrected result still leaves the full nontrivial-cycle
denominator obligation open.

## 4. Independent finite arithmetic replay

In a separate Fraction-based calculation I selected both the smaller and
larger legal exponent for forty successive steps, starting separately at
roots 1 and 7. Every step passed the unit, strict-growth, exact-edge,
prefix-remainder, telescoping-product, and exact valuation identities.
Every prefix sum lay in (0,1/5]. This was 160 actual inverse edges.

Those checks verify the normalization and local arithmetic of the written
proof. They do not certify irrationality, infinite cardinality, or an
infinite real product by finite computation. No review of the later Lean
bridge is included here.
