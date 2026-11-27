import EarlierOffsets

/-! Affine certificates for ordinary shortcut clocks and the canonical rank-three row. -/
set_option autoImplicit false
set_option warningAsError true
namespace UpperClock
open CoreBranching PeakRigidity FloorCounting

def intercept : ℕ → ℕ → ℕ
  | 0, _ => 0
  | j+1,x => if run j x%2=0 then intercept j x else 3*intercept j x+2^j

theorem last (j x : ℕ) : run (j+1) x=step (run j x) := by
  simpa [run] using run_add j 1 x

theorem affine (j x : ℕ) :
    2^j*run j x=3^(grade j x)*x+intercept j x := by
  induction j with
  | zero => simp [grade,run,intercept]
  | succ j ih =>
    rw [last,pow_succ,grade,pow_add,intercept,mul_assoc]
    split
    next e =>
      have st : 2*step (run j x)=run j x := by simp [step,e]; omega
      rw [st,e,pow_zero,mul_one,ih]
    next e =>
      have o : run j x%2=1 := by omega
      have st : 2*step (run j x)=3*run j x+1 := by simp [step,e]; omega
      rw [st,o,pow_one,mul_add,show 2^j*(3*run j x)=3*(2^j*run j x) by ring,ih]
      ring

theorem intercept_bound (j x : ℕ) : intercept j x+2^j≤3^j := by
  induction j with
  | zero => simp [intercept]
  | succ j ih =>
    simp only [intercept,pow_succ]
    split <;> omega

theorem word_extension (j d x : ℕ) :
    grade j x≤grade (j+d) x ∧ grade (j+d) x≤grade j x+d ∧
    (grade (j+d) x=grade j x → intercept (j+d) x=intercept j x) ∧
    (grade (j+d) x=grade j x+d →
      intercept (j+d) x+2^(j+d)=3^d*(intercept j x+2^j)) := by
  induction d with
  | zero => simp
  | succ d ih =>
    rw [show j+(d+1)=(j+d)+1 by omega]
    simp only [grade,intercept]
    rcases ih with ⟨lo,hi,flat,full⟩
    by_cases e : run (j+d) x%2=0
    · simp only [e,ite_true,add_zero]
      refine ⟨by omega,by omega,flat,?_⟩
      omega
    · have o : run (j+d) x%2=1 := by omega
      simp only [o,Nat.one_ne_zero,ite_false]
      refine ⟨by omega,by omega,by omega,?_⟩
      intro h
      have f := full (by omega)
      rw [pow_succ,pow_succ,show
        3*intercept (j+d) x+2^(j+d)+2^(j+d)*2=3*(intercept (j+d) x+2^(j+d)) by ring,f]
      ring

theorem intercept_mono (j d x : ℕ) : intercept j x≤intercept (j+d) x := by
  induction d with
  | zero => simp
  | succ d ih =>
    rw [show j+(d+1)=(j+d)+1 by omega,intercept]
    have pos : 0<(2:ℕ)^(j+d) := by positivity
    split <;> omega

theorem canonical_prefix (y : ℕ) (can : y%48=17) :
    grade 2 (3*y)=2 ∧ intercept 2 (3*y)=5 ∧
    grade 4 y=2 ∧ intercept 4 y=7 := by
  let t := y/48
  have yy : y=17+48*t := by dsimp [t]; omega
  have lo := lift_prefix 4 0 1 (1+3*t)
  have up := lift_prefix 2 0 3 (12+36*t)
  have ly : 1+2^(4+0)*(1+3*t)=y := by rw [yy]; ring
  have uy : 3+2^(2+0)*(12+36*t)=3*y := by rw [yy]; ring
  rw [ly] at lo
  rw [uy] at up
  have loG : grade 4 1=2 := by decide +kernel
  have upG : grade 2 3=2 := by decide +kernel
  have loR : run 4 1=1 := by decide +kernel
  have upR : run 2 3=8 := by decide +kernel
  rw [loG,loR] at lo
  rw [upG,upR] at up
  have ai := affine 2 (3*y)
  have bi := affine 4 y
  rw [up.1,up.2] at ai
  rw [lo.1,lo.2] at bi
  norm_num at ai bi
  exact ⟨up.2,by omega,lo.2,by omega⟩

theorem canonical_hit (y h : ℕ) (can : y%48=17) (hit : run h (3*y)=1) :
    2≤h ∧ 2≤grade h (3*y) ∧ 5≤intercept h (3*y) ∧
    (grade h (3*y)=2 → intercept h (3*y)=5) := by
  have p := canonical_prefix y can
  have ht : 2≤h := by
    by_contra! s
    interval_cases h
    · simp only [run] at hit
      omega
    · change step (3*y)=1 at hit
      unfold step at hit
      split at hit <;> omega
  obtain ⟨d,hd⟩:=Nat.exists_eq_add_of_le ht
  have a := word_extension 2 d (3*y)
  have m := intercept_mono 2 d (3*y)
  rw [←hd,p.1] at a
  rw [←hd,p.2.1] at m
  exact ⟨ht,a.1,m,fun h => (a.2.2.1 h).trans p.2.1⟩

theorem hard_mod (t : ℕ) : 2^(18+162*t)%27=1 := by
  have a : (2:ℕ)^18 ≡ 1 [MOD 27] := by decide +kernel
  have b : (2:ℕ)^162 ≡ 1 [MOD 27] := by decide +kernel
  have c := a.mul (b.pow t)
  change (2^18*(2^162)^t)%27=(1*1^t)%27 at c
  simpa only [pow_add,pow_mul,one_pow,mul_one] using c

/-- Any canonical upper certificate shorter than the hard row forces a
strict factor-two improvement of the underlying canonical source. -/
theorem shorter_forces_half (t z y h : ℕ) (row : 81*z+271=2^(18+162*t))
    (zc : z%48=17) (yc : y%48=17) (hit : run h (3*y)=1) (short : h<18+162*t) :
    2*y+31≤z := by
  let H := 18+162*t
  change 81*z+271=2^H at row
  change h<H at short
  have ht := canonical_hit y h yc hit
  have a := affine h (3*y)
  rw [hit,mul_one] at a
  have twice : 2*2^h≤2^H := by
    calc 2*2^h = 2^(h+1) := by rw [pow_succ,mul_comm]
         _ ≤ _ := Nat.pow_le_pow_right (by decide) short
  have res : 2^H%27=1 := hard_mod t
  have lim : 162*y≤81*z+271 := by
    by_cases rank : grade h (3*y)=2
    · rw [ht.2.2.2 rank,rank] at a
      norm_num at a
      have large : h+3≤H := by
        by_contra! small
        have h1 : H=h+1 ∨ H=h+2 := by omega
        rcases h1 with h1|h1
        · rw [h1,pow_add,a] at res
          omega
        · rw [h1,pow_add,a] at res
          omega
      have eight : 8*2^h≤2^H := by
        calc 8*2^h = 2^(h+3) := by rw [pow_add]; ring
             _ ≤ _ := Nat.pow_le_pow_right (by decide) large
      omega
    · have g : 27≤3^(grade h (3*y)) := Nat.pow_le_pow_right (by decide : 0<3)
          (show 3≤grade h (3*y) by omega)
      have b:=Nat.mul_le_mul_right (3*y) g
      omega
  omega

#print axioms affine
#print axioms word_extension
#print axioms canonical_hit
#print axioms shorter_forces_half
end UpperClock
