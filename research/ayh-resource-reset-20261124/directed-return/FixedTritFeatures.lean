import Mathlib.Data.Finset.Card

/-! The finite inventory step for the block-transversal selection proof. -/

namespace Collatz.FixedTritFeatures

/-- The old shattered sets and the common sets augmented by the current
block's feature give disjoint inventories. -/
theorem split_inventory {α : Type*} [DecidableEq α] (x : α)
    (a b : Finset (Finset α)) (fresh : ∀ s ∈ a ∪ b, x ∉ s) :
    ((a ∪ b) ∪ ((a ∩ b).image (insert x))).card = a.card + b.card := by
  have hd : Disjoint (a ∪ b) ((a ∩ b).image (insert x)) := by
    rw [Finset.disjoint_left]
    intro s hs hi
    obtain ⟨v, _, rfl⟩ := Finset.mem_image.mp hi
    exact fresh (insert x v) hs (Finset.mem_insert_self _ _)
  have hi : Set.InjOn (insert x) (↑(a ∩ b) : Set (Finset α)) := by
    intro s hs t ht heq
    have hsf : x ∉ s := fresh s (Finset.mem_union_left _ (Finset.mem_inter.mp hs).1)
    have htf : x ∉ t := fresh t (Finset.mem_union_left _ (Finset.mem_inter.mp ht).1)
    simpa [hsf,htf] using congrArg (fun v : Finset α => v.erase x) heq
  rw [Finset.card_union_of_disjoint hd, Finset.card_image_of_injOn hi,
    Finset.card_union_add_card_inter]

end Collatz.FixedTritFeatures

#print axioms Collatz.FixedTritFeatures.split_inventory
