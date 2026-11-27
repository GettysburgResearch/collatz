import EarlierOffsets
import DelayedTurns

/-! Crossing from an ordinary earlier exponent at gap four for the entire
cofactor-one delayed family. Two small parameters need their own end words. -/
set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 12000
namespace OffsetFour
open CoreBranching FloorCounting PeakRigidity
open EarlierOffsets (M Good mersenne_peak good_run meet_good)

private abbrev hard := DelayedTurns.hard

private def modPower (a m n : ℕ) : ℕ :=
  if h : n=0 then 1%m else
    let b := modPower a m (n/2)
    (b*b*a^(n%2))%m
termination_by n
decreasing_by omega

private theorem modPower_correct (a m n : ℕ) : modPower a m n=a^n%m := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    rw [modPower]
    split
    · rename_i eq
      simp [eq]
    · rename_i ne
      simp only [ih (n/2) (by omega)]
      have f : a^n=a^(n/2)*a^(n/2)*a^(n%2) := by
        rw [←pow_add,←pow_add]
        congr 1
        omega
      rw [f,Nat.mul_mod (a^(n/2)*a^(n/2)),Nat.mul_mod (a^(n/2)) (a^(n/2)),
        ←Nat.mul_mod]

private theorem period (h : ℕ) : ∃ t, 3^(2^h)=1+2^(h+1)*t := by
  induction h with
  | zero => exact ⟨1,rfl⟩
  | succ h ih =>
    obtain ⟨t,eq⟩:=ih
    refine ⟨t+2^h*t^2,?_⟩
    rw [pow_succ (2:ℕ) h,pow_mul,eq,pow_succ (2:ℕ) (h+1),pow_succ (2:ℕ) h]
    ring

private theorem pow_stable (n h v : ℕ) :
    3^(n+2^h*v) ≡ 3^n [MOD 2^h] := by
  obtain ⟨t,eq⟩ := period h
  have b : 3^(2^h) ≡ 1 [MOD 2^h] := by
    change 3^(2^h)%2^h=1%2^h
    rw [eq,pow_succ,show 2^h*2*t=2^h*(2*t) by ring,Nat.add_mul_mod_self_left]
  rw [pow_add,pow_mul]
  simpa using (b.pow v).mul_left (3^n)

structure Row where
  base : ℕ
  rem : ℕ
  odds : ℕ
  neg : ℕ
  left : ℕ
  right : ℕ
  clocks : ℕ
  residue : ℕ
deriving DecidableEq

def rows : List Row := [
  ⟨7,3,3,55,0,2,31,925119843⟩,
  ⟨8,10,7,34,0,1,109,280482343164554633297535667604585⟩,
  ⟨9,9,7,68,1,0,36,10536291833⟩,
  ⟨10,6,5,61,0,1,64,8188362496081743345⟩,
  ⟨11,8,7,136,0,3,55,7559879358717137⟩]

private def degree (p : Row) (m : ℕ) := 7*((m-5)/11)+3+p.odds-p.left

private structure Checks (p : Row) : Prop where
  wide : 1000≤hard p.base
  rem_eq : p.rem=(hard p.base-5)%11
  odds_le : p.odds≤p.rem
  left_le : p.left≤1
  right_le : p.right≤7
  turn_base : run p.rem (2^p.rem*200-17)+p.neg=3^p.odds*200
  turn_grade : grade p.rem (2^p.rem*200-17)=p.odds
  residue_bound : p.neg≤p.residue
  residue_pos : 0<p.residue
  residue_eq : modPower 3 (2^p.clocks) (degree p (hard p.base))=p.residue
  merge_base : run p.clocks (3^p.left*p.residue-p.neg)=run p.clocks (3^p.right*p.residue-1)
  merge_grade : p.left+grade p.clocks (3^p.left*p.residue-p.neg)=
    p.right+grade p.clocks (3^p.right*p.residue-1)

private def Lift (p : Row) (k : ℕ) :=
  ∃ v, hard k=hard p.base+11*(2^p.clocks*v)

