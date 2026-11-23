module

public import ActualSurvivorMass
public import ExplicitSeed

@[expose] public section

/-!
# A concrete source-preserving completion target

The source atoms, incoming fibers, and finite return budgets are all defined.
The first theorem proves the unconditional quadratic bound. The second proves
full Collatz under an explicitly quantified improvement of that bound.
The improvement is a hypothesis, not a proved estimate or an added axiom.
-/

namespace CollatzShell.ForwardSection

open CollatzHarmonic CollatzFiniteResolvent

/-- The explicit positive seed always satisfies the quadratic baseline. -/
theorem actual_quadratic_baseline (k y : ℕ) :
    coefficient 0 * incoming coefficient k y ≤
      growth k * survivorBudget coefficient k y :=
  quadratic_baseline (fun j ↦ incoming coefficient j y) k
    (fun j _ ↦ (incoming_bounds coefficient_finiteMass j y).1)

/-- A uniform-in-endpoint improvement, with arbitrarily small relative
quadratic factors at selected depths, rules out every original counterexample.
No change of source weights, limiting distribution, or unproved recurrence
claim is used in this implication. -/
theorem collatz_of_explicit_quadratic_saving
    (saving : ∀ ε : ℝ, 0 < ε → ∃ k : ℕ, ∀ y : ℕ,
      coefficient 0 * incoming coefficient k y ≤
        (ε * ((k : ℝ)+1) * ((k : ℝ)+2)) * survivorBudget coefficient k y) :
    Universal := by
  apply collatz_iff_marked.mpr
  intro n hn
  by_contra bad
  let ε : ℝ := coefficient n / 32
  have he : 0 < ε := by dsimp [ε]; exact div_pos (coefficient_pos n) (by norm_num)
  obtain ⟨k,hk⟩ := saving ε he
  have hL : 0 ≤ ε * ((k : ℝ)+1) * ((k : ℝ)+2) := by positivity
  have lower := actual_survivor_budget coefficient_finiteMass hL hn
    (survives_of_not_basin bad k) (hk (returns n k))
  have hfactor : 0 < ((k : ℝ)+1)*((k : ℝ)+2) := by positivity
  have hpositive := mul_pos hfactor (coefficient_pos n)
  dsimp [ε] at lower
  nlinarith

end CollatzShell.ForwardSection
