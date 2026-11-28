import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Nat.Cast.Order.Ring
import Mathlib.Tactic.NormNum

/-! Positive monomial lifts in the full formal period lattice. -/

namespace Collatz.PositiveLift

/-- Chronological numerator with the odd departures listed by their time in the lap. -/
def numerator {u : ℕ} (p : Fin u → ℕ) : ℕ :=
  ∑ j, 2 ^ p j * 3 ^ (u - 1 - j.val)

/-- All representatives have the same translate in the formal full period lattice.
The first exponents are aligned at the physical cut obtained from that translate. -/
def Aligned {n u : ℕ} (p A B : Fin u → ℕ) : Prop :=
  ∃ b : ℤ, ∀ j, ∃ q : ℤ,
    (A j : ℤ) = p j + n*q ∧ (B j : ℤ) = b - j.val - u*q

private theorem nonnegative_quotient {n p A : ℕ} {q : ℤ}
    (hp : p < n) (h : (A : ℤ) = p+n*q) : 0 ≤ q := by
  by_contra hneg
  have hq : q ≤ -1 := by omega
  have hle := mul_le_mul_of_nonneg_left hq (show (0 : ℤ) ≤ n by exact_mod_cast Nat.zero_le n)
  have hp' : (p : ℤ) < n := by exact_mod_cast hp
  simp only [mul_neg, mul_one] at hle
  omega

/-- Trading a complete nonnegative lap of twos for threes can only decrease its weight. -/
theorem reduce_weight {n u p q B : ℕ} (hc : 3^u ≤ 2^n) :
    2^p * 3^(B+u*q) ≤ 2^(p+n*q) * 3^B := by
  have hq : (3^u)^q ≤ (2^n)^q := Nat.pow_le_pow_left hc q
  rw [pow_add, pow_mul, pow_add, pow_mul]
  calc
    2^p * (3^B * (3^u)^q) ≤ 2^p * (3^B * (2^n)^q) := by gcongr
    _ = 2^p * (2^n)^q * 3^B := by ac_rfl

/-- The numerical value of every aligned formal lift dominates the physical cut numerator. -/
theorem numerator_le_lift {n u : ℕ} (hu : 0 < u) (hc : 3^u ≤ 2^n)
    (p A B : Fin u → ℕ) (hp : ∀ j, p j < n) (h : Aligned (n:=n) p A B) :
    numerator p ≤ ∑ j, 2^A j * 3^B j := by
  obtain ⟨b, hb⟩ := h
  let last : Fin u := ⟨u-1, by omega⟩
  obtain ⟨ql, hal, hbl⟩ := hb last
  have hql := nonnegative_quotient (hp last) hal
  have hun : (0 : ℤ) ≤ u := by exact_mod_cast Nat.zero_le u
  have hql' := mul_nonneg hun hql
  have hlast : (last.val : ℤ) = (u:ℤ)-1 := by dsimp [last]; omega
  have hbase : (u:ℤ)-1 ≤ b := by omega
  apply Finset.sum_le_sum
  intro j _
  obtain ⟨q, ha, hb'⟩ := hb j
  have hq := nonnegative_quotient (hp j) ha
  have qcast : (q.toNat : ℤ) = q := Int.toNat_of_nonneg hq
  have haZ : (A j : ℤ) = (p j : ℤ) + (n:ℤ)*(q.toNat:ℤ) := by rw [qcast]; exact ha
  have ha' : A j = p j+n*q.toNat := by exact_mod_cast haZ
  have hs : u - 1 - j.val ≤ B j + u*q.toNat := by
    have hj := j.isLt
    have hs' : ((u - 1 - j.val : ℕ) : ℤ) ≤ (B j : ℤ) + (u:ℤ)*q := by omega
    exact_mod_cast (show ((u - 1 - j.val : ℕ) : ℤ) ≤ (B j : ℤ) + (u:ℤ)*(q.toNat:ℤ) by
      rw [qcast]; exact hs')
  rw [ha']
  exact (Nat.mul_le_mul_left _ (Nat.pow_le_pow_right (by decide : 0 < 3) hs)).trans
    (reduce_weight hc)

/-- The numerator is attained by the canonical representatives at this cut. -/
theorem canonical_aligned {n u : ℕ} (p : Fin u → ℕ) :
    Aligned (n:=n) p p (fun j => u-1-j.val) := by
  refine ⟨(u:ℤ)-1, ?_⟩
  intro j
  refine ⟨0, by simp, ?_⟩
  have hj := j.isLt
  simp only [mul_zero, sub_zero]
  omega

/-- The local minimization over arbitrary representatives at the induced cut is exact. -/
theorem numerator_is_least {n u : ℕ} (hu : 0 < u) (hc : 3^u ≤ 2^n)
    (p : Fin u → ℕ) (hp : ∀ j, p j < n) :
    IsLeast {z : ℕ | ∃ A B : Fin u → ℕ, Aligned (n:=n) p A B ∧
      z = ∑ j, 2^A j * 3^B j} (numerator p) := by
  constructor
  · exact ⟨p, fun j => u-1-j.val, canonical_aligned p, rfl⟩
  · rintro z ⟨A,B,h,rfl⟩
    exact numerator_le_lift hu hc p A B hp h

end Collatz.PositiveLift
