module

public import Mathlib.NumberTheory.Multiplicity
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

@[expose] public section

namespace Collatz.ExplicitConcentration

theorem ternary_valuation (k : ℕ) :
    padicValNat 3 (2 ^ (3 ^ k) + 1) = k + 1 := by
  let : Fact (Nat.Prime 3) := ⟨by decide⟩
  have hodd : Odd (3 ^ k) := (by decide : Odd (3 : ℕ)).pow
  have h := padicValNat.pow_add_pow (p := 3) (x := 2) (y := 1)
    (by decide : Odd (3 : ℕ)) (by decide) (by decide) hodd
  simpa [padicValNat.prime_pow, padicValNat_self, Nat.add_comm] using h

theorem ternary_divisibility (k : ℕ) :
    3 ^ (k + 1) ∣ 2 ^ (3 ^ k) + 1 := by
  have h := pow_padicValNat_dvd (p := 3) (n := 2 ^ (3 ^ k) + 1)
  rwa [ternary_valuation] at h

theorem lift_exists (N m : ℕ) :
    ∃ u : ℕ, 0 < u ∧ Odd u ∧ 3 ^ m ∣ u ∧
      3 ^ (N + 1) * u = 2 ^ (3 ^ (N + m)) + 1 := by
  obtain ⟨z, hz⟩ := ternary_divisibility (N + m)
  refine ⟨3 ^ m * z, ?_, ?_, dvd_mul_right _ _, ?_⟩
  · have hzpos : 0 < z := by
      by_contra h
      have : z = 0 := by omega
      simp [this] at hz
    positivity
  · have hodd : Odd (2 ^ (3 ^ (N + m)) + 1) := by
      obtain ⟨e, he⟩ := Nat.exists_eq_succ_of_ne_zero
        (show 3 ^ (N + m) ≠ 0 by positivity)
      rw [he, pow_succ]
      exact ⟨2 ^ e, by omega⟩
    rw [hz] at hodd
    have hzo : Odd z := (Nat.odd_mul.mp hodd).2
    exact ((by decide : Odd (3 : ℕ)).pow).mul hzo
  · rw [← mul_assoc, ← pow_add]
    rw [show N + 1 + m = N + m + 1 by omega]
    exact hz.symm

def state (k j : ℕ) (u : ℕ) : ℤ :=
  2 ^ (k + 1) * 3 ^ j * (u : ℤ) - 1

theorem state_positive (k j u : ℕ) (hu : 0 < u) : 0 < state k j u := by
  have hu' : (1 : ℤ) ≤ u := by exact_mod_cast hu
  have h2 : (1 : ℤ) ≤ 2 ^ k := one_le_pow₀ (by norm_num)
  have h3 : (1 : ℤ) ≤ 3 ^ j := one_le_pow₀ (by norm_num)
  unfold state
  rw [pow_succ]
  nlinarith [mul_le_mul h2 h3 (by positivity) (by positivity),
    mul_le_mul_of_nonneg_right (mul_le_mul h2 h3 (by positivity) (by positivity))
      (show 0 ≤ (u : ℤ) by positivity)]

theorem state_odd (k j u : ℕ) : Odd (state k j u) := by
  refine ⟨2 ^ k * 3 ^ j * (u : ℤ) - 1, ?_⟩
  simp only [state, pow_succ]
  ring

theorem state_edge (k j u : ℕ) :
    3 * state (k + 1) j u + 1 = 2 * state k (j + 1) u := by
  simp only [state, pow_succ]
  ring

theorem state_strict_growth (k j u : ℕ) (hu : 0 < u) :
    state (k + 1) j u < state k (j + 1) u := by
  have hp := state_positive (k + 1) j u hu
  have he := state_edge k j u
  omega

theorem state_residue (k j u m : ℕ) (hu : 3 ^ m ∣ u) :
    (3 : ℤ) ^ m ∣ state k j u + 1 := by
  obtain ⟨z, hz⟩ := hu
  refine ⟨2 ^ (k + 1) * 3 ^ j * (z : ℤ), ?_⟩
  simp only [state, hz, Nat.cast_mul, Nat.cast_pow, Nat.cast_ofNat]
  ring

theorem terminal_edge (N m u : ℕ)
    (hu : 3 ^ (N + 1) * u = 2 ^ (3 ^ (N + m)) + 1) :
    3 * state 0 N u + 1 = (2 : ℤ) ^ (3 ^ (N + m) + 1) := by
  have h : (3 : ℤ) ^ (N + 1) * (u : ℤ) = (2 : ℤ) ^ (3 ^ (N + m)) + 1 := by
    exact_mod_cast hu
  simp only [state, pow_succ] at *
  linear_combination 2 * h

/-- An unbounded family of positive odd increasing prefixes in one ternary
residue class, followed by the literal odd step to one. -/
theorem explicit_family (N m : ℕ) :
    ∃ u : ℕ, 0 < u ∧ Odd u ∧
      (∀ i ≤ N, 0 < state (N - i) i u ∧ Odd (state (N - i) i u) ∧
        (3 : ℤ) ^ m ∣ state (N - i) i u + 1) ∧
      (∀ i < N,
        3 * state (N - i) i u + 1 = 2 * state (N - (i + 1)) (i + 1) u ∧
        state (N - i) i u < state (N - (i + 1)) (i + 1) u) ∧
      3 * state 0 N u + 1 = (2 : ℤ) ^ (3 ^ (N + m) + 1) := by
  obtain ⟨u, hu, ho, hd, he⟩ := lift_exists N m
  refine ⟨u, hu, ho, ?_, ?_, terminal_edge N m u he⟩
  · intro i _
    exact ⟨state_positive _ _ _ hu, state_odd _ _ _, state_residue _ _ _ _ hd⟩
  · intro i hi
    rw [show N - i = (N - (i + 1)) + 1 by omega]
    exact ⟨state_edge _ _ _, state_strict_growth _ _ _ hu⟩

#print axioms ternary_valuation
#print axioms ternary_divisibility
#print axioms lift_exists
#print axioms state_positive
#print axioms state_odd
#print axioms state_edge
#print axioms state_strict_growth
#print axioms state_residue
#print axioms terminal_edge
#print axioms explicit_family

end Collatz.ExplicitConcentration
