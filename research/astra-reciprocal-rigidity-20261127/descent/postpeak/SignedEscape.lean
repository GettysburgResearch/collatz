import PostWords

namespace RampShadow.Postpeak

theorem minus_one_end {h p x z} (W : Walk h p x z) (X : x = -1) : z = -1 := by
  induction W <;> omega

theorem nonneg_end {h p x z} (W : Walk h p x z) (X : 0 ≤ x) : 0 ≤ z := by
  induction W <;> omega

private theorem odd_magnitude {x y : ℤ} (E : 3*x+1=2*y) (neq : x ≠ -1) :
    (4/3:ℚ)*|(x:ℚ)| ≤ |(y:ℚ)| := by
  by_cases X : 0≤x
  · have YY : 0≤y := by omega
    rw [abs_of_nonneg (by exact_mod_cast X : 0≤(x:ℚ)),abs_of_nonneg (by exact_mod_cast YY : 0≤(y:ℚ))]
    have Q : 3*(x:ℚ)+1=2*y := by exact_mod_cast E
    have Q' : 0≤(x:ℚ) := by exact_mod_cast X
    linarith
  · have XX : x≤ -3 := by omega
    have YY : y≤0 := by omega
    rw [abs_of_nonpos (by exact_mod_cast (show x≤0 by omega) : (x:ℚ)≤0),
      abs_of_nonpos (by exact_mod_cast YY : (y:ℚ)≤0)]
    have Q : 3*(x:ℚ)+1=2*y := by exact_mod_cast E
    have Q' : (x:ℚ)≤ -3 := by exact_mod_cast XX
    linarith

/-- Away from the signed fixed point minus one, each odd step multiplies
    absolute magnitude by at least four thirds. -/
theorem signed_growth {h p x z} (W : Walk h p x z) (neq : z ≠ -1) :
    (4/3:ℚ)^p*|(x:ℚ)| ≤ 2^(h-p)*|(z:ℚ)| := by
  induction W with
  | nil => simp
  | @even h p x y W IH =>
    have hp := count_le W
    rw [show h+1-p=(h-p)+1 by omega,pow_succ]
    push_cast
    rw [abs_mul]
    norm_num
    nlinarith only [IH neq]
  | @odd h p x y z edge W IH =>
    have X : x ≠ -1 := by
      intro no
      exact neq (minus_one_end W (by omega))
    have G := mul_le_mul_of_nonneg_left (odd_magnitude edge X)
      (show (0:ℚ)≤(4/3:ℚ)^p by positivity)
    rw [show h+1-(p+1)=h-p by omega,pow_succ]
    nlinarith only [IH neq,G]

/-- In every signed walk odd steps weakly increase its absolute magnitude.
    A path ending at minus one can only have started at magnitude 2^evens
    or less. -/
theorem origin_magnitude {h p x z} (W : Walk h p x z) :
    |x| ≤ 2^(h-p)*|z| := by
  induction W with
  | nil => simp
  | @even h p x y W IH =>
    have hp := count_le W
    rw [show h+1-p=(h-p)+1 by omega,pow_succ,abs_mul]
    norm_num
    nlinarith only [IH]
  | @odd h p x y z edge W IH =>
    rw [show h+1-(p+1)=h-p by omega]
    apply le_trans _ IH
    by_cases X : 0≤x
    · rw [abs_of_nonneg X,abs_of_nonneg (show 0≤y by omega)]
      omega
    · rw [abs_of_nonpos (show x≤0 by omega),abs_of_nonpos (show y≤0 by omega)]
      omega

private theorem long_growth {p l t : ℕ} (hp : 9*t+3≤p) (hl : l≤2*t) :
    (2:ℚ)^l*(2*3^t) < (4/3:ℚ)^p := by
  have a : (2:ℚ)^l ≤ 2^(2*t) := pow_le_pow_right₀ (by norm_num) hl
  have b : (12:ℚ)^t ≤ ((4/3:ℚ)^9)^t :=
    pow_le_pow_left₀ (by norm_num) (by norm_num) t
  have c : (2:ℚ)<(4/3:ℚ)^3 := by norm_num
  have d := pow_le_pow_right₀ (show (1:ℚ)≤4/3 by norm_num) hp
  rw [pow_add,pow_mul] at d
  have X := mul_le_mul_of_nonneg_right a (show (0:ℚ)≤2*3^t by positivity)
  have Y := mul_le_mul_of_nonneg_right b (show (0:ℚ)≤2 by norm_num)
  have Z := mul_lt_mul_of_pos_left c (show (0:ℚ)<((4/3:ℚ)^9)^t by positivity)
  have sub : (2:ℚ)^(2*t)*3^t=12^t := by rw [pow_mul,←mul_pow];norm_num
  nlinarith only [X,Y,Z,d,sub]

/-- The terminal of a signed prefix with many odds, few evens and small
    magnitude must be minus one. -/
theorem signed_trap {h p t : ℕ} {x z : ℤ} (W : Walk h p x z)
    (high : 9*t+3≤p) (low : h-p≤2*t) (small : |z|≤2*(3:ℤ)^t) : z = -1 := by
  by_contra Z
  have neq : x≠0 := by
    intro X
    have Q := (zero_origin W X).1
    omega
  have X : (1:ℚ) ≤ |(x:ℚ)| := by
    have G : (1:ℤ)≤|x| := by rcases le_total 0 x with L|L <;> simp [abs_of_nonneg,abs_of_nonpos,L] <;> omega
    exact_mod_cast G
  have A := signed_growth W Z
  have B := long_growth high low
  have C : |(z:ℚ)|≤2*(3:ℚ)^t := by exact_mod_cast small
  have D := mul_le_mul_of_nonneg_left C (show (0:ℚ)≤2^(h-p) by positivity)
  have E := mul_le_mul_of_nonneg_left X (show (0:ℚ)≤(4/3:ℚ)^p by positivity)
  linarith

end RampShadow.Postpeak
