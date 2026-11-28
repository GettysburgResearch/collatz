import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! Directed unequal-clock integer spacing used in subcritical collision renewal. -/

namespace Collatz.CollisionClockSpacing

/-- Forward positive-gap numerator, in chronological order. -/
def numerator : List ℕ → ℤ
  | [] => 0
  | e :: w => 3 ^ w.length + 2 ^ e * numerator w

theorem numerator_nonneg (w : List ℕ) : 0 ≤ numerator w := by
  induction w with
  | nil => exact le_refl 0
  | cons e w ih =>
    change 0 ≤ (3 : ℤ) ^ w.length + 2 ^ e * numerator w
    positivity

theorem numerator_pos (e : ℕ) (w : List ℕ) : 0 < numerator (e :: w) := by
  have hn := numerator_nonneg w
  change 0 < (3 : ℤ) ^ w.length + 2 ^ e * numerator w
  positivity

/-- The two clocks differ by d. The ordinary integer displacement is h. -/
def matched (n d : ℕ) (w v : List ℕ) (h : ℤ) : Prop :=
  w.length = n ∧ v.length = n ∧ v.sum = w.sum + d ∧
    (3 : ℤ)^n * h = 2^d * numerator w - numerator v

theorem opposite_bounds {n d : ℕ} {w v : List ℕ} {h : ℤ}
    (hm : matched n d w v h) :
    -(numerator v) ≤ 3^n * h ∧ 3^n * h ≤ 2^d * numerator w := by
  rw [hm.2.2.2]
  have hw : 0 ≤ (2 : ℤ)^d * numerator w :=
    mul_nonneg (by positivity) (numerator_nonneg w)
  have hv := numerator_nonneg v
  omega

/-- At the longer word every candidate displacement lies in one dyadic
residue class, even when the visits are compared at different clocks. -/
theorem single_residue {n d : ℕ} {w₁ w₂ v : List ℕ} {h₁ h₂ : ℤ}
    (a : matched n d w₁ v h₁) (b : matched n d w₂ v h₂) :
    (2 : ℤ)^d ∣ h₂ - h₁ := by
  have base : IsCoprime (2 : ℤ) 3 := ⟨-1, 1, by decide⟩
  have cop : IsCoprime ((2 : ℤ)^d) (3^n) := base.pow
  apply cop.dvd_of_dvd_mul_left
  refine ⟨numerator w₂ - numerator w₁, ?_⟩
  linear_combination b.2.2.2 - a.2.2.2

theorem separation {n d : ℕ} {w₁ w₂ v : List ℕ} {h₁ h₂ : ℤ}
    (a : matched n d w₁ v h₁) (b : matched n d w₂ v h₂) (h : h₁ < h₂) :
    h₁ + (2 : ℤ)^d ≤ h₂ := by
  obtain ⟨k, hk⟩ := single_residue a b
  have hp : 0 < (2 : ℤ)^d := by positivity
  have hprod : 0 < 2^d * k := hk ▸ sub_pos.mpr h
  have hkpos : 0 < k := pos_of_mul_pos_right hprod hp.le
  have hkle : 1 ≤ k := by omega
  have hbound := mul_le_mul_of_nonneg_left hkle hp.le
  simpa only [mul_one, ← hk, le_sub_iff_add_le'] using hbound

/-- Ordered representatives cannot pack more densely than the dyadic spacing.
The bound works for signed displacements on either side of the real origin. -/
theorem interval_span (n d : ℕ) (v : List ℕ) (ws : ℕ → List ℕ) (hs : ℕ → ℤ)
    (m : ℕ) (hm : ∀ i, i ≤ m → matched n d (ws i) v (hs i))
    (hi : ∀ i, i < m → hs i < hs (i+1)) :
    hs 0 + (m : ℤ) * 2^d ≤ hs m := by
  induction m with
  | zero => simp
  | succ m ih =>
    have prev := ih (fun i h => hm i (Nat.le_succ_of_le h))
      (fun i h => hi i (Nat.lt_succ_of_lt h))
    have step := separation (hm m (Nat.le_succ m)) (hm (m+1) (le_refl _))
      (hi m (Nat.lt_succ_self _))
    push_cast
    linarith

end Collatz.CollisionClockSpacing
