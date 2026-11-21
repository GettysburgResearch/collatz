/-
The first-gap-four boundary at initial halving length one closes exactly.
An interval source reset loses two units of source size; its two uncovered
odd targets have explicit ordinary basin transports back inside the child.
-/
import Collatz.BoundedGapCofinal

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzGapComparison CollatzBoundedGapCofinal

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzRetainedEvenBoundary

/-- The source sibling removes two from the first odd gap and retains three
initial halvings. Its entire supplied suffix is preserved. -/
theorem sibling_certificate (q a : Nat) (tail : List Nat)
    (cert : Certificate q (a::tail)) (high : 4≤a) :
    ∃ p, q=4*p+1 ∧ 0<p ∧ Certificate p ((a-2)::tail) ∧
      Less (grades 3 ((a-2)::tail)) (grades 1 (a::tail)) := by
  obtain ⟨_,u,edge,tailCert⟩ := (certificate_cons_iff q a tail).mp cert
  have exponent : a=(a-2)+2 := by omega
  have factor : 2^a=4*2^(a-2) := by
    calc
      2^a = 2^((a-2)+2) := congrArg (fun b : Nat => 2^b) exponent
      _ = 4*2^(a-2) := by rw [Nat.pow_add]; omega
  rw [factor] at edge
  have edge' : 3*q+1=4*(2^(a-2)*u) := by simpa [Nat.mul_assoc] using edge
  let p := (q-1)/4
  have shape : q=4*p+1 := by dsimp [p]; omega
  have childEdge : 3*p+1=2^(a-2)*u := by omega
  have child : Certificate p ((a-2)::tail) :=
    (certificate_cons_iff p (a-2) tail).mpr ⟨by omega,u,childEdge,tailCert⟩
  have odd : p%2=1 := witness_odd (certificate_witness child)
  refine ⟨p,shape,by omega,child,?_⟩
  have below : ∀ b ∈ [7,2*(a-2)], b<2*a := by
    intro b hb
    simp only [List.mem_cons,List.not_mem_nil,or_false] at hb
    omega
  have drop := replace_one_with_tail (2*a) [7,2*(a-2)] (tail.map (2*·)) below
  have first : Less (grades 3 ((a-2)::tail)) (grades 0 (a::tail)) := by
    simpa [grades] using drop
  have erase := replace_one_with_tail 3 [] ((a::tail).map (2*·)) (by simp)
  have second : Less (grades 0 (a::tail)) (grades 1 (a::tail)) := by
    simpa [grades] using erase
  exact less_trans first second

/-- The uncovered lower odd boundary has the exact ordinary prefix [1,3]. -/
theorem boundary_prefix (p : Nat) : Prefix (16*p+3) [1,3] (9*p+2) := by
  refine ⟨by simp [PositiveGaps],?_⟩
  simp [correction,total]
  omega

/-- Every target in the full interval closes when the source has initial
halving length one and first odd gap at least four. This includes the
previous low-alphabet boundary a=4, with no residue or suffix restriction. -/
theorem leading_large_gap_interval_rule (source target a : Nat) (tail : List Nat)
    (cert : PoweredCertificate source 1 (a::tail))
    (positive : 0<target) (upper : target≤2*source+1) (high : 4≤a)
    (ih : Hyp Interval (grades 1 (a::tail))) : Basin target := by
  obtain ⟨q,sourceEq,qcert⟩ := cert
  have sourceShape : source=2*q := by simpa using sourceEq
  obtain ⟨p,qShape,pPositive,pcert,drop⟩ := sibling_certificate q a tail qcert high
  have childCert : PoweredCertificate (8*p) 3 ((a-2)::tail) := ⟨p,rfl,pcert⟩
  have within (u : Nat) (upos : 0<u) (ubound : u≤16*p+1) : Basin u :=
    ih (8*p) u 3 ((a-2)::tail) ⟨upos,by omega⟩ childCert drop
  by_cases even : target%2=0
  · have erase := replace_one_with_tail 3 [] ((a::tail).map (2*·)) (by simp)
    have smaller : Less (grades 0 (a::tail)) (grades 1 (a::tail)) := by
      simpa [grades] using erase
    have half : Basin (target/2) :=
      ih q (target/2) 0 (a::tail) ⟨by omega,by omega⟩ ⟨q,by simp,qcert⟩ smaller
    have targetEq : target=2*(target/2) := by omega
    rw [targetEq]
    exact (basin_twice (target/2)).mpr half
  have odd : target%2=1 := by omega
  by_cases near : target≤16*p+1
  · exact within target positive near
  have cases : target=16*p+3 ∨ target=16*p+5 := by omega
  rcases cases with lower | uppermost
  · rw [lower]
    exact (prefix_basin (boundary_prefix p)).mpr
      (within (9*p+2) (by omega) (by omega))
  · have known : Basin q := witness_basin (certificate_witness qcert)
    have qo : q%2=1 := witness_odd (certificate_witness qcert)
    have top : Basin (4*q+1) :=
      (basin_exch (4*q+1) (3*q+1) q rfl rfl).mpr ((basin_odd q qo).mpr known)
    have topEq : target=4*q+1 := by omega
    rwa [topEq]

end CollatzRetainedEvenBoundary
