import CycleMinimum

open CollatzCycleMinimum

#check whole_cycle_minimum_nat

#print axioms product_deficit_le_sum
#print axioms minimum_product_deficit
#print axioms whole_cycle_ratio
#print axioms whole_cycle_minimum_rat
#print axioms whole_cycle_minimum_nat

run_elab do
  let env ← Lean.getEnv
  for n in env.header.moduleNames do
    Lean.logInfo m!"IMPORT_CLOSURE {n}"
