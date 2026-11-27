module

public import PassageGateSublinear
public import Mathlib.Data.Rat.Cast.Order
public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Analysis.SpecialFunctions.Exp
public import PassageGatePrefix
import all PassageGatePrefix
import all HourTower
import all TernaryItinerary
import all PassageGatePacking
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageGate

open Finset
set_option autoImplicit false

private def band (x n k j : ℕ) : Finset ℕ :=
  (range n).filter (fun i => 256^k ≤ run i x ∧ run i x < 256^(k+j))

private theorem one_band {x n : ℕ} (k : ℕ) (pos : 0<x)
    (simple : (Set.Iio n).InjOn (fun i => run i x)) :
    (∑ i ∈ band x n k 1, 1/(run i x:ℚ))≤61800*(206/256:ℚ)^k := by
  have sub : band x n k 1 ⊆ visitSet x n (8*(k+1)) := by
    intro i hi
    obtain ⟨idx,_,high⟩ := mem_filter.mp hi
    apply mem_filter.mpr
    refine ⟨idx,?_⟩
    rw [pow_mul,show (2:ℕ)^8=256 by decide]
    exact high.le
  have count := (card_le_card sub).trans (explicit_simple_visits (k+1) pos simple)
  have cq : ((band x n k 1).card:ℚ)≤300*(206:ℚ)^(k+1) := by exact_mod_cast count
  calc
    _ ≤ ∑ _i ∈ band x n k 1, 1/(256:ℚ)^k := by
      apply sum_le_sum
      intro i hi
      have low := (mem_filter.mp hi).2.1
      exact one_div_le_one_div_of_le (by positivity) (by exact_mod_cast low)
    _ = ((band x n k 1).card:ℚ)/(256:ℚ)^k := by simp [div_eq_mul_inv]
    _ ≤ 300*206^(k+1)/(256:ℚ)^k := div_le_div_of_nonneg_right cq (by positivity)
    _ = _ := by rw [div_pow,pow_succ]; ring

private theorem bands {x n : ℕ} (k j : ℕ) (pos : 0<x)
    (simple : (Set.Iio n).InjOn (fun i => run i x)) :
    (∑ i ∈ band x n k j, 1/(run i x:ℚ))+316416*(206/256:ℚ)^(k+j)≤
      316416*(206/256:ℚ)^k := by
  induction j generalizing k with
  | zero =>
    have empty : band x n k 0=∅ := by
      apply eq_empty_iff_forall_notMem.mpr
      intro i mem
      obtain ⟨_,lo,hi⟩ := mem_filter.mp mem
      exact (Nat.not_lt_of_ge lo) hi
    simp [empty]
  | succ j ih =>
    have dis : Disjoint (band x n k 1) (band x n (k+1) j) := by
      apply disjoint_left.mpr
      intro i ha hb
      exact (Nat.not_lt_of_ge (mem_filter.mp hb).2.1) (mem_filter.mp ha).2.2
    have divide : band x n k (j+1)=band x n k 1 ∪ band x n (k+1) j := by
      ext i
      have early : (256:ℕ)^k≤256^(k+1) := Nat.pow_le_pow_right (by decide) (by omega)
      have late : (256:ℕ)^(k+1)≤256^(k+(j+1)) := Nat.pow_le_pow_right (by decide) (by omega)
      simp only [band,mem_filter,mem_union,show k+1+j=k+(j+1) by omega]
      constructor
      · rintro ⟨idx,low,top⟩
        by_cases lt : run i x<256^(k+1)
        · exact Or.inl ⟨idx,low,lt⟩
        · exact Or.inr ⟨idx,Nat.le_of_not_gt lt,top⟩
      · rintro (⟨idx,low,top⟩|⟨idx,low,top⟩)
        · exact ⟨idx,low,top.trans_le late⟩
        · exact ⟨idx,early.trans low,top⟩
    have first := one_band k pos simple
    have later := ih (k+1)
    rw [show k+1+j=k+(j+1) by omega] at later
    rw [pow_succ] at later
    rw [divide,sum_union dis]
    linarith

/-- Uniform summable reciprocal tail on the actual integer states of a
finite simple native path. No size cap on its intervening excursions. -/
theorem explicit_reciprocal_tail {x n : ℕ} (k : ℕ) (pos : 0<x)
    (simple : (Set.Iio n).InjOn (fun i => run i x)) :
    (∑ i ∈ (range n).filter (fun i => 256^k≤run i x), 1/(run i x:ℚ))≤
      316416*(206/256:ℚ)^k := by
  let J := (∑ i ∈ range n, run i x)+1
  have hi (i : ℕ) (mem : i∈range n) : run i x<256^(k+J) := by
    have w := single_le_sum (s:=range n) (f:=fun i => run i x) (fun _ _ => Nat.zero_le _) mem
    have exp := (Nat.lt_two_pow_self (n:=k+J)).trans_le (Nat.pow_le_pow_left (by decide : 2≤256) _)
    apply lt_of_le_of_lt _ exp
    dsimp only [J]
    omega
  have setEq : (range n).filter (fun i => 256^k≤run i x)=band x n k J := by
    ext i
    simp only [band,mem_filter]
    exact ⟨fun e => ⟨e.1,e.2,hi i e.1⟩,fun e => ⟨e.1,e.2.1⟩⟩
  rw [setEq]
  have sum := bands k J pos simple
  have hp : 0≤316416*(206/256:ℚ)^(k+J) := by positivity
  linarith

