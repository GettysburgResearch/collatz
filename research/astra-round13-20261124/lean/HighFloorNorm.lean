import Mathlib.Tactic.Ring

import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Algebra.Ring.Int.Parity

namespace Collatz.HighFloorNorm

variable {R : Type*} [CommRing R]

def weightedSeed (y s : R) : R :=
  y^7 + 2*s*y^6 + 4*s^2*y^5 + 8*s^3*y^4 + 32*s^4*y^3 +
    64*s^5*y^2 + 256*s^6*y + 1024*s^7

def factor (y s : R) : R := y^2 + 4*s*y + 8*s^2

theorem interleaved_carry_factor (x s P : R) (n : ℕ) :
    P * weightedSeed (x^n) s = factor (x^n) s *
      (P * ((x^n)^5 - 2*s*(x^n)^4 + 4*s^2*(x^n)^3 + 8*s^3*(x^n)^2
             - 32*s^4*(x^n) + 128*s^5)) := by
  unfold weightedSeed factor
  ring

theorem interleaved_top_factor (x s : R) (n : ℕ) :
    x^(n*4) + 64*s^4 = factor (x^n) s * ((x^n)^2 - 4*s*x^n + 8*s^2) := by
  rw [pow_mul]
  unfold factor
  ring

#print axioms interleaved_carry_factor
#print axioms interleaved_top_factor
def residual (y : ℤ) : ℤ := y^5 - 2*y^4 + 4*y^3 + 8*y^2 - 32*y + 128

theorem exceptional_minus_bezout (y : ℤ) :
    (y^4-3*y^3+14*y^2-20*y+72)*(8-y^2)+(y-1)*residual y=448 := by
  unfold residual
  ring

theorem exceptional_plus_bezout (y : ℤ) :
    (y^3-2*y^2-4*y+24)*(8+y^2)-residual y=64 := by
  unfold residual
  ring

theorem exceptional_quadratic_bezout (y : ℤ) :
    (48-y^4)*(y^2-4*y+8)+(y-2)*residual y=128 := by
  unfold residual
  ring

theorem full_clock_factor (z s : ℤ) :
    4096*s^8-z^8 = factor z s * ((8*s^2-z^2)*(8*s^2+z^2)*(z^2-4*z*s+8*s^2)) := by
  unfold factor
  ring

#print axioms exceptional_minus_bezout
#print axioms exceptional_plus_bezout
#print axioms exceptional_quadratic_bezout
#print axioms full_clock_factor
def residualNumerator (z s : ℤ) : ℤ :=
  z^5-2*s*z^4+4*s^2*z^3+8*s^3*z^2-32*s^4*z+128*s^5

def residualDenominator (z s : ℤ) : ℤ :=
  (8*s^2-z^2)*(8*s^2+z^2)*(z^2-4*z*s+8*s^2)

theorem full_residual_bezout (z s : ℤ) :
    (-z^4-4*s*z^3+48*s^3*z+208*s^4) * residualDenominator z s +
    (-z^5-2*s*z^4+8*s^2*z^3+48*s^3*z^2+128*s^4*z-384*s^5) *
      residualNumerator z s = 57344*s^10 := by
  unfold residualDenominator residualNumerator
  ring

theorem full_residual_gcd_dvd_seven (z : ℤ) (S : ℕ) (hz : Odd z) :
    Int.gcd (residualDenominator z (2^S)) (residualNumerator z (2^S)) ∣ 7 := by
  let s := (2:ℤ)^S
  let V := residualDenominator z s
  let B := residualNumerator z s
  let g := Int.gcd V B
  have ho : Odd V := by
    have hne := Int.not_even_iff_odd.mpr hz
    change Odd ((8*s^2-z^2)*(8*s^2+z^2)*(z^2-4*z*s+8*s^2))
    simp +decide [Int.odd_mul, parity_simps, hz, hne]
  have hg : g.Coprime 2 :=
    Nat.Coprime.coprime_dvd_left (Int.gcd_dvd_natAbs_left V B) ho.natAbs.coprime_two_right
  have h : (g:ℤ) ∣ 57344*s^10 := by
    rw [← full_residual_bezout z s]
    exact Int.dvd_add (Int.dvd_mul_of_dvd_right (Int.gcd_dvd_left V B))
      (Int.dvd_mul_of_dvd_right (Int.gcd_dvd_right V B))
  have he : (57344:ℤ)*s^10 = (7:ℤ)*2^(13+S*10) := by
    dsimp [s]
    rw [pow_add, pow_mul]
    ring
  rw [he] at h
  have hnat : g ∣ 7*2^(13+S*10) := by exact_mod_cast h
  exact (hg.pow_right (13+S*10)).dvd_of_dvd_mul_right hnat

/-- Exact transfer through the arbitrary prefix multiplier. -/
theorem full_prefix_gcd_dvd {V B P : ℕ} (h : Nat.gcd V B ∣ 7) :
    Nat.gcd V (P*B) ∣ P*7 :=
  Nat.dvd_trans (Nat.gcd_mul_right_dvd_mul_gcd V P B)
    (Nat.mul_dvd_mul (Nat.gcd_dvd_right V P) h)

/-- Last integer comparison for the complete reduced denominator. -/
theorem denominator_bound (z s P g d : ℤ) (hz : 0 < z) (hs : 0 < s)
    (hg : 0 < g) (hP : 2*P < s*z)
    (hclock : 1 ≤ 8*s^2-z^2) (hcancel : g ≤ 7*P)
    (hred : g*d = residualDenominator z s) : 4*z^2 < 7*d := by
  have hplus : 4*z*s ≤ 8*s^2+z^2 := by nlinarith [sq_nonneg (z-2*s), sq_nonneg s]
  have hquad : z^2 ≤ 2*(z^2-4*z*s+8*s^2) := by nlinarith [sq_nonneg (z-4*s)]
  have hp0 : 0 ≤ 4*z*s := by positivity
  have hq0 : 0 ≤ z^2-4*z*s+8*s^2 := by nlinarith [sq_nonneg z]
  have hprod := mul_le_mul hplus hquad (sq_nonneg z) (by linarith : 0 ≤ 8*s^2+z^2)
  have hres := mul_le_mul_of_nonneg_right hclock
    (mul_nonneg (by linarith : 0 ≤ 8*s^2+z^2) hq0)
  unfold residualDenominator at hred
  have hgd : 4*z^3*s ≤ 2*g*d := by nlinarith only [hprod, hres, hred]
  have hsmall : 2*g < 7*(s*z) := by linarith
  by_contra! hbad
  have hbad' := mul_le_mul_of_nonneg_left hbad (le_of_lt hg)
  have hstrict := mul_lt_mul_of_pos_right hsmall (show 0 < 4*z^2 by positivity)
  nlinarith only [hgd, hbad', hstrict]

#print axioms full_residual_bezout
#print axioms full_residual_gcd_dvd_seven
#print axioms full_prefix_gcd_dvd
#print axioms denominator_bound
end Collatz.HighFloorNorm

