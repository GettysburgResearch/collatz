import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! The three coefficient rows of the mixed Hardy equation recover every
ordinary odd Collatz edge. No hypothesis concerns a probabilistic word. -/
namespace Collatz.Diagonal.OrdinaryHardy

def Edge (x y e : ℕ) : Prop :=
  x % 2 = 1 ∧ y % 2 = 1 ∧ 3 * x + 1 = 2 ^ e * y

def EdgeLaw (m : ℕ → ℚ) : Prop :=
  ∀ x y e, Edge x y e → (4 : ℚ) ^ e * m x = 9 * m y

structure Compressed (m : ℕ → ℚ) : Prop where
  first : ∀ x y, Edge x y 1 → 4 * m x = 9 * m y
  second : ∀ x y, Edge x y 2 → 16 * m x = 9 * m y
  sibling : ∀ x, x % 2 = 1 → 16 * m (4 * x + 1) = m x

theorem compressed_of_edge_law {m : ℕ → ℚ} (h : EdgeLaw m) : Compressed m := by
  constructor
  · intro x y he
    simpa using h x y 1 he
  · intro x y he
    have heq := h x y 2 he
    norm_num at heq
    exact heq
  · intro x hx
    obtain ⟨e, y, hy, hid⟩ := Nat.exists_eq_two_pow_mul_odd
      (show 3 * x + 1 ≠ 0 by omega)
    have hyo := Nat.odd_iff.mp hy
    have h₁ := h x y e ⟨hx, hyo, hid⟩
    have heq : 3 * (4 * x + 1) + 1 = 2 ^ (e + 2) * y := by
      rw [pow_add]
      calc
        3 * (4 * x + 1) + 1 = 4 * (3 * x + 1) := by ring
        _ = _ := by rw [hid]; ring
    have h₂ := h (4 * x + 1) y (e + 2) ⟨by omega, hyo, heq⟩
    rw [pow_add] at h₂
    apply mul_left_cancel₀ (show (4 : ℚ) ^ e ≠ 0 by positivity)
    calc
      4 ^ e * (16 * m (4 * x + 1)) = 4 ^ e * 4 ^ 2 * m (4 * x + 1) := by ring
      _ = 9 * m y := h₂
      _ = 4 ^ e * m x := h₁.symm

theorem edge_law_of_compressed {m : ℕ → ℚ} (h : Compressed m) : EdgeLaw m := by
  intro x y e
  induction e using Nat.strong_induction_on generalizing x y with
  | h e ih =>
    intro he
    obtain ⟨hx, hy, hid⟩ := he
    match e with
    | 0 => simp at hid; omega
    | 1 => simpa using h.first x y ⟨hx, hy, hid⟩
    | 2 => norm_num only [show (4 : ℚ) ^ 2 = 16 by norm_num]
           exact h.second x y ⟨hx, hy, hid⟩
    | k + 3 =>
      have hid₈ : 3 * x + 1 = 8 * (2 ^ k * y) := by
        rw [hid, pow_add]; ring
      let p := 2 * (x / 8) + 1
      have hxp : x = 4 * p + 1 := by dsimp [p]; omega
      have hp : p % 2 = 1 := by dsimp [p]; omega
      have hpword : 3 * p + 1 = 2 ^ (k + 1) * y := by
        rw [show 2 ^ (k + 1) * y = 2 * (2 ^ k * y) by rw [pow_succ]; ring]
        omega
      have low := ih (k + 1) (by omega) p y ⟨hp, hy, hpword⟩
      have hs := h.sibling p hp
      rw [hxp, show k + 3 = (k + 1) + 2 by omega, pow_add]
      calc
        4 ^ (k + 1) * 4 ^ 2 * m (4 * p + 1) =
            4 ^ (k + 1) * (16 * m (4 * p + 1)) := by ring
        _ = 9 * m y := by rw [hs, low]

theorem edge_law_iff_compressed (m : ℕ → ℚ) : EdgeLaw m ↔ Compressed m :=
  ⟨compressed_of_edge_law, edge_law_of_compressed⟩

/-- The multiplier for the height-normalized coefficient increases strictly
on each nonzero positive odd edge. -/
theorem normalized_edge {m : ℕ → ℚ} (h : EdgeLaw m) {x y e : ℕ}
    (he : Edge x y e) :
    (3 * (x : ℚ) + 1) ^ 2 * m x = 9 * ((y : ℚ) ^ 2 * m y) := by
  have hword : 3 * (x : ℚ) + 1 = 2 ^ e * (y : ℚ) := by exact_mod_cast he.2.2
  rw [hword, mul_pow]
  have hpow : ((2 : ℚ) ^ e) ^ 2 = 4 ^ e := by
    rw [← pow_mul, Nat.mul_comm, pow_mul]; norm_num
  rw [hpow]
  calc
    4 ^ e * (y : ℚ) ^ 2 * m x = (y : ℚ) ^ 2 * (4 ^ e * m x) := by ring
    _ = _ := by rw [h x y e he]; ring

theorem normalized_edge_strict {m : ℕ → ℚ} (h : EdgeLaw m) {x y e : ℕ}
    (he : Edge x y e) (hx : 0 < m x) :
    (x : ℚ) ^ 2 * m x < (y : ℚ) ^ 2 * m y := by
  have hid := normalized_edge h he
  have hnonneg : 0 ≤ (x : ℚ) * m x := mul_nonneg (by positivity) hx.le
  nlinarith

end Collatz.Diagonal.OrdinaryHardy
