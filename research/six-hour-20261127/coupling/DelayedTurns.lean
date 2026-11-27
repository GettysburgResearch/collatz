import PaidCheckpoint

/-! Ordinary turns through the negative 17 cycle. The signed center is
used only to discover the five addresses. The statements and proofs run
the positive natural-number map. -/
set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 12000
namespace DelayedTurns
open CoreBranching FloorCounting PeakRigidity

def hard (k : ℕ) := 12*2^(18*k)-1

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

/-- Literal 11-clock transport on every ordinary lift. -/
theorem long_turns (d U : ℕ) (hu : 0<U) :
    run (11*d) (2^(11*d)*U-17)=3^(7*d)*U-17 := by
  have block (v : ℕ) (hv : 0<v) : run 11 (2048*v-17)=2187*v-17 := by
    obtain ⟨a,va⟩:= Nat.exists_eq_add_of_le (show 1≤v by omega)
    have p := (lift_prefix 11 0 2031 a).1
    norm_num [show run 11 2031=2170 by decide,show grade 11 2031=7 by decide] at p
    rw [show 2048*v-17=2031+2048*a by omega,p]
    omega
  induction d generalizing U with
  | zero => simp [run]
  | succ d ih =>
    rw [show 11*(d+1)=11+11*d by ring,show 7*(d+1)=7*d+7 by ring,pow_add,pow_add,run_add]
    rw [show (2:ℕ)^11*2^(11*d)*U=2048*(2^(11*d)*U) by ring,block _ (by positivity)]
    rw [show 2187*(2^(11*d)*U)=2^(11*d)*(2187*U) by ring,ih _ (by positivity)]
    ring_nf

structure Phase where
  base : ℕ
  rem : ℕ
  odds : ℕ
  neg : ℕ
  shift : ℕ
  clocks : ℕ
  residue : ℕ
deriving DecidableEq

def phases : List Phase := [
  ⟨13,1,1,25,0,29,461579579⟩,
  ⟨14,0,0,17,1,68,280805277589011893753⟩,
  ⟨15,8,7,136,0,23,4177273⟩,
  ⟨16,10,7,34,0,71,402629366566281059537⟩,
  ⟨17,5,4,41,0,229,242205671938496182374078686439653188948608558198709461640393419169833⟩]

private def expn (p : Phase) (m : ℕ) := 7*((m-3)/11)+3+p.odds-p.shift

private structure Checks (p : Phase) : Prop where
  prec : p.clocks≤18*p.base
  wide : 1000≤hard p.base
  rem_eq : p.rem=(hard p.base-3)%11
  odds_le : p.odds≤p.rem
  shift_le : p.shift≤1
  turn_base : run p.rem (2^p.rem*200-17)+p.neg=3^p.odds*200
  turn_grade : grade p.rem (2^p.rem*200-17)=p.odds
  residue_bound : p.neg≤p.residue
  residue_pos : 0<p.residue
  residue_eq : modPower 3 (2^p.clocks) (expn p (hard p.base))=p.residue
  merge_base : run p.clocks (3^p.shift*p.residue-p.neg)=run p.clocks (p.residue-1)
  merge_grade : p.shift+grade p.clocks (3^p.shift*p.residue-p.neg)=grade p.clocks (p.residue-1)

set_option maxHeartbeats 0 in
private theorem finite_phases : ∀ p∈phases, Checks p := by
  simp only [phases,List.mem_cons,List.not_mem_nil,or_false]
  intro p h
  rcases h with h|h|h|h|h <;> subst p <;> constructor <;> decide +kernel

private theorem recover_turn (p : Phase) (chk : Checks p) (U : ℕ) (hu : 200≤U) :
    run p.rem (2^p.rem*U-17)=3^p.odds*U-p.neg := by
  obtain ⟨v,uv⟩:=Nat.exists_eq_add_of_le hu
  have eq := (lift_prefix p.rem 0 (2^p.rem*200-17) v).1
  simp only [Nat.add_zero,pow_zero,one_mul,chk.turn_grade] at eq
  have small : 17≤2^p.rem*200 := by
    have := Nat.two_pow_pos p.rem
    omega
  rw [uv,Nat.mul_add,show 2^p.rem*200+2^p.rem*v-17=(2^p.rem*200-17)+2^p.rem*v by omega,eq,Nat.mul_add]
  have := chk.turn_base
  omega

