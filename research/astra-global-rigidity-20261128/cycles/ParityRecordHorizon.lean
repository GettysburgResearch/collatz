import MersenneCrests
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace Collatz.ParityRecordHorizon

open Collatz.MersenneCrests (State run next)

private def evenAt (z : State) (t : Nat) : Prop := (run z t).1 % 2 = 0
private instance (z : State) (t : Nat) : Decidable (evenAt z t) := by
  unfold evenAt
  infer_instance

def odds (z : State) : Nat → Nat
  | 0 => 0
  | t+1 => if evenAt z t then odds z t else odds z t + 1

def grade (z : State) (t : Nat) : Int := 2*(odds z t : Int) - (t : Int)

def reflected (z : State) : Nat → Nat
  | 0 => 0
  | t+1 => if evenAt z t then reflected z t - 1 else reflected z t + 1

def correction (z : State) : Nat → ℚ
  | 0 => 0
  | t+1 => if evenAt z t then correction z t/2 else (3*correction z t+1)/2

private theorem grade_even (z : State) (t : Nat) (he : evenAt z t) :
    grade z (t+1) = grade z t-1 := by
  simp only [grade, odds, ite_eq_left he, Nat.cast_add, Nat.cast_one]
  ring

private theorem grade_odd (z : State) (t : Nat) (ho : ¬evenAt z t) :
    grade z (t+1) = grade z t+1 := by
  simp only [grade, odds, ite_eq_right ho, Nat.cast_add, Nat.cast_one]
  ring

/-- The reflected counter is an actual difference from a preceding grade. -/
theorem reflected_witness (z : State) (t : Nat) :
    ∃ k ≤ t, grade z k + (reflected z t : Int) = grade z t := by
  induction t with
  | zero => exact ⟨0, Nat.le_refl _, by simp [reflected]⟩
  | succ t ih =>
    obtain ⟨k, hk, hgrade⟩ := ih
    by_cases he : evenAt z t
    · rw [reflected, ite_eq_left he]
      cases hh : reflected z t with
      | zero => exact ⟨t+1, Nat.le_refl _, by simp⟩
      | succ h =>
        refine ⟨k, by omega, ?_⟩
        rw [grade_even z t he]
        rw [hh] at hgrade
        omega
    · refine ⟨k, by omega, ?_⟩
      rw [reflected, ite_eq_right he, grade_odd z t he]
      omega

theorem weak_record_reflected_zero (z : State) (t : Nat)
    (record : ∀ k ≤ t, grade z t ≤ grade z k) : reflected z t = 0 := by
  obtain ⟨k, hk, hw⟩ := reflected_witness z t
  have h := record k hk
  omega

/-- A finite word bound on the exact additive error at every native date. -/
theorem correction_envelope (z : State) (t : Nat) :
    correction z t < (2 : ℚ)^(reflected z t) := by
  induction t with
  | zero => norm_num [correction, reflected]
  | succ t ih =>
    by_cases he : evenAt z t
    · rw [correction, reflected, ite_eq_left he, ite_eq_left he]
      cases hh : reflected z t with
      | zero =>
        rw [hh] at ih
        norm_num at ih ⊢
        linarith
      | succ h =>
        rw [hh, pow_succ] at ih
        simp only [Nat.succ_sub_one]
        linarith
    · rw [correction, reflected, ite_eq_right he, ite_eq_right he, pow_succ]
      have hp : (1 : ℚ) ≤ 2^(reflected z t) := one_le_pow₀ (by norm_num)
      linarith

theorem weak_record_correction (z : State) (t : Nat)
    (record : ∀ k ≤ t, grade z t ≤ grade z k) : correction z t < 1 := by
  simpa [weak_record_reflected_zero z t record] using correction_envelope z t

theorem strict_record_correction (z : State) (t : Nat)
    (record : ∀ k ≤ t, grade z (t+1) < grade z k) :
    2*correction z (t+1) < 1 := by
  have he : evenAt z t := by
    by_contra ho
    have hr := record t (Nat.le_refl _)
    rw [grade_odd z t ho] at hr
    omega
  have hprev : ∀ k ≤ t, grade z t ≤ grade z k := by
    intro k hk
    have hr := record k hk
    rw [grade_even z t he] at hr
    omega
  have hc := weak_record_correction z t hprev
  rw [correction, ite_eq_left he]
  linarith

private theorem observed_step_even (z : State) (he : z.1 % 2 = 0) :
    (2 : ℚ)*((next z).1 : ℚ) = (z.1 : ℚ) := by
  have h : 2*(next z).1 = z.1 := by simp only [next, ite_eq_left he]; omega
  exact_mod_cast h

private theorem observed_step_odd (z : State) (ho : z.1 % 2 ≠ 0) :
    (2 : ℚ)*((next z).1 : ℚ) = 3*(z.1 : ℚ)+1 := by
  have h : 2*(next z).1 = 3*z.1+1 := by simp only [next, ite_eq_right ho]; omega
  exact_mod_cast h

/-- The correction is the additive part of the observed native trajectory. -/
theorem observed_affine (z : State) (t : Nat) :
    (2 : ℚ)^t*((run z t).1 : ℚ) =
      (3 : ℚ)^(odds z t)*(z.1 : ℚ)+(2 : ℚ)^t*correction z t := by
  induction t with
  | zero => simp [run, odds, correction]
  | succ t ih =>
    calc
      _ = (2 : ℚ)^t*(2*((next (run z t)).1 : ℚ)) := by rw [run, pow_succ]; ring
      _ = _ := by
        by_cases he : evenAt z t
        · rw [observed_step_even (run z t) he, ih, odds, correction,
              ite_eq_left he, ite_eq_left he, pow_succ]
          ring
        · rw [observed_step_odd (run z t) he, odds, correction,
              ite_eq_right he, ite_eq_right he, pow_succ, pow_succ]
          linear_combination 3*ih

private theorem positive_run (z : State) (hz : 0 < z.1) (t : Nat) :
    0 < (run z t).1 := by
  induction t with
  | zero => exact hz
  | succ t ih =>
    by_cases he : (run z t).1 % 2 = 0
    · simp only [run, next, ite_eq_left he]; omega
    · simp only [run, next, ite_eq_right he]; omega

/-- Exact integer cutoff at a supplied first strict record. -/
theorem strict_record_clock (z : State) (hz : 0 < z.1) (t : Nat)
    (record : ∀ k ≤ t, grade z (t+1) < grade z k) :
    2^(t+1) < 2*3^(odds z (t+1))*z.1 := by
  have hc := strict_record_correction z t record
  have ha := observed_affine z (t+1)
  have hy : (1 : ℚ) ≤ ((run z (t+1)).1 : ℚ) := by
    exact_mod_cast positive_run z hz (t+1)
  have hp : (0 : ℚ) < 2^(t+1) := by positivity
  have hsmall := mul_lt_mul_of_pos_left hc hp
  have hlarge := mul_le_mul_of_nonneg_left hy (le_of_lt hp)
  have hfinal : (2 : ℚ)^(t+1) < 2*3^(odds z (t+1))*(z.1 : ℚ) := by
    nlinarith [hsmall, hlarge, ha]
  exact_mod_cast hfinal

end Collatz.ParityRecordHorizon
