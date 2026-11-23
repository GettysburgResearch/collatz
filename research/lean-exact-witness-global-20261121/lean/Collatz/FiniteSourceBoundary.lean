/-
Every complete capturing witness reduces to a finite ordinary boundary.
No bound is imposed on its input length, initial even run, or odd gaps.
This proves an exact finite-source optimization interface, not target entry.
-/
import Collatz.JointMinimalCounterexample

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzUnboundedGapReset CollatzJointMinimalCounterexample

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzFiniteSourceBoundary

/-- The last ordinary source state at or above the original capture floor. -/
def Boundary (floor source : Nat) : Prop :=
  floor ≤ source ∧ source < 2 * floor ∧ source % 2 = 0 ∧
    ∀ k, orbit source (k+1) < floor

private theorem hit_orbit (source clock : Nat) (hit : Hits source clock) :
    orbit source clock = 1 := by
  induction clock generalizing source with
  | zero => exact hit
  | succ clock ih => exact ih (shortcut source) hit

private theorem after_hit (source clock k : Nat) (hit : Hits source clock)
    (later : clock ≤ k) : orbit source k ≤ 2 := by
  obtain ⟨j,rfl⟩ := Nat.exists_eq_add_of_le later
  rw [orbit_add,hit_orbit source clock hit]
  have small := CollatzSourceOrbitProgress.cycle_stays_small 1 j (Or.inl rfl)
  omega

private theorem last_large (f : Nat → Nat) (floor N : Nat)
    (initial : floor ≤ f 0) (eventual : ∀ k, N ≤ k → f k < floor) :
    ∃ j, j < N ∧ floor ≤ f j ∧ ∀ k, j < k → f k < floor := by
  induction N with
  | zero => have h := eventual 0 (by omega); omega
  | succ N ih =>
    by_cases high : floor ≤ f N
    · exact ⟨N,by omega,high,by intro k hk; exact eventual k (by omega)⟩
    · have earlier : ∀ k, N ≤ k → f k < floor := by
        intro k hk
        by_cases eq : k=N
        · subst k; omega
        · exact eventual k (by omega)
      obtain ⟨j,small,large,last⟩ := ih earlier
      exact ⟨j,by omega,large,last⟩

/-- Last-exit selection from an actual finite hitting witness. Later visits
to the terminal cycle remain below the floor, so no time cutoff is hidden. -/
theorem last_exit (source floor clock : Nat) (floorLarge : 2 < floor)
    (captures : floor ≤ source) (hit : Hits source clock) :
    ∃ j, j < clock ∧ Boundary floor (orbit source j) := by
  have eventual : ∀ k, clock ≤ k → orbit source k < floor := by
    intro k later
    have small := after_hit source clock k hit later
    omega
  obtain ⟨j,jsmall,high,last⟩ :=
    last_large (orbit source) floor clock captures eventual
  have future : ∀ k, orbit (orbit source j) (k+1) < floor := by
    intro k
    rw [←orbit_add]
    exact last _ (by omega)
  have next := future 0
  change shortcut (orbit source j) < floor at next
  have even : orbit source j % 2 = 0 := by
    unfold shortcut at next
    split at next <;> omega
  have double : orbit source j = 2 * shortcut (orbit source j) := by
    unfold shortcut
    split <;> omega
  refine ⟨j,jsmall,high,?_,even,future⟩
  omega

