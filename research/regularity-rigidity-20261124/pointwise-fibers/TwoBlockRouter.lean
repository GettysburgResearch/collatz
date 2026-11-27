module

public import OrdinaryFiber
public import Mathlib.Data.Fintype.Fin
public import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! A constant-clock pair of padded six-step Collatz blocks. -/

@[expose] public section

namespace TwoBlockRouter

open OrdinaryFiber
open RegularityRigidity (T)

def twoCarry (t : ℕ) : ℕ := 7 * 2 ^ t + 63

/-- Residue certificate at the full precision for preserving a ternary unit.
The coordinate `j` denotes the first block clock minus six. -/
theorem finite_split :
    ∀ r : Fin 243, r.val % 3 ≠ 0 → ∃ j : Fin 108,
      (2 ^ (119 - (j.val + 6)) * r.val) % 9 = 7 ∧
      (2 ^ 119 * r.val) % 81 = twoCarry (j.val + 6) % 81 ∧
      (2 ^ 119 * r.val) % 243 ≠ twoCarry (j.val + 6) % 243 := by
  decide +kernel

/-- Padded A branch on the source and its fivefold companion, in chronological order. -/
def sourceA (t : ℕ) : List Bool :=
  [true, false, true, false, false, false] ++ List.replicate (t - 6) false

def companionA (t : ℕ) : List Bool :=
  [true, false, false, false, false, true] ++ List.replicate (t - 6) false

private theorem zeros_carry (n : ℕ) : carry (List.replicate n false) = 0 := by
  induction n with
  | zero => rfl
  | succ n ih => simp [List.replicate_succ, carry, ih]

private theorem padded_profiles (t : ℕ) (ht : 6 ≤ t) :
    (sourceA t).length = t ∧ (companionA t).length = t ∧
    (sourceA t).count true = 2 ∧ (companionA t).count true = 2 ∧
    carry (sourceA t) = 7 ∧ carry (companionA t) = 35 := by
  simp [sourceA, companionA, carry, zeros_carry, List.count_replicate]
  omega

/-- The integer equation for a padded A block forces both chronological parity words. -/
theorem padded_block_iff (t : ℕ) (ht : 6 ≤ t) (x y : ℤ) :
    9 * x + 7 = (2 : ℤ) ^ t * y ↔
    (parityWord t x = sourceA t ∧ (T^[t]) x = y) ∧
      (parityWord t (5 * x) = companionA t ∧ (T^[t]) (5 * x) = 5 * y) := by
  obtain ⟨he, he', hp, hp', hc, hc'⟩ := padded_profiles t ht
  have h := paired_decoder (sourceA t) (companionA t) x y (he'.trans he.symm) (hp'.trans hp.symm)
  norm_num [he, he', hp, hc, hc'] at h
  exact h

