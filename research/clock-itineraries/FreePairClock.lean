module

public import PairInverseRays
public import TowerSectionData
import all PairInverseRays
import all TernaryItinerary

public section
namespace Collatz.Itinerary.FreePairClock

open PairInverseRays
set_option autoImplicit false
set_option maxRecDepth 12288
set_option maxHeartbeats 4000000

@[expose] def PairAt (h x b : Nat) : Prop := run h x=b ∧ run h (3*x)=b

private def triple (a : Ray) : Ray := (3*a.1,3*a.2)

private theorem value_triple (a : Ray) (t : Nat) : value (triple a) t=3*value a t := by
  simp only [triple,value,Nat.mul_add,Nat.mul_assoc]

/-- Unrestricted x and its triple cover every positive ternary unit at clock
14. The displayed height bounds distinguish the fixed and flexible clocks. -/
theorem bounded_sections (b : Nat) (unit : b%3≠0) :
    (∃ x, 0<x ∧ PairAt 14 x b ∧ 27*x≤16384*b) ∧
    (∃ h≤14, ∃ x, 0<x ∧ PairAt h x b ∧ 81*x≤16384*b) := by
  constructor
  · obtain ⟨h,lo,hi,x,pos,bound,hits⟩ := TowerSectionData.pairFixed b unit
    have eq : h=14 := by omega
    subst h
    exact ⟨x,pos,⟨by simpa using hits 0 (by decide),by simpa using hits 1 (by decide)⟩,bound⟩
  · obtain ⟨h,_,hi,x,pos,bound,hits⟩ := TowerSectionData.pairFlexible b unit
    exact ⟨h,hi,x,pos,⟨by simpa using hits 0 (by decide),by simpa using hits 1 (by decide)⟩,bound⟩

private theorem pad {h x b : Nat} (hit : PairAt h x b) (p : Nat) :
    PairAt (p+h) (2^p*x) b := by
  change run (p+h) _=b ∧ run (p+h) _=b
  rw [show 3*(2^p*x)=2^p*(3*x) by ac_rfl,run_add,run_add,halve,halve]
  exact hit

private theorem negative : (rays 13 439 0).all
    (fun a => (rays 13 439 0).all (fun c => decide (3*a.1≠c.1)))=true := by
  decide +kernel

/-- The same odd target is missed at *every* shorter clock, even allowing
even starts, by padding a purported earlier hit with initial halvings. -/
theorem misses_439 {h x : Nat} (short : h<14) : ¬PairAt h x 439 := by
  intro yes
  have at13 : PairAt 13 (2^(13-h)*x) 439 := by
    simpa only [show 13-h+h=13 by omega] using pad yes (13-h)
  let z := 2^(13-h)*x
  have cert (y : Nat) (hit : run 13 y=439) :
      ∃ a∈rays 13 439 0, y=a.1 := by
    simpa only [value,Nat.mul_zero,Nat.add_zero] using
      ray_complete 13 439 0 0 y (Nat.dvd_zero _) (by simpa using hit)
  obtain ⟨a,ma,ha⟩ := cert z at13.1
  obtain ⟨c,mc,hc⟩ := cert (3*z) at13.2
  have no := List.all_eq_true.mp (List.all_eq_true.mp negative a ma) c mc
  exact (of_decide_eq_true no) (by omega)

/-- The exact threshold for simultaneous coverage of every ternary unit. -/
theorem universal_clock_iff (h : Nat) :
    (∀ b, b%3≠0 → ∃ x, 0<x ∧ PairAt h x b) ↔ 14≤h := by
  constructor
  · intro all
    obtain ⟨x,_,yes⟩ := all 439 (by decide)
    exact Nat.le_of_not_gt (fun sh => misses_439 sh yes)
  · intro late b unit
    obtain ⟨x,pos,hit,_⟩ := (bounded_sections b unit).1
    refine ⟨2^(h-14)*x,Nat.mul_pos (Nat.two_pow_pos _) pos,?_⟩
    simpa only [show h-14+14=h by omega] using pad hit (h-14)

private theorem multiple_preimage {h x b : Nat} (div : b%3=0) (hit : run h x=b) :
    x=2^h*b := by
  induction h generalizing x with
  | zero => simpa [run] using hit
  | succ h ih =>
    have s := ih (x:=step x) hit
    have m : (2^h*b)%3=0 := by simp [Nat.mul_mod,div]
    by_cases even : x%2=0
    · have eq : x=2*step x := by simp [step,even]; omega
      rw [eq,s,Nat.pow_succ]; ac_rfl
    · have eq : 3*x+1=2*step x := by simp [step,even]; omega
      rw [s] at eq
      omega

/-- At all later clocks this describes the entire positive common image. -/
theorem exact_image {h b : Nat} (late : 14≤h) :
    (∃ x, 0<x ∧ PairAt h x b) ↔ b%3≠0 := by
  constructor
  · rintro ⟨x,px,hx,ht⟩ d
    have a := multiple_preimage d hx
    have c := multiple_preimage d ht
    omega
  · exact (universal_clock_iff h).mpr late b

#print axioms bounded_sections
#print axioms misses_439
#print axioms universal_clock_iff
#print axioms exact_image

end Collatz.Itinerary.FreePairClock
