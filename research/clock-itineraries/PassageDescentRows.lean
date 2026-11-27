module

public import PassageDescent
import all ReturnDescent
import all TernaryItinerary
import all BasinTransport
import all TowerFrontierAffine

public section

namespace Collatz.Itinerary.PassageDescent

open TowerFrontier ReturnDescent
set_option autoImplicit false
set_option maxRecDepth 20000
set_option maxHeartbeats 2000000
set_option exponentiation.threshold 1000000

private theorem factor_power {v D w : Nat} (base : v=1+D*w) (s : Nat) :
    ∃ k, v^s=1+D*k := by
  induction s with
  | zero => exact ⟨0,by simp⟩
  | succ s ih =>
    obtain ⟨k,hk⟩ := ih
    exact ⟨k+w+D*k*w,by rw [Nat.pow_succ,hk,base]; grind⟩

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

private theorem ramp (h u : Nat) (pos : 0<u) :
    run h (2^h*u-1)=3^h*u-1 := by
  simpa only [Nat.zero_add,Nat.pow_zero,Nat.one_mul,run] using BasinTransport.affine_rays h 0 0 u pos

/-- A template keeps the physical starts, both low words and its exact full upper price. -/
structure Template where
  residue : Nat
  period : Nat
  gap : Nat
  rank : Nat
  extra : Nat
  carry : Nat
  lower : Nat
  upper : Nat
  remaining : Nat
deriving Inhabited

namespace Template

def baseIndex (r : Template) := if r.residue=0 then r.period else r.residue
def baseM (r : Template) := 11+162*r.baseIndex
def clock (r : Template) := r.baseM+r.extra
def den (r : Template) := 3^(r.rank+1)
def baseY (r : Template) := (2^r.clock-r.carry)/r.den

/-- Every arithmetic and dynamical claim about a template is decided on its
    actual positive base. -/
def Checked (r : Template) : Prop :=
  0<r.period ∧ r.residue<r.period ∧ r.gap≤r.baseM ∧ 4≤r.clock ∧
  r.lower≤r.clock ∧ r.upper≤r.clock ∧
  r.clock-r.lower+r.remaining=r.baseM-r.gap ∧
  r.baseY%48=17 ∧ r.den*r.baseY+r.carry=2^r.clock ∧
  2^(162*r.period)=1+(3*r.den)*((2^(162*r.period)-1)/(3*r.den)) ∧
  track r.lower r.baseY 0=(2^(r.clock-r.lower)*3^r.remaining-1,r.remaining+(r.rank+1)) ∧
  track r.upper (3*r.baseY) 0=(2^(r.clock-r.upper),r.rank)

instance (r : Template) : Decidable (Checked r) := inferInstanceAs (Decidable (
0<r.period ∧ r.residue<r.period ∧ r.gap≤r.baseM ∧ 4≤r.clock ∧
  r.lower≤r.clock ∧ r.upper≤r.clock ∧
  r.clock-r.lower+r.remaining=r.baseM-r.gap ∧
  r.baseY%48=17 ∧ r.den*r.baseY+r.carry=2^r.clock ∧
  2^(162*r.period)=1+(3*r.den)*((2^(162*r.period)-1)/(3*r.den)) ∧
  track r.lower r.baseY 0=(2^(r.clock-r.lower)*3^r.remaining-1,r.remaining+(r.rank+1)) ∧
  track r.upper (3*r.baseY) 0=(2^(r.clock-r.upper),r.rank)))

