/-
The entire valuation-one psi branch closes in the original interval induction.
No inspection of the supplied odd gap word is needed. The same proof covers
every positive target sixteen units below that boundary, with no finite cutoff.
-/
import Collatz.LowGapGlobal

open CollatzReverseBasin CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzBoundedGapCofinal

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzPsiValuationOne

/-- Removing only the initial halving preserves the complete odd certificate
and strictly decreases the same multiset rank used by all interval rules. -/
theorem erase_initial_even (gaps : List Nat) :
    Less (grades 0 gaps) (grades 1 gaps) := by
  have drop := replace_one_with_tail 3 [] (gaps.map (2*·)) (by simp)
  simpa [grades] using drop

/-- An unbounded target lattice closes for every supplied valuation-one
source certificate, with no condition on any odd gap or the word length. -/
theorem lattice_rule (source target offset : Nat) (gaps : List Nat)
    (cert : PoweredCertificate source 1 gaps) (positive : 0<target)
    (boundary : target+16*offset+1=2*source)
    (ih : CollatzGapComparison.Hyp Interval (grades 1 gaps)) : Basin target := by
  obtain ⟨q,parent,sourceCert⟩ := cert
  have parent' : source=2*q := by simpa using parent
  have odd : q%2=1 := witness_odd (certificate_witness sourceCert)
  let v := 9*q-1-36*offset
  have vp : 0<v := by dsimp [v]; omega
  have cap : v≤9*q+3 := by dsimp [v]; omega
  have phase : v%4=(q+3)%4 := by dsimp [v]; omega
  have targetPath : Prefix target [1,1] v := by
    refine ⟨by simp [PositiveGaps],?_⟩
    change 9*target+5=4*v
    dsimp [v]
    omega
  have childIH : CollatzGapComparison.Hyp Interval (grades 0 gaps) := by
    intro s t e word active supplied smaller
    exact ih s t e word active supplied (less_trans smaller (erase_initial_even gaps))
  exact (prefix_basin targetPath).mpr
    (CollatzLowGapGlobal.nine_lattice_return q v gaps sourceCert vp cap phase childIH)

/-- Every psi query with exactly one initial source halving returns under
the original interval induction hypothesis. This is a proved step rule;
the remaining interval coverage premise is not assumed as a theorem. -/
theorem psi_rule (source : Nat) (gaps : List Nat)
    (cert : PoweredCertificate source 1 gaps)
    (ih : CollatzGapComparison.Hyp Interval (grades 1 gaps)) :
    Basin (2*source-1) := by
  obtain ⟨q,parent,sourceCert⟩ := cert
  have odd : q%2=1 := witness_odd (certificate_witness sourceCert)
  have parent' : source=2*q := by simpa using parent
  exact lattice_rule source (2*source-1) 0 gaps ⟨q,parent,sourceCert⟩
    (by omega) (by omega) ih

end CollatzPsiValuationOne
