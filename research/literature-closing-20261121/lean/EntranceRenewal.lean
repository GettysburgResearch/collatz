module

public import BandMass
public import Mathlib.Topology.Algebra.InfiniteSum.NatInt

@[expose] public section

/-!
# Exact renewal identities for the first dyadic-band entrance

The first entrance is unchanged by any initial power of two.  The entrance
of an unmarked source agrees with the entrance of its next shortcut state;
the corresponding identity at a marked source is the positive return map.
The exceptional odd sources in the resulting renewal equation all have
size at least `2^70`.  These are exact identities, not an assertion that
the exceptional source mass disappears after repeated returns.
-/

namespace CollatzShell.ForwardSection.EntranceRenewal

open BandMass

theorem firstVisit_of_marked {n : ℕ} (mark : Marked n) : firstVisit n = 0 := by
  have hn : 0 < n := by have := mark.1; omega
  exact Nat.eq_zero_of_le_zero (firstVisit_min hn (show Marked (orbit 0 n) from mark))

theorem entrance_of_marked {n : ℕ} (mark : Marked n) : entrance n = n := by
  rw [entrance, firstVisit_of_marked mark]
  rfl

theorem firstVisit_pos_of_not_marked {n : ℕ} (hn : 0 < n)
    (unmarked : ¬ Marked n) : 0 < firstVisit n := by
  have mark := firstVisit_spec n hn
  by_contra! h
  have zero : firstVisit n = 0 := by omega
  rw [zero] at mark
  exact unmarked mark

/-- Removing a first unmarked state subtracts exactly one from the first
entrance clock.  Both inequalities use minimality of the actual entrance. -/
theorem firstVisit_of_not_marked {n : ℕ} (hn : 0 < n)
    (unmarked : ¬ Marked n) : firstVisit n = firstVisit (step n) + 1 := by
  have sn : 0 < step n := by unfold step; split <;> omega
  have upper : firstVisit n ≤ firstVisit (step n) + 1 :=
    firstVisit_min hn (show Marked (orbit (firstVisit (step n) + 1) n) from
      firstVisit_spec (step n) sn)
  have positive := firstVisit_pos_of_not_marked hn unmarked
  obtain ⟨k, hk⟩ : ∃ k, firstVisit n = k + 1 := ⟨firstVisit n - 1, by omega⟩
  have mark := firstVisit_spec n hn
  rw [hk] at mark
  have lower := firstVisit_min sn (show Marked (orbit k (step n)) from mark)
  omega

theorem entrance_of_not_marked {n : ℕ} (hn : 0 < n)
    (unmarked : ¬ Marked n) : entrance n = entrance (step n) := by
  rw [entrance, firstVisit_of_not_marked hn unmarked]
  rfl

theorem next_eq_entrance_step (n : ℕ) : next n = entrance (step n) := rfl

theorem entrance_double (n : ℕ) : entrance (2 * n) = entrance n := by
  by_cases hn : n = 0
  · simp [hn]
  have hp : 0 < 2 * n := by omega
  have hm : ¬ Marked (2 * n) := by intro mark; have := mark.1; omega
  rw [entrance_of_not_marked hp hm, step_double]

/-- Removing all initial even steps preserves the endpoint, including its
full original source fiber. -/
theorem entrance_two_pow_mul (k n : ℕ) : entrance (2 ^ k * n) = entrance n := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [show 2 ^ (k + 1) * n = 2 * (2 ^ k * n) by ring, entrance_double, ih]

theorem entrance_idempotent (n : ℕ) : entrance (entrance n) = entrance n := by
  by_cases hn : 0 < n
  · exact entrance_of_marked (firstVisit_spec n hn)
  · have zero : n = 0 := by omega
    subst n
    rfl

/-- Up to binary height 69 the displayed band inequality admits every odd
source.  This uses the exact section constant 70. -/
theorem small_odd_marked {n : ℕ} (odd : n % 2 = 1) (small : n.log2 ≤ 69) :
    Marked n := by
  refine ⟨odd, ?_⟩
  unfold InSection
  have hn : 0 < n := by omega
  have lower : 2 ^ n.log2 ≤ n := Nat.log2_self_le hn.ne'
  have upper : n < 2 * 2 ^ n.log2 := by
    simpa only [pow_succ, Nat.mul_comm] using (Nat.lt_log2_self (n := n))
  calc
    (n.log2 + 1) * (n - 2 ^ n.log2) ≤ 70 * (n - 2 ^ n.log2) :=
      Nat.mul_le_mul_right _ (by omega)
    _ ≤ 70 * 2 ^ n.log2 := Nat.mul_le_mul_left _ (by omega)

