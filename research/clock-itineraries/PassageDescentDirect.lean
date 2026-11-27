module

public import PassageDescentPowers
import all ReturnDescent
import all TowerFrontierAffine
import all TernaryItinerary

public section

namespace Collatz.Itinerary.PassageDescent

open TowerFrontier ReturnDescent
set_option autoImplicit false
set_option maxHeartbeats 2000000
set_option maxRecDepth 10000
set_option exponentiation.threshold 1000000

/- Binary modular exponentiation keeps even the delayed parameter checks
   small. The fuel bounds the exponent's bit length, never an orbit length. -/
private def powRem : Nat → Nat → Nat → Nat → Nat
  | 0, _, _, d => 1%d
  | f+1, a, e, d =>
    let z := powRem f (a*a%d) (e/2) d
    if e%2=0 then z else a*z%d

private theorem powRem_correct (f a e d : Nat) (bits : e<2^f) :
    powRem f a e d=a^e%d := by
  induction f generalizing a e with
  | zero =>
    have eq : e=0 := by simpa using bits
    simp [eq,powRem]
  | succ f ih =>
    have small : e/2<2^f := by rw [Nat.pow_succ] at bits; omega
    have square : (a*a%d)^(e/2)%d=a^(2*(e/2))%d := by
      rw [←Nat.pow_mod,Nat.pow_mul,Nat.pow_succ a 1,Nat.pow_one]
    rw [powRem,ih _ _ small,square]
    split
    · exact congrArg (fun k => a^k%d) (by omega)
    · rw [Nat.mul_mod_mod,Nat.mul_comm,←Nat.pow_succ]
      exact congrArg (fun k => a^k%d) (by omega)

private theorem periodic {a L d : Nat} (dpos : 1<d) (base : a^L%d=1) (e k : Nat) :
    a^(e+L*k)%d=a^e%d := by
  have tail : (a^L)^k%d=1 := by rw [Nat.pow_mod,base,Nat.one_pow,Nat.mod_eq_of_lt dpos]
  rw [Nat.pow_add,Nat.pow_mul,Nat.mul_mod,tail,Nat.mul_one,Nat.mod_mod]

structure DirectRow where
  residue : Nat
  period : Nat
  rank : Nat
  lower : Nat
  carry : Nat
  start : Nat
  base : Nat
deriving Inhabited

namespace DirectRow

def modulus (r : DirectRow) := 3^r.rank
def den (r : DirectRow) := 3*r.modulus
def unit (r : DirectRow) := powRem 64 2 (18*r.residue) r.modulus

/-- Small exact conditions at one ordinary test source and two modular periods. -/
def check (r : DirectRow) : Bool := decide
  (0<r.residue ∧ 0<r.period ∧ 1<r.modulus ∧ 4≤r.lower+2 ∧ r.base<2^64 ∧
   18*r.residue<2^64 ∧ 18*r.period<2^64 ∧ 6*r.modulus<2^64 ∧ 12*r.unit<2^64 ∧
   0<r.unit ∧ powRem 64 2 (18*r.period) r.modulus=1 ∧
   powRem 64 2 (6*r.modulus) (9*r.modulus)=1 ∧
   powRem 64 2 (12*r.unit-3) (9*r.modulus)=r.base%(9*r.modulus) ∧
   r.start%48=17 ∧ r.den*r.start+r.carry=2^(r.lower+2)*r.base ∧
   track r.lower r.start 0=(4*r.base-1,r.rank+1) ∧
   track (r.lower+2) (3*r.start) 0=(r.base,r.rank) ∧
   0<r.base ∧ 0<r.carry ∧ 81*2^r.lower≤128*r.den ∧ 351*r.den<81*r.carry)

private theorem parameter {r : DirectRow} (hc : r.check=true) (s : Nat) :
    let k := r.residue+r.period*s
    let m := delayedExponent k
    ∃ t, 2^(m-2)=r.base+9*r.modulus*t := by
  intro k m
  obtain ⟨kr,_,large,_,bsize,f0,fp,fo,fu,up,cycle,outer,price,_⟩ := of_decide_eq_true hc
  have innerBase : 2^(18*r.residue)%r.modulus=r.unit := (powRem_correct 64 _ _ _ f0).symm
  rw [powRem_correct 64 _ _ _ fp] at cycle
  rw [powRem_correct 64 _ _ _ fo] at outer
  rw [powRem_correct 64 _ _ _ (show 12*r.unit-3<2^64 by omega)] at price
  have split : 18*k=18*r.residue+18*r.period*s := by dsimp only [k]; grind
  have inner : 2^(18*k)%r.modulus=r.unit := by rw [split,periodic large cycle,innerBase]
  let q := 2^(18*k)/r.modulus
  have total : r.unit+r.modulus*q=2^(18*k) := by rw [←inner]; apply Nat.mod_add_div
  have trueExp : m-2=(12*r.unit-3)+(6*r.modulus)*(2*q) := by
    dsimp only [m,delayedExponent]
    rw [←total,Nat.mul_add]
    have coeff : 12*(r.modulus*q)=6*r.modulus*(2*q) := by
      change (6*2)*(r.modulus*q)=6*r.modulus*(2*q)
      ac_rfl
    omega
  have big : 1<9*r.modulus := by omega
  have modEq : 2^(m-2)%(9*r.modulus)=r.base%(9*r.modulus) := by rw [trueExp,periodic big outer,price]
  have kpos : 1≤k := by dsimp only [k]; omega
  have enough : 2^18≤2^(18*k) := Nat.pow_le_pow_right (by decide) (by omega)
  have msize : 64≤m-2 := by dsimp only [m,delayedExponent]; omega
  have floor : r.base≤2^(m-2) := Nat.le_trans (by omega : r.base≤2^64)
    (Nat.pow_le_pow_right (by decide) msize)
  have t1 := Nat.mod_add_div (2^(m-2)) (9*r.modulus)
  have t2 := Nat.mod_add_div r.base (9*r.modulus)
  rw [modEq] at t1
  let v := 2^(m-2)/(9*r.modulus)
  let w := r.base/(9*r.modulus)
  have vw : w≤v := Nat.div_le_div_right floor
  refine ⟨v-w,?_⟩
  rw [Nat.mul_sub]
  dsimp only [v,w]
  omega

