import ActualOneRun
import OrdinaryShadow
import ThreeRunCore

-- New public theorems, including the intermediate bridge theorems.
#print axioms Collatz.PhaseRepulsion.one_run
#print axioms Collatz.PhaseRepulsion.one_run_length
#print axioms Collatz.PhaseRepulsion.three_run_length
#print axioms Collatz.OrdinaryShadow.smaller_nonconverger
#print axioms Collatz.ActualThreeRun.three_run_bound
#print axioms Collatz.ActualThreeRun.carry_lt
#print axioms Collatz.ActualThreeRun.actual_floor
#print axioms Collatz.ActualThreeRun.actual_clock
#print axioms Collatz.ActualThreeRun.actual_three_run
#print axioms Collatz.PhaseRepulsion.actual_one_run

-- Selected upstream results, counted separately from the new theorems.
#print axioms Collatz.CarryTowerRoundTen.ActualScalar.scalar_summable
#print axioms Collatz.CarryTowerRoundTen.ActualScalar.scalar_upper
#print axioms Collatz.CarryTowerRoundTen.ActualScalar.scalar_recurrence
#print axioms Collatz.CarryTowerRoundTen.ActualScalar.scalar_strict_lower
#print axioms Collatz.CarryTowerRoundTen.ActualScalar.converges_iff_triadic
