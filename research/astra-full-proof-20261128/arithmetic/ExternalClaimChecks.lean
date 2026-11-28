import Std

/-! Small independent checks of two external statements inspected while looking
for a full-proof input. These are not imports of either author's development.
The map in the first check is the unaccelerated Collatz map. -/

set_option autoImplicit false
set_option maxRecDepth 20000
set_option maxHeartbeats 0

namespace FullProofExternalChecks

def rawStep (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else 3 * n + 1

def oddCount : Nat → Nat → Nat
  | 0, _ => 0
  | k + 1, n => (if n % 2 = 1 then 1 else 0) + oddCount k (rawStep n)

def mersenne : Nat := 2 ^ 100 - 1

theorem mersenne_input :
    mersenne ≥ 2 ^ 71 ∧ mersenne % 2 = 1 ∧ mersenne % 4 = 3 := by
  decide +kernel

theorem no_short_certificate :
    ∀ k : Fin 201,
      ¬ (oddCount k.val mersenne ≤ 44 ∧
         k.val - oddCount k.val mersenne ≥ 71) := by
  decide +kernel

theorem false_uniform_certificate :
    ¬ (∀ n : Nat, n ≥ 2 ^ 71 → n % 2 = 1 → n % 4 = 3 →
       ∃ k : Nat, k > 0 ∧ k ≤ 200 ∧ oddCount k n ≤ 44 ∧
         k - oddCount k n ≥ 71) := by
  intro h
  obtain ⟨k, _, hk, ho, he⟩ :=
    h mersenne mersenne_input.1 mersenne_input.2.1 mersenne_input.2.2
  exact no_short_certificate ⟨k, by omega⟩ ⟨ho, he⟩

theorem impossible_integer_bound (r : Nat → Nat) :
    ¬ (∀ x : Nat, x % 4 = 1 → x > 1 →
       3 < 2 ^ (r x + 1) ∧ 2 ^ (r x + 1) < 4) := by
  intro h
  have hb := h 5 (by decide) (by decide)
  omega

theorem oracle_value_has_a_name (f : Nat → Nat) (n : Nat) :
    ∃ steps : Nat, f n = steps := ⟨f n, rfl⟩

#print axioms false_uniform_certificate
#print axioms impossible_integer_bound
#print axioms oracle_value_has_a_name

end FullProofExternalChecks
