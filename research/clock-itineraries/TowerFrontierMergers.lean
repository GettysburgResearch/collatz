module

public import TowerFrontierAffine
public import TowerFrontierRotation
import all TowerFrontierAffine

public section

namespace Collatz.Itinerary.TowerFrontier

set_option autoImplicit false
set_option maxRecDepth 8192
set_option maxHeartbeats 2000000
set_option exponentiation.threshold 4096

private def one : Nat := 9991805063649597943951053240468339918574750218820607212730515351651262797958421271804088988674643987067945216580822231506672207592177974410818888469816721902891851208982589713121313858620359985505539337994794894071164897818758395238584049908575398610923558532719558360995616760277329398678979931799372673555324372353643274766389048398504095497653268960727194618015773638347904771644515238157303746360016156241883713
private def five : Nat := 41455595233580214879749619731508581338531941976990846039131725140747278862236802629022019820254823975400138460628783616545047617419142196105728369698381356642082545820548534053527142464892210968601473768740698640276389076769966901293602192571117795621547616839401348992703775857081304909866348571505554570094641082520904857378061467568651342655284962085988608624248536998966461854174905305463901017552700249447300357
private def endOne : Nat := 150400075942300172936097774623913892041888905149338411439747499754068162036237639762177691253276284454475036442382720403241470588599756168499243777058644374900516795711122085346707459058276008937837472135056528727668558317017988103113930301837534968310093537800292771055668259893611563761233550644855435262489119841
private def endFive : Nat := 23111253122475083979797589856653873193078577424845952040070081741182808080989909474624720704891103217580091344690574733538593150404906013472927774421624452039997444506838433339154636745037865363001146086799432129945657434614854703863967549202673300251611713223554936492302490412505952802611642523259259867797855997

private def agrees (w c e r : Nat) : Bool := stride 1381 (3^r*w) r == (c,e)

private theorem one_cert_0 : segment (agrees one endOne 660) 24 0 = true := by decide +kernel
private theorem one_cert_24 : segment (agrees one endOne 660) 24 24 = true := by decide +kernel
private theorem one_cert_48 : segment (agrees one endOne 660) 24 48 = true := by decide +kernel
private theorem one_cert_72 : segment (agrees one endOne 660) 24 72 = true := by decide +kernel
private theorem one_cert_96 : segment (agrees one endOne 660) 24 96 = true := by decide +kernel
private theorem one_cert_120 : segment (agrees one endOne 660) 24 120 = true := by decide +kernel
private theorem one_cert_144 : segment (agrees one endOne 660) 24 144 = true := by decide +kernel
private theorem one_cert_168 : segment (agrees one endOne 660) 24 168 = true := by decide +kernel
private theorem one_cert_192 : segment (agrees one endOne 660) 24 192 = true := by decide +kernel
private theorem one_cert_216 : segment (agrees one endOne 660) 24 216 = true := by decide +kernel
private theorem one_cert_240 : segment (agrees one endOne 660) 24 240 = true := by decide +kernel
private theorem one_cert_264 : segment (agrees one endOne 660) 24 264 = true := by decide +kernel
private theorem one_cert_288 : segment (agrees one endOne 660) 24 288 = true := by decide +kernel
private theorem one_cert_312 : segment (agrees one endOne 660) 24 312 = true := by decide +kernel
private theorem one_cert_336 : segment (agrees one endOne 660) 24 336 = true := by decide +kernel
private theorem one_cert_360 : segment (agrees one endOne 660) 24 360 = true := by decide +kernel
private theorem one_cert_384 : segment (agrees one endOne 660) 24 384 = true := by decide +kernel
private theorem one_cert_408 : segment (agrees one endOne 660) 24 408 = true := by decide +kernel
private theorem one_cert_432 : segment (agrees one endOne 660) 24 432 = true := by decide +kernel
private theorem one_cert_456 : segment (agrees one endOne 660) 24 456 = true := by decide +kernel
private theorem one_cert_480 : segment (agrees one endOne 660) 24 480 = true := by decide +kernel
private theorem one_cert_504 : segment (agrees one endOne 660) 9 504 = true := by decide +kernel

