import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

set_option autoImplicit false

namespace RelativeReset

/-- Exact odd paths. F is a lower bound on the shifted outputs of the resets.
    The five indices are the terminal odd state, odd clock, total valuation,
    number of resets and the accumulated nonnegative shifted correction. -/
inductive Path (F s : ℕ) : ℕ → ℕ → ℕ → ℕ → ℕ → Prop
  | nil (hs : Odd s) : Path F s s 0 0 0 0
  | ascent {x k A R E : ℕ} (p : Path F s x k A R E) (z : ℕ)
      (hz : Odd z) (edge : 2*z = 3*x+1) :
      Path F s z (k+1) (A+1) R (3*E)
  | reset {x k A R E : ℕ} (p : Path F s x k A R E) (z b : ℕ)
      (hz : Odd z) (edge : 2^(b+2)*z = 3*x+1) (floor : F ≤ z+1) :
      Path F s z (k+1) (A+(b+2)) (R+1) (3*E+2^A*(2^(b+2)-2))

/-- The positive bank, the reciprocal floor budget and exact nonvanishing. -/
theorem path_budget {F s z k A R E : ℕ} (p : Path F s z k A R E) :
    2^A*(z+1) = 3^k*(s+1)+E ∧
    F*E ≤ R*(2^A*(z+1)) ∧ (0 < E ↔ 0 < R) := by
  induction p with
  | nil hs => simp
  | @ascent x k A R E p z hz edge ih =>
    obtain ⟨hbank, hbudget, hpos⟩ := ih
    have expansion : 2^(A+1)*(z+1) = 3*(2^A*(x+1)) := by
      rw [pow_succ]
      nlinarith only [congrArg (fun j : ℕ => (2^A)*j) edge]
    rw [expansion]
    refine ⟨?_, ?_, ?_⟩
    · rw [hbank, pow_succ]
      ring
    · nlinarith only [hbudget]
    · omega
  | @reset x k A R E p z b hz edge floor ih =>
    obtain ⟨hbank, hbudget, _⟩ := ih
    let d := 2^(b+2)
    have hd : 4 ≤ d := by
      exact Nat.pow_le_pow_right (by decide : 0 < 2) (show 2 ≤ b+2 by omega)
    have dh : d-2+2 = d := by omega
    have ha : 0 < 2^A := Nat.pow_pos (by decide)
    have add : 2^(A+(b+2))*(z+1) = 3*(2^A*(x+1))+2^A*(d-2) := by
      rw [pow_add]
      change (2^A*d)*(z+1) = _
      change d*z = 3*x+1 at edge
      nlinarith only [congrArg (fun j : ℕ => (2^A)*j) edge,
        congrArg (fun j : ℕ => (2^A)*j) dh]
    have mono : 3*(2^A*(x+1)) ≤ 2^(A+(b+2))*(z+1) := by rw [add]; omega
    have paid : F*(2^A*(d-2)) ≤ 2^(A+(b+2))*(z+1) := by
      rw [pow_add]
      calc
        F * (2^A * (d-2)) ≤ (z+1) * (2^A * (d-2)) :=
          Nat.mul_le_mul_right _ floor
        _ ≤ (z+1) * (2^A * d) := by gcongr; omega
        _ = (2^A * 2^(b+2))*(z+1) := by dsimp [d]; ring
    change _ ∧ F*(3*E+2^A*(d-2)) ≤ (R+1)*_ ∧ _
    refine ⟨?_, ?_, ?_⟩
    · rw [add, hbank, pow_succ]
      dsimp [d]
      ring
    · nlinarith only [hbudget, paid, Nat.mul_le_mul_left R mono]
    · change (0 < 3*E+2^A*(d-2) ↔ 0 < R+1)
      have hcorr := Nat.mul_pos ha (show 0 < d-2 by omega)
      omega

/-- One complete block from 2^t*w-1 ends at z with 2^b*z+1=3^t*w.
    Every common positive odd divisor of the input's odd core and z+1
    divides 2^b-1, even when that divisor includes three. -/
theorem one_reset_divisor {t w b z g : ℕ}
    (edge : 2^b*z+1 = 3^t*w)
    (hw : g ∣ w) (hz : g ∣ z+1) : g ∣ 2^b-1 := by
  have hn : 0 < 2^b := Nat.pow_pos (by decide)
  have hs : 2^b*(z+1) = 3^t*w+(2^b-1) := by
    have sub : 2^b-1+1=2^b := by omega
    nlinarith only [edge, sub]
  have hleft : g ∣ 2^b*(z+1) := dvd_mul_of_dvd_right hz _
  rw [hs] at hleft
  exact (Nat.dvd_add_right (dvd_mul_of_dvd_right hw _)).mp hleft

/-- The integer inequalities behind z < ((2^t*w)/g)^(log_2 3). -/
theorem one_reset_size {t w b z g : ℕ}
    (hb : 0 < b) (hwpos : 0 < w) (hzpos : 0 < z)
    (edge : 2^b*z+1 = 3^t*w) (hw : g ∣ w) (hz : g ∣ z+1) :
    2^t*g ≤ 2^t*w ∧ g*z < 3^t*w := by
  have hg := one_reset_divisor edge hw hz
  have hp : 1 < 2^b := Nat.one_lt_pow (by omega) (by decide)
  have hgd := Nat.le_of_dvd (show 0 < 2^b-1 by omega) hg
  refine ⟨Nat.mul_le_mul_left _ (Nat.le_of_dvd hwpos hw), ?_⟩
  have hh := Nat.mul_lt_mul_of_pos_right (show g < 2^b by omega) hzpos
  omega

/-- An integer version for every rational upper approximation m/d to log₂ 3.
    Taking m=8,d=5 already gives z^5*g^8 < (2^t*w)^8. -/
theorem one_reset_power_bound {t w b z g d m : ℕ}
    (hb : 0 < b) (hwpos : 0 < w) (hzpos : 0 < z) (hgpos : 0 < g)
    (edge : 2^b*z+1 = 3^t*w) (hw : g ∣ w) (hz : g ∣ z+1)
    (hd : 0 < d) (hm : d ≤ m) (hbase : 3^d ≤ 2^m) :
    z^d*g^m < (2^t*w)^m := by
  obtain ⟨_, hlt⟩ := one_reset_size hb hwpos hzpos edge hw hz
  have hwle := Nat.le_of_dvd hwpos hw
  obtain ⟨j, rfl⟩ := Nat.exists_eq_add_of_le hm
  have hp := Nat.pow_lt_pow_left hlt (by omega : d ≠ 0)
  have htimes := Nat.mul_lt_mul_of_pos_right hp (Nat.pow_pos (n := j) hgpos)
  have hcmp : (3^t)^d ≤ (2^t)^(d+j) := by
    rw [← pow_mul, Nat.mul_comm t d, pow_mul, ← pow_mul (2 : ℕ),
      Nat.mul_comm t (d+j), pow_mul]
    exact Nat.pow_le_pow_left hbase t
  calc
    z^d*g^(d+j) = (g*z)^d*g^j := by rw [pow_add, mul_pow]; ring
    _ < (3^t*w)^d*g^j := htimes
    _ ≤ ((2^t)^(d+j)*w^d)*w^j := by
      rw [mul_pow]
      exact Nat.mul_le_mul (Nat.mul_le_mul_right _ hcmp) (Nat.pow_le_pow_left hwle _)
    _ = (2^t*w)^(d+j) := by rw [mul_pow, pow_add w]; ring

#print axioms path_budget
#print axioms one_reset_divisor
#print axioms one_reset_size
#print axioms one_reset_power_bound

end RelativeReset
