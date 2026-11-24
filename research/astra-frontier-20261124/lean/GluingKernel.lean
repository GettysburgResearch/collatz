module

public import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-! Exact algebra for the ordinary all-one prefix.
The general primitive-root gluing argument is proved in BRIDGE_AUDIT.md. -/

@[expose] public section

namespace Collatz.OrdinaryGluing

/-- With k binary factors remaining, j ternary factors accumulated, and fixed odd u,
the physical state is 2^(k+1) 3^j u - 1. -/
def state (k j : ℕ) (u : ℤ) : ℤ := 2 ^ (k+1) * 3 ^ j * u - 1

theorem state_odd (k j : ℕ) (u : ℤ) : Odd (state k j u) := by
  refine ⟨2 ^ k * 3 ^ j * u - 1, ?_⟩
  simp only [state, pow_succ]
  ring

theorem physical_one_edge (k j : ℕ) (u : ℤ) :
    3 * state (k+1) j u + 1 = 2 * state k (j+1) u := by
  simp only [state, pow_succ]
  ring

theorem ternary_residue (k j m : ℕ) (u z : ℤ) (h : u = 3 ^ m * z) :
    (3 : ℤ) ^ m ∣ state k j u + 1 := by
  refine ⟨2 ^ (k+1) * 3 ^ j * z, ?_⟩
  rw [h]
  simp only [state]
  ring

theorem terminal_edge (n r : ℕ) (u : ℤ)
    (h : 3 ^ (n+1) * u = 2 ^ r + 1) :
    3 * state 0 n u + 1 = 2 ^ (r+1) := by
  simp only [pow_succ] at h
  simp only [state, pow_succ]
  linear_combination 2 * h

/-- Connect a literal equation with its ordinary valuation and actual odd-map output. -/
theorem exact_gap (x y g : ℕ) (hy : Odd y) (h : 3*x+1 = 2^g * y) :
    (3*x+1).factorization 2 = g ∧ (3*x+1) / 2^g = y := by
  have hn : y ≠ 0 := by
    rintro rfl
    simp at hy
  have hd : ¬ 2 ∣ y := by
    have he := Nat.odd_iff.mp hy
    omega
  rw [h]
  constructor
  · rw [Nat.factorization_mul (by positivity) hn, Finsupp.add_apply,
      Nat.factorization_pow_self Nat.prime_two, Nat.factorization_eq_zero_of_not_dvd hd,
      Nat.add_zero]
  · exact Nat.mul_div_cancel_left y (by positivity)

end Collatz.OrdinaryGluing

#print axioms Collatz.OrdinaryGluing.state_odd
#print axioms Collatz.OrdinaryGluing.physical_one_edge
#print axioms Collatz.OrdinaryGluing.ternary_residue
#print axioms Collatz.OrdinaryGluing.terminal_edge
#print axioms Collatz.OrdinaryGluing.exact_gap
