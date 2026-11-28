import TwoGapRouting
import Mathlib.Data.Nat.Choose.Sum

/-! Not every ordinary ternary-unit target admits a contractive inverse
route, even with arbitrary clock and odd count. -/
namespace Collatz.MergerThreshold
open Collatz.TwoGapRouting

theorem forward_lower (D n : ℕ) :
    3^(odds D n)*n+odds D n ≤ 2^D*run D n := by
  induction D generalizing n with
  | zero => simp [run,odds]
  | succ h ih =>
    have eq : 2*step n=3^(n%2)*n+n%2 := by
      unfold step
      split <;> rename_i p
      · rw [p]; simp; omega
      · rw [show n%2=1 by omega]; simp; omega
    have v:=Nat.mul_le_mul_left 2 (ih (step n))
    have u:=congrArg (fun a : ℕ => 3^(odds h (step n))*a) eq
    have w:=Nat.mul_le_mul_right (n%2) (Nat.one_le_pow (odds h (step n)) 3 (by decide))
    change 3^(n%2+odds h (step n))*n+(n%2+odds h (step n))≤2^(h+1)*run h (step n)
    rw [pow_add,pow_succ]
    nlinarith only [v,u,w,eq, Nat.zero_le (odds h (step n))]

private def small (n : ℕ) : Prop := n=0 ∨ n=1 ∨ n=2 ∨ n=3 ∨ n=4 ∨ n=5 ∨ n=6 ∨ n=8
private theorem closed (n : ℕ) (h : small n) : small (step n) := by
  rcases h with h|h|h|h|h|h|h|h <;> subst n <;> unfold small <;> decide +kernel

private theorem stays (D n : ℕ) (h : small n) : small (run D n) := by
  induction D generalizing n with
  | zero => exact h
  | succ D ih => exact ih _ (closed n h)

theorem seven_floor (D n : ℕ) (hit : run D n=7) : 7≤n := by
  by_contra! hn
  have h : small n := by unfold small; omega
  have s:=stays D n h
  rw [hit] at s
  unfold small at s
  omega

/-- In particular, an all-unit router cannot cross below the critical slope
merely by allowing arbitrary length or by omitting the root 1. -/
theorem seven_growth (D n : ℕ) (nonempty : 0<D) (hit : run D n=7) :
    3^(odds D n)<2^D := by
  have a:=forward_lower D n
  rw [hit] at a
  have b:=Nat.mul_le_mul_left (3^(odds D n)) (seven_floor D n hit)
  by_cases z : odds D n=0
  · rw [z,pow_zero]
    exact Nat.one_lt_two_pow (by omega)
  · omega

/-- Binomial bound for cheap words at grade 5k. Five chosen positions among
eight per k encode all positive gap lists with cumulative budget at most 8k. -/
theorem cheap_entropy (k : ℕ) :
    (8*k).choose (5*k) * (5^5*3^3)^k ≤ (8^8)^k := by
  have term := Finset.single_le_sum (f:=fun i : ℕ =>
    5^i*3^(8*k-i)*(8*k).choose i) (fun i _ => Nat.zero_le _)
    (show 5*k ∈ Finset.range (8*k+1) by simp; omega)
  have total : (∑ i ∈ Finset.range (8*k+1), 5^i*3^(8*k-i)*(8*k).choose i)=(8:ℕ)^(8*k) := by
    simpa using (add_pow (5:ℕ) 3 (8*k)).symm
  rw [total] at term
  have dif : 8*k-5*k=3*k := by omega
  rw [dif,pow_mul (5:ℕ) 5 k,pow_mul (3:ℕ) 3 k,pow_mul (8:ℕ) 8 k] at term
  rw [mul_pow]
  simpa only [Nat.mul_comm, Nat.mul_left_comm, Nat.mul_assoc] using term

theorem base_strict : (8:ℕ)^8 < 5^5*3^8 := by decide +kernel

#print axioms forward_lower
#print axioms seven_floor
#print axioms seven_growth
#print axioms cheap_entropy
#print axioms base_strict
end Collatz.MergerThreshold
