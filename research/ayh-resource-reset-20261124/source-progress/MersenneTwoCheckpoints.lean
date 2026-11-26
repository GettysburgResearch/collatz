import MersenneParity
import Mathlib.Data.Rat.Cast.Order

namespace CollatzMersenneTwoCheckpoints
open CollatzReverseBasin CollatzMersenneParity

private theorem addClock (k t n : ℕ) : atClock (k+t) n=atClock t (atClock k n) := by
  induction k generalizing n with
  | zero => simp [atClock]
  | succ k ih => simpa [Nat.succ_add,atClock] using ih (shortcut n)

private theorem memClock (k n : ℕ) : Basin (atClock k n) ↔ Basin n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    refine (ih (shortcut n)).trans ⟨?_,?_⟩
    · rintro ⟨t,ht⟩; exact ⟨t+1,ht⟩
    · rintro ⟨t,ht⟩
      cases t with
      | zero => change n=1 at ht; subst n; exact ⟨1,rfl⟩
      | succ t => exact ⟨t,ht⟩

private theorem fiveTurn (t : ℕ) (ht : 0<t) :
    atClock 3 (8*t-5)=9*t-5 := by
  simp only [atClock]
  rw [
    show shortcut (8*t-5)=(12*t-7) by unfold shortcut; split <;> omega,
    show shortcut (12*t-7)=(18*t-10) by unfold shortcut; split <;> omega,
    show shortcut (18*t-10)=(9*t-5) by unfold shortcut; split <;> omega]

private theorem fiveTurns (k t : ℕ) (ht : 0<t) :
    atClock (3*k) (8^k*t-5)=9^k*t-5 := by
  induction k generalizing t with
  | zero => simp [atClock]
  | succ k ih =>
    have pos : 0<8^k*t := Nat.mul_pos (Nat.pow_pos (by decide : 0<8)) ht
    rw [show 3*(k+1)=3+3*k by omega, addClock,
        show 8^(k+1)*t=8*(8^k*t) by ring_nf, fiveTurn _ pos,
        show 9*(8^k*t)=8^k*(9*t) by ring_nf, ih _ (by omega)]
    ring_nf

private theorem seventeenTurn (t : ℕ) (ht : 0<t) :
    atClock 11 (2048*t-17)=2187*t-17 := by
  simp only [atClock]
  rw [
    show shortcut (2048*t-17)=(3072*t-25) by unfold shortcut; split <;> omega,
    show shortcut (3072*t-25)=(4608*t-37) by unfold shortcut; split <;> omega,
    show shortcut (4608*t-37)=(6912*t-55) by unfold shortcut; split <;> omega,
    show shortcut (6912*t-55)=(10368*t-82) by unfold shortcut; split <;> omega,
    show shortcut (10368*t-82)=(5184*t-41) by unfold shortcut; split <;> omega,
    show shortcut (5184*t-41)=(7776*t-61) by unfold shortcut; split <;> omega,
    show shortcut (7776*t-61)=(11664*t-91) by unfold shortcut; split <;> omega,
    show shortcut (11664*t-91)=(17496*t-136) by unfold shortcut; split <;> omega,
    show shortcut (17496*t-136)=(8748*t-68) by unfold shortcut; split <;> omega,
    show shortcut (8748*t-68)=(4374*t-34) by unfold shortcut; split <;> omega,
    show shortcut (4374*t-34)=(2187*t-17) by unfold shortcut; split <;> omega]

private theorem seventeenTurns (k t : ℕ) (ht : 0<t) :
    atClock (11*k) (2048^k*t-17)=2187^k*t-17 := by
  induction k generalizing t with
  | zero => simp [atClock]
  | succ k ih =>
    have pos : 0<2048^k*t := Nat.mul_pos (Nat.pow_pos (by decide : 0<2048)) ht
    rw [show 11*(k+1)=11+11*k by omega, addClock,
        show 2048^(k+1)*t=2048*(2048^k*t) by ring_nf, seventeenTurn _ pos,
        show 2187*(2048^k*t)=2048^k*(2187*t) by ring_nf, ih _ (by omega)]
    ring_nf

