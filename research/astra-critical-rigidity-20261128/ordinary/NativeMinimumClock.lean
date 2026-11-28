import InverseSuffixTransport
import Mathlib.Data.Nat.Find

/-! The true first global minimum clock and its exact additivity at a first odd gate. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.NativeMinimumClock
open Collatz.PoweredAffine Collatz.InverseSuffixTransport
open scoped Classical

private theorem reachable (x : ℕ) : ∃ y, ∃ t : ℕ, orbit x t = y :=
  ⟨x, 0, rfl⟩

noncomputable def minimumValue (x : ℕ) : ℕ := Nat.find (reachable x)

private theorem attained (x : ℕ) : ∃ t, orbit x t = minimumValue x :=
  Nat.find_spec (reachable x)

/-- The first date at which the least value on the entire infinite actual orbit is attained. -/
noncomputable def minimumDate (x : ℕ) : ℕ := Nat.find (attained x)

theorem minimumDate_spec (x : ℕ) :
    (∀ i, orbit x (minimumDate x) ≤ orbit x i) ∧
    (∀ i < minimumDate x, orbit x (minimumDate x) < orbit x i) := by
  have atDate : orbit x (minimumDate x) = minimumValue x := Nat.find_spec (attained x)
  have lower (i : ℕ) : minimumValue x ≤ orbit x i :=
    Nat.find_min' (reachable x) ⟨i, rfl⟩
  refine ⟨fun i => atDate.le.trans (lower i), ?_⟩
  intro i hi
  rw [atDate]
  exact lt_of_le_of_ne (lower i) (Ne.symm (Nat.find_min (attained x) hi))

private theorem date_unique {x t : ℕ}
    (lower : ∀ i, orbit x t ≤ orbit x i)
    (early : ∀ i < t, orbit x t < orbit x i) : minimumDate x = t := by
  obtain ⟨lower', early'⟩ := minimumDate_spec x
  have eq := Nat.le_antisymm (lower (minimumDate x)) (lower' t)
  rcases lt_trichotomy (minimumDate x) t with h | h | h
  · have := early _ h
    omega
  · exact h
  · have := early' _ h
    omega

private theorem orbit_add (x i j : ℕ) : orbit x (i+j) = orbit (orbit x i) j := by
  induction i generalizing x with
  | zero => simp [orbit]
  | succ i ih =>
    rw [Nat.succ_add]
    exact ih (step x)

/-- A first odd entrance is a strict native record, including intervening even states. -/
theorem strict_record_of_firstOddBelow {x z d : ℕ} (entrance : FirstOddBelow x z d) :
    ∀ i < d, orbit x d < orbit x i := by
  intro i hi
  by_cases within : orbit x i ≤ z
  · have coast := prior_target_coast (a := orbit x i) rfl within entrance hi.le
    have pos : 0 < orbit x d := by have := entrance.1.1; omega
    have pow : 2 ≤ (2:ℕ)^(d-i) := by
      exact Nat.pow_le_pow_right (by decide : 0 < (2:ℕ)) (show 1 ≤ d-i by omega)
    have m := Nat.mul_le_mul_right (orbit x d) pow
    omega
  · exact lt_of_le_of_lt entrance.1.2 (by omega)

/-- The complete global-minimum time adds exactly across any actual strict native record. -/
theorem minimumDate_at_record {x d : ℕ} (record : ∀ i < d, orbit x d < orbit x i) :
    minimumDate x = d + minimumDate (orbit x d) := by
  let y := orbit x d
  change minimumDate x = d + minimumDate y
  obtain ⟨lower, early⟩ := minimumDate_spec y
  have min_le_y : orbit y (minimumDate y) ≤ y := lower 0
  apply date_unique
  · intro i
    rw [orbit_add]
    by_cases h : i < d
    · exact min_le_y.trans (record i h).le
    · obtain ⟨j, rfl⟩ := Nat.exists_eq_add_of_le (by omega : d ≤ i)
      rw [orbit_add]
      exact lower j
  · intro i hi
    rw [orbit_add]
    by_cases h : i < d
    · exact lt_of_le_of_lt min_le_y (record i h)
    · obtain ⟨j, rfl⟩ := Nat.exists_eq_add_of_le (by omega : d ≤ i)
      rw [orbit_add]
      exact early j (by omega)

/-- Clocked landing at a genuine first odd gate retains the entire downstream minimum clock. -/
theorem minimumDate_at_firstOddBelow {x z d : ℕ} (entrance : FirstOddBelow x z d) :
    minimumDate x = d + minimumDate (orbit x d) :=
  minimumDate_at_record (strict_record_of_firstOddBelow entrance)

private theorem minimumDate_after_step {x : ℕ} (later : 0 < minimumDate x) :
    minimumDate x = 1 + minimumDate (step x) := by
  obtain ⟨k, hk⟩ := Nat.exists_eq_succ_of_ne_zero (show minimumDate x ≠ 0 by omega)
  have hs := minimumDate_spec x
  have h : minimumDate (step x) = k := by
    apply date_unique
    · intro i
      have h' := hs.1 (i+1)
      simpa [hk, orbit] using h'
    · intro i hi
      have h' := hs.2 (i+1) (by omega)
      simpa [hk, orbit] using h'
  omega

/-- Moving an odd source to the unit embedding 4x+1 costs exactly two extra dates
whenever its true minimum occurs later than its source date. -/
theorem minimumDate_unit_embedding {x : ℕ} (odd : x % 2 = 1) (later : 0 < minimumDate x) :
    minimumDate (4*x+1) = minimumDate x + 2 := by
  have s₁ : step (4*x+1) = 6*x+2 := by unfold step; split <;> omega
  have s₂ : step (6*x+2) = 3*x+1 := by unfold step; split <;> omega
  have s₃ : step (3*x+1) = step x := by unfold step; split <;> split <;> omega
  have update := odd_step odd
  have prior : ∀ i < 3, orbit (4*x+1) 3 < orbit (4*x+1) i := by
    intro i hi
    have dates : i = 0 ∨ i = 1 ∨ i = 2 := by omega
    rcases dates with rfl | rfl | rfl <;> simp only [orbit, s₁, s₂, s₃] <;> omega
  have alternate : minimumDate (4*x+1) = 3 + minimumDate (step x) := by
    simpa only [orbit, s₁, s₂, s₃] using minimumDate_at_record prior
  have original := minimumDate_after_step later
  omega

end Collatz.NativeMinimumClock
