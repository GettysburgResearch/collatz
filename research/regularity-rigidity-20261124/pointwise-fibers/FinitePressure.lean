module

public import Mathlib.Basic.Real.Basic
public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! The finite mass-to-multiplicity estimate at one prescribed clock type. -/

@[expose] public section

namespace FinitePressure

open scoped BigOperators

/-- Each selected event cell has mass at most its multiplicity divided by `W`, and
multiplicity at most `M`. If the total event mass is at least `u`, then cells with
multiplicity at least `uG/4` account for at least half of that mass in this count bound. -/
theorem mass_split {A : Type*} (s : Finset A) (m n : A → ℝ) (u G W M : ℝ)
    (hu : 0 ≤ u) (hG : 0 ≤ G) (hW : 0 ≤ W)
    (hsize : (s.card : ℝ) * G ≤ 2 * W)
    (htotal : u ≤ ∑ a ∈ s, m a)
    (hcell : ∀ a ∈ s, m a * W ≤ n a) (hcap : ∀ a ∈ s, n a ≤ M) :
    u * W ≤ 2 * ((s.filter (fun a => u * G / 4 ≤ n a)).card : ℝ) * M := by
  classical
  let good := s.filter (fun a => u * G / 4 ≤ n a)
  let bad := s.filter (fun a => ¬ u * G / 4 ≤ n a)
  have hsum := Finset.sum_filter_add_sum_filter_not s (fun a => u * G / 4 ≤ n a)
      (fun a => m a * W)
  change (∑ a ∈ good, m a * W) + (∑ a ∈ bad, m a * W) = _ at hsum
  have hgood : (∑ a ∈ good, m a * W) ≤ (good.card : ℝ) * M := calc
    _ ≤ ∑ _a ∈ good, M := by
      apply Finset.sum_le_sum
      intro a ha
      have hs := (Finset.mem_filter.mp ha).1
      exact (hcell a hs).trans (hcap a hs)
    _ = _ := by simp
  have hbad : (∑ a ∈ bad, m a * W) ≤ (s.card : ℝ) * (u * G / 4) := calc
    _ ≤ ∑ _a ∈ bad, u * G / 4 := by
      apply Finset.sum_le_sum
      intro a ha
      obtain ⟨hs, hn⟩ := Finset.mem_filter.mp ha
      exact (hcell a hs).trans (le_of_lt (lt_of_not_ge hn))
    _ = (bad.card : ℝ) * (u * G / 4) := by simp
    _ ≤ _ := by
      have hcard : bad.card ≤ s.card := Finset.card_le_card (Finset.filter_subset _ _)
      exact mul_le_mul_of_nonneg_right (by exact_mod_cast hcard) (by positivity)
  have hhalf : (s.card : ℝ) * (u * G / 4) ≤ u * W / 2 := by
    nlinarith only [mul_le_mul_of_nonneg_left hsize hu]
  have hmass := mul_le_mul_of_nonneg_right htotal hW
  rw [Finset.sum_mul, ← hsum] at hmass
  change u * W ≤ 2 * (good.card : ℝ) * M
  linarith [hbad.trans hhalf]

/-- At common clocks `(e,p)`, at most `2·3^p` fine unit residues support the event.
With the supplied fixed-clock cap `1 + B G`, this gives a lower bound on the
number of residues of multiplicity at least `uG/4`. -/
theorem fixed_clock_split {A : Type*} (s : Finset A) (m : A → ℝ) (N : A → ℕ)
    (e p : ℕ) (u B : ℝ) (hu : 0 ≤ u) (hs : s.card ≤ 2 * 3 ^ p)
    (htotal : u ≤ ∑ a ∈ s, m a)
    (hcell : ∀ a ∈ s, m a * 2 ^ e ≤ (N a : ℝ))
    (hcap : ∀ a ∈ s, (N a : ℝ) ≤ 1 + B * (2 ^ e / 3 ^ p)) :
    u * 2 ^ e ≤
      2 * ((s.filter (fun a => u * (2 ^ e / 3 ^ p) / 4 ≤ (N a : ℝ))).card : ℝ) *
        (1 + B * (2 ^ e / 3 ^ p)) := by
  have hc : (s.card : ℝ) ≤ 2 * (3 : ℝ) ^ p := by exact_mod_cast hs
  have hp : 0 < (3 : ℝ) ^ p := by positivity
  have hsize : (s.card : ℝ) * ((2 : ℝ) ^ e / 3 ^ p) ≤ 2 * 2 ^ e := calc
    _ ≤ (2 * 3 ^ p) * (2 ^ e / 3 ^ p) := mul_le_mul_of_nonneg_right hc (by positivity)
    _ = _ := by rw [mul_assoc, mul_div_cancel₀ _ hp.ne']
  exact mass_split s m (fun a => (N a : ℝ)) u _ _ _ hu (by positivity) (by positivity)
    hsize htotal hcell hcap

#print axioms mass_split
#print axioms fixed_clock_split

end FinitePressure
