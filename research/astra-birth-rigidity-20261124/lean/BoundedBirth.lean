import Std

/-! One-step finite row estimates for counting natural carries at x = 1/3.
The potential at cutoff H is scaled by 3^H so every term is a natural number. -/
namespace Collatz.BoundedBirth

theorem zero_carry_bound {g b cNext : Nat} (hg : 1 ≤ g)
    (edge : g + cNext = b + 3 * 0) : cNext ≤ b - 1 := by omega

/-- Sum of the scaled weights of the possible next carries 0,...,m. -/
def rowMass (H : Nat) : Nat → Nat
  | 0 => 3^H
  | m + 1 => rowMass H m + 2 * 3^(H - (m+1))

theorem row_exact (H m : Nat) (hm : m ≤ H) :
    rowMass H m + 3^(H - m) = 2 * 3^H := by
  induction m with
  | zero => simp [rowMass]; omega
  | succ m ih =>
    have hp := ih (by omega)
    have he : H - m = (H - (m+1)) + 1 := by omega
    rw [he, Nat.pow_succ] at hp
    simp only [rowMass]
    omega

theorem row_le (H m : Nat) (hm : m ≤ H) : rowMass H m ≤ 2 * 3^H :=
  calc
    rowMass H m ≤ rowMass H m + 3^(H-m) := Nat.le_add_right _ _
    _ = 2 * 3^H := row_exact H m hm

def potential (H c : Nat) : Nat :=
  if c = 0 then 3^H else 2 * 3^(H-c)

/-- For a positive carry c, every next carry up to H may be included.
Multiplication by 3^c clears the current edge weight 1/3^c. -/
theorem positive_row (H c : Nat) (hc : 0 < c) (hcH : c ≤ H) :
    rowMass H H ≤ 3^c * potential H c := by
  simp only [potential, Nat.ne_of_gt hc, ite_false]
  have hp : 3^c * 3^(H-c) = 3^H := by
    rw [← Nat.pow_add, show c + (H-c) = H by omega]
  rw [Nat.mul_left_comm (3^c) 2, hp]
  exact row_le H H (Nat.le_refl H)

/-- At zero carry include every possible next carry up to m ≤ b-1.
The multiplier is (5/3)^(b-1), cleared of its denominator. -/
theorem birth_row (H b m : Nat) (hb : 1 ≤ b) (hb3 : b ≤ 3)
    (hm : m ≤ H) (hmb : m ≤ b-1) :
    3^(b-1) * rowMass H m ≤ 5^(b-1) * 3^H := by
  have hcases : b = 1 ∨ b = 2 ∨ b = 3 := by omega
  rcases hcases with h | h | h
  · subst b
    have hm0 : m = 0 := by omega
    simp [hm0, rowMass]
  · subst b
    have hcases : m = 0 ∨ m = 1 := by omega
    rcases hcases with h | h
    · subst m
      change 3 * 3^H ≤ 5 * 3^H
      omega
    · subst m
      have hp : 3^H = 3^(H-1)*3 := by
        conv => lhs; rw [show H = (H-1)+1 by omega, Nat.pow_succ]
      change 3 * (3^H + 2 * 3^(H-1)) ≤ 5 * 3^H
      omega
  · subst b
    change 9 * rowMass H m ≤ 25 * 3^H
    calc
      9 * rowMass H m ≤ 9 * (2 * 3^H) := Nat.mul_le_mul_left 9 (row_le H m hm)
      _ = (9 * 2) * 3^H := (Nat.mul_assoc _ _ _).symm
      _ ≤ 25 * 3^H := Nat.mul_le_mul_right _ (by decide : 9 * 2 ≤ 25)

end Collatz.BoundedBirth

#print axioms Collatz.BoundedBirth.potential
#print axioms Collatz.BoundedBirth.rowMass
#print axioms Collatz.BoundedBirth.zero_carry_bound
#print axioms Collatz.BoundedBirth.row_exact
#print axioms Collatz.BoundedBirth.row_le
#print axioms Collatz.BoundedBirth.positive_row
#print axioms Collatz.BoundedBirth.birth_row
