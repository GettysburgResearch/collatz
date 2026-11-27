import Std

/-! The universal lift-index selector for three 32-gap ordinary suffixes.
The circular problem has circumference four times the suffix modulus. -/
set_option autoImplicit false
set_option warningAsError true

namespace ResonantPhase

def Q : Int := 72057594037927936
def low : Int := 1853015893884545
def middle : Int := 58710943741132417
def high : Int := 150865148058652885

def Selected (c : Int) : Prop := c = low ∨ c = middle ∨ c = high

/-- Every odd phase admits a lift in the top five native binary octaves
whose reduced affine numerator has quotient 1 modulo 4. -/
theorem phase_selector (a : Int) (odd : a % 2 = 1) :
    ∃ c j : Int, Selected c ∧ 2251799813685248 ≤ j ∧ j < Q ∧
      (a + c + 2*j) % (4*Q) = Q := by
  let t := (Q-a) % (4*Q)
  have ht : 0 ≤ t ∧ t < 4*Q := by unfold t Q; omega
  have phase : ∃ c s : Int, Selected c ∧ 4503599627370496 ≤ s ∧
      s < 2*Q ∧ (s=t-c ∨ s=t-c+4*Q) := by
    by_cases h₀ : t < low+4503599627370496
    · refine ⟨high,t-high+4*Q,Or.inr (Or.inr rfl),?_,?_,Or.inr rfl⟩ <;>
        unfold low high Q at * <;> omega
    by_cases h₁ : t < middle+4503599627370496
    · refine ⟨low,t-low,Or.inl rfl,?_,?_,Or.inl rfl⟩ <;>
        unfold low middle Q at * <;> omega
    by_cases h₂ : t < high+4503599627370496
    · refine ⟨middle,t-middle,Or.inr (Or.inl rfl),?_,?_,Or.inl rfl⟩ <;>
        unfold middle high Q at * <;> omega
    · refine ⟨high,t-high,Or.inr (Or.inr rfl),?_,?_,Or.inl rfl⟩ <;>
        unfold high Q at * <;> omega
  obtain ⟨c,s,hc,hs,hs',he⟩ := phase
  have co : c%2 = 1 := by
    rcases hc with h|h|h <;> subst c <;> decide
  refine ⟨c,s/2,hc,?_,?_,?_⟩
  · omega
  · unfold Q at *; omega
  · dsimp [t,Q] at *
    rcases he with h|h <;> omega

#print axioms phase_selector
end ResonantPhase
