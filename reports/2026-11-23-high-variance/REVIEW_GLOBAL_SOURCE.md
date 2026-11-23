# Independent reconstruction of the complete inverse-cluster attack

Date: 23 November 2026. Reviewer: principal researcher (`/root`), distinct
from the source note and checker author (`global_source_synthesis`).

**Verdict: VERIFIED WITH FIXES in the scope stated below.** The only
mathematical premise correction requested in this review was making the
ternary-unit condition on the finite-tree root explicit. It holds at the
nonempty source cuts under consideration and is present in the final
reviewed source. This is an in-session reconstruction, not external peer
review or Lean verification.

Reviewed files and SHA256:

- `research/high-variance-20261123/GLOBAL_SOURCE_SYNTHESIS.md`:
  `de581110256ab48080e66b150eb0d633e225234d56de89a5f8a178d33c111e60`.
- `research/high-variance-20261123/check_global_source.py`:
  `75b239f0492954b9cc90ad9fa1959d14446f6200e390d88d1db1c057a8c00355`.
- `research/high-variance-20261123/global-source-control.json`:
  `9f3803d814688f026bb2d40d1a4f55d65668f6827c03d87968aa50972343d7df`.

## 1. Original-target permission and the entire inverse language

I read the joint minimum at PR177 commit
`0444986571f09f302cb3687b4bba3552600e4119`,
`research/lean-exact-witness-global-20261121/JOINT_MINIMAL_COUNTEREXAMPLE.md`.
It supplies the full interval hypothesis at every lower complete grade,
not merely at target values below the original target. This is exactly
the hypothesis consumed in the new note.

Canceling the retained tail in the multiset grade leaves a removed grade
eight and only inserted grades at most seven. Multiset descent therefore
holds for every replacement length and every new initial exponent at most
three. The proof does not depend on a finite residue search or a bound on
the number of smaller grades. The replacement inverse word is an actual
positive odd integer word to the unchanged cut vertex, followed by the
literal complete original tail. With exponent three, an available source
`x` captures the original target whenever `t <= 16x+1`. The original
lower-grade hypothesis therefore proves the displayed finite-cut
consequence under genuine badness.

## 2. Finite-tree identities

For a unit root greater than one with a complete certificate to one,
there is no nontrivial cycle in its predecessor tree: such a cycle would
prevent its vertices from reaching one. This uses the supplied certificate
rather than a universal cycle exclusion. A nonunit predecessor has no
odd inverse parent and is a leaf. Restricting to units leaves a rooted
tree containing the root.

I recomputed the unit-child table modulo nine. The degrees are one for
residues 1, 4, 5 and 8, two for residue 2, and zero for residue 7. Summing
the root-boundary identity gives `N_7=N_2+1`. Summing with weight `n`
gives the stated five contributions: `3n`, `n+1`, `-(n-1)`, `-(7n-2)`
and `-(5n-1)`. Their sum equals `3v`.

For a nonnegative harmonic weight, every low-gap unit edge is internal
because the cluster is complete. Canceling those finitely many rows
leaves exactly the gap-at-least-four boundary. Row sums are finite;
there is no divergent subtraction. The note correctly does not infer
a cheaper large source from positive mass beyond that grade boundary.

## 3. All-length obstruction with complete ordinary certificates

At `v=7 mod9`, the only legal low-gap parent is `(4v-1)/3`, a nonunit,
so the asserted two-element cluster is exact. With `x=I_4(v)` and
`y=I_2(x)`, the condition `3^(L+2) | 80v-11` makes the next `L`
gap-three inverses integral. The affine recurrence for `5n-1` shows both
legality and the exponentially growing ratio to the small cluster.

The congruence for `4^m` produces such a `v` for every `L`. The order of
four modulo `3^k` follows from the displayed valuation induction, and the
required right-hand class is one modulo three. Taking
`v=(4^m-1)/3` then gives its literal gap `2m` to one. Thus these are
complete positive ordinary certificates, not only rational shadows.
The terminal gap may be large, so this family does not refute a claim
restricted to the bounded-four joint-source domain. That limitation is
stated in the note and is part of this verdict.

## 4. Why the finite control is exhaustive for its comparison

The checker begins with the only first-hit zero-four source, one. A first
four gives five and then the complete low-gap closure. The second four
must attach to a vertex in that complete first layer, followed again by
the complete low-gap closure. This decomposition covers every first-hit
word with at most two fours, at every length. The queue guard aborts on
failure; it never returns a truncated successful set. The second pass
checks closure under all three legal inverse gaps, and every reported
word is replayed against its actual first-hit word.

The full multiset grade comparison introduces no missing larger gap or
initial exponent: either would insert an entry above eight. With at most
two fours and initial exponent at most three, all eligible first-hit
sources are therefore in the 1371-element census. A complete certificate
can add only terminal gap-two padding at one after its first hit. Such
padding raises its grade and changes no source. If it reaches the same
grade from a lower first-hit grade, its source is bounded by the already
computed strict-lower maximum, which is smaller than the same-grade
maximum. The two maxima in the note are consequently comparisons against
all complete certificates in their stated grade range.

I checked the exact target interval, positive-time source floor, full
literal-prefix contractions and retained tail. The control target
`2^51-1` does descend at shortcut time 138 and reaches one at time 384.
The failed cluster replacement therefore cannot be relabeled as a bad
query or a counterexample to the conditional `FloorIntervalStep`.

I executed the checker and obtained the frozen integer output. The
separate execution receipt records the normal and optimized runs and
their exact output match. These calculations substantiate this finite
control; they do not prove every bounded-four cluster finite or establish
Collatz convergence.

## 5. Scope of the outcome

The new implication under an actual joint bad query is the finite-cut
statement. The boundary identities and the explicit complete controls
are correct. The statement that one of those cheaper cuts must contain
a source capturing the original target remains unproved. Neither the
finite control nor its convergent target supplies that missing badness
information. No global source selector or successful descent is assumed
in the checked argument.
