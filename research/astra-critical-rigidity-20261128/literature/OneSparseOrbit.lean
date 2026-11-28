import AffineOrbit
import Mathlib.Logic.Function.Iterate
import Mathlib.Order.Monotone.Basic

/-!
Exact native arithmetic in the one-orbit divergence calibration. The key
preimage theorem gives the whole predecessor set, not only a density estimate.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.OneSparseOrbit

open Collatz.PoweredAffine

private theorem orbit_next (n t : ℕ) : orbit n (t + 1) = step (orbit n t) := by
  induction t generalizing n with
  | zero => rfl
  | succ t ih => exact ih (step n)

private theorem true_unit_step {n : ℕ} (hu : n % 3 ≠ 0) : step n % 3 ≠ 0 := by
  by_cases h : n % 2 = 0
  · have eqn := even_step h
    omega
  · have eqn := odd_step (show n % 2 = 1 by omega)
    omega

private theorem true_unit_orbit {n : ℕ} (hu : n % 3 ≠ 0) (t : ℕ) :
    orbit n t % 3 ≠ 0 := by
  induction t generalizing n with
  | zero => exact hu
  | succ t ih => exact ih (true_unit_step hu)

/-- Following any actual odd departure, every later true state is a ternary unit. -/
theorem after_odd_departure {n : ℕ} (odd : n % 2 = 1) (t : ℕ) :
    orbit (step n) t % 3 ≠ 0 := by
  have eqn := odd_step odd
  exact true_unit_orbit (by omega) t

private theorem doubled_step (n : ℕ) : step (2 * n) = n := by
  simp [step]

private theorem dyadic_arrival (s v : ℕ) : orbit (2 ^ v * s) v = s := by
  induction v with
  | zero => simp [orbit]
  | succ v ih =>
    rw [pow_succ, show 2 ^ v * 2 * s = 2 * (2 ^ v * s) by ring, orbit, doubled_step]
    exact ih

/-- All true predecessors of any multiple of three, including any selected
positive odd source, lie precisely on its initial halving ray. -/
theorem three_multiple_predecessors {s n : ℕ} (hs : s % 3 = 0) :
    (∃ t, orbit n t = s) ↔ ∃ v, n = 2 ^ v * s := by
  constructor
  · rintro ⟨t, hit⟩
    induction t generalizing n with
    | zero => exact ⟨0, by simpa [orbit] using hit⟩
    | succ t ih =>
      change orbit (step n) t = s at hit
      by_cases even : n % 2 = 0
      · obtain ⟨v, hv⟩ := ih hit
        refine ⟨v + 1, ?_⟩
        calc
          n = 2 * step n := (even_step even).symm
          _ = 2 ^ (v + 1) * s := by rw [hv, pow_succ]; ring
      · have h := after_odd_departure (show n % 2 = 1 by omega) t
        exact False.elim (h (by rw [hit, hs]))
  · rintro ⟨v, rfl⟩
    exact ⟨v, dyadic_arrival s v⟩

/-- The positive index k encodes the odd change source 6k+3. -/
def source (k : ℕ) : ℕ := 6 * k + 3

def nextIndex (k : ℕ) : ℕ := (3 * k + 1) / 2

def indexAt (k : ℕ) : ℕ → ℕ
  | 0 => k
  | t + 1 => nextIndex (indexAt k t)

/-- Exact bounded additive error and genuine growth at each chosen odd source. -/
theorem bounded_spine_step (k : ℕ) (hk : 0 < k) :
    source k % 2 = 1 ∧ source k % 3 = 0 ∧ k < nextIndex k ∧
      ((source (nextIndex k) + 2 = step (source k)) ∨
       (source (nextIndex k) = step (source k) + 1)) := by
  have odd : source k % 2 = 1 := by unfold source; omega
  have eqn := odd_step odd
  unfold source nextIndex at *
  omega

private theorem index_lower (k t : ℕ) (hk : 0 < k) : k + t ≤ indexAt k t := by
  induction t with
  | zero => simp [indexAt]
  | succ t ih =>
    have hg := (bounded_spine_step (indexAt k t) (by omega)).2.2.1
    change k + (t + 1) ≤ nextIndex (indexAt k t)
    omega

/-- If the displayed planted successors are used by the modified rule, they
form one actual diverging orbit, with a lower bound at every finite date. -/
theorem modified_spine_orbit (U : ℕ → ℕ) (k : ℕ) (hk : 0 < k)
    (hedge : ∀ t, U (source (indexAt k t)) = source (indexAt k (t + 1))) (t : ℕ) :
    U^[t] (source k) = source (indexAt k t) ∧
      source k + 6 * t ≤ U^[t] (source k) := by
  have actual (j : ℕ) : U^[j] (source k) = source (indexAt k j) := by
    induction j with
    | zero => rfl
    | succ j ih => rw [Function.iterate_succ_apply', ih, hedge]
  refine ⟨actual t, ?_⟩
  rw [actual t]
  have h := index_lower k t hk
  unfold source
  omega

/-- A source outside all selected dyadic rays follows the entire genuine
prefix up through its first anchor, for any rule with precisely these allowed
locations of change. The unmodified orbit may be arbitrarily long. -/
theorem exact_shared_prefix (U : ℕ → ℕ) (anchor n t : ℕ) (spine : ℕ → Prop)
    (hthree : ∀ s, spine s → s % 3 = 0)
    (hout : ∀ s, spine s → ∀ v : ℕ, n ≠ 2 ^ v * s)
    (hagree : ∀ r, r ≠ anchor → ¬ spine r → U r = step r)
    (hanchor : ∀ j < t, orbit n j ≠ anchor) :
    ∀ j ≤ t, U^[j] n = orbit n j := by
  intro j hj
  induction j with
  | zero => rfl
  | succ j ih =>
    rw [Function.iterate_succ_apply', ih (by omega), orbit_next]
    apply hagree _ (hanchor j (by omega))
    intro bad
    obtain ⟨v, hv⟩ := (three_multiple_predecessors (hthree _ bad)).mp ⟨j, rfl⟩
    exact hout _ bad v hv

end Collatz.OneSparseOrbit
