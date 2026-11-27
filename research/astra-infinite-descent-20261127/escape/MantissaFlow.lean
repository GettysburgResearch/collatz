import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-! Exact logarithmic weights for the finite interval exchange used to count
first-hit atoms. Source cells have denominator three. The destination has
denominator two on the first subinterval, and four on the second. -/
set_option autoImplicit false
set_option warningAsError true
namespace MantissaFlow

noncomputable def cell (i : ℕ) : ℝ := Real.log ((i:ℝ)+1)-Real.log i
noncomputable def block (start len : ℕ) (f : ℕ → ℝ) : ℝ :=
  ∑ j ∈ Finset.range len, cell (start+j)*f (start+j)

private theorem telescope (s n : ℕ) :
    ∑ j ∈ Finset.range n, cell (s+j) = Real.log ((s:ℝ)+n)-Real.log s := by
  induction n with
  | zero => simp
  | succ n ih => rw [Finset.sum_range_succ,ih]; simp [cell,Nat.cast_add]; ring_nf

private theorem cells (s q : ℕ) (sp : 0<s) (qp : 0<q) :
    ∑ j ∈ Finset.range q, cell (q*s+j) = cell s := by
  rw [telescope]
  simp only [Nat.cast_mul,cell]
  have hq : (q:ℝ)≠0 := by positivity
  have hs : (s:ℝ)≠0 := by positivity
  have h1 : (s:ℝ)+1≠0 := by positivity
  rw [show (q:ℝ)*s+q=q*(s+1) by ring,Real.log_mul hq h1,Real.log_mul hq hs]
  ring

private theorem split_block (s m n : ℕ) (f : ℕ → ℝ) :
    block s (m+n) f = block s m f+block (s+m) n f := by
  simp only [block,Finset.sum_range_add,Nat.add_assoc]

private theorem rescale (s n q : ℕ) (sp : 0<s) (qp : 0<q) (f : ℕ → ℝ) :
    block (q*s) (q*n) (fun k => f (k/q))=block s n f := by
  induction n with
  | zero => simp [block]
  | succ n ih =>
    rw [Nat.mul_succ,split_block,ih,split_block s n 1]
    rw [show q*s+q*n=q*(s+n) by ring]
    unfold block
    simp only [Finset.sum_range_one,Nat.add_zero,add_right_inj]
    rw [←cells (s+n) q (by omega) qp,Finset.sum_mul]
    exact Finset.sum_congr rfl fun j hj => by
      rw [Nat.mul_add_div qp,Nat.div_eq_of_lt (Finset.mem_range.mp hj),Nat.add_zero]

def dst (n k : ℕ) : ℕ := if k<8*n then k/2 else k/4

theorem outgoing (n : ℕ) (np : 0<n) (f : ℕ → ℝ) :
    block (6*n) (6*n) (fun k=>f (k/3))=block (2*n) (2*n) f := by
  simpa only [←Nat.mul_assoc] using rescale (2*n) (2*n) 3 (by omega) (by decide) f

theorem incoming (n : ℕ) (np : 0<n) (f : ℕ → ℝ) :
    block (6*n) (6*n) (fun k=>f (dst n k))=block (2*n) (2*n) f := by
  rw [show 6*n=2*n+4*n by omega] -- split both the starting index and length below
  rw [split_block]
  have left : block (2*n+4*n) (2*n) (fun k => f (dst n k)) = block (3*n) n f := by
    have same : block (2*n+4*n) (2*n) (fun k => f (dst n k)) =
        block (2*(3*n)) (2*n) (fun k=>f (k/2)) := by
      unfold block
      apply Finset.sum_congr rfl
      intro j hj
      have lt:= Finset.mem_range.mp hj
      dsimp only
      have below : 2*n+4*n+j<8*n := by omega
      rw [dst,ite_eq_left below,show 2*n+4*n=2*(3*n) by omega]
    exact same.trans (rescale (3*n) n 2 (by omega) (by decide) f)
  have right : block (2*n+4*n+2*n) (4*n) (fun k => f (dst n k)) = block (2*n) n f := by
    have same : block (2*n+4*n+2*n) (4*n) (fun k => f (dst n k)) =
        block (4*(2*n)) (4*n) (fun k => f (k/4)) := by
      unfold block
      apply Finset.sum_congr rfl
      intro j _
      dsimp only
      have above : ¬(2*n+4*n+2*n+j<8*n) := by omega
      rw [dst,ite_eq_right above,show 2*n+4*n+2*n=4*(2*n) by omega]
    exact same.trans (rescale (2*n) n 4 (by omega) (by decide) f)
  rw [left,right,show 2*n=n+n by omega]
  rw [split_block,show n+n+n=3*n by omega,add_comm]

