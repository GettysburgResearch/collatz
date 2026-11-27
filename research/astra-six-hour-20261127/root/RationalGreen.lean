import PotentialAssembly
import Mathlib.Tactic.FieldSimp
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-!
An exact rational Green weight. The mean multiplier on the ternary space is
134/135, so the infinite positive Green series has Haar integral 135.
Only the finite rational arithmetic and ordinary path assembly are formalized
here. No ordinary-point bound for that series is asserted.
-/

namespace Collatz.SixHour.RationalGreen

open Collatz.SixHour.PotentialAssembly

def coefficient (e : ℕ) : ℚ := (134 / 25) * (5 / 14) ^ e

def gap (x : ℕ) : ℕ := (3 * x + 1).factorization 2

def pathWeight : ℕ → ℕ → ℚ
  | 0, _ => 1
  | k + 1, x => coefficient (gap x) * pathWeight k (syr x)

theorem exact_mean : (134 / 25 : ℚ) * (5 / 14) / (3 * (1 - 5 / 14)) = 134 / 135 := by
  norm_num

theorem exact_integral_value : (1 : ℚ) / (1 - 134 / 135) = 135 := by
  norm_num

theorem coefficient_positive (e : ℕ) : 0 < coefficient e := by
  unfold coefficient
  positivity

theorem coefficient_scaled (e : ℕ) :
    (coefficient e)^2 * ((2 : ℚ)^e)^3 = (134 / 25 : ℚ)^2 * (50 / 49)^e := by
  unfold coefficient
  induction e with
  | zero => norm_num
  | succ e ih =>
    rw [pow_succ (5 / 14 : ℚ) e, pow_succ (2 : ℚ) e, pow_succ (50 / 49 : ℚ) e]
    calc
      ((134 / 25 : ℚ) * ((5 / 14)^e * (5 / 14)))^2 * ((2 : ℚ)^e * 2)^3
          = (((134 / 25 : ℚ) * (5 / 14)^e)^2 * ((2 : ℚ)^e)^3) * (50 / 49) := by ring
      _ = (134 / 25 : ℚ)^2 * (50 / 49)^e * (50 / 49) := by rw [ih]
      _ = (134 / 25 : ℚ)^2 * ((50 / 49)^e * (50 / 49)) := by ring

theorem coefficient_dominates {e : ℕ} (he : 1 ≤ e) :
    (25 / 24 : ℚ)^2 * 27 ≤ (coefficient e)^2 * ((2 : ℚ)^e)^3 := by
  rw [coefficient_scaled]
  have h := pow_le_pow_right₀ (show (1 : ℚ) ≤ 50 / 49 by norm_num) he
  norm_num only [pow_one] at h
  nlinarith

theorem gap_positive {x : ℕ} (hx : x % 2 = 1) : 1 ≤ gap x := by
  apply (Nat.Prime.dvd_iff_one_le_factorization Nat.prime_two (by omega)).mp
  omega

theorem actual_edge (x : ℕ) : 2 ^ gap x * syr x = 3 * x + 1 :=
  Nat.ordProj_mul_ordCompl_eq_self (3 * x + 1) 2

theorem pathWeight_positive (k x : ℕ) : 0 < pathWeight k x := by
  induction k generalizing x with
  | zero => norm_num [pathWeight]
  | succ k ih => exact mul_pos (coefficient_positive _) (ih _)

theorem pathWeight_succ_last (k x : ℕ) :
    pathWeight (k + 1) x = pathWeight k x * coefficient (gap (syr^[k] x)) := by
  induction k generalizing x with
  | zero => simp [pathWeight]
  | succ k ih =>
    change coefficient (gap x) * pathWeight (k+1) (syr x) =
      (coefficient (gap x) * pathWeight k (syr x)) * coefficient (gap (syr^[k+1] x))
    rw [ih, Function.iterate_succ_apply]
    ring

