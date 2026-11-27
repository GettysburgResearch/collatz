import Mathlib.Algebra.Order.Archimedean.Real.Basic
import Mathlib.Tactic.Linarith

/-!
The complete order argument behind positive invariant-measure uniqueness.

An index can be any measurable set; the distinguished index represents the
whole space. `Mem` represents nonnegative finite invariant measures through
their real evaluations. The hypotheses state positivity, domination by total
mass, closure under a dominated subtraction of invariant measures, and a
uniform lower bound by one normalized invariant measure. The index type is
arbitrary, so the theorem is not restricted to finite state spaces.

This file does not establish the Collatz word minorization or turn an infinite
ordinary reciprocal measure into a finite measure.
-/

namespace CollatzInvariantCone

structure PositiveCone (ι : Type*) (whole : ι) where
  Mem : (ι → ℝ) → Prop
  nonneg : ∀ {f : ι → ℝ}, Mem f → ∀ i, 0 ≤ f i
  le_mass : ∀ {f : ι → ℝ}, Mem f → ∀ i, f i ≤ f whole
  sub_smul : ∀ {f h : ι → ℝ}, Mem f → Mem h → ∀ a : ℝ,
    0 ≤ a → (∀ i, a * h i ≤ f i) → Mem (fun i => f i - a * h i)

variable {ι : Type*} {whole : ι}

/-- Every element of zero total mass is identically zero. -/
theorem zero_mass {C : PositiveCone ι whole} {f : ι → ℝ}
    (hf : C.Mem f) (hzero : f whole = 0) : f = 0 := by
  funext i
  apply le_antisymm
  · simpa only [hzero, Pi.zero_apply] using C.le_mass hf i
  · exact C.nonneg hf i

/-- A lower bound for all positive invariant residuals gives uniqueness.

The lower bound is required on the entire positive invariant cone, including
dominated residuals. A bound known only for the original measure is not enough.
-/
theorem unique_of_uniform_minorization
    (C : PositiveCone ι whole) (h : ι → ℝ) (hh : C.Mem h)
    (hunit : h whole = 1) (c : ℝ) (hc : 0 < c)
    (minor : ∀ f : ι → ℝ, C.Mem f → ∀ i, c * f whole * h i ≤ f i)
    (f : ι → ℝ) (hf : C.Mem f) :
    f = fun i => f whole * h i := by
  let S : Set ℝ := {a | 0 ≤ a ∧ ∀ i, a * h i ≤ f i}
  have hzero : (0 : ℝ) ∈ S := by
    refine ⟨le_rfl, ?_⟩
    intro i
    simpa only [zero_mul] using C.nonneg hf i
  have hne : S.Nonempty := ⟨0, hzero⟩
  have hbdd : BddAbove S := by
    refine ⟨f whole, ?_⟩
    intro a ha
    simpa only [hunit, mul_one] using ha.2 whole
  let a : ℝ := sSup S
  have ha0 : 0 ≤ a := le_csSup hbdd hzero
  have haf : a ≤ f whole := by
    apply csSup_le hne
    intro b hb
    simpa only [hunit, mul_one] using hb.2 whole
  have hadom : ∀ i, a * h i ≤ f i := by
    intro i
    have hi := C.nonneg hh i
    by_cases hz : h i = 0
    · simpa only [hz, mul_zero] using C.nonneg hf i
    · have hip : 0 < h i := lt_of_le_of_ne hi (Ne.symm hz)
      have hsup : a ≤ f i / h i := by
        apply csSup_le hne
        intro b hb
        exact (le_div_iff₀ hip).2 (hb.2 i)
      exact (le_div_iff₀ hip).1 hsup
  let r : ι → ℝ := fun i => f i - a * h i
  have hr : C.Mem r := C.sub_smul hf hh a ha0 hadom
  have hrwhole : r whole = f whole - a := by
    simp only [r, hunit, mul_one]
  have hrnonneg : 0 ≤ r whole := C.nonneg hr whole
  have hbmem : a + c * r whole ∈ S := by
    refine ⟨add_nonneg ha0 (mul_nonneg (le_of_lt hc) hrnonneg), ?_⟩
    intro i
    have hi := minor r hr i
    change c * r whole * h i ≤ f i - a * h i at hi
    nlinarith only [hi]
  have hble : a + c * r whole ≤ a := le_csSup hbdd hbmem
  have hrzero : r whole = 0 := by
    nlinarith only [hc, hrnonneg, hble]
  have haeq : a = f whole := by
    linarith only [hrwhole, hrzero]
  have hrfun := zero_mass hr hrzero
  funext i
  have hri := congrFun hrfun i
  change f i - a * h i = 0 at hri
  rw [haeq] at hri
  linarith only [hri]

/-- In particular there is exactly one normalized positive element. -/
theorem normalized_unique
    (C : PositiveCone ι whole) (h : ι → ℝ) (hh : C.Mem h)
    (hunit : h whole = 1) (c : ℝ) (hc : 0 < c)
    (minor : ∀ f : ι → ℝ, C.Mem f → ∀ i, c * f whole * h i ≤ f i)
    (f : ι → ℝ) (hf : C.Mem f) (funit : f whole = 1) : f = h := by
  have heq := unique_of_uniform_minorization C h hh hunit c hc minor f hf
  simpa only [funit, one_mul] using heq

end CollatzInvariantCone