private theorem cell_bounds (i : ℕ) (ip : 0 < i) :
    1/((i:ℝ)+1)≤cell i ∧ cell i≤1/(i:ℝ) := by
  have hp : (0:ℝ)< i := by exact_mod_cast ip
  have hr : (0:ℝ)<((i:ℝ)+1)/i := by positivity
  have one := Real.one_sub_inv_le_log_of_pos hr
  have two := Real.log_le_sub_one_of_pos hr
  rw [Real.log_div (by positivity) hp.ne'] at one two
  have div1 : (1:ℝ)/((i:ℝ)+1)=1-(((i:ℝ)+1)/i)⁻¹ := by field_simp; ring
  have div2 : ((i:ℝ)+1)/i-1=1/(i:ℝ) := by field_simp; ring
  unfold cell
  rw [div1,←div2]
  exact ⟨one,two⟩

/-- On the octave `[2*n,4*n)`, the atom `A` and strict lower level `F` are
disjoint, and each unaborted outgoing cell from `A ∪ F` enters `F`.
The failed cells bound the complete integer atom count. -/
theorem atom_card (n : ℕ) (np : 0<n) (A F B : ℕ → Prop)
    [DecidablePred A] [DecidablePred F] [DecidablePred B]
    (disjoint : ∀x, A x → ¬F x)
    (flows : ∀ k, 6*n≤k → k<12*n → ¬B k → A (k/3) ∨ F (k/3) → F (dst n k)) :
    3*((Finset.range (2*n)).filter (fun i=>A (2*n+i))).card ≤
      2*((Finset.range (6*n)).filter (fun i=>B (6*n+i))).card := by
  let ind := fun (P : ℕ → Prop) [DecidablePred P] (x : ℕ) => if P x then (1:ℝ) else 0
  have point (k : ℕ) (lo : 6*n≤k) (hi : k<12*n) :
      ind A (k/3)+ind F (k/3) ≤ ind F (dst n k)+ind B k := by
    dsimp [ind]
    have sep := disjoint (k/3)
    have go := flows k lo hi
    by_cases a : A (k/3) <;> by_cases f : F (k/3) <;> by_cases b : B k <;>
      by_cases g : F (dst n k) <;> simp_all
  have hsum := Finset.sum_le_sum (s:=Finset.range (6*n)) (fun j hj =>
    mul_le_mul_of_nonneg_left (point (6*n+j) (by omega) (by have := Finset.mem_range.mp hj; omega))
      ((show (0:ℝ)≤1/(((6*n+j:ℕ):ℝ)+1) by positivity).trans (cell_bounds _ (by omega)).1))
  simp only [mul_add,Finset.sum_add_distrib] at hsum
  change block (6*n) (6*n) (fun k=>ind A (k/3)) + block (6*n) (6*n) (fun k=>ind F (k/3)) ≤
    block (6*n) (6*n) (fun k=>ind F (dst n k)) + block (6*n) (6*n) (ind B) at hsum
  rw [outgoing _ np,outgoing _ np,incoming _ np] at hsum
  have total : block (2*n) (2*n) (ind A)≤block (6*n) (6*n) (ind B) := by linarith
  have sumind (l h : ℕ) (P : ℕ → Prop) [DecidablePred P] :
      ∑j ∈ Finset.range l, ind P (h+j)=(((Finset.range l).filter (fun j=>P (h+j))).card:ℝ) := by
    simp [ind,Finset.sum_boole]
  have low := Finset.sum_le_sum (s:=Finset.range (2*n)) (fun j hj => by
    have jl:=Finset.mem_range.mp hj
    have size : ((2*n+j:ℕ):ℝ)+1≤4*(n:ℝ) := by exact_mod_cast (show 2*n+j+1≤4*n by omega)
    have fl := (one_div_le_one_div_of_le (by positivity) size).trans (cell_bounds (2*n+j) (by omega)).1
    exact mul_le_mul_of_nonneg_right fl (show 0≤ ind A (2*n+j) by dsimp [ind]; split <;> norm_num))
  have high := Finset.sum_le_sum (s:=Finset.range (6*n)) (fun j _ => by
    have sz : (6:ℝ)*n≤((6*n+j:ℕ):ℝ) := by exact_mod_cast (show 6*n≤6*n+j by omega)
    have fl := (cell_bounds (6*n+j) (by omega)).2.trans (one_div_le_one_div_of_le (by positivity) sz)
    exact mul_le_mul_of_nonneg_right fl (show 0≤ ind B (6*n+j) by dsimp [ind]; split <;> norm_num))
  rw [←Finset.mul_sum,sumind] at low
  rw [←Finset.mul_sum,sumind] at high
  have full := low.trans (total.trans high)
  have a : (0:ℝ)<n := by exact_mod_cast np
  field_simp at full
  exact_mod_cast (show 3*(((Finset.range (2*n)).filter (fun i=>A (2*n+i))).card:ℝ)≤
    2*(((Finset.range (6*n)).filter (fun i=>B (6*n+i))).card:ℝ) by nlinarith only [full,a])

#print axioms outgoing
#print axioms incoming
#print axioms atom_card
end MantissaFlow
