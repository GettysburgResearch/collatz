module

public import PassageDescentRows
import all PassageDescentRows
import all ReturnDescent
import all TowerFrontierAffine
import all TernaryItinerary

public section

namespace Collatz.Itinerary.PassageDescent

open TowerFrontier ReturnDescent
set_option autoImplicit false
set_option maxRecDepth 40000
set_option maxHeartbeats 8000000
set_option exponentiation.threshold 1000000

/- residue, ternary period, earlier exponent gap, upper odd departures,
   upper clock minus m, intercept, lower clocks, upper prefix, remaining
   lower power of three. The following theorems check the entire array. -/
private def rows : Array Template := #[
  ⟨7, 9, 10, 5, 3, 7879, 14, 13, 1⟩,
  ⟨1, 9, 9, 5, 6, 33143, 16, 16, 1⟩,
  ⟨13, 27, 17, 6, 1, 87445, 21, 15, 3⟩,
  ⟨4, 27, 10, 6, 5, 32245, 16, 15, 1⟩,
  ⟨12, 27, 10, 6, 5, 40021, 15, 15, 0⟩,
  ⟨23, 27, 17, 6, 5, 1284181, 25, 21, 3⟩,
  ⟨0, 27, 20, 6, 5, 1393045, 33, 19, 8⟩,
  ⟨11, 27, 10, 6, 6, 62789, 17, 16, 1⟩,
  ⟨9, 27, 17, 6, 6, 2578325, 26, 22, 3⟩,
  ⟨26, 27, 10, 6, 7, 116101, 18, 17, 1⟩,
  ⟨21, 27, 10, 6, 8, 230501, 19, 18, 1⟩,
  ⟨22, 27, 9, 6, 8, 133301, 18, 18, 1⟩,
  ⟨8, 27, 17, 6, 8, 10312085, 28, 24, 3⟩,
  ⟨6, 27, 9, 6, 9, 264901, 19, 19, 1⟩,
  ⟨18, 27, 17, 6, 9, 20291989, 29, 25, 3⟩,
  ⟨17, 27, 18, 6, 10, 1434005, 41, 20, 13⟩,
  ⟨14, 81, 17, 7, 2, 180479, 22, 16, 3⟩,
  ⟨42, 81, 17, 7, 6, 2620607, 26, 22, 3⟩,
  ⟨3, 81, 10, 7, 7, 162271, 17, 17, 0⟩,
  ⟨20, 81, 17, 7, 7, 5162239, 27, 23, 3⟩,
  ⟨78, 81, 17, 7, 7, 5177791, 27, 23, 3⟩,
  ⟨69, 81, 10, 7, 8, 319439, 18, 18, 0⟩,
  ⟨47, 81, 10, 7, 8, 253343, 19, 18, 1⟩,
  ⟨51, 81, 17, 7, 9, 20625871, 29, 25, 3⟩,
  ⟨2, 81, 19, 7, 9, 15979711, 35, 23, 7⟩,
  ⟨41, 81, 9, 7, 10, 531503, 20, 20, 1⟩,
  ⟨74, 81, 10, 7, 10, 928079, 21, 20, 1⟩,
  ⟨57, 81, 10, 7, 10, 924191, 21, 20, 1⟩,
  ⟨68, 81, 20, 7, 10, 8614655, 42, 24, 12⟩,
  ⟨32, 81, 17, 7, 11, 82495951, 31, 27, 3⟩,
  ⟨30, 81, 20, 7, 11, 16971487, 43, 25, 12⟩,
  ⟨24, 81, 20, 7, 12, 33937871, 44, 26, 12⟩,
  ⟨218, 243, 17, 8, 3, 377725, 23, 17, 3⟩,
  ⟨5, 243, 17, 8, 5, 1441645, 25, 19, 3⟩,
  ⟨29, 243, 19, 8, 8, 12487421, 33, 22, 6⟩,
  ⟨96, 243, 10, 8, 10, 1284317, 20, 20, 0⟩,
  ⟨137, 243, 17, 8, 11, 82506157, 31, 27, 3⟩,
  ⟨56, 243, 10, 8, 11, 2829373, 21, 21, 0⟩,
  ⟨177, 243, 10, 8, 12, 4881389, 22, 22, 0⟩,
  ⟨191, 243, 17, 8, 12, 161672765, 32, 28, 3⟩,
  ⟨140, 243, 9, 8, 13, 4249837, 23, 23, 1⟩,
  ⟨15, 243, 20, 8, 13, 68044141, 45, 27, 12⟩,
  ⟨86, 243, 17, 8, 13, 329990365, 33, 29, 3⟩,
  ⟨167, 243, 19, 8, 13, 255667357, 39, 27, 7⟩,
  ⟨110, 243, 19, 8, 13, 170310205, 40, 27, 8⟩,
  ⟨464, 729, 20, 9, 6, 2023799, 35, 20, 9⟩,
  ⟨302, 729, 19, 9, 11, 65962231, 37, 25, 7⟩,
  ⟨545, 729, 18, 9, 12, 148989623, 35, 28, 5⟩,
  ⟨221, 729, 17, 9, 12, 108678839, 33, 26, 4⟩,
  ⟨59, 729, 19, 9, 13, 399130183, 38, 27, 6⟩,
  ⟨707, 2187, 20, 10, 8, 8154245, 37, 22, 9⟩,
  ⟨1436, 2187, 18, 10, 15, 1173946405, 38, 29, 5⟩,
  ⟨2165, 2187, 18, 10, 17, 4690648357, 40, 33, 5⟩]

