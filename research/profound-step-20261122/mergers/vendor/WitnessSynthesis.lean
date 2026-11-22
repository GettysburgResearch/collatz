import WitnessGlobal

/-!
Whole-source witness transport for physical dyadic word erasure.

The graded-count relation and initial-run convention below are the exact
formulas of PR177 at a0a0d76f91b4e3846c1b1f0706cad56cb6098317,
Collatz/GapMultiset.lean. We prove the required decrease directly and do not
import that branch's full induction development.

The physical prefix-erasure calculation extends PR185 at
6d2765ef462fb575c49d4133b54286be7ffe68ec, HalfSourceMerge.lean, to two
independent endpoint clocks. No total endpoint-diamond cover is assumed.
-/

namespace CollatzShell.WitnessSynthesis

open WitnessGlobal

/-- The highest grade at which multiplicity changes must decrease. This is
the literal relation used by PR177's well-founded source-word induction. -/
def GradeDrop (new old : List Nat) : Prop :=
  ∃ a, new.count a < old.count a ∧
    ∀ b, a < b → new.count b = old.count b

def sourceGrades (evenRun : Nat) (word : List Nat) : List Nat :=
  (if evenRun = 0 then [] else [2*evenRun+1]) ++ word.map (2*·)

/-- A supplied complete ordinary word, with its initial even run separate. -/
def PoweredTrace (source evenRun : Nat) (word : List Nat) : Prop :=
  ∃ q, 0 < q ∧ source = 2^evenRun*q ∧ GapTrace q 1 word

theorem powered_trace_hit {source e : Nat} {word : List Nat}
    (cert : PoweredTrace source e word) : orbit (e+word.sum) source = 1 := by
  obtain ⟨q,_,rfl,trace⟩ := cert
  rw [orbit_add,orbit_pad]
  exact trace_orbit trace

/-- Only the initial even grade changes; the complete odd word cancels. -/
theorem source_grade_peel (e : Nat) (word : List Nat) :
    GradeDrop (sourceGrades e word) (sourceGrades (e+1) word) := by
  refine ⟨2*(e+1)+1,?_,?_⟩
  · by_cases zero : e=0
    · simp [sourceGrades,zero]
    · simp [sourceGrades,zero]
  · intro b hb
    have old_ne : b ≠ 2*(e+1)+1 := by omega
    have new_ne : b ≠ 2*e+1 := by omega
    by_cases zero : e=0
    · subst e
      have three : 3≠b := by omega
      simp [sourceGrades,three]
    · simp [sourceGrades,zero,Ne.symm old_ne,Ne.symm new_ne]

/-- One physical halving retains the literal supplied odd certificate. -/
theorem peel_powered_source {source e : Nat} {word : List Nat}
    (cert : PoweredTrace source (e+1) word) :
    PoweredTrace (step source) e word ∧ 2*step source=source ∧
      GradeDrop (sourceGrades e word) (sourceGrades (e+1) word) := by
  obtain ⟨q,positive,eq,trace⟩ := cert
  have form : source=2*(2^e*q) := by rw [eq,pow_succ]; ring
  have value : step source=2^e*q := by rw [form,step_double]
  exact ⟨⟨q,positive,value,trace⟩,by rw [value,form],source_grade_peel e word⟩

def Interval (source target : Nat) : Prop := 0<target ∧ target≤2*source+1

/-- This has the same quantifiers as PR177's interval induction hypothesis,
using the physical complete-word representation already present in PR180. -/
def IntervalHyp (old : List Nat) : Prop :=
  ∀ source target e word, Interval source target →
    PoweredTrace source e word → GradeDrop (sourceGrades e word) old → Basin target

/-- Any physical half-size merger is a lower-source-grade interval rule.
The two target clocks are independent, and no new source certificate is chosen. -/
theorem half_size_merger_rule {source target x e a b : Nat} {word : List Nat}
    (cert : PoweredTrace source (e+1) word)
    (active : Interval source target) (positive : 0<x)
    (half : 2*x+1≤target)
    (meeting : orbit a x=orbit b target)
    (ih : IntervalHyp (sourceGrades (e+1) word)) : Basin target := by
  obtain ⟨childCert,twice,drop⟩ := peel_powered_source cert
  have childActive : Interval (step source) x := by
    obtain ⟨_,upper⟩ := active
    exact ⟨positive,by omega⟩
  have child := ih (step source) x e word childActive childCert drop
  have endpoint : Basin (orbit a x) := (basin_at_hit ⟨a,rfl⟩).mp child
  rw [meeting] at endpoint
  exact (basin_at_hit ⟨b,rfl⟩).mpr endpoint

