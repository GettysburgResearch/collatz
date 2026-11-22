/-
Whole source/target prefixes can cross an increasing intermediate multiset
rank and return below the original supplied rank. The arithmetic source clock
strictly decreases on each paired step, but its terminal power-of-two boundary
is not a proved global induction base.
-/
import Collatz.LowGapGlobal

open CollatzReverseBasin CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzLowGapLoops CollatzBoundedGapCofinal
open CollatzLowIntervalRefinement

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzClockSynchronization

/-- The exact number of shortcut clocks encoded by the supplied source word. -/
def clock (e : Nat) (word : List Nat) : Nat := e+total word

theorem length_le_total (word : List Nat) (positive : PositiveGaps word) :
    word.length≤total word := by
  induction word with
  | nil => simp [total]
  | cons a tail ih =>
    have pa := positive a (by simp)
    have pt : PositiveGaps tail := fun b hb => positive b (by simp [hb])
    have bound := ih pt
    simp only [List.length_cons,total]
    omega

/-- Gap-one words have the least affine correction at any fixed length. -/
theorem minimal_correction_bound (word : List Nat) (positive : PositiveGaps word) :
    3^word.length≤correction word+2^word.length := by
  induction word with
  | nil => simp [correction]
  | cons a tail ih =>
    have pa := positive a (by simp)
    have pt : PositiveGaps tail := fun b hb => positive b (by simp [hb])
    have bound := ih pt
    have power : 2≤2^a :=
      Nat.pow_le_pow_right (by decide : 1≤2) (by omega : 1≤a)
    have product := Nat.mul_le_mul_right (correction tail) power
    simp only [List.length_cons,correction,Nat.pow_succ]
    omega

theorem leading_correction (word : List Nat) (nonempty : word≠[]) :
    3^word.length≤3*correction word := by
  cases word with
  | nil => exact False.elim (nonempty rfl)
  | cons a tail =>
    simp only [List.length_cons,correction,Nat.pow_succ]
    omega

private theorem one_gap_prefix (target b v : Nat) (positive : 0<b)
    (step : 3*target+1=2^b*v) : Prefix target [b] v := by
  refine ⟨?_,?_⟩
  · intro c mem
    have eq := List.mem_singleton.mp mem
    simpa [eq] using positive
  · simpa [correction,total] using step

/-- Any paid positive target gap consumes exactly that many supplied source
clocks, including gaps below min(a,e+1). No multiset descent is asserted here. -/
theorem paired_step (source target e a b v : Nat) (tail : List Nat)
    (even : 1≤e) (paid : b≤e+a) (positive : 0<b)
    (active : Interval source target)
    (cert : PoweredCertificate source e (a::tail))
    (targetStep : 3*target+1=2^b*v) :
    ∃ u, Certificate u tail ∧
      PoweredCertificate (2^(e+a-b)*u) (e+a-b) tail ∧
      Interval (2^(e+a-b)*u) v ∧
      clock (e+a-b) tail+b=clock e (a::tail) ∧
      clock (e+a-b) tail<clock e (a::tail) ∧
      (Basin target ↔ Basin v) := by
  obtain ⟨q,parent,sourceCert⟩ := cert
  obtain ⟨_,u,step,tailCert⟩ := (certificate_cons_iff q a tail).mp sourceCert
  have shift : 2^b*2^(e+a-b)=2^e*2^a := by
    rw [←Nat.pow_add,←Nat.pow_add]
    congr 1
    omega
  have slack : 2^b*(2*(2^(e+a-b)*u))=6*source+2^(e+1) := by
    calc
      2^b*(2*(2^(e+a-b)*u)) = 2*(2^b*2^(e+a-b))*u := by ac_rfl
      _ = 2*(2^e*2^a)*u := by rw [shift]
      _ = 2^a*(2*(2^e*u)) := by ac_rfl
      _ = _ := scaled_gap_identity source e q a u parent step
  have vp : 0<v := by
    by_cases zero : v=0
    · simp [zero] at targetStep
    · omega
  have payment : 4≤2^(e+1) :=
    Nat.pow_le_pow_right (by decide : 1≤2) (by omega : 2≤e+1)
  have scaled : 2^b*v≤2^b*(2*(2^(e+a-b)*u)) := by
    have upper := active.2
    omega
  have bound : v≤2*(2^(e+a-b)*u) :=
    Nat.le_of_mul_le_mul_left scaled (Nat.pow_pos (by decide))
  have identity : clock (e+a-b) tail+b=clock e (a::tail) := by
    simp only [clock,total]
    omega
  refine ⟨u,tailCert,⟨u,rfl,tailCert⟩,⟨vp,by omega⟩,identity,?_,?_⟩
  · omega
  · exact prefix_basin (one_gap_prefix target b v positive targetStep)

