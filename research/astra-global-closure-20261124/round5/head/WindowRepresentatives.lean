import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Finset.Lattice.Fold
import Mathlib.Data.Finset.Max
import Mathlib.Tactic.Linarith

/-! Finite kernels for a prefix-dependent list of rightmost representatives.
Equality of the prefix profiles must persist for the continuation being counted. -/

namespace Collatz.HeadWindows

open scoped BigOperators

variable {n : ℕ} {α β : Type*}

/-- The rightmost index of each nonempty prefix class. -/
noncomputable def representatives (c : Fin n → α) : Finset (Fin n) := by
  classical
  exact Finset.univ.filter (fun i => ∀ j, i < j → c i ≠ c j)

/-- The last representative belongs to the original index's class. -/
theorem last_in_class (c : Fin n → α) (i : Fin n) :
    ∃ j ∈ representatives c, c j = c i := by
  classical
  let members := Finset.univ.filter (fun j => c j = c i)
  have hi : i ∈ members := by simp [members]
  have nonempty : members.Nonempty := ⟨i, hi⟩
  let j := members.max' nonempty
  have hj : j ∈ members := Finset.max'_mem members nonempty
  have same : c j = c i := (Finset.mem_filter.mp hj).2
  refine ⟨j, ?_, same⟩
  simp only [representatives, Finset.mem_filter, Finset.mem_univ, true_and]
  intro k hlt heq
  have hk : k ∈ members := Finset.mem_filter.mpr ⟨Finset.mem_univ _, heq.symm.trans same⟩
  exact (not_le_of_gt hlt) (Finset.le_max' members k hk)

/-- Two different representatives have different prefix profiles. -/
theorem separate_representatives (c : Fin n → α) {i j : Fin n}
    (hi : i ∈ representatives c) (hj : j ∈ representatives c) (hne : i ≠ j) :
    c i ≠ c j := by
  classical
  simp only [representatives, Finset.mem_filter, Finset.mem_univ, true_and] at hi hj
  rcases lt_or_gt_of_ne hne with h | h
  · exact hi j h
  · exact fun heq => hj i h heq.symm

/-- Any third eventual label is already carried by a prefix representative. -/
theorem third_on_representative (c : Fin n → α) (label : Fin n → β) (a b : β)
    (persists : ∀ i j, c i = c j → label i = label j)
    (third : ∃ i, label i ≠ a ∧ label i ≠ b) :
    ∃ j ∈ representatives c, label j ≠ a ∧ label j ≠ b := by
  obtain ⟨i, hia, hib⟩ := third
  obtain ⟨j, hj, hji⟩ := last_in_class c i
  exact ⟨j, hj, fun h => hia ((persists j i hji).symm.trans h),
    fun h => hib ((persists j i hji).symm.trans h)⟩

/-- The number of suffixes charged to a prefix-dependent finite family.
The bound on each test is required on that same prefix. -/
theorem prefix_cover {P I S : Type*} [DecidableEq S] (prefixes : Finset P)
    (reps : P → Finset I) (bad : P → Finset S) (tests : P → I → Finset S) (bound : ℕ)
    (covered : ∀ p ∈ prefixes, ∀ s ∈ bad p, ∃ i ∈ reps p, s ∈ tests p i)
    (per_test : ∀ p ∈ prefixes, ∀ i ∈ reps p, (tests p i).card ≤ bound) :
    (∑ p ∈ prefixes, (bad p).card) ≤ (∑ p ∈ prefixes, (reps p).card) * bound := by
  classical
  rw [Finset.sum_mul]
  apply Finset.sum_le_sum
  intro p hp
  have incl : bad p ⊆ (reps p).biUnion (tests p) :=
    fun s hs => Finset.mem_biUnion.mpr (covered p hp s hs)
  calc
    (bad p).card ≤ ((reps p).biUnion (tests p)).card := Finset.card_le_card incl
    _ ≤ ∑ i ∈ reps p, (tests p i).card := Finset.card_biUnion_le
    _ ≤ ∑ _i ∈ reps p, bound := Finset.sum_le_sum (fun i hi => per_test p hp i hi)
    _ = (reps p).card * bound := by simp

/-- A concrete subcritical moment giving a summable error for every b < 1/12. -/
theorem head_exponent (b : ℚ) (hb : 0 ≤ b) (h : b < 1/12) :
    ∃ p : ℚ, 1 < p ∧ p < 3/2 ∧ 1 < p - b * (3 + 2*p) := by
  refine ⟨5/4+3*b, by linarith, by linarith, ?_⟩
  have prod := mul_pos (show 0 < 1-12*b by linarith) (show 0 < 1/4+b/2 by linarith)
  nlinarith

#print axioms last_in_class
#print axioms separate_representatives
#print axioms third_on_representative
#print axioms prefix_cover
#print axioms head_exponent

end Collatz.HeadWindows
