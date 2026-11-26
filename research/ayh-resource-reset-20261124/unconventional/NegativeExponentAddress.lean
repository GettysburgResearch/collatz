import AllMersenneCarries
import DyadicPowerPrecision
import Mathlib.Tactic.Ring

/-! All earlier ternary peaks are excluded at independent ordinary clocks
while the top still follows its signed orbit from exponent -1. -/
set_option autoImplicit false
set_option warningAsError true

namespace NegativeExponentAddress
open CollatzReverseBasin CollatzMersenneParity CollatzAllMersenneCarries

private theorem single {p : Nat} {c : Int} (w : Carry 1 p c) (eqn : c= -1) : p=0 := by
  cases w with
  | even w => cases w; rfl
  | odd w => cases w; norm_num at eqn

/-- The only ways to finish with carry -1 have zero or one odd input. -/
theorem minus_one_grade {t p : Nat} {c : Int} (w : Carry t p c) (val : c= -1) : p≤1 := by
  induction w with
  | start => omega
  | even _ ih => exact ih val
  | @odd t p c w _ =>
    cases t with
    | zero => simp at val; omega
    | succ t =>
      have oddc : c%2=1 := by rw [pow_succ] at val; omega
      have negc : c<0 := by
        have z : 0<(2:Int)^(t+1) := by positivity
        omega
      have ce:=negativeOdd w negc oddc
      subst c
      have e : (2:Int)^(t+1)=2^1 := by omega
      have h:=Nat.pow_right_injective (by decide : 2≤(2:Nat))
      have idx : t+1=1 := h (by exact_mod_cast e)
      cases t with
      | zero => have g:=single w rfl; omega
      | succ t => omega

private theorem carry_bound {t p : Nat} {c : Int} (w : Carry t p c) :
    -(3:Int)^t≤c ∧ c≤3^t-2^t := by
  induction w with
  | start => norm_num
  | @even t p c _ ih =>
    have z : (2:Int)^t≤3^t := pow_le_pow_left₀ (by decide) (by decide) t
    have a : 0<(3:Int)^t := by positivity
    rw [pow_succ,pow_succ]; omega
  | @odd t p c _ ih =>
    have a : 0<(2:Int)^t := by positivity
    rw [pow_succ,pow_succ]; omega

private theorem clock_height (t x : Nat) : atClock t x+1≤3^t*(x+1) := by
  induction t generalizing x with
  | zero => simp [atClock]
  | succ t ih =>
    have step : shortcut x+1≤3*(x+1) := by unfold shortcut; split <;> omega
    calc
      _ ≤ 3^t*(shortcut x+1) := ih _
      _ ≤ 3^t*(3*(x+1)) := Nat.mul_le_mul_left _ step
      _ = _ := by rw [pow_succ]; ring

private theorem two_grade (i t a b : Nat)
    (h : (2:Nat)^i*3^a=2^t*3^b) : i=t ∧ a=b := by
  have pair (i t a b : Nat) (h : (2:Nat)^i*3^a=2^t*3^b) : i≤t := by
    by_contra! bad
    obtain ⟨u,hu⟩ : ∃ u, i=t+(u+1) := ⟨i-t-1,by omega⟩
    rw [hu,pow_add,Nat.mul_assoc] at h
    have ec:=Nat.eq_of_mul_eq_mul_left (by positivity : 0<(2:Nat)^t) h
    obtain ⟨v,hv⟩:=Odd.pow (by decide : Odd (3:Nat)) (n:=b)
    rw [pow_succ,hv] at ec
    have ee : (2:Nat)^u*2*3^a=2*(2^u*3^a) := by ring
    rw [ee] at ec
    omega
  have eqn:=Nat.le_antisymm (pair _ _ _ _ h) (pair _ _ _ _ h.symm)
  subst t
  exact ⟨rfl,Nat.pow_right_injective (by decide : 2≤(3:Nat))
    (Nat.eq_of_mul_eq_mul_left (by positivity : 0<(2:Nat)^i) h)⟩

private theorem separated_factor {i t n p : Nat} {a c : Int} (w : Carry t p c)
    (large : i+t+1<n) (lead : (3:Int)^n*a=2^t+2^i*c) : a=0 := by
  have cb:=carry_bound w
  have ii : (2:Int)^i≤3^i := pow_le_pow_left₀ (by decide) (by decide) i
  have tt : (2:Int)^t≤3^t := pow_le_pow_left₀ (by decide) (by decide) t
  have ti : 0<(2:Int)^i := by positivity
  have pt : 0<(3:Int)^t := by positivity
  have pi : 0<(3:Int)^i := by positivity
  have dom : 3^i*(3:Int)^t*3 < 3^n := by
    rw [←pow_add,←pow_succ]; exact pow_lt_pow_right₀ (by decide) large
  have oneI : 1≤(3:Int)^i := one_le_pow₀ (by decide)
  have lc : -(3:Int)^n < 2^t+2^i*c ∧ 2^t+2^i*c<3^n := by
    have non : 0≤(2:Int)^t := by positivity
    have P : 0<(3:Int)^i*3^t := mul_pos pi pt
    have low:=mul_le_mul_of_nonneg_left cb.1 (le_of_lt ti)
    have high:=mul_le_mul_of_nonneg_left (show c≤(3:Int)^t by omega) (le_of_lt ti)
    have q:=mul_le_mul_of_nonneg_right ii (le_of_lt pt)
    have r:=mul_le_mul_of_nonneg_right oneI (le_of_lt pt)
    constructor <;> nlinarith only [low,high,q,r,tt,dom,non,P]
  have az : a=0 := by
    by_contra h
    rcases lt_or_gt_of_ne h with neg|pos
    · have := mul_le_mul_of_nonneg_left (show a≤ -1 by omega) (show 0≤(3:Int)^n by positivity)
      nlinarith only [this,lc.1,lead]
    · have := mul_le_mul_of_nonneg_left (show 1≤a by omega) (show 0≤(3:Int)^n by positivity)
      nlinarith only [this,lc.2,lead]
  exact az

