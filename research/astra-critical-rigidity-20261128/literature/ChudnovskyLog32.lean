import QuadraticPi.RationalTwoLogLinearForm

/-! The exact Collatz slope and its homogeneous linear-form inequality,
specialized from Chudnovsky's original October 2026 supplement. -/
set_option autoImplicit false
namespace Collatz.ChudnovskyLog32

private theorem logTwo_ne : Real.log 2 ≠ 0 :=
  Real.log_ne_zero_of_pos_of_ne_one (by norm_num) (by norm_num)

private theorem independent : QuadraticPi.TwoLogCharacterCenters.NoPowerRelation 3 2 := by
  apply QuadraticPi.TwoLogCharacterCenters.noPowerRelation_of_irrational_log_ratio logTwo_ne
  simpa only [inv_div] using
    QuadraticPi.TwoLogCharacterCenters.irrational_log_two_div_log_three.inv

theorem exponent_bounds :
    2 ≤ QuadraticPi.irrationalityExponent (Real.log 3 / Real.log 2) ∧
    QuadraticPi.irrationalityExponent (Real.log 3 / Real.log 2) ≤ 3 := by
  simpa only [Rat.cast_ofNat] using
    QuadraticPi.rationalLogRatio_irrationalityExponent_bounds 3 2
      (by norm_num) (by norm_num) (by simpa only [Rat.cast_ofNat] using logTwo_ne)
      (by simpa only [Rat.cast_ofNat] using independent)

theorem finite_good (ν : ℝ) (hν : 3 < ν) :
    (QuadraticPi.GoodRationalApproximations (Real.log 3 / Real.log 2) ν).Finite := by
  simpa only [Rat.cast_ofNat] using
    QuadraticPi.rationalLogRatio_finite_good 3 2
      (by norm_num) (by norm_num) (by simpa only [Rat.cast_ofNat] using logTwo_ne)
      (by simpa only [Rat.cast_ofNat] using independent) ν hν

theorem uniform_linear_form (ε : ℝ) (hε : 0 < ε) :
    ∃ C : ℝ, 0 < C ∧ ∀ p q : ℤ, (p, q) ≠ (0, 0) →
      C * (max 1 (max |(p : ℝ)| |(q : ℝ)|)) ^ (-2 - ε) ≤
        |(p : ℝ) * Real.log 3 + (q : ℝ) * Real.log 2| := by
  simpa only [Rat.cast_ofNat] using
    QuadraticPi.rationalTwoLog_linearForm_lowerBound 3 2
      (by norm_num) (by norm_num) (by simpa only [Rat.cast_ofNat] using logTwo_ne)
      (by simpa only [Rat.cast_ofNat] using independent) ε hε

#print axioms Collatz.ChudnovskyLog32.exponent_bounds
#print axioms Collatz.ChudnovskyLog32.finite_good
#print axioms Collatz.ChudnovskyLog32.uniform_linear_form

end Collatz.ChudnovskyLog32
