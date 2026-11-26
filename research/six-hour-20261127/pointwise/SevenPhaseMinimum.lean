import ReflectedCycleMinimum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

/-! Exact ordinary inverse minima on the seven odd phases of the negative 17 cycle. -/
namespace SevenPhaseMinimum
open MultiBlockCompensation ReflectedCycleMinimum

def ordinaryCount (x : ℕ) : ℕ → ℕ
  | 0 => 0
  | d+1 => bit x+ordinaryCount (shortcut x) d

/-- Odd endpoints on actual shortcut trajectories count accelerated odd departures. -/
def Ancestor (R X y : ℕ) : Prop :=
  0<y ∧ y%2=1 ∧ ∃ d, shortcut^[d] y=X ∧ ordinaryCount y d≤R

private theorem reflected_pos {m : ℕ} (hm : 0<m) : 0<reflected m := by
  unfold reflected
  split <;> omega

private theorem growth (y d : ℕ) :
    3^(ordinaryCount y d)*y ≤ 2^d*(shortcut^[d] y) := by
  induction d generalizing y with
  | zero => simp [ordinaryCount]
  | succ d ih =>
    rw [ordinaryCount,pow_add,pow_succ,Function.iterate_succ_apply]
    have one : 3^bit y*y≤2*shortcut y := by
      by_cases he : y%2=0
      · simp [bit,shortcut,he]; omega
      · have ho : y%2=1 := by omega
        simp [bit,shortcut,ho]; omega
    calc
      3^bit y*3^ordinaryCount (shortcut y) d*y =
          3^ordinaryCount (shortcut y) d*(3^bit y*y) := by ring
      _≤3^ordinaryCount (shortcut y) d*(2*shortcut y) := Nat.mul_le_mul_left _ one
      _=2*(3^ordinaryCount (shortcut y) d*shortcut y) := by ring
      _≤2*(2^d*shortcut^[d] (shortcut y)) := Nat.mul_le_mul_left _ (ih _)
      _=_ := by ring

private theorem dual_step {y m u : ℕ} (hm : 0<m) (hs : y+m=2*u) :
    bit y=bit m ∧ shortcut y+reflected m=3^bit m*u := by
  have hp : y%2=m%2 := by omega
  by_cases he : m%2=0
  · have hx : y%2=0 := hp.trans he
    simp [bit,shortcut,reflected,he,hx]
    omega
  · have ho : m%2=1 := by omega
    have hx : y%2=1 := hp.trans ho
    simp [bit,shortcut,reflected,hx,ho]
    omega

/-- A physical word and its reflected companion have identical parity clocks. -/
theorem dual_transport (d y m c : ℕ) (hm : 0<m) (hs : y+m=2^d*c) :
    ordinaryCount y d=count m d ∧
    shortcut^[d] y+reflected^[d] m=3^(count m d)*c := by
  induction d generalizing y m c with
  | zero => simpa [ordinaryCount,count] using hs
  | succ d ih =>
    have two : y+m=2*(2^d*c) := by rw [hs,pow_succ]; ring
    obtain ⟨bits, pair⟩ := dual_step hm two
    have rest : shortcut y+reflected m=2^d*(3^bit m*c) := by rw [pair]; ring
    obtain ⟨cnt,ends⟩ := ih (shortcut y) (reflected m) (3^bit m*c)
      (reflected_pos hm) rest
    constructor
    · simp [ordinaryCount,count,bits,cnt]
    · rw [Function.iterate_succ_apply,Function.iterate_succ_apply,count,pow_add,ends]
      ring

