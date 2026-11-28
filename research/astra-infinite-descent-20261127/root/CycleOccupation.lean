import ActualPacking

/-! The reciprocal occupation of one simple positive cycle, and a uniform
bound on its logarithmic clock discrepancy, with no dependence on period. -/
set_option autoImplicit false
set_option warningAsError true

namespace CycleOccupation
open Finset CoreBranching PeakRigidity ReciprocalPacking ReciprocalTrace

theorem occupation (z P K : ℕ) (positive : 0<P)
    (simple : ∀i<P, ∀j<P, run i z=run j z → i=j)
    (high : ∀i<P, 8192^K≤run i z) :
    ∑i∈range P, (1/(run i z:ℝ)) ≤ 262144*ratio^K := by
  have previous : P-1+1=P := by omega
  have distinct : ∀i≤P-1, ∀j≤P-1, run i z=run j z → i=j := by
    intro i hi j hj same
    exact simple i (by omega) j (by omega) same
  have packing (k : ℕ) :
      ((range P).filter (fun i => run i z<8192^k)).card ≤ 4*6561^k := by
    simpa only [previous] using OrbitPacking.simple_block_card z (P-1) k distinct
  have bound := finite_tail (range P) (fun i => run i z) packing K
  have full : (range P).filter (fun i => 8192^K≤run i z)=range P := by
    exact filter_eq_self.mpr (fun i hi => high i (mem_range.mp hi))
  simpa only [full] using bound

/-- Every actual positive cycle with a distinct pre-return prefix above
8192^K has a small total clock discrepancy, independent of its length. -/
theorem logarithmic_gap (z P K : ℕ) (zp : 0<z) (positive : 0<P)
    (closed : run P z=z)
    (simple : ∀i<P, ∀j<P, run i z=run j z → i=j)
    (high : ∀i<P, 8192^K≤run i z) :
    (P:ℝ)*Real.log 2-(grade P z:ℝ)*Real.log 3 ≤ 262144*ratio^K := by
  have bound := (log_bound P z zp).trans (occupation z P K positive simple high)
  have zr : (z:ℝ)≠0 := by exact_mod_cast Nat.ne_of_gt zp
  have mark : inverseMark P z=(2:ℝ)^P/(3:ℝ)^(grade P z) := by
    unfold inverseMark
    rw [closed]
    field_simp
  rw [mark,Real.log_div (by positivity) (by positivity),Real.log_pow,Real.log_pow] at bound
  exact bound

/-- The same bound directly controls the ratio of the complete binary
and ternary powers around the loop. -/
theorem power_ratio (z P K : ℕ) (zp : 0<z) (positive : 0<P)
    (closed : run P z=z)
    (simple : ∀i<P, ∀j<P, run i z=run j z → i=j)
    (high : ∀i<P, 8192^K≤run i z) :
    (2:ℝ)^P/(3:ℝ)^(grade P z) ≤ Real.exp (262144*ratio^K) := by
  have bound := logarithmic_gap z P K zp positive closed simple high
  have lg : Real.log ((2:ℝ)^P/(3:ℝ)^(grade P z))=
      (P:ℝ)*Real.log 2-(grade P z:ℝ)*Real.log 3 := by
    rw [Real.log_div (by positivity) (by positivity),Real.log_pow,Real.log_pow]
  have h := Real.exp_le_exp.mpr (lg.trans_le bound)
  simpa only [Real.exp_log (by positivity : 0<(2:ℝ)^P/(3:ℝ)^(grade P z))] using h

#print axioms occupation
#print axioms logarithmic_gap
#print axioms power_ratio
end CycleOccupation