/-- A final source even run may absorb the remaining clock deficit. This
comparison is direct; the intermediate initial even exponents may grow. -/
theorem funded_prefix_interval (source target e f q u v : Nat)
    (front targetWord : List Nat) (even : 1≤e)
    (parent : source=2^e*q) (active : Interval source target)
    (sourcePath : Prefix q front u) (targetPath : Prefix target targetWord v)
    (nonempty : front≠[]) (length : targetWord.length=front.length)
    (time : e+total front≤f+total targetWord)
    (corrections : correction targetWord≤correction front) :
    Interval (2^f*u) v := by
  have first := leading_correction front nonempty
  have payment : 4≤2^(e+1) :=
    Nat.pow_le_pow_right (by decide : 1≤2) (by omega : 2≤e+1)
  have multiplied := Nat.mul_le_mul_right (correction front) payment
  have paid : 3^front.length+correction targetWord≤2^(e+1)*correction front := by
    omega
  have sourceIdentity :
      2^total front*(2*(2^e*u)) =
        3^front.length*(2*source)+2^(e+1)*correction front := by
    calc
      2^total front*(2*(2^e*u)) = 2^(e+1)*(2^total front*u) := by
        rw [Nat.pow_succ]
        ac_rfl
      _ = 2^(e+1)*(3^front.length*q+correction front) := by rw [sourcePath.2]
      _ = _ := by
        rw [Nat.mul_add,parent,Nat.pow_succ]
        congr 1
        ac_rfl
  have targetIdentity : 3^front.length*target+correction targetWord=2^total targetWord*v := by
    simpa [length] using targetPath.2
  have upper := Nat.mul_le_mul_left (3^front.length) active.2
  simp only [Nat.mul_add,Nat.mul_one] at upper
  have power := Nat.pow_le_pow_right (by decide : 1≤2) time
  have compared := Nat.mul_le_mul_right (2*u) power
  have oldFactor : 2^(e+total front)*(2*u)=2^total front*(2*(2^e*u)) := by
    rw [Nat.pow_add]
    ac_rfl
  have newFactor : 2^(f+total targetWord)*(2*u)=2^total targetWord*(2*(2^f*u)) := by
    rw [Nat.pow_add]
    ac_rfl
  rw [oldFactor,newFactor] at compared
  have scaled : 2^total targetWord*v≤2^total targetWord*(2*(2^f*u)) := by omega
  have bound : v≤2*(2^f*u) :=
    Nat.le_of_mul_le_mul_left scaled (Nat.pow_pos (by decide))
  have vp : 0<v := by
    have power : 0<3^front.length := Nat.pow_pos (by decide)
    have p := Nat.mul_pos power active.1
    by_cases zero : v=0
    · simp only [zero,Nat.mul_zero] at targetIdentity
      omega
    · omega
  exact ⟨vp,by omega⟩

/-- Repaying all accumulated clocks permits retaining the original even run. -/
theorem synchronized_prefix_interval (source target e q u v : Nat)
    (front targetWord : List Nat) (even : 1≤e)
    (parent : source=2^e*q) (active : Interval source target)
    (sourcePath : Prefix q front u) (targetPath : Prefix target targetWord v)
    (nonempty : front≠[]) (length : targetWord.length=front.length)
    (time : total front≤total targetWord)
    (corrections : correction targetWord≤correction front) :
    Interval (2^e*u) v :=
  funded_prefix_interval source target e e q u v front targetWord even parent active
    sourcePath targetPath nonempty length (by omega) corrections

