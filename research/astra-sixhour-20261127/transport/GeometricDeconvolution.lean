import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-! Exact positive-gap counts with a total-dependent additive shear.
    This is the finite algebraic kernel of (1) in MARKED_TRACE.md. -/

namespace Collatz.GeometricDeconvolution

set_option autoImplicit false

variable {G : Type*} [AddCommGroup G] [DecidableEq G]

/-- Counts gap sequences of fixed length and total. On appending a positive
gap, the preceding total may be any natural number strictly below the new one. -/
def counts (jump : ℕ → ℕ → G) : ℕ → G → ℕ → ℕ
  | 0, z, t => if z = 0 ∧ t = 0 then 1 else 0
  | j + 1, z, t => ∑ r ∈ Finset.range t, counts jump j (z - jump j t) r

/-- All positive geometric words of a prescribed total have this same weight. -/
def mass (jump : ℕ → ℕ → G) (j : ℕ) (z : G) (t : ℕ) : ℚ :=
  (counts jump j z t : ℚ) / 2 ^ t

/-- Difference of the two consecutive unsheared cumulative counts. -/
theorem unsheared_succ (jump : ℕ → ℕ → G) (j t : ℕ) (z : G) :
    counts jump (j+1) (z + jump j (t+1)) (t+1) =
      counts jump (j+1) (z + jump j t) t + counts jump j z t := by
  simp [counts, Finset.sum_range_succ]

/-- Exact recovery of the full preceding joint law, including its time coordinate. -/
theorem deconvolve (jump : ℕ → ℕ → G) (j t : ℕ) (z : G) :
    mass jump j z t = 2 * mass jump (j+1) (z + jump j (t+1)) (t+1) -
                              mass jump (j+1) (z + jump j t) t := by
  simp only [mass, unsheared_succ, Nat.cast_add, pow_succ]
  field_simp
  ring

/-- Syracuse specialization at a fixed ambient precision, including when
the word length is strictly less than the number of trits retained. -/
def syracuseJump (N j t : ℕ) : ZMod (3^N) :=
  3^j * ((2 : ZMod (3^N))⁻¹)^t

theorem syracuse_recovery (N j t : ℕ) (z : ZMod (3^N)) :
    mass (syracuseJump N) j z t =
      2 * mass (syracuseJump N) (j+1) (z+syracuseJump N j (t+1)) (t+1) -
          mass (syracuseJump N) (j+1) (z+syracuseJump N j t) t :=
  deconvolve _ _ _ _

#print axioms unsheared_succ
#print axioms deconvolve
#print axioms syracuse_recovery

end Collatz.GeometricDeconvolution
