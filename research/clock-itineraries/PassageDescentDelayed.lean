module

public import PassageDescentDirect
import all PassageDescentDirect
import all ReturnDescent
import all TernaryItinerary

public section

namespace Collatz.Itinerary.PassageDescent

open TowerFrontier ReturnDescent
set_option autoImplicit false
set_option maxRecDepth 10000
set_option maxHeartbeats 2000000
set_option exponentiation.threshold 1000000

structure DelayedChart where
  row : DirectRow
  gain : Nat
deriving Inhabited

/-- Each row lists the delayed parameter residue and period, the upper grade,
    lower clock, carry, and a small canonical two-arm test source and its
    terminal upper value. The last field records the certified size factor. -/
@[expose] def delayedCharts : Array DelayedChart := #[
  ⟨⟨3130, 6561, 11, 18, 2692031, 25937, 13148⟩, 3⟩,
  ⟨⟨4831, 6561, 11, 19, 4970719, 1682993, 426491⟩, 1⟩,
  ⟨⟨457, 19683, 12, 21, 20414317, 21817409, 4146578⟩, 1⟩,
  ⟨⟨862, 19683, 12, 20, 10984637, 8371409, 3182111⟩, 2⟩,
  ⟨⟨1375, 19683, 12, 21, 19049629, 5281841, 1003859⟩, 1⟩,
  ⟨⟨2401, 19683, 12, 19, 7686973, 1881425, 1430324⟩, 4⟩,
  ⟨⟨3447, 19683, 12, 21, 16685725, 14351921, 2727701⟩, 1⟩,
  ⟨⟨5020, 19683, 12, 20, 10144829, 4971089, 1889594⟩, 2⟩,
  ⟨⟨7092, 19683, 12, 20, 8962877, 9506129, 3613436⟩, 2⟩,
  ⟨⟨10420, 19683, 12, 21, 21359101, 17778449, 3378941⟩, 1⟩,
  ⟨⟨14065, 19683, 12, 20, 11299565, 11219393, 4264676⟩, 2⟩,
  ⟨⟨14794, 19683, 12, 20, 14133917, 11685425, 4441823⟩, 2⟩,
  ⟨⟨16900, 19683, 12, 21, 20729245, 12082481, 2296376⟩, 1⟩,
  ⟨⟨531, 59049, 13, 22, 37445831, 40636865, 11585051⟩, 1⟩,
  ⟨⟨3373, 59049, 13, 22, 59074775, 33807665, 9638135⟩, 1⟩,
  ⟨⟨7504, 59049, 13, 22, 46792583, 9366785, 2670353⟩, 1⟩,
  ⟨⟨8233, 59049, 13, 22, 58129991, 43542593, 12413438⟩, 1⟩,
  ⟨⟨9610, 59049, 13, 22, 54035927, 1841201, 524906⟩, 1⟩,
  ⟨⟨16444, 59049, 13, 21, 25332151, 20368721, 11613725⟩, 3⟩,
  ⟨⟨28645, 59049, 13, 21, 32342215, 22081985, 12590585⟩, 3⟩,
  ⟨⟨31804, 59049, 13, 22, 42068663, 7709777, 2197961⟩, 1⟩,
  ⟨⟨37825, 59049, 13, 22, 42173639, 1035713, 295271⟩, 1⟩,
  ⟨⟨38365, 59049, 13, 21, 31397431, 6651089, 3792284⟩, 3⟩,
  ⟨⟨40501, 59049, 13, 22, 46944215, 10911281, 3110669⟩, 1⟩,
  ⟨⟨42685, 59049, 13, 22, 41228855, 10770641, 3070574⟩, 1⟩,
  ⟨⟨44602, 59049, 13, 21, 28878007, 15833681, 9027962⟩, 3⟩,
  ⟨⟨52702, 59049, 13, 22, 60964343, 14337809, 4087529⟩, 1⟩,
  ⟨⟨53343, 59049, 13, 22, 33981623, 9222737, 2629286⟩, 1⟩,
  ⟨⟨53350, 59049, 13, 22, 45532871, 39123905, 11153726⟩, 1⟩,
  ⟨⟨57076, 59049, 13, 21, 23839159, 9033041, 5150411⟩, 3⟩,
  ⟨⟨57879, 59049, 13, 22, 36501047, 40145, 11447⟩, 1⟩,
  ⟨⟨58210, 59049, 13, 22, 44588087, 48858833, 13929029⟩, 1⟩,
  ⟨⟨270, 43046721, 19, 32, 51901264991, 43386849041, 8805689198⟩, 1⟩]

