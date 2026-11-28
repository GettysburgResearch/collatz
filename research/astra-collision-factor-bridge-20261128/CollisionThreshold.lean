import Mathlib.Topology.Algebra.InfiniteSum.ENNReal
import Mathlib.Topology.Algebra.InfiniteSum.Ring
import Mathlib.Tactic

/-!
# The countable-cycle maximal collision threshold

The analytic identification of the ordinary median statistic with this
series is an external hypothesis in the written packet. This module proves
the full infinite-series extremal argument, including arbitrary unused mass.
No convergence theorem or analytic Collatz input is postulated as an axiom.
-/

namespace Collatz.CollisionThreshold

variable {ι : Type*}

noncomputable def median (b : ℝ) (w P : ι → ℝ) : ℝ :=
  b ^ 2 / 8 + ∑' i, w i ^ 2 / (4 * P i)

/-- Every other cycle contribution is dominated on the actual remaining
mass scale. The mass budget allows mass on nonperiodic components. -/
theorem term_bound (b : ℝ) (w P : ι → ℝ)
    (hw : ∀ i, 0 ≤ w i) (hs : Summable w)
    (hm : b + ∑' i, w i ≤ 1) (hP : ∀ i, 2 ≤ P i) (i : ι) :
    0 ≤ w i ^ 2 / (4 * P i) ∧
      w i ^ 2 / (4 * P i) ≤ (1 - b) * w i / 8 := by
  have hi : w i ≤ ∑' j, w j := hs.le_tsum i (fun j _ => hw j)
  have hwi : w i ≤ 1 - b := by linarith
  have hp : 0 < 4 * P i := by nlinarith [hP i]
  constructor
  · exact div_nonneg (sq_nonneg _) hp.le
  · have hsq : w i ^ 2 ≤ (1 - b) * w i := by
      nlinarith [mul_nonneg (hw i) (sub_nonneg.mpr hwi)]
    calc
      w i ^ 2 / (4 * P i) ≤ w i ^ 2 / 8 := by
        apply div_le_div_of_nonneg_left (sq_nonneg _) (by norm_num)
        nlinarith [hP i]
      _ ≤ (1 - b) * w i / 8 := div_le_div_of_nonneg_right hsq (by norm_num)

theorem summable_cycle_contributions (b : ℝ) (w P : ι → ℝ)
    (hw : ∀ i, 0 ≤ w i) (hs : Summable w)
    (hm : b + ∑' i, w i ≤ 1) (hP : ∀ i, 2 ≤ P i) :
    Summable (fun i => w i ^ 2 / (4 * P i)) := by
  have hmajor : Summable (fun i => (1 - b) * w i / 8) :=
    (hs.mul_left (1 - b)).div_const 8
  exact Summable.of_nonneg_of_le
    (fun i => (term_bound b w P hw hs hm hP i).1)
    (fun i => (term_bound b w P hw hs hm hP i).2) hmajor

/-- The exact global upper bound includes every other finite cycle and
does not require the total cycle mass to equal one. -/
theorem median_le_two_mass_bound (b : ℝ) (w P : ι → ℝ)
    (_hb : 0 ≤ b) (hw : ∀ i, 0 ≤ w i) (hs : Summable w)
    (hm : b + ∑' i, w i ≤ 1) (hP : ∀ i, 2 ≤ P i) :
    median b w P ≤ (b ^ 2 + (1 - b) ^ 2) / 8 := by
  have hsum0 : 0 ≤ ∑' i, w i := tsum_nonneg hw
  have hb1 : b ≤ 1 := by linarith
  have hmajor : Summable (fun i => (1 - b) * w i / 8) :=
    (hs.mul_left (1 - b)).div_const 8
  have hsum := (summable_cycle_contributions b w P hw hs hm hP).tsum_le_tsum
    (fun i => (term_bound b w P hw hs hm hP i).2)
    hmajor
  have hlin : (∑' i, (1 - b) * w i / 8) =
      (1 - b) * (∑' i, w i) / 8 := by
    rw [tsum_div_const, tsum_mul_left]
  rw [hlin] at hsum
  have hprod := mul_le_mul_of_nonneg_left
    (show (∑' i, w i) ≤ 1 - b by linarith) (sub_nonneg.mpr hb1)
  unfold median
  nlinarith

/-- The collision deficit is at least one quarter of the known basin's
mass times its complement. A positive known basin rules out the other
algebraic endpoint. -/
theorem deficit_lower_bound (b : ℝ) (w P : ι → ℝ)
    (hb : 0 ≤ b) (hw : ∀ i, 0 ≤ w i) (hs : Summable w)
    (hm : b + ∑' i, w i ≤ 1) (hP : ∀ i, 2 ≤ P i) :
    b * (1 - b) / 4 ≤ 1 / 8 - median b w P := by
  have h := median_le_two_mass_bound b w P hb hw hs hm hP
  nlinarith

theorem maximal_collision_forces_full_known_mass (b : ℝ) (w P : ι → ℝ)
    (hb : 0 < b) (hw : ∀ i, 0 ≤ w i) (hs : Summable w)
    (hm : b + ∑' i, w i ≤ 1) (hP : ∀ i, 2 ≤ P i)
    (hlower : 1 / 8 ≤ median b w P) : b = 1 := by
  have hsum0 : 0 ≤ ∑' i, w i := tsum_nonneg hw
  have hb1 : b ≤ 1 := by linarith
  have hd := deficit_lower_bound b w P hb.le hw hs hm hP
  have hp : b * (1 - b) ≤ 0 := by linarith
  have hc : 1 - b ≤ 0 := nonpos_of_mul_nonpos_right hp hb
  linarith

/-- A quantified lower approximation to one eighth controls all mass
outside the known cycle. The positive floor must be independently supplied. -/
theorem near_maximal_collision_mass (b c ε : ℝ) (w P : ι → ℝ)
    (hc : 0 < c) (hcb : c ≤ b)
    (hw : ∀ i, 0 ≤ w i) (hs : Summable w)
    (hm : b + ∑' i, w i ≤ 1) (hP : ∀ i, 2 ≤ P i)
    (hlower : 1 / 8 - ε ≤ median b w P) :
    c * (1 - b) ≤ 4 * ε := by
  have hb : 0 ≤ b := (hc.le).trans hcb
  have hsum0 : 0 ≤ ∑' i, w i := tsum_nonneg hw
  have hb1 : b ≤ 1 := by linarith
  have hd := deficit_lower_bound b w P hb hw hs hm hP
  have hp := mul_le_mul_of_nonneg_right hcb (sub_nonneg.mpr hb1)
  linarith

/-- At full known-cycle mass all other nonnegative masses vanish, so the
series equals one eighth exactly, independently of their periods. -/
theorem full_known_mass_gives_maximal_collision (w P : ι → ℝ)
    (hw : ∀ i, 0 ≤ w i) (hs : Summable w)
    (hm : 1 + ∑' i, w i ≤ 1) : median 1 w P = 1 / 8 := by
  have ht : (∑' i, w i) = 0 := by
    have hnonneg : 0 ≤ ∑' i, w i := tsum_nonneg hw
    linarith
  have hz : ∀ i, w i = 0 := by
    intro i
    have hi : w i ≤ ∑' j, w j := hs.le_tsum i (fun j _ => hw j)
    rw [ht] at hi
    exact le_antisymm hi (hw i)
  simp [median, hz]

/-- The maximal lower bound is precisely the full-known-basin-mass claim.
The positive known basin excludes the extraneous zero-mass endpoint. -/
theorem maximal_collision_iff_full_known_mass (b : ℝ) (w P : ι → ℝ)
    (hb : 0 < b) (hw : ∀ i, 0 ≤ w i) (hs : Summable w)
    (hm : b + ∑' i, w i ≤ 1) (hP : ∀ i, 2 ≤ P i) :
    1 / 8 ≤ median b w P ↔ b = 1 := by
  constructor
  · exact maximal_collision_forces_full_known_mass b w P hb hw hs hm hP
  · intro heq
    subst b
    exact (full_known_mass_gives_maximal_collision w P hw hs hm).ge

end Collatz.CollisionThreshold
