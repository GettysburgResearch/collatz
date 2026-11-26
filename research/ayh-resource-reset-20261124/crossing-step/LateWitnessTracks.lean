import Mathlib

/-! Disjoint binary blocks in a late projected coordinate.  All tests use
the same ordinary base parameter.  The analytical merger probabilities
and the physical source estimates are not formalized here. -/

namespace Collatz.LateWitnessTracks

/-- After fixing the low bits of the projected base, the whole child has
a fixed suffix modulo 81 and its parent has an odd-affine free parameter. -/
theorem projected_head_block (e delta low b q : ℕ) :
    let z := 3 ^ (e+4) * (low + 2 ^ delta * q) / 2 ^ delta + b
    let c := 3 ^ (e+4) * low / 2 ^ delta + b
    z % 81 = c % 81 ∧ z / 81 = 3 ^ e * q + c / 81 := by
  dsimp only
  have hpos : 0 < (2 : ℕ)^delta := by positivity
  have h : 3^(e+4) * (low + 2^delta * q) =
      3^(e+4)*low + (81*(3^e*q)) * 2^delta := by
    rw [pow_add]
    ring
  rw [h, Nat.add_mul_div_right _ _ hpos]
  have hr : 3^(e+4)*low / 2^delta + 81*(3^e*q) + b =
      (3^(e+4)*low / 2^delta + b) + (3^e*q) * 81 := by ring
  rw [hr, Nat.add_mul_mod_self_right, Nat.add_mul_div_right _ _ (by decide : 0 < 81)]
  exact ⟨rfl, Nat.add_comm _ _⟩

/-- An arbitrary fresh dyadic block stays uniform after taking the parent.
This identifies the precise finite permutation used by the multitime proof. -/
theorem parent_residue_bijective (e h c : ℕ) :
    Function.Bijective (fun q : Fin (2^h) =>
      (⟨(3^e * q.val + c) % (2^h), Nat.mod_lt _ (by positivity)⟩ : Fin (2^h))) := by
  apply Finite.injective_iff_bijective.mp
  intro x y he
  have hm : 3^e*x.val+c ≡ 3^e*y.val+c [MOD 2^h] := congrArg Fin.val he
  have hc : 3^e*x.val ≡ 3^e*y.val [MOD 2^h] := Nat.ModEq.add_right_cancel' c hm
  have hcop : Nat.Coprime (2^h) (3^e) :=
    ((by decide : Nat.Coprime 2 3).pow_left h).pow_right e
  have hf := hc.cancel_left_of_coprime hcop
  apply Fin.ext
  simpa [Nat.ModEq, Nat.mod_eq_of_lt x.isLt, Nat.mod_eq_of_lt y.isLt] using hf

/-- A low-block-dependent bad list has exactly its prescribed number of
terms on each complete fresh block, uniformly in the affine translation. -/
theorem parent_test_card (e h c : ℕ) (S : Finset (Fin (2^h))) :
    (Finset.univ.filter fun q : Fin (2^h) =>
      (⟨(3^e*q.val+c) % 2^h, Nat.mod_lt _ (by positivity)⟩ : Fin (2^h)) ∈ S).card =
    S.card := by
  classical
  let p : Fin (2^h) ≃ Fin (2^h) :=
    Equiv.ofBijective _ (parent_residue_bijective e h c)
  change (Finset.univ.filter fun q => p q ∈ S).card = S.card
  have hi : (Finset.univ.filter fun q => p q ∈ S).map p.toEmbedding = S := by
    ext y
    simp
  exact (Finset.card_map p.toEmbedding).symm.trans (congrArg Finset.card hi)

end Collatz.LateWitnessTracks

#print axioms Collatz.LateWitnessTracks.projected_head_block
#print axioms Collatz.LateWitnessTracks.parent_residue_bijective
#print axioms Collatz.LateWitnessTracks.parent_test_card
