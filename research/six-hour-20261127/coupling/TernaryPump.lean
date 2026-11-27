import EarlierOffsets
import PaidCheckpoint

/-! An exponent-one inverse family controlled by the actual ternary
valuation of 2^(m+6)-95. -/
set_option autoImplicit false
set_option warningAsError true
namespace TernaryPump
open CoreBranching PeakRigidity FloorCounting
open EarlierOffsets (M Good good_run ascent)

private theorem lower_chart (x P : ℕ) (eq : 27*x+122=64*P) :
    run 6 x+1=P ∧ grade 6 x=3 := by
  have xr : x=50+64*(x/64) := by omega
  have a := lift_prefix 6 0 50 (x/64)
  simp only [Nat.add_zero,pow_zero,one_mul,show run 6 50=22 by decide,
    show grade 6 50=3 by decide] at a
  change run 6 (50+64*(x/64))=22+27*(x/64) ∧ grade 6 (50+64*(x/64))=3 at a
  rw [←xr] at a
  omega

private theorem upper_chart (x P : ℕ) (eq : 81*x+176=8192*P) :
    run 13 x=P+1 ∧ grade 13 x=4 := by
  have xr : x=1616+8192*(x/8192) := by omega
  have a := lift_prefix 13 0 1616 (x/8192)
  simp only [Nat.add_zero,pow_zero,one_mul,show run 13 1616=17 by decide,
    show grade 13 1616=4 by decide] at a
  change run 13 (1616+8192*(x/8192))=17+81*(x/8192) ∧ grade 13 (1616+8192*(x/8192))=4 at a
  rw [←xr] at a
  omega

private theorem integral_charts (w v t : ℕ) (low : 9*w+23=16*v)
    (high : 9*(3*w)+69=64*(3*t)) :
    run 4 w=v-1 ∧ grade 4 w=2 ∧ run 6 (3*w)=3*t-1 ∧ grade 6 (3*w)=2 := by
  have a : w=1+16*(w/16) := by omega
  have b : 3*w=35+64*(3*w/64) := by omega
  have l := lift_prefix 4 0 1 (w/16)
  have u := lift_prefix 6 0 35 (3*w/64)
  simp only [Nat.add_zero,pow_zero,one_mul,show run 4 1=1 by decide,
    show grade 4 1=2 by decide] at l
  simp only [Nat.add_zero,pow_zero,one_mul,show run 6 35=5 by decide,
    show grade 6 35=2 by decide] at u
  change run 4 (1+16*(w/16))=1+9*(w/16) ∧ grade 4 (1+16*(w/16))=2 at l
  change run 6 (35+64*(3*w/64))=5+9*(3*w/64) ∧ grade 6 (35+64*(3*w/64))=2 at u
  rw [←a] at l
  rw [←b] at u
  omega

private theorem prefix_sub (t B : ℕ) (Bpos : 0<B) : 0<3^t*B ∧ 0<2^t*B := by
  constructor <;> positivity

