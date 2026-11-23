/-
The exact ordinary coefficient underlying retained-source Green mass.
Shifting each state by one removes the odd affine correction. The remaining
integer defect records even inputs, with no convergence assumption.
-/
import Collatz.ReverseBasin146
import Init.Data.Nat.Coprime

open CollatzReverseBasin

set_option autoImplicit false
set_option maxHeartbeats 1000000

namespace CollatzSourceGreenCoefficient

/-- The actual shortcut state after the specified number of clocks. -/
def state (source : Nat) : Nat → Nat
  | 0 => source
  | t+1 => shortcut (state source t)

/-- Count odd inputs, including the input at clock t in the successor case. -/
def oddInputs (source : Nat) : Nat → Nat
  | 0 => 0
  | t+1 => oddInputs source t + if state source t % 2 = 0 then 0 else 1

/-- Shifted affine defect. Odd inputs triple it; even inputs add 2^t. -/
def evenDefect (source : Nat) : Nat → Nat
  | 0 => 0
  | t+1 => if state source t % 2 = 0 then evenDefect source t + 2^t
           else 3 * evenDefect source t

def AllOdd (source t : Nat) : Prop :=
  ∀ j, j < t → state source j % 2 = 1

theorem shifted_identity (source t : Nat) :
    2^t * (state source t + 1) =
      3^(oddInputs source t) * (source + 1) + evenDefect source t := by
  induction t with
  | zero => simp [state, oddInputs, evenDefect]
  | succ t ih =>
    by_cases parity : state source t % 2 = 0
    · have edge : 2 * (shortcut (state source t) + 1) = state source t + 2 := by
        simp only [shortcut, parity, ite_true]
        omega
      simp only [state, oddInputs, evenDefect, parity, ite_true, Nat.add_zero,
        Nat.pow_succ]
      calc
        2^t * 2 * (shortcut (state source t) + 1) =
            2^t * (state source t + 2) := by rw [Nat.mul_assoc, edge]
        _ = 2^t * (state source t + 1) + 2^t := by grind
        _ = _ := by rw [ih]; omega
    · have edge : 2 * (shortcut (state source t) + 1) = 3 * (state source t + 1) := by
        simp only [shortcut, parity, ite_false]
        omega
      simp only [state, oddInputs, evenDefect, parity, ite_false, Nat.pow_succ]
      calc
        2^t * 2 * (shortcut (state source t) + 1) =
            2^t * (3 * (state source t + 1)) := by rw [Nat.mul_assoc, edge]
        _ = 3 * (2^t * (state source t + 1)) := by ac_rfl
        _ = _ := by rw [ih]; grind

theorem evenDefect_pos_iff (source t : Nat) :
    0 < evenDefect source t ↔ ∃ j, j < t ∧ state source j % 2 = 0 := by
  induction t with
  | zero => simp [evenDefect]
  | succ t ih =>
    by_cases parity : state source t % 2 = 0
    · have power : 0 < 2^t := Nat.pow_pos (by decide)
      simp only [evenDefect, parity, ite_true]
      constructor
      · intro _; exact ⟨t, by omega, parity⟩
      · intro _; omega
    · simp only [evenDefect, parity, ite_false]
      constructor
      · intro positive
        obtain ⟨j, before, even⟩ := ih.mp (by omega)
        exact ⟨j, by omega, even⟩
      · rintro ⟨j, before, even⟩
        have earlier : j < t := by
          by_cases earlier : j < t
          · exact earlier
          · have same : j = t := by omega
            exact False.elim (parity (same ▸ even))
        have positive := ih.mpr ⟨j, earlier, even⟩
        omega

theorem evenDefect_zero_iff (source t : Nat) :
    evenDefect source t = 0 ↔ AllOdd source t := by
  constructor
  · intro zero j before
    rcases Nat.mod_two_eq_zero_or_one (state source j) with even | odd
    · have positive := (evenDefect_pos_iff source t).mpr ⟨j, before, even⟩
      omega
    · exact odd
  · intro odd
    by_cases zero : evenDefect source t = 0
    · exact zero
    · obtain ⟨j, before, even⟩ := (evenDefect_pos_iff source t).mp (by omega)
      have other := odd j before
      omega

