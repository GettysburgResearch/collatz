import CoreBranching
import Mathlib.Algebra.Order.Archimedean.Basic
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! A pointwise, ordinary-integer discounted parity criterion.
The boundedness assertion in the final equivalence is not established here.
All iterates use the literal shortcut map imported from the pinned packet. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.DiscountedParity
open CoreBranching

def Converges (n : ℕ) : Prop := ∃ k, run k n = 1

def weight (n : ℕ) : ℚ := if n % 2 = 0 then 17 / 32 else 51 / 32

def rank : ℕ → ℕ → ℚ
  | 0, _ => 1
  | k + 1, n => weight n * rank k (step n)

theorem weight_nonneg (n : ℕ) : 0 ≤ weight n := by
  unfold weight
  split <;> norm_num

theorem rank_nonneg (k n : ℕ) : 0 ≤ rank k n := by
  induction k generalizing n with
  | zero => norm_num [rank]
  | succ k ih => exact mul_nonneg (weight_nonneg n) (ih (step n))

theorem rank_add (a b n : ℕ) :
    rank (a+b) n = rank a n * rank b (run a n) := by
  induction a generalizing n with
  | zero => simp [rank, run]
  | succ a ih => simp only [Nat.succ_add, rank, run, ih, mul_assoc]

private theorem step_positive (n : ℕ) (hn : 0<n) : 0<step n := by
  unfold step
  split <;> omega

private theorem run_positive (k n : ℕ) (hn : 0<n) : 0<run k n := by
  induction k generalizing n with
  | zero => exact hn
  | succ k ih => exact ih (step n) (step_positive n hn)

private def smallClock : ℕ → ℕ
  | 1 => 0 | 2 => 1 | 3 => 5 | 4 => 2 | 5 => 4 | 6 => 6 | _ => 0

theorem small_converges (n : ℕ) (hn : 0<n) (hb : n≤6) : Converges n := by
  refine ⟨smallClock n, ?_⟩
  interval_cases n <;> decide +kernel

theorem convergence_of_iterate (k n : ℕ) (h : Converges (run k n)) : Converges n := by
  obtain ⟨j,hj⟩ := h
  exact ⟨k+j, by rw [run_add, hj]⟩

theorem bad_floor (n : ℕ) (hn : 0<n) (hbad : ¬Converges n) :
    ∀ k, 7≤run k n := by
  intro k
  have hp := run_positive k n hn
  by_contra! hlow
  exact hbad (convergence_of_iterate k n (small_converges _ hp (by omega)))

/-- Physical affine growth is strictly slower than the discounted rank. -/
theorem edge_bound (n : ℕ) (hn : 7≤n) :
    (357/352 : ℚ) * (step n : ℚ) ≤ (n : ℚ) * weight n := by
  by_cases h : n%2=0
  · have e : 2*step n=n := by simp only [step,h,ite_true]; omega
    have eq : (2:ℚ)*(step n:ℚ)=(n:ℚ) := by exact_mod_cast e
    have hp : (0:ℚ)≤n := Nat.cast_nonneg n
    simp only [weight,h,ite_true]
    nlinarith
  · have e : 2*step n=3*n+1 := by simp only [step,h,ite_false]; omega
    have eq : (2:ℚ)*(step n:ℚ)=3*(n:ℚ)+1 := by exact_mod_cast e
    have hb : (7:ℚ)≤n := by exact_mod_cast hn
    simp only [weight,h,ite_false]
    nlinarith

theorem physical_bound (k n : ℕ) (floor : ∀ j, 7≤run j n) :
    (357/352 : ℚ)^k * (run k n : ℚ) ≤ (n : ℚ) * rank k n := by
  induction k generalizing n with
  | zero => simp [run,rank]
  | succ k ih =>
    have next : ∀ j, 7≤run j (step n) := by
      intro j
      exact floor (j+1)
    have old := ih (step n) next
    have first := edge_bound n (by simpa [run] using floor 0)
    have rpos := rank_nonneg k (step n)
    have qpos : (0:ℚ)≤357/352 := by norm_num
    calc
      _ = (357/352:ℚ) * ((357/352:ℚ)^k * (run k (step n):ℚ)) := by
        simp only [run,pow_succ]
        ring
      _ ≤ (357/352:ℚ) * ((step n:ℚ)*rank k (step n)) :=
        mul_le_mul_of_nonneg_left old qpos
      _ ≤ (n:ℚ)*rank (k+1) n := by
        have hmul := mul_le_mul_of_nonneg_right first rpos
        simpa only [rank,mul_assoc] using hmul

theorem linear_growth (k : ℕ) :
    1+(k:ℚ)*(5/352) ≤ (357/352:ℚ)^k := by
  induction k with
  | zero => norm_num
  | succ k ih =>
    have hp : (0:ℚ)≤k := Nat.cast_nonneg k
    have h := mul_le_mul_of_nonneg_right ih (by norm_num : (0:ℚ)≤357/352)
    rw [pow_succ, Nat.cast_add, Nat.cast_one]
    nlinarith

/-- A bound at all times forces the same actual starting integer to reach 1. -/
theorem converges_of_bounded (n : ℕ) (hn : 0<n)
    (B : ℚ) (bound : ∀ k, rank k n≤B) : Converges n := by
  by_contra bad
  have floor := bad_floor n hn bad
  obtain ⟨k,hk⟩ := exists_nat_gt (352*(n:ℚ)*B/35)
  have phys := physical_bound k n floor
  have ppos : (0:ℚ)≤(357/352:ℚ)^k := by positivity
  have high : (7:ℚ)≤run k n := by exact_mod_cast floor k
  have lower := mul_le_mul_of_nonneg_left high ppos
  have upper := mul_le_mul_of_nonneg_left (bound k) (Nat.cast_nonneg n : (0:ℚ)≤n)
  have growth := linear_growth k
  nlinarith

theorem rank_one_two (k : ℕ) : rank k 1≤51/32 ∧ rank k 2≤1 := by
  induction k with
  | zero => norm_num [rank]
  | succ k ih =>
    have h1 := rank_nonneg k 1
    have h2 := rank_nonneg k 2
    norm_num only [rank,weight,step]
    simp only [ite_false, ite_true]
    constructor <;> nlinarith [ih.1,ih.2]

theorem bounded_of_converges (n : ℕ) (h : Converges n) :
    ∃ B : ℚ, ∀ k, rank k n≤B := by
  classical
  obtain ⟨K,hK⟩ := h
  let S : ℚ := ∑ j ∈ Finset.range (K+1), rank j n
  have spos : 0≤S := Finset.sum_nonneg (fun j _ => rank_nonneg j n)
  have entry (j : ℕ) (hj : j≤K) : rank j n≤S := by
    apply Finset.single_le_sum (fun i _ => rank_nonneg i n)
    exact Finset.mem_range.mpr (by omega)
  refine ⟨2*S, ?_⟩
  intro k
  by_cases hk : k≤K
  · exact (entry k hk).trans (by linarith)
  · obtain ⟨t,ht⟩ := Nat.exists_eq_add_of_le (show K≤k by omega)
    rw [ht,rank_add,hK]
    have tail := (rank_one_two t).1
    have product := mul_le_mul_of_nonneg_left tail (rank_nonneg K n)
    have lead := entry K le_rfl
    nlinarith

theorem bounded_rank_iff (n : ℕ) (hn : 0<n) :
    (∃ B : ℚ, ∀ k, rank k n≤B) ↔ Converges n := by
  constructor
  · rintro ⟨B,hB⟩
    exact converges_of_bounded n hn B hB
  · exact bounded_of_converges n

end Collatz.DiscountedParity
