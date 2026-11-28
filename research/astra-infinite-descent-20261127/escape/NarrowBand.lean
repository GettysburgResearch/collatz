import OriginalLoss
import Mathlib.Data.Finset.Max

/-! A completely finite mark floor for every positive shortcut path with
distinct odd departures. It separates the two original PR193 rational-band
rows from every nonperiodic target at every positive grade. -/
set_option autoImplicit false
set_option warningAsError true
namespace NarrowBand
open CoreBranching PeakRigidity FairGrid OriginalLoss Finset ReciprocalTrace

noncomputable def factor (v : ℕ) : ℝ := 3*(v:ℝ)/(3*v+1)

theorem distinct_product (S : Finset ℕ) (pos : ∀v∈S, 0<v) :
    (3:ℝ)≤((S.card:ℝ)+3)*∏v∈S,factor v := by
  induction S using Finset.induction_on_max with
  | empty => simp
  | insert a S max ih =>
    have ap : 0<a := pos a (mem_insert_self a S)
    have hp : ∀v∈S, 0<v := fun v hv => pos v (mem_insert_of_mem hv)
    have ha : a∉S := fun h => (lt_irrefl a) (max a h)
    have inside : S⊆Ico 1 a := fun v hv => mem_Ico.mpr ⟨hp v hv,max v hv⟩
    have card := card_le_card inside
    rw [Nat.card_Ico] at card
    have scale : (S.card:ℝ)+3≤3*a := by exact_mod_cast (show S.card+3≤3*a by omega)
    have large : (S.card:ℝ)+3≤((S.card:ℝ)+1+3)*factor a := by
      unfold factor
      rw [← mul_div_assoc,le_div_iff₀ (by positivity)]
      linarith
    have nonneg : 0≤∏v∈S,factor v := prod_nonneg (fun v _ => by unfold factor; positivity)
    rw [card_insert_of_notMem ha,prod_insert ha,Nat.cast_add,Nat.cast_one]
    calc
      _ ≤ ((S.card:ℝ)+3)*∏v∈S,factor v := ih hp
      _ ≤ (((S.card:ℝ)+1+3)*factor a)*∏v∈S,factor v := mul_le_mul_of_nonneg_right large nonneg
      _ = _ := by ring

def oddTimes (m x : ℕ) : Finset ℕ := (range m).filter (fun i => run i x%2=1)

private theorem card_times (m x : ℕ) : (oddTimes m x).card=grade m x := by
  induction m with
  | zero => simp [oddTimes,grade]
  | succ m ih =>
    have hm : m∉oddTimes m x := by simp [oddTimes]
    rcases Nat.mod_two_eq_zero_or_one (run m x) with e|o
    · simpa [oddTimes,range_add_one,Finset.filter_insert,e,grade] using ih
    · simpa [oddTimes,range_add_one,Finset.filter_insert,o,grade] using ih

private theorem mark_prod (m x : ℕ) (xp : 0<x) :
    mark m x=∏i∈oddTimes m x, factor (run i x) := by
  induction m with
  | zero => simp [mark,weight,grade,run,oddTimes,Nat.ne_of_gt xp]
  | succ m ih =>
    have stepId := one_step m x xp
    have hm : m∉oddTimes m x := by simp [oddTimes]
    rcases Nat.mod_two_eq_zero_or_one (run m x) with e|o
    · simp [loss,e] at stepId
      simpa [oddTimes,range_add_one,Finset.filter_insert,e] using stepId.symm.trans ih
    · have evo : mark (m+1) x=factor (run m x)*mark m x := by
        simp only [loss,o,ite_true] at stepId
        unfold mark at stepId ⊢
        unfold factor
        have den : (3*(run m x:ℝ)+1)≠0 := by positivity
        field_simp at stepId ⊢
        linarith
      rw [evo,ih]
      simp [oddTimes,range_add_one,Finset.filter_insert,o]

/-- The true source mark at the physical horizon. Initial halvings need no
special convention, and the terminal value is not counted as a departure. -/
theorem simple_mark {m x : ℕ} (xp : 0<x)
    (inj : Set.InjOn (fun i => run i x) (oddTimes m x : Set ℕ)) :
    (3:ℝ)≤((grade m x:ℝ)+3)*mark m x := by
  let S := (oddTimes m x).image (fun i => run i x)
  have pos : ∀v∈S,0<v := by
    intro v hv
    obtain ⟨i,_,rfl⟩:=mem_image.mp hv
    exact run_pos i xp
  have result := distinct_product S pos
  dsimp only [S] at result
  rw [card_image_of_injOn inj,Finset.prod_image inj,card_times,←mark_prod m x xp] at result
  exact result

/-- At both clocks appearing in the depth-j original CDF difference, the
band is empty on every simple positive path when j≥1. -/
theorem narrow_empty {m x j : ℕ} (xp : 0<x) (jp : 0<j) (g : grade m x≤j+1)
    (inj : Set.InjOn (fun i => run i x) (oddTimes m x : Set ℕ)) :
    1/((j:ℝ)+1)<mark m x := by
  have h := simple_mark xp inj
  have nonneg : 0≤mark m x := by unfold mark weight; positivity
  have grow : (grade m x:ℝ)+3≤(j:ℝ)+4 := by exact_mod_cast (show grade m x+3≤j+4 by omega)
  have h' := h.trans (mul_le_mul_of_nonneg_right grow nonneg)
  have jr : (1:ℝ)≤j := by exact_mod_cast jp
  by_contra! low
  have bound := mul_le_mul_of_nonneg_left low (show (0:ℝ)≤(j:ℝ)+4 by positivity)
  have both:=h'.trans bound
  rw [mul_one_div,le_div_iff₀ (by positivity)] at both
  linarith

