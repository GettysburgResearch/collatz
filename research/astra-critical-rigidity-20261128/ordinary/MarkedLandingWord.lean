import TernaryLanding

/-! A closed positive-height word is physical precisely when its displayed
carry is integral. For a word ending in an odd departure the terminal mark
supplies the entire ternary-unit obstruction. -/

namespace Collatz.MarkedLandingWord
open Collatz.PoweredAffine Collatz.TernaryLanding

/-- Every requested departure occurs at positive remaining ternary height. -/
def Allowed (h : ℕ) : List Bool → Prop
  | [] => True
  | b :: w => 0 < (if b then 1 else 0) + ones w + h ∧ Allowed h w

private theorem three_power_parity (h : ℕ) : 3 ^ h % 2 = 1 := by
  induction h with
  | zero => decide
  | succ h ih => rw [pow_succ, Nat.mul_mod, ih]

/-- Sufficiency of the exact carry for physical parity, without assuming a run. -/
theorem physical_of_carry (w : List Bool) (h m N : ℕ) (ha : Allowed h w)
    (eq : 2 ^ w.length * N = m + 3 ^ h * numerator w) :
    Run 1 (ones w + h) m w h N := by
  induction w generalizing m with
  | nil =>
    have hm : N = m := by simpa [numerator] using eq
    subst m
    simpa [ones] using (Run.nil (q := 1) h N)
  | cons b w ih =>
    obtain ⟨hp, ht⟩ := ha
    cases b with
    | false =>
      have he : 2 * (2 ^ w.length * N) = m + 2 * (3 ^ h * numerator w) := by
        simpa only [List.length_cons, pow_succ, numerator, Bool.false_eq_true,
          ↓reduceIte, mul_zero, zero_mul, zero_add, mul_assoc, mul_left_comm, mul_comm] using eq
      have ht' := ih (m / 2) ht (by omega)
      simp only [ones, Bool.false_eq_true, ↓reduceIte, zero_add]
      cases hr : ones w + h with
      | zero => simp [hr] at hp
      | succ j =>
        rw [hr] at ht'
        exact Run.even (by omega) ht'
    | true =>
      have he : 2 * (2 ^ w.length * N) =
          m + 3 ^ (ones w + h) + 2 * (3 ^ h * numerator w) := by
        simp only [List.length_cons, pow_succ, numerator, ↓reduceIte, mul_one] at eq
        rw [pow_add]
        calc
          _ = 2 ^ w.length * 2 * N := by ring
          _ = _ := eq
          _ = _ := by ring
      have hpar := three_power_parity (ones w + h)
      have ht' := ih ((m + 3 ^ (ones w + h)) / 2) ht (by omega)
      have hc : ones (true :: w) + h = (ones w + h) + 1 := by simp [ones]; omega
      rw [hc]
      exact Run.odd (by omega) (by simpa using ht')

private theorem count_last (w : List Bool) : ones (w ++ [true]) = ones w + 1 := by
  induction w with
  | nil => decide
  | cons b w ih => simp only [List.cons_append, ones, ih]; omega

private theorem allowed_last (w : List Bool) : Allowed 0 (w ++ [true]) := by
  induction w with
  | nil => simp [Allowed, ones]
  | cons b w ih =>
    simp only [List.cons_append, Allowed, count_last, Nat.add_zero]
    exact ⟨by omega, ih⟩

/-- Exact additive carry of appending the final odd departure. -/
theorem last_odd_carry (w : List Bool) :
    numerator (w ++ [true]) = 3 * numerator w + 2 ^ w.length := by
  induction w with
  | nil => decide
  | cons b w ih =>
    cases b <;> simp only [List.cons_append, numerator, ih, count_last,
      List.length_cons, pow_succ, Bool.false_eq_true, ↓reduceIte, mul_zero,
      zero_add, mul_one] <;> ring

private theorem two_unit (k : ℕ) : 2 ^ k % 3 = 1 ∨ 2 ^ k % 3 = 2 := by
  induction k with
  | zero => decide
  | succ k ih =>
    rcases ih with hk | hk <;> rw [pow_succ, Nat.mul_mod, hk] <;> decide

private theorem marked_unit {w : List Bool} {m N : ℕ}
    (eq : 2 ^ (w ++ [true]).length * N = m + numerator (w ++ [true])) :
    (m % 3 ≠ 0 ↔ N % 3 ≠ 2) := by
  rw [last_odd_carry] at eq
  simp only [List.length_append, List.length_cons, List.length_nil, zero_add,
    pow_succ] at eq
  have em := congrArg (fun k : ℕ => k % 3) eq
  have hm : m % 3 < 3 := Nat.mod_lt _ (by decide)
  have hn : N % 3 < 3 := Nat.mod_lt _ (by decide)
  change (2 ^ w.length * 2 * N) % 3 = (m + (3 * numerator w + 2 ^ w.length)) % 3 at em
  rw [Nat.mul_mod, Nat.mul_mod (2 ^ w.length) 2, Nat.add_mod,
    Nat.add_mod (3 * numerator w), Nat.mul_mod 3 (numerator w)] at em
  rcases two_unit w.length with hk | hk <;>
    rcases (show N % 3 = 0 ∨ N % 3 = 1 ∨ N % 3 = 2 by omega) with ha | ha | ha <;>
    rw [hk, ha] at em <;> norm_num at em <;> omega

/-- There is a positive reduced first preimage of the prescribed last-odd
word exactly at eligible marks above its affine zero-source endpoint. -/
theorem first_mark_iff (w : List Bool) (N : ℕ) :
    (∃ m : ℕ, 0 < m ∧ m % 3 ≠ 0 ∧
       Run 1 (ones (w ++ [true])) m (w ++ [true]) 0 N) ↔
    (N % 3 ≠ 2 ∧ numerator (w ++ [true]) < 2 ^ (w ++ [true]).length * N) := by
  constructor
  · rintro ⟨m, hm, hu, run⟩
    have hc := prefix_carry (by decide : 1 % 2 = 1) run
    simp only [pow_zero, mul_one, one_mul] at hc
    exact ⟨(marked_unit hc).mp hu, by omega⟩
  · rintro ⟨he, hs⟩
    let m := 2 ^ (w ++ [true]).length * N - numerator (w ++ [true])
    have hc : 2 ^ (w ++ [true]).length * N = m + numerator (w ++ [true]) := by
      dsimp [m]; omega
    refine ⟨m, by dsimp [m]; omega, (marked_unit hc).mpr he, ?_⟩
    simpa using physical_of_carry (w ++ [true]) 0 m N (allowed_last w) (by simpa using hc)

end Collatz.MarkedLandingWord
