import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring

/-! Labelled lifted-gap numerators on an integer cycle. Filtering a discrepancy
at arbitrary clocks commutes with the whole finite carry. -/
namespace Collatz.Unconventional.PhasePair

/-- Integer numerator after clearing all n powers of three. -/
def numerator (B : ℕ → ℕ) (J : ℕ → ℤ) : ℕ → ℤ
  | 0 => 0
  | n+1 => 3 * numerator B J n + 2^(B n) * J n

/-- Subtraction uses the same fold at the two ends of a lifted rank interval. -/
theorem lifted_edge {x₀ x₁ y₀ y₁ c₀ c₁ : ℤ} {b : ℕ}
    (h₀ : (2 : ℤ)^b*y₀ = 3*x₀+c₀) (h₁ : (2 : ℤ)^b*y₁ = 3*x₁+c₁) :
    (2 : ℤ)^b*(y₁-y₀) = 3*(x₁-x₀)+(c₁-c₀) := by
  rw [mul_sub, h₁, h₀]
  ring

theorem endpoint {B b : ℕ → ℕ} {J G : ℕ → ℤ}
    (h₀ : B 0 = 0) (hB : ∀ i, B (i+1) = B i+b i)
    (he : ∀ i, (2 : ℤ)^(b i)*G (i+1) = 3*G i+J i) (n : ℕ) :
    (2 : ℤ)^(B n)*G n = 3^n*G 0 + numerator B J n := by
  induction n with
  | zero => simp [h₀, numerator]
  | succ n ih =>
    calc
      (2 : ℤ)^(B (n+1))*G (n+1) = 2^(B n)*(2^(b n)*G (n+1)) := by
        rw [hB, pow_add, mul_assoc]
      _ = 3*(2^(B n)*G n) + 2^(B n)*J n := by rw [he]; ring
      _ = 3^(n+1)*G 0 + numerator B J (n+1) := by rw [ih, pow_succ, numerator]; ring

/-- Each clock can be placed into any one group. The theorem also allows a
discrepancy to be split additively between several groups of integer errors. -/
theorem arbitrary_groups {ι : Type*} (s : Finset ι) (B : ℕ → ℕ)
    (J : ℕ → ℤ) (group : ι → ℕ → ℤ)
    (partition : ∀ i, ∑ h ∈ s, group h i = J i) (n : ℕ) :
    ∑ h ∈ s, numerator B (group h) n = numerator B J n := by
  induction n with
  | zero => simp [numerator]
  | succ n ih =>
    simp only [numerator, Finset.sum_add_distrib, ← Finset.mul_sum, ih, partition]

theorem grouped_endpoint {ι : Type*} (s : Finset ι) {B b : ℕ → ℕ}
    {J G : ℕ → ℤ} (group : ι → ℕ → ℤ)
    (h₀ : B 0 = 0) (hB : ∀ i, B (i+1) = B i+b i)
    (he : ∀ i, (2 : ℤ)^(b i)*G (i+1) = 3*G i+J i)
    (hp : ∀ i, ∑ h ∈ s, group h i = J i) (n : ℕ) :
    (2 : ℤ)^(B n)*G n = 3^n*G 0 + ∑ h ∈ s, numerator B (group h) n := by
  rw [arbitrary_groups s B J group hp, endpoint h₀ hB he]

#print axioms lifted_edge
#print axioms endpoint
#print axioms arbitrary_groups
#print axioms grouped_endpoint

end Collatz.Unconventional.PhasePair
