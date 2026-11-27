import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.ByContra
import Mathlib.Data.Rat.Defs
import Mathlib.Algebra.Group.Basic

/-!
Finite algebraic core for physical Mahler substitutions.
No analytic or transcendence theorem is asserted here.

Derived from the pinned upstream source identified in PROVENANCE.md.
Compiler replay and complete exported-theorem axiom reports are recorded in
reports/astra-global-closure-20261124/formal/final-replay.json.
-/
set_option autoImplicit false

namespace MahlerPhysical

def weight (x y : ℚ) : List Bool → ℚ
  | [] => 1
  | false :: w => x * weight x y w
  | true :: w => y * weight x y w

def zeroSum (x y : ℚ) : List Bool → ℚ
  | [] => 0
  | false :: w => 1 + x * zeroSum x y w
  | true :: w => y * zeroSum x y w

def oneSum (x y : ℚ) : List Bool → ℚ
  | [] => 0
  | false :: w => x * oneSum x y w
  | true :: w => 1 + y * oneSum x y w

theorem telescope (x y : ℚ) (w : List Bool) :
    (1-x) * zeroSum x y w + (1-y) * oneSum x y w =
      1 - weight x y w := by
  induction w with
  | nil => simp [zeroSum, oneSum, weight]
  | cons a w ih =>
    cases a
    · simp only [zeroSum, oneSum, weight]
      linear_combination x * ih
    · simp only [zeroSum, oneSum, weight]
      linear_combination y * ih

theorem weight_append (x y : ℚ) (u v : List Bool) :
    weight x y (u ++ v) = weight x y u * weight x y v := by
  induction u with
  | nil => simp [weight]
  | cons a u ih => cases a <;> simp [weight, ih, mul_assoc]

theorem oneSum_append (x y : ℚ) (u v : List Bool) :
    oneSum x y (u ++ v) =
      oneSum x y u + weight x y u * oneSum x y v := by
  induction u with
  | nil => simp [weight, oneSum]
  | cons a u ih => cases a <;> simp [weight, oneSum, ih] <;> ring

def substitute (u v : List Bool) : List Bool → List Bool
  | [] => []
  | false :: w => u ++ substitute u v w
  | true :: w => v ++ substitute u v w

theorem weight_substitute (x y : ℚ) (u v w : List Bool) :
    weight x y (substitute u v w) =
      weight (weight x y u) (weight x y v) w := by
  induction w with
  | nil => simp [substitute, weight]
  | cons a w ih =>
    cases a <;> simp [substitute, weight_append, weight, ih]

theorem oneSum_substitute (x y : ℚ) (u v w : List Bool) :
    oneSum x y (substitute u v w) =
      oneSum x y u * zeroSum (weight x y u) (weight x y v) w +
      oneSum x y v * oneSum (weight x y u) (weight x y v) w := by
  induction w with
  | nil => simp [substitute, oneSum, zeroSum]
  | cons a w ih =>
    cases a <;> simp [substitute, oneSum_append, oneSum, zeroSum, ih] <;> ring

theorem finite_mahler (x y : ℚ) (u v w : List Bool) :
    (1 - weight x y u) * oneSum x y (substitute u v w) =
      oneSum x y u * (1 - weight (weight x y u) (weight x y v) w) +
      ((1 - weight x y u) * oneSum x y v -
       (1 - weight x y v) * oneSum x y u) *
        oneSum (weight x y u) (weight x y v) w := by
  rw [oneSum_substitute]
  have h := telescope (weight x y u) (weight x y v) w
  linear_combination (oneSum x y u) * h

def affineWord (x y a e : ℚ) : List Bool → ℚ → ℚ
  | [], z => z
  | false :: w, z => a + x * affineWord x y a e w z
  | true :: w, z => e + y * affineWord x y a e w z

theorem affine_expand (x y a e : ℚ) (w : List Bool) (z : ℚ) :
    affineWord x y a e w z =
      a * zeroSum x y w + e * oneSum x y w + weight x y w * z := by
  induction w with
  | nil => simp [affineWord, zeroSum, oneSum, weight]
  | cons i w ih =>
    cases i <;> simp [affineWord, zeroSum, oneSum, weight, ih] <;> ring

theorem eliminate_zero (x y a e u v : ℚ)
    (hx : 1-x ≠ 0) (h : (1-x)*u + (1-y)*v = 1) :
    a*u + e*v = a/(1-x) + (e-a*(1-y)/(1-x))*v := by
  have hu : u = (1-(1-y)*v)/(1-x) := by
    apply (eq_div_iff hx).2
    linear_combination h
  rw [hu]
  ring


end MahlerPhysical

-- Complete transitive axiom audit of all exported theorems.
#print axioms MahlerPhysical.telescope
#print axioms MahlerPhysical.weight_append
#print axioms MahlerPhysical.oneSum_append
#print axioms MahlerPhysical.weight_substitute
#print axioms MahlerPhysical.oneSum_substitute
#print axioms MahlerPhysical.finite_mahler
#print axioms MahlerPhysical.affine_expand
#print axioms MahlerPhysical.eliminate_zero
