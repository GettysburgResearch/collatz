import FinalProofProposal
import ShadowTernaryRescue
import ShadowTernaryDigits

namespace DefectClockFloor

open CollatzReverseBasin CollatzTwoOdd FinalProofProposal WordRank

/-- Each measured count refers to the supplied source, at its actual clock h. -/
theorem source_progress (x h B : Nat) (pos : 0<x) (bound : B≤2720)
    (budget : (3*B+1)^(WordRank.odds h x)*2^40 < B^(WordRank.odds h x)*2^h) :
    SourceProgress x := by
  by_cases good : Basin x
  · exact Or.inl good
  · exact Or.inr ⟨run h x,OddClockFloor.run_pos h x pos,
      OddClockFloor.bad_drop h B x (2^40) bound pos good budget,
      PositiveWordDescent.basinRun h x⟩

/-- A least reverse defect satisfies the all-clock lower bound without
any size assumption on the source or any restriction on upper rank. -/
theorem least_all_clocks (z : Nat) (bad : ReverseDefect z)
    (least : ∀ w, ReverseDefect w → z≤w) (h B : Nat) (bound : B≤2720) :
    B^(WordRank.odds h z)*2^h ≤ (3*B+1)^(WordRank.odds h z)*2^40 := by
  by_contra! budget
  have pos : 0<z := by have := bad.1; omega
  rcases source_progress z h B pos bound budget with good|⟨y,hp,drop,same⟩
  · exact bad.2.2 good
  · obtain ⟨v,hv,upper⟩ := quantitative_return y hp (fun g => bad.2.2 (same.mp g))
    have lower := least v hv
    omega

theorem least_1024 (z : Nat) (bad : ReverseDefect z)
    (least : ∀ w, ReverseDefect w → z≤w) : 621 ≤ WordRank.odds 1024 z := by
  have pos : 0<z := by have := bad.1; omega
  by_contra! below
  have hit := (OddClockFloor.bad_clock_1024 z pos bad.2.2).mpr (by omega)
  have smallBad : ¬Basin (run 1024 z) := fun good => bad.2.2 ((PositiveWordDescent.basinRun _ _).mp good)
  obtain ⟨w,hw,upper⟩ := quantitative_return _ (OddClockFloor.run_pos _ _ pos) smallBad
  have lower := least w hw
  omega

/-- The existing opposite-arm progression, now attached to the specified
parent and the unconditional quantitative return. -/
theorem least_not_ternary_row (k z : Nat) (bad : ReverseDefect z)
    (least : ∀ w, ReverseDefect w → z≤w)
    (parent : 81*z+527=512*2^(98+162*(181+2187*k))) : False :=
  ShadowTernaryRescue.ternary_row_excluded k z bad least quantitative_return parent

/-- On this progression the supplied simultaneous-shadow parameter is itself
excluded. The two delayed checkpoint comparisons need not succeed. -/
theorem least_not_simultaneous_shadow_row (u z : Nat) (bad : ReverseDefect z)
    (least : ∀ w, ReverseDefect w → z≤w)
    (parent : 81*z+527=512*2^(98+162*ShadowTernaryDigits.index (2034+2187*u))) : False :=
  ShadowTernaryRescue.simultaneous_shadow_rescue u _ z
    (ShadowTernaryDigits.shadow_equation _) parent bad least quantitative_return

#print axioms source_progress
#print axioms least_all_clocks
#print axioms least_1024
#print axioms least_not_ternary_row
#print axioms least_not_simultaneous_shadow_row
end DefectClockFloor
