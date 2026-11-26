import BasinRouting
import Mathlib.RingTheory.Coprime.Lemmas

namespace NativeReset
open BasinRouting BasinCarry

theorem affine {d y z : ℤ} {es : List ℕ} (path : Path d es y z) :
    (2:ℤ)^es.sum*y=3^es.length*z+d*(carry es : ℕ) := by
  induction path with
  | nil => simp [carry]
  | @step e es y v z _ _ _ edge _ ih =>
    simp only [List.sum_cons,List.length_cons,carry,Nat.cast_add,Nat.cast_mul,
      Nat.cast_pow,Nat.cast_ofNat,pow_add,pow_succ]
    linear_combination 2^es.sum*edge + 3*ih

/-- If only the first reversed exponent has changed, the entire ternary
length divides the discrepancy after the incoming power of two. -/
theorem padded_guard {d x y u v : ℤ} {e t : ℕ} {es : List ℕ}
    (native : Path d (e::es) x u) (competitor : Path d ((e+t)::es) y v) :
    (3:ℤ)^(es.length+1) ∣ 2^t*y-x := by
  have a := affine native
  have b := affine competitor
  simp only [List.sum_cons,List.length_cons,carry] at a b
  have cop : IsCoprime (3:ℤ) 2 := ⟨1,-1,by norm_num⟩
  apply ((cop.pow_left (m:=es.length+1)).pow_right (n:=e+es.sum)).dvd_of_dvd_mul_left
  refine ⟨v-u, ?_⟩
  have powId : (2:ℤ)^(e+t+es.sum)=2^(e+es.sum)*2^t := by
    rw [← pow_add]; congr 1; omega
  rw [powId] at b
  linear_combination b-a

/-- Binary-ternary divisibility across an unchanged inverse block. -/
theorem common_block {d x y u v : ℤ} {es : List ℕ}
    (native : Path d es x u) (competitor : Path d es y v) :
    (3:ℤ)^es.length ∣ y-x := by
  have a := affine native
  have b := affine competitor
  have cop : IsCoprime (3:ℤ) 2 := ⟨1,-1,by norm_num⟩
  apply ((cop.pow_left (m:=es.length)).pow_right (n:=es.sum)).dvd_of_dvd_mul_left
  exact ⟨v-u,by linear_combination b-a⟩

/-- Propagate an integer upper ratio backwards over a pair of genuine
inverse edges. The penalty is exactly the deleted binary exponent. -/
theorem ratio_step {a e : ℕ} {x x' y y' C : ℤ}
    (native : 2^a*x=3*x'+1) (competitor : 2^e*y=3*y'+1)
    (Cpos : 1≤C) (xpos : 0≤x) (bound : y'≤C*x') :
    y≤2^(a-e)*C*x := by
  have first : 2^e*y≤C*(2^a*x) := by nlinarith only [native,competitor,Cpos,bound]
  rcases le_total e a with le|le
  · have powId : (2:ℤ)^a=2^e*2^(a-e) := by
      rw [←pow_add]; congr 1; omega
    rw [powId] at first
    have pos : (0:ℤ)<2^e := by positivity
    apply (le_of_mul_le_mul_left _ pos)
    linear_combination first
  · have ep : (2:ℤ)^a≤2^e := by exact_mod_cast Nat.pow_le_pow_right (by decide : 0 < (2:ℕ)) le
    have prod : (2:ℤ)^a*(C*x)≤2^e*(C*x) := mul_le_mul_of_nonneg_right ep (mul_nonneg (by omega) xpos)
    rw [Nat.sub_eq_zero_of_le le,pow_zero,one_mul]
    have pos : (0:ℤ)<2^e := by positivity
    apply (le_of_mul_le_mul_left _ pos)
    nlinarith only [first,prod]

#print axioms affine
#print axioms padded_guard
#print axioms common_block
#print axioms ratio_step
end NativeReset