private def idx (i : Nat) : Nat :=
  rows.findIdx (fun r => i%r.period==r.residue)%53

private def atRow (i : Nat) := rows[i]!

private def gapOK (g : Nat) : Prop := g=9 ∨ g=10 ∨ g=17 ∨ g=18 ∨ g=19 ∨ g=20

private def safe (r : Template) : Bool := decide
  ((r.gap=9 ∨ r.gap=10 ∨ r.gap=17 ∨ r.gap=18 ∨ r.gap=19 ∨ r.gap=20) ∧
   r.extra≤17 ∧ r.rank≤10 ∧ 0<r.carry ∧ 2^r.extra≤r.den ∧
   162*2^r.extra≤128*r.den ∧ 271*r.den<162*r.carry)

private def sharp (r : Template) : Bool := decide
  (r.extra≤8 ∧ r.rank≤6 ∧ 2187*2^r.extra≤256*r.den ∧ 542*r.den<2187*r.carry)

private theorem checked : ∀ i : Fin 53, (atRow i.val).Checked ∧ safe (atRow i.val)=true := by
  decide +kernel

private def coverage (i : Nat) : Bool :=
  let r := atRow (idx i)
  decide (i%r.period=r.residue ∧ 2187%r.period=0) &&
    (!(i%3==1 || i%27==0) || sharp r)

private theorem covered : ∀ i : Fin 2187, coverage i.val=true := by
  decide +kernel

/-- The six inexpensive templates suffice on every ternary square unit and
    the full zero class modulo 27. -/
@[expose] def PowerWindow (j : Nat) : Prop := j%3=1 ∨ j%27=0

private theorem extract (j : Nat) (pos : 0<j) :
    ∃ (r : Template) (s : Nat), r.Checked ∧ safe r=true ∧
      j=r.baseIndex+r.period*s ∧ (PowerWindow j → sharp r=true) := by
  let i := j%2187
  let r := atRow (idx i)
  obtain ⟨ck,safeR⟩ := checked ⟨idx i,Nat.mod_lt _ (by decide)⟩
  have cov := covered ⟨i,Nat.mod_lt _ (by decide)⟩
  change (decide (i%r.period=r.residue ∧ 2187%r.period=0) &&
    (!(i%3==1 || i%27==0) || sharp r))=true at cov
  obtain ⟨cc,sc⟩ := Bool.and_eq_true_iff.mp cov
  obtain ⟨ic,div⟩ := of_decide_eq_true cc
  have jc : j%r.period=r.residue := by
    rw [←ic]
    exact (Nat.mod_mod_of_dvd j (Nat.dvd_of_mod_eq_zero div)).symm
  have spec := Nat.mod_add_div j r.period
  rw [jc] at spec
  have shape : ∃ s, j=r.baseIndex+r.period*s := by
    by_cases zero : r.residue=0
    · cases q : j/r.period with
      | zero => rw [q,zero] at spec; simp_all
      | succ t =>
        refine ⟨t,?_⟩
        rw [q,zero,Nat.mul_succ] at spec
        simp only [Template.baseIndex,zero,↓reduceIte]
        omega
    · exact ⟨j/r.period,by simpa [Template.baseIndex,zero] using spec.symm⟩
  obtain ⟨s,hs⟩ := shape
  refine ⟨r,s,ck,safeR,hs,?_⟩
  intro hw
  have c3 : i%3=j%3 := Nat.mod_mod_of_dvd j (by decide : 3∣2187)
  have c27 : i%27=j%27 := Nat.mod_mod_of_dvd j (by decide : 27∣2187)
  rcases hw with h|h
  · simpa only [c3,h,beq_self_eq_true,Bool.true_or,Bool.not_true,Bool.false_or] using sc
  · simpa only [c27,h,beq_self_eq_true,Bool.or_true,Bool.not_true,Bool.false_or] using sc

