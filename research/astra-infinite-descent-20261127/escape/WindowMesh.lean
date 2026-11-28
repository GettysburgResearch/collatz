import InverseSpreading
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.FieldSimp

/-! A finite rotation cover gives ordinary sources in relative windows. The
same integer m appearing in the cover is the actual shortcut visit clock. -/
set_option autoImplicit false
set_option warningAsError true

namespace FastWindow
open CoreBranching PeakRigidity InverseSpreading

private theorem seed {L y : ℕ} (hL : 0<L) (hy : unitOdd y) (d : ℕ) :
    ∃ a S B : ℕ, unitOdd a ∧ run S a=y ∧ grade S a=d ∧ S≤L+3+6*d ∧
       3^d*a+B=2^S*y ∧ 5*2^L*B≤8*2^S := by
  cases d with
  | zero => exact ⟨y,0,0,hy,rfl,rfl,by omega,by simp,by simp⟩
  | succ r =>
    obtain ⟨a,S,B,ua,hit,gr,_,hi,eqn,slack⟩ := spread_witness hy hL r
    exact ⟨a,S,B,ua,hit,gr,by omega,eqn,by omega⟩

private theorem small_remainder {P Q T R y ε : ℝ}
    (positive : 0<P) (time : 0<T) (source : 1≤y) (ep : 0<ε)
    (calibration : 8*(1+ε)≤5*ε*P) (form : Q+R=T*y)
    (cost : 5*P*R≤8*T) : T*y≤(1+ε)*Q := by
  have rem : (1+ε)*R≤ε*(T*y) := by
    apply (mul_le_mul_iff_right₀ (show 0<5*P by positivity)).mp
    calc
      5*P*((1+ε)*R) = (1+ε)*(5*P*R) := by ring
      _ ≤ (1+ε)*(8*T) := mul_le_mul_of_nonneg_left cost (by positivity)
      _ = (8*(1+ε))*T := by ring
      _ ≤ (5*ε*P)*T := mul_le_mul_of_nonneg_right calibration time.le
      _ ≤ (5*ε*P)*T*y := le_mul_of_one_le_right (by positivity) source
      _ = _ := by ring
  rw [←form] at rem ⊢
  linarith