private theorem recover_merger (p : Phase) (chk : Checks p) (n : ℕ)
    (addr : 3^n%2^p.clocks=p.residue) :
    run p.clocks (3^(n+p.shift)-p.neg)=run p.clocks (3^n-1) := by
  let v := 3^n/2^p.clocks
  have rep : 3^n=p.residue+2^p.clocks*v := by
    dsimp [v]
    rw [←addr,Nat.mod_add_div]
  have a := (lift_prefix p.clocks 0 (3^p.shift*p.residue-p.neg) (3^p.shift*v)).1
  have b := (lift_prefix p.clocks 0 (p.residue-1) v).1
  simp only [Nat.add_zero,pow_zero,one_mul] at a b
  have nn := chk.residue_bound
  have ww := chk.residue_pos
  have bound : p.neg≤3^p.shift*p.residue := by
    exact nn.trans (Nat.le_mul_of_pos_left _ (by positivity))
  rw [pow_add,mul_comm (3^n),rep,Nat.mul_add,
    show 3^p.shift*(2^p.clocks*v)=2^p.clocks*(3^p.shift*v) by ring,
    show 3^p.shift*p.residue+2^p.clocks*(3^p.shift*v)-p.neg=
      (3^p.shift*p.residue-p.neg)+2^p.clocks*(3^p.shift*v) by omega,
    show p.residue+2^p.clocks*v-1=p.residue-1+2^p.clocks*v by omega,
    a,b,chk.merge_base,←mul_assoc,←pow_add,add_comm (grade _ _),chk.merge_grade]

private theorem grow_address (p : Phase) (chk : Checks p) (t : ℕ) :
    ∃ v, hard (p.base+5*t)=hard p.base+11*(2^p.clocks)*v := by
  have b : (2:ℕ)^90 ≡ 1 [MOD 11] := by decide +kernel
  have bt : ((2:ℕ)^90)^t%11=1 := by
    have be : ((2:ℕ)^90)^t ≡ 1 [MOD 11] := by simpa using b.pow t
    exact be
  have base_pos : 0<(2:ℕ)^(18*p.base) := by positivity
  have r : 2^(18*p.base)=2^p.clocks*2^(18*p.base-p.clocks) := by
    rw [←pow_add, Nat.add_sub_of_le chk.prec]
  let a := (2^90)^t/11
  have aw : (2^90)^t=1+11*a := by
    change (2^90)^t=1+11*((2^90)^t/11)
    rw [←bt]
    exact (Nat.mod_add_div _ _).symm
  refine ⟨12*2^(18*p.base-p.clocks)*a,?_⟩
  unfold hard
  rw [show 18*(p.base+5*t)=18*p.base+90*t by ring,pow_add,pow_mul (2:ℕ) 90,aw]
  have out : 12*(2^(18*p.base)*(1+11*a))=
      12*2^(18*p.base)+11*2^p.clocks*(12*2^(18*p.base-p.clocks)*a) := by
    conv_lhs => rw [r]
    conv_rhs => lhs; rw [r]
    ring
  omega