/-- Whole-witness synchronization returns below the ORIGINAL source grade.
The entire supplied suffix survives; no output convergence witness is reused. -/
theorem whole_prefix_rewrite (source target e v : Nat) (front targetWord tail : List Nat)
    (even : 1≤e) (active : Interval source target)
    (cert : PoweredCertificate source e (front++tail))
    (targetPath : Prefix target targetWord v)
    (nonempty : front≠[]) (length : targetWord.length=front.length)
    (time : total front≤total targetWord)
    (corrections : correction targetWord≤correction front) :
    ∃ u, Certificate u tail ∧
      PoweredCertificate (2^e*u) e tail ∧ Interval (2^e*u) v ∧
      Less (grades e tail) (grades e (front++tail)) ∧
      clock e tail+total front=clock e (front++tail) ∧
      (Basin target ↔ Basin v) := by
  obtain ⟨q,parent,sourceCert⟩ := cert
  obtain ⟨u,sourcePath,tailCert⟩ := split_certificate q front tail sourceCert
  refine ⟨u,tailCert,⟨u,rfl,tailCert⟩,?_,prefix_rank e front tail nonempty,?_,
    prefix_basin targetPath⟩
  · exact synchronized_prefix_interval source target e q u v front targetWord even
      parent active sourcePath targetPath nonempty length time corrections
  · simp [clock,total_append,Nat.add_left_comm,Nat.add_comm]

/-- At each proper odd-step prefix, the target has consumed no more clock
than the source. The final cumulative totals are deliberately unrestricted. -/
inductive PrefixClockOrder : List Nat → List Nat → Prop
  | nil : PrefixClockOrder [] []
  | snoc (source target : List Nat) (a b : Nat)
      (previous : PrefixClockOrder source target) (budget : total target≤total source) :
      PrefixClockOrder (source++[a]) (target++[b])

theorem prefix_order_length (front targetWord : List Nat)
    (order : PrefixClockOrder front targetWord) : targetWord.length=front.length := by
  induction order with
  | nil => rfl
  | snoc source target a b previous budget ih => simpa using ih

theorem prefix_order_correction (front targetWord : List Nat)
    (order : PrefixClockOrder front targetWord) : correction targetWord≤correction front := by
  induction order with
  | nil => exact Nat.le_refl _
  | snoc source target a b previous budget ih =>
    have multiplied := Nat.mul_le_mul_left 3 ih
    have powers := Nat.pow_le_pow_right (by decide : 1≤2) budget
    simp only [correction_append,List.length_cons,List.length_nil,correction,
      Nat.pow_zero,Nat.mul_zero,Nat.add_zero,Nat.mul_one]
    omega

/-- The remaining clock debt can be funded by a consumed source gap. Keeping
the same even run deletes the front; a changed even grade lies below a removed
odd-gap grade. Both alternatives use the original common multiset order. -/
theorem funded_prefix_rank (e f : Nat) (front tail : List Nat) (even : 1≤e)
    (nonempty : front≠[]) (funding : f=e ∨ ∃ a∈front, f<a) :
    Less (grades f tail) (grades e (front++tail)) := by
  rcases funding with same | ⟨a,mem,small⟩
  · subst f
    exact prefix_rank e front tail nonempty
  · have base : Less (if f=0 then [] else [2*f+1])
        ([2*e+1]++front.map (2*·)) := by
      apply replace_many _ _ (by simp)
      intro b hb
      by_cases zero : f=0
      · simp [zero] at hb
      · have eq : b=2*f+1 := by simpa [zero] using hb
        refine ⟨2*a,?_,by omega⟩
        apply List.mem_append_right
        exact List.mem_map.mpr ⟨a,mem,rfl⟩
    have full := (less_append_right_iff (if f=0 then [] else [2*f+1])
      ([2*e+1]++front.map (2*·)) (tail.map (2*·))).mpr base
    simpa [grades,show e≠0 by omega,List.map_append,List.append_assoc] using full

