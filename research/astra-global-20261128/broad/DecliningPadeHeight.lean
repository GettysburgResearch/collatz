import DecliningPadeValuations
import PadeHeight

/-! Integer-only comparison between finite decreasing-clock divisibility and archimedean height. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.DecliningPadeHeight
open Collatz.PadeArithmetic Collatz.FinitePade Collatz.PadeValuations Collatz.PadeHeight
open Collatz.DecliningPadeIntegral Collatz.DecliningPadeCoefficients Collatz.DecliningPadeValuations
open Collatz.PadeIntegral (zBase heightFactor)
open scoped BigOperators

private theorem curvature_budget (n m k l : ℕ) (hk : k≤n) (hl : l≤m+k) :
    twoCurvature m k l+((n-k)*(n+m)+tri l)+k*(n-k)=tri m+n*(n+m) := by
  have hi := tri_mono hl
  have ha := tri_add m k
  have ht := twice_tri k
  have hc : tri l≤tri m+k*(k+m) := by nlinarith
  have he := Nat.sub_add_cancel hc
  have hs := Nat.sub_add_cancel hk
  have hx := congrArg (fun u : ℕ => u*(n+m)) hs
  have hy := congrArg (fun u : ℕ => k*u) hs
  unfold twoCurvature
  nlinarith only [he,hx,hy]

theorem int_term_height (h b n m k l : ℕ) (hk : k≤n) (hl : l≤m+k) :
    |intTerm h b n m k l|≤(n.choose k:ℤ)*heightFactor h b n m := by
  let zl := n-k+l
  let zr := m+k-l
  let ql := twoCurvature m k l
  let qr := (n-k)*(n+m)+tri l
  let qc := k*(n-k)
  have hz : zl+zr=n+m := by dsimp [zl,zr]; omega
  have hq : ql+qr+qc=tri m+n*(n+m) := curvature_budget n m k l hk hl
  have hz1 : (2:ℤ)^(b+1)≤2*3^b := by
    rw [pow_succ']
    exact mul_le_mul_of_nonneg_left (pow_le_pow_left₀ (by decide) (by decide) b) (by decide)
  have hz2 : (3:ℤ)^b≤2*3^b := by
    have hp : 0≤(3:ℤ)^b := by positivity
    linarith
  have hqb : (2:ℤ)^h≤3^h := pow_le_pow_left₀ (by decide) (by decide) h
  have wz := mul_le_mul (pow_le_pow_left₀ (by positivity) hz1 zl)
      (pow_le_pow_left₀ (by positivity) hz2 zr) (by positivity) (by positivity)
  rw [←pow_add,hz] at wz
  have wq : ((2:ℤ)^h)^ql*(3^h)^qr*(3^h)^qc≤3^(h*(tri m+n*(n+m))) := by
    calc
      _ ≤ ((3:ℤ)^h)^ql*(3^h)^qr*(3^h)^qc := by
        exact mul_le_mul_of_nonneg_right
          (mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (by positivity) hqb ql) (by positivity)) (by positivity)
      _ = _ := by rw [←pow_add,←pow_add,hq,←pow_mul]
  have hpos : 0≤(2:ℤ)^(twoIndex h b n m k l)*3^(threeIndex h b n m k l) := by positivity
  have hb := mul_le_mul_of_nonneg_right (normalized_height h n k) hpos
  calc
    |intTerm h b n m k l| = |normalized h n k| *((2:ℤ)^((b+1)*zl+h*ql)*3^(b*zr+h*qr)) := by
      simp only [intTerm,abs_mul,abs_pow,abs_of_nonneg (by decide : (0:ℤ)≤2),
        abs_of_nonneg (by decide : (0:ℤ)≤3),mul_assoc]
      rfl
    _ ≤ ((n.choose k:ℤ)*3^(h*qc))*(2^((b+1)*zl+h*ql)*3^(b*zr+h*qr)) := hb
    _ = (n.choose k:ℤ)*((((2:ℤ)^(b+1))^zl*(3^b)^zr)*(((2^h)^ql*(3^h)^qr)*(3^h)^qc)) := by
      simp only [pow_add,pow_mul]
      ring
    _ ≤ _ := mul_le_mul_of_nonneg_left (mul_le_mul wz wq (by positivity) (by positivity)) (by positivity)

private theorem scaled_abs_sum (D : ℤ) (hD : 0≤D) (n : ℕ) (f : ℕ→ℤ) :
    D * |∑ k ∈ Finset.range n,f k| ≤ ∑ k ∈ Finset.range n,D*|f k| := by
  rw [←Finset.mul_sum]
  exact mul_le_mul_of_nonneg_left (Finset.abs_sum_le_sum_abs _ _) hD

private theorem binomial_sum (n : ℕ) (u : ℤ) :
    (∑ k ∈ Finset.range (n+1),(n.choose k:ℤ)*u)=(2:ℤ)^n*u := by
  rw [←Finset.sum_mul]
  congr 1
  exact_mod_cast Nat.sum_range_choose n

