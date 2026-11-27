import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-! A synchronized pair of actual shortcut itineraries.  The positive
constant forcing after the change of coordinates u = 2x+q permits
term-by-term comparison at every phase of any common-length return. -/
set_option autoImplicit false
set_option warningAsError true
namespace Collatz.InfiniteDescent.ShiftHeights

def grade : List Bool → ℕ
  | [] => 0
  | b::w => b.toNat + grade w

def carry : List Bool → ℕ
  | [] => 0
  | _::w => 3^grade w + 2*carry w

def rises : List (Bool × Bool) → ℕ
  | [] => 0
  | (a,b)::w => (if !a && b then 1 else 0) + rises w

theorem grade_bound (w : List (Bool × Bool)) :
    grade (w.map Prod.snd) ≤ grade (w.map Prod.fst) + rises w := by
  induction w with
  | nil => simp [grade,rises]
  | cons p w ih =>
    obtain ⟨a,b⟩ := p
    cases a <;> cases b <;> simp_all [grade,rises,Bool.toNat] <;> omega

theorem carry_bound (w : List (Bool × Bool)) :
    carry (w.map Prod.snd) ≤ 3^(rises w) * carry (w.map Prod.fst) := by
  induction w with
  | nil => simp [carry,rises]
  | cons p w ih =>
    have exp := Nat.pow_le_pow_right (by decide : 0<3) (grade_bound w)
    rw [pow_add] at exp
    have add := Nat.add_le_add exp (Nat.mul_le_mul_left 2 ih)
    obtain ⟨a,b⟩ := p
    have inc : rises w ≤ rises ((a,b)::w) := by simp [rises]
    calc
      carry (((a,b)::w).map Prod.snd)
           ≤ 3^(rises w)*carry (((a,b)::w).map Prod.fst) := by
             simpa [carry,Nat.mul_add,Nat.mul_left_comm,Nat.mul_comm,Nat.mul_assoc] using add
      _ ≤ _ := Nat.mul_le_mul_right _ (Nat.pow_le_pow_right (by decide) inc)

/-- Cleared ordinary shortcut branch equation over the common odd
denominator q.  A closed instance supplies the actual fixed point. -/
inductive Trace (q : ℤ) : ℤ → List Bool → ℤ → Prop where
  | nil (x : ℤ) : Trace q x [] x
  | cons {x y z : ℤ} {b : Bool} {w : List Bool}
      (step : 2*y=3^b.toNat*x+(if b then q else 0))
      (tail : Trace q y w z) : Trace q x (b::w) z

theorem constant_force {q x y : ℤ} {b : Bool}
    (step : 2*y=3^b.toNat*x+(if b then q else 0)) :
    2*(2*y+q)=3^b.toNat*(2*x+q)+q := by
  cases b <;> simp [Bool.toNat] at * <;> omega

theorem trace_formula {q x z : ℤ} {w : List Bool} (tr : Trace q x w z) :
    2^w.length*(2*z+q) = 3^grade w*(2*x+q)+q*(carry w:ℤ) := by
  induction tr with
  | nil => simp [grade,carry]
  | @cons x y z b w step tail ih =>
    have first := constant_force step
    simp only [List.length_cons,grade,carry,pow_succ,pow_add,Nat.cast_add,
      Nat.cast_pow,Nat.cast_ofNat,Nat.cast_mul]
    linear_combination 2*ih + 3^grade w*first

/-- The exact pair-height comparison after a full common-length return.
For chronological rotations the two grades and lengths agree. -/
theorem periodic_comparison {q x y : ℤ} (hq : 0 ≤ q) (pairs : List (Bool × Bool))
    (tx : Trace q x (pairs.map Prod.fst) x)
    (ty : Trace q y (pairs.map Prod.snd) y)
    (same : grade (pairs.map Prod.fst)=grade (pairs.map Prod.snd))
    (contracting : (3:ℤ)^grade (pairs.map Prod.fst)<2^pairs.length) :
    2*y+q ≤ 3^(rises pairs)*(2*x+q) := by
  have fx := trace_formula tx
  have fy := trace_formula ty
  simp only [List.length_map] at fx fy
  rw [←same] at fy
  have cb : (carry (pairs.map Prod.snd):ℤ) ≤ 3^(rises pairs)*(carry (pairs.map Prod.fst):ℤ) := by
    exact_mod_cast carry_bound pairs
  have qc := mul_le_mul_of_nonneg_left cb hq
  apply le_of_mul_le_mul_left (a := (2:ℤ)^pairs.length-3^grade (pairs.map Prod.fst))
  · calc
      _ = q*(carry (pairs.map Prod.snd):ℤ) := by linear_combination fy
      _ ≤ 3^rises pairs*(q*(carry (pairs.map Prod.fst):ℤ)) := by convert qc using 1; ring
      _ = _ := by linear_combination -(3^rises pairs)*fx
  · omega

/-- Each exact shared block forces an actual integer spacing at its start,
irrespective of the common odd denominator or the intervening valuations. -/
theorem shared_block {q a b a' b' : ℤ} {w : List Bool}
    (ta : Trace q a w a') (tb : Trace q b w b') (different : a≠b) :
    (2:ℤ)^w.length ≤ |a-b| := by
  have left := trace_formula ta
  have right := trace_formula tb
  have product : (2:ℤ)^w.length*(a'-b')=3^grade w*(a-b) := by
    nlinarith only [left,right]
  have cop : IsCoprime (2:ℤ) 3 := ⟨-1,1,by decide⟩
  have divides : (2:ℤ)^w.length ∣ a-b :=
    (cop.pow (m:=w.length) (n:=grade w)).dvd_of_dvd_mul_left ⟨a'-b',product.symm⟩
  obtain ⟨k,hk⟩ := divides
  have nz : k ≠ 0 := by intro hn; subst k; simp at hk; omega
  have hkpos : 1 ≤ |k| := by have := abs_pos.mpr nz; omega
  rw [hk,abs_mul,abs_of_nonneg (by positivity : (0:ℤ) ≤ 2^w.length)]
  simpa using mul_le_mul_of_nonneg_left hkpos (by positivity : (0:ℤ) ≤ 2^w.length)

#print axioms grade_bound
#print axioms carry_bound
#print axioms periodic_comparison
#print axioms shared_block
end Collatz.InfiniteDescent.ShiftHeights
