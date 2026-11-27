import Mathlib.Logic.Function.Iterate
import Mathlib.Data.Finset.Max
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Algebra.Order.BigOperators.GroupWithZero.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Source and clock estimates at the reflected shortcut root 2,
corresponding to the ordinary negative target −2. -/

namespace NegativeShadow

/-- The shortcut map on the absolute values of negative ordinary integers. -/
def step (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3*n-1)/2

private theorem one_fixed (k : ℕ) : step^[k] 1 = 1 :=
  Function.iterate_fixed (show step 1 = 1 by decide) k

private theorem zero_fixed (k : ℕ) : step^[k] 0 = 0 :=
  Function.iterate_fixed (show step 0 = 0 by decide) k

theorem unique_clock {x i j : ℕ} (hi : step^[i] x = 2) (hj : step^[j] x = 2) :
    i = j := by
  wlog hle : i ≤ j generalizing i j
  · exact (this hj hi (by omega)).symm
  by_contra h
  have eq : j = (j-i-1+1)+i := by omega
  rw [eq, Function.iterate_add_apply, hi, Function.iterate_succ_apply,
    show step 2 = 1 by decide, one_fixed] at hj
  contradiction

private theorem no_return {x k d : ℕ} (hit : step^[k] x = 2) (hd : 0 < d) :
    step^[d] x ≠ x := by
  intro h
  have second : step^[k+d] x = 2 := by rw [Function.iterate_add_apply, h, hit]
  have := unique_clock hit second
  omega

private theorem source_ge_two {x k : ℕ} (hit : step^[k] x = 2) : 2 ≤ x := by
  by_contra! h
  have : x = 0 ∨ x = 1 := by omega
  rcases this with rfl | rfl
  · rw [zero_fixed] at hit
    contradiction
  · rw [one_fixed] at hit
    contradiction

def oddInputs (x : ℕ) : ℕ → List ℕ
  | 0 => []
  | k+1 => if x % 2 = 0 then oddInputs (step x) k else x :: oddInputs (step x) k

private theorem odd_mem {x k m : ℕ} (h : m ∈ oddInputs x k) :
    ∃ i < k, step^[i] x = m := by
  induction k generalizing x with
  | zero => simp [oddInputs] at h
  | succ k ih =>
    have lift (hm : m ∈ oddInputs (step x) k) : ∃ i < k+1, step^[i] x = m := by
      obtain ⟨i, hi, hn⟩ := ih hm
      exact ⟨i+1, by omega, by simpa [Function.iterate_succ_apply] using hn⟩
    by_cases even : x % 2 = 0
    · exact lift (by simpa [oddInputs, even] using h)
    · simp only [oddInputs, even, ite_false, List.mem_cons] at h
      rcases h with rfl | h
      · exact ⟨0, by omega, rfl⟩
      · exact lift h

private theorem odd_nodup {x k : ℕ} (hit : step^[k] x = 2) :
    (oddInputs x k).Nodup := by
  induction k generalizing x with
  | zero => simp [oddInputs]
  | succ k ih =>
    have tail : step^[k] (step x) = 2 := by simpa [Function.iterate_succ_apply] using hit
    by_cases even : x % 2 = 0
    · simpa [oddInputs, even] using ih tail
    · simp only [oddInputs, even, ite_false, List.nodup_cons]
      refine ⟨?_, ih tail⟩
      intro bad
      obtain ⟨i, _, hx⟩ := odd_mem bad
      apply no_return hit (d := i+1) (by omega)
      simpa [Function.iterate_succ_apply] using hx

/-- Among distinct integers at least two the product of m/(m−1) is
maximized on the initial interval of the same cardinality. -/
theorem product_bound (t : Finset ℕ) (h : ∀ x ∈ t, 2 ≤ x) :
    ∏ x ∈ t, ((x : ℚ) / (x-1)) ≤ (t.card : ℚ) + 1 := by
  induction t using Finset.induction_on_max with
  | empty => simp
  | insert a t above ih =>
    have ha : 2 ≤ a := h a (Finset.mem_insert_self a t)
    have hn : a ∉ t := fun mem => (above a mem).false
    have hsub : t ⊆ Finset.Ico 2 a := by
      intro x hx
      exact Finset.mem_Ico.mpr ⟨h x (Finset.mem_insert_of_mem hx), above x hx⟩
    have small := Finset.card_le_card hsub
    rw [Nat.card_Ico] at small
    have hc : (t.card : ℚ) + 2 ≤ a := by exact_mod_cast (show t.card+2 ≤ a by omega)
    have hden : (0:ℚ) < a-1 := by
      apply sub_pos.mpr
      exact_mod_cast (show 1 < a by omega)
    have factor : 0 ≤ (a : ℚ)/(a-1) := div_nonneg (by positivity) hden.le
    rw [Finset.prod_insert hn, Finset.card_insert_of_notMem hn, Nat.cast_add, Nat.cast_one]
    refine (mul_le_mul_of_nonneg_left (ih (fun x hx => h x (Finset.mem_insert_of_mem hx))) factor).trans ?_
    rw [div_mul_eq_mul_div, div_le_iff₀ hden]
    nlinarith

