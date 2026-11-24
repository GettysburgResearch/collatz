import Mathlib

/-! Proposed finite core. Not compiled in the authoring environment.
    The scalar and exact physical transport hypotheses are external to
    this finite algebra. No convergence axiom or admission. -/
namespace Collatz.OctavePhase

theorem native_budget (A B K k0 km m t : ℕ)
    (ht : A + km = B + 2*K + k0)
    (hheight : 15*km + 5*A ≤ 5*t + 8*m + 20)
    (hA : A ≤ t) :
    15*(2*K+B) ≤ 15*t+8*m+20 := by
  omega

theorem native_large_count_budget (B K m t : ℕ)
    (h : 15*(2*K+B) ≤ 15*t+8*m+20)
    (hm : 3*t ≤ 16*m) :
    80*(2*K+B) ≤ 73*t+80*m+107 := by
  omega

theorem terminal_carry_unique (A B K k0 km km' : ℕ)
    (h : A + km = B + 2*K + k0)
    (h' : A + km' = B + 2*K + k0) :
    km = km' := by omega

theorem rational_birth_constants :
    (1-(49/144 : ℚ))/(1-2*(49/144)) = 95/46 ∧
    1+(95/46 : ℚ)*(49/144) ≤ 12/7 ∧
    1+(95/46 : ℚ)*((49/144)+(49/144)^2) ≤ (12/7)^2 := by
  norm_num

theorem native_exponent_constants :
    (3 : ℕ)^5 < 2^8 ∧
    (12 : ℕ)^365 < 2^284*7^365 ∧
    ((16 : ℕ)^16)^25 < 2^284*(3^3*13^13)^25 := by
  constructor
  · decide
  · constructor <;> decide

def variation (f : ℕ → ℝ) : ℕ → ℝ
  | 0 => 0
  | n+1 => variation f n + |f (n+1)-f n|

theorem displacement_le_variation (f : ℕ → ℝ) (n : ℕ) :
    |f n-f 0| ≤ variation f n := by
  induction n with
  | zero => simp [variation]
  | succ n ih =>
    calc
      |f (n+1)-f 0| =
          |(f (n+1)-f n)+(f n-f 0)| := by
        congr 1 <;> ring
      _ ≤ |f (n+1)-f n|+|f n-f 0| := abs_add_le _ _
      _ ≤ variation f (n+1) := by
        simp only [variation]
        linarith

/-- Finite version of the two-sided discrete variation charge.
    The infinite countable-fiber TV argument is in the written note. -/
theorem peak_charge (f : ℕ → ℝ) (n k : ℕ)
    (h0 : f 0 = 0) (hend : f (n+k) = 0) (hn : 0 ≤ f n) :
    2*f n ≤ variation f n + variation (fun i => f (n+i)) k := by
  have hl : f n ≤ variation f n := by
    simpa [h0, abs_of_nonneg hn] using displacement_le_variation f n
  have hr : f n ≤ variation (fun i => f (n+i)) k := by
    simpa [hend, abs_of_nonneg hn] using
      displacement_le_variation (fun i => f (n+i)) k
  linarith

end Collatz.OctavePhase

#print axioms Collatz.OctavePhase.native_budget
#print axioms Collatz.OctavePhase.native_large_count_budget
#print axioms Collatz.OctavePhase.terminal_carry_unique
#print axioms Collatz.OctavePhase.rational_birth_constants
#print axioms Collatz.OctavePhase.native_exponent_constants
#print axioms Collatz.OctavePhase.displacement_le_variation
#print axioms Collatz.OctavePhase.peak_charge
