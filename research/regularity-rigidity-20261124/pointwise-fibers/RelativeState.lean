module

public import OrdinaryFiber
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! A necessary sign bound for a relative five-comparison state, with both words
attached to the same actual pair of starts at a common physical clock. -/

@[expose] public section

namespace RelativeState

open OrdinaryFiber
open RegularityRigidity (T)

/-- Clearing the actual relative endpoint identity gives a difference of the two word carries. -/
theorem relative_carry_identity (u v : List Bool) (x y Y D : ℤ) (plus minus : ℕ)
    (he : v.length = u.length) (hp : minus + v.count true = plus + u.count true)
    (hu : parityWord u.length x = u ∧ (T^[u.length]) x = y)
    (hv : parityWord v.length (5 * x) = v ∧ (T^[v.length]) (5 * x) = Y)
    (hrel : (3 : ℤ) ^ minus * Y = 5 * 3 ^ plus * y + D) :
    (2 : ℤ) ^ u.length * D =
      3 ^ minus * carry v - 5 * 3 ^ plus * carry u := by
  have hs := (affine_iff_orbit ..).mpr hu
  have ht := (affine_iff_orbit ..).mpr hv
  rw [he] at ht
  have hpow : (3 : ℤ) ^ minus * 3 ^ v.count true =
      3 ^ plus * 3 ^ u.count true := by rw [← pow_add, ← pow_add, hp]
  have hD : D = 3 ^ minus * Y - 5 * 3 ^ plus * y := by omega
  calc
    (2 : ℤ) ^ u.length * D =
        3 ^ minus * (2 ^ u.length * Y) - 5 * 3 ^ plus * (2 ^ u.length * y) := by
      rw [hD]; ring
    _ = 5 * x * (3 ^ minus * 3 ^ v.count true - 3 ^ plus * 3 ^ u.count true) +
          (3 ^ minus * carry v - 5 * 3 ^ plus * carry u) := by rw [← hs, ← ht]; ring
    _ = _ := by rw [hpow]; ring

/-- A source offset at most b/c and a positive companion carry force
`c D > -5·3^plus b`. The integer inequality includes the exact denominator. -/
theorem relative_offset_gate (u v : List Bool) (x y Y D : ℤ) (plus minus b c : ℕ)
    (he : v.length = u.length) (hp : minus + v.count true = plus + u.count true)
    (hu : parityWord u.length x = u ∧ (T^[u.length]) x = y)
    (hv : parityWord v.length (5 * x) = v ∧ (T^[v.length]) (5 * x) = Y)
    (hrel : (3 : ℤ) ^ minus * Y = 5 * 3 ^ plus * y + D)
    (hc : 0 < c) (hcut : c * carry u ≤ b * 2 ^ u.length) (hpos : 0 < carry v) :
    -5 * (3 : ℤ) ^ plus * b < (c : ℤ) * D := by
  have h := relative_carry_identity u v x y Y D plus minus he hp hu hv hrel
  have hcut' : (c : ℤ) * carry u ≤ b * (2 : ℤ) ^ u.length := by exact_mod_cast hcut
  have h1 := mul_le_mul_of_nonneg_left hcut' (by positivity : 0 ≤ 5 * (3 : ℤ) ^ plus)
  have h2 : 0 < (c : ℤ) * ((3 : ℤ) ^ minus * carry v) := by
    have hpv : (0 : ℤ) < carry v := by exact_mod_cast hpos
    have hpc : (0 : ℤ) < c := by exact_mod_cast hc
    exact mul_pos hpc (mul_pos (pow_pos (by decide) _) hpv)
  apply lt_of_mul_lt_mul_left (a := (2 : ℤ) ^ u.length) _ (by positivity)
  calc
    _ ≤ -(5 * 3 ^ plus * ((c : ℤ) * carry u)) := by nlinarith only [h1]
    _ < c * (3 ^ minus * carry v - 5 * 3 ^ plus * carry u) := by
      nlinarith only [h2]
    _ = _ := by rw [← h]; ring

/-- The integral candidate `Y=5y-4` is impossible at equal odd counts and source offset
at most one half when the companion word starts odd. -/
theorem excludes_minus_four (u v : List Bool) (x y Y : ℤ)
    (he : (true :: v).length = u.length) (hp : (true :: v).count true = u.count true)
    (hu : parityWord u.length x = u ∧ (T^[u.length]) x = y)
    (hv : parityWord (true :: v).length (5 * x) = true :: v ∧
      (T^[(true :: v).length]) (5 * x) = Y)
    (hcap : 2 * carry u ≤ 2 ^ u.length) : Y ≠ 5 * y - 4 := by
  intro hbad
  have hpos : 0 < carry (true :: v) := by
    simp only [carry]
    positivity
  have h := relative_offset_gate u (true :: v) x y Y (-4) 0 0 1 2 he
    (by simpa using hp) hu hv (by simpa [sub_eq_add_neg] using hbad) (by decide) (by simpa using hcap) hpos
  norm_num at h

#print axioms relative_carry_identity
#print axioms relative_offset_gate
#print axioms excludes_minus_four

end RelativeState
