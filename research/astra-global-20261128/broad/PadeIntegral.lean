import PadeCoefficients
import FinitePade
import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-! Every scaled coefficient and finite partial-sum term is an explicit integer.
The uniform bounds retain the separate costs of the first spacing and curvature. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.PadeIntegral
open Collatz.PadeArithmetic Collatz.PadeCoefficients Collatz.FinitePade
open scoped BigOperators

def qBase (h : ℕ) : ℚ := (3/2:ℚ)^h
def zBase (b : ℕ) : ℚ := 2^(b+1)/(3:ℚ)^b

/-- The integer clearing factor shared by the two forms. -/
def scale (h b n m : ℕ) : ℤ :=
  2^(n*(b+1)+h*(n*(n+m)))*3^(b*m+h*tri m)

def twoExponent (h b n m k l : ℕ) : ℕ :=
  (b+1)*(n-k+l)+h*((n-k)*(n+m)+tri l)

def threeExponent (h b m k l : ℕ) : ℕ :=
  b*(m+k-l)+h*(tri (m+k)-tri l)

def integralTerm (h b n m k l : ℕ) : ℤ :=
  coeffInt h n k*2^(twoExponent h b n m k l)*3^(threeExponent h b m k l)

def integralHead (h b n m : ℕ) : ℤ :=
  ∑ k ∈ Finset.range (n+1), integralTerm h b n m k 0

def integralConstant (h b n m : ℕ) : ℤ :=
  ∑ k ∈ Finset.range (n+1), ∑ l ∈ Finset.range (k+m+1), integralTerm h b n m k l

def heightFactor (h b n m : ℕ) : ℤ :=
  (2*(3:ℤ)^b)^(n+m)*3^(h*(tri m+n*(n+m)))

private theorem two_balance (h b n m k l : ℕ) (hk : k≤n) :
    twoExponent h b n m k l+(h*degreeIndex n k+h*(tri k+k*m)+(b+1)*k) =
      n*(b+1)+h*(n*(n+m))+(b+1)*l+h*tri l := by
  have hnk := Nat.sub_add_cancel hk
  have hd := degreeIndex_plus_exponent n m k (by omega)
  unfold twoExponent
  calc
    _ = (b+1)*(n-k+l+k)+h*((n-k)*(n+m)+tri l+(degreeIndex n k+(tri k+k*m))) := by ring
    _ = _ := by
      rw [hd,show n-k+l+k=n+l by omega]
      have he : (n-k)*(n+m)+tri l+k*(n+m)=n*(n+m)+tri l := by
        calc
          _ = (n-k+k)*(n+m)+tri l := by ring
          _ = _ := by rw [hnk]
      rw [he]
      ring

private theorem three_balance (h b m k l : ℕ) (hl : l≤m+k) :
    threeExponent h b m k l+(b*l+h*tri l) =
      b*m+h*tri m+h*(tri k+k*m)+b*k := by
  have hz := Nat.sub_add_cancel hl
  have hq := Nat.sub_add_cancel (tri_mono hl)
  unfold threeExponent
  calc
    _ = b*((m+k-l)+l)+h*((tri (m+k)-tri l)+tri l) := by ring
    _ = _ := by rw [hz,hq,tri_add]; ring

private theorem q_pow (h j : ℕ) :
    (qBase h)^j=(3:ℚ)^(h*j)/2^(h*j) := by
  rw [qBase,←pow_mul,div_pow]

private theorem z_pow (b j : ℕ) :
    (zBase b)^j=(2:ℚ)^((b+1)*j)/3^(b*j) := by
  rw [zBase,div_pow,←pow_mul,←pow_mul]

/-- A coefficient times a Taylor monomial after the single common scaling. -/
theorem scale_raw_term (h b n m k l : ℕ) (hk : k≤n) (hl : l≤m+k) :
    (scale h b n m:ℚ)*rawCoeff n m (qBase h) (zBase b) k*
        term (qBase h) (zBase b) l = (integralTerm h b n m k l:ℚ) := by
  have h2 := two_balance h b n m k l hk
  have h3 := three_balance h b m k l hl
  have hc : (padePoly n (qBase h)).coeff k =
      (coeffInt h n k:ℚ)/2^(h*degreeIndex n k) := poly_coeff_eq h n k
  calc
    _ = (coeffInt h n k:ℚ) *
        (2^(n*(b+1)+h*(n*(n+m))+(b+1)*l+h*tri l)*
         3^(b*m+h*tri m+h*(tri k+k*m)+b*k)) /
        (2^(h*degreeIndex n k+h*(tri k+k*m)+(b+1)*k)*3^(b*l+h*tri l)) := by
          simp only [scale,Int.cast_mul,Int.cast_pow,Int.cast_ofNat,rawCoeff,term,hc,q_pow,z_pow,pow_add]
          field_simp
          ring
    _ = _ := by
      rw [←h2,←h3,pow_add,pow_add]
      simp only [integralTerm,Int.cast_mul,Int.cast_pow,Int.cast_ofNat]
      field_simp
      ring

