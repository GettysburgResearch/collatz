import PermanentSafeDebt
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Tactic.Ring

/-!
The ordinary accelerated Collatz map and the exact all-future safe-suffix
equivalence. The proof uses integer fourth powers and a least integer debt;
it does not import a trajectory-distribution theorem or assume Collatz.
-/

namespace PermanentSafeOrdinary

def valuation (n : Nat) : Nat := (3 * n + 1).factorization 2

def oddMap (n : Nat) : Nat := (3 * n + 1) / 2 ^ valuation n

def state (n : Nat) : Nat → Nat
  | 0 => n
  | j + 1 => oddMap (state n j)

def clock (n : Nat) : Nat → Nat
  | 0 => 0
  | j + 1 => clock n j + valuation (state n j)

def Bad (n : Nat) : Prop := ∀ j : Nat, state n j ≠ 1

def PermanentlySafe (n : Nat) : Prop := ∀ j : Nat, 4 * clock n j ≤ 7 * j

theorem exact_step (n : Nat) : 2 ^ valuation n * oddMap n = 3 * n + 1 := by
  simpa only [valuation, oddMap] using
    (Nat.ordProj_mul_ordCompl_eq_self (3 * n + 1) 2)

theorem oddMap_odd (n : Nat) : oddMap n % 2 = 1 := by
  have h : ¬ 2 ∣ oddMap n :=
    Nat.not_dvd_ordCompl Nat.prime_two (show 3 * n + 1 ≠ 0 by omega)
  omega

theorem state_odd (n : Nat) (hn : n % 2 = 1) (j : Nat) : state n j % 2 = 1 := by
  cases j with
  | zero => exact hn
  | succ j => exact oddMap_odd (state n j)

theorem bad_state_lower (n : Nat) (hn : n % 2 = 1) (hb : Bad n) (j : Nat) :
    3 ≤ state n j := by
  have ho := state_odd n hn j
  have hne := hb j
  omega

theorem state_add (n t j : Nat) : state n (t + j) = state (state n t) j := by
  induction j with
  | zero => simp [state]
  | succ j ih =>
    change oddMap (state n (t + j)) = oddMap (state (state n t) j)
    exact congrArg oddMap ih

theorem clock_add (n t j : Nat) : clock n (t + j) = clock n t + clock (state n t) j := by
  induction j with
  | zero => simp [clock]
  | succ j ih =>
    change clock n (t + j) + valuation (state n (t + j)) =
      clock n t + (clock (state n t) j + valuation (state (state n t) j))
    rw [ih, state_add]
    omega