/-- Delete an arbitrary positive number of initial odd steps. The endpoint
clocks need not coincide. The endpoint partner is allowed to be even. -/
theorem erase_prefix_asynchronous (k r leftClock rightClock u : Nat)
    (positiveErase : 0<r) (within : r≤k) (positiveCore : 0<u)
    (positivePartner : 1<2^(k-r)*u)
    (diamond : orbit leftClock (3^(k-r)*u-1)=
      orbit rightClock (3^k*u-1)) :
    let n := 2^k*u-1
    let x := 2^(k-r)*u-1
    0<x ∧ 2^r*(x+1)=n+1 ∧ 2*x+1≤n ∧
      orbit (k-r+leftClock) x=orbit (k+rightClock) n := by
  dsimp only
  have two : 2≤2^r := (show 2=2^1 by rfl) ▸
    Nat.pow_le_pow_right (by decide : 0<2) positiveErase
  have scale : 2^k*u=2^r*(2^(k-r)*u) := by
    rw [← mul_assoc,← pow_add,show r+(k-r)=k by omega]
  have large : 1≤2^k*u := by
    have positive : 0<2^k*u := Nat.mul_pos (by positivity) positiveCore
    omega
  have lower : 2*(2^(k-r)*u)≤2^k*u := by
    rw [scale]
    exact Nat.mul_le_mul_right _ two
  refine ⟨by omega,?_,by omega,?_⟩
  · rw [Nat.sub_add_cancel (by omega : 1≤2^(k-r)*u),
      Nat.sub_add_cancel large]
    exact scale.symm
  · rw [orbit_add,orbit_add,(odd_run (k-r) u positiveCore).1,
      (odd_run k u positiveCore).1]
    exact diamond

/-- The arbitrary-clock erasure enters the existing complete-source order
after exactly one source halving. All source suffix letters are unchanged. -/
theorem erasure_interval_rule (source e k r leftClock rightClock u : Nat)
    (word : List Nat) (cert : PoweredTrace source (e+1) word)
    (active : Interval source (2^k*u-1))
    (positiveErase : 0<r) (within : r≤k) (positiveCore : 0<u)
    (positivePartner : 1<2^(k-r)*u)
    (diamond : orbit leftClock (3^(k-r)*u-1)=
      orbit rightClock (3^k*u-1))
    (ih : IntervalHyp (sourceGrades (e+1) word)) : Basin (2^k*u-1) := by
  obtain ⟨positive,_,half,meeting⟩ :=
    erase_prefix_asynchronous k r leftClock rightClock u
      positiveErase within positiveCore positivePartner diamond
  exact half_size_merger_rule cert active positive half meeting ih

/-- The unsuccessful short-diamond phase leaves this exact unbounded carry.
This identity does not assert convergence of either endpoint. -/
theorem unresolved_endpoint_pair (r : Nat) :
    orbit 2 (4*r)=r ∧ orbit 2 (12*r+2)=9*r+2 := by
  constructor
  · simpa using orbit_pad 2 r
  · have first : step (12*r+2)=6*r+1 := by
      simp [step,show (12*r+2)%2=0 by omega]
      omega
    have second : step (6*r+1)=9*r+2 := by
      simp [step,show (6*r+1)%2≠0 by omega]
      omega
    simp only [orbit,first,second]

private theorem cycle_phases_differ (h : Nat) : orbit h 1≠orbit h 2 := by
  induction h with
  | zero => decide
  | succ h ih =>
    change orbit h 2≠orbit h 1
    exact Ne.symm ih

/-- Synchronous endpoint deletion is not total even on a convergent target.
The asynchronous interface above does not impose this false restriction. -/
theorem seven_has_no_synchronous_endpoint_erasure (h : Nat) :
    orbit h 8≠orbit h 26 ∧ orbit h 2≠orbit h 26 := by
  by_cases small : h<8
  · interval_cases h <;> decide
  · have decomp : h=8+(h-8) := by omega
    rw [decomp,orbit_add,orbit_add,orbit_add]
    change orbit (h-8) 2≠orbit (h-8) 1 ∧ orbit (h-8) 2≠orbit (h-8) 1
    exact ⟨Ne.symm (cycle_phases_differ _),Ne.symm (cycle_phases_differ _)⟩

/-- The formerly excluded example has an actual two-clock endpoint witness. -/
theorem seven_asynchronous_erasure :
    0<3 ∧ 2*(3+1)=7+1 ∧ 2*3+1≤7 ∧ orbit 5 3=orbit 11 7 := by
  have diamond : orbit 3 (3^(3-1)*1-1)=orbit 8 (3^3*1-1) := by decide
  exact erase_prefix_asynchronous 3 1 3 8 1
    (by decide) (by decide) (by decide) (by decide) diamond

#print axioms powered_trace_hit
#print axioms source_grade_peel
#print axioms peel_powered_source
#print axioms half_size_merger_rule
#print axioms erase_prefix_asynchronous
#print axioms erasure_interval_rule
#print axioms unresolved_endpoint_pair
#print axioms seven_has_no_synchronous_endpoint_erasure
#print axioms seven_asynchronous_erasure

end CollatzShell.WitnessSynthesis
