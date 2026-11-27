module
public import PassageTwoOdds
import all TowerFrontierAffine
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageRootClock
open TowerFrontier PassageAligned
set_option autoImplicit false

theorem clock_three {j x : ℕ} (upper : x<2^(j+1)) :
    (∃ h, track (j+h) x 0=track h 1 0) ↔ track (j+3) x 0=track 3 1 0 := by
  constructor
  · intro aligned
    obtain ⟨q,small,hq⟩ := (three_clocks upper).mp aligned
    interval_cases q
    · change track (j+0) x 0=(1,0) at hq
      rw [Nat.add_zero] at hq
      rw [TowerFrontier.track_add j 3,hq]
    · change track (j+2) x 0=(1,1) at hq
      rw [show j+3=(j+2)+1 by omega,TowerFrontier.track_add (j+2) 1,hq]
      decide
    · change track (j+4) x 0=(1,2) at hq
      rw [show j+4=(j+3)+1 by omega,TowerFrontier.track_add (j+3) 1] at hq
      generalize e : track (j+3) x 0=z at hq ⊢
      obtain ⟨n,p⟩ := z
      change track 1 n p=(1,2) at hq
      change (n,p)=(2,2)
      simp only [track] at hq
      split at hq <;> simp only [Prod.mk.injEq] at hq <;> apply Prod.ext <;> dsimp <;> omega
  · exact fun eq => ⟨3,eq⟩

theorem sharp : 3<2^(1+1) ∧ track (1+3) 3 0=track 3 1 0 ∧
    ∀ h : Fin 3, track (1+h.val) 3 0≠track h.val 1 0 := by decide +kernel

#print axioms clock_three
#print axioms sharp
end Collatz.Itinerary.PassageRootClock
