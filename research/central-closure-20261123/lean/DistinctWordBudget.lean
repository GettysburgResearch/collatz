import Mathlib.Tactic
import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Algebra.Order.BigOperators.Ring.Finset

/-!
An exact finite arithmetic core for the distinct-gap-word count.

`h s` counts selected positive compositions with total cost `s+1`.
The capacity bound `h s ≤ s.choose k` corresponds to words of length `k+1`.
The Collatz word injection, the sliding cost bound, and the Stirling
asymptotic remain written mathematics in COLLISION_LOGARITHMIC_GAIN.md.
-/

open scoped BigOperators

namespace CollatzDistinctWordBudget

theorem choose_prefix_sum (K k : ℕ) :
    (∑ s ∈ Finset.range K, s.choose k) = K.choose (k+1) := by
  induction K with
  | zero => simp
  | succ K ih =>
      rw [Finset.sum_range_succ, ih, Nat.choose_succ_succ]
      simp [Nat.succ_eq_add_one, Nat.add_comm]

theorem weighted_choose_sum (K k : ℕ) :
    (∑ s ∈ Finset.range K, (K-(s+1)) * s.choose k) =
      K.choose (k+2) := by
  induction K with
  | zero => simp
  | succ K ih =>
      rw [Finset.sum_range_succ]
      simp only [Nat.succ_sub_succ_eq_sub, Nat.sub_self, zero_mul, add_zero]
      have heq :
          (∑ s ∈ Finset.range K, (K-s) * s.choose k) =
          (∑ s ∈ Finset.range K, ((K-(s+1))+1) * s.choose k) := by
        apply Finset.sum_congr rfl
        intro s hs
        have hs' : s < K := Finset.mem_range.mp hs
        congr 1
        omega
      rw [heq]
      simp only [Nat.add_mul, one_mul, Finset.sum_add_distrib]
      rw [ih, choose_prefix_sum]
      rw [Nat.add_comm (K.choose (k+2)) (K.choose (k+1))]
      simpa only [Nat.succ_eq_add_one, Nat.add_assoc] using
        (Nat.choose_succ_succ K (k+1)).symm

theorem squared_weighted_choose_sum (K k : ℕ) :
    (∑ s ∈ Finset.range K, (K-(s+1))^2 * s.choose k) =
      K.choose (k+2) + 2 * K.choose (k+3) := by
  induction K with
  | zero => simp
  | succ K ih =>
      rw [Finset.sum_range_succ]
      simp only [Nat.succ_sub_succ_eq_sub, Nat.sub_self, zero_pow (by decide : 2 ≠ 0),
        zero_mul, add_zero]
      have heq :
          (∑ s ∈ Finset.range K, (K-s)^2 * s.choose k) =
          (∑ s ∈ Finset.range K,
            ((K-(s+1))^2 * s.choose k +
              2 * ((K-(s+1)) * s.choose k) + s.choose k)) := by
        apply Finset.sum_congr rfl
        intro s hs
        have hs' : s < K := Finset.mem_range.mp hs
        have hsub : K-s = K-(s+1)+1 := by omega
        rw [hsub]
        ring
      rw [heq]
      simp only [Finset.sum_add_distrib, ← Finset.mul_sum]
      rw [ih, weighted_choose_sum, choose_prefix_sum]
      have h2 : (K+1).choose (k+2) = K.choose (k+1) + K.choose (k+2) := by
        simpa only [Nat.succ_eq_add_one, Nat.add_assoc] using
          Nat.choose_succ_succ K (k+1)
      have h3 : (K+1).choose (k+3) = K.choose (k+2) + K.choose (k+3) := by
        simpa only [Nat.succ_eq_add_one, Nat.add_assoc] using
          Nat.choose_succ_succ K (k+2)
      rw [h2,h3]
      omega

