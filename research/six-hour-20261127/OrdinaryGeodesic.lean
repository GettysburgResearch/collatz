import FloorCertificate
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Rat.Cast.Order

/-! A finite ordinary-source consequence of the checked reciprocal budget.
No assertion of termination, escape exclusion or cycle uniqueness is made. -/
set_option autoImplicit false
set_option warningAsError true
namespace SixHour.OrdinaryGeodesic
open CoreBranching PeakRigidity
open scoped BigOperators

private theorem last (j x : ℕ) : run (j+1) x = step (run j x) := by
  simpa [run] using run_add j 1 x

private theorem positive (j x : ℕ) (hx : 0<x) : 0<run j x := by
  induction j with
  | zero => simpa [run] using hx
  | succ j ih =>
    rw [last]
    unfold step
    split <;> omega

def correction (x : ℕ) : ℚ := if x%2=0 then 0 else 1/(3*(x:ℚ))

private theorem correction_nonneg (x : ℕ) : 0≤correction x := by
  unfold correction
  split
  · exact le_rfl
  · exact div_nonneg (by norm_num) (by positivity)

private theorem edge (x : ℕ) (hx : 0<x) :
    2*(step x:ℚ) = 3^(x%2)*(x:ℚ)*(1+correction x) := by
  have xp : (0:ℚ)<x := by exact_mod_cast hx
  by_cases e : x%2=0
  · have a : 2*step x=x := by simp [step,e]; omega
    have b : (2:ℚ)*(step x:ℚ)=x := by exact_mod_cast a
    simpa [correction,e] using b
  · have o : x%2=1 := by omega
    have a : 2*step x=3*x+1 := by simp [step,e]; omega
    have b : (2:ℚ)*(step x:ℚ)=3*(x:ℚ)+1 := by exact_mod_cast a
    rw [o,pow_one,b,show correction x=1/(3*(x:ℚ)) by simp [correction,e]]
    field_simp

theorem residue_identity (x n : ℕ) (hx : 0<x) :
    (2:ℚ)^n*(run n x:ℚ) =
      3^(grade n x)*(x:ℚ)*∏ i ∈ Finset.range n, (1+correction (run i x)) := by
  induction n with
  | zero => simp [run,grade]
  | succ n ih =>
    rw [pow_succ,last,Finset.prod_range_succ,grade,pow_add]
    have e := edge (run n x) (positive n x hx)
    calc
      _ = (2:ℚ)^n*(2*(step (run n x):ℚ)) := by ring
      _ = (2:ℚ)^n*(3^(run n x%2)*(run n x:ℚ)*(1+correction (run n x))) := by rw [e]
      _ = 3^(run n x%2)*(1+correction (run n x))*((2:ℚ)^n*(run n x:ℚ)) := by ring
      _ = _ := by rw [ih]; ring

private theorem product_budget (s : Finset ℕ) (u : ℕ → ℚ)
    (hu : ∀ i, 0≤u i) :
    (1-∑ i ∈ s, u i)*(∏ i ∈ s, (1+u i))≤1 := by
  induction s using Finset.induction_on with
  | empty => simp
  | @insert a s ha ih =>
    rw [Finset.sum_insert ha,Finset.prod_insert ha]
    have S : 0≤∑ i ∈ s, u i := Finset.sum_nonneg (fun i _ => hu i)
    have P : 0≤∏ i ∈ s, (1+u i) := Finset.prod_nonneg (fun i _ => by linarith [hu i])
    have drop : 0≤(u a)*(u a+∑ i ∈ s, u i)*(∏ i ∈ s, (1+u i)) :=
      mul_nonneg (mul_nonneg (hu a) (by linarith [hu a])) P
    nlinarith

theorem residue_floor (x n : ℕ)
    (simple : ∀ a≤n, ∀ b≤n, run a x=run b x → a=b)
    (floor : ∀ t≤n, 2^71≤run t x) :
    (2:ℚ)^n*(run n x:ℚ) < (3/2:ℚ)*3^(grade n x)*(x:ℚ) := by
  have hx : 0<x := by
    have h := floor 0 (by omega)
    simp only [run] at h
    omega
  have all := FloorCertificate.reciprocal_floor x n simple floor
  rw [Finset.sum_range_succ] at all
  have tailpos : (0:ℚ)≤1/(run n x:ℚ) := div_nonneg (by norm_num) (by positivity)
  have each (i : ℕ) : correction (run i x)≤(1/3:ℚ)*(1/(run i x:ℚ)) := by
    unfold correction
    split
    · exact mul_nonneg (by norm_num) (div_nonneg (by norm_num) (by positivity))
    · simp [div_eq_mul_inv,mul_inv_rev,mul_comm]
  have sum_bound := Finset.sum_le_sum (s:=Finset.range n) (fun i _ => each i)
  rw [←Finset.mul_sum] at sum_bound
  have sum_small : (∑ i ∈ Finset.range n, correction (run i x)) < 1/3 := by linarith
  have prodpos : (0:ℚ)<∏ i ∈ Finset.range n, (1+correction (run i x)) := by
    apply Finset.prod_pos
    intro i _
    linarith [correction_nonneg (run i x)]
  have budget := product_budget (Finset.range n) (fun i => correction (run i x))
    (fun i => correction_nonneg (run i x))
  have prodsmall : (∏ i ∈ Finset.range n, (1+correction (run i x))) < (3/2:ℚ) := by nlinarith
  rw [residue_identity x n hx]
  have factor : (0:ℚ)<3^(grade n x)*(x:ℚ) := by positivity
  nlinarith

theorem coefficient_lower (x n : ℕ) (hx : 0<x) :
    3^(grade n x)*(x:ℚ) ≤ (2:ℚ)^n*(run n x:ℚ) := by
  rw [residue_identity x n hx]
  have prod : (1:ℚ)≤∏ i ∈ Finset.range n, (1+correction (run i x)) := by
    apply Finset.one_le_prod₀
    intro i _
    linarith [correction_nonneg (run i x)]
  have p : (0:ℚ)≤3^(grade n x)*(x:ℚ) := by positivity
  nlinarith

theorem shorter_same_grade_is_smaller (x n y m : ℕ)
    (simple : ∀ a≤n, ∀ b≤n, run a x=run b x → a=b)
    (floor : ∀ t≤n, 2^71≤run t x)
    (hy : 0<y) (same : run m y=run n x)
    (grades : grade m y=grade n x) (shorter : m<n) : y<x := by
  have hi := residue_floor x n simple floor
  have lo := coefficient_lower y m hy
  rw [same,grades] at lo
  have pow : 2*(2:ℚ)^m≤(2:ℚ)^n := by
    have h := pow_le_pow_right₀ (by norm_num : (1:ℚ)≤2) (show m+1≤n by omega)
    simpa [pow_succ,mul_comm] using h
  have endpoint : (0:ℚ)≤run n x := by positivity
  have p : (0:ℚ)<3^(grade n x) := by positivity
  have scaled := mul_le_mul_of_nonneg_right pow endpoint
  have : (y:ℚ)<x := by nlinarith
  exact_mod_cast this

#print axioms residue_identity
#print axioms residue_floor
#print axioms coefficient_lower
#print axioms shorter_same_grade_is_smaller
end SixHour.OrdinaryGeodesic
