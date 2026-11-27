module

public import PairInverseRays
public import UniformTowerRouting
public import FreeTripleClock
public import TowerCapture
import all UniformTowerRouting
import all TernaryItinerary
import all FiberTransport
import all TowerCapture

public section
namespace Collatz.Itinerary.StableTowerFibers

open PairInverseRays
set_option autoImplicit false

/-- Ordinary starts x and m*x for every listed multiplier, at one clock. -/
def Joint (ms : List Nat) (h x b : Nat) : Prop :=
  run h x=b ∧ ∀ m∈ms, run h (m*x)=b

def scaled (m : Nat) (p : Ray) : Ray := (m*p.1,m*p.2)

private def cap : List Nat → Nat
  | [] => 1
  | m::ms => max m (cap ms)

private theorem cap_one (ms : List Nat) : 1≤cap ms := by
  induction ms with
  | nil => decide
  | cons m ms ih => exact Nat.le_trans ih (Nat.le_max_right ..)

private theorem cap_mem {ms : List Nat} {m : Nat} (mem : m∈ms) : m≤cap ms := by
  induction ms with
  | nil => simp at mem
  | cons y ys ih =>
    rcases List.mem_cons.mp mem with eq | tail
    · subst m; exact Nat.le_max_left ..
    · exact Nat.le_trans (ih tail) (Nat.le_max_right ..)

private theorem intercept {h a d : Nat} {p : Ray} (mem : p∈rays h a d) : p.1≤2^h*a := by
  have atZero : run h p.1=a := by simpa only [value,Nat.mul_zero,Nat.add_zero] using ray_sound mem 0
  have bound := TowerCapture.input_bound h p.1
  rwa [atZero] at bound

/-- Beyond an explicit offset, all simultaneous predecessors are exactly
the affine rays that already synchronize over the entire target progression. -/
theorem high_fiber {ms : List Nat} {h a x t C : Nat}
    (one : 1≤C) (bound : ∀ m∈ms, m≤C) (large : C*(2^h*a)<t) :
    Joint ms h x (a+3^h*t) ↔ ∃ p∈rays h a (3^h),
      x=value p t ∧ ∀ m∈ms, scaled m p∈rays h a (3^h) := by
  constructor
  · rintro ⟨anchor,others⟩
    obtain ⟨p,mem,hp⟩ := ray_complete h a (3^h) t x (Nat.dvd_refl _) anchor
    refine ⟨p,mem,hp,?_⟩
    intro m mm
    obtain ⟨q,mq,hq⟩ := ray_complete h a (3^h) t (m*x) (Nat.dvd_refl _) (others m mm)
    have left := Nat.mul_le_mul (bound m mm) (intercept mem)
    have right := Nat.le_trans (intercept mq) (Nat.le_mul_of_pos_left (2^h*a) one)
    rw [hp] at hq
    have eq : m*p.1+(m*p.2)*t=q.1+q.2*t := by
      simpa only [value,Nat.mul_add,Nat.mul_assoc] using hq
    have slope : m*p.2=q.2 := UniformTowerRouting.same_slope
      (Nat.lt_of_le_of_lt left large) (Nat.lt_of_le_of_lt right large) eq
    rw [slope] at eq
    have same : scaled m p=q := Prod.ext (by change m*p.1=q.1; omega) slope
    rwa [same]
  · rintro ⟨p,mem,rfl,others⟩
    refine ⟨ray_sound mem t,?_⟩
    intro m mm
    simpa only [scaled,value,Nat.mul_add,Nat.mul_assoc] using ray_sound (others m mm) t

