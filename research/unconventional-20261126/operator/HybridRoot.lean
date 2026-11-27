import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

/-! Finite signed arithmetic for OP-D2. After the initial forward run, `d`
counts the remaining dyadic denominator budget of the ternary coordinate.
The state stores its integer numerator `u`, the real value `x` of the
first coordinate, and the full slope `p`. The odd guards below express
the literal exact division by three. -/
namespace CollatzMixedRoot

inductive Reach : ℕ → ℤ → ℚ → ℚ → Prop where
  | start (j : ℕ) :
      Reach j (2 * 3 ^ j - 2 ^ j) (-1) ((3 / 2 : ℚ) ^ j)
  | evenBefore {d u x p} (prior : Reach (d + 1) u x p) :
      Reach d u (2*x) (2*p)
  | oddBefore {d u v x p} (prior : Reach (d + 1) u x p)
      (guard : 3*v = u - 2^d) :
      Reach d v ((2*x-1)/3) ((2/3)*p)
  | evenAfter {u x p} (prior : Reach 0 u x p) :
      Reach 0 (2*u) (2*x) (2*p)
  | oddAfter {u v x p} (prior : Reach 0 u x p)
      (guard : 3*v = 2*u-1) :
      Reach 0 v ((2*x-1)/3) ((2/3)*p)

private theorem pow23 (d : ℕ) : (2:ℤ)^d ≤ 3^d :=
  pow_le_pow_left₀ (by decide) (by decide) _

theorem invariants {d u x p} (path : Reach d u x p) :
    x ≤ -1 ∧ 2 * (3:ℤ)^d - 2^d ≤ u ∧
      (u:ℚ) = (2:ℚ)^d * (x+2*p) := by
  induction path with
  | start j =>
    refine ⟨le_rfl, le_rfl, ?_⟩
    push_cast
    rw [div_pow]
    field_simp
    ring
  | @evenBefore d u x p prior ih =>
    obtain ⟨hx, hu, hv⟩ := ih
    rw [pow_succ, pow_succ] at hu
    rw [pow_succ] at hv
    refine ⟨by linarith, ?_, ?_⟩
    · linarith [pow23 d, show 0 ≤ (3:ℤ)^d by positivity]
    · rw [hv]
      ring
  | @oddBefore d u v x p prior guard ih =>
    obtain ⟨hx, hu, hv⟩ := ih
    rw [pow_succ, pow_succ] at hu
    rw [pow_succ] at hv
    have gq : 3*(v:ℚ) = (u:ℚ)-(2:ℚ)^d := by exact_mod_cast guard
    refine ⟨by linarith, by omega, ?_⟩
    rw [hv] at gq
    nlinarith only [gq]
  | evenAfter prior ih =>
    obtain ⟨hx, hu, hv⟩ := ih
    simp only [pow_zero, one_mul] at hu hv ⊢
    push_cast
    exact ⟨by linarith, by omega, by linarith⟩
  | @oddAfter u v x p prior guard ih =>
    obtain ⟨hx, hu, hv⟩ := ih
    simp only [pow_zero, one_mul] at hu hv ⊢
    have gq : 3*(v:ℚ) = 2*(u:ℚ)-1 := by exact_mod_cast guard
    exact ⟨by linarith, by omega, by linarith⟩

theorem slope_ge_one {d u x p} (path : Reach d u x p) : 1 ≤ p := by
  obtain ⟨hx, hu, hv⟩ := invariants path
  have hz : (2:ℤ)^d ≤ u := by linarith [pow23 d]
  have hq : (2:ℚ)^d ≤ (u:ℚ) := by exact_mod_cast hz
  rw [hv] at hq
  have hpos : 0 < (2:ℚ)^d := by positivity
  have hgap : 1 ≤ x + 2*p := by
    apply (mul_le_mul_iff_right₀ hpos).mp
    simpa using hq
  linarith

#print axioms CollatzMixedRoot.invariants
#print axioms CollatzMixedRoot.slope_ge_one

end CollatzMixedRoot
