import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fintype.Fin
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Finite kernels for cutting a head edge by its terminating clock phase.
    Label 0 represents nonconvergence, and 1 and 2 the two terminating phases. -/

namespace Collatz.HeadPhaseCut

open scoped BigOperators

abbrev Label := Fin 3

def phase (q : Bool) : Label := if q then 1 else 2

def flip (a : Label) : Label := if a = 0 then 0 else if a = 1 then 2 else 1

def cross (q : Bool) (a b : Label) : Prop :=
  (a = 0 ∧ b = phase q) ∨ (a = phase q ∧ b = 0)

instance (q : Bool) (a b : Label) : Decidable (cross q a b) := by
  unfold cross
  infer_instance

def score (q : Bool) (a b : Label) : ℤ :=
  if a = 0 ∧ b = phase q then 1 else if a = phase q ∧ b = 0 then -1 else 0

def bad (a : Label) : ℤ := if a = 0 then 1 else 0

theorem phase_swap : ∀ (q : Bool) (a b : Label),
    score q (flip a) (flip b) = score (!q) a b := by decide

theorem collapse_score : ∀ (a b : Label),
    score true a b + score false a b = bad a - bad b := by decide

def squareError (q : Bool) (a b c d : Label) : ℤ :=
  score q a b - score q c d - score q a c + score q b d

/-- If any label is absent from a quadrilateral, its oriented defect is zero. -/
theorem binary_square : ∀ (q : Bool) (a b c d omitted : Label),
    a ≠ omitted → b ≠ omitted → c ≠ omitted → d ≠ omitted →
    squareError q a b c d = 0 := by decide

theorem square_bound : ∀ (q : Bool) (a b c d : Label),
    |squareError q a b c d| ≤ 4 := by decide

def pathCost (q : Bool) (a : Label) : List Label → Label → ℕ
  | [], b => if cross q a b then 1 else 0
  | v :: rest, b => (if cross q a v then 1 else 0) + pathCost q v rest b

private theorem remaining_cross : ∀ (q : Bool) (a v b : Label),
    cross q a b → (v = 0 ∨ v = phase q) → ¬cross q a v → cross q v b := by decide

/-- A path between different endpoints in one two-label set pays a crossing. -/
theorem path_forces_cross (q : Bool) (middle : List Label) (a b : Label)
    (ends : cross q a b) (binary : ∀ v ∈ middle, v = 0 ∨ v = phase q) :
    1 ≤ pathCost q a middle b := by
  induction middle generalizing a with
  | nil => simp [pathCost, ends]
  | cons v rest ih =>
    have at_v := binary v (List.mem_cons_self ..)
    have next_binary : ∀ w ∈ rest, w = 0 ∨ w = phase q :=
      fun w hw => binary w (List.mem_cons_of_mem _ hw)
    by_cases seen : cross q a v
    · simp [pathCost, seen]
    · simpa [pathCost, seen] using ih v (remaining_cross q a v b ends at_v seen) next_binary

/-- Horizontal cross terms cancel between successive physical comparison squares. -/
theorem accumulate_squares (q : Bool) (a b : ℕ → Label) (n : ℕ) :
    (∑ i ∈ Finset.range n, score q (a (i+1)) (a i)) -
        (∑ i ∈ Finset.range n, score q (b (i+1)) (b i)) =
      score q (a n) (b n) - score q (a 0) (b 0) +
        ∑ i ∈ Finset.range n, squareError q (a (i+1)) (a i) (b (i+1)) (b i) := by
  induction n with
  | zero => simp
  | succ n ih =>
    simp only [Finset.sum_range_succ, squareError] at ih ⊢
    linarith

/-- Summing the adjacent-child recursion keeps the factor 1/81 at a carry. -/
theorem pay_horizontal (h e : ℕ → ℚ) (n : ℕ) (nonneg : 0 ≤ h n)
    (step : ∀ i < n, 81 * h (i+1) ≤ 81 * e i + h i) :
    80 * (∑ i ∈ Finset.range n, h (i+1)) ≤ 81 * (∑ i ∈ Finset.range n, e i) + h 0 := by
  have exact_bound : 80 * (∑ i ∈ Finset.range n, h (i+1)) + h n ≤
      81 * (∑ i ∈ Finset.range n, e i) + h 0 := by
    clear nonneg
    induction n with
    | zero => simp
    | succ n ih =>
      have previous := ih (fun i hi => step i (by omega))
      have last := step n (by omega)
      simp only [Finset.sum_range_succ]
      linarith
  linarith

#print axioms phase_swap
#print axioms collapse_score
#print axioms binary_square
#print axioms square_bound
#print axioms path_forces_cross
#print axioms accumulate_squares
#print axioms pay_horizontal

end Collatz.HeadPhaseCut