/-- Any supplied ancestor through the available odd rank specializes to a
positive reflected ancestor, with an exact natural-integer displacement. -/
theorem project {R X t z d y : ℕ} (ht : 0<t) (hx : X+t=2*3^R*z)
    (hend : shortcut^[d] y=X) (qle : ordinaryCount y d≤R) (odd : y%2=1) :
    ∃ m, 0<m ∧ m%2=1 ∧ reflected^[d] m=t ∧
      count m d=ordinaryCount y d ∧ y+m=2^d*(2*3^(R-ordinaryCount y d)*z) := by
  let q := ordinaryCount y d
  let c := 2*3^(R-q)*z
  have qeq : 3^q*c=X+t := by
    dsimp [c]
    have pows : 3^q*3^(R-q)=(3:ℕ)^R := by rw [←pow_add]; congr 1; dsimp [q]; omega
    rw [hx,←pows]; ring
  have gy := growth y d
  rw [hend] at gy
  have strict : 3^q*y < 3^q*(2^d*c) := calc
    3^q*y ≤ 2^d*X := gy
    _<2^d*(X+t) := Nat.mul_lt_mul_of_pos_left (by omega) (by positivity)
    _=3^q*(2^d*c) := by rw [←qeq]; ring
  have ys : y<2^d*c := Nat.lt_of_mul_lt_mul_left strict
  let m := 2^d*c-y
  have pos : 0<m := by dsimp [m]; omega
  have sum : y+m=2^d*c := by dsimp [m]; omega
  have even : 2^d*c=2*(2^d*3^(R-q)*z) := by dsimp [c]; ring
  obtain ⟨cnt,ends⟩ := dual_transport d y m c pos sum
  rw [hend,←cnt] at ends
  change X+reflected^[d] m=3^q*c at ends
  rw [qeq] at ends
  exact ⟨m,pos,by omega,by omega,cnt.symm,sum⟩

private theorem count_add (m d e : ℕ) :
    count m (d+e)=count m d+count (reflected^[d] m) e := by
  induction d generalizing m with
  | zero => simp [count]
  | succ d ih =>
    rw [Nat.succ_add,count,count,Function.iterate_succ_apply,ih]
    omega

private theorem iter_append (d e m : ℕ) :
    reflected^[d+e] m=reflected^[e] (reflected^[d] m) := by
  rw [Nat.add_comm,Function.iterate_add_apply]

private theorem cycle (k : ℕ) :
    reflected^[11*k] 17=17 ∧ count 17 (11*k)=7*k := by
  induction k with
  | zero => simp [count]
  | succ k ih =>
    rw [Nat.mul_succ,Nat.mul_succ,count_add,iter_append]
    simp [ih.1,ih.2,period.1,period.2]

private theorem row_path {t a h : ℕ} (row : (t,a,h)∈phases) (k : ℕ) :
    reflected^[11*k+h] 17=t ∧ count 17 (11*k+h)=7*k+a := by
  obtain ⟨atT,atA,_,_⟩ := phases_calibrated _ row
  rw [count_add,iter_append]
  simp [cycle k,atT,atA]

private theorem row_bounds : ∀ v ∈ phases,
    0<v.1 ∧ v.1%2=1 ∧ v.2.1≤6 ∧ v.2.1≤v.2.2 ∧ v.2.2<11 ∧ v.1≤91 := by decide

private theorem phase_lookup : ∀ v ∈ phases, ∀ i : Fin 11,
    reflected^[i.val] 17=v.1 → i.val=v.2.2 := by decide

/-- No other phase of the same physical cycle can hit the specified terminal. -/
theorem rigid_cycle {t a h d : ℕ} (row : (t,a,h)∈phases) (endpt : reflected^[d] 17=t) :
    ∃ j, d=11*j+h ∧ count 17 d=7*j+a := by
  have decomp : d=11*(d/11)+d%11 := by omega
  rw [decomp,iter_append,(cycle (d/11)).1] at endpt
  have r := phase_lookup (t,a,h) row ⟨d%11,by omega⟩ endpt
  change d%11=h at r
  have exactD : d=11*(d/11)+h := by omega
  exact ⟨d/11,exactD,by simpa only [←exactD] using (row_path row (d/11)).2⟩

private theorem calibration {t a h : ℕ} (row : (t,a,h)∈phases) (k : ℕ) :
    128^(11*k+h)*potential t=2048^(7*k+a)*170^7 := by
  have atPhase := (phases_calibrated _ row).2.2.2
  change 128^h*potential t=2048^a*170^7 at atPhase
  have lap : (128:ℕ)^(11*k)=2048^(7*k) := by
    rw [pow_mul,pow_mul]
    norm_num
  calc
    _=128^(11*k)*(128^h*potential t) := by rw [pow_add]; ring
    _=2048^(7*k)*(2048^a*170^7) := by rw [lap,atPhase]
    _=_ := by rw [pow_add]; ring