theorem normalized_edge {e : ℕ} {x y : ℚ} (he : 1 ≤ e)
    (hx : 13 ≤ x) (hrel : (2 : ℚ)^e * y = 3 * x + 1) :
    (201 / 200 : ℚ) * y^3 ≤ (coefficient e)^2 * x^3 := by
  have hm : (201 / 200 : ℚ) ≤ (25 / 24 : ℚ)^2 * (3*x/(3*x+1))^3 := by
    have hr : (39/40 : ℚ) ≤ 3*x/(3*x+1) := by
      apply (le_div_iff₀ (show 0 < 3*x+1 by linarith)).2
      linarith
    have hp := pow_le_pow_left₀ (show (0:ℚ)≤39/40 by norm_num) hr 3
    nlinarith [hp]
  have hd : 0 < (3*x+1)^3 := by positivity
  have hc : (201/200 : ℚ) * (3*x+1)^3 ≤ (25/24 : ℚ)^2 * (3*x)^3 := by
    apply (le_div_iff₀ hd).mp
    calc
      (201/200 : ℚ) ≤ (25/24 : ℚ)^2 * (3*x/(3*x+1))^3 := hm
      _ = ((25/24 : ℚ)^2 * (3*x)^3)/(3*x+1)^3 := by
        rw [div_pow (3*x) (3*x+1) 3]
        ring
  have hcoef := mul_le_mul_of_nonneg_right (coefficient_dominates he)
    (show (0:ℚ) ≤ x^3 by positivity)
  apply le_of_mul_le_mul_left (a := ((2:ℚ)^e)^3) (a0 := by positivity)
  calc
    ((2:ℚ)^e)^3 * ((201/200:ℚ)*y^3)
        = (201/200:ℚ)*((2:ℚ)^e*y)^3 := by ring
    _ = (201/200:ℚ)*(3*x+1)^3 := by rw [hrel]
    _ ≤ (25/24:ℚ)^2*(3*x)^3 := hc
    _ ≤ ((2:ℚ)^e)^3*((coefficient e)^2*x^3) := by nlinarith [hcoef]

def finiteGreen (K H y : ℕ) : ℚ :=
  ∑ k ∈ Finset.range (K + 1), ∑ x ∈ Finset.range (H + 1),
    if 0 < x ∧ x % 2 = 1 ∧ syr^[k] x = y then pathWeight k x else 0

theorem path_in_finiteGreen {x : ℕ} (hx : 0 < x) (ho : x % 2 = 1) (k : ℕ) :
    pathWeight k x ≤ finiteGreen k x (syr^[k] x) := by
  have nonneg (j z : ℕ) : (0 : ℚ) ≤
      if 0 < z ∧ z % 2 = 1 ∧ syr^[j] z = syr^[k] x then pathWeight j z else 0 := by
    split
    · exact le_of_lt (pathWeight_positive _ _)
    · exact le_rfl
  have inner := Finset.single_le_sum (fun z (_ : z ∈ Finset.range (x+1)) => nonneg k z)
    (show x ∈ Finset.range (x+1) by simp)
  have outer : (∑ z ∈ Finset.range (x+1),
      if 0 < z ∧ z % 2 = 1 ∧ syr^[k] z = syr^[k] x then pathWeight k z else 0) ≤
      finiteGreen k x (syr^[k] x) := Finset.single_le_sum
    (fun j (_ : j ∈ Finset.range (k+1)) =>
      Finset.sum_nonneg (fun z (_ : z ∈ Finset.range (x+1)) => nonneg j z))
    (show k ∈ Finset.range (k+1) by simp)
  have hi : pathWeight k x ≤ (∑ z ∈ Finset.range (x+1),
      if 0 < z ∧ z % 2 = 1 ∧ syr^[k] z = syr^[k] x then pathWeight k z else 0) := by
    simpa only [hx, ho, and_self, ite_true] using inner
  exact hi.trans outer

/-- The remaining assertion is an upper bound on completely explicit finite
rational sums.  No witness for this assertion is supplied in this packet. -/
def FiniteGreenBound : Prop := ∃ C : ℚ, ∀ K H y : ℕ,
  0 < y → y % 2 = 1 → (finiteGreen K H y)^2 ≤ C * (y : ℚ)^3

