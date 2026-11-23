import Mathlib.MeasureTheory.OuterMeasure.BorelCantelli
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
The infinite Borel--Cantelli bridge used in BOUNDARY_OVERLAP.md, Sections 4--5.

The first Borel--Cantelli lemma is applied to the supplied bad-event mass sum;
eventual avoidance is a conclusion, not an additional hypothesis. Infinitely
many actual good returns remain infinitely many after the null exceptional
set is removed. The final theorem specializes this to real closed-ball mass
at path-dependent positive radii tending to zero.

The statements use `OuterMeasureClass`, so the path law can be an ordinary
measure or its outer measure. No event measurability or independence is
required for this direction of Borel--Cantelli. The bad-event sum, actual
good-return hypothesis, and scale convergence must still be supplied by the
analytic argument; their Collatz-specific construction is not formalized here.
-/

namespace CollatzSourceClock.BoundaryBorelCantelli

open Filter MeasureTheory
open scoped ENNReal Topology

variable {Ω M : Type*} [FunLike M (Set Ω) ℝ≥0∞] [OuterMeasureClass M Ω]

/-- A summable sequence of bad-event masses removes only finitely many
indices almost surely. Thus almost-sure infinitely many good returns still
occur infinitely often outside the bad events. -/
theorem ae_frequently_good_avoiding_bad
    (μ : M) (good bad : ℕ → Set Ω)
    (hsum : (∑' n, μ (bad n)) ≠ ∞)
    (hgood : ∀ᵐ ω ∂μ, ∃ᶠ n in atTop, ω ∈ good n) :
    ∀ᵐ ω ∂μ, ∃ᶠ n in atTop, ω ∈ good n ∧ ω ∉ bad n := by
  filter_upwards [hgood, ae_eventually_notMem (μ := μ) hsum] with ω hreturn havoid
  exact hreturn.and_eventually havoid

/-- The infinite surviving returns can be selected as a strictly increasing
subsequence for almost every path. No bound on the gaps is asserted. -/
theorem ae_exists_good_subsequence_avoiding_bad
    (μ : M) (good bad : ℕ → Set Ω)
    (hsum : (∑' n, μ (bad n)) ≠ ∞)
    (hgood : ∀ᵐ ω ∂μ, ∃ᶠ n in atTop, ω ∈ good n) :
    ∀ᵐ ω ∂μ, ∃ φ : ℕ → ℕ, StrictMono φ ∧
      ∀ j, ω ∈ good (φ j) ∧ ω ∉ bad (φ j) := by
  filter_upwards [ae_frequently_good_avoiding_bad μ good bad hsum hgood] with ω hω
  exact extraction_of_frequently_atTop hω

/-- The boundary application: almost every sampled path has arbitrarily
small positive good radii at which a fixed reference real measure satisfies
the desired power bound. The reference law need not equal the sampled
boundary marginal. The exponent is arbitrary here; the dimension argument
uses each fixed `0 < s < 1` and then a countable family of exponents. -/
theorem ae_arbitrarily_small_real_ball_bounds
    (μ : M) (η : OuterMeasure ℝ) (boundary : Ω → ℝ)
    (radius : ℕ → Ω → ℝ) (s : ℝ) (good : ℕ → Set Ω)
    (hsum : (∑' n, μ {ω | ω ∈ good n ∧
      ENNReal.ofReal ((radius n ω) ^ s) <
        η (Metric.closedBall (boundary ω) (radius n ω))}) ≠ ∞)
    (hgood : ∀ᵐ ω ∂μ, ∃ᶠ n in atTop, ω ∈ good n)
    (hpositive : ∀ n ω, ω ∈ good n → 0 < radius n ω)
    (hzero : ∀ᵐ ω ∂μ, Tendsto (fun n => radius n ω) atTop (𝓝 0)) :
    ∀ᵐ ω ∂μ, ∀ ε : ℝ, 0 < ε → ∃ n,
      ω ∈ good n ∧ 0 < radius n ω ∧ radius n ω < ε ∧
      η (Metric.closedBall (boundary ω) (radius n ω)) ≤
        ENNReal.ofReal ((radius n ω) ^ s) := by
  let bad : ℕ → Set Ω := fun n => {ω | ω ∈ good n ∧
    ENNReal.ofReal ((radius n ω) ^ s) <
      η (Metric.closedBall (boundary ω) (radius n ω))}
  have hsurvive := ae_frequently_good_avoiding_bad μ good bad hsum hgood
  filter_upwards [hsurvive, hzero] with ω hω hlimit
  intro ε hε
  have hsmall : ∀ᶠ n in atTop, radius n ω < ε :=
    hlimit.eventually (gt_mem_nhds hε)
  obtain ⟨n, hreturn, hscale⟩ := (hω.and_eventually hsmall).exists
  refine ⟨n, hreturn.1, hpositive n ω hreturn.1, hscale, ?_⟩
  exact le_of_not_gt (fun hlarge => hreturn.2 ⟨hreturn.1, hlarge⟩)

end CollatzSourceClock.BoundaryBorelCantelli