/-- The reflected certificate bounds the real affine slope even when the
competing clock greatly exceeds the prescribed depth. The sharp exponent
loss here uses only six surplus odd steps. -/
theorem slope_margin {m t q d p H : ℕ}
    (safe : trapped t=false) (dest : reflected^[d] m=t) (cnt : count m d=q)
    (cal : 128^H*potential t=2048^p*170^7) (rank : q≤p+6) :
    5*m*2^H*3^q ≤ 102*2^d*3^p := by
  have all := path_bound m d (by rw [dest]; exact safe)
  rw [dest,cnt] at all
  have weighted : 2048^q*(9*m)^7*128^H≤128^d*2048^p*170^7 := calc
    _≤2048^q*potential m*128^H := by
      apply Nat.mul_le_mul_right
      apply Nat.mul_le_mul_left
      simpa only [Nat.mul_pow] using potential_floor m
    _≤128^d*potential t*128^H := Nat.mul_le_mul_right _ all
    _=128^d*(128^H*potential t) := by ring
    _=_ := by rw [cal]; ring
  have wr : (2048:ℚ)^q*(9*(m:ℚ))^7*128^H≤128^d*2048^p*170^7 := by
    exact_mod_cast weighted
  let c : ℚ := 2187/2048
  have hc : 1≤c := by norm_num [c]
  have cpos : 0<c := by norm_num [c]
  have adjust : (5/9:ℚ)^7*c^q≤(102/170:ℚ)^7*c^p := calc
    _≤(5/9:ℚ)^7*c^(p+6) := by
      apply mul_le_mul_of_nonneg_left (pow_le_pow_right₀ hc rank)
      norm_num
    _=((5/9:ℚ)^7*c^6)*c^p := by rw [pow_add]; ring
    _≤(102/170:ℚ)^7*c^p := by
      apply mul_le_mul_of_nonneg_right _ (le_of_lt (pow_pos cpos p))
      norm_num [c]
  have three (n : ℕ) : (2048:ℚ)^n*c^n=((3:ℚ)^n)^7 := calc
    _=(2048*c)^n := (mul_pow ..).symm
    _=((3:ℚ)^7)^n := by norm_num [c]
    _=_ := by rw [←pow_mul,←pow_mul,Nat.mul_comm]
  have two (n : ℕ) : (128:ℚ)^n=((2:ℚ)^n)^7 := calc
    _=((2:ℚ)^7)^n := by norm_num
    _=_ := by rw [←pow_mul,←pow_mul,Nat.mul_comm]
  have ans : (5*(m:ℚ)*2^H*3^q)^7≤(102*2^d*3^p)^7 := calc
    _=((5/9:ℚ)^7*c^q)*((2048:ℚ)^q*(9*(m:ℚ))^7*128^H) := by
      simp only [mul_pow]
      rw [←three q,two H]
      ring
    _≤((102/170:ℚ)^7*c^p)*((128:ℚ)^d*2048^p*170^7) := by
      exact mul_le_mul adjust wr (by positivity) (by positivity)
    _=_ := by
      simp only [mul_pow]
      rw [←three p,two d]
      ring
  have powers : (5*m*2^H*3^q)^7≤(102*2^d*3^p)^7 := by exact_mod_cast ans
  exact (Nat.pow_le_pow_iff_left (by decide : 7≠0)).mp powers

private theorem transfer_margin {m V Y C d H q p : ℕ}
    (scaled : 5*m*2^H*3^q≤102*2^d*3^p)
    (ref : 3^p*V=2^H*C) (other : 3^q*Y=2^d*C) :
    5*m*V≤102*Y := by
  apply Nat.le_of_mul_le_mul_left (c:=3^p*3^q)
  · calc
      3^p*3^q*(5*m*V)=5*m*(3^p*V)*3^q := by ring
      _=(5*m*2^H*3^q)*C := by rw [ref]; ring
      _≤(102*2^d*3^p)*C := Nat.mul_le_mul_right C scaled
      _=102*(2^d*C)*3^p := by ring
      _=_ := by rw [←other]; ring
  · positivity

private theorem small_reflected : ∀ i : Fin 21, i.val%2=1 →
    trapped i.val=false → i.val=17 := by decide

private theorem not_trapped {m d : ℕ} (safe : trapped (reflected^[d] m)=false) :
    trapped m=false := by
  induction d generalizing m with
  | zero => exact safe
  | succ d ih =>
    rw [Function.iterate_succ_apply] at safe
    have next := ih safe
    by_cases lt : m<65
    · have test : ∀ j : Fin 65, trapped (reflected j.val)=false → trapped j.val=false := by decide
      exact test ⟨m,lt⟩ next
    · simp [trapped,lt]

