import Mathlib.Data.Finset.Max
import Mathlib.Tactic.NormNum

/-!
The exact finite-cut interface in the permanently safe-entry argument.

`clock` is an arbitrary integer-valued cumulative exponent. These theorems
do not assume or prove a global Collatz growth estimate. They prove that
an explicitly supplied nonnegative debt tail gives an actual finite
suffix on which every future prefix obeys the 7/4 gate, and they retain
the corresponding finite clock bound. The analytic manuscript supplies
the debt-tail hypothesis for each ordinary source that never reaches 1.
-/

namespace PermanentSafeDebt

def debt (clock : Nat → Int) (n : Nat) : Int :=
  7 * (n : Int) - 4 * clock n

def SafeAt (clock : Nat → Int) (t : Nat) : Prop :=
  ∀ j : Nat, 4 * (clock (t + j) - clock t) ≤ 7 * (j : Int)

theorem safeAt_iff_tail_minimum (clock : Nat → Int) (t : Nat) :
    SafeAt clock t ↔ ∀ j : Nat, debt clock t ≤ debt clock (t + j) := by
  unfold SafeAt debt
  constructor
  · intro h j
    have hj := h j
    push_cast
    omega
  · intro h j
    have hj := h j
    push_cast at hj
    omega

theorem finite_prefix_minimum (f : Nat → Int) (cut : Nat) :
    ∃ t ≤ cut, ∀ j ≤ cut, f t ≤ f j := by
  have hn : (Finset.range (cut + 1)).Nonempty := ⟨0, by simp⟩
  obtain ⟨t, ht, hmin⟩ := Finset.exists_min_image (Finset.range (cut + 1)) f hn
  refine ⟨t, ?_, ?_⟩
  · simpa only [Finset.mem_range, Nat.lt_succ_iff] using ht
  · intro j hj
    exact hmin j (by simpa only [Finset.mem_range, Nat.lt_succ_iff] using hj)

theorem global_minimum_of_nonnegative_tail (f : Nat → Int) (cut : Nat)
    (hzero : f 0 = 0) (htail : ∀ j : Nat, cut < j → 0 ≤ f j) :
    ∃ t ≤ cut, f t ≤ 0 ∧ ∀ j : Nat, f t ≤ f j := by
  obtain ⟨t, ht, hmin⟩ := finite_prefix_minimum f cut
  have hnonpos : f t ≤ 0 := by simpa only [hzero] using hmin 0 (Nat.zero_le cut)
  refine ⟨t, ht, hnonpos, ?_⟩
  intro j
  by_cases hj : j ≤ cut
  · exact hmin j hj
  · exact hnonpos.trans (htail j (Nat.lt_of_not_ge hj))

theorem bounded_safe_suffix (clock : Nat → Int) (cut : Nat)
    (hzero : clock 0 = 0)
    (htail : ∀ j : Nat, cut < j → 0 ≤ debt clock j) :
    ∃ t ≤ cut, debt clock t ≤ 0 ∧ SafeAt clock t := by
  have hd0 : debt clock 0 = 0 := by simp [debt, hzero]
  obtain ⟨t, ht, hnonpos, hmin⟩ :=
    global_minimum_of_nonnegative_tail (debt clock) cut hd0 htail
  exact ⟨t, ht, hnonpos, (safeAt_iff_tail_minimum clock t).mpr
    (fun j => hmin (t + j))⟩

theorem global_minimum_of_integer_lower_bound (f : Nat → Int) (lower : Int)
    (hlower : ∀ j : Nat, lower ≤ f j) :
    ∃ t : Nat, ∀ j : Nat, f t ≤ f j := by
  classical
  let g : Nat → Nat := fun j => (f j - lower).toNat
  have hex : ∃ m : Nat, ∃ t : Nat, g t = m := ⟨g 0, 0, rfl⟩
  obtain ⟨t, ht⟩ := Nat.find_spec hex
  refine ⟨t, ?_⟩
  intro j
  have hnat : g t ≤ g j := by
    rw [ht]
    exact Nat.find_min' hex ⟨j, rfl⟩
  have hlt := hlower t
  have hlj := hlower j
  dsimp [g] at hnat
  omega

theorem safe_suffix_of_integer_debt_bound (clock : Nat → Int) (lower : Int)
    (hlower : ∀ j : Nat, lower ≤ debt clock j) :
    ∃ t : Nat, SafeAt clock t := by
  obtain ⟨t, hmin⟩ := global_minimum_of_integer_lower_bound (debt clock) lower hlower
  exact ⟨t, (safeAt_iff_tail_minimum clock t).mpr (fun j => hmin (t + j))⟩

theorem safe_suffix_clock_bound (clock : Nat → Int) (t : Nat)
    (h : SafeAt clock t) (j : Nat) :
    4 * clock (t + j) ≤ 7 * (j : Int) + 4 * clock t := by
  have hj := h j
  omega

theorem safeAt_shift (clock : Nat → Int) (t : Nat) :
    SafeAt clock t ↔ SafeAt (fun j => clock (t + j) - clock t) 0 := by
  simp [SafeAt]

theorem eventually_two_not_safe (clock : Nat → Int) (t N : Nat)
    (htwo : ∀ j : Nat, N ≤ j → clock (t + j) - clock t =
      2 * (j : Int) + clock (t + N) - clock t - 2 * (N : Int)) :
    ¬ SafeAt clock t := by
  intro hs
  let C : Int := clock (t + N) - clock t - 2 * (N : Int)
  let j : Nat := (-4 * C).toNat + N + 1
  have hN : N ≤ j := by omega
  have hj : -4 * C < (j : Int) := by omega
  have hjtwo := htwo j hN
  have hsafej := hs j
  dsimp [C] at hj
  omega

end PermanentSafeDebt

#print axioms PermanentSafeDebt.safeAt_iff_tail_minimum
#print axioms PermanentSafeDebt.finite_prefix_minimum
#print axioms PermanentSafeDebt.global_minimum_of_nonnegative_tail
#print axioms PermanentSafeDebt.bounded_safe_suffix
#print axioms PermanentSafeDebt.global_minimum_of_integer_lower_bound
#print axioms PermanentSafeDebt.safe_suffix_of_integer_debt_bound
#print axioms PermanentSafeDebt.safe_suffix_clock_bound
#print axioms PermanentSafeDebt.safeAt_shift
#print axioms PermanentSafeDebt.eventually_two_not_safe
