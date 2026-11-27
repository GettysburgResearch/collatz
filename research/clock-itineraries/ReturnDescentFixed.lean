module

public import ReturnDescentRows
import all ReturnDescentRows
import all ReturnDescent
import all TowerFrontierAffine
import all TernaryItinerary

public section

namespace Collatz.Itinerary.ReturnDescent

open TowerFrontier
set_option autoImplicit false
set_option maxRecDepth 200000
set_option maxHeartbeats 2000000
set_option exponentiation.threshold 100000

/-- A smaller canonical source with a shorter, three-odd upper certificate. -/
@[expose] def CanonicalReturn (m : Nat) : Prop :=
  ∃ H Y, H≤m ∧ Y<hardParent m ∧ Y%48=17 ∧ track H (3*Y) 0=(1,3) ∧ Meets (hardParent m) Y

/-- A supplied earlier exponent satisfying the row's actual price gives a
    canonical return at the original hard parent, without any leastness input. -/
theorem return_of_earlier {j m t : Nat} (row : m=11+162*j) (positive : 0<t)
    (budget : max 18 (t+clockCharge t)≤m) (meeting : Meets (M m) (M t)) :
    CanonicalReturn m := by
  obtain ⟨H,Y,cost,hy⟩ := priced_representative t positive
  obtain ⟨floor,_,lower,_⟩ := hard_source j
  rw [←row] at floor lower
  have hbound := Nat.le_trans cost budget
  have ht := Nat.pow_le_pow_right (by decide : 0<2) hbound
  have hyz := Nat.lt_trans (Nat.lt_of_lt_of_le hy.2.1 ht) floor
  exact ⟨H,Y,hbound,hyz,hy.1,hy.2.2.1,(Meets.trans (show Meets (hardParent m) (M m) from
    ⟨7,0,lower⟩) meeting).trans hy.2.2.2.symm⟩

theorem return_of_gap {j m t : Nat} (row : m=11+162*j) (positive : 0<t)
    (budget : t+2081≤m) (meeting : Meets (M m) (M t)) : CanonicalReturn m := by
  exact return_of_earlier row positive (by have := charge_bound t; omega) meeting

private def powerMod : Nat → Nat → Nat → Nat → Nat
  | 0, _, _, D => 1%D
  | f+1, a, e, D =>
    let z := powerMod f (a*a%D) (e/2) D
    if e%2=0 then z else (a*z)%D

private theorem powerMod_spec (f a e D : Nat) (bits : e<2^f) :
    powerMod f a e D=a^e%D := by
  induction f generalizing a e with
  | zero =>
    have eq : e=0 := by simpa using bits
    simp [eq,powerMod]
  | succ f ih =>
    have b : e/2<2^f := by rw [Nat.pow_succ] at bits; omega
    have square : (a*a%D)^(e/2)%D=a^(2*(e/2))%D := by
      rw [←Nat.pow_mod, Nat.pow_mul, Nat.pow_succ a 1, Nat.pow_one]
    rw [powerMod,ih _ _ b,square]
    split
    · exact congrArg (fun k => a^k%D) (by omega)
    · rw [Nat.mul_mod_mod,Nat.mul_comm,←Nat.pow_succ]
      exact congrArg (fun k => a^k%D) (by omega)

/-- Use a positive small representative for the earlier peak. Both its endpoint
    and its augmented odd grade must agree for the meeting to lift. -/
private theorem peak_cert {h d t b : Nat} (pos : 0<b) (res : b=3^t%2^h)
    (ck : track h (3^d*b-1) d=track h (b-1) 0) :
    Meets (M (t+d)) (M t) := by
  let u := 3^t/2^h
  have eq : b+2^h*u=3^t := by simpa only [res] using Nat.mod_add_div (3^t) (2^h)
  have start : 3^(t+d)-1=(3^d*b-1)+2^h*3^d*u := by
    have p : 0<3^d*b := Nat.mul_pos (Nat.pow_pos (by decide)) pos
    rw [Nat.add_comm t d,Nat.pow_add,←eq,Nat.mul_add,
      show 3^d*(2^h*u)=2^h*3^d*u by ac_rfl]
    omega
  have earlier : 3^t-1=(b-1)+2^h*3^0*u := by rw [←eq]; simp only [Nat.pow_zero,Nat.mul_one]; omega
  refine ⟨(t+d)+h,t+h,?_⟩
  rw [run_add,peak,run_add,peak,start,earlier,affine,affine,ck]

