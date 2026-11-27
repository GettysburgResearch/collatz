module

public import FinalProposal
public import EscapeRecords
public import WindowCapture
import all FixedGate

public section
namespace Collatz.Itinerary.NovemberProposal

open FixedGate ClockRecurrence CycleAmplification
set_option autoImplicit false

/-- An uncorrected coefficient bound on each individual positive odd unit,
together with the cofinal negative cycle tests, is equivalent to Collatz.
Both right-hand conditions are obligations, with no assumed axiom. -/
theorem universal_iff_bounded_clocks_and_cycle_tests : Universal ↔
    (∀ (a : Nat) (c : Bool), a%2=1 → a%3=digit c →
      ∃ M, ∀ k, 3^k ≤ M*2^(elapsed k a)) ∧
    (∀ N, ∃ b, N≤b ∧ witnessTest b=false) := by
  constructor
  · intro all
    obtain ⟨crosses,tests⟩ := Proposal.final_proposal.mp all
    refine ⟨?_,tests⟩
    intro a c odd col
    apply (EscapeRecords.repeats_iff_bounded_deficit odd col).mp
    apply (repeats_iff_every_tail_crosses odd col).mpr
    intro k
    obtain ⟨_,_,_,odd',d,col'⟩ := route_exists k a odd col
    exact crosses _ d odd' col'
  · rintro ⟨bounds,tests⟩
    apply Proposal.final_proposal.mpr
    refine ⟨?_,tests⟩
    intro a c odd col
    exact crosses_of_repeats odd col ((EscapeRecords.repeats_iff_bounded_deficit odd col).mpr
      (bounds a c odd col))

/-- The finite-window proposal and the two orbitwise obligations give
equivalent criteria using the same ordinary shortcut dynamics. -/
theorem windows_iff_bounded_clocks_and_cycle_tests :
    (∀ N, ∃ k H y, N≤k ∧
      (WindowCapture.misses (WindowCapture.window k) H y).length<WindowCapture.quota k (k/2)) ↔
    (∀ (a : Nat) (c : Bool), a%2=1 → a%3=digit c →
      ∃ M, ∀ k, 3^k ≤ M*2^(elapsed k a)) ∧
    (∀ N, ∃ b, N≤b ∧ witnessTest b=false) :=
  WindowCapture.universal_iff_window_capture.symm.trans universal_iff_bounded_clocks_and_cycle_tests

#print axioms universal_iff_bounded_clocks_and_cycle_tests
#print axioms windows_iff_bounded_clocks_and_cycle_tests
end Collatz.Itinerary.NovemberProposal
