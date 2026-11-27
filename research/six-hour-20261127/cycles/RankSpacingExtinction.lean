import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.NormNum

/-! Finite divisibility of positive arithmetic-progression spacings along a
common mechanical clock. Each edge may have its own even divisor. -/

namespace RankSpacingExtinction

theorem two_pow_dvd_start (t : Nat) (g q : Nat → Nat)
    (heven : ∀ i < t, 2 ∣ q i)
    (hstep : ∀ i < t, q i * g (i + 1) = 3 * g i) :
    2 ^ t ∣ g 0 := by
  induction t generalizing g q with
  | zero => simp
  | succ t ih =>
    have ht : 2 ^ t ∣ g 1 :=
      ih (fun i => g (i + 1)) (fun i => q (i + 1))
        (fun i hi => heven (i + 1) (by omega))
        (fun i hi => hstep (i + 1) (by omega))
    have hq := heven 0 (by omega)
    have hd : 2 ^ (t + 1) ∣ 3 * g 0 := by
      rw [← hstep 0 (by omega), pow_succ, Nat.mul_comm (2^t) 2]
      exact Nat.mul_dvd_mul hq ht
    have hc : (2 ^ (t + 1)).Coprime 3 :=
      (by decide : Nat.Coprime 2 3).pow_left (t + 1)
    exact hc.dvd_of_dvd_mul_left hd

theorem positive_spacing_lower_bound (t : Nat) (g q : Nat → Nat)
    (hg : 0 < g 0) (heven : ∀ i < t, 2 ∣ q i)
    (hstep : ∀ i < t, q i * g (i + 1) = 3 * g i) :
    2 ^ t ≤ g 0 :=
  Nat.le_of_dvd hg (two_pow_dvd_start t g q heven hstep)

theorem impossible_long_mechanical_run (t : Nat) (g q : Nat → Nat)
    (hg : 0 < g 0) (hsmall : g 0 < 2 ^ t)
    (hclock : ∀ i < t, q i = 2 ∨ q i = 4)
    (hstep : ∀ i < t, q i * g (i + 1) = 3 * g i) : False := by
  have hq : ∀ i < t, 2 ∣ q i := by
    intro i hi
    rcases hclock i hi with he | he <;> simp [he]
  exact (Nat.not_le_of_gt hsmall) (positive_spacing_lower_bound t g q hg hq hstep)

end RankSpacingExtinction

#print axioms RankSpacingExtinction.two_pow_dvd_start
#print axioms RankSpacingExtinction.positive_spacing_lower_bound
#print axioms RankSpacingExtinction.impossible_long_mechanical_run