/-- A first clock repayment need only reach the deficit paid by one removed
source gap. No intermediate rank comparisons or new output certificates are
used. This includes arbitrarily long excursions above the original rank. -/
theorem funded_repayment_rule (source target e f v : Nat)
    (front targetWord tail : List Nat) (even : 1≤e) (active : Interval source target)
    (cert : PoweredCertificate source e (front++tail))
    (targetPath : Prefix target targetWord v) (nonempty : front≠[])
    (order : PrefixClockOrder front targetWord)
    (repaid : e+total front≤f+total targetWord)
    (funding : f=e ∨ ∃ a∈front, f<a)
    (ih : CollatzGapComparison.Hyp Interval (grades e (front++tail))) : Basin target := by
  obtain ⟨q,parent,sourceCert⟩ := cert
  obtain ⟨u,sourcePath,tailCert⟩ := split_certificate q front tail sourceCert
  have childActive := funded_prefix_interval source target e f q u v front targetWord
    even parent active sourcePath targetPath nonempty
    (prefix_order_length front targetWord order) repaid
    (prefix_order_correction front targetWord order)
  have drop := funded_prefix_rank e f front tail even nonempty funding
  have child := ih (2^f*u) v f tail childActive ⟨u,rfl,tailCert⟩ drop
  exact (prefix_basin targetPath).mpr child

/-- Any first repayment of the target's cumulative source-clock deficit
closes in the original multiset induction, regardless of intermediate debt.
This is an actual path rule, not an assertion that a repayment must occur. -/
theorem first_repayment_rule (source target e v : Nat) (front targetWord tail : List Nat)
    (even : 1≤e) (active : Interval source target)
    (cert : PoweredCertificate source e (front++tail))
    (targetPath : Prefix target targetWord v) (nonempty : front≠[])
    (order : PrefixClockOrder front targetWord) (repaid : total front≤total targetWord)
    (ih : CollatzGapComparison.Hyp Interval (grades e (front++tail))) : Basin target := by
  obtain ⟨u,_,child,childActive,drop,_,link⟩ :=
    whole_prefix_rewrite source target e v front targetWord tail even active cert
      targetPath nonempty (prefix_order_length front targetWord order) repaid
      (prefix_order_correction front targetWord order)
  exact link.mpr (ih (2^e*u) v e tail childActive child drop)

/-- Put the compensating target halving run at the END of the entire word.
Only source length and total are used; the individual source gaps are free. -/
def delayedWord (front : List Nat) : List Nat :=
  repeatHead 1 (front.length-1) [total front-front.length+1]

theorem delayed_stats (front : List Nat) (nonempty : front≠[])
    (positive : PositiveGaps front) :
    PositiveGaps (delayedWord front) ∧
      (delayedWord front).length=front.length ∧
      total (delayedWord front)=total front ∧
      correction (delayedWord front)≤correction front := by
  have lp : 0<front.length := List.length_pos_iff.mpr nonempty
  have bound := length_le_total front positive
  have length : (delayedWord front).length=front.length := by
    simp only [delayedWord,repeatHead_length,List.length_cons,List.length_nil]
    omega
  have time : total (delayedWord front)=total front := by
    simp only [delayedWord,repeatHead_total,total,Nat.one_mul]
    omega
  have legal : PositiveGaps (delayedWord front) := by
    apply repeatHead_positive 1 _ _ (by decide)
    intro a mem
    have eq := List.mem_singleton.mp mem
    omega
  have minimal := ones_correction (front.length-1) (total front-front.length+1)
  have index : front.length-1+1=front.length := by omega
  rw [index] at minimal
  change correction (delayedWord front)+2^front.length=3^front.length at minimal
  have comparison := minimal_correction_bound front positive
  exact ⟨legal,length,time,by omega⟩

/-- An unbounded actual coverage family: any supplied nonempty source prefix
can be consumed against its delayed target word, even through initially
forbidden target gap-one steps. -/
theorem delayed_repayment_rule (source target e v : Nat) (front tail : List Nat)
    (even : 1≤e) (active : Interval source target)
    (cert : PoweredCertificate source e (front++tail))
    (targetPath : Prefix target (delayedWord front) v) (nonempty : front≠[])
    (ih : CollatzGapComparison.Hyp Interval (grades e (front++tail))) : Basin target := by
  have positive : PositiveGaps front := by
    obtain ⟨q,_,qc⟩ := cert
    intro a mem
    exact qc.1 a (List.mem_append_left tail mem)
  obtain ⟨_,length,time,corrections⟩ := delayed_stats front nonempty positive
  obtain ⟨u,_,child,childActive,drop,_,link⟩ :=
    whole_prefix_rewrite source target e v front (delayedWord front) tail
      even active cert targetPath nonempty length (Nat.le_of_eq time.symm) corrections
  exact link.mpr (ih (2^e*u) v e tail childActive child drop)

