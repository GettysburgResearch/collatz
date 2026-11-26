import PositiveWordDescent
import FinalProofProposal

/-! New proved ordinary cases of the existing closing proposal. The residual
universal proposition remains OPEN; it is an explicit theorem parameter. -/
namespace SourceProgressCases
open CollatzReverseBasin CollatzTwoOdd FinalProofProposal

/-- A finite, source-dependent ordinary word test, with the terminal cofactor
and all clocks tied to the same supplied positive source. -/
def TailCase (z : Nat) : Prop :=
  ∃ q t a : Nat, t % 2 = 1 ∧ 81*z+271 = 128*2^q*t ∧
    WordRank.word (q+40+a) (WordRank.run a (WordRank.run (q+8) z)) =
      List.replicate (q+40+a) false

theorem tail_case_progress (z : Nat) (hz : z%48=17) (h : TailCase z) :
    SourceProgress z := by
  obtain ⟨q,t,a,ot,eq,bits⟩ := h
  obtain ⟨positive,drop,same⟩ := PositiveWordDescent.delayed_tail_drop q z t a hz ot eq bits
  exact Or.inr ⟨_,positive,drop,same⟩

/-- The new pointwise test excludes an actual least reverse defect, using
the already proved quantitative return. There is no analytic input. -/
theorem least_defect_not_tail (z : Nat) (hz : ReverseDefect z)
    (least : ∀ w : Nat, ReverseDefect w → z ≤ w) : ¬TailCase z := by
  intro h
  rcases tail_case_progress z hz.1 h with good | ⟨n,positive,drop,same⟩
  · exact hz.2.2 good
  · obtain ⟨w,bad,bound⟩ := quantitative_return n positive (fun good => hz.2.2 (same.mp good))
    have lower := least w bad
    omega

private theorem odds_agree (j x : Nat) : WordRank.odds j x = CollatzTwoOdd.odds j x := by
  induction j generalizing x with
  | zero => rfl
  | succ j ih => exact congrArg (fun n => x%2+n) (ih (shortcut x))

/-- Cofinal genuinely progressing sources in every prescribed finite lower
word, at every upper first-hit rank above an explicit uniform threshold. -/
theorem dense_closing_cases (q : Nat) (hq : 2≤q) (W : List Bool) (r L : Nat)
    (hr : q+44+2*W.length≤r) :
    ∃ z t J : Nat, L≤z ∧ z%48=17 ∧ 81*z+271=128*2^q*t ∧
      WordRank.word W.length (WordRank.run (q+8) z)=W ∧
      Hits (3*z) J ∧ (∀ i<J, ¬Hits (3*z) i) ∧
      CollatzTwoOdd.odds J (3*z)=r ∧ SourceProgress z := by
  obtain ⟨z,t,J,n,size,hz,eq,_,_,word,hit,first,rank,_,positive,drop,same⟩ :=
    PositiveWordDescent.dense_progress q hq W r L hr
  refine ⟨z,t,J,size,hz,eq,word,hit,first,?_,Or.inr ⟨n,positive,drop,same⟩⟩
  exact (odds_agree J (3*z)).symm.trans rank

/-- OPEN. This is the original all-rank progress requirement restricted to
sources not covered by the new proved finite test. -/
def RemainingProgress : Prop :=
  ∀ z j : Nat, z%48=17 → Hits (3*z) j →
    3 ≤ CollatzTwoOdd.odds j (3*z) → ¬TailCase z → SourceProgress z

theorem collatz_from_remaining (remaining : RemainingProgress) : UniversalConvergence := by
  apply collatz_from_proposal
  intro z j hz hit rank
  by_cases tail : TailCase z
  · exact tail_case_progress z hz tail
  · exact remaining z j hz hit rank tail

theorem collatz_iff_remaining : UniversalConvergence ↔ RemainingProgress := by
  constructor
  · intro all z _ hz _ _ _
    exact Or.inl (all z (by omega))
  · exact collatz_from_remaining

#print axioms tail_case_progress
#print axioms least_defect_not_tail
#print axioms dense_closing_cases
#print axioms collatz_from_remaining
#print axioms collatz_iff_remaining
end SourceProgressCases
