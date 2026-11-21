import Std

/-!
The exact arithmetic obstruction to pulling a multiplier backwards through
an affine Collatz word. For a word with p odd steps, take A = 3^p and B its
usual additive numerator. The separate word argument proves Coprime A B.
This file does not assume or assert that arbitrary wild-semigroup multipliers
preserve ordinary Collatz components.
-/

namespace WildLift

theorem correction_iff (A B m : Nat) (hm : 1 ≤ m)
    (hcop : Nat.Coprime A B) :
    (∃ c : Nat, A * c + B = m * B) ↔ A ∣ m - 1 := by
  have hm' : m - 1 + 1 = m := by omega
  constructor
  · rintro ⟨c, hc⟩
    have heq : A * c = (m - 1) * B := by
      have hexpand : m * B = (m - 1) * B + B := by
        calc
          m * B = (m - 1 + 1) * B := congrArg (fun x => x * B) hm'.symm
          _ = (m - 1) * B + B := by simp only [Nat.add_mul, Nat.one_mul]
      rw [hexpand] at hc
      omega
    exact hcop.dvd_of_dvd_mul_right ⟨c, heq.symm⟩
  · rintro ⟨k, hk⟩
    refine ⟨k * B, ?_⟩
    calc
      A * (k * B) + B = (A * k) * B + B := by rw [Nat.mul_assoc]
      _ = (m - 1) * B + B := by rw [← hk]
      _ = (m - 1 + 1) * B := by simp only [Nat.add_mul, Nat.one_mul]
      _ = m * B := by rw [hm']

theorem correction_unique (A B m c d : Nat) (hA : 0 < A)
    (hc : A * c + B = m * B) (hd : A * d + B = m * B) : c = d := by
  have hh : A * c = A * d := by omega
  exact Nat.eq_of_mul_eq_mul_left hA hh

theorem pullback_identity (A B m n c : Nat)
    (hc : A * c + B = m * B) :
    A * (m * n + c) + B = m * (A * n + B) := by
  calc
    A * (m * n + c) + B = A * (m * n) + (A * c + B) := by
      rw [Nat.mul_add, Nat.add_assoc]
    _ = A * (m * n) + m * B := by rw [hc]
    _ = m * (A * n + B) := by
      simp only [Nat.mul_add, Nat.mul_comm, Nat.mul_left_comm]

theorem pullback_congruence (A B D m n c y : Nat) (hm : 1 ≤ m)
    (hn : D * y = A * n + B) (hc : A * c + B = m * B)
    (hcop : Nat.Coprime A D) : D ∣ (m * n + c) - n := by
  have hge : n ≤ m * n + c := by
    have hmul := Nat.mul_le_mul_right n hm
    simp only [Nat.one_mul] at hmul
    omega
  have heq := pullback_identity A B m n c hc
  have hmul : A * ((m * n + c) - n) = (m - 1) * (D * y) := by
    rw [Nat.mul_sub_left_distrib, Nat.sub_mul, Nat.one_mul]
    have h0 : m * (A * n + B) = m * (D * y) := by rw [← hn]
    omega
  have hdiv : D ∣ A * ((m * n + c) - n) := by
    rw [hmul]
    exact Nat.dvd_mul_left_of_dvd (Nat.dvd_mul_right D y) (m - 1)
  exact hcop.symm.dvd_of_dvd_mul_left hdiv

theorem thirteen_after_one_odd (n : Nat) :
    3 * (13 * n + 4) + 1 = 13 * (3 * n + 1) := by omega

theorem thirteen_after_two_odds_impossible :
    ¬ ∃ c : Nat, 9 * c + 5 = 13 * 5 := by omega

#print axioms correction_iff
#print axioms pullback_identity
#print axioms pullback_congruence
#print axioms thirteen_after_two_odds_impossible

end WildLift