/-- A direct integral affine guard constructs the entire delayed target path. -/
theorem delayed_target_prefix (target v : Nat) (front : List Nat)
    (nonempty : front≠[]) (positive : PositiveGaps front)
    (guard : 3^front.length*(target+1)=2^front.length+2^total front*v) :
    Prefix target (delayedWord front) v := by
  obtain ⟨legal,length,time,_⟩ := delayed_stats front nonempty positive
  have lp : 0<front.length := List.length_pos_iff.mpr nonempty
  have minimal := ones_correction (front.length-1) (total front-front.length+1)
  have index : front.length-1+1=front.length := by omega
  rw [index] at minimal
  change correction (delayedWord front)+2^front.length=3^front.length at minimal
  simp only [Nat.mul_add,Nat.mul_one] at guard
  refine ⟨legal,?_⟩
  have identity : 3^front.length*target+correction (delayedWord front)=
      2^total front*v := by omega
  simpa [length,time] using identity

/-- The delayed family can be activated directly from its exact arithmetic
identity, without supplying intermediate target iterates or a target witness. -/
theorem delayed_affine_rule (source target e v : Nat) (front tail : List Nat)
    (even : 1≤e) (active : Interval source target)
    (cert : PoweredCertificate source e (front++tail)) (nonempty : front≠[])
    (guard : 3^front.length*(target+1)=2^front.length+2^total front*v)
    (ih : CollatzGapComparison.Hyp Interval (grades e (front++tail))) : Basin target := by
  have positive : PositiveGaps front := by
    obtain ⟨q,_,qc⟩ := cert
    intro a mem
    exact qc.1 a (List.mem_append_left tail mem)
  exact delayed_repayment_rule source target e v front tail even active cert
    (delayed_target_prefix target v front nonempty positive guard) nonempty ih

/-- This concrete residual family starts with the previously forbidden
target gap one and repays it on the second source gap. -/
theorem two_twos_residue_rule (source target e : Nat) (tail : List Nat)
    (even : 1≤e) (active : Interval source target)
    (cert : PoweredCertificate source e ([2,2]++tail))
    (residue : target%16=3)
    (ih : CollatzGapComparison.Hyp Interval (grades e ([2,2]++tail))) :
    Basin target := by
  have path : Prefix target (delayedWord [2,2]) (9*(target/16)+2) := by
    refine ⟨by simp [PositiveGaps,delayedWord,repeatHead,total],?_⟩
    change 9*target+5=16*(9*(target/16)+2)
    omega
  exact delayed_repayment_rule source target e _ [2,2] tail even active cert path
    (by decide) ih

/-- Delete the initial even run in addition to a nonempty supplied prefix. -/
theorem odd_tail_rank (e : Nat) (front tail : List Nat) (even : 1≤e)
    (nonempty : front≠[]) : Less (grades 0 tail) (grades e (front++tail)) := by
  have erased := replace_one_with_tail (2*e+1) [] (tail.map (2*·)) (by simp)
  have first : Less (grades 0 tail) (grades e tail) := by
    simpa [grades,show e≠0 by omega] using erased
  exact less_trans first (prefix_rank e front tail nonempty)

