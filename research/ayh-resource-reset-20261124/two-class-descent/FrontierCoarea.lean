import Mathlib

/-! Finite incidence counting for dyadic first-passage floors. -/

namespace Collatz.FrontierCoarea

/-- A clock cannot first cross two distinct integer dyadic levels if the
previous joint running minimum is at most twice the current minimum. -/
theorem single_dyadic_floor {y z a b : ℕ} (hstep : z ≤ 2 * y)
    (ha : y < 2 ^ a) (ha' : 2 ^ a ≤ z)
    (hb : y < 2 ^ b) (hb' : 2 ^ b ≤ z) : a = b := by
  have forbid : ∀ i j : ℕ, y < 2 ^ i → 2 ^ j ≤ z → i < j → False := by
    intro i j hi hj hij
    have hpow : 2 ^ (i + 1) ≤ (2 : ℕ) ^ j :=
      Nat.pow_le_pow_right (by decide) (by omega)
    rw [pow_succ] at hpow
    omega
  by_contra h
  rcases lt_or_gt_of_ne h with hab | hba
  · exact forbid a b ha hb' hab
  · exact forbid b a hb ha' hba

/-- If each original surviving source is incident with at most K selected
floors, the total small-lag count over floors costs only K times the number
of original surviving sources. The surviving set may be determined by a
finite certificate independently of the colors. -/
theorem total_incidence_le {Source Floor : Type*}
    (survivors : Finset Source) (floors : Finset Floor)
    (incidence : Source → Floor → ℕ) (K : ℕ)
    (h : ∀ n ∈ survivors, ∑ l ∈ floors, incidence n l ≤ K) :
    (∑ l ∈ floors, ∑ n ∈ survivors, incidence n l) ≤ survivors.card * K := by
  rw [Finset.sum_comm]
  calc
    _ ≤ ∑ _n ∈ survivors, K := Finset.sum_le_sum h
    _ = survivors.card * K := by simp

/-- Some tested floor attains at most the arithmetic mean of all the finite
counts, expressed without division. -/
theorem exists_floor_le {Source Floor : Type*}
    (survivors : Finset Source) (floors : Finset Floor) (hn : floors.Nonempty)
    (incidence : Source → Floor → ℕ) (K : ℕ)
    (h : ∀ n ∈ survivors, ∑ l ∈ floors, incidence n l ≤ K) :
    ∃ l ∈ floors, floors.card * (∑ n ∈ survivors, incidence n l) ≤
      survivors.card * K := by
  classical
  obtain ⟨l, hl, hmin⟩ := Finset.exists_min_image floors
    (fun t => ∑ n ∈ survivors, incidence n t) hn
  refine ⟨l, hl, ?_⟩
  calc
    _ = ∑ _t ∈ floors, ∑ n ∈ survivors, incidence n l := by simp
    _ ≤ ∑ t ∈ floors, ∑ n ∈ survivors, incidence n t :=
      Finset.sum_le_sum hmin
    _ ≤ _ := total_incidence_le survivors floors incidence K h

end Collatz.FrontierCoarea

#print axioms Collatz.FrontierCoarea.single_dyadic_floor
#print axioms Collatz.FrontierCoarea.exists_floor_le
