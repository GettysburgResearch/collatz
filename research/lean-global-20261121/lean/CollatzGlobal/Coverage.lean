import CollatzGlobal.PsiNormalization

set_option maxRecDepth 10000
set_option maxHeartbeats 1000000

/-! Exact coverage diagnostics for the common-potential attempt.
No assertion here assumes a hypothetical failing source exists. -/

open CollatzReverseBasin

namespace CollatzGlobal

/-- A finite, decidable first-hit assertion about the actual ordinary orbit. -/
def FirstHitAt (n d : Nat) : Prop :=
  orbit n d = 1 ∧ ∀ i : Fin d, orbit n i.val ≠ 1

instance (n d : Nat) : Decidable (FirstHitAt n d) := by
  unfold FirstHitAt
  infer_instance

/-- These are canonical first-hit clocks, not artificially padded witnesses. -/
theorem binary_source_first_hits :
    FirstHitAt 1153 96 ∧ FirstHitAt 1281 36 := by decide

/-- The same example after the exact seven-clock binary-to-psi conjugation. -/
theorem psi_source_first_hits :
    FirstHitAt 731 89 ∧ FirstHitAt 812 29 := by decide

/-- Numeric order and the proposed clock-weighted potential disagree even on
canonical source certificates. Cross multiplication is over exact integers. -/
theorem source_order_not_potential_order :
    1153 < 1281 ∧ 1154*201^60 > 1282*200^60 ∧
    731 < 812 ∧ 732*201^60 > 813*200^60 := by decide

/-- Every member of the rank-five parameter equation is 2 modulo4. The full
exponent progression is not needed for this guard obstruction. -/
theorem rank_five_parameter_mod_four (M e : Nat)
    (h : 243*M+22 = 8*2^e) : M%4=2 := by omega

/-- All eight fixed negative-reference templates require this guard; the entire
rank-five parameter family fails it, independently of certificate length. -/
theorem rank_five_parameter_misses_negative_guard (M e : Nat)
    (h : 243*M+22 = 8*2^e) : M%2048 ≠ 2047 := by
  have hfour := rank_five_parameter_mod_four M e h
  omega

end CollatzGlobal