/-- Any ordinary endpoint with upper affine numerator 3^(j+1)-1 has no
meeting with any earlier peak whose lower clock satisfies the height margin. -/
theorem separated_endpoint (i t j n y : Nat) (earlier : n<j)
    (margin : 2*(i+t+1)<j) (upper : 2^i*y+1=3^(j+1))
    (lower : atClock t (3^n-1)=y) : False := by
  have ht:=clock_height t (3^n-1)
  have hp : 0<(3:Nat)^n := by positivity
  rw [lower,show (3:Nat)^n-1+1=3^n by omega,←pow_add] at ht
  have hi : (2:Nat)^i≤3^i := pow_le_pow_left₀ (by decide) (by decide) i
  have zi : 0<(2:Nat)^i := by positivity
  have upperBound : (3:Nat)^(j+1)≤3^(i+(t+n)) := calc
    _ = 2^i*y+1 := upper.symm
    _ ≤ 2^i*(y+1) := by nlinarith only [zi]
    _ ≤ 3^i*3^(t+n) := Nat.mul_le_mul hi ht
    _ = _ := (pow_add _ _ _).symm
  have expo : j+1≤i+(t+n) := (pow_le_pow_iff_right₀ (by decide : 1<(3:Nat))).mp upperBound
  have large : i+t+1<n := by omega
  obtain ⟨p,c,w,e⟩:=physical n t
  rw [lower] at e
  let a : Int := 2^t*3^(j+1-n)-2^i*3^p
  have jj : n+(j+1-n)=j+1 := by omega
  have castu : (2:Int)^i*y+1=3^(j+1) := by exact_mod_cast upper
  have lead : (3:Int)^n*a=2^t+2^i*c := by
    dsimp [a]
    have e1 : (3:Int)^n*3^(j+1-n)=3^(j+1) := by rw [←pow_add,jj]
    rw [pow_add] at e
    calc
      _ = (2:Int)^t*(3^n*3^(j+1-n))-2^i*(3^n*3^p) := by ring
      _ = _ := by rw [e1,show (3:Int)^n*3^p=2^t*y-c by omega,←castu]; ring
  have az:=separated_factor w large lead
  have ti : 0<(2:Int)^i := by positivity
  have hh : (2:Nat)^t*3^(j+1-n)=2^i*3^p := by
    exact_mod_cast (sub_eq_zero.mp az : (2:Int)^t*3^(j+1-n)=2^i*3^p)
  obtain ⟨eqi,eqp⟩:=two_grade _ _ _ _ hh
  subst t
  rw [az,mul_zero] at lead
  have cv : c= -1 := by
    have e0 : (2:Int)^i*(c+1)=0 := by nlinarith only [lead]
    rcases mul_eq_zero.mp e0 with z|z <;> omega
  have := minus_one_grade w cv
  omega


private theorem clock_add (h t x : Nat) : atClock (h+t) x=atClock t (atClock h x) := by
  induction h generalizing x with
  | zero => simp [atClock]
  | succ h ih => simpa [Nat.succ_add,atClock] using ih (shortcut x)

private theorem halves (r y : Nat) : atClock r (2^r*y)=y := by
  induction r with
  | zero => simp [atClock]
  | succ r ih =>
    have st : shortcut (2^(r+1)*y)=2^r*y := by
      rw [pow_succ,show (2:Nat)^r*2*y=2*(2^r*y) by ring]
      unfold shortcut
      split <;> omega
    change atClock r (shortcut (2^(r+1)*y))=y
    rw [st,ih]

private theorem residue (m : Nat) : (3:Nat)^(11+162*m)%4=3 := by
  have t : (3:Nat)^162 ≡ 1 [MOD 4] := by decide +kernel
  have p:=t.pow m
  have z : (3:Nat)^11 ≡ 3 [MOD 4] := by decide +kernel
  simpa [pow_add,pow_mul,one_pow,Nat.ModEq] using z.mul p

private theorem top_form (j i : Nat) (rj : (3:Nat)^j%4=3) (h : 2≤i)
    (powd : 2^i ∣ 3^(j+1)-1) :
    2^i*atClock i (3^j-1)+1=3^(j+1) := by
  let r:=i-2
  have fi : i=2+r := by dsimp [r]; omega
  obtain ⟨y,hy⟩:=powd
  have pj : 0<(3:Nat)^j := by positivity
  have z : (3:Nat)^(j+1)=3^j*3 := pow_succ _ _
  have b2 : 4*atClock 2 (3^j-1)+1=3^(j+1) := by
    rw [z]
    change 4*shortcut (shortcut (3^j-1))+1=3^j*3
    have s : shortcut (3^j-1)=(3^j-1)/2 := by unfold shortcut; split <;> omega
    rw [s]
    unfold shortcut
    split <;> omega
  have f2 : atClock 2 (3^j-1)=2^r*y := by
    rw [fi,pow_add (2:Nat) 2 r] at hy
    simp only [show (2:Nat)^2=4 by decide] at hy
    rw [show 4*2^r*y=4*(2^r*y) by ring] at hy
    omega
  rw [fi,clock_add,f2,halves]
  rw [fi] at hy
  rw [z] at *
  omega

private theorem exponent_div (m k : Nat) (condition : 2^k ∣ 27*m+2) :
    2^(k+3) ∣ 3^(11+162*m+1)-1 := by
  have q:=DyadicPowerPrecision.precision 9 1 1 0 (3*(27*m+2)) k (by decide) (by decide)
  have h:=q.mpr (dvd_mul_of_dvd_right condition 3)
  simp only [Nat.zero_add,pow_zero] at h
  rw [show (9:Nat)=3^2 by decide,←pow_mul,
    show 2*(3*(27*m+2))=11+162*m+1 by ring,show 1+k+2=k+3 by omega] at h
  exact h

