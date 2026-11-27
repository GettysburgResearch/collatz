import EvenMinimum
import AscentMerger
import Mathlib.Data.Nat.ModEq

/-! Complete three-odd, score j+2 exclusion on the bounded gap-six
branch. The last odd clock is an arbitrary natural number. -/
namespace Collatz.ScoreTwo
open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.RankTwoControl

set_option maxHeartbeats 2500000

private theorem split_binary (h r x B : Nat) (small : r<2^h)
    (unit : Nat.gcd (2^h) 81=1) (rr : 2^h ∣ 81*r+B)
    (xx : 2^h ∣ 81*x+B) : x=r+2^h*(x/2^h) := by
  have same := xx.modEq_zero_nat.trans rr.modEq_zero_nat.symm
  have residues:=Nat.ModEq.cancel_left_of_coprime unit (Nat.ModEq.add_right_cancel' B same)
  change x%(2^h)=r%(2^h) at residues
  rw [Nat.mod_eq_of_lt small] at residues
  exact (Nat.mod_add_div x (2^h)).symm.trans (by rw [residues])

private theorem prefix_divisor (h H x A b : Nat) (hb : h≤b) (bh : b≤H)
    (certificate : 81*x+A+2^b=2^H) : 2^h ∣ 81*x+A := by
  apply (Nat.dvd_add_iff_left (pow_dvd_pow (2:Nat) hb)).mpr
  rw [certificate]
  exact pow_dvd_pow _ (hb.trans bh)

private theorem direct (h r x N : Nat) (site : x=r+2^h*(x/2^h))
    (pay : 0<run h r+3^(odds h r)*(x/2^h) ∧
           8*(run h r+3^(odds h r)*(x/2^h))<3*N)
    (floor : ∀ y, 0<y → 8*y<3*N → Good y) : Good x := by
  have rr : run h x=run h r+3^(odds h r)*(x/2^h) := by
    conv_lhs => rw [site,lift]
  exact (good_run h x).mp (rr ▸ floor _ pay.1 pay.2)

private theorem far (a b H x N : Nat) (ha : 10≤a) (ab : a<b) (bh : b≤H)
    (_large : 2048≤N) (size : 81*x≤32*N)
    (cert : 81*x+(9+3*2^a)+2^b=2^H)
    (floor : ∀ y, 0<y → 8*y<3*N → Good y) : Good x := by
  have dv:=prefix_divisor 10 H x (9+3*2^a) b (by omega) bh cert
  have dm : 2^10 ∣ 3*2^a := dvd_mul_of_dvd_right (pow_dvd_pow 2 ha) _
  have dn : 2^10 ∣ 81*x+9 :=
    (Nat.dvd_add_iff_left dm).mpr (by simpa only [Nat.add_assoc] using dv)
  have site:=split_binary 10 455 x 9 (by decide) (by decide) (by decide) dn
  apply direct 10 455 x N site _ floor
  change 0<325+729*(x/1024) ∧ 8*(325+729*(x/1024))<3*N
  norm_num at site
  omega

private def depth : Nat → Nat
  | 1 => 2 | 2 => 10 | 3 => 13 | 4 => 5 | 5 => 6
  | 6 => 7 | 7 => 10 | 8 => 9 | 9 => 18 | _ => 0

private theorem sufficient_bits (a b : Nat) (ha : 1≤a) (small : a≤9) (ab : a<b)
    (res : (9+3*2^a+2^b)%81=65536%81) : depth a≤b := by
  by_cases big : 18≤b
  · interval_cases a <;> norm_num [depth] <;> omega
  · have little : b≤17 := by omega
    interval_cases a <;> interval_cases b <;> norm_num [depth] at *

private theorem complete_mod (m a b x : Nat)
    (cert : 81*x+(9+3*2^a)+2^b=2^(16+162*m)) :
    (9+3*2^a+2^b)%81=65536%81 := by
  have rotate : (2:Nat)^162 ≡ 1 [MOD 81] := by decide
  have main:= (rotate.pow m).mul_left ((2:Nat)^16)
  rw [one_pow,Nat.mul_one,←pow_mul,←pow_add] at main
  change 2^(16+162*m)%81=65536%81 at main
  rw [←cert] at main
  simpa only [Nat.add_assoc,Nat.mul_add_mod_self_left] using main

private theorem direct_rows (a b H x N : Nat)
    (row : a=1 ∨ a=2 ∨ a=3 ∨ a=4 ∨ a=6 ∨ a=8)
    (hb : depth a≤b) (bh : b≤H) (_large : 2048≤N) (size : 81*x≤32*N)
    (cert : 81*x+(9+3*2^a)+2^b=2^H)
    (floor : ∀ y, 0<y → 8*y<3*N → Good y) : Good x := by
  have dv:=prefix_divisor (depth a) H x (9+3*2^a) b hb bh cert
  rcases row with h|h|h|h|h|h <;> subst a
  · have site:=split_binary 2 1 x 15 (by decide) (by decide) (by decide) dv
    apply direct 2 1 x N site _ floor
    change 0<1+3*(x/4) ∧ 8*(1+3*(x/4))<3*N
    norm_num at site
    omega
  · have site:=split_binary 10 379 x 21 (by decide) (by decide) (by decide) dv
    apply direct 10 379 x N site _ floor
    change 0<271+729*(x/1024) ∧ 8*(271+729*(x/1024))<3*N
    norm_num at site
    omega
  · have site:=split_binary 13 303 x 33 (by decide) (by decide) (by decide) dv
    apply direct 13 303 x N site _ floor
    change 0<244+6561*(x/8192) ∧ 8*(244+6561*(x/8192))<3*N
    norm_num at site
    omega
  · have site:=split_binary 5 23 x 57 (by decide) (by decide) (by decide) dv
    apply direct 5 23 x N site _ floor
    change 0<20+27*(x/32) ∧ 8*(20+27*(x/32))<3*N
    norm_num at site
    omega
  · have site:=split_binary 7 7 x 201 (by decide) (by decide) (by decide) dv
    apply direct 7 7 x N site _ floor
    change 0<5+81*(x/128) ∧ 8*(5+81*(x/128))<3*N
    norm_num at site
    omega
  · have site:=split_binary 9 199 x 777 (by decide) (by decide) (by decide) dv
    apply direct 9 199 x N site _ floor
    change 0<95+243*(x/512) ∧ 8*(95+243*(x/512))<3*N
    norm_num at site
    omega

private theorem seven (b H x z N : Nat) (hb : 10≤b) (bh : b≤H)
    (large : 2048≤N) (size : 81*x≤32*N) (pin : 81*z+271=128*N)
    (cert : 81*x+(9+3*2^7)+2^b=2^H)
    (floor : ∀ y, 0<y → 8*y<3*N → Good y)
    (least : ∀ y, 0<y → y<z → y%48=17 → Good (3*y) → Good y) : Good x := by
  have dv:=prefix_divisor 10 H x 393 b hb bh cert
  have site:=split_binary 10 71 x 393 (by decide) (by decide) (by decide) dv
  let t:=x/1024
  change x=71+1024*t at site
  have rr:=lift 2 71 (256*t)
  change run 2 (71+4*(256*t))=161+9*(256*t) at rr
  have low : run 2 x=161+2304*t := by
    conv_lhs => rw [site,show 71+1024*t=71+4*(256*t) by ring,rr]
    ring
  have ru:=lift 8 483 (27*t)
  change run 8 (483+256*(27*t))=17+9*(27*t) at ru
  have hi : run 8 (3*(161+2304*t))=17+243*t := by
    rw [show 3*(161+2304*t)=483+256*(27*t) by ring,ru]
    ring
  have sg:=floor (17+243*t) (by omega) (by omega)
  have up := (good_run 8 (3*(161+2304*t))).mp (hi ▸ sg)
  have lo:=least (161+2304*t) (by omega) (by omega) (by omega) up
  exact (good_run 2 x).mp (low ▸ lo)

private theorem nine (b H x N : Nat) (hb : 18≤b) (bh : b≤H)
    (_large : 2048≤N) (size : 81*x≤32*N)
    (cert : 81*x+(9+3*2^9)+2^b=2^H)
    (triple : ∀ y, 0<y → 3∣y → 4*y<3*N → Good y) : Good x := by
  have dv:=prefix_divisor 18 H x 1545 b hb bh cert
  have site:=split_binary 18 19399 x 1545 (by decide) (by decide) (by decide) dv
  let t:=x/262144
  change x=19399+262144*t at site
  have rx:=lift 18 19399 t
  change run 18 (19399+262144*t)=39332+531441*t at rx
  have ry:=lift 4 23307 (19683*t)
  change run 4 (23307+16*(19683*t))=39332+27*(19683*t) at ry
  have gg:=triple (23307+16*(19683*t)) (by omega) (by exact ⟨7769+104976*t,by ring⟩) (by omega)
  have yy:=(good_run 4 _).mpr gg
  rw [ry,show 39332+27*(19683*t)=39332+531441*t by ring,←rx,←site] at yy
  exact (good_run 18 x).mp yy

/-- Reuse one complete upper odd run on each side of the positive merge. -/
private theorem neighbors (k V : Nat) (vpos : 0<V) (phase : (3^k*V)%4=3) :
    Good (2^(k+1)*V-1) ↔ Good (2^k*V-1) := by
  have hi:=(Collatz.AscentMerger.ramp (k+1) V vpos).1
  have lo:=(Collatz.AscentMerger.ramp k V vpos).1
  let t:=(3^k*V)/4
  have d : 3^k*V=4*t+3 := by dsimp [t];omega
  have dhi : 3^(k+1)*V=3*(3^k*V) := by rw [pow_succ];ring
  have h₁ : run 2 (3^(k+1)*V-1)=3*t+2 := by
    rw [dhi,d]
    simp only [run,step];split <;> split <;> omega
  have h₂ : run 2 (3^k*V-1)=3*t+2 := by
    rw [d]
    simp only [run,step];split <;> split <;> omega
  rw [←good_run (k+1) (2^(k+1)*V-1),←good_run k (2^k*V-1),hi,lo,
      ←good_run 2 (3^(k+1)*V-1),←good_run 2 (3^k*V-1),h₁,h₂]

private def rep : Nat → Nat
  | 0 => 1
  | k+1 => 4*rep k+1

private theorem rep_info (t : Nat) : 3*rep t+1=2^(2+2*t) ∧ rep t%4=1 ∧ 0<rep t := by
  induction t with
  | zero => decide
  | succ t ih =>
    rw [show 2+2*(t+1)=(2+2*t)+2 by omega,pow_add,←ih.1]
    simp only [rep];constructor
    · ring
    · omega

private theorem five (u t x N : Nat) (_size : 81*x≤32*N)
    (cert : 81*x+105+2^(6+2*u)=32*N)
    (product : 32*N=2^(6+2*u)*2^(2+2*t))
    (floor : ∀ y, 0<y → 8*y<3*N → Good y) : Good x := by
  let k:=1+2*u
  let V:=rep t
  obtain ⟨rv,par,pos⟩:=rep_info t
  change 3*V+1=2^(2+2*t) at rv
  change V%4=1 at par
  change 0<V at pos
  have poweq : (2:Nat)^(6+2*u)=32*2^k := by
    dsimp [k];rw [show 6+2*u=5+(1+2*u) by omega,pow_add];rfl
  rw [poweq] at cert product
  rw [←rv] at product
  let A:=2^k*V
  have Ap : 0<A := Nat.mul_pos (Nat.two_pow_pos _) pos
  have rel : 27*x+35=32*A := by dsimp [A];nlinarith only [cert,product]
  have dv : 16∣81*x+105 := ⟨6*A,by omega⟩
  have site:=split_binary 4 7 x 105 (by decide) (by decide) (by decide) dv
  have rr:=lift 4 7 (x/16)
  change run 4 (7+16*(x/16))=13+27*(x/16) at rr
  change x=7+16*(x/16) at site
  have r : run 4 x=2^(k+1)*V-1 := by
    conv_lhs => rw [site,rr]
    rw [pow_succ,show (2^k*2)*V=2*A by dsimp [A];ring]
    omega
  have p3 : (3:Nat)^k%4=3 := by
    dsimp [k];rw [pow_add,pow_mul]
    have eqv : (9:Nat)≡1 [MOD 4] := by decide
    have eqn:=(eqv.pow u).mul_left 3
    change (3*9^u)%4=3
    change (3*9^u)%4=(3*1^u)%4 at eqn
    simpa using eqn
  have mod : (3^k*V)%4=3 := by rw [Nat.mul_mod,p3,par]
  have safe:=floor (A-1) (by
    have p : 2≤(2:Nat)^k := by dsimp [k];exact Nat.pow_le_pow_right (by decide : 0<(2:Nat)) (by omega : 1≤1+2*u)
    have L:=Nat.mul_le_mul p (show 1≤V by omega)
    dsimp [A];omega) (by omega)
  have g:=(neighbors k V pos mod).mpr safe
  exact (good_run 4 x).mp (r ▸ g)

private theorem even_exponent (b : Nat) (cong : 2^b%3=1) : b%2=0 := by
  by_contra no
  let k:= b/2
  have fb : b=2*k+1 := by dsimp [k];omega
  rw [fb,pow_add,pow_mul] at cong
  have base : (4:Nat)≡1 [MOD 3] := by decide
  have cl:=(base.pow k).mul_right 2
  change (4^k*2)%3=(1^k*2)%3 at cl
  norm_num at cl
  change (4^k*2)%3=1 at cong
  omega

/-- Every true upper word of the indicated score-two three-odd shape
has a good lower source under its original three ordinary tests. -/
theorem score_two (m a b x z N : Nat) (ha : 1≤a) (ab : a<b)
    (bh : b<16+162*m) (large : 2048≤N)
    (power : 32*N=2^(16+162*m)) (pin : 81*z+271=128*N)
    (cert : 81*x+(9+3*2^a)+2^b=32*N)
    (floor : ∀ y, 0<y → 8*y<3*N → Good y)
    (triple : ∀ y, 0<y → 3∣y → 4*y<3*N → Good y)
    (least : ∀ y, 0<y → y<z → y%48=17 → Good (3*y) → Good y) : Good x := by
  have full:=cert.trans power
  have cap : 81*x≤32*N := by
    rw [←cert]
    exact (Nat.le_add_right _ _).trans (Nat.le_add_right _ _)
  by_cases farGap : 10≤a
  · exact far a b _ x N farGap ab bh.le large cap full floor
  have am : a≤9 := by omega
  have res:=complete_mod m a b x full
  have bits:=sufficient_bits a b ha am ab res
  by_cases av : a=5
  · subst a
    have mod3 : (9+3*2^5+2^b)%3=65536%3 := by
      change 9+3*2^5+2^b ≡ 65536 [MOD 3]
      exact (show 9+3*2^5+2^b ≡ 65536 [MOD 81] from res).of_dvd (by decide)
    have evenb:=even_exponent b (by omega)
    let u:=(b-6)/2
    let t:=(16+162*m-b-2)/2
    have eqb : b=6+2*u := by dsimp [u];change 6≤b at bits;omega
    have eqh : 16+162*m=(6+2*u)+(2+2*t) := by dsimp [t];omega
    exact five u t x N cap (by rw [←eqb];norm_num at cert;exact cert) (by rw [power,eqh,pow_add]) floor
  by_cases av7 : a=7
  · subst a
    exact seven b _ x z N bits bh.le large cap pin full floor least
  by_cases av9 : a=9
  · subst a
    exact nine b _ x N bits bh.le large cap full triple
  exact direct_rows a b _ x N (by omega) bits bh.le large cap full floor

#print axioms score_two
end Collatz.ScoreTwo
