import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Exact finite kernels for the asynchronous component-boundary argument.
The infinite summability/zero-one theorem and its analytic source imports
remain written proofs in DYADIC_BOUNDARY_ZERO_ONE.md. -/

namespace Collatz.BoundaryEnergy

def shortcut (n : ℕ) : ℕ :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def BasinLabel (f : ℕ → Bool) : Prop := ∀ n, f (shortcut n) = f n

theorem basin_label_doubles {f : ℕ → Bool} (hf : BasinLabel f) (n : ℕ) :
    f (2 * n) = f n := by
  have h := hf (2 * n)
  simpa [shortcut] using h.symm

theorem basin_label_odd {f : ℕ → Bool} (hf : BasinLabel f) (n : ℕ) :
    f (2 * n + 1) = f (3 * n + 2) := by
  have h := hf (2 * n + 1)
  have he : (2 * n + 1) % 2 ≠ 0 := by omega
  have hd : (3 * (2 * n + 1) + 1) / 2 = 3 * n + 2 := by omega
  simpa [shortcut, he, hd] using h.symm

def boundary (f : ℕ → Bool) (n : ℕ) : ℕ :=
  if f n = f (n + 1) then 0 else 1

def birth (f : ℕ → Bool) (n : ℕ) : ℕ :=
  if f n = f (n + 1) ∧ f (2 * n + 1) ≠ f n then 1 else 0

/-- A binary parent boundary is inherited once, while a new opposite
middle label creates precisely two boundaries. -/
theorem boundary_creation {f : ℕ → Bool}
    (hf : ∀ n, f (2 * n) = f n) (n : ℕ) :
    boundary f (2 * n) + boundary f (2 * n + 1) =
      boundary f n + 2 * birth f n := by
  have hnext : f (2 * n + 1 + 1) = f (n + 1) := by
    convert hf (n + 1) using 1
  unfold boundary birth
  rw [hf n, hnext]
  cases h₀ : f n <;> cases h₁ : f (n + 1) <;>
    cases hm : f (2 * n + 1) <;> simp_all

/-- The finite dyadic variation bound used in the sharp construction. -/
theorem paired_boundary_bound {f : ℕ → Bool}
    (hf : ∀ n, f (2 * n) = f n) (n : ℕ) :
    boundary f (2 * n) + boundary f (2 * n + 1) ≤
      boundary f n + 2 * boundary f (2 * n) := by
  have hnext : f (2 * n + 1 + 1) = f (n + 1) := by
    convert hf (n + 1) using 1
  unfold boundary
  rw [hf n, hnext]
  cases h₀ : f n <;> cases h₁ : f (n + 1) <;>
    cases hm : f (2 * n + 1) <;> simp_all

/-- Summation over any complete finite shell, with no asymptotic premise. -/
theorem finite_shell_bound {f : ℕ → Bool}
    (hf : ∀ n, f (2 * n) = f n) (m N : ℕ) :
    (∑ i ∈ Finset.range N,
      (boundary f (2 * (m + i)) + boundary f (2 * (m + i) + 1))) ≤
      (∑ i ∈ Finset.range N, boundary f (m + i)) +
      2 * (∑ i ∈ Finset.range N, boundary f (2 * (m + i))) := by
  calc
    _ ≤ ∑ i ∈ Finset.range N,
        (boundary f (m + i) + 2 * boundary f (2 * (m + i))) := by
      exact Finset.sum_le_sum fun i _ => paired_boundary_bound hf (m + i)
    _ = _ := by simp [Finset.sum_add_distrib, Finset.mul_sum]

/-- The even boundary is the exact affine-label discrepancy that must
be controlled; the identity consumes both actual shortcut branches. -/
theorem even_boundary_affine {f : ℕ → Bool} (hf : BasinLabel f) (n : ℕ) :
    boundary f (2 * n) = if f n = f (3 * n + 2) then 0 else 1 := by
  simp only [boundary, basin_label_doubles hf, basin_label_odd hf]

/-- Two distinct affine slopes cannot give two source witnesses for
the same prescribed pair of terminal word maps. -/
theorem affine_merger_unique {a b c d x y : ℚ} (hab : a ≠ b)
    (hx : a * x + c = b * (x + 1) + d)
    (hy : a * y + c = b * (y + 1) + d) : x = y := by
  have h : (a - b) * (x - y) = 0 := by nlinarith
  exact sub_eq_zero.mp ((mul_eq_zero.mp h).resolve_left (sub_ne_zero.mpr hab))

/-- Conversely, two different sources force equality of the slopes. -/
theorem two_mergers_equal_slope {a b c d x y : ℚ} (hxy : x ≠ y)
    (hx : a * x + c = b * (x + 1) + d)
    (hy : a * y + c = b * (y + 1) + d) : a = b := by
  by_contra hab
  exact hxy (affine_merger_unique hab hx hy)

end Collatz.BoundaryEnergy