/-- The precise integer form of D_t(source)/(state+1) ≤ 1/(source+1). -/
theorem coefficient_bound (source t : Nat) :
    3^(oddInputs source t) * (source + 1) ≤ 2^t * (state source t + 1) := by
  have exactIdentity := shifted_identity source t
  omega

theorem coefficient_strict_iff (source t : Nat) :
    3^(oddInputs source t) * (source + 1) < 2^t * (state source t + 1) ↔
      ∃ j, j < t ∧ state source j % 2 = 0 := by
  rw [shifted_identity]
  constructor
  · intro strict
    exact (evenDefect_pos_iff source t).mp (by omega)
  · intro even
    have positive := (evenDefect_pos_iff source t).mpr even
    omega

theorem coefficient_eq_iff (source t : Nat) :
    3^(oddInputs source t) * (source + 1) = 2^t * (state source t + 1) ↔
      AllOdd source t := by
  rw [shifted_identity]
  constructor
  · intro equal
    exact (evenDefect_zero_iff source t).mp (by omega)
  · intro odd
    have zero := (evenDefect_zero_iff source t).mpr odd
    omega

theorem allOdd_count (source t : Nat) (odd : AllOdd source t) :
    oddInputs source t = t := by
  induction t with
  | zero => rfl
  | succ t ih =>
    have last := odd t (by omega)
    have previous : AllOdd source t := fun j before => odd j (by omega)
    have count := ih previous
    simp only [oddInputs, count]
    have nonzero : ¬ state source t % 2 = 0 := by omega
    simp [nonzero]

theorem allOdd_shifted_identity (source t : Nat) (odd : AllOdd source t) :
    2^t * (state source t + 1) = 3^t * (source + 1) := by
  have exactIdentity := shifted_identity source t
  rw [allOdd_count source t odd, (evenDefect_zero_iff source t).mpr odd] at exactIdentity
  simpa using exactIdentity

/-- A positive ordinary source cannot support an arbitrarily long all-odd prefix. -/
theorem allOdd_divisibility (source t : Nat) (odd : AllOdd source t) :
    2^t ∣ source + 1 := by
  have divisible : 2^t ∣ 3^t * (source + 1) :=
    ⟨state source t + 1, (allOdd_shifted_identity source t odd).symm⟩
  have coprime : Nat.Coprime (2^t) (3^t) :=
    Nat.gcd_pow_right_of_gcd_eq_one
      (Nat.gcd_pow_left_of_gcd_eq_one (by decide : Nat.gcd 2 3 = 1))
  exact coprime.dvd_of_dvd_mul_left divisible

theorem even_input_before_large_power (source t : Nat) (large : source + 1 < 2^t) :
    ∃ j, j < t ∧ state source j % 2 = 0 := by
  by_cases present : ∃ j, j < t ∧ state source j % 2 = 0
  · exact present
  · have odd : AllOdd source t := by
      intro j before
      rcases Nat.mod_two_eq_zero_or_one (state source j) with even | odd
      · exact False.elim (present ⟨j, before, even⟩)
      · exact odd
    have bound := Nat.le_of_dvd (by omega : 0 < source + 1)
      (allOdd_divisibility source t odd)
    omega

private theorem shortcut_pred_double (q : Nat) (positive : 0 < q) :
    shortcut (2*q-1) = 3*q-1 := by
  unfold shortcut
  split <;> omega

/-- The entire initial all-odd ascent, with an arbitrary positive upper factor. -/
theorem state_pow_two_pred (q j k : Nat) (positive : 0 < q) :
    state (2^(k+j)*q-1) j = 3^j * 2^k * q - 1 := by
  induction j generalizing k with
  | zero => simp [state]
  | succ j ih =>
    have exponents : k+(j+1)=(k+1)+j := by omega
    simp only [state]
    rw [exponents, ih (k+1)]
    have value : 3^j * 2^(k+1) * q = 2 * (3^j * 2^k * q) := by
      rw [Nat.pow_succ]
      ac_rfl
    have valuePositive : 0 < 3^j * 2^k * q :=
      Nat.mul_pos (Nat.mul_pos (Nat.pow_pos (by decide)) (Nat.pow_pos (by decide))) positive
    rw [value, shortcut_pred_double _ valuePositive, Nat.pow_succ]
    congr 1
    ac_rfl

