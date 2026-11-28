import Mathlib.Data.Nat.Basic
import Mathlib.Tactic.Ring

/-! The geometric physical step in the moving-residue proper-arc obstruction. -/

namespace Collatz.SimpleArc

/-- Physical numerator evolution with odd common denominator `d`. -/
def step (d a : ℕ) : ℕ := if 2 ∣ a then a / 2 else (3*a+d)/2

/-- A given number of initial twos forces the exact prefix of even halvings. -/
theorem forced_prefix {d L e t : ℕ} {x : ℕ → ℕ}
    (hs : ∀ j < L, x (j+1) = step d (x j)) (start : x 0 = 2^e*t)
    {j : ℕ} (hj : j ≤ L) (he : j ≤ e) : x j = 2^(e-j)*t := by
  induction j with
  | zero => simpa using start
  | succ j ih =>
    have h := ih (by omega) (by omega)
    have exponent : e-j = (e-(j+1))+1 := by omega
    have doubled : x j = 2*(2^(e-(j+1))*t) := by
      rw [h, exponent, pow_succ]
      ring
    simp [hs j (by omega), step, doubled]

/-- A simple forward arc containing an odd departure cannot start at a
power-of-two multiple of its own endpoint. -/
theorem mixed_arc_no_forward_multiple {d L : ℕ} {x : ℕ → ℕ}
    (hs : ∀ j < L, x (j+1) = step d (x j))
    (simpleEnd : ∀ j < L, x j ≠ x L)
    (oddDepart : ∃ j < L, ¬ 2 ∣ x j) (e : ℕ) : x 0 ≠ 2^e*x L := by
  intro start
  by_cases he : e < L
  · exact simpleEnd e he (by simpa using forced_prefix hs start he.le (le_refl e))
  · obtain ⟨j, hj, hodd⟩ := oddDepart
    have h := forced_prefix hs start hj.le (by omega : j ≤ e)
    have exponent : e-j = (e-(j+1))+1 := by omega
    apply hodd
    refine ⟨2^(e-(j+1))*x L, ?_⟩
    rw [h, exponent, pow_succ]
    ring

/-- On both complementary simple physical arcs an interior odd departure
excludes either orientation of a dyadic endpoint ratio. -/
theorem complementary_arcs_no_dyadic_ratio {d L M : ℕ} {x y : ℕ → ℕ}
    (hx : ∀ j < L, x (j+1) = step d (x j))
    (hy : ∀ j < M, y (j+1) = step d (y j))
    (hxy : x L = y 0) (hyx : y M = x 0)
    (sx : ∀ j < L, x j ≠ x L) (sy : ∀ j < M, y j ≠ y M)
    (ox : ∃ j < L, ¬ 2 ∣ x j) (oy : ∃ j < M, ¬ 2 ∣ y j) (e : ℕ) :
    x 0 ≠ 2^e*x L ∧ x L ≠ 2^e*x 0 := by
  constructor
  · exact mixed_arc_no_forward_multiple hx sx ox e
  · rw [hxy, ← hyx]
    exact mixed_arc_no_forward_multiple hy sy oy e

end Collatz.SimpleArc
