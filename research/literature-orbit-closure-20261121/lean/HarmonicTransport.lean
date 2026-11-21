module

public import Mathlib.Order.Interval.Finset.Nat
public import Mathlib.Algebra.Order.Archimedean.Real.Basic
public import Mathlib.Algebra.BigOperators.Ring.Finset
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Positivity

@[expose] public section

/-!
# The critical reciprocal budget for atomic transport

These are elementary deterministic theorems.  A Collatz application must
supply the weight and the transport bound; no such bound is an axiom here.
-/

namespace CollatzHarmonic

open Finset

/-- A formulation of finite nonnegative mass using only finite sums. -/
def FiniteMass {α : Type*} (w : α → ℝ) (W : ℝ) : Prop :=
  (∀ x, 0 ≤ w x) ∧ ∀ E : Finset α, ∑ x ∈ E, w x ≤ W

theorem mass_of_distinct {α : Type*} [DecidableEq α]
    {w : α → ℝ} {W : ℝ} (hw : FiniteMass w W)
    (x : ℕ → α) (N : ℕ)
    (hi : Set.InjOn x (Set.Iio N)) :
    ∑ k ∈ range N, w (x k) ≤ W := by
  have h := hw.2 ((range N).image x)
  rw [sum_image] at h
  · exact h
  · intro a ha b hb hab
    exact hi (by simpa using ha) (by simpa using hb) hab

/-- Every surviving original atom consumes a reciprocal amount of the
finite mass budget at each distinct endpoint. -/
theorem finite_reciprocal_budget {α : Type*} [DecidableEq α]
    {w : α → ℝ} {W a : ℝ} (hw : FiniteMass w W)
    (x : ℕ → α) (M : ℕ → ℝ) (N : ℕ)
    (hi : Set.InjOn x (Set.Iio N))
    (hp : ∀ k < N, 0 < M k)
    (ht : ∀ k < N, a ≤ M k * w (x k)) :
    a * (∑ k ∈ range N, 1 / M k) ≤ W := by
  calc
    a * (∑ k ∈ range N, 1 / M k) = ∑ k ∈ range N, a / M k := by
      rw [mul_sum]
      apply sum_congr rfl
      intro k _
      ring
    _ ≤ ∑ k ∈ range N, w (x k) := by
      apply sum_le_sum
      intro k hk
      exact (div_le_iff₀ (hp k (mem_range.mp hk))).mpr
        (by simpa [mul_comm] using ht k (mem_range.mp hk))
    _ ≤ W := mass_of_distinct hw x N hi

noncomputable def harmonicPrefix (N : ℕ) : ℝ := ∑ k ∈ range N, 1 / ((k : ℝ) + 1)

/-- Every dyadic block contributes at least one half to the harmonic sum. -/
theorem harmonic_dyadic (J : ℕ) :
    (J : ℝ) / 2 ≤ harmonicPrefix (2 ^ J) := by
  induction J with
  | zero => simp [harmonicPrefix]
  | succ J ih =>
    have hp : 0 < (2 ^ J : ℝ) := by positivity
    have block : (1 : ℝ) / 2 ≤
        ∑ k ∈ range (2 ^ J), 1 / (((2 ^ J + k : ℕ) : ℝ) + 1) := by
      calc
        (1 : ℝ) / 2 = ∑ _k ∈ range (2 ^ J), 1 / (2 * (2 ^ J : ℝ)) := by
          simp only [sum_const, card_range, nsmul_eq_mul, Nat.cast_pow, Nat.cast_ofNat]
          field_simp
        _ ≤ _ := by
          apply sum_le_sum
          intro k hk
          apply one_div_le_one_div_of_le (by positivity)
          have hk' : (k : ℝ) + 1 ≤ 2 ^ J := by exact_mod_cast Nat.succ_le_of_lt (mem_range.mp hk)
          push_cast
          linarith
    have hsum : harmonicPrefix (2 ^ (J + 1)) = harmonicPrefix (2 ^ J) +
        ∑ k ∈ range (2 ^ J), 1 / (((2 ^ J + k : ℕ) : ℝ) + 1) := by
      unfold harmonicPrefix
      rw [pow_succ, Nat.mul_two, sum_range_add]
    rw [hsum]
    push_cast at block ⊢
    linarith