/-- Full ordinary turns consume the entire available binary exponent. -/
theorem five_endpoint (m : ℕ) :
    atClock (3*(33+54*m)) (12*2^(97+162*m)-5)=3^(67+108*m)-5 := by
  let k:=33+54*m
  have a : 12*2^(97+162*m)=8^k*3 := by
    rw [show (8:ℕ)=2^3 by decide,←pow_mul,show 3*k=(97+162*m)+2 by dsimp [k]; omega,pow_add]
    ring_nf
  have b : 9^k*3=3^(67+108*m) := by
    rw [show (9:ℕ)=3^2 by decide,←pow_mul,show 67+108*m=2*k+1 by dsimp [k]; omega,pow_succ]
  rw [a,fiveTurns k 3 (by decide),b]

theorem seventeen_endpoint (j : ℕ) :
    atClock (11*((j-1)/11)) (27*2^(j-1)-17)=
      3^(3+7*((j-1)/11))*2^((j-1)%11)-17 := by
  let k:=(j-1)/11
  let r:=(j-1)%11
  have e : j-1=11*k+r := (Nat.div_add_mod (j-1) 11).symm
  have a : 27*2^(j-1)=2048^k*(27*2^r) := by
    calc 27*2^(j-1)=27*2^(11*k+r) := congrArg (fun i : ℕ => 27*2^i) e
         _ = _ := by rw [pow_add,pow_mul]; ring_nf
  rw [a,seventeenTurns k (27*2^r) (Nat.mul_pos (by decide) (Nat.pow_pos (by decide)))]
  change 2187^k*(27*2^r)-17=3^(3+7*k)*2^r-17
  rw [pow_add,pow_mul]; ring_nf

private theorem word1 (t : ℕ) : atClock 8 (9437184*t+8815793)=(995328*t+929791) := by
  simp only [atClock]
  rw [
    show shortcut (9437184*t+8815793)=(14155776*t+13223690) by unfold shortcut; split <;> omega,
    show shortcut (14155776*t+13223690)=(7077888*t+6611845) by unfold shortcut; split <;> omega,
    show shortcut (7077888*t+6611845)=(10616832*t+9917768) by unfold shortcut; split <;> omega,
    show shortcut (10616832*t+9917768)=(5308416*t+4958884) by unfold shortcut; split <;> omega,
    show shortcut (5308416*t+4958884)=(2654208*t+2479442) by unfold shortcut; split <;> omega,
    show shortcut (2654208*t+2479442)=(1327104*t+1239721) by unfold shortcut; split <;> omega,
    show shortcut (1327104*t+1239721)=(1990656*t+1859582) by unfold shortcut; split <;> omega,
    show shortcut (1990656*t+1859582)=(995328*t+929791) by unfold shortcut; split <;> omega]

private theorem word2 (t : ℕ) : atClock 9 (28311552*t+26447379)=(13436928*t+12552175) := by
  simp only [atClock]
  rw [
    show shortcut (28311552*t+26447379)=(42467328*t+39671069) by unfold shortcut; split <;> omega,
    show shortcut (42467328*t+39671069)=(63700992*t+59506604) by unfold shortcut; split <;> omega,
    show shortcut (63700992*t+59506604)=(31850496*t+29753302) by unfold shortcut; split <;> omega,
    show shortcut (31850496*t+29753302)=(15925248*t+14876651) by unfold shortcut; split <;> omega,
    show shortcut (15925248*t+14876651)=(23887872*t+22314977) by unfold shortcut; split <;> omega,
    show shortcut (23887872*t+22314977)=(35831808*t+33472466) by unfold shortcut; split <;> omega,
    show shortcut (35831808*t+33472466)=(17915904*t+16736233) by unfold shortcut; split <;> omega,
    show shortcut (17915904*t+16736233)=(26873856*t+25104350) by unfold shortcut; split <;> omega,
    show shortcut (26873856*t+25104350)=(13436928*t+12552175) by unfold shortcut; split <;> omega]

