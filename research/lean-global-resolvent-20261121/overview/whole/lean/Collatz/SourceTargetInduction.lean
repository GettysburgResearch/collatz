import Collatz.AffineDispatcher

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzSourceTargetInduction

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzBoundedGapCofinal CollatzGapComparison
open CollatzTerminalCarry (iterate iterate_basin iterate_positive)

/-- Inner induction at exactly the same powered source and complete source
certificate. Its target decreases; the source grade need not decrease. -/
def SameSourceHyp (source target : Nat) : Prop :=
  ∀ child, Interval source child → child<target → Basin child

/-- A local solver may use both lower complete-source grades and smaller
targets at the same fixed source. Successful coverage remains a hypothesis. -/
def JointComplete : Prop :=
  ∀ source target e word, Interval source target →
    PoweredCertificate source e word → Hyp Interval (grades e word) →
    SameSourceHyp source target → Basin target

/-- The ordinary target interval is downward closed among positive values. -/
theorem interval_downward {source target child : Nat}
    (active : Interval source target) (positive : 0<child) (smaller : child≤target) :
    Interval source child := ⟨positive,by obtain ⟨_,bound⟩ := active; omega⟩

/-- Inner strong induction discharges the extra same-source hypothesis,
yielding the existing PR177 complete-source induction interface unchanged. -/
theorem complete_of_joint (solver : JointComplete) : Complete Interval := by
  intro source target e word active cert lower
  have all : ∀ n, Interval source n → Basin n := by
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro current
      apply solver source n e word current cert lower
      intro child childActive smaller
      exact ih child smaller childActive
  exact all target active

/-- Both inductions close every activated source/target comparison. The
source's actual basin certificate is supplied by the existing outer kernel. -/
theorem close_of_joint (solver : JointComplete) {source target : Nat}
    (active : Interval source target) : Claim source target :=
  CollatzGapComparison.close (complete_of_joint solver) active

/-- Full ordinary convergence follows conditionally from total mixed
coverage. No such universal solver is asserted by this module. -/
theorem collatz_of_joint (solver : JointComplete) : ∀n, 0<n → Basin n := by
  apply collatz_of_complete_psi (complete_of_joint solver)
  intro source positive
  exact ⟨by omega,by omega⟩

/-- Direct ordinary descent preserves the exact current source certificate.
The comparison is with this query's original target, not a later larger
endpoint at which a different carry description happens to be available. -/
theorem same_source_descent {source target clock : Nat}
    (active : Interval source target) (smaller : iterate target clock<target)
    (ih : SameSourceHyp source target) : Basin target := by
  have positive := iterate_positive active.1 clock
  have child := ih (iterate target clock)
    (interval_downward active positive (Nat.le_of_lt smaller)) smaller
  exact (iterate_basin target clock).mp child

/-- An independently timed merger with any smaller positive partner is
admissible at the same source grade. The partner need not lie in the
maximal lower-grade literal-cut envelope. -/
theorem same_source_merger {source target partner L R : Nat}
    (active : Interval source target) (positive : 0<partner) (smaller : partner<target)
    (meeting : iterate partner L=iterate target R)
    (ih : SameSourceHyp source target) : Basin target := by
  have child := ih partner (interval_downward active positive (Nat.le_of_lt smaller)) smaller
  have endpoint := (iterate_basin partner L).mpr child
  rw [meeting] at endpoint
  exact (iterate_basin target R).mp endpoint

/-- Concrete local alternatives in one induction. A paid child retains an
explicit complete certificate and strict old-grade comparison. A smaller
partner retains the current source; known terminal cases are permitted. -/
inductive MixedWitness (source target : Nat) (old : List Nat) : Prop where
  | known : Basin target → MixedWitness source target old
  | smaller {partner L R : Nat} : 0<partner → partner<target →
      iterate partner L=iterate target R → MixedWitness source target old
  | paid {childSource childTarget e : Nat} {word : List Nat} :
      Interval childSource childTarget → PoweredCertificate childSource e word →
      Less (grades e word) old → (Basin childTarget → Basin target) →
      MixedWitness source target old

/-- The ordinary descent class singled out by PR183's carry-compression
bridge. This identity is credited to that packet, not claimed as a new ray. -/
theorem residue23_descent (a : Nat) : iterate (32*a+23) 5=27*a+20 := by
  have h0 : shortcut (32*a+23)=48*a+35 := by unfold shortcut; split <;> omega
  have h1 : shortcut (48*a+35)=72*a+53 := by unfold shortcut; split <;> omega
  have h2 : shortcut (72*a+53)=108*a+80 := by unfold shortcut; split <;> omega
  have h3 : shortcut (108*a+80)=54*a+40 := by unfold shortcut; split <;> omega
  have h4 : shortcut (54*a+40)=27*a+20 := by unfold shortcut; split <;> omega
  simp only [iterate,h0,h1,h2,h3,h4]

/-- The credited descent class is a valid branch of the SAME combined
source-grade/target induction, for every supplied source and old grade.
Its sound application still requires that target 32a+23 is currently active. -/
theorem residue23_mixed_witness (source a : Nat) (old : List Nat) :
    MixedWitness source (32*a+23) old := by
  apply MixedWitness.smaller (partner:=27*a+20) (L:=0) (R:=5) (by omega) (by omega)
  simpa only [iterate] using (residue23_descent a).symm

/-- Every PR183 debt-growth target in this residue family is captured by
halving an ALREADY SUPPLIED source 8r. The complete odd word is retained and
the even exponent drops 3 to 2. No padding is obtained for free from a query
whose original source was r with initial exponent zero. -/
theorem residue13_carry_paid_capture (a : Nat) (word : List Nat)
    (cert : Certificate (32*a+13) word)
    (lower : Hyp Interval (grades 3 word)) : Basin (9*(32*a+13)+2) := by
  have form : 9*(32*a+13)+2=32*(9*a+3)+23 := by omega
  have endpoint : iterate (9*(32*a+13)+2) 5=243*a+101 := by
    rw [form,residue23_descent]
    omega
  have child := lower (4*(32*a+13)) (243*a+101) 2 word
    ⟨by omega,by omega⟩ ⟨32*a+13,rfl,cert⟩ (grades_even_decrease 2 word)
  apply (iterate_basin (9*(32*a+13)+2) 5).mp
  simpa only [endpoint] using child

theorem mixed_witness_sound {source target : Nat} {old : List Nat}
    (witness : MixedWitness source target old) (active : Interval source target)
    (lower : Hyp Interval old) (inner : SameSourceHyp source target) : Basin target := by
  cases witness with
  | known proof => exact proof
  | smaller positive smaller meeting => exact same_source_merger active positive smaller meeting inner
  | paid childActive cert decrease transport =>
    exact transport (lower _ _ _ _ childActive cert decrease)

/-- This is the remaining coverage obligation for the combined program.
The obligation is universal in source, target, initial run, and complete word. -/
def MixedCover : Prop :=
  ∀ source target e word, Interval source target → PoweredCertificate source e word →
    MixedWitness source target (grades e word)

theorem joint_of_mixed_cover (cover : MixedCover) : JointComplete := by
  intro source target e word active cert lower inner
  exact mixed_witness_sound (cover source target e word active cert) active lower inner

theorem collatz_of_mixed_cover (cover : MixedCover) : ∀n, 0<n → Basin n :=
  collatz_of_joint (joint_of_mixed_cover cover)

end CollatzSourceTargetInduction
