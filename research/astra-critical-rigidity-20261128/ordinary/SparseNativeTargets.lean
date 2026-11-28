import AffineOrbit
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-! Exact decoding of ordinary values in an odd-gap calendar and a finite
union bound on physical sources. The stationary and limiting estimates are
separate written arguments. -/

namespace Collatz.SparseNativeTargets

open Collatz.PoweredAffine

private theorem three_pow_mod_two (k : ℕ) : 3 ^ k % 2 = 1 := by
  induction k with
  | zero => decide
  | succ k ih => rw [pow_succ, Nat.mul_mod, ih]

/-- The balance for the actual shortcut forces every stated parity and its
integer endpoint, even when either integer is zero. -/
theorem native_balance_iff (w : List Bool) (n y : ℕ) :
    2 ^ w.length * y = 3 ^ ones w * n + numerator w ↔
      Realizes n w ∧ orbit n w.length = y := by
  constructor
  · induction w generalizing n with
    | nil => simp [ones, numerator, Realizes, orbit, eq_comm]
    | cons b w ih =>
      intro balance
      let z := if b then 3 * n + 1 else n
      have paired : 2 * (2 ^ w.length * y) = 3 ^ ones w * z + 2 * numerator w := by
        cases b <;> simp only [List.length_cons, pow_succ, ones, numerator, z,
          Bool.false_eq_true, ↓reduceIte, zero_add, mul_zero, mul_one] at balance ⊢
        · nlinarith only [balance]
        · rw [pow_add, pow_one] at balance
          nlinarith only [balance]
      have hz : z % 2 = 0 := by
        have h := congrArg (fun v : ℕ => v % 2) paired
        change (2 * (2 ^ w.length * y)) % 2 =
          (3 ^ ones w * z + 2 * numerator w) % 2 at h
        rw [Nat.add_mod, Nat.mul_mod (3 ^ ones w) z, three_pow_mod_two] at h
        omega
      have hb : n % 2 = (if b then 1 else 0) := by
        cases b <;> simp only [z, Bool.false_eq_true, ↓reduceIte] at hz ⊢ <;> omega
      have hs : 2 * step n = z := by
        cases b with
        | false => exact even_step hb
        | true => exact odd_step hb
      have ht : 2 ^ w.length * y = 3 ^ ones w * step n + numerator w := by
        rw [← hs] at paired
        nlinarith only [paired]
      obtain ⟨hr, hy⟩ := ih (step n) ht
      exact ⟨⟨hb, hr⟩, hy⟩
  · rintro ⟨h, rfl⟩
    exact actual_word_affine h

/-- The height threshold and ternary divisor exactly characterize physical
integer targets for a supplied word. -/
theorem target_exists_iff (w : List Bool) (y : ℕ) :
    (∃ n : ℕ, Realizes n w ∧ orbit n w.length = y) ↔
      numerator w ≤ 2 ^ w.length * y ∧ 3 ^ ones w ∣ 2 ^ w.length * y - numerator w := by
  constructor
  · rintro ⟨n, h⟩
    have e := (native_balance_iff w n y).mpr h
    refine ⟨by omega, n, by omega⟩
  · rintro ⟨h, n, e⟩
    exact ⟨n, (native_balance_iff w n y).mp (by omega)⟩

/-- A calendar entry records the number of even departures after its odd one.
Hence the actual Syracuse valuation is one plus that entry. -/
def gapWord : List ℕ → List Bool
  | [] => []
  | e :: v => true :: (List.replicate e false ++ gapWord v)

private theorem even_prefix (e : ℕ) (w : List Bool) :
    ones (List.replicate e false ++ w) = ones w ∧
      numerator (List.replicate e false ++ w) = 2 ^ e * numerator w := by
  induction e with
  | zero => simp
  | succ e ih =>
    simp only [List.replicate_succ, List.cons_append, ones, numerator, Bool.false_eq_true,
      ↓reduceIte, zero_add, mul_zero, ih.1, ih.2, pow_succ]
    constructor
    · trivial
    · ring

