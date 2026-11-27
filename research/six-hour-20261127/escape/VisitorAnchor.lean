import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.IntervalCases

/-! Finite ordinary inputs to the universal ternary visitor bound. The
    stopped-word estimate, measure transfer, and infinite sum are written
    arguments. The finite orbit computation below uses kernel reduction. -/
namespace EscapeVisitorAnchor

def oddPart (n : ℕ) : ℕ :=
  if h : 0 < n ∧ n % 2 = 0 then oddPart (n/2) else n
termination_by n
decreasing_by exact Nat.div_lt_self h.1 (by decide)

def step (x : ℕ) : ℕ := oddPart (3*x+1)

def walk : ℕ → ℕ → ℕ
  | 0, x => x
  | n+1, x => if x = 1 then 1 else walk n (step x)

theorem step_one : step 1 = 1 := by decide +kernel

@[simp] theorem walk_one (n : ℕ) : walk n 1 = 1 := by
  cases n <;> simp [walk]

theorem walk_succ (n x : ℕ) : walk (n+1) x = walk n (step x) := by
  by_cases h : x = 1
  · subst x
    simp [step_one]
  · simp [walk, h]

set_option maxRecDepth 20000 in
set_option maxHeartbeats 0 in
theorem checked_block :
    (List.range 2048).all (fun i => walk 87 (2*i+1) == 1) = true := by
  decide +kernel

theorem fates_through_4095 (i : ℕ) (hi : i < 2048) : walk 87 (2*i+1) = 1 := by
  exact beq_iff_eq.mp (List.all_eq_true.mp checked_block i (List.mem_range.mpr hi))

def smallCore : List ℕ := [1,3,5,7,9,11,13,15,17,19,23,29,35,53]

theorem core_closed (x : ℕ) (hx : x ∈ smallCore) : step x ∈ smallCore := by
  have hc : smallCore.all (fun y => smallCore.contains (step y)) = true := by
    decide +kernel
  exact List.contains_iff_mem.mp (List.all_eq_true.mp hc x hx)

theorem core_iterates (t x : ℕ) (hx : x ∈ smallCore) : walk t x ∈ smallCore := by
  induction t generalizing x with
  | zero => exact hx
  | succ n ih => exact walk_succ n x ▸ ih (step x) (core_closed x hx)

theorem core_excludes_targets (t x : ℕ) (hx : x ∈ smallCore) :
    walk t x ≠ 31 ∧ walk t x < 61 := by
  have hc : smallCore.all (fun y => decide (y ≠ 31 ∧ y < 61)) = true := by decide +kernel
  exact of_decide_eq_true (List.all_eq_true.mp hc _ (core_iterates t x hx))

theorem anchored_square_loss (g u c p : ℚ)
    (hg : 0 ≤ g) (hu : 0 ≤ u) (hp : 0 ≤ p)
    (hgu : g*u ≤ c) (hc : c ≤ 5*p) :
    (4/3 : ℚ) * (g*u)^2 ≤ (100/3 : ℚ)*p^2 := by
  have h₁ : 0 ≤ 5*p - g*u := by linarith
  have h₂ : 0 ≤ 5*p + g*u := add_nonneg (by linarith) (mul_nonneg hg hu)
  nlinarith [mul_nonneg h₁ h₂]

theorem failure_below_one_percent :
    (2/3 : ℚ) * (3/4 : ℚ)^82 + 100 / (3*4095 : ℚ) < 1/100 := by norm_num

#print axioms walk_succ
#print axioms fates_through_4095
#print axioms core_iterates
#print axioms core_excludes_targets
#print axioms anchored_square_loss
#print axioms failure_below_one_percent
end EscapeVisitorAnchor
