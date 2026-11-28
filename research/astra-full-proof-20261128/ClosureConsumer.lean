import ParityTail

/-! The full universal consumer of the one-sided five-clock parity target.
The positive-density theorem is an explicit external premise. The upper-tail
premise is OPEN; no theorem in this file asserts it. -/

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.FullProof.Closure

open Parity

noncomputable def badSources (X : ℕ) : Finset ℕ := by
  classical
  exact (Finset.range (X + 1)).filter Nonconvergent

def tailSources (X k : ℕ) : Finset ℕ :=
  (Finset.range (X + 1)).filter
    (fun n => 0 < n ∧ 501 * (5 * k) ≤ 1000 * count n (5 * k))

theorem bad_card_le_tail {k : ℕ} (hk : 0 < k) :
    (badSources (2 ^ k)).card ≤ (tailSources (2 ^ k) k).card := by
  classical
  apply Finset.card_le_card
  intro n hn
  simp only [badSources, Finset.mem_filter, Finset.mem_range] at hn
  simp only [tailSources, Finset.mem_filter, Finset.mem_range]
  exact ⟨hn.1, hn.2.1,
    le_of_lt (fifth_clock_needs_high_count hn.2 hk (by omega))⟩

def CounterexampleDensity : Prop :=
  (∃ n, Nonconvergent n) →
    ∃ d X₀ : ℕ, 0 < d ∧ ∀ X : ℕ, X₀ ≤ X →
      X ≤ d * (badSources X).card

def RealCounterexampleDensity : Prop :=
  (∃ n, Nonconvergent n) →
    ∃ c : ℝ, 0 < c ∧ ∃ X₀ : ℕ, ∀ X : ℕ, X₀ ≤ X →
      c * (X : ℝ) ≤ ((badSources X).card : ℝ)

theorem integer_density_of_real (density : RealCounterexampleDensity) :
    CounterexampleDensity := by
  intro hbad
  obtain ⟨c, hc, X₀, hX⟩ := density hbad
  obtain ⟨d, hd⟩ := exists_nat_gt (1 / c)
  have hd0 : 0 < d := by
    have hpos : (0 : ℝ) < (d : ℝ) := lt_trans (by positivity) hd
    exact_mod_cast hpos
  have hdc : (1 : ℝ) < (d : ℝ) * c := (div_lt_iff₀ hc).mp hd
  refine ⟨d, X₀, hd0, ?_⟩
  intro X hlarge
  have hx := hX X hlarge
  have hprod : (X : ℝ) ≤ (d : ℝ) * ((badSources X).card : ℝ) := by
    have hmul := mul_le_mul_of_nonneg_left hx (Nat.cast_nonneg d)
    have hscale := mul_le_mul_of_nonneg_right (le_of_lt hdc) (Nat.cast_nonneg X)
    nlinarith
  exact_mod_cast hprod

/-- Only an unbounded subsequence with a vanishing proportion is needed. -/
def UpperTailSubsequence : Prop :=
  ∀ d K : ℕ, 0 < d → ∃ k : ℕ,
    K ≤ k ∧ 0 < k ∧ d * (tailSources (2 ^ k) k).card < 2 ^ k

private theorem source_scale (k : ℕ) : k ≤ 2 ^ k := by
  induction k with
  | zero => simp
  | succ k ih =>
    have hp : 0 < 2 ^ k := by positivity
    simp only [pow_succ]
    omega

theorem all_reach_one_of_upper_tail
    (density : CounterexampleDensity) (tail : UpperTailSubsequence) :
    ∀ n : ℕ, 0 < n → ∃ t : ℕ, run n t = 1 := by
  classical
  intro n hn
  by_contra h
  have hbad : Nonconvergent n := ⟨hn, by simpa only [not_exists] using h⟩
  obtain ⟨d, X₀, hd, hbound⟩ := density ⟨n, hbad⟩
  obtain ⟨k, hkX, hk, htail⟩ := tail d X₀ hd
  have hlarge : X₀ ≤ 2 ^ k := le_trans hkX (source_scale k)
  have hlower := hbound (2 ^ k) hlarge
  have hinclusion := Nat.mul_le_mul_left d (bad_card_le_tail hk)
  omega

theorem all_reach_one_of_real_density_and_upper_tail
    (density : RealCounterexampleDensity) (tail : UpperTailSubsequence) :
    ∀ n : ℕ, 0 < n → ∃ t : ℕ, run n t = 1 :=
  all_reach_one_of_upper_tail (integer_density_of_real density) tail

#print axioms bad_card_le_tail
#print axioms integer_density_of_real
#print axioms all_reach_one_of_real_density_and_upper_tail

end Collatz.FullProof.Closure
