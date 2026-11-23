import Mathlib.Tactic

/-!
Finite height separation for a triadic approximation to a fixed rational target.
The target's nonzero cross-product is an explicit hypothesis: no unknown Collatz
dual is assumed rational, and no universal small-residue estimate is asserted.
-/

namespace CollatzWeightedSelector

def weight : ℕ → ℕ
  | 0 => 1
  | r + 1 => weight r * (1 + 3 ^ r)

theorem weight_pos (r : ℕ) : 0 < weight r := by
  induction r with
  | zero => norm_num [weight]
  | succ r ih =>
      simp only [weight]
      positivity

theorem power_weight_bound (r : ℕ) : 2 * 3 ^ r ≤ 3 * weight r := by
  induction r with
  | zero => norm_num [weight]
  | succ r ih =>
      cases r with
      | zero => norm_num [weight]
      | succ j =>
          have hp : 0 < 3 ^ j := by positivity
          have hf : 3 ≤ 1 + 3 ^ (j + 1) := by
            rw [pow_succ]
            omega
          have hm := Nat.mul_le_mul_left (weight (j + 1)) hf
          calc
            2 * 3 ^ (j + 1 + 1) = 3 * (2 * 3 ^ (j + 1)) := by
              rw [pow_succ]
              ring
            _ ≤ 3 * (3 * weight (j + 1)) := Nat.mul_le_mul_left 3 ih
            _ ≤ 3 * (weight (j + 1) * (1 + 3 ^ (j + 1))) := by
              nlinarith
            _ = 3 * weight (j + 1 + 1) := rfl

theorem rational_gap (K q : ℕ) (a u d : ℤ)
    (hdiv : (2 : ℤ) ^ K ∣ d * a - u * q)
    (hne : d * a - u * q ≠ 0) :
    2 ^ K ≤ d.natAbs * a.natAbs + u.natAbs * q := by
  have hlo := Int.natAbs_le_of_dvd_ne_zero hdiv hne
  have hhi := Int.natAbs_add_le (d * a) (-(u * q))
  have hlo' : 2 ^ K ≤ (d * a - u * q).natAbs := by
    simpa only [Int.natAbs_pow, show (2 : ℤ).natAbs = 2 from rfl] using hlo
  have hhi' : (d * a - u * q).natAbs ≤
      d.natAbs * a.natAbs + u.natAbs * q := by
    simpa only [sub_eq_add_neg, Int.natAbs_neg, Int.natAbs_mul,
      Int.natAbs_natCast] using hhi
  exact hlo'.trans hhi'

theorem weighted_rational_gap (K r : ℕ) (a u d : ℤ)
    (hdiv : (2 : ℤ) ^ K ∣ d * a - u * 3 ^ r)
    (hne : d * a - u * 3 ^ r ≠ 0) :
    2 * 2 ^ K ≤ (2 * d.natAbs + 3 * u.natAbs) *
      weight r * max 1 a.natAbs := by
  have hdiv' : (2 : ℤ) ^ K ∣ d * a - u * ((3 ^ r : ℕ) : ℤ) := by
    simpa only [Nat.cast_pow, Nat.cast_ofNat] using hdiv
  have hne' : d * a - u * ((3 ^ r : ℕ) : ℤ) ≠ 0 := by
    simpa only [Nat.cast_pow, Nat.cast_ofNat] using hne
  have hg := rational_gap K (3 ^ r) a u d hdiv' hne'
  have hw : 1 ≤ weight r := weight_pos r
  have hm : 1 ≤ max 1 a.natAbs := le_max_left _ _
  have ha : a.natAbs ≤ weight r * max 1 a.natAbs := by
    calc
      a.natAbs ≤ max 1 a.natAbs := le_max_right _ _
      _ = 1 * max 1 a.natAbs := by omega
      _ ≤ weight r * max 1 a.natAbs := Nat.mul_le_mul_right _ hw
  have hp : 2 * 3 ^ r ≤ 3 * weight r * max 1 a.natAbs := by
    calc
      2 * 3 ^ r ≤ 3 * weight r := power_weight_bound r
      _ = 3 * weight r * 1 := by omega
      _ ≤ 3 * weight r * max 1 a.natAbs := Nat.mul_le_mul_left _ hm
  have hda := Nat.mul_le_mul_left (2 * d.natAbs) ha
  have hup := Nat.mul_le_mul_left u.natAbs hp
  nlinarith

theorem forced_weight_growth (g : ℕ → ℕ)
    (hstep : ∀ j, (1 + 3 ^ j) * g j ≤ 4 * g (j + 1)) (r : ℕ) :
    weight r * g 0 ≤ 4 ^ r * g r := by
  induction r with
  | zero => simp [weight]
  | succ r ih =>
      calc
        weight (r + 1) * g 0 = (1 + 3 ^ r) * (weight r * g 0) := by
          rw [weight]
          ring
        _ ≤ (1 + 3 ^ r) * (4 ^ r * g r) := Nat.mul_le_mul_left _ ih
        _ = 4 ^ r * ((1 + 3 ^ r) * g r) := by ring
        _ ≤ 4 ^ r * (4 * g (r + 1)) := Nat.mul_le_mul_left _ (hstep r)
        _ = 4 ^ (r + 1) * g (r + 1) := by
          rw [pow_succ]
          ring

end CollatzWeightedSelector
