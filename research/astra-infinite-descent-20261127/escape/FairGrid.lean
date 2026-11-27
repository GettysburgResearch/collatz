import AsynchronousGuard
import Mathlib.Basic.Real.Basic
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Data.Finset.Max

/-! A finite interval cover bounds the actual source count in a fixed ordinary
clock and grade. The real covering input is explicit. -/
set_option autoImplicit false
set_option warningAsError true

namespace FairGrid
open CoreBranching PeakRigidity

/-- Physical fair weight divided by the positive target. -/
noncomputable def weight (m d y : ℕ) : ℝ := (3:ℝ)^d / ((2:ℝ)^m*y)

theorem mark_le_one {m d y z : ℕ} (yp : 0<y) (hit : run m z=y) (gr : grade m z=d) :
    weight m d y * z ≤ 1 := by
  have form := AsynchronousGuard.affine m z
  rw [hit,gr] at form
  have bound : 3^d*z≤2^m*y := by omega
  have cast : (3:ℝ)^d*z≤(2:ℝ)^m*y := by exact_mod_cast bound
  rw [weight,div_mul_eq_mul_div,div_le_one (by positivity)]
  exact cast

/-- Finite mesh bound for one arbitrary real interval. -/
theorem interval_count (A : Finset ℕ) {h a b : ℝ} (hp : 0≤h) (ab : a≤b)
    (inside : ∀z∈A, a≤h*z ∧ h*z≤b) :
    h*A.card ≤ b-a+h := by
  by_cases ne : A.Nonempty
  · let lo := A.min' ne
    let hi := A.max' ne
    have sub : A⊆Finset.Icc lo hi := fun z hz =>
      Finset.mem_Icc.mpr ⟨A.min'_le z hz,A.le_max' z hz⟩
    have size := Finset.card_le_card sub
    rw [Nat.card_Icc] at size
    have order : lo≤hi := A.min'_le_max' ne
    have integer : A.card+lo≤hi+1 := by omega
    have real : (A.card:ℝ)+lo≤hi+1 := by exact_mod_cast integer
    have bottom := (inside lo (A.min'_mem ne)).1
    have top := (inside hi (A.max'_mem ne)).2
    nlinarith [mul_le_mul_of_nonneg_left real hp]
  · have empty : A=∅ := Finset.not_nonempty_iff_eq_empty.mp ne
    simp [empty]
    linarith

/-- Sum over any finite cover, with no disjointness assumption. -/
theorem cover_count {n : ℕ} (A : Finset ℕ) {h : ℝ} (hp : 0≤h) (a b : Fin n → ℝ)
    (ab : ∀i, a i≤b i)
    (cover : ∀z∈A, ∃i, a i≤h*z ∧ h*z≤b i) :
    h*A.card ≤ (∑i, (b i-a i)) + n*h := by
  classical
  let piece := fun i : Fin n => A.filter (fun z : ℕ => a i≤h*(z:ℝ) ∧ h*(z:ℝ)≤b i)
  have sub : A⊆Finset.univ.biUnion piece := by
    intro z hz
    obtain ⟨i,hi⟩ := cover z hz
    exact Finset.mem_biUnion.mpr ⟨i,Finset.mem_univ _,Finset.mem_filter.mpr ⟨hz,hi⟩⟩
  have count : A.card≤∑i, (piece i).card :=
    (Finset.card_le_card sub).trans Finset.card_biUnion_le
  have real : (A.card:ℝ)≤∑i, ((piece i).card:ℝ) := by exact_mod_cast count
  calc
    _ ≤ h*(∑i, ((piece i).card:ℝ)) := mul_le_mul_of_nonneg_left real hp
    _ = ∑i, h*((piece i).card:ℝ) := Finset.mul_sum ..
    _ ≤ ∑i, (b i-a i+h) := Finset.sum_le_sum fun i _ =>
      interval_count (piece i) hp (ab i) (fun _ hz => (Finset.mem_filter.mp hz).2)
    _ = _ := by simp [Finset.sum_add_distrib]

/-- Checked finite source-cutoff kernel. First visit and simplicity are only
needed to obtain the geometric cover, so all actual visits satisfying it work. -/
theorem ordinary_tail {m d y n : ℕ} (yp : 0<y) (A : Finset ℕ) {R : ℝ} (Rp : 0<R)
    (actual : ∀z∈A, run m z=y ∧ grade m z=d ∧ R≤(z:ℝ))
    (a b : Fin n → ℝ) (ab : ∀i, a i≤b i)
    (cover : ∀z∈A, ∃i, a i≤weight m d y*z ∧ weight m d y*z≤b i) :
    weight m d y * A.card ≤ (∑i, (b i-a i)) + n/R := by
  have wp : 0≤weight m d y := by unfold weight; positivity
  by_cases ne : A.Nonempty
  · obtain ⟨z,hz⟩ := ne
    obtain ⟨hit,gr,large⟩ := actual z hz
    have hR : weight m d y ≤ 1/R :=
      (le_div_iff₀ Rp).mpr ((mul_le_mul_of_nonneg_left large wp).trans (mark_le_one yp hit gr))
    have cost := cover_count A wp a b ab cover
    have scaled := mul_le_mul_of_nonneg_left hR (show (0:ℝ)≤n by positivity)
    have combine : weight m d y * A.card ≤ (∑i, (b i-a i)) + (n:ℝ)*(1/R) := by linarith
    simpa only [one_div,div_eq_mul_inv,one_mul] using combine
  · have empty : A=∅ := Finset.not_nonempty_iff_eq_empty.mp ne
    rw [empty]
    simp only [Finset.card_empty,Nat.cast_zero,mul_zero]
    exact add_nonneg (Finset.sum_nonneg fun i _ => sub_nonneg.mpr (ab i)) (by positivity)

#print axioms mark_le_one
#print axioms interval_count
#print axioms cover_count
#print axioms ordinary_tail
end FairGrid

