import PotentialAssembly
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-!
An exact rational finite energy for ordinary trajectories.  The final theorem
retains both a uniform finite bound and vanishing at large ordinary targets as
explicit premises. Neither premise is established by this module.
-/

namespace Collatz.SixHour.RationalEnergy

open Collatz.SixHour.PotentialAssembly

def edgeWeight (n : ℕ) : ℚ :=
  if n < 13 then 1 / 4 else 1 + 1 / (32 * (n : ℚ)^2)

def pathWeight (k n : ℕ) : ℚ :=
  match k with
  | 0 => 1
  | k + 1 => pathWeight k n * edgeWeight (syr^[k] n)

def finiteEnergy (K H y : ℕ) : ℚ :=
  ∑ k ∈ Finset.range (K+1), ∑ x ∈ Finset.range (H+1),
    if 0 < x ∧ x % 2 = 1 ∧ syr^[k] x = y
      then pathWeight k x / (x : ℚ)^3 else 0

theorem edgeWeight_positive (n : ℕ) : 0 < edgeWeight n := by
  unfold edgeWeight
  split
  · norm_num
  · positivity

theorem edgeWeight_high {n : ℕ} (hn : 13 ≤ n) : 1 ≤ edgeWeight n := by
  rw [edgeWeight, ite_eq_right (by omega)]
  have : (0 : ℚ) ≤ 1 / (32 * (n : ℚ)^2) := by positivity
  linarith

theorem pathWeight_positive (k n : ℕ) : 0 < pathWeight k n := by
  induction k with
  | zero => norm_num [pathWeight]
  | succ k ih => exact mul_pos ih (edgeWeight_positive _)

theorem high_path_weight {n : ℕ} (high : ∀ k, 13 ≤ syr^[k] n) (k : ℕ) :
    1 ≤ pathWeight k n := by
  induction k with
  | zero => norm_num [pathWeight]
  | succ k ih =>
    change 1 ≤ pathWeight k n * edgeWeight (syr^[k] n)
    nlinarith [edgeWeight_high (high k)]

theorem finiteEnergy_nonnegative (K H y : ℕ) : 0 ≤ finiteEnergy K H y := by
  apply Finset.sum_nonneg
  intro k _
  apply Finset.sum_nonneg
  intro x _
  split
  · exact div_nonneg (le_of_lt (pathWeight_positive _ _)) (by positivity)
  · exact le_rfl

theorem path_in_finiteEnergy {n : ℕ} (hn : 0 < n) (ho : n % 2 = 1) (k : ℕ) :
    pathWeight k n / (n : ℚ)^3 ≤ finiteEnergy k n (syr^[k] n) := by
  have nn (j x : ℕ) : (0 : ℚ) ≤
      if 0 < x ∧ x % 2 = 1 ∧ syr^[j] x = syr^[k] n
        then pathWeight j x / (x : ℚ)^3 else 0 := by
    split
    · exact div_nonneg (le_of_lt (pathWeight_positive _ _)) (by positivity)
    · exact le_rfl
  have inner := Finset.single_le_sum
    (fun x (_ : x ∈ Finset.range (n+1)) => nn k x)
    (show n ∈ Finset.range (n+1) by simp)
  have outer : (∑ x ∈ Finset.range (n+1),
      if 0 < x ∧ x % 2 = 1 ∧ syr^[k] x = syr^[k] n
        then pathWeight k x / (x : ℚ)^3 else 0) ≤
      finiteEnergy k n (syr^[k] n) := Finset.single_le_sum
    (fun j (_ : j ∈ Finset.range (k+1)) =>
      Finset.sum_nonneg (fun x (_ : x ∈ Finset.range (n+1)) => nn j x))
    (show k ∈ Finset.range (k+1) by simp)
  have hi : pathWeight k n / (n : ℚ)^3 ≤ (∑ x ∈ Finset.range (n+1),
      if 0 < x ∧ x % 2 = 1 ∧ syr^[k] x = syr^[k] n
        then pathWeight k x / (x : ℚ)^3 else 0) := by
    simpa only [hn, ho, and_self, ite_true] using inner
  exact hi.trans outer

/-- Both assertions are open on all ordinary targets. -/
def EnergyCriterion : Prop :=
  (∀ K H y : ℕ, finiteEnergy K H y ≤ 8) ∧
  (∀ ε : ℚ, 0 < ε → ∃ Y : ℕ, ∀ K H y : ℕ,
    Y ≤ y → finiteEnergy K H y ≤ ε)

