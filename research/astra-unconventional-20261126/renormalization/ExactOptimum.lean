import AscentMerger

/-! Exact all-cofactor optimization, with an ordinary smaller visitor witnessing
the upper bound at arbitrarily large positive source cofactors. -/
namespace Collatz.ExactOptimum
open Collatz.SourceDeletion Collatz.SignedBudget Collatz.ShadowBarrier Collatz.AscentMerger

private theorem signed_append (a b : Nat) (s : Int) :
    travel (a+b) s=travel b (travel a s) ∧
    digits (a+b) s=digits a s+digits b (travel a s) := by
  induction a generalizing s with
  | zero => simp [travel,digits]
  | succ a ih =>
    obtain ⟨ha,hb⟩ := ih (signedStep s)
    rw [Nat.succ_add]
    simp only [travel,digits,ha,hb]
    exact ⟨trivial,by omega⟩

private theorem unit_ancestor (u : Nat) (hu : 2≤u) (unit : u%3≠0) :
    ∃ v e : Nat, 2≤v ∧ v%3≠0 ∧ e≤4 ∧ travel e (-(v:Int))= -(u:Int) ∧
      digits e (-(v:Int))=1 := by
  let t := u/9
  have row (r e v : Nat) (eqn : u=r+9*t) (base : travel e (-(v:Int))= -(r:Int))
      (count : digits e (-(v:Int))=1) :
      travel e (-(v+2^e*(3*t):Nat))= -(u:Int) ∧
      digits e (-(v+2^e*(3*t):Nat))=1 := by
    obtain ⟨a,b⟩ := signed_lift e (-(v:Int)) (-(3*(t:Int)))
    push_cast
    rw [show -((v:Int)+2^e*(3*t)) = -v+2^e*(-(3*t)) by ring,a,b,base,count,eqn]
    push_cast
    constructor
    · ring
    · trivial
  have cases : u=1+9*t ∨ u=2+9*t ∨ u=4+9*t ∨ u=5+9*t ∨
      u=7+9*t ∨ u=8+9*t := by dsimp [t]; omega
  rcases cases with e|e|e|e|e|e
  · refine ⟨1+2^1*(3*t),1,by omega,by omega,by decide,row 1 1 1 e (by decide) (by decide)⟩
  · refine ⟨11+2^4*(3*t),4,by omega,by omega,by decide,row 2 4 11 e (by decide) (by decide)⟩
  · refine ⟨11+2^3*(3*t),3,by omega,by omega,by decide,row 4 3 11 e (by decide) (by decide)⟩
  · refine ⟨7+2^2*(3*t),2,by omega,by omega,by decide,row 5 2 7 e (by decide) (by decide)⟩
  · refine ⟨5+2^1*(3*t),1,by omega,by omega,by decide,row 7 1 5 e (by decide) (by decide)⟩
  · refine ⟨11+2^2*(3*t),2,by omega,by omega,by decide,row 8 2 11 e (by decide) (by decide)⟩

/-- Every requested number of odds occurs on a signed word, with linear
constructive clock bound. The signed starting magnitude remains a ternary unit. -/
theorem feasible_clock (r : Nat) : ∃ S u : Nat, S≤4*r ∧ 2≤u ∧ u%3≠0 ∧
    travel S (-(u:Int))= -2 ∧ digits S (-(u:Int))=r := by
  induction r with
  | zero => exact ⟨0,2,by decide,by decide,by decide,rfl,rfl⟩
  | succ r ih =>
    obtain ⟨S,u,cost,big,unit,tr,gr⟩ := ih
    obtain ⟨v,e,vbig,vunit,ec,vt,vg⟩ := unit_ancestor u big unit
    obtain ⟨a,b⟩ := signed_append e S (-(v:Int))
    rw [vt,tr] at a
    rw [vg,vt,gr] at b
    exact ⟨e+S,v,by omega,vbig,vunit,a,by omega⟩

private theorem clock_exists (r : Nat) : ∃ S, SignedClock r S := by
  obtain ⟨S,u,_,_,_,a,b⟩ := feasible_clock r
  exact ⟨S,-(u:Int),a,b⟩

noncomputable def L (r : Nat) : Nat := by
  classical
  exact Nat.find (clock_exists r)

private theorem min_clock (r : Nat) : SignedClock r (L r) := by
  classical
  exact Nat.find_spec (clock_exists r)

private theorem smaller_clock (r S : Nat) (ok : SignedClock r S) : L r≤S := by
  classical
  exact Nat.find_min' (clock_exists r) ok

def Paid (k S r : Nat) : Prop := 2^(k+(S-r+1)) < (3:Nat)^k

