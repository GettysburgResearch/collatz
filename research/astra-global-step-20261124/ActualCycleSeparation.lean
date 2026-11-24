import RotationalDistance
import CycleRotation
import Mathlib.Data.Int.NatAbs
import Mathlib.Data.Int.Lemmas

namespace Collatz.ActualCycleSeparation

set_option autoImplicit false

open RotationalDistance

/-- The ordinary shortcut Collatz map on natural numbers. -/
def shortcut (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3*n+1) / 2

def bit (n : ℕ) : Bool := decide (n % 2 = 1)

theorem actual_step (n : ℕ) : Step 1 (bit n) (n : ℤ) (shortcut n : ℤ) := by
  have hm := Nat.mod_lt n (by decide : 0 < 2)
  by_cases he : n % 2 = 0
  · have h : 2 * (n / 2) = n := by omega
    simp only [Step, bit, ↓reduceIte, shortcut, he]
    exact_mod_cast h
  · have hn : n % 2 = 1 := by omega
    have h : 2 * ((3*n+1) / 2) = 3*n+1 := by omega
    simp only [Step, bit, hn, decide_true, ↓reduceIte, shortcut]
    exact_mod_cast h

def itinerary : ℕ → ℕ → List Bool
  | 0, _ => []
  | k+1, n => bit n :: itinerary k (shortcut n)

theorem itinerary_length (k n : ℕ) : (itinerary k n).length = k := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => simp [itinerary, ih]

theorem actual_walk (k n : ℕ) :
    Walk 1 (itinerary k n) (n : ℤ) (shortcut^[k] n : ℤ) := by
  induction k generalizing n with
  | zero => exact Walk.nil _
  | succ k ih =>
    rw [Function.iterate_succ_apply]
    exact Walk.cons (actual_step n) (ih (shortcut n))

/-- Equal ordinary parity words force equality of the starts modulo their
full dyadic word modulus. This statement has no cycle hypothesis. -/
theorem actual_common_run (k n m : ℕ) (h : itinerary k n = itinerary k m) :
    (2 : ℤ)^k ∣ (n : ℤ) - m := by
  have hm := actual_walk k m
  rw [← h] at hm
  simpa only [itinerary_length] using common_run_dvd (actual_walk k n) hm

/-- A common word on two different natural sources cannot be longer than
the binary size of their largest source. -/
theorem distinct_common_run_bound (k n m : ℕ)
    (hne : n ≠ m) (h : itinerary k n = itinerary k m) :
    2^k ≤ max n m := by
  have hd := actual_common_run k n m h
  have hn : (n : ℤ) - m ≠ 0 := by exact sub_ne_zero.mpr (by exact_mod_cast hne)
  have hp : 0 < ((n : ℤ) - m).natAbs := Int.natAbs_pos.mpr hn
  have hdiv : 2^k ∣ ((n : ℤ) - m).natAbs := by
    simpa using Int.natAbs_dvd_natAbs.mpr hd
  exact (Nat.le_of_dvd hp hdiv).trans
    (Int.natAbs_coe_sub_coe_le_of_le (le_max_left n m) (le_max_right n m))

/-- At every phase of every least-period ordinary cycle, a nonidentity
rotation with L common literal bits requires a state at least 2^L.
The clocks, bit word and noncollision come from the actual map. -/
theorem primitive_cycle_common_run_bound (x N r j L : ℕ)
    (hN : 0 < N) (hp : shortcut^[N] x = x)
    (least : ∀ k, 0 < k → k < N → shortcut^[k] x ≠ x)
    (hr : 0 < r) (hrN : r < N)
    (hword : itinerary L (shortcut^[j] x) = itinerary L (shortcut^[j+r] x)) :
    2^L ≤ max (shortcut^[j] x) (shortcut^[j+r] x) := by
  apply distinct_common_run_bound L _ _ _ hword
  exact (CycleRotation.primitive_rotation_ne shortcut x N r j hN hp least hr hrN).symm

#print axioms actual_step
#print axioms actual_walk
#print axioms actual_common_run
#print axioms distinct_common_run_bound
#print axioms primitive_cycle_common_run_bound

end Collatz.ActualCycleSeparation
