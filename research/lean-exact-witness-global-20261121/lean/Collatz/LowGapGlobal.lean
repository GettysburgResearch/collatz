/-
Whole-certificate carry returns, using actual ordinary source steps.
The negative-nine carry returns for every supplied odd source certificate.
Consequently the positive-nine carry needs only a first source gap one;
its entire remaining source word is unrestricted.

This strengthens the source language in PR185 CarryLanguage.lean. The
improvement uses retained even runs and the enlarged odd-source ceiling,
while preserving PR177's original complete-source multiset rank.
-/
import Collatz.LowIntervalRefinement

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzHighGapPump CollatzBoundedGapCofinal

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzLowGapGlobal

/-- One ordinary step of a nonterminal odd source covers the larger target
ceiling 3q+2. Its actual complete child certificate strictly lowers Γ. -/
theorem odd_source_cap (q target : Nat) (gaps : List Nat)
    (cert : Certificate q gaps) (positive : 0<target) (upper : target≤3*q+2)
    (ih : CollatzGapComparison.Hyp Interval (grades 0 gaps)) : Basin target := by
  by_cases one : q=1
  · exact CollatzLowIntervalRefinement.terminal_range target positive (by omega)
  have odd : q%2=1 := witness_odd (certificate_witness cert)
  have step : 2*shortcut q=3*q+1 := by unfold shortcut; split <;> omega
  exact CollatzGapComparison.ordinary_source (show PoweredCertificate q 0 gaps from
    ⟨q,by simp,cert⟩) one ⟨positive,by omega⟩ ih

/-- An unbounded affine cone returns for every complete odd source witness.
For q=1 mod4, divide the target by four and advance the source once.
For q=3 mod4, divide the target by two and advance the source twice.
No new active domain is assumed: the recursive query is inside Interval. -/
theorem nine_lattice_return (q target : Nat) (gaps : List Nat)
    (cert : Certificate q gaps) (positive : 0<target) (upper : target≤9*q+3)
    (phaseTarget : target%4=(q+3)%4)
    (ih : CollatzGapComparison.Hyp Interval (grades 0 gaps)) : Basin target := by
  have odd : q%2=1 := witness_odd (certificate_witness cert)
  by_cases one : q=1
  · exact CollatzLowIntervalRefinement.terminal_range target positive (by omega)
  by_cases phase : q%4=1
  · let childTarget := target/4
    have identity : target=4*childTarget := by dsimp [childTarget]; omega
    have known := odd_source_cap q childTarget gaps cert (by omega) (by omega) ih
    have factor : target=2^2*childTarget := by omega
    rw [factor]
    exact (basin_pow_two 2 childTarget).mpr known
  · have phase' : q%4=3 := by omega
    let v := shortcut q
    have step : 2*v=3*q+1 := by dsimp [v]; unfold shortcut; split <;> omega
    have vo : v%2=1 := by omega
    obtain ⟨e,tail,child,drop⟩ := ordinary_step
      (show PoweredCertificate q 0 gaps from ⟨q,by simp,cert⟩) one
    obtain ⟨u,childValue,childCert⟩ := child
    have childValue' : v=2^e*u := childValue
    cases e with
    | zero =>
      have value : v=u := by simpa using childValue'
      have vcert : Certificate v tail := by simpa [←value] using childCert
      have childIH : CollatzGapComparison.Hyp Interval (grades 0 tail) := by
        intro s t e word active supplied smaller
        exact ih s t e word active supplied (less_trans smaller drop)
      have known := odd_source_cap v (target/2) tail vcert (by omega) (by omega) childIH
      have factor : target=2*(target/2) := by omega
      rw [factor]
      exact (basin_twice (target/2)).mpr known
    | succ e =>
      have evenForm : v=2*(2^e*u) := by rw [childValue',Nat.pow_succ]; grind
      omega

/-- The negative-nine carry is a uniform member of the returned cone. -/
theorem negative_nine_return (q : Nat) (gaps : List Nat)
    (cert : Certificate q gaps)
    (ih : CollatzGapComparison.Hyp Interval (grades 0 gaps)) : Basin (9*q-1) := by
  have odd : q%2=1 := witness_odd (certificate_witness cert)
  exact nine_lattice_return q (9*q-1) gaps cert (by omega) (by omega) (by omega) ih

/-- Every positive-nine carry whose complete source certificate begins with
one returns. There is no restriction on the second gap, any later gap, or
the length of the literal supplied tail. -/
theorem positive_nine_first_one (q : Nat) (tail : List Nat)
    (cert : Certificate q (1::tail))
    (ih : CollatzGapComparison.Hyp Interval (grades 0 (1::tail))) : Basin (9*q+2) := by
  obtain ⟨_,u,step,tailCert⟩ := (certificate_cons_iff q 1 tail).mp cert
  have step' : 3*q+1=2*u := by simpa using step
  have odd : u%2=1 := witness_odd (certificate_witness tailCert)
  have path : Prefix (9*q+2) [1] (9*u-1) := by
    refine ⟨by simp [PositiveGaps],?_⟩
    simp only [List.length_cons,List.length_nil,correction,total]
    omega
  have drop : Less (grades 0 tail) (grades 0 (1::tail)) := by
    simpa using CollatzLowIntervalRefinement.prefix_rank 0 [1] tail (by simp)
  have childIH : CollatzGapComparison.Hyp Interval (grades 0 tail) := by
    intro s t e word active supplied smaller
    exact ih s t e word active supplied (less_trans smaller drop)
  exact (prefix_basin path).mpr (negative_nine_return u tail tailCert childIH)

/-- The two-letter source prefix [2,1] also returns every positive-nine
carry. The target uses [1,2] and enters the same unbounded affine cone. -/
theorem positive_nine_two_one (q : Nat) (tail : List Nat)
    (cert : Certificate q (2::1::tail))
    (ih : CollatzGapComparison.Hyp Interval (grades 0 (2::1::tail))) : Basin (9*q+2) := by
  obtain ⟨u,path,tailCert⟩ := CollatzLowGapLoops.split_certificate q [2,1] tail cert
  have sourceEq : 9*q+7=8*u := by simpa [Prefix,correction,total] using path.2
  have odd : u%2=1 := witness_odd (certificate_witness tailCert)
  have targetPath : Prefix (9*q+2) [1,2] (9*u-5) := by
    refine ⟨by simp [PositiveGaps],?_⟩
    simp only [List.length_cons,List.length_nil,correction,total]
    omega
  have drop : Less (grades 0 tail) (grades 0 (2::1::tail)) := by
    simpa using CollatzLowIntervalRefinement.prefix_rank 0 [2,1] tail (by simp)
  have childIH : CollatzGapComparison.Hyp Interval (grades 0 tail) := by
    intro s t e word active supplied smaller
    exact ih s t e word active supplied (less_trans smaller drop)
  have child := nine_lattice_return u (9*u-5) tail tailCert
    (by omega) (by omega) (by omega) childIH
  exact (prefix_basin targetPath).mpr child

end CollatzLowGapGlobal
