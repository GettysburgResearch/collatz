import EarlierOffsets
import Mathlib.Data.Fintype.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-! Finite dyadic boundary budget for actual asynchronous Collatz meetings.
`failed` tests different clocks for the two paths. No decision procedure for
infinite reachability occurs in this test. `fate` is solely a comparison label. -/
set_option autoImplicit false
set_option warningAsError true

namespace DyadicBoundary
open CoreBranching EarlierOffsets
open scoped BigOperators

/-- A finite rational upper bound for distinct terminal fates. -/
def failed (k n : ℕ) : ℚ := if ∃ i j : Fin (k+1), run i n=run j (3*n+2) then 0 else 1

noncomputable def fate (n : ℕ) : ℚ := by
  classical
  exact if Good n then 1 else 0

private theorem fate_step (n : ℕ) : fate (step n) = fate n := by
  have eqv : Good (step n) ↔ Good n := good_run 1 n
  unfold fate
  by_cases h : Good n
  · simp [h,eqv.mpr h]
  · have hs : ¬ Good (step n) := fun hs => h (eqv.mp hs)
    simp [h,hs]

theorem left_fate (n : ℕ) : fate (2*n) = fate n := by
  simpa only [step_double] using (fate_step (2*n)).symm

theorem right_fate (n : ℕ) : fate (2*n+1) = fate (3*n+2) := by
  simpa only [step_odd] using (fate_step (2*n+1)).symm

theorem mismatch_le_failed (k n : ℕ) : |fate (2*n+1)-fate n| ≤ failed k n := by
  rw [right_fate, failed]
  split_ifs with hm
  · obtain ⟨i,j,h⟩ := hm
    have ef := meet_good h
    unfold fate
    by_cases h : Good n
    · simp [h, ef.mp h]
    · have hn : ¬Good (3*n+2) := fun hn => h (ef.mpr hn)
      simp [h, hn]
  · unfold fate
    split_ifs <;> norm_num

/-- The original source in each summand is the indicated positive integer
when the cone starts at a positive integer. -/
def cone (k : ℕ) (f : ℕ → ℚ) (n : ℕ) : ℚ :=
  (∑ t ∈ Finset.range (2^k), f (2^k*n+t)) / 2^k

private theorem parity_sum (N : ℕ) (f : ℕ → ℚ) :
    ∑ t ∈ Finset.range (2*N), f t = ∑ t ∈ Finset.range N, (f (2*t)+f (2*t+1)) := by
  induction N with
  | zero => simp
  | succ N ih =>
    rw [Nat.mul_succ, Finset.sum_range_succ, Finset.sum_range_succ, ih, Finset.sum_range_succ]
    ring

private theorem cone_step (k n : ℕ) (f : ℕ → ℚ) :
    cone (k+1) f n = cone k (fun x => (f (2*x)+f (2*x+1))/2) n := by
  unfold cone
  have hi : (2:ℕ)^(k+1)=2*2^k := by rw [pow_succ, Nat.mul_comm]
  rw [hi, parity_sum]
  have ie (t : ℕ) : (2*(2^k)*n+2*t, 2*(2^k)*n+(2*t+1)) =
      (2*(2^k*n+t), 2*(2^k*n+t)+1) := by congr 1 <;> ring
  simp only [show ∀ t : ℕ, 2*(2^k)*n+2*t=2*(2^k*n+t) from fun t => congrArg Prod.fst (ie t),
    show ∀ t : ℕ, 2*(2^k)*n+(2*t+1)=2*(2^k*n+t)+1 from fun t => congrArg Prod.snd (ie t)]
  simp only [div_eq_mul_inv, ←Finset.sum_mul, pow_succ]
  ring

private theorem cone_sub (k n : ℕ) (f g : ℕ → ℚ) :
    cone k f n-cone k g n = cone k (fun x => f x-g x) n := by
  simp only [cone, Finset.sum_sub_distrib, sub_div]

private theorem cone_abs (k n : ℕ) (f g : ℕ → ℚ) (bound : ∀ m, |f m|≤g m) :
    |cone k f n|≤cone k g n := by
  unfold cone
  rw [abs_div, abs_of_pos (by positivity : 0<(2:ℚ)^k)]
  apply div_le_div_of_nonneg_right _ (by positivity)
  exact (Finset.abs_sum_le_sum_abs _ _).trans (Finset.sum_le_sum (fun t _ => bound _))

/-- The unsmoothed signed disagreement occurs only on the right child. -/
theorem signed_increment (k n : ℕ) :
    cone (k+1) fate n - cone k fate n = cone k (fun v => (fate (3*v+2)-fate v)/2) n := by
  rw [cone_step, cone_sub]
  congr 1
  funext v
  rw [left_fate, right_fate]
  ring

theorem increment_budget (clock : ℕ → ℕ) (k n : ℕ) :
    |cone (k+1) fate n-cone k fate n| ≤ cone k (fun v => failed (clock v) v / 2) n := by
  rw [signed_increment]
  apply cone_abs
  intro v
  rw [abs_div, abs_of_pos (by norm_num : (0:ℚ)<2)]
  apply div_le_div_of_nonneg_right _ (by norm_num)
  rw [←right_fate]
  exact mismatch_le_failed _ _

/-- For every source cone and every finite horizon, the budget keeps the
actual nonmeeting pair and the source-dependent searching deadline. -/
theorem finite_boundary_budget (clock : ℕ → ℕ) (r n : ℕ) :
    |cone r fate n-fate n| ≤
      ∑ k ∈ Finset.range r, cone k (fun v => failed (clock v) v / 2) n := by
  induction r with
  | zero => simp [cone]
  | succ r ih =>
    rw [Finset.sum_range_succ]
    calc
      |cone (r+1) fate n-fate n| = |(cone r fate n-fate n)+(cone (r+1) fate n-cone r fate n)| := by ring_nf
      _ ≤ _ := abs_add_le _ _
      _ ≤ _ := add_le_add ih (increment_budget clock r n)

#print axioms signed_increment
#print axioms finite_boundary_budget

end DyadicBoundary
