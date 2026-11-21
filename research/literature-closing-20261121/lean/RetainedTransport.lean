module
public import BandMass

@[expose] public section

/-!
# Source-preserving return transport and an atomic budget

The first inequality transports fresh marked source weights into the actual
entrance measure.  It does not substitute those fresh weights for the complete
entrance packet.  The latter contains all off-section entrance fibers.

The atomic budget keeps a fixed positive source weight along distinct endpoints.
Its domination and finite-budget hypotheses are explicit; the file supplies no
global return domination hypothesis for Collatz.
-/

namespace CollatzShell.ForwardSection.RetainedTransport

open BandMass

noncomputable def sourceWeight (n : ℕ) : ℝ := ((n : ℝ) ^ 4)⁻¹

theorem sourceWeight_nonneg (n : ℕ) : 0 ≤ sourceWeight n := by
  unfold sourceWeight
  positivity

theorem sourceWeight_pos {n : ℕ} (hn : 0 < n) : 0 < sourceWeight n := by
  unfold sourceWeight
  positivity

theorem sourceWeight_le_sixteen_step {n : ℕ} (hn : 0 < n) :
    sourceWeight n ≤ 16 * sourceWeight (step n) := by
  have hp : 0 < step n := by
    unfold step
    split <;> omega
  have hnr : (0 : ℝ) < n := by exact_mod_cast hn
  have hpr : (0 : ℝ) < step n := by exact_mod_cast hp
  have hstep : (step n : ℝ) ≤ 2 * (n : ℝ) := by
    exact_mod_cast step_le_twice n
  have hpow := pow_le_pow_left₀ (by positivity : (0 : ℝ) ≤ step n) hstep 4
  have hbound : (step n : ℝ) ^ 4 ≤ 16 * (n : ℝ) ^ 4 := by
    nlinarith only [hpow]
  unfold sourceWeight
  apply (le_mul_inv_iff₀ (by positivity : (0 : ℝ) < (step n : ℝ) ^ 4)).mpr
  apply (inv_mul_le_iff₀ (by positivity : (0 : ℝ) < (n : ℝ) ^ 4)).mpr
  nlinarith only [hbound]

theorem step_injective_on_marked {n m : ℕ} (hn : Marked n) (hm : Marked m)
    (heq : step n = step m) : n = m := by
  have hnodd := hn.1
  have hmodd := hm.1
  have hnstep : 2 * step n = 3 * n + 1 := by
    unfold step
    simp only [show n % 2 ≠ 0 by omega, if_false]
    omega
  have hmstep : 2 * step m = 3 * m + 1 := by
    unfold step
    simp only [show m % 2 ≠ 0 by omega, if_false]
    omega
  omega

/-- A finite positive test-function version of `R_*(mu restricted to D) <= 16 rho`.
The right side is a sum over genuine new source integers, before grouping their
entrance fibers.  This assertion does not concern `R_* rho`. -/
theorem fresh_return_packet_le (S : Finset ℕ) (hS : ∀ n ∈ S, Marked n)
    (F : ℕ → ℝ) (hF : ∀ m, 0 ≤ F m) :
    (∑ n ∈ S, sourceWeight n * F (next n)) ≤
      16 * ∑ u ∈ S.image step, sourceWeight u * F (entrance u) := by
  classical
  have hsum : (∑ u ∈ S.image step, sourceWeight u * F (entrance u)) =
      ∑ n ∈ S, sourceWeight (step n) * F (entrance (step n)) := by
    apply Finset.sum_image
    intro n hn m hm heq
    exact step_injective_on_marked (hS n hn) (hS m hm) heq
  rw [hsum, Finset.mul_sum]
  apply Finset.sum_le_sum
  intro n hn
  have hpos : 0 < n := by have := (hS n hn).1; omega
  have heq : next n = entrance (step n) := rfl
  rw [heq]
  have h := mul_le_mul_of_nonneg_right (sourceWeight_le_sixteen_step hpos)
    (hF (entrance (step n)))
  nlinarith only [h]

/-- Every endpoint in `z(I)` is counted once.  The same atom `a` appears at
every source time in `I`; it is never replaced by an endpoint weight. -/
theorem retained_atom_uniform_budget (I : Finset ℕ) (z : ℕ → ℕ)
    (hinj : Set.InjOn z (I : Set ℕ)) (rho V : ℕ → ℝ) (a C B : ℝ)
    (hC : 0 ≤ C) (hV : ∀ m, 0 ≤ V m)
    (hatom : ∀ j ∈ I, a ≤ C * rho (z j))
    (hbudget : ∑ m ∈ I.image z, rho m * V m ≤ B) :
    a * (∑ j ∈ I, V (z j)) ≤ C * B := by
  classical
  have hsum : (∑ m ∈ I.image z, rho m * V m) =
      ∑ j ∈ I, rho (z j) * V (z j) := by
    apply Finset.sum_image
    intro i hi j hj hij
    exact hinj hi hj hij
  calc
    a * (∑ j ∈ I, V (z j)) = ∑ j ∈ I, a * V (z j) := by
      rw [Finset.mul_sum]
    _ ≤ ∑ j ∈ I, (C * rho (z j)) * V (z j) := by
      apply Finset.sum_le_sum
      intro j hj
      exact mul_le_mul_of_nonneg_right (hatom j hj) (hV (z j))
    _ = C * (∑ m ∈ I.image z, rho m * V m) := by
      rw [hsum, Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j hj
      ring
    _ ≤ C * B := mul_le_mul_of_nonneg_left hbudget hC

/-- The variable-cost atomic budget, suited to summing over disjoint dyadic
time blocks.  `hatom` is a hypothesis about actual retained source packets. -/
theorem retained_atom_budget (I : Finset ℕ) (z : ℕ → ℕ)
    (hinj : Set.InjOn z (I : Set ℕ)) (rho V C : ℕ → ℝ) (a B : ℝ)
    (hC : ∀ j ∈ I, 0 < C j) (hV : ∀ m, 0 ≤ V m)
    (hatom : ∀ j ∈ I, a ≤ C j * rho (z j))
    (hbudget : ∑ m ∈ I.image z, rho m * V m ≤ B) :
    (∑ j ∈ I, a * V (z j) / C j) ≤ B := by
  classical
  have hsum : (∑ m ∈ I.image z, rho m * V m) =
      ∑ j ∈ I, rho (z j) * V (z j) := by
    apply Finset.sum_image
    intro i hi j hj hij
    exact hinj hi hj hij
  calc
    (∑ j ∈ I, a * V (z j) / C j) ≤ ∑ j ∈ I, rho (z j) * V (z j) := by
      apply Finset.sum_le_sum
      intro j hj
      apply (div_le_iff₀ (hC j hj)).mpr
      have h := mul_le_mul_of_nonneg_right (hatom j hj) (hV (z j))
      nlinarith only [h]
    _ = ∑ m ∈ I.image z, rho m * V m := hsum.symm
    _ ≤ B := hbudget

end CollatzShell.ForwardSection.RetainedTransport

#print axioms CollatzShell.ForwardSection.RetainedTransport.sourceWeight_le_sixteen_step
#print axioms CollatzShell.ForwardSection.RetainedTransport.step_injective_on_marked
#print axioms CollatzShell.ForwardSection.RetainedTransport.fresh_return_packet_le
#print axioms CollatzShell.ForwardSection.RetainedTransport.retained_atom_uniform_budget
#print axioms CollatzShell.ForwardSection.RetainedTransport.retained_atom_budget
