import CycleCancellation
import CarryFibers
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Full-denominator tests at a least-carry cyclic root

The complete chronological carry and both clocks are retained. The
minimum comparison is supplied for the actual cut, and the strict gap
consumer derives distinct carries from distinct rotated words. The
suffix barrier is necessary for a minimum; it is not a selector of that
minimum or a sufficient condition for integrality. The necklace counting
and literature comparisons remain written mathematics in CYCLE_RIGIDITY.md.
-/

namespace Collatz.HighVariance.CycleRigidity

open Collatz.HighVariance.CycleWordAlgebra
open Collatz.HighVariance.CycleCancellation
open CollatzShell.CarryFibers

set_option autoImplicit false

/-- The whole-word numerical rotation gap is a signed determinant of
the two complete block carries and their own signed denominators. -/
theorem cut_determinant (u v : List Bool) :
    (carry (v ++ u) : Int) - carry (u ++ v) =
      denominator v * carry u - denominator u * carry v := by
  simp only [carry_append, Nat.cast_add, Nat.cast_mul, Nat.cast_pow,
    Nat.cast_ofNat, denominator]
  ring

/-- Exact transport before a modulus is applied. The denominator on the
right is that of u ++ v, not either block denominator. -/
theorem rotation_transport (u v : List Bool)
    (hpositive : 3 ^ ones (u ++ v) < 2 ^ (u ++ v).length) :
    2 ^ u.length * carry (v ++ u) =
      3 ^ ones u * carry (u ++ v) +
        (2 ^ (u ++ v).length - 3 ^ ones (u ++ v)) * carry u := by
  have hd := Nat.sub_add_cancel hpositive.le
  simp only [List.length_append, ones_append, pow_add] at hd ⊢
  rw [carry_append v u, carry_append u v]
  nlinarith

/-- Full numerical divisibility, including every prime power, survives
a cyclic cut. Coprimality is derived from this same positive denominator. -/
theorem full_denominator_rotation_dvd (u v : List Bool)
    (hp : 0 < ones (u ++ v))
    (hpositive : 3 ^ ones (u ++ v) < 2 ^ (u ++ v).length)
    (hzero : (2 ^ (u ++ v).length - 3 ^ ones (u ++ v)) ∣ carry (u ++ v)) :
    (2 ^ (u ++ v).length - 3 ^ ones (u ++ v)) ∣ carry (v ++ u) := by
  have hA : 0 < (u ++ v).length := by
    by_contra h
    have hz : (u ++ v).length = 0 := by omega
    have hw : u ++ v = [] := List.eq_nil_of_length_eq_zero hz
    simp [hw, ones] at hp
  have hcop := (denominator_coprime_two_three _ _ hA hp hpositive.le).1
  apply (hcop.pow_right u.length).dvd_of_dvd_mul_left
  rw [rotation_transport u v hpositive]
  exact dvd_add (dvd_mul_of_dvd_right hzero _) (dvd_mul_right _ _)

/-- At a least-carry root, a genuinely different cyclic cut has an
ordinary integer carry gap of at least the complete positive denominator.
The distinct-word hypothesis is what a proper cut of a primitive word supplies. -/
theorem least_rotation_full_denominator_gap (u v : List Bool)
    (hp : 0 < ones (u ++ v))
    (hpositive : 3 ^ ones (u ++ v) < 2 ^ (u ++ v).length)
    (hzero : (2 ^ (u ++ v).length - 3 ^ ones (u ++ v)) ∣ carry (u ++ v))
    (hroot : carry (u ++ v) ≤ carry (v ++ u))
    (hne : u ++ v ≠ v ++ u) :
    2 ^ (u ++ v).length - 3 ^ ones (u ++ v) ≤
      carry (v ++ u) - carry (u ++ v) := by
  have hcarry : carry (u ++ v) ≠ carry (v ++ u) := by
    intro he
    exact hne (word_eq_of_length_ones_carry
      (by simp [Nat.add_comm]) (by simp [ones_append, Nat.add_comm]) he)
  have hgap : 0 < carry (v ++ u) - carry (u ++ v) :=
    Nat.sub_pos_of_lt (lt_of_le_of_ne hroot hcarry)
  have hd := Nat.dvd_sub (full_denominator_rotation_dvd u v hp hpositive hzero) hzero
  exact Nat.le_of_dvd hgap hd

private theorem carry_pos_of_ones_pos (w : List Bool) (h : 0 < ones w) :
    0 < carry w := by
  induction w with
  | nil => simp [ones] at h
  | cons b w ih =>
    cases b with
    | false =>
      have hh : 0 < ones w := by simpa [ones] using h
      simpa [carry] using Nat.mul_pos (by decide : 0 < 2) (ih hh)
    | true =>
      simp only [carry, ite_true, mul_one]
      exact lt_of_lt_of_le (by positivity : 0 < 3 ^ ones w) (Nat.le_add_right _ _)

/-- Every nonempty suffix of a least-carry positive cycle word is
strictly contracting in its multiplicative coefficient. This holds for
rational cycle words as well and does not imply full-denominator divisibility. -/
theorem least_rotation_suffix_contracts (u v : List Bool)
    (hv : 0 < v.length)
    (hpositive : 3 ^ ones (u ++ v) < 2 ^ (u ++ v).length)
    (hroot : carry (u ++ v) ≤ carry (v ++ u)) :
    3 ^ ones v < 2 ^ v.length := by
  by_contra hbad
  have hvbad : 2 ^ v.length ≤ 3 ^ ones v := by omega
  have hvones : 0 < ones v := by
    by_contra h
    have hz : ones v = 0 := by omega
    have htwo : 2 ≤ 2 ^ v.length := by
      simpa using Nat.pow_le_pow_right (by decide : 1 ≤ 2) hv
    simp only [hz, pow_zero] at hvbad
    omega
  have hcv := carry_pos_of_ones_pos v hvones
  have hup : 3 ^ ones u < 2 ^ u.length := by
    have ht := hpositive
    simp only [ones_append, List.length_append, pow_add] at ht
    by_contra hu
    have hh := Nat.mul_le_mul (Nat.le_of_not_gt hu) hvbad
    omega
  rw [carry_append u v, carry_append v u] at hroot
  have hleft := Nat.mul_le_mul_right (carry u) hvbad
  have hright := Nat.mul_lt_mul_of_pos_right hup hcv
  omega

/-- This primitive rational-cycle control satisfies the suffix barrier
at more than one rotation. Its small positive root gap rejects integrality. -/
example :
    carry [true, true, true, false, false, true, false] = 89 ∧
    carry [true, false, true, true, true, false, false] = 103 ∧
    denominator [true, true, true, false, false, true, false] = 47 ∧
    ¬ (47 : Nat) ∣ carry [true, true, true, false, false, true, false] := by
  norm_num [carry, ones, denominator]

end Collatz.HighVariance.CycleRigidity
