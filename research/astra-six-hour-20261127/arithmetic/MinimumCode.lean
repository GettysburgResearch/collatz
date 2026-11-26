import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

/-! Arithmetic of decoding a rational shortcut cycle from its parity prefix at the minimum.
A trace uses integer numerators over a single positive odd denominator. -/

namespace Collatz.SixHour.MinimumCode

def digit : Bool → ℕ
  | false => 0
  | true => 1

def grade : List Bool → ℕ
  | [] => 0
  | b :: w => digit b + grade w

def carry : List Bool → ℕ
  | [] => 0
  | b :: w => 3 ^ grade w * digit b + 2 * carry w

inductive Trace (d floor : ℕ) : ℕ → List Bool → ℕ → Prop where
  | nil (x : ℕ) (hx : floor ≤ x) : Trace d floor x [] x
  | cons {x y z : ℕ} {b : Bool} {w : List Bool} (hx : floor ≤ x)
      (hstep : 2 * y = 3 ^ digit b * x + d * digit b)
      (htail : Trace d floor y w z) : Trace d floor x (b :: w) z

theorem trace_affine {d floor x z : ℕ} {w : List Bool} (tr : Trace d floor x w z) :
    2 ^ w.length * z = 3 ^ grade w * x + d * carry w := by
  induction tr with
  | nil => simp [grade, carry]
  | @cons x y z b w hx hstep htail ih =>
    simp only [List.length_cons, pow_succ, grade, pow_add, carry]
    calc
      2 ^ w.length * 2 * z = 2 * (2 ^ w.length * z) := by ring
      _ = 2 * (3 ^ grade w * y + d * carry w) := by rw [ih]
      _ = 3 ^ grade w * (2*y) + 2*d*carry w := by ring
      _ = _ := by rw [hstep]; ring

def suffixFits : List Bool → Prop
  | [] => True
  | b :: w => 3 ^ grade (b :: w) ≤ 2 ^ (b :: w).length ∧ suffixFits w

theorem suffix_fits_at_minimum {d floor x : ℕ} {w : List Bool} (hpos : 0 < floor)
    (tr : Trace d floor x w floor) : suffixFits w := by
  induction w generalizing x with
  | nil => trivial
  | cons b w ih =>
    have ha := trace_affine tr
    cases tr with
    | cons hx hs ht =>
      refine ⟨?_, ih ht⟩
      have hb : 3 ^ grade (b :: w) * floor ≤ 2 ^ (b :: w).length * floor :=
        (Nat.mul_le_mul_left _ hx).trans (by omega)
      exact Nat.le_of_mul_le_mul_right hb hpos

theorem minimum_carry_cap {w : List Bool} (hf : suffixFits w) :
    3 * carry w ≤ grade w * 2 ^ w.length := by
  induction w with
  | nil => simp [grade, carry]
  | cons b w ih =>
    obtain ⟨hfull, htail⟩ := hf
    have hb := ih htail
    cases b with
    | false => simpa [carry, digit, grade, pow_succ, Nat.mul_left_comm, Nat.mul_assoc,
                       Nat.mul_comm] using Nat.mul_le_mul_left 2 hb
    | true =>
      simp only [grade, digit, List.length_cons, pow_succ, pow_add] at hfull ⊢
      simp only [carry, digit, mul_one]
      calc
        3 * (3 ^ grade w + 2 * carry w) = 3 * 3 ^ grade w + 2 * (3 * carry w) := by ring
        _ ≤ 2 ^ w.length * 2 + 2 * (grade w * 2 ^ w.length) :=
          Nat.add_le_add hfull (Nat.mul_le_mul_left 2 hb)
        _ = _ := by ring

theorem minimum_numerator_cap {d g m : ℕ} {w : List Bool} (hpos : 0 < m)
    (tr : Trace d m m w m) (hcancel : carry w = g * m) :
    3 * (g * m) ≤ grade w * 2 ^ w.length := by
  rw [← hcancel]
  exact minimum_carry_cap (suffix_fits_at_minimum hpos tr)

theorem same_prefix_same_residue {d f f' x x' z z' : ℕ} {w : List Bool}
    (tr : Trace d f x w z) (tr' : Trace d f' x' w z') :
    x ≡ x' [MOD 2 ^ w.length] := by
  have cop : Nat.Coprime (2 ^ w.length) (3 ^ grade w) :=
    ((by decide : Nat.Coprime 2 3).pow_left _).pow_right _
  apply Nat.ModEq.cancel_left_of_coprime cop
  apply Nat.ModEq.add_right_cancel' (d * carry w)
  rw [← trace_affine tr, ← trace_affine tr']
  simp [Nat.ModEq]

theorem decode_bounded_prefix {d f f' x x' z z' : ℕ} {w : List Bool}
    (tr : Trace d f x w z) (tr' : Trace d f' x' w z')
    (hx : x < 2 ^ w.length) (hx' : x' < 2 ^ w.length) : x = x' :=
  (same_prefix_same_residue tr tr').eq_of_lt_of_lt hx hx'

end Collatz.SixHour.MinimumCode