/-- With s=6+t, both paths have fixed formulas for their full lengths.
No optimality or convergence hypothesis is used. -/
theorem pumped_paths (t m B w : ℕ) (Bpos : 0<B) (m7 : 7≤m)
    (val : 3^(6+t)*B+95=2^(m+6)) (paid : 9*w+23=2^(7+t)*B) :
    let V := 2^(3+t)*B-1
    run 4 w=V ∧ grade 4 w=2 ∧ run (9+t) V=M m ∧
      run (13+t) w=M m ∧ run (20+t) (3*w)=2^(m-7)+1 := by
  let V := 2^(3+t)*B-1
  let L := 3^(3+t)*B-1
  let U := 3^(2+t)*B-1
  have mref : 2^(m+6)=8192*2^(m-7) := by
    change 2^(m+6)=2^13*2^(m-7)
    rw [←pow_add]; congr 1; omega
  have lm : 27*L+122=64*2^m := by
    have r := val
    rw [show 6+t=3+(3+t) by omega,pow_add,pow_add (2:ℕ),mul_assoc,mul_comm (2^m)] at r
    have z := (prefix_sub (3+t) B Bpos).1
    dsimp [L]
    omega
  have um : 81*U+176=8192*2^(m-7) := by
    have r := val
    rw [show 6+t=4+(2+t) by omega,pow_add,mul_assoc,mref] at r
    have z := (prefix_sub (2+t) B Bpos).1
    dsimp [U]
    omega
  have lo := (lower_chart _ _ lm).1
  have up := (upper_chart _ _ um).1
  have wlo : 9*w+23=16*(2^(3+t)*B) := by
    rw [paid,show 7+t=4+(3+t) by omega,pow_add,mul_assoc]
    rfl
  have whi : 9*(3*w)+69=64*(3*(2^(1+t)*B)) := by
    have f := paid
    rw [show 7+t=6+(1+t) by omega,pow_add,mul_assoc] at f
    omega
  have ch := integral_charts w _ _ wlo whi
  have lp := ascent (3+t) B Bpos
  have upturn := ascent (1+t) (3*B) (by omega)
  have t3 : 3^(1+t)*(3*B)=3^(2+t)*B := by
    rw [←mul_assoc,←pow_succ,show 1+t+1=2+t by omega]
  rw [t3] at upturn
  dsimp only
  change run 4 w=V ∧ grade 4 w=2 ∧ run (9+t) V=M m ∧
    run (13+t) w=M m ∧ run (20+t) (3*w)=2^(m-7)+1
  have vl : run (9+t) V=M m := by
    rw [show 9+t=(3+t)+6 by omega,run_add]
    change run 6 (run (3+t) (2^(3+t)*B-1))=M m
    rw [lp]
    change run 6 L=2^m-1
    omega
  refine ⟨ch.1,ch.2.1,vl,?_,?_⟩
  · rw [show 13+t=4+(9+t) by omega,run_add,ch.1,vl]
  · rw [show 20+t=6+((1+t)+13) by omega,run_add 6,run_add (1+t),ch.2.2.1,
      show 3*(2^(1+t)*B)=2^(1+t)*(3*B) by ring,upturn]
    exact up

private theorem ratio (t : ℕ) : 9*(2:ℕ)^(6+t)<3^(6+t) := by
  induction t with
  | zero => decide
  | succ t ih =>
    rw [show 6+(t+1)=6+t+1 by omega,pow_succ (2:ℕ),pow_succ (3:ℕ)]
    omega

private theorem contraction (t : ℕ) : 2^40*(3^(83+t)+1)<128*(4:ℕ)^(83+t) := by
  induction t with
  | zero => decide +kernel
  | succ t ih =>
    rw [show 83+(t+1)=83+t+1 by omega,pow_succ (3:ℕ),pow_succ (4:ℕ)]
    omega

private theorem parent_link (t m z B : ℕ)
    (parent : 81*z+271=128*2^m) (val : 3^(6+t)*B+95=2^(m+6)) :
    z+1=3^(2+t)*(2*B) := by
  rw [show 6+t=4+(2+t) by omega,pow_add,pow_add (2:ℕ),mul_assoc] at val
  rw [show 3^(2+t)*(2*B)=2*(3^(2+t)*B) by ring]
  omega

