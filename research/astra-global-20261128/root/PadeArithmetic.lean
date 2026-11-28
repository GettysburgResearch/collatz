import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.Algebra.Polynomial.Eval.Degree

/-! Finite arithmetic shared by the explicit Padé kernels. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.PadeArithmetic

def tri : ℕ → ℕ
  | 0 => 0
  | n+1 => tri n+n

@[simp] theorem tri_zero : tri 0=0 := rfl

@[simp] theorem tri_succ (n : ℕ) : tri (n+1)=tri n+n := rfl

theorem tri_add (a b : ℕ) : tri (a+b)=tri a+tri b+a*b := by
  induction b with
  | zero => simp
  | succ b ih =>
    simp only [Nat.add_succ,tri_succ,ih]
    simp only [Nat.succ_eq_add_one]
    ring

theorem twice_tri (n : ℕ) : 2*tri n+n=n*n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    rw [tri_succ]
    nlinarith

theorem tri_mono {a b : ℕ} (hab : a≤b) : tri a≤tri b := by
  induction b generalizing a with
  | zero =>
    have : a=0 := by omega
    subst a
    exact le_rfl
  | succ b ih =>
    by_cases h : a≤b
    · have hh := ih h
      rw [tri_succ]
      omega
    · have : a=b+1 := by omega
      subst a
      exact le_rfl

theorem tri_le_mul (k n : ℕ) (hkn : k≤n+1) : tri k≤k*n := by
  have ht := twice_tri k
  have hm := Nat.mul_le_mul_left k hkn
  nlinarith

def degreeIndex (n k : ℕ) : ℕ := k*n-tri k

theorem degreeIndex_add_tri (n k : ℕ) (hkn : k≤n+1) :
    degreeIndex n k+tri k=k*n := by
  exact Nat.sub_add_cancel (tri_le_mul k n hkn)

theorem degreeIndex_succ_same (n k : ℕ) (hkn : k≤n+1) :
    degreeIndex (n+1) k=degreeIndex n k+k := by
  have h0 := degreeIndex_add_tri n k hkn
  have h1 := degreeIndex_add_tri (n+1) k (by omega)
  nlinarith

theorem degreeIndex_succ_both (n k : ℕ) (hkn : k≤n+1) :
    degreeIndex (n+1) (k+1)=degreeIndex n k+n+1 := by
  have h0 := degreeIndex_add_tri n k hkn
  have h1 := degreeIndex_add_tri (n+1) (k+1) (by omega)
  rw [tri_succ] at h1
  nlinarith

theorem degreeIndex_plus_exponent (n m k : ℕ) (hkn : k≤n+1) :
    degreeIndex n k+(tri k+k*m)=k*(n+m) := by
  have h := degreeIndex_add_tri n k hkn
  nlinarith

theorem tri_double (s : ℕ) : tri (2*s)=2*tri s+s*s := by
  simpa only [two_mul] using tri_add s s

noncomputable def padePoly (n : ℕ) (q : ℚ) : Polynomial ℚ :=
  ∏ j ∈ Finset.range n, (1-Polynomial.C (q^(j+1))*Polynomial.X)

theorem padePoly_zero (q : ℚ) : padePoly 0 q=1 := by simp [padePoly]

theorem padePoly_succ (n : ℕ) (q : ℚ) :
    padePoly (n+1) q=padePoly n q*(1-Polynomial.C (q^(n+1))*Polynomial.X) := by
  simp only [padePoly,Finset.prod_range_succ]

theorem padePoly_degree (n : ℕ) (q : ℚ) : (padePoly n q).natDegree≤n := by
  induction n with
  | zero => simp [padePoly]
  | succ n ih =>
    rw [padePoly_succ]
    apply Polynomial.natDegree_mul_le_of_le ih
    have hc : (Polynomial.C (q^(n+1))*Polynomial.X : Polynomial ℚ).natDegree≤1 := by
      simpa only [pow_one] using Polynomial.natDegree_C_mul_X_pow_le (q^(n+1)) 1
    have ho : (1:Polynomial ℚ).natDegree≤1 := by simp
    simpa using Polynomial.natDegree_sub_le_of_le ho hc

end Collatz.PadeArithmetic