theorem bounded_path_reaches_small {n : ℕ} (hn : 0 < n) (ho : n % 2 = 1)
    (M : ℚ) (hb : ∀ k, (pathWeight k n)^2 ≤ M * (syr^[k] n : ℚ)^3) :
    ∃ k, syr^[k] n < 13 := by
  by_contra h
  have high (k : ℕ) : 13 ≤ syr^[k] n := by
    by_contra hk
    exact h ⟨k, by omega⟩
  have odd (k : ℕ) : syr^[k] n % 2 = 1 := by
    cases k with
    | zero => exact ho
    | succ k => rw [Function.iterate_succ_apply']; exact syr_odd _
  let v : ℕ → ℚ := fun k => (pathWeight k n)^2 / (syr^[k] n : ℚ)^3
  have positive (k : ℕ) : (0 : ℚ) < (syr^[k] n : ℚ)^3 := by
    have : (0 : ℚ) < (syr^[k] n : ℚ) := by exact_mod_cast (show 0 < syr^[k] n by have := high k; omega)
    positivity
  have vpos : 0 < v 0 := by
    dsimp [v, pathWeight]
    have : (0 : ℚ) < n := by exact_mod_cast hn
    positivity
  have vb (k : ℕ) : v k ≤ M := (div_le_iff₀ (positive k)).2 (hb k)
  have vs (k : ℕ) : (201/200 : ℚ) * v k ≤ v (k+1) := by
    have hrel : (2 : ℚ)^(gap (syr^[k] n)) * (syr (syr^[k] n) : ℚ) =
        3 * (syr^[k] n : ℚ) + 1 := by exact_mod_cast actual_edge (syr^[k] n)
    have hm := normalized_edge (gap_positive (odd k))
      (show (13 : ℚ) ≤ (syr^[k] n : ℚ) by exact_mod_cast high k) hrel
    change (201/200 : ℚ) * ((pathWeight k n)^2 / (syr^[k] n : ℚ)^3) ≤
      (pathWeight (k+1) n)^2 / (syr^[k+1] n : ℚ)^3
    rw [pathWeight_succ_last, ← mul_div_assoc]
    apply (div_le_div_iff₀ (positive k) (positive (k+1))).2
    rw [Function.iterate_succ_apply']
    calc
      ((201/200 : ℚ) * (pathWeight k n)^2) * (syr (syr^[k] n) : ℚ)^3
          = (pathWeight k n)^2 * ((201/200 : ℚ) * (syr (syr^[k] n) : ℚ)^3) := by ring
      _ ≤ (pathWeight k n)^2 * ((coefficient (gap (syr^[k] n)))^2 * (syr^[k] n : ℚ)^3) :=
        mul_le_mul_of_nonneg_left hm (sq_nonneg _)
      _ = (pathWeight k n * coefficient (gap (syr^[k] n)))^2 * (syr^[k] n : ℚ)^3 := by ring
  exact bounded_growth_not_infinite (fun k => (v k : ℝ)) (M : ℝ)
    (by exact_mod_cast vpos) (fun k => by exact_mod_cast vb k)
    (fun k => by
      have hc : (((201/200 : ℚ) * v k : ℚ) : ℝ) ≤ (v (k+1) : ℝ) :=
        Rat.cast_le.mpr (vs k)
      norm_num only [Rat.cast_mul, Rat.cast_div, Rat.cast_ofNat] at hc
      exact hc)

/-- A concrete finite-sum proposal, not an unconditional proof. -/
theorem finite_green_bound_implies_collatz (bound : FiniteGreenBound) : Universal := by
  obtain ⟨C, hC⟩ := bound
  intro n hn
  let a := oddPart n
  have ha : 0 < a := oddPart_positive hn
  have hao : a % 2 = 1 := oddPart_odd hn
  have pos (k : ℕ) : 0 < syr^[k] a := by
    cases k with
    | zero => exact ha
    | succ k => rw [Function.iterate_succ_apply']; exact syr_positive _
  have odd (k : ℕ) : syr^[k] a % 2 = 1 := by
    cases k with
    | zero => exact hao
    | succ k => rw [Function.iterate_succ_apply']; exact syr_odd _
  have pathBound (k : ℕ) : (pathWeight k a)^2 ≤ C * (syr^[k] a : ℚ)^3 := by
    have hp := pathWeight_positive k a
    have hi := path_in_finiteGreen ha hao k
    have hu := hC k a (syr^[k] a) (pos k) (odd k)
    nlinarith
  obtain ⟨k, hk⟩ := bounded_path_reaches_small ha hao C pathBound
  exact reaches_trans (reaches_oddPart n)
    (reaches_trans (reaches_syr_iterate hao k) (small_odds_reach_one (pos k) (odd k) hk))

end Collatz.SixHour.RationalGreen
