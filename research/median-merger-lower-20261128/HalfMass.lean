import MedianMerger
import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.IntervalCases

open Collatz.PoweredAffine
open scoped BigOperators

namespace Collatz.MedianLower

def FirstOne (n t : ℕ) : Prop :=
  orbit n t = 1 ∧ ∀ j < t, orbit n j ≠ 1

def Active (n h : ℕ) : Prop := orbit n h = 1 ∨ orbit n h = 2

theorem orbit_after (n t u : ℕ) : orbit n (t+u) = orbit (orbit n t) u := by
  induction t generalizing n with
  | zero => simp [orbit]
  | succ t ih => simpa only [Nat.succ_add, orbit] using ih (step n)

private theorem keep_active {n h : ℕ} (h₀ : Active n h) (k : ℕ) : Active n (h+k) := by
  induction k with
  | zero => simpa using h₀
  | succ k ih =>
    unfold Active at *
    rw [Nat.add_succ, Collatz.MedianMerger.orbit_last]
    rcases ih with h1 | h2
    · exact Or.inr (by rw [h1]; rfl)
    · exact Or.inl (by rw [h2]; rfl)

theorem active_iff_hit_by_next (n h : ℕ) :
    Active n h ↔ ∃ t ≤ h+1, orbit n t = 1 := by
  constructor
  · rintro (h1 | h2)
    · exact ⟨h, by omega, h1⟩
    · exact ⟨h+1, le_rfl, by rw [Collatz.MedianMerger.orbit_last, h2]; rfl⟩
  · rintro ⟨t, ht, hit⟩
    by_cases le : t ≤ h
    · obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le le
      exact keep_active (Or.inl hit : Active n t) k
    · obtain rfl : t = h+1 := by omega
      rw [Collatz.MedianMerger.orbit_last] at hit
      right
      unfold step at hit
      split_ifs at hit <;> omega

theorem two_step_cycle {n : ℕ} (positive : 0 < n) :
    orbit n 2 = n ↔ n = 1 ∨ n = 2 := by
  change step (step n) = n ↔ _
  unfold step
  split_ifs <;> omega

def oddDepartures (n : ℕ) : ℕ → ℕ
  | 0 => 0
  | w+1 => n % 2 + oddDepartures (step n) w

private theorem shifted_step (q r : ℕ) :
    step (2*q+r) = 3^(r%2)*q + step r := by
  by_cases h : r%2 = 0
  · simp [step, h]
    omega
  · have h' : r%2 = 1 := by omega
    simp [step, h']
    omega

/-- The block certificate keeps the exact image of each residue. -/
theorem exact_block (w q r : ℕ) :
    orbit (2^w*q+r) w = 3^(oddDepartures r w)*q + orbit r w := by
  induction w generalizing q r with
  | zero => simp [orbit, oddDepartures]
  | succ w ih =>
    rw [show 2^(w+1)*q+r = 2*(2^w*q)+r by ring, orbit, shifted_step]
    rw [show 3^(r%2)*(2^w*q)+step r = 2^w*(3^(r%2)*q)+step r by ring, ih]
    simp only [oddDepartures, orbit, pow_add]
    ring

theorem descent_bound (n w : ℕ) : n ≤ 2^w * orbit n w := by
  induction w generalizing n with
  | zero => simp [orbit]
  | succ w ih =>
    have h : n ≤ 2 * step n := by unfold step; split_ifs <;> omega
    calc
      n ≤ 2 * step n := h
      _ ≤ 2 * (2^w * orbit (step n) w) := Nat.mul_le_mul_left _ (ih (step n))
      _ = _ := by simp only [orbit, pow_succ]; ring

theorem no_early_one {n w : ℕ} (big : 2^w < n) :
    ∀ j ≤ w, orbit n j ≠ 1 := by
  intro j hj h1
  have hb := descent_bound n j
  rw [h1, Nat.mul_one] at hb
  have hp : (2:ℕ)^j ≤ 2^w := Nat.pow_le_pow_right (by decide) hj
  omega

private theorem embed_three {n : ℕ} (odd : n%2 = 1) :
    orbit (4*n+1) 3 = step n := by
  change step (step (step (4*n+1))) = step n
  unfold step
  split_ifs <;> omega

/-- The unit replacement used between two inverse stages preserves the
first visit to 1, and adds exactly two shortcut dates. -/
theorem embed_first_one {n t : ℕ} (odd : n%2 = 1) (large : 1 < n)
    (hit : FirstOne n t) : FirstOne (4*n+1) (t+2) := by
  have ht : 0 < t := by
    by_contra! z
    obtain rfl : t = 0 := by omega
    have hn : n = 1 := hit.1
    omega
  obtain ⟨u, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : t ≠ 0)
  have shift (j : ℕ) : orbit (4*n+1) (3+j) = orbit n (j+1) := by
    rw [orbit_after, embed_three odd]
    rfl
  refine ⟨by rw [show u+1+2 = 3+u by omega, shift]; exact hit.1, ?_⟩
  intro j hj
  by_cases early : j < 3
  · interval_cases j <;> simp only [orbit, step] <;> (try split_ifs) <;> omega
  · obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le (show 3 ≤ j by omega)
    rw [shift]
    exact hit.2 _ (by omega)

def unitLift (n : ℕ) : ℕ := if n%3 = 0 then 4*n+1 else n

theorem unitLift_mod (n : ℕ) : unitLift n % 3 ≠ 0 := by
  unfold unitLift
  split_ifs <;> omega

