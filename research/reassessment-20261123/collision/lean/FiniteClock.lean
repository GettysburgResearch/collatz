import Mathlib.Topology.Algebra.InfiniteSum.Real
import Mathlib.Topology.Algebra.InfiniteSum.Ring
import Mathlib.Tactic.Linarith

/-!
The deterministic infinite-series core of finite-clock explosion.  No
existence of a Collatz escape, harmonic flow, or stochastic process is
asserted.  A positive nondecreasing flow on an injective ordinary orbit,
and a summable normalization on the whole state set, force summability
of that orbit's reciprocal jump rates with an explicit total bound.
The accompanying written proof supplies the exponential holding-time
and minimal-process consequences.
-/

namespace CollatzReassessment.FiniteClock

theorem floor_along_orbit (nu : ℕ → ℝ) (q : ℕ → ℕ)
    (hmono : ∀ j, nu (q j) ≤ nu (q (j + 1))) :
    ∀ j, nu (q 0) ≤ nu (q j) := by
  intro j
  induction j with
  | zero => exact le_rfl
  | succ j ih => exact ih.trans (hmono j)

/-- Every finite positive normalization of a nondecreasing flow gives
finite total reciprocal rate along any injective orbit. -/
theorem finite_normalization_forces_summable_clock
    (nu rate : ℕ → ℝ) (q : ℕ → ℕ)
    (hnu : ∀ n, 0 ≤ nu n) (hrate : ∀ n, 0 < rate n)
    (hinj : Function.Injective q)
    (hpositive : 0 < nu (q 0))
    (hmono : ∀ j, nu (q j) ≤ nu (q (j + 1)))
    (hmass : Summable (fun n => nu n / rate n)) :
    Summable (fun j => 1 / rate (q j)) ∧
      (∑' j, 1 / rate (q j)) ≤
        (∑' n, nu n / rate n) / nu (q 0) := by
  have hfloor := floor_along_orbit nu q hmono
  have horbit : Summable (fun j => nu (q j) / rate (q j)) :=
    hmass.comp_injective hinj
  have hscaled : Summable (fun j => (nu (q j) / rate (q j)) / nu (q 0)) :=
    horbit.div_const _
  have hterm : ∀ j, 1 / rate (q j) ≤
      (nu (q j) / rate (q j)) / nu (q 0) := by
    intro j
    apply (le_div_iff₀ hpositive).2
    have hh := mul_le_mul_of_nonneg_right (hfloor j)
      (inv_nonneg.mpr (hrate (q j)).le)
    simp only [div_eq_mul_inv] at *
    nlinarith
  have hsum : Summable (fun j => 1 / rate (q j)) :=
    Summable.of_nonneg_of_le
      (fun j => (one_div_pos.mpr (hrate (q j))).le) hterm hscaled
  refine ⟨hsum, ?_⟩
  calc
    (∑' j, 1 / rate (q j)) ≤
        ∑' j, (nu (q j) / rate (q j)) / nu (q 0) :=
      hsum.tsum_le_tsum hterm hscaled
    _ = (∑' j, nu (q j) / rate (q j)) / nu (q 0) := tsum_div_const
    _ ≤ (∑' n, nu n / rate n) / nu (q 0) := by
      apply div_le_div_of_nonneg_right _ hpositive.le
      exact tsum_comp_le_tsum_of_inj hmass
        (fun n => div_nonneg (hnu n) (hrate n).le) hinj

end CollatzReassessment.FiniteClock
