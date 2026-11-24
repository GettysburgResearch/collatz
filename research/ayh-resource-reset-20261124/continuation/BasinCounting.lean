import CriticalSection
import Mathlib.Data.Finset.Prod

namespace CollatzShell.CriticalCounting
open MarkedCylinders

/-- The four-clock lift begins with at most three halvings. -/
theorem inv4_mod16 (q : Nat) :
    inv4 q % 16 = 4 ∨ inv4 q % 16 = 8 ∨ inv4 q % 16 = 10 ∨ inv4 q % 16 = 5 := by
  unfold inv4
  split <;> omega

/-- After the initial halvings the odd part still hits the prescribed target;
the number of remaining clocks is bounded independently of the exponent of the
outer critical predecessor. -/
theorem remaining_clocks {q s h u : Nat} (unit : q % 3 ≠ 0) (hs : 0 < s)
    (hh : h ≤ 3) (split : lift s q = 2^h*u) :
    orbit (4*s-h) u = q := by
  have path := (lift_spec s q unit).1
  rw [show 4*s = h+(4*s-h) by omega, orbit_add, split, orbit_pad] at path
  exact path

/-- A fixed source with a known post-reset endpoint supplies at most H+1
targets in H clocks. The union bound retains the individual target values. -/
theorem finite_target_bound (sources targets : Finset Nat) (post : Nat → Nat) (H : Nat)
    (cover : ∀ q ∈ targets, ∃ n ∈ sources, ∃ j ≤ H, orbit j (post n) = q) :
    targets.card ≤ sources.card*(H+1) := by
  let choices := sources ×ˢ Finset.range (H+1)
  let eval : Nat × Nat → Nat := fun p => orbit p.2 (post p.1)
  have sub : targets ⊆ choices.image eval := by
    intro q hq
    obtain ⟨n,hn,j,hj,rfl⟩ := cover q hq
    exact Finset.mem_image.mpr ⟨(n,j),Finset.mem_product.mpr ⟨hn,Finset.mem_range.mpr (by omega)⟩,rfl⟩
  calc
    targets.card ≤ (choices.image eval).card := Finset.card_le_card sub
    _ ≤ choices.card := Finset.card_image_le
    _ = _ := by simp [choices]

/-- Finite-scale collision budget for a fixed possibly bad target. If removing
the proposed exceptional sources would make the row too small to cover its
targets, at least one complementary source reaches that target. -/
theorem deletion_witness (sources targets exceptions : Finset Nat) (post : Nat → Nat)
    (H b : Nat)
    (cover : ∀ q ∈ targets, ∃ n ∈ sources, ∃ j ≤ H, orbit j (post n) = q)
    (physical : ∀ n ∈ sources, Hits n (post n))
    (ancestors : ∀ q ∈ targets, Hits q b)
    (budget : exceptions.card*(H+1) < targets.card) :
    ∃ n ∈ sources, n ∉ exceptions ∧ Hits n b := by
  classical
  by_contra! absent
  have small : ∀ q ∈ targets, ∃ n ∈ exceptions, ∃ j ≤ H, orbit j (post n) = q := by
    intro q hq
    obtain ⟨n,hn,j,hj,hx⟩ := cover q hq
    have hit : Hits n b := Hits.trans (physical n hn) (Hits.trans ⟨j,hx⟩ (ancestors q hq))
    exact ⟨n, Classical.byContradiction (fun he => absent n hn he hit),j,hj,hx⟩
  have bound := finite_target_bound exceptions targets post H small
  omega

#print axioms inv4_mod16
#print axioms remaining_clocks
#print axioms finite_target_bound
#print axioms deletion_witness
end CollatzShell.CriticalCounting
