import BoundedLanguage

open CollatzBoundedLanguage

#check correction_identity
#check defect_identity
#check numerator_defect_identity
#check exists_reaches_iff_dvd
#check Block.ofCounts
#check Block.reaches_unique
#check Block.preimage_reaches_iff_dvd
#check Block.zero_defect_source
#check Block.exponent_lt_defect
#check Block.sources_finite
#check Block.mem_inverseFinset
#check sources_finite
#check mem_inverseFinset

#print axioms correction_identity
#print axioms defect_identity
#print axioms numerator_defect_identity
#print axioms exists_reaches_iff_dvd
#print axioms Block.ofCounts
#print axioms Block.u_ne_zero
#print axioms Block.slope_ne
#print axioms Block.reaches_unique
#print axioms Block.preimage_eq_of_reaches
#print axioms Block.preimage_reaches_iff_dvd
#print axioms Block.zero_defect_source
#print axioms Block.exponent_lt_defect
#print axioms Block.sources_finite
#print axioms Block.mem_inverseFinset
#print axioms sources_finite
#print axioms mem_inverseFinset

run_elab do
  let env ← Lean.getEnv
  for n in env.header.moduleNames do
    Lean.logInfo m!"IMPORT_CLOSURE {n}"