theorem unmarked_odd_log_large {n : ℕ} (odd : n % 2 = 1)
    (unmarked : ¬ Marked n) : 70 ≤ n.log2 := by
  by_contra! small
  exact unmarked (small_odd_marked odd (by omega))

/-- A small total exceptional mass is not zero mass: this theorem locates
its sources but asserts no extinction after further section returns. -/
theorem unmarked_odd_large {n : ℕ} (odd : n % 2 = 1)
    (unmarked : ¬ Marked n) : 2 ^ 70 ≤ n := by
  have hn : 0 < n := by omega
  exact (Nat.pow_le_pow_right (by decide : 0 < 2)
    (unmarked_odd_log_large odd unmarked)).trans (Nat.log2_self_le hn.ne')

/-- A complete entrance fiber retains the weight of each original integer.
The harmless index zero has weight zero. -/
noncomputable def entranceFiberTerm (m n : ℕ) : ℝ :=
  if entrance n = m then ((n : ℝ) ^ 4)⁻¹ else 0

noncomputable def entranceMass (m : ℕ) : ℝ := ∑' n, entranceFiberTerm m n

noncomputable def oddEntranceMass (m : ℕ) : ℝ :=
  ∑' k, entranceFiberTerm m (2 * k + 1)

noncomputable def markedFiberTerm (m k : ℕ) : ℝ :=
  if Marked (2 * k + 1) then entranceFiberTerm m (2 * k + 1) else 0

noncomputable def exceptionalFiberTerm (m k : ℕ) : ℝ :=
  if Marked (2 * k + 1) then 0 else entranceFiberTerm m (2 * k + 1)

noncomputable def exceptionalEntranceMass (m : ℕ) : ℝ :=
  ∑' k, exceptionalFiberTerm m k

noncomputable def markedSourceMass (m : ℕ) : ℝ :=
  if Marked m then ((m : ℝ) ^ 4)⁻¹ else 0

theorem entranceFiberTerm_nonneg (m n : ℕ) : 0 ≤ entranceFiberTerm m n := by
  unfold entranceFiberTerm
  split <;> positivity

theorem entranceFiberTerm_le (m n : ℕ) :
    entranceFiberTerm m n ≤ ((n : ℝ) ^ 4)⁻¹ := by
  unfold entranceFiberTerm
  split
  · exact le_rfl
  · positivity

theorem entranceFiberTerm_summable (m : ℕ) : Summable (entranceFiberTerm m) := by
  apply Summable.of_nonneg_of_le (entranceFiberTerm_nonneg m) (entranceFiberTerm_le m)
  exact Real.summable_nat_pow_inv.mpr (by decide : 1 < 4)

theorem entranceFiberTerm_double (m n : ℕ) :
    entranceFiberTerm m (2 * n) = (1 / 16 : ℝ) * entranceFiberTerm m n := by
  unfold entranceFiberTerm
  rw [entrance_double]
  split
  · norm_num [Nat.cast_mul, mul_pow, mul_inv_rev]
    ring
  · ring

/-- The full even-source contribution is exactly one sixteenth of the
complete entrance law, with no injectivity assumption on entrance fibers. -/
theorem entranceMass_even_odd (m : ℕ) :
    entranceMass m = (1 / 16 : ℝ) * entranceMass m + oddEntranceMass m := by
  have h := entranceFiberTerm_summable m
  have he : Summable (fun k => entranceFiberTerm m (2 * k)) :=
    h.comp_injective (by intro a b hab; omega)
  have ho : Summable (fun k => entranceFiberTerm m (2 * k + 1)) :=
    h.comp_injective (by intro a b hab; change 2 * a + 1 = 2 * b + 1 at hab; omega)
  have split := tsum_even_add_odd he ho
  have even : (∑' k, entranceFiberTerm m (2 * k)) =
      (1 / 16 : ℝ) * entranceMass m := by
    simp_rw [entranceFiberTerm_double]
    simp only [tsum_mul_left, entranceMass]
  rw [even] at split
  exact split.symm

theorem entranceMass_eq_odd (m : ℕ) :
    entranceMass m = (16 / 15 : ℝ) * oddEntranceMass m := by
  have h := entranceMass_even_odd m
  linarith

theorem markedFiberTerm_summable (m : ℕ) : Summable (markedFiberTerm m) := by
  have ho : Summable (fun k => entranceFiberTerm m (2 * k + 1)) :=
    (entranceFiberTerm_summable m).comp_injective
      (by intro a b hab; change 2 * a + 1 = 2 * b + 1 at hab; omega)
  apply Summable.of_nonneg_of_le _ _ ho
  · intro k; unfold markedFiberTerm; split <;> first | positivity | exact entranceFiberTerm_nonneg _ _
  · intro k; unfold markedFiberTerm; split
    · exact le_rfl
    · exact entranceFiberTerm_nonneg _ _

theorem exceptionalFiberTerm_summable (m : ℕ) : Summable (exceptionalFiberTerm m) := by
  have ho : Summable (fun k => entranceFiberTerm m (2 * k + 1)) :=
    (entranceFiberTerm_summable m).comp_injective
      (by intro a b hab; change 2 * a + 1 = 2 * b + 1 at hab; omega)
  apply Summable.of_nonneg_of_le _ _ ho
  · intro k; unfold exceptionalFiberTerm; split <;> first | positivity | exact entranceFiberTerm_nonneg _ _
  · intro k; unfold exceptionalFiberTerm; split
    · exact entranceFiberTerm_nonneg _ _
    · exact le_rfl

theorem markedFiberTerm_sum (m : ℕ) :
    (∑' k, markedFiberTerm m k) = markedSourceMass m := by
  by_cases mark : Marked m
  · have odd := mark.1
    have repr : 2 * (m / 2) + 1 = m := by omega
    rw [tsum_eq_single (m / 2)]
    · simp [markedFiberTerm, repr, mark, entranceFiberTerm, entrance_of_marked mark,
        markedSourceMass]
    · intro k hk
      by_cases mk : Marked (2 * k + 1)
      · have neq : 2 * k + 1 ≠ m := by omega
        simp [markedFiberTerm, mk, entranceFiberTerm, entrance_of_marked mk, neq]
      · simp [markedFiberTerm, mk]
  · rw [show markedSourceMass m = 0 by simp [markedSourceMass, mark]]
    calc
      (∑' k, markedFiberTerm m k) = ∑' _ : ℕ, (0 : ℝ) := by
        apply tsum_congr
        intro k
        by_cases mk : Marked (2 * k + 1)
        · have neq : 2 * k + 1 ≠ m := by intro eq; exact mark (eq ▸ mk)
          simp [markedFiberTerm, mk, entranceFiberTerm, entrance_of_marked mk, neq]
        · simp [markedFiberTerm, mk]
      _ = 0 := tsum_zero

theorem oddEntranceMass_decomposition (m : ℕ) :
    oddEntranceMass m = markedSourceMass m + exceptionalEntranceMass m := by
  have terms : (fun k => entranceFiberTerm m (2 * k + 1)) =
      (fun k => markedFiberTerm m k + exceptionalFiberTerm m k) := by
    funext k
    by_cases h : Marked (2 * k + 1) <;>
      simp [markedFiberTerm, exceptionalFiberTerm, h]
  unfold oddEntranceMass exceptionalEntranceMass
  rw [terms, (markedFiberTerm_summable m).tsum_add (exceptionalFiberTerm_summable m),
    markedFiberTerm_sum]

/-- Exact atomwise renewal equation.  The exceptional term contains all
unmarked odd source fibers and is retained without approximation. -/
theorem entranceMass_renewal (m : ℕ) :
    entranceMass m = (16 / 15 : ℝ) *
      (markedSourceMass m + exceptionalEntranceMass m) := by
  rw [entranceMass_eq_odd, oddEntranceMass_decomposition]

end CollatzShell.ForwardSection.EntranceRenewal
