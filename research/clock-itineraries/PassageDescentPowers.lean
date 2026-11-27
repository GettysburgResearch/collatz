module

public import PassageDescentCover
import all PassageDescentCover
import all ReturnDescent
import all TernaryItinerary

public section

namespace Collatz.Itinerary.PassageDescent

open TowerFrontier ReturnDescent
set_option autoImplicit false
set_option maxHeartbeats 1000000
set_option exponentiation.threshold 1000000

private theorem window_of_degree {b n : Nat} (degree : 2^494 ∣ n) : PowerWindow (b^n) := by
  by_cases hn : n=0
  · subst n
    exact Or.inl rfl
  obtain ⟨s,hs⟩ := degree
  have ns : 3≤n := by omega
  by_cases triple : b%3=0
  · right
    have repr := Nat.mod_add_div b 3
    rw [triple,Nat.zero_add] at repr
    have cube : b^3%27=0 := by rw [←repr,Nat.mul_pow]; omega
    rw [show n=3+(n-3) by omega,Nat.pow_add,Nat.mul_mod,cube]
    simp
  · left
    have b2 : b^2%3=1 := by
      rw [Nat.pow_mod]
      have choice : b%3=1 ∨ b%3=2 := by omega
      rcases choice with h|h <;> rw [h] <;> decide
    have en : n=2*(2^493*s) := by rw [hs,←Nat.mul_assoc]
    rw [en,Nat.pow_mul,Nat.pow_mod,b2,Nat.one_pow]

/-- Every supplied odd-base perfect power with the specified degree has
    an actual pair of ordinary lower trajectories and a six-odd upper bound. -/
theorem odd_power_return {b n : Nat} (odd : b%2=1) (degree : 2^494 ∣ n) :
    let m := 11+162*b^n
    ∃ H p Y, ReturnAt m H p Y ∧ 27*Y<2*hardParent m ∧ H≤m+8 ∧ p≤6 := by
  obtain ⟨H,p,Y,act,_,_,_,_,more⟩ := binary_return (power_parameter odd degree)
  exact ⟨H,p,Y,act,more (window_of_degree degree)⟩

/-- Canonical minimality now suffices without a boundedness or ordinary floor
    hypothesis for every individual input of this binary progression. -/
theorem good_under_canonical_minimality {j : Nat} (binary : ∃ s, j=1+2^496*s)
    (minimal : ∀ y, y%48=17 → y<hardParent (11+162*j) →
      ReachesOne (3*y) → ReachesOne y) : ReachesOne (hardParent (11+162*j)) := by
  obtain ⟨H,p,Y,act,_,half,_⟩ := binary_return binary
  obtain ⟨cls,upper,lower⟩ := act
  have good : ReachesOne (3*Y) := ⟨H,by rw [←track_run H (3*Y) 0,upper]⟩
  exact reaches_of_meets (minimal Y cls (by omega) good) lower

#print axioms odd_power_return
#print axioms good_under_canonical_minimality

end Collatz.Itinerary.PassageDescent
