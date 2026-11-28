import MinimumWindow
import Mathlib.Algebra.GroupWithZero.Divisibility

/-! An unrestricted rational affine word with an integral endpoint must
follow the genuine shortcut parity choices. The proof is phrased in
cleared integer numerators, so no rational rounding is involved. -/

namespace Collatz.AffineReachability

open Collatz.MinimumWindow

def scale : List Bool → ℕ
  | [] => 1
  | b :: w => scale w * (if b then 3 else 1)

def offset : List Bool → ℕ
  | [] => 0
  | b :: w => scale w * (if b then 1 else 0) + 2 * offset w

def numerator (w : List Bool) (n : ℕ) : ℕ := scale w * n + offset w

def legal : List Bool → ℕ → Prop
  | [], _ => True
  | b :: w, n => (if b then n % 2 = 1 else n % 2 = 0) ∧ legal w (step n)

theorem scale_odd (w : List Bool) : scale w % 2 = 1 := by
  induction w with
  | nil => rfl
  | cons b w ih =>
    cases b <;> simp [scale, Nat.mul_mod, ih]

theorem numerator_cons (b : Bool) (w : List Bool) (n : ℕ) :
    numerator (b :: w) n =
      scale w * (if b then 3*n+1 else n) + 2 * offset w := by
  cases b <;> simp [numerator, scale, offset]
  ring

theorem numerator_cons_even (b : Bool) (w : List Bool) (n : ℕ)
    (h : 2 ∣ numerator (b :: w) n) :
    if b then n % 2 = 1 else n % 2 = 0 := by
  have hm := Nat.mod_eq_zero_of_dvd h
  rw [numerator_cons] at hm
  cases b
  · simpa [Nat.add_mod, Nat.mul_mod, scale_odd] using hm
  · change n % 2 = 1
    simp [Nat.add_mod, Nat.mul_mod, scale_odd] at hm
    omega

theorem numerator_step (b : Bool) (w : List Bool) (n : ℕ)
    (h : if b then n % 2 = 1 else n % 2 = 0) :
    numerator (b :: w) n = 2 * numerator w (step n) := by
  have hb : (if b then 3*n+1 else n) = 2 * step n := by
    cases b
    · simp only [Bool.false_eq_true, ite_false] at h ⊢
      simp only [step, h, ite_true]
      omega
    · simp only [ite_true] at h ⊢
      have he : ¬ n % 2 = 0 := by omega
      simp only [step, he, ite_false]
      omega
  rw [numerator_cons, hb]
  simp only [numerator]
  ring

theorem integral_implies_legal (w : List Bool) (n : ℕ)
    (h : 2^w.length ∣ numerator w n) : legal w n := by
  induction w generalizing n with
  | nil => trivial
  | cons b w ih =>
    have htwo : 2 ∣ numerator (b :: w) n := by
      apply dvd_trans (show 2 ∣ 2^(b :: w).length from ?_) h
      simp only [List.length_cons, pow_succ]
      exact dvd_mul_left 2 (2^w.length)
    have hb := numerator_cons_even b w n htwo
    have hn := numerator_step b w n hb
    have ht : 2^w.length ∣ numerator w (step n) := by
      rw [List.length_cons, pow_succ, hn] at h
      have hh : 2 * 2^w.length ∣ 2 * numerator w (step n) := by
        simpa only [Nat.mul_comm] using h
      exact (mul_dvd_mul_iff_left (by decide : (2 : ℕ) ≠ 0)).mp hh
    exact ⟨hb, ih (step n) ht⟩

theorem legal_numerator (w : List Bool) (n : ℕ) (h : legal w n) :
    numerator w n = 2^w.length * orbit w.length n := by
  induction w generalizing n with
  | nil => simp [numerator, scale, offset, orbit]
  | cons b w ih =>
    obtain ⟨hb, ht⟩ := h
    rw [numerator_step b w n hb, ih (step n) ht]
    simp only [List.length_cons, orbit, pow_succ]
    ring

theorem integral_iff_legal (w : List Bool) (n : ℕ) :
    2^w.length ∣ numerator w n ↔ legal w n := by
  constructor
  · exact integral_implies_legal w n
  · intro h
    rw [legal_numerator w n h]
    exact dvd_mul_right _ _

/-- Specifying an integer endpoint of an unrestricted affine word already
forces the true orbit and every intervening parity choice. -/
theorem integer_endpoint (w : List Bool) (n m : ℕ)
    (h : numerator w n = 2^w.length * m) :
    legal w n ∧ orbit w.length n = m := by
  have hl := integral_implies_legal w n (by rw [h]; exact dvd_mul_right _ _)
  refine ⟨hl, ?_⟩
  have he := legal_numerator w n hl
  rw [h] at he
  exact (Nat.eq_of_mul_eq_mul_left (by positivity : 0 < 2^w.length) he).symm

#print axioms integral_iff_legal
#print axioms integer_endpoint

end Collatz.AffineReachability
