import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.ByContra
import Mathlib.Data.Rat.Defs
import Mathlib.Algebra.Group.Basic

/-!
Coprime-cycle residue kernel.
No ordinary cycle or unrestricted selector is asserted to exist.

Derived from the pinned upstream source identified in PROVENANCE.md.
Compiler replay and complete exported-theorem axiom reports are recorded in
reports/astra-global-closure-20261124/formal/final-replay.json.
-/
set_option autoImplicit false

namespace Collatz.ResidueDefect

variable {R : Type*} [CommRing R]

def geom (x : R) : ℕ → R
  | 0 => 0
  | n+1 => geom x n + x^n

theorem geom_mul (x : R) (n : ℕ) :
    (x-1)*geom x n = x^n-1 := by
  induction n with
  | zero => simp [geom]
  | succ n ih =>
    simp only [geom, mul_add, ih, pow_succ]
    ring

/-- In the Bezout-root quotient x^p = 2, the balanced sum is a unit. -/
theorem balanced_unit (x : R) (p : ℕ) (hx : x^p = 2) :
    (x-1)*geom x p = 1 := by
  rw [geom_mul, hx]
  norm_num

theorem exponent_transport (x : R) (p A d i e : ℕ)
    (hp : x^p = 2) (hA : x^A = 3) (he : A*i+e = p*d) :
    (3:R)^i*x^e = (2:R)^d := by
  calc
    _ = (x^A)^i*x^e := by rw [hA]
    _ = x^(A*i+e) := by rw [pow_add, pow_mul]
    _ = x^(p*d) := by rw [he]
    _ = _ := by rw [pow_mul, hp]

theorem cycle_term (x : R) (p A d i e : ℕ)
    (hi : i < p) (hp : x^p = 2) (hA : x^A = 3)
    (he : A*i+e = p*d) :
    (3:R)^(p-1-i)*(2:R)^d = (3:R)^(p-1)*x^e := by
  rw [← exponent_transport x p A d i e hp hA he, ← mul_assoc, ← pow_add]
  rw [show p-1-i+i = p-1 by omega]

/-- A complete inverse witness, rather than a prime-field test. -/
theorem balanced_numerator_inverse (x y : R) (p : ℕ)
    (hp : x^p = 2) (hy : y*3 = 1) :
    ((x-1)*y^(p-1))*((3:R)^(p-1)*geom x p) = 1 := by
  calc
    _ = ((x-1)*geom x p)*(y*3)^(p-1) := by rw [mul_pow]; ring
    _ = 1 := by rw [balanced_unit x p hp, hy]; simp

/-- A single interior interval of elevated coefficients has a trinomial defect. -/
theorem single_interval_defect (x : R) (p u v : ℕ) (hp : x^p = 2) :
    (x-1)*(geom x p + (geom x v-geom x u)) = 1+x^v-x^u := by
  rw [mul_add, mul_sub, balanced_unit x p hp, geom_mul, geom_mul]
  ring

end Collatz.ResidueDefect

-- Complete transitive axiom audit of all exported theorems.
#print axioms Collatz.ResidueDefect.geom_mul
#print axioms Collatz.ResidueDefect.balanced_unit
#print axioms Collatz.ResidueDefect.exponent_transport
#print axioms Collatz.ResidueDefect.cycle_term
#print axioms Collatz.ResidueDefect.balanced_numerator_inverse
#print axioms Collatz.ResidueDefect.single_interval_defect
