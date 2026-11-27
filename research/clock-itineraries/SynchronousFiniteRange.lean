module

public import SynchronousBasinCount
import all MinimumDescent
import all WindowCapture

public section
namespace Collatz.Itinerary.SynchronousFiniteRange

open SynchronousBasinCount
set_option autoImplicit false

/-- A finite verified range for ordinary bases already supplies a common
deadline at gate 1 for the whole corresponding stage. -/
theorem zero_misses_of_verified_range (X B : Nat) (size : limit X<B)
    (checked : ∀ x, 0<x → x<B → ReachesOne x) : ∃ O, misses X O 1=[] := by
  have finite (L : Nat) (small : L<B) :
      ∃ O, ∀ x, 0<x → x≤L → ∃ t≤O, run t (run 28 x)=1 := by
    induction L with
    | zero => exact ⟨0,by intro x pos bound; omega⟩
    | succ L ih =>
      obtain ⟨O,prev⟩ := ih (by omega)
      obtain ⟨j,hit⟩ := (MinimumDescent.good_run 28 (L+1)).mpr (checked _ (by omega) small)
      refine ⟨O+j,?_⟩
      intro x pos within
      by_cases eq : x=L+1
      · exact ⟨j,by omega,eq ▸ hit⟩
      · obtain ⟨t,bound,done⟩ := prev x pos (by omega)
        exact ⟨t,by omega,done⟩
  obtain ⟨O,allHit⟩ := finite _ size
  refine ⟨O,List.eq_nil_iff_forall_not_mem.mpr ?_⟩
  intro x member
  obtain ⟨inside,cond⟩ := List.mem_filter.mp member
  have bound := List.mem_range.mp inside
  simp only [Bool.and_eq_true,Bool.not_eq_true',decide_eq_true_eq] at cond
  have reached := (WindowCapture.hitBy_iff O (run 28 x) 1).mpr
    (allHit x cond.1.1.1 (by omega))
  rw [reached] at cond
  simp at cond

/-- Barina's published finite verification is an explicit external input.
The deadline in this conclusion may depend on the stage. -/
theorem below_barina_range (checked : ∀ x, 0<x → x<2^71 → ReachesOne x)
    (X : Nat) (stage : X<9*2^43) : ∃ O, misses X O 1=[] := by
  apply zero_misses_of_verified_range X (2^71) _ checked
  change 268435456*X/9<2361183241434822606848
  change X<79164837199872 at stage
  omega

#print axioms zero_misses_of_verified_range
#print axioms below_barina_range
end Collatz.Itinerary.SynchronousFiniteRange
