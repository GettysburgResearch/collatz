import ValuationRows
import ValuationSharp
import Mathlib.Data.Nat.ModEq
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-! A finite set of signed matches gives thirteen complete classes of
supplied hard exponents, including height savings up to 17,026 bits. -/
namespace Collatz.ValuationDictionary
open Itinerary Itinerary.ReturnDescent Itinerary.TowerFrontier Itinerary.ReturnDescent.ValuationReturns
set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 60000
set_option maxHeartbeats 12000000
set_option exponentiation.threshold 60000

private theorem base_odd (q : ℕ) : ∃c : ℕ,
    3^(12*2^q)=1+2^(q+4)*(2*c+1) := by
  induction q with
  | zero => exact ⟨16607,by decide⟩
  | succ q ih =>
    obtain ⟨c,old⟩:=ih
    refine ⟨c+2^(q+2)*(2*c+1)^2,?_⟩
    rw [show 12*2^(q+1)=(12*2^q)*2 by ring,Nat.pow_mul,old]; ring

private theorem odd_power (q r : ℕ) : ∃v : ℕ,
    3^(12*2^q*(2*r+1))=1+2^(q+4)*(2*v+1) := by
  obtain ⟨c,base⟩:=base_odd q
  induction r with
  | zero => exact ⟨c,by simpa using base⟩
  | succ r ih =>
    obtain ⟨v,old⟩:=ih
    let A:=2^(q+4)
    let E:=(2*c+1)+2^(q+3)*(2*c+1)^2
    have sq : (3^(12*2^q))^2=1+2*A*E := by rw [base]; dsimp [A,E]; ring
    refine ⟨v+E*(1+A*(2*v+1)),?_⟩
    rw [show 12*2^q*(2*(r+1)+1)=12*2^q*(2*r+1)+(12*2^q)*2 by ring,Nat.pow_add,show 3^((12*2^q)*2)=(3^(12*2^q))^2 from Nat.pow_mul ..,sq,old]
    dsimp only [A]; ring

private theorem realize (e : Entry) (ck : Checked e) (n : ℕ) :
    PaidPeak (12*2^e.q*(e.a+54*n)-1) e.gap (e.q+5) e.savings := by
  let B:=12*2^e.q
  let N:=B*e.a-1
  let P:=B*54
  let m:=B*(e.a+54*n)-1
  let t:=m-e.gap
  let b:=entryBase e
  let h:=e.q+5
  obtain ⟨ao,bp,rc,per,gap,small,price,bpos,blt,bin,words⟩:=ck
  change 0<B*e.a at bp
  change N%162=11 at rc
  change P%162=0 at per
  change e.gap<N at gap
  change 18+e.savings≤N at small
  change clockCharge (N-e.gap)+e.savings≤e.gap at price
  change b<2^h at blt
  have grow : m=N+P*n := by
    dsimp [m,N,P]
    rw [Nat.mul_add,←Nat.mul_assoc]; omega
  have mt : t+e.gap=m := by dsimp [t]; omega
  have tform : t=(N-e.gap)+P*n := by dsimp [t]; omega
  have rOdd : e.a+54*n=2*((e.a+54*n)/2)+1 := by omega
  obtain ⟨v,addr⟩:=odd_power e.q ((e.a+54*n)/2)
  have scale : 0<B*(e.a+54*n) := by
    have ba : 0<e.a := by omega
    dsimp [B]; positivity
  have mp : m+1=B*(e.a+54*n) := Nat.sub_add_cancel scale
  rw [←rOdd,←mp] at addr
  have modAddr : 3^(m+1)%2^h=1+2^(e.q+4) := by
    rw [addr,show 1+2^(e.q+4)*(2*v+1)=2^h*v+(1+2^(e.q+4)) by dsimp [h]; ring,
      Nat.mul_add_mod_self_left,Nat.mod_eq_of_lt]
    have : 2≤2^(e.q+4) := by simpa only [Nat.pow_one] using Nat.pow_le_pow_right (by decide : 0<2) (show 1≤e.q+4 by omega)
    calc
      1+2^(e.q+4)<2^(e.q+4)*2 := by omega
      _=2^h := by dsimp [h]; rw [show e.q+5=(e.q+4)+1 by omega,Nat.pow_succ 2 (e.q+4)]
  have factor : 3^(e.gap+1)*3^t=3^(m+1) := by rw [←Nat.pow_add]; congr 1; omega
  have cop : Nat.Coprime (2^h) (3^(e.gap+1)) := ((by decide : Nat.Coprime 2 3).pow_left _).pow_right _
  have res : b=3^t%2^h := by
    have tied : 3^(e.gap+1)*b ≡ 3^(e.gap+1)*3^t [MOD 2^h] := by
      change _%_= _%_; rw [factor,modAddr]; exact bin
    have same := Nat.ModEq.cancel_left_of_coprime cop tied
    calc
      b=b%2^h := (Nat.mod_eq_of_lt blt).symm
      _=_ := same
  rw [stride_eq,stride_eq] at words
  have hits:=Itinerary.ReturnDescent.ValuationReturns.lift_peak bpos res words
  rw [mt] at hits
  have mr : m%162=11 := by rw [grow,Nat.add_mod,Nat.mul_mod,per,rc]; simp
  have sourceRow : m=11+162*(m/162) := by omega
  obtain ⟨bound,_,source,_⟩:=hard_source (m/162)
  rw [←sourceRow] at bound source
  have sameCost : clockCharge t=clockCharge (N-e.gap) := by
    rw [tform,Itinerary.ReturnDescent.ValuationReturns.periodic_charge _ _ _ (by omega) per]
  obtain ⟨C,Y,cl,hy⟩:=priced_representative t (by omega)
  rw [sameCost] at cl
  have cs : C+e.savings≤m := by
    rcases Nat.le_total 18 (t+clockCharge (N-e.gap)) with le|le
    · rw [Nat.max_eq_right le] at cl; omega
    · rw [Nat.max_eq_left le] at cl; omega
  have ht : 2^e.savings*Y<hardParent m := by
    calc
      _<2^e.savings*2^C := Nat.mul_lt_mul_of_pos_left hy.2.1 (Nat.two_pow_pos _)
      _=2^(C+e.savings) := by rw [Nat.add_comm C,Nat.pow_add]
      _≤2^m := Nat.pow_le_pow_right (by decide) cs
      _<_ := bound
  have meet : Meets (M m) (M t) := ⟨m+h,t+h,by rw [run_add m,run_add t h,peak,peak,hits]⟩
  exact ⟨hits,C,Y,cs,ht,hy.1,hy.2.2.1,(Meets.trans (show Meets (hardParent m) (M m) from ⟨7,0,source⟩) meet).trans hy.2.2.2.symm⟩

theorem paid_classes (e : Entry) (mem : e∈entries) (n : ℕ) :
    PaidPeak (12*2^e.q*(e.a+54*n)-1) e.gap (e.q+5) e.savings :=
  realize e (checked_all e mem) n

/-- The common postpeak deadline is optimal against every earlier exponent
and every pair of independent clocks on each whole listed class. -/
theorem sharp_classes (e : Entry) (mem : e∈entries) (n : ℕ) :
    ValuationSharp.SharpPaidPeak (12*2^e.q*(e.a+54*n)-1) e.gap (e.q+4) e.savings := by
  have odd := (checked_all e mem).1
  exact ⟨paid_classes e mem n,ValuationSharp.initial_delay e.q _ (by omega)⟩

#print axioms paid_classes
#print axioms sharp_classes
end Collatz.ValuationDictionary
