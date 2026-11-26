import Mathlib.Data.Int.Basic
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# The finite integer at a joint odd date

Clear the source's odd denominator `d`. Each of two prefix identities then has
its own power of three, gap date, odd endpoint and carry. Orient the prefixes
so the second power of three is at least the first. This proves the local
coalescence-or-spacing step, independently of all future behavior.
-/

namespace TriplingCut

private theorem odd_units {a b : ℕ} {x y : ℤ} (hx : Odd x) (hy : Odd y)
    (eqn : 2 ^ a * x = 2 ^ b * y) : a = b ∧ x = y := by
  induction a generalizing b with
  | zero =>
      cases b with
      | zero => simpa using eqn
      | succ b =>
          simp only [pow_zero, one_mul, pow_succ] at eqn
          have even_x : x = 2 * (2 ^ b * y) := by rw [eqn]; ring
          obtain ⟨u, eu⟩ := hx
          omega
  | succ a ih =>
      cases b with
      | zero =>
          simp only [pow_zero, one_mul, pow_succ] at eqn
          have even_y : y = 2 * (2 ^ a * x) := by rw [← eqn]; ring
          obtain ⟨u, eu⟩ := hy
          omega
      | succ b =>
          simp only [pow_succ] at eqn
          have half : 2 ^ a * x = 2 ^ b * y := by linarith only [eqn]
          obtain ⟨h, e⟩ := ih half
          exact ⟨congrArg Nat.succ h, e⟩

private theorem coprime_odd {d : ℤ} (hd : Odd d) : IsCoprime (2 : ℤ) d := by
  obtain ⟨q, eqn⟩ := hd
  exact ⟨-q, 1, by rw [eqn]; ring⟩

/-- The oriented cross-difference vanishes only on a synchronized merger;
otherwise its real absolute value pays the dyadic clock to the next joint date. -/
theorem merge_or_gap {source d f g x y : ℤ} {a b m h : ℕ}
    (hd : Odd d) (hg : ¬ (3 : ℤ) ∣ g) (hx : Odd x) (hy : Odd y)
    (left : 2 ^ a * x = 3 ^ m * source + d * f)
    (right : 2 ^ b * y = 3 ^ (m + h) * source + d * g) :
    (a = b ∧ x = y) ∨ 2 ^ min a b ≤ (3 ^ h * f - g).natAbs := by
  have cross : d * (3 ^ h * f - g) =
      3 ^ h * (2 ^ a * x) - 2 ^ b * y := by
    rw [left, right, pow_add]
    ring
  by_cases zero : 3 ^ h * f - g = 0
  · left
    have same : h = 0 := by
      cases h with
      | zero => rfl
      | succ k =>
          exfalso
          apply hg
          refine ⟨3 ^ k * f, ?_⟩
          rw [pow_succ] at zero
          linarith only [zero]
    rw [same, pow_zero, one_mul] at zero
    rw [same, pow_zero, one_mul, zero, mul_zero] at cross
    exact odd_units hx hy (by linarith only [cross])
  · right
    have ca : (2 : ℤ) ^ min a b ∣ 2 ^ a := pow_dvd_pow _ (min_le_left _ _)
    have cb : (2 : ℤ) ^ min a b ∣ 2 ^ b := pow_dvd_pow _ (min_le_right _ _)
    have div : (2 : ℤ) ^ min a b ∣ d * (3 ^ h * f - g) := by
      rw [cross]
      exact dvd_sub (dvd_mul_of_dvd_right (dvd_mul_of_dvd_left ca x) _) (dvd_mul_of_dvd_left cb y)
    have cut := ((coprime_odd hd).pow_left (m := min a b)).dvd_of_dvd_mul_left div
    have gap := Int.natAbs_le_of_dvd_ne_zero cut zero
    rw [Int.natAbs_pow] at gap
    exact_mod_cast gap

#print axioms odd_units
#print axioms coprime_odd

end TriplingCut

#print axioms TriplingCut.merge_or_gap
