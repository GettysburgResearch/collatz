module

public import ReturnDescent
import all ReturnDescent
import all TowerFrontierAffine
import all TernaryItinerary

public section

namespace Collatz.Itinerary.ReturnDescent

open TowerFrontier
set_option autoImplicit false
set_option maxRecDepth 30000
set_option maxHeartbeats 2000000
set_option exponentiation.threshold 20000

private structure Row where
  gap : Nat
  start : Nat
  shift : Nat
  delta : Nat
  lowerClocks : Nat
  grade : Nat
deriving Inhabited

/- One template per odd residue. The shift selects one of two neighboring
   Mersenne exponents. Every table entry is checked below on both physical arms. -/
private def rows : Array Row := #[
  ⟨476, 1135, 1, 1050, 2028, 978⟩,
  ⟨250, 651, 0, 631, 1279, 648⟩,
  ⟨189, 491, 1, 439, 863, 424⟩,
  ⟨122, 331, 1, 276, 536, 260⟩,
  ⟨730, 1953, 0, 1789, 3596, 1807⟩,
  ⟨6, 11, 0, 7, 7, 0⟩,
  ⟨124, 337, 1, 278, 538, 260⟩,
  ⟨254, 663, 0, 635, 1283, 648⟩,
  ⟨36, 179, 1, 66, 114, 48⟩,
  ⟨114, 343, 1, 268, 528, 260⟩,
  ⟨860, 2127, 0, 2081, 4165, 2084⟩,
  ⟨344, 833, 0, 825, 1644, 819⟩,
  ⟨128, 349, 1, 282, 542, 260⟩,
  ⟨166, 513, 1, 378, 737, 359⟩,
  ⟨487, 1001, 1, 1061, 2039, 978⟩,
  ⟨474, 1003, 1, 1048, 2026, 978⟩,
  ⟨285, 681, 1, 597, 1127, 530⟩,
  ⟨185, 521, 1, 435, 859, 424⟩,
  ⟨434, 1009, 1, 1008, 1986, 978⟩,
  ⟨244, 687, 0, 625, 1273, 648⟩,
  ⟨195, 527, 1, 445, 869, 424⟩,
  ⟨656, 1663, 0, 1567, 3121, 1554⟩,
  ⟨724, 1827, 0, 1783, 3590, 1807⟩,
  ⟨19, 47, 1, 35, 59, 24⟩,
  ⟨21, 49, 0, 30, 42, 12⟩,
  ⟨732, 1833, 0, 1791, 3598, 1807⟩,
  ⟨133, 377, 1, 287, 547, 260⟩,
  ⟨173, 379, 1, 385, 744, 359⟩,
  ⟨158, 381, 1, 370, 729, 359⟩,
  ⟨495, 1031, 1, 1069, 2047, 978⟩,
  ⟨165, 385, 1, 377, 736, 359⟩,
  ⟨160, 387, 1, 372, 731, 359⟩,
  ⟨129, 389, 1, 283, 543, 260⟩,
  ⟨180, 553, 1, 430, 854, 424⟩,
  ⟨343, 879, 0, 824, 1643, 819⟩,
  ⟨127, 395, 1, 281, 541, 260⟩,
  ⟨132, 397, 1, 286, 546, 260⟩,
  ⟨164, 399, 1, 376, 735, 359⟩,
  ⟨12, 77, 1, 18, 25, 7⟩,
  ⟨265, 727, 0, 646, 1294, 648⟩,
  ⟨772, 1863, 0, 1831, 3638, 1807⟩,
  ⟨523, 1055, 1, 1097, 2075, 978⟩,
  ⟨492, 1057, 1, 1066, 2044, 978⟩,
  ⟨85, 249, 1, 187, 358, 171⟩,
  ⟨491, 1061, 1, 1065, 2043, 978⟩,
  ⟨182, 577, 1, 432, 856, 424⟩,
  ⟨170, 417, 1, 382, 741, 359⟩,
  ⟨80, 257, 1, 182, 353, 171⟩,
  ⟨7, 97, 1, 9, 10, 1⟩,
  ⟨154, 423, 1, 366, 725, 359⟩,
  ⟨193, 425, 1, 443, 867, 424⟩,
  ⟨263, 751, 0, 644, 1292, 648⟩,
  ⟨750, 1887, 0, 1809, 3616, 1807⟩,
  ⟨112, 269, 0, 245, 469, 224⟩,
  ⟨255, 757, 0, 636, 1284, 648⟩,
  ⟨83, 273, 1, 185, 356, 171⟩,
  ⟨477, 1085, 1, 1051, 2029, 978⟩,
  ⟨442, 1087, 1, 1016, 1994, 978⟩,
  ⟨178, 441, 1, 390, 749, 359⟩,
  ⟨187, 443, 1, 437, 861, 424⟩,
  ⟨106, 283, 1, 260, 520, 260⟩,
  ⟨168, 447, 1, 380, 739, 359⟩,
  ⟨191, 449, 1, 441, 865, 424⟩,
  ⟨167, 451, 1, 379, 738, 359⟩,
  ⟨256, 777, 0, 637, 1285, 648⟩,
  ⟨183, 455, 1, 433, 857, 424⟩,
  ⟨177, 457, 1, 389, 748, 359⟩,
  ⟨357, 945, 0, 838, 1657, 819⟩,
  ⟨181, 461, 1, 431, 855, 424⟩,
  ⟨18, 139, 1, 34, 58, 24⟩,
  ⟨373, 951, 0, 854, 1673, 819⟩,
  ⟨203, 467, 1, 453, 877, 424⟩,
  ⟨9, 145, 0, 12, 14, 2⟩,
  ⟨740, 1929, 0, 1799, 3606, 1807⟩,
  ⟨647, 1607, 0, 1558, 3112, 1554⟩,
  ⟨16, 151, 1, 32, 56, 24⟩,
  ⟨172, 477, 1, 384, 743, 359⟩,
  ⟨82, 317, 1, 184, 355, 171⟩,
  ⟨174, 481, 1, 424, 848, 424⟩,
  ⟨279, 645, 1, 591, 1121, 530⟩,
  ⟨485, 1133, 1, 1059, 2037, 978⟩]

