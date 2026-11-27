import EarlierOffsets

/-! Positive affine chart transport and an exhaustive least-significant-digit
ternary partition for ordinary canonical parent comparisons. -/
set_option autoImplicit false
set_option warningAsError true
set_option maxHeartbeats 1500000
namespace ValuationCharts
open CoreBranching FloorCounting PeakRigidity
open EarlierOffsets (Good M good_run)

structure Row where
  rank : ℕ
  evens : ℕ
  constant : ℕ
  upper : ℕ
  upperOdds : ℕ
  /-- The signed constant in the upper endpoint is sign-1. -/
  sign : ℕ
deriving DecidableEq, Repr

def lower (r : Row) := r.rank+r.evens
def delta (r : Row) := r.upper-lower r
def gain (r : Row) := r.upperOdds+1-r.rank
def factor (r : Row) := 3^(gain r)*2^(100-delta r)
def base (r : Row) (x : ℕ) := (2^(100+lower r)*x-r.constant)/3^r.rank
def stride (r : Row) (s : ℕ) := 2^(100+lower r)*s/3^r.rank

def profile : ℕ → ℕ → ℕ×ℕ
  | 0,x => (x,0)
  | h+1,x =>
    let y := profile h (step x)
    (y.1,x%2+y.2)

theorem profile_spec (h x : ℕ) : profile h x=(run h x,grade h x) := by
  have first (k a : ℕ) : grade (k+1) a=a%2+grade k (step a) := by
    induction k with
    | zero => simp [grade,run]
    | succ k ih => rw [grade,ih,run,grade,Nat.add_assoc]
  induction h generalizing x with
  | zero => rfl
  | succ h ih => simp only [profile,ih,run,first]

/-- All endpoint comparisons and parity counts refer to actual positive
reductions of an ordinary representative. -/
def Valid (r : Row) (x s : ℕ) : Prop :=
  let w := base r x
  let a := stride r s
  let f := lower r
  let u := r.upper
  let g := gain r
  let d := delta r
  let n := (173-d)/2
  let rem := (173-d)%2
  0<w ∧ w%48=17 ∧ a%48=0 ∧
  81*w+271<128*2^100*x ∧ 81*a≤128*2^100*s ∧
  (profile f w).1+1=2^100*x ∧ (profile f w).2=r.rank ∧
  (profile u (3*w)).1+1=factor r*x+r.sign ∧ (profile u (3*w)).2=r.upperOdds ∧
  2^f*(a/2^f)=a ∧ 2^u*(3*a/2^u)=3*a ∧
  3^r.rank*(a/2^f)=2^100*s ∧ 3^r.upperOdds*(3*a/2^u)=factor r*s ∧
  f≤u ∧ d≤100 ∧ r.rank≤r.upperOdds+1 ∧ r.sign≤2 ∧
  (r.sign=0 → g+5≤d) ∧
  (r.sign=1 → 2^40*3^g<2^173) ∧
  (r.sign=2 → 2^40*(2^rem*3^(g+n)+1)<2^173)

instance (r : Row) (x s : ℕ) : Decidable (Valid r x s) := by
  unfold Valid
  infer_instance

theorem lift (h x a v : ℕ) (ha : 2^h*(a/2^h)=a) :
    run h (x+a*v)=run h x+(3^grade h x*(a/2^h))*v ∧
    grade h (x+a*v)=grade h x := by
  have t := lift_prefix h 0 x ((a/2^h)*v)
  simp only [Nat.add_zero,pow_zero,one_mul] at t
  rw [←mul_assoc,ha,←mul_assoc] at t
  exact t

private theorem cost {w u hi di z : ℕ} (a : 81*w+271<hi)
    (b : 81*u≤di) (c : 81*z+271=hi+di) : w+u<z := by omega

/-- One checked row simultaneously certifies canonicality, the strict query
budget, both ordinary clocks, both odd grades and the compensated endpoints. -/
theorem physical (r : Row) (x s t z : ℕ) (ok : Valid r x s)
    (parent : 81*z+271=128*2^100*(x+s*t)) :
    let w := base r x+stride r s*t
    0<w ∧ w<z ∧ w%48=17 ∧
    run (lower r) w+1=2^100*(x+s*t) ∧ grade (lower r) w=r.rank ∧
    run r.upper (3*w)+1=factor r*(x+s*t)+r.sign ∧ grade r.upper (3*w)=r.upperOdds := by
  rcases ok with ⟨wp,wc,ac,wb,ab,lo,lg,hi,hg,sa,sb,sl,sh,_⟩
  simp only [profile_spec] at lo lg hi hg
  have a := lift (lower r) (base r x) (stride r s) t sa
  have b := lift r.upper (3*base r x) (3*stride r s) t sb
  rw [lg,sl] at a
  rw [hg,sh] at b
  have coeff := Nat.mul_le_mul_right t ab
  rw [mul_assoc 81,mul_assoc (128*2^100)] at coeff
  dsimp only
  refine ⟨by clear * -wp; omega,?_,?_,?_,a.2,?_,?_⟩
  · rw [Nat.mul_add] at parent
    exact cost wb coeff parent
  · rw [Nat.add_mod,Nat.mul_mod,ac,wc]
    simp
  · rw [a.1,Nat.mul_add,←mul_assoc]
    clear * -lo
    omega
  · rw [Nat.mul_add,←mul_assoc,b.1,Nat.mul_add,←mul_assoc]
    clear * -hi
    omega
  · rw [Nat.mul_add,←mul_assoc,b.2]