private theorem cost_at_cycle {j k a h R : ℕ} (jk : j≤k) (rank : 7*k+a≤R) :
    2^(11*k+h)*3^(R-(7*k+a)) ≤ 2^(11*j+h)*3^(R-(7*j+a)) := by
  let e := k-j
  have sH : 11*k+h=(11*j+h)+11*e := by dsimp [e]; omega
  have sQ : R-(7*j+a)=7*e+(R-(7*k+a)) := by dsimp [e]; omega
  have factor : (2:ℕ)^(11*e)≤3^(7*e) := by
    rw [pow_mul,pow_mul]
    exact Nat.pow_le_pow_left (by decide) e
  rw [sH,sQ,pow_add 2 _ (11*e),pow_add 3 (7*e) _]
  calc
    _≤2^(11*j+h)*3^(7*e)*3^(R-(7*k+a)) :=
      Nat.mul_le_mul_right _ (Nat.mul_le_mul_left _ factor)
    _=_ := by ring

private theorem precise_displacement (q R d z : ℕ) (rank : q≤R) :
    3^q*(2^d*(2*3^(R-q)*z))=2^d*(2*3^R*z) := by
  have factor : (3:ℕ)^q*3^(R-q)=3^R := by rw [←pow_add]; congr 1; omega
  rw [←factor]
  ring

/-- The integer expression for the displacement above the reflected start. -/
def displacement (d q R z : ℕ) := 2^d*(2*3^(R-q)*z)

private theorem displacement_large {p H R z : ℕ} (hr : 7≤R) (hz : 0<z)
    (ph : p≤H) (pr : p≤R) : 256≤displacement H p R z := by
  have add : R+1=p+(R-p)+1 := by omega
  calc
    256≤2^(R+1) := Nat.pow_le_pow_right (show (2:ℕ)>0 by decide) (show 8≤R+1 by omega)
    _=2^p*(2*2^(R-p)*1) := by rw [add,pow_succ,pow_add]; ring
    _≤2^H*(2*3^(R-p)*z) := by
      apply Nat.mul_le_mul (Nat.pow_le_pow_right (by decide) ph)
      exact Nat.mul_le_mul (Nat.mul_le_mul_left _ (Nat.pow_le_pow_left (by decide) _)) hz

private theorem phase_target {t a h R z : ℕ} (row : (t,a,h)∈phases) (hr : 7≤R) (hz : 0<z) :
    (2*3^R*z-t)+t=2*3^R*z := by
  have cap := (row_bounds _ row).2.2.2.2.2
  change t≤91 at cap
  have big : 91≤2*3^R*z := calc
    91≤2*(3:ℕ)^7*1 := by decide
    _≤2*3^R*z := Nat.mul_le_mul (Nat.mul_le_mul_left _ (Nat.pow_le_pow_right (by decide) hr)) hz
  omega

private theorem positive_margin {m V y : ℕ} (mlo : 21≤m) (large : 256≤V)
    (bound : 5*m*V≤102*(y+m)) : V-17<y := by
  obtain ⟨u,hu⟩ := Nat.exists_eq_add_of_le mlo
  obtain ⟨v,hv⟩ := Nat.exists_eq_add_of_le large
  have strict : 102*(V+m)<5*m*V+102*17 := by
    rw [hu,hv]
    nlinarith [Nat.zero_le (u*v)]
  omega

