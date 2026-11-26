import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Fintype.Card
import Lean.Elab.Tactic.Omega

/-! A list of independent binary carry changes, each a unit modulo a fixed
    integer, attains every residue after at most modulus minus one changes. -/

namespace ModularCarry

variable {m : ℕ} [NeZero m]

/-- Adjoin the option of adding one unit. -/
def step (u : (ZMod m)ˣ) (s : Finset (ZMod m)) : Finset (ZMod m) :=
  s ∪ s.image (fun x => x + (u : ZMod m))

/-- All subset sums of the listed increments. -/
def sums : List (ZMod m)ˣ → Finset (ZMod m)
  | [] => {0}
  | u :: us => step u (sums us)

omit [NeZero m] in
theorem seed_mem (us : List (ZMod m)ˣ) : 0 ∈ sums us := by
  induction us with
  | nil => simp [sums]
  | cons u us ih => exact Finset.mem_union_left _ ih

theorem fixed_univ (u : (ZMod m)ˣ) (s : Finset (ZMod m))
    (hz : 0 ∈ s) (hf : step u s = s) : s = Finset.univ := by
  have next (x : ZMod m) (hx : x ∈ s) : x + (u : ZMod m) ∈ s := by
    rw [← hf]
    exact Finset.mem_union_right _ (Finset.mem_image.mpr ⟨x, hx, rfl⟩)
  have allNat (n : ℕ) : n • (u : ZMod m) ∈ s := by
    induction n with
    | zero => simpa using hz
    | succ n ih => rw [succ_nsmul]; exact next _ ih
  apply Finset.eq_univ_of_forall
  intro y
  have h := allNat (y * (↑(u⁻¹) : ZMod m)).val
  simpa [mul_assoc] using h

theorem gains (u : (ZMod m)ˣ) (s : Finset (ZMod m))
    (hz : 0 ∈ s) (hs : s ≠ Finset.univ) : s.card < (step u s).card := by
  apply Finset.card_lt_card
  apply Finset.ssubset_iff_subset_ne.mpr
  exact ⟨Finset.subset_union_left, fun h => hs (fixed_univ u s hz h.symm)⟩

theorem cardinal_bound (us : List (ZMod m)ˣ) :
    min (us.length + 1) m ≤ (sums us).card := by
  induction us with
  | nil => simp [sums]
  | cons u us ih =>
    by_cases h : sums us = Finset.univ
    · rw [sums, step, h, Finset.union_eq_left.mpr (Finset.subset_univ _)]
      simpa only [Finset.card_univ, ZMod.card] using (Nat.min_le_right ((u :: us).length + 1) m)
    · have hgain := gains u (sums us) (seed_mem us) h
      simp only [sums, List.length_cons]
      omega

theorem all_residues (us : List (ZMod m)ˣ) (h : m ≤ us.length + 1) :
    sums us = Finset.univ := by
  have hc := cardinal_bound us
  rw [Nat.min_eq_right h] at hc
  apply Finset.eq_univ_of_card
  have hmax := (sums us).card_le_univ
  rw [ZMod.card] at hmax ⊢
  omega

/-- Advancing the selected odd dates by one doubles precisely their carry terms. -/
theorem shifted_carry (p : ℕ) (dates : Fin p → ℕ) (chosen : Finset (Fin p)) :
    (∑ i : Fin p, 3 ^ (p - 1 - i.val) * 2 ^ (dates i + if i ∈ chosen then 1 else 0)) =
      (∑ i : Fin p, 3 ^ (p - 1 - i.val) * 2 ^ dates i) +
        ∑ i ∈ chosen, 3 ^ (p - 1 - i.val) * 2 ^ dates i := by
  classical
  let term (i : Fin p) : ℕ := 3 ^ (p - 1 - i.val) * 2 ^ dates i
  have each (i : Fin p) :
      3 ^ (p - 1 - i.val) * 2 ^ (dates i + if i ∈ chosen then 1 else 0) =
        term i + if i ∈ chosen then term i else 0 := by
    by_cases h : i ∈ chosen
    · simp [h, term, pow_succ, Nat.mul_two, Nat.mul_add]
    · simp [h, term]
  simp only [each, Finset.sum_add_distrib]
  simp [term]

#print axioms shifted_carry

#print axioms seed_mem
#print axioms fixed_univ
#print axioms gains
#print axioms cardinal_bound
#print axioms all_residues

end ModularCarry
