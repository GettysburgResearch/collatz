import RankTwoControl
import AscentMerger
import MinimumFailure
import Mathlib.Data.Nat.ModEq

/-! Positive-exponent anchors for the gap-six Mersenne row. Clocks count
actual shortcut applications. The two-power perturbation is kept at the
same original exponent on both trajectories. -/
namespace Collatz.OrdinaryDerivative
open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.RankTwoControl

set_option maxRecDepth 10000
set_option maxHeartbeats 2000000
set_option exponentiation.threshold 10000

/-- Remove a dyadic perturbation of a ternary power at an actual clock. -/
theorem peak_lift (a s H u : Nat) (perturb : 3^s=1+2^H*u) :
    run H (3^(a+s)-1)=run H (3^a-1)+3^(a+odds H (3^a-1))*u := by
  have ap : 1≤(3:Nat)^a := Nat.pow_pos (by decide)
  have form : (3:Nat)^(a+s)-1=(3^a-1)+2^H*(3^a*u) := by
    rw [pow_add,perturb,Nat.mul_add,Nat.mul_one]
    have e : (3:Nat)^a*(2^H*u)=2^H*(3^a*u) := by ring
    omega
  rw [form,lift,pow_add]
  ring

private theorem at_two (n : Nat) : run (2*n) 2=2 ∧ odds (2*n) 2=n := by
  induction n with
  | zero => decide
  | succ n ih =>
    obtain ⟨a,b⟩ := append 2 (2*n) 2
    rw [show run 2 2=2 by decide] at a b
    rw [show odds 2 2=1 by decide] at b
    rw [show 2*(n+1)=2+2*n by omega]
    exact ⟨a.trans ih.1,by omega⟩

/-- The entire long clock consists of ordinary visits to the 1,2 cycle
at both base points, followed by a physical affine lift. -/
theorem log_phases (r s u : Nat) (large : 43≤r) (powEq : 3^s=1+2^(2*r+3)*u) :
    run (2*r+3) (3^(11+s)-1)=1+3^13*(3^r*u) ∧
    run (2*r+3) (3^(6+s)-1)=2+3^10*(3^r*u) := by
  let k:=r-43
  have time : 2*r+3=89+2*k := by dsimp [k];omega
  have n11 : run 89 (3^11-1)=1 ∧ odds 89 (3^11-1)=45 := by decide
  have n6 : run 89 (3^6-1)=2 ∧ odds 89 (3^6-1)=47 := by decide
  obtain ⟨x,xc⟩ := append 89 (2*k) (3^11-1)
  obtain ⟨y,yc⟩ := append 89 (2*k) (3^6-1)
  rw [n11.1,(cycle_pairs k).1] at x
  rw [n11.1,n11.2,(cycle_pairs k).2] at xc
  rw [n6.1,(at_two k).1] at y
  rw [n6.1,n6.2,(at_two k).2] at yc
  obtain a:=peak_lift 11 s (2*r+3) u powEq
  obtain b:=peak_lift 6 s (2*r+3) u powEq
  rw [time,x,xc] at a
  rw [time,y,yc] at b
  rw [time,a,b,show 11+(45+k)=13+r by dsimp [k];omega,
    show 6+(47+k)=10+r by dsimp [k];omega,pow_add,pow_add]
  constructor <;> ring

def derivativeResidue : Nat := 164232366001155405

private theorem finite64 :
    run 64 (1+3^13*derivativeResidue)=2922489638071279607 ∧
    run 64 (2+3^10*derivativeResidue)=2922489638071279607 ∧
    odds 64 (1+3^13*derivativeResidue)=30 ∧
    odds 64 (2+3^10*derivativeResidue)=33 := by decide

private theorem lift_pair (H b U : Nat) (small : b<2^H)
    (unit : U ≡ b [MOD 2^H])
    (meeting : run H (1+3^13*b)=run H (2+3^10*b))
    (grade : 13+odds H (1+3^13*b)=10+odds H (2+3^10*b)) :
    run H (1+3^13*U)=run H (2+3^10*U) := by
  let v:=U/(2^H)
  have e : U=b+2^H*v := by
    change U%2^H=b%2^H at unit
    rw [Nat.mod_eq_of_lt small] at unit
    exact (Nat.mod_add_div U (2^H)).symm.trans (by rw [unit])
  have a:=lift H (1+3^13*b) (3^13*v)
  have d:=lift H (2+3^10*b) (3^10*v)
  rw [e,show 1+3^13*(b+2^H*v)=(1+3^13*b)+2^H*(3^13*v) by ring,
    show 2+3^10*(b+2^H*v)=(2+3^10*b)+2^H*(3^10*v) by ring,a,d,meeting]
  rw [←Nat.mul_assoc,←Nat.mul_assoc,←pow_add,←pow_add]
  rw [show odds H (1+3^13*b)+13=odds H (2+3^10*b)+10 by omega]

