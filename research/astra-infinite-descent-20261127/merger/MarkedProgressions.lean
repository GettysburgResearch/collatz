import AllProgressions
import MarkedWindow

/-! Independently prescribed first-hit time and odd-departure residue
classes for ordinary finite patterns in relative intervals. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.MarkedProgressions

theorem mixed_blocks (F : List ℕ) (v r s M Q : ℕ) (mp : 0<M) (qp : 0<Q)
    (δ : ℝ) (positive : 0<δ) : FastBlocks.Placement F v r s M Q δ :=
  FastBlocks.of_marked_visitors F v r s M Q mp qp δ positive
    (fun η ep => FastWindow.visitors_residues η ep M Q mp qp)

/-- One certificate covers every source residue of any prescribed
positive modulus, at one common near-fast first clock and odd grade
with independently chosen congruences on both quantities. -/
theorem all_residues (F : List ℕ) (m M Q : ℕ) (mp : 0<m) (tm : 0<M) (gm : 0<Q)
    (δ : ℝ) (positive : 0<δ) : AllProgressions.Placement F m M Q δ :=
  AllProgressions.of_marked_visitors F m M Q mp tm gm δ positive
    (fun η ep => FastWindow.visitors_residues η ep M Q tm gm)

#print axioms mixed_blocks
#print axioms all_residues
end Collatz.MarkedProgressions