/-- The least pointwise source among all positive odd ancestors, with unrestricted
physical time, through the stated odd budget. The budget may leave six steps unused. -/
theorem exact_minimum {t a h R z : ℕ} (row : (t,a,h)∈phases) (hr : 7≤R) (hz : 0<z) :
    let k := (R-a)/7
    let X := 2*3^R*z-t
    let V := displacement (11*k+h) (7*k+a) R z
    IsLeast {y : ℕ | Ancestor R X y} (V-17) := by
  let k := (R-a)/7
  let p := 7*k+a
  let H := 11*k+h
  let X := 2*3^R*z-t
  let V := displacement H p R z
  change IsLeast {y : ℕ | Ancestor R X y} (V-17)
  obtain ⟨tpos,_,amax,ah,_,_⟩ := row_bounds _ row
  change 0<t at tpos
  change a≤6 at amax
  change a≤h at ah
  have rank : p≤R := by dsimp [p,k]; omega
  have slack : R≤p+6 := by dsimp [p,k]; omega
  have ph : p≤H := by dsimp [p,H]; omega
  have large : 256≤V := displacement_large hr hz ph rank
  have target : X+t=2*3^R*z := phase_target row hr hz
  have even : V=2*(2^H*3^(R-p)*z) := by dsimp [V,displacement]; ring
  have odd : (V-17)%2=1 := by omega
  have lifted := dual_transport H (V-17) 17 (2*3^(R-p)*z) (by decide)
    (show V-17+17=2^H*(2*3^(R-p)*z) by change V-17+17=V; omega)
  have atT : reflected^[H] 17=t := (row_path row k).1
  have atP : count 17 H=p := (row_path row k).2
  rw [atT,atP] at lifted
  have finish : 3^p*(2*3^(R-p)*z)=2*3^R*z := by
    simpa only [pow_zero,one_mul] using precise_displacement p R 0 z rank
  rw [finish,←target] at lifted
  constructor
  · exact ⟨by omega,odd,H,by omega,lifted.1.le.trans rank⟩
  · intro y hy
    obtain ⟨_,yo,d,dy,qr⟩ := hy
    let q := ordinaryCount y d
    obtain ⟨m,mp,mo,dest,cnt,sum⟩ := project tpos target dy qr yo
    change count m d=q at cnt
    change y+m=displacement d q R z at sum
    have safe := (phases_calibrated _ row).2.2.1
    change trapped t=false at safe
    by_cases ml : 21≤m
    · have bound := slope_margin safe dest cnt (calibration row k)
        (show q≤7*k+a+6 by change q≤p+6; dsimp [q]; omega)
      have oth : 3^q*(y+m)=2^d*(2*3^R*z) := by
        rw [sum]; exact precise_displacement q R d z qr
      have ref : 3^p*V=2^H*(2*3^R*z) := precise_displacement p R H z rank
      exact (positive_margin ml large (transfer_margin bound ref oth)).le
    · have safem := not_trapped (show trapped (reflected^[d] m)=false by rw [dest]; exact safe)
      have m17 := small_reflected ⟨m,by omega⟩ mo safem
      change m=17 at m17
      subst m
      obtain ⟨j,jd,jq⟩ := rigid_cycle row dest
      have qeq : q=7*j+a := cnt.symm.trans jq
      have jk : j≤k := by dsimp [q] at qeq; dsimp [k]; omega
      have costs := cost_at_cycle (a:=a) (h:=h) jk rank
      have gap : V≤y+17 := calc
        V=(2^(11*k+h)*3^(R-(7*k+a)))*(2*z) := by dsimp [V,H,p,displacement]; ring
        _≤(2^(11*j+h)*3^(R-(7*j+a)))*(2*z) := Nat.mul_le_mul_right _ costs
        _=displacement d q R z := by rw [jd,qeq]; unfold displacement; ring
        _=y+17 := sum.symm
      omega

end SevenPhaseMinimum

#print axioms SevenPhaseMinimum.reflected_pos
#print axioms SevenPhaseMinimum.growth
#print axioms SevenPhaseMinimum.dual_step
#print axioms SevenPhaseMinimum.dual_transport
#print axioms SevenPhaseMinimum.project
#print axioms SevenPhaseMinimum.count_add
#print axioms SevenPhaseMinimum.iter_append
#print axioms SevenPhaseMinimum.cycle
#print axioms SevenPhaseMinimum.row_path
#print axioms SevenPhaseMinimum.row_bounds
#print axioms SevenPhaseMinimum.phase_lookup
#print axioms SevenPhaseMinimum.rigid_cycle
#print axioms SevenPhaseMinimum.calibration
#print axioms SevenPhaseMinimum.slope_margin
#print axioms SevenPhaseMinimum.transfer_margin
#print axioms SevenPhaseMinimum.small_reflected
#print axioms SevenPhaseMinimum.not_trapped
#print axioms SevenPhaseMinimum.cost_at_cycle
#print axioms SevenPhaseMinimum.precise_displacement
#print axioms SevenPhaseMinimum.displacement_large
#print axioms SevenPhaseMinimum.phase_target
#print axioms SevenPhaseMinimum.positive_margin
#print axioms SevenPhaseMinimum.exact_minimum
