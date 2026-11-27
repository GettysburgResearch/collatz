import ValuationCharts
import ValuationAddress

/-! A complete finite ternary tree for all hard parents with 3^12 | z+1.
The root address is the least X=2^(m-100) with 2^106 X=95 mod 3^16. -/
set_option autoImplicit false
set_option warningAsError true
namespace ValuationCover
open CoreBranching FloorCounting PeakRigidity ValuationCharts
open EarlierOffsets (Good)

def trie : Tree :=
(.fork
  (.fork
    (.leaf ⟨17,8,1986909805,32,16,2⟩)
    (.leaf ⟨17,9,2036717165,37,20,0⟩)
    (.fork
      (.leaf ⟨18,11,31403136391,36,17,2⟩)
      (.fork
        (.leaf ⟨19,7,5136081077,33,18,2⟩)
        (.fork
          (.leaf ⟨20,11,272444910895,41,21,0⟩)
          (.leaf ⟨20,10,78690512831,37,19,2⟩)
          (.leaf ⟨20,12,381010954943,39,19,2⟩))
        (.fork
          (.fork
            (.leaf ⟨21,12,628361841181,40,20,2⟩)
            (.leaf ⟨21,9,90313127501,37,20,2⟩)
            (.fork
              (.fork
                (.leaf ⟨23,14,6947064557605,44,22,2⟩)
                (.leaf ⟨23,11,4363448583653,45,24,0⟩)
                (.leaf ⟨23,13,5685896981237,43,23,0⟩))
              (.leaf ⟨22,12,1413628980407,41,22,0⟩)
              (.leaf ⟨22,11,1444269391015,60,27,2⟩)))
          (.leaf ⟨20,8,21706585775,35,19,2⟩)
          (.fork
            (.fork
              (.leaf ⟨22,11,2169520546423,44,23,0⟩)
              (.leaf ⟨22,9,393320103463,38,21,2⟩)
              (.leaf ⟨22,12,1357840429991,41,21,2⟩))
            (.leaf ⟨21,11,336845019197,39,20,2⟩)
            (.leaf ⟨21,8,95714937565,36,20,2⟩))))
      (.leaf ⟨18,8,5910922055,33,18,0⟩)))
  (.fork
    (.leaf ⟨17,7,584511053,28,16,1⟩)
    (.fork
      (.fork
        (.fork
          (.fork
            (.leaf ⟨21,12,753713892733,40,21,0⟩)
            (.leaf ⟨21,12,586348241485,40,20,2⟩)
            (.fork
              (.leaf ⟨22,13,2857950272887,46,21,2⟩)
              (.leaf ⟨22,12,1664333083511,40,21,0⟩)
              (.fork
                (.fork
                  (.leaf ⟨24,12,9010911804719,57,32,0⟩)
                  (.fork
                    (.leaf ⟨25,15,143327300266061,47,24,2⟩)
                    (.leaf ⟨25,12,22258266656653,50,28,0⟩)
                    (.fork
                      (.leaf ⟨26,11,20563689437767,44,25,2⟩)
                      (.fork
                        (.leaf ⟨27,12,84796623579397,46,26,2⟩)
                        (.leaf ⟨27,15,609742611270293,49,26,2⟩)
                        (.leaf ⟨27,16,861082140746197,49,26,0⟩))
                      (.fork
                        (.fork
                          (.leaf ⟨28,15,2391285369400255,50,27,2⟩)
                          (.leaf ⟨28,15,927170652282751,50,27,2⟩)
                          (.fork
                            (.leaf ⟨29,16,3731559401585965,52,28,2⟩)
                            (.leaf ⟨29,16,9221989590776605,52,28,2⟩)
                            (.leaf ⟨29,15,5125722625624925,72,30,2⟩)))
                        (.leaf ⟨27,16,1430460086291893,50,26,2⟩)
                        (.leaf ⟨27,14,321393433519285,48,26,2⟩))))
                  (.leaf ⟨24,13,13785380562223,44,24,0⟩))
                (.leaf ⟨23,12,3799382061157,42,22,2⟩)
                (.leaf ⟨23,14,9454794336181,44,22,2⟩))))
          (.leaf ⟨20,11,201503914687,38,19,2⟩)
          (.leaf ⟨20,11,145715364271,38,19,2⟩))
        (.leaf ⟨19,8,12811918693,34,18,2⟩)
        (.leaf ⟨19,10,36138275701,36,18,2⟩))
      (.fork
        (.leaf ⟨19,10,48535731349,40,18,2⟩)
        (.leaf ⟨19,11,79637540693,37,18,2⟩)
        (.fork
          (.leaf ⟨20,11,176709003391,38,19,2⟩)
          (.leaf ⟨20,12,301116240767,39,19,2⟩)
          (.fork
            (.fork
              (.leaf ⟨22,11,968344843639,60,27,2⟩)
              (.leaf ⟨22,12,1465973793143,40,21,0⟩)
              (.fork
                (.leaf ⟨23,11,2407405581413,45,22,2⟩)
                (.fork
                  (.fork
                    (.fork
                      (.fork
                        (.leaf ⟨27,16,1392164345795221,50,26,2⟩)
                        (.leaf ⟨27,13,182599340395013,47,26,2⟩)
                        (.leaf ⟨27,13,304608900154805,68,28,2⟩))
                      (.leaf ⟨26,12,45014368641671,45,25,2⟩)
                      (.leaf ⟨26,10,19514656102487,49,29,0⟩))
                    (.leaf ⟨25,9,4666841873261,47,28,0⟩)
                    (.fork
                      (.fork
                        (.leaf ⟨27,15,1146416068816565,49,26,2⟩)
                        (.fork
                          (.leaf ⟨28,17,8599408739158495,56,29,0⟩)
                          (.leaf ⟨28,17,4939121946364735,51,27,0⟩)
                          (.leaf ⟨28,17,6769265342761615,54,28,0⟩))
                        (.leaf ⟨27,16,2178448175358325,70,32,2⟩))
                      (.leaf ⟨26,13,106127220862759,52,29,0⟩)
                      (.leaf ⟨26,12,72127604143847,45,25,2⟩)))
                  (.fork
                    (.fork
                      (.leaf ⟨26,15,563181785863207,63,34,0⟩)
                      (.leaf ⟨26,10,24033528686183,64,27,2⟩)
                      (.leaf ⟨26,13,88051730527975,46,25,2⟩))
                    (.leaf ⟨25,10,5662099772269,42,24,2⟩)
                    (.leaf ⟨25,15,193896521854253,53,28,0⟩))
                  (.fork
                    (.fork
                      (.fork
                        (.leaf ⟨27,16,881531743837573,50,26,2⟩)
                        (.leaf ⟨27,14,458682857365237,52,26,2⟩)
                        (.leaf ⟨27,13,286533409820021,47,26,2⟩))
                      (.leaf ⟨26,9,13005267720775,63,27,2⟩)
                      (.leaf ⟨26,13,83532857944279,46,25,2⟩))
                    (.leaf ⟨25,14,98784052914253,50,24,2⟩)
                    (.leaf ⟨25,12,20671392333709,44,24,2⟩)))
                (.leaf ⟨23,12,3402663480421,42,22,2⟩)))
            (.fork
              (.fork
                (.leaf ⟨23,13,6062641883429,43,23,0⟩)
                (.leaf ⟨23,10,1240314026917,40,22,2⟩)
                (.fork
                  (.fork
                    (.leaf ⟨25,14,66482482223389,45,24,0⟩)
                    (.leaf ⟨25,14,52925864472301,46,24,2⟩)
                    (.leaf ⟨25,14,80039099974477,46,24,2⟩))
                  (.leaf ⟨24,11,5055399286495,42,23,2⟩)
                  (.leaf ⟨24,13,16550013171727,43,23,0⟩)))
              (.fork
                (.leaf ⟨23,13,6564738837173,43,22,2⟩)
                (.fork
                  (.leaf ⟨24,14,42922298001071,45,23,2⟩)
                  (.fork
                    (.leaf ⟨25,15,140339513454893,50,26,0⟩)
                    (.leaf ⟨25,14,90081039049357,66,30,2⟩)
                    (.leaf ⟨25,15,86113042450541,47,24,2⟩))
                  (.fork
                    (.leaf ⟨25,15,171971621540765,47,24,2⟩)
                    (.leaf ⟨25,11,13343047712717,64,26,2⟩)
                    (.leaf ⟨25,14,72005548714573,46,24,2⟩)))
                (.leaf ⟨23,14,11717329991941,43,22,0⟩))
              (.leaf ⟨22,12,1633339444391,41,21,2⟩))
            (.leaf ⟨21,11,405719772797,39,20,2⟩))))
      (.leaf ⟨18,7,3106124551,32,17,2⟩))
    (.fork
      (.fork
        (.leaf ⟨19,8,10745676085,34,18,2⟩)
        (.fork
          (.fork
            (.leaf ⟨21,12,695859099709,40,21,0⟩)
            (.fork
              (.fork
                (.leaf ⟨23,13,9071091120677,57,31,0⟩)
                (.leaf ⟨23,14,9198580252789,44,23,0⟩)
                (.fork
                  (.leaf ⟨24,14,49935125412623,51,27,0⟩)
                  (.fork
                    (.leaf ⟨25,13,71964629258141,45,24,2⟩)
                    (.leaf ⟨25,14,104106693872461,50,24,2⟩)
                    (.fork
                      (.fork
                        (.fork
                          (.leaf ⟨28,14,1833501398731871,49,27,2⟩)
                          (.leaf ⟨28,16,5572492575895487,55,27,2⟩)
                          (.leaf ⟨28,15,3323850910639327,53,28,0⟩))
                        (.leaf ⟨27,15,1116695235143093,69,32,2⟩)
                        (.leaf ⟨27,14,737549158468741,48,26,2⟩))
                      (.leaf ⟨26,15,417274064099287,52,25,2⟩)
                      (.leaf ⟨26,13,183751823160103,46,25,2⟩)))
                  (.leaf ⟨24,12,17920549930415,43,23,2⟩)))
              (.leaf ⟨22,13,4300187613271,42,21,2⟩)
              (.leaf ⟨22,10,572827143719,39,21,2⟩))
            (.leaf ⟨21,9,140591697629,37,20,2⟩))
          (.leaf ⟨20,9,44144965807,36,19,2⟩)
          (.leaf ⟨20,12,321778666847,39,19,2⟩))
        (.leaf ⟨19,11,38312688533,37,18,2⟩))
      (.leaf ⟨18,11,16250690599,40,21,0⟩)
      (.leaf ⟨18,8,2467184375,30,17,1⟩)))
  (.leaf ⟨16,8,670604495,37,20,0⟩))

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
theorem checked : check trie 3221021 43046721=true := by decide +kernel