theorem bounded_additive_growth_impossible (v : ℕ → ℚ) (M δ : ℚ)
    (hd : 0 < δ) (hp : 0 ≤ v 0) (hb : ∀ k, v k ≤ M)
    (hs : ∀ k, v k + δ ≤ v (k+1)) : False := by
  have grow (k : ℕ) : (k : ℚ) * δ ≤ v k := by
    induction k with
    | zero => simpa using hp
    | succ k ih =>
      push_cast
      linarith [hs k]
  obtain ⟨k, hk⟩ := exists_nat_gt (M / δ)
  have hm : M < (k : ℚ) * δ := (div_lt_iff₀ hd).mp hk
  linarith [grow k, hb k]

theorem criterion_reaches_small (criterion : EnergyCriterion)
    {n : ℕ} (hn : 0 < n) (ho : n % 2 = 1) :
    ∃ k, syr^[k] n < 13 := by
  by_contra h
  have high (k : ℕ) : 13 ≤ syr^[k] n := by
    by_contra hk
    exact h ⟨k, by omega⟩
  have hnq : (0 : ℚ) < n := by exact_mod_cast hn
  have hn3 : (0 : ℚ) < (n : ℚ)^3 := by positivity
  have lower (k : ℕ) : 1 / (n : ℚ)^3 ≤ finiteEnergy k n (syr^[k] n) :=
    (div_le_div_of_nonneg_right (high_path_weight high k) (le_of_lt hn3)).trans
      (path_in_finiteEnergy hn ho k)
  obtain ⟨Y, hY⟩ := criterion.2 (1 / (2 * (n : ℚ)^3)) (by positivity)
  have bounded (k : ℕ) : syr^[k] n < Y := by
    by_contra hk
    have hu := hY k n (syr^[k] n) (by omega)
    have hl := lower k
    have hc : (1 : ℚ) / (2 * (n : ℚ)^3) < 1 / (n : ℚ)^3 := by
      apply one_div_lt_one_div_of_lt hn3
      linarith
    linarith
  have Ypos : 0 < Y := by have h0 := bounded 0; simp only [Function.iterate_zero_apply] at h0; omega
  have Yq : (0 : ℚ) < Y := by exact_mod_cast Ypos
  let δ : ℚ := 1 / (32 * (Y : ℚ)^2)
  have δpos : 0 < δ := by dsimp [δ]; positivity
  have margin (k : ℕ) : 1 + δ ≤ edgeWeight (syr^[k] n) := by
    rw [edgeWeight, ite_eq_right (by have := high k; omega)]
    have hx : (0 : ℚ) < (syr^[k] n : ℚ) := by
      exact_mod_cast (show 0 < syr^[k] n by have := high k; omega)
    have hxY : (syr^[k] n : ℚ) ≤ (Y : ℚ) := by exact_mod_cast le_of_lt (bounded k)
    have hs := pow_le_pow_left₀ (le_of_lt hx) hxY 2
    have hd : 0 < 32 * (syr^[k] n : ℚ)^2 := by positivity
    have hr : δ ≤ 1 / (32 * (syr^[k] n : ℚ)^2) := by
      dsimp [δ]
      apply one_div_le_one_div_of_le hd
      linarith
    linarith
  have upper (k : ℕ) : pathWeight k n ≤ 8 * (n : ℚ)^3 := by
    apply (div_le_iff₀ hn3).mp
    exact (path_in_finiteEnergy hn ho k).trans (criterion.1 k n (syr^[k] n))
  apply bounded_additive_growth_impossible (fun k => pathWeight k n)
    (8 * (n : ℚ)^3) δ δpos (by norm_num [pathWeight]) upper
  intro k
  change pathWeight k n + δ ≤ pathWeight k n * edgeWeight (syr^[k] n)
  have hp := high_path_weight high k
  have hm := margin k
  nlinarith

/-- Full ordinary Collatz convergence, conditional on the displayed finite
rational bound and uniform decay assertion. -/
theorem energy_criterion_implies_collatz (criterion : EnergyCriterion) : Universal := by
  intro n hn
  have hp := oddPart_positive hn
  have ho := oddPart_odd hn
  obtain ⟨k, hk⟩ := criterion_reaches_small criterion hp ho
  have hpos : 0 < syr^[k] (oddPart n) := by
    cases k with
    | zero => exact hp
    | succ k => rw [Function.iterate_succ_apply']; exact syr_positive _
  have hodd : syr^[k] (oddPart n) % 2 = 1 := by
    cases k with
    | zero => exact ho
    | succ k => rw [Function.iterate_succ_apply']; exact syr_odd _
  exact reaches_trans (reaches_oddPart n)
    (reaches_trans (reaches_syr_iterate ho k) (small_odds_reach_one hpos hodd hk))

end Collatz.SixHour.RationalEnergy
