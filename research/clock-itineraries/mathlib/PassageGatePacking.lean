module

public import HourTower
public import Mathlib.Algebra.BigOperators.Group.Finset.Basic
public import Mathlib.Data.Nat.Choose.Basic
public import Mathlib.Data.Nat.Log
import all HourTower
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageGate

open Finset HourTower
set_option autoImplicit false

private theorem split_sum (m : ℕ) (f : ℕ → ℕ) :
    ∑ t ∈ range (2*m), f t = (∑ t ∈ range m, f (2*t)) + ∑ t ∈ range m, f (2*t+1) := by
  induction m with
  | zero => simp
  | succ m ih =>
    rw [Nat.mul_succ,sum_range_succ,sum_range_succ,ih,sum_range_succ,sum_range_succ]
    omega

private theorem affine_branch (a s t : ℕ) :
    step (a+2*(s*t))=step a+(if a%2=0 then s else 3*s)*t := by
  unfold step
  rw [show (a+2*(s*t))%2=a%2 by omega]
  split <;> first | omega | rw [Nat.mul_assoc]; omega

/-- Exact native odd-count histogram on a translated packet of odd stride. -/
theorem count_histogram (h a s d : ℕ) (odd : s%2=1) :
    (∑ t ∈ range (2^h), if count h (a+s*t)=d then 1 else 0)=h.choose d := by
  induction h generalizing a s d with
  | zero =>
    cases d <;> simp [count]
  | succ h ih =>
    have arm (z : ℕ) :
        (∑ t ∈ range (2^h), if count (h+1) (z+2*(s*t))=d then 1 else 0)=
          if z%2≤d then h.choose (d-z%2) else 0 := by
      let b := if z%2=0 then s else 3*s
      have bo : b%2=1 := by dsimp [b]; split <;> simp [Nat.mul_mod,odd]
      have expr (t : ℕ) : count (h+1) (z+2*(s*t))=count h (step z+b*t)+z%2 := by
        rw [count,affine_branch,show (z+2*(s*t))%2=z%2 by omega]
      by_cases lo : z%2≤d
      · rw [ite_eq_left lo,←ih (step z) b (d-z%2) bo]
        apply sum_congr rfl
        intro t _
        rw [expr]
        simp only [show count h (step z+b*t)+z%2=d ↔ count h (step z+b*t)=d-z%2 by omega]
      · rw [ite_eq_right lo]
        apply sum_eq_zero
        intro t _
        rw [expr,ite_eq_right (by omega)]
    rw [pow_succ,Nat.mul_comm (2^h) 2,split_sum]
    have first (t : ℕ) : a+s*(2*t)=a+2*(s*t) := by ac_rfl
    have second (t : ℕ) : a+s*(2*t+1)=a+s+2*(s*t) := by
      rw [Nat.mul_add,Nat.mul_one]; ac_rfl
    simp only [first,second,arm]
    by_cases even : a%2=0
    · have next : (a+s)%2=1 := by omega
      cases d with
      | zero => simp [even,next]
      | succ d => simp [even,next,Nat.choose_succ_succ,Nat.add_comm]
    · have ao : a%2=1 := by omega
      have next : (a+s)%2=0 := by omega
      cases d with
      | zero => simp [ao,next]
      | succ d => simp [ao,next,Nat.choose_succ_succ]

/-- Number of binary parity strings with at least k ones in h ticks. -/
def tail (h k : ℕ) : ℕ := ∑ d ∈ Icc k h, h.choose d

theorem high_census (h k : ℕ) :
    ((range (2^h)).filter (fun t => k≤count h (1+t))).card=tail h k := by
  have hist (d : ℕ) :
      ((range (2^h)).filter (fun t => count h (1+t)=d)).card=h.choose d := by
    simpa using count_histogram h 1 1 d (by decide)
  rw [tail,←sum_congr rfl (fun d _ => hist d)]
  rw [sum_card_fiberwise_eq_card_filter]
  congr 1
  apply filter_congr
  intro t _
  simp [count_le]

