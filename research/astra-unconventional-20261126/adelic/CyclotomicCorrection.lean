import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Actual field factorizations in the two-place Bloch correction, tested against
arbitrary pairs of additive logarithmic coordinates of nonzero field elements. -/

namespace Collatz.CyclotomicCorrection

set_option autoImplicit false

variable {K : Type*} [Field K]

/-- A coordinate of the rational vector space of nonzero field elements under
multiplication. The value at zero is irrelevant to the theorems below. -/
structure LogCoord (K : Type*) [Field K] where
  val : K → ℚ
  one : val 1 = 0
  mul : ∀ {x y : K}, x ≠ 0 → y ≠ 0 → val (x*y) = val x + val y

private theorem pow_coord (a : LogCoord K) {x : K} (hx : x ≠ 0) (n : ℕ) :
    a.val (x^n) = n * a.val x := by
  induction n with
  | zero => simp [a.one]
  | succ n ih =>
    rw [pow_succ, a.mul (pow_ne_zero _ hx) hx, ih]
    push_cast
    ring

/-- An alternating coordinate of the rationalized exterior boundary. -/
def detCoord (a b : LogCoord K) (x y : K) : ℚ := a.val x*b.val y - b.val x*a.val y

def boundary (a b : LogCoord K) (x : K) : ℚ := detCoord a b x (1-x)

/-- The cyclotomic quotient of two power symbols has a single wedge boundary. -/
theorem power_correction (a b : LogCoord K) {t h : K} {k j : ℕ}
    (hk : 0 < k) (hj : 0 < j) (ht : t ≠ 0) (hbase : 1-t^k ≠ 0)
    (hh : h ≠ 0) (factor : 1-t^(k*j) = (1-t^k)*h) :
    boundary a b (t^k)/(k : ℚ) - boundary a b (t^(k*j))/(k*j : ℚ) =
      -detCoord a b t h := by
  have hk0 : (k : ℚ) ≠ 0 := by exact_mod_cast hk.ne'
  have hj0 : (j : ℚ) ≠ 0 := by exact_mod_cast hj.ne'
  simp only [boundary, detCoord, pow_coord a ht, pow_coord b ht, factor,
    a.mul hbase hh, b.mul hbase hh, Nat.cast_mul]
  field_simp [hk0, hj0]
  ring

/-- No algebraic independence or local logarithm-series hypotheses are needed
for the two global exterior factorizations. -/
theorem two_corrections (a b : LogCoord K) {r z : K}
    (hr : r ≠ 0) (hz : z ≠ 0) (hr6 : 1-r^6 ≠ 0) (hz24 : 1-z^24 ≠ 0)
    (hh : 1+r^6+r^12 ≠ 0) (hj : 1+z^24 ≠ 0) :
    (boundary a b (r^6)/6 - boundary a b (r^18)/18 =
        -detCoord a b r (1+r^6+r^12)) ∧
    (boundary a b (z^24)/24 - boundary a b (z^48)/48 =
        -detCoord a b z (1+z^24)) := by
  constructor
  · have hc := power_correction a b (k := 6) (j := 3) (by decide) (by decide)
      hr hr6 hh (by ring)
    norm_num at hc
    exact hc
  · have hc := power_correction a b (k := 24) (j := 2) (by decide) (by decide)
      hz hz24 hj (by ring)
    norm_num at hc
    exact hc

/-- A complete coordinate of the two-place repair, including the adjustment to the
second place made by clearing the first. The other coordinate of the determinant
is arbitrary, so this tests the whole valuation contraction. -/
theorem repair_coordinates (c3 c2 r h z : ℚ) (A : ℕ)
    (at3 : 2*c3 = r) (at2 : 2*c2 + A*h = -z) :
    c3-r/2 = 0 ∧ c2-(-A*h)/2+z/2 = 0 := by
  constructor <;> linarith

#print axioms power_correction
#print axioms two_corrections
#print axioms repair_coordinates

end Collatz.CyclotomicCorrection