theorem allOdd_pow_two_pred (q k : Nat) (positive : 0 < q) :
    AllOdd (2^k*q-1) k := by
  intro j before
  have exponents : k=(k-j)+j := by omega
  have trace := state_pow_two_pred q j (k-j) positive
  rw [←exponents] at trace
  rw [trace]
  obtain ⟨r, successor⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : k-j ≠ 0)
  rw [successor, Nat.pow_succ]
  have value : 3^j * (2^r*2) * q = 2 * (3^j * 2^r * q) := by ac_rfl
  rw [value]
  have valuePositive : 0 < 3^j * 2^r * q :=
    Nat.mul_pos (Nat.mul_pos (Nat.pow_pos (by decide)) (Nat.pow_pos (by decide))) positive
  omega

theorem initial_ascent (k : Nat) :
    state (2^k-1) k = 3^k-1 ∧ oddInputs (2^k-1) k = k := by
  constructor
  · simpa using state_pow_two_pred 1 k 0 (by decide)
  · have odd : AllOdd (2^k-1) k := by
      simpa using allOdd_pow_two_pred 1 k (by decide)
    exact allOdd_count _ _ odd

private theorem cubic_growth_shifted (j : Nat) :
    8^(j+10) < 3*9^(j+9) := by
  induction j with
  | zero => decide
  | succ j ih =>
    have first : 8^(j+1+10) = 8^(j+10)*8 := by
      rw [show j+1+10=(j+10)+1 by omega, Nat.pow_succ]
    have last : 3*9^(j+9)*9 = 3*9^(j+1+9) := by
      calc
        3*9^(j+9)*9 = 3*(9^(j+9)*9) := by ac_rfl
        _ = 3*9^((j+9)+1) := congrArg (3*·) (Nat.pow_succ 9 (j+9)).symm
        _ = 3*9^(j+1+9) := by congr 2
    calc
      8^(j+1+10) = 8^(j+10)*8 := first
      _ < 3*9^(j+9)*8 := Nat.mul_lt_mul_of_pos_right ih (by decide)
      _ < 3*9^(j+9)*9 :=
        Nat.mul_lt_mul_of_pos_left (by decide)
          (Nat.mul_pos (by decide) (Nat.pow_pos (by decide)))
      _ = 3*9^(j+1+9) := last

/-- A cofinal integer certificate for the negative cubic Green residual.
The real series and its residual are interpreted in GLOBAL_GREEN_MERGER.md. -/
theorem cubic_surplus (k : Nat) (large : 9 ≤ k) :
    8^(k+1) < 3*9^k + 3*3^k + 1 := by
  have shifted := cubic_growth_shifted (k-9)
  have first : k-9+10=k+1 := by omega
  have second : k-9+9=k := by omega
  rw [first,second] at shifted
  omega

theorem cubic_path_certificate (k : Nat) (large : 9 ≤ k) :
    state (2^k-1) k = 3^k-1 ∧
    oddInputs (2^k-1) k = k ∧
    (3^k)^3 + 8^(k+1) < (3^k+1)^3 := by
  have square : 3^k * 3^k = 9^k := by
    simpa using (Nat.mul_pow 3 3 k).symm
  have polynomial : (3^k+1)^3 = (3^k)^3 + 3*9^k + 3*3^k + 1 := by
    simp only [Nat.pow_succ, Nat.pow_zero]
    rw [←square]
    grind
  have surplus := cubic_surplus k large
  refine ⟨(initial_ascent k).1, (initial_ascent k).2, ?_⟩
  omega

end CollatzSourceGreenCoefficient
