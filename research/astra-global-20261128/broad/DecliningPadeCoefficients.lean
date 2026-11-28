import PadeCoefficients

/-! A doubly normalized integer coefficient for decreasing finite clocks.
The binary numerator power and ternary denominator power are both kept explicit. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.DecliningPadeCoefficients
open Collatz.PadeArithmetic
open Polynomial

def normalized (h : ℕ) : ℕ → ℕ → ℤ
  | 0, 0 => 1
  | 0, _+1 => 0
  | _+1, 0 => 1
  | n+1, k+1 => 3^(h*(k+1))*normalized h n (k+1)-2^(h*(n-k))*normalized h n k

@[simp] theorem normalized_zero (h n : ℕ) : normalized h n 0=1 := by cases n <;> rfl

theorem normalized_vanish (h n k : ℕ) (hk : n<k) : normalized h n k=0 := by
  induction n generalizing k with
  | zero => cases k <;> simp_all [normalized]
  | succ n ih =>
    cases k with
    | zero => omega
    | succ k => simp only [normalized,ih (k+1) (by omega),ih k (by omega),mul_zero,sub_zero]

@[simp] theorem normalized_diagonal (h n : ℕ) :
    normalized h (n+1) (n+1)= -normalized h n n := by
  simp only [normalized,normalized_vanish h n (n+1) (by omega),mul_zero,Nat.sub_self,
    pow_zero,one_mul,zero_sub]

theorem normalized_odd (h n k : ℕ) (hh : 0<h) (hk : k≤n) : Odd (normalized h n k) := by
  induction n generalizing k with
  | zero =>
    have hk' : k=0 := by omega
    subst k
    simpa only [normalized_zero] using (odd_one : Odd (1:ℤ))
  | succ n ih =>
    cases k with
    | zero => simpa only [normalized_zero] using (odd_one : Odd (1:ℤ))
    | succ k =>
      by_cases hkn : k=n
      · subst k
        rw [normalized_diagonal]
        exact (ih n (by omega)).neg
      · have hkn' : k<n := by omega
        have ho : Odd (3:ℤ) := by decide
        have he := (even_two : Even (2:ℤ)).pow_of_ne_zero
          (Nat.ne_of_gt (Nat.mul_pos hh (show 0<n-k by omega)))
        exact (ho.pow.mul (ih (k+1) (by omega))).sub_even (he.mul_right _)