@[expose] def delayedExponent (k : Nat) := 12*2^(18*k)-1

private def Physical (k d h : Nat) : Prop :=
  let m := delayedExponent k
  let t := m-d
  let f := 18*k+4
  let b := powerMod f 3 t (2^h)
  m%162=11 ∧ 0<t ∧ t+d=m ∧ t<2^f ∧ 0<b ∧ max 18 (t+clockCharge t)≤m ∧
  stride h (3^d*b-1) d=stride h (b-1) 0

private instance (k d h : Nat) : Decidable (Physical k d h) := by
  unfold Physical; infer_instance

private theorem physical_return {k d h : Nat} (cert : Physical k d h) :
    CanonicalReturn (delayedExponent k) := by
  let m := delayedExponent k
  let t := m-d
  let b := powerMod (18*k+4) 3 t (2^h)
  obtain ⟨rc,pt,eq,bits,pb,cost,words⟩ := cert
  rw [stride_eq,stride_eq] at words
  have matchPeaks := peak_cert pb (powerMod_spec _ _ _ _ bits) words
  rw [eq] at matchPeaks
  have row : m=11+162*(m/162) := by change m%162=11 at rc; omega
  exact return_of_earlier row pt cost matchPeaks

private def visits : Array (Nat × Nat) := #[
  (0,0), (27,110), (27,6160), (28,1950), (95,5110), (75,2480), (75,1090), (75,190),
  (95,3560), (123,480), (123,4100), (125,300), (125,370), (124,610), (126,3690), (155,460),
  (155,440), (162,460), (189,500), (195,520), (195,1030), (190,1040), (196,2220), (196,4140),
  (237,620), (126,6170), (238,1170), (248,1240), (309,22640), (285,670), (287,720), (309,4730),
  (309,760), (321,780), (317,3610), (324,1350), (328,1530), (351,1410), (357,830), (346,1440),
  (346,1730), (376,930), (386,1490), (423,1680), (409,970), (410,990), (423,1300), (432,1030),
  (441,1010), (450,920), (469,1090), (483,960), (507,1090), (501,1070), (492,1150), (505,1030),
  (557,2110), (557,1760), (533,1220), (540,1210), (548,1140), (559,1840), (567,1850), (581,1310),
  (585,1890), (601,2420), (603,1370), (623,3420), (618,1960), (624,1980), (651,2000), (648,2020),
  (691,3010), (666,2050), (691,2840), (691,2090), (692,1430), (725,1860), (711,1550), (0,0),
  (728,3870), (753,1640), (753,2210), (754,2230), (765,1700), (774,2270), (782,2290), (813,1760),
  (801,2320), (810,1780), (823,2360), (837,2380), (837,1850), (846,1820), (859,2430), (864,3220),
  (885,2470), (903,2480), (903,2500), (903,2520), (925,4040), (918,5200), (927,2570), (936,9380),
  (944,2610), (965,4270), (1035,2380), (970,2110), (980,2680), (990,2700), (999,5320), (1008,7010),
  (0,0), (1026,4840), (1083,3560), (1044,2190), (1053,2270), (1065,2840), (1083,2310), (1083,2880),
  (1089,4870), (1096,2920), (1107,7910), (1116,2360), (1125,2420), (1132,2990), (1138,6680), (1148,9800),
  (1243,4990), (0,0), (1179,3850), (1188,3100), (1243,3880), (1206,3130), (0,0), (1269,5260),
  (1243,2630), (0,0), (1246,3220), (1265,2680), (1268,3260), (1281,2690), (1365,4060), (1315,8270),
  (1325,2770), (1325,3350), (1323,3370), (1332,2830), (1341,2810), (0,0), (1365,7860), (1368,6810),
  (1403,3470), (1403,3490), (1395,3510), (1405,3530), (1413,2870), (1422,3560), (0,0), (1422,6910),
  (1412,3060), (1412,3080), (1467,3650), (1476,3110), (1485,3100), (1499,3160), (1503,3140), (1512,3740),
  (1551,7630), (1530,3220), (1539,3800), (1548,6060), (1559,3280), (1566,4620), (1575,6120), (1582,6130),
  (1593,7660), (1629,4690), (1643,4350), (0,0), (1629,3980), (1638,4000), (1647,4010), (1656,4030),
  (1662,3500), (1677,4070), (1701,4850), (1690,3560), (1698,4120), (1713,3550), (1718,3570), (1728,6420)]

