import Mathlib.Data.Finset.Prod
import Mathlib.Data.Nat.ModEq

/-! Finite ordinary-source separation and packing for canonical phase windows. -/

namespace Collatz.CanonicalWindows

open Finset
open scoped Finset

noncomputable local instance (m : ℕ) : DecidableEq (Fin m → ℕ) := Classical.decEq _

/-- Two equal ordinary gap words determine equal terminal ternary residues. -/
theorem same_past_residue (q a : ℕ → ℕ)
    (edge : ∀ i, 2 ^ a i * q (i+1) = 3 * q i + 1)
    (i j m : ℕ) (same : ∀ k < m, a (i+k) = a (j+k)) :
    q (i+m) ≡ q (j+m) [MOD 3^m] := by
  induction m with
  | zero => simp only [Nat.ModEq, Nat.pow_zero, Nat.mod_one]
  | succ m ih =>
    have prev := ih (fun k hk => same k (by omega))
    have prod := (prev.mul_left' 3).add_right 1
    rw [← edge (i+m), ← edge (j+m), ← same m (by omega)] at prod
    have cop : Nat.Coprime (3^(m+1)) (2^a (i+m)) :=
      (show Nat.Coprime 3 2 by decide).pow _ _
    apply Nat.ModEq.cancel_left_of_coprime cop
    simpa only [Nat.pow_succ, Nat.mul_comm 3, Nat.add_assoc] using prod

/-- The positive-carry vertices contaminate at most m+1 starts each.
All remaining canonical words at these actual endpoints are distinct. -/
theorem canonical_window_count (q a b c : ℕ → ℕ) (N m : ℕ) (hm : m ≤ N)
    (edge : ∀ i, 2 ^ a i * q (i+1) = 3 * q i + 1)
    (clock : ∀ i, a i + c (i+1) = b i + 3*c i)
    (distinct : ∀ i ≤ N, ∀ j ≤ N, q i = q j → i = j)
    (height : ∀ i ≤ N, q i < 3^m) :
    N-m+1 ≤
      (((range (N-m+1)).image (fun i (k : Fin m) => b (i+k.val))).card) +
      (((range (N+1)).filter (fun i => 0 < c i)).card) * (m+1) := by
  classical
  let starts := range (N-m+1)
  let paid := (range (N+1)).filter (fun i => 0 < c i)
  let bad := (paid ×ˢ range (m+1)).image (fun t => t.1-t.2)
  let good := starts \ bad
  let word := fun i (k : Fin m) => b (i+k.val)
  have good_carry (i : ℕ) (hi : i ∈ good) (k : ℕ) (hk : k ≤ m) :
      c (i+k) = 0 := by
    obtain ⟨hist, hib⟩ := mem_sdiff.mp hi
    have hit : i < N-m+1 := mem_range.mp hist
    by_contra hn
    have hp : i+k ∈ paid :=
      mem_filter.mpr ⟨mem_range.mpr (by omega), by omega⟩
    have hprod : (i+k,k) ∈ paid ×ˢ range (m+1) :=
      mem_product.mpr ⟨hp, mem_range.mpr (by omega)⟩
    exact hib (mem_image.mpr ⟨(i+k,k), hprod, by simp⟩)
  have good_gap (i : ℕ) (hi : i ∈ good) (k : ℕ) (hk : k < m) :
      a (i+k) = b (i+k) := by
    have h1 := good_carry i hi k (by omega)
    have h2 := good_carry i hi (k+1) (by omega)
    have h := clock (i+k)
    simpa [Nat.add_assoc,h1,h2] using h
  have inject : Set.InjOn word (↑good) := by
    intro i hi j hj heq
    have hiN : i+m ≤ N := by
      have h : i < N-m+1 := mem_range.mp (mem_sdiff.mp hi).1
      omega
    have hjN : j+m ≤ N := by
      have h : j < N-m+1 := mem_range.mp (mem_sdiff.mp hj).1
      omega
    have hs := same_past_residue q a edge i j m (by
      intro k hk
      rw [good_gap i hi k hk,good_gap j hj k hk]
      exact congrFun heq ⟨k,hk⟩)
    have vals : q (i+m) = q (j+m) := by
      simpa [Nat.ModEq, Nat.mod_eq_of_lt (height _ hiN),
        Nat.mod_eq_of_lt (height _ hjN)] using hs
    have := distinct _ hiN _ hjN vals
    omega
  have hsub : starts ⊆ good ∪ bad := by
    intro i hi
    by_cases h : i ∈ bad
    · exact mem_union_right _ h
    · exact mem_union_left _ (mem_sdiff.mpr ⟨hi,h⟩)
  have hg : good.card ≤ (starts.image word).card := by
    rw [← card_image_iff.mpr inject]
    exact card_le_card (image_mono word sdiff_subset)
  have hb : bad.card ≤ paid.card * (m+1) := by
    exact (card_image_le).trans (by simp [card_product])
  have htotal := (card_le_card hsub).trans (card_union_le good bad)
  change N-m+1 ≤ (starts.image word).card + paid.card*(m+1)
  have hs : starts.card = N-m+1 := card_range _
  omega

#print axioms same_past_residue
#print axioms canonical_window_count

end Collatz.CanonicalWindows