theorem physical (r : Template) (check : r.Checked) (s : Nat) :
    let j := r.baseIndex+r.period*s
    let m := 11+162*j
    let H := m+r.extra
    ∃ Y, Y%48=17 ∧ r.den*Y+r.carry=2^H ∧
      track H (3*Y) 0=(1,r.rank) ∧ Meets Y (M (m-r.gap)) := by
  intro j m H
  obtain ⟨_,_,gap,size,lh,uh,exp,cls,source,per,lo,up⟩ := check
  obtain ⟨k,scale⟩ := factor_power per s
  rw [←Nat.pow_mul] at scale
  let l := 162*r.period*s
  change 2^l=1+3*r.den*k at scale
  have em : m=r.baseM+l := by dsimp only [m,j,baseM,l]; grind
  have eh : H=r.clock+l := by dsimp only [H,clock]; omega
  let a := r.clock-r.lower
  let v := r.clock-r.upper
  let b := r.remaining
  let y := r.baseY+2^r.clock*(3*k)
  have spl (i t : Nat) (hi : i+t=r.clock) : 2^r.clock=2^i*2^t := by rw [←hi,Nat.pow_add]
  have la : r.lower+a=r.clock := by dsimp only [a]; omega
  have ua : r.upper+v=r.clock := by dsimp only [v]; omega
  have yl : y=r.baseY+2^r.lower*(2^a*(3*k)) := by dsimp only [y]; rw [spl _ _ la,Nat.mul_assoc]
  have yu : 3*y=3*r.baseY+2^r.upper*(2^v*(9*k)) := by
    dsimp only [y]
    rw [Nat.mul_add,spl _ _ ua]
    congr 1
    change 3*(2^r.upper*2^v*(3*k))=2^r.upper*(2^v*((3*3)*k))
    ac_rfl
  have L := track_lift r.lower r.baseY (2^a*(3*k))
  have U := track_lift r.upper (3*r.baseY) (2^v*(9*k))
  rw [←yl,lo] at L
  rw [←yu,up] at U
  have bpos : 0<3^b := Nat.pow_pos (by decide)
  have abpos : 0<2^a*3^b := Nat.mul_pos (Nat.two_pow_pos _) bpos
  have ls : 2^a*3^b-1+3^(b+(r.rank+1))*(2^a*(3*k))=2^(a+l)*3^b-1 := by
    rw [Nat.pow_add 2 a,scale,Nat.pow_add 3 b]
    change 2^a*3^b-1+3^b*r.den*(2^a*(3*k))=2^a*(1+3*r.den*k)*3^b-1
    have eq : 3^b*r.den*(2^a*(3*k))=2^a*(3*r.den*k)*3^b := by ac_rfl
    rw [eq,Nat.mul_add,Nat.mul_one,Nat.add_mul]
    omega
  have us : 2^v+3^r.rank*(2^v*(9*k))=2^(v+l) := by
    rw [Nat.pow_add,scale,Nat.mul_add,Nat.mul_one]
    congr 1
    unfold den
    rw [Nat.pow_succ]
    change 3^r.rank*(2^v*((3*3)*k))=2^v*(3*(3^r.rank*3)*k)
    ac_rfl
  have lrun : run r.lower y=2^(a+l)*3^b-1 := by rw [←track_run r.lower y 0,L]; exact ls
  have urun : track H (3*y) 0=(1,r.rank) := by
    rw [show H=r.upper+(v+l) by omega,append_track,U,us,halves]
  have price : r.den*y+r.carry=2^H := by
    rw [eh,Nat.pow_add,scale]
    dsimp only [y]
    grind
  have cy : y%48=17 := by
    have fact : 2^r.clock*(3*k)=48*(2^(r.clock-4)*k) := by
      rw [spl 4 (r.clock-4) (by omega)]
      change 16*2^(r.clock-4)*(3*k)=(16*3)*(2^(r.clock-4)*k)
      ac_rfl
    dsimp only [y]
    rw [fact,Nat.add_mul_mod_self_left,cls]
  refine ⟨y,cy,price,urun,r.lower+(a+l),m-r.gap,?_⟩
  rw [run_add,lrun,ramp _ _ bpos,peak,←Nat.pow_add]
  congr 2
  dsimp only [a,b]
  omega

end Template

end Collatz.Itinerary.PassageDescent