private theorem high_product {m x B : ℕ} (xp : 0<x)
    (high : ∀i∈oddTimes m x, B≤run i x) :
    (factor B)^(grade m x)≤mark m x := by
  rw [mark_prod m x xp,←card_times m x,←prod_const]
  apply prod_le_prod₀
  · intro i hi
    unfold factor
    positivity
  · intro i hi
    unfold factor
    have le : (B:ℝ)≤run i x := by exact_mod_cast high i hi
    rw [div_le_div_iff₀ (by positivity) (by positivity)]
    linarith

private theorem block_half {B : ℕ} (bp : 0<B) : 1/2<(factor B)^B := by
  have p : (0:ℝ)<factor B := by unfold factor; positivity
  have bern := one_add_mul_sub_le_pow (a:=factor B) (show -1≤factor B by linarith) B
  apply lt_of_lt_of_le _ bern
  unfold factor
  have br : (0:ℝ)<B := by exact_mod_cast bp
  field_simp
  nlinarith

private theorem all_high {b m x j : ℕ} (xp : 0<x) (jp : 0<j)
    (cap : j+1≤b*2^b) (g : grade m x≤j+1)
    (high : ∀i∈oddTimes m x, 2^b≤run i x) :
    1/((j:ℝ)+1)<mark m x := by
  let B := 2^b
  have Bp : 0<B := by dsimp [B]; positivity
  have fp : 0≤factor B := by unfold factor; positivity
  have small : factor B≤1 := by unfold factor; rw [div_le_one (by positivity)]; linarith
  have half := block_half Bp
  have endMark:=high_product xp high
  change (factor B)^(grade m x)≤mark m x at endMark
  by_cases early : j+1≤B
  · have first := pow_le_pow_of_le_one fp small (g.trans early)
    have d : (1:ℝ)≤j := by exact_mod_cast jp
    have compare : (1:ℝ)/((j:ℝ)+1)≤1/2 := by
      rw [div_le_div_iff₀ (by positivity) (by norm_num)]; linarith
    exact compare.trans_lt ((half.trans_le first).trans_le endMark)
  · have bp : 0<b := by by_contra! h; interval_cases b; simp at cap
    have r : ((1:ℝ)/2)^b < ((factor B)^B)^b :=
      pow_lt_pow_left₀ half (by norm_num) bp.ne'
    rw [←pow_mul] at r
    have lim : grade m x≤B*b := by simpa only [B,Nat.mul_comm] using g.trans cap
    have first := pow_le_pow_of_le_one fp small lim
    have d : (B:ℝ)≤(j:ℝ)+1 := by exact_mod_cast (show B≤j+1 by omega)
    have invB : (1:ℝ)/(B:ℝ)=((1:ℝ)/2)^b := by simp [B,one_div]
    have compare : (1:ℝ)/((j:ℝ)+1)≤((1:ℝ)/2)^b := by
      rw [←invB]
      exact one_div_le_one_div_of_le (by positivity) d
    exact compare.trans_lt ((r.trans_le first).trans_le endMark)

private theorem stays_small (h : ℕ) : run h 1≤2 ∧ run h 2≤2 := by
  induction h with
  | zero => decide
  | succ h ih => exact ⟨ih.2,ih.1⟩

private theorem simple_if_reaches_one {m x : ℕ} (large : 2<run m x)
    (hit : ∃h,run h x=1) : Set.InjOn (fun i => run i x) (oddTimes m x : Set ℕ) := by
  let H := Nat.find hit
  have hn : run H x=1 := Nat.find_spec hit
  have earliest : ∀i<H,run i x≠1 := fun i hi => Nat.find_min hit hi
  have hm : m<H := by
    by_contra! le
    have state : run m x=run (m-H) 1 := by
      calc
        _ = run (H+(m-H)) x := by rw [show H+(m-H)=m by omega]
        _ = _ := by rw [run_add,hn]
    have b: run m x≤2 := state ▸ (stays_small _).1
    omega
  have distinct := first_simple hn earliest
  intro i hi j hj eq
  have ii := mem_range.mp (mem_filter.mp hi).1
  have jj := mem_range.mp (mem_filter.mp hj).1
  exact distinct i (by omega) j (by omega) eq

/-- A verified positive prefix up to 2^b clears both original narrow-band
rows at every odd target greater than one through grade b*2^b-1. -/
theorem verified_narrow_empty {b m x j : ℕ} (xp : 0<x) (jp : 0<j)
    (cap : j+1≤b*2^b) (g : grade m x≤j+1) (large : 2<run m x)
    (verified : ∀n, 0<n → n≤2^b → ∃h,run h n=1) :
    1/((j:ℝ)+1)<mark m x := by
  by_cases high : ∀i∈oddTimes m x,2^b≤run i x
  · exact all_high xp jp cap g high
  · push Not at high
    obtain ⟨i,_,low⟩:=high
    obtain ⟨h,hit⟩:=verified _ (run_pos i xp) low.le
    have visits : ∃h,run h x=1 := ⟨i+h,by rw [run_add,hit]⟩
    exact narrow_empty xp jp g (simple_if_reaches_one large visits)

#print axioms verified_narrow_empty
#print axioms distinct_product
#print axioms simple_mark
#print axioms narrow_empty
end NarrowBand