private def valid (a : DelayedChart) : Bool := a.row.check && decide
  (0<a.gain ∧ 81*a.gain*2^a.row.lower≤128*a.row.den ∧
   351*a.row.den<81*a.gain*a.row.carry)

private theorem all_charts : ∀ i : Fin 33, valid delayedCharts[i.val]! = true := by
  decide +kernel

theorem delayed_is_hard (k : Nat) : ∃ j, delayedExponent k=11+162*j := by
  have shape : ∃ v, (2^18)^k=1+27*v := by
    induction k with
    | zero => exact ⟨0,rfl⟩
    | succ k ih =>
      obtain ⟨v,hv⟩ := ih
      exact ⟨262144*v+9709,by rw [Nat.pow_succ,hv]; omega⟩
  obtain ⟨v,hv⟩ := shape
  rw [←Nat.pow_mul] at hv
  exact ⟨2*v,by unfold delayedExponent; rw [hv]; omega⟩

/-- For every ordinary parameter in any of the 33 full ternary classes, a
    smaller canonical pair joins both actual native arms before the peak. -/
theorem delayed_two_arm (i : Fin 33) (s : Nat) :
    let a := delayedCharts[i.val]!
    let r := a.row
    let k := r.residue+r.period*s
    let m := delayedExponent k
    let z := hardParent m
    ∃ Y, Y%48=17 ∧ Y<z ∧ a.gain*Y<z ∧
      r.den*Y+r.carry=2^(m+r.lower) ∧
      track r.lower Y 0=(M m,r.rank+1) ∧ run 7 z=M m ∧
      track (r.lower+2) (3*Y) 0=(2^(m-2),r.rank) ∧
      track 9 (3*z) 0=(2^(m-2),3) ∧ track (m+r.lower) (3*Y) 0=(1,r.rank) := by
  intro a r k m z
  obtain ⟨hc,hp⟩ := Bool.and_eq_true_iff.mp (all_charts i)
  obtain ⟨_,slope,constant⟩ := of_decide_eq_true hp
  obtain ⟨Y,cls,sm,affine,L,U,hit⟩ := DirectRow.before_peak r hc s
  change r.den*Y+r.carry=2^(m+r.lower) at affine
  have gain : a.gain*Y<z := by
    have grow := Nat.mul_le_mul_right (2^m) slope
    have factor := congrArg (fun n => 81*a.gain*n) affine
    rw [Nat.pow_add] at factor
    change a.gain*Y<(2^(m+7)-271)/81
    rw [Nat.pow_add]
    by_cases ok : a.gain*Y<(2^m*2^7-271)/81
    · exact ok
    have cap : 2^m*128≤81*(a.gain*Y)+351 := by omega
    have mul := Nat.mul_le_mul_left r.den cap
    change 81*a.gain*2^r.lower≤128*r.den at slope
    change 351*r.den<81*a.gain*r.carry at constant
    change 81*a.gain*2^r.lower*2^m≤128*r.den*2^m at grow
    grind
  obtain ⟨j,ej⟩ := delayed_is_hard k
  obtain ⟨_,_,nativeL,nativeU,_⟩ := hard_source_data j
  change m=11+162*j at ej
  rw [←ej] at nativeL nativeU
  exact ⟨Y,cls,sm,gain,affine,L,nativeL,U,nativeU,hit⟩

/-- A hypothetical bad member of any listed class has a strictly smaller
    canonical bad lower source with an unconditionally good triple. -/
theorem delayed_not_least (i : Fin 33) (s : Nat) :
    let r := delayedCharts[i.val]!.row
    let m := delayedExponent (r.residue+r.period*s)
    let z := hardParent m
    ¬ReachesOne z → ∃ Y, Y%48=17 ∧ Y<z ∧ ¬ReachesOne Y ∧ ReachesOne (3*Y) := by
  intro r m z bad
  obtain ⟨Y,cls,sm,_,_,lower,native,_,_,upper⟩ := delayed_two_arm i s
  refine ⟨Y,cls,sm,?_,m+r.lower,?_⟩
  · intro good
    apply bad
    apply reaches_of_meets good
    refine ⟨7,r.lower,?_⟩
    rw [native,←track_run r.lower Y 0,lower]
  · rw [←track_run (m+r.lower) (3*Y) 0,upper]

#print axioms delayed_two_arm
#print axioms delayed_not_least

end Collatz.Itinerary.PassageDescent
