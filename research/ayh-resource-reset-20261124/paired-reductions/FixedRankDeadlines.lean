import OddClockFloor
import MersenneBarrier

/-! Upper first-hit odd count does not give a uniform deadline for physical
descent on the lower arm, even when a single exact rank is prescribed. -/
namespace FixedRankDeadlines
open CollatzReverseBasin WordRank OrdinaryWordRealization

private theorem count_bound (k x : Nat) : odds k x≤k := by
  induction k generalizing x with
  | zero => rfl
  | succ k ih =>
    change x%2+odds k (shortcut x)≤k+1
    have tail := ih (shortcut x)
    omega

private theorem lower_floor (z q : Nat) (ascent : odds q (run 7 z)=q) :
    ∀ i≤7+q, z≤128*run i z := by
  have elementary (j : Nat) (small : j≤7) : z≤128*run j z := by
    have coeff := OddClockFloor.linear_lower j z
    have pos : 0<3^(odds j z) := Nat.pow_pos (by decide)
    have two := Nat.pow_le_pow_right (by decide : 0<2) small
    calc
      z ≤ 3^(odds j z)*z := by simpa using Nat.mul_le_mul_right z pos
      _ ≤ 2^j*run j z := coeff
      _ ≤ _ := Nat.mul_le_mul_right _ two
  intro i cap
  by_cases small : i≤7
  · exact elementary i small
  obtain ⟨k,identity⟩ := Nat.exists_eq_add_of_le (by omega : 7≤i)
  let n := run 7 z
  have part := oddsAdd k (q-k) n
  rw [show k+(q-k)=q by omega] at part
  have tail := count_bound (q-k) (run k n)
  change odds q n=q at ascent
  have lead := count_bound k n
  have allOdd : odds k n=k := by omega
  have up := OddClockFloor.linear_lower k n
  rw [allOdd] at up
  have grow : n≤run k n := by
    have left := Nat.mul_le_mul_right n (Nat.pow_le_pow_left (by decide : 2≤3) k)
    exact Nat.le_of_mul_le_mul_left (left.trans up) (Nat.pow_pos (by decide : 0<2))
  rw [identity,runAdd]
  exact (elementary 7 le_rfl).trans (Nat.mul_le_mul_left _ grow)

private theorem rank_three (H L : Nat) :
    ∃ z J q, L≤z ∧ z%48=17 ∧ H≤q ∧ FirstHit (3*z) J ∧ odds J (3*z)=3 ∧
      odds q (run 7 z)=q := by
  let m := L+H
  let q := 162*m+11
  obtain ⟨z,res,eq,_,_⟩ := MersenneBarrier.mersenne_family m
  change 81*z+271=128*2^q at eq
  have high : H≤q := by dsimp [q,m]; omega
  have size : L≤z := by
    have p := Nat.lt_two_pow_self (n:=q)
    dsimp [q,m] at eq p
    omega
  have eq' : 81*z+271=128*2^(0+2)*2^(q-2) := by
    rw [eq,show q=(q-2)+2 by dsimp [q]; omega] at ⊢
    simp only [Nat.add_sub_cancel,pow_add]
    ring
  obtain ⟨power,cnt⟩ := upper 0 (2^(q-2)) z eq'
  obtain ⟨first,rank⟩ := powerFinish (9+0) (3*z) (q-2) (by dsimp [q]; omega) power
  have actual := lower q 1 z (by decide) (by simpa using eq)
  exact ⟨z,_,q,size,res,high,first,rank.trans cnt,actual.2.1⟩

/-- At any fixed exact upper rank from three onwards, arbitrarily long
lower expansions occur at cofinally many positive sources. Every physical
lower iterate through the supplied deadline stays at least z/128. -/
theorem no_rank_deadline (R H L : Nat) (rank : 3≤R) :
    ∃ z J q, L≤z ∧ z%48=17 ∧ H≤q ∧ FirstHit (3*z) J ∧ odds J (3*z)=R ∧
      odds q (run 7 z)=q ∧ ∀ i≤7+q, z≤128*run i z := by
  suffices exists_source : ∃ z J q, L≤z ∧ z%48=17 ∧ H≤q ∧
      FirstHit (3*z) J ∧ odds J (3*z)=R ∧ odds q (run 7 z)=q by
    obtain ⟨z,J,q,size,res,high,first,cnt,asc⟩ := exists_source
    exact ⟨z,J,q,size,res,high,first,cnt,asc,lower_floor z q asc⟩
  by_cases three : R=3
  · subst R; exact rank_three H L
  let q := H+2
  obtain ⟨s,lo,hi,make⟩ := realization q (by dsimp [q]; omega) []
  change s≤0+1 at hi
  obtain ⟨z,_,J,size,res,_,_,_,asc,_,_,first,cnt⟩ := make (R-4) L
  exact ⟨z,J,q,size,res,by dsimp [q]; omega,first,by omega,asc⟩

#print axioms no_rank_deadline
end FixedRankDeadlines
