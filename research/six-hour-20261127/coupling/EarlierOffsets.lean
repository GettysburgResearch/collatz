import PaidCheckpoint

/-! Seventeen ordinary lower/upper comparisons covering all even offsets
between the first four exponents and the forty-bit return. -/
set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 8000
namespace EarlierOffsets
open CoreBranching FloorCounting PeakRigidity

def M (n : ℕ) := 2^n-1
def Good (x : ℕ) := ∃ h, run h x=1

theorem ascent (n b : ℕ) (pos : 0<b) :
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

theorem mersenne_peak (n : ℕ) : run n (M n)=3^n-1 := by
  simpa [M] using ascent n 1 (by decide)

private theorem good_step (x : ℕ) : Good (step x) ↔ Good x := by
  constructor
  · rintro ⟨h,eq⟩
    exact ⟨h+1,eq⟩
  · rintro ⟨h,eq⟩
    cases h with
    | zero => change x=1 at eq; subst x; exact ⟨1,rfl⟩
    | succ h => exact ⟨h,eq⟩

theorem good_run (n x : ℕ) : Good (run n x) ↔ Good x := by
  induction n generalizing x with
  | zero => rfl
  | succ n ih => exact (ih (step x)).trans (good_step x)

theorem meet_good {a b x y : ℕ} (meet : run a x=run b y) : Good x ↔ Good y := by
  rw [←good_run a x,←good_run b y,meet]

/-- Positive ordinary witnesses for the familiar adjacent even-index merger. -/
theorem even_index (n : ℕ) (hn : 0<n) (he : n%2=0) : Good (M n) ↔ Good (M (n-1)) := by
  obtain ⟨a,eq⟩ : ∃ a, n=2*a+2 := ⟨n/2-1,by omega⟩
  let A := 3^(2*a+1)
  have Aeq : A%4=3 := by
    have base : (3:ℕ)^2 ≡ 1 [MOD 4] := by decide
    have b : ((3:ℕ)^2)^a*3 ≡ 3 [MOD 4] := by simpa using (base.pow a).mul_right 3
    change ((3^2)^a*3)%4=3 at b
    dsimp only [A]
    rw [pow_succ,pow_mul]
    exact b
  let v := A/4
  have Av : A=4*v+3 := by dsimp [v]; omega
  have peak : run n (M n)=3*A-1 := by
    rw [mersenne_peak,eq,show 2*a+2=(2*a+1)+1 by omega,pow_succ]
    dsimp [A]
    omega
  have old : run (n-1) (M (n-1))=A-1 := by
    rw [mersenne_peak,show n-1=2*a+1 by omega]
  apply meet_good (a:=n+2) (b:=n-1+2)
  rw [run_add,run_add,peak,old,Av]
  have a1 : 3*(4*v+3)-1=2*(2*(3*v+2)) := by omega
  have a2 : 4*v+3-1=2*(2*v+1) := by omega
  rw [a1,a2]
  simp [run,step_double,step_odd]

structure Row where
  offset : ℕ
  rank : ℕ
  evens : ℕ
  constant : ℕ
  ascend : ℕ
  upper : ℕ
  extra : ℕ
  gain : ℕ
deriving DecidableEq

def rows : List Row := [
  ⟨6,4,7,1951,1,14,2,1⟩, ⟨8,2,9,1543,1,28,11,6⟩,
  ⟨10,1,7,173,1,28,13,7⟩, ⟨12,4,9,10495,0,26,8,5⟩,
  ⟨14,4,9,7423,1,35,14,8⟩, ⟨16,2,2,23,0,6,1,1⟩,
  ⟨18,1,9,461,2,31,14,7⟩, ⟨20,4,8,4463,0,20,5,3⟩,
  ⟨22,1,7,173,1,28,13,7⟩, ⟨24,1,9,461,2,31,14,7⟩,
  ⟨26,2,9,1543,1,28,11,6⟩, ⟨28,3,3,101,0,8,1,1⟩,
  ⟨30,1,9,461,2,31,14,7⟩, ⟨32,3,6,469,1,12,2,1⟩,
  ⟨34,2,2,23,0,6,1,1⟩, ⟨36,4,6,1007,1,13,2,1⟩,
  ⟨38,3,7,1109,0,18,5,3⟩]

