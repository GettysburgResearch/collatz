import Mathlib.Data.Finset.Max
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.BigOperators.GroupWithZero.Finset
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-! Exact finite cost calibration for distinct negative rational inverse paths.
Write a state as -q/D with q,D positive. A positive inverse gap e has the
literal numerator equation 3*q' = 2^e*q+D. All results below are finite and
make no assertion that an arbitrary policy has distinct states. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.SignedDistinctCost
open Finset

/-- Among distinct positive integer denominators, the first n integers maximize
the product of the factors (q+D)/q. This is the denominator-cleared form. -/
theorem extremal_product (D : ℕ) (s : Finset ℕ) (hs : ∀ q ∈ s, 0 < q) :
    s.card.factorial * (∏ q ∈ s, (q+D)) ≤
      (D+1).ascFactorial s.card * (∏ q ∈ s, q) := by
  induction s using Finset.induction_on_max with
  | empty => simp
  | insert q s hmax ih =>
    have hnot : q ∉ s := by intro h; exact (lt_irrefl q) (hmax q h)
    have hpos : 0 < q := hs q (mem_insert_self q s)
    have hs' : ∀ x ∈ s, 0 < x := fun x hx => hs x (mem_insert_of_mem hx)
    have hc : s.card+1 ≤ q := by
      have hcard : (insert q s).card ≤ (range q).card := by
        apply Finset.card_le_card_of_injOn (fun x : ℕ => x-1)
        · intro x hx
          have hp := hs x hx
          have hb : x ≤ q := by
            rcases mem_insert.mp hx with rfl | hx
            · exact le_rfl
            · exact (hmax x hx).le
          apply mem_range.mpr
          change x-1 < q
          omega
        · intro x hx y hy he
          have hxp := hs x hx
          have hyp := hs y hy
          change x-1 = y-1 at he
          omega
      simpa only [card_insert_of_notMem hnot, card_range] using hcard
    have hstep : (s.card+1)*(q+D) ≤ (D+1+s.card)*q := by
      have hd := Nat.mul_le_mul_left D hc
      nlinarith
    rw [card_insert_of_notMem hnot, Nat.factorial_succ, Nat.ascFactorial_succ,
      prod_insert hnot, prod_insert hnot]
    calc
      (s.card+1)*s.card.factorial*((q+D)*(∏ x ∈ s, (x+D))) =
          ((s.card+1)*(q+D))*(s.card.factorial*(∏ x ∈ s, (x+D))) := by ring
      _ ≤ ((D+1+s.card)*q)*((D+1).ascFactorial s.card*(∏ x ∈ s, x)) :=
        Nat.mul_le_mul hstep (ih hs')
      _ = _ := by ring

def total (e : ℕ → ℕ) (n : ℕ) : ℕ := ∑ j ∈ range n, (e j+1)

/-- Actual negative numerator recurrence, with positive gap e(j)+1. -/
def Follows (D : ℕ) (q e : ℕ → ℕ) (n : ℕ) : Prop :=
  ∀ j < n, 3*q (j+1) = 2^(e j+1)*q j+D

private theorem product_calibration (D n : ℕ) (q e : ℕ → ℕ)
    (h : Follows D q e n) :
    3^n*q n*(∏ j ∈ range n, q j) ≤
      2^(total e n)*q 0*(∏ j ∈ range n, (q j+D)) := by
  induction n with
  | zero => simp [total]
  | succ n ih =>
    have hi := ih (fun j hj => h j (by omega))
    have he := h n (by omega)
    have hp : 1 ≤ 2^(e n+1) := Nat.one_le_pow _ _ (by decide)
    have hb : 3*q (n+1) ≤ 2^(e n+1)*(q n+D) := by
      have hd := Nat.mul_le_mul_right D hp
      rw [he]
      nlinarith
    have ht : total e (n+1) = total e n+(e n+1) := by
      simp only [total, sum_range_succ]
    rw [prod_range_succ, prod_range_succ, ht, pow_add, pow_succ]
    calc
      3^n*3*q (n+1)*((∏ j ∈ range n, q j)*q n) =
          (3*q (n+1))*(3^n*q n*(∏ j ∈ range n, q j)) := by ring
      _ ≤ (2^(e n+1)*(q n+D))*(3^n*q n*(∏ j ∈ range n, q j)) :=
        Nat.mul_le_mul_right _ hb
      _ ≤ (2^(e n+1)*(q n+D))*(2^(total e n)*q 0*(∏ j ∈ range n, (q j+D))) :=
        Nat.mul_le_mul_left _ hi
      _ = _ := by ring

/-- An exact factorial bound for any supplied finite distinct negative rational
inverse path. It keeps the true terminal numerator as an extra strengthening. -/
theorem distinct_path_cost (D n : ℕ) (q e : ℕ → ℕ)
    (h : Follows D q e n) (hp : ∀ j < n, 0 < q j)
    (hi : Set.InjOn q (range n)) :
    3^n*q n*n.factorial ≤ 2^(total e n)*q 0*(D+1).ascFactorial n := by
  have he := extremal_product D ((range n).image q) (by
    intro x hx
    obtain ⟨j,hj,rfl⟩ := mem_image.mp hx
    exact hp j (mem_range.mp hj))
  rw [card_image_of_injOn hi, card_range,
    prod_image (fun i hi' j hj' heq => hi hi' hj' heq),
    prod_image (fun i hi' j hj' heq => hi hi' hj' heq)] at he
  have hc := product_calibration D n q e h
  have hh : (3^n*q n*n.factorial)*(∏ j ∈ range n, q j) ≤
      (2^(total e n)*q 0*(D+1).ascFactorial n)*(∏ j ∈ range n, q j) := by
    calc
      (3^n*q n*n.factorial)*(∏ j ∈ range n, q j) =
          n.factorial*(3^n*q n*(∏ j ∈ range n, q j)) := by ring
      _ ≤ n.factorial*(2^(total e n)*q 0*(∏ j ∈ range n, (q j+D))) :=
        Nat.mul_le_mul_left _ hc
      _ = (2^(total e n)*q 0)*(n.factorial*(∏ j ∈ range n, (q j+D))) := by ring
      _ ≤ (2^(total e n)*q 0)*((D+1).ascFactorial n*(∏ j ∈ range n, q j)) :=
        Nat.mul_le_mul_left _ he
      _ = _ := by ring
  exact le_of_mul_le_mul_right hh (Finset.prod_pos fun j hj => hp j (mem_range.mp hj))

/-- Dropping a positive terminal numerator gives the direct lower bound on the
total binary exponent; all denominator and state-size dependence is explicit. -/
theorem positive_terminal_cost (D n : ℕ) (q e : ℕ → ℕ)
    (h : Follows D q e n) (hp : ∀ j ≤ n, 0 < q j)
    (hi : Set.InjOn q (range n)) :
    3^n*n.factorial ≤ 2^(total e n)*q 0*(D+1).ascFactorial n := by
  have hc := distinct_path_cost D n q e h (fun j hj => hp j (by omega)) hi
  have hq : 1 ≤ q n := hp n le_rfl
  have hh := Nat.mul_le_mul_left (3^n) hq
  have ht := Nat.mul_le_mul_right n.factorial hh
  simpa only [Nat.mul_one] using ht.trans hc

/-- The same exact native bound in binomial form. For fixed D the remaining
factor grows only polynomially with the number of distinct departures. -/
theorem binomial_cost (D n : ℕ) (q e : ℕ → ℕ)
    (h : Follows D q e n) (hp : ∀ j ≤ n, 0 < q j)
    (hi : Set.InjOn q (range n)) :
    3^n ≤ 2^(total e n)*q 0*(D+n).choose n := by
  have hc := positive_terminal_cost D n q e h hp hi
  rw [Nat.ascFactorial_eq_factorial_mul_choose] at hc
  have hh : 3^n*n.factorial ≤ (2^(total e n)*q 0*(D+n).choose n)*n.factorial := by
    calc
      _ ≤ 2^(total e n)*q 0*(n.factorial*(D+n).choose n) := hc
      _ = _ := by ring
  exact le_of_mul_le_mul_right hh (Nat.factorial_pos n)

end Collatz.SignedDistinctCost