/-- The affine parent and divisibility pick the tree's ordinary root address. -/
theorem address (j z : ℕ) (parent : 81*z+271=128*2^(173+162*j))
    (divisible : 3^12 ∣ z+1) : ∃ v, 2^(73+162*j)=3221021+43046721*v := by
  obtain ⟨b,hb⟩:=divisible
  rw [ValuationAddress.power] at parent
  exact ⟨2^(73+162*j)/43046721,ValuationAddress.root z _ b (3^12) 22446560
    84609524449110711920911683438399 99 3221021 parent hb
    (by decide +kernel) (by decide +kernel) (by decide +kernel)⟩

/-- A smaller positive canonical ordinary source with both fully charged
prefixes exists at every parameter of the ternary ball. -/
theorem witnesses (j z : ℕ) (parent : 81*z+271=128*2^(173+162*j))
    (divisible : 3^12 ∣ z+1) :
    ∃ r x s t, Valid r x s ∧ 2^(73+162*j)=x+s*t ∧
    ∃ w, 0<w ∧ w<z ∧ w%48=17 ∧
      run (lower r) w+1=2^(173+162*j) ∧ grade (lower r) w=r.rank ∧
      run r.upper (3*w)+1=factor r*2^(73+162*j)+r.sign ∧ grade r.upper (3*w)=r.upperOdds := by
  obtain ⟨v,hv⟩:=address j z parent divisible
  obtain ⟨r,x,s,t,ok,e⟩:=select trie 3221021 43046721 v checked
  have ex := hv.trans e
  have p : 2^(173+162*j)=2^100*(x+s*t) := by rw [←ex,←pow_add]; congr 1; omega
  have cp : 81*z+271=128*2^100*(x+s*t) := by rw [parent,p,mul_assoc]
  have hit:=physical r x s t z ok cp
  rw [←p,←ex] at hit
  exact ⟨r,x,s,t,ok,ex,_,hit⟩

/-- All parameters, including both terminal ternary units and every higher
digit, are paid under the original two leastness consequences. -/
theorem good_parent (j z : ℕ) (parent : 81*z+271=128*2^(173+162*j))
    (divisible : 3^12 ∣ z+1)
    (floor : ∀ y, 0<y → 2^40*y<z → Good y)
    (canonical : ∀ w, 0<w → w<z → w%48=17 → Good (3*w) → Good w) : Good z := by
  obtain ⟨v,hv⟩:=address j z parent divisible
  obtain ⟨r,x,s,t,ok,e⟩:=select trie 3221021 43046721 v checked
  exact row_good r x s t j z ok (hv.trans e) parent floor canonical

#print axioms checked
#print axioms address
#print axioms witnesses
#print axioms good_parent
end ValuationCover
