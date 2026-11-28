import DecliningPadeCoefficients
import PadeIntegral

/-! Explicit integral forms for a finite decreasing clock and their common binary factor. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.DecliningPadeIntegral
open Collatz.PadeArithmetic Collatz.DecliningPadeCoefficients Collatz.FinitePade
open Collatz.PadeIntegral (zBase heightFactor)
open scoped BigOperators

def qDown (h : ℕ) : ℚ := (2/3:ℚ)^h

def clearing (h b n m : ℕ) : ℤ := 2^(n*(b+1)+h*tri m)*3^(b*m+h*(n*(n+m)))

def commonExponent (h n m : ℕ) : ℕ := h*(tri m+n*(n+m))

def twoCurvature (m k l : ℕ) : ℕ := tri m+k*(k+m)-tri l

def twoIndex (h b n m k l : ℕ) : ℕ :=
  (b+1)*(n-k+l)+h*(twoCurvature m k l)

def threeIndex (h b n m k l : ℕ) : ℕ :=
  b*(m+k-l)+h*((n-k)*(n+m)+tri l)

def intTerm (h b n m k l : ℕ) : ℤ :=
  normalized h n k*2^(twoIndex h b n m k l)*3^(threeIndex h b n m k l)

def reducedTwo (h b n m k l : ℕ) : ℕ :=
  (n-k)*(b+1-h*(n+k+m))+((b+1)*l-h*tri l)

def reducedTerm (h b n m k l : ℕ) : ℤ :=
  normalized h n k*2^(reducedTwo h b n m k l)*3^(threeIndex h b n m k l)

def reducedHead (h b n m : ℕ) : ℤ :=
  ∑ k ∈ Finset.range (n+1), reducedTerm h b n m k 0

def reducedConstant (h b n m : ℕ) : ℤ :=
  ∑ k ∈ Finset.range (n+1), ∑ l ∈ Finset.range (m+k+1), reducedTerm h b n m k l

private theorem curvature_identity (m k : ℕ) :
    k*(k+m)=tri (k+1)+(tri k+k*m) := by
  rw [tri_succ]
  nlinarith [twice_tri k]

private theorem curvature_add (m k l : ℕ) (hl : l≤m+k) :
    twoCurvature m k l+tri l=tri m+k*(k+m) := by
  have hm := tri_mono hl
  have hk := tri_add m k
  have hf := curvature_identity m k
  exact Nat.sub_add_cancel (show tri l≤tri m+k*(k+m) by nlinarith)

private theorem two_balance (h b n m k l : ℕ) (hk : k≤n) (hl : l≤m+k) :
    twoIndex h b n m k l+((b+1)*k+h*tri l)=
      n*(b+1)+h*tri m+h*tri (k+1)+h*(tri k+k*m)+(b+1)*l := by
  unfold twoIndex
  calc
    _ = (b+1)*(n-k+l+k)+h*(twoCurvature m k l+tri l) := by ring
    _ = _ := by rw [show n-k+l+k=n+l by omega,curvature_add m k l hl,curvature_identity]; ring

private theorem three_balance (h b n m k l : ℕ) (hk : k≤n) (hl : l≤m+k) :
    threeIndex h b n m k l+(h*degreeIndex n k+h*(tri k+k*m)+b*l)=
      b*m+h*(n*(n+m))+b*k+h*tri l := by
  have hd := degreeIndex_plus_exponent n m k (by omega)
  unfold threeIndex
  calc
    _ = b*((m+k-l)+l)+h*((n-k)*(n+m)+(degreeIndex n k+(tri k+k*m))+tri l) := by ring
    _ = _ := by rw [Nat.sub_add_cancel hl,hd,←Nat.add_mul,Nat.sub_add_cancel hk]; ring

private theorem q_pow (h j : ℕ) : (qDown h)^j=(2:ℚ)^(h*j)/3^(h*j) := by
  rw [qDown,←pow_mul,div_pow]

private theorem z_pow (b j : ℕ) : (zBase b)^j=(2:ℚ)^((b+1)*j)/3^(b*j) := by
  rw [zBase,div_pow,←pow_mul,←pow_mul]

theorem clearing_term (h b n m k l : ℕ) (hk : k≤n) (hl : l≤m+k) :
    (clearing h b n m:ℚ)*rawCoeff n m (qDown h) (zBase b) k*
      term (qDown h) (zBase b) l=(intTerm h b n m k l:ℚ) := by
  have hc : (padePoly n (qDown h)).coeff k=
      (normalized h n k:ℚ)*2^(h*tri (k+1))/3^(h*degreeIndex n k) := poly_coeff_eq h n k
  have h2 := two_balance h b n m k l hk hl
  have h3 := three_balance h b n m k l hk hl
  calc
    _ = (normalized h n k:ℚ)*
      (2^(n*(b+1)+h*tri m+h*tri (k+1)+h*(tri k+k*m)+(b+1)*l)*
       3^(b*m+h*(n*(n+m))+b*k+h*tri l))/
      (2^((b+1)*k+h*tri l)*3^(h*degreeIndex n k+h*(tri k+k*m)+b*l)) := by
        simp only [clearing,Int.cast_mul,Int.cast_pow,Int.cast_ofNat,rawCoeff,term,hc,q_pow,z_pow,pow_add]
        field_simp
        ring
    _ = _ := by
      rw [←h2,←h3,pow_add,pow_add]
      simp only [intTerm,Int.cast_mul,Int.cast_pow,Int.cast_ofNat]
      field_simp
      ring