/-- The low-even psi branch with e=1 and first gap2 needs only that one gap.
Its actual target prefix [1,3] merges with psi at the literal source tail. -/
theorem psi_head_two_handoff (source : Nat) (tail : List Nat)
    (cert : PoweredCertificate source 1 (2::tail)) :
    ∃ u, 0<u ∧ u<source ∧ 3*source+2=8*u ∧ Certificate u tail ∧
      Less (grades 0 tail) (grades 1 (2::tail)) ∧
      (Basin (2*source-1) ↔ Basin (2*u-1)) := by
  obtain ⟨q,parent,sourceCert⟩ := cert
  obtain ⟨_,u,edge,tailCert⟩ := (certificate_cons_iff q 2 tail).mp sourceCert
  have qo := witness_odd (certificate_witness sourceCert)
  have uo := witness_odd (certificate_witness tailCert)
  change source=2*q at parent
  change 3*q+1=4*u at edge
  have path : Prefix (2*source-1) [1,3] (3*u-1) := by
    refine ⟨by simp [PositiveGaps],?_⟩
    change 9*(2*source-1)+5=16*(3*u-1)
    omega
  refine ⟨u,by omega,by omega,by omega,tailCert,?_,?_⟩
  · exact odd_tail_rank 1 [2] tail (by decide) (by decide)
  · exact (prefix_basin path).trans (CollatzClosure.basin_psi u (by omega)).symm

theorem psi_head_two_rule (source : Nat) (tail : List Nat)
    (cert : PoweredCertificate source 1 (2::tail))
    (ih : CollatzGapComparison.Hyp Interval (grades 1 (2::tail))) :
    Basin (2*source-1) := by
  obtain ⟨u,positive,_,_,tailCert,drop,link⟩ := psi_head_two_handoff source tail cert
  apply link.mpr
  exact ih u (2*u-1) 0 tail ⟨by omega,by omega⟩
    ⟨u,by simp,tailCert⟩ drop

/-- At e=2 or3, four supplied gap-twos merge with the SAME carry 3u-2.
The target uses five odd steps, while only four source odd steps are removed. -/
theorem psi_four_twos_handoff (source e : Nat) (tail : List Nat)
    (level : e=2 ∨ e=3)
    (cert : PoweredCertificate source e ([2,2,2,2]++tail)) :
    ∃ u, 0<u ∧ u<source ∧
      81*source+175*2^e=256*(2^e*u) ∧ Certificate u tail ∧
      Less (grades 0 tail) (grades e ([2,2,2,2]++tail)) ∧
      (Basin (2*source-1) ↔ Basin (3*u-2)) := by
  obtain ⟨q,parent,sourceCert⟩ := cert
  obtain ⟨u,sourcePath,tailCert⟩ :=
    split_certificate q [2,2,2,2] tail sourceCert
  have qo := witness_odd (certificate_witness sourceCert)
  have uo := witness_odd (certificate_witness tailCert)
  have edge : 81*q+175=256*u := sourcePath.2
  have rank := odd_tail_rank e [2,2,2,2] tail (by omega) (by decide)
  rcases level with two | three
  · subst e
    change source=4*q at parent
    have path : Prefix (2*source-1) [1,1,2,3,4] (3*u-2) := by
      refine ⟨by simp [PositiveGaps],?_⟩
      change 243*(2*source-1)+347=2048*(3*u-2)
      omega
    refine ⟨u,by omega,by omega,?_,tailCert,rank,prefix_basin path⟩
    change 81*source+700=256*(4*u)
    omega
  · subst e
    change source=8*q at parent
    have path : Prefix (2*source-1) [1,1,1,5,4] (3*u-2) := by
      refine ⟨by simp [PositiveGaps],?_⟩
      change 243*(2*source-1)+451=4096*(3*u-2)
      omega
    refine ⟨u,by omega,by omega,?_,tailCert,rank,prefix_basin path⟩
    change 81*source+1400=256*(8*u)
    omega

/-- These low-even psi families close using the original interval hypothesis;
no unproved carry closure premise is added. -/
theorem psi_four_twos_rule (source e : Nat) (tail : List Nat)
    (level : e=2 ∨ e=3)
    (cert : PoweredCertificate source e ([2,2,2,2]++tail))
    (ih : CollatzGapComparison.Hyp Interval (grades e ([2,2,2,2]++tail))) :
    Basin (2*source-1) := by
  obtain ⟨u,positive,_,_,tailCert,drop,link⟩ :=
    psi_four_twos_handoff source e tail level cert
  apply link.mpr
  apply CollatzLowGapGlobal.odd_source_cap u (3*u-2) tail tailCert (by omega) (by omega)
  intro s t f word active child decrease
  exact ih s t f word active child (less_trans decrease drop)

end CollatzClockSynchronization
