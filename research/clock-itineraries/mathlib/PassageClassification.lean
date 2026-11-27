module

public import PassageRouting
import all PassageRouting
import all PassageFusion
import all FiberTransport
import all UniformTowerRouting
import all TowerFrontierAffine
import all TernaryItinerary
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageClassification

open PassageRouting PassageFusion TowerFrontier
set_option autoImplicit false

/-- A binary and ternary residue requirement can be fixed before the clock
and target, including on the common translating parameter itself. -/
theorem on_progression (bs : List Ray) (l g r : ℕ) :
    ∃ N, ∀ S≥N, ∀ b, b%3≠0 → ∃ t, 0<t ∧
      let x := r+2^l*3^g*t
      FirstLow S x b ∧ ∀ z∈bs, FirstLow S (z.value x) b := by
  let anchor : Ray := ⟨0,0⟩
  let after (z : Ray) : Ray :=
    ⟨(track l (z.value r) 0).1,(track l (z.value r) 0).2+z.grade+g⟩
  obtain ⟨_,_,_,_,N,route⟩ := affine_first ((anchor::bs).map after)
  refine ⟨l+N+1,?_⟩
  intro S late b ub
  let f := S-l
  have hf : l+f=S := by dsimp only [f]; omega
  obtain ⟨t,_,tp,_,_,first,arms⟩ := route f (by dsimp only [f]; omega) b ub
  have bt : b<t := first.2 0 (by dsimp only [f]; omega)
  let x := r+2^l*3^g*t
  have each (z : Ray) (mem : z∈anchor::bs) : FirstLow S (z.value x) b := by
    have tail := arms (after z) (List.mem_map_of_mem mem)
    have hit : run l (z.value x)=(after z).value t := by
      have eq : z.value x=z.value r+2^l*3^0*(3^z.grade*3^g*t) := by
        simp only [Ray.value,x,pow_zero]; ring
      rw [eq,affine]
      simp only [after,Ray.value,pow_add]; ring
    rw [←hf]
    apply first_append hit _ tail
    intro j hj
    have size : 2^l*t≤z.value x := calc
      2^l*t ≤ (2^l*t)*3^g := Nat.le_mul_of_pos_right _ (by positivity)
      _ ≤ x := by dsimp only [x]; rw [show 2^l*t*3^g=2^l*3^g*t by ring]; omega
      _ ≤ 3^z.grade*x := Nat.le_mul_of_pos_left _ (by positivity)
      _ ≤ z.value x := Nat.le_add_left _ _
    have le := Nat.mul_le_mul_right t (Nat.pow_le_pow_right (by decide : 0<2) hj.le)
    have cap := self_le_run j (z.value x)
    have lower := Nat.le_of_mul_le_mul_left (le.trans (size.trans cap)) (Nat.two_pow_pos j)
    omega
  refine ⟨t,tp,?_,fun z hz => each z (List.mem_cons_of_mem _ hz)⟩
  simpa only [anchor,Ray.value,pow_zero,one_mul,zero_add] using each anchor (by simp)

