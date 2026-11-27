import ReciprocalPacking
import ReciprocalTrace
import OrbitPacking

/-! Uniform actual reciprocal tails, a positive physical correction floor and
a height-uniform first-arrival bound on orbits avoiding all small states. -/
set_option autoImplicit false
set_option warningAsError true

namespace ActualPacking
open Finset CoreBranching PeakRigidity FairGrid ReciprocalPacking ReciprocalTrace

theorem simple_tail (z m K : ℕ)
    (simple : ∀i≤m, ∀j≤m, run i z=run j z → i=j) :
    ∑ i∈(range m).filter (fun i => 8192^K≤run i z), (1/(run i z:ℝ)) ≤
      262144*ratio^K := by
  apply finite_tail (range m) (fun i => run i z)
  intro k
  have sub : (range m).filter (fun i => run i z<8192^k) ⊆
      (range (m+1)).filter (fun i => run i z<8192^k) := by
    intro i hi
    obtain ⟨before,cap⟩ := mem_filter.mp hi
    exact mem_filter.mpr ⟨mem_range.mpr (Nat.lt_succ_of_lt (mem_range.mp before)),cap⟩
  exact (card_le_card sub).trans (OrbitPacking.simple_block_card z m k simple)

theorem high_occupation (z m K : ℕ)
    (simple : ∀i≤m, ∀j≤m, run i z=run j z → i=j)
    (high : ∀i<m, 8192^K≤run i z) :
    ∑ i∈range m, (1/(run i z:ℝ)) ≤ 262144*ratio^K := by
  have full : (range m).filter (fun i => 8192^K≤run i z)=range m := by
    apply filter_eq_self.mpr
    intro i hi
    exact high i (mem_range.mp hi)
  simpa only [full] using simple_tail z m K simple

theorem first_floor {z m y d : ℕ} (zp : 0<z) (hit : run m z=y)
    (gr : grade m z=d) (first : ∀j<m, run j z≠y) :
    Real.exp (-262144)≤weight m d y*z := by
  have occ := high_occupation z m 0 (first_simple hit first) (fun i _ => by
    rw [pow_zero]
    have vp := run_pos i zp
    omega)
  have total : ∑i∈range m, (1/(run i z:ℝ)) ≤262144 := by simpa using occ
  simpa only [gr,hit] using mark_floor zp total

theorem row_bound {m d y : ℕ} (yp : 0<y) (A : Finset ℕ) (K : ℕ)
    (actual : ∀z∈A, 0<z ∧ run m z=y ∧ grade m z=d ∧ ∀j<m, run j z≠y)
    (above : ∀z∈A, ∀j≤m, 8192^K≤run j z) :
    weight m d y * A.card ≤ 262145*ratio^K := by
  have rp : 0≤ratio^K := by unfold ratio; positivity
  have wp : 0≤weight m d y := by unfold weight; positivity
  have low (z : ℕ) (hz : z∈A) : 1-262144*ratio^K≤weight m d y*z := by
    obtain ⟨zp,hit,gr,first⟩ := actual z hz
    have occ := high_occupation z m K (first_simple hit first) (fun i hi => above z hz i hi.le)
    have f := mark_floor zp occ
    rw [gr,hit] at f
    have ex := Real.add_one_le_exp (-(262144*ratio^K))
    linarith
  have inside := interval_count A wp (show 1-262144*ratio^K≤1 by linarith) (fun z hz => by
    obtain ⟨_,hit,gr,_⟩ := actual z hz
    exact ⟨low z hz,mark_le_one yp hit gr⟩)
  by_cases ne : A.Nonempty
  · obtain ⟨z,hz⟩ := ne
    obtain ⟨_,hit,gr,_⟩ := actual z hz
    have large : (8192:ℝ)^K≤z := by
      exact_mod_cast (show 8192^K≤z from above z hz 0 (Nat.zero_le _))
    have scale : weight m d y≤1/(8192:ℝ)^K := (le_div_iff₀ (by positivity)).mpr
      ((mul_le_mul_of_nonneg_left large wp).trans (mark_le_one yp hit gr))
    have cmp : 1/(8192:ℝ)^K≤ratio^K := by
      simpa only [one_div,inv_pow] using
        pow_le_pow_left₀ (by norm_num : 0≤(8192:ℝ)⁻¹) (by norm_num [ratio] : (8192:ℝ)⁻¹≤ratio) K
    linarith
  · have empty : A=∅ := Finset.not_nonempty_iff_eq_empty.mp ne
    simp only [empty,card_empty,Nat.cast_zero,mul_zero]
    exact mul_nonneg (by norm_num) rp

#print axioms simple_tail
#print axioms high_occupation
#print axioms first_floor
#print axioms row_bound
end ActualPacking

