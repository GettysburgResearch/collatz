import Mathlib.Data.Finset.Card
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Exact source shells and finite transport on the original indices.
The renewal population and the rotation discrepancy estimates are written mathematics. -/

namespace Collatz.TraceWindow

/-- Appending the inverse gap to a supplied positive gate keeps the affine
    prefix's offset at its exact scale. The center is in original source units. -/
theorem source_shell_identity {x t a scale gap center beta : ℚ}
    (pref : t = scale*x+beta) (last : gap*a = 3*t+1)
    (norm : gap*a = 3*scale*center) :
    3*scale*(center-x) = 1+3*beta := by linarith

/-- Scaled band inequalities avoid division by the center, so the statement
    also records exactly which two positive denominators are needed. -/
theorem source_shell_band {x t a scale gap center beta F : ℚ}
    (pref : t = scale*x+beta) (last : gap*a = 3*t+1)
    (norm : gap*a = 3*scale*center) (cpos : 0 < center)
    (gpos : 0 < gap*a) (beta0 : 0 ≤ beta) (betaF : beta ≤ F) :
    1/(gap*a) ≤ 1-x/center ∧ 1-x/center ≤ (1+3*F)/(gap*a) := by
  have eq := source_shell_identity pref last norm
  have linear : gap*a = 3*scale*center := norm
  have cp : center ≠ 0 := ne_of_gt cpos
  have dividen : (1-x/center)*(gap*a) = 1+3*beta := by
    calc
      _ = ((center-x)/center)*(gap*a) := by rw [sub_div,div_self cp]
      _ = (center-x)*(3*scale) := by
        rw [linear, mul_comm (3*scale) center, ← mul_assoc, div_mul_cancel₀ _ cp]
      _ = 1+3*beta := by rw [mul_comm, eq]
  constructor
  · apply (div_le_iff₀ gpos).mpr
    linarith
  · apply (le_div_iff₀ gpos).mpr
    linarith

/-- Multiplying a unit residue by a power of two finds one of the residues
    for which the divided predecessor is odd and prime to three. -/
theorem find_predecessor_residue (v : ℕ) (hv : v < 9) (hu : v % 3 ≠ 0) :
    ∃ d : Fin 6, (2^(d:ℕ)*v)%9 = 4 ∨ (2^(d:ℕ)*v)%9 = 7 := by
  have cases : v=0 ∨ v=1 ∨ v=2 ∨ v=3 ∨ v=4 ∨ v=5 ∨ v=6 ∨ v=7 ∨ v=8 := by omega
  rcases cases with h|h|h|h|h|h|h|h|h <;> subst v <;> first | exact (hu (by decide)).elim | decide

/-- Addition over disjoint chronological blocks charges each recorded unit
    of variation once. The entries are signed count errors and variations. -/
theorem variation_ledger (blocks : List (ℚ × ℚ)) (fixed mult : ℚ)
    (perBlock : ∀ p ∈ blocks, |p.1| ≤ fixed+mult*p.2) :
    |(blocks.map Prod.fst).sum| ≤ blocks.length*fixed+mult*(blocks.map Prod.snd).sum := by
  induction blocks with
  | nil => simp
  | cons p rest ih =>
    have h := perBlock p (.head _)
    have tail := ih (fun t ht => perBlock t (.tail _ ht))
    simp only [List.map_cons,List.sum_cons,List.length_cons,Nat.cast_add,Nat.cast_one]
    calc
      _ ≤ |p.1| + |(rest.map Prod.fst).sum| := abs_add_le _ _
      _ ≤ (fixed+mult*p.2)+(rest.length*fixed+mult*(rest.map Prod.snd).sum) := add_le_add h tail
      _ = _ := by ring

/-- The low-terminal cutoff may be counted just among the observed arc
    indices. The retained distinct terminals preserve their cardinality. -/
theorem retained_terminals (arc cutoff : Finset ℕ) (q : ℕ → ℕ)
    (distinct : ∀ i ∈ arc, ∀ j ∈ arc, q i = q j → i=j) :
    ((arc \ cutoff).image q).card + (arc ∩ cutoff).card = arc.card := by
  classical
  have sub : arc \ cutoff ⊆ arc := Finset.sdiff_subset
  have inj : Set.InjOn q (↑(arc \ cutoff) : Set ℕ) :=
    fun i hi j hj eq => distinct i (sub hi) j (sub hj) eq
  rw [Finset.card_image_of_injOn inj]
  exact Finset.card_sdiff_add_card_inter _ _

/-- One fixed-clock word has one ternary offset. Coverage of all required
    offset residues therefore consumes at least as many words as residues. -/
theorem residue_image_ceiling (words targets : Finset ℕ) (offset : ℕ → ℕ)
    (coverage : ∀ r ∈ targets, ∃ w ∈ words, offset w=r) :
    targets.card ≤ words.card := by
  classical
  have contained : targets ⊆ words.image offset := by
    intro r hr
    obtain ⟨w,hw,eq⟩ := coverage r hr
    exact Finset.mem_image.mpr ⟨w,hw,eq⟩
  exact (Finset.card_le_card contained).trans Finset.card_image_le

theorem translated_exponents : 3^24 < (2:ℕ)^39 ∧ 5^40 < (2:ℕ)^55*3^24 := by decide

#print axioms source_shell_identity
#print axioms source_shell_band
#print axioms find_predecessor_residue
#print axioms variation_ledger
#print axioms retained_terminals
#print axioms residue_image_ceiling
#print axioms translated_exponents

end Collatz.TraceWindow
