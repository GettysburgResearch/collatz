import Mathlib.Logic.Function.Iterate
import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Ring

/-! Finite return-count and single-step reconstruction kernels for a rounded
positive dyadic octave. -/

namespace Collatz.GridClock

theorem prefix_iterate {S : Type*} (f : S → S) (count : S → ℤ) (A : ℤ)
    (step : ∀ z, count (f z) ≤ count z - A) (n : ℕ) (z : S) :
    count (f^[n] z) ≤ count z - (n : ℤ)*A := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Function.iterate_succ_apply']
    calc
      count (f (f^[n] z)) ≤ count (f^[n] z) - A := step _
      _ ≤ count z - (n : ℤ)*A - A := sub_le_sub_right ih _
      _ = count z - ((n+1 : ℕ) : ℤ)*A := by push_cast; ring

/-- One genuine count decrement at every periodic grid site bounds the two
cross-multiplied integer clocks. -/
theorem periodic_clock_bound {S : Type*} (f : S → S) (count : S → ℤ)
    (A p a : ℤ) (q : ℕ) (z : S)
    (step : ∀ x, count (f x) ≤ count x - A)
    (winding : count (f^[q] z) = count z - a*p) :
    (q : ℤ)*A ≤ a*p := by
  have h := prefix_iterate f count A step q z
  rw [winding] at h
  omega

/-- The odd part in an octave orbit excluding multiples of four. -/
def twoGradeOdd (z : ℕ) : ℕ := if z % 2 = 0 then z/2 else z

/-- The reverse rounded division, excluding the stated forbidden residue
classes at both actual integer endpoints, gives a genuine positive native
exponent on their odd parts. -/
theorem rounded_edge_native {x y b : ℕ} (hb : b = 1 ∨ b = 2)
    (hy : y = 2^b*x/3) (h3 : x % 3 ≠ 0)
    (hx4 : x % 4 ≠ 0) (hy4 : y % 4 ≠ 0) :
    ∃ e : ℕ, 1 ≤ e ∧ e ≤ 3 ∧ 2^e * twoGradeOdd x = 3 * twoGradeOdd y + 1 := by
  rcases hb with rfl | rfl <;> norm_num1 at hy <;>
    by_cases hx : x % 2 = 0 <;> by_cases hyy : y % 2 = 0 <;>
    simp only [twoGradeOdd, hx, hyy, ite_true, ite_false] <;>
    first | exact ⟨1, by decide, by decide, by norm_num1; omega⟩
          | exact ⟨2, by decide, by decide, by norm_num1; omega⟩
          | exact ⟨3, by decide, by decide, by norm_num1; omega⟩

end Collatz.GridClock
