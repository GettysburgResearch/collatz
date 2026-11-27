import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Nat.GCD.Basic

/-! Adjacent ordered gaps accumulate a factor of three on every edge on
which the additive corrections at the two ends agree. -/

namespace CollatzRankGaps

variable {G : Type*} [DecidableEq G]

/-- Endpoints whose last `k` edges include a marked departure. -/
def markedPast (next : Equiv.Perm G) (marks : Finset G) : ℕ → Finset G
  | 0 => ∅
  | k + 1 => ((markedPast next marks k) ∪ marks).image next

theorem markedPast_card (next : Equiv.Perm G) (marks : Finset G) (k : ℕ) :
    (markedPast next marks k).card ≤ k * marks.card := by
  induction k with
  | zero => simp [markedPast]
  | succ k ih =>
    calc
      _ ≤ ((markedPast next marks k) ∪ marks).card := Finset.card_image_le
      _ ≤ (markedPast next marks k).card + marks.card := Finset.card_union_le _ _
      _ ≤ (k + 1) * marks.card := by rw [Nat.succ_mul]; omega

/-- The predecessor may divide by any power of two. -/
theorem cleanPast_dvd (next : Equiv.Perm G) (marks : Finset G) (gap clocks : G → ℕ)
    (edge : ∀ x ∉ marks, 2 ^ clocks x * gap (next x) = 3 * gap x)
    (k : ℕ) : ∀ y ∉ markedPast next marks k, 3 ^ k ∣ gap y := by
  induction k with
  | zero => simp
  | succ k ih =>
    intro y hy
    let x := next.symm y
    have hn : next x = y := next.apply_symm_apply y
    have hx : x ∉ markedPast next marks k ∪ marks := by
      intro h
      exact hy (Finset.mem_image.mpr ⟨x, h, hn⟩)
    have hp : x ∉ markedPast next marks k := fun h => hx (Finset.mem_union_left _ h)
    have hm : x ∉ marks := fun h => hx (Finset.mem_union_right _ h)
    have hd : 3 ^ (k + 1) ∣ 2 ^ clocks x * gap y := by
      rw [← hn, edge x hm, pow_succ']
      exact Nat.mul_dvd_mul_left _ (ih x hp)
    have hc : Nat.Coprime (3 ^ (k + 1)) (2 ^ clocks x) :=
      ((by decide : Nat.Coprime 3 2).pow_left _).pow_right _
    exact hc.dvd_of_dvd_mul_left hd

/-- A quantitative bound at every inspection length, on an entire finite cycle
or permutation. Truncated subtraction also handles large marked sets. -/
theorem rank_gap_budget [Fintype G] (next : Equiv.Perm G) (marks : Finset G) (gap clocks : G → ℕ)
    (positive : ∀ x, 0 < gap x)
    (edge : ∀ x ∉ marks, 2 ^ clocks x * gap (next x) = 3 * gap x)
    (k : ℕ) :
    (Fintype.card G - k * marks.card) * 3 ^ k ≤ ∑ x, gap x := by
  let good := Finset.univ \ markedPast next marks k
  have hc : Fintype.card G - k * marks.card ≤ good.card := by
    dsimp [good]
    rw [Finset.card_sdiff_of_subset (Finset.subset_univ _), Finset.card_univ]
    exact Nat.sub_le_sub_left (markedPast_card next marks k) _
  calc
    _ ≤ good.card * 3 ^ k := Nat.mul_le_mul_right _ hc
    _ = ∑ _x ∈ good, 3 ^ k := by simp
    _ ≤ ∑ x ∈ good, gap x := by
      apply Finset.sum_le_sum
      intro x hx
      exact Nat.le_of_dvd (positive x) (cleanPast_dvd next marks gap clocks edge k x
        (Finset.mem_sdiff.mp hx).2)
    _ ≤ ∑ x, gap x :=
      Finset.sum_le_sum_of_subset_of_nonneg (Finset.subset_univ _) (by simp)

/-- Exact normalized adjacent-gap arithmetic, including a carry at the seam.
If the next upper endpoint changes octave, `upper` is its lifted value. -/
theorem equal_corrections_give_gap {scale lower upper nextLower nextUpper corr : ℕ}
    (hl : scale * nextLower = 3 * lower + corr)
    (hu : scale * nextUpper = 3 * upper + corr) :
    scale * (nextUpper - nextLower) = 3 * (upper - lower) := by
  rw [Nat.mul_sub, hu, hl, Nat.add_sub_add_right, Nat.mul_sub]

/-- Iterating the doubling convention for the increasing lifted rank list. -/
theorem lift_octaves {p : ℕ} (z : ℕ → ℕ)
    (lift : ∀ i, z (i + p) = 2 * z i) (i a : ℕ) :
    z (i + p * a) = 2 ^ a * z i := by
  induction a with
  | zero => simp
  | succ a ih =>
    rw [Nat.mul_succ, ← Nat.add_assoc, lift, ih, pow_succ', Nat.mul_assoc]

/-- Changes are measured in sorted rank, with the doubled endpoint at index p. -/
def changes (p : ℕ) (corr : ℕ → ℕ) : Finset (Fin p) :=
  Finset.univ.filter fun i => corr (i.val + 1) ≠ corr i.val

/-- The ordered odd-cycle recurrence itself yields the complete scale bound.
There is no assumption on its gap differences. -/
theorem ordered_lap_budget {p h : ℕ} (z corr : ℕ → ℕ) (next : Equiv.Perm (Fin p))
    (shift : ∀ i : Fin p, (next i).val = (i.val + h) % p)
    (lift : ∀ i, z (i + p) = 2 * z i)
    (inc : StrictMono z)
    (affine : ∀ i ≤ p, z (i + h) = 3 * z i + corr i)
    (k : ℕ) :
    (p - k * (changes p corr).card) * 3 ^ k ≤ z 0 := by
  let gap (i : Fin p) := z (i.val + 1) - z i.val
  let clocks (i : Fin p) := (i.val + h) / p
  have edge (i : Fin p) (hi : i ∉ changes p corr) :
      2 ^ clocks i * gap (next i) = 3 * gap i := by
    have same : corr (i.val + 1) = corr i.val := by simpa [changes] using hi
    have decomp : (next i).val + p * clocks i = i.val + h := by
      rw [shift]
      exact Nat.mod_add_div _ _
    have hl := lift_octaves z lift (next i).val (clocks i)
    have hu := lift_octaves z lift ((next i).val + 1) (clocks i)
    rw [decomp, affine _ (Nat.le_of_lt i.isLt)] at hl
    have du : (next i).val + 1 + p * clocks i = i.val + 1 + h := by omega
    rw [du, affine _ i.isLt, same] at hu
    exact equal_corrections_give_gap hl.symm hu.symm
  have budget := rank_gap_budget next (changes p corr) gap clocks
    (fun i => Nat.sub_pos_of_lt (inc (Nat.lt_succ_self _))) edge k
  have width : (∑ i, gap i) = z 0 := by
    dsimp [gap]
    rw [Fin.sum_univ_eq_sum_range (fun v => z (v + 1) - z v),
      Finset.sum_range_tsub inc.monotone]
    have hw := lift 0
    simp at hw
    omega
  simpa [width] using budget

#print axioms markedPast_card
#print axioms cleanPast_dvd
#print axioms rank_gap_budget
#print axioms equal_corrections_give_gap
#print axioms lift_octaves
#print axioms ordered_lap_budget

end CollatzRankGaps
