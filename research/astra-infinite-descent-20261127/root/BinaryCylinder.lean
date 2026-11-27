import BinaryPrefixCriterion
import Mathlib.Algebra.BigOperators.Ring.Finset

/-! Exact binary-cylinder bookkeeping for the actual shortcut map.
The six imported modules are unchanged PR201 sources pinned in SOURCES.json.
No convergence premise is used in this file. -/
set_option autoImplicit false
set_option warningAsError true

namespace BinaryCylinder
open CoreBranching PeakRigidity FloorCounting BinaryPrefixCriterion
open scoped BigOperators

theorem grade_le (N x : ℕ) : grade N x ≤ N := by
  induction N with
  | zero => simp [grade]
  | succ N ih =>
    simp only [grade]
    have h : run N x % 2 < 2 := Nat.mod_lt _ (by decide)
    omega

theorem gate_zero (x : ℕ) : Gate 0 x := by
  intro j hj
  have : j=0 := by simpa using Finset.mem_range.mp hj
  subst j
  simp [grade]

theorem gate_succ (N x : ℕ) :
    Gate (N+1) x ↔ Gate N x ∧ 5*(N+1) ≤ 8*grade (N+1) x := by
  constructor
  · intro h
    constructor
    · intro j hj
      exact h j (Finset.mem_range.mpr (by
        have := Finset.mem_range.mp hj
        omega))
    · exact h (N+1) (Finset.mem_range.mpr (by omega))
  · rintro ⟨h, hlast⟩ j hj
    have jle := Finset.mem_range.mp hj
    by_cases hjn : j=N+1
    · simpa [hjn] using hlast
    · exact h j (Finset.mem_range.mpr (by omega))

theorem gate_mono {N M x : ℕ} (h : Gate N x) (le : M≤N) : Gate M x := by
  intro j hj
  exact h j (Finset.mem_range.mpr (by
    have := Finset.mem_range.mp hj
    omega))

theorem grade_shift (N x : ℕ) : grade N (x+2^N)=grade N x := by
  simpa using (lift_prefix N 0 x 1).2

theorem run_shift (N x : ℕ) : run N (x+2^N)=run N x+3^(grade N x) := by
  simpa using (lift_prefix N 0 x 1).1

theorem gate_shift (N x : ℕ) : Gate N (x+2^N) ↔ Gate N x := by
  have eq (j : ℕ) (hj : j≤N) : grade j (x+2^N)=grade j x := by
    have h := (lift_prefix j (N-j) x 1).2
    simpa [Nat.add_sub_of_le hj] using h
  constructor <;> intro h j hj
  · have jn : j≤N := by have := Finset.mem_range.mp hj; omega
    simpa [eq j jn] using h j hj
  · have jn : j≤N := by have := Finset.mem_range.mp hj; omega
    simpa [eq j jn] using h j hj

theorem paired_parity (N x : ℕ) :
    run N x%2 + run N (x+2^N)%2=1 := by
  rw [run_shift, Nat.add_mod]
  have odd : 3^(grade N x)%2=1 := by simp [Nat.pow_mod]
  rw [odd]
  have h := Nat.mod_lt (run N x) (by decide : 0<2)
  omega

theorem paired_power (N x : ℕ) :
    2^(grade (N+1) x)+2^(grade (N+1) (x+2^N))=3*2^(grade N x) := by
  have pp := paired_parity N x
  simp only [grade, grade_shift, pow_add]
  have h0 := Nat.mod_lt (run N x) (by decide : 0<2)
  have h1 := Nat.mod_lt (run N (x+2^N)) (by decide : 0<2)
  rcases (show run N x%2=0 ∨ run N x%2=1 by omega) with h|h
  · have h' : run N (x+2^N)%2=1 := by omega
    simp [h,h']; omega
  · have h' : run N (x+2^N)%2=0 := by omega
    simp [h,h']; omega

/-- The exact grade generating polynomial at the positive weight two. -/
theorem grade_power_sum (N : ℕ) :
    ∑ x ∈ Finset.range (2^N), 2^(grade N x) = 3^N := by
  induction N with
  | zero => simp [grade]
  | succ N ih =>
    rw [pow_succ, Nat.mul_two, Finset.sum_range_add]
    rw [←Finset.sum_add_distrib]
    calc
      ∑ x ∈ Finset.range (2^N),
          (2^(grade (N+1) x)+2^(grade (N+1) (2^N+x))) =
          ∑ x ∈ Finset.range (2^N), 3*2^(grade N x) := by
            apply Finset.sum_congr rfl
            intro x _
            simpa [Nat.add_comm] using paired_power N x
      _ = 3*(∑ x ∈ Finset.range (2^N), 2^(grade N x)) := by rw [Finset.mul_sum]
      _ = 3^(N+1) := by rw [ih,pow_succ]; omega

def accepted (N : ℕ) : Finset ℕ := (Finset.range (2^N)).filter (Gate N)

/-- A rational Chernoff bound at every eighth binary clock. -/
theorem accepted_card_eighth (k : ℕ) :
    (accepted (8*k)).card * 2^(5*k) ≤ 3^(8*k) := by
  calc
    (accepted (8*k)).card * 2^(5*k) =
        ∑ _x ∈ accepted (8*k), 2^(5*k) := by simp
    _ ≤ ∑ x ∈ accepted (8*k), 2^(grade (8*k) x) := by
      apply Finset.sum_le_sum
      intro x hx
      have hg := (Finset.mem_filter.mp hx).2
      have b := hg (8*k) (Finset.mem_range.mpr (by omega))
      exact Nat.pow_le_pow_right (by decide) (by omega)
    _ ≤ ∑ x ∈ Finset.range (2^(8*k)), 2^(grade (8*k) x) := by
      exact Finset.sum_le_sum_of_subset_of_nonneg
        (Finset.filter_subset _ _) (by intros; positivity)
    _ = 3^(8*k) := grade_power_sum (8*k)

#print axioms grade_power_sum
#print axioms accepted_card_eighth
end BinaryCylinder