private theorem progress (p : Row) (prec : p.clocks≤18*p.base) (t : ℕ) :
    Lift p (p.base+5*t) := by
  have b : (2:ℕ)^90 ≡ 1 [MOD 11] := by decide +kernel
  have bt : ((2:ℕ)^90)^t%11=1 := by
    have be : ((2:ℕ)^90)^t ≡ 1 [MOD 11] := by simpa using b.pow t
    exact be
  have base_pos : 0<(2:ℕ)^(18*p.base) := by positivity
  have r : 2^(18*p.base)=2^p.clocks*2^(18*p.base-p.clocks) := by
    rw [←pow_add,Nat.add_sub_of_le prec]
  let a := (2^90)^t/11
  have aw : (2^90)^t=1+11*a := by
    change (2^90)^t=1+11*((2^90)^t/11)
    rw [←bt]
    exact (Nat.mod_add_div _ _).symm
  refine ⟨12*2^(18*p.base-p.clocks)*a,?_⟩
  unfold hard DelayedTurns.hard
  rw [show 18*(p.base+5*t)=18*p.base+90*t by ring,pow_add,pow_mul (2:ℕ) 90,aw]
  have out : 12*(2^(18*p.base)*(1+11*a))=
      12*2^(18*p.base)+11*(2^p.clocks*(12*2^(18*p.base-p.clocks)*a)) := by
    conv_lhs => rw [r]
    conv_rhs => lhs; rw [r]
    ring
  omega

