import CycleCancellation
import Mathlib.Algebra.Order.BigOperators.GroupWithZero.Finset
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# The exceptional reduced clock and its nontrivial denominator prime

These are finite arithmetic statements for positive ordinary cycle states.
The cycle equation is supplied at every index and the successor is a
permutation, so the product identity is derived rather than postulated.

Every nontrivial positive cycle has a prime other than two or three in
`2 ^ u - 3 ^ v`, for any positive clock reduction `A = g * u`, `p = g * v`.
The associated rational-function pole and arithmetic Taylor-series
obstruction are written mathematics in CYCLE_ARITHMETIC.md and the
companion rational-selector note. No all-time jet hypothesis or exclusion
of all nontrivial cycles is proved here.
-/

namespace Collatz.ProfoundRoundSix.CycleArithmetic

open Collatz.HighVariance.CycleCancellation
open scoped BigOperators

set_option autoImplicit false

private theorem three_pow_mod_eight (v : Nat) :
    3 ^ v % 8 = 1 ∨ 3 ^ v % 8 = 3 := by
  induction v with
  | zero => norm_num
  | succ v ih =>
    rcases ih with h | h <;> simp [pow_succ, Nat.mul_mod, h]

/-- The only positive exponents whose powers differ by one are `(2, 1)`.
The proof uses modulo eight, not an unproved exponential-Diophantine input. -/
theorem two_pow_eq_three_pow_add_one {u v : Nat}
    (hu : 0 < u) (hv : 0 < v) (h : 2 ^ u = 3 ^ v + 1) :
    u = 2 ∧ v = 1 := by
  have hu3 : u < 3 := by
    by_contra hn
    have hdiv : 8 ∣ 2 ^ u := by
      simpa using Nat.pow_dvd_pow 2 (show 3 ≤ u by omega)
    have hz : 2 ^ u % 8 = 0 := Nat.mod_eq_zero_of_dvd hdiv
    have hm := congrArg (fun n : Nat => n % 8) h
    rcases three_pow_mod_eight v with h3 | h3 <;>
      simp [hz, Nat.add_mod, h3] at hm
  have hp : 3 ≤ 3 ^ v := by
    simpa using Nat.pow_le_pow_right (by decide : 1 ≤ 3) hv
  have hu2 : u = 2 := by
    by_contra hn
    have hu1 : u = 1 := by omega
    rw [hu1] at h
    norm_num at h
    omega
  have hp3 : 3 ^ v = 3 ^ 1 := by rw [hu2] at h; norm_num at h ⊢; omega
  exact ⟨hu2, (pow_right_strictMono₀ (by decide : 1 < (3 : Nat))).injective hp3⟩

/-- Multiplication of the actual affine equations retains every state and
every division exponent. A permutation of the successor indices is enough. -/
theorem cycle_product {p : Nat} (σ : Equiv.Perm (Fin p))
    (a x : Fin p → Nat)
    (hcycle : ∀ i, 2 ^ a i * x (σ i) = 3 * x i + 1) :
    (∏ i, (3 * x i + 1)) = 2 ^ (∑ i, a i) * ∏ i, x i := by
  calc
    (∏ i, (3 * x i + 1)) = ∏ i, (2 ^ a i * x (σ i)) := by
      apply Finset.prod_congr rfl
      intro i _
      exact (hcycle i).symm
    _ = (∏ i, 2 ^ a i) * ∏ i, x (σ i) := Finset.prod_mul_distrib
    _ = 2 ^ (∑ i, a i) * ∏ i, x i := by
      rw [Finset.prod_pow_eq_pow_sum, Equiv.prod_comp]

/-- A positive cycle has strictly positive full clock denominator. -/
theorem cycle_clock_positive {p : Nat} (hp : 0 < p)
    (σ : Equiv.Perm (Fin p)) (a x : Fin p → Nat)
    (hx : ∀ i, 0 < x i)
    (hcycle : ∀ i, 2 ^ a i * x (σ i) = 3 * x i + 1) :
    3 ^ p < 2 ^ (∑ i, a i) := by
  have hprod : (∏ i, (3 * x i)) < ∏ i, (3 * x i + 1) := by
    apply Finset.prod_lt_prod₀
    · intro i _; exact Nat.mul_pos (by decide) (hx i)
    · intro i _; omega
    · exact ⟨⟨0, hp⟩, Finset.mem_univ _, by omega⟩
  rw [Finset.prod_mul_distrib, Finset.prod_const, Finset.card_univ,
    Fintype.card_fin, cycle_product σ a x hcycle] at hprod
  exact Nat.lt_of_mul_lt_mul_right hprod