/-- A finite, explicit obstruction to a long injective path with a linear
transport bound.  No infinite series theorem is used in this certificate. -/
theorem finite_linear_budget {α : Type*} [DecidableEq α]
    {w : α → ℝ} {W a C : ℝ} (hw : FiniteMass w W)
    (ha : 0 ≤ a) (hC : 0 < C) (x : ℕ → α) (J : ℕ)
    (hi : Set.InjOn x (Set.Iio (2 ^ J)))
    (ht : ∀ k : ℕ, k < 2 ^ J → a ≤ C * ((k : ℝ) + 1) * w (x k)) :
    (J : ℝ) * a ≤ 2 * C * W := by
  have hsum : a * harmonicPrefix (2 ^ J) ≤ C * W := by
    calc
      a * harmonicPrefix (2 ^ J) =
          ∑ k ∈ range (2 ^ J), a / ((k : ℝ) + 1) := by
        simp only [harmonicPrefix, mul_sum]
        apply sum_congr rfl
        intro k _
        ring
      _ ≤ ∑ k ∈ range (2 ^ J), C * w (x k) := by
        apply sum_le_sum
        intro k hk
        apply (div_le_iff₀ (show 0 < (k : ℝ) + 1 by positivity)).mpr
        nlinarith [ht k (mem_range.mp hk)]
      _ = C * ∑ k ∈ range (2 ^ J), w (x k) := (mul_sum ..).symm
      _ ≤ C * W := mul_le_mul_of_nonneg_left (mass_of_distinct hw x (2 ^ J) hi) hC.le
  have hlow := mul_le_mul_of_nonneg_left (harmonic_dyadic J) ha
  nlinarith

/-- A positive atom cannot follow an infinite injective path under a linear
transport bound in a finite mass space. -/
theorem not_injective_of_linear {α : Type*} [DecidableEq α]
    {w : α → ℝ} {W a C : ℝ} (hw : FiniteMass w W)
    (ha : 0 < a) (hC : 0 < C) (x : ℕ → α)
    (ht : ∀ k : ℕ, a ≤ C * ((k : ℝ) + 1) * w (x k)) :
    ¬ Function.Injective x := by
  intro hi
  obtain ⟨J, hJ⟩ := exists_nat_gt (2 * C * W / a)
  have bound := finite_linear_budget hw ha.le hC x J hi.injOn (fun k _ ↦ ht k)
  have strict : 2 * C * W < (J : ℝ) * a := (div_lt_iff₀ ha).mp hJ
  linarith

/-- The exact general threshold: divergence of reciprocal transport bounds
excludes an injective path.  This is weaker than uniform power boundedness. -/
theorem not_injective_of_reciprocal {α : Type*} [DecidableEq α]
    {w : α → ℝ} {W a : ℝ} (hw : FiniteMass w W)
    (ha : 0 < a) (x : ℕ → α) (M : ℕ → ℝ)
    (hp : ∀ k, 0 < M k)
    (hunbounded : ∀ B : ℝ, ∃ N, B < ∑ k ∈ range N, 1 / M k)
    (ht : ∀ k, a ≤ M k * w (x k)) :
    ¬ Function.Injective x := by
  intro hi
  obtain ⟨N, hN⟩ := hunbounded (W / a)
  have bound := finite_reciprocal_budget hw x M N hi.injOn (fun k _ ↦ hp k)
    (fun k _ ↦ ht k)
  have strict : W < (∑ k ∈ range N, 1 / M k) * a := (div_lt_iff₀ ha).mp hN
  nlinarith

end CollatzHarmonic
