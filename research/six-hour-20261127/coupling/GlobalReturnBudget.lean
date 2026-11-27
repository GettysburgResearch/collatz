import ReturnTwentyFour
import QuantitativeReturn

/-! Composition with the byte-pinned PR197 binary-class localization.
Both ordinary map definitions and both hitting predicates are compared here. -/
set_option autoImplicit false
set_option warningAsError true
open private CollatzQuantitativeReturn.from16 CollatzQuantitativeReturn.Ans
  CollatzQuantitativeReturn.D CollatzQuantitativeReturn.f from QuantitativeReturn
namespace GlobalReturnBudget
open CoreBranching CollatzReverseBasin CollatzTwoOdd
open EarlierOffsets (Good)

theorem hits (n k : ℕ) : Hits n k ↔ run k n=1 := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact ih (step n)

theorem basin (n : ℕ) : Basin n ↔ Good n := by
  constructor
  · rintro ⟨k,h⟩; exact ⟨k,(hits _ _).mp h⟩
  · rintro ⟨k,h⟩; exact ⟨k,(hits _ _).mpr h⟩

/-- Every actual bad positive n forces a genuine reverse defect at an
ordinary canonical cofactor at most 201326592 times n. -/
theorem bounded_defect (n : ℕ) (positive : 0<n) (bad : ¬Good n) :
    ∃ y, ReverseDefect y ∧ y≤201326592*n := by
  obtain ⟨w,_,res,wb,b,g⟩:=ReturnTwentyFour.binary_defect n positive bad
  have bw : ¬Basin w := fun h => b ((basin w).mp h)
  have gw : Basin (3*w) := (basin _).mpr g
  have defect : CollatzQuantitativeReturn.D w := by
    simp only [CollatzQuantitativeReturn.D,CollatzQuantitativeReturn.f,
      decide_eq_false_iff_not,decide_eq_true_eq]
    exact ⟨bw,gw⟩
  obtain ⟨y,defy,cap⟩:=CollatzQuantitativeReturn.from16 w res defect
  exact ⟨y,defy,by omega⟩

/-- A least canonical reverse disagreement has this global ordinary floor.
The statement makes no bounded-cycle or special-Mersenne assumption. -/
theorem least_floor (z : ℕ) (least : ∀ y, ReverseDefect y → z≤y)
    (n : ℕ) (positive : 0<n) (below : 201326592*n<z) : Good n := by
  by_contra bad
  obtain ⟨y,dy,cap⟩:=bounded_defect n positive bad
  exact (Nat.not_lt_of_ge (least y dy)) (by omega)

#print axioms hits
#print axioms basin
#print axioms bounded_defect
#print axioms least_floor
end GlobalReturnBudget