private def Row.clock (r : Row) := r.start+r.shift+r.delta
private def Row.parent (r : Row) := (2^r.clock-15-2^(r.gap+2))/81

private def Checked (i : Nat) (r : Row) : Prop :=
  r.start%162=2*i+1 ∧ r.start≤2127 ∧ r.shift≤1 ∧ r.shift+r.delta≤2081 ∧
  4≤r.clock ∧ r.lowerClocks≤r.clock ∧ r.gap+3≤r.clock ∧
  r.clock-r.lowerClocks+r.grade=r.start+r.shift ∧
  r.parent<2^r.clock ∧ r.parent%48=17 ∧
  stride r.lowerClocks r.parent 0=(2^(r.clock-r.lowerClocks)*3^r.grade-1,r.grade+4) ∧
  stride (r.gap+3) (3*r.parent) 0=(2^(r.clock-(r.gap+3)),3)

private instance (i : Nat) (r : Row) : Decidable (Checked i r) := by
  unfold Checked; infer_instance

private def rowTest (i : Nat) := decide (Checked i rows[i]!)

private theorem block0 : segment rowTest 9 0=true := by decide +kernel
private theorem block1 : segment rowTest 9 9=true := by decide +kernel
private theorem block2 : segment rowTest 9 18=true := by decide +kernel
private theorem block3 : segment rowTest 9 27=true := by decide +kernel
private theorem block4 : segment rowTest 9 36=true := by decide +kernel
private theorem block5 : segment rowTest 9 45=true := by decide +kernel
private theorem block6 : segment rowTest 9 54=true := by decide +kernel
private theorem block7 : segment rowTest 9 63=true := by decide +kernel
private theorem block8 : segment rowTest 9 72=true := by decide +kernel
private theorem allRows : segment rowTest 81 0=true :=
  @segment_join rowTest 27 54 0
    (@segment_join rowTest 9 18 0 block0 (@segment_join rowTest 9 9 9 block1 block2))
    (@segment_join rowTest 27 27 27
      (@segment_join rowTest 9 18 27 block3 (@segment_join rowTest 9 9 36 block4 block5))
      (@segment_join rowTest 9 18 54 block6 (@segment_join rowTest 9 9 63 block7 block8)))

