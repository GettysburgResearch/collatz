import NestedCharts

/-! All hard original parents in the entire 3^11 divisibility ball.
Each terminal query chain is over the same ordinary original z. -/
set_option autoImplicit false
set_option warningAsError true
namespace NestedCover
open CoreBranching FloorCounting PeakRigidity ValuationCharts
open NestedCharts (Plan initial)
open EarlierOffsets (Good)

def trie : Atlas Plan :=
(.fork
  (.fork
    (.fork
      (.leaf (.query ⟨17,25,1986909805,32,16⟩ ⟨0,7,18⟩ .finish))
      (.leaf (.query ⟨17,26,2036717165,37,20⟩ ⟨4,11,16⟩ .finish))
      (.fork
        (.leaf (.query ⟨18,29,31403136391,36,17⟩ ⟨0,7,18⟩ .finish))
        (.leaf (.query ⟨18,27,6010536775,36,21⟩ ⟨4,9,12⟩ (.query ⟨15,26,460575477,24,10⟩ ⟨0,7,18⟩ .finish)))
        (.leaf (.query ⟨18,26,5910922055,33,18⟩ ⟨1,7,16⟩ .finish))))
    (.leaf (.query ⟨16,25,695508175,29,15⟩ ⟨0,4,16⟩ (.query ⟨4,10,1391,11,6⟩ ⟨3,5,0⟩ (.query ⟨14,23,158778279,22,10⟩ ⟨0,4,17⟩ .finish))))
    (.leaf (.query ⟨16,24,670604495,37,20⟩ ⟨5,13,16⟩ .finish)))
  (.fork
    (.fork
      (.fork
        (.leaf (.query ⟨18,29,13954865479,33,17⟩ ⟨0,4,17⟩ .finish))
        (.leaf (.query ⟨18,28,9883086407,34,18⟩ ⟨1,6,16⟩ .finish))
        (.fork
          (.leaf (.query ⟨19,29,25577480149,36,18⟩ ⟨0,7,18⟩ .finish))
          (.leaf (.query ⟨19,30,33721038293,37,18⟩ ⟨0,7,18⟩ .finish))
          (.fork
            (.fork
              (.leaf (.query ⟨21,32,222053763197,39,20⟩ ⟨0,7,18⟩ .finish))
              (.fork
                (.leaf (.query ⟨22,32,535864359287,43,21⟩ ⟨0,11,18⟩ .finish))
                (.leaf (.query ⟨22,35,3000291430327,42,21⟩ ⟨0,7,18⟩ .finish))
                (.leaf (.query ⟨22,33,601012824439,40,21⟩ ⟨0,7,18⟩ .finish)))
              (.leaf (.query ⟨21,31,189479530621,38,21⟩ ⟨1,7,16⟩ .finish)))
            (.leaf (.query ⟨20,31,84875998591,40,24⟩ ⟨5,9,0⟩ (.query ⟨2,4,279,12,5⟩ ⟨9,17,12⟩ (.query ⟨15,27,1163481813,30,14⟩ ⟨9,20,16⟩ .finish))))
            (.leaf (.query ⟨20,30,68588882303,41,19⟩ ⟨0,11,18⟩ .finish)))))
      (.leaf (.query ⟨17,27,3972991981,38,20⟩ ⟨4,11,16⟩ .finish))
      (.leaf (.query ⟨17,26,2955047213,35,20⟩ ⟨4,9,12⟩ (.query ⟨15,26,460575477,24,10⟩ ⟨0,7,18⟩ .finish))))
    (.leaf (.query ⟨16,26,974898047,36,19⟩ ⟨4,10,16⟩ .finish))
    (.leaf (.query ⟨16,22,192761711,29,15⟩ ⟨0,7,18⟩ .finish)))
  (.leaf (.query ⟨15,24,240137285,34,18⟩ ⟨4,10,16⟩ .finish)))

set_option maxHeartbeats 0 in
set_option maxRecDepth 16000 in
theorem checked : checkWith (fun p => NestedCharts.check p initial) trie 3221021 14348907=true := by
  decide +kernel

theorem address (j z : ℕ) (parent : 81*z+271=128*2^(173+162*j))
    (divisible : 3^11 ∣ z+1) : ∃ v, 2^(73+162*j)=3221021+14348907*v := by
  obtain ⟨b,hb⟩:=divisible
  rw [ValuationAddress.power] at parent
  exact ⟨2^(73+162*j)/14348907,ValuationAddress.root z _ b (3^11) 8097653
    91569296518118772371157040027069 107 3221021 parent hb (by decide +kernel) (by decide +kernel) (by decide +kernel)⟩

/-- Every original parameter on this ball gets a finite checked physical plan. -/
theorem plan_exists (j z : ℕ) (parent : 81*z+271=128*2^(173+162*j))
    (divisible : 3^11 ∣ z+1) :
    ∃ p x s t, NestedCharts.check p initial x s=true ∧ 2^(73+162*j)=x+s*t := by
  obtain ⟨v,hv⟩:=address j z parent divisible
  obtain ⟨p,x,s,t,ok,e⟩:=selectWith _ trie 3221021 14348907 v checked
  exact ⟨p,x,s,t,ok,hv.trans e⟩

theorem good_parent (j z : ℕ) (parent : 81*z+271=128*2^(173+162*j))
    (divisible : 3^11 ∣ z+1)
    (floor : ∀ y, 0<y → 2^40*y<z → Good y)
    (canonical : ∀ w, 0<w → w<z → w%48=17 → Good (3*w) → Good w) : Good z := by
  obtain ⟨p,x,s,t,ok,e⟩:=plan_exists j z parent divisible
  have g := NestedCharts.sound p initial x s t j z ok e parent floor canonical
  rw [←e] at g
  exact NestedCharts.original z j parent g

#print axioms checked
#print axioms address
#print axioms plan_exists
#print axioms good_parent
end NestedCover