/-- Fixed parent parameters whose three-odd canonical returns are checked here. -/
@[expose] def verifiedParameter (k : Nat) : Bool :=
  decide (1≤k ∧ k≤192) && ![1,80,113,130,135,138,150,159,180].contains k

private def visitTest (i : Nat) : Bool :=
  let v := visits[i]!
  if verifiedParameter (i+1) then decide (Physical (i+1) v.1 v.2) else true

private theorem visit0 : segment visitTest 8 0=true := by decide +kernel
private theorem visit1 : segment visitTest 8 8=true := by decide +kernel
private theorem visit2 : segment visitTest 8 16=true := by decide +kernel
private theorem visit3 : segment visitTest 8 24=true := by decide +kernel
private theorem visit4 : segment visitTest 8 32=true := by decide +kernel
private theorem visit5 : segment visitTest 8 40=true := by decide +kernel
private theorem visit6 : segment visitTest 8 48=true := by decide +kernel
private theorem visit7 : segment visitTest 8 56=true := by decide +kernel
private theorem visit8 : segment visitTest 8 64=true := by decide +kernel
private theorem visit9 : segment visitTest 8 72=true := by decide +kernel
private theorem visit10 : segment visitTest 8 80=true := by decide +kernel
private theorem visit11 : segment visitTest 8 88=true := by decide +kernel
private theorem visit12 : segment visitTest 8 96=true := by decide +kernel
private theorem visit13 : segment visitTest 8 104=true := by decide +kernel
private theorem visit14 : segment visitTest 8 112=true := by decide +kernel
private theorem visit15 : segment visitTest 8 120=true := by decide +kernel
private theorem visit16 : segment visitTest 8 128=true := by decide +kernel
private theorem visit17 : segment visitTest 8 136=true := by decide +kernel
private theorem visit18 : segment visitTest 8 144=true := by decide +kernel
private theorem visit19 : segment visitTest 8 152=true := by decide +kernel
private theorem visit20 : segment visitTest 8 160=true := by decide +kernel
private theorem visit21 : segment visitTest 8 168=true := by decide +kernel
private theorem visit22 : segment visitTest 8 176=true := by decide +kernel
private theorem visit23 : segment visitTest 8 184=true := by decide +kernel
private theorem visitAll : segment visitTest 192 0=true :=
  (@segment_join visitTest 96 96 0 (@segment_join visitTest 48 48 0 (@segment_join visitTest 24 24 0 (@segment_join visitTest 8 16 0 visit0 (@segment_join visitTest 8 8 8 visit1 visit2)) (@segment_join visitTest 8 16 24 visit3 (@segment_join visitTest 8 8 32 visit4 visit5))) (@segment_join visitTest 24 24 48 (@segment_join visitTest 8 16 48 visit6 (@segment_join visitTest 8 8 56 visit7 visit8)) (@segment_join visitTest 8 16 72 visit9 (@segment_join visitTest 8 8 80 visit10 visit11)))) (@segment_join visitTest 48 48 96 (@segment_join visitTest 24 24 96 (@segment_join visitTest 8 16 96 visit12 (@segment_join visitTest 8 8 104 visit13 visit14)) (@segment_join visitTest 8 16 120 visit15 (@segment_join visitTest 8 8 128 visit16 visit17))) (@segment_join visitTest 24 24 144 (@segment_join visitTest 8 16 144 visit18 (@segment_join visitTest 8 8 152 visit19 visit20)) (@segment_join visitTest 8 16 168 visit21 (@segment_join visitTest 8 8 176 visit22 visit23)))))

theorem fixed_canonical_returns {k : Nat} (certified : verifiedParameter k=true) :
    CanonicalReturn (delayedExponent k) := by
  have interval : 1≤k ∧ k≤192 := of_decide_eq_true (Bool.and_eq_true_iff.mp certified).1
  have test := segment_sound visitAll (Nat.zero_le (k-1)) (by omega)
  unfold visitTest at test
  dsimp only at test
  rw [show k-1+1=k by omega,certified] at test
  exact physical_return (of_decide_eq_true test)

#print axioms fixed_canonical_returns

end Collatz.Itinerary.ReturnDescent