private theorem square_difference (n m k : ℕ) (hk : k≤n) :
    (n-k)*(n+k+m)+k*(k+m)=n*(n+m) := by
  have he := congrArg (fun j : ℕ => j*(n+k+m)) (Nat.sub_add_cancel hk)
  nlinarith only [he]

theorem exponent_split (h b n m k l : ℕ) (hk : k≤n) (hl : l≤m+k)
    (hb : h*(2*n+m)≤b+1) :
    commonExponent h n m+reducedTwo h b n m k l=twoIndex h b n m k l := by
  have hki : h*(n+k+m)≤b+1 :=
    le_trans (Nat.mul_le_mul_left h (by omega)) hb
  have hnm : h*(n+m)≤b+1 := le_trans (Nat.mul_le_mul_left h (by omega)) hb
  have hli : h*tri l≤(b+1)*l := by
    calc
      _ ≤ h*(l*(n+m)) := Nat.mul_le_mul_left h (tri_le_mul l (n+m) (by omega))
      _ = (h*(n+m))*l := by ring
      _ ≤ _ := Nat.mul_le_mul_right l hnm
  have hq := square_difference n m k hk
  have hc := curvature_add m k l hl
  have hz := congrArg (fun j : ℕ => (n-k)*j) (Nat.sub_add_cancel hki)
  have hqh := congrArg (fun j : ℕ => h*j) hq
  have hch := congrArg (fun j : ℕ => h*j) hc
  have ht := Nat.sub_add_cancel hli
  unfold commonExponent reducedTwo twoIndex
  nlinarith only [hz,hqh,hch,ht]

/-- The finite denominator reduction never introduces fractional Taylor coefficients. -/
theorem common_factor (h b n m k l : ℕ) (hk : k≤n) (hl : l≤m+k)
    (hb : h*(2*n+m)≤b+1) :
    intTerm h b n m k l=2^(commonExponent h n m)*reducedTerm h b n m k l := by
  rw [intTerm,reducedTerm,←exponent_split h b n m k l hk hl hb,pow_add]
  ring

def reducedScale (h b n m : ℕ) : ℚ := (clearing h b n m:ℚ)/2^(commonExponent h n m)

theorem reduced_scale_term (h b n m k l : ℕ) (hk : k≤n) (hl : l≤m+k)
    (hb : h*(2*n+m)≤b+1) :
    reducedScale h b n m*rawCoeff n m (qDown h) (zBase b) k*
      term (qDown h) (zBase b) l=(reducedTerm h b n m k l:ℚ) := by
  have he := clearing_term h b n m k l hk hl
  rw [common_factor h b n m k l hk hl hb,Int.cast_mul,Int.cast_pow,Int.cast_ofNat] at he
  unfold reducedScale
  field_simp
  exact he

theorem reduced_scale_raw (h b n m k : ℕ) (hk : k≤n) (hb : h*(2*n+m)≤b+1) :
    reducedScale h b n m*rawCoeff n m (qDown h) (zBase b) k=(reducedTerm h b n m k 0:ℚ) := by
  simpa only [term,pow_zero,tri_zero,div_one,mul_one] using reduced_scale_term h b n m k 0 hk (by omega) hb

theorem reduced_scale_head (h b n m : ℕ) (hb : h*(2*n+m)≤b+1) :
    reducedScale h b n m*headCoeff n m (qDown h) (zBase b)=(reducedHead h b n m:ℚ) := by
  simp only [headCoeff,reducedHead,Int.cast_sum,Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro k hk
  exact reduced_scale_raw h b n m k (by have := Finset.mem_range.mp hk; omega) hb

theorem reduced_scale_constant (h b n m : ℕ) (hb : h*(2*n+m)≤b+1) :
    reducedScale h b n m*constantCoeff n m (qDown h) (zBase b)=(reducedConstant h b n m:ℚ) := by
  simp only [constantCoeff,reducedConstant,Int.cast_sum,Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro k hk
  rw [Nat.add_comm k m]
  apply Finset.sum_congr rfl
  intro l hl
  rw [←mul_assoc]
  exact reduced_scale_term h b n m k l (by have := Finset.mem_range.mp hk; omega)
    (by have := Finset.mem_range.mp hl; omega) hb

end Collatz.DecliningPadeIntegral