private noncomputable def tax (v : ℕ) : ℝ :=
  if v%2=1 then 1/(3*(v:ℝ)) else 0

private theorem row_tax (v : ℕ) (pos : 0<v) :
    2*(step v:ℝ)=(3:ℝ)^(v%2)*(v:ℝ)*(1+tax v) := by
  by_cases odd : v%2=1
  · have eqn : 2*step v=3*v+1 := by simp [step,odd]; omega
    have realEq : 2*(step v:ℝ)=3*(v:ℝ)+1 := by exact_mod_cast eqn
    rw [realEq,tax,ite_eq_left odd,odd,pow_one]
    field_simp
  · have even : v%2=0 := by omega
    have eqn : 2*step v=v := by simp [step,even]; omega
    have realEq : 2*(step v:ℝ)=(v:ℝ) := by exact_mod_cast eqn
    simp [tax,even,realEq]

private theorem tax_transport (x n : ℕ) (pos : 0<x) :
    (2:ℝ)^n*(run n x:ℝ)=(3:ℝ)^(HourTower.count n x)*(x:ℝ)*
      ∏ i ∈ range n, (1+tax (run i x)) := by
  induction n with
  | zero => simp [run,HourTower.count]
  | succ n ih =>
    have nextEq : run (n+1) x=step (run n x) := by rw [run_add]; rfl
    have grade : HourTower.count (n+1) x=HourTower.count n x+run n x%2 := by
      simpa [HourTower.count] using append_count n 1 x
    rw [nextEq,grade,prod_range_succ,pow_add (3:ℝ),pow_succ (2:ℝ) n]
    calc
      (2:ℝ)^n*2*(step (run n x):ℝ)=(2:ℝ)^n*(2*(step (run n x):ℝ)) := by ring
      _ = (3:ℝ)^(run n x%2)*(1+tax (run n x))*((2:ℝ)^n*(run n x:ℝ)) := by
        rw [row_tax _ (positive_run _ _ pos)]; ring
      _ = _ := by rw [ih]; ring

/-- Uniform geometric high-floor distortion loss for the actual
affine clock of a finite simple trajectory. Only its odd states must
clear the floor; the even states may be smaller. -/
theorem explicit_clock_distortion {x n : ℕ} (k : ℕ) (pos : 0<x)
    (simple : (Set.Iio n).InjOn (fun i => run i x))
    (floor : ∀ i<n, run i x%2=1 → 256^k≤run i x) :
    (2:ℝ)^n*(run n x:ℝ)≤(3:ℝ)^(HourTower.count n x)*(x:ℝ)*
      Real.exp (105472*(206/256:ℝ)^k) := by
  have raw := explicit_reciprocal_tail k pos simple
  have data : (∑ i ∈ (range n).filter (fun i => 256^k≤run i x), 1/(run i x:ℝ))≤
      316416*(206/256:ℝ)^k := by
    have lifted := (Rat.cast_le (K:=ℝ)).mpr raw
    push_cast at lifted
    exact lifted
  have compare : (∑ i ∈ range n, tax (run i x))≤
      (1/3:ℝ)*(∑ i ∈ (range n).filter (fun i => 256^k≤run i x), 1/(run i x:ℝ)) := by
    rw [sum_filter,mul_sum]
    apply sum_le_sum
    intro i mem
    by_cases odd : run i x%2=1
    · have tall := floor i (mem_range.mp mem) odd
      simp [tax,odd,tall,div_eq_mul_inv,mul_comm]
    · simp only [tax,ite_eq_right odd]
      split <;> positivity
  have bound : (∑ i ∈ range n, tax (run i x))≤105472*(206/256:ℝ)^k := by linarith
  rw [tax_transport x n pos]
  apply mul_le_mul_of_nonneg_left _ (by positivity)
  apply le_trans (Real.prod_one_add_le_exp_sum _ (f:=fun i => tax (run i x)) _)
    (Real.exp_le_exp.mpr bound)
  intro i
  unfold tax
  split <;> positivity

#print axioms explicit_clock_distortion
#print axioms explicit_reciprocal_tail
end Collatz.Itinerary.PassageGate
