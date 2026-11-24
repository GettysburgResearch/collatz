import Std
import CycleShadows

/-! Exact ordinary descent in all three remaining five-block cases of
PR192, on two ternary-unit cylinders of the original source. -/
set_option maxRecDepth 12000
set_option maxHeartbeats 850000
namespace WordCert
open CycleShadows

def scale : List Bool → Nat
 | [] => 1
 | b::tail => (if b then 3 else 1) * scale tail

def carry : List Bool → Nat
 | [] => 0
 | b::tail => (if b then scale tail else 0) + 2*carry tail

theorem odd_scale (bs : List Bool) : scale bs % 2 = 1 := by
  induction bs with
  | nil => decide
  | cons b bs ih => cases b <;> simp only [scale, Bool.false_eq_true, ite_false,
      ite_true,Nat.one_mul] <;> omega

theorem realize (bs : List Bool) (x w : Nat)
    (eqn : 2^bs.length*w=scale bs*x+carry bs) : run T bs.length x=w := by
  induction bs generalizing x with
  | nil => simpa [scale,carry,run] using eqn.symm
  | cons b bs ih =>
    have odd := odd_scale bs
    rw [List.length_cons,Nat.pow_succ,Nat.mul_right_comm] at eqn
    have oddprod : (scale bs*x)%2=x%2 := by rw [Nat.mul_mod,odd,Nat.one_mul,Nat.mod_mod]
    cases b with
    | false =>
      change 2^bs.length*w*2=1*scale bs*x+(0+2*carry bs) at eqn
      rw [Nat.one_mul,Nat.zero_add] at eqn
      have xe : x%2=0 := by omega
      have hT : T x=x/2 := by simp [T,xe]
      have hx : x=2*(x/2) := by omega
      have fac : scale bs*x =2*(scale bs*(x/2)) := calc
        scale bs*x = scale bs*(2*(x/2)) := congrArg (fun t=>scale bs*t) hx
        _ = _ := by ac_rfl
      rw [fac] at eqn
      change run T bs.length (T x)=w
      apply ih
      rw [hT]
      omega
    | true =>
      change 2^bs.length*w*2=3*scale bs*x+(scale bs+2*carry bs) at eqn
      rw [Nat.mul_assoc 3 (scale bs) x] at eqn
      have xe : x%2=1 := by omega
      have hT : 2*T x=3*x+1 := by unfold T; split <;> omega
      have fac : 3*(scale bs*x)+scale bs=2*(scale bs*T x) := by
        calc
          _ = scale bs*(3*x+1) := by rw [Nat.mul_add,Nat.mul_one]; ac_rfl
          _ = _ := by rw [←hT]; ac_rfl
      have reorg : 2^bs.length*w*2=(3*(scale bs*x)+scale bs)+2*carry bs := by omega
      rw [fac] at reorg
      change run T bs.length (T x)=w
      apply ih
      omega
end WordCert

namespace ResidualDescent
open CycleShadows

inductive Cell where | pplll | pllpp | pllpl
deriving DecidableEq, Repr

def modulus : Cell → Nat | .pllpp => 1048576 | _ => 262144
def tailClock : Cell → Nat | .pllpp => 20 | _ => 18
def carry : Cell → Nat | .pplll => 691706 | .pllpp => 239485 | .pllpl => 305021
def anchor : Cell → Nat | .pplll => 7 | _ => 10
def firstClock : Cell → Nat | .pplll => 10 | _ => 18
def partner (c : Cell) (h : Nat) := match c with
  | .pplll => 248832*h+4799
  | _ => 262144*h+5055

/-- The listed equalities are the five actual ordinary block equations
on the same list of boundaries. -/
def Five (c : Cell) (q a b d e w : Nat) : Prop :=
  32*a=9*q+5 ∧ match c with
  | .pplll => 32*b=9*a+5 ∧ 8*d=9*b+7 ∧ 8*e=9*d+7 ∧ 8*w=9*e+7
  | .pllpp => 8*b=9*a+7 ∧ 8*d=9*b+7 ∧ 32*e=9*d+5 ∧ 32*w=9*e+5
  | .pllpl => 8*b=9*a+7 ∧ 8*d=9*b+7 ∧ 32*e=9*d+5 ∧ 8*w=9*e+7

