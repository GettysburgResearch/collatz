import Mathlib.Tactic.NormNum
import Lean.Elab.Tactic.Omega

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.UnitInverseFork

/-- Two small exponents giving different unit predecessors of every odd unit. -/
def firstExponent (r : Nat) : Nat :=
  if r = 1 then 4 else if r = 2 then 3 else if r = 4 then 6
  else if r = 5 then 3 else if r = 7 then 4 else 5

def secondExponent (r : Nat) : Nat :=
  if r = 1 then 8 else if r = 2 then 7 else if r = 4 then 8
  else if r = 5 then 5 else if r = 7 then 6 else 7

def child (n e : Nat) : Nat := (2 ^ e * n - 1) / 3

/-- The first finite inverse branch is integral, odd, a ternary unit, strictly
larger than its parent, and has the exact stated native edge. -/
theorem first_branch (n : Nat) (positive : 0 < n)
    (odd : n % 2 = 1) (unit : n % 3 ≠ 0) :
    let e := firstExponent (n % 9)
    3 ≤ e ∧ e ≤ 8 ∧ n < child n e ∧
      child n e % 2 = 1 ∧ child n e % 3 ≠ 0 ∧
      3 * child n e + 1 = 2 ^ e * n := by
  have residues : n % 9 = 1 ∨ n % 9 = 2 ∨ n % 9 = 4 ∨
      n % 9 = 5 ∨ n % 9 = 7 ∨ n % 9 = 8 := by omega
  rcases residues with h | h | h | h | h | h <;>
    norm_num [firstExponent, child, h] <;> omega

/-- The second finite inverse branch has the same retained arithmetic. -/
theorem second_branch (n : Nat) (positive : 0 < n)
    (odd : n % 2 = 1) (unit : n % 3 ≠ 0) :
    let e := secondExponent (n % 9)
    3 ≤ e ∧ e ≤ 8 ∧ n < child n e ∧
      child n e % 2 = 1 ∧ child n e % 3 ≠ 0 ∧
      3 * child n e + 1 = 2 ^ e * n := by
  have residues : n % 9 = 1 ∨ n % 9 = 2 ∨ n % 9 = 4 ∨
      n % 9 = 5 ∨ n % 9 = 7 ∨ n % 9 = 8 := by omega
  rcases residues with h | h | h | h | h | h <;>
    norm_num [secondExponent, child, h] <;> omega

/-- A bounded native inverse edge has a unique odd target and exponent.
This prevents two different branches of the finite inverse tree from merging. -/
theorem target_unique (x u v e f : Nat)
    (eu : 3 ≤ e) (ev : e ≤ 8) (fu : 3 ≤ f) (fv : f ≤ 8)
    (ou : u % 2 = 1) (ov : v % 2 = 1)
    (hu : 3 * x + 1 = 2 ^ e * u) (hv : 3 * x + 1 = 2 ^ f * v) :
    u = v ∧ e = f := by
  have he : e = 3 ∨ e = 4 ∨ e = 5 ∨ e = 6 ∨ e = 7 ∨ e = 8 := by omega
  have hf : f = 3 ∨ f = 4 ∨ f = 5 ∨ f = 6 ∨ f = 7 ∨ f = 8 := by omega
  rcases he with rfl | rfl | rfl | rfl | rfl | rfl <;>
    rcases hf with rfl | rfl | rfl | rfl | rfl | rfl <;>
      norm_num at hu hv ⊢ <;> omega

/-- The two branches at one parent use different exponents. -/
theorem distinct_exponents (n : Nat) (unit : n % 3 ≠ 0) :
    firstExponent (n % 9) < secondExponent (n % 9) := by
  have residues : n % 9 = 1 ∨ n % 9 = 2 ∨ n % 9 = 4 ∨
      n % 9 = 5 ∨ n % 9 = 7 ∨ n % 9 = 8 := by omega
  rcases residues with h | h | h | h | h | h <;>
    norm_num [firstExponent, secondExponent, h]

end Collatz.UnitInverseFork
