import EvenMinimum
import AscentMerger

/-! Ordinary unbounded odd-ancestor exchange, including the even count
on the triple of each individual positive source. -/
namespace Collatz.AncestorExchange
open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.RankTwoControl
open Collatz.SignedBudget Collatz.EvenMinimum

set_option maxHeartbeats 1500000

theorem lifted_odds (H n k : Nat) : odds H (n+2^H*k)=odds H n := by
  have v:=(signed_lift H (n:Int) (k:Int)).2
  have a:=(physical H (n+2^H*k)).2
  have b:=(physical H n).2
  push_cast at a
  exact a.symm.trans (v.trans b)

/-- At every depth at least three the true triple has exactly two even
departures before the common output. The final lower output is fixed. -/
theorem triple_stack (k u : Nat) (pos : 0<u) :
    let w:=2^(k+3)*u-1
    run (k+3) w=3^(k+3)*u-1 ∧ odds (k+3) w=k+3 ∧
    run (k+3) (3*w)=3^(k+2)*u-1 ∧ odds (k+3) (3*w)=k+1 := by
  dsimp only
  obtain ⟨low,lo⟩:=Collatz.AscentMerger.ramp (k+3) u pos
  refine ⟨low,lo,?_⟩
  let v:=2^k*u
  have vp : 0<v := Nat.mul_pos (Nat.two_pow_pos _) pos
  have eq : 2^(k+3)*u=8*v := by dsimp [v];rw [pow_add];ring
  have shape : 3*(2^(k+3)*u-1)=5+8*(3*v-1) := by rw [eq];omega
  have lr:=lift 3 5 (3*v-1)
  change run 3 (5+8*(3*v-1))=2+3*(3*v-1) at lr
  have la:=lifted_odds 3 5 (3*v-1)
  change odds 3 (5+8*(3*v-1))=1 at la
  obtain ⟨ra,oa⟩:=append 3 k (3*(2^(k+3)*u-1))
  rw [shape,lr] at ra
  rw [shape,lr,la] at oa
  have target : 2+3*(3*v-1)=2^k*(9*u)-1 := by
    have ident : 2^k*(9*u)=9*v := by dsimp [v];ring
    rw [ident];omega
  rw [target,(Collatz.AscentMerger.ramp k (9*u) (by omega)).1] at ra
  rw [target,(Collatz.AscentMerger.ramp k (9*u) (by omega)).2] at oa
  have same : 3^k*(9*u)=3^(k+2)*u := by rw [pow_add];ring
  rw [same] at ra
  rw [shape,show k+3=3+k by omega]
  exact ⟨ra,by omega⟩