theorem scale_raw (h b n m k : ℕ) (hk : k≤n) :
    (scale h b n m:ℚ)*rawCoeff n m (qBase h) (zBase b) k =
      (integralTerm h b n m k 0:ℚ) := by
  simpa only [term,pow_zero,tri_zero,div_one,mul_one] using scale_raw_term h b n m k 0 hk (by omega)

theorem scale_head (h b n m : ℕ) :
    (scale h b n m:ℚ)*headCoeff n m (qBase h) (zBase b)=(integralHead h b n m:ℚ) := by
  simp only [headCoeff,integralHead,Int.cast_sum,Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro k hk
  exact scale_raw h b n m k (by have := Finset.mem_range.mp hk; omega)

theorem scale_constant (h b n m : ℕ) :
    (scale h b n m:ℚ)*constantCoeff n m (qBase h) (zBase b)=(integralConstant h b n m:ℚ) := by
  simp only [constantCoeff,integralConstant,Int.cast_sum,Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro k hk
  apply Finset.sum_congr rfl
  intro l hl
  rw [←mul_assoc]
  exact scale_raw_term h b n m k l (by have := Finset.mem_range.mp hk; omega)
    (by have := Finset.mem_range.mp hl; omega)

/-- Its displayed odd factor permits exact binary valuation without any infinite series. -/
theorem weight_factor (h b n m k : ℕ) :
    integralTerm h b n m k 0 =
      2^((n-k)*(b+1+h*(n+m)))*
      (coeffInt h n k*3^(b*(m+k)+h*tri (m+k))) := by
  simp only [integralTerm,twoExponent,threeExponent,add_zero,tri_zero,Nat.sub_zero]
  rw [show (b+1)*(n-k)+h*((n-k)*(n+m))=(n-k)*(b+1+h*(n+m)) by ring]
  ring

theorem weight_odd_factor (h b n m k : ℕ) (hh : 0<h) (hk : k≤n) :
    Odd (coeffInt h n k*3^(b*(m+k)+h*tri (m+k))) := by
  have ho : Odd (3:ℤ) := ⟨1,by decide⟩
  exact (coeffInt_odd h n k hh hk).mul ho.pow

private theorem budget_split (n m k l : ℕ) (hk : k≤n) (hl : l≤m+k) :
    ((n-k+l)+(m+k-l)=n+m) ∧
    (((n-k)*(n+m)+tri l)+(tri (m+k)-tri l)+degreeIndex n k=tri m+n*(n+m)) := by
  have hs := Nat.sub_add_cancel hk
  have hu := Nat.sub_add_cancel hl
  have hv := Nat.sub_add_cancel (tri_mono hl)
  have hd := degreeIndex_plus_exponent n m k (by omega)
  have ht := tri_add m k
  constructor
  · omega
  · nlinarith [congrArg (fun j : ℕ => j*(n+m)) hs]

/-- Every finite Taylor term spends the same total exponent budgets. -/
theorem term_height (h b n m k l : ℕ) (hk : k≤n) (hl : l≤m+k) :
    |integralTerm h b n m k l|≤(n.choose k:ℤ)*heightFactor h b n m := by
  obtain ⟨hz,hq⟩ := budget_split n m k l hk hl
  let zl := n-k+l
  let zr := m+k-l
  let ql := (n-k)*(n+m)+tri l
  let qr := tri (m+k)-tri l
  have hz' : zl+zr=n+m := hz
  have hq' : ql+qr+degreeIndex n k=tri m+n*(n+m) := hq
  have two_base : (2:ℤ)^(b+1) ≤ 2*3^b := by
    rw [pow_succ']
    exact mul_le_mul_of_nonneg_left (pow_le_pow_left₀ (by decide) (by decide) b) (by decide)
  have three_base : (3:ℤ)^b ≤ 2*3^b := by
    have hp : 0≤(3:ℤ)^b := by positivity
    linarith
  have q_base : (2:ℤ)^h ≤ 3^h := pow_le_pow_left₀ (by decide) (by decide) h
  have wz := mul_le_mul (pow_le_pow_left₀ (by positivity) two_base zl)
      (pow_le_pow_left₀ (by positivity) three_base zr) (by positivity) (by positivity)
  rw [←pow_add,hz'] at wz
  have wq : ((2:ℤ)^h)^ql*(3^h)^qr*(3^h)^degreeIndex n k ≤
      3^(h*(tri m+n*(n+m))) := by
    calc
      _ ≤ ((3:ℤ)^h)^ql*(3^h)^qr*(3^h)^degreeIndex n k := by
        exact mul_le_mul_of_nonneg_right
          (mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (by positivity) q_base ql) (by positivity)) (by positivity)
      _ = _ := by rw [←pow_add,←pow_add,hq',←pow_mul]
  have hpos : 0≤(2:ℤ)^(twoExponent h b n m k l)*3^(threeExponent h b m k l) := by positivity
  have hb := mul_le_mul_of_nonneg_right (coeffInt_height h n k) hpos
  calc
    |integralTerm h b n m k l| =
      |coeffInt h n k| *((2:ℤ)^((b+1)*zl+h*ql)*3^(b*zr+h*qr)) := by
        simp only [integralTerm,abs_mul,abs_pow,abs_of_nonneg (by decide : (0:ℤ)≤2),
          abs_of_nonneg (by decide : (0:ℤ)≤3),mul_assoc]
        rfl
    _ ≤ ((n.choose k:ℤ)*3^(h*degreeIndex n k))*
        (2^((b+1)*zl+h*ql)*3^(b*zr+h*qr)) := hb
    _ = (n.choose k:ℤ)*((((2:ℤ)^(b+1))^zl*(3^b)^zr)*
        (((2^h)^ql*(3^h)^qr)*(3^h)^degreeIndex n k)) := by simp only [pow_add,pow_mul]; ring
    _ ≤ _ := mul_le_mul_of_nonneg_left (mul_le_mul wz wq (by positivity) (by positivity)) (by positivity)

private theorem sum_choose_factor (n : ℕ) (u : ℤ) :
    (∑ k ∈ Finset.range (n+1), (n.choose k:ℤ)*u)=(2:ℤ)^n*u := by
  rw [←Finset.sum_mul]
  congr 1
  exact_mod_cast Nat.sum_range_choose n

/-- The leading coefficient has no partial-sum length cost. -/
theorem integralHead_height (h b n m : ℕ) :
    |integralHead h b n m| ≤ (2:ℤ)^n*heightFactor h b n m := by
  calc
    _ ≤ ∑ k ∈ Finset.range (n+1), |integralTerm h b n m k 0| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ k ∈ Finset.range (n+1), (n.choose k:ℤ)*heightFactor h b n m := by
      apply Finset.sum_le_sum
      intro k hk
      exact term_height h b n m k 0 (by have := Finset.mem_range.mp hk; omega) (by omega)
    _ = _ := sum_choose_factor n _

/-- A common archimedean bound for the finite constant form. -/
theorem integralConstant_height (h b n m : ℕ) :
    |integralConstant h b n m| ≤ ((n+m+1:ℕ):ℤ)*2^n*heightFactor h b n m := by
  let H := heightFactor h b n m
  have hH : 0≤H := by dsimp [H,heightFactor]; positivity
  let f (k : ℕ) := ∑ l ∈ Finset.range (k+m+1), integralTerm h b n m k l
  have hrow (k : ℕ) (hk : k≤n) : |f k| ≤ (n.choose k:ℤ)*(((n+m+1:ℕ):ℤ)*H) := by
    calc
      _ ≤ ∑ l ∈ Finset.range (k+m+1), |integralTerm h b n m k l| :=
        Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ _l ∈ Finset.range (k+m+1), (n.choose k:ℤ)*H := by
        apply Finset.sum_le_sum
        intro l hl
        exact term_height h b n m k l hk (by have := Finset.mem_range.mp hl; omega)
      _ = ((k+m+1:ℕ):ℤ)*((n.choose k:ℤ)*H) := by simp
      _ ≤ ((n+m+1:ℕ):ℤ)*((n.choose k:ℤ)*H) := by
        exact mul_le_mul_of_nonneg_right (by exact_mod_cast (show k+m+1≤n+m+1 by omega)) (by positivity)
      _ = _ := by ring
  calc
    _ ≤ ∑ k ∈ Finset.range (n+1), |f k| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ k ∈ Finset.range (n+1), (n.choose k:ℤ)*(((n+m+1:ℕ):ℤ)*H) := by
      apply Finset.sum_le_sum
      intro k hk
      exact hrow k (by have := Finset.mem_range.mp hk; omega)
    _ = _ := by rw [sum_choose_factor]; change _ = _*_*H; ring

/-- The terminal coefficient is odd, and every earlier coefficient is even. -/
theorem integralHead_odd (h b n m : ℕ) (hh : 0<h) : Odd (integralHead h b n m) := by
  have he (k : ℕ) (hk : k<n) : Even (integralTerm h b n m k 0) := by
    rw [weight_factor]
    have hp : 0<(n-k)*(b+1+h*(n+m)) := Nat.mul_pos (by omega) (by omega)
    exact (Even.pow_of_ne_zero (by decide : Even (2:ℤ)) hp.ne').mul_right _
  have hsum : Even (∑ k ∈ Finset.range n, integralTerm h b n m k 0) := by
    apply Finset.even_sum
    intro k hk
    exact he k (Finset.mem_range.mp hk)
  rw [integralHead,Finset.sum_range_succ,weight_factor,Nat.sub_self,Nat.zero_mul,pow_zero,one_mul]
  exact hsum.add_odd (weight_odd_factor h b n m n hh (by omega))

end Collatz.PadeIntegral