theorem histogram_deficit_le (h : ℕ → ℕ) (K L k : ℕ)
    (hcap : ∀ s, h s ≤ s.choose k) :
    (∑ s ∈ Finset.range L, (K-(s+1)) * h s) ≤ K.choose (k+2) := by
  let F := (Finset.range L).filter (fun s => s < K)
  have hrestrict :
      (∑ s ∈ Finset.range L, (K-(s+1)) * h s) =
      ∑ s ∈ F, (K-(s+1)) * h s := by
    symm
    apply Finset.sum_subset
    · exact Finset.filter_subset _ _
    · intro s hs hsF
      have hnot : ¬ s < K := by
        intro hlt
        exact hsF (Finset.mem_filter.mpr ⟨hs,hlt⟩)
      have hz : K-(s+1) = 0 := by omega
      simp [hz]
  rw [hrestrict]
  calc
    (∑ s ∈ F, (K-(s+1)) * h s) ≤
        ∑ s ∈ F, (K-(s+1)) * s.choose k := by
      apply Finset.sum_le_sum
      intro s hs
      exact Nat.mul_le_mul_left _ (hcap s)
    _ ≤ ∑ s ∈ Finset.range K, (K-(s+1)) * s.choose k := by
      apply Finset.sum_le_sum_of_subset
      intro s hs
      exact Finset.mem_range.mpr (Finset.mem_filter.mp hs).2
    _ = K.choose (k+2) := weighted_choose_sum K k

theorem histogram_cost_budget (h : ℕ → ℕ) (K L k : ℕ)
    (hcap : ∀ s, h s ≤ s.choose k) :
    K * (∑ s ∈ Finset.range L, h s) ≤
      (∑ s ∈ Finset.range L, (s+1) * h s) + K.choose (k+2) := by
  have hpoint (s : ℕ) : K * h s ≤
      (s+1) * h s + (K-(s+1)) * h s := by
    rw [← Nat.add_mul]
    exact Nat.mul_le_mul_right _ (by omega : K ≤ s+1+(K-(s+1)))
  calc
    K * (∑ s ∈ Finset.range L, h s) =
        ∑ s ∈ Finset.range L, K * h s := by rw [Finset.mul_sum]
    _ ≤ ∑ s ∈ Finset.range L,
        ((s+1) * h s + (K-(s+1)) * h s) :=
      Finset.sum_le_sum (fun s _ => hpoint s)
    _ = (∑ s ∈ Finset.range L, (s+1) * h s) +
        (∑ s ∈ Finset.range L, (K-(s+1)) * h s) := by
      rw [Finset.sum_add_distrib]
    _ ≤ (∑ s ∈ Finset.range L, (s+1) * h s) + K.choose (k+2) :=
      Nat.add_le_add_left (histogram_deficit_le h K L k hcap) _

theorem histogram_squared_deficit_le (h : ℕ → ℕ) (K L k : ℕ)
    (hcap : ∀ s, h s ≤ s.choose k) :
    (∑ s ∈ Finset.range L, (K-(s+1))^2 * h s) ≤
      K.choose (k+2) + 2 * K.choose (k+3) := by
  let F := (Finset.range L).filter (fun s => s < K)
  have hrestrict :
      (∑ s ∈ Finset.range L, (K-(s+1))^2 * h s) =
      ∑ s ∈ F, (K-(s+1))^2 * h s := by
    symm
    apply Finset.sum_subset
    · exact Finset.filter_subset _ _
    · intro s hs hsF
      have hnot : ¬ s < K := by
        intro hlt
        exact hsF (Finset.mem_filter.mpr ⟨hs,hlt⟩)
      have hz : K-(s+1) = 0 := by omega
      simp [hz]
  rw [hrestrict]
  calc
    (∑ s ∈ F, (K-(s+1))^2 * h s) ≤
        ∑ s ∈ F, (K-(s+1))^2 * s.choose k := by
      apply Finset.sum_le_sum
      intro s hs
      exact Nat.mul_le_mul_left _ (hcap s)
    _ ≤ ∑ s ∈ Finset.range K, (K-(s+1))^2 * s.choose k := by
      apply Finset.sum_le_sum_of_subset
      intro s hs
      exact Finset.mem_range.mpr (Finset.mem_filter.mp hs).2
    _ = K.choose (k+2) + 2 * K.choose (k+3) := squared_weighted_choose_sum K k

