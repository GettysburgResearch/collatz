import CoreBranching
import Mathlib.Tactic.Linarith

/-! Small positive visitors to a Mersenne orbit, with two independent
native clocks. All clocks are for CoreBranching.step. -/
set_option autoImplicit false
set_option warningAsError true
namespace PeakRigidity
open CoreBranching

def grade : ℕ → ℕ → ℕ
  | 0, _ => 0
  | j+1, x => grade j x + run j x % 2

private theorem last (j x : ℕ) : run (j+1) x = step (run j x) := by
  simpa [run] using run_add j 1 x

private theorem shifted_step (v : ℕ) :
    ((step v : ℕ) : ℚ) + 1 ≤ (3/2 : ℚ)^(v%2) * (v+1) ∧
    (v:ℚ)+1 ≤ 2*((step v:ℚ)+1) := by
  by_cases h : v%2=0
  · have e : 2*step v=v := by simp [step,h]; omega
    have e' : (2:ℚ)*(step v:ℚ)=v := by exact_mod_cast e
    rw [h,pow_zero,one_mul]
    constructor <;> linarith
  · have h' : v%2=1 := by omega
    have e : 2*step v=3*v+1 := by simp [step,h]; omega
    have e' : (2:ℚ)*(step v:ℚ)=3*v+1 := by exact_mod_cast e
    rw [h',pow_one]
    constructor <;> linarith

theorem shifted (j x : ℕ) :
    (run j x:ℚ)+1 ≤ (3/2 : ℚ)^(grade j x)*(x+1) ∧
    (x:ℚ)+1 ≤ 2^j*((run j x:ℚ)+1) := by
  induction j with
  | zero => simp [run,grade]
  | succ j ih =>
    have s := shifted_step (run j x)
    rw [last,grade,pow_add,pow_succ]
    constructor
    · calc
        _ ≤ _ := s.1
        _ ≤ (3/2:ℚ)^(run j x%2) * ((3/2:ℚ)^(grade j x)*(x+1)) :=
          mul_le_mul_of_nonneg_left ih.1 (by positivity)
        _ = _ := by ring
    · calc
        _ ≤ _ := ih.2
        _ ≤ (2:ℚ)^j*(2*((step (run j x):ℚ)+1)) :=
          mul_le_mul_of_nonneg_left s.2 (by positivity)
        _ = _ := by ring

theorem meeting_grade (m i h x : ℕ) (sm : x+1<2^m)
    (hit : run i (3^m-1)=run h x) : m<grade h x+2*i := by
  have a := (shifted i (3^m-1)).2
  have b := (shifted h x).1
  have p : 0<(3:ℕ)^m := by positivity
  have three : (((3^m-1 : ℕ):ℚ)+1)=(3:ℚ)^m := by
    exact_mod_cast (show (3^m-1:ℕ)+1=3^m by omega)
  rw [three,hit] at a
  have sm' : (x:ℚ)+1 < (2:ℚ)^m := by exact_mod_cast sm
  have c : (3:ℚ)^m < 2^i*((3/2:ℚ)^(grade h x)*2^m) := by
    apply lt_of_le_of_lt a
    apply mul_lt_mul_of_pos_left _ (by positivity)
    exact lt_of_le_of_lt b (mul_lt_mul_of_pos_left sm' (by positivity))
  have w : (3/2:ℚ)^m < 2^i*(3/2:ℚ)^(grade h x) := by
    rw [div_pow,div_lt_iff₀ (by positivity)]
    linarith only [c, show (2:ℚ)^i*((3/2:ℚ)^(grade h x)*2^m)=
      2^i*(3/2:ℚ)^(grade h x)*2^m by ring]
  have ii : (2:ℚ)^i ≤ (3/2:ℚ)^(2*i) := by
    rw [pow_mul]
    exact pow_le_pow_left₀ (by norm_num) (by norm_num) _
  have lim : (3/2:ℚ)^m < (3/2:ℚ)^(grade h x+2*i) := by
    rw [pow_add,mul_comm]
    exact w.trans_le (mul_le_mul_of_nonneg_right ii (by positivity))
  exact (pow_lt_pow_iff_right₀ (by norm_num : (1:ℚ)<3/2)).mp lim

private def carry : ℕ → ℕ → ℤ
  | 0, _ => -1
  | j+1, x => if run j x % 2=0 then carry j x else 3*carry j x+2^j

private theorem carry_bounds (j x : ℕ) :
    -(3:ℤ)^j ≤ carry j x ∧ carry j x < 3^j-2^j := by
  induction j with
  | zero => norm_num [carry]
  | succ j ih =>
    have a : 0<(2:ℤ)^j := by positivity
    have b : (2:ℤ)^j≤3^j := pow_le_pow_left₀ (by decide) (by decide) _
    simp only [carry,pow_succ]
    split <;> omega

private theorem carry_identity (j x : ℕ) :
    (2:ℤ)^j*(run j x:ℤ) = 3^(grade j x)*((x:ℤ)+1)+carry j x := by
  induction j with
  | zero => simp [run,grade,carry]
  | succ j ih =>
    rw [last,grade,carry,pow_succ]
    split
    next z =>
      have e : 2*step (run j x)=run j x := by simp [step,z]; omega
      have e' : (2:ℤ)*(step (run j x):ℤ)=run j x := by exact_mod_cast e
      rw [z,Nat.add_zero,mul_assoc,e',ih]
    next nz =>
      have z : run j x%2=1 := by omega
      have e : 2*step (run j x)=3*run j x+1 := by simp [step,nz]; omega
      have e' : (2:ℤ)*(step (run j x):ℤ)=3*run j x+1 := by exact_mod_cast e
      rw [z,pow_succ,mul_assoc,e']
      nlinarith only [ih]


private theorem scaled_bound (J j x : ℕ) (hj : j ≤ J) :
    |(2:ℤ)^(J-j)*carry j x| ≤ 3^J := by
  obtain ⟨a,b⟩ := carry_bounds j x
  have u : 0 ≤ (2:ℤ)^j := by positivity
  have bv : |carry j x| ≤ 3^j := (abs_le).mpr ⟨a,by omega⟩
  have coeff : (2:ℤ)^(J-j)*3^j ≤ 3^J := calc
    _ ≤ (3:ℤ)^(J-j)*3^j := by
      exact mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (by decide) (by decide) _) (by positivity)
    _ = _ := by rw [←pow_add,Nat.sub_add_cancel hj]
  have lo := mul_le_mul_of_nonneg_left a (show 0≤(2:ℤ)^(J-j) by positivity)
  have hi := mul_le_mul_of_nonneg_left (abs_le.mp bv).2 (show 0≤(2:ℤ)^(J-j) by positivity)
  apply abs_le.mpr
  constructor <;> nlinarith only [lo,hi,coeff]

/-- Clearing the two offsets at a common binary denominator preserves
their full ternary gain. -/
private theorem clear_offsets (J i l a b e : ℕ) 
    (A B : ℤ) (ha : J<a) (hb : J<b)
    (bound₁ : |(2:ℤ)^(J-i)*A| ≤ 3^J) (bound₂ : |(2:ℤ)^(J-l)*B| ≤ 3^J)
    (eqn : (2:ℤ)^(J-i)*(3^a+A)=(2:ℤ)^(J-l)*(3^b*e+B)) :
    (2:ℕ)^(J-i)*3^a=2^(J-l)*(3^b*e) := by
  let L : ℤ := 2^(J-i)*3^(a-(J+1))-2^(J-l)*(3^(b-(J+1))*e)
  have fa : (3:ℤ)^(J+1)*3^(a-(J+1))=3^a := by rw [←pow_add]; congr 1; omega
  have fb : (3:ℤ)^(J+1)*3^(b-(J+1))=3^b := by rw [←pow_add]; congr 1; omega
  have key : (3:ℤ)^(J+1)*L = 2^(J-l)*B-2^(J-i)*A := by
    dsimp [L]
    calc
      _ = (2:ℤ)^(J-i)*(3^(J+1)*3^(a-(J+1)))
        -2^(J-l)*(3^(J+1)*3^(b-(J+1))*e) := by ring
      _ = _ := by rw [fa,fb]; linarith only [eqn]
  obtain ⟨l₁,u₁⟩:=abs_le.mp bound₁
  obtain ⟨l₂,u₂⟩:=abs_le.mp bound₂
  have p : 0<(3:ℤ)^J := by positivity
  have sq : (3:ℤ)^(J+1)*L=0 := by
    rw [pow_succ] at key ⊢
    by_cases z : L=0
    · simp [z]
    · rcases lt_or_gt_of_ne z with neg|pos
      · have h := mul_le_mul_of_nonneg_left (show L≤ -1 by omega) (show 0≤(3:ℤ)^J*3 by positivity)
        omega
      · have h := mul_le_mul_of_nonneg_left (show 1≤L by omega) (show 0≤(3:ℤ)^J*3 by positivity)
        omega
  have off : (2:ℤ)^(J-l)*B=(2:ℤ)^(J-i)*A := by omega
  have leading : (2:ℤ)^(J-i)*3^a=(2:ℤ)^(J-l)*(3^b*e) := by
    linarith only [eqn,off]
  exact_mod_cast leading

private theorem equal_binary (I L u v : ℕ) (hu : Odd u) (hv : Odd v)
    (e : 2^I*u=2^L*v) : I=L := by
  have lower (I L u v : ℕ) (hu : Odd u) (e : 2^I*u=2^L*v) : L≤I := by
    by_contra! lt
    obtain ⟨k,hk⟩ : ∃ k, L=I+(k+1) := ⟨L-I-1,by omega⟩
    rw [hk,pow_add,Nat.mul_assoc] at e
    have a := Nat.eq_of_mul_eq_mul_left (by positivity : 0<2^I) e
    obtain ⟨t,ht⟩ := hu
    rw [pow_succ] at a
    have z : 2^k*2*v=2*(2^k*v) := by ring
    omega
  exact Nat.le_antisymm (lower _ _ _ _ hv e.symm) (lower _ _ _ _ hu e)

private theorem grade_add (a b x : ℕ) :
    grade (a+b) x = grade a x+grade b (run a x) := by
  induction b with
  | zero => simp [grade]
  | succ b ih =>
    rw [←Nat.add_assoc,grade,ih,run_add,grade,Nat.add_assoc]

private theorem ascent (n b : ℕ) (pos : 0<b) :
    run n (2^n*b-1)=3^n*b-1 ∧ grade n (2^n*b-1)=n := by
  induction n generalizing b with
  | zero => simp [run,grade]
  | succ n ih =>
    have p : 0<2^n*b := by positivity
    have form : 2^(n+1)*b-1=2*(2^n*b-1)+1 := by rw [pow_succ,show 2^n*2*b=2*(2^n*b) by ring]; omega
    have st : step (2^(n+1)*b-1)=2^n*(3*b)-1 := by
      rw [form,step_odd,show 2^n*(3*b)=3*(2^n*b) by ring]; omega
    have h := ih (3*b) (by omega)
    have r : n+1=1+n := by omega
    have word : run 1 (2^(n+1)*b-1)=2^n*(3*b)-1 := by simpa [run] using st
    have odd : grade 1 (2^(n+1)*b-1)=1 := by simp [grade,run,form]
    constructor
    · calc
        _ = run n (run 1 (2^(n+1)*b-1)) := by
          conv_lhs => lhs; rw [r]
          rw [run_add]
        _ = 3^n*(3*b)-1 := by rw [word,h.1]
        _ = _ := by rw [pow_succ]; ring_nf
    · calc
        _ = grade 1 (2^(n+1)*b-1)+grade n (run 1 (2^(n+1)*b-1)) := by
          conv_lhs => lhs; rw [r]
          rw [grade_add]
        _ = n+1 := by rw [odd,word,h.2]; omega

/-- A supplied smaller source with an independent postpeak clock must
be a pure Mersenne-peak lift whenever both clocks lie in the stated cone. -/
theorem postpeak_rigidity (m i l n b : ℕ) (positive : 0<b) (odd : Odd b)
    (small : 2^n*b<2^m) (cone : 2*i+max i l<m)
    (hit : run i (3^m-1)=run (n+l) (2^n*b-1)) :
    i=l ∧ ∃ d, b=3^d ∧ n+d<m ∧
      run i (3^m-1)=run i (3^(n+d)-1) ∧
      n+d+grade i (3^(n+d)-1)=m+grade i (3^m-1) := by
  let J := max i l
  let u := 3^m-1
  let v := 3^n*b-1
  let p := grade i u
  let q := grade l v
  have sp : 0<2^n*b := by positivity
  have np : 0<3^n*b := by positivity
  have mp : 0<(3:ℕ)^m := by positivity
  have ab := ascent n b positive
  have base : run i u=run l v := by simpa [u,v,run_add,ab.1] using hit
  have high := meeting_grade m i (n+l) (2^n*b-1) (by omega) hit
  rw [grade_add,ab.1,ab.2] at high
  have hj₁ : i≤J := le_max_left _ _
  have hj₂ : l≤J := le_max_right _ _
  have ha : J<m+p := by dsimp [J]; omega
  have hb : J<n+q := by dsimp [q,v,J]; omega
  have uu : (u:ℤ)+1=(3:ℤ)^m := by
    exact_mod_cast (show u+1=3^m by dsimp [u]; omega)
  have vv : (v:ℤ)+1=(3:ℤ)^n*b := by
    exact_mod_cast (show v+1=3^n*b by dsimp [v]; omega)
  have e₁ := carry_identity i u
  have e₂ := carry_identity l v
  rw [uu] at e₁
  rw [vv] at e₂
  change (2:ℤ)^i * (run i u:ℤ)=3^p*3^m+carry i u at e₁
  change (2:ℤ)^l * (run l v:ℤ)=3^q*(3^n*b)+carry l v at e₂
  have e : (2:ℤ)^(J-i)*(3^(m+p)+carry i u) =
      2^(J-l)*(3^(n+q)*b+carry l v) := by
    rw [pow_add,pow_add,show (3:ℤ)^m*3^p=3^p*3^m by ring,
        show (3:ℤ)^n*3^q*b=3^q*(3^n*b) by ring,←e₁,←e₂,
        ←mul_assoc,←mul_assoc,←pow_add,←pow_add,
        Nat.sub_add_cancel hj₁,Nat.sub_add_cancel hj₂,base]
  have eqn := clear_offsets J i l (m+p) (n+q) b _ _ ha hb
    (scaled_bound J i u hj₁) (scaled_bound J l v hj₂) e
  have eqClock := equal_binary (J-i) (J-l) (3^(m+p)) (3^(n+q)*b)
    ((by decide : Odd (3:ℕ)).pow) (((by decide : Odd (3:ℕ)).pow).mul odd) eqn
  have same : i=l := by omega
  rw [←same] at eqn
  have leading := Nat.eq_of_mul_eq_mul_left (by positivity : 0<2^(J-i)) eqn
  have le : n+q ≤ m+p := by
    apply (pow_le_pow_iff_right₀ (by decide : 1<(3:ℕ))).mp
    rw [leading]
    exact Nat.le_mul_of_pos_right _ positive
  let d := m+p-(n+q)
  have split : m+p=n+q+d := by dsimp [d]; omega
  have val : b=3^d := by
    rw [split,pow_add] at leading
    exact (Nat.eq_of_mul_eq_mul_left (by positivity : 0<3^(n+q)) leading).symm
  have lower : n+d<m := by
    apply (pow_lt_pow_iff_right₀ (by decide : 1<(2:ℕ))).mp
    rw [pow_add]
    exact lt_of_le_of_lt (Nat.mul_le_mul_left (2^n)
      (show 2^d≤b by rw [val]; exact Nat.pow_le_pow_left (by decide) _)) small
  have vp : v=3^(n+d)-1 := by dsimp [v]; rw [val,pow_add]
  refine ⟨same,d,val,lower,?_,?_⟩
  · simpa [vp,same,u] using base
  · have g : grade i (3^(n+d)-1)=q := by change _=grade l v; rw [←vp,same]
    change n+d+grade i (3^(n+d)-1)=m+p
    rw [g]; omega

private theorem peak_carry_odd (m i : ℕ) : carry i (3^m-1)%2=1 := by
  induction i with
  | zero => norm_num [carry]
  | succ i ih =>
    rcases i with _|i
    · obtain ⟨a,ha⟩ := (show Odd ((3:ℕ)^m) from (by decide : Odd (3:ℕ)).pow)
      simp [carry,run,ha]
    · rw [carry]
      split
      · exact ih
      · rw [pow_succ]; omega

/-- The other visitor cannot be on its own initial ascent, including
at clock zero, while the top postpeak clock lies inside the linear cone. -/
theorem prepeak_disjoint (m i h n b : ℕ) (positive : 0<b)
    (small : 2^n*b<2^m) (before : h<n) (cone : 3*i<m) :
    run i (3^m-1) ≠ run h (2^n*b-1) := by
  intro hit
  let B := 2^(n-h)*b
  have posB : 0<B := by dsimp [B]; positivity
  have src : 2^n*b=2^h*B := by
    dsimp [B]; rw [←mul_assoc,←pow_add]; congr 2; omega
  have paths := ascent h B posB
  have sourcepos : 0<2^n*b := by positivity
  have high := meeting_grade m i h (2^n*b-1) (by omega) hit
  rw [src,paths.2] at high
  have hm : n<m := by
    apply (pow_lt_pow_iff_right₀ (by decide : 1<(2:ℕ))).mp
    exact lt_of_le_of_lt (Nat.le_mul_of_pos_right _ positive) small
  have hi : i<h := by omega
  have zero : i≠0 := by omega
  have e := carry_identity i (3^m-1)
  have mp : 0<(3:ℕ)^m := by positivity
  have uu : ((3^m-1:ℕ):ℤ)+1=(3:ℤ)^m := by exact_mod_cast (show (3^m-1:ℕ)+1=3^m by omega)
  rw [uu,hit,src,paths.1] at e
  have np : 0<3^h*B := by positivity
  have vv : ((3^h*B-1:ℕ):ℤ)=(3:ℤ)^h*B-1 := by rw [Nat.cast_sub (by omega : 1≤3^h*B)]; push_cast; rfl
  rw [vv] at e
  let p := grade i (3^m-1)
  have fac : (3:ℤ)^h*3^(m-h) = 3^m := by rw [←pow_add]; congr 1; omega
  let D : ℤ := 2^i*B-3^p*3^(m-h)
  have key : (3:ℤ)^h*D=carry i (3^m-1)+2^i := by
    dsimp [D]
    calc
      _ = (2:ℤ)^i*((3:ℤ)^h*B)-3^p*(3^h*3^(m-h)) := by ring
      _ = _ := by rw [fac]; dsimp [p]; linarith only [e]
  have bnd := carry_bounds i (3^m-1)
  have pt : 0<(2:ℤ)^i := by positivity
  have strict : (3:ℤ)^i<3^h := pow_lt_pow_right₀ (by decide) hi
  have odd := peak_carry_odd m i
  have even : (2:ℤ)^i%2=0 := by
    rcases i with _|i
    · omega
    · rw [pow_succ]; omega
  rcases lt_trichotomy D 0 with neg|eq|pos
  · have a := mul_le_mul_of_nonneg_left (show D≤ -1 by omega) (show 0≤(3:ℤ)^h by positivity)
    omega
  · rw [eq,mul_zero] at key
    omega
  · have a := mul_le_mul_of_nonneg_left (show 1≤D by omega) (show 0≤(3:ℤ)^h by positivity)
    omega

#print axioms shifted
#print axioms meeting_grade
#print axioms postpeak_rigidity
#print axioms prepeak_disjoint
end PeakRigidity