private theorem halves (h e : Nat) : track h (2^h) e=(1,e) := by
  induction h generalizing e with
  | zero => rfl
  | succ h ih =>
    simp only [Nat.pow_succ,track,show 2^h*2%2=0 by omega,↓reduceIte,
      show 2^h*2/2=2^h by omega]
    exact ih e

private theorem append_track (i j n e : Nat) :
    track (i+j) n e=track j (track i n e).1 (track i n e).2 := by
  induction i generalizing n e with
  | zero => simp [track]
  | succ i ih => rw [Nat.succ_add,track,track]; split <;> apply ih

/-- The physical lower meets M_m before its ascent even begins. The upper
    meets exactly the same power of two as the ninth original upper step. -/
theorem before_peak (r : DirectRow) (hc : r.check=true) (s : Nat) :
    let k := r.residue+r.period*s
    let m := delayedExponent k
    ∃ Y, Y%48=17 ∧ Y<hardParent m ∧ r.den*Y+r.carry=2^(m+r.lower) ∧
      track r.lower Y 0=(M m,r.rank+1) ∧
      track (r.lower+2) (3*Y) 0=(2^(m-2),r.rank) ∧
      track (m+r.lower) (3*Y) 0=(1,r.rank) := by
  intro k m
  obtain ⟨kr,_,_,lc,_,_,_,_,_,_,_,_,_,cls,source,lo,hi,bpos,_,slope,constant⟩ :=
    of_decide_eq_true hc
  obtain ⟨t,pt⟩ := parameter hc s
  change 2^(m-2)=r.base+9*r.modulus*t at pt
  have kpos : 1≤k := by dsimp only [k]; omega
  have mm : 2≤m := by
    have pos : 0<2^(18*k) := Nat.two_pow_pos _
    dsimp only [m,delayedExponent]; omega
  have power : 2^m=4*2^(m-2) := by
    rw [show (4:Nat)=2^2 by decide,←Nat.pow_add]; congr 1; omega
  let Y := r.start+2^(r.lower+2)*(3*t)
  have yl : Y=r.start+2^r.lower*(12*t) := by
    dsimp only [Y]; rw [Nat.pow_add]; change _+2^r.lower*4*(3*t)=_; grind
  have yu : 3*Y=3*r.start+2^(r.lower+2)*(9*t) := by dsimp only [Y]; grind
  have L := track_lift r.lower r.start (12*t)
  have U := track_lift (r.lower+2) (3*r.start) (9*t)
  rw [←yl,lo] at L
  rw [←yu,hi] at U
  have lv : 4*r.base-1+3^(r.rank+1)*(12*t)=M m := by
    unfold M
    rw [power,pt,Nat.pow_succ]
    change 4*r.base-1+r.modulus*3*(12*t)=4*(r.base+9*r.modulus*t)-1
    have eq : r.modulus*3*(12*t)=4*(9*r.modulus*t) := by grind
    rw [eq,Nat.mul_add]
    omega
  have uv : r.base+3^r.rank*(9*t)=2^(m-2) := by rw [pt]; change _+r.modulus*(9*t)=_; grind
  change track r.lower Y 0=(4*r.base-1+3^(r.rank+1)*(12*t),r.rank+1) at L
  change track (r.lower+2) (3*Y) 0=(r.base+3^r.rank*(9*t),r.rank) at U
  rw [lv] at L
  rw [uv] at U
  have endU : track (m+r.lower) (3*Y) 0=(1,r.rank) := by
    rw [show m+r.lower=(r.lower+2)+(m-2) by omega,append_track,U,halves]
  have cY : Y%48=17 := by
    have fac : 2^(r.lower+2)*(3*t)=48*(2^(r.lower+2-4)*t) := by
      rw [show r.lower+2=4+(r.lower+2-4) by omega,Nat.pow_add]
      have rem : 4+(r.lower+2-4)-4=r.lower+2-4 := by omega
      rw [rem]
      change 16*2^(r.lower+2-4)*(3*t)=(16*3)*(2^(r.lower+2-4)*t)
      ac_rfl
    dsimp only [Y]
    rw [fac,Nat.add_mul_mod_self_left,cls]
  have affine : r.den*Y+r.carry=2^(m+r.lower) := by
    rw [Nat.pow_add,power,pt]
    dsimp only [Y]
    rw [Nat.pow_add] at source ⊢
    dsimp only [den] at source ⊢
    grind
  have sm : Y<hardParent m := by
    have h0 := Nat.mul_le_mul_right (2^m) slope
    have hh := congrArg (fun n => 81*n) affine
    rw [Nat.pow_add] at hh
    unfold hardParent
    rw [Nat.pow_add]
    by_cases ok : Y<(2^m*2^7-271)/81
    · exact ok
    have cmp : 2^m*128≤81*Y+351 := by omega
    have mul := Nat.mul_le_mul_left r.den cmp
    grind
  exact ⟨Y,cY,sm,affine,L,U,endU⟩

end DirectRow

end Collatz.Itinerary.PassageDescent
