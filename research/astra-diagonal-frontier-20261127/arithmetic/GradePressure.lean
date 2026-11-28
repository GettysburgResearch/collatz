import Mathlib.Tactic

namespace Collatz.GradePressure

noncomputable def gradeMass (t C : ℝ) (m : ℕ) : ℝ :=
  1 + ∑ k ∈ Finset.range m, t * C^(k+1)

/-- The exact row sum after the positive-grade geometric reweighting. -/
theorem gradeMassEq (t C : ℝ) (hC : (1-t)*C=1) (m : ℕ) :
    gradeMass t C m = C^m := by
  induction m with
  | zero => simp [gradeMass]
  | succ m ih =>
    calc
      gradeMass t C (m+1) = gradeMass t C m + t*C^(m+1) := by
        simp [gradeMass, Finset.sum_range_succ, add_assoc]
      _ = C^(m+1) := by
        rw [ih, pow_succ]
        linear_combination -(C^m)*hC

noncomputable def paths (t C : ℝ) : List ℕ → ℕ → ℝ
  | [], g => C^g
  | d :: ds, g =>
    paths t C ds 0 + ∑ k ∈ Finset.range (g+d), t * paths t C ds (k+1)

/-- Exact total weight of every finite admissible grade path, including
the terminal factor. The arrivals are the actual folded shifts minus one. -/
theorem pathMass (t C : ℝ) (hC : (1-t)*C=1) (ds : List ℕ) (g : ℕ) :
    paths t C ds g = C^(g+ds.sum) := by
  induction ds generalizing g with
  | nil => simp [paths]
  | cons d ds ih =>
    simp only [paths, ih, zero_add, List.sum_cons]
    calc
      C^ds.sum + ∑ k ∈ Finset.range (g+d), t*C^(k+1+ds.sum) =
          gradeMass t C (g+d) * C^ds.sum := by
          simp only [gradeMass, add_mul, one_mul, Finset.sum_mul, pow_add]
          apply congrArg (fun z : ℝ => C^ds.sum + z)
          apply Finset.sum_congr rfl
          intro i _
          ring
      _ = C^(g+(d+ds.sum)) := by rw [gradeMassEq t C hC, ← pow_add, Nat.add_assoc]

/-- Making grade one free increases the reweighted row by at most \(2-t\). -/
theorem freeFirstGrade (t C : ℝ) (hC : (1-t)*C=1) (ht : t≤1)
    (h1 : 1≤C) (m : ℕ) :
    gradeMass t C m + (if 0<m then (1-t)*C else 0) ≤ (2-t)*C^m := by
  rw [gradeMassEq t C hC]
  by_cases hm : 0<m
  · rw [ite_eq_left hm, hC]
    have hpow : C≤C^m := by
      simpa using (pow_le_pow_right₀ h1 (show 1≤m by omega))
    nlinarith [mul_le_mul_of_nonneg_left hpow (sub_nonneg.mpr ht)]
  · have hz : m=0 := by omega
    subst m
    simp only [lt_self_iff_false, ite_false, pow_zero, add_zero, mul_one]
    linarith

#print axioms gradeMassEq
#print axioms pathMass
#print axioms freeFirstGrade

end Collatz.GradePressure
