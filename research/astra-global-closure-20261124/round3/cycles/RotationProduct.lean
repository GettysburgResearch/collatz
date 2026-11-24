import Mathlib.Tactic.Ring

/-! Signed differences of two shortcut walks with the same literal carry. -/
set_option autoImplicit false
namespace Collatz.RotationProduct

def numerator (b : Bool) (d n : Int) : Int := if b then 3*n+d else n

/-- On a mismatch, signed odd-minus-even difference. -/
def before (b c : Bool) (x y : Int) : Int :=
  if b = c then 1 else if b then x-y else y-x

/-- Same orientation after applying the numerator rule. -/
def after (b c : Bool) (d x y : Int) : Int :=
  if b = c then 1 else if b then 3*x+d-y else 3*y+d-x

def commonOdd (b c : Bool) : Nat := if b && c then 1 else 0

def product (f : Nat → Int) : Nat → Int
  | 0 => 1
  | k+1 => product f k * f k

def count (f : Nat → Nat) : Nat → Nat
  | 0 => 0
  | k+1 => count f k + f k

/-- The local identity includes all four ordered parity pairs. -/
theorem edge_factors (b c : Bool) (d x y x' y' : Int)
    (hx : 2*x' = numerator b d x) (hy : 2*y' = numerator c d y) :
    2*(y'-x') * before b c x y = (3:Int)^(commonOdd b c)*(y-x)*after b c d x y := by
  have h : 2*(y'-x') = numerator c d y - numerator b d x := by
    rw [←hx, ←hy]
    ring
  rw [h]
  cases b <;> cases c <;> simp [before, after, commonOdd, numerator] <;> ring

/-- Telescoping with the initial and final pair differences retained. -/
theorem product_path (b c : Nat → Bool) (d : Int) (x y : Nat → Int) (k : Nat)
    (hx : ∀ i, i<k → 2*x (i+1) = numerator (b i) d (x i))
    (hy : ∀ i, i<k → 2*y (i+1) = numerator (c i) d (y i))
    (distinct : ∀ i, i<k → y i ≠ x i) :
    (2:Int)^k * product (fun i => before (b i) (c i) (x i) (y i)) k * (y k-x k) =
      (3:Int)^(count (fun i => commonOdd (b i) (c i)) k) *
      product (fun i => after (b i) (c i) d (x i) (y i)) k * (y 0-x 0) := by
  induction k with
  | zero => simp [product, count]
  | succ k ih =>
    have prev := ih (fun i hi => hx i (by omega)) (fun i hi => hy i (by omega))
      (fun i hi => distinct i (by omega))
    have last := edge_factors (b k) (c k) d (x k) (y k) (x (k+1)) (y (k+1))
      (hx k (by omega)) (hy k (by omega))
    have nonzero : y k - x k ≠ 0 := sub_ne_zero.mpr (distinct k (by omega))
    apply mul_right_cancel₀ nonzero
    simp only [product, count, pow_succ, pow_add]
    calc
      _ = ((2:Int)^k * product (fun i => before (b i) (c i) (x i) (y i)) k * (y k-x k)) *
            (2*(y (k+1)-x (k+1))*before (b k) (c k) (x k) (y k)) := by ring
      _ = _ := by rw [prev, last]; ring

/-- Any nonidentity rotation of a primitive cycle has distinct pairs and
closed endpoints, so the hypotheses hold for its common reduced denominator. -/
theorem product_lap (b c : Nat → Bool) (d : Int) (x y : Nat → Int) (k : Nat)
    (hx : ∀ i, i<k → 2*x (i+1) = numerator (b i) d (x i))
    (hy : ∀ i, i<k → 2*y (i+1) = numerator (c i) d (y i))
    (distinct : ∀ i, i<k → y i ≠ x i) (atZero : y 0 ≠ x 0)
    (closedX : x k=x 0) (closedY : y k=y 0) :
    (2:Int)^k * product (fun i => before (b i) (c i) (x i) (y i)) k =
      (3:Int)^(count (fun i => commonOdd (b i) (c i)) k) *
      product (fun i => after (b i) (c i) d (x i) (y i)) k := by
  apply mul_right_cancel₀ (sub_ne_zero.mpr atZero)
  simpa only [closedX, closedY] using product_path b c d x y k hx hy distinct

#print axioms edge_factors
#print axioms product_path
#print axioms product_lap
end Collatz.RotationProduct
