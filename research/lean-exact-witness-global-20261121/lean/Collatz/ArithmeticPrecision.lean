/-
The exact correction size at every ordinary clock of one positive orbit.
The odd core is an actual later iterate. For a least bad target, removing
all endpoint powers of two cannot make the normalized correction arbitrarily
small. This is the integer core of an S-adic hypothesis check; no analytic
or Diophantine approximation theorem is imported or assumed.
-/
import Collatz.SourceGreenCoefficient
import Collatz.DirectedInduction

open CollatzReverseBasin CollatzClosure CollatzDirected
open CollatzSourceGreenCoefficient

set_option autoImplicit false
set_option maxHeartbeats 1000000

namespace CollatzArithmeticPrecision

/-- The unshifted affine correction of the actual ordinary parity history. -/
def ordinaryCorrection (target : Nat) : Nat → Nat
  | 0 => 0
  | k+1 => if state target k % 2 = 0 then ordinaryCorrection target k
           else 3 * ordinaryCorrection target k + 2^k

theorem affine_identity (target k : Nat) :
    2^k * state target k =
      3^(oddInputs target k) * target + ordinaryCorrection target k := by
  induction k with
  | zero => simp [state, oddInputs, ordinaryCorrection]
  | succ k ih =>
    by_cases parity : state target k % 2 = 0
    · have edge : 2 * shortcut (state target k) = state target k := by
        simp only [shortcut, parity, ite_true]
        omega
      simp only [state, oddInputs, ordinaryCorrection, parity, ite_true,
        Nat.add_zero, Nat.pow_succ]
      calc
        2^k * 2 * shortcut (state target k) = 2^k * state target k := by
          rw [Nat.mul_assoc, edge]
        _ = _ := ih
    · have edge : 2 * shortcut (state target k) = 3 * state target k + 1 := by
        simp only [shortcut, parity, ite_false]
        omega
      simp only [state, oddInputs, ordinaryCorrection, parity, ite_false, Nat.pow_succ]
      calc
        2^k * 2 * shortcut (state target k) = 2^k * (3 * state target k + 1) := by
          rw [Nat.mul_assoc, edge]
        _ = 3 * (2^k * state target k) + 2^k := by grind
        _ = _ := by rw [ih]; grind

/-- The first odd input contributes one, which every later odd input triples.
This form avoids division and the predecessor of the odd-event count. -/
theorem first_odd_contribution (target k : Nat) (odd : target % 2 = 1)
    (positiveClock : 0 < k) :
    3^(oddInputs target k) ≤ 3 * ordinaryCorrection target k := by
  induction k with
  | zero => omega
  | succ k ih =>
    cases k with
    | zero =>
      have notEven : ¬ target % 2 = 0 := by omega
      simp [oddInputs, ordinaryCorrection, state, notEven]
    | succ k =>
      have previous := ih (by omega)
      by_cases parity : state target (k+1) % 2 = 0
      · simpa only [oddInputs, ordinaryCorrection, parity, ite_true, Nat.add_zero]
          using previous
      · have count : oddInputs target ((k+1)+1) = oddInputs target (k+1)+1 := by
          rw [oddInputs]
          simp only [parity, ite_false]
        have correction : ordinaryCorrection target ((k+1)+1) =
            3 * ordinaryCorrection target (k+1) + 2^(k+1) := by
          rw [ordinaryCorrection]
          simp only [parity, ite_false]
        rw [count, correction, Nat.pow_succ]
        calc
          3^(oddInputs target (k+1)) * 3 ≤
              (3 * ordinaryCorrection target (k+1)) * 3 :=
            Nat.mul_le_mul_right 3 previous
          _ = 3 * (3 * ordinaryCorrection target (k+1)) := by ac_rfl
          _ ≤ 3 * (3 * ordinaryCorrection target (k+1) + 2^(k+1)) :=
            Nat.mul_le_mul_left 3 (Nat.le_add_right _ _)

theorem state_add (target a b : Nat) :
    state target (a+b) = state (state target a) b := by
  induction b with
  | zero => simp [state]
  | succ b ih => simp [state, ih]

private theorem state_succ_first (target k : Nat) :
    state target (k+1) = state (shortcut target) k := by
  have compose := state_add target 1 k
  simpa [Nat.add_comm, state] using compose

theorem state_pow_two (v core : Nat) : state (2^v * core) v = core := by
  induction v with
  | zero => simp [state]
  | succ v ih =>
    have form : 2^(v+1)*core = 2*(2^v*core) := by
      rw [Nat.pow_succ]
      ac_rfl
    rw [state_succ_first, form]
    simpa [shortcut] using ih

