module
public import ReturnOrbitPacking
import all HourEscapeBinary
import all HourEscapeSigned
import all HourCycleShadow
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.HourEscape
open Collatz.HourCycleShadow
set_option autoImplicit false

/-- A computable sample size, linear in the starting absolute rational value
and polynomial of degree 19 in the denominator at fixed strip width. -/
def rationalSample (d K : ℕ) (A : ℤ) : ℕ :=
  A.natAbs/d+1+(76*K^10)^20*((3^200)*(4*K^2*d))^19

def rationalHorizon (d K : ℕ) (A : ℤ) : ℕ := 30*K^4*rationalSample d K A

theorem sample_adequate {d K : ℕ} (A : ℤ) (kp : 0<K) :
    ((19^(stripPadding K))*4)^20*((3^200)*(4*K^2*d))^19<rationalSample d K A := by
  have pad : 19^(stripPadding K)*4≤76*K^10 := by
    nlinarith only [Nat.mul_le_mul_right 4 (padding_cost kp)]
  exact (Nat.mul_le_mul_right _ (Nat.pow_le_pow_left pad 20)).trans_lt
    (Nat.lt_add_of_pos_left (Nat.succ_pos _))

private theorem sample_large (d K : ℕ) (A : ℤ) (dp : 0<d) :
    A.natAbs≤d*rationalSample d K A := by
  have h := Nat.lt_mul_div_succ A.natAbs dp
  have bound : A.natAbs/d+1≤rationalSample d K A := by unfold rationalSample; omega
  exact h.le.trans (Nat.mul_le_mul_left d bound)

private theorem drift_before_horizon {d K n : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ}
    (kp : 0<K) (dp : 0<d) (np : 0<n)
    (small : (y 0).natAbs≤d*n)
    (path : ∀ i,i<30*K^4*n → (2:ℤ)^(e i)*y (i+1)=3*y i+d)
    (band : ∀ i,i≤30*K^4*n → 1≤(K:ℝ)*weight e i ∧ weight e i≤K) :
    (∀ i,i≤n → (y i).natAbs≤2*K^2*d*n) ∧
    (∀ i,i≤n → y i≠y (30*K^4*n)) := by
  let T := 30*K^4*n
  let w := weight e
  let v := fun i => (y i:ℝ)/w i
  have kr : 1≤(K:ℝ) := by exact_mod_cast kp
  have dr : 0<(d:ℝ) := by exact_mod_cast dp
  have nr : 0<(n:ℝ) := by exact_mod_cast np
  have wp (i : ℕ) : 0<w i := weight_pos e i
  have vp : v 0=(y 0:ℝ) := by simp [v,w,weight]
  have inc (i : ℕ) (hi : i<T) : v (i+1)-v i=(d:ℝ)/(3*w i) := by
    have eqn : (2:ℝ)^(e i)*(y (i+1):ℝ)=3*(y i:ℝ)+d := by exact_mod_cast path i hi
    have scale : (2:ℝ)^(e i)*w (i+1)=3*w i := weight_step e i
    dsimp only [v]
    field_simp [ne_of_gt (wp i),ne_of_gt (wp (i+1))]
    linear_combination (w (i+1))*eqn-(y (i+1):ℝ)*scale
  have drift (i : ℕ) (fits : i≤T) :
      v 0+(i:ℝ)*((d:ℝ)/(3*K))≤v i ∧ v i≤v 0+(i:ℝ)*(d*K) := by
    induction i with
    | zero => simp
    | succ i ih =>
      have old := ih (by omega)
      have bnd := band i (by change i≤T; omega)
      have denominator : 0<3*w i := mul_pos (by norm_num) (wp i)
      have low : (d:ℝ)/(3*K)≤d/(3*w i) := by
        apply (div_le_div_iff₀ (by positivity : 0<(3:ℝ)*K) denominator).mpr
        exact mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_left bnd.2 (by norm_num)) dr.le
      have high : (d:ℝ)/(3*w i)≤d*K := by
        apply (div_le_iff₀ denominator).mpr
        have lower : 1≤(K:ℝ)*w i := bnd.1
        nlinarith only [mul_le_mul_of_nonneg_left lower dr.le]
      have step := inc i (by omega)
      push_cast
      constructor <;> linarith only [old.1,old.2,step,low,high]
  have value (i : ℕ) : (y i:ℝ)=w i*v i := by dsimp [v]; field_simp [ne_of_gt (wp i)]
  have first : |(y 0:ℝ)|≤d*n := by
    have h : |y 0|≤((d*n:ℕ):ℤ) := by rw [←Int.natCast_natAbs]; exact_mod_cast small
    exact_mod_cast h
  have kn : 1≤K^4 := Nat.one_le_pow _ _ kp
  have nt : n≤T := by
    have h := Nat.mul_le_mul_right n kn
    dsimp [T]; nlinarith only [h,Nat.zero_le (K^4*n)]
  have dnK : (d:ℝ)*n≤(d:ℝ)*n*K :=
    by simpa using mul_le_mul_of_nonneg_left kr (show 0≤(d:ℝ)*n by positivity)
  have early (i : ℕ) (hi : i≤n) : |(y i:ℝ)|≤2*(K:ℝ)^2*d*n := by
    have bounds := drift i (hi.trans nt)
    have ir : (i:ℝ)≤n := by exact_mod_cast hi
    have increment := mul_le_mul_of_nonneg_right ir (show 0≤(d:ℝ)*K by positivity)
    have absV : |v i|≤2*((d:ℝ)*n*K) := by
      apply abs_le.mpr
      rw [vp] at bounds
      obtain ⟨al,ah⟩ := abs_le.mp first
      constructor <;> nlinarith only [al,ah,bounds.1,bounds.2,dnK,increment,
        show 0≤(i:ℝ)*((d:ℝ)/(3*K)) by positivity,show 0≤(d:ℝ)*n*K by positivity]
    rw [value,abs_mul,abs_of_pos (wp i)]
    calc
      _ ≤ (K:ℝ)*(2*(d*n*K)) := mul_le_mul (band i (hi.trans nt)).2 absV (abs_nonneg _) (by positivity)
      _ = _ := by ring
  have late : 2*(K:ℝ)^2*d*n<(y T:ℝ) := by
    have last := (drift T (by omega)).1
    have number : (T:ℝ)*((d:ℝ)/(3*K))=10*(K:ℝ)^3*d*n := by
      dsimp [T]; push_cast; field_simp; ring
    rw [vp,number] at last
    have larger : (d:ℝ)*n≤(K:ℝ)^3*d*n := by
      have one : (1:ℝ)≤(K:ℝ)^3 := one_le_pow₀ kr
      have h := mul_le_mul_of_nonneg_right one (show 0≤(d:ℝ)*n by positivity)
      nlinarith only [h]
    have vhigh : 2*(K:ℝ)^3*d*n<v T := by
      have al := (abs_le.mp first).1
      nlinarith only [al,last,larger,mul_pos dr nr]
    have scale := mul_lt_mul_of_pos_left vhigh (wp T)
    have bnd := mul_le_mul_of_nonneg_right (band T (by omega)).1
      (show 0≤2*(K:ℝ)^2*d*n by positivity)
    rw [value]
    change 1*(2*(K:ℝ)^2*d*n)≤(K:ℝ)*w T*(2*(K:ℝ)^2*d*n) at bnd
    nlinarith only [scale,bnd]
  constructor
  · intro i hi
    have h : |y i|≤((2*K^2*d*n:ℕ):ℤ) := by exact_mod_cast early i hi
    rw [←Int.natCast_natAbs] at h
    exact_mod_cast h
  · intro i hi eqn
    have lim := (le_abs_self (y i:ℝ)).trans (early i hi)
    rw [eqn] at lim
    exact (not_le_of_gt late) lim

