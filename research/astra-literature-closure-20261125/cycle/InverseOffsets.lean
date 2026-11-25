import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Data.Nat.ModEq

namespace Collatz.LiteratureInverseOffsets

/-- A finite affine odd-to-odd path. The partial lower bound applies to every
departure, so the statement also applies to a first crossing read in reverse. -/
inductive Arc (s : Nat) : Nat → Nat → Nat → Nat → Prop where
  | nil (z : Nat) : Arc s z z 0 0
  | cons {z w y e k b : Nat} (floor : s ≤ 3*z) (val : 0 < e)
      (odd : z%2=1) (endOdd : w%2=1) (edge : 2^e*w=3*z+1)
      (tail : Arc s w y k b) : Arc s z y (k+1) (e+b)

/-- Both affine length estimates come from the genuine unrolled path. -/
theorem distortion {s z y k b : Nat} (path : Arc s z y k b) (short : k ≤ s) :
    3^k*z ≤ 2^b*y ∧ (s-k)*(2^b*y) ≤ s*(3^k*z) := by
  induction path with
  | nil => simp
  | @cons z w y e k b floor _ _ _ edge _ ih =>
    obtain ⟨lower,upper⟩ := ih (by omega)
    have sk : 0<s-k := by omega
    have succ : s-k = (s-(k+1))+1 := by omega
    have base : (s-(k+1))*(2^e*w) ≤ (s-k)*(3*z) := by
      rw [edge,succ]
      nlinarith only [show s-(k+1)≤3*z by omega]
    refine ⟨?_, ?_⟩
    · calc
        3^(k+1)*z = 3^k*(3*z) := by rw [Nat.pow_succ]; ac_rfl
        _ ≤ 3^k*(2^e*w) := Nat.mul_le_mul_left _ (by omega)
        _ = 2^e*(3^k*w) := by ac_rfl
        _ ≤ 2^e*(2^b*y) := Nat.mul_le_mul_left _ lower
        _ = 2^(e+b)*y := by rw [Nat.pow_add]; ac_rfl
    · apply Nat.le_of_mul_le_mul_left (c:=s-k) _ sk
      calc
        (s-k)*((s-(k+1))*(2^(e+b)*y)) =
            ((s-(k+1))*2^e)*((s-k)*(2^b*y)) := by rw [Nat.pow_add]; ac_rfl
        _ ≤ ((s-(k+1))*2^e)*(s*(3^k*w)) := Nat.mul_le_mul_left _ upper
        _ = (s*3^k)*((s-(k+1))*(2^e*w)) := by ac_rfl
        _ ≤ (s*3^k)*((s-k)*(3*z)) := Nat.mul_le_mul_left _ base
        _ = (s-k)*(s*(3^(k+1)*z)) := by rw [Nat.pow_succ]; ac_rfl

/-- A budget class at depth k begins in a one-sided interval of length 3k,
with its upper endpoint computed from y and b alone. -/
theorem source_window {s z y k b : Nat} (path : Arc s z y k b)
    (short : 12*k ≤ s) (pos : 0<s) (height : z≤2*s) :
    3^k*z≤2^b*y ∧ 2^b*y ≤ 3^k*(z+3*k) := by
  obtain ⟨lo,hi⟩ := distortion path (by omega)
  refine ⟨lo, ?_⟩
  apply Nat.le_of_mul_le_mul_left (c:=s-k) _ (by omega)
  calc
    (s-k)*(2^b*y) ≤ s*(3^k*z) := hi
    _ ≤ (s-k)*(3^k*(z+3*k)) := by
      have sk : s=(s-k)+k := by omega
      have aux : z≤3*(s-k) := by omega
      have scaled := Nat.mul_le_mul_right k aux
      have left : s*z ≤ (s-k)*(z+3*k) := by
        conv_lhs => rw [sk]
        nlinarith only [scaled]
      calc
        s*(3^k*z) = 3^k*(s*z) := by ac_rfl
        _ ≤ 3^k*((s-k)*(z+3*k)) := Nat.mul_le_mul_left _ left
        _ = (s-k)*(3^k*(z+3*k)) := by ac_rfl

/-- In a first reverse descent from the ordinary floor the terminal departure
still satisfies the weaker lower bound used by Arc. -/
theorem first_floor {s w z e : Nat} (hs : 3≤s) (hw : 3*s+1≤4*w)
    (positive : 0<e) (edge : 2^e*w=3*z+1) : s≤3*z := by
  have pow : 2≤2^e := by
    have := Nat.pow_le_pow_right (n:=2) (by decide) (show 1≤e by omega)
    simpa using this
  have := Nat.mul_le_mul_right w pow
  omega

/-- Full common-denominator cancellation for aligned inverse clocks. The
hypotheses are numerator congruences from the two integer affine carries. -/
theorem offset_class {d k v n m : Nat} (unit : Nat.Coprime 3 d)
    (same : 3^k*n ≡ 3^k*(2^v*m) [MOD d]) : n ≡ 2^v*m [MOD d] := by
  exact Nat.ModEq.cancel_left_of_coprime (unit.pow_left k).symm same

/-- Adjacent integer labels retain the entire denominator. This is valid for
composite d and every multiplicity of its prime divisors. -/
theorem adjacent_unit {u d p : Nat} (positive : 0<u)
    (root : u^p ≡ 2 [MOD d]) : Nat.Coprime (u-1) d := by
  let g := Nat.gcd (u-1) d
  have gu : g∣u-1 := Nat.gcd_dvd_left _ _
  have gd : g∣d := Nat.gcd_dvd_right _ _
  have first : 1 ≡ u [MOD g] := (Nat.modEq_iff_dvd' (by omega)).mpr gu
  have raised := first.pow p
  rw [one_pow] at raised
  have diff : 1 ≡ 2 [MOD g] := raised.trans (root.of_dvd gd)
  have one : g∣1 := (Nat.modEq_iff_dvd' (by decide)).mp diff
  exact Nat.dvd_one.mp one

/-- Removing common unit factors leaves precisely the gcd of the label
difference factor. This measures all prime powers, not only its support. -/
theorem exact_gap_gcd {d m a b t : Nat} (unit : Nat.Coprime m d)
    (difference : b-a ≡ m*t [MOD d]) :
    Nat.gcd (b-a) d=Nat.gcd t d := by
  have e := difference.gcd_eq
  rw [e, unit.gcd_mul_left_cancel t]

/-- Two labeled positive numerators recover the exact common factor of their
difference and d. The orientation here puts the smaller numerator first. -/
theorem labeled_gap {d a b u t : Nat} (unit : Nat.Coprime a d)
    (order : a≤b) (positive : 0<u) (rel : b ≡ a*u^t [MOD d]) :
    Nat.gcd (b-a) d = Nat.gcd (u^t-1) d := by
  apply exact_gap_gcd unit
  have one : 1≤u^t := Nat.pow_pos positive
  have bound : a≤a*u^t := by
    simpa using Nat.mul_le_mul_left a one
  have delta := rel.sub_right order bound
  rwa [Nat.mul_sub, Nat.mul_one]

#print axioms labeled_gap
#print axioms adjacent_unit
#print axioms exact_gap_gcd
#print axioms distortion
#print axioms source_window
#print axioms first_floor
#print axioms offset_class

end Collatz.LiteratureInverseOffsets