private theorem state_positive (target k : Nat) (positive : 0 < target) :
    0 < state target k := by
  induction k with
  | zero => exact positive
  | succ k ih =>
    simp only [state]
    unfold shortcut
    split <;> omega

private theorem basin_state (target k : Nat) :
    Basin (state target k) ↔ Basin target := by
  induction k with
  | zero => rfl
  | succ k ih =>
    exact (basin_step (state target k)).trans ih

/-- Normalizing an endpoint keeps the original orbit and adds only actual
halving clocks. The existential exponent is its exact dyadic valuation,
because the defined odd core is positive and odd. -/
theorem odd_core_at_later_clock (target k : Nat) (positive : 0 < target) :
    ∃ v, state target k = 2^v * oddCore (state target k) ∧
      state target (k+v) = oddCore (state target k) := by
  obtain ⟨v, factor⟩ := oddCore_factor (state target k) (state_positive target k positive)
  refine ⟨v, factor, ?_⟩
  calc
    state target (k+v) = state (state target k) v := state_add target k v
    _ = state (2^v * oddCore (state target k)) v :=
      congrArg (fun n => state n v) factor
    _ = oddCore (state target k) := state_pow_two v _

/-- Integral form of C_k / 2^(k+v) ≥ oddCore(n_k)/(3*target+1). -/
theorem normalized_correction_bound (target k v : Nat)
    (odd : target % 2 = 1) (positiveClock : 0 < k)
    (factor : state target k = 2^v * oddCore (state target k)) :
    oddCore (state target k) * 2^(k+v) ≤
      (3*target+1) * ordinaryCorrection target k := by
  have contribution := first_odd_contribution target k odd positiveClock
  have scaled := Nat.mul_le_mul_right target contribution
  calc
    oddCore (state target k) * 2^(k+v) = 2^k * state target k := by
      calc
        oddCore (state target k) * 2^(k+v) =
            2^k * (2^v * oddCore (state target k)) := by
          rw [Nat.pow_add]
          ac_rfl
        _ = 2^k * state target k := congrArg (fun n => 2^k*n) factor.symm
    _ = 3^(oddInputs target k) * target + ordinaryCorrection target k :=
      affine_identity target k
    _ ≤ 3 * ordinaryCorrection target k * target + ordinaryCorrection target k :=
      Nat.add_le_add_right scaled _
    _ = (3*target+1) * ordinaryCorrection target k := by grind

/-- The original numerical prior pays any smaller odd core, since it is
an actual later iterate of this same target. -/
theorem least_bad_odd_core (target k : Nat) (positive : 0 < target)
    (bad : ¬ Basin target)
    (prior : ∀ n, 0 < n → n < target → Basin n) :
    target ≤ oddCore (state target k) := by
  by_cases lower : target ≤ oddCore (state target k)
  · exact lower
  · have corePositive := (oddCore_spec (state target k)
      (state_positive target k positive)).1
    have coreBasin := prior _ corePositive (by omega)
    obtain ⟨v, _, reached⟩ := odd_core_at_later_clock target k positive
    have endpointBasin : Basin (state target (k+v)) := by
      rw [reached]
      exact coreBasin
    exact False.elim (bad ((basin_state target (k+v)).mp endpointBasin))

/-- At every positive ordinary clock of a least bad odd target, the full
normalized endpoint correction has an explicit original-target lower bound.
There is no source reset and no bounded lookahead restriction. -/
theorem least_bad_precision_bound (target k : Nat) (odd : target % 2 = 1)
    (positiveClock : 0 < k) (bad : ¬ Basin target)
    (prior : ∀ n, 0 < n → n < target → Basin n) :
    ∃ v, state target k = 2^v * oddCore (state target k) ∧
      state target (k+v) = oddCore (state target k) ∧
      target * 2^(k+v) ≤ (3*target+1) * ordinaryCorrection target k := by
  have positive : 0 < target := by omega
  obtain ⟨v, factor, reached⟩ := odd_core_at_later_clock target k positive
  refine ⟨v, factor, reached, ?_⟩
  have lower := least_bad_odd_core target k positive bad prior
  exact Nat.le_trans (Nat.mul_le_mul_right (2^(k+v)) lower)
    (normalized_correction_bound target k v odd positiveClock factor)

end CollatzArithmeticPrecision