def gapCarry : List ℕ → ℕ
  | [] => 0
  | e :: v => 3 ^ v.length + 2 ^ (e + 1) * gapCarry v

theorem gapWord_counts (v : List ℕ) :
    ones (gapWord v) = v.length ∧ (gapWord v).length = v.length + v.sum ∧
      numerator (gapWord v) = gapCarry v := by
  induction v with
  | nil => simp [gapWord, ones, numerator, gapCarry]
  | cons e v ih =>
    have hp := even_prefix e (gapWord v)
    simp only [gapWord, ones, numerator, ↓reduceIte, mul_one, hp.1, hp.2,
      List.length_cons, List.length_append, List.length_replicate, List.sum_cons, gapCarry,
      ih.1, ih.2.1, ih.2.2, pow_succ]
    exact ⟨by omega, by omega, by ring⟩

private theorem realized_suffix {n : ℕ} {v w : List Bool} (h : Realizes n (v ++ w)) :
    Realizes (orbit n v.length) w ∧
      orbit n (v ++ w).length = orbit (orbit n v.length) w.length := by
  induction v generalizing n with
  | nil => exact ⟨h, rfl⟩
  | cons b v ih => exact ih h.2

/-- The last gap list fixes the ternary residue after clearing the power of
two, regardless of all earlier native departures. -/
theorem actual_suffix_gap_residue {n : ℕ} {v : List Bool} {gaps : List ℕ}
    (h : Realizes n (v ++ gapWord gaps)) :
    (2 ^ (gaps.length + gaps.sum) * orbit n (v ++ gapWord gaps).length) % 3 ^ gaps.length =
      gapCarry gaps % 3 ^ gaps.length := by
  obtain ⟨hr, he⟩ := realized_suffix h
  have hc := actual_word_affine hr
  obtain ⟨hg, hl, hn⟩ := gapWord_counts gaps
  rw [he, ← hl, hc, hg, hn, Nat.add_mod]
  simp

noncomputable def visits (sources targets : Finset ℕ) (word : List Bool) : Finset ℕ :=
  by classical exact sources.filter (fun n => Realizes n word ∧ orbit n word.length ∈ targets)

def targetsAt (targets : Finset ℕ) (word : List Bool) : Finset ℕ :=
  targets.filter (fun y => (2 ^ word.length * y) % 3 ^ ones word = numerator word % 3 ^ ones word)

/-- The full physical hit count is bounded by one target residue count per
calendar, including lists that can witness the same source more than once. -/
theorem finite_visits_le (sources targets : Finset ℕ) (words : Finset (List Bool)) :
    (words.biUnion (visits sources targets)).card ≤
      ∑ w ∈ words, (targetsAt targets w).card := by
  classical
  refine Finset.card_biUnion_le.trans (Finset.sum_le_sum fun w _ => ?_)
  apply Finset.card_le_card_of_injOn (fun n => orbit n w.length)
  · intro n h
    obtain ⟨_, hr, hy⟩ := Finset.mem_filter.mp (show n ∈ visits sources targets w from h)
    apply Finset.mem_filter.mpr
    refine ⟨hy, ?_⟩
    rw [actual_word_affine hr, Nat.add_mod]
    simp
  · intro n hn m hm e
    have an := actual_word_affine (Finset.mem_filter.mp
      (show n ∈ visits sources targets w from hn)).2.1
    have am := actual_word_affine (Finset.mem_filter.mp
      (show m ∈ visits sources targets w from hm)).2.1
    change orbit n w.length = orbit m w.length at e
    rw [e, am] at an
    have hpos : 0 < 3 ^ ones w := by positivity
    exact Nat.eq_of_mul_eq_mul_left hpos (by omega)

end Collatz.SparseNativeTargets
