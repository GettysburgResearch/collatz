module

public import PassageRouting
public import TowerSectionTree
import all PassageRouting
import all TowerSectionTree
import all TowerFrontierAffine
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageIntervals

open PassageRouting TowerFrontier TowerSectionTree
set_option autoImplicit false

def Block (w h b : ℕ) := ∃ x, 0<x ∧ ∀ o<w, FirstLow h (x+o) b

def AllTargets (w h : ℕ) := ∀ b, b%3≠0 → Block w h b

theorem later {w h : ℕ} (given : AllTargets w h) (s : ℕ) : AllTargets w (h+s) := by
  intro b ub
  have bp : 0<b := by omega
  have unit : (2^s*b)%3≠0 := by
    induction s with
    | zero => simpa
    | succ s ih => rw [pow_succ,Nat.mul_right_comm]; omega
  obtain ⟨x,xp,hit⟩ := given _ unit
  refine ⟨x,xp,?_⟩
  intro o ho
  have first := hit o ho
  have by' : b≤2^s*b := Nat.le_mul_of_pos_left _ (Nat.two_pow_pos s)
  exact first_append first.1 (fun j hj => by'.trans_lt (first.2 j hj)) (first_dyadic s b bp)

@[expose] def rowCheck (w h x a k : ℕ) : Bool :=
  let q := (track h x 0).2
  decide (0<x ∧ q≤k) && (List.range w).all fun o =>
    track h (x+o) 0 == (a,q) && (List.range h).all fun j =>
      let v := track j (x+o) 0
      decide (a<v.1 ∧ 3^q≤3^v.2*2^(h-j))

private theorem row_sound {w h x a k : ℕ} (ok : rowCheck w h x a k=true) (u : ℕ) :
    Block w h (a+3^k*u) := by
  simp only [rowCheck,Bool.and_eq_true,decide_eq_true_eq] at ok
  obtain ⟨⟨xp,grade⟩,rows⟩ := ok
  let q := (track h x 0).2
  let t := 3^(k-q)*u
  have rt : 3^q*t=3^k*u := by
    rw [show 3^q*t=3^(q+(k-q))*u by dsimp only [t]; rw [pow_add]; ring]
    have le : q≤k := grade
    rw [show q+(k-q)=k by omega]
  refine ⟨x+2^h*t,by omega,?_⟩
  intro o ho
  have row := List.all_eq_true.mp rows o (List.mem_range.mpr ho)
  simp only [Bool.and_eq_true,beq_iff_eq] at row
  have value (j : ℕ) (jh : j≤h) :
      run j (x+2^h*t+o)=(track j (x+o) 0).1+
        3^(track j (x+o) 0).2*(2^(h-j)*t) := by
    have eq : x+2^h*t+o=(x+o)+2^j*3^0*(2^(h-j)*t) := by
      conv => lhs; rw [show h=j+(h-j) by omega,pow_add]
      simp only [pow_zero]; ring
    rw [eq,affine]
  refine ⟨?_,?_⟩
  · rw [value h le_rfl,row.1]; simpa only [Nat.sub_self,pow_zero,one_mul] using congrArg (a+·) rt
  · intro j jh
    have early := List.all_eq_true.mp row.2 j (List.mem_range.mpr jh)
    simp only [decide_eq_true_eq] at early
    have slope := Nat.mul_le_mul_right t early.2
    rw [Nat.mul_assoc] at slope
    rw [value j jh.le,←rt]
    exact Nat.add_lt_add_of_lt_of_le early.1 slope

@[expose] def treeCheck (w h : ℕ) : Tree → ℕ → ℕ → Bool
  | .leaf z x, a, k => (z==h) && rowCheck w h x a k
  | .fork l m r, a, k => treeCheck w h l a (k+1) && treeCheck w h m (a+3^k) (k+1) &&
      treeCheck w h r (a+2*3^k) (k+1)

theorem tree_sound (w h : ℕ) (tree : Tree) (a k : ℕ)
    (ok : treeCheck w h tree a k=true) (u : ℕ) : Block w h (a+3^k*u) := by
  induction tree generalizing a k u with
  | leaf z x =>
    simp only [treeCheck,Bool.and_eq_true] at ok
    exact row_sound ok.2 u
  | fork l m r il im ir =>
    simp only [treeCheck,Bool.and_eq_true] at ok
    have split := Nat.mod_add_div u 3
    rcases (show u%3=0 ∨ u%3=1 ∨ u%3=2 by omega) with z | o | t
    · have eq : a+3^k*u=a+3^(k+1)*(u/3) := by
        conv => lhs; rw [←split,z,Nat.zero_add]
        rw [pow_succ]; ring
      rw [eq]; exact il _ _ ok.1.1 _
    · have eq : a+3^k*u=a+3^k+3^(k+1)*(u/3) := by
        conv => lhs; rw [←split,o]
        rw [pow_succ]; ring
      rw [eq]; exact im _ _ ok.1.2 _
    · have eq : a+3^k*u=a+2*3^k+3^(k+1)*(u/3) := by
        conv => lhs; rw [←split,t]
        rw [pow_succ]; ring
      rw [eq]; exact ir _ _ ok.2 _

theorem from_trees {w h : ℕ} (l r : Tree) (c1 : treeCheck w h l 1 1=true)
    (c2 : treeCheck w h r 2 1=true) : AllTargets w h := by
  intro b unit
  rcases (show b%3=1 ∨ b%3=2 by omega) with h1 | h2
  · have eq : b=1+3^1*(b/3) := by omega
    exact eq ▸ tree_sound w h l 1 1 c1 (b/3)
  · have eq : b=2+3^1*(b/3) := by omega
    exact eq ▸ tree_sound w h r 2 1 c2 (b/3)

@[expose] def parents (y : ℕ) : List ℕ :=
  if y%3=2 then [2*y,(2*y-1)/3] else [2*y]

private theorem mem_parents (x : ℕ) : x∈parents (step x) := by
  by_cases e : x%2=0
  · have sx : step x=x/2 := by rw [step,if_pos e]
    rw [sx,parents]; split <;> simp <;> omega
  · have sx : step x=(3*x+1)/2 := by rw [step,if_neg e]
    rw [sx,parents,if_pos (show ((3*x+1)/2)%3=2 by omega)]
    simp; omega

@[expose] def aboveTree (b : ℕ) : ℕ → List ℕ
  | 0 => [b]
  | n+1 => ((aboveTree b n).flatMap parents).filter (fun x => b<x)

private theorem mem_above {h x b : ℕ} (first : FirstLow h x b) : x∈aboveTree b h := by
  induction h generalizing x with
  | zero => exact List.mem_singleton.mpr first.1
  | succ h ih =>
    have tail : FirstLow h (step x) b := ⟨first.1,fun j hj => first.2 (j+1) (by omega)⟩
    apply List.mem_filter.mpr
    exact ⟨List.mem_flatMap.mpr ⟨step x,ih tail,mem_parents x⟩,
      decide_eq_true (first.2 0 (by omega))⟩

@[expose] def containsBlock (w h b : ℕ) : Bool :=
  let xs := aboveTree b h
  xs.any fun x => (List.range w).all fun o => xs.contains (x+o)

theorem missed {w h b : ℕ} (wp : 0<w) (gap : containsBlock w h b=false) : ¬Block w h b := by
  rintro ⟨x,_,hit⟩
  have zero := mem_above (hit 0 wp)
  simp only [Nat.add_zero] at zero
  have found : containsBlock w h b=true := by
    apply List.any_eq_true.mpr
    refine ⟨x,zero,List.all_eq_true.mpr ?_⟩
    intro o ho
    exact List.contains_iff_mem.mpr (mem_above (hit o (List.mem_range.mp ho)))
  rw [gap] at found
  contradiction

theorem optimal {w h b : ℕ} (wp : 0<w) (ub : b%3≠0) (gap : containsBlock w h b=false)
    (cover : AllTargets w (h+1)) (s : ℕ) : AllTargets w s ↔ h+1≤s := by
  constructor
  · intro first
    by_contra! short
    have old := later first (h-s)
    rw [show s+(h-s)=h by omega] at old
    exact missed wp gap (old b ub)
  · intro late
    have next := later cover (s-(h+1))
    rwa [show h+1+(s-(h+1))=s by omega] at next

#print axioms tree_sound
#print axioms optimal
end Collatz.Itinerary.PassageIntervals
