module

public import FiberTransport
import all TernaryItinerary
import all TowerFrontierAffine
import all FiberTransport

public section
namespace Collatz.Itinerary.BasinUnitEncoding

open TowerFrontier FiberTransport
set_option autoImplicit false

/-- Replace the odd part o of n by its sibling 4o+1, retaining the initial
powers of two. Both odd parts reach T(o), two shortcut steps apart. -/
@[expose] def sibling (n : Nat) : Nat :=
  if n=0 then 0 else if n%2=0 then 2*sibling (n/2) else 4*n+1
termination_by n
decreasing_by omega

private theorem sibling_rep (k o : Nat) (odd : o%2=1) :
    sibling (2^k*o)=2^k*(4*o+1) := by
  induction k with
  | zero =>
    simp only [Nat.pow_zero,Nat.one_mul]
    rw [sibling,if_neg (by omega),if_neg (by omega)]
  | succ k ih =>
    let n := 2^k*o
    have pos : 0<n := Nat.mul_pos (Nat.two_pow_pos _) (by omega)
    have split : 2^(k+1)*o=2*n := by simp only [n,Nat.pow_succ]; ac_rfl
    rw [split,sibling,if_neg (by omega),if_pos (by omega)]
    have half : 2*n/2=n := by omega
    rw [half,show sibling n=2^k*(4*o+1) from ih,Nat.pow_succ]
    ac_rfl

private theorem odd_rep_unique (k l a b : Nat) (oa : a%2=1) (ob : b%2=1)
    (eq : 2^k*a=2^l*b) : k=l ∧ a=b := by
  induction k generalizing l with
  | zero =>
    cases l with
    | zero => simpa using eq
    | succ l =>
      have e : a=2*(2^l*b) := by
        simpa only [Nat.pow_zero,Nat.one_mul,Nat.pow_succ,Nat.mul_right_comm (2^l) 2 b,
          Nat.mul_comm (2^l*b) 2] using eq
      omega
  | succ k ih =>
    have left : 2^(k+1)*a=2*(2^k*a) := by rw [Nat.pow_succ]; ac_rfl
    cases l with
    | zero => rw [left,Nat.pow_zero,Nat.one_mul] at eq; omega
    | succ l =>
      have right : 2^(l+1)*b=2*(2^l*b) := by rw [Nat.pow_succ]; ac_rfl
      rw [left,right] at eq
      obtain ⟨same,rest⟩ := ih l (by omega)
      exact ⟨by omega,rest⟩

private theorem sibling_inj {n m : Nat} (pn : 0<n) (pm : 0<m)
    (eq : sibling n=sibling m) : n=m := by
  obtain ⟨k,a,hn,oa⟩ := split_twos n pn
  obtain ⟨l,b,hm,ob⟩ := split_twos m pm
  rw [hn,hm,sibling_rep k a oa,sibling_rep l b ob] at eq
  obtain ⟨same,rest⟩ := odd_rep_unique k l (4*a+1) (4*b+1) (by omega) (by omega) eq
  rw [hn,hm,same,show a=b by omega]

private theorem sibling_facts {n : Nat} (pos : 0<n) (div : n%3=0) :
    sibling n%3≠0 ∧ sibling n≤5*n ∧
    ∀ h b, b%3≠0 → run h n=b → run (h+2) (sibling n)=b := by
  obtain ⟨k,o,eq,odd⟩ := split_twos n pos
  have od : o%3=0 := by
    apply Classical.byContradiction
    intro hu
    exact unit_pow_two k o hu (eq ▸ div)
  rw [eq,sibling_rep k o odd]
  refine ⟨unit_pow_two _ _ (by omega),?_,?_⟩
  · have le := Nat.mul_le_mul_left (2^k) (show 4*o+1≤5*o by omega)
    simpa only [Nat.mul_left_comm (2^k) 5] using le
  · intro h b unit hit
    have late : k<h := by
      apply Classical.byContradiction
      intro no
      have repr : 2^k*o=2^h*(2^(k-h)*o) := by
        rw [←Nat.mul_assoc,←Nat.pow_add,show h+(k-h)=k by omega]
      rw [repr,halve] at hit
      have zero : (2^(k-h)*o)%3=0 := by simp [Nat.mul_mod,od]
      exact unit (hit ▸ zero)
    let j := h-(k+1)
    have clock : h=k+(1+j) := by dsimp [j]; omega
    have extra : h+2=k+(3+j) := by omega
    have agree : run 3 (4*o+1)=step o := by
      have first : step (4*o+1)=2*(3*o+1) := by
        simp only [step,if_neg (show (4*o+1)%2≠0 by omega)]
        omega
      change run 2 (step (4*o+1))=step o
      rw [first]
      change run 1 (step (2*(3*o+1)))=step o
      rw [show step (2*(3*o+1))=3*o+1 by simp [step]]
      change step (3*o+1)=step o
      rw [show step (3*o+1)=(3*o+1)/2 by simp [step,show (3*o+1)%2=0 by omega]]
      simp [step,odd]
    rw [clock,run_add k,halve,run_add 1] at hit
    rw [extra,run_add k,halve,run_add 3,agree]
    exact hit

