import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.NormNum

/-!
Backward zero propagation on a finite genuine binary-tag tube.

The comparison is scaled by the complete denominator q. Its forcing is
q times an integer in [-2,2]. Coprimality of q with three, rather than
integrality of the unscaled comparison or a closed cyclic return, forces
a zero to propagate backwards. The physical tube and prime dilation
remain written in COMPLETE_DENOMINATOR_BAND_EXITS.md.
-/

set_option autoImplicit false
namespace Collatz.NativeTubeZero

/-- One zero at the next native date forces both the preceding comparison
and its signed binary-tag forcing to be zero, retaining the full q. -/
theorem backward_zero (q U V d : ℤ) (b : ℕ)
    (coprime : IsCoprime q 3) (lower : -2 ≤ d) (upper : d ≤ 2)
    (edge : 2 ^ b * V = 3 * U + q * d) (zero : V = 0) :
    U = 0 ∧ d = 0 := by
  have h : 3 * U + q * d = 0 := by simpa only [zero, mul_zero] using edge.symm
  have product : (3 : ℤ) ∣ q * d := by
    refine ⟨-U, ?_⟩
    omega
  have divisible : (3 : ℤ) ∣ d := coprime.symm.dvd_of_dvd_mul_left product
  obtain ⟨k, hk⟩ := divisible
  have forcing : d = 0 := by omega
  constructor
  · rw [forcing, mul_zero, add_zero] at h
    omega
  · exact forcing

/-- A zero at the end of a finite native tube makes every preceding
comparison and every forcing in that tube vanish. No transitivity,
periodicity, denominator-size or spatial-order premise is used. -/
theorem zero_tube (q : ℤ) (coprime : IsCoprime q 3)
    (U d : ℕ → ℤ) (b : ℕ → ℕ)
    (lower : ∀ i, -2 ≤ d i) (upper : ∀ i, d i ≤ 2) :
    ∀ N : ℕ,
      (∀ i < N, 2 ^ b i * U (i + 1) = 3 * U i + q * d i) →
      U N = 0 → (∀ i ≤ N, U i = 0) ∧ (∀ i < N, d i = 0) := by
  intro N
  induction N with
  | zero =>
    intro _ endpoint
    constructor
    · intro i hi
      have : i = 0 := by omega
      simpa only [this] using endpoint
    · intro i hi
      omega
  | succ N ih =>
    intro edge endpoint
    have last := backward_zero q (U N) (U (N + 1)) (d N) (b N)
      coprime (lower N) (upper N) (edge N (by omega)) endpoint
    have preceding := ih (fun i hi => edge i (by omega)) last.1
    constructor
    · intro i hi
      by_cases final : i = N + 1
      · simpa only [final] using endpoint
      · exact preceding.1 i (by omega)
    · intro i hi
      by_cases final : i = N
      · simpa only [final] using last.2
      · exact preceding.2 i (by omega)

end Collatz.NativeTubeZero