/-- On the complete dyadic packet the integer rounding gives an exact
bound without a separate affine-carry error. -/
theorem low_count_lands {h r x : ℕ} (ht : x≤2^h)
    (low : count h x≤Nat.log 3 (2^r)) : run h x≤2^r := by
  have up : run h x≤3^(count h x) := by
    simpa using HourTower.upper (h:=h) (n:=x) (t:=1) (by simpa using ht)
  exact up.trans ((Nat.pow_le_pow_right (by decide : 0<3) low).trans
    (Nat.pow_log_le_self 3 (by positivity)))

/-- Positive sites of the specified set in (0,2^h]. -/
noncomputable def sites (S : Set ℕ) (h : ℕ) : Finset ℕ := by
  classical exact (Icc 1 (2^h)).filter (· ∈ S)

private theorem in_sites {S : Set ℕ} {h x : ℕ} :
    x ∈ sites S h ↔ 0<x ∧ x≤2^h ∧ x∈S := by
  classical simp [sites,and_assoc,Nat.succ_le_iff]

/-- Finitely many distinct input sites in one packet with a high native count. -/
private theorem high_sites (S : Set ℕ) (h k : ℕ) :
    ((sites S h).filter (fun x => k≤count h x)).card≤tail h k := by
  rw [←high_census]
  apply card_le_card_of_injOn (fun x : ℕ => x-1)
  · intro x hx
    obtain ⟨hx,hi⟩ := mem_filter.mp hx
    obtain ⟨pos,upper,_⟩ := in_sites.mp hx
    change x-1∈(range (2^h)).filter (fun t => k≤count h (1+t))
    exact mem_filter.mpr ⟨mem_range.mpr (by omega),by simpa [show 1+(x-1)=x by omega] using hi⟩
  · intro x hx y hy eqn
    have xp := (in_sites.mp (mem_filter.mp hx).1).1
    have yp := (in_sites.mp (mem_filter.mp hy).1).1
    change x-1=y-1 at eqn
    omega

private theorem positive_run (h x : ℕ) (pos : 0<x) : 0<run h x := by
  induction h generalizing x with
  | zero => exact pos
  | succ h ih => apply ih; unfold step; split <;> omega

/-- A common native clock sends every low-count site into the smaller
packet. The fiber cap is only required on this discarded portion. -/
theorem packet_bound (S : Set ℕ) (h r B : ℕ)
    (forward : ∀ x∈S, run h x∈S)
    (fiber : ∀ y, (((sites S h).filter (fun x => run h x=y))).card≤B) :
    (sites S h).card ≤ tail h (Nat.log 3 (2^r)+1)+B*(sites S r).card := by
  classical
  let k := Nat.log 3 (2^r)+1
  let src := sites S h
  let lo := src.filter (fun x => ¬k≤count h x)
  have maps : (lo : Set ℕ).MapsTo (run h) (sites S r) := by
    intro x hx
    obtain ⟨sub,small⟩ := mem_filter.mp hx
    obtain ⟨pos,ht,inside⟩ := in_sites.mp sub
    exact in_sites.mpr ⟨positive_run _ _ pos,low_count_lands ht (by dsimp [k] at small; omega),
      forward _ inside⟩
  have lowBound : lo.card≤B*(sites S r).card := by
    rw [card_eq_sum_card_fiberwise maps,Nat.mul_comm]
    calc
      _ ≤ ∑ _y ∈ sites S r, B := by
        apply sum_le_sum
        intro y _
        apply le_trans _ (fiber y)
        apply card_le_card
        intro x hx
        exact mem_filter.mpr ⟨(mem_filter.mp (mem_filter.mp hx).1).1,(mem_filter.mp hx).2⟩
      _ = _ := by simp
  have high := high_sites S h k
  have parts := card_filter_add_card_filter_not (s:=src) (fun x => k≤count h x)
  change (src.filter (fun x => k≤count h x)).card+lo.card=src.card at parts
  change (src.filter (fun x => k≤count h x)).card≤tail h k at high
  change src.card≤tail h k+B*(sites S r).card
  omega

def cutoff (h : ℕ) : ℕ := Nat.log 3 (2^h)+1

/-- Budget for first visits on any finite segment, with a native clock
end correction even if the future beyond that segment later repeats. -/
def budget : ℕ → ℕ
  | 0 => 1
  | h+1 => budget h+(h+1)+tail (h+1) (cutoff h)

def visitSet (x n h : ℕ) : Finset ℕ :=
  (range n).filter (fun i => run i x≤2^h)