private def earlyClocks : Array Nat := #[
  0, 11, 67, 31, 41, 0, 102, 85, 144, 116, 194, 299, 282, 246, 286, 288,
  336, 338, 340, 342, 344, 376, 378, 0, 0, 384, 543, 388, 547, 549, 551, 553,
  550, 473, 597, 599, 601, 687, 0, 607, 918, 920, 922, 867, 926, 928, 930, 932,
  0, 936, 938, 921, 923, 925, 946, 948, 1053, 1055, 935, 956, 939, 941, 1065, 1067,
  1069, 1274, 1035, 1037, 1039, 0, 1257, 1286, 0, 1290, 1292, 0, 1296, 1298, 1300, 1302,
  1304, 1306, 1308, 1310, 1312, 1314, 0, 1318, 1320, 0, 1335, 1326, 1328, 1341, 1343, 1345,
  1897, 1899, 1749, 1751, 1905, 1357, 1909, 1911, 0, 0, 1917, 1919, 1921, 1923, 1941, 1943,
  1929, 1947, 1933, 1935, 1937, 1939, 1941, 0, 1945, 1947, 1949, 1951, 0, 1955, 1957, 1959,
  0, 0, 1965, 1967, 1969, 1971, 0, 1975, 0, 1979, 2241, 2243, 2692, 0, 2249, 2251,
  2700, 2702, 2257, 2259, 2261, 3111, 0, 3115, 3117, 0, 3121, 3123, 0, 3127, 0, 3131,
  3133, 3135, 3137, 3139, 3141, 0, 3145, 0, 0, 3151, 0, 0, 3157, 3159, 0, 3163,
  3165, 3167, 3169, 3171, 3173, 3140, 3142, 3144, 3146, 0, 0, 3152, 0, 0, 0, 3160,
  0, 0, 0, 3168, 3170, 0, 0, 0, 0, 3180, 3610, 3184, 3614, 0, 3618, 3620,
  0, 0, 0, 0, 0, 3632, 3634, 0, 3638, 0, 3642, 3644, 0, 0, 0, 0,
  0, 0, 3983, 0, 0, 3989, 0, 0, 3995, 0, 0, 4302, 4003, 0, 0, 0,
  0, 4314, 4316, 4318, 4320, 0, 0, 4326, 0, 0, 4332, 0, 0, 4449, 4451, 0,
  0, 4457, 4348, 4350, 0, 4465, 4467, 0, 4471, 4473, 0, 0, 4479, 0, 0, 0,
  4850, 0, 0, 0, 0, 4860, 0, 0, 0, 0, 4870, 4872, 4874, 4876, 0, 4880,
  0, 0, 0, 0, 0, 0, 4894, 4896, 0, 4900, 0, 5435, 5437, 0, 0, 0,
  0, 0, 0, 5451, 0, 0, 5823, 0, 0, 5829, 0, 0, 5098, 5100, 0, 0,
  0, 0, 0, 5719, 5721, 0, 0, 0, 5729, 0, 0, 0, 0, 0, 5741, 5743,
  0, 0, 5749, 5881, 0, 0, 5887, 0, 0, 5893, 5895, 0, 0, 5901, 0, 0,
  0, 5909, 0, 0, 0, 0, 6087, 0, 0, 0, 0, 0, 6099, 6101, 6103, 0,
  6107, 0, 0, 0, 0, 0, 0, 0, 6123, 0, 0, 0, 6131, 6133, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 6749, 0, 0, 6755, 0, 0, 6761, 6763, 0,
  0, 0, 0, 0, 6775, 6777, 0, 0, 0, 7129, 0, 0, 0, 0, 0, 7141,
  0, 0, 0, 7393, 7395, 0, 0, 7401, 0, 0, 7407, 7409, 0, 0, 7171, 0,
  0, 0, 7710, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7201, 7734, 7736,
  0, 7740, 0, 0, 0, 0, 0, 0, 0, 7756, 0, 0, 0, 7764, 7766, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7798, 7800,
  0, 0, 0, 0, 0, 7812, 7814, 0, 0, 0, 7822, 0, 0, 0, 0, 0,
  7834, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9135, 9137, 0, 0, 9143,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9097, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9121, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9873,
  9875, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10084, 0, 0, 0, 0,
  0, 10096, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9931, 10120, 0, 0,
  9939, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10156,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10180, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  10978, 10980, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11002, 0, 0, 0,
  0, 0, 11014, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12052, 12436, 0,
  0, 11044, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  12472, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12496, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 12538, 12540, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13112, 0, 0,
  0, 0, 0, 12574, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12596, 12598,
  0, 0, 12604, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 13184, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14338, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 14380, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14404, 0,
  0, 0, 0, 0, 14416, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  14440, 0, 0, 14446, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 14476, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14928, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 15371, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15395,
  0, 0, 0, 0, 0, 15808, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 17539]

private def earlyTest (a : Nat) : Bool :=
  let t := 2*a+1
  let row := rows[a%81]!
  if row.start≤t then true else (stride (earlyClocks[a]?.getD 0) (M t) 0).1==1

