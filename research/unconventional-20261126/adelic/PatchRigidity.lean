import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Ring

/-! The integer part of the Fourier patch argument. A centered congruence
    whose discrepancy has magnitude strictly below the modulus is an equality.
    A consecutive run of such congruences forces a ternary divisor at its source.
    The Fourier estimates and logarithmic forms are outside this formalization. -/
namespace PatchRigidity

inductive SmallRun (modulus : ℤ) (width : ℕ) : List ℕ → ℤ → ℤ → Prop where
  | nil (x : ℤ) : SmallRun modulus width [] x x
  | step {q : ℕ} {grades : List ℕ} {x y z : ℤ}
      (reduction : modulus ∣ (3 : ℤ) ^ q * y - 2 ^ width * x)
      (small : ((3 : ℤ) ^ q * y - 2 ^ width * x).natAbs < modulus.natAbs)
      (tail : SmallRun modulus width grades y z) :
      SmallRun modulus width (q :: grades) x z

theorem telescope {modulus : ℤ} {width : ℕ} {grades : List ℕ} {x z : ℤ}
    (h : SmallRun modulus width grades x z) :
    (3 : ℤ) ^ grades.sum * z = ((2 : ℤ) ^ width) ^ grades.length * x := by
  induction h with
  | nil => simp
  | @step q grades x y z reduction small _ ih =>
      have edge : (3 : ℤ) ^ q * y = 2 ^ width * x :=
        sub_eq_zero.mp (Int.eq_zero_of_dvd_of_natAbs_lt_natAbs reduction small)
      simp only [List.sum_cons, List.length_cons, pow_add, pow_succ]
      calc
        _ = (3 : ℤ) ^ q * (3 ^ grades.sum * z) := by ring
        _ = 3 ^ q * (((2 : ℤ) ^ width) ^ grades.length * y) := by rw [ih]
        _ = ((2 : ℤ) ^ width) ^ grades.length * (3 ^ q * y) := by ring
        _ = _ := by rw [edge]; ring

theorem ternary_divides_source {modulus : ℤ} {width : ℕ}
    {grades : List ℕ} {x z : ℤ} (h : SmallRun modulus width grades x z) :
    (3 : ℤ) ^ grades.sum ∣ x := by
  have hthree : IsCoprime (3 : ℤ) 2 := ⟨1, -1, by decide⟩
  have hc : IsCoprime ((3 : ℤ) ^ grades.sum) (((2 : ℤ) ^ width) ^ grades.length) :=
    ((hthree.pow_left).pow_right).pow_right
  apply hc.dvd_of_dvd_mul_left
  rw [← telescope h]
  exact dvd_mul_right _ _

theorem no_long_small_run {modulus : ℤ} {width : ℕ}
    {grades : List ℕ} {x z : ℤ} (hx : x ≠ 0)
    (hsize : x.natAbs < ((3 : ℤ) ^ grades.sum).natAbs) :
    ¬ SmallRun modulus width grades x z := by
  intro h
  exact hx (Int.eq_zero_of_dvd_of_natAbs_lt_natAbs (ternary_divides_source h) hsize)

#print axioms telescope
#print axioms ternary_divides_source
#print axioms no_long_small_run

end PatchRigidity