theorem normalized_height (h n k : ℕ) :
    |normalized h n k|≤(n.choose k:ℤ)*3^(h*(k*(n-k))) := by
  induction n generalizing k with
  | zero => cases k <;> simp [normalized]
  | succ n ih =>
    cases k with
    | zero => simp
    | succ k =>
      by_cases hkn : k<n
      · have he1 : k+1+(k+1)*(n-(k+1))=(k+1)*(n-k) := by
          calc
            _ = (k+1)*(n-(k+1)+1) := by ring
            _ = _ := by rw [show n-(k+1)+1=n-k by omega]
        have he2 : n-k+k*(n-k)=(k+1)*(n-k) := by ring
        have hp1 : (3:ℤ)^(h*(k+1))*3^(h*((k+1)*(n-(k+1))))=3^(h*((k+1)*(n-k))) := by
          rw [←pow_add,←Nat.mul_add,he1]
        have hp2 : (3:ℤ)^(h*(n-k))*3^(h*(k*(n-k)))=3^(h*((k+1)*(n-k))) := by
          rw [←pow_add,←Nat.mul_add,he2]
        have hb1 := mul_le_mul_of_nonneg_left (ih (k+1)) (by positivity : (0:ℤ)≤3^(h*(k+1)))
        have hb2 := mul_le_mul
          (pow_le_pow_left₀ (by decide : (0:ℤ)≤2) (by decide : (2:ℤ)≤3) (h*(n-k)))
          (ih k) (abs_nonneg _) (by positivity)
        calc
          |normalized h (n+1) (k+1)| ≤ (3:ℤ)^(h*(k+1))*|normalized h n (k+1)|+
              2^(h*(n-k))*|normalized h n k| := by
            simpa only [normalized,abs_mul,abs_pow,abs_of_nonneg (by decide : (0:ℤ)≤2),
              abs_of_nonneg (by decide : (0:ℤ)≤3)] using
              (abs_sub ((3:ℤ)^(h*(k+1))*normalized h n (k+1)) (2^(h*(n-k))*normalized h n k))
          _ ≤ (3:ℤ)^(h*(k+1))*((n.choose (k+1):ℤ)*3^(h*((k+1)*(n-(k+1)))))+
              3^(h*(n-k))*((n.choose k:ℤ)*3^(h*(k*(n-k)))) := add_le_add hb1 hb2
          _ = (n.choose (k+1):ℤ)*(3^(h*(k+1))*3^(h*((k+1)*(n-(k+1)))))+
              (n.choose k:ℤ)*(3^(h*(n-k))*3^(h*(k*(n-k)))) := by ring
          _ = _ := by rw [hp1,hp2,Nat.choose_succ_succ',Nat.cast_add,Nat.succ_sub_succ_eq_sub]; ring
      · by_cases htop : k=n
        · subst k
          simpa only [normalized_diagonal,abs_neg,Nat.choose_self,Nat.sub_self,
            Nat.mul_zero,pow_zero,Nat.cast_one,mul_one] using ih n
        · rw [normalized_vanish h (n+1) (k+1) (by omega),abs_zero]
          positivity

private theorem zero_column (n : ℕ) (q : ℚ) : (padePoly n q).coeff 0=1 := by
  induction n with
  | zero => simp [padePoly]
  | succ n ih => rw [padePoly_succ,mul_sub,mul_one,←mul_assoc,coeff_sub,coeff_mul_X_zero,sub_zero,ih]

private theorem next_column (n k : ℕ) (q : ℚ) :
    (padePoly (n+1) q).coeff (k+1)=
      (padePoly n q).coeff (k+1)-(padePoly n q).coeff k*q^(n+1) := by
  simp only [padePoly_succ,mul_sub,mul_one,←mul_assoc,coeff_sub,coeff_mul_X,coeff_mul_C]

theorem scaled_coeff (h n k : ℕ) :
    (3:ℚ)^(h*degreeIndex n k)*(padePoly n ((2/3:ℚ)^h)).coeff k =
      (normalized h n k:ℚ)*2^(h*tri (k+1)) := by
  induction n generalizing k with
  | zero => cases k <;> simp [padePoly,degreeIndex,normalized,Polynomial.coeff_one]
  | succ n ih =>
    cases k with
    | zero => simp [zero_column,degreeIndex]
    | succ k =>
      by_cases hk : k≤n
      · have he1 := degreeIndex_succ_same n (k+1) (by omega)
        have he2 := degreeIndex_succ_both n k (by omega)
        have h1 : (3:ℚ)^(h*degreeIndex (n+1) (k+1))=
            3^(h*(k+1))*3^(h*degreeIndex n (k+1)) := by
          rw [he1,Nat.mul_add,pow_add,mul_comm]
        have h2 : (3:ℚ)^(h*degreeIndex (n+1) (k+1))*(2/3)^(h*(n+1))=
            2^(h*(n+1))*3^(h*degreeIndex n k) := by
          rw [he2,show degreeIndex n k+n+1=degreeIndex n k+(n+1) by omega,Nat.mul_add,pow_add,div_pow]
          field_simp
        have he3 : h*(n+1)+h*tri (k+1)=h*(n-k)+h*tri (k+1+1) := by
          rw [←Nat.mul_add,←Nat.mul_add]
          congr 1
          rw [tri_succ (k+1)]
          omega
        have h3 : (2:ℚ)^(h*(n+1))*2^(h*tri (k+1))=
            2^(h*(n-k))*2^(h*tri (k+1+1)) := by rw [←pow_add,←pow_add,he3]
        simp only [next_column,←pow_mul,normalized,Int.cast_sub,Int.cast_mul,Int.cast_pow,Int.cast_ofNat]
        calc
          _ = 3^(h*(k+1))*(3^(h*degreeIndex n (k+1))*(padePoly n ((2/3:ℚ)^h)).coeff (k+1))-
              2^(h*(n+1))*(3^(h*degreeIndex n k)*(padePoly n ((2/3:ℚ)^h)).coeff k) := by
            rw [←mul_assoc,←h1,←mul_assoc,←h2]
            ring
          _ = _ := by
            rw [ih,ih]
            calc
              _ = 3^(h*(k+1))*((normalized h n (k+1):ℚ)*2^(h*tri (k+1+1)))-
                  (normalized h n k:ℚ)*(2^(h*(n+1))*2^(h*tri (k+1))) := by ring
              _ = _ := by rw [h3]; ring
      · rw [normalized_vanish h (n+1) (k+1) (by omega),
          coeff_eq_zero_of_natDegree_lt (lt_of_le_of_lt (padePoly_degree (n+1) _) (by omega : n+1<k+1))]
        simp

theorem poly_coeff_eq (h n k : ℕ) :
    (padePoly n ((2/3:ℚ)^h)).coeff k=(normalized h n k:ℚ)*2^(h*tri (k+1))/3^(h*degreeIndex n k) := by
  apply (eq_div_iff (by positivity)).mpr
  rw [mul_comm,scaled_coeff]

end Collatz.DecliningPadeCoefficients