private theorem early0 : segment earlyTest 32 0=true := by decide +kernel
private theorem early1 : segment earlyTest 32 32=true := by decide +kernel
private theorem early2 : segment earlyTest 32 64=true := by decide +kernel
private theorem early3 : segment earlyTest 32 96=true := by decide +kernel
private theorem early4 : segment earlyTest 32 128=true := by decide +kernel
private theorem early5 : segment earlyTest 32 160=true := by decide +kernel
private theorem early6 : segment earlyTest 32 192=true := by decide +kernel
private theorem early7 : segment earlyTest 32 224=true := by decide +kernel
private theorem early8 : segment earlyTest 32 256=true := by decide +kernel
private theorem early9 : segment earlyTest 32 288=true := by decide +kernel
private theorem early10 : segment earlyTest 32 320=true := by decide +kernel
private theorem early11 : segment earlyTest 32 352=true := by decide +kernel
private theorem early12 : segment earlyTest 32 384=true := by decide +kernel
private theorem early13 : segment earlyTest 32 416=true := by decide +kernel
private theorem early14 : segment earlyTest 32 448=true := by decide +kernel
private theorem early15 : segment earlyTest 32 480=true := by decide +kernel
private theorem early16 : segment earlyTest 32 512=true := by decide +kernel
private theorem early17 : segment earlyTest 32 544=true := by decide +kernel
private theorem early18 : segment earlyTest 32 576=true := by decide +kernel
private theorem early19 : segment earlyTest 32 608=true := by decide +kernel
private theorem early20 : segment earlyTest 32 640=true := by decide +kernel
private theorem early21 : segment earlyTest 32 672=true := by decide +kernel
private theorem early22 : segment earlyTest 32 704=true := by decide +kernel
private theorem early23 : segment earlyTest 32 736=true := by decide +kernel
private theorem early24 : segment earlyTest 32 768=true := by decide +kernel
private theorem early25 : segment earlyTest 32 800=true := by decide +kernel
private theorem early26 : segment earlyTest 32 832=true := by decide +kernel
private theorem early27 : segment earlyTest 32 864=true := by decide +kernel
private theorem early28 : segment earlyTest 32 896=true := by decide +kernel
private theorem early29 : segment earlyTest 32 928=true := by decide +kernel
private theorem early30 : segment earlyTest 32 960=true := by decide +kernel
private theorem early31 : segment earlyTest 32 992=true := by decide +kernel
private theorem early32 : segment earlyTest 32 1024=true := by decide +kernel
private theorem early33 : segment earlyTest 32 1056=true := by decide +kernel
private theorem allEarly : segment earlyTest 1088 0=true :=
  (@segment_join earlyTest 544 544 0 (@segment_join earlyTest 256 288 0 (@segment_join earlyTest 128 128 0 (@segment_join earlyTest 64 64 0 (@segment_join earlyTest 32 32 0 early0 early1) (@segment_join earlyTest 32 32 64 early2 early3)) (@segment_join earlyTest 64 64 128 (@segment_join earlyTest 32 32 128 early4 early5) (@segment_join earlyTest 32 32 192 early6 early7))) (@segment_join earlyTest 128 160 256 (@segment_join earlyTest 64 64 256 (@segment_join earlyTest 32 32 256 early8 early9) (@segment_join earlyTest 32 32 320 early10 early11)) (@segment_join earlyTest 64 96 384 (@segment_join earlyTest 32 32 384 early12 early13) (@segment_join earlyTest 32 64 448 early14 (@segment_join earlyTest 32 32 480 early15 early16))))) (@segment_join earlyTest 256 288 544 (@segment_join earlyTest 128 128 544 (@segment_join earlyTest 64 64 544 (@segment_join earlyTest 32 32 544 early17 early18) (@segment_join earlyTest 32 32 608 early19 early20)) (@segment_join earlyTest 64 64 672 (@segment_join earlyTest 32 32 672 early21 early22) (@segment_join earlyTest 32 32 736 early23 early24))) (@segment_join earlyTest 128 160 800 (@segment_join earlyTest 64 64 800 (@segment_join earlyTest 32 32 800 early25 early26) (@segment_join earlyTest 32 32 864 early27 early28)) (@segment_join earlyTest 64 96 928 (@segment_join earlyTest 32 32 928 early29 early30) (@segment_join earlyTest 32 64 992 early31 (@segment_join earlyTest 32 32 1024 early32 early33))))))

def clockCharge (t : Nat) : Nat :=
  let r := rows[((t-1)/2)%81]!
  r.shift+r.delta

theorem charge_bound (t : Nat) : clockCharge t≤2081 := by
  let i := ((t-1)/2)%81
  have idx : i<81 := Nat.mod_lt _ (by decide)
  have ck : Checked i rows[i]! := of_decide_eq_true (segment_sound allRows (Nat.zero_le i) idx)
  exact ck.2.2.2.1