private theorem double_k (k : Nat) : 2*k≤2^k := by
  induction k with
  | zero => decide
  | succ k ih =>
    cases k with
    | zero => decide
    | succ k =>
      have z : 2≤(2:Nat)^(k+1) := by
        exact_mod_cast (pow_le_pow_right₀ (by decide : 1≤(2:Nat)) (show 1≤k+1 by omega))
      rw [pow_succ (2:Nat) (k+1)]; omega

/-- Every original m≥1 and every earlier peak. A merger has to outlast the
top zero-shadow or use more than one third of j clocks on the lower arm.
The statement uses a divisor so every requested depth can be supplied. -/
theorem all_earlier (m k i t n : Nat) (pos : 0<m) (condition : 2^k ∣ 27*m+2)
    (earlier : n<11+162*m) (it : i≤k+3) (tt : 3*t≤11+162*m) :
    atClock i (3^(11+162*m)-1)≠atClock t (3^n-1) := by
  intro merge
  let j:=11+162*m
  let v:=2-i
  have two : 2≤i+v := by dsimp [v]; omega
  have lim : i+v≤k+3 := by dsimp [v]; omega
  have times : 2*(i+v+(t+v)+1)<j := by
    have hk:=(double_k k).trans (Nat.le_of_dvd (by omega : 0<27*m+2) condition)
    dsimp [v,j]; omega
  have top:=top_form j (i+v) (residue m) two
    ((pow_dvd_pow 2 lim).trans (exponent_div m k condition))
  apply separated_endpoint (i+v) (t+v) j n _ earlier times top
  rw [clock_add,clock_add]
  exact congrArg (atClock v) merge.symm


/-- An explicit positive ordinary representative of every requested
precision. The affine recurrence follows from 2^18=1+27*9709. -/
def representative : Nat → Nat
  | 0 => 19418
  | s+1 => 262144*representative s+19418

theorem representative_form (k : Nat) :
    27*representative k+2=2^(18*(k+1)+1) := by
  induction k with
  | zero => decide +kernel
  | succ k ih =>
    rw [show 18*(k+1+1)+1=(18*(k+1)+1)+18 by omega,pow_add,←ih]
    simp only [representative]
    ring

theorem progression (k r : Nat) :
    let m:=representative k+2^k*r
    2^k ∣ 27*m+2 := by
  have h : 2^k ∣ 27*representative k+2 := by
    rw [representative_form]
    exact pow_dvd_pow 2 (by omega)
  dsimp
  rw [show 27*(representative k+2^k*r)+2=(27*representative k+2)+2^k*(27*r) by ring]
  exact Nat.dvd_add h (dvd_mul_right _ _)

theorem not_perfect_power (m k : Nat) (depth : 2≤k) (condition : 2^k ∣ 27*m+2)
    (b h : Nat) (multiple : 2≤h) : m≠b^h := by
  have four : 4∣27*m+2 := (pow_dvd_pow 2 depth).trans condition
  have residue : m%4=2 := by omega
  intro eqn
  have hb : b%2=0 ∨ b%2=1 := by omega
  rcases hb with eb|ob
  · obtain ⟨v,hv⟩ : ∃ v, b=2*v := ⟨b/2,by omega⟩
    have f : 4∣b^h := by
      rw [hv,mul_pow]
      exact dvd_mul_of_dvd_left (pow_dvd_pow 2 multiple) _
    omega
  · have bo : Odd b := ⟨b/2,by omega⟩
    obtain ⟨v,hv⟩:=bo.pow (n:=h)
    omega

private theorem physical_base (B t : Nat) (pos : 0<B) :
    ∃ p c, Carry t p c ∧ (2:Int)^t*atClock t (B-1)=B*3^p+c ∧
          2^p*(atClock t (B-1)+1)≤3^p*B := by
  induction t with
  | zero =>
    refine ⟨0,-1,.start,?_⟩
    simp [atClock,Nat.cast_sub (by omega : 1≤B),sub_eq_add_neg]
    omega
  | succ t ih =>
    obtain ⟨p,c,w,e,g⟩:=ih
    let x:=atClock t (B-1)
    change (2:Int)^t*x=_ at e
    change 2^p*(x+1)≤3^p*B at g
    have clk : atClock (t+1) (B-1)=shortcut x := clock_add t 1 _
    by_cases h : x%2=0
    · have eqn : (2:Int)*shortcut x=x := by unfold shortcut; split <;> omega
      refine ⟨p,c,.even w,by rw [clk,pow_succ,mul_assoc,eqn,e],?_⟩
      rw [clk]
      have z : shortcut x+1≤x+1 := by unfold shortcut; split <;> omega
      exact (Nat.mul_le_mul_left _ z).trans g
    · have eqn : (2:Int)*shortcut x=3*x+1 := by unfold shortcut; split <;> omega
      refine ⟨p+1,3*c+2^t,.odd w,?_,?_⟩
      · rw [clk,pow_succ,mul_assoc,eqn,pow_succ]; nlinarith only [e]
      · have z : 2*(shortcut x+1)=3*(x+1) := by unfold shortcut; split <;> omega
        rw [clk,pow_succ,pow_succ,Nat.mul_assoc,z]
        nlinarith only [g]

private theorem precise_height (t x : Nat) : 2^t*(atClock t x+1)≤3^t*(x+1) := by
  induction t generalizing x with
  | zero => simp [atClock]
  | succ t ih =>
    have step : 2*(shortcut x+1)≤3*(x+1) := by unfold shortcut; split <;> omega
    calc
      _ = 2*(2^t*(atClock t (shortcut x)+1)) := by rw [atClock,pow_succ]; ring
      _ ≤ 2*(3^t*(shortcut x+1)) := Nat.mul_le_mul_left _ (ih _)
      _ = 3^t*(2*(shortcut x+1)) := by ring
      _ ≤ 3^t*(3*(x+1)) := Nat.mul_le_mul_left _ step
      _ = _ := by rw [pow_succ]; ring

