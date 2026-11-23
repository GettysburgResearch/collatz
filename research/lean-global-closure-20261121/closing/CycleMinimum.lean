import Mathlib.Algebra.BigOperators.Field
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Rat.Lemmas
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum

/-!
An exact minimum bound for an arbitrary finite ordinary cycle.

The hypothesis contains every equation `2^(a i) * x (next i) = 3*x i+1`
and a permutation of the full state list. No bound on period, valuation
alphabet, number of runs, or block complexity is used. The theorem does
not exclude all cycles. Its consumer is the written zero-atom count.
-/

open scoped BigOperators

namespace CollatzCycleMinimum

theorem product_deficit_le_sum {ι : Type*} (s : Finset ι) (f : ι → ℚ)
    (h0 : ∀ i ∈ s, 0 ≤ f i) (h1 : ∀ i ∈ s, f i ≤ 1) :
    1 - ∏ i ∈ s, (1 - f i) ≤ ∑ i ∈ s, f i := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | @insert a s ha ih =>
      have ha0 := h0 a (Finset.mem_insert_self a s)
      have ha1 := h1 a (Finset.mem_insert_self a s)
      have hs0 : ∀ i ∈ s, 0 ≤ f i := fun i hi => h0 i (Finset.mem_insert_of_mem hi)
      have hs1 : ∀ i ∈ s, f i ≤ 1 := fun i hi => h1 i (Finset.mem_insert_of_mem hi)
      have hi := ih hs0 hs1
      have hsum : 0 ≤ ∑ i ∈ s, f i := Finset.sum_nonneg hs0
      have hmul := mul_le_mul_of_nonneg_left hi (sub_nonneg.mpr ha1)
      have hc := mul_nonneg ha0 hsum
      rw [Finset.prod_insert ha, Finset.sum_insert ha]
      nlinarith

theorem minimum_product_deficit {p : ℕ} (x : Fin p → ℚ) (m : ℚ)
    (hm : 0 < m) (hmin : ∀ i, m ≤ x i) :
    (1 - ∏ i, (3 * x i / (3 * x i + 1))) * (3 * m + 1) ≤ p := by
  have hden : 0 < 3 * m + 1 := by linarith
  have hx : ∀ i, 0 < x i := fun i => lt_of_lt_of_le hm (hmin i)
  have hxi : ∀ i, 0 < 3 * x i + 1 := fun i => by linarith [hx i]
  have hf0 : ∀ i ∈ (Finset.univ : Finset (Fin p)), 0 ≤ 1 / (3 * x i + 1) :=
    fun i _ => le_of_lt (one_div_pos.mpr (hxi i))
  have hf1 : ∀ i ∈ (Finset.univ : Finset (Fin p)), 1 / (3 * x i + 1) ≤ 1 := by
    intro i _
    apply (div_le_iff₀ (hxi i)).mpr
    linarith [hx i]
  have hu := product_deficit_le_sum Finset.univ (fun i => 1 / (3 * x i + 1)) hf0 hf1
  have hp : (∏ i, (1 - 1 / (3 * x i + 1))) =
      ∏ i, (3 * x i / (3 * x i + 1)) := by
    apply Finset.prod_congr rfl
    intro i _
    field_simp [ne_of_gt (hxi i)]
    simp
  rw [hp] at hu
  have hs : (∑ i, 1 / (3 * x i + 1)) ≤ (p : ℚ) / (3 * m + 1) := by
    calc
      (∑ i, 1 / (3 * x i + 1)) ≤ ∑ _i : Fin p, 1 / (3 * m + 1) := by
        apply Finset.sum_le_sum
        intro i _
        apply one_div_le_one_div_of_le hden
        linarith [hmin i]
      _ = (p : ℚ) / (3 * m + 1) := by simp [div_eq_mul_inv]
  exact (le_div_iff₀ hden).mp (le_trans hu hs)

