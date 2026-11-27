module

public import PassageGatePacking
public import PassageGateSublinear
import all PassageGateSublinear
import all PassageGatePacking
import all TernaryItinerary
import all HourTower
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageGate

open Finset HourTower
set_option autoImplicit false

/-- Exact integer count of the native inputs that clear every chosen
prefix barrier in the packet (0, 2^h]. -/
noncomputable def survivingPacket (h : ℕ) (bank : ℕ → ℕ) : Finset ℕ := by
  classical
  exact (sites Set.univ h).filter fun z =>
    ∀ t ≤ h, 2^(h-bank t) < 3^(count t z)*2^(h-t)

/-- A different drop margin may be prescribed at every inspected tick.
A fixed time shift counts its own smaller packet. Only h final sites
are discarded in total. -/
theorem moving_packet (x n h : ℕ) (bank : ℕ → ℕ) (positive : 0 < x)
    (simple : (Set.Iio n).InjOn (fun i => run i x)) :
    (visitSet x n h).card ≤ (survivingPacket h bank).card + h +
      ∑ t ∈ range (h+1), (visitSet x n (h-bank t)).card := by
  classical
  let data := visitSet x n h
  let keep := data.filter (fun i => run i x ∈ survivingPacket h bank)
  let late := Ico (n-h) n
  let hit (t : ℕ) := data.filter (fun i => i+h<n ∧
    3^(count t (run i x))*2^(h-t)≤2^(h-bank t))
  have cover : data ⊆ (keep ∪ late) ∪ (range (h+1)).biUnion hit := by
    intro i hi
    obtain ⟨idx,ht⟩ := mem_filter.mp hi
    have it := mem_range.mp idx
    by_cases ends : n ≤ i+h
    · apply mem_union_left
      apply mem_union_right
      exact mem_Ico.mpr ⟨by omega,it⟩
    by_cases alive : run i x ∈ survivingPacket h bank
    · exact mem_union_left _ (mem_union_left _ (mem_filter.mpr ⟨hi,alive⟩))
    have isSite : run i x ∈ sites Set.univ h := in_sites.mpr ⟨positive_run _ _ positive,ht,trivial⟩
    simp only [survivingPacket,mem_filter,isSite,true_and,not_forall,not_lt] at alive
    obtain ⟨t,le,small⟩ := alive
    apply mem_union_right
    exact mem_biUnion.mpr ⟨t,mem_range.mpr (by omega),mem_filter.mpr ⟨hi,by omega,small⟩⟩
  have keepBound : keep.card ≤ (survivingPacket h bank).card := by
    apply card_le_card_of_injOn (fun i => run i x)
    · intro i hi
      exact (mem_filter.mp hi).2
    · intro i hi j hj eqn
      exact simple (mem_range.mp (mem_filter.mp (mem_filter.mp hi).1).1)
        (mem_range.mp (mem_filter.mp (mem_filter.mp hj).1).1) eqn
  have hitBound (t : ℕ) (le : t≤h) : (hit t).card ≤ (visitSet x n (h-bank t)).card := by
    apply card_le_card_of_injOn (fun i : ℕ => i+t)
    · intro i hi
      obtain ⟨dom,early,small⟩ := mem_filter.mp hi
      obtain ⟨_,ht⟩ := mem_filter.mp dom
      apply mem_filter.mpr
      refine ⟨mem_range.mpr (show i+t < n by omega),?_⟩
      rw [run_add]
      have packet : run i x ≤ 2^t*2^(h-t) := by
        rw [←pow_add,show t+(h-t)=h by omega]
        exact ht
      exact (HourTower.upper packet).trans small
    · intro i _ j _ eqn
      change i+t=j+t at eqn
      omega
  have sumBound := sum_le_sum (s:=range (h+1))
    (f:=fun t => (hit t).card) (g:=fun t => (visitSet x n (h-bank t)).card)
    (fun t ht => hitBound t (by have := mem_range.mp ht; omega))
  have lateBound : late.card≤h := by simp [late]; omega
  have big := card_le_card cover
  have both := card_union_le (keep ∪ late) ((range (h+1)).biUnion hit)
  have first := card_union_le keep late
  have many := card_biUnion_le (s:=range (h+1)) (t:=hit)
  change data.card ≤ _
  omega

/-- A single moving-barrier recursion also counts an entire invariant
set when each shift is injective there, with no finite-path endpoint loss. -/
theorem moving_invariant_packet (S : Set ℕ) (h : ℕ) (bank : ℕ → ℕ)
    (forward : ∀ t x, x∈S → run t x∈S)
    (inj : ∀ t, S.InjOn (run t)) :
    (sites S h).card ≤ (survivingPacket h bank).card +
      ∑ t ∈ range (h+1), (sites S (h-bank t)).card := by
  classical
  let hit (t : ℕ) := (sites S h).filter (fun z =>
    3^(count t z)*2^(h-t)≤2^(h-bank t))
  have cover : sites S h ⊆ survivingPacket h bank ∪ (range (h+1)).biUnion hit := by
    intro z hz
    by_cases alive : z ∈ survivingPacket h bank
    · exact mem_union_left _ alive
    have hsite := in_sites.mp hz
    have univ : z ∈ sites Set.univ h := in_sites.mpr ⟨hsite.1,hsite.2.1,trivial⟩
    simp only [survivingPacket,mem_filter,univ,true_and,not_forall,not_lt] at alive
    obtain ⟨t,le,small⟩ := alive
    exact mem_union_right _ (mem_biUnion.mpr
      ⟨t,mem_range.mpr (by omega),mem_filter.mpr ⟨hz,small⟩⟩)
  have hitBound (t : ℕ) (le : t≤h) : (hit t).card ≤ (sites S (h-bank t)).card := by
    apply card_le_card_of_injOn (run t)
    · intro z hz
      obtain ⟨sub,small⟩ := mem_filter.mp hz
      obtain ⟨positive,ht,mem⟩ := in_sites.mp sub
      have packet : z ≤ 2^t*2^(h-t) := by
        rw [←pow_add,show t+(h-t)=h by omega]
        exact ht
      exact in_sites.mpr ⟨positive_run _ _ positive,(HourTower.upper packet).trans small,
        forward _ _ mem⟩
    · intro z hz y hy eqn
      exact inj t (in_sites.mp (mem_filter.mp hz).1).2.2
        (in_sites.mp (mem_filter.mp hy).1).2.2 eqn
  have sumBound := sum_le_sum (s:=range (h+1))
    (f:=fun t => (hit t).card) (g:=fun t => (sites S (h-bank t)).card)
    (fun t ht => hitBound t (by have := mem_range.mp ht; omega))
  have big := card_le_card cover
  have both := card_union_le (survivingPacket h bank) ((range (h+1)).biUnion hit)
  have many := card_biUnion_le (s:=range (h+1)) (t:=hit)
  omega

/-- All positive periodic states, counted simultaneously. -/
theorem moving_periodic_packet (h : ℕ) (bank : ℕ → ℕ) :
    (sites {x | periodicSite x} h).card ≤ (survivingPacket h bank).card +
      ∑ t ∈ range (h+1), (sites {x | periodicSite x} (h-bank t)).card :=
  moving_invariant_packet _ h bank periodic_forward periodic_injective

#print axioms moving_invariant_packet
#print axioms moving_periodic_packet
#print axioms moving_packet
end Collatz.Itinerary.PassageGate
