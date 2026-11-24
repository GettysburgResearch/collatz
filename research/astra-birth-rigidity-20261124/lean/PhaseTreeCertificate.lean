import Std

/-!
Finite residue certificate for the phase-one inverse tree.
Each row contains a residue modulo 27 and three pairs of child carries,
one pair for each lift of that residue modulo 81.
-/

namespace Collatz.PhaseTreeCertificate

abbrev Row := Nat × Array (Nat × Nat)

def table : Array Row := #[
  ( 1, #[(6, 8), (6, 8), (10, 16)]),
  ( 4, #[(6, 12), (6, 10), (6, 10)]),
  ( 5, #[(7, 13), (7, 11), (7, 11)]),
  (10, #[(6, 8), (6, 8), (6, 8)]),
  (13, #[(8, 12), (6, 8), (6, 8)]),
  (14, #[(11, 15), (9, 11), (9, 11)]),
  (17, #[(7, 9), (7, 9), (7, 9)]),
  (22, #[(10, 14), (8, 10), (8, 10)]),
  (23, #[(7, 9), (9, 13), (7, 9)]),
  (26, #[(7, 13), (7, 9), (9, 11)])
]

def rowResidue (i : Fin 10) : Nat := table[i.val]!.1

def liftedResidue (i : Fin 10) (j : Fin 3) : Nat := rowResidue i + 27 * j.val

def choices (i : Fin 10) (j : Fin 3) : Nat × Nat := table[i.val]!.2[j.val]!

/-- The least nonnegative residue of 4 * 4^d * v - 2^(-d) modulo 81. -/
def numeratorResidue (v d : Nat) : Nat := (4 * 4^d * v + (81 - 41^d % 81)) % 81

def validChild (v d : Nat) : Prop :=
  6 ≤ d ∧ d ≤ 16 ∧ numeratorResidue v d % 3 = 0 ∧
    ∃ r : Fin 10, numeratorResidue v d / 3 = rowResidue r

instance (v d : Nat) : Decidable (validChild v d) := by
  unfold validChild
  infer_instance

theorem dimensions : table.size = 10 ∧ ∀ i : Fin 10, table[i.val]!.2.size = 3 := by
  decide

theorem inverseOfTwo : (2 * 41) % 81 = 1 := by decide

set_option maxRecDepth 20000 in
set_option maxHeartbeats 1600000 in
theorem all_lifts :
    ∀ (i : Fin 10) (j : Fin 3),
      (choices i j).1 ≠ (choices i j).2 ∧
      (choices i j).1 + (choices i j).2 ≤ 26 ∧
      validChild (liftedResidue i j) (choices i j).1 ∧
      validChild (liftedResidue i j) (choices i j).2 := by
  decide

end Collatz.PhaseTreeCertificate

#print axioms Collatz.PhaseTreeCertificate.dimensions
#print axioms Collatz.PhaseTreeCertificate.inverseOfTwo
#print axioms Collatz.PhaseTreeCertificate.all_lifts
