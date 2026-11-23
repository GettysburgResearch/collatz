module

public import HarmonicTransport

@[expose] public section

/-!
# A clock coordinate retains the cycle case

The transport premise in these closing theorems remains an explicit
hypothesis.  In particular, the module does not construct a critical weight.
-/

namespace CollatzHarmonic

open Finset Function

/-- The terminal state resets the clock.  Every nonterminal step increments it. -/
def clockLift (F : ℕ → ℕ) (s : ℕ × ℕ) : ℕ × ℕ :=
  if s.1 = 1 then (1, 0) else (F s.1, s.2 + 1)

theorem clockLift_iterate (F : ℕ → ℕ) (n h k : ℕ)
    (avoid : ∀ j < k, (F^[j]) n ≠ 1) :
    ((clockLift F)^[k]) (n,h) = ((F^[k]) n, h+k) := by
  induction k with
  | zero => rfl
  | succ k ih =>
    rw [Function.iterate_succ_apply']
    rw [ih (fun j hj ↦ avoid j (by omega))]
    simp only [clockLift, avoid k (by omega), ↓reduceIte]
    rw [Function.iterate_succ_apply']
    rfl

theorem clockLift_injective_of_avoid (F : ℕ → ℕ) (n h : ℕ)
    (avoid : ∀ j, (F^[j]) n ≠ 1) :
    Function.Injective (fun k ↦ ((clockLift F)^[k]) (n,h)) := by
  intro i j eq
  change ((clockLift F)^[i]) (n,h) = ((clockLift F)^[j]) (n,h) at eq
  rw [clockLift_iterate F n h i (fun k _ ↦ avoid k),
      clockLift_iterate F n h j (fun k _ ↦ avoid k)] at eq
  have := congrArg Prod.snd eq
  simp only at this
  omega

/-- A finite fiber formulation of an upper bound for the atomic pushforward.
Singleton fibers are enough for the absorption theorem, while retaining
whole fibers records the source/endpoint orientation correctly. -/
def ColumnBound {α : Type*} (F : α → α) (w : α → ℝ) (k : ℕ) (M : ℝ) : Prop :=
  ∀ y (E : Finset α), (∀ x ∈ E, (F^[k]) x = y) → ∑ x ∈ E, w x ≤ M * w y

theorem atom_of_column {α : Type*} [DecidableEq α]
    {F : α → α} {w : α → ℝ} {k : ℕ} {M : ℝ}
    (h : ColumnBound F w k M) (x : α) :
    w x ≤ M * w ((F^[k]) x) := by
  have h' := h ((F^[k]) x) {x} (by
    intro y hy
    simp only [Finset.mem_singleton] at hy
    subst y
    rfl)
  simpa using h'

/-- This concludes actual absorption, including the case of a nontrivial
cycle of F, because a clock-lifted nonabsorbed orbit is injective. -/
theorem absorption_of_linear_columns (F : ℕ → ℕ)
    {w : (ℕ × ℕ) → ℝ} {W C : ℝ} (hw : FiniteMass w W)
    (hC : 0 < C) (n : ℕ) (ha : 0 < w (n,0))
    (columns : ∀ k, ColumnBound (clockLift F) w k (C*((k : ℝ)+1))) :
    ∃ k, (F^[k]) n = 1 := by
  by_contra! avoid
  have bad := not_injective_of_linear hw ha hC
    (fun k ↦ ((clockLift F)^[k]) (n,0))
    (fun k ↦ by simpa [mul_assoc] using atom_of_column (columns k) (n,0))
  exact bad (clockLift_injective_of_avoid F n 0 avoid)

theorem absorption_of_reciprocal_columns (F : ℕ → ℕ)
    {w : (ℕ × ℕ) → ℝ} {W : ℝ} (hw : FiniteMass w W)
    (n : ℕ) (ha : 0 < w (n,0)) (M : ℕ → ℝ)
    (hp : ∀ k, 0 < M k)
    (hunbounded : ∀ B : ℝ, ∃ N, B < ∑ k ∈ range N, 1 / M k)
    (columns : ∀ k, ColumnBound (clockLift F) w k (M k)) :
    ∃ k, (F^[k]) n = 1 := by
  by_contra! avoid
  have bad := not_injective_of_reciprocal hw ha
    (fun k ↦ ((clockLift F)^[k]) (n,0)) M hp hunbounded
    (fun k ↦ atom_of_column (columns k) (n,0))
  exact bad (clockLift_injective_of_avoid F n 0 avoid)

end CollatzHarmonic
