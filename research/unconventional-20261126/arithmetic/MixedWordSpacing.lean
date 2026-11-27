import Mathlib.Data.Int.Basic
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Ordinary spacing of cuts in two copies of one Syracuse word

The relation `Follows` contains the affine equations over the integers, with an
arbitrary additive parameter. Terminal parity is assumed explicitly wherever
it supplies the last factor of two. The proofs use neither an upper size bound
nor eventual termination.
-/

namespace MixedWordSpacing

/-- The unrounded affine equations for the stated list of gap exponents. -/
inductive Follows (d : ℤ) : ℤ → List ℕ → ℤ → Prop where
  | nil (x : ℤ) : Follows d x [] x
  | step {x y z : ℤ} {e : ℕ} {w : List ℕ}
      (eqn : 2 ^ e * y = 3 * x + d) (tail : Follows d y w z) :
      Follows d x (e :: w) z

/-- The additive offsets cancel between two physical copies of the same word. -/
theorem same_word {d x y z u : ℤ} {w : List ℕ}
    (hx : Follows d x w z) (hy : Follows d y w u) :
    3 ^ w.length * (x - y) = 2 ^ w.sum * (z - u) := by
  induction hx generalizing y u with
  | nil x =>
      cases hy
      simp
  | @step x x' z e w ex _ ih =>
      cases hy with
      | @step _ y' _ _ _ ey tail =>
          have head : 3 * (x - y) = 2 ^ e * (x' - y') := by
            linarith [ex, ey]
          have rest := ih tail
          simp only [List.length_cons, List.sum_cons, pow_succ, pow_add]
          calc
            3 ^ w.length * 3 * (x - y) = 3 ^ w.length * (3 * (x - y)) := by ring
            _ = 2 ^ e * (3 ^ w.length * (x' - y')) := by rw [head]; ring
            _ = 2 ^ e * 2 ^ w.sum * (z - u) := by rw [rest]; ring

private theorem coprime_two_three : IsCoprime (2 : ℤ) 3 :=
  ⟨-1, 1, by norm_num⟩

/-- Two odd terminals force one more dyadic bit at the beginning of the word. -/
theorem start_divisibility {d x y z u : ℤ} {w : List ℕ}
    (hx : Follows d x w z) (hy : Follows d y w u) (hz : Odd z) (hu : Odd u) :
    (2 : ℤ) ^ (w.sum + 1) ∣ x - y := by
  apply (coprime_two_three.pow (m := w.sum + 1) (n := w.length)).dvd_of_dvd_mul_left
  rw [same_word hx hy]
  obtain ⟨a, ha⟩ := hz
  obtain ⟨b, hb⟩ := hu
  refine ⟨a-b, ?_⟩
  rw [ha, hb, pow_succ]
  ring

/-- The reversed constraint is a ternary divisibility at the end of the word. -/
theorem end_divisibility {d x y z u : ℤ} {w : List ℕ}
    (hx : Follows d x w z) (hy : Follows d y w u) :
    (3 : ℤ) ^ w.length ∣ z - u := by
  apply (coprime_two_three.symm.pow (m := w.length) (n := w.sum)).dvd_of_dvd_mul_left
  rw [← same_word hx hy]
  exact dvd_mul_right _ _

/-- Two copies of one bilateral word impose both local obligations at the cut. -/
theorem cut_divisibility {d a b x y z u : ℤ} {past future : List ℕ}
    (ha : Follows d a past x) (hb : Follows d b past y)
    (hx : Follows d x future z) (hy : Follows d y future u) (hz : Odd z) (hu : Odd u) :
    (3 : ℤ) ^ past.length * 2 ^ (future.sum + 1) ∣ x - y :=
  (coprime_two_three.symm.pow).mul_dvd (end_divisibility ha hb) (start_divisibility hx hy hz hu)

/-- At distinct ordinary cuts the congruence gives an Archimedean gap. -/
theorem cut_spacing {d a b x y z u : ℤ} {past future : List ℕ}
    (ha : Follows d a past x) (hb : Follows d b past y)
    (hx : Follows d x future z) (hy : Follows d y future u) (hz : Odd z) (hu : Odd u)
    (hne : x ≠ y) :
    3 ^ past.length * 2 ^ (future.sum + 1) ≤ (x - y).natAbs := by
  have h := Int.natAbs_le_of_dvd_ne_zero (cut_divisibility ha hb hx hy hz hu) (sub_ne_zero.mpr hne)
  rw [Int.natAbs_mul, Int.natAbs_pow, Int.natAbs_pow] at h
  exact_mod_cast h

#print axioms coprime_two_three

end MixedWordSpacing

#print axioms MixedWordSpacing.same_word
#print axioms MixedWordSpacing.start_divisibility
#print axioms MixedWordSpacing.end_divisibility
#print axioms MixedWordSpacing.cut_divisibility
#print axioms MixedWordSpacing.cut_spacing