theorem state_eq_iterate (n j : Nat) : state n j = oddMap^[j] n := by
  induction j with
  | zero => rfl
  | succ j ih =>
    rw [state, ih, Function.iterate_succ_apply']

theorem fourth_power_step_bound (x : Nat) (hx : 3 ≤ x) :
    (3 * x + 1) ^ 4 ≤ 128 * x ^ 4 := by
  have hbase : 3 * (3 * x + 1) ≤ 10 * x := by omega
  have hp := Nat.pow_le_pow_left hbase 4
  have he : 81 * (3 * x + 1) ^ 4 ≤ 10000 * x ^ 4 := by
    simpa only [mul_pow, show (3 : Nat) ^ 4 = 81 by decide,
      show (10 : Nat) ^ 4 = 10000 by decide] using hp
  omega

theorem fourth_power_trajectory_bound (n : Nat)
    (hfloor : ∀ j : Nat, 3 ≤ state n j) (j : Nat) :
    2 ^ (4 * clock n j) * (state n j) ^ 4 ≤ 128 ^ j * n ^ 4 := by
  induction j with
  | zero => simp [clock, state]
  | succ j ih =>
    calc
      2 ^ (4 * clock n (j + 1)) * (state n (j + 1)) ^ 4 =
          2 ^ (4 * clock n j) *
            (2 ^ valuation (state n j) * oddMap (state n j)) ^ 4 := by
              simp only [clock, state, mul_add, pow_add, mul_pow, ← pow_mul]
              ring
      _ = 2 ^ (4 * clock n j) * (3 * state n j + 1) ^ 4 := by rw [exact_step]
      _ ≤ 2 ^ (4 * clock n j) * (128 * (state n j) ^ 4) :=
        Nat.mul_le_mul_left _ (fourth_power_step_bound _ (hfloor j))
      _ = 128 * (2 ^ (4 * clock n j) * (state n j) ^ 4) := by ring
      _ ≤ 128 * (128 ^ j * n ^ 4) := Nat.mul_le_mul_left _ ih
      _ = 128 ^ (j + 1) * n ^ 4 := by rw [pow_succ]; ring

theorem cumulative_clock_bound (n : Nat)
    (hfloor : ∀ j : Nat, 3 ≤ state n j) (j : Nat) :
    4 * clock n j ≤ 7 * j + 4 * n := by
  have hsmall : 1 ≤ (state n j) ^ 4 := Nat.one_le_pow 4 _ (by have := hfloor j; omega)
  have hpower : 2 ^ (4 * clock n j) ≤ 2 ^ (7 * j + 4 * n) := by
    calc
      2 ^ (4 * clock n j) ≤ 2 ^ (4 * clock n j) * (state n j) ^ 4 :=
        Nat.le_mul_of_pos_right _ (by omega)
      _ ≤ 128 ^ j * n ^ 4 := fourth_power_trajectory_bound n hfloor j
      _ ≤ 128 ^ j * (2 ^ n) ^ 4 :=
        Nat.mul_le_mul_left _ (Nat.pow_le_pow_left (Nat.le_of_lt n.lt_two_pow_self) 4)
      _ = 2 ^ (7 * j + 4 * n) := by
        rw [show (128 : Nat) = 2 ^ 7 by decide, ← pow_mul, ← pow_mul, ← pow_add]
        congr 1
        omega
  exact (Nat.pow_le_pow_iff_right (by decide : 1 < (2 : Nat))).mp hpower

theorem bad_has_safe_suffix (n : Nat) (hn : n % 2 = 1) (hb : Bad n) :
    ∃ t : Nat, PermanentlySafe (state n t) := by
  have hfloor := bad_state_lower n hn hb
  have hdebt : ∀ j : Nat,
      -(4 * (n : Int)) ≤ PermanentSafeDebt.debt (fun j => (clock n j : Int)) j := by
    intro j
    have h := cumulative_clock_bound n hfloor j
    dsimp only [PermanentSafeDebt.debt]
    omega
  obtain ⟨t, hs⟩ := PermanentSafeDebt.safe_suffix_of_integer_debt_bound
    (fun j => (clock n j : Int)) (-(4 * (n : Int))) hdebt
  refine ⟨t, ?_⟩
  intro j
  have h := hs j
  change 4 * ((clock n (t + j) : Int) - (clock n t : Int)) ≤ 7 * (j : Int) at h
  rw [clock_add, Nat.cast_add] at h
  omega

theorem oddMap_one : oddMap 1 = 1 := by decide +kernel

theorem valuation_one : valuation 1 = 2 := by decide +kernel

theorem state_one (j : Nat) : state 1 j = 1 := by
  induction j with
  | zero => rfl
  | succ j ih => simp only [state, ih, oddMap_one]

theorem clock_one (j : Nat) : clock 1 j = 2 * j := by
  induction j with
  | zero => rfl
  | succ j ih => simp only [clock, state_one, valuation_one, ih]; omega

theorem safe_is_bad (n : Nat) (hs : PermanentlySafe n) : Bad n := by
  intro t ht
  have h := hs (t + (7 * t + 1))
  rw [clock_add, ht, clock_one] at h
  omega

theorem safe_suffix_implies_bad (n t : Nat) (hs : PermanentlySafe (state n t)) : Bad n := by
  have hb := safe_is_bad (state n t) hs
  intro j hj
  apply hb j
  calc
    state (state n t) j = state n (t + j) := (state_add n t j).symm
    _ = state n (j + t) := by rw [Nat.add_comm t j]
    _ = state (state n j) t := state_add n j t
    _ = 1 := by rw [hj, state_one]

theorem bad_iff_safe_suffix (n : Nat) (hn : n % 2 = 1) :
    Bad n ↔ ∃ t : Nat, PermanentlySafe (state n t) := by
  exact ⟨bad_has_safe_suffix n hn, fun ⟨t, ht⟩ => safe_suffix_implies_bad n t ht⟩

theorem not_safe_iff_prefix_failure (n : Nat) :
    ¬ PermanentlySafe n ↔ ∃ j : Nat, 7 * j < 4 * clock n j := by
  classical
  simp only [PermanentlySafe, not_forall, not_le]

theorem all_odd_converge_iff_no_safe_source :
    (∀ n : Nat, n % 2 = 1 → ∃ j : Nat, state n j = 1) ↔
    (∀ n : Nat, n % 2 = 1 → ¬ PermanentlySafe n) := by
  classical
  constructor
  · intro hall n hn hs
    obtain ⟨j, hj⟩ := hall n hn
    exact safe_is_bad n hs j hj
  · intro hnone n hn
    by_contra hfail
    have hb : Bad n := by simpa only [Bad, not_exists] using hfail
    obtain ⟨t, ht⟩ := bad_has_safe_suffix n hn hb
    exact hnone (state n t) (state_odd n hn t) ht

theorem all_odd_converge_iff_prefix_gate_fails :
    (∀ n : Nat, n % 2 = 1 → ∃ j : Nat, state n j = 1) ↔
    (∀ n : Nat, n % 2 = 1 → ∃ j : Nat, 7 * j < 4 * clock n j) := by
  rw [all_odd_converge_iff_no_safe_source]
  simp only [not_safe_iff_prefix_failure]

end PermanentSafeOrdinary

#print axioms PermanentSafeOrdinary.exact_step
#print axioms PermanentSafeOrdinary.oddMap_odd
#print axioms PermanentSafeOrdinary.state_odd
#print axioms PermanentSafeOrdinary.bad_state_lower
#print axioms PermanentSafeOrdinary.state_add
#print axioms PermanentSafeOrdinary.clock_add
#print axioms PermanentSafeOrdinary.state_eq_iterate
#print axioms PermanentSafeOrdinary.fourth_power_step_bound
#print axioms PermanentSafeOrdinary.fourth_power_trajectory_bound
#print axioms PermanentSafeOrdinary.cumulative_clock_bound
#print axioms PermanentSafeOrdinary.bad_has_safe_suffix
#print axioms PermanentSafeOrdinary.oddMap_one
#print axioms PermanentSafeOrdinary.valuation_one
#print axioms PermanentSafeOrdinary.state_one
#print axioms PermanentSafeOrdinary.clock_one
#print axioms PermanentSafeOrdinary.safe_is_bad
#print axioms PermanentSafeOrdinary.safe_suffix_implies_bad
#print axioms PermanentSafeOrdinary.bad_iff_safe_suffix
#print axioms PermanentSafeOrdinary.not_safe_iff_prefix_failure
#print axioms PermanentSafeOrdinary.all_odd_converge_iff_no_safe_source
#print axioms PermanentSafeOrdinary.all_odd_converge_iff_prefix_gate_fails
