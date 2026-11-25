import TowerClock
import Mathlib.Tactic.Linarith

/-! Finite ordinary-word and affine-chain identities used in the written
bounded-template theorem. The external S-unit theorem and the finiteness
conclusion are not asserted as kernel theorems in this module. -/

namespace Collatz.TemplateChain
open Collatz.SourceDeletion Collatz.TowerClock

/-- A physically realized ordinary word has its exact rational centered map.
The center equation is meaningful also for an all-even word, whose center is 0. -/
theorem physical_center {v : List Bool} {n y : Nat} {a c : ℚ}
    (path : trace v.length n = v) (endpoint : run v.length n = y)
    (slope : a * 2^v.length = 3^(weight v))
    (center : (1-a)*c*2^v.length = (carry v : ℚ)) :
    (y : ℚ) = c + a*((n : ℚ)-c) := by
  have hn := (word_iff v n y).mpr ⟨path,endpoint⟩
  have hq : (2:ℚ)^v.length*(y:ℚ) = 3^(weight v)*(n:ℚ)+(carry v:ℚ) := by
    exact_mod_cast hn
  have nz : (2:ℚ)^v.length ≠ 0 := pow_ne_zero _ (by norm_num)
  apply mul_left_cancel₀ nz
  calc
    (2:ℚ)^v.length*(y:ℚ) = 3^(weight v)*(n:ℚ)+(carry v:ℚ) := hq
    _ = (a*2^v.length)*(n:ℚ)+(1-a)*c*2^v.length := by rw [slope,center]
    _ = _ := by ring

def centeredRun (a c : ℚ) : Nat → ℚ → ℚ
  | 0, x => x
  | n+1, x => centeredRun a c n (c+a*(x-c))

/-- Arbitrarily many repetitions of a template retain one rational center. -/
theorem centered_power (a c x : ℚ) (n : Nat) :
    centeredRun a c n x = c+a^n*(x-c) := by
  induction n generalizing x with
  | zero => simp [centeredRun]
  | succ n ih => rw [centeredRun,ih,pow_succ]; ring

/-- Interior terms after summation by parts; index j is the j+1 boundary. -/
def interior (c u : Nat → ℚ) : Nat → ℚ
  | 0 => 0
  | n+1 => interior c u n + (c n-c (n+1))*u (n+1)

/-- The finite chain identity uses every original boundary and multiplier.
Here u is the reciprocal cumulative multiplier, not a fresh independent input. -/
theorem chain_identity (x c u : Nat → ℚ) (n : Nat)
    (edge : ∀ j≤n, x (j+1)*u (j+1) =
      x j*u j+c j*(u (j+1)-u j)) :
    x (n+1)*u (n+1) = (x 0-c 0)*u 0 +
      interior c u n + c n*u (n+1) := by
  induction n with
  | zero => rw [edge 0 (by omega)]; simp [interior]; ring
  | succ n ih =>
    have prev := ih (fun j hj => edge j (by omega))
    rw [edge (n+1) (by omega),prev,interior]
    ring

/-- Exact sparse equation to which the written S-unit argument applies. -/
theorem endpoint_equation (x c u : Nat → ℚ) (n : Nat)
    (initial : u 0=1)
    (edge : ∀ j≤n, x (j+1)*u (j+1) =
      x j*u j+c j*(u (j+1)-u j)) :
    x 0-c 0+interior c u n+c n*u (n+1)-x (n+1)*u (n+1)=0 := by
  have eq := chain_identity x c u n edge
  rw [initial,mul_one] at eq
  linarith

#print axioms physical_center
#print axioms centered_power
#print axioms chain_identity
#print axioms endpoint_equation

end Collatz.TemplateChain
