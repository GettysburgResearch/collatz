import SourceDeletion

namespace Collatz.ExponentTransport

open Collatz.SourceDeletion

private theorem upper_one (t : Nat) : step (96*t+51)=144*t+77 := by
  unfold step; split <;> omega
private theorem upper_two (t : Nat) : step (144*t+77)=216*t+116 := by
  unfold step; split <;> omega
private theorem upper_three (t : Nat) : step (216*t+116)=108*t+58 := by
  unfold step; split <;> omega
private theorem upper_four (t : Nat) : step (108*t+58)=54*t+29 := by
  unfold step; split <;> omega
private theorem upper_five (t : Nat) : step (54*t+29)=81*t+44 := by
  unfold step; split <;> omega
private theorem transported_one (t : Nat) : step (216*t+117)=324*t+176 := by
  unfold step; split <;> omega
private theorem transported_two (t : Nat) : step (324*t+176)=162*t+88 := by
  unfold step; split <;> omega
private theorem transported_three (t : Nat) : step (162*t+88)=81*t+44 := by
  unfold step; split <;> omega

/-- The source lower arm reaches Y = 24t+13. Its triple and nine times Y
merge on their ordinary trajectories, saving two odd inputs on every tail. -/
theorem exponent_transport (t c : Nat) :
    run 2 (32*t+17)=24*t+13 ∧
    run (c+5) (3*(32*t+17))=run (c+3) (9*(24*t+13)) ∧
    odds (c+5) (3*(32*t+17))=odds (c+3) (9*(24*t+13))+2 := by
  have l₁ : step (32*t+17)=48*t+26 := by unfold step; split <;> omega
  have l₂ : step (48*t+26)=24*t+13 := by unfold step; split <;> omega
  rw [show 3*(32*t+17)=96*t+51 by omega,show 9*(24*t+13)=216*t+117 by omega]
  simp only [run,odds,l₁,l₂,upper_one,upper_two,upper_three,
    upper_four,upper_five,transported_one,transported_two,transported_three]
  refine ⟨True.intro,True.intro,?_⟩
  omega

/-- Extracts literally the same suffix of the supplied hitting certificate.
Every hit of the upper arm already contains the five displayed shortcuts. -/
theorem certificate_transport {t h : Nat} (hit : run h (3*(32*t+17))=1) :
    ∃ k, run k (9*(24*t+13))=1 ∧ odds k (9*(24*t+13))+2=odds h (3*(32*t+17)) := by
  have len : 5≤h := by
    by_contra short
    have small : h=0 ∨ h=1 ∨ h=2 ∨ h=3 ∨ h=4 := by omega
    rw [show 3*(32*t+17)=96*t+51 by omega] at hit
    rcases small with c|c|c|c|c <;> subst h <;>
      simp only [run,upper_one,upper_two,upper_three,upper_four] at hit <;> omega
  let c := h-5
  have eq : h=c+5 := by dsimp [c]; omega
  obtain ⟨_,endpoints,counts⟩ := exponent_transport t c
  rw [eq] at hit ⊢
  exact ⟨c+3,endpoints ▸ hit,counts.symm⟩

/-- After the exponent changes from one to two, the remaining lower and
upper values have a signed offset of one. -/
theorem transported_offset (t : Nat) :
    run 3 (9*(24*t+13))+1 = 9*run 3 (24*t+13) := by
  have l₁ : step (24*t+13)=36*t+20 := by unfold step; split <;> omega
  have l₂ : step (36*t+20)=18*t+10 := by unfold step; split <;> omega
  have l₃ : step (18*t+10)=9*t+5 := by unfold step; split <;> omega
  rw [show 9*(24*t+13)=216*t+117 by omega]
  simp only [run,l₁,l₂,l₃,transported_one,transported_two,transported_three]
  omega

#print axioms exponent_transport
#print axioms certificate_transport
#print axioms transported_offset

end Collatz.ExponentTransport