private theorem firstEntry (c : Cell) (h : Nat) :
    run T (firstClock c) (partner c h) + anchor c = 9*(177147*h+3418) := by
  cases c with
  | pplll =>
    have A := lift 10 (248832*h+4799) 321 (243*h+5) (by decide) (by omega)
    change run T 10 (248832*h+4799) + 2050 = 6561*(243*h+5) at A
    change run T 10 (248832*h+4799)+7=_
    omega
  | pllpp | pllpl =>
    have A := lift 18 (262144*h+5055) 257089 (h+1) (by decide) (by omega)
    change run T 18 (262144*h+5055) + 1563571 = 1594323*(h+1) at A
    change run T 18 (262144*h+5055)+10=_
    omega

inductive Gate where | entry | paid
deriving DecidableEq

def period : Gate → Nat | .entry => 177147 | .paid => 1594323
def base : Gate → Nat | .entry => 3418 | .paid => 9148
def startClock (g : Gate) (c : Cell) := match g with
  | .entry => firstClock c
  | .paid => match c with | .pplll => 21 | _ => 13

def start (g : Gate) (c : Cell) (h : Nat) := match g with
  | .entry => partner c h
  | .paid => match c with | .pplll => 2097152*h+12031 | _ => 1990656*h+11419

private theorem first (g : Gate) (c : Cell) (h : Nat) :
    run T (startClock g c) (start g c h)+anchor c = 9*(period g*h+base g) := by
  cases g with
  | entry => exact firstEntry c h
  | paid => cases c with
    | pplll =>
      have A := lift 21 (2097152*h+12031) 2085121 (h+1) (by decide) (by omega)
      change run T 21 (2097152*h+12031)+14266582=14348907*(h+1) at A
      change run T 21 (2097152*h+12031)+7=9*(1594323*h+9148)
      omega
    | pllpp | pllpl =>
      have A := lift 13 (1990656*h+11419) 4965 (243*h+2) (by decide) (by omega)
      change run T 13 (1990656*h+11419)+35776=59049*(243*h+2) at A
      change run T 13 (1990656*h+11419)+10=9*(1594323*h+9148)
      omega

private theorem cycle (c : Cell) (r : Nat) :
    run S (3*r) (anchor c) = anchor c ∧ weight (3*r) (anchor c)=2*r := by
  induction r with
  | zero => cases c <;> decide
  | succ r ih =>
    have a : run S 3 (anchor c)=anchor c := by cases c <;> decide
    have b : weight 3 (anchor c)=2 := by cases c <;> decide
    rw [Nat.mul_succ, run_add, weight_add, ih.1, ih.2,a,b,Nat.mul_succ]
    exact ⟨rfl,rfl⟩

def targetWord : Cell → List Bool
 | .pplll => [false,true,true,false,false,false,false,true,false,false,false,true,true,false,true,true,false,true]
 | .pllpp => [true,true,false,false,false,false,true,true,false,false,true,true,false,false,false,true,true,false,false,false]
 | .pllpl => [true,true,false,false,false,false,true,true,false,false,true,true,false,false,false,true,false,true]

private theorem last {c : Cell} {y w : Nat}
    (h : modulus c*w=6561*y+carry c) : run T (tailClock c) y = w := by
  have hc : WordCert.carry (targetWord c)=carry c := by cases c <;> decide
  have hs : WordCert.scale (targetWord c)=6561 := by cases c <;> decide
  have ht : (targetWord c).length=tailClock c := by cases c <;> decide
  have hm : 2^(tailClock c)=modulus c := by cases c <;> decide
  rw [←ht]
  apply WordCert.realize
  rw [ht,hm,hc,hs]
  exact h

private theorem next_edge {D M C N K x y q : Nat}
    (pre : D*x=M*q+C) (edge : N*y=9*x+K) :
    (D*N)*y=(9*M)*q+(9*C+D*K) := by
  calc
    D*N*y = D*(N*y) := by ac_rfl
    _ = 9*(D*x) + D*K := by rw [edge,Nat.mul_add]; ac_rfl
    _ = _ := by rw [pre,Nat.mul_add]; ac_rfl

private theorem compose {c : Cell} {q a b d e w y : Nat}
    (hf : Five c q a b d e w) (hy : 2*(y+anchor c)=9*(q+7)) :
    modulus c*w=6561*y+carry c := by
  cases c <;> obtain ⟨h1,h2,h3,h4,h5⟩ := hf <;>
    have finalEq := next_edge (next_edge (next_edge (next_edge h1 h2) h3) h4) h5 <;>
    clear h1 h2 h3 h4 h5
  · change 524288*w=59049*q+1704901 at finalEq
    change 2*(y+7)=9*(q+7) at hy
    change 262144*w=6561*y+691706
    omega
  · change 2097152*w=59049*q+761093 at finalEq
    change 2*(y+10)=9*(q+7) at hy
    change 1048576*w=6561*y+239485
    omega
  · change 524288*w=59049*q+892165 at finalEq
    change 2*(y+10)=9*(q+7) at hy
    change 262144*w=6561*y+305021
    omega