/-- Any missed ordinary unit target forces arbitrarily late misses even
among the pure doublings of *any specified unit*, in its own component. -/
theorem recurrent_failure {ms : List Nat} {h b : Nat} (ub : b%3≠0)
    (miss : ¬∃ x, Joint ms h x b) (u E : Nat) (uu : u%3≠0) :
    ∃ e≥E, ∃ t, 2^e*u=b+3^h*t ∧ ¬∃ x, Joint ms h x (2^e*u) := by
  let B := cap ms*(2^h*b)
  let z := b+3^(h+1)*(B+1)
  have zu : z%3≠0 := by
    have repr : z=b+3*(3^h*(B+1)) := by simp only [z,Nat.pow_succ]; ac_rfl
    rwa [repr,Nat.add_mul_mod_self_left]
  obtain ⟨e,v,he,eq⟩ := FiberTransport.large_dyadic_lift h u z E uu zu
  let t := 3*(B+1+v)
  have repr : 2^e*u=b+3^h*t := by
    rw [eq]; simp only [z,t,Nat.pow_succ]; grind
  refine ⟨e,he,t,repr,?_⟩
  rintro ⟨x,hx⟩
  rw [repr] at hx
  have big : B<t := by dsimp [t]; omega
  obtain ⟨p,mem,_,others⟩ := (high_fiber (cap_one ms) (fun _ hm => cap_mem hm) big).mp hx
  refine miss ⟨p.1,?_,?_⟩
  · simpa only [value,Nat.mul_zero,Nat.add_zero] using ray_sound mem 0
  · intro m mm
    simpa only [scaled,value,Nat.mul_zero,Nat.add_zero] using ray_sound (others m mm) 0

/-- Testing all sufficiently large powers of two times any one fixed unit
at a fixed clock is equivalent to testing every ordinary unit target. -/
theorem dyadic_test (ms : List Nat) (h u : Nat) (uu : u%3≠0) :
    (∀ b, b%3≠0 → ∃ x, Joint ms h x b) ↔
      ∃ E, ∀ e≥E, ∃ x, Joint ms h x (2^e*u) := by
  constructor
  · intro all
    exact ⟨0,fun e _ => all _ (FiberTransport.unit_pow_two e u uu)⟩
  · rintro ⟨E,passed⟩ b ub
    apply Classical.byContradiction
    intro miss
    obtain ⟨e,le,_,_,no⟩ := recurrent_failure ub miss u E uu
    exact no (passed e le)

theorem pair_misses_in_every_component {h : Nat} (short : h<14) (u E : Nat) (uu : u%3≠0) :
    ∃ e≥E, ¬∃ x, FreePairClock.PairAt h x (2^e*u) := by
  have no : ¬∃ x, Joint [3] h x 439 := by
    rintro ⟨x,hx,other⟩
    exact FreePairClock.misses_439 short ⟨hx,other 3 (by simp)⟩
  obtain ⟨e,le,_,_,bad⟩ := recurrent_failure (by decide : 439%3≠0) no u E uu
  refine ⟨e,le,?_⟩
  rintro ⟨x,hx,ht⟩
  refine bad ⟨x,hx,?_⟩
  intro m hm
  have eq : m=3 := by simpa using hm
  simpa only [eq] using ht

theorem triple_misses_in_every_component {h : Nat} (short : h<28) (u E : Nat) (uu : u%3≠0) :
    ∃ e≥E, ¬∃ x, FreeTripleClock.TowerAt 2 h x (2^e*u) := by
  have no : ¬∃ x, Joint [3,9] h x 475963 := by
    rintro ⟨x,hx,other⟩
    apply FreeTripleClock.misses_475963 short (x:=x)
    intro r hr
    rcases (show r=0 ∨ r=1 ∨ r=2 by omega) with z | o | t
    · simpa only [z,Nat.pow_zero,Nat.one_mul] using hx
    · subst r; exact other 3 (by simp)
    · subst r; exact other 9 (by simp)
  obtain ⟨e,le,_,_,bad⟩ := recurrent_failure (by decide : 475963%3≠0) no u E uu
  refine ⟨e,le,?_⟩
  rintro ⟨x,hx⟩
  refine bad ⟨x,by simpa only [Nat.pow_zero,Nat.one_mul] using hx 0 (by decide),?_⟩
  intro m hm
  rcases (show m=3 ∨ m=9 by simpa using hm) with rfl | rfl
  · exact hx 1 (by decide)
  · exact hx 2 (by decide)

#print axioms high_fiber
#print axioms recurrent_failure
#print axioms dyadic_test
#print axioms pair_misses_in_every_component
#print axioms triple_misses_in_every_component
end Collatz.Itinerary.StableTowerFibers