private def gainPow (p : Row) := 80-p.offset+p.rank+p.evens
private def wBase (p : Row) := (2^gainPow p*35-p.constant)/3^p.rank
private def wStride (p : Row) := (2^gainPow p*243)/3^p.rank
def lowerClock (p : Row) := p.rank+p.evens+p.ascend
private def lowFactor (p : Row) := 3^p.ascend*2^(80-p.offset-p.ascend)
private def highFactor (p : Row) := 3^p.extra*2^(gainPow p-p.upper)

private structure Checks (p : Row) : Prop where
  starts : 0<wBase p
  upperGap : p.upper=p.rank+p.evens+p.extra+p.gain
  tops : p.offset+p.ascend≤80
  binary : p.upper≤gainPow p
  nonzero : 0<p.gain
  limited : p.offset+p.gain<80
  canon : wBase p%48=17
  period : wStride p%48=0
  under : 81*wBase p+271<128*2^80*35
  underSlope : 81*wStride p≤128*2^80*243
  lowerEq : run (lowerClock p) (wBase p)+1=lowFactor p*35
  upperEq : run p.upper (3*wBase p)+1=highFactor p*35
  lowerGrade : grade (lowerClock p) (wBase p)=p.rank+p.ascend
  upperGrade : grade p.upper (3*wBase p)=p.rank-1+p.extra
  loStride : 2^(lowerClock p)*(wStride p/2^(lowerClock p))=wStride p
  hiStride : 2^p.upper*(3*wStride p/2^p.upper)=3*wStride p
  loSlope : 3^(p.rank+p.ascend)*(wStride p/2^(lowerClock p))=lowFactor p*243
  hiSlope : 3^(p.rank-1+p.extra)*(3*wStride p/2^p.upper)=highFactor p*243

set_option maxHeartbeats 0 in
private theorem row_checks (p : Row) (hp : p∈rows) : Checks p := by
  simp only [rows,List.mem_cons,List.not_mem_nil,or_false] at hp
  rcases hp with h|h|h|h|h|h|h|h|h|h|h|h|h|h|h|h|h <;>
    subst p <;> constructor <;> decide +kernel

private theorem offset_address (d : ℕ) : 2^(93+162*d)%243=35 := by
  have a : (2:ℕ)^93≡35 [MOD 243] := by decide +kernel
  have b : (2:ℕ)^162≡1 [MOD 243] := by decide +kernel
  have c := a.mul (b.pow d)
  change (2^93*(2^162)^d)%243=(35*1^d)%243 at c
  simpa only [pow_add,pow_mul,one_pow,mul_one] using c

private theorem lift_slope (h x D v : ℕ) (splitD : 2^h*(D/2^h)=D) :
    run h (x+D*v)=run h x+(3^grade h x*(D/2^h))*v := by
  have tr := (lift_prefix h 0 x ((D/2^h)*v)).1
  simp only [Nat.add_zero,pow_zero,one_mul] at tr
  rw [←mul_assoc,splitD,←mul_assoc] at tr
  exact tr

private theorem charts (p : Row) (chk : Checks p) (v z : ℕ)
    (parent : 81*z+271=128*2^80*(35+243*v)) :
    let w := wBase p+wStride p*v
    let X := 35+243*v
    0<w ∧ w<z ∧ w%48=17 ∧
    run (lowerClock p) w+1=lowFactor p*X ∧ run p.upper (3*w)+1=highFactor p*X := by
  dsimp only
  have a := lift_slope (lowerClock p) (wBase p) (wStride p) v chk.loStride
  rw [chk.lowerGrade,chk.loSlope] at a
  have b := lift_slope p.upper (3*wBase p) (3*wStride p) v chk.hiStride
  rw [chk.upperGrade,chk.hiSlope] at b
  have pos := chk.starts
  have bound := chk.under
  have coeff := Nat.mul_le_mul_right v chk.underSlope
  rw [mul_assoc 81, mul_assoc (128*2^80)] at coeff
  have fit : wBase p+wStride p*v<z := by
    rw [Nat.mul_add] at parent
    omega
  have cg : (wBase p+wStride p*v)%48=17 := by
    rw [Nat.add_mod,Nat.mul_mod,chk.period,chk.canon]
    simp
  have l := chk.lowerEq
  have u := chk.upperEq
  refine ⟨by omega,fit,cg,?_,?_⟩
  · rw [a,Nat.mul_add, mul_assoc]
    omega
  · rw [show 3*(wBase p+wStride p*v)=3*wBase p+(3*wStride p)*v by ring,b,Nat.mul_add,mul_assoc]
    omega

