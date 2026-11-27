import Mathlib.Algebra.Polynomial.Div
import Mathlib.Algebra.Polynomial.Degree.TrailingDegree
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.NormNum

/-! Integer-root arithmetic for a cleared polynomial relation on an actual word. -/
namespace Collatz.SixHour.OrdinaryRelations

open Polynomial

theorem root_dvd_first_coefficient {p : Polynomial ℤ} {x : ℤ}
    (hx : x ≠ 0) (hroot : p.IsRoot x) :
    x ∣ p.coeff p.natTrailingDegree := by
  let k := p.natTrailingDegree
  obtain ⟨g, hg⟩ : X ^ k ∣ p :=
    X_pow_dvd_iff.mpr (fun _ h => coeff_eq_zero_of_lt_natTrailingDegree h)
  have hz : x ^ k * g.eval x = 0 := by
    simpa only [IsRoot, hg, eval_mul, eval_pow, eval_X] using hroot
  have hgr : g.IsRoot x :=
    (mul_eq_zero.mp hz).resolve_left (pow_ne_zero _ hx)
  have hc := coeff_X_pow_mul g k 0
  rw [Nat.zero_add, ← hg] at hc
  exact hc.symm ▸ hgr.dvd_coeff_zero

theorem root_bounded_by_first_coefficient {p : Polynomial ℤ} {x : ℤ}
    (hp : p ≠ 0) (hx : x ≠ 0) (hroot : p.IsRoot x) :
    x.natAbs ≤ (p.coeff p.natTrailingDegree).natAbs :=
  Int.natAbs_le_of_dvd_ne_zero (root_dvd_first_coefficient hx hroot)
    (coeff_natTrailingDegree_ne_zero.mpr hp)

theorem zero_polynomial_of_small_coefficients {p : Polynomial ℤ} {x : ℤ}
    (hx : x ≠ 0) (hroot : p.IsRoot x)
    (hsmall : ∀ j, (p.coeff j).natAbs < x.natAbs) : p = 0 := by
  by_contra hp
  exact (not_lt_of_ge (root_bounded_by_first_coefficient hp hx hroot))
    (hsmall p.natTrailingDegree)

end Collatz.SixHour.OrdinaryRelations