private def seed (r : Nat) : Nat := ([0,4,8,0,20,26,0,37,40] : List Nat)[r]?.getD 0
private def other (u : Nat) := seed (u%9)+48*(u/9)

private theorem seeds : ∀ i : Fin 9, i.val%3≠0 →
    (track 4 (seed i.val) 0=(i.val,1) ∧ (seed i.val)%3≠0 ∧
      (seed i.val)%16≠0 ∧ 3*seed i.val<16*i.val) := by decide +kernel

private theorem other_spec {u : Nat} (unit : u%3≠0) :
    run 4 (other u)=u ∧ (other u)%3≠0 ∧ (other u)%16≠0 ∧ 3*other u≤16*u := by
  let r := u%9
  let v := u/9
  have ru : r%3≠0 := by simpa only [r,Nat.mod_mod_of_dvd _ (by decide : 3∣9)] using unit
  obtain ⟨val,un,tag,bound⟩ := seeds ⟨r,Nat.mod_lt _ (by decide)⟩ ru
  change track 4 (seed r) 0=(r,1) at val
  change seed r%3≠0 at un
  change seed r%16≠0 at tag
  change 3*seed r<16*r at bound
  have split : r+9*v=u := Nat.mod_add_div u 9
  change run 4 (seed r+48*v)=u ∧ (seed r+48*v)%3≠0 ∧
    (seed r+48*v)%16≠0 ∧ 3*(seed r+48*v)≤16*u
  refine ⟨?_,by omega,by omega,by omega⟩
  rw [show seed r+48*v=seed r+2^4*3^0*(3*v) by omega,affine,val]
  change r+3*(3*v)=u
  omega

/-- An injective encoding of all positive starts into ordinary ternary units.
The two source types are decoded by the residue modulo 16 and four halvings
or shortcut steps. Every downstream unit target is retained. -/
def code (n : Nat) := if n%3=0 then other (sibling n) else 16*n

theorem code_spec {n : Nat} (pn : 0<n) :
    (code n)%3≠0 ∧ code n≤27*n ∧
    ∀ h b, b%3≠0 → run h n=b → ∃ j≤h+6, run j (code n)=b := by
  by_cases div : n%3=0
  · obtain ⟨unit,size,path⟩ := sibling_facts pn div
    obtain ⟨first,good,_,small⟩ := other_spec unit
    rw [code,if_pos div]
    refine ⟨good,by omega,?_⟩
    intro h b ub hit
    exact ⟨4+(h+2),by omega,by rw [run_add,first,path h b ub hit]⟩
  · rw [code,if_neg div]
    refine ⟨by omega,by omega,?_⟩
    intro h b _ hit
    refine ⟨4+h,by omega,?_⟩
    change run (4+h) (2^4*n)=b
    rw [run_add,halve,hit]

theorem code_injective {n m : Nat} (pn : 0<n) (pm : 0<m) (eq : code n=code m) : n=m := by
  unfold code at eq
  by_cases dn : n%3=0 <;> by_cases dm : m%3=0
  · rw [if_pos dn,if_pos dm] at eq
    have a := (other_spec (sibling_facts pn dn).1).1
    have b := (other_spec (sibling_facts pm dm).1).1
    rw [eq,b] at a
    exact sibling_inj pn pm a.symm
  · rw [if_pos dn,if_neg dm] at eq
    have a := (other_spec (sibling_facts pn dn).1).2.2.1
    rw [eq] at a; omega
  · rw [if_neg dn,if_pos dm] at eq
    have b := (other_spec (sibling_facts pm dm).1).2.2.1
    rw [←eq] at b; omega
  · rw [if_neg dn,if_neg dm] at eq; omega

#print axioms code_spec
#print axioms code_injective
end Collatz.Itinerary.BasinUnitEncoding