private theorem slope_constraint {h m c : ℕ}
    (all : ∀ b, b%3≠0 → ∃ x, run h x=b ∧ run h (m*x+c)=b) : ∃ j, m=3^j := by
  let d := 2^h
  let cap := d*(m*d+c)+d*d
  let L := d*(cap+1)
  let b := 3*(d*L)+1
  obtain ⟨x,hx,hm⟩ := all b (by dsimp only [b]; omega)
  have small := UniformTowerRouting.run_upper h x
  rw [hx] at small
  have big : L<x := by
    by_contra! no
    have max := Nat.mul_le_mul_left d no
    change b≤d*x at small
    dsimp only [b] at small
    omega
  have dp := Nat.two_pow_pos h
  let t := x/d
  let r := x%d
  have tall : cap<t := Nat.lt_of_succ_le <| (Nat.le_div_iff_mul_le dp).mpr
    (by rw [Nat.mul_comm]; exact big.le)
  have split : r+d*t=x := Nat.mod_add_div x d
  let p := (track h r 0).2
  let q := (track h (m*r+c) 0).2
  have ra : run h x=run h r+3^p*t := by
    conv => lhs; rw [←split]
    simpa only [p,d,pow_zero,Nat.mul_one,FiberTransport.track_value] using affine h r 0 t
  have rb : run h (m*x+c)=run h (m*r+c)+3^q*(m*t) := by
    have eq : m*x+c=(m*r+c)+d*(m*t) := by
      conv => lhs; rw [←split]
      ring
    rw [eq]
    simpa only [q,d,pow_zero,Nat.mul_one,FiberTransport.track_value] using affine h (m*r+c) 0 (m*t)
  have rd : r≤d := (Nat.mod_lt x dp).le
  have amax : run h r≤cap :=
    ((UniformTowerRouting.run_upper h r).trans (Nat.mul_le_mul_left d rd)).trans
      (Nat.le_add_left _ _)
  have bmax : run h (m*r+c)≤cap :=
    ((UniformTowerRouting.run_upper h _).trans (Nat.mul_le_mul_left d
      (Nat.add_le_add_right (Nat.mul_le_mul_left m rd) c))).trans (Nat.le_add_right _ _)
  have eq := hx.trans hm.symm
  rw [ra,rb,←Nat.mul_assoc] at eq
  have slopes := UniformTowerRouting.same_slope (amax.trans_lt tall) (bmax.trans_lt tall) eq
  have mp : 0<m := by
    by_contra! z
    have zero : m=0 := by omega
    rw [zero,Nat.mul_zero] at slopes
    exact (pow_ne_zero p (by decide : (3:ℕ)≠0)) slopes
  have lower := Nat.le_mul_of_pos_right (3^q) mp
  have le : q≤p := by
    by_contra! lt
    have := Nat.pow_lt_pow_right (by decide : 1<3) lt
    omega
  refine ⟨p-q,Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide : 0<3) (n:=q)) ?_⟩
  rw [←slopes,←Nat.pow_add,show q+(p-q)=p by omega]

def Covers (ps : List (ℕ×ℕ)) : Prop :=
  ∃ N, ∀ S≥N, ∀ b, b%3≠0 → ∃ x, 0<x ∧ FirstLow S x b ∧
    ∀ p∈ps, FirstLow S (p.1*x+p.2) b

/-- Exact algebraic classification with the anchoring arm x. Intercepts may
be arbitrary naturals and the same deadline is prescribed for all arms. -/
theorem classification (ps : List (ℕ×ℕ)) :
    Covers ps ↔ ∀ p∈ps, ∃ j, p.1=3^j := by
  constructor
  · rintro ⟨N,cover⟩ p hp
    apply slope_constraint (h:=N) (c:=p.2)
    intro b ub
    obtain ⟨x,_,anchor,rest⟩ := cover N le_rfl b ub
    exact ⟨x,anchor.1,(rest p hp).1⟩
  · intro h
    classical
    let grade (m : ℕ) := if e : ∃ j : ℕ, m=3^j then e.choose else 0
    let ray (p : ℕ×ℕ) : Ray := ⟨p.2,grade p.1⟩
    obtain ⟨_,_,_,_,N,route⟩ := affine_first (ps.map ray)
    refine ⟨N,?_⟩
    intro S late b ub
    obtain ⟨x,_,xp,_,_,root,arms⟩ := route S late b ub
    refine ⟨x,xp,root,?_⟩
    intro p hp
    have coeff : p.1=3^(grade p.1) := by
      dsimp only [grade]; rw [dif_pos (h p hp)]; exact (h p hp).choose_spec
    have eq : (ray p).value x=p.1*x+p.2 := by
      change p.2+3^(grade p.1)*x=p.1*x+p.2
      rw [←coeff,Nat.add_comm]
    exact eq ▸ arms (ray p) (List.mem_map_of_mem hp)

private theorem unique_ancestor (h x b : ℕ) (mul : b%3=0) (hit : run h x=b) :
    x=2^h*b := by
  induction h generalizing x with
  | zero => simpa [run] using hit
  | succ h ih =>
    have prior := ih (step x) hit
    have div : (2^h*b)%3=0 := by simp [Nat.mul_mod,mul]
    change (if x%2=0 then x/2 else (3*x+1)/2)=2^h*b at prior
    split at prior <;> rw [pow_succ,Nat.mul_right_comm] <;> omega

/-- Distinct sources cannot meet at a multiple of three on a common clock. -/
theorem disjoint_at_three {h x y b : ℕ} (mul : b%3=0) (hx : run h x=b)
    (hy : run h y=b) : x=y :=
  (unique_ancestor h x b mul hx).trans (unique_ancestor h y b mul hy).symm

#print axioms on_progression
#print axioms classification
#print axioms disjoint_at_three
end Collatz.Itinerary.PassageClassification