theorem unitLift_injective_in_band {Y a b : ℕ} (ha : a ≤ Y) (hb : b ≤ Y)
    (hla : Y < 4*a) (hlb : Y < 4*b) (eq : unitLift a = unitLift b) : a = b := by
  unfold unitLift at eq
  split_ifs at eq <;> omega

/-- Distinct first-landing labels give disjoint sets of ordinary sources. -/
theorem distinct_label_count (sources targets : Finset ℕ) (tag : ℕ → ℕ) (b : ℕ)
    (each : ∀ a ∈ targets, b ≤ (sources.filter (fun n => tag n = a)).card) :
    targets.card * b ≤ (sources.filter (fun n => tag n ∈ targets)).card := by
  rw [← Finset.sum_card_fiberwise_eq_card_filter]
  calc
    targets.card * b = ∑ _a ∈ targets, b := by simp
    _ ≤ _ := Finset.sum_le_sum each

theorem retained_mass (m : ℕ → ℝ) (c : ℝ) (hc : 0 ≤ c)
    (base : 1 ≤ m 0) (link : ∀ i, c * m i ≤ m (i+1)) (k : ℕ) :
    c^k ≤ m k := by
  induction k with
  | zero => simpa using base
  | succ k ih =>
    rw [pow_succ, mul_comm]
    exact le_trans (mul_le_mul_of_nonneg_left ih hc) (link k)

/-- The other genuine cycles can consume at most a twelfth of the
squared mass outside the basin of 1 at the median. -/
theorem collision_gap (d r : ℝ) (hr : 0 ≤ r) (hcap : r ≤ (1-d)^2/12) :
    (1-d)*(1+5*d)/24 ≤ 1/8-(d^2/8+r) ∧
    1/8-(d^2/8+r) ≤ (1-d)*(1+d)/8 := by
  constructor <;> nlinarith

/-- Successful nearby samples have identical first-hit dates when the two
prefixes are too high to have visited 1. -/
theorem first_one_after_fusion {n m t : ℕ} (meet : orbit n t = orbit m t)
    (hn : 2^t < n) (hm : 2^t < m) (h : ℕ) : FirstOne n h ↔ FirstOne m h := by
  have same (j : ℕ) : orbit n j = 1 ↔ orbit m j = 1 := by
    by_cases early : j ≤ t
    · exact iff_of_false (no_early_one hn j early) (no_early_one hm j early)
    · obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le (show t ≤ j by omega)
      rw [orbit_after, orbit_after, meet]
  constructor
  · rintro ⟨v, before⟩
    exact ⟨(same h).mp v, fun j lt hj => before j lt ((same j).mpr hj)⟩
  · rintro ⟨v, before⟩
    exact ⟨(same h).mpr v, fun j lt hj => before j lt ((same j).mp hj)⟩

/-- The fraction of failing choices is charged once for a thin source
window and at most failures divided by L in each well-supplied window. -/
theorem window_failure_budget (starts : Finset ℕ) (choices fails : ℕ → ℝ) {L : ℝ}
    (hL : 0 < L) (hc : ∀ n ∈ starts, 0 < choices n)
    (hf : ∀ n ∈ starts, 0 ≤ fails n ∧ fails n ≤ choices n) :
    ∑ n ∈ starts, fails n / choices n ≤
      (∑ n ∈ starts, if choices n < L then (1:ℝ) else 0) +
      ∑ n ∈ starts, fails n / L := by
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_le_sum
  intro n hn
  obtain ⟨pos, bound⟩ := hf n hn
  by_cases small : choices n < L
  · rw [ite_eq_left small]
    have h₁ : fails n / choices n ≤ 1 := (div_le_one (hc n hn)).mpr bound
    exact le_trans h₁ (le_add_of_nonneg_right (div_nonneg pos hL.le))
  · rw [ite_eq_right small, zero_add]
    exact div_le_div_of_nonneg_left pos hL (le_of_not_gt small)

/-- The octave receipt is sufficient at every intermediate integer cutoff
when the total squared tie cohorts and the two initial diagonals are paid. -/
theorem gate_octave_certificate {E x C G m S : ℝ} (hx : 0 < x) (hle : x ≤ E)
    (half : E ≤ 2*x) (hm : 0 ≤ m) (hs : 0 ≤ S)
    (mass : 3*x+m ≤ 5*C) (energy : C^2 ≤ 2*(G+S+2))
    (cert : 7*E^2+200*(S+2) < (3*E+m)^2) : 7*x^2 < 50*G := by
  have hE : 0 < E := lt_of_lt_of_le hx hle
  have base : (3*E+m)*x ≤ 5*E*C := by
    nlinarith [mul_nonneg (sub_nonneg.mpr mass) hE.le,
      mul_nonneg hm (sub_nonneg.mpr hle)]
  have square := pow_le_pow_left₀ (show 0 ≤ (3*E+m)*x by positivity) base 2
  have bound := pow_le_pow_left₀ hE.le half 2
  by_contra! neg
  have upper := mul_le_mul_of_nonneg_right neg (sq_nonneg E)
  nlinarith [mul_nonneg (sub_nonneg.mpr energy) (show 0 ≤ 25*E^2 by positivity),
    mul_nonneg (sub_nonneg.mpr bound) (show 0 ≤ 50*(S+2) by positivity),
    mul_pos (sub_pos.mpr cert) (sq_pos_of_pos hx)]

end Collatz.MedianLower
