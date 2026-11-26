module

public import FreeTripleClock
public import BasinUnitEncoding
import all TernaryItinerary

public section
namespace Collatz.Itinerary.SynchronousBasin

open FreeTripleClock BasinUnitEncoding
set_option autoImplicit false

/-- F codes every positive start injectively. All its tower arms agree at H
and reach any supplied downstream unit together within six additional steps
beyond the original time, after the H-step section. -/
structure Encoding (R H den num : Nat) (F : Nat → Nat) : Prop where
  positive : ∀ n, 0<n → 0<F n
  injective : ∀ {n m}, 0<n → 0<m → F n=F m → n=m
  size : ∀ n, 0<n → den*F n≤num*n
  common : ∀ n, 0<n → TowerAt R H (F n) (code n)
  downstream : ∀ {n h b}, 0<n → b%3≠0 → run h n=b →
    ∃ j≤h+6, TowerAt R (H+j) (F n) b

private theorem from_section {R H den num : Nat}
    (sections : ∀ b, b%3≠0 → ∃ x, 0<x ∧ den*x≤num*b ∧ TowerAt R H x b) :
    ∃ F, Encoding R H den (27*num) F := by
  classical
  let pick (b : Nat) := if hu : b%3≠0 then (sections b hu).choose else 0
  have selected (b : Nat) (unit : b%3≠0) :
      0<pick b ∧ den*pick b≤num*b ∧ TowerAt R H (pick b) b := by
    simpa only [pick,dif_pos unit] using (sections b unit).choose_spec
  let F (n : Nat) := pick (code n)
  have rows (n : Nat) (hn : 0<n) := selected (code n) (code_spec hn).1
  refine ⟨F,fun n pn => (rows n pn).1,?_,?_,fun n pn => (rows n pn).2.2,?_⟩
  · intro n m pn pm eq
    have left : run H (F n)=code n := by simpa using (rows n pn).2.2 0 (Nat.zero_le _)
    have right : run H (F m)=code m := by simpa using (rows m pm).2.2 0 (Nat.zero_le _)
    exact code_injective pn pm (left.symm.trans ((congrArg (run H) eq).trans right))
  · intro n pn
    have bound := Nat.le_trans (rows n pn).2.1 (Nat.mul_le_mul_left num (code_spec pn).2.1)
    simpa only [F,Nat.mul_left_comm num 27,Nat.mul_assoc] using bound
  · intro n h b pn unit hit
    obtain ⟨time,short,done⟩ := (code_spec pn).2.2 h b unit hit
    refine ⟨time,short,?_⟩
    intro r hr
    rw [run_add,(rows n pn).2.2 r hr,done]

/-- Every ordinary basin admits an injective encoding by synchronized pairs
with the same 14-step prefix and a universal linear size bound. -/
theorem pair_encoding : ∃ F, Encoding 1 14 1 16384 F := by
  have sections (b : Nat) (unit : b%3≠0) : ∃ x, 0<x ∧ 27*x≤16384*b ∧ TowerAt 1 14 x b := by
    obtain ⟨x,pos,⟨first,second⟩,bound⟩ := (FreePairClock.bounded_sections b unit).1
    refine ⟨x,pos,bound,?_⟩
    intro r hr
    rcases (show r=0 ∨ r=1 by omega) with z | o
    · simpa only [z,Nat.pow_zero,Nat.one_mul] using first
    · simpa only [o,Nat.pow_one] using second
  obtain ⟨F,enc⟩ := from_section sections
  refine ⟨F,enc.positive,enc.injective,?_,enc.common,enc.downstream⟩
  intro n pn
  have small := enc.size n pn
  omega

/-- Every ordinary basin admits an injective encoding by synchronized triples.
The same F works for all positive starts and every downstream unit target. -/
theorem triple_encoding : ∃ F, Encoding 2 28 9 268435456 F := by
  obtain ⟨F,enc⟩ := from_section at_28
  refine ⟨F,enc.positive,enc.injective,?_,enc.common,enc.downstream⟩
  intro n pn
  have small := enc.size n pn
  omega

#print axioms pair_encoding
#print axioms triple_encoding
end Collatz.Itinerary.SynchronousBasin