private theorem odd_clock (i t a b : Nat) (ao : Odd a) (bo : Odd b)
    (h : (2:Nat)^i*a=2^t*b) : i=t := by
  have side (i t a b : Nat) (bo : Odd b) (h : (2:Nat)^i*a=2^t*b) : i≤t := by
    by_contra! bad
    obtain ⟨u,hu⟩ : ∃ u, i=t+(u+1) := ⟨i-t-1,by omega⟩
    rw [hu,pow_add,Nat.mul_assoc] at h
    have ec:=Nat.eq_of_mul_eq_mul_left (by positivity : 0<(2:Nat)^t) h
    obtain ⟨v,hv⟩:=bo
    rw [pow_succ,hv,show (2:Nat)^u*2*a=2*(2^u*a) by ring] at ec
    omega
  exact Nat.le_antisymm (side _ _ _ _ bo h) (side _ _ _ _ ao h.symm)

private theorem cofactor_height (i t j n b y : Nat) (nj : n<j) (cheap : b<2^(j-n))
    (bp : 0<b) (upper : 2^i*y+1=3^(j+1)) (lower : atClock t (b*3^n-1)=y) :
    j-n<t+2*i := by
  let d:=j-n
  have jn : j=n+d := by dsimp [d]; omega
  have ht:=precise_height t (b*3^n-1)
  have pp : 0<b*(3:Nat)^n := by positivity
  rw [lower,show b*3^n-1+1=b*3^n by omega] at ht
  have up : (3:Nat)^(j+1)≤2^i*(y+1) := by
    rw [←upper]; have z : 0<(2:Nat)^i := by positivity
    nlinarith only [z]
  have both : (2:Nat)^t*3^(j+1) ≤ 2^i*(3^t*(b*3^n)) := calc
    _ ≤ 2^t*(2^i*(y+1)) := Nat.mul_le_mul_left _ up
    _ = 2^i*(2^t*(y+1)) := by ring
    _ ≤ _ := Nat.mul_le_mul_left _ ht
  by_contra! bad
  obtain ⟨u,du⟩ : ∃ u, d=t+2*i+u := ⟨d-t-2*i,by dsimp [d] at *; omega⟩
  have bound : (2:Nat)^i*(3^t*(b*3^n))≤2^t*3^j := calc
    _ ≤ 2^i*(3^t*(2^d*3^n)) :=
      Nat.mul_le_mul_left _ (Nat.mul_le_mul_left _ (Nat.mul_le_mul_right _ (le_of_lt cheap)))
    _ = (2^t*3^t*3^n)*((2*(2^2))^i*2^u) := by simp only [du,pow_add,pow_mul,mul_pow]; ring
    _ ≤ (2^t*3^t*3^n)*((3^2)^i*3^u) :=
      Nat.mul_le_mul_left _ (Nat.mul_le_mul (pow_le_pow_left₀ (by decide) (by decide) _)
        (pow_le_pow_left₀ (by decide) (by decide) _))
    _ = _ := by simp only [jn,du,pow_add,pow_mul]; ring
  have lt : (2:Nat)^t*3^j<2^t*3^(j+1) :=
    Nat.mul_lt_mul_of_pos_left (pow_lt_pow_right₀ (by decide) (by omega)) (by positivity)
  omega

/-- Every cheaper source, with arbitrary odd cofactor on its canonical
initial ascent, obeys the same two unequal post-ascent deadlines. -/
theorem all_smaller (m k i t n b : Nat) (pos : 0<m) (condition : 2^k ∣ 27*m+2)
    (earlier : n<11+162*m) (oddB : Odd b) (cheap : b<2^(11+162*m-n))
    (it : i≤k+3) (tt : 3*t≤11+162*m) :
    atClock i (3^(11+162*m)-1)≠atClock (n+t) (2^n*b-1) := by
  intro merge
  let j:=11+162*m
  let v:=2-i
  let I:=i+v
  let H:=t+v
  have hI : 2≤I := by dsimp [I,v]; omega
  have lim : I≤k+3 := by dsimp [I,v]; omega
  have bounds : 3*I+2*H+1<j := by
    have hk:=(double_k k).trans (Nat.le_of_dvd (by omega : 0<27*m+2) condition)
    dsimp [I,H,v,j]; omega
  have bp : 0<b := by obtain ⟨z,hz⟩:=oddB; omega
  rw [clock_add,ascent _ _ bp,Nat.mul_comm (3^n) b] at merge
  let y:=atClock I (3^j-1)
  have upper : 2^I*y+1=3^(j+1) := top_form j I (residue m) hI
    ((pow_dvd_pow 2 lim).trans (exponent_div m k condition))
  have lower : atClock H (b*3^n-1)=y := by
    dsimp [y,I,H,j]; rw [clock_add,clock_add]; exact congrArg (atClock v) merge.symm
  have dlim:=cofactor_height I H j n b y earlier cheap bp upper lower
  have large : I+H+1<n := by omega
  obtain ⟨p,c,w,e,_⟩:=physical_base (b*3^n) H (by positivity)
  rw [lower] at e
  push_cast at e
  let a : Int := 2^H*3^(j+1-n)-2^I*(b*3^p)
  have jj : n+(j+1-n)=j+1 := by omega
  have cu : (2:Int)^I*y+1=3^(j+1) := by exact_mod_cast upper
  have lead : (3:Int)^n*a=2^H+2^I*c := by
    dsimp [a]
    have e1 : (3:Int)^n*3^(j+1-n)=3^(j+1) := by rw [←pow_add,jj]
    calc
      _ = (2:Int)^H*(3^n*3^(j+1-n))-2^I*(b*3^n*3^p) := by ring
      _ = _ := by rw [e1,show (b:Int)*3^n*3^p=2^H*y-c by omega,←cu]; ring
  have az:=separated_factor w large lead
  have hh : (2:Nat)^H*3^(j+1-n)=2^I*(b*3^p) := by
    exact_mod_cast (sub_eq_zero.mp az : (2:Int)^H*3^(j+1-n)=2^I*(b*3^p))
  have eqI:=odd_clock _ _ _ _ ((by decide : Odd (3:Nat)).pow)
    (oddB.mul ((by decide : Odd (3:Nat)).pow)) hh
  rw [eqI] at hh lead
  have cl:=Nat.eq_of_mul_eq_mul_left (by positivity : 0<(2:Nat)^I) hh
  rw [az,mul_zero] at lead
  have cv : c= -1 := by
    have zero : (2:Int)^I*(c+1)=0 := by nlinarith only [lead]
    have nz : (2:Int)^I≠0 := by positivity
    rcases mul_eq_zero.mp zero with h|h <;> omega
  have grade:=minus_one_grade w cv
  have ep : (3:Nat)^p≤3^1 := pow_le_pow_right₀ (by decide) grade
  have bc : b<3^(j-n) := lt_of_lt_of_le cheap (pow_le_pow_left₀ (by decide) (by decide) _)
  have lo : b*3^p<3^(j-n)*3 := Nat.mul_lt_mul_of_lt_of_le bc ep (by positivity)
  rw [show j+1-n=(j-n)+1 by omega,pow_succ] at cl
  omega