private theorem select_row (a : ℕ) (lo : 6≤a) (hi : a≤38) (ea : a%2=0) :
    ∃ p∈rows, p.offset=a := by
  have all : ∀ i : Fin 17, (rows[i.val]'(by change i.val<17; exact i.isLt)).offset
      =6+2*i.val := by decide +kernel
  let i : Fin 17 := ⟨(a-6)/2,by omega⟩
  have il : i.val<rows.length := by change i.val<17; exact i.isLt
  exact ⟨rows[i.val]'il,List.getElem_mem il,(all i).trans (by dsimp [i]; omega)⟩

/-- Every row returns the triple of a smaller canonical query to an actual
strictly earlier Mersenne, after a stated number of physical shortcuts. -/
theorem actual_decrease (j z : ℕ) (p : Row) (hp : p∈rows)
    (parent : 81*z+271=128*2^(173+162*j)) :
    let m := 173+162*j
    let n := m-p.offset
    let u := n+p.rank+p.evens-p.upper
    ∃ w, 0<w ∧ w<z ∧ w%48=17 ∧
      run (lowerClock p) w=run p.ascend (M n) ∧
      run (p.upper+u) (3*w)=run (n-p.gain) (M (n-p.gain)) ∧
      0<n-p.gain ∧ n-p.gain<n := by
  let m := 173+162*j
  let n := m-p.offset
  let u := n+p.rank+p.evens-p.upper
  let X := 2^(93+162*j)
  let v := X/243
  have residue := offset_address j
  change X%243=35 at residue
  have Xv : X=35+243*v := by dsimp [v]; omega
  have power : 2^m=2^80*X := by
    change 2^(173+162*j)=2^80*2^(93+162*j)
    rw [←pow_add]
    congr 1
    omega
  change 81*z+271=128*2^m at parent
  rw [power,←mul_assoc,Xv] at parent
  have chk := row_checks p hp
  have ch := charts p chk v z parent
  rw [←Xv] at ch
  obtain ⟨wp,wz,wc,wl,wu⟩:=ch
  have top := chk.tops
  have bg := chk.binary
  unfold gainPow at bg
  have less := chk.limited
  have g := chk.nonzero
  have ec := chk.upperGap
  have m80 : 80≤m := by dsimp [m]; omega
  have npos : 0<n-p.gain ∧ n-p.gain<n := by dsimp [n]; omega
  have eq1 : (80-p.offset-p.ascend)+(93+162*j)=n-p.ascend := by dsimp [n,m]; omega
  have eq2 : gainPow p-p.upper+(93+162*j)=u := by dsimp [gainPow,u,n,m]; omega
  have eq3 : u+p.extra=n-p.gain := by dsimp [u,n]; omega
  have loF : lowFactor p*X=3^p.ascend*2^(n-p.ascend) := by
    change (3^p.ascend*2^(80-p.offset-p.ascend))*2^(93+162*j)=_
    rw [mul_assoc,←pow_add,eq1]
  have hiF : highFactor p*X=2^u*3^p.extra := by
    change (3^p.extra*2^(gainPow p-p.upper))*2^(93+162*j)=_
    rw [mul_assoc,←pow_add,eq2,mul_comm]
  rw [loF] at wl
  rw [hiF] at wu
  have low : run p.ascend (M n)=3^p.ascend*2^(n-p.ascend)-1 := by
    have h := ascent p.ascend (2^(n-p.ascend)) (by positivity)
    rw [←pow_add,show p.ascend+(n-p.ascend)=n by dsimp [n]; omega] at h
    exact h
  have high : run u (2^u*3^p.extra-1)=3^(n-p.gain)-1 := by
    rw [ascent _ _ (by positivity),←pow_add,eq3]
  refine ⟨_,wp,wz,wc,?_,?_,npos⟩
  · change run _ _=run p.ascend (M n)
    rw [low]
    omega
  · change run (p.upper+u) _=run (n-p.gain) (M (n-p.gain))
    rw [run_add,mersenne_peak,show run p.upper (3*(wBase p+wStride p*v))=2^u*3^p.extra-1 by omega,high]

/-- The two hypotheses are the exact consequences of least canonical
disagreement and the pinned forty-bit return consumed in this deduction. -/
theorem earlier_good (j z : ℕ) (parent : 81*z+271=128*2^(11+162*j))
    (floor : ∀ y, 0<y → 2^40*y<z → Good y)
    (canonical : ∀ w, 0<w → w<z → w%48=17 → Good (3*w) → Good w) :
    ∀ n, 0<n → n+5≤11+162*j → Good (M n) := by
  cases j with
  | zero =>
    intro n hn lim
    have hi : n≤6 := by omega
    interval_cases n
    · exact ⟨0,rfl⟩
    · exact ⟨5,rfl⟩
    · exact ⟨11,rfl⟩
    · exact ⟨12,rfl⟩
    · exact ⟨67,by decide⟩
    · exact ⟨68,by decide⟩
  | succ j =>
    let m := 173+162*j
    have id : 11+162*(j+1)=m := by dsimp [m]; omega
    rw [id] at parent ⊢
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro hn lim
      by_cases far : n+40≤m
      · apply floor
        · have : (2:ℕ)^0<2^n := Nat.pow_lt_pow_right (by decide) hn
          unfold M
          omega
        · have f : (2:ℕ)^(n+40)≤2^m := Nat.pow_le_pow_right (by decide) far
          rw [pow_add,mul_comm] at f
          have sub := Nat.mul_le_mul_left (2^40) (Nat.sub_le (2^n) 1)
          have big : (2:ℕ)^3≤2^m := Nat.pow_le_pow_right (by decide) (by dsimp [m]; omega)
          unfold M
          omega
      · by_cases ev : n%2=0
        · exact (even_index _ hn ev).mpr (ih (n-1) (by omega) (by omega) (by omega))
        · let a := m-n
          have aa : 6≤a ∧ a≤38 ∧ a%2=0 := by dsimp [a,m] at *; omega
          obtain ⟨p,pm,pa⟩:=select_row a aa.1 aa.2.1 aa.2.2
          have stmt := actual_decrease j z p pm parent
          have eqn : m-p.offset=n := by rw [pa]; dsimp [a]; omega
          dsimp only at stmt
          change 173+162*j-p.offset=n at eqn
          rw [eqn] at stmt
          obtain ⟨w,wp,wz,wc,lo,hi,sp,sm⟩:=stmt
          have earlier := ih _ sm sp (by omega)
          exact (meet_good lo).mp (canonical w wp wz wc ((meet_good hi).mpr earlier))

/-- A physical peak merger with gap at least five now consumes only the
two general leastness consequences in earlier_good. -/
theorem gap_five_return (j z s i l : ℕ) (parent : 81*z+271=128*2^(11+162*j))
    (floor : ∀ y, 0<y → 2^40*y<z → Good y)
    (canonical : ∀ w, 0<w → w<z → w%48=17 → Good (3*w) → Good w)
    (sp : 0<s) (gap : s+5≤11+162*j)
    (hit : run i (3^(11+162*j)-1)=run l (3^s-1)) : Good z := by
  have earlier := earlier_good j z parent floor canonical s sp gap
  have goodPeak := (good_run s (M s)).mpr earlier
  rw [mersenne_peak] at goodPeak
  have native := (meet_good hit).mpr goodPeak
  rw [←mersenne_peak] at native
  have goodM := (good_run _ _).mp native
  have zm : z%128=33 := by omega
  have rep : z=33+128*(z/128) := by omega
  have tr := (lift_prefix 7 0 33 (z/128)).1
  norm_num [show run 7 33=22 by decide,show grade 7 33=4 by decide] at tr
  rw [←rep,show 22+81*(z/128)=M (11+162*j) by unfold M; omega] at tr
  exact (good_run 7 z).mp (tr ▸ goodM)

#print axioms even_index
#print axioms actual_decrease
#print axioms earlier_good
#print axioms gap_five_return
end EarlierOffsets