private theorem physical (p : Row) (ok : Checks p) (k : ℕ) (lift : Lift p k) :
    ∃ h s l, run h (27*2^(hard k-5)-17)=run (s+l) (M s) ∧
      0<s ∧ s+40<hard k := by
  let m := hard k
  let d := (m-5)/11
  obtain ⟨g,growth⟩:=lift
  let v := 2^p.clocks*g
  change m=hard p.base+11*v at growth
  have wide := ok.wide
  have rr := ok.rem_eq
  have oo := ok.odds_le
  have sl := ok.left_le
  have sr := ok.right_le
  have di : 90≤d := by dsimp [d]; omega
  have drift : d=(hard p.base-5)/11+v := by dsimp [d]; omega
  have bal : m-5=11*d+p.rem := by dsimp [d]; omega
  have remSmall : p.rem<11 := by omega
  have ex : degree p m=degree p (hard p.base)+2^p.clocks*(7*g) := by
    unfold degree
    change 7*d+3+p.odds-p.left=_+_
    rw [drift,show 2^p.clocks*(7*g)=7*v by dsimp [v]; ring]
    omega
  have addr : 3^(degree p m)%2^p.clocks=p.residue := by
    rw [ex]
    have h := pow_stable (degree p (hard p.base)) p.clocks (7*g)
    change 3^(degree p (hard p.base)+2^p.clocks*(7*g))%2^p.clocks=
      3^(degree p (hard p.base))%2^p.clocks at h
    exact h.trans (by simpa only [modPower_correct] using ok.residue_eq)
  let N := 3^(degree p m)
  let U := 3^(7*d+3)
  have ub : 200≤U := calc
    200 ≤ (3:ℕ)^5 := by decide
    _ ≤ U := Nat.pow_le_pow_right (by decide) (by omega)
  have norm : run p.rem (2^p.rem*U-17)=3^p.left*N-p.neg := by
    obtain ⟨w,ww⟩:=Nat.exists_eq_add_of_le ub
    have tr := (lift_prefix p.rem 0 (2^p.rem*200-17) w).1
    simp only [Nat.add_zero,pow_zero,one_mul,ok.turn_grade] at tr
    have sm : 17≤2^p.rem*200 := by have := Nat.two_pow_pos p.rem; omega
    have fac : 3^p.left*N=3^p.odds*U := by
      dsimp [N,U]
      rw [←pow_add,←pow_add]
      congr 1
      unfold degree
      change p.left+(7*d+3+p.odds-p.left)=p.odds+(7*d+3)
      omega
    rw [fac,ww,Nat.mul_add,show 2^p.rem*200+2^p.rem*w-17=(2^p.rem*200-17)+2^p.rem*w by omega,
        tr,Nat.mul_add]
    have := ok.turn_base
    omega
  let s := degree p m+p.right
  have tgt : 3^s=3^p.right*N := by dsimp [s,N]; rw [pow_add,mul_comm]
  have meet : run p.clocks (3^p.left*N-p.neg)=run p.clocks (3^s-1) := by
    let w := N/2^p.clocks
    have rep : N=p.residue+2^p.clocks*w := by
      change N%2^p.clocks=p.residue at addr
      dsimp [w]
      rw [←addr,Nat.mod_add_div]
    have factors (c b : ℕ) (hb : b≤3^c*p.residue) :
        run p.clocks (3^c*N-b)=run p.clocks (3^c*p.residue-b)+
        3^(c+grade p.clocks (3^c*p.residue-b))*w := by
      have h := (lift_prefix p.clocks 0 (3^c*p.residue-b) (3^c*w)).1
      simp only [Nat.add_zero,pow_zero,one_mul] at h
      rw [rep,Nat.mul_add,show 3^c*(2^p.clocks*w)=2^p.clocks*(3^c*w) by ring,
          show 3^c*p.residue+2^p.clocks*(3^c*w)-b=(3^c*p.residue-b)+2^p.clocks*(3^c*w) by omega,
          h,pow_add]
      ring
    have bg := ok.residue_bound.trans (Nat.le_mul_of_pos_left _ (show 0<3^p.left by positivity))
    have bg' := ok.residue_pos.trans_le (Nat.le_mul_of_pos_left _ (show 0<3^p.right by positivity))
    rw [tgt,factors _ _ bg,factors _ _ bg',ok.merge_grade,ok.merge_base]
  have full := DelayedTurns.long_turns d (2^p.rem*27) (by positivity)
  have src : 27*2^(m-5)=2^(11*d)*(2^p.rem*27) := by rw [bal,pow_add]; ring
  have mid : 3^(7*d)*(2^p.rem*27)=2^p.rem*U := by dsimp [U]; rw [pow_add]; ring
  refine ⟨11*d+p.rem+p.clocks,s,p.clocks,?_,?_⟩
  · change run _ (27*2^(m-5)-17)=_
    rw [run_add,run_add,src,full,mid,norm,meet,run_add s p.clocks,mersenne_peak]
  · change 0<degree p m+p.right ∧ degree p m+p.right+40<m
    unfold degree
    change 0<(7*d+3+p.odds-p.left)+p.right ∧ (7*d+3+p.odds-p.left)+p.right+40<m
    omega

set_option maxHeartbeats 0 in
private theorem row_valid (p : Row) (pm : p∈rows) : Checks p ∧ p.clocks≤18*p.base := by
  simp only [rows,List.mem_cons,List.not_mem_nil,or_false] at pm
  rcases pm with h|h|h|h|h <;> subst p <;> constructor
  all_goals first | constructor <;> decide +kernel | decide +kernel

def initialRows : List Row := [
  ⟨1,8,7,136,0,7,80,478383465533037361011921⟩,
  ⟨2,3,3,55,0,2,31,925119843⟩,
  ⟨3,10,7,34,0,1,205,7548976411468858440705357527827992136827202867336784063302761⟩,
  ⟨4,9,7,68,1,0,36,10536291833⟩,
  ⟨5,6,5,61,0,1,64,8188362496081743345⟩,
  ⟨6,8,7,136,0,3,55,7559879358717137⟩]

set_option maxHeartbeats 0 in
private theorem initial_valid (p : Row) (pm : p∈initialRows) : Checks p := by
  simp only [initialRows,List.mem_cons,List.not_mem_nil,or_false] at pm
  rcases pm with h|h|h|h|h|h <;> subst p <;> constructor <;> decide +kernel

/-- The negative-seventeen opposing branch at offset four has an ordinary
earlier Mersenne merger for every positive delayed parameter. -/
theorem earlier_after_turns (k : ℕ) (hk : 0<k) :
    ∃ h s l, run h (27*2^(hard k-5)-17)=run (s+l) (M s) ∧
      0<s ∧ s+40<hard k := by
  by_cases big : 7≤k
  · let i := (k-7)%5
    have il : i<rows.length := by change (k-7)%5<5; omega
    let p := rows[i]'il
    have pm : p∈rows := List.getElem_mem il
    have pi : i<5 := by dsimp [i]; omega
    have pb : p.base=7+i := by interval_cases i <;> simp [p,rows]
    let v := (k-7)/5
    have kv : p.base+5*v=k := by dsimp [v]; rw [pb]; dsimp [i]; omega
    have ok := row_valid p pm
    have pr := progress p ok.2 v
    rw [kv] at pr
    exact physical p ok.1 k pr
  · let i := k-1
    have il : i<initialRows.length := by change k-1<6; omega
    let p := initialRows[i]'il
    have pm : p∈initialRows := List.getElem_mem il
    have pi : i<6 := by dsimp [i]; omega
    have pb : p.base=i+1 := by interval_cases i <;> simp [p,initialRows]
    have kb : p.base=k := by dsimp [i] at pb; omega
    exact physical p (initial_valid p pm) k ⟨0,by simp [kb]⟩

private theorem hard_address (k : ℕ) : ∃ j, hard k=11+162*j := by
  have per : (2:ℕ)^18 ≡ 1 [MOD 27] := by decide
  have b : (2:ℕ)^(18*k) ≡ 1 [MOD 27] := by simpa only [pow_mul,one_pow] using per.pow k
  change (2:ℕ)^(18*k)%27=1 at b
  exact ⟨2*(2^(18*k)/27),by unfold hard DelayedTurns.hard; omega⟩

private theorem short_address (j : ℕ) : 2^(6+162*j)%243=64 := by
  have per : (2:ℕ)^162 ≡ 1 [MOD 243] := by decide
  have base : (2:ℕ)^6 ≡ 64 [MOD 243] := by decide
  have b := base.mul (per.pow j)
  rw [←pow_mul,←pow_add,one_pow,mul_one] at b
  exact b

/-- Explicit smaller canonical query shared by the entire arithmetic
progression. Its two shortcut prefixes are witnessed separately. -/
theorem paid_chart (j z : ℕ) (parent : 81*z+271=128*2^(11+162*j)) :
    ∃ w, 0<w ∧ 2*w+31=z ∧ w<z ∧ w%48=17 ∧
      run 10 w=M (11+162*j-4) ∧ grade 10 w=4 ∧
      run 11 (3*w)=27*2^(11+162*j-5)-17 ∧ grade 11 (3*w)=6 := by
  let X := 2^(6+162*j)
  let v := X/243
  have r := short_address j
  change X%243=64 at r
  have rep : X=64+243*v := by dsimp [v]; omega
  have pm : 2^(11+162*j)=32*X := by
    change 2^(11+162*j)=2^5*2^(6+162*j)
    rw [←pow_add]; congr 1; omega
  have pn : 2^(11+162*j-4)=2*X := by
    change 2^(11+162*j-4)=2^1*2^(6+162*j)
    rw [←pow_add]; congr 1; omega
  let w := 1601+6144*v
  have lo := lift_prefix 10 0 1601 (6*v)
  have hi := lift_prefix 11 0 (3*1601) (9*v)
  have le : 3*w=3*1601+2^11*(9*v) := by dsimp [w]; ring
  simp only [Nat.add_zero,pow_zero,one_mul] at lo hi
  have we : w=1601+2^10*(6*v) := by dsimp [w]; ring
  rw [←we] at lo
  rw [show grade 10 1601=4 by decide,show run 10 1601=127 by decide] at lo
  rw [←le,show grade 11 (3*1601)=6 by decide,show run 11 (3*1601)=1711 by decide] at hi
  rw [pm] at parent
  have vpos : 0<w := by dsimp [w]; omega
  have ze : 2*w+31=z := by dsimp [w]; omega
  refine ⟨w,vpos,ze,by omega,by dsimp [w]; omega,?_,lo.2,?_,hi.2⟩
  · unfold M
    rw [pn,lo.1]
    omega
  · have e : 11+162*j-5=6+162*j := by omega
    rw [e,hi.1]
    change _=27*X-17
    omega

/-- Two leastness hypotheses suffice to return every earlier exponent up
through m-3 on the whole delayed family. -/
theorem earlier_good_delayed (k z : ℕ) (hk : 0<k)
    (parent : 81*z+271=128*2^(hard k))
    (floor : ∀ y, 0<y → 2^40*y<z → Good y)
    (canonical : ∀ w, 0<w → w<z → w%48=17 → Good (3*w) → Good w) :
    ∀ n, 0<n → n+3≤hard k → Good (M n) := by
  obtain ⟨j,addr⟩:=hard_address k
  have par := parent
  rw [addr] at par
  have small := EarlierOffsets.earlier_good j z par floor canonical
  rw [←addr] at small
  obtain ⟨w,wp,_,wz,wc,lo,_,hi,_⟩:=paid_chart j z par
  rw [←addr] at lo hi
  obtain ⟨h,s,l,meet,sp,gap⟩:=earlier_after_turns k hk
  have goodS := small s sp (by omega)
  have link : run (11+h) (3*w)=run (s+l) (M s) := by rw [run_add,hi,meet]
  have gw := (good_run 10 w).mpr (canonical w wp wz wc ((meet_good link).mpr goodS))
  rw [lo] at gw
  have good4 := gw
  intro n pos lim
  by_cases far : n+5≤hard k
  · exact small n pos far
  by_cases near : n=hard k-4
  · exact near ▸ good4
  have ne : n%2=0 := by omega
  exact (EarlierOffsets.even_index _ pos ne).mpr ((by omega : n-1=hard k-4) ▸ good4)

#print axioms earlier_after_turns
#print axioms paid_chart
#print axioms earlier_good_delayed
end OffsetFour
