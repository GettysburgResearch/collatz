import Residue17Closure
import TwoOddCertificate
import QuantitativeReturn

/-!
A complete kernel-checked consumer for the proposed closing step.
HigherRankProgress remains an OPEN proposition. The quantitative return
is now an unconditional kernel theorem of the imported finite certificates.
The final consumer has only HigherRankProgress as its remaining input.
-/
namespace FinalProofProposal
open CollatzReverseBasin CollatzTwoOdd

def UniversalConvergence : Prop := ∀ n : Nat, 0 < n → Basin n

def QuantitativeReturn : Prop :=
  ∀ n : Nat, 0 < n → ¬ Basin n →
    ∃ w : Nat, ReverseDefect w ∧ w ≤ 2^40 * n

/-- Actual ordinary progress at the supplied source, with the factor needed
to return from its nonbasin endpoint to a strictly smaller reverse defect. -/
def SourceProgress (z : Nat) : Prop :=
  Basin z ∨ ∃ n : Nat, 0 < n ∧ 2^40 * n < z ∧ (Basin n ↔ Basin z)

/-- OPEN. A proof must supply the source progress for every finite upper
certificate having at least three odd inputs. No such proof is provided. -/
def HigherRankProgress : Prop :=
  ∀ z j : Nat, z % 48 = 17 → Hits (3*z) j →
    3 ≤ odds j (3*z) → SourceProgress z

/-- The complete finite certificate supplies the numerical return bound. -/
theorem quantitative_return : QuantitativeReturn :=
  CollatzQuantitativeReturn.bounded_return

theorem upper_has_two_odds (z j : Nat) (hz : z % 48 = 17)
    (hj : Hits (3*z) j) : 2 ≤ odds j (3*z) := by
  let t := z / 16
  have zt : z = 16*t+1 := by dsimp [t]; omega
  have h1 : shortcut (3*z) = 72*t+5 := by
    unfold shortcut
    split <;> omega
  have h2 : shortcut (72*t+5) = 108*t+8 := by
    unfold shortcut
    split <;> omega
  cases j with
  | zero =>
    change 3*z = 1 at hj
    omega
  | succ j =>
    cases j with
    | zero =>
      change shortcut (3*z) = 1 at hj
      rw [h1] at hj
      omega
    | succ k =>
      change 2 ≤ 3*z%2 + (shortcut (3*z)%2 + odds k (shortcut (shortcut (3*z))))
      rw [h1,h2]
      omega

/-- The two-odd layer is established unconditionally by the actual finite
orbits and the 203-step ordinary contraction. -/
theorem two_odd_layer (z j : Nat) (hz : z % 48 = 17)
    (hj : Hits (3*z) j) (ho : odds j (3*z) = 2) : SourceProgress z :=
  two_odd_progress z j hz hj ho

/-- The final assembly is complete. Higher-rank progress remains an OPEN
mathematical input; the quantitative return is proved in the kernel. -/
theorem collatz_from_proposal (higher : HigherRankProgress) : UniversalConvergence := by
  classical
  apply Residue17Closure.collatz_iff_reverse_seventeen.mpr
  intro z
  induction z using Nat.strong_induction_on with
  | h z ih =>
    intro hz good
    by_contra bad
    obtain ⟨j,hj⟩ := good
    have ho := upper_has_two_odds z j hz hj
    have progress : SourceProgress z := by
      by_cases two : odds j (3*z) = 2
      · exact two_odd_layer z j hz hj two
      · exact higher z j hz hj (by omega)
    rcases progress with done | ⟨n,hn,drop,same⟩
    · exact bad done
    · obtain ⟨w,hw,bound⟩ := quantitative_return n hn (fun h => bad (same.mp h))
      have smaller : w < z := lt_of_le_of_lt bound drop
      exact hw.2.2 (ih w smaller hw.1 hw.2.1)

/-- This equivalence makes the remaining logical strength visible. A proof
of HigherRankProgress would be decisive; defining it is not such a proof. -/
theorem collatz_iff_higher_rank :
    UniversalConvergence ↔ HigherRankProgress := by
  constructor
  · intro all z j hz _ _
    exact Or.inl (all z (by omega))
  · exact collatz_from_proposal

#print axioms quantitative_return
#print axioms upper_has_two_odds
#print axioms two_odd_layer
#print axioms collatz_from_proposal
#print axioms collatz_iff_higher_rank
end FinalProofProposal
