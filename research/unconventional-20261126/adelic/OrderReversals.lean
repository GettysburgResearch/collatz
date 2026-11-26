import CoreBranching

/-! Exact grades and ordinary outputs for the order-reversal argument. The
    finite sorted-residue tests include the end-to-start lift by one dyadic
    modulus. All closed computations below are decided by the Lean kernel. -/
namespace OrderReversals

open CoreBranching

def grade : ℕ → ℕ → ℕ
  | 0, _ => 0
  | h+1, n => n%2 + grade h (step n)

def sortedFrom (previous : ℕ) : List ℕ → Bool
  | [] => true
  | a :: tail => decide (previous ≤ a) && sortedFrom a tail

def gradeClassSorted (h p : ℕ) : Bool :=
  let residues := (List.range (2^h)).filter (fun n => grade h n == p)
  match residues.map (run h) with
  | [] => true
  | first :: rest => sortedFrom first (rest ++ [first + 3^p])

set_option maxRecDepth 10000 in
set_option maxHeartbeats 3000000 in
theorem three_even_finite_rows :
    gradeClassSorted 5 2 = true ∧ gradeClassSorted 6 3 = true ∧
    gradeClassSorted 7 4 = true := by decide

theorem reversal_seeds :
    grade 6 48 = 2 ∧ grade 6 49 = 2 ∧ run 6 48 = 8 ∧ run 6 49 = 7 ∧
    grade 8 248 = 5 ∧ grade 8 249 = 5 ∧ run 8 248 = 242 ∧ run 8 249 = 238 := by decide

theorem contraction_reversal :
    grade 46 859 = 29 ∧ grade 46 860 = 29 ∧ (3 : ℕ)^29 < 2^46 ∧
    run 46 859 = 890 ∧ run 46 860 = 866 ∧ 859 < run 46 860 ∧
    run 46 860 < run 46 859 := by decide

theorem double_lap_carry (q a c₀ c₁ : ℤ) (h : c₀-c₁=q+a) :
    a*c₀ + q*c₁ = (q+a)*(c₀-q) := by
  have hc : c₀=c₁+q+a := by omega
  rw [hc]
  ring

#print axioms three_even_finite_rows
#print axioms reversal_seeds
#print axioms contraction_reversal
#print axioms double_lap_carry
end OrderReversals
