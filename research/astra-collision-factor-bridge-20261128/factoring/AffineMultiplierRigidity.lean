import AffineOrbit
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.LinearCombination

/-!
A finite-cell obstruction for transferring arithmetic multiplier samplers to
genuine Collatz mergers. No assertion that the two paths fail to meet at
unbounded times is made.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.FactoringBridge
open Collatz.PoweredAffine

private theorem cross_word_identity (w v : List Bool) (x a b : ℚ)
    (h : evalWord w x = evalWord v (a * x + b)) :
    (2 : ℚ) ^ v.length * ((3 : ℚ) ^ ones w * x + numerator w) =
      (2 : ℚ) ^ w.length *
        ((3 : ℚ) ^ ones v * (a * x + b) + numerator v) := by
  calc
    (2 : ℚ) ^ v.length * ((3 : ℚ) ^ ones w * x + numerator w) =
        (2 : ℚ) ^ v.length * ((2 : ℚ) ^ w.length * evalWord w x) := by
          rw [word_affine]
    _ = (2 : ℚ) ^ w.length *
        ((2 : ℚ) ^ v.length * evalWord v (a * x + b)) := by rw [h]; ring
    _ = (2 : ℚ) ^ w.length *
        ((3 : ℚ) ^ ones v * (a * x + b) + numerator v) := by
          rw [word_affine]

/-- Two distinct points in one pair of affine word charts force the slope. -/
theorem two_point_word_slope (w v : List Bool) (x y a b : ℚ) (hxy : x ≠ y)
    (hx : evalWord w x = evalWord v (a * x + b))
    (hy : evalWord w y = evalWord v (a * y + b)) :
    (2 : ℚ) ^ v.length * (3 : ℚ) ^ ones w =
      a * (2 : ℚ) ^ w.length * (3 : ℚ) ^ ones v := by
  have h₁ := cross_word_identity w v x a b hx
  have h₂ := cross_word_identity w v y a b hy
  have hprod :
      ((2 : ℚ) ^ v.length * (3 : ℚ) ^ ones w -
        a * (2 : ℚ) ^ w.length * (3 : ℚ) ^ ones v) * (x - y) = 0 := by
    linear_combination h₁ - h₂
  exact sub_eq_zero.mp ((mul_eq_zero.mp hprod).resolve_right (sub_ne_zero.mpr hxy))

/-- The slope identity is forced by actual ordinary integer replays. -/
theorem actual_two_point_slope (w v : List Bool) (n m a b : ℕ) (hnm : n ≠ m)
    (hn : Realizes n w) (hm : Realizes m w)
    (han : Realizes (a * n + b) v) (ham : Realizes (a * m + b) v)
    (hen : orbit n w.length = orbit (a * n + b) v.length)
    (hem : orbit m w.length = orbit (a * m + b) v.length) :
    2 ^ v.length * 3 ^ ones w = a * 2 ^ w.length * 3 ^ ones v := by
  have hneq : (n : ℚ) ≠ (m : ℚ) := by exact_mod_cast hnm
  have he₁ : evalWord w (n : ℚ) = evalWord v ((a : ℚ) * n + b) := by
    rw [evalWord_actual hn]
    have ha := evalWord_actual han
    push_cast at ha
    rw [ha, hen]
  have he₂ : evalWord w (m : ℚ) = evalWord v ((a : ℚ) * m + b) := by
    rw [evalWord_actual hm]
    have ha := evalWord_actual ham
    push_cast at ha
    rw [ha, hem]
  have h := two_point_word_slope w v n m a b hneq he₁ he₂
  exact_mod_cast h

/-- A prime other than two and three in the multiplier excludes a two-point cell. -/
theorem prime_multiplier_cell_unique (w v : List Bool) (n m a b p : ℕ)
    (hp : p.Prime) (hp2 : p ≠ 2) (hp3 : p ≠ 3) (hpa : p ∣ a)
    (hn : Realizes n w) (hm : Realizes m w)
    (han : Realizes (a * n + b) v) (ham : Realizes (a * m + b) v)
    (hen : orbit n w.length = orbit (a * n + b) v.length)
    (hem : orbit m w.length = orbit (a * m + b) v.length) :
    n = m := by
  by_contra hnm
  have h := actual_two_point_slope w v n m a b hnm hn hm han ham hen hem
  have hd : p ∣ 2 ^ v.length * 3 ^ ones w := by
    rw [h]
    exact dvd_mul_of_dvd_left (dvd_mul_of_dvd_left hpa _) _
  rcases hp.dvd_mul.mp hd with h₂ | h₃
  · have := hp.dvd_of_dvd_pow h₂
    exact hp2 ((Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).mp this)
  · have := hp.dvd_of_dvd_pow h₃
    exact hp3 ((Nat.prime_dvd_prime_iff_eq hp (by decide : Nat.Prime 3)).mp this)

end Collatz.FactoringBridge
