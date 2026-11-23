/-
Actual coalescence clocks for a multiplicative lift of Collatz sources.

The semigroup theorem of Applegate--Lagarias permits prime multipliers.
This module checks a necessary condition for replacing such multiplication
by ordinary Collatz mergers.  A multiplier with a factor coprime to six
cannot have a source-independent merger-clock budget.  The proof retains
the actual affine corrections on both trajectories; it does not assert
that these mergers exist at any larger clock.
-/
import Collatz.ArithmeticPrecision

open CollatzReverseBasin CollatzSourceGreenCoefficient
open CollatzArithmeticPrecision

set_option autoImplicit false
set_option maxHeartbeats 1000000

namespace CollatzMultiplierTransport

private theorem correction_budget (n k : Nat) :
    ordinaryCorrection n k + 2^k ≤ 3^k := by
  induction k with
  | zero => simp [ordinaryCorrection]
  | succ k ih =>
    simp only [ordinaryCorrection, Nat.pow_succ]
    split <;> omega

private theorem separated (m d p q k l : Nat)
    (factor : d ∣ m) (large : 1 < d) (primeToSix : Nat.Coprime d 6) :
    3^p*m*2^l ≠ 3^q*2^k := by
  intro same
  have unitTwo : Nat.Coprime d 2 :=
    primeToSix.coprime_dvd_right (by decide : 2 ∣ 6)
  have unitThree : Nat.Coprime d 3 :=
    primeToSix.coprime_dvd_right (by decide : 3 ∣ 6)
  have coprime : Nat.Coprime d (3^q*2^k) :=
    (unitThree.pow_right q).mul_right (unitTwo.pow_right k)
  have divides : d ∣ 3^q*2^k := by
    rw [←same]
    obtain ⟨v, hv⟩ := factor
    refine ⟨3^p*v*2^l, ?_⟩
    rw [hv]
    ac_rfl
  have one := coprime.eq_one_of_dvd divides
  omega

private theorem small_remainders (a b c d n : Nat)
    (left : b < n) (right : d < n)
    (same : a*n+b=c*n+d) : a=c := by
  have leAC : a ≤ c := by
    by_cases notLe : a ≤ c
    · exact notLe
    have oneMore : c+1 ≤ a := by omega
    have mul := Nat.mul_le_mul_right n oneMore
    have distribute : (c+1)*n=c*n+n := by grind
    rw [distribute] at mul
    omega
  have leCA : c ≤ a := by
    by_cases notLe : c ≤ a
    · exact notLe
    have oneMore : a+1 ≤ c := by omega
    have mul := Nat.mul_le_mul_right n oneMore
    have distribute : (a+1)*n=a*n+n := by grind
    rw [distribute] at mul
    omega
  omega

private theorem cross_correction (source k l N : Nat)
    (first : k ≤ N) (second : l ≤ N) :
    2^k*ordinaryCorrection source l < 6^N := by
  have correction := correction_budget source l
  have positive : 0 < 2^l := Nat.pow_pos (by decide)
  have below : ordinaryCorrection source l < 3^l := by omega
  have strict := Nat.mul_lt_mul_of_pos_left below
    (Nat.pow_pos (by decide : 0 < 2) (n:=k))
  have powers : 2^k*3^l ≤ 2^N*3^N :=
    Nat.mul_le_mul (Nat.pow_le_pow_right (by decide) first)
      (Nat.pow_le_pow_right (by decide) second)
  have product : 2^N*3^N=6^N := by rw [←Nat.mul_pow]
  rw [product] at powers
  omega

/-- Uniform in both physical clocks, the actual parity words, and the
multiplier.  The hypothesis on d permits every m having a prime factor
outside {2,3}; no fixed parity cylinder is assumed. -/
theorem merger_clock_budget (m d n k l N : Nat)
    (factor : d ∣ m) (large : 1 < d) (primeToSix : Nat.Coprime d 6)
    (first : k ≤ N) (second : l ≤ N)
    (meeting : state (m*n) k = state n l) : n < 6^N := by
  by_cases notSmall : n < 6^N
  · exact notSmall
  have floor : 6^N ≤ n := by omega
  have left := affine_identity (m*n) k
  have right := affine_identity n l
  have firstScaled := congrArg (fun a => 2^l*a) left
  have secondScaled := congrArg (fun a => 2^k*a) right
  have same :
      (3^(oddInputs (m*n) k)*m*2^l)*n + 2^l*ordinaryCorrection (m*n) k =
      (3^(oddInputs n l)*2^k)*n + 2^k*ordinaryCorrection n l := by
    rw [meeting] at firstScaled
    grind
  have leftSmall : 2^l*ordinaryCorrection (m*n) k < n :=
    Nat.lt_of_lt_of_le (cross_correction (m*n) l k N second first) floor
  have rightSmall : 2^k*ordinaryCorrection n l < n :=
    Nat.lt_of_lt_of_le (cross_correction n k l N first second) floor
  exact False.elim (separated m d _ _ k l factor large primeToSix
    (small_remainders _ _ _ _ n leftSmall rightSmall same))

/-- Even if all ordinary pairs eventually merge, their independent clocks
cannot be bounded independently of the input.  This rules out lifting a
wild prime multiplier by a finite collection of fixed physical path pairs. -/
theorem no_uniform_merger_clock (m d : Nat)
    (factor : d ∣ m) (large : 1 < d) (primeToSix : Nat.Coprime d 6) :
    ¬∃ N, ∀ n, 0<n → ∃ k l, k≤N ∧ l≤N ∧ state (m*n) k=state n l := by
  rintro ⟨N, uniform⟩
  obtain ⟨k,l,first,second,meeting⟩ :=
    uniform (6^N) (Nat.pow_pos (by decide))
  have impossible := merger_clock_budget m d (6^N) k l N
    factor large primeToSix first second meeting
  omega

end CollatzMultiplierTransport
