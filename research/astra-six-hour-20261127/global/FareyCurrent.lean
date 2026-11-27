import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-! The exact integer cone of the positive odd edge d*y = 3*x+1. -/
namespace Collatz.SixHour.Farey

def Heights (x y d t : ℤ) := {j : ℤ // 3*t < y*j ∧ x*j ≤ d*t}

def Coordinates (x y t : ℤ) :=
  {p : ℤ × ℤ // 0 < p.1 ∧ 0 ≤ p.2 ∧ p.1*x + p.2*y = t}

theorem inverse_first (x y d t j : ℤ) (h : d*y = 3*x+1) :
    (y*j-3*t)*x + (d*t-x*j)*y = t := by
  calc
    _ = (d*y-3*x)*t := by ring
    _ = t := by rw [h]; ring

theorem inverse_second (x y d t j : ℤ) (h : d*y = 3*x+1) :
    (y*j-3*t)*d + (d*t-x*j)*3 = j := by
  calc
    _ = (d*y-3*x)*j := by ring
    _ = j := by rw [h]; ring

theorem forward_first (x y d r s : ℤ) (h : d*y = 3*x+1) :
    y*(r*d+s*3) - 3*(r*x+s*y) = r := by
  calc
    _ = (d*y-3*x)*r := by ring
    _ = r := by rw [h]; ring

theorem forward_second (x y d r s : ℤ) (h : d*y = 3*x+1) :
    d*(r*x+s*y) - x*(r*d+s*3) = s := by
  calc
    _ = (d*y-3*x)*s := by ring
    _ = s := by rw [h]; ring

/-- All lattice points in the half-open Farey sector at one height. -/
def sectorEquiv (x y d t : ℤ) (h : d*y = 3*x+1) :
    Heights x y d t ≃ Coordinates x y t where
  toFun j := ⟨(y*j.1-3*t,d*t-x*j.1), by
    exact ⟨sub_pos.mpr j.2.1, sub_nonneg.mpr j.2.2, inverse_first x y d t j.1 h⟩⟩
  invFun p := ⟨p.1.1*d+p.1.2*3, by
    obtain ⟨hr, hs, ht⟩ := p.2
    have hf := forward_first x y d p.1.1 p.1.2 h
    have hg := forward_second x y d p.1.1 p.1.2 h
    rw [ht] at hf hg
    omega⟩
  left_inv j := Subtype.ext (inverse_second x y d t j.1 h)
  right_inv p := by
    apply Subtype.ext
    apply Prod.ext
    · change y*(p.1.1*d+p.1.2*3)-3*t = p.1.1
      have he := forward_first x y d p.1.1 p.1.2 h
      rw [p.2.2.2] at he
      exact he
    · change d*t-x*(p.1.1*d+p.1.2*3) = p.1.2
      have he := forward_second x y d p.1.1 p.1.2 h
      rw [p.2.2.2] at he
      exact he

theorem no_point_before_source (x y d t : ℤ) (h : d*y = 3*x+1)
    (hx : 0 < x) (hy : 0 < y) (ht : t < x) : IsEmpty (Heights x y d t) := by
  constructor
  intro j
  let p := sectorEquiv x y d t h j
  obtain ⟨hr, hs, heq⟩ := p.2
  have h1 : 1 ≤ p.1.1 := by omega
  have h2 := mul_le_mul_of_nonneg_right h1 (le_of_lt hx)
  have h3 := mul_nonneg hs (le_of_lt hy)
  linarith

theorem point_at_source_unique (x y d : ℤ) (h : d*y = 3*x+1)
    (hx : 0 < x) (hy : 0 < y) (j : Heights x y d x) : j.1 = d := by
  let p := sectorEquiv x y d x h j
  obtain ⟨hr, hs, heq⟩ := p.2
  have h1 : 1 ≤ p.1.1 := by omega
  have h2 := mul_le_mul_of_nonneg_right h1 (le_of_lt hx)
  have h3 := mul_nonneg hs (le_of_lt hy)
  have h4 : p.1.1*x = x := by linarith
  have h5 : p.1.2*y = 0 := by linarith
  have hr1 : p.1.1 = 1 := by
    apply (mul_left_inj' (ne_of_gt hx)).mp
    simpa using h4
  have hs0 : p.1.2 = 0 := (mul_eq_zero.mp h5).resolve_right (ne_of_gt hy)
  have hj : p.1.1*d+p.1.2*3 = j.1 := inverse_second x y d x j.1 h
  simpa [hr1, hs0] using hj.symm

theorem point_at_source (x y d : ℤ) (h : d*y = 3*x+1) :
    3*x < y*d ∧ x*d ≤ d*x := by constructor <;> nlinarith

theorem arc_identity (x y d : ℚ) (hx : 0 < x) (hy : 0 < y)
    (h : d*y = 3*x+1) : d/x - 3/y = 1/(x*y) := by
  field_simp
  linarith

theorem arc_square_bound (x y : ℚ) (hx : 0 < x) (hy : 0 < y) :
    1/(x*y) ≤ (1/x^2 + 1/y^2)/2 := by
  field_simp
  nlinarith [sq_nonneg (x-y)]

end Collatz.SixHour.Farey