/-- Natural residues lift to the exact two ordinary inverse equations and the terminal
fine test. The inner and outer padded clocks add to the same 119 for every target. -/
theorem target_split (q : ℕ) (hunit : q % 3 ≠ 0) :
    ∃ t s : ℕ, 6 ≤ t ∧ 6 ≤ s ∧ t + s = 119 ∧
      (9 : ℤ) ∣ 2 ^ s * (q : ℤ) - 7 ∧
      (81 : ℤ) ∣ 2 ^ 119 * (q : ℤ) - twoCarry t ∧
      ¬ (243 : ℤ) ∣ 2 ^ 119 * (q : ℤ) - twoCarry t := by
  let r : Fin 243 := ⟨q % 243, Nat.mod_lt _ (by decide)⟩
  have hqr : r.val ≡ q [MOD 243] := Nat.mod_modEq q 243
  have hr : r.val % 3 ≠ 0 := by
    change q % 243 % 3 ≠ 0
    rwa [Nat.mod_mod_of_dvd _ (by decide : 3 ∣ 243)]
  obtain ⟨j, h9, h81, h243⟩ := finite_split r hr
  let t := j.val + 6
  let s := 119 - t
  have hj := j.isLt
  refine ⟨t, s, by dsimp [t]; omega, by dsimp [s,t]; omega, by dsimp [s,t]; omega, ?_, ?_, ?_⟩
  · have hm : 7 ≡ 2 ^ s * q [MOD 9] :=
      (show 7 ≡ 2 ^ s * r.val [MOD 9] from h9.symm).trans
        ((hqr.of_dvd (by decide : 9 ∣ 243)).mul_left _)
    exact_mod_cast hm.dvd
  · have hm : twoCarry t ≡ 2 ^ 119 * q [MOD 81] :=
      (show twoCarry t ≡ 2 ^ 119 * r.val [MOD 81] from h81.symm).trans
        ((hqr.of_dvd (by decide : 81 ∣ 243)).mul_left _)
    exact_mod_cast hm.dvd
  · intro hd
    have hd' : (243 : ℤ) ∣ ((2 ^ 119 * q : ℕ) : ℤ) - (twoCarry t : ℤ) := by exact_mod_cast hd
    have he := ((Nat.modEq_of_dvd hd').trans (hqr.mul_left _).symm).symm
    exact h243 he

/-- Every supplied positive odd ordinary ternary unit has a positive odd unit paired
ancestor, through two indicated literal A blocks at the common total clock 119. -/
theorem two_block_router (q : ℕ) (hodd : q % 2 = 1) (hunit : q % 3 ≠ 0) :
    ∃ (t s : ℕ) (x y : ℤ), 6 ≤ t ∧ 6 ≤ s ∧ t + s = 119 ∧
      0 < x ∧ x % 2 = 1 ∧ ¬ (3 : ℤ) ∣ x ∧ 0 < y ∧ y % 2 = 1 ∧
      (parityWord t x = sourceA t ∧ (T^[t]) x = y) ∧
      (parityWord t (5 * x) = companionA t ∧ (T^[t]) (5 * x) = 5 * y) ∧
      (parityWord s y = sourceA s ∧ (T^[s]) y = q) ∧
      (parityWord s (5 * y) = companionA s ∧ (T^[s]) (5 * y) = 5 * q) := by
  obtain ⟨t, s, ht, hs, hclock, h9, h81, h243⟩ := target_split q hunit
  obtain ⟨y, hy⟩ := h9
  obtain ⟨x, hx⟩ := h81
  have hq : 1 ≤ (q : ℤ) := by omega
  have he : (2 : ℤ) ^ t * 2 ^ s = 2 ^ 119 := by rw [← pow_add, hclock]
  have hy' : 9 * y + 7 = (2 : ℤ) ^ s * q := by omega
  have h2 : (2 : ℤ) ^ 119 * q = 9 * (2 ^ t * y) + 7 * 2 ^ t := calc
    _ = (2 : ℤ) ^ t * (2 ^ s * (q : ℤ)) := by rw [← mul_assoc, he]
    _ = _ := by rw [← hy']; ring
  have hc : (twoCarry t : ℤ) = 7 * 2 ^ t + 63 := by simp [twoCarry]
  rw [hc, h2] at hx
  have hx' : 9 * x + 7 = (2 : ℤ) ^ t * y := by omega
  have hux : ¬ (3 : ℤ) ∣ x := by
    rintro ⟨z, hz⟩
    apply h243
    use z
    rw [h2, hc]
    omega
  have hl (n : ℕ) (hn : 6 ≤ n) : (64 : ℤ) ≤ 2 ^ n :=
    (show (2 : ℤ) ^ 6 ≤ 2 ^ n from pow_le_pow_right₀ (by decide) hn)
  have hqy := mul_le_mul_of_nonneg_left hq (by positivity : 0 ≤ (2 : ℤ) ^ s)
  have hsy := hl s hs
  have hypos : 0 < y := by simp only [mul_one] at hqy; omega
  have htx := hl t ht
  have hy1 : 1 ≤ y := by omega
  have hxy := mul_le_mul_of_nonneg_left hy1 (by positivity : 0 ≤ (2 : ℤ) ^ t)
  have hxpos : 0 < x := by simp only [mul_one] at hxy; omega
  have h1 := (padded_block_iff t ht x y).mp hx'
  have h2' := (padded_block_iff s hs y q).mp hy'
  have odd (n : ℕ) (hn : 6 ≤ n) (z : ℤ) (hh : parityWord n z = sourceA n) :
      z % 2 = 1 := by
    have hlen := (padded_profiles n hn).1
    have hw : parityWord (sourceA n).length z = sourceA n := by rw [hlen]; exact hh
    exact odd_source_of_word (sourceA n) z (by rfl) hw
  exact ⟨t, s, x, y, ht, hs, hclock, hxpos, odd t ht x h1.1.1, hux, hypos,
    odd s hs y h2'.1.1, h1.1, h1.2, h2'.1, h2'.2⟩

#print axioms finite_split
#print axioms zeros_carry
#print axioms padded_profiles
#print axioms padded_block_iff
#print axioms target_split
#print axioms two_block_router

end TwoBlockRouter
