import CollatzGlobalClosure.SignedCarry

/-!
Actual integration of the signed carry compiler with the new PR177 returns.

The odd-source cap and nine-lattice proof are dependency-light ports of
Collatz/LowGapGlobal.lean at PR177 commit
2efabba9a341839b67ed011d6b878b23730ee51d. The source return theorems and the
valuation-one psi conclusion are credited to that checkpoint. This module
keeps the existing older frozen vendor untouched, reproduces the exact
powered-source interval-hypothesis signature, and proves composition with
the signed compiler's arbitrary actual source prefix and common grade.

All induction hypotheses remain explicit. No total successful stopping
policy or unconditional interval coverage is asserted.
-/

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzSignedCarryReturns

open CollatzEndpointSteering CollatzSignedCarry
open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset

def Interval (source target : Nat) : Prop := 0<target ∧ target≤2*source+1

/-- Exactly the body of PR177's `CollatzGapComparison.Hyp Interval old`.
This includes arbitrary powered child certificates, not only odd sources. -/
def IntervalHyp (old : List Nat) : Prop :=
  ∀ source target e gaps, Interval source target →
    PoweredCertificate source e gaps → Less (grades e gaps) old → Basin target

private def hitDecision (x : Nat) : (k : Nat) → Decidable (Hits x k)
  | 0 => inferInstanceAs (Decidable (x=1))
  | k+1 => hitDecision (shortcut x) k

private theorem terminal_range (n : Nat) (positive : 0<n) (small : n≤12) : Basin n := by
  letI (x k : Nat) : Decidable (Hits x k) := hitDecision x k
  have finite : ∀ n : Fin 13, n.val≠0 → ∃ k : Fin 14, Hits n.val k.val := by decide
  let v : Fin 13 := ⟨n,by omega⟩
  have nonzero : v.val≠0 := by dsimp [v]; omega
  obtain ⟨k,hit⟩ := finite v nonzero
  exact ⟨k.val,by simpa [v] using hit⟩

theorem restrict_hyp {new old : List Nat} (drop : Less new old)
    (ih : IntervalHyp old) : IntervalHyp new := by
  intro source target e gaps active cert smaller
  exact ih source target e gaps active cert (less_trans smaller drop)

/-- Port of PR177 `LowGapGlobal.odd_source_cap` at the frozen new head. -/
theorem odd_source_cap (q target : Nat) (gaps : List Nat)
    (cert : Certificate q gaps) (positive : 0<target) (upper : target≤3*q+2)
    (ih : IntervalHyp (grades 0 gaps)) : Basin target := by
  by_cases one : q=1
  · exact terminal_range target positive (by omega)
  have odd : q%2=1 := witness_odd (certificate_witness cert)
  have stepEq : 2*shortcut q=3*q+1 := by unfold shortcut; split <;> omega
  obtain ⟨e,tail,child,drop⟩ := ordinary_step
    (show PoweredCertificate q 0 gaps from ⟨q,by simp,cert⟩) one
  exact ih (shortcut q) target e tail ⟨positive,by omega⟩ child drop

