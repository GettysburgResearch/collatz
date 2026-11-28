import StoppedRecord
import Mathlib.Tactic.Ring

/-! The exact computable median test for a genuine Collatz visit. -/
set_option autoImplicit false
set_option warningAsError true
namespace Collatz.MedianDeadline
open CoreBranching Collatz.CofactorDescent

def reachedByMedian (n y : ℕ) : Prop :=
  ∃ m : ℕ, run m n = y ∧ 4^m ≤ 3^m * n^2

private theorem block_ratio (B : ℕ) :
    3^(5*B) * (2^B)^2 ≤ 4^(5*B) := by
  calc
    3^(5*B) * (2^B)^2 = (3^5 * 2^2)^B := by
      rw [mul_pow, ← pow_mul, ← pow_mul, ← pow_mul]
      rw [Nat.mul_comm B 2]
    _ ≤ (4^5)^B := Nat.pow_le_pow_left (by decide) _
    _ = 4^(5*B) := (pow_mul _ _ _).symm

/-- Any qualifying date lies strictly before five times any strict binary
    size bound on the ordinary source. -/
theorem clock_lt_five_bits (n B m : ℕ) (hn : n < 2^B)
    (hm : 4^m ≤ 3^m*n^2) : m < 5*B := by
  by_contra! h
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le h
  have hstrict : 3^(5*B)*n^2 < 4^(5*B) :=
    lt_of_lt_of_le (Nat.mul_lt_mul_of_pos_left
      (Nat.pow_lt_pow_left hn (by decide)) (Nat.pow_pos (by decide))) (block_ratio B)
  have htail : 3^k ≤ 4^k := Nat.pow_le_pow_left (by decide) k
  have hbound : (3^(5*B)*n^2)*3^k < 4^(5*B)*4^k :=
    lt_of_lt_of_le (Nat.mul_lt_mul_of_pos_right hstrict (Nat.pow_pos (by decide)))
      (Nat.mul_le_mul_left _ htail)
  rw [pow_add,pow_add] at hm
  have : (3^(5*B)*n^2)*3^k = 3^(5*B)*3^k*n^2 := by ring
  omega

def test (n y : ℕ) : Bool :=
  (List.range (5*(n.log2+1))).any fun m =>
    decide (run m n = y ∧ 4^m ≤ 3^m*n^2)

/-- Boolean finite search agrees with the unbounded integer-power definition,
    including starts already at their target. -/
theorem test_iff (n y : ℕ) : test n y = true ↔ reachedByMedian n y := by
  simp only [test, List.any_eq_true, List.mem_range, decide_eq_true_eq,
    reachedByMedian]
  constructor
  · rintro ⟨m, _, hm⟩
    exact ⟨m, hm⟩
  · rintro ⟨m, hm⟩
    exact ⟨m, clock_lt_five_bits n _ m Nat.lt_log2_self hm.2, hm⟩

set_option maxRecDepth 100000 in
set_option maxHeartbeats 1000000 in
theorem native_examples : test 3 1 = true ∧ test 27 1 = false ∧ run 70 27 = 1 := by
  decide

end Collatz.MedianDeadline
