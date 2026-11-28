import CofactorDescent
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-! Native finite shortcut blocks and a digit-window carry after an arbitrary cut. -/
set_option autoImplicit false
set_option warningAsError true
namespace Collatz.NativeWindowBlock

open CoreBranching Collatz.CofactorDescent

private theorem step_lift (u x : ℕ) :
    step (2 * u + x) = 3 ^ (x % 2) * u + step x := by
  have hp : (2 * u + x) % 2 = x % 2 := by omega
  by_cases h : x % 2 = 0
  · simp only [step, hp, h, ite_true, pow_zero, one_mul]
    omega
  · have he : x % 2 = 1 := by omega
    simp only [step, hp, he, one_ne_zero, ite_false, pow_one]
    omega

/-- The represented dyadic residue supplies both the actual count and endpoint. -/
theorem block_lift (s a q : ℕ) :
    odds s (2 ^ s * q + a) = odds s a ∧
    run s (2 ^ s * q + a) = 3 ^ odds s a * q + run s a := by
  induction s generalizing a q with
  | zero => simp [odds, run]
  | succ s ih =>
    have h : 2 ^ (s + 1) * q + a = 2 * (2 ^ s * q) + a := by rw [pow_succ]; ring
    have hstep : step (2 ^ (s + 1) * q + a) =
        2 ^ s * (3 ^ (a % 2) * q) + step a := by rw [h, step_lift]; ring
    have htag : (2 ^ (s + 1) * q + a) % 2 = a % 2 := by rw [h]; omega
    obtain ⟨hcount, hend⟩ := ih (step a) (3 ^ (a % 2) * q)
    constructor
    · simp only [odds, hstep, htag, hcount]
    · change run s (step (2 ^ (s + 1) * q + a)) =
          3 ^ (a % 2 + odds s (step a)) * q + run s (step a)
      rw [hstep, hend, pow_add]
      ring

/-- The bottom block has room for the literal endpoint in exactly `odds s a` trits. -/
theorem endpoint_below (s a B : ℕ) (ha : a < 2 ^ s * B) :
    run s a < 3 ^ odds s a * B := by
  induction s generalizing a B with
  | zero => simpa [run, odds] using ha
  | succ s ih =>
    have hcap : 2 ^ (s + 1) * B = 2 * (2 ^ s * B) := by rw [pow_succ]; ring
    rw [hcap] at ha
    have hs : step a < 2 ^ s * (3 ^ (a % 2) * B) := by
      by_cases h : a % 2 = 0
      · simp only [step, h, ite_true, pow_zero, one_mul]
        omega
      · have he : a % 2 = 1 := by omega
        simp only [step, he, one_ne_zero, ite_false, pow_one]
        have heq : 2 ^ s * (3 * B) = 3 * (2 ^ s * B) := by ring
        rw [heq]
        omega
    have later := ih (step a) (3 ^ (a % 2) * B) hs
    simpa only [run, odds, pow_add, Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm] using later

/-- At a cut of width `g`, the quotient trits and the low remainder determine the
entire native input-window arc, including its carry in `[0,m)`. -/
theorem cut_arc (m a q g w : ℕ) (ha : a < m) (hg : 0 < g) (hw : 0 < w) :
    (m * q + a) / g % (m * w) = m * (q / g % w) + (m * (q % g) + a) / g ∧
    (m * (q % g) + a) / g < m := by
  have low : m * (q % g) + a < g * m := by
    have t := Nat.mul_le_mul_left m (show q % g + 1 ≤ g by have h := Nat.mod_lt q hg; omega)
    nlinarith
  have hc : (m * (q % g) + a) / g < m := (Nat.div_lt_iff_lt_mul hg).2 (by simpa [Nat.mul_comm] using low)
  have sep : m * q + a = g * (m * (q / g)) + (m * (q % g) + a) := by
    calc
      _ = m * (g * (q / g) + q % g) + a := by rw [Nat.div_add_mod]
      _ = _ := by ring
  rw [sep, Nat.mul_add_div hg]
  refine ⟨?_, hc⟩
  have upper : m * (q / g % w) + (m * (q % g) + a) / g < m * w := by
    have t := Nat.mul_le_mul_left m (show q / g % w + 1 ≤ w by have h := Nat.mod_lt (q / g) hw; omega)
    nlinarith
  have normalized : m * (q / g) + (m * (q % g) + a) / g =
      (m * w) * (q / g / w) + (m * (q / g % w) + (m * (q % g) + a) / g) := by
    conv_lhs => lhs; rhs; rw [← Nat.div_add_mod (q / g) w]
    ring
  rw [normalized, Nat.mul_add_mod, Nat.mod_eq_of_lt upper]

#print axioms block_lift
#print axioms endpoint_below
#print axioms cut_arc
end Collatz.NativeWindowBlock