private theorem split_twos (a : Nat) (positive : 0<a) :
    ∃ n b, a=2^n*b ∧ Odd b := by
  induction a using Nat.strong_induction_on with
  | h a ih =>
    by_cases odd : a%2=1
    · exact ⟨0,a,by simp,⟨a/2,by omega⟩⟩
    · obtain ⟨n,b,eqn,ob⟩:=ih (a/2) (by omega) (by omega)
      refine ⟨n+1,b,?_,ob⟩
      have aa : a=2*(a/2) := by omega
      calc
        _ = 2*(a/2) := aa
        _ = 2^(n+1)*b := by rw [eqn,pow_succ]; ring

/-- For each actual smaller start, its own canonical initial odd run is
chosen once before the bounds on either subsequent clock. -/
theorem pointwise (m k x : Nat) (positive : 0<m) (condition : 2^k ∣ 27*m+2)
    (small : x<2^(11+162*m)-1) :
    ∃ n b, x+1=2^n*b ∧ Odd b ∧ ∀ i t, i≤k+3 → 3*t≤11+162*m →
      atClock i (3^(11+162*m)-1)≠atClock (n+t) x := by
  obtain ⟨n,b,eqn,bo⟩:=split_twos (x+1) (by omega)
  have bp : 0<b := by obtain ⟨u,hu⟩:=bo; omega
  have bound : 2^n*b<2^(11+162*m) := by omega
  have nj : n<11+162*m := by
    by_contra! bad
    have g : (2:Nat)^(11+162*m)≤2^n := pow_le_pow_right₀ (by decide) bad
    have h:=Nat.mul_le_mul_left (2^n) (show 1≤b by omega)
    omega
  have cf : b<2^(11+162*m-n) := by
    have eq : n+(11+162*m-n)=11+162*m := by omega
    have h : 2^n*b<2^n*2^(11+162*m-n) := by rw [←pow_add,eq]; exact bound
    exact (Nat.mul_lt_mul_left (by positivity)).mp h
  refine ⟨n,b,eqn,bo,?_⟩
  intro i t hi ht
  have result:=all_smaller m k i t n b positive condition nj bo cf hi ht
  rwa [show 2^n*b-1=x by omega] at result

private theorem before_ascent (j n H I x b y : Nat) (small : x<2^j-1)
    (form : x+1=2^n*b) (bp : 0<b) (nj : n<j) (pre : H<n)
    (Ilo : 2≤I) (room : 5*I≤j) (upper : 2^I*y+1=3^(j+1))
    (lower : atClock H x=y) : False := by
  have np : n=H+(n-H) := by omega
  have formH : 2^H*(2^(n-H)*b)-1=x := by
    rw [←Nat.mul_assoc,←pow_add,←np]; omega
  have asc:=ascent H (2^(n-H)*b) (by positivity)
  rw [formH,lower] at asc
  have ap : 0<(3:Nat)^H*(2^(n-H)*b) := by positivity
  have yc : y+1=3^H*(2^(n-H)*b) := by omega
  have dvd1 : 3^H ∣ 2^I*(y+1) := by rw [yc]; exact dvd_mul_of_dvd_right (dvd_mul_right _ _) _
  have dvd2 : 3^H ∣ (3:Nat)^(j+1) := pow_dvd_pow 3 (by omega)
  have df:=Nat.dvd_sub dvd1 dvd2
  rw [←upper,Nat.mul_add,Nat.mul_one,show 2^I*y+2^I-(2^I*y+1)=2^I-1 by omega] at df
  have two : 2≤(2:Nat)^I := (pow_le_pow_right₀ (by decide : 1≤(2:Nat)) (show 1≤I by omega))
  have smallH:=Nat.le_of_dvd (by omega : 0<2^I-1) df
  have lh : (3:Nat)^H≤3^I := smallH.trans ((Nat.sub_le _ _).trans (pow_le_pow_left₀ (by decide) (by decide) _))
  have ht:=clock_height H x
  rw [lower] at ht
  have top : (3:Nat)^(j+1)≤2^I*(3^I*2^j) := calc
    _ = 2^I*y+1 := upper.symm
    _ ≤ 2^I*(y+1) := by rw [Nat.mul_add,Nat.mul_one]; omega
    _ ≤ _ := Nat.mul_le_mul_left _ (ht.trans (Nat.mul_le_mul lh (by omega)))
  obtain ⟨u,uj⟩ : ∃ u, j=5*I+u := ⟨j-5*I,by omega⟩
  have bound : (2:Nat)^I*(3^I*2^j)≤3^j := calc
    _ = (2*3*2^5)^I*2^u := by simp only [uj,pow_add,pow_mul,mul_pow]; ring
    _ ≤ (3^5)^I*3^u := Nat.mul_le_mul (pow_le_pow_left₀ (by decide) (by decide) _)
      (pow_le_pow_left₀ (by decide) (by decide) _)
    _ = _ := by rw [uj,pow_add,pow_mul]
  have order : (3:Nat)^j<3^(j+1) := pow_lt_pow_right₀ (by decide) (by omega)
  omega

