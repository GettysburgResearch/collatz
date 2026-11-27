module

public import TowerFrontierAffine
import all TernaryItinerary

public section
namespace Collatz.Itinerary.TowerSectionTree

open TowerFrontier
set_option autoImplicit false

/-- Branches prescribe the next base-three digit of the target. A leaf
contains a common physical clock and a positive base at its representative. -/
inductive Tree where
  | leaf (clock start : Nat)
  | fork (zero one two : Tree)

@[expose] def leafCheck (R lo hi den num a k h x : Nat) : Bool :=
  let g := (track h x 0).2
  decide (lo≤h ∧ h≤hi ∧ 0<x ∧ g≤k ∧ den*x≤num*a ∧
    den*(2^h*3^(k-g))≤num*3^k) &&
  (List.range (R+1)).all (fun r => track h (3^r*x) r == (a,g))

@[expose] def check (R lo hi den num : Nat) : Tree → Nat → Nat → Bool
  | .leaf h x, a, k => leafCheck R lo hi den num a k h x
  | .fork l m r, a, k => check R lo hi den num l a (k+1) &&
      check R lo hi den num m (a+3^k) (k+1) &&
      check R lo hi den num r (a+2*3^k) (k+1)

@[expose] def Section (R lo hi den num b : Nat) : Prop :=
  ∃ h, lo≤h ∧ h≤hi ∧ ∃ x, 0<x ∧ den*x≤num*b ∧
    ∀ r≤R, run h (3^r*x)=b

private theorem leaf_sound {R lo hi den num a k h x : Nat}
    (ok : leafCheck R lo hi den num a k h x=true) (v : Nat) :
    Section R lo hi den num (a+3^k*v) := by
  simp only [leafCheck,Bool.and_eq_true,decide_eq_true_eq] at ok
  obtain ⟨⟨low,high,px,grade,base,slope⟩,rows⟩ := ok
  let g := (track h x 0).2
  let d := 2^h*3^(k-g)
  refine ⟨h,low,high,x+d*v,by omega,?_,?_⟩
  · simpa only [d,g,Nat.mul_add,←Nat.mul_assoc] using
      Nat.add_le_add base (Nat.mul_le_mul_right v slope)
  · intro r bound
    have row := List.all_eq_true.mp rows r (List.mem_range.mpr (by omega))
    have hit : track h (3^r*x) r=(a,g) := beq_iff_eq.mp row
    have repr : 3^r*(x+d*v)=3^r*x+2^h*3^r*(3^(k-g)*v) := by
      simp only [d,Nat.mul_add]; ac_rfl
    rw [repr,affine,hit]
    change a+3^g*(3^(k-g)*v)=a+3^k*v
    rw [←Nat.mul_assoc,←Nat.pow_add,show g+(k-g)=k by dsimp [g]; omega]

/-- A finite ternary tree certifies all positive ordinary lifts, preserving
the clock, the full tower of inputs, and the requested linear height bound. -/
theorem sound {R lo hi den num : Nat} (tree : Tree) (a k : Nat)
    (ok : check R lo hi den num tree a k=true) (v : Nat) :
    Section R lo hi den num (a+3^k*v) := by
  induction tree generalizing a k v with
  | leaf h x => exact leaf_sound ok v
  | fork l m r left mid right =>
    simp only [check,Bool.and_eq_true] at ok
    obtain ⟨⟨hl,hm⟩,hr⟩ := ok
    have split := Nat.mod_add_div v 3
    rcases (show v%3=0 ∨ v%3=1 ∨ v%3=2 by omega) with z | o | t
    · have eq : a+3^k*v=a+3^(k+1)*(v/3) := by
        conv => lhs; rw [←split,z,Nat.zero_add]
        rw [Nat.pow_succ]; ac_rfl
      rw [eq]; exact left _ _ hl _
    · have eq : a+3^k*v=a+3^k+3^(k+1)*(v/3) := by
        conv => lhs; rw [←split,o]
        rw [Nat.mul_add,Nat.pow_succ,Nat.mul_one]; ac_rfl
      rw [eq]; exact mid _ _ hm _
    · have eq : a+3^k*v=a+2*3^k+3^(k+1)*(v/3) := by
        conv => lhs; rw [←split,t]
        rw [Nat.mul_add,Nat.pow_succ]; ac_rfl
      rw [eq]; exact right _ _ hr _

#print axioms sound
end Collatz.Itinerary.TowerSectionTree