theorem simple_packet (x n h r : ℕ) (positive : 0<x)
    (simple : (Set.Iio n).InjOn (fun i => run i x)) :
    (visitSet x n h).card≤tail h (cutoff r)+(visitSet x n r).card+h := by
  classical
  let data := visitSet x n h
  let high (i : ℕ) := cutoff r≤count h (run i x)
  have small : (data.filter (fun i => ¬high i)).card≤(visitSet x n r).card+h := by
    let dst := (visitSet x n r)∪Ico n (n+h)
    have le : (data.filter (fun i => ¬high i)).card≤dst.card := by
      apply card_le_card_of_injOn (fun i : ℕ => i+h)
      · intro i hi
        obtain ⟨dom,lo⟩ := mem_filter.mp hi
        obtain ⟨idx,ht⟩ := mem_filter.mp dom
        have ix : i<n := mem_range.mp idx
        by_cases late : i+h<n
        · apply mem_union_left
          apply mem_filter.mpr
          refine ⟨mem_range.mpr late,?_⟩
          rw [run_add]
          exact low_count_lands ht (by dsimp only [high,cutoff] at lo; omega)
        · apply mem_union_right
          apply mem_Ico.mpr
          change n ≤ i + h ∧ i + h < n + h
          omega
      · intro i _ j _ eqn
        change i+h=j+h at eqn
        omega
    exact le.trans (by simpa [dst] using card_union_le (visitSet x n r) (Ico n (n+h)))
  have tall : (data.filter high).card≤tail h (cutoff r) := by
    apply le_trans _ (high_sites Set.univ h (cutoff r))
    apply card_le_card_of_injOn (fun i => run i x)
    · intro i hi
      obtain ⟨dom,ok⟩ := mem_filter.mp hi
      exact mem_filter.mpr ⟨in_sites.mpr ⟨positive_run _ _ positive,(mem_filter.mp dom).2,trivial⟩,ok⟩
    · intro i hi j hj eqn
      exact simple (mem_range.mp (mem_filter.mp (mem_filter.mp hi).1).1)
        (mem_range.mp (mem_filter.mp (mem_filter.mp hj).1).1) eqn
  have parts := card_filter_add_card_filter_not (s:=data) high
  change data.card≤_
  omega

theorem simple_visits (x n h : ℕ) (positive : 0<x)
    (simple : (Set.Iio n).InjOn (fun i => run i x)) :
    (visitSet x n h).card≤budget h := by
  induction h with
  | zero =>
    apply card_le_one.mpr
    intro i hi j hj
    have ie := mem_filter.mp hi
    have je := mem_filter.mp hj
    apply simple (mem_range.mp ie.1) (mem_range.mp je.1)
    have pi := positive_run i x positive
    have pj := positive_run j x positive
    simp only [pow_zero] at ie je
    change run i x=run j x
    obtain ⟨_,li⟩ := ie
    obtain ⟨_,lj⟩ := je
    omega
  | succ h ih =>
    have bound := simple_packet x n (h+1) h positive simple
    rw [budget]
    omega

/-- If the initial n distinct states of one given source all lie below
the indicated gate, the explicit dyadic budget bounds their number. -/
theorem time_before_exit (x n h : ℕ) (positive : 0<x)
    (simple : (Set.Iio n).InjOn (fun i => run i x))
    (below : ∀ i<n, run i x≤2^h) : n≤budget h := by
  have eqn : visitSet x n h=range n := filter_eq_self.mpr (fun i hi => below i (mem_range.mp hi))
  have visits := simple_visits x n h positive simple
  simpa [eqn] using visits

theorem escape_exits_by_budget (x h : ℕ) (positive : 0<x)
    (injective : Function.Injective (fun i => run i x)) :
    ∃ i≤budget h, 2^h<run i x := by
  by_contra! bounded
  have impossible := time_before_exit x (budget h+1) h positive injective.injOn
    (fun i hi => bounded i (by omega))
  omega

#print axioms simple_packet
#print axioms simple_visits
#print axioms time_before_exit
#print axioms escape_exits_by_budget
#print axioms count_histogram
#print axioms high_census
#print axioms low_count_lands
#print axioms packet_bound
end Collatz.Itinerary.PassageGate
