import OAI.LinearAlgebra.SpectralBooks.BlockDiagRank
import Mathlib.Data.Finset.Card

/-! Rank detects when finite batches of ordinary trajectories meet.
Rows retain the full source and clock. Columns retain each actual endpoint
once. Tags on the columns of independent batches can then be forgotten. -/

namespace Collatz.TensorBridge

open OAI.LinearAlgebra.SpectralBooks

variable {I J : Type*} [Fintype I] [Fintype J]

def attained (f : I → Nat) : Finset Nat := Finset.univ.image f

@[simp] theorem mem_attained (f : I → Nat) (y : Nat) :
    y ∈ attained f ↔ ∃ i, f i = y := by simp [attained]

def incidence (F : Type*) [Field F] (f : I → Nat) : Matrix I (attained f) F :=
  fun i y => if f i = y.val then 1 else 0

theorem incidence_rank (F : Type*) [Field F] (f : I → Nat) :
    (incidence F f).rank = (attained f).card := by
  classical
  have repr (y : attained f) : ∃ i, f i = y.val := (mem_attained f y).mp y.property
  let row (y : attained f) := Classical.choose (repr y)
  have hrow (y : attained f) : f (row y) = y.val := Classical.choose_spec (repr y)
  have minor : (incidence F f).submatrix row id = 1 := by
    ext a b
    change (if f (row a) = b.val then (1 : F) else 0) = _
    rw [hrow, Matrix.one_apply]
    by_cases hab : a = b
    · subst b
      simp
    · have hv : a.val ≠ b.val := fun h => hab (Subtype.ext h)
      simp [hab, hv]
  apply le_antisymm
  · simpa using (incidence F f).rank_le_card_width
  · have h := Matrix.rank_submatrix_le (incidence F f) row id
    simpa [minor, Matrix.rank_one] using h

theorem attained_sum (f : I → Nat) (g : J → Nat) :
    attained (Sum.elim f g) = attained f ∪ attained g := by
  ext y
  simp only [mem_attained, Finset.mem_union]
  constructor
  · rintro ⟨i | j, h⟩
    · exact Or.inl ⟨i, h⟩
    · exact Or.inr ⟨j, h⟩
  · rintro (⟨i, h⟩ | ⟨j, h⟩)
    · exact ⟨Sum.inl i, h⟩
    · exact ⟨Sum.inr j, h⟩

noncomputable def taggedRank (F : Type*) [Field F] (f : I → Nat) (g : J → Nat) : Nat :=
  (Matrix.fromBlocks (incidence F f) 0 0 (incidence F g)).rank

/-- The independent block theorem, after identifying equal ordinary endpoints.
The exact rank loss is the number of distinct meetings, counting each
endpoint once even if several source-clock pairs witness it. -/
theorem rank_balance (F : Type*) [Field F] (f : I → Nat) (g : J → Nat) :
    (incidence F (Sum.elim f g)).rank + (attained f ∩ attained g).card =
      taggedRank F f g := by
  rw [taggedRank, rank_fromBlocks_diagonal, incidence_rank, incidence_rank,
    incidence_rank, attained_sum]
  exact Finset.card_union_add_card_inter _ _

theorem rank_drop_iff_meeting (F : Type*) [Field F] (f : I → Nat) (g : J → Nat) :
    (incidence F (Sum.elim f g)).rank < taggedRank F f g ↔ ∃ i j, f i = g j := by
  have h := rank_balance F f g
  constructor
  · intro drop
    have hp : 0 < (attained f ∩ attained g).card := by omega
    obtain ⟨y, hy⟩ := Finset.card_pos.mp hp
    obtain ⟨hf, hg⟩ := Finset.mem_inter.mp hy
    obtain ⟨i, hi⟩ := (mem_attained f y).mp hf
    obtain ⟨j, hj⟩ := (mem_attained g y).mp hg
    exact ⟨i, j, hi.trans hj.symm⟩
  · rintro ⟨i, j, hij⟩
    have hp : 0 < (attained f ∩ attained g).card := Finset.card_pos.mpr
      ⟨f i, Finset.mem_inter.mpr ⟨(mem_attained _ _).mpr ⟨i, rfl⟩,
        (mem_attained _ _).mpr ⟨j, hij.symm⟩⟩⟩
    omega

/-- A batch can vary both its ordinary positive starting integer and its clock.
Specializing the endpoint test to any ordinary iteration yields an actual
meeting at the reported two clocks. -/
theorem orbit_rank_drop_iff_meeting (F : Type*) [Field F] (step : Nat → Nat)
    (left : I → Nat × Nat) (right : J → Nat × Nat) :
    let f := fun i => step^[(left i).2] (left i).1
    let g := fun j => step^[(right j).2] (right j).1
    (incidence F (Sum.elim f g)).rank < taggedRank F f g ↔
      ∃ i j, step^[(left i).2] (left i).1 = step^[(right j).2] (right j).1 :=
  rank_drop_iff_meeting F _ _

end Collatz.TensorBridge
