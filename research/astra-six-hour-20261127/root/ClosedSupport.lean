import Mathlib.Topology.Order.LeftRightNhds
import Mathlib.Basic.Real.Basic
import Mathlib.Data.Finset.Max
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Linarith

/-!
The topological core of CLOSED_CORRECTION_SUPPORT.md.  The analytic work
supplies a null exceptional set outside which only finitely many physical
edges cross a phase.  This module proves, with that hypothesis explicit, that
the closed range outside the exceptional set is countable.  It does not assert
the singularity or the local mass estimate of the Collatz inverse measure.
-/

namespace Collatz.SixHour.ClosedSupport

open Set Filter Topology

variable {V : Type*}

/-- The analytic density estimate can be supplied as this scalar vanishing
condition; a crossing has a fixed positive normalized local mass. -/
theorem finite_crossings_of_vanishing_mass (T : ℕ → ℕ) (f : ℕ → ℝ)
    (θ c : ℝ) (d : ℕ → ℝ) (hc : 0 < c)
    (hvanish : ∀ ε > 0, ∃ N, ∀ n ≥ N, d n < ε)
    (hmass : ∀ n, f n < θ ∧ θ ≤ f (T n) → c ≤ d n) :
    {n | f n < θ ∧ θ ≤ f (T n)}.Finite := by
  obtain ⟨N, hN⟩ := hvanish c hc
  apply (Finset.range N).finite_toSet.subset
  intro n hn
  rw [Finset.mem_coe, Finset.mem_range]
  by_contra h
  exact (not_le_of_gt (hN n (Nat.le_of_not_gt h)) (hmass n hn))

theorem exists_crossing (T : V → V) (f : V → ℝ)
    (hmono : ∀ x, f x ≤ f (T x)) {x : V} {θ : ℝ}
    (hx : f x < θ) {n : ℕ} (hn : θ ≤ f (T^[n] x)) :
    ∃ y, f x ≤ f y ∧ f y < θ ∧ θ ≤ f (T y) := by
  induction n generalizing x with
  | zero =>
      simp only [Function.iterate_zero, id_eq] at hn
      exact (not_le_of_gt hx hn).elim
  | succ n ih =>
      by_cases hnext : θ ≤ f (T x)
      · exact ⟨x, le_rfl, hx, hnext⟩
      · have hn' : θ ≤ f (T^[n] (T x)) := by
          simpa only [Function.iterate_succ_apply] using hn
        obtain ⟨y, hy, hyt, hty⟩ := ih (lt_of_not_ge hnext) hn'
        exact ⟨y, (hmono x).trans hy, hyt, hty⟩

theorem finite_crossing_gap (T : V → V) (f : V → ℝ) (θ : ℝ)
    (hmono : ∀ x, f x ≤ f (T x))
    (hfuture : ∀ x, ∃ n, θ ≤ f (T^[n] x))
    (hfinite : {x | f x < θ ∧ θ ≤ f (T x)}.Finite) :
    ∃ M < θ, ∀ x, f x < θ → f x ≤ M := by
  classical
  let s := hfinite.toFinset
  have hs (x : V) : x ∈ s ↔ f x < θ ∧ θ ≤ f (T x) := by
    simp [s]
  by_cases hne : s.Nonempty
  · obtain ⟨y, hy, hmax⟩ := Finset.exists_max_image s f hne
    refine ⟨f y, ((hs y).mp hy).1, ?_⟩
    intro x hx
    obtain ⟨n, hn⟩ := hfuture x
    obtain ⟨z, hxz, hzt, htz⟩ := exists_crossing T f hmono hx hn
    exact hxz.trans (hmax z ((hs z).mpr ⟨hzt, htz⟩))
  · refine ⟨θ - 1, by linarith, ?_⟩
    intro x hx
    obtain ⟨n, hn⟩ := hfuture x
    obtain ⟨z, _, hzt, htz⟩ := exists_crossing T f hmono hx hn
    exact (hne ⟨z, (hs z).mpr ⟨hzt, htz⟩⟩).elim

variable [TopologicalSpace ℝ] [OrderTopology ℝ]

theorem closure_gap (f : V → ℝ) {M θ : ℝ}
    (hgap : ∀ x, f x < θ → f x ≤ M) :
    closure (range f) ⊆ Iic M ∪ Ici θ := by
  apply closure_minimal _ (isClosed_Iic.union isClosed_Ici)
  rintro _ ⟨x, rfl⟩
  by_cases hx : f x < θ
  · exact Or.inl (hgap x hx)
  · exact Or.inr (le_of_not_gt hx)

