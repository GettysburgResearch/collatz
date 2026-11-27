import SignedBudget
import MinimumFailure

/-! A physical return from the negative-seventeen phase to a smaller visitor
shadowing the negative-five cycle. All clocks here are positive shortcuts. -/
namespace Collatz.PhaseReturn
set_option exponentiation.threshold 65536
set_option maxRecDepth 65536
open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.SignedBudget

private theorem sappend (a b : Nat) (x : Int) :
    travel (a+b) x=travel b (travel a x) ∧ digits (a+b) x=digits a x+digits b (travel a x) := by
  induction a generalizing x with
  | zero => simp [travel,digits]
  | succ a ih =>
    obtain ⟨f,p⟩ := ih (signedStep x)
    rw [Nat.succ_add]
    simp only [travel,digits,f,p]
    exact ⟨trivial,by omega⟩

private theorem laps (L p : Nat) (b : Int) (state : travel L b=b) (work : digits L b=p)
    (k : Nat) : travel (L*k) b=b ∧ digits (L*k) b=p*k := by
  induction k with
  | zero => simp [travel,digits]
  | succ k ih =>
    obtain ⟨a,c⟩ := sappend (L*k) L b
    rw [ih.1,state] at a
    rw [ih.1,ih.2,work] at c
    rw [Nat.mul_succ,Nat.mul_succ]
    exact ⟨a,c⟩

private theorem natLift (h x c n : Nat) (start : n+c=2^h*x) :
    (run h n:Int)=travel h (-(c:Int))+3^(digits h (-(c:Int)))*(x:Int) := by
  obtain ⟨s,_⟩ := signed_lift h (-(c:Int)) x
  obtain ⟨phys,_⟩ := physical h n
  have val : (n:Int)+(c:Int)=2^h*(x:Int) := by exact_mod_cast start
  have eqn : (n:Int) = -c+2^h*(x:Int) := by linarith only [val]
  rw [←eqn,phys] at s
  exact s

private theorem cross_row (v : Nat) : run 3 (24*v+16)=run 3 (8*v+4) := by
  have a := lift 3 16 (3*v)
  have b := lift 3 4 v
  change run 3 (16+8*(3*v))=2+1*(3*v) at a
  change run 3 (4+8*v)=2+3*v at b
  rw [show 24*v+16=16+8*(3*v) by ring,show 8*v+4=4+8*v by ring,a,b]; ring

/-- The three-clock merger applies at every even exponent, with an explicit
ordinary smaller candidate whose full incoming clock may grow arbitrarily. -/
theorem faster_phase (k : Nat) (positive : 1≤k) :
    Good (3^(2*k+2)-17) ↔ Good (2^(3*k+1)-5) := by
  have plus (d : Nat) : ∃ a : Nat, 3^(2*d+1)=8*a+3 := by
    induction d with
    | zero => exact ⟨0,by decide⟩
    | succ d ih =>
      obtain ⟨a,e⟩ := ih
      refine ⟨9*a+3,?_⟩
      rw [show 2*(d+1)+1=(2*d+1)+2 by omega,pow_add,e]; ring
  obtain ⟨a,power⟩ := plus k
  have big : 27≤(3:Nat)^(2*k+1) := Nat.pow_le_pow_right (by decide : 0<(3:Nat)) (show 3≤2*k+1 by omega)
  obtain ⟨v,eqn⟩ := Nat.exists_eq_add_of_le (show 1≤a by omega)
  have xeq : (3:Nat)^(2*k+2)-17=24*v+16 := by
    rw [show 2*k+2=(2*k+1)+1 by omega,pow_succ,power,eqn]; omega
  have yeq : (3:Nat)^(2*k+1)-7=8*v+4 := by rw [power,eqn]; omega
  obtain ⟨q0,p0⟩ := laps 3 2 (-5) (by decide) (by decide) k
  obtain ⟨q1,p1⟩ := sappend (3*k) 1 (-5)
  rw [q0,show travel 1 (-5)= -7 by decide] at q1
  rw [q0,p0,show digits 1 (-5)=1 by decide] at p1
  have bp : 8≤(2:Nat)^(3*k+1) := Nat.pow_le_pow_right (by decide : 0<(2:Nat)) (show 3≤3*k+1 by omega)
  have path := natLift (3*k+1) 1 5 (2^(3*k+1)-5) (by omega)
  change (run (3*k+1) (2^(3*k+1)-5):Int)=travel (3*k+1) (-5)+3^(digits (3*k+1) (-5))*1 at path
  rw [q1,p1] at path
  have end_eq : run (3*k+1) (2^(3*k+1)-5)=3^(2*k+1)-7 := by
    apply Int.ofNat_inj.mp
    rw [Nat.cast_sub (show 7≤(3:Nat)^(2*k+1) by omega)]
    push_cast
    rw [path]; ring
  calc
    _ ↔ Good (run 3 (24*v+16)) := by rw [xeq]; exact (good_run _ _).symm
    _ ↔ Good (8*v+4) := by rw [cross_row]; exact good_run _ _
    _ ↔ _ := by rw [←yeq,←end_eq]; exact good_run _ _