/-- Complete ordinary clock interval from zero on every smaller source,
including all clocks before its own canonical ascent finishes. -/
theorem full_clock (m k x : Nat) (positive : 0<m) (condition : 2^k ∣ 27*m+2)
    (small : x<2^(11+162*m)-1) :
    ∃ n b, x+1=2^n*b ∧ Odd b ∧ ∀ i h, i≤k+3 → 3*h≤3*n+(11+162*m) →
      atClock i (3^(11+162*m)-1)≠atClock h x := by
  obtain ⟨n,b,form,bo,ex⟩:=pointwise m k x positive condition small
  refine ⟨n,b,form,bo,?_⟩
  intro i h hi hh merger
  by_cases post : n≤h
  · have hit:=ex i (h-n) hi (by omega)
    rw [show n+(h-n)=h by omega] at hit; contradiction
  · let j:=11+162*m
    let v:=2-i
    let I:=i+v
    let H:=h+v
    have hlo : 2≤I := by dsimp [I,v]; omega
    have lim : I≤k+3 := by dsimp [I,v]; omega
    have bp : 0<b := by obtain ⟨u,hu⟩:=bo; omega
    have nj : n<j := by
      by_contra! bad
      have g : (2:Nat)^j≤2^n := pow_le_pow_right₀ (by decide) bad
      have q:=Nat.mul_le_mul_left (2^n) (show 1≤b by omega)
      dsimp [j] at *; omega
    have late : atClock I (3^j-1)=atClock H x := by
      dsimp [I,H,j]; rw [clock_add,clock_add]; exact congrArg (atClock v) merger
    by_cases reached : n≤H
    · have add : n+(H-n)=H := by omega
      have limH : 3*(H-n)≤j := by dsimp [H,v,j] at *; omega
      exact (ex I (H-n) lim limH) (by rwa [add])
    · have rm : 5*I≤j := by
        have hk:=(double_k k).trans (Nat.le_of_dvd (by omega : 0<27*m+2) condition)
        dsimp [I,v,j]; omega
      have upper:=top_form j I (residue m) hlo ((pow_dvd_pow 2 lim).trans (exponent_div m k condition))
      exact before_ascent j n H I x b _ small form bp nj (by omega) hlo rm upper late.symm

private theorem grade_floor (I q j : Nat)
    (ineq : 2^q*3^(j+1)≤2^I*(3^q*2^j)) : j<q+2*I := by
  by_contra! h
  obtain ⟨u,ju⟩ : ∃ u, j=q+2*I+u := ⟨j-q-2*I,by omega⟩
  have bound : (2:Nat)^I*(3^q*2^j)≤2^q*3^j := calc
    _ = (2^q*3^q)*((2*2^2)^I*2^u) := by simp only [ju,pow_add,pow_mul,mul_pow]; ring
    _ ≤ (2^q*3^q)*((3^2)^I*3^u) := Nat.mul_le_mul_left _
      (Nat.mul_le_mul (pow_le_pow_left₀ (by decide) (by decide) _) (pow_le_pow_left₀ (by decide) (by decide) _))
    _ = _ := by simp only [ju,pow_add,pow_mul]; ring
  have ord : (2:Nat)^q*3^j<2^q*3^(j+1) := Nat.mul_lt_mul_of_pos_left
    (pow_lt_pow_right₀ (by decide) (by omega)) (by positivity)
  omega

private theorem post_margin (j n b I h y : Nat) (nj : n<j)
    (bo : Odd b) (cheap : b<2^(j-n)) (upper : 2^I*y+1=3^(j+1))
    (lower : atClock h (b*3^n-1)=y) (room : 3*I+h+1≤j) : False := by
  have bp : 0<b := by obtain ⟨u,hu⟩:=bo; omega
  obtain ⟨p,c,w,e,g⟩:=physical_base (b*3^n) h (by positivity)
  rw [lower] at e g
  push_cast at e
  let q:=n+p
  have grade : 2^q*(y+1)≤3^q*2^j := calc
    _ = 2^n*(2^p*(y+1)) := by dsimp [q]; rw [pow_add]; ring
    _ ≤ 2^n*(3^p*(b*3^n)) := Nat.mul_le_mul_left _ g
    _ = 3^q*(2^n*b) := by dsimp [q]; rw [pow_add]; ring
    _ ≤ _ := Nat.mul_le_mul_left _ (by
      have small:=Nat.mul_le_mul_left (2^n) (le_of_lt cheap)
      rwa [←pow_add,show n+(j-n)=j by omega] at small)
  have bnd : 2^q*3^(j+1)≤2^I*(3^q*2^j) := calc
    _ ≤ 2^q*(2^I*(y+1)) := Nat.mul_le_mul_left _ (by
      rw [←upper,Nat.mul_add,Nat.mul_one]
      have : 0<(2:Nat)^I := by positivity
      omega)
    _ = 2^I*(2^q*(y+1)) := by ring
    _ ≤ _ := Nat.mul_le_mul_left _ grade
  have gf:=grade_floor I q j bnd
  let D:=min (j+1) q
  have large : I+h+1<D := by dsimp [D]; omega
  have jd : D+(j+1-D)=j+1 := by dsimp [D]; omega
  have qd : D+(q-D)=q := by dsimp [D]; omega
  have cu : (2:Int)^I*y+1=3^(j+1) := by exact_mod_cast upper
  have ee : (3:Int)^q*b=2^h*y-c := by dsimp [q]; rw [pow_add]; nlinarith only [e]
  let A : Int:=2^h*3^(j+1-D)-2^I*(b*3^(q-D))
  have lead : (3:Int)^D*A=2^h+2^I*c := by
    dsimp [A]
    calc
      _ = (2:Int)^h*(3^D*3^(j+1-D))-2^I*(3^D*3^(q-D)*b) := by ring
      _ = _ := by rw [←pow_add,←pow_add,jd,qd,ee,←cu]; ring
  have az:=separated_factor w large lead
  have hh : (2:Nat)^h*3^(j+1-D)=2^I*(b*3^(q-D)) := by
    exact_mod_cast (sub_eq_zero.mp az : (2:Int)^h*3^(j+1-D)=2^I*(b*3^(q-D)))
  have eqI:=odd_clock _ _ _ _ ((by decide : Odd (3:Nat)).pow)
    (bo.mul ((by decide : Odd (3:Nat)).pow)) hh
  subst h
  rw [az,mul_zero] at lead
  have cv : c= -1 := by
    have zero : (2:Int)^I*(c+1)=0 := by nlinarith only [lead]
    have nz : (2:Int)^I≠0 := by positivity
    rcases mul_eq_zero.mp zero with h|h <;> omega
  have pg:=minus_one_grade w cv
  have hb : b*3^p<3^(j-n)*3 := Nat.mul_lt_mul_of_lt_of_le
    (lt_of_lt_of_le cheap (pow_le_pow_left₀ (by decide) (by decide) _))
    (show (3:Nat)^p≤3^1 from pow_le_pow_right₀ (by decide) pg) (by positivity)
  have ord := Nat.mul_lt_mul_of_pos_left hb (by positivity : 0<(3:Nat)^n)
  have eq : (3:Nat)^n*(3^(j-n)*3)=3^(j+1) := by
    rw [←mul_assoc,←pow_add,show n+(j-n)=j by omega,pow_succ]
  rw [eq] at ord
  have casto : (3:Int)^n*(b*3^p)<3^(j+1) := by exact_mod_cast ord
  nlinarith only [cv,cu,e,casto]