private theorem paid_exists (r : Nat) : ∃ k, Paid k (L r) r := by
  let d := L r-r+1
  refine ⟨2*d,?_⟩
  change (2:Nat)^(2*d+d)<3^(2*d)
  rw [show 2*d+d=3*d by omega,pow_mul,pow_mul]
  exact Nat.pow_lt_pow_left (by decide) (by dsimp [d]; omega)

noncomputable def K (r : Nat) : Nat := by
  classical
  exact Nat.find (paid_exists r)

private theorem pays (r : Nat) : Paid (K r) (L r) r := by
  classical
  exact Nat.find_spec (paid_exists r)

private theorem least_paid (r k : Nat) (ok : Paid k (L r) r) : K r≤k := by
  classical
  exact Nat.find_min' (paid_exists r) ok

/-- The sharp numerical lower bound applies to every actual smaller visitor
of the required other predecessor, without an exemption for long words. -/
theorem exact_lower {H w r a : Nat} (pos : 0<a) (small : w<2^r*a-1)
    (ending : run H w+2=2*a*3^r) : r+K r≤odds H w := by
  obtain ⟨above,S,word,paid⟩ := lower_witness pos small ending
  have le := smaller_clock r S word
  have le' : 2^(odds H w-r+(L r-r+1))≤(2:Nat)^(odds H w-r+(S-r+1)) :=
    Nat.pow_le_pow_right (by decide) (by omega)
  have min := least_paid r (odds H w-r) (le'.trans_lt paid)
  omega

private theorem signed_negative (h : Nat) (s : Int) (dst : travel h s≤ -2) : s≤ -2 := by
  induction h generalizing s with
  | zero => exact dst
  | succ h ih =>
    have le : signedStep s≤ -2 := ih _ dst
    unfold signedStep at le
    split at le <;> omega

private theorem signed_bits (h : Nat) (s : Int) : digits h s≤h := by
  induction h generalizing s with
  | zero => rfl
  | succ h ih => simp only [digits,bit]; split <;> have := ih (signedStep s) <;> omega

private theorem two_unit (e : Nat) : (2:Int)^e%3≠0 := by
  induction e with
  | zero => decide
  | succ e ih => rw [pow_succ]; omega

private theorem digit (b d : Int) (unit : b%3≠0) :
    ∃ t : Nat, t≤2 ∧ (d+b*t)%3=0 := by
  by_cases z : d%3=0
  · exact ⟨0,by decide,by simpa using z⟩
  by_cases one : (d+b)%3=0
  · exact ⟨1,by decide,by simpa using one⟩
  refine ⟨2,by decide,?_⟩
  have a : b%3=1 ∨ b%3=2 := by omega
  have c : d%3=1 ∨ d%3=2 := by omega
  rw [Int.add_emod] at one
  change (d+b*2)%3=0
  rw [Int.add_emod,Int.mul_emod b 2]
  rcases a with a|a <;> rcases c with c|c <;> simp_all

/-- Select an ordinary arbitrarily large cofactor, keeping the positive
quotient required for the final consecutive odd block. -/
theorem cofactor (S k bound : Nat) (s : Int) :
    ∃ a d : Nat, bound<a ∧ 0<d ∧ (3:Int)^k*d=2^(S+1)*a+s+1 := by
  induction k with
  | zero =>
    let a := bound+(-s).toNat+2
    have p : (0:Int)<(2:Int)^(S+1)*a+s+1 := by
      have factor : 1≤(2:Int)^(S+1) := by
        have hp : 0<(2:Int)^(S+1) := by positivity
        omega
      have base : -s<(a:Int) := by dsimp [a]; omega
      have mult := Int.mul_le_mul_of_nonneg_right factor (show 0≤(a:Int) by positivity)
      rw [one_mul] at mult
      omega
    exact ⟨a,((2:Int)^(S+1)*a+s+1).toNat,by dsimp [a]; omega,
      by omega,by rw [Int.toNat_of_nonneg (by omega)]; simp⟩
  | succ k ih =>
    obtain ⟨a,d,big,pos,fit⟩ := ih
    obtain ⟨t,_,div⟩ := digit (2^(S+1)) d (two_unit _)
    let d' : Int := (d+2^(S+1)*(t:Int))/3
    have divEq : 3*d'=d+2^(S+1)*(t:Int) := by dsimp [d']; omega
    have p : 0<d' := by
      have nn : (0:Int)≤2^(S+1)*(t:Int) := by positivity
      omega
    refine ⟨a+3^k*t,d'.toNat,by omega,by omega,?_⟩
    rw [Int.toNat_of_nonneg (by omega)]
    push_cast
    calc
      _ = 3^k*(3*d') := by ring
      _ = 3^k*(d+2^(S+1)*(t:Int)) := by rw [divEq]
      _ = _ := by rw [mul_add,fit]; ring

/-- For every r and every lower bound on the cofactor choose a genuine
positive smaller visitor attaining exactly the stated cost at the other edge. -/
theorem exact_attainment (r bound : Nat) :
    ∃ a w H : Nat, bound<a ∧ 0<w ∧ w<2^r*a-1 ∧
      run H w=2*(3^r*a-1) ∧ odds H w=r+K r ∧
      run (H+1) w=3^r*a-1 ∧ odds (H+1) w=r+K r := by
  obtain ⟨s,sh,sq⟩ := min_clock r
  have signed : s≤ -2 := signed_negative (L r) s (by rw [sh])
  have le : r≤L r := by have := signed_bits (L r) s; omega
  obtain ⟨a,d,big,pd,fit⟩ := cofactor (L r) (K r) bound s
  have pa : 0<a := by omega
  have kt : 0<K r := by
    have p := pays r
    by_contra! fail
    have : K r=0 := by omega
    simp only [Paid,this,pow_zero,Nat.zero_add] at p
    have nz : 0<(2:Nat)^(L r-r+1) := Nat.two_pow_pos _
    omega
  have kd : 1<2^(K r)*d := by
    have two : 1<(2:Nat)^(K r) := Nat.one_lt_pow (by omega) (by decide)
    have mult := Nat.mul_le_mul_left (2^(K r)) (show 1≤d by omega)
    omega
  let w := 2^(K r)*d-1
  let H := K r+L r
  have wpos : 0<w := by dsimp [w]; omega
  have scaled : 2^(K r+L r+1)<(3:Nat)^(K r)*2^r := by
    have p := pays r
    have cmp := Nat.mul_lt_mul_of_pos_right p (Nat.two_pow_pos r)
    rw [←pow_add] at cmp
    convert cmp using 1
    congr 1
    omega
  have compare : 2^(K r)*d < (2:Nat)^r*a := by
    have sf : (3:Int)^(K r)*d < 2^(L r+1)*a := by omega
    have ein : (3:Nat)^(K r)*d < 2^(L r+1)*a := by exact_mod_cast sf
    have left := Nat.mul_lt_mul_of_pos_left ein (Nat.two_pow_pos (K r))
    have right := Nat.mul_lt_mul_of_pos_right scaled pa
    have cmp : 3^(K r)*(2^(K r)*d) < (3:Nat)^(K r)*(2^r*a) := calc
      _ = 2^(K r)*(3^(K r)*d) := by ring
      _ < 2^(K r)*(2^(L r+1)*a) := left
      _ = 2^(K r+L r+1)*a := by rw [←Nat.mul_assoc,←pow_add]; congr 1
      _ < _ := by simpa only [Nat.mul_assoc] using right
    exact Nat.lt_of_mul_lt_mul_left cmp
  have small : w<2^r*a-1 := by dsimp [w]; omega
  obtain ⟨final,tot⟩ := sharp_word pa pd sh sq fit
  obtain ⟨rampEnd,rampCount⟩ := ramp (K r) d pd
  let b := 3^(K r)*d-1
  have bpos : 1≤(3:Nat)^(K r)*d := Nat.mul_pos (Nat.pow_pos (by decide)) pd
  have bc : (b:Int)=s+2^(L r)*(2*(a:Int)) := by
    dsimp [b]; rw [Nat.cast_sub bpos]; push_cast
    rw [pow_succ] at fit
    linarith only [fit]
  obtain ⟨tr,od⟩ := signed_lift (L r) s (2*(a:Int))
  rw [←bc,sh,sq] at tr
  rw [←bc,sq] at od
  obtain ⟨phys,grade⟩ := physical (L r) b
  rw [phys] at tr
  rw [grade] at od
  obtain ⟨aRun,aOdd⟩ := physical (K r) w
  rw [rampEnd] at aRun
  rw [rampCount] at aOdd
  obtain ⟨stepRun,stepOdd⟩ := signed_append (K r) (L r) (w:Int)
  rw [aRun,(physical (L r) b).1] at stepRun
  rw [aOdd,aRun,(physical (L r) b).2] at stepOdd
  obtain ⟨whole,wholeOdds⟩ := physical H w
  have ent : run H w=2*(3^r*a-1) := by
    have one : 1≤(3:Nat)^r*a := Nat.mul_pos (Nat.pow_pos (by decide)) pa
    apply Int.ofNat_inj.mp
    push_cast [Nat.cast_sub one]
    rw [←whole,stepRun,tr]
    ring
  have cost : odds H w=r+K r := by
    rw [←wholeOdds,stepOdd,od]; omega
  exact ⟨a,w,H,big,wpos,small,ent,cost,final,by simpa only [Nat.add_comm] using tot⟩

#print axioms feasible_clock
#print axioms exact_lower
#print axioms cofactor
#print axioms exact_attainment
end Collatz.ExactOptimum