private theorem one_cert : segment (agrees one endOne 660) 513 0 = true :=
  (@segment_join (agrees one endOne 660) 264 249 0
    (@segment_join (agrees one endOne 660) 120 144 0
      (@segment_join (agrees one endOne 660) 48 72 0
        (@segment_join (agrees one endOne 660) 24 24 0 one_cert_0 one_cert_24)
        (@segment_join (agrees one endOne 660) 24 48 48
          one_cert_48
          (@segment_join (agrees one endOne 660) 24 24 72 one_cert_72 one_cert_96)))
      (@segment_join (agrees one endOne 660) 72 72 120
        (@segment_join (agrees one endOne 660) 24 48 120
          one_cert_120
          (@segment_join (agrees one endOne 660) 24 24 144 one_cert_144 one_cert_168))
        (@segment_join (agrees one endOne 660) 24 48 192
          one_cert_192
          (@segment_join (agrees one endOne 660) 24 24 216 one_cert_216 one_cert_240))))
    (@segment_join (agrees one endOne 660) 120 129 264
      (@segment_join (agrees one endOne 660) 48 72 264
        (@segment_join (agrees one endOne 660) 24 24 264 one_cert_264 one_cert_288)
        (@segment_join (agrees one endOne 660) 24 48 312
          one_cert_312
          (@segment_join (agrees one endOne 660) 24 24 336 one_cert_336 one_cert_360)))
      (@segment_join (agrees one endOne 660) 72 57 384
        (@segment_join (agrees one endOne 660) 24 48 384
          one_cert_384
          (@segment_join (agrees one endOne 660) 24 24 408 one_cert_408 one_cert_432))
        (@segment_join (agrees one endOne 660) 24 33 456
          one_cert_456
          (@segment_join (agrees one endOne 660) 24 9 480 one_cert_480 one_cert_504)))))

private theorem five_cert_0 : segment (agrees five endFive 657) 24 0 = true := by decide +kernel
private theorem five_cert_24 : segment (agrees five endFive 657) 24 24 = true := by decide +kernel
private theorem five_cert_48 : segment (agrees five endFive 657) 24 48 = true := by decide +kernel
private theorem five_cert_72 : segment (agrees five endFive 657) 24 72 = true := by decide +kernel
private theorem five_cert_96 : segment (agrees five endFive 657) 24 96 = true := by decide +kernel
private theorem five_cert_120 : segment (agrees five endFive 657) 24 120 = true := by decide +kernel
private theorem five_cert_144 : segment (agrees five endFive 657) 24 144 = true := by decide +kernel
private theorem five_cert_168 : segment (agrees five endFive 657) 24 168 = true := by decide +kernel
private theorem five_cert_192 : segment (agrees five endFive 657) 24 192 = true := by decide +kernel
private theorem five_cert_216 : segment (agrees five endFive 657) 24 216 = true := by decide +kernel
private theorem five_cert_240 : segment (agrees five endFive 657) 24 240 = true := by decide +kernel
private theorem five_cert_264 : segment (agrees five endFive 657) 24 264 = true := by decide +kernel
private theorem five_cert_288 : segment (agrees five endFive 657) 24 288 = true := by decide +kernel
private theorem five_cert_312 : segment (agrees five endFive 657) 24 312 = true := by decide +kernel
private theorem five_cert_336 : segment (agrees five endFive 657) 24 336 = true := by decide +kernel
private theorem five_cert_360 : segment (agrees five endFive 657) 24 360 = true := by decide +kernel
private theorem five_cert_384 : segment (agrees five endFive 657) 24 384 = true := by decide +kernel
private theorem five_cert_408 : segment (agrees five endFive 657) 24 408 = true := by decide +kernel
private theorem five_cert_432 : segment (agrees five endFive 657) 24 432 = true := by decide +kernel
private theorem five_cert_456 : segment (agrees five endFive 657) 24 456 = true := by decide +kernel
private theorem five_cert_480 : segment (agrees five endFive 657) 24 480 = true := by decide +kernel
private theorem five_cert_504 : segment (agrees five endFive 657) 9 504 = true := by decide +kernel

private theorem five_cert : segment (agrees five endFive 657) 513 0 = true :=
  (@segment_join (agrees five endFive 657) 264 249 0
    (@segment_join (agrees five endFive 657) 120 144 0
      (@segment_join (agrees five endFive 657) 48 72 0
        (@segment_join (agrees five endFive 657) 24 24 0 five_cert_0 five_cert_24)
        (@segment_join (agrees five endFive 657) 24 48 48
          five_cert_48
          (@segment_join (agrees five endFive 657) 24 24 72 five_cert_72 five_cert_96)))
      (@segment_join (agrees five endFive 657) 72 72 120
        (@segment_join (agrees five endFive 657) 24 48 120
          five_cert_120
          (@segment_join (agrees five endFive 657) 24 24 144 five_cert_144 five_cert_168))
        (@segment_join (agrees five endFive 657) 24 48 192
          five_cert_192
          (@segment_join (agrees five endFive 657) 24 24 216 five_cert_216 five_cert_240))))
    (@segment_join (agrees five endFive 657) 120 129 264
      (@segment_join (agrees five endFive 657) 48 72 264
        (@segment_join (agrees five endFive 657) 24 24 264 five_cert_264 five_cert_288)
        (@segment_join (agrees five endFive 657) 24 48 312
          five_cert_312
          (@segment_join (agrees five endFive 657) 24 24 336 five_cert_336 five_cert_360)))
      (@segment_join (agrees five endFive 657) 72 57 384
        (@segment_join (agrees five endFive 657) 24 48 384
          five_cert_384
          (@segment_join (agrees five endFive 657) 24 24 408 five_cert_408 five_cert_432))
        (@segment_join (agrees five endFive 657) 24 33 456
          five_cert_456
          (@segment_join (agrees five endFive 657) 24 9 480 five_cert_480 five_cert_504)))))