/-- The supplied witness itself pays the trimming. The output grade is
identical only when no ordinary source clock was consumed. -/
theorem trim_certificate (source floor e : Nat) (gaps : List Nat)
    (floorLarge : 2 < floor) (captures : floor ≤ source)
    (cert : PoweredCertificate source e gaps) :
    ∃ child f tail, Boundary floor child ∧ PoweredCertificate child f tail ∧
      ((child=source ∧ f=e ∧ tail=gaps) ∨
        Less (grades f tail) (grades e gaps)) := by
  obtain ⟨clock,hit⟩ := powered_certificate_basin cert
  obtain ⟨j,_,boundary⟩ := last_exit source floor clock floorLarge captures hit
  by_cases zero : j=0
  · subst j
    exact ⟨source,e,gaps,boundary,cert,Or.inl ⟨rfl,rfl,rfl⟩⟩
  · have outside : 2 < orbit source j := by have high := boundary.1; omega
    obtain ⟨f,tail,child,drop⟩ :=
      CollatzSourceOrbitProgress.advance_certificate source j e gaps cert outside
    refine ⟨orbit source j,f,tail,boundary,child,Or.inr ?_⟩
    rcases drop with absent | strict
    · exact False.elim (zero absent)
    · exact strict

/-- This geometry follows from source-grade minimality alone. No bad target,
least-target hypothesis, alphabet restriction, or target orbit is assumed. -/
theorem minimum_on_boundary (floor source e : Nat) (gaps : List Nat)
    (floorLarge : 2 < floor) (captures : floor ≤ source)
    (cert : PoweredCertificate source e gaps)
    (minimum : SourceMinimal (2*floor+1) source e gaps) :
    Boundary floor source := by
  obtain ⟨child,f,tail,boundary,childCert,relation⟩ :=
    trim_certificate source floor e gaps floorLarge captures cert
  rcases relation with ⟨rfl,_,_⟩ | drop
  · exact boundary
  · exact False.elim (minimum child f tail childCert
      ⟨by omega,by have high := boundary.1; omega⟩ drop)

/-- Search for a smaller complete grade can be restricted exactly to the
finite source interval [floor,2*floor), with the actual future below floor.
Certificates remain universally quantified; the written algorithm removes
terminal padding and uses the unique first-hit certificate at each source. -/
theorem boundary_minimum_iff (floor source e : Nat) (gaps : List Nat)
    (floorLarge : 2 < floor) :
    SourceMinimal (2*floor+1) source e gaps ↔
      (∀ child f tail, Boundary floor child → PoweredCertificate child f tail →
        ¬Less (grades f tail) (grades e gaps)) := by
  constructor
  · intro minimum child f tail boundary cert drop
    exact minimum child f tail cert
      ⟨by omega,by have high := boundary.1; omega⟩ drop
  · intro boundaryMinimum child f tail cert active drop
    have captures : floor ≤ child := by have upper := active.2; omega
    obtain ⟨trimmed,g,rest,boundary,trimmedCert,relation⟩ :=
      trim_certificate child floor f tail floorLarge captures cert
    apply boundaryMinimum trimmed g rest boundary trimmedCert
    rcases relation with ⟨_,rfl,rfl⟩ | strict
    · exact drop
    · exact less_trans strict drop

/-- Once the minimum grade is fixed, its maximum-source tie also ranges over
the same finite boundary. A same-grade capture outside it would trim to a
strictly smaller capturing grade, contradicting the original minimum. -/
theorem boundary_maximum_iff (floor source e : Nat) (gaps : List Nat)
    (floorLarge : 2 < floor)
    (minimum : SourceMinimal (2*floor+1) source e gaps) :
    SourceMaximal (2*floor+1) source e gaps ↔
      (∀ child f tail, Boundary floor child → PoweredCertificate child f tail →
        (grades f tail).Perm (grades e gaps) → child ≤ source) := by
  constructor
  · intro maximum child f tail boundary cert same
    exact maximum child f tail cert
      ⟨by omega,by have high := boundary.1; omega⟩ same
  · intro maximum child f tail cert active same
    have childMinimum : SourceMinimal (2*floor+1) child f tail := by
      intro other g rest otherCert otherActive drop
      exact minimum other g rest otherCert otherActive
        ((less_perm (List.Perm.refl _) same).mp drop)
    have boundary := minimum_on_boundary floor child f tail floorLarge
      (by have upper := active.2; omega) cert childMinimum
    exact maximum child f tail boundary cert same

end CollatzFiniteSourceBoundary
