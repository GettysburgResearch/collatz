import Collatz

open CollatzHalfCrossing CollatzBudgetCheck

set_option maxRecDepth 10000
set_option maxHeartbeats 0

/-- Exact ordinary fixture at the tight input found during the attack. -/
theorem twenty_seven_account :
    (run 27 65).value = 10 ∧ (run 27 65).odds = 40 ∧
      search 27 83 0 = some 65 := by decide

/-- This fixture certifies a single input, not universal acceptance. -/
theorem twenty_seven_accepted : budgetCheck 27 = true := by decide

/-- One is the separately handled induction base; the proposed budget excludes it. -/
theorem one_is_separate : budgetCheck 1 = false := by decide

#print axioms twenty_seven_account
#print axioms twenty_seven_accepted
#print axioms one_is_separate
