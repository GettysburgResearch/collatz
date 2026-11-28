import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.Ring

/-! Recover odd physical numerators from an integral semimodule quotient. -/

namespace Collatz.BalancedCarry

private theorem power_dvd (a b : ℕ) (h : a ≤ b) : 2^a ∣ 2^b := by
  exact pow_dvd_pow 2 h

/-- A positive difference of levels makes every cyclic quotient coefficient
divisible by its full prescribed binary level. Finite order is subsumed by
surjectivity; the precision induction is uniform across the index set. -/
theorem all_levels_dvd {I : Type*} {next : I → I} (onto : Function.Surjective next)
    (L d k : I → ℕ) (hd : ∀ i, 0 < d i)
    (legal : ∀ i, L (next i) < L i+d i)
    (carry : ∀ i, 2^(d i)*k i = 3*k (next i)+2^(L (next i))) :
    ∀ i, 2^(L i) ∣ k i := by
  have precision : ∀ t i, 2^(min t (L i)) ∣ k i := by
    intro t
    induction t with
    | zero => simp
    | succ t ih =>
      intro j
      obtain ⟨i,rfl⟩ := onto j
      let m := min (t+1) (L (next i))
      have hm : m ≤ d i + min t (L i) := by
        dsimp [m]
        have h := hd i
        have hl := legal i
        omega
      obtain ⟨w,hw⟩ := ih i
      have left : 2^m ∣ 2^(d i)*k i := by
        rw [hw, ← Nat.mul_assoc, ← pow_add]
        exact dvd_mul_of_dvd_left (power_dvd _ _ hm) _
      have right : 2^m ∣ 2^(L (next i)) := power_dvd _ _ (min_le_right _ _)
      rw [carry i] at left
      have multiple : 2^m ∣ 3*k (next i) := (Nat.dvd_add_right right).mp (by
        simpa [Nat.add_comm] using left)
      have cop : (2^m).Coprime 3 := (by decide : Nat.Coprime 2 3).pow_left m
      exact cop.dvd_of_dvd_mul_left multiple
  intro i
  simpa using precision (L i) i

/-- The signed coefficient quotient produces the actual odd-to-odd equation
in the reverse order of the residue rotation, with positive division gaps. -/
theorem physical_numerators {I : Type*} {next : I → I} (onto : Function.Surjective next)
    (L d k : I → ℕ) (hd : ∀ i, 0 < d i)
    (legal : ∀ i, L (next i) < L i+d i)
    (carry : ∀ i, 2^(d i)*k i = 3*k (next i)+2^(L (next i))) :
    ∃ y : I → ℕ, (∀ i, k i = 2^(L i)*y i) ∧
      (∀ i, 2^(d i+L i-L (next i))*y i = 3*y (next i)+1) ∧
      (∀ i, ¬ 2 ∣ y i) := by
  choose y hy using all_levels_dvd onto L d k hd legal carry
  have physical : ∀ i, 2^(d i+L i-L (next i))*y i = 3*y (next i)+1 := by
    intro i
    have h := carry i
    rw [hy i, hy (next i), ← Nat.mul_assoc, ← pow_add] at h
    have sumLevel : L (next i)+(d i+L i-L (next i)) = d i+L i := by
      have hl := legal i
      omega
    have scaled : 2^(L (next i))*(2^(d i+L i-L (next i))*y i) =
        2^(L (next i))*(3*y (next i)+1) := by
      rw [← Nat.mul_assoc, ← pow_add, sumLevel, h]
      ring
    exact Nat.eq_of_mul_eq_mul_left (pow_pos (by decide : 0 < (2 : ℕ)) _) scaled
  refine ⟨y,hy,physical,?_⟩
  intro j
  obtain ⟨i,rfl⟩ := onto j
  have H := physical i
  have e : d i+L i-L (next i) = (d i+L i-L (next i)-1)+1 := by
    have hl := legal i
    omega
  rw [e, pow_succ] at H
  intro even
  obtain ⟨q,hq⟩ := even
  rw [hq] at H
  have H' : 2*(2^(d i+L i-L (next i)-1)*y i) = 3*(2*q)+1 := by
    rw [← H]
    ring
  omega

/-- Height at most one converts the quotient recurrence into a uniquely
specified floor step and a nonzero remainder. -/
theorem binary_level_floor {d k k' l : ℕ} (hl : l ≤ 1)
    (eqn : 2^d*k = 3*k'+2^l) : 2^d*k / 3 = k' ∧ 2^d*k % 3 = 2^l := by
  have cases : l = 0 ∨ l = 1 := by omega
  rcases cases with rfl | rfl <;> simp at eqn ⊢ <;> omega

end Collatz.BalancedCarry
