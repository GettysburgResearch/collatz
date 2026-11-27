import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
Rebuilt arithmetic kernels and the closing logical interface, copied from
PR200 at 8e6add443b13acbcfd553676898c120183f07377 with a proof/API repair.
No new axiom: the missing global hypotheses remain explicit parameters.
The original candidate and its original status are preserved upstream.
See verified/README.md and the strict replay receipt for this copy's scope.
-/

namespace GlobalTrace20261125

def step (n : ℕ) : ℕ :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def run : ℕ → ℕ → ℕ
  | 0, n => n
  | k + 1, n => run k (step n)

def Good (n : ℕ) : Prop := ∃ k : ℕ, run k n = 1

def Escapes (n : ℕ) : Prop := ∀ B : ℕ, ∃ k : ℕ, B < run k n

def EventuallyPeriodic (n : ℕ) : Prop :=
  ∃ i j : ℕ, i < j ∧ run i n = run j n

-- A full theorem still needs a proof that no positive orbit escapes
-- and a proof that every eventually periodic positive orbit reaches 1.
theorem final_proposal
    (dichotomy : ∀ n : ℕ, 0 < n → Escapes n ∨ EventuallyPeriodic n)
    (traceExcludesEscape : ∀ n : ℕ, 0 < n → ¬ Escapes n)
    (ordinaryCycleExclusion : ∀ n : ℕ, 0 < n → EventuallyPeriodic n → Good n) :
    ∀ n : ℕ, 0 < n → Good n := by
  intro n hn
  rcases dichotomy n hn with he | hp
  · exact False.elim (traceExcludesEscape n hn he)
  · exact ordinaryCycleExclusion n hn hp

-- A single large point already forces a large normalized second moment.
-- Here H^2 <= M*X is supplied by the actual nonnegative octave sum.
theorem moment_spike (X H M c : ℝ)
    (hx : 0 < X) (hc : 0 < c)
    (hh : c * X ≤ H) (hm : H ^ 2 ≤ M * X) :
    c ^ 2 * X ≤ M := by
  have hcx : 0 ≤ c * X := mul_nonneg hc.le hx.le
  have hsum : 0 ≤ H + c * X := by linarith
  have hs : (c * X) ^ 2 ≤ H ^ 2 := by
    nlinarith [mul_nonneg (sub_nonneg.mpr hh) hsum]
  have hprod : (c ^ 2 * X) * X ≤ M * X := by
    calc
      (c ^ 2 * X) * X = (c * X) ^ 2 := by ring
      _ ≤ H ^ 2 := hs
      _ ≤ M * X := hm
  exact le_of_mul_le_mul_right hprod hx

-- Finite-lap truncation kernel: the first-hit weight has a uniform cap.
-- The canonical trace supplies B <= h*(1-lam).
theorem truncation_ratio (r h B lam u C : ℝ)
    (hh : 0 < h) (hu : 0 ≤ u) (hC : 0 ≤ C)
    (hr : r ≤ C * B * u) (htrace : B ≤ h * (1-lam)) :
    r / h ≤ C * (1-lam) * u := by
  apply (div_le_iff₀ hh).2
  calc
    r ≤ C * B * u := hr
    _ ≤ C * (h * (1-lam)) * u :=
      mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left htrace hC) hu
    _ = C * (1-lam) * u * h := by ring

-- Exact rational-lattice numerator map, distinct from the ordinary map.
def stepD (D u : ℕ) : ℕ :=
  if u % 2 = 0 then u / 2 else (3*u+D)/2

def runD (D : ℕ) : ℕ → ℕ → ℕ
  | 0, u => u
  | k + 1, u => runD D k (stepD D u)

theorem model5_lap : runD 5 5 23 = 23 := by decide
theorem model5_pair : 3 * 17 = (2 * 23 + 5 : ℕ) := by decide


#print axioms final_proposal
#print axioms moment_spike
#print axioms truncation_ratio
#print axioms model5_lap
#print axioms model5_pair

end GlobalTrace20261125