/-- Port of PR177 `LowGapGlobal.nine_lattice_return`, preserving its odd
source requirement and its exact original-grade interval hypothesis. -/
theorem nine_lattice_return (q target : Nat) (gaps : List Nat)
    (cert : Certificate q gaps) (positive : 0<target) (upper : target≤9*q+3)
    (phaseTarget : target%4=(q+3)%4)
    (ih : IntervalHyp (grades 0 gaps)) : Basin target := by
  have odd : q%2=1 := witness_odd (certificate_witness cert)
  by_cases one : q=1
  · exact terminal_range target positive (by omega)
  by_cases phase : q%4=1
  · let childTarget := target/4
    have identity : target=4*childTarget := by dsimp [childTarget]; omega
    have known := odd_source_cap q childTarget gaps cert (by omega) (by omega) ih
    have factor : target=2^2*childTarget := by omega
    rw [factor]
    exact (basin_pow_two 2 childTarget).mpr known
  · have phase' : q%4=3 := by omega
    let v := shortcut q
    have stepEq : 2*v=3*q+1 := by dsimp [v]; unfold shortcut; split <;> omega
    have vo : v%2=1 := by omega
    obtain ⟨e,tail,child,drop⟩ := ordinary_step
      (show PoweredCertificate q 0 gaps from ⟨q,by simp,cert⟩) one
    obtain ⟨u,childValue,childCert⟩ := child
    have childValue' : v=2^e*u := childValue
    cases e with
    | zero =>
      have value : v=u := by simpa using childValue'
      have vcert : Certificate v tail := by simpa [←value] using childCert
      have childIH : IntervalHyp (grades 0 tail) := restrict_hyp drop ih
      have known := odd_source_cap v (target/2) tail vcert (by omega) (by omega) childIH
      have factor : target=2*(target/2) := by omega
      rw [factor]
      exact (basin_twice (target/2)).mpr known
    | succ e =>
      have evenForm : v=2*(2^e*u) := by rw [childValue',Nat.pow_succ]; grind
      omega

theorem negative_nine_return (q : Nat) (gaps : List Nat)
    (cert : Certificate q gaps) (ih : IntervalHyp (grades 0 gaps)) : Basin (9*q-1) := by
  have odd : q%2=1 := witness_odd (certificate_witness cert)
  exact nine_lattice_return q (9*q-1) gaps cert (by omega) (by omega) (by omega) ih

/-- These are sufficient successful carry states, not a claim that the
compiler reaches one on every complete source word. Debt is signed. -/
def Absorbing (s : Carry) : Prop :=
  (s.power=0 ∧ 0≤s.debt) ∨
  (s.power=1 ∧ -2≤s.debt) ∨
  (s.power=2 ∧ -3≤s.debt ∧ s.debt%4=1)

instance (s : Carry) : Decidable (Absorbing s) := by unfold Absorbing; infer_instance

/-- Every state in the enlarged absorbing set has a valid original-grade
return for any actual complete odd source certificate. -/
theorem absorbing_return (s : Carry) (q target : Nat) (gaps : List Nat)
    (cert : Certificate q gaps) (positive : 0<target)
    (value : (target : Int)=(3 : Int)^s.power*q-s.debt)
    (absorbing : Absorbing s) (ih : IntervalHyp (grades 0 gaps)) : Basin target := by
  rcases absorbing with ⟨power,debt⟩ | ⟨power,debt⟩ | ⟨power,debt,phase⟩
  · rw [power] at value
    simp only [Int.pow_zero,Int.one_mul] at value
    exact odd_source_cap q target gaps cert positive (by omega) ih
  · rw [power] at value
    simp only [Int.pow_one] at value
    exact odd_source_cap q target gaps cert positive (by omega) ih
  · rw [power] at value
    change (target : Int)=9*q-s.debt at value
    exact nine_lattice_return q target gaps cert positive (by omega) (by omega) ih

/-- Whole-word composition with the new return cone. The actual complete
suffix supplies the child, and the original parent grade funds every
recursive query used by the cone. No output certificate is re-ranked. -/
theorem compiled_return_rule (s : Carry) (front tail : List Nat) (r n : Nat)
    (enabled : Enabled s front) (cert : Certificate r (front++tail))
    (target : (n : Int)=(3 : Int)^s.power*r-s.debt)
    (nonempty : front≠[]) (positive : 0<n)
    (absorbing : Absorbing (run s front))
    (ih : IntervalHyp (grades 0 (front++tail))) : Basin n := by
  obtain ⟨u,tailCert,result⟩ := complete_word_transport s front tail r n enabled cert target
  have childIH : IntervalHyp (grades 0 tail) :=
    restrict_hyp (consumed_prefix_rank front tail nonempty) ih
  have child := absorbing_return (run s front) u (orbit (total front) n) tail
    tailCert (orbit_positive _ _ positive) result absorbing childIH
  exact (CollatzSignedCarry.orbit_basin _ _).mp child

/-- The exact signed initialization composes directly with any successful
prefix, independently of the remaining complete source word. -/
theorem positive_nine_compiled_rule (front tail : List Nat) (r : Nat)
    (enabled : Enabled ⟨2,-2⟩ front) (cert : Certificate r (front++tail))
    (nonempty : front≠[]) (absorbing : Absorbing (run ⟨2,-2⟩ front))
    (ih : IntervalHyp (grades 0 (front++tail))) : Basin (9*r+2) := by
  apply compiled_return_rule ⟨2,-2⟩ front tail r (9*r+2) enabled cert ?_
    nonempty (by omega) absorbing ih
  change ((9*r+2 : Nat) : Int)=(3 : Int)^2*r-(-2)
  omega

/-- PR177's entire first-gap-one family recovered through the general
signed compiler and the original common-grade return theorem. -/
theorem positive_nine_first_one (r : Nat) (tail : List Nat)
    (cert : Certificate r (1::tail))
    (ih : IntervalHyp (grades 0 (1::tail))) : Basin (9*r+2) := by
  exact positive_nine_compiled_rule [1] tail r (by decide) cert (by decide) (by decide) ih

/-- PR177's entire first-prefix-two-one family, with arbitrary literal tail. -/
theorem positive_nine_two_one (r : Nat) (tail : List Nat)
    (cert : Certificate r (2::1::tail))
    (ih : IntervalHyp (grades 0 (2::1::tail))) : Basin (9*r+2) := by
  exact positive_nine_compiled_rule [2,1] tail r (by decide) cert (by decide) (by decide) ih

/-- Reconstruct PR177's valuation-one psi conclusion with the unchanged
literal odd certificate, including every possible supplied terminal tail. -/
theorem valuation_one_psi (q : Nat) (gaps : List Nat)
    (cert : Certificate q gaps) (ih : IntervalHyp (grades 1 gaps)) : Basin (4*q-1) := by
  have odd : q%2=1 := witness_odd (certificate_witness cert)
  have drop : Less (grades 0 gaps) (grades 1 gaps) := by
    simpa using even_to_odd_replacement 1 [] gaps (by decide) (by simp)
  have child := negative_nine_return q gaps cert (restrict_hyp drop ih)
  have first : step (4*q-1)=6*q-1 := by unfold step; split <;> omega
  have second : step (6*q-1)=9*q-1 := by unfold step; split <;> omega
  have path : orbit 2 (4*q-1)=9*q-1 := by simp only [orbit,first,second]
  exact (CollatzSignedCarry.orbit_basin 2 (4*q-1)).mp (path ▸ child)

/-- Exact obstruction to declaring the enlarged state tests total: this
actual complete alphabet-four source has no accepted prefix, including
its exhausted word. The displayed target still has its ordinary meaning. -/
theorem cap_four_guard_not_total :
    Certificate 17 [2,3,4] ∧
    (∀ a∈([2,3,4] : List Nat), a≤4) ∧
    Enabled ⟨2,-2⟩ [2,3,4] ∧
    (∀ k : Fin 4, ¬Absorbing (run ⟨2,-2⟩ ([2,3,4].take k.val))) ∧
    run ⟨2,-2⟩ [2,3,4]=⟨6,61⟩ ∧ orbit 9 155=668 := by
  refine ⟨?_,?_,by decide,by decide,by decide,by decide⟩
  · constructor
    · intro a mem
      simp only [List.mem_cons,List.not_mem_nil,or_false] at mem
      omega
    · decide
  · intro a mem
    simp only [List.mem_cons,List.not_mem_nil,or_false] at mem
    omega

end CollatzSignedCarryReturns

#print axioms CollatzSignedCarryReturns.restrict_hyp
#print axioms CollatzSignedCarryReturns.odd_source_cap
#print axioms CollatzSignedCarryReturns.nine_lattice_return
#print axioms CollatzSignedCarryReturns.negative_nine_return
#print axioms CollatzSignedCarryReturns.absorbing_return
#print axioms CollatzSignedCarryReturns.compiled_return_rule
#print axioms CollatzSignedCarryReturns.positive_nine_compiled_rule
#print axioms CollatzSignedCarryReturns.positive_nine_first_one
#print axioms CollatzSignedCarryReturns.positive_nine_two_one
#print axioms CollatzSignedCarryReturns.valuation_one_psi
#print axioms CollatzSignedCarryReturns.cap_four_guard_not_total
