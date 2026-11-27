import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Algebra.Order.Archimedean.Real.Basic
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
End-to-end conditional assembly for the ordinary positive potential route.
The positive, bounded potential and its exact edge inequality are PREMISES.
This file does not construct that potential or prove Collatz unconditionally.
The accelerated map is connected explicitly to the usual full Collatz map.
-/

namespace Collatz.SixHour.PotentialAssembly

def full (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else 3 * n + 1

def oddPart (n : ℕ) : ℕ := ordCompl[2] n

def syr (n : ℕ) : ℕ := oddPart (3 * n + 1)

def Reaches (n m : ℕ) : Prop := ∃ k : ℕ, full^[k] n = m

def Universal : Prop := ∀ n : ℕ, 0 < n → Reaches n 1

theorem reaches_trans {a b c : ℕ} (hab : Reaches a b) (hbc : Reaches b c) :
    Reaches a c := by
  obtain ⟨i, hi⟩ := hab
  obtain ⟨j, hj⟩ := hbc
  refine ⟨j + i, ?_⟩
  rw [Function.iterate_add_apply, hi, hj]

theorem full_even (n : ℕ) : full (2 * n) = n := by
  simp [full]

theorem halving_run (e n : ℕ) : full^[e] (2 ^ e * n) = n := by
  induction e with
  | zero => simp
  | succ e ih =>
    rw [pow_succ, show 2 ^ e * 2 * n = 2 * (2 ^ e * n) by ring,
      Function.iterate_succ_apply, full_even, ih]

theorem reaches_oddPart (n : ℕ) : Reaches n (oddPart n) := by
  refine ⟨n.factorization 2, ?_⟩
  have h := halving_run (n.factorization 2) (oddPart n)
  rw [show 2 ^ n.factorization 2 * oddPart n = n from
    Nat.ordProj_mul_ordCompl_eq_self n 2] at h
  exact h

theorem oddPart_positive {n : ℕ} (hn : 0 < n) : 0 < oddPart n :=
  Nat.ordCompl_pos 2 (Nat.ne_of_gt hn)

theorem oddPart_odd {n : ℕ} (hn : 0 < n) : oddPart n % 2 = 1 := by
  have h := Nat.not_dvd_ordCompl Nat.prime_two (Nat.ne_of_gt hn)
  change ¬ 2 ∣ oddPart n at h
  rw [Nat.dvd_iff_mod_eq_zero] at h
  omega

theorem syr_positive (n : ℕ) : 0 < syr n :=
  oddPart_positive (by omega)

theorem syr_odd (n : ℕ) : syr n % 2 = 1 :=
  oddPart_odd (by omega)

theorem reaches_syr {n : ℕ} (hn : n % 2 = 1) : Reaches n (syr n) := by
  apply reaches_trans (b := 3 * n + 1)
  · exact ⟨1, by simp [full, hn]⟩
  · exact reaches_oddPart (3 * n + 1)

theorem reaches_syr_iterate {n : ℕ} (hn : n % 2 = 1) (k : ℕ) :
    Reaches n (syr^[k] n) := by
  induction k generalizing n with
  | zero => exact ⟨0, rfl⟩
  | succ k ih =>
    rw [Function.iterate_succ_apply]
    exact reaches_trans (reaches_syr hn) (ih (syr_odd n))

theorem small_odds_reach_one {n : ℕ} (hn : 0 < n) (ho : n % 2 = 1)
    (hb : n < 13) : Reaches n 1 := by
  have cases : n = 1 ∨ n = 3 ∨ n = 5 ∨ n = 7 ∨ n = 9 ∨ n = 11 := by omega
  rcases cases with rfl | rfl | rfl | rfl | rfl | rfl
  · exact ⟨0, rfl⟩
  · exact ⟨7, by decide⟩
  · exact ⟨5, by decide⟩
  · exact ⟨16, by decide⟩
  · exact ⟨19, by decide⟩
  · exact ⟨14, by decide⟩

/-- The numerical growth margin used above the independently checked floor. -/
theorem high_edge_margin {x : ℝ} (hx : 13 ≤ x) :
    (201 / 200 : ℝ) ≤ (25 / 24 : ℝ) ^ 2 * (3 * x / (3 * x + 1)) ^ 3 := by
  have hd : 0 < 3 * x + 1 := by linarith
  have hr : (39 / 40 : ℝ) ≤ 3 * x / (3 * x + 1) := by
    apply (le_div_iff₀ hd).2
    linarith
  have hp := pow_le_pow_left₀ (show (0 : ℝ) ≤ 39 / 40 by norm_num) hr 3
  nlinarith [hp]

/-- A bounded positive potential cannot increase by this fixed factor forever. -/
theorem bounded_growth_not_infinite (v : ℕ → ℝ) (M : ℝ)
    (hv : 0 < v 0) (hb : ∀ k, v k ≤ M)
    (hs : ∀ k, (201 / 200 : ℝ) * v k ≤ v (k + 1)) : False := by
  have grow (k : ℕ) : v 0 + (k : ℝ) * (v 0 / 200) ≤ v k := by
    induction k with
    | zero => simp
    | succ k ih =>
      have hk : 0 ≤ (k : ℝ) := by positivity
      have hbase : v 0 ≤ v k := by nlinarith
      push_cast
      nlinarith [hs k]
  obtain ⟨k, hk⟩ := exists_nat_gt (200 * M / v 0)
  have hkm : 200 * M < (k : ℝ) * v 0 := (div_lt_iff₀ hv).mp hk
  have hg := grow k
  have hu := hb k
  nlinarith

/-- This is the open sufficient condition.  No instance is supplied. -/
def OrdinaryPotential : Prop := ∃ V : ℕ → ℝ, ∃ M : ℝ,
  (∀ n, 0 < n → n % 2 = 1 → 0 < V n ∧ V n ≤ M) ∧
  (∀ n : ℕ, 13 ≤ n → n % 2 = 1 →
    (25 / 24 : ℝ) ^ 2 * (3 * (n : ℝ) / (3 * (n : ℝ) + 1)) ^ 3 * V n
      ≤ V (syr n))

theorem potential_reaches_small (V : ℕ → ℝ) (M : ℝ)
    (hv : ∀ n, 0 < n → n % 2 = 1 → 0 < V n ∧ V n ≤ M)
    (hs : ∀ n : ℕ, 13 ≤ n → n % 2 = 1 →
      (25 / 24 : ℝ) ^ 2 * (3 * (n : ℝ) / (3 * (n : ℝ) + 1)) ^ 3 * V n
        ≤ V (syr n))
    {n : ℕ} (hn : 0 < n) (ho : n % 2 = 1) :
    ∃ k, syr^[k] n < 13 := by
  by_contra h
  have high (k : ℕ) : 13 ≤ syr^[k] n := by
    by_contra hk
    exact h ⟨k, by omega⟩
  have odd (k : ℕ) : syr^[k] n % 2 = 1 := by
    cases k with
    | zero => exact ho
    | succ k => rw [Function.iterate_succ_apply']; exact syr_odd _
  apply bounded_growth_not_infinite (fun k => V (syr^[k] n)) M
  · exact (hv n hn ho).1
  · intro k
    exact (hv _ (by have := high k; omega) (odd k)).2
  · intro k
    have hm := high_edge_margin (x := (syr^[k] n : ℕ)) (by exact_mod_cast high k)
    have hp := (hv _ (by have := high k; omega) (odd k)).1
    have ht := hs _ (high k) (odd k)
    rw [Function.iterate_succ_apply']
    exact (mul_le_mul_of_nonneg_right hm (le_of_lt hp)).trans ht

/-- Complete conditional proposal for the usual positive-integer conjecture. -/
theorem ordinary_potential_implies_collatz (gate : OrdinaryPotential) : Universal := by
  obtain ⟨V, M, hv, hs⟩ := gate
  intro n hn
  have hp := oddPart_positive hn
  have ho := oddPart_odd hn
  obtain ⟨k, hk⟩ := potential_reaches_small V M hv hs hp ho
  have hx : 0 < syr^[k] (oddPart n) := by
    cases k with
    | zero => exact hp
    | succ k => rw [Function.iterate_succ_apply']; exact syr_positive _
  have hodd : syr^[k] (oddPart n) % 2 = 1 := by
    cases k with
    | zero => exact ho
    | succ k => rw [Function.iterate_succ_apply']; exact syr_odd _
  exact reaches_trans (reaches_oddPart n)
    (reaches_trans (reaches_syr_iterate ho k) (small_odds_reach_one hx hodd hk))

end Collatz.SixHour.PotentialAssembly
