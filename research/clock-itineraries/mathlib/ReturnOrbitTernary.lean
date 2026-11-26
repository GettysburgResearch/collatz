module
public import ReturnOrbitBinary
import all ReturnOrbitBinary
import all HourEscapeSigned
import all HourEscapePacking
import all HourCycleShadow
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.HourEscape
open Collatz.HourCycleShadow
set_option autoImplicit false

private theorem finite_inverse_parent {d L : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} (dp : 0 < d)
    (pos : ∀ i,0 < e i) (path : ∀ i,i < L → 3*y (i+1)+(d:ℤ)=2^(e i)*y i) :
    ∀ i j, d ≤ i → d ≤ j → i < L → j < L → y (i+1)=y (j+1) → y i=y j := by
  induction d using Nat.strongRecOn generalizing L e y with
  | ind d ih =>
    have even (i : ℕ) (hi : i < L) : (3*y (i+1)+(d:ℤ))%2=0 := by
      obtain ⟨r,rfl'⟩ := Nat.exists_eq_add_of_le (show 1 ≤ e i from pos i)
      rw [path i hi,rfl',pow_add]
      change (2*2^r*y i)%2=0
      rw [mul_assoc]; omega
    by_cases odd : d%2=1
    · have o (i : ℕ) (hi : i < L) : y (i+1)%2=1 := by
        have h := even i hi
        have dc : (d:ℤ)%2=1 := by exact_mod_cast odd
        omega
      intro i j li lj it jt eqn
      have pi := path i it
      have pj := path j jt
      rw [eqn] at pi
      apply odd_part_unique (m:=e i) (n:=e j) _ _ (pi.symm.trans pj)
      · have z := o (i-1) (by omega); rwa [show i-1+1=i by omega] at z
      · have z := o (j-1) (by omega); rwa [show j-1+1=j by omega] at z
    · let d' := d/2
      let v := fun i => y (i+1)/2
      let f := fun i => e (i+1)
      have deq : d=2*d' := by dsimp [d']; omega
      have dc : (d:ℤ)=2*(d':ℤ) := by exact_mod_cast deq
      have norm (i : ℕ) (hi : i < L) : y (i+1)=2*v i := by
        have h := even i hi
        dsimp [v]; omega
      have reduced (i : ℕ) (hi : i < L-1) : 3*v (i+1)+(d':ℤ)=2^(f i)*v i := by
        have h := path (i+1) (by omega)
        rw [norm (i+1) (by omega),norm i (by omega),dc] at h
        dsimp only [f]
        nlinarith only [h]
      have back := ih d' (by dsimp [d']; omega) (by dsimp [d']; omega)
        (fun i => pos (i+1)) reduced
      intro i j li lj it jt eqn
      have si : i-1+1=i := by omega
      have sj : j-1+1=j := by omega
      have equal : v ((i-1)+1)=v ((j-1)+1) := by rw [si,sj]; exact congrArg (·/2) eqn
      have same := back (i-1) (j-1) (by dsimp [d']; omega) (by dsimp [d']; omega)
        (by omega) (by omega) equal
      have ni := norm (i-1) (by omega)
      have nj := norm (j-1) (by omega)
      rw [si] at ni
      rw [sj] at nj
      omega

private theorem inverse_bounds {d K L n : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ}
    (dp : 0 < d) (kp : 0 < K) (np : 0 < n)
    (small : (y 0).natAbs ≤ d*n) (band : FiniteWeightStrip e K L)
    (path : ∀ i,i < L → 3*y (i+1)+(d:ℤ)=2^(e i)*y i) :
    (∀ i,i ≤ L → (y i).natAbs ≤ K*d*n+K^2*i*d) ∧
    (∀ a j, a ≤ n → a ≤ L → 30*K^4*n ≤ j → j ≤ L → y j < y a) := by
  let w := weight e
  have kr : 1 ≤ (K:ℝ) := by exact_mod_cast kp
  have dr : 0 < (d:ℝ) := by exact_mod_cast dp
  have nr : 0 < (n:ℝ) := by exact_mod_cast np
  have initial : |(y 0:ℝ)|≤d*n := by
    have h : |y 0|≤((d*n:ℕ):ℤ) := by rw [←Int.natCast_natAbs]; exact_mod_cast small
    exact_mod_cast h
  have est (i : ℕ) (hi : i ≤ L) :
      3*K*w i*y i ≤ 3*K*(y 0:ℝ)-(i:ℝ)*d ∧
      3*(y 0:ℝ)-(i:ℝ)*d*K ≤ 3*w i*y i := by
    induction i with
    | zero => simp [w,weight]
    | succ i ih =>
      obtain ⟨older,newer⟩ := ih (by omega)
      have eqn : 3*(y (i+1):ℝ)+(d:ℝ)=(2:ℝ)^(e i)*(y i:ℝ) := by exact_mod_cast path i (by omega)
      have scale : (2:ℝ)^(e i)*w (i+1)=3*w i := weight_step e i
      have step : 3*w (i+1)*(y (i+1):ℝ)+d*w (i+1)=3*w i*(y i:ℝ) := by
        linear_combination w (i+1)*eqn+(y i:ℝ)*scale
      have scaled := congrArg ((K:ℝ)*·) step
      have lower : 1 ≤ (K:ℝ)*w (i+1) := (band _ hi).1
      have upper : w (i+1) ≤ K := (band _ hi).2
      have minCost := mul_le_mul_of_nonneg_left lower dr.le
      have maxCost := mul_le_mul_of_nonneg_left upper dr.le
      push_cast
      constructor <;> nlinarith only [older,newer,scaled,step,minCost,maxCost]
  have bnd (i : ℕ) (hi : i ≤ L) : |(y i:ℝ)|≤K*d*n+(K:ℝ)^2*i*d := by
    obtain ⟨up,low⟩ := est i hi
    have top : w i*(y i:ℝ) ≤ (y 0:ℝ) := by
      apply le_of_mul_le_mul_left (a:=(3:ℝ)*K) _ (by positivity)
      nlinarith only [up,show 0 ≤ (i:ℝ)*d by positivity]
    have bound : |w i*(y i:ℝ)|≤(d:ℝ)*n+(i:ℝ)*d*K := by
      apply abs_le.mpr
      obtain ⟨sl,sh⟩ := abs_le.mp initial
      constructor <;> nlinarith only [top,low,sl,sh,show 0 ≤ (i:ℝ)*d*K by positivity]
    have cmp := mul_le_mul_of_nonneg_left bound (show 0 ≤ (K:ℝ) by positivity)
    rw [abs_mul,abs_of_pos (weight_pos e i)] at cmp
    have one := mul_le_mul_of_nonneg_right (band i hi).1 (abs_nonneg (y i:ℝ))
    nlinarith only [cmp,one]
  constructor
  · intro i hi
    have h : |y i|≤((K*d*n+K^2*i*d:ℕ):ℤ) := by exact_mod_cast bnd i hi
    rw [←Int.natCast_natAbs] at h
    exact_mod_cast h
  · intro a j an al jl jL
    by_contra! rev
    have yrev : (y a:ℝ) ≤ (y j:ℝ) := by exact_mod_cast rev
    have up := (est j jL).1
    have cap := bnd a al
    have ar : (a:ℝ) ≤ n := by exact_mod_cast an
    have lower : -(2*(K:ℝ)^2*d*n) ≤ (y j:ℝ) := by
      have aa := mul_le_mul_of_nonneg_left ar (show 0 ≤ (K:ℝ)^2*d by positivity)
      have bb := mul_le_mul_of_nonneg_right kr (show 0 ≤ (K:ℝ)*d*n by positivity)
      nlinarith only [aa,bb,cap,neg_abs_le (y a:ℝ),yrev]
    have wj : 0 ≤ w j := (weight_pos e j).le
    have front := mul_le_mul_of_nonneg_left lower wj
    have stretch := mul_le_mul_of_nonneg_right (band j jL).2
      (show 0 ≤ 2*(K:ℝ)^2*d*n by positivity)
    have low : -(2*(K:ℝ)^3*d*n) ≤ w j*(y j:ℝ) := by nlinarith only [front,stretch]
    have scaled := mul_le_mul_of_nonneg_left low (show 0 ≤ 3*(K:ℝ) by positivity)
    have comp : (30:ℝ)*K^4*n ≤ j := by exact_mod_cast jl
    have last := mul_le_mul_of_nonneg_right comp dr.le
    have initialup := (le_abs_self (y 0:ℝ)).trans initial
    have top := mul_le_mul_of_nonneg_left initialup (show 0 ≤ 3*(K:ℝ) by positivity)
    have kcube : (1:ℝ) ≤ (K:ℝ)^3 := one_le_pow₀ kr
    have high := mul_le_mul_of_nonneg_right kcube (show 0 ≤ (K:ℝ)*d*n by positivity)
    nlinarith only [scaled,up,last,top,high,show 0 < (K:ℝ)^4*d*n by positivity]

private theorem finite_window_factor {e : ℕ → ℕ} {w : ℕ → ℝ} {L : ℕ}
    (rec : ∀ i,i < L → (2:ℝ)^(e i)*w (i+1)=3*w i) (i b : ℕ) (fit : i+b ≤ L) :
    (2:ℝ)^(window e b i).sum*w (i+b)=3^b*w i := by
  induction b generalizing i with
  | zero => simp [window]
  | succ b ih =>
    have prev := ih (i+1) (by omega)
    rw [show i+1+b=i+(b+1) by omega] at prev
    simp only [window,List.sum_cons,pow_add]
    calc
      _ = (2:ℝ)^(e i)*(2^(window e b (i+1)).sum*w (i+(b+1))) := by ring
      _ = 3^b*(2^(e i)*w (i+1)) := by rw [prev]; ring
      _ = _ := by rw [rec i (by omega)]; ring

/-- A horizon usable for every positive denominator of a ternary coordinate. -/
def inverseRationalHorizon (d K : ℕ) (A : ℤ) : ℕ :=
  (30*K^4+1)*rationalSample d (10*K^3) A

/-- A finite inverse rational shadow cannot persist on a bounded normalized
clock strip past a polynomial horizon, for arbitrary positive gaps and
every positive denominator. -/
theorem finite_ternary_rational_rigidity {d K : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ}
    (kp : 0 < K) (dp : 0 < d) (pos : ∀ i,0 < e i)
    (path : ∀ i,i < inverseRationalHorizon d K (y 0) → 3*y (i+1)+(d:ℤ)=2^(e i)*y i)
    (band : FiniteWeightStrip e K (inverseRationalHorizon d K (y 0))) : False := by
  let Q := 10*K^3
  let n := rationalSample d Q (y 0)
  let J := 30*K^4*n
  let L := inverseRationalHorizon d K (y 0)
  have Leq : L=J+n := by dsimp only [L,J,n,Q,inverseRationalHorizon]; ring
  have kn : 1 ≤ K^4 := Nat.one_le_pow 4 K kp
  have kn3 : 1 ≤ K^3 := Nat.one_le_pow 3 K kp
  have kq : K ≤ Q := by
    have h : K ≤ K^3 := by simpa using Nat.pow_le_pow_right kp (show 1 ≤ 3 by decide)
    dsimp [Q]; omega
  have np : 0 < n := Nat.add_pos_left (Nat.succ_pos _) _
  have qpos : 0 < Q := by dsimp [Q]; positivity
  let D := 4*Q^2*d
  have large : ((19^(stripPadding Q))*4)^20*((3^200)*D)^19 < n := sample_adequate (y 0) qpos
  have dbound : d ≤ n := by
    have bpos : 0 < ((19^(stripPadding Q))*4)^20 := by positivity
    have dd : d ≤ (3^200)*D := by
      have k1 : 1 ≤ Q^2 := Nat.one_le_pow 2 Q qpos
      have h := Nat.mul_le_mul_right d k1
      dsimp [D]; nlinarith only [h,Nat.zero_le (Q^2*d)]
    have pp : 0 < (3^200)*D := by dsimp [D]; positivity
    have power : (3^200)*D ≤ ((3^200)*D)^19 := by simpa using Nat.pow_le_pow_right pp (show 1 ≤ 19 by decide)
    have room := Nat.mul_le_mul_right (((3^200)*D)^19) bpos
    omega
  have nj : n ≤ J := by
    have h := Nat.mul_le_mul_right n kn
    dsimp [J]; nlinarith only [h,Nat.zero_le (K^4*n)]
  obtain ⟨size,apart⟩ := inverse_bounds dp kp np (sample_large d Q (y 0) dp) band path
  let T := L-d
  let g := fun i => e (L-(i+1))
  let z := fun i => y (L-i)
  have nt : n ≤ T := by dsimp [T]; omega
  have hpath (i : ℕ) (hi : i < T) : (2:ℤ)^(g i)*z (i+1)=3*z i+d := by
    have fit : L-(i+1) < L := by dsimp [T] at hi; omega
    have h := path (L-(i+1)) fit
    rw [show L-(i+1)+1=L-i by dsimp [T] at hi; omega] at h
    exact h.symm
  have parent := finite_inverse_parent dp pos path
  have advance (i j : ℕ) (hi : i < T) (hj : j < T) (eqn : z i=z j) : z (i+1)=z (j+1) := by
    apply parent (L-(i+1)) (L-(j+1)) <;> try (dsimp [T] at *; omega)
    simpa only [show L-(i+1)+1=L-i by dsimp [T] at hi; omega,
      show L-(j+1)+1=L-j by dsimp [T] at hj; omega] using eqn
  have away (i : ℕ) (hi : i ≤ n) : z i≠z T := by
    have h := apart d (L-i) dbound (by omega) (by change J ≤ L-i; omega) (by omega)
    change y (L-i)≠y (L-(L-d))
    rw [show L-(L-d)=d by omega]
    exact ne_of_lt h
  have distinct := distinct_before_extreme advance away nt
  obtain ⟨r,_,wide,cap⟩ := finite_packing_scale (H:=stripPadding Q) (D:=D) (by dsimp [D]; positivity) np large
  apply finite_forward_packing (K:=Q) hpath nt cap (fun i => pos _) _ _ distinct
  · intro i fits
    let w := fun j => (weight e (L-j))⁻¹
    have recurrence (j : ℕ) (hj : j < T) : (2:ℝ)^(g j)*w (j+1)=3*w j := by
      have rel := weight_step e (L-(j+1))
      rw [show L-(j+1)+1=L-j by dsimp [T] at hj; omega] at rel
      dsimp only [w,g]; field_simp [ne_of_gt (weight_pos e _)]
      linarith only [rel]
    have sb (j : ℕ) : 1 ≤ (Q:ℝ)*w j ∧ w j ≤ Q := by
      have bd := band (L-j) (by omega)
      have positive := weight_pos e (L-j)
      have qr : (K:ℝ) ≤ Q := by exact_mod_cast kq
      dsimp [w]
      constructor
      · rw [←div_eq_mul_inv]; exact (le_div_iff₀ positive).mpr (by simpa using bd.2.trans qr)
      · rw [inv_le_iff_one_le_mul₀ positive]
        exact bd.1.trans (mul_le_mul_of_nonneg_right qr positive.le)
    have scale := finite_window_factor recurrence i (200*r) (fits.trans nt)
    have first := mul_le_mul_of_nonneg_left (sb (i+200*r)).1
      (show 0 ≤ (2:ℝ)^(window g (200*r) i).sum by positivity)
    have last := mul_le_mul_of_nonneg_left (sb i).2 (show 0 ≤ (3:ℝ)^(200*r) by positivity)
    have bound : (2:ℝ)^(window g (200*r) i).sum ≤ (Q:ℝ)*Q*3^(200*r) := by
      calc
        _ ≤ 2^(window g (200*r) i).sum*((Q:ℝ)*w (i+200*r)) := by simpa using first
        _ = (Q:ℝ)*(3^(200*r)*w i) := by rw [←scale]; ring
        _ ≤ (Q:ℝ)*(3^(200*r)*Q) := mul_le_mul_of_nonneg_left last (Nat.cast_nonneg Q)
        _ = _ := by ring
    exact_mod_cast bound
  · intro i j _ _
    have limit (a : ℕ) : (z a).natAbs ≤ 2*Q^2*d*n := by
      have h := size (L-a) (by omega)
      have c := Nat.mul_le_mul_left (K^2*d) (show L-a ≤ L by omega)
      have norm : K*d*n+K^2*(L-a)*d ≤ K*d*n+K^2*L*d := by nlinarith only [c]
      apply h.trans (norm.trans _)
      rw [Leq]; dsimp only [J,Q]
      have h₁ : K ≤ K^6 := by simpa using Nat.pow_le_pow_right kp (show 1 ≤ 6 by decide)
      have h₂ : K^2 ≤ K^6 := Nat.pow_le_pow_right kp (by decide)
      have a₁ := Nat.mul_le_mul_right (d*n) h₁
      have a₂ := Nat.mul_le_mul_right (d*n) h₂
      nlinarith only [a₁,a₂,Nat.zero_le (K^6*d*n)]
    have dist := Int.natAbs_sub_le (z i) (z j)
    exact (dist.trans (Nat.add_le_add (limit i) (limit j))).trans_lt (by
      change 4*Q^2*d*n < 3^(200*r) at wide
      convert wide using 1; ring)

#print axioms finite_ternary_rational_rigidity
end Collatz.Itinerary.HourEscape
