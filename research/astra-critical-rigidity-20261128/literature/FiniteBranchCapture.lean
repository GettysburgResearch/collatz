import AffineOrbit
import Mathlib.Data.Nat.Find
import Mathlib.Logic.Function.Iterate

/-!
A finite local first-drop test on the actual positive shortcut. A rule which
changes every guarded vertex and sends each changed edge within two steps of a
designated set captures every positive start by its true minimum date plus
three. The analytic estimates and frequency-selection construction are separate.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.FiniteBranchCapture

open Collatz.PoweredAffine

private theorem iterate_eq_orbit (n k : ℕ) : step^[k] n = orbit n k := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => simpa only [Function.iterate_succ_apply, orbit] using ih (step n)

private theorem orbit_next (n k : ℕ) : orbit n (k + 1) = step (orbit n k) := by
  simp only [← iterate_eq_orbit, Function.iterate_succ_apply']

private theorem orbit_from (n t j : ℕ) : orbit (orbit n t) j = orbit n (t + j) := by
  simp only [← iterate_eq_orbit, Nat.add_comm t j, Function.iterate_add_apply]

/-- A decidable test, including all dates from zero to the chosen local horizon. -/
def noSmallerGuard (bound : ℕ → ℕ) (r : ℕ) : Bool :=
  decide (r % 2 = 1 ∧ ∀ j : Fin (bound r + 1), r ≤ orbit r j.val)

/-- Every actual positive integer orbit has a finite date at its global minimum. -/
theorem attained_minimum (n : ℕ) : ∃ t, ∀ k, orbit n t ≤ orbit n k := by
  classical
  have reachable : ∃ y : ℕ, ∃ t : ℕ, orbit n t = y := ⟨n, 0, rfl⟩
  obtain ⟨t, ht⟩ := Nat.find_spec reachable
  refine ⟨t, fun k => ?_⟩
  rw [ht]
  exact Nat.find_min' reachable ⟨k, rfl⟩

/-- The global minimum is an odd source passing every finite first-drop guard. -/
theorem minimum_passes_guard {n t : ℕ} (hn : 0 < n)
    (hmin : ∀ k, orbit n t ≤ orbit n k) (bound : ℕ → ℕ) :
    noSmallerGuard bound (orbit n t) = true := by
  have hp := orbit_positive hn t
  have next := hmin (t + 1)
  rw [orbit_next] at next
  have odd : orbit n t % 2 = 1 := by
    by_contra h
    have even : orbit n t % 2 = 0 := by omega
    have eqn := even_step even
    omega
  apply decide_eq_true
  refine ⟨odd, fun j => ?_⟩
  rw [orbit_from]
  exact hmin _

/-- The first physical disagreement occurs at a source date at most the minimum
date, with equality of both iterates through that source and strict inequality
one step later. -/
theorem first_disagreement_by_minimum {n t : ℕ} (hn : 0 < n)
    (hmin : ∀ k, orbit n t ≤ orbit n k) (bound U : ℕ → ℕ)
    (hguard : ∀ r, noSmallerGuard bound r = true → U r ≠ step r) :
    ∃ z ≤ t, (∀ j ≤ z, U^[j] n = orbit n j) ∧
      (∀ j < z, U (orbit n j) = step (orbit n j)) ∧
      U (orbit n z) ≠ step (orbit n z) ∧ U^[z + 1] n ≠ orbit n (z + 1) := by
  classical
  have changed : ∃ j, U (orbit n j) ≠ step (orbit n j) :=
    ⟨t, hguard _ (minimum_passes_guard hn hmin bound)⟩
  let z := Nat.find changed
  have prior (j : ℕ) (hj : j < z) : U (orbit n j) = step (orbit n j) :=
    not_not.mp (Nat.find_min changed hj)
  have shared (j : ℕ) (hj : j ≤ z) : U^[j] n = orbit n j := by
    induction j with
    | zero => rfl
    | succ j ih =>
      rw [Function.iterate_succ_apply', ih (by omega), orbit_next]
      exact prior j (by omega)
  have different : U (orbit n z) ≠ step (orbit n z) := Nat.find_spec changed
  refine ⟨z, Nat.find_min' changed (hguard _ (minimum_passes_guard hn hmin bound)),
    shared, prior, different, ?_⟩
  rwa [Function.iterate_succ_apply', shared z (by omega), orbit_next]

/-- The actual first date in the designated set differs from the first
disagreement date by an amount in [-1,3]. Local hypotheses are the two-step
route from a changed edge and a forced change at one of the first two sources
from any designated vertex. -/
theorem first_capture_window {n t : ℕ} (hn : 0 < n)
    (hmin : ∀ k, orbit n t ≤ orbit n k) (bound U : ℕ → ℕ)
    (designated : ℕ → Prop)
    (hguard : ∀ r, noSmallerGuard bound r = true → U r ≠ step r)
    (hroute : ∀ r, U r ≠ step r → ∃ i ≤ 2, designated (U^[i] (U r)))
    (hforced : ∀ r, designated r → U r ≠ step r ∨ U (step r) ≠ step (step r)) :
    ∃ z ≤ t, ∃ h, (∀ j ≤ z, U^[j] n = orbit n j) ∧
      U^[z + 1] n ≠ orbit n (z + 1) ∧ designated (U^[h] n) ∧
      (∀ j < h, ¬ designated (U^[j] n)) ∧ z ≤ h + 1 ∧ h ≤ z + 3 := by
  classical
  obtain ⟨z, hzt, shared, prior, different, mismatch⟩ :=
    first_disagreement_by_minimum hn hmin bound U hguard
  obtain ⟨i, hi, hr⟩ := hroute _ different
  have landed : designated (U^[i + (z + 1)] n) := by
    rwa [Function.iterate_add_apply, Function.iterate_succ_apply', shared z le_rfl]
  have somewhere : ∃ k, designated (U^[k] n) := ⟨_, landed⟩
  let h := Nat.find somewhere
  have hlate : h ≤ i + (z + 1) := Nat.find_min' somewhere landed
  have entrance : designated (U^[h] n) := Nat.find_spec somewhere
  refine ⟨z, hzt, h, shared, mismatch, entrance, fun j hj => Nat.find_min somewhere hj,
    ?_, by omega⟩
  by_contra tooEarly
  have hh : h < z := by omega
  rw [shared h hh.le] at entrance
  rcases hforced _ entrance with first | second
  · exact first (prior h hh)
  · have hnext := prior (h + 1) (by omega)
    rw [orbit_next] at hnext
    exact second hnext

end Collatz.FiniteBranchCapture