/-- For every cheaper ordinary start the lower deadline extends almost
one whole original ascent past its own initial odd run. -/
theorem full_margin (m k x : Nat) (positive : 0<m) (condition : 2^k ∣ 27*m+2)
    (small : x<2^(11+162*m)-1) :
    ∃ n b, x+1=2^n*b ∧ Odd b ∧ ∀ i h, i≤k+3 →
      3*i+h+11≤n+(11+162*m) →
      atClock i (3^(11+162*m)-1)≠atClock h x := by
  obtain ⟨n,b,form,bo,old⟩:=full_clock m k x positive condition small
  refine ⟨n,b,form,bo,?_⟩
  intro i h hi hh merger
  by_cases early : h≤n
  · exact old i h hi (by omega) merger
  · let j:=11+162*m
    let v:=2-i
    let I:=i+v
    let H:=h-n+v
    have hI : 2≤I := by dsimp [I,v]; omega
    have lim : I≤k+3 := by dsimp [I,v]; omega
    have room : 3*I+H+1≤j := by dsimp [I,H,v,j]; omega
    have bp : 0<b := by obtain ⟨u,hu⟩:=bo; omega
    have bound : 2^n*b<2^j := by dsimp [j]; omega
    have nj : n<j := by
      by_contra! bad
      have g : (2:Nat)^j≤2^n := pow_le_pow_right₀ (by decide) bad
      have q:=Nat.mul_le_mul_left (2^n) (show 1≤b by omega)
      omega
    have cheap : b<2^(j-n) := by
      have e : n+(j-n)=j := by omega
      have h : 2^n*b<2^n*2^(j-n) := by rw [←pow_add,e]; exact bound
      exact (Nat.mul_lt_mul_left (by positivity)).mp h
    have asn : atClock n x=b*3^n-1 := by
      have z:=ascent n b bp; rwa [show 2^n*b-1=x by omega,Nat.mul_comm (3^n) b] at z
    let y:=atClock I (3^j-1)
    have top:=top_form j I (residue m) hI ((pow_dvd_pow 2 lim).trans (exponent_div m k condition))
    apply post_margin j n b I H y nj bo cheap top _ room
    dsimp [y,I,H]
    rw [clock_add (h-n) v,clock_add i v,←asn,←clock_add n (h-n),show n+(h-n)=h by omega]
    exact congrArg (atClock v) merger.symm

private theorem phase_grade (q u j a : Nat) (uj : u≤j)
    (grow : 2^q*(3^u*2^(j-u)*a)<3^q*(2^j*a)) : u<q := by
  by_contra! bad
  obtain ⟨v,uv⟩ : ∃ v, u=q+v := ⟨u-q,by omega⟩
  let e:=j-u
  have je : j=u+e := by dsimp [e]; omega
  change 2^q*(3^u*2^e*a)<3^q*(2^j*a) at grow
  have big : 3^q*(2^j*a)≤2^q*(3^u*2^e*a) := calc
    _ = (3^q*2^q*2^e*a)*2^v := by rw [je,uv,pow_add (2:Nat) (q+v) e,pow_add (2:Nat) q v]; ring
    _ ≤ (3^q*2^q*2^e*a)*3^v := Nat.mul_le_mul_left _ (pow_le_pow_left₀ (by decide) (by decide) _)
    _ = _ := by rw [uv,pow_add]; ring
  omega

private theorem unit_mismatch (L a Y H U : Nat) (unit : ¬3∣a) (gt : U<H) :
    3^U*(2^L*a)≠3^H*Y := by
  have nz (k : Nat) : (2^k*a)%3≠0 := by
    induction k with
    | zero => simp only [pow_zero,one_mul]; omega
    | succ k ih =>
      rw [pow_succ,show (2:Nat)^k*2*a=(2^k*a)*2 by ring,Nat.mul_mod]
      omega
  intro eqn
  obtain ⟨v,hv⟩ : ∃ v, H=U+(v+1) := ⟨H-U-1,by omega⟩
  rw [hv,pow_add,Nat.mul_assoc] at eqn
  have sub:=Nat.eq_of_mul_eq_mul_left (by positivity : 0<(3:Nat)^U) eqn
  have mod:=nz L
  rw [sub,pow_succ,show (3:Nat)^v*3*Y=3*(3^v*Y) by ring] at mod
  omega