/-- Every selected ternary unit digit on every s=6+t gives a smaller
canonical source physically reaching z itself in s clocks. Its triple
returns to a point strictly below z/2^40. -/
theorem paid_valuation (j t B z : ℕ) (bp : 0<B)
    (parent : 81*z+271=128*2^(173+162*j))
    (val : 3^(6+t)*B+95=2^(173+162*j+6))
    (digit : (2^(7+t)*B)%27=14) :
    ∃ w x, 0<w ∧ w<z ∧ w%48=17 ∧ run (6+t) w=z ∧
      run (20+t+(173+162*j-7)) (3*w)=x ∧ 0<x ∧ 2^40*x<z := by
  let m := 173+162*j
  let n := 83+81*j
  let X := 2^(7+t)*B
  let w := (X-23)/9
  have rep : X=128*(2^t*B) := by dsimp [X]; rw [pow_add,mul_assoc]; rfl
  have bs := (prefix_sub t B bp).2
  change X%27=14 at digit
  have paid : 9*w+23=X := by dsimp [w]; omega
  have wc : w%48=17 := by omega
  have wp : 0<w := by omega
  have zv := parent_link t m z B parent val
  have rat := Nat.mul_lt_mul_of_pos_right (ratio t) bp
  rw [mul_assoc] at rat
  change 81*z+271=128*2^m at parent
  change 3^(6+t)*B+95=2^(m+6) at val
  have cow : 2*3^(6+t)*B=81*(z+1) := by
    rw [pow_add (2:ℕ) m] at val
    rw [mul_assoc]
    omega
  have bx : X=2*(2^(6+t)*B) := by
    dsimp [X]; rw [show 7+t=1+(6+t) by omega,pow_add,mul_assoc]; rfl
  have wz : w<z := by rw [mul_assoc] at cow; omega
  have paid' : 9*w+23=2^(7+t)*B := paid
  have paths := pumped_paths t m B w bp (by dsimp [m]; omega) val paid'
  dsimp only at paths
  have toz := ascent (2+t) (2*B) (by omega)
  rw [←zv,Nat.add_sub_cancel] at toz
  have repV : 2^(3+t)*B=2^(2+t)*(2*B) := by
    rw [show 3+t=2+t+1 by omega,pow_succ,mul_assoc]
  rw [←repV] at toz
  have wtoz : run (6+t) w=z := by
    rw [show 6+t=4+(2+t) by omega,run_add,paths.1,toz]
  have mn : m-7=2*n := by dsimp [m,n]; omega
  have hi : run (20+t+(m-7)) (3*w)=3^n+1 := by
    rw [run_add,paths.2.2.2.2,mn,pow_mul]
    have tr := PaidCheckpoint.positive_turns n 1
    simpa only [mul_one,show (2:ℕ)^2=4 by decide] using tr
  have bound := contraction (81*j)
  change 2^40*(3^n+1)<128*4^n at bound
  have pm : 2^m=128*4^n := by
    rw [show m=7+2*n by dsimp [m,n]; omega,pow_add,pow_mul]; rfl
  have index : 3≤173+162*j := by omega
  have large : 8≤2^m := Nat.pow_le_pow_right (n:=2) (by decide) index
  rw [←pm] at bound
  have final : 2^40*(3^n+1)<z := by
    clear * -parent large bound
    omega
  exact ⟨w,3^n+1,wp,wz,wc,wtoz,hi,Nat.zero_lt_succ _,final⟩

/-- The simple direct floor alternative, valid for every original
positive integer with 3^69 dividing its shift. -/
theorem deep_shift (t A z : ℕ) (pos : 0<A) (shape : z+1=3^(69+t)*A) :
    ∃ y, 0<y ∧ 2^40*y<z ∧ run (69+t) y=z := by
  have ratio' : 2^40*(2:ℕ)^(69+t)<3^(69+t) := by
    clear shape pos A z
    induction t with
    | zero => decide +kernel
    | succ t ih =>
      rw [show 69+(t+1)=69+t+1 by omega,pow_succ (2:ℕ),pow_succ (3:ℕ)]
      omega
  have b := Nat.mul_lt_mul_of_pos_right ratio' pos
  rw [mul_assoc] at b
  have d : 2≤2^(69+t)*A := by
    have h : 2≤(2:ℕ)^(69+t) := Nat.pow_le_pow_right (n:=2) (by decide) (by omega : 1≤69+t)
    have v := Nat.mul_le_mul_right A h
    omega
  have orig := ascent (69+t) A pos
  rw [←shape,Nat.add_sub_cancel] at orig
  refine ⟨_,by omega,?_,orig⟩
  have eq : 2^(69+t)*A-1+1=2^(69+t)*A := by omega
  have eq' := congrArg (fun n : ℕ => 2^40*n) eq
  norm_num [Nat.mul_add] at eq'
  omega

theorem valuation_return (j t B z : ℕ) (bp : 0<B)
    (parent : 81*z+271=128*2^(173+162*j))
    (val : 3^(6+t)*B+95=2^(173+162*j+6))
    (address : (2^(7+t)*B)%27=14 ∨ 67≤t)
    (floor : ∀ y, 0<y → 2^40*y<z → Good y)
    (canonical : ∀ w, 0<w → w<z → w%48=17 → Good (3*w) → Good w) : Good z := by
  rcases address with digit|deep
  · obtain ⟨w,x,wp,wz,wc,lo,hi,xp,xz⟩:=paid_valuation j t B z bp parent val digit
    have gx := floor x xp xz
    have g3 := (good_run _ _).mp (hi ▸ gx)
    have gw := (good_run (6+t) w).mpr (canonical w wp wz wc g3)
    rwa [lo] at gw
  · have zf := parent_link t _ z B parent val
    rw [show 2+t=69+(t-67) by omega] at zf
    obtain ⟨y,yp,yz,comm⟩:=deep_shift (t-67) (2*B) z (by omega) zf
    have gy := (good_run (69+(t-67)) y).mpr (floor y yp yz)
    rwa [comm] at gy

#print axioms pumped_paths
#print axioms paid_valuation
#print axioms deep_shift
#print axioms valuation_return
end TernaryPump
