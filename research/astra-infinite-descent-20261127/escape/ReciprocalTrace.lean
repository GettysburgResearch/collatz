import FairGrid
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.FieldSimp

/-! The normalized affine mark of a genuine ordinary shortcut path stays
above the exponential of minus its reciprocal occupation. -/
set_option autoImplicit false
set_option warningAsError true

namespace ReciprocalTrace
open CoreBranching PeakRigidity FairGrid

theorem step_pos {x : ℕ} (hx : 0<x) : 0<step x := by
  by_cases he : x%2=0
  · simp only [step,he,ite_true]; omega
  · simp only [step,he,ite_false]; omega

theorem run_pos (m : ℕ) {x : ℕ} (hx : 0<x) : 0<run m x := by
  induction m generalizing x with
  | zero => exact hx
  | succ m ih => exact ih (step_pos hx)

private theorem step_num (x : ℕ) : 2*step x=3^(x%2)*x+x%2 := by
  rcases Nat.mod_two_eq_zero_or_one x with h|h
  · simp [step,h]; omega
  · simp [step,h]; omega

private theorem step_log (x : ℕ) (xp : 0<x) :
    Real.log ((2:ℝ)*step x / ((3:ℝ)^(x%2)*x)) ≤ 1/x := by
  have sat : (2:ℝ)*step x=(3:ℝ)^(x%2)*x+(x%2:ℕ) := by exact_mod_cast step_num x
  rw [sat]
  rcases Nat.mod_two_eq_zero_or_one x with h|h
  · rw [h]
    simp [Nat.ne_of_gt xp]
  · rw [h]
    simp only [pow_one,Nat.cast_one]
    calc
      _ ≤ (3*(x:ℝ)+1)/(3*(x:ℝ))-1 := Real.log_le_sub_one_of_pos (by positivity)
      _ ≤ 1/x := by
        have hreal : (0:ℝ)<x := by exact_mod_cast xp
        field_simp
        linarith

noncomputable def inverseMark (m z : ℕ) : ℝ :=
  (2:ℝ)^m*run m z / ((3:ℝ)^(grade m z)*z)

private theorem succ_mark (m z : ℕ) (zp : 0<z) :
    inverseMark (m+1) z =
    inverseMark m z*((2:ℝ)*step (run m z)/((3:ℝ)^(run m z%2)*run m z)) := by
  have last : run (m+1) z=step (run m z) := by simpa [run] using run_add m 1 z
  have vp := run_pos m zp
  have vr : (run m z:ℝ)≠0 := by exact_mod_cast Nat.ne_of_gt vp
  dsimp [inverseMark]
  rw [last,grade,pow_add,pow_succ]
  field_simp
  ring

theorem log_bound (m z : ℕ) (zp : 0<z) :
    Real.log (inverseMark m z) ≤ ∑i∈Finset.range m, (1/(run i z:ℝ)) := by
  induction m with
  | zero => simp [inverseMark,run,grade,Nat.ne_of_gt zp]
  | succ m ih =>
    have vp := run_pos m zp
    have sp := step_pos vp
    have old : 0 < inverseMark m z := by unfold inverseMark; positivity
    rw [succ_mark m z zp, Real.log_mul old.ne' (by positivity),Finset.sum_range_succ]
    exact add_le_add ih (step_log (run m z) vp)

theorem mark_floor {m z : ℕ} (zp : 0<z) {B : ℝ}
    (occupation : ∑i∈Finset.range m, (1/(run i z:ℝ)) ≤ B) :
    Real.exp (-B) ≤ weight m (grade m z) (run m z)*z := by
  have vp := run_pos m zp
  have positive : 0<weight m (grade m z) (run m z)*z := by unfold weight; positivity
  have im : inverseMark m z=(weight m (grade m z) (run m z)*z)⁻¹ := by
    unfold weight inverseMark
    field_simp
  have lb := (log_bound m z zp).trans occupation
  rw [im,Real.log_inv] at lb
  rw [← Real.exp_log positive]
  exact Real.exp_le_exp.mpr (by linarith)

/-- A first visit gives the pairwise distinct physical prefix needed in the
finite packing theorem, including the endpoint index. -/
theorem first_simple {m z y : ℕ} (hit : run m z=y) (first : ∀ j<m, run j z≠y) :
    ∀i≤m, ∀j≤m, run i z=run j z → i=j := by
  have ordered (i j : ℕ) (lt : i<j) (jm : j≤m) (same : run i z=run j z) : False := by
    have later : run (i+(m-j)) z=y := by
      rw [run_add,same,←run_add,show j+(m-j)=m by omega]
      exact hit
    exact first _ (by omega) later
  intro i im j jm same
  rcases lt_trichotomy i j with lt|eq|gt
  · exact (ordered i j lt jm same).elim
  · exact eq
  · exact (ordered j i gt im same.symm).elim

#print axioms log_bound
#print axioms mark_floor
#print axioms first_simple
end ReciprocalTrace

