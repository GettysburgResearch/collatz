import AnchorControl
import TemplateChain
import TraceCensus
import LocalDenominator

/-! End-of-pass proposal. `remaining` in the last theorem is OPEN.
The preceding closed theorems do not establish it. The imported cycle and
trace kernels are separate finite results, not assumed universal exclusions. -/

namespace Collatz.RoundEleven
open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.SmoothCore
open Collatz.AnchorDescent

/-- One immediate transfer through phase +1, or a negative periodic phase
of magnitude at most 136. All preperiod and lap clocks are unrestricted. -/
def AnchorTransfer (x y : Nat) : Prop :=
  (∃ a h d t : Nat, 0<a ∧ 0<d ∧ run h a=1 ∧
    x=a+2^h*4^d*t ∧ y=a+2^h*3^d*t) ∨
  (∃ m C h e t : Nat, 0<m ∧ 0<C ∧ C≤136 ∧ 0<e ∧
    negRun h m=C ∧ negRun e C=C ∧
    x+m=2^h*2^e*t ∧ y+m=2^h*3^(negOdds e C)*t)

/-- A closed ordinary countercontrol to complete coverage by this anchor
architecture. Its source reaches 1, and every immediate lower-cone option
from the stated architecture is impossible. -/
theorem convergent_control_outside_anchors :
    Good 3645 ∧ ¬∃ y, AnchorControl.Lower y ∧ AnchorTransfer 3645 y := by
  refine ⟨AnchorControl.control_good,?_⟩
  rintro ⟨y,lower,positive|negative⟩
  · obtain ⟨a,h,d,t,ha,hd,hit,src,dst⟩ := positive
    exact AnchorControl.no_positive ha hd hit src dst lower
  · obtain ⟨m,C,h,e,t,hm,hc,capC,he,hit,lap,src,dst⟩ := negative
    exact AnchorControl.no_negative hm hc capC he hit lap src dst lower

/-- A whole physical descent progression exists at every supplied initial
exponent and positive exponent gain. The base varies with the progression;
this is not coverage of each prescribed base. -/
theorem all_exponents_have_descent (r d : Nat) (hd : 0<d) :
    ∃ b : Nat, 0<b ∧ ∀ t : Nat,
      let h := 2*3^(r+d)
      let w := 3^d*b+2^h*4^d*t
      run h (3^r*w)<w ∧ ¬FirstTower w r := by
  obtain ⟨b,hb,hit,_⟩ := all_exponents r d hd
  refine ⟨b,hb,?_⟩
  intro t
  dsimp only
  refine ⟨grade_gain_native hd hb hit rfl,?_⟩
  intro tower
  exact exclude_first_tower tower hd hb hit rfl

/-- OPEN mathematical input: this is the unchanged ordinary merger
consumer. A standard axiom inventory does not prove `remaining`. -/
theorem final_proposal (remaining : FrontierMerger) :
    ∀ n : Nat, 0<n → Good n :=
  universal_iff_frontier_merger.mpr remaining

#print axioms convergent_control_outside_anchors
#print axioms all_exponents_have_descent
#print axioms final_proposal

end Collatz.RoundEleven