inductive Atlas (α : Type) where
  | leaf (item : α)
  | fork (zero one two : Atlas α)

def checkWith {α : Type} (test : α → ℕ → ℕ → Bool) : Atlas α → ℕ → ℕ → Bool
  | .leaf r,x,s => test r x s
  | .fork a b c,x,s =>
    checkWith test a x (3*s) && checkWith test b (x+s) (3*s) && checkWith test c (x+2*s) (3*s)

/-- Every nonnegative parameter has a certified representative and stride. -/
theorem selectWith {α : Type} (test : α → ℕ → ℕ → Bool) (tree : Atlas α) (x s v : ℕ) (ok : checkWith test tree x s=true) :
    ∃ r y a t, test r y a=true ∧ x+s*v=y+a*t := by
  induction tree generalizing x s v with
  | leaf r => exact ⟨r,x,s,v,ok,rfl⟩
  | fork a b c ia ib ic =>
    simp only [checkWith,Bool.and_eq_true] at ok
    have decomp : v=v%3+3*(v/3) := by omega
    rcases (show v%3=0 ∨ v%3=1 ∨ v%3=2 by omega) with h|h|h
    · obtain ⟨r,y,d,t,f,e⟩:=ia x (3*s) (v/3) ok.1.1
      refine ⟨r,y,d,t,f,?_⟩
      rw [←e]
      nth_rw 1 [decomp]
      rw [h]
      ring
    · obtain ⟨r,y,d,t,f,e⟩:=ib (x+s) (3*s) (v/3) ok.1.2
      refine ⟨r,y,d,t,f,?_⟩
      rw [←e]
      nth_rw 1 [decomp]
      rw [h]
      ring
    · obtain ⟨r,y,d,t,f,e⟩:=ic (x+2*s) (3*s) (v/3) ok.2
      refine ⟨r,y,d,t,f,?_⟩
      rw [←e]
      nth_rw 1 [decomp]
      rw [h]
      ring

abbrev Tree := Atlas Row
abbrev check := checkWith (fun r x s => decide (Valid r x s))

theorem select (tree : Tree) (x s v : ℕ) (ok : check tree x s=true) :
    ∃ r y a t, Valid r y a ∧ x+s*v=y+a*t := by
  obtain ⟨r,y,a,t,checked,e⟩:=selectWith _ tree x s v ok
  exact ⟨r,y,a,t,of_decide_eq_true checked,e⟩

private theorem halves (n v : ℕ) : run n (2^n*v)=v := by
  induction n with
  | zero => simp [run]
  | succ n ih =>
    rw [pow_succ,show 2^n*2*v=2*(2^n*v) by ring,run,step_double,ih]

private theorem scale (n A : ℕ) : 2^40*(A+1)<2^173 →
    2^40*(A*3^n+1)<2^173*4^n := by
  intro basecase
  induction n with
  | zero => simpa using basecase
  | succ n ih =>
    rw [pow_succ (3:ℕ),pow_succ (4:ℕ),←mul_assoc]
    omega

