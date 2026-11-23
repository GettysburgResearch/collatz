import Mathlib.Data.Nat.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
Finite arithmetic core of ARITHMETIC_MINIMUM.md, Sections 4--5.
The physical source identities imply a nonzero carry difference divisible by
2 * 3^(i+l); the unrestricted positive-gap carry range supplies hbound.
Those source and word facts are explicit parameters here, not axioms.
-/

namespace CollatzWholeSource.ArithmeticRepair

/-- A nonzero integral same-clock window repair needs this excess clock. -/
theorem repair_excess_clock
    (i l e d : ℕ) (hl : 0 < l) (hd : 0 < d)
    (hdiv : 2 * 3 ^ (i + l) ∣ d)
    (hbound : d ≤ 2 * (2 ^ e - 1) * (3 ^ (l - 1) - 2 ^ (l - 1))) :
    3 ^ (i + 1) < 2 ^ e := by
  have hmin : 2 * 3 ^ (i + l) ≤ d := Nat.le_of_dvd hd hdiv
  have hpow : 0 < (3 : ℕ) ^ (l - 1) := by positivity
  have hsub : 2 ^ e - 1 < 2 ^ e := Nat.sub_lt (by positivity) (by decide)
  have hrough : d < 2 * 2 ^ e * 3 ^ (l - 1) := by
    calc
      d ≤ 2 * (2 ^ e - 1) * (3 ^ (l - 1) - 2 ^ (l - 1)) := hbound
      _ ≤ 2 * (2 ^ e - 1) * 3 ^ (l - 1) :=
        Nat.mul_le_mul_left _ (Nat.sub_le _ _)
      _ < 2 * 2 ^ e * 3 ^ (l - 1) :=
        Nat.mul_lt_mul_of_pos_right
          (Nat.mul_lt_mul_of_pos_left hsub (by decide)) hpow
  have hexp : i + l = (l - 1) + (i + 1) := by omega
  have hproduct : (2 * 3 ^ (l - 1)) * 3 ^ (i + 1) <
      (2 * 3 ^ (l - 1)) * 2 ^ e := by
    calc
      (2 * 3 ^ (l - 1)) * 3 ^ (i + 1) = 2 * 3 ^ (i + l) := by
        rw [hexp, pow_add]
        ring
      _ ≤ d := hmin
      _ < 2 * 2 ^ e * 3 ^ (l - 1) := hrough
      _ = (2 * 3 ^ (l - 1)) * 2 ^ e := by ring
  exact Nat.lt_of_mul_lt_mul_left hproduct

/-- The excess-clock inequality and actual prefix expansion force a long span.
Here the window total is l+e, and A is the unchanged prefix clock. -/
theorem repair_span_power
    (i l e A : ℕ) (hl : 0 < l) (hprefix : i ≤ A)
    (hexcess : 3 ^ (i + 1) < 2 ^ e)
    (hexpansion : 2 ^ (A + l + e) < 3 ^ (i + l)) :
    2 ^ (i + l) < 3 ^ (l - 1) := by
  have hpow2 : 0 < (2 : ℕ) ^ (i + l) := by positivity
  have hclock : 2 ^ (i + l + e) < 3 ^ (i + l) := by
    calc
      2 ^ (i + l + e) ≤ 2 ^ (A + l + e) := by
        exact Nat.pow_le_pow_right (by decide) (by omega)
      _ < 3 ^ (i + l) := hexpansion
  have hcombined : 3 ^ (i + 1) * 2 ^ (i + l) < 3 ^ (i + l) := by
    calc
      3 ^ (i + 1) * 2 ^ (i + l) < 2 ^ e * 2 ^ (i + l) :=
        Nat.mul_lt_mul_of_pos_right hexcess hpow2
      _ = 2 ^ (i + l + e) := by rw [← pow_add]; congr 1; omega
      _ < 3 ^ (i + l) := hclock
  have hlid : l = (l - 1) + 1 := by omega
  have hthree : (3 : ℕ) ^ l = 3 ^ (l - 1) * 3 := by
    nth_rewrite 1 [hlid]
    rw [pow_succ]
  have hcancel : (3 ^ i * 3) * 2 ^ (i + l) <
      (3 ^ i * 3) * 3 ^ (l - 1) := by
    calc
      (3 ^ i * 3) * 2 ^ (i + l) = 3 ^ (i + 1) * 2 ^ (i + l) := by
        rw [pow_succ]
      _ < 3 ^ (i + l) := hcombined
      _ = (3 ^ i * 3) * 3 ^ (l - 1) := by
        rw [pow_add, hthree]
        ring
  exact Nat.lt_of_mul_lt_mul_left hcancel

/-- Composition of the actual repair range with the prefix coefficient bound. -/
theorem nonlocal_integral_repair
    (i l e A d : ℕ) (hl : 0 < l) (hd : 0 < d) (hprefix : i ≤ A)
    (hdiv : 2 * 3 ^ (i + l) ∣ d)
    (hbound : d ≤ 2 * (2 ^ e - 1) * (3 ^ (l - 1) - 2 ^ (l - 1)))
    (hexpansion : 2 ^ (A + l + e) < 3 ^ (i + l)) :
    2 ^ (i + l) < 3 ^ (l - 1) := by
  exact repair_span_power i l e A hl hprefix
    (repair_excess_clock i l e d hl hd hdiv hbound) hexpansion

/-- A weaker simple span consequence, avoiding real logarithms. -/
theorem repair_span_exceeds_prefix
    (i l : ℕ) (hspan : 2 ^ (i + l) < 3 ^ (l - 1)) :
    i + 1 < l := by
  by_contra h
  have hli : l ≤ i + 1 := by omega
  have hexp : 2 * (l - 1) ≤ i + l := by omega
  have hleft : (3 : ℕ) ^ (l - 1) ≤ 2 ^ (i + l) := by
    calc
      3 ^ (l - 1) ≤ 4 ^ (l - 1) :=
        Nat.pow_le_pow_left (by decide : 3 ≤ 4) (l - 1)
      _ = 2 ^ (2 * (l - 1)) := by rw [pow_mul]; norm_num
      _ ≤ 2 ^ (i + l) := Nat.pow_le_pow_right (by decide) hexp
  omega

end CollatzWholeSource.ArithmeticRepair
