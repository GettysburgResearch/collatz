import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

import Mathlib.Data.Int.ModEq
import Mathlib.Data.Int.Basic

namespace Collatz.CycleNorm

/-- Weighted numerator of the shifted eight-gap family, with common gap
increment k encoded by t = 2^k. -/
def numerator (x t : ℤ) : ℤ :=
  x^7 + 2*t*x^6 + 4*t^2*x^5 + 32*t^3*x^4 + 128*t^4*x^3 +
    2048*t^5*x^2 + 32768*t^6*x + 262144*t^7

def commonFactor (x t : ℤ) : ℤ := x^2 + 8*t*x + 32*t^2

theorem numerator_factor (x t : ℤ) :
    numerator x t = commonFactor x t *
      (x^5 - 6*t*x^4 + 20*t^2*x^3 + 64*t^3*x^2 - 1024*t^4*x + 8192*t^5) := by
  unfold numerator commonFactor
  ring

theorem top_factor (x t : ℤ) :
    x^4 + 1024*t^4 = commonFactor x t * (x^2 - 8*t*x + 32*t^2) := by
  unfold commonFactor
  ring

theorem reduced_closure : (389545 : ℤ) * 16031 = 1042015 * 5993 := by
  norm_num

#print axioms numerator_factor
#print axioms top_factor
#print axioms reduced_closure
/-- Remaining numerator after the structural factor at x = 3. -/
def residual (t : ℤ) : ℤ :=
  243 - 486*t + 540*t^2 + 576*t^3 - 3072*t^4 + 8192*t^5

theorem bezout_minus (t : ℤ) :
    (-65536*t^4 + 55296*t^3 - 34560*t^2 + 13392*t - 3807) * (32*t^2-9)
      + (256*t - 120) * residual t = 5103 := by
  unfold residual
  ring

theorem bezout_plus (t : ℤ) :
    (2048*t^3 - 768*t^2 - 432*t + 351) * (32*t^2+9) - 8 * residual t = 1215 := by
  unfold residual
  ring

theorem bezout_quadratic (t : ℤ) :
    (-16384*t^4 + 1152*t^2 + 216*t + 1215) * (32*t^2-24*t+9)
      + (64*t-24) * residual t = 5103 := by
  unfold residual
  ring

#print axioms bezout_minus
#print axioms bezout_plus
#print axioms bezout_quadratic


/-- Every common divisor of two evaluated factors divides their certificate. -/
theorem gcd_dvd_certificate {x y a b K : Int} (h : a*x + b*y = K) :
    (Int.gcd x y : Int) ∣ K := by
  rw [← h]
  exact Int.dvd_add (Int.dvd_mul_of_dvd_right (Int.gcd_dvd_left x y))
    (Int.dvd_mul_of_dvd_right (Int.gcd_dvd_right x y))

/-- A certificate coprime to the evaluated numerator excludes cancellation. -/
theorem coprime_of_certificate {x y a b K : Int} (h : a*x + b*y = K)
    (hy : Int.gcd y K = 1) : Int.gcd x y = 1 := by
  apply Nat.dvd_one.mp
  rw [← hy]
  exact Int.dvd_gcd (Int.gcd_dvd_right x y) (gcd_dvd_certificate h)

#print axioms gcd_dvd_certificate
#print axioms coprime_of_certificate
private theorem residual_congr {u v : ℤ} (h : u ≡ v [ZMOD 105]) :
    residual u ≡ residual v [ZMOD 105] := by
  unfold residual
  have h1 := (Int.ModEq.refl (243:ℤ)).sub ((Int.ModEq.refl (486:ℤ)).mul h)
  have h2 := h1.add ((Int.ModEq.refl (540:ℤ)).mul (h.pow 2))
  have h3 := h2.add ((Int.ModEq.refl (576:ℤ)).mul (h.pow 3))
  have h4 := h3.sub ((Int.ModEq.refl (3072:ℤ)).mul (h.pow 4))
  exact h4.add ((Int.ModEq.refl (8192:ℤ)).mul (h.pow 5))

theorem residual_coprime_105 (k : ℕ) : Int.gcd (residual (2^k)) 105 = 1 := by
  have h12 : (2:ℤ)^12 ≡ 1 [ZMOD 105] := by decide
  have ht : (2:ℤ)^k ≡ 2^(k%12) [ZMOD 105] := by
    calc (2:ℤ)^k = 2^(12*(k/12) + k%12) := by rw [Nat.div_add_mod]
         _ = ((2:ℤ)^12)^(k/12) * 2^(k%12) := by rw [pow_add, pow_mul]
         _ ≡ (1:ℤ)^(k/12) * 2^(k%12) [ZMOD 105] :=
           (h12.pow (k/12)).mul Int.ModEq.rfl
         _ = 2^(k%12) := by simp
  have finite : ∀ j : Fin 12, Int.gcd (residual (2^(j:ℕ))) 105 = 1 := by decide
  calc Int.gcd (residual (2^k)) 105 = Int.gcd (residual (2^k) % 105) 105 :=
          (Int.gcd_emod _ _).symm
       _ = Int.gcd (residual (2^(k%12)) % 105) 105 := by rw [(residual_congr ht).eq]
       _ = Int.gcd (residual (2^(k%12))) 105 := Int.gcd_emod _ _
       _ = 1 := finite ⟨k%12, Nat.mod_lt _ (by decide)⟩

theorem residual_full_coprime (k : ℕ) :
    let t := (2:ℤ)^k
    Int.gcd ((32*t^2-9)*(32*t^2+9)*(32*t^2-24*t+9)) (residual t) = 1 := by
  let t := (2:ℤ)^k
  change Int.gcd ((32*t^2-9)*(32*t^2+9)*(32*t^2-24*t+9)) (residual t) = 1
  have hc : (residual t).natAbs.Coprime 105 := residual_coprime_105 k
  have h1 : Int.gcd (residual t) 5103 = 1 :=
    Nat.Coprime.coprime_dvd_right (by decide : 5103 ∣ 105^6) (hc.pow_right 6)
  have h2 : Int.gcd (residual t) 1215 = 1 :=
    Nat.Coprime.coprime_dvd_right (by decide : 1215 ∣ 105^6) (hc.pow_right 6)
  have hm := coprime_of_certificate (bezout_minus t) h1
  have hp' : (2048*t^3 - 768*t^2 - 432*t + 351) * (32*t^2+9)
      + (-8) * residual t = 1215 := by simpa only [neg_mul, sub_eq_add_neg] using bezout_plus t
  have hp := coprime_of_certificate hp' h2
  have hq := coprime_of_certificate (bezout_quadratic t) h1
  change Nat.Coprime _ _
  rw [Int.natAbs_mul, Int.natAbs_mul]
  exact Nat.Coprime.mul_left (Nat.Coprime.mul_left hm hp) hq

#print axioms residual_coprime_105
#print axioms residual_full_coprime
end Collatz.CycleNorm