/-- Clock `A = 2p` saturates each positive-state inequality
`3*x + 1 ≤ 4*x`; hence all states of the cycle are one. -/
theorem cycle_clock_two_rigidity {p : Nat}
    (σ : Equiv.Perm (Fin p)) (a x : Fin p → Nat)
    (hx : ∀ i, 0 < x i)
    (hcycle : ∀ i, 2 ^ a i * x (σ i) = 3 * x i + 1)
    (hclock : (∑ i, a i) = 2 * p) :
    ∀ i, x i = 1 := by
  intro i
  by_contra hi
  have hprod : (∏ j, (3 * x j + 1)) < ∏ j, (4 * x j) := by
    apply Finset.prod_lt_prod₀
    · intro j _; omega
    · intro j _; have := hx j; omega
    · exact ⟨i, Finset.mem_univ _, by have := hx i; omega⟩
  rw [cycle_product σ a x hcycle, hclock, Finset.prod_mul_distrib,
    Finset.prod_const, Finset.card_univ, Fintype.card_fin] at hprod
  have hpow : 2 ^ (2 * p) = 4 ^ p := by rw [pow_mul]; norm_num
  rw [hpow] at hprod
  exact (lt_irrefl _) hprod

/-- Passing to any positive common clock divisor preserves the strict
inequality. No primitive-word or coprimality assumption is needed here. -/
theorem reduced_clock_positive {A p g u v : Nat}
    (hA : A = g * u) (hp : p = g * v)
    (hclock : 3 ^ p < 2 ^ A) :
    3 ^ v < 2 ^ u := by
  by_contra hn
  have hle : 2 ^ u ≤ 3 ^ v := by omega
  have hpow := Nat.pow_le_pow_left hle g
  rw [← pow_mul, ← pow_mul] at hpow
  rw [hA, hp, Nat.mul_comm g u, Nat.mul_comm g v] at hclock
  exact (not_lt_of_ge hpow) hclock

/-- A nontrivial positive ordinary cycle supplies a genuine denominator
prime away from two and three in the reduced clock. This is an arithmetic
input to the Taylor-series obstruction, not a proof that such cycles exist. -/
theorem nontrivial_cycle_reduced_clock_prime {p g u v : Nat}
    (hp : 0 < p) (hu : 0 < u) (hv : 0 < v)
    (σ : Equiv.Perm (Fin p)) (a x : Fin p → Nat)
    (hx : ∀ i, 0 < x i)
    (hcycle : ∀ i, 2 ^ a i * x (σ i) = 3 * x i + 1)
    (hA : (∑ i, a i) = g * u) (hpv : p = g * v)
    (hnontrivial : ∃ i, x i ≠ 1) :
    ∃ ℓ : Nat, ℓ.Prime ∧ ℓ ∣ 2 ^ u - 3 ^ v ∧ ℓ ≠ 2 ∧ ℓ ≠ 3 := by
  have hred := reduced_clock_positive hA hpv
    (cycle_clock_positive hp σ a x hx hcycle)
  have hne : 2 ^ u - 3 ^ v ≠ 1 := by
    intro he
    have heq : 2 ^ u = 3 ^ v + 1 := by omega
    obtain ⟨hu2, hv1⟩ := two_pow_eq_three_pow_add_one hu hv heq
    have hc : (∑ i, a i) = 2 * p := by rw [hA, hpv, hu2, hv1]; omega
    obtain ⟨i, hi⟩ := hnontrivial
    exact hi (cycle_clock_two_rigidity σ a x hx hcycle hc i)
  obtain ⟨ℓ, hprime, hdvd⟩ := Nat.exists_prime_and_dvd hne
  obtain ⟨hc2, hc3⟩ := denominator_coprime_two_three u v hu hv hred.le
  refine ⟨ℓ, hprime, hdvd, ?_, ?_⟩
  · intro hℓ
    subst ℓ
    exact ((Nat.prime_two.coprime_iff_not_dvd).mp hc2.symm) hdvd
  · intro hℓ
    subst ℓ
    exact ((Nat.prime_three.coprime_iff_not_dvd).mp hc3.symm) hdvd

end Collatz.ProfoundRoundSix.CycleArithmetic