/-- The finite Cauchy core. The capacity input is the unweighted sum of
squared positive deficits over distinct support words, not a probability
average and not a fresh random source. -/
theorem finite_collision_budget {ι : Type*} (W : Finset ι)
    (p c : ι → ℝ) (K B Q : ℝ)
    (hp : ∀ i ∈ W, 0 ≤ p i)
    (hmass : ∑ i ∈ W, p i = 1)
    (hmean : ∑ i ∈ W, p i * c i ≤ B)
    (hcapacity : ∑ i ∈ W, (max 0 (K-c i))^2 ≤ Q)
    (hmargin : B ≤ K) :
    (K-B)^2 ≤ Q * (∑ i ∈ W, (p i)^2) := by
  let d : ι → ℝ := fun i => max 0 (K-c i)
  have hdeficit : K-B ≤ ∑ i ∈ W, p i * d i := by
    calc
      K-B ≤ K-(∑ i ∈ W, p i * c i) := sub_le_sub_left hmean K
      _ = ∑ i ∈ W, p i * (K-c i) := by
        simp only [mul_sub, Finset.sum_sub_distrib, ← Finset.sum_mul, hmass, one_mul]
      _ ≤ ∑ i ∈ W, p i * d i := by
        apply Finset.sum_le_sum
        intro i hi
        exact mul_le_mul_of_nonneg_left (le_max_right _ _) (hp i hi)
  have hdelta : 0 ≤ K-B := sub_nonneg.mpr hmargin
  have hpair : 0 ≤ ∑ i ∈ W, p i * d i := hdelta.trans hdeficit
  have hsquare : (K-B)^2 ≤ (∑ i ∈ W, p i * d i)^2 := by
    nlinarith
  have hcs := Finset.sum_mul_sq_le_sq_mul_sq W p d
  have hp2 : 0 ≤ ∑ i ∈ W, (p i)^2 :=
    Finset.sum_nonneg (fun i _ => sq_nonneg (p i))
  have hcap' : ∑ i ∈ W, (d i)^2 ≤ Q := hcapacity
  calc
    (K-B)^2 ≤ (∑ i ∈ W, p i * d i)^2 := hsquare
    _ ≤ (∑ i ∈ W, (p i)^2) * (∑ i ∈ W, (d i)^2) := hcs
    _ ≤ (∑ i ∈ W, (p i)^2) * Q := mul_le_mul_of_nonneg_left hcap' hp2
    _ = Q * (∑ i ∈ W, (p i)^2) := mul_comm _ _

theorem mean_cost_budget (h : ℕ → ℕ) (K L k : ℕ) (B : ℝ)
    (hcap : ∀ s, h s ≤ s.choose k)
    (hmean : (∑ s ∈ Finset.range L, ((s+1) * h s : ℕ) : ℝ) ≤
      B * (∑ s ∈ Finset.range L, h s : ℕ)) :
    ((K : ℝ)-B) * (∑ s ∈ Finset.range L, h s : ℕ) ≤
      (K.choose (k+2) : ℝ) := by
  have hbudget := histogram_cost_budget h K L k hcap
  have hbudget' :
      (K : ℝ) * (∑ s ∈ Finset.range L, h s : ℕ) ≤
      (∑ s ∈ Finset.range L, ((s+1) * h s : ℕ) : ℝ) +
      (K.choose (k+2) : ℝ) := by
    exact_mod_cast hbudget
  nlinarith

theorem count_le_choose_of_mean (h : ℕ → ℕ) (K L k : ℕ) (B : ℝ)
    (hcap : ∀ s, h s ≤ s.choose k)
    (hmean : (∑ s ∈ Finset.range L, ((s+1) * h s : ℕ) : ℝ) ≤
      B * (∑ s ∈ Finset.range L, h s : ℕ))
    (hmargin : B+1 ≤ (K : ℝ)) :
    (∑ s ∈ Finset.range L, h s) ≤ K.choose (k+2) := by
  have hbudget := mean_cost_budget h K L k B hcap hmean
  have hnonneg : (0 : ℝ) ≤ (∑ s ∈ Finset.range L, h s : ℕ) := by positivity
  have hreal : (∑ s ∈ Finset.range L, h s : ℕ) ≤
      (K.choose (k+2) : ℝ) := by nlinarith
  exact_mod_cast hreal

#print axioms choose_prefix_sum
#print axioms weighted_choose_sum
#print axioms squared_weighted_choose_sum
#print axioms histogram_deficit_le
#print axioms histogram_cost_budget
#print axioms histogram_squared_deficit_le
#print axioms finite_collision_budget
#print axioms mean_cost_budget
#print axioms count_le_choose_of_mean

end CollatzDistinctWordBudget