theorem reduced_term_height (h b n m k l : ℕ) (hk : k≤n) (hl : l≤m+k) (hb : h*(2*n+m)≤b+1) :
    (2:ℤ)^(commonExponent h n m)*|reducedTerm h b n m k l|≤(n.choose k:ℤ)*heightFactor h b n m := by
  have hi := int_term_height h b n m k l hk hl
  rwa [common_factor h b n m k l hk hl hb,abs_mul,abs_of_nonneg (by positivity : 0≤(2:ℤ)^commonExponent h n m)] at hi

theorem down_head_height (h b n m : ℕ) (hb : h*(2*n+m)≤b+1) :
    (2:ℤ)^(commonExponent h n m)*|reducedHead h b n m|≤2^n*heightFactor h b n m := by
  let D := (2:ℤ)^(commonExponent h n m)
  calc
    _ ≤ ∑ k ∈ Finset.range (n+1),D*|reducedTerm h b n m k 0| := scaled_abs_sum D (by positivity) _ _
    _ ≤ ∑ k ∈ Finset.range (n+1),(n.choose k:ℤ)*heightFactor h b n m := by
      apply Finset.sum_le_sum
      intro k hk
      exact reduced_term_height h b n m k 0 (by have := Finset.mem_range.mp hk; omega) (by omega) hb
    _ = _ := binomial_sum n _

theorem down_constant_height (h b n m : ℕ) (hb : h*(2*n+m)≤b+1) :
    (2:ℤ)^(commonExponent h n m)*|reducedConstant h b n m|≤totalHeight h b n m := by
  let D := (2:ℤ)^(commonExponent h n m)
  let H := heightFactor h b n m
  have hH : 0≤H := by dsimp [H,heightFactor]; positivity
  let f (k : ℕ) := ∑ l ∈ Finset.range (m+k+1),reducedTerm h b n m k l
  have hrow (k : ℕ) (hk : k≤n) : D*|f k|≤(n.choose k:ℤ)*(((n+m+1:ℕ):ℤ)*H) := by
    calc
      _ ≤ ∑ l ∈ Finset.range (m+k+1),D*|reducedTerm h b n m k l| := scaled_abs_sum D (by positivity) _ _
      _ ≤ ∑ _l ∈ Finset.range (m+k+1),(n.choose k:ℤ)*H := by
        apply Finset.sum_le_sum
        intro l hl
        exact reduced_term_height h b n m k l hk (by have := Finset.mem_range.mp hl; omega) hb
      _ = ((m+k+1:ℕ):ℤ)*((n.choose k:ℤ)*H) := by simp
      _ ≤ ((n+m+1:ℕ):ℤ)*((n.choose k:ℤ)*H) :=
        mul_le_mul_of_nonneg_right (by exact_mod_cast (show m+k+1≤n+m+1 by omega)) (by positivity)
      _ = _ := by ring
  calc
    _ ≤ ∑ k ∈ Finset.range (n+1),D*|f k| := scaled_abs_sum D (by positivity) _ _
    _ ≤ ∑ k ∈ Finset.range (n+1),(n.choose k:ℤ)*(((n+m+1:ℕ):ℤ)*H) := by
      apply Finset.sum_le_sum
      intro k hk
      exact hrow k (by have := Finset.mem_range.mp hk; omega)
    _ = _ := by rw [binomial_sum]; change _=_*_*H; ring

theorem down_form_upper (h b n m : ℕ) (hb : h*(2*n+m)≤b+1) (y : ℤ) :
    (2:ℤ)^(commonExponent h n m)*|reducedHead h b n m*y-reducedConstant h b n m|≤
      (|y|+1)*totalHeight h b n m := by
  let D := (2:ℤ)^(commonExponent h n m)
  let Y := |y|
  have hh := down_head_height h b n m hb
  have ha := down_constant_height h b n m hb
  have hH : 0≤heightFactor h b n m := by unfold heightFactor; positivity
  have hbig : D*|reducedHead h b n m|≤totalHeight h b n m := by
    calc
      _ ≤ _ := hh
      _ = 1*((2:ℤ)^n*heightFactor h b n m) := by rw [one_mul]
      _ ≤ ((n+m+1:ℕ):ℤ)*((2:ℤ)^n*heightFactor h b n m) := by
        exact mul_le_mul_of_nonneg_right (by exact_mod_cast (show 1≤n+m+1 by omega)) (by positivity)
      _ = _ := by unfold totalHeight; ring
  calc
    _ ≤ D*(|reducedHead h b n m*y|+|reducedConstant h b n m|) :=
      mul_le_mul_of_nonneg_left (abs_sub _ _) (by positivity)
    _ = (D*|reducedHead h b n m|)*Y+D*|reducedConstant h b n m| := by rw [abs_mul]; dsimp [Y]; ring
    _ ≤ totalHeight h b n m*Y+totalHeight h b n m :=
      add_le_add (mul_le_mul_of_nonneg_right hbig (abs_nonneg y)) ha
    _ = _ := by dsimp [Y]; ring