/-- Parameter for advancing eleven compatible rank-three exponents while
preserving every earlier ordinary bit of the base certificate. -/
def shift : Nat → Nat
  | 0 => 0
  | t+1 => 2^1782*shift t+(2^1782-1)/81

theorem shift_eq (t : Nat) : 81*shift t+1=2^(1782*t) := by
  induction t with
  | zero => decide
  | succ t ih =>
    have stepEq : 81*((2^1782-1)/81) + 1 = 2^1782 := by decide
    rw [shift,Nat.mul_succ,pow_add,←ih]
    let A : Nat := 2^1782
    let B : Nat := (2^1782-1)/81
    change 81*(A*shift t+B)+1=(81*shift t+1)*A
    have eqn : 81*B+1=A := stepEq
    calc
      _ = 81*shift t*A+(81*B+1) := by ring
      _ = _ := by rw [eqn]; ring

/-- Advance any genuine base word arriving at the phase −17 through the
supplied upper hit. Each eleven exponent increments contributes 162 laps. -/
theorem repeated_phase {z H k : Nat} (kpos : 1≤k)
    (lower : run H z=3^(2*k+2)-17) (count : odds H z=2*k+6) (t : Nat) :
    Good (z+2^H*shift t) ↔ Good (2^(3*(k+567*t)+1)-5) := by
  have lx := lift H z (shift t)
  rw [lower,count] at lx
  let b := run H (z+2^H*shift t)
  have large : 81≤(3:Nat)^(2*k+2) := Nat.pow_le_pow_right (by decide : 0<(3:Nat)) (show 4≤2*k+2 by omega)
  have first : b+17=2^(1782*t)*3^(2*k+2) := by
    dsimp [b]
    rw [lx,←shift_eq,show 2*k+6=(2*k+2)+4 by omega,pow_add]
    have sub := Nat.sub_add_cancel (show 17≤(3:Nat)^(2*k+2) by omega)
    calc
      _ = ((3^(2*k+2)-17)+17)+3^(2*k+2)*(81*shift t) := by ring
      _ = _ := by rw [sub]; ring
  obtain ⟨s,p⟩ := laps 11 7 (-17) (by decide) (by decide) (162*t)
  rw [show 11*(162*t)=1782*t by ring] at s p
  have physical := natLift (1782*t) (3^(2*k+2)) 17 b first
  change (run (1782*t) b:Int)=travel (1782*t) (-17)+3^(digits (1782*t) (-17))*(3:Nat)^(2*k+2) at physical
  rw [s,p] at physical
  norm_num only [Nat.cast_ofNat] at physical
  have pp : 3^(7*(162*t))*(3:Nat)^(2*k+2)=3^(2*(k+567*t)+2) := by
    rw [←pow_add]; congr 1; ring
  have big : 81≤(3:Nat)^(2*(k+567*t)+2) := Nat.pow_le_pow_right (by decide : 0<(3:Nat)) (show 4≤_ by omega)
  have end_eq : run (1782*t) b=3^(2*(k+567*t)+2)-17 := by
    apply Int.ofNat_inj.mp
    rw [Nat.cast_sub (show 17≤(3:Nat)^(2*(k+567*t)+2) by omega)]
    push_cast
    have pc := congrArg (fun a : Nat => (a:Int)) pp
    push_cast at pc
    rw [physical,pc]; ring
  calc
    _ ↔ Good b := (good_run _ _).symm
    _ ↔ Good (run (1782*t) b) := (good_run _ _).symm
    _ ↔ _ := by rw [end_eq]; exact faster_phase _ (by omega)

