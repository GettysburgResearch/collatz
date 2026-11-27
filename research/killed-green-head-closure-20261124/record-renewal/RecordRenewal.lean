import Mathlib

/-! Candidate finite core. Uncompiled in the authoring environment.
    The asymptotic and topological parts are in README.md. -/
namespace RecordRenewal

def aff (m s : ℕ) (C z : ℚ) : ℚ :=
  ((3 : ℚ)^m*z+C)/(2 : ℚ)^s

theorem positive_carry_expanding_fixed_negative (m s : ℕ) (C z : ℚ)
    (h : (2:ℚ)^s < 3^m) (hc : 0<C) (hz : aff m s C z=z) :
    z < 0 := by
  have hp : (0:ℚ)<2^s := by positivity
  have he : (3:ℚ)^m*z+C=(2:ℚ)^s*z := by
    have hh := (div_eq_iff hp.ne').mp hz
    simpa [aff, mul_comm] using hh
  by_contra hn
  have hz0 : 0≤z := le_of_not_gt hn
  have hm := mul_nonneg (le_of_lt (sub_pos.mpr h)) hz0
  nlinarith

/-- The exact prefix-ratio maximum of a complete backward block cannot
    be exceeded by a later critical continuation. -/
theorem strict_ratio_tail (r a : ℚ) (hr : 0<r) (ha : a<1) :
    r*a < r := by
  simpa using mul_lt_mul_of_pos_left ha hr

/-- The integer carry difference, with complete clock and modulus
    retained, is exactly a multiple of the original ternary power. -/
theorem equal_row_difference (A P q x y C D : ℤ)
    (hx : A*q=P*x+C) (hy : A*q=P*y+D) :
    C-D=P*(y-x) := by
  linarith [show P*(y-x)=P*y-P*x by ring]

theorem affine_difference (m s : ℕ) (C x y : ℚ) :
    aff m s C x-aff m s C y =
       ((3:ℚ)^m/(2:ℚ)^s)*(x-y) := by
  unfold aff
  ring

/-- No cancellation of a dyadic denominator can occur after
    applying an odd-gap formula to a rational with odd numerator
    and even denominator. -/
theorem odd_plus_even (a d : ℤ)
    (ha : a%2=1) (hd : d%2=0) : (3*a+d)%2=1 := by omega

theorem even_plus_odd (a d : ℤ)
    (ha : a%2=0) (hd : d%2=1) : (3*a+d)%2=1 := by omega

/-- Wrong-gap case e>g, with the reduced odd numerator exposed. -/
theorem wrong_gap_over (a d u : ℚ) (e g : ℕ)
    (he : g≤e) (hd : d≠0) (h : 3*a+d=(2:ℚ)^g*u) :
    (3*(a/d)+1)/(2:ℚ)^e = u/((2:ℚ)^(e-g)*d) := by
  have hs : e=g+(e-g) := by omega
  have htwo : (2:ℚ)^e=(2:ℚ)^g*(2:ℚ)^(e-g) := by
    conv_lhs => rw [hs]
    rw [pow_add]
  rw [htwo]
  field_simp [hd]
  <;> nlinarith [h]

/-- Wrong-gap case e<g, with the residual even numerator exposed. -/
theorem wrong_gap_under (a d u : ℚ) (e g : ℕ)
    (he : e≤g) (hd : d≠0) (h : 3*a+d=(2:ℚ)^g*u) :
    (3*(a/d)+1)/(2:ℚ)^e = ((2:ℚ)^(g-e)*u)/d := by
  have hs : g=e+(g-e) := by omega
  have htwo : (2:ℚ)^g=(2:ℚ)^e*(2:ℚ)^(g-e) := by
    conv_lhs => rw [hs]
    rw [pow_add]
  rw [htwo] at h
  field_simp [hd]
  <;> nlinarith [h]

theorem dyadic_unbounded (n : ℕ) (hn : 0<n)
    (hall : ∀ k : ℕ, 2^k ∣ n) : False := by
  have hpow : ∀ k : ℕ, k<2^k := by
    intro k
    induction k with
    | zero => decide
    | succ k ih =>
      rw [pow_succ]
      omega
  exact (not_le_of_gt (hpow n)) (Nat.le_of_dvd hn (hall n))

/-- The finite divisibility consumer in the fixed-source lock argument.
    The derivation of its premise from a common infinite physical word
    is separate written mathematics. -/
theorem fixed_positive_gap_cannot_lock (x d n : ℕ)
    (hx : 0<x) (hd : 0<d)
    (h : ∀ k : ℕ, 2^k ∣ d*x+n) : False := by
  have hdx : 0<d*x := Nat.mul_pos hd hx
  exact dyadic_unbounded (d*x+n) (by omega) h

end RecordRenewal

#print axioms RecordRenewal.positive_carry_expanding_fixed_negative
#print axioms RecordRenewal.strict_ratio_tail
#print axioms RecordRenewal.equal_row_difference
#print axioms RecordRenewal.affine_difference
#print axioms RecordRenewal.odd_plus_even
#print axioms RecordRenewal.even_plus_odd
#print axioms RecordRenewal.wrong_gap_over
#print axioms RecordRenewal.wrong_gap_under
#print axioms RecordRenewal.dyadic_unbounded
#print axioms RecordRenewal.fixed_positive_gap_cannot_lock
