import WitnessSynthesis

/-!
Finite arithmetic for a failure of the universal extremal-source-clock claim.
The all-word grade-maximality argument is written separately. This module
checks complete physical certificates, their strict grade comparison, and
the actual original-target clock obstruction. It asserts no open analytic
premise and no universal Collatz conclusion.
-/

namespace CollatzShell.ExtremalSourceClock

open WitnessGlobal WitnessSynthesis

set_option maxRecDepth 10000

theorem source_1092_complete :
    PoweredTrace 1092 2 [2,3,3,3,1,2,3,4] := by
  refine ⟨273, by decide, by decide, ?_⟩
  exact ⟨by decide, 205, by decide,
    ⟨by decide, 77, by decide,
    ⟨by decide, 29, by decide,
    ⟨by decide, 11, by decide,
    ⟨by decide, 17, by decide,
    ⟨by decide, 13, by decide,
    ⟨by decide, 5, by decide,
    ⟨by decide, 1, by decide, rfl⟩⟩⟩⟩⟩⟩⟩⟩

theorem source_820_complete :
    PoweredTrace 820 2 [3,3,3,1,2,3,4] := by
  refine ⟨205, by decide, by decide, ?_⟩
  exact ⟨by decide, 77, by decide,
    ⟨by decide, 29, by decide,
    ⟨by decide, 11, by decide,
    ⟨by decide, 17, by decide,
    ⟨by decide, 13, by decide,
    ⟨by decide, 5, by decide,
    ⟨by decide, 1, by decide, rfl⟩⟩⟩⟩⟩⟩⟩

theorem source_820_grade_drop :
    GradeDrop (sourceGrades 2 [3,3,3,1,2,3,4])
      (sourceGrades 2 [2,3,3,3,1,2,3,4]) := by
  refine ⟨4, by decide, ?_⟩
  intro b hb
  have ne : b ≠ 4 := by omega
  simp [sourceGrades, List.count_cons, Ne.symm ne]

theorem source_1092_clock : orbit 23 1092 = 1 := by decide

theorem target_2047_is_new :
    2*820+1 < 2047 ∧ Interval 1092 2047 := by
  unfold Interval
  decide

theorem target_2047_at_source_clock : orbit 23 2047 = 283763 := by decide

theorem target_2047_no_descent_before_58 :
    ∀ k : Fin 57, 2134 ≤ orbit (k.val+1) 2047 := by decide

theorem target_2047_at_58 : orbit 58 2047 = 1067 := by decide

#print axioms source_1092_complete
#print axioms source_820_complete
#print axioms source_820_grade_drop
#print axioms source_1092_clock
#print axioms target_2047_is_new
#print axioms target_2047_at_source_clock
#print axioms target_2047_no_descent_before_58
#print axioms target_2047_at_58

end CollatzShell.ExtremalSourceClock
