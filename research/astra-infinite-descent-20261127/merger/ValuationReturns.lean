module

public import FixedMersenneRows
import all FixedMersenneRows
import all ReturnDescentRows
import all ReturnDescent
import all TowerFrontierAffine
import all TernaryItinerary

public section

/-! For every original hard exponent on either of two complete valuation
classes, the specified earlier peak gives a large paid physical return
exactly one shortcut beyond the valuation. -/
namespace Collatz.Itinerary.ReturnDescent.ValuationReturns
open TowerFrontier
set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 15000
set_option maxHeartbeats 3000000
set_option exponentiation.threshold 10000

/-- Actual common postpeak deadline, shorter canonical upper certificate,
strict factor in ordinary height and a meeting with the original lower. -/
def PaidPeak (m d h savings : Nat) : Prop :=
  run h (3^m-1)=run h (3^(m-d)-1) ∧ ∃C Y : Nat,
    C+savings≤m ∧ 2^savings*Y<hardParent m ∧ Y%48=17 ∧
    track C (3*Y) 0=(1,3) ∧ Meets (hardParent m) Y

theorem lift_peak {h d t b : Nat} (pos : 0<b) (res : b=3^t%2^h)
    (ck : track h (3^d*b-1) d=track h (b-1) 0) :
    run h (3^(t+d)-1)=run h (3^t-1) := by
  let u := 3^t/2^h
  have eq : b+2^h*u=3^t := by simpa only [res] using Nat.mod_add_div (3^t) (2^h)
  have start : 3^(t+d)-1=(3^d*b-1)+2^h*3^d*u := by
    have p : 0<3^d*b := Nat.mul_pos (Nat.pow_pos (by decide)) pos
    rw [Nat.add_comm t d,Nat.pow_add,←eq,Nat.mul_add,
      show 3^d*(2^h*u)=2^h*3^d*u by ac_rfl]
    omega
  have earlier : 3^t-1=(b-1)+2^h*3^0*u := by rw [←eq]; simp only [Nat.pow_zero,Nat.mul_one]; omega
  rw [start,earlier,affine,affine,ck]

theorem periodic_charge (t P n : Nat) (pos : 0<t) (per : P%162=0) :
    clockCharge (t+P*n)=clockCharge t := by
  have mult : P=162*(P/162) := by omega
  have term : P*n=162*((P/162)*n) := by calc
    _=(162*(P/162))*n := congrArg (fun x => x*n) mult
    _=_ := Nat.mul_assoc ..
  unfold clockCharge
  rw [show ((t+P*n-1)/2)%81=((t-1)/2)%81 by rw [term]; omega]

private def Certified (m P d h savings f : Nat) : Prop :=
  let t:=m-d
  let b:=Supplied.powerMod f 3 t (2^h)
  m%162=11 ∧ P%162=0 ∧ d<m ∧ 18+savings≤m ∧ clockCharge t+savings≤d ∧
  t<2^f ∧ P<2^f ∧ 0<b ∧ Supplied.powerMod f 3 P (2^h)=1 ∧
  stride h (3^d*b-1) d=stride h (b-1) 0

private instance (m P d h savings f : Nat) : Decidable (Certified m P d h savings f) := by
  unfold Certified; infer_instance

private theorem all_lifts {m P d h savings f : Nat} (cert : Certified m P d h savings f) (n : Nat) :
    PaidPeak (m+P*n) d h savings := by
  let t:=m-d
  let b:=Supplied.powerMod f 3 t (2^h)
  obtain ⟨row,per,gap,small,price,tbits,pbits,pos,ord,certWords⟩:=cert
  have tp : 0<t := by dsimp [t]; omega
  have tbase : t+d=m := by dsimp [t]; omega
  have earlier : (m+P*n)-d=t+P*n := by dsimp [t]; omega
  have combined : (t+P*n)+d=m+P*n := by omega
  have oldres : b=3^t%2^h := Supplied.powerMod_spec _ _ _ _ tbits
  have period : 3^P%2^h=1 := (Supplied.powerMod_spec _ _ _ _ pbits).symm.trans ord
  have res : b=3^(t+P*n)%2^h := by
    rw [Nat.pow_add,Nat.pow_mul,Nat.mul_mod,Nat.pow_mod (3^P) n,period,Nat.one_pow,
      Nat.mul_mod_mod,Nat.mul_one,Nat.mod_mod]
    exact oldres
  rw [stride_eq,stride_eq] at certWords
  have hits := lift_peak pos res certWords
  rw [combined] at hits
  have rc : (m+P*n)%162=11 := by rw [Nat.add_mod,Nat.mul_mod,per,row]; simp
  let j:=(m+P*n)/162
  have address : m+P*n=11+162*j := by dsimp [j]; omega
  obtain ⟨bound,_,source,_⟩:=hard_source j
  rw [←address] at bound source
  obtain ⟨C,Y,cl,hy⟩:=priced_representative (t+P*n) (by omega)
  rw [periodic_charge t P n tp per] at cl
  change clockCharge t+savings≤d at price
  have cs : C+savings≤m+P*n := by
    rcases Nat.le_total 18 (t+P*n+clockCharge t) with le|le
    · rw [Nat.max_eq_right le] at cl; omega
    · rw [Nat.max_eq_left le] at cl; omega
  have ht : 2^savings*Y<hardParent (m+P*n) := by
    calc
      _<2^savings*2^C := Nat.mul_lt_mul_of_pos_left hy.2.1 (Nat.two_pow_pos _)
      _=2^(C+savings) := by rw [Nat.add_comm C,Nat.pow_add]
      _≤2^(m+P*n) := Nat.pow_le_pow_right (by decide) cs
      _<_ := bound
  have meet : Meets (M (m+P*n)) (M (t+P*n)) :=
    ⟨(m+P*n)+h,(t+P*n)+h,by rw [run_add (m+P*n),run_add (t+P*n),peak,peak,hits]⟩
  refine ⟨by simpa only [earlier] using hits,C,Y,cs,ht,hy.1,hy.2.2.1,?_⟩
  exact (Meets.trans (show Meets (hardParent (m+P*n)) (M (m+P*n)) from ⟨7,0,source⟩) meet).trans hy.2.2.2.symm

private theorem family_form (B a n : Nat) (big : 0<B*a) :
    B*(a+54*n)-1=(B*a-1)+(B*54)*n := by
  rw [Nat.mul_add,←Nat.mul_assoc B 54 n]; omega

/-- Every odd cofactor in the full canonical valuation-856 class. -/
theorem valuation_856 (n : Nat) : PaidPeak (12*2^852*(19+54*n)-1) 420 857 401 := by
  have cert : Certified (12*2^852*19-1) (12*2^852*54) 420 857 401 863 := by decide +kernel
  rw [family_form _ _ _ (by decide)]
  exact all_lifts cert n

/-- Every odd cofactor in the full canonical valuation-1736 class. -/
theorem valuation_1736 (n : Nat) : PaidPeak (12*2^1732*(49+54*n)-1) 886 1737 876 := by
  have cert : Certified (12*2^1732*49-1) (12*2^1732*54) 886 1737 876 1743 := by decide +kernel
  rw [family_form _ _ _ (by decide)]
  exact all_lifts cert n

#print axioms valuation_856
#print axioms valuation_1736
end Collatz.Itinerary.ReturnDescent.ValuationReturns