private theorem hard_exact (j : Nat) :
    let m := 11+162*j
    81*hardParent m+271=128*2^m := by
  intro m
  have factor : ∃ v, (2^162)^j=1+243*v := by
    induction j with
    | zero => exact ⟨0,rfl⟩
    | succ j ih =>
      obtain ⟨v,hv⟩ := ih
      let d := (2^162-1)/243
      have b : 2^162=1+243*d := by decide +kernel
      exact ⟨v+d+243*v*d,by rw [Nat.pow_succ,hv,b]; grind⟩
  obtain ⟨v,hv⟩ := factor
  rw [←Nat.pow_mul] at hv
  have pp : 2^m=2048*(1+243*v) := by dsimp only [m]; rw [Nat.pow_add,hv]
  unfold hardParent
  rw [Nat.pow_add,pp]
  omega

private theorem price_inequality {a b D C E X y z : Nat}
    (base : D*y+C=E*X) (original : 81*z+271=128*X)
    (slope : (81*a)*E≤(128*b)*D) (constant : (271*b)*D<(81*a)*C) :
    a*y<b*z := by
  have amount := Nat.mul_le_mul_right X slope
  have edge := congrArg (fun n => 81*a*n) base
  have source := congrArg (fun n => b*D*n) original
  by_cases hn : a*y<b*z
  · exact hn
  have opp : b*z≤a*y := by omega
  have prod := Nat.mul_le_mul_left (81*D) opp
  grind

/-- Actual canonical comparison with the original physical parent. -/
@[expose] def ReturnAt (m H p Y : Nat) : Prop :=
  Y%48=17 ∧ track H (3*Y) 0=(1,p) ∧ Meets (hardParent m) Y

/-- Every supplied parameter in the complete binary progression gets a
    strictly smaller canonical visitor with a proven upper hit. -/
theorem binary_return {j : Nat} (binary : ∃ s, j=1+2^496*s) :
    let m := 11+162*j
    let z := hardParent m
    ∃ H p Y, ReturnAt m H p Y ∧ Y<2^m ∧ 2*Y<z ∧ H≤m+17 ∧ p≤10 ∧
      (PowerWindow j → 27*Y<2*z ∧ H≤m+8 ∧ p≤6) := by
  intro m z
  obtain ⟨d,jd⟩ := binary
  have pos : 0<j := by omega
  obtain ⟨r,s,ck,sf,js,pw⟩ := extract j pos
  obtain ⟨g,et,pt,cp,price,sl,cn⟩ := of_decide_eq_true sf
  have phys := r.physical ck s
  rw [←js] at phys
  obtain ⟨y,cls,eq,hit,meet⟩ := phys
  let H := m+r.extra
  have affine : r.den*y+r.carry=2^r.extra*2^m := by
    change r.den*y+r.carry=2^(m+r.extra) at eq
    rw [Nat.pow_add,Nat.mul_comm (2^m) (2^r.extra)] at eq
    exact eq
  have size : y<2^m := by
    have p := Nat.mul_le_mul_right (2^m) price
    by_cases hn : y<2^m
    · exact hn
    have p' := Nat.mul_le_mul_left r.den (show 2^m≤y by omega)
    omega
  have orig := hard_exact j
  change 81*z+271=128*2^m at orig
  have two := price_inequality (a:=2) (b:=1) affine orig sl cn
  have route : Meets z y :=
    ((show Meets z (M m) from ⟨7,0,(hard_source j).2.2.1⟩).trans
      (meeting_of_chart (anchor_499 ⟨d,jd⟩ g))).trans meet.symm
  refine ⟨H,r.rank,y,⟨cls,hit,route⟩,size,by simpa using two,by dsimp [H]; omega,pt,?_⟩
  intro window
  obtain ⟨et',pt',sl',cn'⟩ := of_decide_eq_true (pw window)
  exact ⟨price_inequality (a:=27) (b:=2) affine orig sl' cn',by dsimp [H]; omega,pt'⟩

end Collatz.Itinerary.PassageDescent
