import Mathlib.Tactic

/-!
# The integer stage of the center-one scalar certificate

The actual odd clock has `2^g * q' = 3*q+1`.  The discounted gap scalar
has `h' = 3*h-g`.  Once this scalar is a positive integer, put
`a=2^h`, `b=2^g`, `c=2^h'`; then `b*c=a^3`.

The main arithmetic result below proves contraction of
`(q-1)/(2^h-1)` by at most `3/4`.  The real discounted series, its
derivative interpretation, and the arbitrary-source arithmetic
construction are not formalized or assumed as custom axioms here.
-/

namespace Collatz.RepoSynthesisRoundEight.GermBridge

set_option autoImplicit false

/-- The polynomial inequality behind the exact integer-stage potential. -/
theorem polynomial_gap_contraction (q a b : ℤ)
    (hq : 3 ≤ q) (ha : 2 ≤ a) (hb : 2 ≤ b) (hba : 2 * b ≤ a ^ 3) :
    4 * (3 * q + 1 - b) * (a - 1) ≤
      3 * (q - 1) * (a ^ 3 - b) := by
  have hquad : 0 ≤ a ^ 2 + 2 * a - 4 := by nlinarith [sq_nonneg a]
  have hfactor : 0 ≤ (a - 2) * (a ^ 2 + 2 * a - 4) :=
    mul_nonneg (by omega) hquad
  have hcoefficient : 0 ≤ 3 * a ^ 3 - 3 * b - 12 * a + 12 := by
    nlinarith [hfactor]
  have hcharge : 0 ≤ (q - 3) * (3 * a ^ 3 - 3 * b - 12 * a + 12) :=
    mul_nonneg (by omega) hcoefficient
  have hbase : 0 ≤ 6 * a ^ 3 - 40 * a + 40 + b * (4 * a - 10) := by
    rcases (show a = 2 ∨ 3 ≤ a by omega) with rfl | ha3
    · norm_num at hba ⊢
      omega
    · have hbcharge : 0 ≤ (b - 2) * (4 * a - 10) :=
        mul_nonneg (by omega) (by omega)
      have hquad' : 0 ≤ 6 * a ^ 2 + 12 * a - 8 := by
        nlinarith [sq_nonneg a]
      have hfactor' : 0 ≤ (a - 2) * (6 * a ^ 2 + 12 * a - 8) :=
        mul_nonneg (by omega) hquad'
      nlinarith [hfactor', hbcharge]
  nlinarith [hcharge, hbase]

/-- Exact literal gap equations give the cross-multiplied `3/4` contraction.
The powers `a,b,c` remain complete; no gap or ordinary quotient is dropped. -/
theorem integer_gap_potential_step (q q' a b c : ℤ)
    (hq : 3 ≤ q) (ha : 2 ≤ a) (hb : 2 ≤ b) (hc : 2 ≤ c)
    (hstep : b * q' = 3 * q + 1) (hscalar : b * c = a ^ 3) :
    4 * (q' - 1) * (a - 1) ≤ 3 * (q - 1) * (c - 1) := by
  have hba : 2 * b ≤ a ^ 3 := by nlinarith
  have hp := polynomial_gap_contraction q a b hq ha hb hba
  have hid :
      3 * (q - 1) * (a ^ 3 - b) - 4 * (3 * q + 1 - b) * (a - 1) =
      b * (3 * (q - 1) * (c - 1) - 4 * (q' - 1) * (a - 1)) := by
    rw [← hscalar, ← hstep]
    ring
  have hnonneg : 0 ≤ b *
      (3 * (q - 1) * (c - 1) - 4 * (q' - 1) * (a - 1)) := by
    rw [← hid]
    linarith
  have hresult : 0 ≤ 3 * (q - 1) * (c - 1) -
      4 * (q' - 1) * (a - 1) := by
    nlinarith
  linarith

/-- The exact scalar charge produces the complete power relation. -/
theorem scalar_charge_power (h h' g : ℕ) (hcharge : h' + g = 3 * h) :
    (2 : ℤ) ^ g * 2 ^ h' = ((2 : ℤ) ^ h) ^ 3 := by
  calc
    (2 : ℤ) ^ g * 2 ^ h' = 2 ^ (g + h') := (pow_add _ _ _).symm
    _ = 2 ^ (h * 3) := by congr 1; omega
    _ = ((2 : ℤ) ^ h) ^ 3 := pow_mul _ _ _

/-- A surviving positive integer candidate fits below its ordinary bit length. -/
theorem scalar_guard_below_bitlength (h b : ℕ)
    (hb : 2 ≤ b) (hguard : 3 * h ≤ b + 3) : h ≤ b - 1 := by
  omega

/-- Three integer-stage steps cost strictly more than one binary digit. -/
theorem three_quarters_cube : (3 / 4 : ℚ) ^ 3 < 1 / 2 := by
  norm_num

/-- The final finite contraction contradicts the retained positive potential. -/
theorem finite_scalar_budget (v q : ℚ) (b : ℕ)
    (hv : 1 ≤ v) (hq : q < (2 : ℚ) ^ b)
    (hbound : v ≤ (1 / 2 : ℚ) ^ b * q) : False := by
  have hp : 0 < (1 / 2 : ℚ) ^ b := pow_pos (by norm_num) _
  have hprod : (1 / 2 : ℚ) ^ b * (2 : ℚ) ^ b = 1 := by
    rw [← mul_pow]
    norm_num
  have hlt := mul_lt_mul_of_pos_left hq hp
  rw [hprod] at hlt
  linarith

end Collatz.RepoSynthesisRoundEight.GermBridge
