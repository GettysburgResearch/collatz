import Mathlib.Data.Nat.Log
import Mathlib.Algebra.Order.Monoid.Unbundled.Pow
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Finite interfaces for the critical binary gate at log base 3 of 2. -/
set_option autoImplicit false
set_option warningAsError true

namespace EscapeCriticalSourceSector

def criticalGrade (n : ℕ) : ℕ := Nat.clog 3 (2^n)

theorem criticalGrade_spec (n g : ℕ) :
    criticalGrade n ≤ g ↔ 2^n ≤ 3^g :=
  Nat.clog_le_iff_le_pow (by decide)

theorem criticalDen_interval (n : ℕ) :
    2^n ≤ 3^(criticalGrade n) ∧ 3^(criticalGrade n) < 3*2^n := by
  constructor
  · exact (criticalGrade_spec n _).mp (le_refl _)
  · cases n with
    | zero => decide
    | succ n =>
      have x : 1 < (2:ℕ)^(n+1) := one_lt_pow₀ (by decide) (by omega)
      have h : 0 < criticalGrade (n+1) := by
        apply (Nat.lt_clog_iff_pow_lt (by decide : 1 < 3)).2
        simp [x]
      have hp := Nat.pow_pred_clog_lt_self (by decide : 1 < 3) x
      change 3^(criticalGrade (n+1)-1) < 2^(n+1) at hp
      calc
        3 ^ criticalGrade (n+1) = 3 * 3^(criticalGrade (n+1)-1) := by
          conv_lhs => rw [← Nat.sub_add_cancel (show 1 ≤ criticalGrade (n+1) by omega)]
          rw [pow_succ, Nat.mul_comm]
        _ < 3 * 2^(n+1) := Nat.mul_lt_mul_of_pos_left hp (by decide)

/-- A successive running floor for the multiplier gives an exact critical
suffix, with no roundoff or real-log gate in the test. -/
theorem gate_after_minimum (i g u v : ℕ)
    (h : 3^g*2^(i+u) ≤ 3^(g+v)*2^i) : 2^u ≤ 3^v := by
  rw [pow_add, pow_add] at h
  have h' : (3^g*2^i)*2^u ≤ (3^g*2^i)*3^v := by
    calc
      _ = 3^g*(2^i*2^u) := by ring
      _ ≤ 3^g*3^v*2^i := h
      _ = _ := by ring
  exact Nat.le_of_mul_le_mul_left h' (by positivity)

/-- A positive affine intercept on a positive integer lap forces
its multiplicative gain to be strictly smaller than one. -/
theorem strict_cycle_gain (a h g c : ℕ) (hc : 0<c)
    (lap : 2^h*a=3^g*a+c) : 3^g<2^h := by
  by_contra! hle
  have _ := Nat.mul_le_mul_right a hle
  omega

/-- Positive fixed slack is exhausted by iterating a strict cycle gain. -/
theorem laps_exhaust_slack (a b s : ℕ) (ha : 0<a) (hab : a<b) :
    ∃ k : ℕ, s*a^k < b^k := by
  have lower (k : ℕ) : (a+k+1)*a^k ≤ b^(k+1) := by
    induction k with
    | zero => simp; omega
    | succ k ih =>
      have hbase : a*(a+k+2) ≤ (a+k+1)*b := by
        have hmul := Nat.mul_le_mul_left (a+k+1) (show a+1≤b by omega)
        nlinarith
      calc
        _ = (a*(a+k+2))*a^k := by rw [pow_succ]; ring
        _ ≤ ((a+k+1)*b)*a^k := Nat.mul_le_mul_right _ hbase
        _ = ((a+k+1)*a^k)*b := by ring
        _ ≤ b^(k+1)*b := Nat.mul_le_mul_right _ ih
        _ = _ := by rw [pow_succ b (k+1)]
  refine ⟨s*a+1, ?_⟩
  calc
    s*a^(s*a+1) = (s*a)*a^(s*a) := by rw [pow_succ]; ring
    _ < (a+s*a+1)*a^(s*a) := Nat.mul_lt_mul_of_pos_right (by omega) (pow_pos ha _)
    _ ≤ b^(s*a+1) := lower _

/-- A debt affordable by a critical prefix and the following source
is affordable on their full concatenation. -/
theorem critical_slack_join (t j G g d : ℕ)
    (bank : 2^t*d ≤ 3^G) (debt : 2^j ≤ d*3^g) :
    2^(t+j) ≤ 3^(G+g) := by
  rw [pow_add, pow_add]
  calc
    2^t*2^j ≤ 2^t*(d*3^g) := Nat.mul_le_mul_left _ debt
    _ = (2^t*d)*3^g := by ring
    _ ≤ 3^G*3^g := Nat.mul_le_mul_right _ bank

#print axioms criticalGrade_spec
#print axioms criticalDen_interval
#print axioms gate_after_minimum
#print axioms strict_cycle_gain
#print axioms laps_exhaust_slack
#print axioms critical_slack_join
end EscapeCriticalSourceSector