private theorem cylinder {w c e : Nat} (cert : segment (agrees w c e) 513 0=true)
    (hc : c<w) (hs : 3^e ≤ 2^1381) (t : Nat) :
    ∃ y < w+2^1381*t, ∀ r ≤ 512, run 1381 (3^r*(w+2^1381*t)) = y := by
  refine ⟨c+3^e*t,Nat.add_lt_add_of_lt_of_le hc (Nat.mul_le_mul_right t hs),?_⟩
  intro r hr
  have h := segment_sound (r:=r) cert (by omega) (by omega)
  have endpt : track 1381 (3^r*w) r = (c,e) := by simpa [agrees,stride_eq] using h
  have hx : 3^r*(w+2^1381*t)=3^r*w+2^1381*3^r*t := by rw [Nat.mul_add]; ac_rfl
  rw [hx,affine,endpt]

private theorem rotate_entry (x : Nat) (odd : x%2=1) :
    ∃ b ≤ 1, ∃ a, (a=one ∨ a=five) ∧ (3^b*x)%8=a%8 := by
  have lo := Nat.mod_lt x (by decide : 0<8)
  have hx : x%8%2=1 := by omega
  by_cases h : x%8=1 ∨ x%8=5
  · rcases h with h|h
    · exact ⟨0,by decide,one,Or.inl rfl,by simpa [show one%8=1 by decide] using h⟩
    · exact ⟨0,by decide,five,Or.inr rfl,by simpa [show five%8=5 by decide] using h⟩
  · have alt : x%8=3 ∨ x%8=7 := by omega
    rcases alt with h|h
    · exact ⟨1,by decide,one,Or.inl rfl,by simp [Nat.mul_mod,h,show one%8=1 by decide]⟩
    · exact ⟨1,by decide,five,Or.inr rfl,by simp [Nat.mul_mod,h,show five%8=5 by decide]⟩

/-- Above any specified phase on every odd tower, a block of 513 consecutive
    ranks has a single physical endpoint strictly below the first base of
    the block. The offset locates the block on the tower. -/
theorem recurring_common_endpoint (w s : Nat) (odd : w%2=1) :
    ∃ d ≤ 2^1379, ∃ y < 3^(s+d)*w,
      ∀ r ≤ 512, run 1381 (3^(s+d+r)*w) = y := by
  let x := 3^s*w
  have hx : x%2=1 := by simp [x,Nat.mul_mod,Nat.pow_mod,odd]
  obtain ⟨b,hb,a,ha,hb8⟩ := rotate_entry x hx
  have hbOdd : (3^b*x)%2=1 := by simp [Nat.mul_mod,Nat.pow_mod,hx]
  obtain ⟨k,hk,hit⟩ := rotate hbOdd hb8 1378
  have had : a<2^1381 := by rcases ha with rfl|rfl <;> decide
  have hit' : (3^k*(3^b*x))%2^1381=a := by
    change (3^k*(3^b*x))%2^1381=a%2^1381 at hit
    simpa [Nat.mod_eq_of_lt had] using hit
  let z := 3^k*(3^b*x)
  let t := z / 2^1381
  have repr : z = a+2^1381*t := by
    have h := Nat.mod_add_div z (2^1381)
    rw [show z%2^1381=a from hit'] at h
    exact h.symm
  have phys : ∃ y < z, ∀ r ≤ 512, run 1381 (3^r*z)=y := by
    rw [repr]
    rcases ha with rfl|rfl
    · exact cylinder one_cert (by decide) (by decide) t
    · exact cylinder five_cert (by decide) (by decide) t
  obtain ⟨y,hy,all⟩ := phys
  have eq : 3^(s+(b+k))*w = z := by simp only [z,x,Nat.pow_add]; ac_rfl
  refine ⟨b+k,by change k<2^1379 at hk; omega,y,by rwa [eq],?_⟩
  intro r hr
  rw [Nat.pow_add,show 3^(s+(b+k))*3^r*w=3^r*(3^(s+(b+k))*w) by ac_rfl,eq]
  exact all r hr

#print axioms recurring_common_endpoint

end Collatz.Itinerary.TowerFrontier