theorem finite_crossing_isolated_left (T : V → V) (f : V → ℝ) (θ : ℝ)
    (hmono : ∀ x, f x ≤ f (T x))
    (hfuture : ∀ x, ∃ n, θ ≤ f (T^[n] x))
    (hfinite : {x | f x < θ ∧ θ ≤ f (T x)}.Finite) :
    𝓝[closure (range f) ∩ Iio θ] θ = ⊥ := by
  obtain ⟨M, hM, hgap⟩ := finite_crossing_gap T f θ hmono hfuture hfinite
  apply empty_mem_iff_bot.mp
  rw [mem_nhdsWithin_iff_exists_mem_nhds_inter]
  refine ⟨Ioi M, isOpen_Ioi.mem_nhds hM, ?_⟩
  rintro z ⟨hzM, hzK, hzθ⟩
  rcases closure_gap f hgap hzK with h | h
  · exact (not_le_of_gt (show M < z from hzM) (show z ≤ M from h)).elim
  · exact (not_le_of_gt (show z < θ from hzθ) (show θ ≤ z from h)).elim

variable [SecondCountableTopology ℝ]

/-- A null exceptional set can be supplied by differentiation of a singular
measure.  Countability here is stronger than the remaining measure-zero step. -/
theorem closed_range_countable_outside (T : V → V) (f : V → ℝ) (E : Set ℝ)
    (hmono : ∀ x, f x ≤ f (T x))
    (hrange : ∀ x, 0 ≤ f x ∧ f x ≤ 1)
    (hfuture : ∀ x, ∀ θ < 1, ∃ n, θ ≤ f (T^[n] x))
    (hfinite : ∀ θ ∈ Ioo (0 : ℝ) 1, θ ∉ E →
      {x | f x < θ ∧ θ ≤ f (T x)}.Finite) :
    (closure (range f) \ E).Countable := by
  have hK : closure (range f) ⊆ Icc (0 : ℝ) 1 := by
    apply closure_minimal _ isClosed_Icc
    rintro _ ⟨x, rfl⟩
    exact hrange x
  have hcount : {θ ∈ closure (range f) |
      𝓝[closure (range f) ∩ Iio θ] θ = ⊥}.Countable :=
    countable_setOfPred_isolated_left_within
  apply (hcount.union (Set.toFinite ({0, 1} : Set ℝ)).countable).mono
  intro θ hθ
  by_cases hzero : θ = 0
  · exact Or.inr (by simp [hzero])
  by_cases hone : θ = 1
  · exact Or.inr (by simp [hone])
  have hinterval : θ ∈ Ioo (0 : ℝ) 1 := by
    obtain ⟨hl, hu⟩ := hK hθ.1
    exact ⟨lt_of_le_of_ne hl (Ne.symm hzero), lt_of_le_of_ne hu hone⟩
  refine Or.inl ⟨hθ.1, ?_⟩
  exact finite_crossing_isolated_left T f θ hmono
    (fun x => hfuture x θ hinterval.2) (hfinite θ hinterval hθ.2)

/-- Complete abstract assembly.  The lower local mass and its vanishing
outside `E` remain explicit analytic premises. -/
theorem closed_range_of_singular_current (T : ℕ → ℕ) (f : ℕ → ℝ)
    (E : Set ℝ) (d : ℝ → ℕ → ℝ)
    (hmono : ∀ x, f x ≤ f (T x))
    (hrange : ∀ x, 0 ≤ f x ∧ f x ≤ 1)
    (hfuture : ∀ x, ∀ θ < 1, ∃ n, θ ≤ f (T^[n] x))
    (hvanish : ∀ θ ∈ Ioo (0 : ℝ) 1, θ ∉ E →
      ∀ ε > 0, ∃ N, ∀ n ≥ N, d θ n < ε)
    (hmass : ∀ θ ∈ Ioo (0 : ℝ) 1, ∃ c > 0,
      ∀ n, f n < θ ∧ θ ≤ f (T n) → c ≤ d θ n) :
    (closure (range f) \ E).Countable := by
  apply closed_range_countable_outside T f E hmono hrange hfuture
  intro θ hθ hE
  obtain ⟨c, hc, hcross⟩ := hmass θ hθ
  exact finite_crossings_of_vanishing_mass T f θ c (d θ) hc
    (hvanish θ hθ hE) hcross

end Collatz.SixHour.ClosedSupport
