import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Reciprocals of the least nonnegative representatives of exact dyadic
valuation siblings. The natural reciprocal of zero is zero in ℚ. -/
namespace EscapeHarmonicBirth

def siblings : List Bool → List ℕ
  | [] => []
  | false :: bits => 1 :: (siblings bits).map (fun j => 2*j)
  | true :: bits => 0 :: (siblings bits).map (fun j => 2*j+1)

def total (f : ℕ → ℚ) : List ℕ → ℚ
  | [] => 0
  | j :: js => f j + total f js

def invNat (j : ℕ) : ℚ := (j : ℚ)⁻¹
def zeroFlag (j : ℕ) : ℚ := if j = 0 then 1 else 0

theorem double_inv (j : ℕ) : invNat (2*j) = invNat j / 2 := by
  simp [invNat, Nat.cast_mul, div_eq_mul_inv, mul_comm]

theorem odd_inv (j : ℕ) : invNat (2*j+1) ≤ zeroFlag j + invNat j / 2 := by
  by_cases hj : j = 0
  · simp [hj, zeroFlag, invNat]
  · have hpos : 0 < (2*j : ℚ) := by positivity
    have h := one_div_le_one_div_of_le hpos (show (2*j : ℚ) ≤ 2*j+1 by linarith)
    simpa [zeroFlag, hj, invNat, one_div, div_eq_mul_inv, mul_comm] using h

theorem even_inv_total (js : List ℕ) :
    total invNat (js.map (fun j => 2*j)) = total invNat js / 2 := by
  induction js with
  | nil => simp [total]
  | cons j js ih =>
    simp only [List.map_cons, total, double_inv, ih]
    ring

theorem odd_inv_total (js : List ℕ) :
    total invNat (js.map (fun j => 2*j+1)) ≤ total zeroFlag js + total invNat js / 2 := by
  induction js with
  | nil => simp [total]
  | cons j js ih =>
    simp only [List.map_cons, total]
    linarith [odd_inv j]

theorem even_flag_total (js : List ℕ) :
    total zeroFlag (js.map (fun j => 2*j)) = total zeroFlag js := by
  induction js with
  | nil => rfl
  | cons j js ih => simp [total, zeroFlag, ih]

theorem odd_flag_total (js : List ℕ) :
    total zeroFlag (js.map (fun j => 2*j+1)) = 0 := by
  induction js with
  | nil => rfl
  | cons j js ih => simp [total, zeroFlag, ih]

theorem sibling_bounds (bits : List Bool) :
    total zeroFlag (siblings bits) ≤ 1 ∧ total invNat (siblings bits) ≤ 2 := by
  induction bits with
  | nil => norm_num [siblings, total]
  | cons bit bits ih =>
    rcases ih with ⟨hz, hm⟩
    cases bit with
    | false =>
      simp only [siblings, total, even_flag_total, even_inv_total]
      norm_num [zeroFlag, invNat]
      constructor <;> linarith
    | true =>
      simp only [siblings, total, odd_flag_total]
      norm_num [zeroFlag, invNat]
      linarith [odd_inv_total (siblings bits)]

/-- The legal next-letter reserve for d+7=4k+r, indexed from e=1. -/
def debtRow (k : ℕ) (r : ℚ) : ℚ :=
  ∑ i ∈ Finset.range k, (1/2 : ℚ)^(i+1) * (4*(k:ℚ)+r+8-4*((i:ℚ)+1))

theorem debtRow_succ (k : ℕ) (r : ℚ) :
    debtRow (k+1) r = ((4*(k:ℚ)+r+8) + debtRow k r)/2 := by
  calc
    debtRow (k+1) r =
        (∑ i ∈ Finset.range k, (1/2 : ℚ) *
          ((1/2 : ℚ)^(i+1) * (4*(k:ℚ)+r+8-4*((i:ℚ)+1)))) +
            (1/2 : ℚ) * (4*(k:ℚ)+r+8) := by
      simp only [debtRow, Finset.sum_range_succ', Nat.cast_succ]
      congr 1
      · apply Finset.sum_congr rfl
        intro i hi
        rw [pow_succ (1/2 : ℚ) (i+1)]
        ring
      · norm_num
        ring
    _ = _ := by rw [← Finset.mul_sum, debtRow]; ring

theorem debtRow_closed (k : ℕ) (r : ℚ) :
    debtRow k r = 4*(k:ℚ)+r-r*(1/2 : ℚ)^k := by
  induction k with
  | zero => simp [debtRow]
  | succ k ih =>
    rw [debtRow_succ, ih, pow_succ, Nat.cast_succ]
    ring

theorem exact_reserve_drift (d k r : ℕ) (hsplit : d+7 = 4*k+r) :
    1 + debtRow k r = (d:ℚ)+8-(r:ℚ)*(1/2 : ℚ)^k := by
  have h : (d:ℚ)+7 = 4*(k:ℚ)+r := by exact_mod_cast hsplit
  rw [debtRow_closed]
  linarith

theorem augmented_monotone (J J' B reserve reserve' : ℚ)
    (hb : J' ≤ J+B) (hr : B+reserve' ≤ reserve) :
    J'+reserve' ≤ J+reserve := by linarith

theorem centered_cutoff (atom envelope bound : ℚ)
    (ha : 0 < atom) (hsmall : atom ≤ bound) (hupper : 1/atom ≤ envelope)
    (hcert : envelope < 1/bound) : False := by
  linarith [one_div_le_one_div_of_le ha hsmall]

theorem minimum_gate_comparison : (10 : ℕ)^4 < 2^7 * 3^4 := by decide +kernel
theorem rational_chernoff_comparison : (7 : ℕ)^7 * 64^4 < 8^4 * 6^3 * 63^4 := by decide +kernel

#print axioms sibling_bounds
#print axioms exact_reserve_drift
#print axioms augmented_monotone
#print axioms centered_cutoff
#print axioms minimum_gate_comparison
#print axioms rational_chernoff_comparison
end EscapeHarmonicBirth
