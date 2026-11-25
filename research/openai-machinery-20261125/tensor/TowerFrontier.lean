import PositiveTower
import TensorBridge
import SmoothCore

/-! The same positive-shift witnesses in PR #192's original ordinary map,
its first-tower predicate, and the imported independent-block rank model. -/

namespace Collatz.TensorBridge

private theorem itinerary_eq_frontier_run (k n : Nat) :
    Itinerary.run k n = SourceDeletion.run k n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    simp only [Itinerary.run, SourceDeletion.run]
    exact ih _

/-- One singleton batch at each true source and its own clock, followed by
the independently tagged versus integer-aligned rank comparison. -/
def pairRankDrop (F : Type*) [Field F] (n k p l : Nat) : Prop :=
  let f := fun _ : Unit => SourceDeletion.run k n
  let g := fun _ : Unit => SourceDeletion.run l p
  (incidence F (Sum.elim f g)).rank < taggedRank F f g

/-- Every positive tower row has arbitrarily large arithmetic frontier
inputs that cannot be a first bad tower. Their first accelerated odd
target is larger than the base. The certificate uses a true smaller-base
merger, expressible equivalently as a strict rank drop over every field. -/
theorem unbounded_guarded_tower_exclusions (r limit : Nat) (hr : 0<r) :
    ∃ w b j a y : Nat, limit<w ∧ 0<b ∧ b<w ∧
      w%2=1 ∧ w%3≠0 ∧ 0<a ∧ a%2=1 ∧ 3^r*w+1=2*a ∧ 2≤3^r ∧
      (3^r*w)%512≠85 ∧ 3*(3^r*w)+1=4*y ∧ y%2=1 ∧ y%3=1 ∧ w<y ∧
      SourceDeletion.run 1 (3^r*w)=SourceDeletion.run (2*3^r+1) (3^j*b) ∧
      (∀ (F : Type) [Field F], pairRankDrop F (3^r*w) 1 (3^j*b) (2*3^r+1)) ∧
      ¬ SmoothCore.FirstTower w r := by
  obtain ⟨w,b,j,a,y,hw,ha,hb,hbw,hw2,hw3,_,heq,ha2,hsmall,h85,hy,hy2,hwy,meet⟩ :=
    positive_shift_survivors r limit hr
  rw [itinerary_eq_frontier_run, itinerary_eq_frontier_run] at meet
  refine ⟨w,b,j,a,y,hw,hb,hbw,hw2,hw3,ha,ha2,heq,hsmall,h85,hy,hy2,by omega,hwy,meet,?_,?_⟩
  · intro F hF
    exact (rank_drop_iff_meeting F _ _).mpr ⟨(),(),meet⟩
  · intro tower
    have goodComparison := tower.smaller b hb hbw j
    have goodMeeting := (MinimumFailure.good_run (2*3^r+1) _).mpr goodComparison
    rw [← meet] at goodMeeting
    exact tower.bad ((MinimumFailure.good_run 1 _).mp goodMeeting)

end Collatz.TensorBridge