/-- The e=23 row has a completely kernel-checked base. The ordinary floor
holds at any alleged least canonical reverse disagreement by quantitative return. -/
def base23 : Nat := 2202542735657345495460317854088727061904801

def source23 (t : Nat) : Nat := base23+2^147*shift t

set_option maxHeartbeats 1200000 in
private theorem base23_path :
    run 147 base23=3^80-17 ∧ odds 147 base23=84 ∧ run 675 base23=1 := by decide

theorem source23_eq (t : Nat) : 81*source23 t+15+2^25=2^(147+1782*t) := by
  have base : 81*base23+15+2^25=2^147 := by decide
  calc
    _ = (81*base23+15+2^25)+2^147*(81*shift t) := by unfold source23; ring
    _ = 2^147*(81*shift t+1) := by rw [base]; ring
    _ = _ := by rw [shift_eq,pow_add]

theorem closed23 (t : Nat)
    (floor : ∀ n, 0<n → 2^40*n<source23 t → Good n) : Good (source23 t) := by
  cases t with
  | zero =>
    change Good base23
    exact ⟨675,base23_path.2.2⟩
  | succ t =>
    let d := t+1
    have link := repeated_phase (z:=base23) (H:=147) (k:=39) (by decide)
      base23_path.1 base23_path.2.1 d
    let w := 2^(3*(39+567*d)+1)-5
    have exponent : 40+(3*(39+567*d)+1)=158+1701*d := by omega
    have pospow : 32≤(2:Nat)^(3*(39+567*d)+1) :=
      Nat.pow_le_pow_right (by decide : 0<(2:Nat)) (show 5≤_ by omega)
    have price : 2^40*w<2^(1782*d)*base23 := calc
      _ ≤ 2^40*2^(3*(39+567*d)+1) := Nat.mul_le_mul_left _ (Nat.sub_le _ _)
      _ = 2^158*2^(1701*d) := by rw [←pow_add,exponent,pow_add]
      _ < (2^81*base23)*2^(1701*d) :=
        Nat.mul_lt_mul_of_pos_right (by decide) (Nat.two_pow_pos _)
      _ = 2^(81+1701*d)*base23 := by rw [pow_add]; ring
      _ ≤ _ := Nat.mul_le_mul_right _ (Nat.pow_le_pow_right (by decide : 0<(2:Nat))
                                         (show 81+1701*d≤1782*d by dsimp [d]; omega))
    have lower : 2^(1782*d)*base23≤source23 d := calc
      _ = base23+(81*base23)*shift d := by rw [←shift_eq]; ring
      _ ≤ _ := Nat.add_le_add_left (Nat.mul_le_mul_right _ (by decide : 81*base23≤2^147)) _
    exact link.mpr (floor w (by dsimp [w]; omega) (price.trans_le lower))

#print axioms faster_phase
#print axioms shift_eq
#print axioms repeated_phase
#print axioms source23_eq
#print axioms closed23
end Collatz.PhaseReturn
