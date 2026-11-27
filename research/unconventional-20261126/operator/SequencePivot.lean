module

public import Mathlib.Algebra.Group.Basic
public import Mathlib.Data.Nat.Basic
public import Mathlib.Tactic.Abel
public import Mathlib.Tactic.Positivity

/-! The monic triangular pivot for the product-topology shortcut transfer.
The scalar group is arbitrary. Coordinates below degree three are ignored. -/
@[expose] public section

namespace OrdinarySequencePivot

variable {G : Type*} [AddCommGroup G]

def observed : Nat → (Nat → G) → Nat → G
  | 0, f, n => f n
  | k+1, f, n => observed k f (2*n) +
      if n % 3 = 2 ∧ 3 ≤ (2*n-1)/3 then observed k f ((2*n-1)/3) else 0

theorem pivot_difference (k n : Nat) (hn : 3 ≤ n) (f g : Nat → G)
    (agree : ∀ j, 3 ≤ j → j < 2^k*n → f j = g j) :
    observed k f n - observed k g n = f (2^k*n) - g (2^k*n) := by
  induction k generalizing n with
  | zero => simp [observed]
  | succ k ih =>
    have he : 2^k * (2*n) = 2^(k+1)*n := by simp [pow_succ, Nat.mul_assoc]
    have ev := ih (2*n) (by omega) (fun j hj h => agree j hj (he ▸ h))
    rw [observed, observed]
    by_cases hbranch : n % 3 = 2 ∧ 3 ≤ (2*n-1)/3
    · simp only [hbranch]
      have ho : 2^k * ((2*n-1)/3) < 2^(k+1)*n := by
        rw [← he]
        exact Nat.mul_lt_mul_of_pos_left (by omega) (by positivity)
      have hSmall : 3 ≤ 2^k * ((2*n-1)/3) :=
        le_trans hbranch.2 (Nat.le_mul_of_pos_left _ (by positivity))
      have od := ih ((2*n-1)/3) hbranch.2 (fun j hj h => agree j hj (lt_trans h ho))
      rw [agree _ hSmall ho, sub_self, sub_eq_zero] at od
      rw [od, add_sub_add_right_eq_sub, ev, he]
    · simpa only [hbranch, ↓reduceIte, add_zero, ← he] using ev

theorem observed_congr (k n : Nat) (hn : 3 ≤ n) (f g : Nat → G)
    (agree : ∀ j, 3 ≤ j → j ≤ 2^k*n → f j = g j) :
    observed k f n = observed k g n := by
  have h := pivot_difference k n hn f g (fun j hj h => agree j hj (le_of_lt h))
  have hp : 3 ≤ 2^k*n := le_trans hn (Nat.le_mul_of_pos_left _ (by positivity))
  apply sub_eq_zero.mp
  simpa [agree _ hp (le_refl _)] using h

/-- Every degree in the quotient has a dyadic pivot rooted at four or an odd degree. -/
theorem pivot_exists (n : Nat) (hn : 3 ≤ n) :
    ∃ u k : Nat, 3 ≤ u ∧ (u = 4 ∨ u % 2 = 1) ∧ 2^k*u=n := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases hroot : n=4 ∨ n%2=1
    · exact ⟨n,0,hn,hroot,by simp⟩
    · have hhalf : 3 ≤ n/2 := by omega
      obtain ⟨u,k,hu,hr,hk⟩ := ih (n/2) (by omega) hhalf
      exact ⟨u,k+1,hu,hr,by rw [pow_succ, Nat.mul_right_comm, hk]; omega⟩

end OrdinarySequencePivot

#print axioms OrdinarySequencePivot.pivot_difference
#print axioms OrdinarySequencePivot.observed_congr
#print axioms OrdinarySequencePivot.pivot_exists
