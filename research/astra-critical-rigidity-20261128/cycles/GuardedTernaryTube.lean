import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
The scaled comparison U is integral after multiplication by its complete
denominator q. A guard of g preceding homogeneous edges supplies 3^g at
the departure. This raises the strict forcing cutoff to 3^(g+1) on
an arbitrary finite interval. Winding exponents vary at each edge.
-/

set_option autoImplicit false

namespace Collatz.GuardedTernaryTube

/-- Consecutive genuine homogeneous edges accumulate their full ternary divisor. -/
theorem homogeneous_guard (U : ℕ → ℤ) (b : ℕ → ℕ) (start : ℕ) :
    ∀ g : ℕ, (∀ j < g, 2 ^ b (start + j) * U (start + j + 1) = 3 * U (start + j)) →
      (3 : ℤ) ^ g ∣ U (start + g) := by
  intro g
  induction g with
  | zero => simp
  | succ g ih =>
    intro edges
    obtain ⟨z, hz⟩ := ih (fun j hj => edges j (by omega))
    have primeToTwo : IsCoprime (3 : ℤ) 2 := ⟨1, -1, by norm_num⟩
    have coprime : IsCoprime ((3 : ℤ) ^ (g + 1)) (2 ^ b (start + g)) := primeToTwo.pow
    apply coprime.dvd_of_dvd_mul_left
    rw [show start + (g + 1) = start + g + 1 by omega, edges g (by omega), hz]
    refine ⟨z, ?_⟩
    rw [pow_succ]
    ring

/-- A zero at the next edge peels one signed forcing if its prior scaled
comparison carries the guard divisor. The denominator can be arbitrarily large. -/
theorem guarded_backward (q u v d : ℤ) (g b : ℕ) (coprime : IsCoprime q 3)
    (guard : (3 : ℤ) ^ g ∣ u)
    (small : d.natAbs < 3 ^ (g + 1))
    (edge : 2 ^ b * v = 3 * u + q * d) (zero : v = 0) :
    u = 0 ∧ d = 0 := by
  have closed : 3 * u + q * d = 0 := by simpa only [zero, mul_zero] using edge.symm
  obtain ⟨z, hz⟩ := guard
  have dividesProduct : (3 : ℤ) ^ (g+1) ∣ q*d := by
    refine ⟨-z, ?_⟩
    rw [show q*d = -(3*u) by omega, hz, pow_succ]
    ring
  have whole : (3 : ℤ) ^ (g+1) ∣ d := coprime.pow_right.symm.dvd_of_dvd_mul_left dividesProduct
  have forcing : d = 0 := Int.eq_zero_of_dvd_of_natAbs_lt_natAbs whole (by simpa using small)
  simp only [forcing, mul_zero, add_zero] at closed
  exact ⟨by omega, forcing⟩

/-- Starting after a supplied guard, one final zero forces all signed
comparisons and all forcings to vanish down to the encoded left edge.
The actual edge equation also holds on the initial guard dates. -/
theorem guarded_zero_tube (q : ℤ) (coprime : IsCoprime q 3)
    (U d : ℕ → ℤ) (b : ℕ → ℕ) (g : ℕ) :
    ∀ N : ℕ,
      (∀ i < N+g, 2 ^ b i * U (i+1) = 3 * U i + q * d i) →
      (∀ i < N, (d (i+g)).natAbs < 3 ^ (g+1)) →
      (∀ i < N, d (i+g) ≠ 0 → ∀ j < g, d (i+j) = 0) →
      U (N+g) = 0 →
      (∀ i ≤ N, U (i+g) = 0) ∧ (∀ i < N, d (i+g) = 0) := by
  intro N
  induction N with
  | zero =>
    intro _ _ _ endpoint
    exact ⟨fun i hi => by simpa only [show i = 0 by omega] using endpoint, fun i hi => by omega⟩
  | succ N ih =>
    intro edges small sparse endpoint
    have lastEdge := edges (N+g) (by omega)
    have lastValue : U (N+g+1) = 0 := by simpa only [show N+g+1 = N+1+g by omega] using endpoint
    have last : U (N+g) = 0 ∧ d (N+g) = 0 := by
      by_cases inactive : d (N+g) = 0
      · simp only [inactive, mul_zero, add_zero, lastValue] at lastEdge
        exact ⟨by omega, inactive⟩
      · have guards : (3 : ℤ) ^ g ∣ U (N+g) := by
          apply homogeneous_guard U b N g
          intro j hj
          have e := edges (N+j) (by omega)
          simpa only [sparse N (by omega) inactive j hj, mul_zero, add_zero] using e
        exact guarded_backward q _ _ _ g _ coprime guards (small N (by omega)) lastEdge lastValue
    have prior := ih (fun i hi => edges i (by omega)) (fun i hi => small i (by omega))
      (fun i hi => sparse i (by omega)) last.1
    constructor
    · intro i hi
      by_cases atEnd : i = N+1
      · simpa only [atEnd] using endpoint
      · exact prior.1 i (by omega)
    · intro i hi
      by_cases atEnd : i = N
      · simpa only [atEnd] using last.2
      · exact prior.2 i (by omega)

end Collatz.GuardedTernaryTube