private theorem phase_actual (p : Phase) (chk : Checks p) (v : ℕ) :
    let m := hard (p.base+5*v)
    let d := (m-3)/11
    run (11*d+p.rem+p.clocks) (27*2^(m-3)-17)=
      run p.clocks (3^(expn p m)-1) ∧ 0<expn p m ∧ expn p m+40<m := by
  dsimp only
  let m := hard (p.base+5*v)
  let d := (m-3)/11
  change run (11*d+p.rem+p.clocks) (27*2^(m-3)-17)=
    run p.clocks (3^(expn p m)-1) ∧ 0<expn p m ∧ expn p m+40<m
  obtain ⟨v',growth⟩:=grow_address p chk v
  let V := 2^p.clocks*v'
  change m=hard p.base+11*2^p.clocks*v' at growth
  rw [mul_assoc] at growth
  change m=hard p.base+11*V at growth
  have g := chk.wide
  have r0 := chk.rem_eq
  have ro := chk.odds_le
  have sc := chk.shift_le
  have drift : d=(hard p.base-3)/11+V := by dsimp [d]; omega
  have balance : m-3=11*d+p.rem := by dsimp [d]; omega
  have di : 90≤d := by omega
  have remSmall : p.rem<11 := by omega
  have ex : expn p m=expn p (hard p.base)+2^p.clocks*(7*v') := by
    unfold expn
    change 7*d+3+p.odds-p.shift=_+_
    rw [drift,show 2^p.clocks*(7*v')=7*V by dsimp [V]; ring]
    omega
  have res : 3^(expn p m)%2^p.clocks=p.residue := by
    rw [ex]
    have b := pow_stable (expn p (hard p.base)) p.clocks (7*v')
    change 3^(expn p (hard p.base)+2^p.clocks*(7*v'))%2^p.clocks=
      3^(expn p (hard p.base))%2^p.clocks at b
    exact b.trans (by simpa only [modPower_correct] using chk.residue_eq)
  have ub : 200≤3^(7*d+3) := calc
    200 ≤ (3:ℕ)^5 := by decide
    _ ≤ 3^(7*d+3) := Nat.pow_le_pow_right (by decide) (by omega)
  have turn := recover_turn p chk _ ub
  have full := long_turns d (2^p.rem*27) (by positivity)
  have src : 27*2^(m-3)=2^(11*d)*(2^p.rem*27) := by rw [balance,pow_add]; ring
  have mid : 3^(7*d)*(2^p.rem*27)=2^p.rem*3^(7*d+3) := by rw [pow_add]; ring
  have finalPower : 3^p.odds*3^(7*d+3)=3^(expn p m+p.shift) := by
    rw [←pow_add]
    congr 1
    unfold expn
    change p.odds+(7*d+3)=7*d+3+p.odds-p.shift+p.shift
    omega
  have merger := recover_merger p chk (expn p m) res
  constructor
  · rw [run_add,run_add,src,full,mid,turn,finalPower,merger]
  · unfold expn
    change 0<7*d+3+p.odds-p.shift ∧ 7*d+3+p.odds-p.shift+40<m
    omega

/-- The same finite five-row kernel works at every original delayed k≥13.
The earlier exponent is more than forty below the original exponent. -/
theorem earlier_after_turns (k : ℕ) (hk : 13≤k) :
    ∃ h t l, run h (27*2^(hard k-3)-17)=run l (3^t-1) ∧ 0<t ∧ t+40<hard k := by
  let i := (k-13)%5
  have il : i<phases.length := by change (k-13)%5<5; omega
  let p := phases[i]'il
  have pm : p∈phases := List.getElem_mem il
  have pi : i<5 := by dsimp [i]; omega
  have pb : p.base=13+i := by
    interval_cases i <;> simp [p,phases]
  let v := (k-13)/5
  have kv : p.base+5*v=k := by dsimp [v]; rw [pb]; dsimp [i]; omega
  have eq := phase_actual p (finite_phases p pm) v
  rw [kv] at eq
  exact ⟨_,_,_,eq⟩

private theorem pow_residue (a b c d m t : ℕ)
    (h : a^b ≡ c [MOD m]) (p : a^d ≡ 1 [MOD m]) :
    a^(b+d*t) ≡ c [MOD m] := by
  rw [pow_add,pow_mul]
  simpa only [one_pow,mul_one] using h.mul (p.pow t)

private theorem raw_parent (m z : ℕ) (eq : 81*z+271=128*2^m) :
    run 7 z=2^m-1 ∧ grade 7 z=4 := by
  have zm : z%128=33 := by omega
  have rep : z=33+128*(z/128) := by omega
  have tr := lift_prefix 7 0 33 (z/128)
  norm_num [show run 7 33=22 by decide,show grade 7 33=4 by decide] at tr
  rwa [←rep,show 22+81*(z/128)=2^m-1 by omega] at tr

private theorem ascent (n b : ℕ) (pos : 0<b) :
    run n (2^n*b-1)=3^n*b-1 := by
  induction n generalizing b with
  | zero => simp [run]
  | succ n ih =>
    have p : 0<2^n*b := by positivity
    have form : 2^(n+1)*b-1=2*(2^n*b-1)+1 := by
      rw [pow_succ,show 2^n*2*b=2*(2^n*b) by ring]
      omega
    have st : step (2^(n+1)*b-1)=2^n*(3*b)-1 := by
      rw [form,step_odd,show 2^n*(3*b)=3*(2^n*b) by ring]
      omega
    rw [run,st,ih _ (by omega),pow_succ,mul_assoc]

private structure Seed where
  index : ℕ
  lower : ℕ
  upper : ℕ
  offset : ℕ
  w0 : ℕ
  x0 : ℕ
  exponentResidue : ℕ

private def leftSeed : Seed := ⟨1429,17,20,962197,388433,65623,23923⟩
private def rightSeed : Seed := ⟨376,18,21,1786613,2407985,203404,41419⟩

private structure SeedChecks (p : Seed) : Prop where
  k13 : 13≤p.index
  gap : p.upper=p.lower+3
  bounded : p.upper≤21
  xr : p.x0<531441
  wr : p.w0%48=17
  wp : 0<p.w0
  compare : 81*p.w0+271 < 1024*p.x0
  slope : 81*(3*2^p.upper)<1024*531441
  wide : 4≤12*p.exponentResidue
  kres : 2^(18*p.index)%59049=p.exponentResidue
  xres : 2^(12*p.exponentResidue-4)%531441=p.x0
  shape : 177147*p.w0+p.offset=2^p.upper*p.x0
  lo : run p.lower p.w0+1=8*p.x0
  lg : grade p.lower p.w0=11
  hi : run p.upper (3*p.w0)+17=27*p.x0
  hg : grade p.upper (3*p.w0)=13

private theorem seeds (p : Seed) (hp : p=leftSeed ∨ p=rightSeed) : SeedChecks p := by
  rcases hp with h|h <;> subst p <;> constructor <;> decide +kernel

private theorem source_address (p : Seed) (chk : SeedChecks p) (t : ℕ) :
    2^(hard (p.index+2187*t)-3)%531441=p.x0 := by
  have per : 2^39366≡1 [MOD 59049] := by decide +kernel
  have base : 2^(18*p.index)≡p.exponentResidue [MOD 59049] := by
    have c := chk.kres
    have small : p.exponentResidue<59049 := c ▸ Nat.mod_lt _ (by decide)
    exact c.trans (Nat.mod_eq_of_lt small).symm
  have kr := pow_residue 2 (18*p.index) p.exponentResidue 39366 59049 t base per
  have e : 18*(p.index+2187*t)=18*p.index+39366*t := by ring
  rw [←e] at kr
  have ks : p.exponentResidue<59049 := chk.kres ▸ Nat.mod_lt _ (by decide)
  change 2^(18*(p.index+2187*t))%59049=p.exponentResidue%59049 at kr
  rw [Nat.mod_eq_of_lt ks] at kr
  have big := chk.wide
  have form : hard (p.index+2187*t)-3 =
      (12*p.exponentResidue-4)+354294*(2*(2^(18*(p.index+2187*t))/59049)) := by
    unfold hard
    omega
  have b : 2^(12*p.exponentResidue-4)≡p.x0 [MOD 531441] :=
    chk.xres.trans (Nat.mod_eq_of_lt chk.xr).symm
  have z := pow_residue 2 (12*p.exponentResidue-4) p.x0 354294 531441
    (2*(2^(18*(p.index+2187*t))/59049)) b (by decide +kernel)
  rw [←form] at z
  change 2^(hard (p.index+2187*t)-3)%531441=p.x0%531441 at z
  exact z.trans (Nat.mod_eq_of_lt chk.xr)

private theorem seed_lift (p : Seed) (chk : SeedChecks p) (v : ℕ) :
    let w := p.w0+3*2^p.upper*v
    let X := p.x0+531441*v
    w%48=17 ∧ run p.lower w+1=8*X ∧ grade p.lower w=11 ∧
      run p.upper (3*w)+17=27*X ∧ grade p.upper (3*w)=13 := by
  dsimp only
  have lo := lift_prefix p.lower 0 p.w0 (24*v)
  have hi := lift_prefix p.upper 0 (3*p.w0) (9*v)
  simp only [Nat.add_zero,pow_zero,one_mul,chk.lg,chk.hg] at lo hi
  have a : 3*2^p.upper*v=2^p.lower*(24*v) := by rw [chk.gap,pow_add]; ring
  have b : 3*(p.w0+3*2^p.upper*v)=3*p.w0+2^p.upper*(9*v) := by ring
  have low : 4≤p.upper := by
    have g := chk.gap
    have lg := chk.lg
    have le := grade_le p.lower p.w0
    omega
  have mod : 48 ∣ 3*2^p.upper*v := by
    refine ⟨2^(p.upper-4)*v,?_⟩
    conv_lhs => rw [show p.upper=4+(p.upper-4) by omega,pow_add]
    ring
  have lower := chk.lo
  have upper := chk.hi
  rw [b, a,lo.1,lo.2,hi.1,hi.2]
  have mc : (p.w0+2^p.lower*(24*v))%48=17 := by
    rw [←a,Nat.add_mod,Nat.mod_eq_zero_of_dvd mod,chk.wr]
  norm_num at *
  omega

set_option maxHeartbeats 2000000 in
/-- Both qualifying classes in the actual k parameter. The lower equality
starts on the original parent. The opposing meeting starts at a positive
earlier Mersenne number and pays the forty-bit return test. -/
theorem paid_delayed_merger (k z : ℕ) (address : k%2187=1429 ∨ k%2187=376)
    (parent : 81*z+271=128*2^(hard k)) :
    ∃ w a b h s l, 0<w ∧ w<z ∧ w%48=17 ∧ 0<s ∧ s+40<hard k ∧
      run a w=run 7 z ∧ run 7 z=2^(hard k)-1 ∧ grade a w=11 ∧
      run b (3*w)=27*2^(hard k-3)-17 ∧ grade b (3*w)=13 ∧
      run (b+h) (3*w)=run (s+l) (2^s-1) ∧ 2^40*(2^s-1)<z := by
  have select : ∃ p, (p=leftSeed ∨ p=rightSeed) ∧ k=p.index+2187*(k/2187) := by
    rcases address with a|a
    · exact ⟨leftSeed,Or.inl rfl,by change k=1429+2187*(k/2187); omega⟩
    · exact ⟨rightSeed,Or.inr rfl,by change k=376+2187*(k/2187); omega⟩
  obtain ⟨p,hp,kp⟩:=select
  have chk := seeds p hp
  have kres := source_address p chk (k/2187)
  rw [←kp] at kres
  let X := 2^(hard k-3)
  let v := X/531441
  have Xv : X=p.x0+531441*v := by
    change X%531441=p.x0 at kres
    dsimp [v]
    omega
  have tr := seed_lift p chk v
  rw [←Xv] at tr
  obtain ⟨can,lo,lg,hi,hg⟩:=tr
  have hk : 13≤k := by have := chk.k13; omega
  have m3 : 5≤hard k := by
    unfold hard
    have : (2:ℕ)^(18*k)>0 := by positivity
    omega
  have power : 2^(hard k)=8*X := by
    conv_lhs => rw [show hard k=3+(hard k-3) by omega,pow_add]
    rfl
  have val := parent
  rw [power] at val
  have compare := chk.compare
  have sl := Nat.mul_le_mul_right v (Nat.le_of_lt chk.slope)
  have wp := chk.wp
  have small : p.w0+3*2^p.upper*v<z := by
    rw [show 81*(3*2^p.upper)*v=81*(3*2^p.upper*v) by ring] at sl
    omega
  obtain ⟨h,s,l,meet,sp,gap⟩:=earlier_after_turns k hk
  have raw := raw_parent _ _ parent
  have mas : run s (2^s-1)=3^s-1 := by simpa using ascent s 1 (by decide)
  have less : (2:ℕ)^40*(2^s-1)<z := by
    have f : (2:ℕ)^(s+40)≤2^(hard k) := Nat.pow_le_pow_right (by decide) (by omega)
    rw [pow_add,Nat.mul_comm] at f
    have bnd := Nat.mul_le_mul_left (2^40) (Nat.sub_le (2^s) 1)
    have u : 8*X<z := by
      have xv := Nat.two_pow_pos (hard k-3)
      change 0<X at xv
      omega
    rw [←power] at u
    exact bnd.trans_lt (f.trans_lt u)
  refine ⟨p.w0+3*2^p.upper*v,p.lower,p.upper,h,s,l,by omega,small,can,sp,gap,?_,raw.1,lg,?_,hg,?_,less⟩
  · rw [raw.1,power]
    omega
  · change run _ _=27*X-17
    omega
  · rw [run_add,run_add s l,mas,show run p.upper (3*(p.w0+3*2^p.upper*v))=27*X-17 by omega]
    exact meet

#print axioms long_turns
#print axioms earlier_after_turns
#print axioms paid_delayed_merger
end DelayedTurns