def gain (x : ℕ) : ℕ → ℚ
  | 0 => 1
  | k+1 => (if x % 2 = 0 then 1/2 else 3/2) * gain (step x) k

private def correction (x : ℕ) : ℚ := (3*x : ℚ)/(3*x-1)

private theorem gain_formula {x k : ℕ} (hit : step^[k] x = 2) :
    gain x k * x = 2 * ((oddInputs x k).map correction).prod := by
  induction k generalizing x with
  | zero =>
    have hx : x = 2 := hit
    simp [gain, oddInputs, hx]
  | succ k ih =>
    have tail : step^[k] (step x) = 2 := by simpa [Function.iterate_succ_apply] using hit
    have form := ih tail
    have hx := source_ge_two hit
    by_cases even : x % 2 = 0
    · have edge : (2 : ℚ) * (step x) = x := by
        exact_mod_cast (show 2*step x=x by simp only [step, even, ite_true]; omega)
      simp only [gain, oddInputs, even, ite_true]
      rw [← form]
      nlinarith only [congrArg (fun a : ℚ => a * gain (step x) k) edge]
    · have edge : (2 : ℚ) * (step x) = 3*x-1 := by
        have e : 2*step x+1 = 3*x := by simp only [step, even, ite_false]; omega
        exact sub_eq_of_eq_add (by exact_mod_cast (show 3*x = 2*step x+1 from e.symm)) |>.symm
      have hden : (3*(x:ℚ)-1) ≠ 0 := by
        have lo : (2:ℚ) ≤ x := by exact_mod_cast hx
        linarith
      simp only [gain, oddInputs, even, ite_false, List.map_cons, List.prod_cons, correction]
      rw [mul_left_comm (2:ℚ), ← form]
      field_simp
      rw [← edge]
      ring

/-- Every actual inverse word with source −x and target −2 satisfies this
bound using only its count of odd departures. -/
theorem reflected_gain_bound {x k : ℕ} (hit : step^[k] x = 2) :
    gain x k * x ≤ 2 * (((oddInputs x k).length : ℚ) + 1) := by
  let t := (oddInputs x k).toFinset
  have ht (m : ℕ) (hm : m ∈ t) : 2 ≤ m := by
    obtain ⟨i, hi, eq⟩ := odd_mem (List.mem_toFinset.mp hm)
    apply source_ge_two (k := k-i)
    rw [← eq, ← Function.iterate_add_apply, Nat.sub_add_cancel (by omega), hit]
  have comp (m : ℕ) (hm : m ∈ t) : correction m ≤ (m : ℚ)/(m-1) := by
    have lo : (2:ℚ) ≤ m := by exact_mod_cast ht m hm
    unfold correction
    rw [div_le_div_iff₀ (by linarith) (by linarith)]
    nlinarith
  have card : t.card = (oddInputs x k).length := List.toFinset_card_of_nodup (odd_nodup hit)
  rw [gain_formula hit, ← List.prod_toFinset _ (odd_nodup hit)]
  apply mul_le_mul_of_nonneg_left _ (by decide)
  calc
    ∏ m ∈ t, correction m ≤ ∏ m ∈ t, ((m : ℚ)/(m-1)) :=
      Finset.prod_le_prod₀ (fun m hm => by
        have lo : (2:ℚ) ≤ m := by exact_mod_cast ht m hm
        unfold correction
        exact div_nonneg (by positivity) (by linarith)) comp
    _ ≤ (t.card : ℚ)+1 := product_bound t ht
    _ = _ := by rw [card]

#print axioms unique_clock
#print axioms reflected_gain_bound

end NegativeShadow
