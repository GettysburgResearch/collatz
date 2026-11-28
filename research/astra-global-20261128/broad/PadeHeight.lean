import PadeValuations

/-! The positive quadratic-clock height margin using integer powers only. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.PadeHeight
open Collatz.PadeArithmetic Collatz.PadeIntegral Collatz.PadeValuations Collatz.FinitePade

def totalHeight (h b n m : ℕ) : ℤ := ((n+m+1:ℕ):ℤ)*2^n*heightFactor h b n m

def threeBudget (h b s : ℕ) : ℕ := 3*b*s+h*(tri s+(2*s)*(2*s+s))

def excess (h b s : ℕ) : ℕ := 3*h*s*s+4*b*s

theorem form_upper (h b n m : ℕ) (y : ℤ) :
    |integralHead h b n m*y-integralConstant h b n m| ≤ (|y|+1)*totalHeight h b n m := by
  have hu := integralConstant_height h b n m
  have hh := integralHead_height h b n m
  have hF : 0≤heightFactor h b n m := by unfold heightFactor; positivity
  have hc : (1:ℤ)≤((n+m+1:ℕ):ℤ) := by exact_mod_cast (show 1≤n+m+1 by omega)
  have hh' : |integralHead h b n m|≤totalHeight h b n m := by
    calc
      _ ≤ _ := hh
      _ = 1*((2:ℤ)^n*heightFactor h b n m) := by rw [one_mul]
      _ ≤ ((n+m+1:ℕ):ℤ)*((2:ℤ)^n*heightFactor h b n m) :=
        mul_le_mul_of_nonneg_right hc (by positivity)
      _ = _ := by unfold totalHeight; ring
  calc
    _ ≤ |integralHead h b n m*y|+|integralConstant h b n m| := abs_sub _ _
    _ ≤ totalHeight h b n m*|y|+totalHeight h b n m := by
      rw [abs_mul]
      exact add_le_add (mul_le_mul_of_nonneg_right hh' (abs_nonneg y)) hu
    _ = _ := by ring

private theorem row_count (s : ℕ) : 3*s+1≤2^(2*s) := by
  induction s with
  | zero => decide
  | succ s ih =>
    have hs : 2*(s+1)=2*s+2 := by ring
    rw [hs,pow_add]
    norm_num
    omega

theorem total_height_special (h b s : ℕ) :
    totalHeight h b (2*s) s ≤ (2:ℤ)^(7*s)*3^(threeBudget h b s) := by
  have hc : ((2*s+s+1:ℕ):ℤ)≤(2:ℤ)^(2*s) := by
    exact_mod_cast (show 2*s+s+1≤2^(2*s) by simpa only [show 2*s+s=3*s by ring] using row_count s)
  unfold totalHeight heightFactor
  calc
    _ ≤ 2^(2*s)*2^(2*s)*((2*(3:ℤ)^b)^(2*s+s)*3^(h*(tri s+2*s*(2*s+s)))) := by
      exact mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_right hc (by positivity)) (by positivity)
    _ = _ := by
      rw [mul_pow,←pow_mul]
      unfold threeBudget
      rw [show 3*b*s=b*(2*s+s) by ring,pow_add,show 7*s=2*s+2*s+(2*s+s) by ring,pow_add,pow_add]
      ring

/-- The positive margin retains the linear first-spacing and quadratic curvature terms. -/
theorem exponent_margin (h b s : ℕ) (hh : 0<h) :
    excess h b s+17*(7*s)+27*threeBudget h b s≤17*formExponent h b (2*s) s := by
  unfold excess threeBudget formExponent
  have hsmall := twice_tri s
  have hbig := twice_tri (2*s+s+1)
  have ht0 := congrArg (fun t : ℕ => h*t) hsmall
  have ht1 := congrArg (fun t : ℕ => h*t) hbig
  have hs : s≤h*s := by simpa only [one_mul] using Nat.mul_le_mul_right s (show 1≤h by omega)
  nlinarith only [ht0,ht1,hs,Nat.zero_le b,Nat.zero_le s]

/-- Integer comparison and cancellation of the common archimedean factor. -/
theorem power_margin (h b s : ℕ) (hh : 0<h) (y : ℤ)
    (lower : (2:ℤ)^(formExponent h b (2*s) s) ≤
      |integralHead h b (2*s) s*y-integralConstant h b (2*s) s|) :
    (2:ℤ)^(excess h b s) ≤ (|y|+1)^17 := by
  let E := threeBudget h b s
  let W := formExponent h b (2*s) s
  let D := excess h b s
  let Y := |y|+1
  have hY : 0≤Y := by dsimp [Y]; positivity
  have hu : (2:ℤ)^W≤Y*(2^(7*s)*3^E) := (lower.trans (form_upper h b (2*s) s y)).trans
    (mul_le_mul_of_nonneg_left (total_height_special h b s) hY)
  have he : D+(17*(7*s)+27*E)≤W*17 := by
    have := exponent_margin h b s hh
    dsimp only [D,E,W]
    omega
  have h3 : (3:ℤ)^17≤2^27 := by decide
  have h3E : ((3:ℤ)^E)^17≤2^(27*E) := by
    rw [←pow_mul,mul_comm, pow_mul, pow_mul]
    exact pow_le_pow_left₀ (by positivity) h3 E
  have hc : (2:ℤ)^D*2^(17*(7*s)+27*E) ≤ Y^17*2^(17*(7*s)+27*E) := by
    calc
      _ = (2:ℤ)^(D+(17*(7*s)+27*E)) := (pow_add _ _ _).symm
      _ ≤ (2:ℤ)^(W*17) := pow_le_pow_right₀ (by decide) he
      _ = ((2:ℤ)^W)^17 := pow_mul _ _ _
      _ ≤ (Y*(2^(7*s)*3^E))^17 := pow_le_pow_left₀ (by positivity) hu _
      _ = Y^17*(2^(17*(7*s))*((3:ℤ)^E)^17) := by
        rw [mul_pow,mul_pow,←pow_mul,Nat.mul_comm (7*s) 17]
      _ ≤ Y^17*(2^(17*(7*s))*2^(27*E)) := by
        exact mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_left h3E (by positivity)) (by positivity)
      _ = _ := by rw [pow_add]
  exact le_of_mul_le_mul_right hc (by positivity)

/-- A single connected theorem from physical finite tail evidence to the height barrier. -/
theorem finite_height_barrier (h b s : ℕ) (hh : 0<h) (y : ℤ)
    (ht : ∀ k≤2*s,AtLeast (clockExponent h b (2*s+s+k+2))
      ((y:ℚ)-partialSum (qBase h) (zBase b) (2*s+s+k+2))) :
    (2:ℤ)^(3*h*s*s+4*b*s) ≤ (|y|+1)^17 :=
  power_margin h b s hh y (integer_form_lower h b (2*s) s hh y ht)

end Collatz.PadeHeight
