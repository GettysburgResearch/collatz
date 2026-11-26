import Mathlib.Algebra.Field.ZMod
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! The cubic trace of the ordinary Pell unit, including the obstruction to a
rational root at three and the local factorizations used for its discriminant. -/

namespace Collatz.CubicLift

set_option autoImplicit false

/-- Cubing the norm-one lift acts on its trace by the Dickson cubic. -/
theorem trace_cube {K : Type*} [Field K] (t : K) (ht : t ≠ 0) :
    (t+t⁻¹)^3-3*(t+t⁻¹) = t^3+(t⁻¹)^3 := by
  field_simp [ht]
  ring

/-- A shift at three, and both local factorizations away from three. -/
theorem trace_factorizations {K : Type*} [CommRing K] (u x : K) :
    (u+2)^3-3*(u+2)-(12*x+2) = u*(u+3)^2-12*x ∧
    u^3-3*u-(12*x+2) = (u-2)*(u+1)^2-12*x ∧
    u^3-3*u-(12*x+2) = (u+2)*(u-1)^2-4*(3*x+1) := by
  constructor
  · ring
  · constructor <;> ring

/-- A primitive rational projective pair cannot solve the homogenized cubic.
Only primitivity at three is needed. -/
theorem no_primitive_root (n d x : ℤ) (hx : ¬ (3 : ℤ) ∣ x)
    (primitive : ¬ ((3 : ℤ) ∣ n ∧ (3 : ℤ) ∣ d)) :
    n*(n+3*d)^2 ≠ 12*x*d^3 := by
  intro he
  have h3 : (3 : ZMod 3) = 0 := by decide
  have h12 : (12 : ZMod 3) = 0 := by decide
  have h4 : (4 : ZMod 3) = 1 := by decide
  have hn := congrArg (Int.castRingHom (ZMod 3)) he
  simp only [map_mul, map_pow, map_add, map_ofNat] at hn
  change (n : ZMod 3)*(n+3*d)^2 = 12*x*d^3 at hn
  rw [h3, h12] at hn
  simp only [zero_mul, add_zero, mul_eq_zero, pow_eq_zero_iff (by decide : 2 ≠ 0),
    or_self] at hn
  have hdN := (ZMod.intCast_zmod_eq_zero_iff_dvd n 3).mp hn
  obtain ⟨k, hk⟩ := hdN
  have he' : 9*k*(k+d)^2 = 4*x*d^3 := by
    rw [hk] at he
    norm_num at he
    nlinarith only [he]
  have hd := congrArg (Int.castRingHom (ZMod 3)) he'
  simp only [map_mul, map_pow, map_add, map_ofNat] at hd
  change (9 : ZMod 3)*k*(k+d)^2 = 4*x*d^3 at hd
  rw [show (9 : ZMod 3) = 0 by decide, h4] at hd
  have hx' : (x : ZMod 3) ≠ 0 := by
    intro hz
    exact hx ((ZMod.intCast_zmod_eq_zero_iff_dvd x 3).mp hz)
  have hd' : (d : ZMod 3) = 0 := by
    simpa only [zero_mul, one_mul, mul_eq_zero, hx', false_or,
      pow_eq_zero_iff (by decide : 3 ≠ 0)] using hd.symm
  exact primitive ⟨⟨k,hk⟩, (ZMod.intCast_zmod_eq_zero_iff_dvd d 3).mp hd'⟩

/-- The polynomial discriminant is a rational square times the negative
consecutive product before clearing the physical dyadic clock. -/
theorem polynomial_discriminant (x : ℤ) :
    -4*(-3)^3 - 27*(-(12*x+2))^2 = -(36^2)*x*(3*x+1) := by ring

/-- As a rational function of the physical cubic trace the normalized number
has just two linear factors in its numerator and in its denominator. -/
theorem normalized_parameter {K : Type*} [Field K] [CharZero K] (t : K)
    (h₁ : t-1 ≠ 0) (h₂ : t-2 ≠ 0) (h₃ : t+1 ≠ 0) :
    let x := (t-2)*(t+1)^2/12
    ((t+1)/(t-1))^3 * (3*x+1)/(3*x) = (t+1)*(t+2)/((t-1)*(t-2)) := by
  dsimp
  field_simp [h₁, h₂, h₃]
  ring

/-- The primitive cubic used for the exact absolute height. -/
theorem normalized_polynomial {K : Type*} [Field K] [CharZero K] (t : K)
    (h₁ : t-1 ≠ 0) (h₂ : t-2 ≠ 0) :
    let x := (t-2)*(t+1)^2/12
    let u := (t+1)*(t+2)/((t-1)*(t-2))
    x*(3*x+1)*(u-1)^3 = 9*(3*x+1)*u^2+27*x*u := by
  dsimp
  field_simp [h₁, h₂]
  ring

#print axioms normalized_parameter
#print axioms normalized_polynomial
#print axioms trace_cube
#print axioms trace_factorizations
#print axioms no_primitive_root
#print axioms polynomial_discriminant

end Collatz.CubicLift
