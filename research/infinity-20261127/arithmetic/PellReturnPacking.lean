import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

set_option autoImplicit false
set_option warningAsError true
set_option maxHeartbeats 1200000

namespace Collatz.PellReturnPacking

/-- The return norm for two integer Pell solutions is an odd integer whenever
the forward homogeneous numerator is odd and its denominator is even. -/
theorem returnNormOdd (D X Y V W a b : ℤ)
    (hx : X^2-D*V^2=1) (hy : Y^2-D*W^2=1) :
    Odd (((2*b)*Y-(2*a+1)*X)^2-D*((2*b)*W-(2*a+1)*V)^2) := by
  use 2*a^2+2*a+2*b^2-2*b*(2*a+1)*(X*Y-D*V*W)
  linear_combination (2*a+1)^2*hx + (2*b)^2*hy

/-- The physical odd-source and affine arc substitutions in the return norm. -/
theorem returnCarry (A B C x y : ℤ) (h : B*y=A*x+C) :
    B*(6*y+1)-A*(6*x+1)=6*C+B-A := by
  linear_combination 6*h

/-- The Pell equation obtained from the squarefree part of the neighboring
integers 3x and 3x+1. -/
theorem pellOfKernel (D x v : ℤ) (h : 3*x*(3*x+1)=D*v^2) :
    (6*x+1)^2-D*(2*v)^2=1 := by
  linear_combination 4*h

section OrderedField

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- If a conjugate pair has norm of absolute value at least one, its smaller
specified factor cannot approach zero faster than the reciprocal trace. -/
theorem conjugateGap {e K : F} (hn : 1 ≤ |e*(2*K-e)|) :
    1 ≤ |e| *(2*|K|+1) := by
  by_cases h : |e| ≤ 1
  · have hc : |2*K-e| ≤ 2*|K|+1 := by
      calc
        |2*K-e| ≤ |2*K|+|e| := abs_sub _ _
        _ ≤ 2*|K|+1 := by simpa [abs_mul] using add_le_add_left h (2*|K|)
    rw [abs_mul] at hn
    exact hn.trans (mul_le_mul_of_nonneg_left hc (abs_nonneg _))
  · have h1 : 1 < |e| := lt_of_not_ge h
    have hk : 1 ≤ 2*|K|+1 := by linarith [abs_nonneg K]
    exact h1.le.trans (by simpa using mul_le_mul_of_nonneg_left hk (abs_nonneg e))

/-- Exact physical return bound in any ordered coefficient field containing
the positive square root. The final displayed hypothesis is supplied by
the nonzero integer norm, for example by returnNormOdd. -/
theorem returnHeight {x y A B C D V W d : F}
    (hx : 0<x) (ha : 0<A) (hb : 0<B) (hc : 0<C)
    (hv : 0<V) (hw : 0<W) (hd : 0<d) (hsq : d^2=D)
    (harc : B*y=A*x+C)
    (px : (6*x+1)^2-D*V^2=1) (py : (6*y+1)^2-D*W^2=1)
    (hn : 1 ≤ |(6*C+B-A)^2-D*(B*W-A*V)^2|) :
    6*x < (2*|6*C+B-A|+1)*max A (B^2/A) := by
  let X := 6*x+1
  let Y := 6*y+1
  let K := 6*C+B-A
  let e := B/(Y+d*W)-A/(X+d*V)
  have hy : 0<y := by
    have : 0 < B*y := by rw [harc]; positivity
    exact pos_of_mul_pos_right this hb.le
  have hxden : 0<X+d*V := by dsimp [X]; positivity
  have hyden : 0<Y+d*W := by dsimp [Y]; positivity
  have hxinv : 1/(X+d*V) = X-d*V := by
    apply (div_eq_iff hxden.ne').2
    dsimp [X]
    rw [← hsq] at px
    linear_combination -px
  have hyinv : 1/(Y+d*W) = Y-d*W := by
    apply (div_eq_iff hyden.ne').2
    dsimp [Y]
    rw [← hsq] at py
    linear_combination -py
  have he : e = K-d*(B*W-A*V) := by
    dsimp [e]
    calc
      _ = B*(1/(Y+d*W))-A*(1/(X+d*V)) := by ring
      _ = _ := by
        rw [hyinv, hxinv]
        dsimp [X,Y,K]
        linear_combination 6*harc
  have hprod : e*(2*K-e)=K^2-D*(B*W-A*V)^2 := by
    rw [he, ← hsq]
    ring
  have hgap := conjugateGap (show 1 ≤ |e*(2*K-e)| from by rw [hprod]; exact hn)
  have boundA : 6*x*(A/(X+d*V)) < A := by
    rw [mul_div_assoc', div_lt_iff₀ hxden]
    dsimp [X]
    have : 0 < A*(d*V) := mul_pos ha (mul_pos hd hv)
    linarith only [this, ha]
  have boundB : 6*x*(B/(Y+d*W)) < B^2/A := by
    rw [mul_div_assoc', div_lt_div_iff₀ hyden ha]
    have diff : B^2*(Y+d*W)-(6*x*B)*A = B^2*(1+d*W)+6*B*C := by
      dsimp [Y]
      linear_combination 6*B*harc
    have hpos : 0 < B^2*(1+d*W)+6*B*C := by positivity
    linarith only [diff, hpos]
  have ax : 0 < A/(X+d*V) := div_pos ha hxden
  have by' : 0 < B/(Y+d*W) := div_pos hb hyden
  have hscaled : 6*x*|e| < max A (B^2/A) := by
    by_cases ep : 0 ≤ e
    · rw [abs_of_nonneg ep]
      apply lt_of_lt_of_le _ (le_max_right _ _)
      have hle : e ≤ B/(Y+d*W) := sub_le_self _ ax.le
      exact (mul_le_mul_of_nonneg_left hle (show 0 ≤ 6*x by positivity)).trans_lt boundB
    · rw [abs_of_neg (lt_of_not_ge ep)]
      apply lt_of_lt_of_le _ (le_max_left _ _)
      have hle : -e ≤ A/(X+d*V) := by dsimp [e]; linarith only [by']
      exact (mul_le_mul_of_nonneg_left hle (show 0 ≤ 6*x by positivity)).trans_lt boundA
  have hfac : 0 < 2*|K|+1 := by linarith [abs_nonneg K]
  calc
    6*x ≤ (6*x)*(|e| *(2*|K|+1)) := by
      simpa using mul_le_mul_of_nonneg_left hgap (show 0 ≤ 6*x by positivity)
    _ = (2*|K|+1)*(6*x*|e|) := by ring
    _ < _ := mul_lt_mul_of_pos_left hscaled hfac

end OrderedField

#print axioms returnNormOdd
#print axioms returnCarry
#print axioms pellOfKernel
#print axioms conjugateGap
#print axioms returnHeight

end Collatz.PellReturnPacking
