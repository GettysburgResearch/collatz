import OffsetFour

/-! Exact delayed ordinary sources after their common valuation clock.
The two earlier exponents give a fixed affine pair. -/
set_option autoImplicit false
set_option warningAsError true
namespace DelayedUnit
open CoreBranching FloorCounting PeakRigidity
open EarlierOffsets (M Good good_run mersenne_peak meet_good)

def unit : ℕ → ℕ
  | 0 => 33215
  | b+1 => unit b+2^(b+3)*(unit b)^2

theorem unit_factor (b : ℕ) : 3^(12*2^b)=1+2^(b+4)*unit b := by
  induction b with
  | zero => decide
  | succ b ih =>
    rw [pow_succ (2:ℕ) b,←Nat.mul_assoc,pow_mul,ih,unit]
    rw [show b+1+4=(b+3)+2 by omega,show b+4=(b+3)+1 by omega,pow_add,pow_succ]
    ring

theorem unit_odd (b : ℕ) : unit b%2=1 := by
  induction b with
  | zero => decide
  | succ b ih =>
    rw [unit,show b+3=(b+2)+1 by omega,pow_succ]
    have f : 2^(b+2)*2*unit b^2=2*(2^(b+2)*unit b^2) := by ring
    rw [f,Nat.add_mul_mod_self_left]
    exact ih

theorem unit_stable (a t : ℕ) : unit (a+t) ≡ unit a [MOD 2^(a+3)] := by
  induction t with
  | zero => rfl
  | succ t ih =>
    change unit ((a+t)+1)%2^(a+3)=unit a%2^(a+3)
    rw [unit,show a+t+3=(a+3)+t by omega,pow_add]
    change (unit (a+t)+2^(a+3)*2^t*unit (a+t)^2)%2^(a+3)=_
    rw [Nat.mul_assoc,Nat.add_mul_mod_self_left]
    exact ih

private theorem two_turn (n v : ℕ) : run (2*n) (4^n*v+2)=3^n*v+2 := by
  induction n generalizing v with
  | zero => simp [run]
  | succ n ih =>
    have pair (s : ℕ) : run 2 (4*s+2)=3*s+2 := by
      rw [show 4*s+2=2*(2*s+1) by omega,run,step_double,run,step_odd,run]
    rw [show 2*(n+1)=2+2*n by omega,pow_succ,pow_succ,
        show 4^n*4*v+2=4*(4^n*v)+2 by ring,run_add,pair,
        show 3*(4^n*v)+2=4^n*(3*v)+2 by ring,ih]
    ring

private theorem chart_three (x y : ℕ) (eq : 27*x+26=64*y) :
    run 6 x=3*y+2 := by
  have xr : x=18+64*(x/64) := by omega
  have f := (lift_prefix 6 0 18 (x/64)).1
  simp only [Nat.add_zero,pow_zero,one_mul,show run 6 18=26 by decide,
    show grade 6 18=4 by decide] at f
  change run 6 (18+64*(x/64))=26+81*(x/64) at f
  rw [←xr] at f
  omega

private theorem chart_five (x y : ℕ) (eq : 243*x+242=4096*y) :
    run 12 x=3*y+2 := by
  have xr : x=2106+4096*(x/4096) := by omega
  have f := (lift_prefix 12 0 2106 (x/4096)).1
  simp only [Nat.add_zero,pow_zero,one_mul,show run 12 2106=377 by decide,
    show grade 12 2106=6 by decide] at f
  change run 12 (2106+4096*(x/4096))=377+729*(x/4096) at f
  rw [←xr] at f
  omega

private theorem halves (n U : ℕ) : run n (2^n*U)=U := by
  induction n with
  | zero => simp [run]
  | succ n ih =>
    rw [pow_succ,show 2^n*2*U=2*(2^n*U) by ring,run,step_double,ih]

private theorem native (x y : ℕ) (eq : 3*x+2=4*y) : run 2 x=y := by
  have xr : x=2+4*(x/4) := by omega
  have f := (lift_prefix 2 0 2 (x/4)).1
  simp only [Nat.add_zero,pow_zero,one_mul,show run 2 2=2 by decide,
    show grade 2 2=1 by decide] at f
  change run 2 (2+4*(x/4))=2+3*(x/4) at f
  rw [←xr] at f
  omega

private theorem fitted (m q k : ℕ) (eq : m+1=12*2^(18*k)) (small : q≤m+1) :
    3^q*(3^(m+1-q)-1)+(3^q-1)=2^(18*k+4)*unit (18*k) := by
  have b := unit_factor (18*k)
  rw [←eq,←show q+(m+1-q)=m+1 by omega,pow_add] at b
  have pos : 0<(3:ℕ)^(m+1-q) := by positivity
  have p2 : 0<(3:ℕ)^q := by positivity
  have f : 3^q*((3^(m+1-q)-1)+1)=3^q*3^(m+1-q) := by rw [Nat.sub_add_cancel (by omega)]
  rw [Nat.mul_add,mul_one] at f
  omega