private theorem tight_carry {t p : Nat} {c : Int} (w : Carry t p c) :
    c<3^t-2^t := by
  induction w with
  | start => decide
  | @even t p c _ ih =>
    have h : (2:Int)^t≤3^t := pow_le_pow_left₀ (by decide) (by decide) t
    have z : 0<(3:Int)^t := by positivity
    rw [pow_succ,pow_succ]; omega
  | @odd t p c _ ih => rw [pow_succ,pow_succ]; omega

/-- Every ascent from a power of two times a ternary unit, every smaller
start, and every phase. The lower clock strictly exceeds the sum of the
source's own initial odd-run length and the target phase. -/
theorem prepeak_clock (j a x : Nat) (unit : ¬3∣a) (small : x<2^j*a-1) :
    ∃ n b, x+1=2^n*b ∧ Odd b ∧ ∀ u h, u≤j →
      atClock h x=3^u*2^(j-u)*a-1 → n+u<h := by
  obtain ⟨n,b,form,bo⟩:=split_twos (x+1) (by omega)
  have bp : 0<b := by obtain ⟨v,hv⟩:=bo; omega
  have ap : 0<a := by
    by_contra! z
    have az : a=0 := by omega
    subst a
    exact unit (dvd_zero _)
  have cheap : x+1<2^j*a := by omega
  refine ⟨n,b,form,bo,?_⟩
  intro u h uj meet
  let y:=atClock h x
  have yp : 0<3^u*2^(j-u)*a := by positivity
  have coord : y+1=3^u*2^(j-u)*a := by dsimp [y]; omega
  by_cases early : h≤n
  · have f : 2^h*(2^(n-h)*b)-1=x := by
      rw [←Nat.mul_assoc,←pow_add,show h+(n-h)=n by omega]; omega
    have asc:=ascent h (2^(n-h)*b) (by positivity)
    rw [f] at asc
    have qp : 0<(3:Nat)^h*(2^(n-h)*b) := by positivity
    have eqn : y+1=3^h*(2^(n-h)*b) := by dsimp [y]; omega
    have g : 2^h*(y+1)=3^h*(x+1) := by
      have pn : (2:Nat)^n=2^h*2^(n-h) := by rw [←pow_add,show h+(n-h)=n by omega]
      rw [eqn,form,pn]; ring
    have grade:=phase_grade h u j a uj (by
      rw [←coord,g]; exact Nat.mul_lt_mul_of_pos_left cheap (by positivity))
    have err : 3^u*(2^(j-u)*a)=3^h*(2^(n-h)*b) := by rw [←Nat.mul_assoc,←coord,eqn]
    exact False.elim (unit_mismatch _ _ _ _ _ unit grade err)
  · let t:=h-n
    have tm : n+t=h := by dsimp [t]; omega
    have base:=ascent n b bp
    rw [show 2^n*b-1=x by omega,Nat.mul_comm (3^n) b] at base
    have lower : atClock t (b*3^n-1)=y := by rw [←base,←clock_add,tm]
    obtain ⟨p,c,w,e,g⟩:=physical_base (b*3^n) t (by positivity)
    rw [lower] at e g
    push_cast at e
    let q:=n+p
    have weighted : 2^q*(3^u*2^(j-u)*a)<3^q*(2^j*a) := calc
      _ = 2^n*(2^p*(y+1)) := by rw [←coord,show q=n+p by rfl,pow_add]; ring
      _ ≤ 2^n*(3^p*(b*3^n)) := Nat.mul_le_mul_left _ g
      _ = 3^q*(x+1) := by rw [form,show q=n+p by rfl,pow_add]; ring
      _ < _ := Nat.mul_lt_mul_of_pos_left cheap (by positivity)
    have gf:=phase_grade q u j a uj weighted
    have ee : (3:Int)^q*b=2^t*y-c := by dsimp [q]; rw [pow_add]; nlinarith only [e]
    have cz : (y:Int)+1=3^u*2^(j-u)*a := by exact_mod_cast coord
    let A : Int:=2^(t+(j-u))*a-3^(q-u)*b
    have lead : (3:Int)^u*A=2^t+c := by
      dsimp [A]
      calc
        _ = (2:Int)^t*(3^u*2^(j-u)*a)-(3^u*3^(q-u))*b := by rw [pow_add (2:Int) t]; ring
        _ = _ := by rw [←pow_add,show u+(q-u)=q by omega,ee,←cz]; ring
    by_contra! late
    have tu : t≤u := by omega
    have cl:=carry_bound w
    have cr:=tight_carry w
    have big : (3:Int)^t≤3^u := pow_le_pow_right₀ (by decide) tu
    have positive : 0<(2:Int)^t := by positivity
    have van:=Int.eq_zero_of_abs_lt_dvd (show (3:Int)^u∣2^t+c from ⟨A,lead.symm⟩)
      (abs_lt.mpr (by constructor <;> omega))
    rw [van] at lead
    have az : A=0 := (mul_eq_zero.mp lead).resolve_left (by positivity)
    have eqn : (2:Nat)^(t+(j-u))*a=3^(q-u)*b := by
      exact_mod_cast (sub_eq_zero.mp az : (2:Int)^(t+(j-u))*a=3^(q-u)*b)
    exact unit_mismatch (t+(j-u)) a b (q-u) 0 unit (by omega) (by simpa using eqn)

#print axioms minus_one_grade
#print axioms separated_endpoint
#print axioms all_earlier
#print axioms progression
#print axioms not_perfect_power
#print axioms all_smaller
#print axioms pointwise
#print axioms full_clock
#print axioms full_margin
#print axioms prepeak_clock
end NegativeExponentAddress
