module

public import Mathlib.Data.Nat.Choose.Sum
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring

/-! The chronological-word carry signatures used in O8 and the exact
finite-binomial average in O9. This module has no operator-theory assumptions. -/
@[expose] public section

namespace OrdinaryOperatorCarry

def odds : List Bool → ℕ
  | [] => 0
  | false :: w => odds w
  | true :: w => odds w + 1

def evens : List Bool → ℕ
  | [] => 0
  | false :: w => evens w + 1
  | true :: w => evens w

def carry : List Bool → ℕ
  | [] => 0
  | false :: w => 2 * carry w
  | true :: w => 3^(odds w) + 2 * carry w

def affineForward : List Bool → ℚ → ℚ
  | [], x => x
  | false :: w, x => affineForward w (x/2)
  | true :: w, x => affineForward w ((3*x+1)/2)

theorem chronological_carry (w : List Bool) (x : ℚ) :
    (2:ℚ)^w.length * affineForward w x = 3^(odds w)*x + (carry w : ℚ) := by
  induction w generalizing x with
  | nil => simp [affineForward, carry, odds]
  | cons b w ih =>
    cases b with
    | false =>
      simp only [List.length_cons, pow_succ, affineForward, odds, carry,
        Nat.cast_mul, Nat.cast_ofNat]
      nlinarith only [ih (x/2)]
    | true =>
      simp only [List.length_cons, pow_succ, affineForward, odds, carry,
        Nat.cast_add, Nat.cast_mul, Nat.cast_pow, Nat.cast_ofNat]
      nlinarith only [ih ((3*x+1)/2)]

theorem clock_split (w : List Bool) : odds w + evens w = w.length := by
  induction w with
  | nil => rfl
  | cons b w ih => cases b <;> simp [odds, evens] <;> omega

theorem carry_bound (w : List Bool) :
    carry w + 2^w.length ≤ 2^(evens w)*3^(odds w) := by
  induction w with
  | nil => decide
  | cons b w ih =>
    cases b with
    | false =>
      simp only [carry, odds, evens, List.length_cons, pow_succ]
      nlinarith only [ih]
    | true =>
      simp only [carry, odds, evens, List.length_cons, pow_succ]
      have hpow : 1 ≤ 2^(evens w) := Nat.one_le_pow _ _ (by decide)
      nlinarith only [ih, Nat.mul_le_mul_right (3^(odds w)) hpow]

theorem three_pow_odd (n : ℕ) : 3^n % 2 = 1 := by
  induction n with
  | zero => rfl
  | succ _ ih => rw [pow_succ]; omega

theorem signature_injective (w v : List Bool) (hl : w.length = v.length)
    (ho : odds w = odds v) (hc : carry w = carry v) : w = v := by
  induction w generalizing v with
  | nil => simpa using hl.symm
  | cons b w ih =>
    cases v with
    | nil => simp at hl
    | cons c v =>
      simp only [List.length_cons, Nat.succ.injEq] at hl
      cases b <;> cases c <;> simp only [carry, odds] at hc ho
      · exact congrArg (List.cons false) (ih v hl ho (by omega))
      · have h := three_pow_odd (odds v)
        omega
      · have h := three_pow_odd (odds w)
        omega
      · have ho' : odds w = odds v := by omega
        rw [ho'] at hc
        exact congrArg (List.cons true) (ih v hl ho' (by omega))

theorem carry_quotient_lt (w : List Bool) :
    carry w / 3^(odds w) < 2^(evens w) := by
  apply (Nat.div_lt_iff_lt_mul (by positivity : 0 < 3^(odds w))).2
  have h := carry_bound w
  have hpos : 0 < 2^w.length := by positivity
  omega

theorem fiber_quotient_injective (w v : List Bool) (hl : w.length = v.length)
    (ho : odds w = odds v)
    (hr : carry w % 3^(odds w) = carry v % 3^(odds v))
    (hq : carry w / 3^(odds w) = carry v / 3^(odds v)) : w = v := by
  apply signature_injective w v hl ho
  have hw := Nat.mod_add_div (carry w) (3^(odds w))
  have hv := Nat.mod_add_div (carry v) (3^(odds v))
  rw [hr, hq, ho] at hw
  exact hw.symm.trans hv

theorem integer_slope_mass (k : ℕ) :
    ∑ q ∈ Finset.range (k+1), 9^(k-q)*k.choose q = 10^k := by
  simpa using (add_pow (1:ℕ) 9 k).symm

theorem rational_slope_average (k : ℕ) :
    ∑ q ∈ Finset.range (k+1), ((2:ℚ)^k*(1/9)^q*(k.choose q)) = (20/9)^k := by
  have h := (add_pow (1/9:ℚ) 1 k).symm
  simp only [one_pow, mul_one] at h
  calc
    _ = (2:ℚ)^k * (∑ q ∈ Finset.range (k+1), (1/9:ℚ)^q*(k.choose q)) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro q _
      ring
    _ = _ := by rw [h, ← mul_pow]; norm_num

end OrdinaryOperatorCarry

#print axioms OrdinaryOperatorCarry.chronological_carry
#print axioms OrdinaryOperatorCarry.clock_split
#print axioms OrdinaryOperatorCarry.carry_bound
#print axioms OrdinaryOperatorCarry.three_pow_odd
#print axioms OrdinaryOperatorCarry.signature_injective
#print axioms OrdinaryOperatorCarry.carry_quotient_lt
#print axioms OrdinaryOperatorCarry.fiber_quotient_injective
#print axioms OrdinaryOperatorCarry.integer_slope_mass
#print axioms OrdinaryOperatorCarry.rational_slope_average