private theorem odd_representative (a : Nat) :
    ∃ H Y, H≤max 18 ((2*a+1)+clockCharge (2*a+1)) ∧ Representative (2*a+1) H Y := by
  let i := a%81
  let r := rows[i]!
  have idx : i<81 := Nat.mod_lt _ (by decide)
  have ck : Checked i r := of_decide_eq_true (segment_sound allRows (Nat.zero_le i) idx)
  obtain ⟨res,start,shift,delta,clock,lowClk,upClk,base,small,canonical,low,up⟩ := ck
  have residue : (2*a+1)%162=2*i+1 := by dsimp only [i]; omega
  by_cases late : r.start≤2*a+1
  · let j := (2*a+1-r.start)/162
    have rep : r.start+162*j=2*a+1 := by dsimp only [j]; omega
    rw [stride_eq] at low up
    obtain ⟨y,hy⟩ := extend_row small canonical clock (Nat.add_sub_of_le lowClk)
      (Nat.add_sub_of_le upClk) base low up j
    have charge : clockCharge (2*a+1)=r.shift+r.delta := by
      simp only [clockCharge,show (2*a+1-1)/2=a by omega]; rfl
    have bound : r.clock+162*j≤max 18 (2*a+1+clockCharge (2*a+1)) := by
      rw [charge]; dsimp only [Row.clock]; omega
    have join : Meets (M (r.start+r.shift+162*j)) (M (2*a+1)) := by
      by_cases s : r.shift=0
      · rw [s,Nat.add_zero,rep]; exact ⟨0,0,rfl⟩
      · rw [show r.start+r.shift+162*j=2*a+2 by omega]
        exact (neighbors a).symm
    exact ⟨_,y,bound,hy.1,hy.2.1,hy.2.2.1,hy.2.2.2.trans join⟩
  · have lim : a<1088 := by omega
    have test := segment_sound allEarly (Nat.zero_le a) lim
    have ht : (stride (earlyClocks[a]?.getD 0) (M (2*a+1)) 0).1=1 := by
      change (if r.start≤2*a+1 then true else ((stride (earlyClocks[a]?.getD 0) (M (2*a+1)) 0).1==1))=true at test
      simpa [late] using test
    have reached : run (earlyClocks[a]?.getD 0) (M (2*a+1))=1 := by
      rwa [stride_eq,track_run] at ht
    have baseHit : track 18 (3*3233) 0=(1,3) := by decide +kernel
    have baseLow : run 107 3233=1 := by decide +kernel
    exact ⟨18,3233,by omega,by decide,by decide,baseHit,107,_,baseLow.trans reached.symm⟩

/-- Every positive Mersenne exponent has a canonical representative whose
    triple hits one in exactly three odd departures at the stated clock bound. -/
theorem priced_representative (t : Nat) (positive : 0<t) :
    ∃ H Y, H≤max 18 (t+clockCharge t) ∧ Representative t H Y := by
  let a := (t-1)/2
  obtain ⟨H,Y,b,hy⟩ := odd_representative a
  by_cases same : t=2*a+1
  · rw [same]; exact ⟨H,Y,b,hy⟩
  · have even : t=2*a+2 := by dsimp only [a] at *; omega
    rw [even]
    have cost : clockCharge (2*a+1)=clockCharge (2*a+2) := by
      simp only [clockCharge,show (2*a+1-1)/2=a by omega,show (2*a+2-1)/2=a by omega]
    exact ⟨H,Y,by rw [cost] at b; omega,hy.1,hy.2.1,hy.2.2.1,hy.2.2.2.trans (neighbors a)⟩

theorem mersenne_representative (t : Nat) (positive : 0<t) :
    ∃ H Y, H≤t+2081 ∧ Representative t H Y := by
  obtain ⟨H,Y,b,hy⟩ := priced_representative t positive
  have bound := charge_bound t
  exact ⟨H,Y,by omega,hy⟩

#print axioms mersenne_representative

/-- A specified bad Mersenne would give a bad canonical lower source with a
    witnessed three-odd upper, without assumptions on any other component. -/
theorem bad_mersenne_witness {t : Nat} (positive : 0<t) (bad : ¬ReachesOne (M t)) :
    ∃ H Y, H≤t+2081 ∧ Representative t H Y ∧ ¬ReachesOne Y := by
  obtain ⟨H,Y,cost,hy⟩ := mersenne_representative t positive
  exact ⟨H,Y,cost,hy,fun hit => bad (reaches_of_meets hit hy.2.2.2.symm)⟩

#print axioms bad_mersenne_witness

end Collatz.Itinerary.ReturnDescent
