/-
The initial-even-exponent-two psi branch closes for every supplied first
odd gap two. The literal tail is unrestricted, and both residue cases use
the original complete-source interval induction hypothesis.
-/
import Collatz.ClockSynchronization

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzLowIntervalRefinement CollatzBoundedGapCofinal

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzPsiEvenHeadTwo

/-- The exact target path uses only the supplied first source gap. Its
endpoint may be even, and no target convergence certificate is assumed. -/
theorem target_prefix (source q u : Nat) (parent : source=4*q)
    (edge : 3*q+1=4*u) :
    Prefix (2*source-1) [1,1,2,1] (27*u-7) := by
  refine ⟨by simp [PositiveGaps],?_⟩
  change 81*(2*source-1)+73=32*(27*u-7)
  omega

/-- All initial-exponent-two psi queries with first source gap two close.
If the literal tail endpoint is1 mod4, quarter the target carry and retain
the initial exponent2. If it is3 mod4, consume the actual following gap1;
the resulting odd source exceeds the old odd source and keeps the target
inside the interval. No restriction on any later source gap is imposed. -/
theorem psi_rule (source : Nat) (tail : List Nat)
    (cert : PoweredCertificate source 2 (2::tail))
    (ih : CollatzGapComparison.Hyp Interval (grades 2 (2::tail))) :
    Basin (2*source-1) := by
  obtain ⟨q,parent,qcert⟩ := cert
  obtain ⟨_,u,edge,tailCert⟩ := (certificate_cons_iff q 2 tail).mp qcert
  change source=4*q at parent
  change 3*q+1=4*u at edge
  have qo := witness_odd (certificate_witness qcert)
  have uo := witness_odd (certificate_witness tailCert)
  have first : Less (grades 2 tail) (grades 2 (2::tail)) :=
    prefix_rank 2 [2] tail (by decide)
  by_cases phase : u%4=1
  · let v := (27*u-7)/4
    have factor : 27*u-7=4*v := by dsimp [v]; omega
    have child : Basin v :=
      ih (4*u) v 2 tail ⟨by omega,by omega⟩ ⟨u,rfl,tailCert⟩ first
    have carried : Basin (27*u-7) := by
      rw [factor]
      exact (basin_pow_two 2 v).mpr child
    exact (prefix_basin (target_prefix source q u parent edge)).mpr carried
  · have phase' : u%4=3 := by omega
    let v := shortcut u
    have step : 2*v=3*u+1 := by dsimp [v]; unfold shortcut; split <;> omega
    have vo : v%2=1 := by omega
    have grows : q<v := by omega
    obtain ⟨f,word,child,decrease⟩ := ordinary_step
      (show PoweredCertificate u 0 tail from ⟨u,by simp,tailCert⟩) (by omega)
    obtain ⟨w,value,wcert⟩ := child
    have value' : v=2^f*w := value
    cases f with
    | zero =>
      have same : v=w := by simpa using value'
      have vcert : Certificate v word := by simpa [←same] using wcert
      have lifted : Less (grades 2 word) (grades 2 tail) := by
        have before : Less (word.map (2*·)) (tail.map (2*·)) := by
          simpa [grades] using decrease
        have both := (less_append_left_iff [5] (word.map (2*·))
          (tail.map (2*·))).mpr before
        simpa [grades] using both
      exact ih (4*v) (2*source-1) 2 word ⟨by omega,by omega⟩
        ⟨v,rfl,vcert⟩ (less_trans lifted first)
    | succ f =>
      have evenForm : v=2*(2^f*w) := by
        rw [value',Nat.pow_succ]
        ac_rfl
      omega

end CollatzPsiEvenHeadTwo