/-- The normalized weight at every prefix through the horizon belongs to
the closed interval from the reciprocal width to the width. -/
def FiniteWeightStrip (e : ℕ → ℕ) (K T : ℕ) : Prop :=
  ∀ i,i≤T → 1≤(K:ℝ)*weight e i ∧ weight e i≤K

/-- A signed dyadic history with odd states cannot stay in a bounded clock
strip through this explicit polynomial horizon. -/
theorem finite_dyadic_rational_rigidity {d K : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ}
    (kp : 0<K) (dp : 0<d) (pos : ∀ i,0<e i)
    (path : ∀ i,i<rationalHorizon d K (y 0) → (2:ℤ)^(e i)*y (i+1)=3*y i+d)
    (oddY : ∀ i,i≤rationalHorizon d K (y 0) → y i%2=1)
    (band : FiniteWeightStrip e K (rationalHorizon d K (y 0))) : False := by
  let n := rationalSample d K (y 0)
  let T := rationalHorizon d K (y 0)
  have np : 0<n := Nat.add_pos_left (Nat.succ_pos _) _
  have nt : n≤T := by
    have h := Nat.mul_le_mul_right n (Nat.one_le_pow 4 K kp)
    dsimp [T,rationalHorizon]; change n≤30*K^4*n; nlinarith only [h,Nat.zero_le (K^4*n)]
  obtain ⟨bounds,apart⟩ := drift_before_horizon kp dp np (sample_large d K (y 0) dp) path band
  have adv (i j : ℕ) (it : i<T) (jt : j<T) (eqn : y i=y j) : y (i+1)=y (j+1) := by
    have l := path i it
    rw [eqn] at l
    exact odd_part_unique (oddY _ (by change i+1≤T; omega)) (oddY _ (by change j+1≤T; omega))
      (l.trans (path j jt).symm)
  have distinct := distinct_before_extreme adv apart nt
  let D := 4*K^2*d
  have dbig := sample_adequate (d:=d) (y 0) kp
  obtain ⟨r,_,wide,cap⟩ := finite_packing_scale (H:=stripPadding K) (D:=D) (by dsimp [D]; positivity) np dbig
  apply finite_forward_packing path nt cap pos _ _ distinct
  · intro i fits
    have scale := window_factor (weight_step e) i (200*r)
    have first := mul_le_mul_of_nonneg_left (band (i+200*r) (fits.trans nt)).1
      (show 0≤(2:ℝ)^(window e (200*r) i).sum by positivity)
    have last := mul_le_mul_of_nonneg_left (band i ((by omega : i≤n).trans nt)).2
      (show 0≤(3:ℝ)^(200*r) by positivity)
    have bound : (2:ℝ)^(window e (200*r) i).sum≤(K:ℝ)*K*3^(200*r) := by
      calc
        _ ≤ 2^(window e (200*r) i).sum*((K:ℝ)*weight e (i+200*r)) := by simpa using first
        _ = (K:ℝ)*(3^(200*r)*weight e i) := by rw [←scale]; ring
        _ ≤ (K:ℝ)*(3^(200*r)*K) := mul_le_mul_of_nonneg_left last (Nat.cast_nonneg K)
        _ = _ := by ring
    exact_mod_cast bound
  · intro i j hi hj
    have left := bounds i hi
    have right := bounds j hj
    have dist := Int.natAbs_sub_le (y i) (y j)
    change 4*K^2*d*n<3^(200*r) at wide
    exact (dist.trans (Nat.add_le_add left right)).trans_lt (by
      convert wide using 1; ring)

#print axioms finite_dyadic_rational_rigidity
end Collatz.Itinerary.HourEscape