theorem whole_cycle_ratio {p : ℕ} (x : Fin p → ℚ) (a : Fin p → ℕ)
    (next : Equiv.Perm (Fin p)) (hx : ∀ i, 0 < x i)
    (hedge : ∀ i, (2 : ℚ) ^ a i * x (next i) = 3 * x i + 1) :
    (∏ i, (3 * x i / (3 * x i + 1))) = (3 : ℚ) ^ p / 2 ^ (∑ i, a i) := by
  have hperm : (∏ i, x (next i)) = ∏ i, x i :=
    Fintype.prod_equiv next _ _ (fun _ => rfl)
  have hprod : (∏ i, (3 * x i + 1)) = (2 : ℚ) ^ (∑ i, a i) * ∏ i, x i := by
    calc
      (∏ i, (3 * x i + 1)) = ∏ i, ((2 : ℚ) ^ a i * x (next i)) := by
        apply Finset.prod_congr rfl
        intro i _
        exact (hedge i).symm
      _ = (2 : ℚ) ^ (∑ i, a i) * ∏ i, x i := by
        rw [Finset.prod_mul_distrib, Finset.prod_pow_eq_pow_sum, hperm]
  have hX : (∏ i, x i) ≠ 0 := Finset.prod_ne_zero_iff.mpr (fun i _ => ne_of_gt (hx i))
  rw [Finset.prod_div_distrib, Finset.prod_mul_distrib, hprod]
  simp only [Finset.prod_const, Finset.card_univ, Fintype.card_fin]
  exact mul_div_mul_right _ _ hX

theorem whole_cycle_minimum_rat {p : ℕ} (x : Fin p → ℚ) (a : Fin p → ℕ)
    (next : Equiv.Perm (Fin p)) (m : ℚ) (hm : 0 < m)
    (hmin : ∀ i, m ≤ x i)
    (hedge : ∀ i, (2 : ℚ) ^ a i * x (next i) = 3 * x i + 1) :
    ((2 : ℚ) ^ (∑ i, a i) - 3 ^ p) * (3 * m + 1) ≤ p * 2 ^ (∑ i, a i) := by
  have hd := minimum_product_deficit x m hm hmin
  rw [whole_cycle_ratio x a next (fun i => lt_of_lt_of_le hm (hmin i)) hedge] at hd
  have h2 : 0 < (2 : ℚ) ^ (∑ i, a i) := by positivity
  have hs : 1 - (3 : ℚ) ^ p / 2 ^ (∑ i, a i) =
      (2 ^ (∑ i, a i) - 3 ^ p) / 2 ^ (∑ i, a i) := by field_simp
  rw [hs, div_mul_eq_mul_div] at hd
  exact (div_le_iff₀ h2).mp hd

theorem whole_cycle_minimum_nat {p : ℕ} (x : Fin p → ℕ) (a : Fin p → ℕ)
    (next : Equiv.Perm (Fin p)) (m D : ℕ) (hm : 0 < m)
    (hmin : ∀ i, m ≤ x i)
    (hedge : ∀ i, 2 ^ a i * x (next i) = 3 * x i + 1)
    (hD : D + 3 ^ p = 2 ^ (∑ i, a i)) :
    D * (3 * m + 1) ≤ p * 2 ^ (∑ i, a i) := by
  have hh : ∀ i, (2 : ℚ) ^ a i * (x (next i) : ℚ) = 3 * (x i : ℚ) + 1 := by
    intro i
    exact_mod_cast hedge i
  have hmr : (0 : ℚ) < m := by exact_mod_cast hm
  have hxr : ∀ i, (m : ℚ) ≤ x i := by intro i; exact_mod_cast hmin i
  have hr := whole_cycle_minimum_rat (fun i => (x i : ℚ)) a next m hmr hxr hh
  have hDr : (D : ℚ) + 3 ^ p = 2 ^ (∑ i, a i) := by exact_mod_cast hD
  rw [← hDr] at hr
  have hres : (D : ℚ) * (3 * (m : ℚ) + 1) ≤ p * 2 ^ (∑ i, a i) := by
    nlinarith only [hr, hDr]
  exact_mod_cast hres

end CollatzCycleMinimum
