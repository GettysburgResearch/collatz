import SignedHardFamily
import Mathlib.Tactic.Linarith

set_option maxHeartbeats 2000000

namespace Collatz.TernaryPortal

private theorem exchange (w : Nat) (hm : w%27=10) (hb : w%8=7) :
    ∃ y, y%48=17 ∧ 9*y+7=16*w ∧ run 4 y=w ∧ odds 4 y=2 ∧
    run 7 (3*y)=run 3 (3*w) ∧ odds 7 (3*y)=3 ∧ odds 3 (3*w)=1 := by
  have eq : w=199+216*(w/216) := by omega
  let s := w/216
  have lo := prefix_lift 4 353 (24*s)
  have up := prefix_lift 7 1059 (9*s)
  have old := prefix_lift 3 597 (81*s)
  norm_num [show run 4 353=199 by decide,show odds 4 353=2 by decide,
    show run 7 1059=224 by decide,show odds 7 1059=3 by decide,
    show run 3 597=224 by decide,show odds 3 597=1 by decide] at lo up old
  refine ⟨353+384*s,by omega,by change 9*(353+384*(w/216))+7=16*w; omega,?_,?_,?_,?_,?_⟩
  · calc
      _ = 199+9*(24*s) := by convert lo.1 using 2; ring
      _ = w := by dsimp [s]; omega
  · convert lo.2 using 2; ring
  · have ul : 3*(353+384*s)=1059+128*(9*s) := by ring
    have ur : 3*w=597+8*(81*s) := by dsimp [s]; omega
    rw [ul,ur]
    calc
      _ = 224+27*(9*s) := by convert up.1 using 2
      _ = 224+3*(81*s) := by ring
      _ = _ := by convert old.1.symm using 2
  · convert up.2 using 2; ring
  · have ur : 3*w=597+8*(81*s) := by dsimp [s]; omega
    rw [ur]
    convert old.2 using 2

private theorem scale_nine (n : Nat) :
    32*2^19*2^(9+n)<27*3^9*3^(9+n) := by
  induction n with
  | zero => decide
  | succ n ih =>
    have h2 : (2:Nat)^(9+(n+1))=2^(9+n)*2 := pow_succ _ _
    have h3 : (3:Nat)^(9+(n+1))=3^(9+n)*3 := pow_succ _ _
    rw [h2,h3]
    calc
      _ = (32*2^19*2^(9+n))*2 := by ring
      _ < (27*3^9*3^(9+n))*2 := Nat.mul_lt_mul_of_pos_right ih (by decide)
      _ ≤ (27*3^9*3^(9+n))*3 := Nat.mul_le_mul_left _ (by decide)
      _ = _ := by ring

private theorem smaller_narrow {k t parent z n y : Nat} (hk : 9≤k) (ht : 0<t) (_hn : 512≤n)
    (old : 81*parent+271=512*n) (seed : 19683*z+1293643=2097152*n)
    (lap : z+1=3^k*(8*t)) (edge : 9*y+7=16*(2^k*(8*t)-1)) : y<parent := by
  obtain ⟨d,rfl⟩ := Nat.exists_eq_add_of_le hk
  have scal := Nat.mul_lt_mul_of_pos_right (scale_nine d) (Nat.mul_pos (by decide : 0<8) ht)
  have l : 32*2^19*(2^(9+d)*(8*t)) < 27*(19683*(z+1)) := by
    rw [lap]
    convert scal using 1 <;> ring
  have seedbound : 19683*(z+1)<2097152*n := by omega
  have result : 32*524288*(2^(9+d)*(8*t))<27*(2097152*n) :=
    l.trans (Nat.mul_lt_mul_of_pos_left seedbound (by decide : 0<27))
  omega

