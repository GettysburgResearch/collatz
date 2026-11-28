import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
The full-denominator zero-propagation kernel for rational cyclic pair sums.

`U` is the comparison after multiplication by the complete odd denominator.
One zero propagates divisibility by that entire denominator. The resulting
integer comparison has forcing between -2 and 2, so every nonzero sign would
persist until returning to the zero. No denominator factor is discarded.

The construction of the actual dyadic columns, their transitive native clock,
and the sparse spatial recurrence which excludes an everywhere-zero
comparison remain written in GLOBAL_DYADIC_PAIR_ABUNDANCE.md.
-/

set_option autoImplicit false
namespace Collatz.FullDenominatorPairZero

variable {α : Type*}

/-- A zero of the scaled comparison makes the complete denominator divide
every later comparison, and transitivity reaches the entire cycle. -/
theorem full_denominator_divides_of_zero
    (U : α → ℤ) (σ : α → α) (b : α → ℕ) (d : α → ℤ) (q : ℤ)
    (coprime : IsCoprime q 2)
    (reach : ∀ r s, ∃ n : ℕ, (σ^[n]) r = s)
    (edge : ∀ r, 2 ^ b r * U (σ r) = 3 * U r + q * d r)
    (r₀ : α) (zero : U r₀ = 0) : ∀ r, q ∣ U r := by
  have advance (r : α) (h : q ∣ U r) : q ∣ U (σ r) := by
    have cp : IsCoprime q (2 ^ b r) := coprime.pow_right
    apply cp.dvd_of_dvd_mul_left
    rw [edge r]
    exact dvd_add (dvd_mul_of_dvd_right h 3) (by exact ⟨d r, rfl⟩)
  have along (n : ℕ) : q ∣ U ((σ^[n]) r₀) := by
    induction n with
    | zero => simpa only [Function.iterate_zero, id_eq, zero] using (dvd_zero q)
    | succ n ih =>
      rw [Function.iterate_succ_apply']
      exact advance _ ih
  intro r
  obtain ⟨n, hn⟩ := reach r₀ r
  simpa only [hn] using along n

private theorem positive_advance (x y d : ℤ) (b : ℕ)
    (hx : 0 < x) (hd : -2 ≤ d) (edge : 2 ^ b * y = 3 * x + d) : 0 < y := by
  have h : 0 < 3 * x + d := by omega
  rw [← edge] at h
  exact pos_of_mul_pos_right h (by positivity)

private theorem negative_advance (x y d : ℤ) (b : ℕ)
    (hx : x < 0) (hd : d ≤ 2) (edge : 2 ^ b * y = 3 * x + d) : y < 0 := by
  have h : 3 * x + d < 0 := by omega
  rw [← edge] at h
  exact neg_of_mul_neg_right h (by positivity)

/-- On a transitive native cycle, one rational pair-sum zero forces the
comparison to vanish everywhere, with the full denominator retained. -/
theorem one_zero_forces_all_zero
    (U : α → ℤ) (σ : α → α) (b : α → ℕ) (d : α → ℤ) (q : ℤ)
    (nonzero : q ≠ 0) (coprime : IsCoprime q 2)
    (reach : ∀ r s, ∃ n : ℕ, (σ^[n]) r = s)
    (lower : ∀ r, -2 ≤ d r) (upper : ∀ r, d r ≤ 2)
    (edge : ∀ r, 2 ^ b r * U (σ r) = 3 * U r + q * d r)
    (r₀ : α) (zero : U r₀ = 0) : ∀ r, U r = 0 := by
  have divisible := full_denominator_divides_of_zero U σ b d q coprime reach edge r₀ zero
  let H : α → ℤ := fun r => U r / q
  have quotient (r : α) : q * H r = U r := Int.mul_ediv_cancel' (divisible r)
  have normalized (r : α) : 2 ^ b r * H (σ r) = 3 * H r + d r := by
    apply mul_left_cancel₀ nonzero
    calc
      q * (2 ^ b r * H (σ r)) = 2 ^ b r * (q * H (σ r)) := by ring
      _ = 3 * (q * H r) + q * d r := by
        rw [quotient (σ r), quotient r]
        exact edge r
      _ = q * (3 * H r + d r) := by ring
  have initial : H r₀ = 0 := by simp only [H, zero, Int.zero_ediv]
  have vanishes (r : α) : H r = 0 := by
    obtain ⟨n, hn⟩ := reach r r₀
    rcases lt_trichotomy (H r) 0 with negative | equal | positive
    · have along (k : ℕ) : H ((σ^[k]) r) < 0 := by
        induction k with
        | zero => simpa using negative
        | succ k ih =>
          rw [Function.iterate_succ_apply']
          exact negative_advance _ _ _ _ ih (upper _) (normalized _)
      have bad := along n
      rw [hn, initial] at bad
      exact False.elim (lt_irrefl 0 bad)
    · exact equal
    · have along (k : ℕ) : 0 < H ((σ^[k]) r) := by
        induction k with
        | zero => simpa using positive
        | succ k ih =>
          rw [Function.iterate_succ_apply']
          exact positive_advance _ _ _ _ ih (lower _) (normalized _)
      have bad := along n
      rw [hn, initial] at bad
      exact False.elim (lt_irrefl 0 bad)
  intro r
  rw [← quotient r, vanishes r, mul_zero]

end Collatz.FullDenominatorPairZero
