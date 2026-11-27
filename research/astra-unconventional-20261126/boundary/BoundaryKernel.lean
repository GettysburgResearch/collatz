import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Finite ordinary arithmetic used by the tilted boundary calculation.
    A path retains its odd and physical clocks. -/

namespace Collatz.BoundaryKernel

def multiplier (k s : ℕ) : ℚ := 3 ^ k / 2 ^ s

def retention (x y k s : ℕ) : ℚ := (x : ℚ) * multiplier k s / y

def address (a x kx sx ka sa : ℕ) : ℚ :=
  (x : ℚ) * multiplier kx sx / ((a : ℚ) * multiplier ka sa)

theorem multiplier_pos (k s : ℕ) : 0 < multiplier k s := by
  unfold multiplier
  positivity

theorem multiplier_append (k s b d : ℕ) :
    multiplier (k+b) (s+d) = multiplier k s * multiplier b d := by
  unfold multiplier
  rw [pow_add, pow_add]
  ring

/-- The exact equation for a genuine odd-to-odd step. Odd endpoints ensure
    that the prescribed power of two is the full valuation. -/
structure Edge (x y e : ℕ) : Prop where
  exponent_pos : 0 < e
  source_odd : x % 2 = 1
  target_odd : y % 2 = 1
  equation : 2^e * y = 3*x + 1

theorem Edge.target_pos {x y e : ℕ} (h : Edge x y e) : 0 < y := by
  rcases Nat.eq_zero_or_pos y with h0 | hp
  · have hf := h.target_odd
    simp [h0] at hf
  · exact hp

theorem Edge.retention {x y e : ℕ} (h : Edge x y e) :
    retention x y 1 e = (3*(x : ℚ))/(3*x+1) := by
  have he : (2 : ℚ)^e*y = 3*x+1 := by exact_mod_cast h.equation
  have hy : (y : ℚ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt h.target_pos)
  have hp : (2 : ℚ)^e ≠ 0 := by positivity
  have ha : 3*(x : ℚ)+1 ≠ 0 := by positivity
  unfold BoundaryKernel.retention multiplier
  rw [pow_one]
  field_simp [hy, hp, ha]
  rw [mul_assoc, he]
  ring

theorem retention_append (x y z k s b d : ℕ) (hy : y ≠ 0) :
    retention x y k s * retention y z b d = retention x z (k+b) (s+d) := by
  have hy' : (y : ℚ) ≠ 0 := by exact_mod_cast hy
  unfold retention
  rw [multiplier_append]
  field_simp [hy']

/-- Extending both actual paths by the same clocks preserves the address. -/
theorem address_append (a x kx sx ka sa b d : ℕ) :
    address a x (kx+b) (sx+d) (ka+b) (sa+d) = address a x kx sx ka sa := by
  unfold address
  rw [multiplier_append, multiplier_append]
  have hp := ne_of_gt (multiplier_pos b d)
  by_cases ha : a=0
  · simp [ha]
  have ha' : (a : ℚ) ≠ 0 := by exact_mod_cast ha
  field_simp [hp, ha', ne_of_gt (multiplier_pos ka sa)]


/-- Distinct ordinary units have different addresses, even if the two
    routes that define their addresses have unequal clocks. -/
theorem strip_clocks {x y : ℕ} (x2 : x.Coprime 2) (x3 : x.Coprime 3)
    (y2 : y.Coprime 2) (y3 : y.Coprime 3) (a b c d : ℕ)
    (h : x * (3^a * 2^b) = y * (3^c * 2^d)) : x = y := by
  apply Nat.dvd_antisymm
  · apply ((x3.pow_right c).mul_right (x2.pow_right d)).dvd_of_dvd_mul_right
    rw [← h]
    exact Nat.dvd_mul_right _ _
  · apply ((y3.pow_right a).mul_right (y2.pow_right b)).dvd_of_dvd_mul_right
    rw [h]
    exact Nat.dvd_mul_right _ _

theorem address_injective_source {a x y : ℕ} (ha : 0<a)
    (x2 : x.Coprime 2) (x3 : x.Coprime 3) (y2 : y.Coprime 2) (y3 : y.Coprime 3)
    (kx sx ky sy ka sa : ℕ)
    (h : address a x kx sx ka sa = address a y ky sy ka sa) : x=y := by
  have den : (a : ℚ) * multiplier ka sa ≠ 0 := by
    exact mul_ne_zero (by exact_mod_cast (Nat.ne_of_gt ha)) (ne_of_gt (multiplier_pos ka sa))
  have hm : (x : ℚ)*multiplier kx sx = (y : ℚ)*multiplier ky sy := by
    unfold address at h
    exact (div_left_inj' den).mp h
  unfold multiplier at hm
  have xpow : (2 : ℚ)^sx ≠ 0 := by positivity
  have ypow : (2 : ℚ)^sy ≠ 0 := by positivity
  have hc : (x : ℚ) * (3^kx * 2^sy) = (y : ℚ) * (3^ky * 2^sx) := by
    field_simp [xpow, ypow] at hm
    simpa only [mul_assoc, mul_left_comm, mul_comm] using hm
  apply strip_clocks x2 x3 y2 y3 kx sy ky sx
  exact_mod_cast hc

theorem square_atom_weight (a x kx sx ka sa : ℕ) (hx : x ≠ 0) :
    (multiplier kx sx / ((a : ℚ)*multiplier ka sa))^2 =
      (address a x kx sx ka sa)^2 / (x : ℚ)^2 := by
  unfold address
  have hx' : (x : ℚ) ≠ 0 := by exact_mod_cast hx
  by_cases h : (a : ℚ)*multiplier ka sa=0
  · simp [h]
  field_simp [hx', h]


#print axioms Edge.retention
#print axioms retention_append
#print axioms address_append
#print axioms address_injective_source
#print axioms square_atom_weight

end Collatz.BoundaryKernel
