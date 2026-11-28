import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Ring

namespace AstraNine.PhysicalInverseBudget

/-- A true positive odd word read from its target. Its last two indices are
the odd depth and the physical total. Requiring the target odd makes the
edge's supplied exponent its exact two-adic valuation. -/
inductive Path : ℕ → ℕ → ℕ → ℕ → Prop where
  | nil (y : ℕ) (positive : 0 < y) (odd : Odd y) : Path y y 0 0
  | edge {y u x e r s : ℕ} (positive : 0 < e) (odd : Odd y)
      (actual : 3*u+1 = 2^e*y) (previous : Path u x r s) :
      Path y x (r+1) (s+e)

/-- A finite overcount of inverse words. Each choice charges its full positive
exponent to the remaining physical budget. Illegal divisions can only enlarge
this overcount. -/
def candidates : ℕ → ℕ → ℕ → Finset ℕ
  | 0, _, y => {y}
  | r+1, budget, y =>
    (Finset.range budget).biUnion fun remaining =>
      candidates r remaining ((2^(budget-remaining)*y-1)/3)

theorem path_mem_candidates {y x r s : ℕ} (path : Path y x r s)
    (budget : ℕ) (fits : s ≤ budget) : x ∈ candidates r budget y := by
  induction path generalizing budget with
  | nil y _ _ => simp [candidates]
  | @edge y u x e r s pos _ actual _ ih =>
    rw [candidates, Finset.mem_biUnion]
    refine ⟨budget-e, Finset.mem_range.mpr (by omega), ?_⟩
    have he : budget-(budget-e) = e := by omega
    rw [he, ← actual]
    have hu : (3*u+1-1)/3 = u := by omega
    rw [hu]
    exact ih _ (by omega)

private theorem sum_choose_column (budget r : ℕ) :
    (∑ i ∈ Finset.range budget, i.choose r) = budget.choose (r+1) := by
  induction budget with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih, Nat.choose_succ_succ]
    exact Nat.add_comm _ _

theorem candidates_card_le (r budget y : ℕ) :
    (candidates r budget y).card ≤ budget.choose r := by
  induction r generalizing budget y with
  | zero => simp [candidates]
  | succ r ih =>
    rw [candidates]
    exact Finset.card_biUnion_le.trans <| (Finset.sum_le_sum
      (fun i _ => ih i ((2^(budget-i)*y-1)/3))).trans_eq
      (sum_choose_column budget r)

/-- At the first low visit the grade fixes one depth per physical target.
The sum ranges over the supplied actual low vertices. -/
theorem many_targets_budget (sources targets : Finset ℕ)
    (depth budget : ℕ → ℕ)
    (cover : ∀ x ∈ sources, ∃ y ∈ targets, ∃ s ≤ budget y, Path y x (depth y) s) :
    sources.card ≤ ∑ y ∈ targets, (budget y).choose (depth y) := by
  have sub : sources ⊆ targets.biUnion (fun y => candidates (depth y) (budget y) y) := by
    intro x hx
    obtain ⟨y, hy, s, hs, path⟩ := cover x hx
    exact Finset.mem_biUnion.mpr ⟨y, hy, path_mem_candidates path _ hs⟩
  exact (Finset.card_le_card sub).trans <| Finset.card_biUnion_le.trans <|
    Finset.sum_le_sum (fun y _ => candidates_card_le (depth y) (budget y) y)

/-- The affine intercept is nonnegative on the full ordinary path. -/
theorem source_height {y x r s : ℕ} (path : Path y x r s) :
    3^r*x ≤ 2^s*y := by
  induction path with
  | nil y _ _ => simp
  | @edge y u x e r s _ _ actual _ ih =>
    calc
      3^(r+1)*x = 3*(3^r*x) := by rw [pow_succ]; ring
      _ ≤ 3*(2^s*u) := Nat.mul_le_mul_left _ ih
      _ = 2^s*(3*u) := by ring
      _ ≤ 2^s*(3*u+1) := Nat.mul_le_mul_left _ (by omega)
      _ = 2^(s+e)*y := by rw [actual, pow_add]; ring

/-- One integer cutoff detects every synchronous side witness with the
specified combined excess, including arbitrarily high sibling exponents. -/
theorem matched_sibling_cutoff {a b x j s h A d : ℕ}
    (sibling : 3*b+1 = 2^(2*h)*(3*a+1))
    (path : Path b x j s) (fits : s+2*h ≤ A+d) :
    3^(j+1)*x ≤ 2^(A+d)*(3*a+1) := by
  calc
    3^(j+1)*x = 3*(3^j*x) := by rw [pow_succ]; ring
    _ ≤ 3*(2^s*b) := Nat.mul_le_mul_left _ (source_height path)
    _ = 2^s*(3*b) := by ring
    _ ≤ 2^s*(3*b+1) := Nat.mul_le_mul_left _ (by omega)
    _ = 2^(s+2*h)*(3*a+1) := by rw [sibling, pow_add]; ring
    _ ≤ 2^(A+d)*(3*a+1) := Nat.mul_le_mul_right _ (Nat.pow_le_pow_right (by decide) fits)

/-- A single positive source cannot belong to two synchronized first-side
cuts. The argument also applies to a finite prefix of a periodic graph. -/
theorem synchronous_cut_unique {α : Type*} (f : α → α) (m x : α)
    (side : ℕ → α) (attach : ∀ j, f (side j) = f^[j+1] m)
    (proper : ∀ j, side j ≠ f^[j] m)
    {j k : ℕ} (hj : f^[j] x = side j) (hk : f^[k] x = side k) : j = k := by
  have exclude : ∀ {u v : ℕ}, u < v → f^[u] x = side u → f^[v] x ≠ side v := by
    intro u v huv hu hv
    have hh : f^[u+1] x = f^[u+1] m := by
      rw [Function.iterate_succ_apply', hu, attach]
    obtain ⟨r, hr⟩ : ∃ r : ℕ, v = r+(u+1) := ⟨v-(u+1), by omega⟩
    apply proper v
    rw [← hv, hr]
    exact (Function.iterate_add_apply f r (u+1) x).trans <|
      (congrArg (f^[r]) hh).trans (Function.iterate_add_apply f r (u+1) m).symm
  rcases lt_trichotomy j k with h | h | h
  · exact False.elim (exclude h hj hk)
  · exact h
  · exact False.elim (exclude h hk hj)

end AstraNine.PhysicalInverseBudget
