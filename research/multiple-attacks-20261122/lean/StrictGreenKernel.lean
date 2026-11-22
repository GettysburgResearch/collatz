module

public import ShellCover
public import Mathlib.Analysis.SpecialFunctions.Exp
public import Mathlib.Algebra.BigOperators.Ring.Finset

@[expose] public section

/-!
# The finite path kernel of the strict Green correction

These identities hold for every finite list of intermediate weights. They
check the cancellation giving the closed resolvent kernel, its complete
subset polynomial, and the exponential absolute majorant. The countable
operator bounds and actual path-count input remain written mathematics in
STRICT_GREEN_VOLTERRA.md; they are not installed as axioms here.
-/

namespace CollatzStrictGreen

section Ring

variable {R : Type*} [CommRing R]

def survival (z : R) (weights : List R) : R :=
  (weights.map (fun w => 1 - z*w)).prod

def weightedTail (z : R) : List R → R
  | [] => 0
  | w :: rest => w * survival z rest + weightedTail z rest

/-- The finite path product telescopes exactly, retaining every intermediate
state. There is no division by the parameter, including at parameter zero. -/
theorem path_telescope (z : R) (weights : List R) :
    z * weightedTail z weights = 1 - survival z weights := by
  induction weights with
  | nil => simp [weightedTail, survival]
  | cons w rest ih =>
      simp only [weightedTail, survival, List.map_cons, List.prod_cons] at *
      linear_combination ih

/-- The off-diagonal entry in the product of I+zK with the proposed inverse
vanishes on every actual finite path. Its interior sum is weightedTail. -/
theorem inverse_path_cancellation (z initialWeight : R) (interior : List R) :
    -z*initialWeight*survival z interior + z*initialWeight -
      z^2*initialWeight*weightedTail z interior = 0 := by
  have h := path_telescope z interior
  linear_combination -z*initialWeight*h

/-- Every ordered selection of intermediate states is present in the finite
Neumann polynomial. The use of indices permits repeated numerical weights. -/
theorem subset_kernel {ι : Type*} (s : Finset ι) (w : ι → R) (z : R) :
    (∑ t ∈ s.powerset, ∏ i ∈ t, (-z*w i)) =
      ∏ i ∈ s, (1-z*w i) := by
  simpa only [sub_eq_add_neg, neg_mul] using
    (Finset.prod_one_add (f := fun i => -z*w i) s).symm

end Ring

/-- At the positive physical correction parameter, every finite survival
product lies in [0,1]. This gives the sharper written inverse bound at z=1. -/
theorem survival_unit_interval (z : ℝ) (weights : List ℝ)
    (bounds : ∀ w ∈ weights, 0 ≤ z*w ∧ z*w ≤ 1) :
    0 ≤ survival z weights ∧ survival z weights ≤ 1 := by
  induction weights with
  | nil => simp [survival]
  | cons w rest ih =>
      have hw := bounds w (by simp)
      have hr : ∀ a ∈ rest, 0 ≤ z*a ∧ z*a ≤ 1 := by
        intro a ha
        exact bounds a (by simp [ha])
      have tail := ih hr
      have factor_nonnegative : 0 ≤ 1-z*w := by linarith [hw.2]
      have factor_le_one : 1-z*w ≤ 1 := by linarith [hw.1]
      change 0 ≤ (1-z*w)*survival z rest ∧ (1-z*w)*survival z rest ≤ 1
      constructor
      · exact mul_nonneg factor_nonnegative tail.1
      · calc
          (1-z*w)*survival z rest ≤ 1*1 :=
            mul_le_mul factor_le_one tail.2 tail.1 (by norm_num)
          _ = 1 := by norm_num

/-- The complete path kernel is bounded by an exponential of the summed
nonnegative immigration weights. This controls the infinite-source passage
in the written argument, without assuming convergence of an orbit. -/
theorem survival_abs_bound (z : ℝ) (weights : List ℝ)
    (nonnegative : ∀ w ∈ weights, 0 ≤ w) :
    |survival z weights| ≤ Real.exp (|z| * weights.sum) := by
  induction weights with
  | nil => simp [survival]
  | cons w rest ih =>
      have hw : 0 ≤ w := nonnegative w (by simp)
      have hr : ∀ a ∈ rest, 0 ≤ a := by
        intro a ha
        exact nonnegative a (by simp [ha])
      have factor_bound : |1-z*w| ≤ Real.exp (|z| * w) := by
        calc
          |1-z*w| ≤ |(1:ℝ)| + |z*w| := by
            simpa only [sub_zero, zero_sub, abs_neg] using
              (abs_sub_le (1:ℝ) 0 (z*w))
          _ = 1 + |z| * w := by rw [abs_one, abs_mul, abs_of_nonneg hw]
          _ ≤ Real.exp (|z| * w) := by linarith [Real.add_one_le_exp (|z| * w)]
      have tail := ih hr
      change |(1-z*w) * survival z rest| ≤ Real.exp (|z| * (w+rest.sum))
      rw [abs_mul]
      calc
        |1-z*w| * |survival z rest| ≤
            Real.exp (|z| * w) * Real.exp (|z| * rest.sum) :=
          mul_le_mul factor_bound tail (abs_nonneg _) (le_of_lt (Real.exp_pos _))
        _ = Real.exp (|z| * (w+rest.sum)) := by
          rw [← Real.exp_add]
          congr 1
          ring

end CollatzStrictGreen

#print axioms CollatzStrictGreen.path_telescope
#print axioms CollatzStrictGreen.inverse_path_cancellation
#print axioms CollatzStrictGreen.subset_kernel
#print axioms CollatzStrictGreen.survival_unit_interval
#print axioms CollatzStrictGreen.survival_abs_bound
