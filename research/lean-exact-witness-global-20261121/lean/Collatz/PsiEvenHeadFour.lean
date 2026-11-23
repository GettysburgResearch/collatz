/-
Complete valuation-two, first-gap-four psi closure. An ordinary target
merger is followed by an exhaustive three-cell ternary source rewrite.
The supplied suffix is retained in every case, including endpoint one.
-/
import Collatz.LowGapGlobal

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzBoundedGapCofinal

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzPsiEvenHeadFour

/-- The target 8q-1 and the smaller ordinary partner 27u-2 have exact
positive-gap prefixes to the same endpoint, whenever 3q+1=16u. -/
theorem head_four_target_equivalence (q u : Nat)
    (edge : 3*q+1=16*u) (odd : u%2=1) :
    Basin (8*q-1) ↔ Basin (27*u-2) := by
  let endpoint := (81*u-5)/2
  have identity : 2*endpoint=81*u-5 := by dsimp [endpoint]; omega
  have big : Prefix (8*q-1) [1,1,2,1,3] endpoint := by
    refine ⟨by simp [PositiveGaps],?_⟩
    simp only [List.length_cons,List.length_nil,correction,total]
    omega
  have small : Prefix (27*u-2) [1] endpoint := by
    refine ⟨by simp [PositiveGaps],?_⟩
    simp only [List.length_cons,List.length_nil,correction,total]
    omega
  exact (prefix_basin big).trans (prefix_basin small).symm

/-- Removing the leading four pays the new initial run three and every
new odd gap at most three. The old initial grade is also removed. -/
theorem replaced_four_rank (word tail : List Nat) (bounded : ∀ a∈word, a≤3) :
    Less (grades 3 (word++tail)) (grades 2 (4::tail)) := by
  have below : ∀ b∈7::word.map (2*·), b<8 := by
    intro b hb
    rcases List.mem_cons.mp hb with eq | mem
    · omega
    · obtain ⟨a,ha,eq⟩ := List.mem_map.mp mem
      have small := bounded a ha
      omega
  have drop := replace_one_with_tail 8 (7::word.map (2*·)) (tail.map (2*·)) below
  have first : Less (grades 3 (word++tail)) (grades 0 (4::tail)) := by
    simpa [grades,List.map_append] using drop
  have erase := replace_one_with_tail 5 [] ((4::tail).map (2*·)) (by simp)
  have second : Less (grades 0 (4::tail)) (grades 2 (4::tail)) := by
    simpa [grades] using erase
  exact less_trans first second

/-- Retaining the leading four is also permitted: decrease the initial
grade five to three and insert one odd grade four. -/
theorem retained_four_rank (tail : List Nat) :
    Less (grades 1 (2::4::tail)) (grades 2 (4::tail)) := by
  have below : ∀ b∈[3,4], b<5 := by
    intro b hb
    simp only [List.mem_cons,List.not_mem_nil,or_false] at hb
    omega
  have drop := replace_one_with_tail 5 [3,4] ((4::tail).map (2*·)) below
  simpa [grades] using drop

/-- Every initial-valuation-two source beginning with odd gap four closes
its psi query under the original common interval induction hypothesis.
All three ternary residue cells and the endpoint-one case are included. -/
theorem psi_even_head_four_rule (source : Nat) (tail : List Nat)
    (cert : PoweredCertificate source 2 (4::tail))
    (ih : CollatzGapComparison.Hyp Interval (grades 2 (4::tail))) : Basin (2*source-1) := by
  obtain ⟨q,sourceEq,qcert⟩ := cert
  obtain ⟨_,u,edge,tailCert⟩ := (certificate_cons_iff q 4 tail).mp qcert
  have sourceShape : source=4*q := by simpa using sourceEq
  have edge' : 3*q+1=16*u := by simpa using edge
  have odd : u%2=1 := witness_odd (certificate_witness tailCert)
  have unit : u%3=1 := by omega
  have targetShape : 2*source-1=8*q-1 := by omega
  rw [targetShape]
  apply (head_four_target_equivalence q u edge' odd).mpr
  have cells : u%9=1 ∨ u%9=4 ∨ u%9=7 := by omega
  rcases cells with cell | cell | cell
  · let p := (16*u-7)/9
    have equation : 9*p+7=16*u := by dsimp [p]; omega
    have path : Prefix p [2,2] u := by
      refine ⟨by simp [PositiveGaps],?_⟩
      simpa [correction,total] using equation
    have childCert : PoweredCertificate (8*p) 3 ([2,2]++tail) :=
      ⟨p,rfl,append_certificate path tailCert⟩
    have drop := replaced_four_rank [2,2] tail (by
      intro a ha
      simp only [List.mem_cons,List.not_mem_nil,or_false] at ha
      omega)
    by_cases terminal : u=1
    · have pOne : p=1 := by omega
      have targetPath : Prefix (27*u-2) [2,1,3] 11 := by
        subst u
        exact ⟨by simp [PositiveGaps],by decide⟩
      have child : Basin 11 := ih (8*p) 11 3 ([2,2]++tail)
        ⟨by decide,by omega⟩ childCert drop
      exact (prefix_basin targetPath).mpr child
    · have large : 10≤u := by omega
      exact ih (8*p) (27*u-2) 3 ([2,2]++tail)
        ⟨by omega,by omega⟩ childCert drop
  · let p := (32*u-11)/9
    have equation : 9*p+11=32*u := by dsimp [p]; omega
    have path : Prefix p [3,2] u := by
      refine ⟨by simp [PositiveGaps],?_⟩
      simpa [correction,total] using equation
    have childCert : PoweredCertificate (8*p) 3 ([3,2]++tail) :=
      ⟨p,rfl,append_certificate path tailCert⟩
    have drop := replaced_four_rank [3,2] tail (by
      intro a ha
      simp only [List.mem_cons,List.not_mem_nil,or_false] at ha
      omega)
    exact ih (8*p) (27*u-2) 3 ([3,2]++tail)
      ⟨by omega,by omega⟩ childCert drop
  · have qUnit : q%3=1 := by omega
    let p := (4*q-1)/3
    have equation : 3*p+1=4*q := by dsimp [p]; omega
    have path : Prefix p [2] q := by
      refine ⟨by simp [PositiveGaps],?_⟩
      simpa [correction,total] using equation
    have childCert : PoweredCertificate (2*p) 1 (2::4::tail) :=
      ⟨p,rfl,by simpa using append_certificate path qcert⟩
    exact ih (2*p) (27*u-2) 1 (2::4::tail)
      ⟨by omega,by omega⟩ childCert (retained_four_rank tail)

end CollatzPsiEvenHeadFour
