import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
Exact finite weighted prefix sums in the scalar substitution identity.
A false bit has multiplier x and reward u. A true bit has multiplier y
and reward v. The statement applies in particular to rational weights.
-/
namespace Collatz.SubstitutionMass

variable {R : Type*} [CommSemiring R]

def scale (x y : R) : List Bool → R
  | [] => 1
  | false :: w => x * scale x y w
  | true :: w => y * scale x y w

def mass (x y u v : R) : List Bool → R
  | [] => 0
  | false :: w => u + x * mass x y u v w
  | true :: w => v + y * mass x y u v w

def encode (p q : List Bool) : List Bool → List Bool
  | [] => []
  | false :: w => p ++ encode p q w
  | true :: w => q ++ encode p q w

theorem scale_append (x y : R) (a b : List Bool) :
    scale x y (a ++ b) = scale x y a * scale x y b := by
  induction a with
  | nil => simp [scale]
  | cons bit a ih =>
    cases bit <;> simp [scale, ih, mul_assoc]

theorem mass_append (x y u v : R) (a b : List Bool) :
    mass x y u v (a ++ b) = mass x y u v a + scale x y a * mass x y u v b := by
  induction a with
  | nil => simp [scale, mass]
  | cons bit a ih =>
    cases bit <;> simp only [List.cons_append, mass, scale, ih] <;> ring

theorem mass_linear (x y u v : R) (w : List Bool) :
    mass x y u v w = u * mass x y 1 0 w + v * mass x y 0 1 w := by
  induction w with
  | nil => simp [mass]
  | cons bit w ih =>
    cases bit <;> simp only [mass, ih] <;> ring

theorem mass_substitution (x y u v : R) (p q w : List Bool) :
    mass x y u v (encode p q w) =
      mass (scale x y p) (scale x y q) (mass x y u v p) (mass x y u v q) w := by
  induction w with
  | nil => rfl
  | cons bit w ih =>
    cases bit <;> simp only [encode, mass_append, mass, ih]

theorem weighted_telescope (x y : R) (w : List Bool) :
    1 + x * mass x y 1 0 w + y * mass x y 0 1 w =
      scale x y w + mass x y 1 0 w + mass x y 0 1 w := by
  induction w with
  | nil => simp [mass, scale]
  | cons bit w ih =>
    cases bit with
    | false =>
      simp only [mass, scale]
      have h := congrArg (fun t : R => 1 + x * t) ih
      convert h using 1 <;> ring
    | true =>
      simp only [mass, scale]
      have h := congrArg (fun t : R => 1 + y * t) ih
      convert h using 1 <;> ring

/-- The finite-boundary correction is the full weight of the source word.
This denominator-free identity yields the scalar infinite-prefix relation
when that boundary tends to zero at the selected place. -/
theorem scalar_substitution {K : Type*} [CommRing K] (x y : K)
    (p q w : List Bool) :
    (1 - scale x y p) * mass x y 0 1 (encode p q w) =
      (1 - scale (scale x y p) (scale x y q) w) * mass x y 0 1 p +
      ((1 - scale x y p) * mass x y 0 1 q -
       (1 - scale x y q) * mass x y 0 1 p) *
       mass (scale x y p) (scale x y q) 0 1 w := by
  rw [mass_substitution, mass_linear (scale x y p) (scale x y q)
    (mass x y 0 1 p) (mass x y 0 1 q)]
  linear_combination -(mass x y 0 1 p) *
    weighted_telescope (scale x y p) (scale x y q) w

end Collatz.SubstitutionMass
