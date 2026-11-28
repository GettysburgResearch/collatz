import PadeArithmetic
import Mathlib.Algebra.Polynomial.Coeff
import Mathlib.Algebra.Ring.Parity
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

/-! Integer coefficients of the dyadic Padé interpolant for a positive clock. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.PadeCoefficients
open Collatz.PadeArithmetic
open Polynomial

/-- Signed coefficients after clearing precisely the largest possible power of two. -/
def coeffInt (h : ℕ) : ℕ → ℕ → ℤ
  | 0, 0 => 1
  | 0, _+1 => 0
  | _+1, 0 => 1
  | n+1, k+1 => 2^(h*(k+1))*coeffInt h n (k+1) -
      3^(h*(n+1))*coeffInt h n k

@[simp] theorem coeffInt_zero (h n : ℕ) : coeffInt h n 0=1 := by
  cases n <;> rfl

theorem coeffInt_vanish (h n k : ℕ) (hkn : n<k) : coeffInt h n k=0 := by
  induction n generalizing k with
  | zero => cases k <;> simp_all [coeffInt]
  | succ n ih =>
    cases k with
    | zero => omega
    | succ k =>
      simp only [coeffInt,ih k (by omega),ih (k+1) (by omega),mul_zero,sub_zero]

/-- Only one of the two recurrence terms is odd within the triangular support. -/
theorem coeffInt_odd (h n k : ℕ) (hh : 0<h) (hkn : k≤n) : Odd (coeffInt h n k) := by
  induction n generalizing k with
  | zero =>
    have hk : k=0 := by omega
    subst k
    simpa only [coeffInt_zero] using (odd_one : Odd (1:ℤ))
  | succ n ih =>
    cases k with
    | zero => simpa only [coeffInt_zero] using (odd_one : Odd (1:ℤ))
    | succ k =>
      have evenTerm : Even ((2:ℤ)^(h*(k+1))*coeffInt h n (k+1)) :=
        ((even_two : Even (2:ℤ)).pow_of_ne_zero (Nat.ne_of_gt (Nat.mul_pos hh (by omega)))).mul_right _
      have oddThree : Odd (3:ℤ) := ⟨1,by decide⟩
      exact evenTerm.sub_odd ((oddThree.pow.mul) (ih k (by omega)))

private theorem topInsert (n k : ℕ) (hkn : k≤n) :
    degreeIndex (n+1) (k+1)=degreeIndex n k+(n+1) := by
  have h := degreeIndex_succ_both n k (by omega)
  omega

