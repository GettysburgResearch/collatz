module

public import FreeTripleClock
import all TowerFrontierAffine
import all TernaryItinerary

public section
namespace Collatz.Itinerary.SynchronousFirstHits

open TowerFrontier FreeTripleClock
set_option autoImplicit false
set_option exponentiation.threshold 2048

def FirstOne (x s : Nat) : Prop := run s x=1 ∧ ∀ j<s, run j x≠1

private theorem after_power {h x e : Nat} (big : 2≤e) (hit : run h x=2^e) :
    FirstOne x (h+e) := by
  constructor
  · rw [run_add,hit]
    simpa only [Nat.mul_one] using halve e 1
  · intro j earlier reached
    by_cases before : j≤h
    · have eq : run (h-j) 1=2^e := by
        rw [←reached,←run_add,show j+(h-j)=h by omega,hit]
      have small := small_cycle (h-j) 1 (Or.inl rfl)
      have four := Nat.pow_le_pow_right (by decide : 0<2) big
      change 4≤2^e at four
      omega
    · let k := j-h
      have sh : k<e := by dsimp [k]; omega
      have pow : 2^e=2^k*2^(e-k) := by rw [←Nat.pow_add,show k+(e-k)=e by omega]
      rw [show j=h+k by dsimp [k]; omega,run_add,hit,pow,halve] at reached
      have two := Nat.pow_le_pow_right (by decide : 0<2) (show 1≤e-k by omega)
      change 2≤2^(e-k) at two
      omega

/-- An explicit odd family. The quotient is integral for every t. -/
def base (t : Nat) := 955+2^21*((2^(1458*t)-1)/2187)

private theorem residues (t : Nat) : 2^(1458*t)=1+2187*((2^(1458*t)-1)/2187) := by
  have u : 2^(1458*t)%2187=1 := by
    rw [Nat.pow_mul,Nat.pow_mod,show 2^1458%2187=1 by decide]
    simp
  have split := Nat.mod_add_div (2^(1458*t)) 2187
  rw [u] at split
  have eq : 2^(1458*t)-1=2187*(2^(1458*t)/2187) := by omega
  rw [eq,Nat.mul_div_cancel_left _ (by decide : 0<2187)]
  exact split.symm

/-- All three odd starts have the same exact first time at 1. The common
value at time 14 is the power of two 2^(7+1458*t). -/
theorem explicit_triples (t : Nat) :
    base t%16384=955 ∧ TowerAt 2 14 (base t) (2^(7+1458*t)) ∧
    ∀ r≤2, FirstOne (3^r*base t) (21+1458*t) := by
  let v := (2^(1458*t)-1)/2187
  have cert : ∀ r : Fin 3, track 14 (3^r.val*955) r.val=(128,7) := by decide +kernel
  have joint : TowerAt 2 14 (base t) (2^(7+1458*t)) := by
    intro r short
    have row : track 14 (3^r*955) r=(128,7) := cert ⟨r,by omega⟩
    have repr : 3^r*base t=3^r*955+2^14*3^r*(128*v) := by
      change 3^r*(955+2097152*v)=3^r*955+16384*3^r*(128*v)
      rw [Nat.mul_add]
      grind
    rw [repr,affine,row,Nat.pow_add,residues t]
    change 128+2187*(128*v)=128*(1+2187*v)
    omega
  refine ⟨by change (955+2097152*v)%16384=955; omega,joint,?_⟩
  intro r short
  simpa only [show 14+(7+1458*t)=21+1458*t by omega] using
    after_power (by omega : 2≤7+1458*t) (joint r short)

#print axioms explicit_triples
end Collatz.Itinerary.SynchronousFirstHits