set_option maxHeartbeats 2000000 in
/-- The three initial Mersennes first take their own all-odd paths and then
the same H ordinary shortcuts to the displayed positive sources. -/
theorem actual_sources (k : ℕ) (hk : 0<k) :
    let m := DelayedTurns.hard k
    let H := 18*k+4
    let U := unit (18*k)
    let Y := 3^(9*k-3)*U
    run (m+H) (M m)=U ∧ run (m-2+H) (M (m-2))=27*Y+2 ∧
      run (m-4+H) (M (m-4))=Y+2 := by
  let m := DelayedTurns.hard k
  let U := unit (18*k)
  have pos : 0<(2:ℕ)^(18*k) := by positivity
  have me : m+1=12*2^(18*k) := by dsimp [m,DelayedTurns.hard]; omega
  have big : 10≤m := by omega
  let H := 18*k+4
  have e (q : ℕ) (hq : q≤m+1) := fitted m q k me hq
  have m1 := e 1 (by omega)
  have m3 := e 3 (by omega)
  have m5 := e 5 (by omega)
  rw [show m+1-1=m by omega] at m1
  rw [show m+1-3=m-2 by omega] at m3
  rw [show m+1-5=m-4 by omega] at m5
  have eh : H=2+(H-2) := by dsimp [H]; omega
  have et : H=6+2*(9*k-1) := by dsimp [H]; omega
  have ef : H=12+2*(9*k-4) := by dsimp [H]; omega
  have ep (s : ℕ) : (2:ℕ)^(2*s)=4^s := by rw [pow_mul]; rfl
  change _=2^H*U at m1 m3 m5
  rw [eh,pow_add,mul_assoc] at m1
  rw [et,pow_add,ep,mul_assoc] at m3
  rw [ef,pow_add,ep,mul_assoc] at m5
  have c1 := native _ _ m1
  have c3 := chart_three _ _ m3
  have c5 := chart_five _ _ m5
  dsimp only
  change run (m+H) (M m)=U ∧ run (m-2+H) (M (m-2))=27*(3^(9*k-3)*U)+2 ∧
      run (m-4+H) (M (m-4))=3^(9*k-3)*U+2
  rw [run_add m H,run_add (m-2) H,run_add (m-4) H,mersenne_peak,mersenne_peak,mersenne_peak]
  constructor
  · rw [eh,run_add,c1,halves]
  constructor
  · rw [et,run_add,c3,show 3*(4^(9*k-1)*U)=4^(9*k-1)*(3*U) by ring,two_turn]
    have f : 3^(9*k-1)*3=27*3^(9*k-3) := by
      change 3^(9*k-1)*3=3^3*3^(9*k-3)
      rw [←pow_succ,←pow_add,show 9*k-1+1=3+(9*k-3) by omega]
    rw [←mul_assoc,f,mul_assoc]
  · rw [ef,run_add,c5,show 3*(4^(9*k-4)*U)=4^(9*k-4)*(3*U) by ring,two_turn]
    have e4 : 9*k-4+1=9*k-3 := by omega
    rw [←mul_assoc,←pow_succ,e4]

/-- Any actual merger of the fixed affine pair returns every strictly
earlier positive Mersenne under the two general leastness consequences. -/
theorem all_earlier_of_pair (k z i : ℕ) (hk : 0<k)
    (parent : 81*z+271=128*2^(DelayedTurns.hard k))
    (floor : ∀ y, 0<y → 2^40*y<z → Good y)
    (canonical : ∀ w, 0<w → w<z → w%48=17 → Good (3*w) → Good w)
    (hit : let Y := 3^(9*k-3)*unit (18*k)
           run i (27*Y+2)=run i (Y+2)) :
    ∀ n, 0<n → n<DelayedTurns.hard k → Good (M n) := by
  let m := DelayedTurns.hard k
  have wide : 10≤m := by
    have g := Nat.two_pow_pos (18*k)
    dsimp [m,DelayedTurns.hard]
    omega
  have odd : m%2=1 := by
    dsimp [m,DelayedTurns.hard]
    have g := Nat.two_pow_pos (18*k)
    omega
  let H := 18*k+4
  have src := actual_sources k hk
  dsimp only at src hit
  obtain ⟨_,l,r⟩:=src
  have link : run (m-2+H+i) (M (m-2))=run (m-4+H+i) (M (m-4)) := by
    rw [run_add (m-2+H) i,run_add (m-4+H) i,l,r,hit]
  have old := OffsetFour.earlier_good_delayed k z hk parent floor canonical
  change ∀ n, 0<n → n+3≤m → Good (M n) at old
  have two := (meet_good link).mpr (old (m-4) (by omega) (by omega))
  intro n hn lim
  change n<m at lim
  by_cases low : n+3≤m
  · exact old n hn low
  by_cases edge : n=m-2
  · exact edge ▸ two
  exact (EarlierOffsets.even_index _ hn (by omega)).mpr ((by omega : n-1=m-2) ▸ two)

#print axioms unit_factor
#print axioms unit_odd
#print axioms unit_stable
#print axioms actual_sources
#print axioms all_earlier_of_pair
end DelayedUnit
