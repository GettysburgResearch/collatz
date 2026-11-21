import Collatz

-- The #check lines retain the unproved global hypothesis in the displayed type.
#check @CollatzHalfCrossing.collatz_of_half_budget
#check @CollatzBudgetCheck.collatz_of_universal_budget_check
#print axioms CollatzHalfCrossing.run_identity
#print axioms CollatzHalfCrossing.run_debt
#print axioms CollatzHalfCrossing.half_crossing_descent
#print axioms CollatzHalfCrossing.collatz_of_half_budget
#print axioms CollatzBudgetCheck.witness_clock_bound
#print axioms CollatzBudgetCheck.budgetCheck_iff
#print axioms CollatzBudgetCheck.collatz_of_universal_budget_check
#print axioms CollatzCrossShadow.trace_holds
#print axioms CollatzCrossShadow.psi_terminal_counts
#print axioms CollatzCrossShadow.psi_close_of_terminal_guard
#print axioms CollatzCrossShadow.terminal_clock_counterexample
#print axioms CollatzInverseReturn.source_run
#print axioms CollatzInverseReturn.companion_run
#print axioms CollatzInverseReturn.excludes_least_failure
