import AffineReachability
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-! Finite binary likelihood and coefficient identities for aligned shortcuts.
The polynomials specialize to any field, including the dyadic local field. -/

namespace Collatz.BinaryAffineLikelihood

open Collatz.AffineReachability

def ones : List Bool → ℕ
  | [] => 0
  | b :: w => ones w + (if b then 1 else 0)

/-- The even-letter weight is `q`, the odd-letter weight is `q * odds`. -/
def weight {K : Type*} [CommMonoid K] (q odds : K) : List Bool → K
  | [] => 1
  | b :: w => (if b then q * odds else q) * weight q odds w

theorem weight_eq {K : Type*} [CommMonoid K] (q odds : K) (w : List Bool) :
    weight q odds w = q ^ w.length * odds ^ ones w := by
  induction w with
  | nil => simp [weight, ones]
  | cons b w ih =>
    cases b <;> simp [weight, ones, ih, pow_succ] <;> ac_rfl

theorem scale_eq (w : List Bool) : scale w = 3 ^ ones w := by
  induction w with
  | nil => rfl
  | cons b w ih => cases b <;> simp [scale, ones, ih, pow_succ]

/-- The cleared likelihood ratio when the second word has `r` extra ticks
and the first word has `k` extra odd departures. -/
theorem aligned_weight {K : Type*} [CommMonoid K] (q odds : K)
    (u v : List Bool) (r k : ℕ) (hlen : v.length = u.length+r)
    (hcount : ones u = ones v+k) :
    weight q odds v * odds ^ k = q ^ r * weight q odds u := by
  simp only [weight_eq, hlen, hcount, pow_add]
  ac_rfl

/-- A rational or local-field affine pair `x ↦ a*x+b` with aligned
endpoints at two distinct inputs has both forced coefficients. The
premises use the ordinary shortcut's integer word offsets. -/
theorem aligned_coefficients {K : Type*} [Field K] (u v : List Bool)
    (a b c x y : K) (hne : x ≠ y)
    (hx : (scale v : K) * (a*x+b) + (offset v : K) =
      c*((scale u : K)*x+(offset u : K)))
    (hy : (scale v : K) * (a*y+b) + (offset v : K) =
      c*((scale u : K)*y+(offset u : K))) :
    (3:K)^(ones v) * a = c*(3:K)^(ones u) ∧
      (3:K)^(ones v) * b = c*(offset u:K)-(offset v:K) := by
  have hprod : ((scale v:K)*a-c*(scale u:K))*(x-y) = 0 := by
    linear_combination hx - hy
  have hs : (scale v:K)*a = c*(scale u:K) :=
    sub_eq_zero.mp ((mul_eq_zero.mp hprod).resolve_right (sub_ne_zero.mpr hne))
  have hb : (scale v:K)*b = c*(offset u:K)-(offset v:K) := by
    linear_combination hx - x*hs
  simpa [scale_eq] using And.intro hs hb

end Collatz.BinaryAffineLikelihood
