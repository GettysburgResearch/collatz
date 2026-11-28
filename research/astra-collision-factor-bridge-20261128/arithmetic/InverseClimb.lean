import Mathlib.Tactic.IntervalCases
import Lean.Elab.Tactic.Omega

/-!
# Actual inverse blocks carrying first odd doublings

This module certifies the finite positive-integer arithmetic used in
HARMONIC_BOUNDARY_ATOM.md. It does not formalize infinite harmonic
profiles, boundary measures, density limits, or any Collatz conclusion.

The residue table has explicit witnesses checked by norm_num and the kernel.
No native-decision axiom or untrusted external evaluator is used.
-/

namespace Collatz.InverseClimb

set_option maxRecDepth 100000
set_option maxHeartbeats 200000

/-- One of the 27 bounded odd exponents makes the complete inverse block
integral. The modulus includes both the ternary and parity constraints. -/
theorem residue_exponent_table :
    ∀ r : Fin 162, r.val % 6 = 5 →
      ∃ j : Fin 27, (2 ^ (2 * j.val + 5) * r.val + 2) % 162 = 0 := by
  intro r hr
  obtain ⟨r, hlt⟩ := r
  change r % 6 = 5 at hr
  interval_cases r <;> norm_num at hr
  · exact ⟨⟨0, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨5, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨22, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨6, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨20, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨19, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨12, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨8, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨16, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨18, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨23, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨13, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨24, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨11, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨10, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨3, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨26, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨7, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨9, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨14, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨4, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨15, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨2, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨1, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨21, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨17, by norm_num⟩, by norm_num⟩
  · exact ⟨⟨25, by norm_num⟩, by norm_num⟩

/-- The three odd nodes are a certified inverse block. The exact equations
and odd residues certify forward valuations 1, 1, and e in the written
consumer. The middle height is below twice x and the next exceeds it. -/
def HasDoublingBlock (a : ℕ) : Prop :=
  ∃ e b c x : ℕ,
    5 ≤ e ∧ e ≤ 57 ∧
    b % 6 = 5 ∧ c % 6 = 5 ∧ x % 6 = 5 ∧
    3 * b + 1 = 2 ^ e * a ∧
    3 * c + 1 = 2 * b ∧
    3 * x + 1 = 2 * c ∧
    4 * a ≤ x ∧ x < 2 ^ 55 * a ∧
    c < 2 * x ∧ 2 * x < b

/-- The explicit integral parameter yields every required identity and
height bound; no trajectory simulation is used in this proof. -/
theorem block_from_parameter (a e m : ℕ)
    (ha : 5 ≤ a) (he : 5 ≤ e) (he' : e ≤ 57)
    (hmul : 2 ^ e * a + 2 = 162 * m) :
    HasDoublingBlock a := by
  have hlo : 32 ≤ 2 ^ e := by
    calc
      32 = (2 : ℕ) ^ 5 := by norm_num
      _ ≤ 2 ^ e := Nat.pow_le_pow_right (by norm_num) he
  have hhi : 2 ^ e ≤ (2 : ℕ) ^ 57 :=
    Nat.pow_le_pow_right (by norm_num) he'
  have hlow := Nat.mul_le_mul_right a hlo
  have hupp := Nat.mul_le_mul_right a hhi
  norm_num at hupp
  have hm : 1 ≤ m := by omega
  let b := 54 * m - 1
  let c := 36 * m - 1
  let x := 24 * m - 1
  have hb : b + 1 = 54 * m := by dsimp [b]; omega
  have hc : c + 1 = 36 * m := by dsimp [c]; omega
  have hx : x + 1 = 24 * m := by dsimp [x]; omega
  refine ⟨e, b, c, x, he, he', ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · omega
  · omega
  · omega
  · omega
  · omega
  · omega
  · omega
  · norm_num
    omega
  · omega
  · omega

/-- Every eligible root admits such a block, and the resulting root is
again eligible. This is the finite kernel used recursively in the note. -/
theorem exists_doubling_block (a : ℕ) (ha : 5 ≤ a) (hmod : a % 6 = 5) :
    HasDoublingBlock a := by
  have hr : (a % 162) % 6 = 5 := by omega
  obtain ⟨j, hj⟩ :=
    residue_exponent_table ⟨a % 162, Nat.mod_lt a (by norm_num)⟩ hr
  let e := 2 * j.val + 5
  have he : 5 ≤ e := by dsimp [e]; omega
  have he' : e ≤ 57 := by dsimp [e]; omega
  have hz : (2 ^ e * a + 2) % 162 = 0 := by
    simpa [e, Nat.add_mod, Nat.mul_mod] using hj
  obtain ⟨m, hm⟩ := Nat.dvd_of_mod_eq_zero hz
  exact block_from_parameter a e m ha he he' hm

end Collatz.InverseClimb
