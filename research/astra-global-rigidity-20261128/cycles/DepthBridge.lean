import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Tactic.Ring
import Lean.Elab.Tactic.Omega

/-!
Finite legality and weight kernels used by the depth-bridge proof. These
lemmas do not formalize infinite Gibbs states, pressure differentiability,
return-time integrability, or the Collatz conjecture.
-/
namespace Collatz.DepthBridge

def usable (x y nx ny c : ℕ) : Prop := max nx ny ≤ min x y + c

theorem min_step (x y nx ny c : ℕ) (hx : nx ≤ x + c) (hy : ny ≤ y + c) :
    min nx ny ≤ min x y + c := by
  omega

theorem max_step (x y nx ny c : ℕ) (hx : nx ≤ x + c) (hy : ny ≤ y + c) :
    max nx ny ≤ max x y + c := by
  omega

theorem swap_step (x y nx ny c : ℕ) (h : usable x y nx ny c) :
    ny ≤ x + c ∧ nx ≤ y + c := by
  unfold usable at h
  omega

theorem swap_invariant (x y nx ny c : ℕ) :
    usable x y nx ny c ↔ usable x y ny nx c := by
  simp only [usable, max_comm ny nx]

theorem crossing_usable (x y nx ny c : ℕ) (hx : nx ≤ x + c)
    (horder : x ≤ y) (hcross : ny ≤ nx) : usable x y nx ny c := by
  unfold usable
  omega

theorem no_swap_order (x y nx ny c : ℕ) (hx : nx ≤ x + c)
    (hno : ¬ usable x y nx ny c) (horder : x ≤ y) : nx < ny := by
  unfold usable at hno
  omega

theorem opposite_zeros_force_swap (n : ℕ) (x y c : ℕ → ℕ)
    (hx : x 0 = 0) (hy : y (n + 1) = 0)
    (hstep : ∀ t ≤ n, x (t + 1) ≤ x t + c t) :
    ∃ t ≤ n, usable (x t) (y t) (x (t + 1)) (y (t + 1)) (c t) := by
  classical
  by_contra h
  have hn : ∀ t ≤ n, ¬ usable (x t) (y t) (x (t + 1)) (y (t + 1)) (c t) := by
    intro t ht hu
    exact h ⟨t, ht, hu⟩
  have ho : ∀ k, k ≤ n + 1 → x k ≤ y k := by
    intro k
    induction k with
    | zero =>
        intro hk
        omega
    | succ k ih =>
        intro hk
        have hkn : k ≤ n := by omega
        have hki : k ≤ n + 1 := by omega
        have hh := no_swap_order _ _ _ _ _ (hstep k hkn) (hn k hkn) (ih hki)
        omega
  have hh := no_swap_order _ _ _ _ _ (hstep n (by omega)) (hn n (by omega))
      (ho n (by omega))
  omega

theorem lattice_reward (a : ℚ) (x y : ℕ) :
    a * (1 / 2 : ℚ) ^ (min x y) + a * (1 / 2 : ℚ) ^ (max x y) =
    a * (1 / 2 : ℚ) ^ x + a * (1 / 2 : ℚ) ^ y := by
  rcases le_total x y with h | h
  · simp only [min_eq_left h, max_eq_right h]
  · simp only [min_eq_right h, max_eq_left h]
    ring

theorem shifted_positive_step (x y c : ℕ) (hx : 0 < x) (hy : 0 < y)
    (hstep : y ≤ x + c) : y - 1 ≤ x - 1 + c := by
  omega

theorem half_tilt_reward (a : ℚ) (j : ℕ) (hj : 0 < j) :
    a * (1 / 2 : ℚ) ^ j = (1 / 2 : ℚ) * (a * (1 / 2 : ℚ) ^ (j - 1)) := by
  calc
    a * (1 / 2 : ℚ) ^ j = a * (1 / 2 : ℚ) ^ ((j - 1) + 1) := by
      rw [Nat.sub_add_cancel (by omega : 1 ≤ j)]
    _ = _ := by rw [pow_succ]; ring

end Collatz.DepthBridge