theorem coeffInt_height (h n k : ℕ) :
    |coeffInt h n k|≤(n.choose k:ℤ)*3^(h*degreeIndex n k) := by
  induction n generalizing k with
  | zero =>
    cases k <;> simp [coeffInt,degreeIndex]
  | succ n ih =>
    cases k with
    | zero => simp [degreeIndex]
    | succ k =>
      by_cases hkn : k≤n
      · have top1 := degreeIndex_succ_same n (k+1) (by omega)
        have top2 := topInsert n k hkn
        have hp1 : (3:ℤ)^(h*(k+1))*3^(h*degreeIndex n (k+1)) =
            3^(h*degreeIndex (n+1) (k+1)) := by
          rw [← pow_add,top1]
          congr 1
          ring
        have hp2 : (3:ℤ)^(h*(n+1))*3^(h*degreeIndex n k) =
            3^(h*degreeIndex (n+1) (k+1)) := by
          rw [← pow_add,top2]
          congr 1
          ring
        have hb1 := mul_le_mul
          (pow_le_pow_left₀ (by decide : (0:ℤ)≤2) (by decide : (2:ℤ)≤3) (h*(k+1)))
          (ih (k+1)) (abs_nonneg _) (by positivity)
        have hb2 := mul_le_mul_of_nonneg_left (ih k) (by positivity : (0:ℤ)≤3^(h*(n+1)))
        calc
          |coeffInt h (n+1) (k+1)| ≤
              (2:ℤ)^(h*(k+1))*|coeffInt h n (k+1)|+
              3^(h*(n+1))*|coeffInt h n k| := by
                have ht := abs_add_le ((2:ℤ)^(h*(k+1))*coeffInt h n (k+1))
                    (-(3^(h*(n+1))*coeffInt h n k))
                simpa only [coeffInt,sub_eq_add_neg,abs_neg,abs_mul,abs_pow,
                  abs_of_nonneg (by decide : (0:ℤ)≤2),abs_of_nonneg (by decide : (0:ℤ)≤3)] using ht
          _ ≤ (3:ℤ)^(h*(k+1))*((n.choose (k+1):ℤ)*3^(h*degreeIndex n (k+1)))+
              3^(h*(n+1))*((n.choose k:ℤ)*3^(h*degreeIndex n k)) := add_le_add hb1 hb2
          _ = (n.choose (k+1):ℤ)*(3^(h*(k+1))*3^(h*degreeIndex n (k+1)))+
              (n.choose k:ℤ)*(3^(h*(n+1))*3^(h*degreeIndex n k)) := by ring
          _ = _ := by rw [hp1,hp2,Nat.choose_succ_succ',Nat.cast_add]; ring
      · rw [coeffInt_vanish h (n+1) (k+1) (by omega),abs_zero]
        positivity

private theorem poly_zero_coeff (n : ℕ) (q : ℚ) : (padePoly n q).coeff 0=1 := by
  induction n with
  | zero => simp [padePoly]
  | succ n ih =>
    rw [padePoly_succ,mul_sub,mul_one,← mul_assoc,coeff_sub,coeff_mul_X_zero,sub_zero,ih]

private theorem poly_next_coeff (n k : ℕ) (q : ℚ) :
    (padePoly (n+1) q).coeff (k+1) =
      (padePoly n q).coeff (k+1)-(padePoly n q).coeff k*q^(n+1) := by
  simp only [padePoly_succ,mul_sub,mul_one,← mul_assoc,coeff_sub,
    coeff_mul_X,coeff_mul_C]

/-- Exact scaling of each actual polynomial coefficient. -/
theorem coeffInt_eq_scaled (h n k : ℕ) :
    (coeffInt h n k:ℚ)=(2:ℚ)^(h*degreeIndex n k)*
      (padePoly n ((3/2:ℚ)^h)).coeff k := by
  induction n generalizing k with
  | zero => cases k <;> simp [coeffInt,padePoly,degreeIndex,Polynomial.coeff_one]
  | succ n ih =>
    cases k with
    | zero => simp [poly_zero_coeff,degreeIndex]
    | succ k =>
      by_cases hkn : k≤n
      · have top1 := degreeIndex_succ_same n (k+1) (by omega)
        have top2 := topInsert n k hkn
        have h1 : (2:ℚ)^(h*degreeIndex (n+1) (k+1)) =
            2^(h*(k+1))*2^(h*degreeIndex n (k+1)) := by
          rw [top1,Nat.mul_add,pow_add,mul_comm]
        have h2 : (2:ℚ)^(h*degreeIndex (n+1) (k+1))*(3/2)^(h*(n+1)) =
            3^(h*(n+1))*2^(h*degreeIndex n k) := by
          rw [top2,Nat.mul_add,pow_add,div_pow]
          field_simp
        simp only [coeffInt,Int.cast_sub,Int.cast_mul,Int.cast_pow,Int.cast_ofNat,ih,
          poly_next_coeff,← pow_mul]
        calc
          _ = ((2:ℚ)^(h*(k+1))*2^(h*degreeIndex n (k+1)))*
              (padePoly n ((3/2:ℚ)^h)).coeff (k+1) -
              (3^(h*(n+1))*2^(h*degreeIndex n k))*(padePoly n ((3/2:ℚ)^h)).coeff k := by ring
          _ = _ := by rw [← h1,← h2]; ring
      · rw [coeffInt_vanish h (n+1) (k+1) (by omega),
          coeff_eq_zero_of_natDegree_lt (lt_of_le_of_lt (padePoly_degree (n+1) _) (by omega : n+1<k+1))]
        simp

theorem poly_coeff_eq (h n k : ℕ) :
    (padePoly n ((3/2:ℚ)^h)).coeff k=(coeffInt h n k:ℚ)/2^(h*degreeIndex n k) := by
  apply (eq_div_iff (by positivity)).mpr
  rw [coeffInt_eq_scaled,mul_comm]

end Collatz.PadeCoefficients
