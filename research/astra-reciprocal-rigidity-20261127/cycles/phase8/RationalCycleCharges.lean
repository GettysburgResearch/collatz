import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Exact finite arithmetic behind the denominator-uniform cyclic charge estimate. -/

namespace CollatzResearch.RationalCycleCharges

/-- Least partial sum, including the empty prefix. -/
def floorPrefix : List ℚ → ℚ
  | [] => 0
  | q :: w => min 0 (q + floorPrefix w)

theorem floorPrefix_nonpos (w : List ℚ) : floorPrefix w ≤ 0 := by
  cases w with
  | nil => rfl
  | cons q qs => exact min_le_left _ _

theorem floorPrefix_le_take (w : List ℚ) (n : ℕ) :
    floorPrefix w ≤ (w.take n).sum := by
  induction w generalizing n with
  | nil => simp [floorPrefix]
  | cons q qs ih =>
    cases n with
    | zero => simpa using floorPrefix_nonpos (q :: qs)
    | succ n =>
      simp only [List.take_succ_cons, List.sum_cons, floorPrefix]
      exact (min_le_right _ _).trans (add_le_add_right (ih n) q)

theorem floorPrefix_append (v w : List ℚ) :
    floorPrefix (v ++ w) = min (floorPrefix v) (v.sum + floorPrefix w) := by
  induction v with
  | nil => simp [floorPrefix, min_eq_right (floorPrefix_nonpos w)]
  | cons q qs ih =>
    simp only [List.cons_append, floorPrefix, ih, List.sum_cons,
      add_min, min_assoc, add_assoc]

/-- A completed nonnegative lap cannot lower the minimum of its proper prefixes. -/
theorem floorPrefix_last (w : List ℚ) (q : ℚ) (lap : 0 ≤ w.sum + q) :
    floorPrefix (w ++ [q]) = floorPrefix w := by
  rw [floorPrefix_append]
  have whole : floorPrefix w ≤ w.sum := by
    simpa using floorPrefix_le_take w w.length
  simp only [floorPrefix, add_zero, add_min]
  exact min_eq_left (le_min whole ((floorPrefix_nonpos w).trans lap))

/-- Charge at the initial cut, computed using only the actual finite cyclic word. -/
def charge (q : ℚ) (tail : List ℚ) : ℚ :=
  q + floorPrefix (tail ++ [q]) - floorPrefix (q :: tail)

theorem charge_eq (q : ℚ) (tail : List ℚ) (lap : 0 ≤ tail.sum + q) :
    charge q tail = max 0 (q + floorPrefix tail) := by
  rw [charge, floorPrefix_last tail q lap, floorPrefix]
  by_cases h : 0 ≤ q + floorPrefix tail
  · rw [min_eq_left h, max_eq_right h, sub_zero]
  · rw [min_eq_right (le_of_not_ge h), max_eq_left (le_of_not_ge h), sub_self]

theorem charge_spec (q : ℚ) (tail : List ℚ) (lap : 0 ≤ tail.sum + q) :
    0 ≤ charge q tail ∧
    (0 < charge q tail → charge q tail ≤ q ∧ ∀ n, 0 < q + (tail.take n).sum) := by
  rw [charge_eq q tail lap]
  refine ⟨le_max_left _ _, ?_⟩
  intro pos
  have h : 0 < q + floorPrefix tail := by
    rcases lt_max_iff.mp pos with hp | hp
    · exact False.elim ((lt_irrefl _) hp)
    · exact hp
  rw [max_eq_right h.le]
  refine ⟨by linarith [floorPrefix_nonpos tail], ?_⟩
  intro n
  exact h.trans_le (add_le_add_right (floorPrefix_le_take tail n) q)

/-- A potential returns to its initial value after a lap, so its differences telescope. -/
theorem lap_sum (q potential : ℕ → ℚ) (n : ℕ) (closed : potential n = potential 0) :
    ∑ i ∈ Finset.range n, (q i + potential (i+1) - potential i) =
    ∑ i ∈ Finset.range n, q i := by
  have sum_step (k : ℕ) :
      ∑ i ∈ Finset.range k, (q i + potential (i+1) - potential i) =
      (∑ i ∈ Finset.range k, q i) + potential k - potential 0 := by
    induction k with
    | zero => simp
    | succ k ih => rw [Finset.sum_range_succ, ih, Finset.sum_range_succ]; ring
  rw [sum_step n, closed]
  ring

/-- Finite discrete Gronwall bound; no positivity of the starting value is needed. -/
theorem reciprocal_growth (r : ℕ → ℚ) (c : ℚ) (hc : 0 ≤ c)
    (hprefix : ∀ j, r j ≤ r 0 + c * ∑ i ∈ Finset.range j, r i) (j : ℕ) :
    r j ≤ r 0 * (1+c)^j := by
  let major (k : ℕ) := r 0 + c * ∑ i ∈ Finset.range k, r i
  have major_bound (k : ℕ) : major k ≤ r 0 * (1+c)^k := by
    induction k with
    | zero => simp [major]
    | succ k ih =>
      have update : major (k+1) = major k + c * r k := by
        simp only [major, Finset.sum_range_succ]
        ring
      calc
        major (k+1) = major k + c * r k := update
        _ ≤ major k + c * major k := by
          exact add_le_add_right (mul_le_mul_of_nonneg_left (hprefix k) hc) _
        _ = major k * (1+c) := by ring
        _ ≤ (r 0 * (1+c)^k) * (1+c) :=
          mul_le_mul_of_nonneg_right ih (by linarith)
        _ = r 0 * (1+c)^(k+1) := by rw [pow_succ]; ring
  exact (hprefix j).trans (major_bound j)

/-- All nonnegative partial charges imply the reciprocal prefix comparison for the
actual bounded majorants and their rational endpoint coboundaries. -/
theorem charged_reciprocal_growth (r b q : ℕ → ℚ) (B : ℚ) (hB : 0 < B)
    (hq : ∀ i, q i = b i + B * (r i - r (i+1)))
    (hb : ∀ i, b i ≤ r i / 2)
    (nonneg : ∀ k, 0 ≤ ∑ i ∈ Finset.range k, q i) (j : ℕ) :
    r j ≤ r 0 * (1 + 1/(2*B))^j := by
  have sum_eq (k : ℕ) : ∑ i ∈ Finset.range k, q i =
      (∑ i ∈ Finset.range k, b i) + B * (r 0 - r k) := by
    induction k with
    | zero => simp
    | succ k ih => rw [Finset.sum_range_succ, ih, hq, Finset.sum_range_succ]; ring
  apply reciprocal_growth r (1/(2*B)) (div_nonneg (by norm_num) (mul_nonneg (by norm_num) hB.le)) _ j
  intro k
  have total : ∑ i ∈ Finset.range k, b i ≤ (∑ i ∈ Finset.range k, r i) / 2 := by
    induction k with
    | zero => simp
    | succ k ih =>
      rw [Finset.sum_range_succ, Finset.sum_range_succ]
      linarith only [ih, hb k]
  have h := nonneg k
  rw [sum_eq k] at h
  have scalar : B * (1 / (2 * B)) = 1/2 := by field_simp [ne_of_gt hB]
  apply le_of_mul_le_mul_left _ hB
  rw [mul_add, ← mul_assoc, scalar]
  linarith only [h, total]

#print axioms floorPrefix_last
#print axioms charge_spec
#print axioms lap_sum
#print axioms reciprocal_growth
#print axioms charged_reciprocal_growth

end CollatzResearch.RationalCycleCharges