/-- A paid source with three more prescribed ternary digits has a smaller
canonical representative starting at k=9. -/
theorem signed_narrow (k minimum : Nat) (hk : 9≤k) :
    ∃ j ≥ minimum, ∃ original y : Nat, y%48=17 ∧ original%48=17 ∧ 0<y ∧ y<original ∧
      81*original+271=2^(18+162*j) ∧
      run (k+23) y=2^(11+162*j)-1 ∧ odds (k+23) y=k+11 ∧
      run (k+25) (3*y)=2^(9+162*j) ∧ odds (k+25) (3*y)=k+10 ∧
      ∀ H, run H (3*original)=1 → run (H+k+16) (3*y)=1 ∧
        odds (H+k+16) (3*y)=odds H (3*original)+k+7 := by
  let s := 11*14^k
  let m := 3^(9+k)
  let target := 1273960+m*s
  have modm : m%243=0 := by
    dsimp [m]
    rw [show 9+k=5+(4+k) by omega,pow_add,show (3:Nat)^5=243 by decide]
    omega
  have addr : target%243=154 := by
    dsimp [target]
    rw [Nat.add_mod,Nat.mul_mod m s,modm]
    simp
  obtain ⟨j,hj,c,jump⟩ := Collatz.SignedMersenneIndex.compatible_target (7+k) minimum target addr
  let v := s+27*c
  have link : 2^(30+162*j)=1273960+3^(9+k)*v := by
    rw [jump,show 5+(7+k)=(9+k)+3 by omega,pow_add]
    dsimp [target,m,v]
    ring
  obtain ⟨parent,z,t,ht,canon,old,seed,lap,vt⟩ := prepare_signed link
  let w:=2^k*(8*t)-1
  have pos := Nat.mul_pos (Nat.two_pow_pos k) (Nat.mul_pos (by decide : 0<8) ht)
  have wp : w+1=2^k*(8*t) := Nat.sub_add_cancel pos
  have wb : w%8=7 := by rw [show w=8*(2^k*t)-1 by dsimp [w]; ring_nf]; have := Nat.mul_pos (Nat.two_pow_pos k) ht; omega
  have factor : (2:Nat)^k*v=11*28^k+27*(2^k*c) := by dsimp [v,s]; rw [show (28:Nat)=2*14 by decide,mul_pow]; ring
  have md : (28:Nat)^k ≡ 1 [MOD 27] := by simpa using (show 28 ≡ 1 [MOD 27] by decide).pow k
  have md' : (28:Nat)^k%27=1 := md
  have wm : w%27=10 := by rw [←vt,factor] at wp; omega
  obtain ⟨y,cy,edge,yw,oy,upper,ou,ow⟩ := exchange w wm wb
  obtain ⟨wl,wo,wu,uw⟩ := hard_mersenne_paid ht seed lap
  change run (k+19) w=4*2^(9+162*j)-1 at wl
  change odds (k+19) w=k+9 at wo
  change run (k+21) (3*w)=2^(9+162*j) at wu
  change odds (k+21) (3*w)=k+8 at uw
  have hn : 512≤(2:Nat)^(9+162*j) := Nat.pow_le_pow_right (by decide : 0<2) (show 9≤9+162*j by omega)
  have lt := smaller_narrow hk ht hn old seed lap edge
  have yp : 0<y := by omega
  refine ⟨j,hj,parent,y,cy,canon,yp,lt,?_,?_,?_,?_,?_,?_⟩
  · rw [show 18+162*j=9+(9+162*j) by omega,pow_add]
    exact old
  · rw [show k+23=4+(k+19) by omega,run_add,yw,wl,
        show 11+162*j=2+(9+162*j) by omega,pow_add (2:Nat) 2 (9+162*j)]
    rfl
  · rw [show k+23=4+(k+19) by omega,odds_add,oy,yw,wo]
    omega
  · rw [show k+25=7+(k+18) by omega,run_add,upper,←run_add,show 3+(k+18)=k+21 by omega,wu]
  · rw [show k+25=7+(k+18) by omega,odds_add,ou,upper]
    rw [show k+21=3+(k+18) by omega,odds_add,ow] at uw
    omega
  · intro H hit
    obtain ⟨hitW,oddW⟩ := hard_mersenne_certificate ht (lt_of_lt_of_le (by decide : 2<512) hn) old seed lap hit
    change run (H+k+12) (3*w)=1 at hitW
    change odds (H+k+12) (3*w)=odds H (3*parent)+k+5 at oddW
    rw [show H+k+12=3+(H+k+9) by omega,run_add] at hitW
    rw [show H+k+12=3+(H+k+9) by omega,odds_add,ow] at oddW
    rw [show H+k+16=7+(H+k+9) by omega,run_add,odds_add,upper,ou,hitW]
    omega

#print axioms signed_narrow

end Collatz.TernaryPortal
