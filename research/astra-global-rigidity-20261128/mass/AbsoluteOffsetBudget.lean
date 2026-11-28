import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Finite integer forms of the visit and floor bounds for an absolute Collatz
affine offset. A list contains the odd states departed from before the tested
endpoint. Repetitions are permitted. The survival product is top / den and
the exact intercept at endpoint y is y * loss / den. -/

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.AbsoluteOffsetBudget

def top : List Nat → Nat
  | [] => 1
  | x :: xs => (3*x) * top xs

def loss : List Nat → Nat
  | [] => 0
  | x :: xs => (3*x+1) * loss xs + top xs

def den : List Nat → Nat
  | [] => 1
  | x :: xs => (3*x+1) * den xs

def atMost (M : Nat) : List Nat → Nat
  | [] => 0
  | x :: xs => atMost M xs + if x ≤ M then 1 else 0

theorem top_add_loss (xs : List Nat) : top xs + loss xs = den xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    simp only [top, loss, den, ← ih]
    ring

theorem denominator_positive (xs : List Nat) : 0 < den xs := by
  induction xs with
  | nil => decide
  | cons x xs ih =>
    exact Nat.mul_pos (Nat.succ_pos _) ih

theorem count_times_survival (M : Nat) (xs : List Nat) :
    top xs * atMost M xs ≤ (3*M) * loss xs := by
  induction xs with
  | nil => simp [top, loss, atMost]
  | cons x xs ih =>
    have scaled := Nat.mul_le_mul_left (3*x) ih
    by_cases hx : x ≤ M
    · have size := Nat.mul_le_mul_right (top xs) (Nat.mul_le_mul_left 3 hx)
      simp only [top, loss, atMost, ite_eq_left hx]
      nlinarith only [scaled, size, Nat.zero_le ((3*M)*loss xs)]
    · simp only [top, loss, atMost, ite_eq_right hx, Nat.add_zero]
      nlinarith only [scaled, Nat.zero_le ((3*M)*loss xs), Nat.zero_le ((3*M)*top xs)]

theorem previous_low_floor (M y B : Nat) (xs : List Nat)
    (visited : 0 < atMost M xs) (mark : y * loss xs ≤ B * den xs) :
    y ≤ B * (3*M+1) := by
  have h : top xs ≤ top xs * atMost M xs := by
    simpa using Nat.mul_le_mul_left (top xs) visited
  have lo := Nat.le_trans h (count_times_survival M xs)
  have bound : den xs ≤ (3*M+1) * loss xs := by
    rw [← top_add_loss xs]
    nlinarith only [lo]
  have total : y * den xs ≤ (B*(3*M+1)) * den xs := by
    calc
      y * den xs ≤ y *((3*M+1)*loss xs) := Nat.mul_le_mul_left _ bound
      _ = (3*M+1) * (y*loss xs) := by ring
      _ ≤ (3*M+1) * (B*den xs) := Nat.mul_le_mul_left _ mark
      _ = (B*(3*M+1)) * den xs := by ring
  exact Nat.le_of_mul_le_mul_right total (denominator_positive xs)

theorem few_earlier_visits (Z y B : Nat) (xs : List Nat)
    (hy : 0 < y) (half : 2*B ≤ y) (positive : 0 < top xs)
    (mark : y * loss xs ≤ B * den xs) :
    y * atMost Z xs ≤ 6*Z*B := by
  have smallLoss : 2 * loss xs ≤ den xs := by
    apply Nat.le_of_mul_le_mul_left _ hy
    calc
      y*(2*loss xs) = 2*(y*loss xs) := by ring
      _ ≤ 2*(B*den xs) := Nat.mul_le_mul_left _ mark
      _ = (2*B)*den xs := by ring
      _ ≤ y*den xs := Nat.mul_le_mul_right _ half
  have denominator : den xs ≤ 2*top xs := by
    have eq := top_add_loss xs
    omega
  have total : (y*atMost Z xs)*top xs ≤ (6*Z*B)*top xs := by
    calc
      (y*atMost Z xs)*top xs = y*(top xs*atMost Z xs) := by ring
      _ ≤ y*((3*Z)*loss xs) := Nat.mul_le_mul_left _ (count_times_survival Z xs)
      _ = (3*Z)*(y*loss xs) := by ring
      _ ≤ (3*Z)*(B*den xs) := Nat.mul_le_mul_left _ mark
      _ = (3*Z*B)*den xs := by ring
      _ ≤ (3*Z*B)*(2*top xs) := Nat.mul_le_mul_left _ denominator
      _ = (6*Z*B)*top xs := by ring
  exact Nat.le_of_mul_le_mul_right total positive

end Collatz.AbsoluteOffsetBudget
