module

public import PairCoverData
public import FiberTransport
import all TowerFrontierAffine
import all TernaryItinerary
import all PairCoverData
import all FiberTransport

public section
namespace Collatz.Itinerary.PairCover

open TowerFrontier FiberTransport
set_option autoImplicit false
set_option maxRecDepth 20000
set_option maxHeartbeats 6000000

private def representative (i : Nat) := 6*(i/2)+1+4*(i%2)
private def check (i : Nat) : Bool :=
  let tr := track 18 (20+27*seed i) 0
  tr.1 == representative i && decide (tr.2≤5)

-- Each finite decision is evaluated by the kernel against the ordinary map.
private theorem checked_blocks : ∀ q : Fin 81,
    segment check 54 (54*q.val)=true := by decide +kernel

private theorem checked_seed (i : Nat) (hi : i<4374) : check i=true := by
  have block := checked_blocks ⟨i/54,by omega⟩
  exact segment_sound block (by change 54*(i/54)≤i; omega)
    (by change i<54*(i/54)+54; omega)

private theorem pair_five (t : Nat) :
    run 5 (23+32*t)=20+27*t ∧ run 5 (3*(23+32*t))=20+27*t := by
  have a : track 5 23 0=(20,3) := by decide
  have b : track 5 (3*23) 1=(20,3) := by decide
  constructor
  · exact (affine 5 23 0 t).trans (by rw [a]; rfl)
  · have eq : 3*(23+32*t)=3*23+2^5*3^1*t := by omega
    rw [eq,affine,b]; rfl

/-- Every positive odd input coprime to three is the common 23-step image of
23+32*t and its triple, at one fixed clock independent of the target. -/
theorem all_at_23 (b : Nat) (odd : b%2=1) (unit : b%3≠0) :
    ∃ t, run 23 (23+32*t)=b ∧ run 23 (3*(23+32*t))=b := by
  let b₀ := b%13122
  let i := 2*(b₀/6)+(b₀%6)/4
  have cap : b₀<13122 := Nat.mod_lt _ (by decide)
  have b2 : b₀%2=1 := by dsimp [b₀]; omega
  have b3 : b₀%3≠0 := by dsimp [b₀]; omega
  have ib : i<4374 := by dsimp [i]; omega
  have rep : representative i=b₀ := by
    have r2 : b₀%6%2=1 := (Nat.mod_mod_of_dvd b₀ (by decide : 2∣6)).trans b2
    have r3 : b₀%6%3≠0 := by rwa [Nat.mod_mod_of_dvd b₀ (by decide : 3∣6)]
    have r : b₀%6=1 ∨ b₀%6=5 := by omega
    have split := Nat.mod_add_div b₀ 6
    rcases r with r|r <;> simp [i,representative,r] <;> omega
  have h := checked_seed i ib
  simp only [check,Bool.and_eq_true,beq_iff_eq,decide_eq_true_eq] at h
  let t₀ := seed i
  let z := 20+27*t₀
  let j := (track 18 z 0).2
  have grade : j≤5 := h.2
  have val : (track 18 z 0).1=b₀ := h.1.trans rep
  let v := b/13122
  let scale := 2*3^(5-j)*v
  let t := t₀+2^18*scale
  have sum : 3^j*3^(5-j)=243 := by rw [←Nat.pow_add,show j+(5-j)=5 by omega]
  have reach : run 18 (20+27*t)=b := by
    have move : 20+27*t=z+2^18*3^0*(27*scale) := by dsimp [t,z]; grind
    rw [move,affine,val]
    change b₀+3^j*(27*(2*3^(5-j)*v))=b
    have mul (a c t : Nat) : a*(27*(2*c*t))=(a*c)*(54*t) := by grind
    rw [mul,sum]
    have div := Nat.mod_add_div b 13122
    change b₀+13122*v=b at div
    omega
  have heads := pair_five t
  refine ⟨t,?_,?_⟩
  · change run (5+18) _=b
    rw [run_add,heads.1,reach]
  · change run (5+18) _=b
    rw [run_add,heads.2,reach]

/-- Enumerate the exact backward alternatives from a supplied endpoint. -/
private def reaches_class : Nat → Nat → Bool
  | 0, y => decide (20≤y ∧ y%27=20)
  | h+1, y => reaches_class h (2*y) ||
      (decide (y%3=2) && reaches_class h ((2*y-1)/3))

private theorem extend (h x : Nat) (yes : reaches_class h x=true) :
    reaches_class (h+1) (step x)=true := by
  rw [reaches_class,Bool.or_eq_true]
  by_cases even : x%2=0
  · left
    have eq : 2*step x=x := by simp [step,even]; omega
    rw [eq]; exact yes
  · right
    have e : 2*step x=3*x+1 := by simp [step,even]; omega
    have back : (2*step x-1)/3=x := by omega
    have residue : step x%3=2 := by omega
    simp [residue,back,yes]

private theorem scan_complete (t h : Nat) :
    reaches_class h (run h (20+27*t))=true := by
  induction h with
  | zero => simp [run,reaches_class]
  | succ h ih =>
    change reaches_class (h+1) (run (h+1) (20+27*t))=true
    rw [run_add h 1]
    exact extend h _ ih

private def missing (h : Nat) := ([1,1,1,1,1,1,5,5,5,5,7,5,49,7,79,109,295,8161] : List Nat)[h]?.getD 1
private theorem negatives : ∀ i : Fin 18, missing i%2=1 ∧ missing i%3≠0 ∧
    reaches_class i (missing i)=false := by decide +kernel

/-- A particular odd-unit target is absent at each earlier common clock.
For clock 22 the target is 8161. -/
theorem fails_before_23 (n : Nat) (early : n<23) :
    ∃ b, b%2=1 ∧ b%3≠0 ∧ ∀ t, run n (23+32*t)≠b := by
  by_cases soon : n<5
  · refine ⟨1,by decide,by decide,?_⟩
    intro t hit
    have h := pair_five t
    have eq : run 5 (23+32*t)=run (5-n) 1 := by
      calc
        run 5 (23+32*t)=run (n+(5-n)) (23+32*t) := by congr 1 <;> omega
        _ = run (5-n) 1 := by rw [run_add,hit]
    have small : ∀ i : Fin 6, run i 1≤2 := by decide
    have le := small ⟨5-n,by omega⟩
    change run (5-n) 1≤2 at le
    have same := h.1.symm.trans eq
    omega
  · let h := n-5
    have le : h<18 := by dsimp [h]; omega
    have ⟨bo,bu,no⟩ := negatives ⟨h,le⟩
    refine ⟨missing h,bo,bu,?_⟩
    intro t hit
    rw [show n=5+h by dsimp [h]; omega,run_add,(pair_five t).1] at hit
    have yes := scan_complete t h
    rw [hit,no] at yes
    contradiction

#print axioms all_at_23
#print axioms fails_before_23

end Collatz.Itinerary.PairCover
