import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.Sum
import Mathlib.Data.Fintype.Sigma
import Mathlib.Data.Fintype.Prod

/-! Finite bucket shortening with unequal coordinate alphabets. -/

namespace Collatz.MixedAlphabet

/-- Additive Sidon uniqueness makes every ordered nonzero difference unique. -/
theorem distinct_differences {C G : Type*} [AddCommGroup G] (v : C → G)
    (sidon : ∀ a b c d, v a + v b = v c + v d →
      (a = c ∧ b = d) ∨ (a = d ∧ b = c))
    {a b c d : C} (hab : a ≠ b) (h : v a - v b = v c - v d) :
    a = c ∧ b = d := by
  have m : v a + v d = v c + v b := sub_eq_sub_iff_add_eq_add.mp h
  rcases sidon a d c b m with h' | h'
  · exact ⟨h'.1,h'.2.symm⟩
  · exact (hab h'.1).elim

/-- Each element of a finite code lies in one bucket box. A suffix fingerprint
distinguishes the ordered distinct pairs in equal boxes. -/
theorem finite_shortening {P C D : Type*} [Fintype P] [Fintype C] [Fintype D]
    [DecidableEq P] (bucket : C → P) (signature : C → C → D)
    (unique : ∀ a b c d, a ≠ b → c ≠ d → bucket a = bucket b →
      bucket c = bucket d → signature a b = signature c d → a = c ∧ b = d) :
    Fintype.card C ^ 2 ≤ Fintype.card P * (Fintype.card C + Fintype.card D) := by
  classical
  let F := fun p => {x : C // bucket x = p}
  let T := (p : P) × (F p × F p)
  let enc : T → C ⊕ D := fun ⟨_,x,y⟩ =>
    if x.1 = y.1 then Sum.inl x.1 else Sum.inr (signature x.1 y.1)
  have hi : Function.Injective enc := by
    rintro ⟨p,⟨⟨a,ha⟩,⟨b,hb⟩⟩⟩ ⟨q,⟨⟨c,hc⟩,⟨d,hd⟩⟩⟩ he
    dsimp [enc] at he
    split at he <;> rename_i hab <;> split at he <;> rename_i hcd
    · obtain rfl : a = c := Sum.inl.inj he
      subst b
      subst d
      subst p
      subst q
      rfl
    · contradiction
    · contradiction
    · obtain ⟨rfl,rfl⟩ := unique _ _ _ _ hab hcd (ha.trans hb.symm)
        (hc.trans hd.symm) (Sum.inr.inj he)
      subst p
      subst q
      rfl
  have represented : (∑ p, Fintype.card (F p)) = Fintype.card C := by
    rw [← Fintype.card_sigma]
    exact Fintype.card_congr (Equiv.sigmaFiberEquiv bucket)
  have encoded : (∑ p, Fintype.card (F p)^2) ≤ Fintype.card C + Fintype.card D := by
    have h := Fintype.card_le_of_injective enc hi
    simpa [T, Fintype.card_sigma, Fintype.card_prod, pow_two] using h
  have cs := Finset.sum_mul_sq_le_sq_mul_sq (R := ℕ) (Finset.univ : Finset P)
    (fun _ => 1) (fun p => Fintype.card (F p))
  simp only [one_mul, one_pow, Finset.sum_const, Finset.card_univ, Nat.nsmul_eq_mul, mul_one] at cs
  rw [represented] at cs
  exact cs.trans <| Nat.mul_le_mul_left _ encoded

/-- A one-division folded date cannot drop the binary logarithmic tag. -/
theorem one_step_forbids_drop {x x' e : ℕ} (hx : 0 < x') (he : 0 < e)
    (physical : 2^e*x' = 3*x+1) (folded : 2*x' = 3*(2*x)+2) : False := by
  have h : 2*x' = 2*(2^e*x') := by omega
  have lower : 2 ≤ 2^e := by
    obtain ⟨k,rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt he)
    rw [pow_succ]
    have := Nat.two_pow_pos k
    omega
  have bound := Nat.mul_le_mul_right x' lower
  omega

end Collatz.MixedAlphabet