/-- The reference multiplicative mesh may be certified by an explicit finite
rotation calculation. For any target unit and every real X above the displayed
uniform threshold this produces a positive ordinary unit in the actual window.
The final inequality controls visit time beyond the absolute halving floor. -/
theorem visit_from_mesh_with (mark : ℕ → ℕ → Prop) {ε X : ℝ} {L D y : ℕ} (ep : 0<ε) (hL : 0<L)
    (calibration : 8*(1+ε)≤5*ε*(2:ℝ)^L) (hy : unitOdd y)
    (large : (2:ℝ)^(L+3+6*D)*y≤X)
    (mesh : ∀ u : ℝ, 1≤u → ∃ d m : ℕ, d≤D ∧
      u≤(2:ℝ)^m/3^d ∧ (2:ℝ)^m/3^d<(1+ε)*u ∧ mark d m) :
    ∃ z m d : ℕ, 0<z ∧ z%3≠0 ∧ X≤z ∧ (z:ℝ)<(1+ε)^2*X ∧
      run m z=y ∧ grade m z=d ∧ d≤D ∧
      (2:ℝ)^m*y≤(1+ε)*3^d*z ∧ mark d m := by
  have yp : 0<y := by have := hy.1; omega
  have yr : 1≤(y:ℝ) := by exact_mod_cast yp
  have ypositive : 0<(y:ℝ) := by positivity
  have base : 1≤(2:ℝ)^(L+3+6*D) := one_le_pow₀ (by norm_num)
  have yx : (y:ℝ)≤X := (le_mul_of_one_le_left ypositive.le base).trans large
  have xp : 0<X := ypositive.trans_le yx
  have enlarge : X≤(1+ε)*X := by linarith [mul_pos ep xp]
  let u := (1+ε)*X/y
  have has : 1≤u := by dsimp [u]; apply (le_div_iff₀ ypositive).mpr; simpa using yx.trans enlarge
  obtain ⟨d,m,dBound,below,above,marked⟩ := mesh u has
  obtain ⟨a,S,B,ua,visit,gr,SBound,eqn,slack⟩ := seed hL hy d
  have three : 0<(3:ℝ)^d := by positivity
  have threeOne : 1≤(3:ℝ)^d := one_le_pow₀ (by norm_num)
  have bot : ((1+ε)*X)*3^d≤(2:ℝ)^m*y :=
    (div_le_div_iff₀ ypositive three).mp below
  have top : (2:ℝ)^m*y < ((1+ε)^2*X)*3^d := by
    have h := (div_lt_iff₀ three).mp above
    dsimp [u] at h
    calc
      _ < ((1+ε)*((1+ε)*X/y)*3^d)*y := mul_lt_mul_of_pos_right h ypositive
      _ = _ := by field_simp
  have spow : (2:ℝ)^S≤2^m := by
    apply (mul_le_mul_iff_left₀ ypositive).mp
    calc
      (2:ℝ)^S*y ≤ 2^(L+3+6*D)*y :=
        mul_le_mul_of_nonneg_right (pow_le_pow_right₀ (by norm_num) (by omega)) ypositive.le
      _ ≤ X := large
      _ ≤ (1+ε)*X := enlarge
      _ ≤ (1+ε)*X*3^d := le_mul_of_one_le_right (by positivity) threeOne
      _ ≤ _ := bot
  have Sm : S≤m := (pow_le_pow_iff_right₀ (by norm_num : 1<(2:ℝ))).mp spow
  let k := m-S
  have period : k+S=m := by dsimp [k]; omega
  let z := 2^k*a
  have ha : 0<a := by have := ua.1; omega
  have zp : 0<z := by dsimp [z]; positivity
  obtain ⟨actual,odds,uz⟩ := lift_run_grade_unit k S a y visit ua.2
  rw [period] at actual odds
  have fr : (3:ℝ)^d*a+B=(2:ℝ)^S*y := by exact_mod_cast eqn
  have sr : 5*(2:ℝ)^L*B≤8*(2:ℝ)^S := by exact_mod_cast slack
  have seedLower := small_remainder (by positivity : 0<(2:ℝ)^L) (by positivity : 0<(2:ℝ)^S)
    yr ep calibration fr sr
  have kr : 0<(2:ℝ)^k := by positivity
  have zr : (z:ℝ)=2^k*a := by dsimp [z]; norm_cast
  have scale : (2:ℝ)^m=2^k*2^S := by rw [←period,pow_add]
  have slow : (2:ℝ)^m*y ≤ (1+ε)*(3^d*z) := by
    rw [zr,scale]
    nlinarith only [mul_le_mul_of_nonneg_left seedLower kr.le]
  have fast : (3:ℝ)^d*z≤2^m*y := by
    rw [zr,scale]
    have l : (3:ℝ)^d*a≤2^S*y := by linarith [show 0≤(B:ℝ) by positivity]
    nlinarith only [mul_le_mul_of_nonneg_left l kr.le]
  refine ⟨z,m,d,zp,uz,?_,?_,actual,odds.trans gr,dBound,(by linarith only [slow]),marked⟩
  · apply (mul_le_mul_iff_left₀ (mul_pos (show 0<1+ε by positivity) three)).mp
    nlinarith only [bot,slow]
  · apply (mul_lt_mul_iff_left₀ three).mp
    nlinarith only [fast,top]

theorem visit_from_mesh {ε X : ℝ} {L D y : ℕ} (ep : 0<ε) (hL : 0<L)
    (calibration : 8*(1+ε)≤5*ε*(2:ℝ)^L) (hy : unitOdd y)
    (large : (2:ℝ)^(L+3+6*D)*y≤X)
    (mesh : ∀ u : ℝ, 1≤u → ∃ d m : ℕ, d≤D ∧
      u≤(2:ℝ)^m/3^d ∧ (2:ℝ)^m/3^d<(1+ε)*u) :
    ∃ z m d : ℕ, 0<z ∧ z%3≠0 ∧ X≤z ∧ (z:ℝ)<(1+ε)^2*X ∧
      run m z=y ∧ grade m z=d ∧ d≤D ∧
      (2:ℝ)^m*y≤(1+ε)*3^d*z := by
  obtain ⟨z,m,d,zp,uz,lo,hi,hit,gr,hd,clock,_⟩ :=
    visit_from_mesh_with (fun _ _ => True) ep hL calibration hy large (fun u hu => by
      obtain ⟨d,k,hd,lo,hi⟩ := mesh u hu
      exact ⟨d,k,hd,lo,hi,True.intro⟩)
  exact ⟨z,m,d,zp,uz,lo,hi,hit,gr,hd,clock⟩

#print axioms visit_from_mesh_with
#print axioms visit_from_mesh
end FastWindow
