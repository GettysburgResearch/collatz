module

public import FreePairClock
import all TernaryItinerary
import all PairInverseRays
import all FreePairClock

public section
namespace Collatz.Itinerary.FreeTripleClock

open PairInverseRays TowerSectionData
set_option autoImplicit false
set_option maxRecDepth 16000
set_option maxHeartbeats 4000000

/-- The same ordinary target from x, 3x, ..., 3^R*x at a single clock. -/
@[expose] def TowerAt (R h x b : Nat) : Prop := ∀ r≤R, run h (3^r*x)=b

theorem at_28 (b : Nat) (unit : b%3≠0) :
    ∃ x, 0<x ∧ 243*x≤268435456*b ∧ TowerAt 2 28 x b := by
  obtain ⟨h,lo,hi,x,pos,small,hits⟩ := tripleFixed b unit
  have eq : h=28 := by omega
  exact ⟨x,pos,small,eq ▸ hits⟩

theorem pad {R h x b : Nat} (hit : TowerAt R h x b) (p : Nat) :
    TowerAt R (p+h) (2^p*x) b := by
  intro r bound
  rw [show 3^r*(2^p*x)=2^p*(3^r*x) by ac_rfl,run_add,halve]
  exact hit r bound

private theorem missing : (rays 27 475963 0).all (fun a =>
    decide (run 27 (3*a.1)≠475963 ∨ run 27 (9*a.1)≠475963))=true := by
  decide +kernel

/-- This positive ordinary target rules out all shorter universal clocks. -/
theorem misses_475963 {h x : Nat} (short : h<28) : ¬TowerAt 2 h x 475963 := by
  intro hit
  let y := 2^(27-h)*x
  have at27 : TowerAt 2 27 y 475963 := by
    simpa only [show 27-h+h=27 by omega] using pad hit (27-h)
  have path : run 27 y=475963 := by simpa only [Nat.pow_zero,Nat.one_mul] using at27 0 (by decide)
  obtain ⟨a,ma,ha⟩ := ray_complete 27 475963 0 0 y (Nat.dvd_zero _) (by simpa using path)
  change y=a.1+_ * 0 at ha
  simp only [Nat.mul_zero,Nat.add_zero] at ha
  have no := of_decide_eq_true (List.all_eq_true.mp missing a ma)
  have three : run 27 (3*y)=475963 := at27 1 (by decide)
  have nine : run 27 (9*y)=475963 := at27 2 (by decide)
  rw [ha] at three nine
  exact no.elim (fun n => n three) (fun n => n nine)

theorem universal_clock_iff (h : Nat) :
    (∀ b, b%3≠0 → ∃ x, 0<x ∧ TowerAt 2 h x b) ↔ 28≤h := by
  constructor
  · intro all
    obtain ⟨x,_,hit⟩ := all 475963 (by decide)
    exact Nat.le_of_not_gt (fun sh => misses_475963 sh hit)
  · intro late b unit
    obtain ⟨x,pos,_,hit⟩ := at_28 b unit
    refine ⟨2^(h-28)*x,Nat.mul_pos (Nat.two_pow_pos _) pos,?_⟩
    simpa only [show h-28+28=h by omega] using pad hit (h-28)

theorem exact_image {h b : Nat} (late : 28≤h) :
    (∃ x, 0<x ∧ TowerAt 2 h x b) ↔ b%3≠0 := by
  constructor
  · rintro ⟨x,pos,hit⟩
    refine (FreePairClock.exact_image (by omega : 14≤h)).mp ⟨x,pos,?_,?_⟩
    · simpa only [Nat.pow_zero,Nat.one_mul] using hit 0 (by decide)
    · exact hit 1 (by decide)
  · exact (universal_clock_iff h).mpr late b

#print axioms at_28
#print axioms misses_475963
#print axioms universal_clock_iff
#print axioms exact_image
end Collatz.Itinerary.FreeTripleClock
