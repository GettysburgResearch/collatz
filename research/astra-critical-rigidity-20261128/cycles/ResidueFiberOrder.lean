import Mathlib.Data.ZMod.Basic
import Mathlib.GroupTheory.OrderOfElement
import Mathlib.Logic.Function.Iterate
import Mathlib.Order.Monotone.Defs

/-! The finite-order kernel behind the complete-denominator residue test.

For the intended dyadic lift, `F` is the reduced-clock return
`D^(-B) N^P`, `g` is the gcd of the full native clock and odd period, and
`a` is the corresponding unit modulo the complete denominator. The physical
construction and the width-nine argument that supplies fiber monotonicity
remain written mathematics. No residue-order conclusion is assumed below.
-/

set_option autoImplicit false

namespace Collatz.ResidueFiberOrder

private theorem periodic_fiber_fixed {α β : Type*} [LinearOrder α]
    (f : α → α) (residue : α → β)
    (preserves : ∀ x, residue (f x) = residue x)
    (increasing : ∀ x y, residue x = residue y → x < y → f x < f y)
    (n : ℕ) (hn : 0 < n) (period : ∀ x, (f^[n]) x = x) :
    ∀ x, f x = x := by
  have same (k : ℕ) (x : α) : residue ((f^[k]) x) = residue x := by
    induction k with
    | zero => rfl
    | succ k ih => rw [Function.iterate_succ_apply', preserves, ih]
  have hn1 : 1 ≤ n := hn
  intro x
  rcases lt_trichotomy (f x) x with lower | equal | upper
  · have below (k : ℕ) : (f^[k+1]) x < x := by
      induction k with
      | zero => simpa using lower
      | succ k ih =>
        rw [Function.iterate_succ_apply']
        exact (increasing _ _ (same (k+1) x) ih).trans lower
    have bad := below (n-1)
    rw [Nat.sub_add_cancel hn1, period] at bad
    exact False.elim (lt_irrefl x bad)
  · exact equal
  · have above (k : ℕ) : x < (f^[k+1]) x := by
      induction k with
      | zero => simpa using upper
      | succ k ih =>
        rw [Function.iterate_succ_apply']
        exact upper.trans (increasing _ _ (same (k+1) x).symm ih)
    have bad := above (n-1)
    rw [Nat.sub_add_cancel hn1, period] at bad
    exact False.elim (lt_irrefl x bad)

/-- A periodic ordered lift with a full cyclic phase cannot hide any of that
phase period in an order-preserving residue fiber. Its multiplier has exactly
the full order `g`, not merely a divisor of `g`. -/
theorem residue_order_eq_period {α G : Type*} [LinearOrder α] [Group G]
    (F : α → α) (residue : α → G) (a : G)
    (g : ℕ) (hg : 0 < g) (x₀ : α)
    (period : ∀ x, (F^[g]) x = x)
    (residue_step : ∀ x, residue (F x) = a * residue x)
    (increasing : ∀ x y, residue x = residue y → x < y → F x < F y)
    (phase : α → ZMod g)
    (phase_step : ∀ x, phase (F x) = phase x + 1) :
    orderOf a = g := by
  have residue_iter (n : ℕ) (x : α) :
      residue ((F^[n]) x) = a ^ n * residue x := by
    induction n with
    | zero => simp
    | succ n ih =>
      rw [Function.iterate_succ_apply', residue_step, ih, pow_succ']
      exact (mul_assoc _ _ _).symm
  have phase_iter (n : ℕ) (x : α) :
      phase ((F^[n]) x) = phase x + (n : ZMod g) := by
    induction n with
    | zero => simp
    | succ n ih =>
      rw [Function.iterate_succ_apply', phase_step, ih, Nat.cast_succ, add_assoc]
  have power : a ^ g = 1 := by
    apply mul_right_cancel (b := residue x₀)
    rw [one_mul, ← residue_iter, period]
  have divides : orderOf a ∣ g := orderOf_dvd_iff_pow_eq_one.mpr power
  have iterate_increasing (n : ℕ) :
      ∀ x y, residue x = residue y → x < y → (F^[n]) x < (F^[n]) y := by
    induction n with
    | zero => intro x y _ h; exact h
    | succ n ih =>
      intro x y he hxy
      rw [Function.iterate_succ_apply', Function.iterate_succ_apply']
      apply increasing
      · rw [residue_iter, residue_iter, he]
      · exact ih x y he hxy
  let h := orderOf a
  have preserves (x : α) : residue ((F^[h]) x) = residue x := by
    rw [residue_iter]
    simp [h]
  have lifted_period (x : α) : ((F^[h])^[g]) x = x := by
    rw [← Function.iterate_mul, Nat.mul_comm h g, Function.iterate_mul]
    have same : (F^[g]) = id := funext period
    rw [same, Function.iterate_id]
    rfl
  have fixed := periodic_fiber_fixed (F^[h]) residue preserves
    (iterate_increasing h) g hg lifted_period
  have cast_zero : (h : ZMod g) = 0 := by
    have value := phase_iter h x₀
    rw [fixed] at value
    exact add_left_cancel (by simpa using value.symm : phase x₀ + (h : ZMod g) = phase x₀ + 0)
  have reverse : g ∣ h := (ZMod.natCast_eq_zero_iff h g).mp cast_zero
  exact Nat.dvd_antisymm divides reverse

#print axioms residue_order_eq_period

end Collatz.ResidueFiberOrder
