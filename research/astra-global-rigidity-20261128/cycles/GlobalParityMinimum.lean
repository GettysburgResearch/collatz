import ParityRecordHorizon
import Mathlib.Tactic.GCongr

namespace Collatz.GlobalParityMinimum

open Collatz.MersenneCrests (State)
open Collatz.ParityRecordHorizon (grade odds strict_record_clock)

/-- The integer cutoff test propagates forward in the native clock. -/
theorem cutoff_monotone (n K m : Nat) (hKm : K ≤ m)
    (hK : 4*n^2*3^K ≤ 4^K) : 4*n^2*3^m ≤ 4^m := by
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hKm
  have hp : (3 : Nat)^d ≤ 4^d := Nat.pow_le_pow_left (by decide) d
  calc
    _ = (4*n^2*3^K)*3^d := by rw [pow_add]; ac_rfl
    _ ≤ 4^K*4^d := Nat.mul_le_mul hK hp
    _ = _ := (pow_add _ _ _).symm

private theorem strict_below_cut (z : State) (hz : 0 < z.1) (t : Nat)
    (record : ∀ k ≤ t, grade z (t+1) < grade z k) :
    4^(t+1) < 4*z.1^2*3^(t+1) := by
  have hoc : 2*odds z (t+1) ≤ t+1 := by
    have hg := record 0 (Nat.zero_le _)
    have hzero : grade z 0 = 0 := by simp [grade, odds]
    rw [hzero] at hg
    unfold grade at hg
    omega
  have ha := strict_record_clock z hz t record
  have hs : (2^(t+1))^2 < (2*3^(odds z (t+1))*z.1)^2 :=
    Nat.pow_lt_pow_left ha (by decide)
  have hp : (3 : Nat)^(2*odds z (t+1)) ≤ 3^(t+1) :=
    Nat.pow_le_pow_right (by decide) hoc
  calc
    4^(t+1) = (2^(t+1))^2 := by
      rw [← pow_mul, Nat.mul_comm (t+1) 2, pow_mul]
      rfl
    _ < _ := hs
    _ = 4*z.1^2*3^(2*odds z (t+1)) := by
      rw [Nat.mul_comm 2 (odds z (t+1)), pow_mul]
      ring
    _ ≤ _ := Nat.mul_le_mul_left _ hp

/-- A finite prefix of each supplied positive orbit attains its entire lifetime grade minimum. -/
theorem cutoff_covers_all (z : State) (hz : 0 < z.1) (K : Nat)
    (cut : 4*z.1^2*3^K ≤ 4^K) (m : Nat) :
    ∃ k ≤ K, grade z k ≤ grade z m := by
  induction m using Nat.strong_induction_on with
  | h m ih =>
    by_cases hshort : m ≤ K
    · exact ⟨m, hshort, le_refl _⟩
    have hKm : K ≤ m := by omega
    have previous : ∃ k < m, grade z k ≤ grade z m := by
      by_contra! hall
      obtain ⟨t, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : m ≠ 0)
      have hr := strict_below_cut z hz t (fun k hk => hall k (by omega))
      have hl := cutoff_monotone z.1 K (t+1) hKm cut
      omega
    obtain ⟨j, hj, hgrade⟩ := previous
    obtain ⟨k, hk, hprev⟩ := ih j hj
    exact ⟨k, hk, le_trans hprev hgrade⟩

end Collatz.GlobalParityMinimum
