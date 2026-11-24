import CarryFibers

/-!
# Finite ordinary-word pressure at the original source height

The shortcut map and its chronological parity prefix are defined here on
ordinary natural numbers. Their complete affine identity is proved before
using it: no freely chosen modular representative replaces a source.

Below the original binary precision the parity-prefix map is injective.
At arbitrary height a word has at most one source in each binary quotient
cell. These finite arithmetic facts are the inputs to the written entropy
inequality in FIXED_SOURCE_PRESSURE.md. Shannon entropy, stationary limits,
and an all-time Collatz conclusion are not formalized in this module.
-/

namespace CollatzShell.FixedSourcePressure

open Collatz.HighVariance.CycleWordAlgebra
open CollatzShell.CarryFibers

set_option autoImplicit false

def shortcut (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def parity (n : Nat) : Bool := decide (n % 2 = 1)

def endpoint (n : Nat) : Nat → Nat
  | 0 => n
  | m + 1 => endpoint (shortcut n) m

def parityPrefix (n : Nat) : Nat → List Bool
  | 0 => []
  | m + 1 => parity n :: parityPrefix (shortcut n) m

theorem parityPrefix_length (n m : Nat) : (parityPrefix n m).length = m := by
  induction m generalizing n with
  | zero => rfl
  | succ m ih => simp [parityPrefix, ih]

/-- The ordinary shortcut branch, including its integer affine correction. -/
theorem shortcut_affine (n : Nat) :
    2 * shortcut n =
      3 ^ (if parity n then 1 else 0) * n + (if parity n then 1 else 0) := by
  have hm : n % 2 < 2 := Nat.mod_lt _ (by decide)
  by_cases h : n % 2 = 0
  · simp [shortcut, parity, h]
    omega
  · have h1 : n % 2 = 1 := by omega
    simp [shortcut, parity, h1]
    omega

/-- Every actual finite ordinary prefix retains the complete chronological
carry, rather than only a residue or a truncated correction. -/
theorem parityPrefix_affine (n m : Nat) :
    2 ^ m * endpoint n m =
      3 ^ ones (parityPrefix n m) * n + carry (parityPrefix n m) := by
  induction m generalizing n with
  | zero => simp [endpoint, parityPrefix, ones, carry]
  | succ m ih =>
    have hs := shortcut_affine n
    have ht := ih (shortcut n)
    simp only [endpoint, parityPrefix, ones, carry]
    calc
      2 ^ (m + 1) * endpoint (shortcut n) m =
          2 * (2 ^ m * endpoint (shortcut n) m) := by ring
      _ = 2 * (3 ^ ones (parityPrefix (shortcut n) m) * shortcut n +
          carry (parityPrefix (shortcut n) m)) := by rw [ht]
      _ = 3 ^ ones (parityPrefix (shortcut n) m) * (2 * shortcut n) +
          2 * carry (parityPrefix (shortcut n) m) := by ring
      _ = 3 ^ ones (parityPrefix (shortcut n) m) *
          (3 ^ (if parity n then 1 else 0) * n + (if parity n then 1 else 0)) +
          2 * carry (parityPrefix (shortcut n) m) := by rw [hs]
      _ = 3 ^ ((if parity n then 1 else 0) + ones (parityPrefix (shortcut n) m)) * n +
          (3 ^ ones (parityPrefix (shortcut n) m) * (if parity n then 1 else 0) +
          2 * carry (parityPrefix (shortcut n) m)) := by rw [pow_add]; ring

/-- Two occurrences of the same actual parity prefix have the same original
source residue at the full binary clock. -/
theorem same_prefix_source_mod {n₁ n₂ m : Nat}
    (hw : parityPrefix n₁ m = parityPrefix n₂ m) :
    n₁ % (2 ^ m) = n₂ % (2 ^ m) := by
  have h₁ := parityPrefix_affine n₁ m
  have h₂ := parityPrefix_affine n₂ m
  rw [hw] at h₁
  exact same_carry_source_mod h₁ h₂

/-- Below the actual source-height precision, equal words force equal
ordinary sources. This includes the full carry and both endpoints. -/
theorem source_eq_of_prefix_of_height {n₁ n₂ m : Nat}
    (h₁ : n₁ < 2 ^ m) (h₂ : n₂ < 2 ^ m)
    (hw : parityPrefix n₁ m = parityPrefix n₂ m) : n₁ = n₂ := by
  simpa [Nat.mod_eq_of_lt h₁, Nat.mod_eq_of_lt h₂] using same_prefix_source_mod hw

/-- The exact finite word count at height below one binary modulus. -/
theorem prefix_image_card (S : Finset Nat) (m : Nat)
    (hh : ∀ n ∈ S, n < 2 ^ m) :
    (S.image (fun n => parityPrefix n m)).card = S.card := by
  apply Finset.card_image_of_injOn
  intro n₁ hn₁ n₂ hn₂ hw
  exact source_eq_of_prefix_of_height (hh n₁ hn₁) (hh n₂ hn₂) hw

/-- Arbitrary height pays exactly for binary source cells. In particular,
repeated words are counted with their original source multiplicity. -/
theorem prefix_fiber_card_le (S : Finset Nat) (m H : Nat) (w : List Bool)
    (hh : ∀ n ∈ S, n ≤ H) :
    (S.filter (fun n => parityPrefix n m = w)).card ≤ H / (2 ^ m) + 1 := by
  have hc : (S.filter (fun n => parityPrefix n m = w)).card ≤
      (Finset.range (H / (2 ^ m) + 1)).card := by
    apply Finset.card_le_card_of_injOn (fun n => n / (2 ^ m))
    · intro n hn
      apply Finset.mem_range.mpr
      have hle : n / (2 ^ m) ≤ H / (2 ^ m) :=
        Nat.div_le_div_right (hh n (Finset.mem_filter.mp hn).1)
      exact Nat.lt_succ_of_le hle
    · intro n₁ hn₁ n₂ hn₂ he
      have hw : parityPrefix n₁ m = parityPrefix n₂ m :=
        (Finset.mem_filter.mp hn₁).2.trans (Finset.mem_filter.mp hn₂).2.symm
      have h₁ := parityPrefix_affine n₁ m
      have h₂ := parityPrefix_affine n₂ m
      rw [hw] at h₁
      exact (same_carry_same_source_block h₁ h₂ he).1
  simpa using hc

end CollatzShell.FixedSourcePressure