/-- For any odd target the depth-two and all deeper ancestors share the
same positive upper endpoint, at a site-dependent clock with two evens. -/
theorem odd_stack (l u z : Nat) (depth : 2≤l) (pos : 0<u)
    (shape : z+1=3^l*u) (odd : z%2=1) :
    let w:=2^l*u-1
    run l w=z ∧ odds l w=l ∧
    run (l+1) (3*w)=(z-1)/2 ∧ odds (l+1) (3*w)=l-1 := by
  dsimp only
  obtain ⟨rl,ol⟩:=Collatz.AscentMerger.ramp l u pos
  refine ⟨by omega,ol,?_⟩
  by_cases small : l=2
  · subst l
    have triple : 3*(2^2*u-1)=1+4*(3*u-1) := by omega
    have lr:=lift 2 1 (3*u-1)
    have la:=lifted_odds 2 1 (3*u-1)
    change run 2 (1+4*(3*u-1))=1+3*(3*u-1) at lr
    change odds 2 (1+4*(3*u-1))=1 at la
    obtain ⟨r,o⟩:=append 2 1 (3*(2^2*u-1))
    rw [triple,lr] at r
    rw [triple,lr,la] at o
    change run 3 _=step (1+3*(3*u-1)) at r
    change odds 3 _=1+(0+(1+3*(3*u-1))%2) at o
    rw [triple,r,o]
    unfold step;split <;> constructor <;> omega
  · obtain ⟨k,hk⟩:=Nat.exists_eq_add_of_le (show 3≤l by omega)
    have kl : l=k+3 := by omega
    rw [kl] at shape ⊢
    obtain ⟨_,_,a,b⟩:=triple_stack k u pos
    obtain ⟨ra,oa⟩:=append (k+3) 1 (3*(2^(k+3)*u-1))
    rw [a] at ra
    rw [a,b] at oa
    have eq : 3^(k+3)*u=3*(3^(k+2)*u) := by rw [pow_succ];ring
    rw [eq] at shape
    change run _ _=step (3^(k+2)*u-1) at ra
    change odds _ _=(k+1)+(0+(3^(k+2)*u-1)%2) at oa
    have oddThree : (3^(k+2))%2=1 := by
      rw [Nat.pow_mod];norm_num
    have evenU : u%2=0 := by
      have h:=congrArg (fun v:Nat=>v%2) shape
      have mod2 : (3*(3^(k+2)*u))%2=u%2 := by
        rw [Nat.mul_mod, Nat.mul_mod (3^(k+2)),oddThree];omega
      rw [mod2] at h
      omega
    have parity : (3^(k+2)*u)%2=0 := by rw [Nat.mul_mod,evenU];simp
    rw [ra,oa]
    unfold step;split <;> constructor <;> omega

private theorem split_site (v n : Nat) (eq : 81*v+176=8192*n) :
    v=1616+8192*(v/8192) ∧ 17+81*(v/8192)=1+n := by
  have ar : v+8192*(22*v+48)=1616+8192*(2225*n) := by omega
  have md:=congrArg (fun t:Nat=>t%8192) ar
  simp only [Nat.add_mul_mod_self_left] at md
  have dec:=Nat.mod_add_div v 8192
  omega

/-- Each physical gap-six stack reaches the stated small upper site. -/
theorem physical_stack (j l u z : Nat) (large : 7≤j) (depth : 2≤l)
    (pos : 0<u) (shape : z+1=3^l*u) (odd : z%2=1)
    (family : 81*z+271=128*2^j) :
    let w:=2^l*u-1
    run l w=z ∧ odds l w=l ∧
    run (l+14) (3*w)=1+2^(j-7) ∧ odds (l+14) (3*w)=l+3 := by
  dsimp only
  obtain ⟨rl,ol,r,o⟩:=odd_stack l u z depth pos shape odd
  refine ⟨rl,ol,?_⟩
  have power : (2:Nat)^j=128*2^(j-7) := by
    calc
      (2:Nat)^j = 2^(7+(j-7)) := by congr 1;omega
      _ = _ := by rw [pow_add];rfl
  let v:=(z-1)/2
  have eq : 81*v+176=8192*2^(j-7) := by dsimp [v];rw [power] at family;omega
  obtain ⟨site,out⟩:=split_site _ _ eq
  have lift13:=lift 13 1616 (v/8192)
  change run 13 (1616+8192*(v/8192))=17+81*(v/8192) at lift13
  have o13:=lifted_odds 13 1616 (v/8192)
  change odds 13 (1616+8192*(v/8192))=4 at o13
  have r13 : run 13 v=1+2^(j-7) := by
    conv_lhs => rw [site,lift13]
    exact out
  have c13 : odds 13 v=4 := by
    conv_lhs => rw [site,o13]
  obtain ⟨rr,oo⟩:=append (l+1) 13 (3*(2^l*u-1))
  rw [r,r13] at rr
  rw [r,o,c13] at oo
  change odds (l+14) (3*(2^l*u-1))=(l-1)+4 at oo
  exact ⟨rr,by omega⟩

#print axioms triple_stack
#print axioms odd_stack
#print axioms physical_stack
end Collatz.AncestorExchange