theorem native_spacing (h b s : ℕ) (hs : 0<s) (hb : 200*h*s≤b) :
    h*(2*(2*s)+s+1)<b+1 := by
  have h0 : 2*(2*s)+s+1≤200*s := by omega
  have h1 := Nat.mul_le_mul_left h h0
  nlinarith only [h1,hb]

theorem down_exponent_margin (h b s : ℕ) (hh : 0<h) (hs : 0<s) (hb : 200*h*s≤b) :
    17*(b*s)+8*(17*(7*s)+27*threeBudget h b s)≤136*rawNat h b (2*s) s := by
  have hr := rawNat_cast h b (2*s) s (native_spacing h b s hs hb)
  have ht := congrArg (fun j : ℤ => (h:ℤ)*j)
    (show 2*(tri s:ℤ)+s=(s:ℤ)*s by exact_mod_cast twice_tri s)
  have hbs : (200:ℤ)*h*s*s≤(b:ℤ)*s := by exact_mod_cast Nat.mul_le_mul_right s hb
  have hb' : (200:ℤ)*h*s≤b := by exact_mod_cast hb
  have hhs : (s:ℤ)≤(h:ℤ)*s := by
    exact_mod_cast (show s≤h*s by simpa only [one_mul] using Nat.mul_le_mul_right s (show 1≤h by omega))
  zify
  unfold threeBudget rawExponent at *
  push_cast at hr ⊢
  nlinarith only [hr,ht,hbs,hb',hhs,show 0≤(h:ℤ)*s*s by positivity,show (0:ℤ)≤s by positivity]

/-- The reduced finite form gives a uniform power margin with constants independent of the slope. -/
theorem down_finite_height (h b s : ℕ) (hh : 0<h) (hs : 0<s) (hb : 200*h*s≤b) (y : ℤ)
    (ht : ∀ k≤2*s,AtLeast (downClock h b (2*s+s+k+2))
       ((y:ℚ)-partialSum (qDown h) (zBase b) (2*s+s+k+2))) :
    (2:ℤ)^(b*s)≤(|y|+1)^8 := by
  let E := threeBudget h b s
  let W := rawNat h b (2*s) s
  let T := 8*(17*(7*s)+27*E)
  let Y := |y|+1
  have hy : 0≤Y := by dsimp [Y]; positivity
  have hsp := native_spacing h b s hs hb
  have hc : h*(2*(2*s)+s)≤b+1 :=
    (Nat.mul_le_mul_left h (show 2*(2*s)+s≤2*(2*s)+s+1 by omega)).trans hsp.le
  have hl := down_integer_lower h b (2*s) s hh hsp y ht
  have hu : (2:ℤ)^W≤Y*(2^(7*s)*3^E) := (hl.trans (down_form_upper h b (2*s) s hc y)).trans
    (mul_le_mul_of_nonneg_left (total_height_special h b s) hy)
  have he : (b*s)*17+T≤W*136 := by
    have := down_exponent_margin h b s hh hs hb
    dsimp only [T,E,W]
    omega
  have h3 : (3:ℤ)^17≤2^27 := by decide
  have h3E : ((3:ℤ)^E)^136≤2^(8*(27*E)) := by
    calc
      _ = (((3:ℤ)^17)^E)^8 := by rw [←pow_mul,←pow_mul,←pow_mul]; congr 1; ring
      _ ≤ (((2:ℤ)^27)^E)^8 :=
        pow_le_pow_left₀ (by positivity) (pow_le_pow_left₀ (by positivity) h3 E) 8
      _ = _ := by rw [←pow_mul,←pow_mul]; congr 1; ring
  have hx : ((2:ℤ)^(b*s))^17*2^T≤(Y^8)^17*2^T := by
    calc
      _ = (2:ℤ)^((b*s)*17+T) := by rw [←pow_mul,←pow_add]
      _ ≤ (2:ℤ)^(W*136) := pow_le_pow_right₀ (by decide) he
      _ = ((2:ℤ)^W)^136 := pow_mul _ _ _
      _ ≤ (Y*(2^(7*s)*3^E))^136 := pow_le_pow_left₀ (by positivity) hu _
      _ = (Y^8)^17*(2^((7*s)*136)*((3:ℤ)^E)^136) := by
        rw [mul_pow,mul_pow,←pow_mul,←pow_mul Y]
      _ ≤ (Y^8)^17*(2^((7*s)*136)*2^(8*(27*E))) := by
        exact mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_left h3E (by positivity)) (by positivity)
      _ = _ := by rw [←pow_add]; dsimp only [T]; congr 2; ring
  exact le_of_pow_le_pow_left₀ (by decide : (17:ℕ)≠0) (by positivity)
    (le_of_mul_le_mul_right hx (by positivity))

end Collatz.DecliningPadeHeight