/-- The separation of the powers of 8 and 9 uses only the given ordinary
light edges. No factorization or lift is presumed for the fixed source. -/
private theorem cofactor (q : Nat → Nat) (r : Nat) (odd : q r%2=1)
    (light : ∀ i, i<r → 8*q (i+1)=9*q i+7) :
    ∃ v, q 0+7=2*(8^r*v) ∧ q r+7=2*(9^r*v) := by
  have eqn (j : Nat) (hj : j≤r) : 8^j*(q j+7)=9^j*(q 0+7) := by
    induction j with
    | zero => simp
    | succ j ih =>
      have h := light j (by omega)
      have hstep : 8*(q (j+1)+7)=9*(q j+7) := by omega
      calc
        8^(j+1)*(q (j+1)+7)=8^j*(8*(q (j+1)+7)) := by rw [Nat.pow_succ]; ac_rfl
        _=9*(8^j*(q j+7)) := by rw [hstep]; ac_rfl
        _=9^(j+1)*(q 0+7) := by rw [ih (by omega),Nat.pow_succ]; ac_rfl
  have h := eqn r (by omega)
  have he : q r+7=2*((q r+7)/2) := by omega
  have hd : 2*8^r ∣ 9^r*(q 0+7) := by
    refine ⟨(q r+7)/2,?_⟩
    rw [←h]
    calc
      8^r*(q r+7) = 8^r*(2*((q r+7)/2)) := congrArg (fun x => 8^r*x) he
      _ = _ := by ac_rfl
  have cop : Nat.Coprime (2*8^r) (9^r) :=
    ((show Nat.Coprime 2 9 by decide).mul_left
      ((show Nat.Coprime 8 9 by decide).pow_left r)).pow_right r
  obtain ⟨v,hv⟩ := cop.dvd_of_dvd_mul_left hd
  refine ⟨v, by rw [hv]; ac_rfl, ?_⟩
  apply Nat.eq_of_mul_eq_mul_left (n:=8^r) (Nat.pow_pos (by decide))
  rw [h,hv]; ac_rfl

/-- All three residual cases, at arbitrary initial light-run length. The
ternary condition is imposed on the original ordinary boundary. -/
theorem residual_descent (g : Gate) (c : Cell) (q : Nat → Nat) (r : Nat) (odd : q r%2=1)
    (light : ∀ i, i<r → 8*q (i+1)=9*q i+7)
    (hf : Five c (q r) (q (r+1)) (q (r+2)) (q (r+3)) (q (r+4)) (q (r+5)))
    (guard : ((q 0+7)/2)%period g=base g) :
    ∃ m, 0<m ∧ m%2=1 ∧ m<q 0 ∧ m<(3*q 0+1)/4 ∧
      run T (startClock g c+3*r+tailClock c) m=q (r+5) := by
  obtain ⟨v,hv,hq⟩ := cofactor q r odd light
  let h := ((q 0+7)/2)/period g
  have hh : 8^r*v=period g*h+base g := by cases g <;> simp only [period,base] at guard ⊢ <;> dsimp [h,period] <;> omega
  let t := run T (startClock g c) (start g c h)
  have hfirst : t+anchor c=9*(period g*h+base g) := first g c h
  have hmid : t+anchor c=2^(3*r)*(9*v) := by
    rw [hfirst,←hh,Nat.pow_mul]
    change 9*(8^r*v)=8^r*(9*v)
    ac_rfl
  have hpos : 0<anchor c := by cases c <;> decide
  have B := lift (3*r) t (anchor c) (9*v) hpos hmid
  obtain ⟨hs,hw⟩ := cycle c r
  rw [hs,hw,Nat.pow_mul] at B
  change run T (3*r) t+anchor c=9^r*(9*v) at B
  have hy : 2*(run T (3*r) t+anchor c)=9*(q r+7) := by rw [B,hq]; ac_rfl
  refine ⟨start g c h,?_,?_,?_,?_,?_⟩
  all_goals try (cases g <;> cases c <;> simp only [start,partner,period,base] at hh ⊢ <;> omega)
  rw [run_add,run_add]
  exact last (compose hf hy)

#print axioms residual_descent
end ResidualDescent
