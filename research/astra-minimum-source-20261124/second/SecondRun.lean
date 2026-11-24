import MinimumFailure
import UpperRepresentative

namespace Collatz.SecondRun

open Collatz.MinimumFailure

/-- After a short first odd run, a merger at the actual second odd-run exit
reaches a multiple of three below the least bad multiple. -/
theorem second_exit_excludes {q : Nat} (least : LeastDiscordance q)
    (d a u e b : Nat) (short : d ≤ 2) (ha : 0 < a) (hb : 0 < b)
    (firstShape : 2^(d+1)*a = 3*q+1) (firstExit : 3^d*a = 4*u+1)
    (secondShape : 2^(e+1)*b = 6*u+2) (secondExit : (3^e*b)%4 = 3) :
    False := by
  have size : 0 < u ∧ u < q := by
    have cases_d : d=0 ∨ d=1 ∨ d=2 := by omega
    rcases cases_d with rfl | rfl | rfl <;> norm_num at firstShape firstExit <;> omega
  have safe : Good (3*u) :=
    smaller_multiples_good least (3*u) (by omega) (by omega) (by omega)
  have upper := UpperRepresentative.invariant_run (f := label) label_step
    (d+1) (2^(d+1)*a-1)
  rw [UpperRepresentative.all_odd _ _ ha, firstShape, Nat.add_sub_cancel] at upper
  have firstEnd : 3^(d+1)*a-1 = 12*u+2 := by
    rw [Nat.pow_succ, Nat.mul_right_comm, firstExit]
    omega
  have halve : SourceDeletion.step (12*u+2) = 6*u+1 := by
    unfold SourceDeletion.step
    split <;> omega
  rw [firstEnd, ← label_step (12*u+2), halve] at upper
  have meet := UpperRepresentative.first_exit_labels label label_step e b hb secondExit
  have twice : 2^(e+1)*b = 2*(2^e*b) := by rw [Nat.pow_succ]; ring
  rw [secondShape, show 2^e*b-1=3*u by omega] at meet
  have original : label (3*q) = label 1 :=
    upper.symm.trans ((by simpa using meet : label (6*u+1) = label (3*u)).trans
      ((label_eq_one _).mpr safe))
  exact upper_bad least ((label_eq_one _).mp original)

#print axioms second_exit_excludes

end Collatz.SecondRun