private theorem word3 (t : ℕ) : atClock 5 (10616832*t+9917777)=(2985984*t+2789375) := by
  simp only [atClock]
  rw [
    show shortcut (10616832*t+9917777)=(15925248*t+14876666) by unfold shortcut; split <;> omega,
    show shortcut (15925248*t+14876666)=(7962624*t+7438333) by unfold shortcut; split <;> omega,
    show shortcut (7962624*t+7438333)=(11943936*t+11157500) by unfold shortcut; split <;> omega,
    show shortcut (11943936*t+11157500)=(5971968*t+5578750) by unfold shortcut; split <;> omega,
    show shortcut (5971968*t+5578750)=(2985984*t+2789375) by unfold shortcut; split <;> omega]

private theorem word4 (t : ℕ) : atClock 6 (31850496*t+29753331)=(13436928*t+12552187) := by
  simp only [atClock]
  rw [
    show shortcut (31850496*t+29753331)=(47775744*t+44629997) by unfold shortcut; split <;> omega,
    show shortcut (47775744*t+44629997)=(71663616*t+66944996) by unfold shortcut; split <;> omega,
    show shortcut (71663616*t+66944996)=(35831808*t+33472498) by unfold shortcut; split <;> omega,
    show shortcut (35831808*t+33472498)=(17915904*t+16736249) by unfold shortcut; split <;> omega,
    show shortcut (17915904*t+16736249)=(26873856*t+25104374) by unfold shortcut; split <;> omega,
    show shortcut (26873856*t+25104374)=(13436928*t+12552187) by unfold shortcut; split <;> omega]

private theorem word5 (t : ℕ) : atClock 3 (11943936*t+11157499)=(13436928*t+12552187) := by
  simp only [atClock]
  rw [
    show shortcut (11943936*t+11157499)=(17915904*t+16736249) by unfold shortcut; split <;> omega,
    show shortcut (17915904*t+16736249)=(26873856*t+25104374) by unfold shortcut; split <;> omega,
    show shortcut (26873856*t+25104374)=(13436928*t+12552187) by unfold shortcut; split <;> omega]

private theorem residue (m : ℕ) : 2^(97+162*m)%995328=929792 := by
  induction m with
  | zero => decide
  | succ m ih =>
    rw [show 97+162*(m+1)=162+(97+162*m) by omega,pow_add,Nat.mul_mod,ih]
    decide