theorem terminal_good (j d g sign y z : ℕ) (dc : d≤100) (sc : sign≤2)
    (hi : y+1=2^(173+162*j-d)*3^g+sign)
    (capital : 2^(173+162*j)<z)
    (neg : sign=0 → g+5≤d) (pure : sign=1 → 2^40*3^g<2^173)
    (pos : sign=2 → 2^40*(2^((173-d)%2)*3^(g+(173-d)/2)+1)<2^173)
    (floor : ∀ a, 0<a → 2^40*a<z → Good a)
    (earlier : ∀ a, 0<a → a+5≤11+162*(j+1) → Good (M a)) : Good y := by
  let m := 173+162*j
  let v := m-d
  change y+1=2^v*3^g+sign at hi
  change 2^m<z at capital
  rcases (show sign=0 ∨ sign=1 ∨ sign=2 by omega) with h|h|h
  · have gap := neg h
    rw [h] at hi
    have positive : 0<v+g := by dsimp [v,m]; omega
    have prev := earlier (v+g) positive (by dsimp [v,m]; omega)
    have peak := (good_run (v+g) (M (v+g))).mpr prev
    rw [EarlierOffsets.mersenne_peak] at peak
    apply (good_run v _).mp
    rw [show y=2^v*3^g-1 by omega,
      EarlierOffsets.ascent v _ (by positivity),←pow_add]
    exact peak
  · have budget := pure h
    rw [h] at hi
    have baseBound : 2^173≤2^m := Nat.pow_le_pow_right (n:=2) (by decide) (by dsimp [m]; clear * -j; omega)
    apply (good_run v _).mp
    rw [show y=2^v*3^g by omega,halves]
    exact floor _ (by positivity) (by omega)
  · have budget := pos h
    let n := (173-d)/2
    let rem := (173-d)%2
    let n' := n+81*j
    change 2^40*(2^rem*3^(g+n)+1)<2^173 at budget
    rw [h] at hi
    have vn : v=2*n'+rem := by dsimp [v,m,n',n,rem]; omega
    have power : 2^v*3^g=4^n'*(2^rem*3^g) := by
      rw [vn,pow_add,pow_mul,show (2:ℕ)^2=4 by decide,mul_assoc]
    have small := scale (81*j) _ budget
    have main : 2^173*4^(81*j)=2^m := by
      rw [show (4:ℕ)=2^2 by decide,←pow_mul,←pow_add]; congr 1; dsimp [m]; omega
    rw [main] at small
    have comp : 3^n'*(2^rem*3^g)=2^rem*3^(g+n)*3^(81*j) := by
      dsimp [n']; rw [pow_add,pow_add]; ring
    apply (good_run (2*n') _).mp
    rw [show y=4^n'*(2^rem*3^g)+1 by omega,
      PaidCheckpoint.positive_turns,comp]
    exact floor _ (by positivity) (by omega)

/-- The negative branch meets a gap-five covered ordinary Mersenne peak.
The pure and positive branches enter the actual forty-bit return. -/
theorem row_good (r : Row) (x s t j z : ℕ) (ok : Valid r x s)
    (address : 2^(73+162*j)=x+s*t)
    (parent : 81*z+271=128*2^(173+162*j))
    (floor : ∀ y, 0<y → 2^40*y<z → Good y)
    (canonical : ∀ w, 0<w → w<z → w%48=17 → Good (3*w) → Good w) : Good z := by
  let m := 173+162*j
  let g := gain r
  let d := delta r
  let v := m-d
  have powm : 2^m=2^100*(x+s*t) := by rw [←address,←pow_add]; congr 1; dsimp [m]; omega
  have cp : 81*z+271=128*2^100*(x+s*t) := by
    change 81*z+271=128*2^m at parent
    rw [parent,powm,mul_assoc]
  obtain ⟨wp,wz,wc,lo,_,hi,_⟩:=physical r x s t z ok cp
  rcases ok with ⟨_,_,_,_,_,_,_,_,_,_,_,_,_,_,dc,_,sc,neg,pure,pos⟩
  change d≤100 at dc
  have big : (2:ℕ)^3≤2^m := Nat.pow_le_pow_right (n:=2) (by decide) (by dsimp [m]; clear * -j; omega)
  have capital : 2^m<z := by change 81*z+271=128*2^m at parent; clear * -big parent; omega
  have coeff : factor r*(x+s*t)=2^v*3^g := by
    rw [←address]
    change 3^g*2^(100-d)*2^(73+162*j)=_
    rw [mul_assoc,←pow_add,show (100-d)+(73+162*j)=v by dsimp [v,m]; clear * -dc; omega,mul_comm]
  rw [coeff] at hi
  let w := base r x+stride r s*t
  change run r.upper (3*w)+1=2^v*3^g+r.sign at hi
  have earlier := EarlierOffsets.earlier_good (j+1) z
    (by rw [show 11+162*(j+1)=173+162*j by clear * -j; omega]; exact parent) floor canonical
  have goodUpper := terminal_good j d g r.sign (run r.upper (3*w)) z dc sc hi capital
    neg pure pos floor earlier
  have goodW := canonical w wp wz wc ((good_run _ _).mp goodUpper)
  have goodM := (good_run (lower r) w).mpr goodW
  rw [←powm] at lo
  change run (lower r) w+1=2^m at lo
  rw [show run (lower r) w=M m by unfold M; clear * -lo; omega] at goodM
  have rep : z=33+128*(z/128) := by change 81*z+271=128*2^m at parent; clear * -parent; omega
  have tr := (lift_prefix 7 0 33 (z/128)).1
  norm_num [show run 7 33=22 by decide,show grade 7 33=4 by decide] at tr
  rw [←rep,show 22+81*(z/128)=M m by unfold M; change 81*z+271=128*2^m at parent; clear * -parent; omega] at tr
  exact (good_run 7 z).mp (tr ▸ goodM)

#print axioms profile_spec
#print axioms lift
#print axioms physical
#print axioms selectWith
#print axioms terminal_good
#print axioms select
#print axioms row_good
end ValuationCharts