theorem derivative_merger (U : Nat) (unit : U ≡ derivativeResidue [MOD 2^64]) :
    run 64 (1+3^13*U)=run 64 (2+3^10*U) :=
  lift_pair 64 derivativeResidue U (by decide) unit
    (finite64.1.trans finite64.2.1.symm) (by rw [finite64.2.2.1,finite64.2.2.2])

def negativeResidue : Nat := 4447453652426232499

private theorem finite62 :
    run 62 (1+3^13*negativeResidue)=11724704031194517008 ∧
    run 62 (2+3^10*negativeResidue)=11724704031194517008 ∧
    odds 62 (1+3^13*negativeResidue)=27 ∧
    odds 62 (2+3^10*negativeResidue)=30 := by decide

theorem negative_merger (U : Nat) (unit : U ≡ negativeResidue [MOD 2^62]) :
    run 62 (1+3^13*U)=run 62 (2+3^10*U) :=
  lift_pair 62 negativeResidue U (by decide) unit
    (finite62.1.trans finite62.2.1.symm) (by rw [finite62.2.2.1,finite62.2.2.2])

/-- Both postpeak clocks grow with the valuation r. The second base exponent
is five less than the first and positive even at s=0. -/
theorem physical_log_meeting (r s u : Nat) (large : 43≤r)
    (powEq : 3^s=1+2^(2*r+3)*u) (unit : 3^r*u ≡ derivativeResidue [MOD 2^64]) :
    run (2*r+67) (3^(11+s)-1)=run (2*r+67) (3^(6+s)-1) := by
  obtain ⟨a,b⟩:=log_phases r s u large powEq
  rw [show 2*r+67=(2*r+3)+64 by omega,(append _ _ _).1,(append _ _ (3^(6+s)-1)).1,a,b]
  exact derivative_merger _ unit

theorem negative_log_meeting (r s u : Nat) (large : 43≤r)
    (powEq : 3^s=1+2^(2*r+3)*u) (unit : 3^r*u ≡ negativeResidue [MOD 2^62]) :
    run (2*r+65) (3^(11+s)-1)=run (2*r+65) (3^(6+s)-1) := by
  obtain ⟨a,b⟩:=log_phases r s u large powEq
  rw [show 2*r+65=(2*r+3)+62 by omega,(append _ _ _).1,(append _ _ (3^(6+s)-1)).1,a,b]
  exact negative_merger _ unit

private theorem finite499 :
    run 499 (3^173-1)=run 499 (3^164-1) ∧
    odds 499 (3^173-1)=241 ∧ odds 499 (3^164-1)=250 := by decide +kernel

theorem odd_anchor_meeting (s u : Nat) (powEq : 3^s=1+2^499*u) :
    run 499 (3^(173+s)-1)=run 499 (3^(164+s)-1) := by
  rw [peak_lift 173 s 499 u powEq,peak_lift 164 s 499 u powEq,
    finite499.1,finite499.2.1,finite499.2.2]

/-- A genuine postpeak meeting with any two-exponent saving yields a hit
at one under the stated bounded-cycle floor. -/
theorem floor_return (j n z H : Nat) (earlier : n+2≤j) (np : 0<n) (jp : 11≤j)
    (shape : 81*z+271=128*2^j)
    (floor : ∀ w, 0<w → 1024*w<243*z → Good w)
    (meet : run H (3^j-1)=run H (3^n-1)) : Good z := by
  have jb : 4*2^n≤(2:Nat)^j := by
    have q:=Nat.pow_le_pow_right (by decide : 0<(2:Nat)) earlier
    rw [pow_add] at q;omega
  have npos : 1<(2:Nat)^n := Nat.one_lt_two_pow (by omega)
  have smaller : Good (2^n-1) := floor _ (by omega) (by omega)
  have p1 := (good_run n (2^n-1)).mpr smaller
  have rn : run n (2^n-1)=3^n-1 := by simpa using (Collatz.AscentMerger.ramp n 1 (by decide)).1
  have rj : run j (2^j-1)=3^j-1 := by simpa using (Collatz.AscentMerger.ramp j 1 (by decide)).1
  rw [rn] at p1
  have merged := (good_run H (3^n-1)).mpr p1
  rw [←meet] at merged
  have goodj := (good_run H (3^j-1)).mp merged
  have low : Good (2^j-1) := (good_run j _).mp (rj ▸ goodj)
  obtain ⟨e,ee⟩:=Nat.exists_eq_add_of_le jp
  have powj : (2:Nat)^j=2048*2^e := by rw [ee,pow_add];rfl
  have zd : z=33+128*(z/128) := by rw [powj] at shape;omega
  have q:=lift 7 33 (z/128)
  change run 7 (33+128*(z/128))=22+81*(z/128) at q
  have zz : run 7 z=2^j-1 := by
    conv_lhs => rw [zd,q]
    omega
  exact (good_run 7 z).mp (zz ▸ low)

#print axioms peak_lift
#print axioms log_phases
#print axioms derivative_merger
#print axioms physical_log_meeting
#print axioms negative_merger
#print axioms negative_log_meeting
#print axioms odd_anchor_meeting
#print axioms floor_return
end Collatz.OrdinaryDerivative
