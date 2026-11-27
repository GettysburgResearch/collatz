module

public import TernaryItinerary
import all TernaryItinerary

public section

namespace Collatz.Itinerary.TowerFrontier

set_option autoImplicit false

theorem odd_steps (k u : Nat) (hu : 0<u) :
    run k (2^k*u-1) = 3^k*u-1 := by
  induction k generalizing u with
  | zero => simp [run]
  | succ k ih =>
    have pos := Nat.mul_pos (Nat.two_pow_pos k) hu
    have pow : 2^(k+1)*u = 2*(2^k*u) := by rw [Nat.pow_succ]; ac_rfl
    have hs : step (2*(2^k*u)-1) = 2^k*(3*u)-1 := by
      have odd : (2*(2^k*u)-1)%2=1 := by omega
      simp only [step,odd,Nat.reduceEqDiff,↓reduceIte]
      rw [show 2^k*(3*u)=3*(2^k*u) by ac_rfl]
      omega
    rw [pow,run,hs,ih _ (by omega),Nat.pow_succ]
    congr 1
    ac_rfl

theorem first_three (n : Nat) (hn : 0<n) :
    step (8*n-1)=12*n-1 ∧ step (12*n-1)=18*n-1 ∧
    step (3*(8*n-1))=36*n-4 ∧ step (36*n-4)=18*n-2 ∧
    step (18*n-2)=9*n-1 := by
  simp only [step]
  repeat' constructor
  all_goals split <;> omega

/-- At the prescribed ranks zero and one, arbitrarily large eligible bases
    defeat both common-clock merging and descent below the base up to any
    supplied finite deadline. -/
theorem fixed_rank_obstruction (H L : Nat) :
    ∃ w > L, w%6=5 ∧ ∀ k ≤ H,
      w ≤ run k w ∧ w < run k (3*w) ∧ run k w ≠ run k (3*w) := by
  let n := 3*(2^H*(L+1))
  have hn : 0<n := Nat.mul_pos (by decide) (Nat.mul_pos (Nat.two_pow_pos _) (by omega))
  have large : L+1 ≤ 2^H*(L+1) := Nat.le_mul_of_pos_left _ (Nat.two_pow_pos _)
  refine ⟨8*n-1,by dsimp [n]; omega,by dsimp [n]; omega,?_⟩
  intro k hk
  obtain ⟨l1,l2,r1,r2,r3⟩ := first_three n hn
  cases k with
  | zero => simp only [run]; omega
  | succ k =>
    cases k with
    | zero => simp only [run,l1,r1]; omega
    | succ k =>
      cases k with
      | zero => simp only [run,l1,l2,r1,r2]; omega
      | succ j =>
        let u := 3*(2^(H-j)*(L+1))
        have hu : 0<u := Nat.mul_pos (by decide) (Nat.mul_pos (Nat.two_pow_pos _) (by omega))
        have repr : n=2^j*u := by
          dsimp [n,u]
          rw [show H=j+(H-j) by omega] at ⊢
          simp only [Nat.add_sub_cancel_left,Nat.pow_add]
          ac_rfl
        have left : run (j+3) (8*n-1) = 27*(3^j*u)-1 := by
          have arg : 8*n-1=2^(j+3)*u-1 := by
            rw [repr,Nat.pow_add,show 2^3=8 by decide]; congr 1; ac_rfl
          rw [arg,odd_steps _ _ hu,Nat.pow_add,show 3^3=27 by decide]
          congr 1
          ac_rfl
        have right : run (j+3) (3*(8*n-1)) = 9*(3^j*u)-1 := by
          rw [Nat.add_comm j 3,run_add,show run 3 (3*(8*n-1))=9*n-1 by
            simp only [run,r1,r2,r3]]
          have arg : 9*n=2^j*(9*u) := by rw [repr]; ac_rfl
          rw [arg,odd_steps _ _ (by omega)]
          congr 1
          ac_rfl
        have grow : 2^j*u ≤ 3^j*u :=
          Nat.mul_le_mul_right _ (Nat.pow_le_pow_left (by decide : 2≤3) _)
        have pos := Nat.mul_pos (Nat.pow_pos (by decide : 0<3) (n:=j)) hu
        rw [left,right,repr]
        omega

#print axioms fixed_rank_obstruction

end Collatz.Itinerary.TowerFrontier