/-- Under the supplied bad Mersenne starts and least-defect comparison rule,
both shorter-exponent ordinary ternary checkpoints must also be nonbasin. -/
theorem two_bad_checkpoints (m z : ℕ) (j : ℕ) (hj : j=97+162*m)
    (parent : 81*z+527=1024*2^j)
    (minimal : ∀ w : ℕ, w%48=17 → w<z → Basin (3*w) → Basin w)
    (bad : ¬Basin (2^j-1)) :
    ¬Basin (3^(67+108*m)-5) ∧ ¬Basin (3^(3+7*((j-1)/11))*2^((j-1)%11)-17) := by
  have merger := even_mersenne_basin (48+81*m)
  rw [show 2*(48+81*m)+2=j+1 by omega, show 2*(48+81*m)+1=j by omega] at merger
  have badNext : ¬Basin (2^(j+1)-1) := fun hb => bad (merger.mp hb)
  let t:=2^j/995328
  have n : 2^j=995328*t+929792 := by
    dsimp [t]
    have res : 2^j%995328=929792 := hj ▸ residue m
    omega
  have n1 : 2^(j+1)=2*(2^j) := by rw [pow_succ,Nat.mul_comm]
  have jp : 0<j := by omega
  have nh : 2^j=2*(2^(j-1)) := by
    calc _ = 2^((j-1)+1) := congrArg (fun i : ℕ => 2^i) (by omega)
         _ = _ := by rw [pow_succ,Nat.mul_comm]
  let w1:=9437184*t+8815793
  let w2:=10616832*t+9917777
  have h1 : ¬Basin w1 := by
    have h := word1 t
    change atClock 8 w1 = _ at h
    rw [show 995328*t+929791=2^j-1 by omega] at h
    exact fun hb => bad (h ▸ (memClock 8 w1).mpr hb)
  have h2 : ¬Basin w2 := by
    have h := word3 t
    change atClock 5 w2 = _ at h
    have start : shortcut (2^(j+1)-1)=3*(2^j)-1 := by rw [n1]; unfold shortcut; split <;> omega
    rw [show 2985984*t+2789375=3*(2^j)-1 by omega, ←start] at h
    intro hb
    have step : Basin (shortcut (2^(j+1)-1)) := h ▸ (memClock 5 w2).mpr hb
    exact badNext ((memClock 1 _).mp step)
  have q1 : ¬Basin (3*w1) := fun hb => h1 (minimal _ (by dsimp [w1]; omega) (by dsimp [w1]; omega) hb)
  have q2 : ¬Basin (3*w2) := fun hb => h2 (minimal _ (by dsimp [w2]; omega) (by dsimp [w2]; omega) hb)
  have h17 : ¬Basin (27*2^(j-1)-17) := by
    have h := word2 t
    rw [show 28311552*t+26447379=3*w1 by dsimp [w1]; ring_nf, show 13436928*t+12552175=27*2^(j-1)-17 by omega] at h
    exact fun hb => q1 ((memClock 9 _).mp (h.symm ▸ hb))
  have h5 : ¬Basin (12*2^j-5) := by
    have h := word4 t
    have k := word5 t
    rw [show 31850496*t+29753331=3*w2 by dsimp [w2]; ring_nf] at h
    rw [show 11943936*t+11157499=12*2^j-5 by omega] at k
    exact fun hb => q2 ((memClock 6 _).mp (h.symm ▸ (k ▸ (memClock 3 _).mpr hb)))
  constructor
  · rw [←five_endpoint]
    subst j
    exact fun hb => h5 ((memClock _ _).mp hb)
  · rw [←seventeen_endpoint]
    exact fun hb => h17 ((memClock _ _).mp hb)

private theorem mergeWord1 (v : ℕ) : atClock 8 (256*v+134) = 81*v+44 := by
  simp only [atClock]
  rw [
    show shortcut (256*v+134)=128*v+67 by unfold shortcut; split <;> omega,
    show shortcut (128*v+67)=192*v+101 by unfold shortcut; split <;> omega,
    show shortcut (192*v+101)=288*v+152 by unfold shortcut; split <;> omega,
    show shortcut (288*v+152)=144*v+76 by unfold shortcut; split <;> omega,
    show shortcut (144*v+76)=72*v+38 by unfold shortcut; split <;> omega,
    show shortcut (72*v+38)=36*v+19 by unfold shortcut; split <;> omega,
    show shortcut (36*v+19)=54*v+29 by unfold shortcut; split <;> omega,
    show shortcut (54*v+29)=81*v+44 by unfold shortcut; split <;> omega]

private theorem mergeWord2 (v : ℕ) : atClock 8 (2304*v+1250) = 81*v+44 := by
  simp only [atClock]
  rw [
    show shortcut (2304*v+1250)=1152*v+625 by unfold shortcut; split <;> omega,
    show shortcut (1152*v+625)=1728*v+938 by unfold shortcut; split <;> omega,
    show shortcut (1728*v+938)=864*v+469 by unfold shortcut; split <;> omega,
    show shortcut (864*v+469)=1296*v+704 by unfold shortcut; split <;> omega,
    show shortcut (1296*v+704)=648*v+352 by unfold shortcut; split <;> omega,
    show shortcut (648*v+352)=324*v+176 by unfold shortcut; split <;> omega,
    show shortcut (324*v+176)=162*v+88 by unfold shortcut; split <;> omega,
    show shortcut (162*v+88)=81*v+44 by unfold shortcut; split <;> omega]

set_option exponentiation.threshold 2000 in
set_option maxRecDepth 4096 in
private theorem ternaryResidue (t : ℕ) : 3^(391+1728*t)%256=139 := by
  induction t with
  | zero => decide
  | succ t ih =>
    rw [show 391+1728*(t+1)=1728+(391+1728*t) by omega,pow_add,Nat.mul_mod,ih]
    decide

/-- On a full one-sixteenth of the exponent row, eight additional ordinary
steps from the ternary checkpoint meet an earlier Mersenne orbit. -/
theorem exclude_sixteenth (t z : ℕ) (m j : ℕ) (hm : m=3+16*t) (hj : j=97+162*m)
    (parent : 81*z+527=1024*2^j)
    (minimal : ∀ w : ℕ, w%48=17 → w<z → Basin (3*w) → Basin w)
    (earlier : ∀ a : ℕ, 0<a → a<j → Basin (2^a-1)) : Basin (2^j-1) := by
  classical
  by_contra bad
  have hbad := (two_bad_checkpoints m z j hj parent minimal bad).1
  let q:=67+108*m
  have hq : 3^q%256=139 := by
    rw [show q=391+1728*t by dsimp [q]; omega]
    exact ternaryResidue t
  let v:=3^q/256
  have form : 3^q=256*v+139 := by dsimp [v]; omega
  have hp := earlier (q+2) (by omega) (by dsimp [q]; omega)
  have ascent' := ascent (q+2) 1 (by decide)
  simp only [Nat.mul_one] at ascent'
  have prev : Basin (3^(q+2)-1) := ascent' ▸ (memClock _ _).mpr hp
  have a := mergeWord1 v
  rw [show 256*v+134=3^q-5 by omega] at a
  have b := mergeWord2 v
  rw [show 2304*v+1250=3^(q+2)-1 by rw [pow_add]; omega] at b
  have common : Basin (81*v+44) := b ▸ (memClock _ _).mpr prev
  exact hbad ((memClock _ _).mp (a.symm ▸ common))

/-- The two post-turn exponents retain an exact integer relation. -/
theorem checkpoint_exponents (m : ℕ) :
    22*(3+7*((96+162*m)/11))+14*((96+162*m)%11)=21*(67+108*m)+3 := by
  omega

/-- The cleared simultaneous relation has no rational solution with a
negative first coordinate. -/
theorem no_negative_rational_pair (x y : ℚ) (r : ℕ) (hx : x<0) :
    (3:ℚ)^(14*r)*y^22 ≠ 27*x^21 := by
  have yl : 0≤y^22 := by rw [show 22=11*2 by decide,pow_mul]; exact sq_nonneg _
  have xl : x^21<0 := by
    rw [show 21=10*2+1 by decide,pow_succ,pow_mul]
    exact mul_neg_of_pos_of_neg (lt_of_le_of_ne (sq_nonneg _) (Ne.symm (pow_ne_zero _ (pow_ne_zero _ (ne_of_lt hx))))) hx
  exact ne_of_gt (lt_of_lt_of_le (mul_neg_of_pos_of_neg (by decide : (0:ℚ)<27) xl)
      (mul_nonneg (pow_nonneg (by decide : (0:ℚ)≤3) _) yl))

#print axioms checkpoint_exponents
#print axioms no_negative_rational_pair
#print axioms exclude_sixteenth

#print axioms five_endpoint
#print axioms seventeen_endpoint
#print axioms two_bad_checkpoints
end CollatzMersenneTwoCheckpoints
