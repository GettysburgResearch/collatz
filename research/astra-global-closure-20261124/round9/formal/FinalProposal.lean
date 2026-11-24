import MinimumFailure
import CycleOrder

/-!
An explicit ordinary-basin certificate interface and a new certified arithmetic
progression. The universal cover is an OPEN hypothesis; no proof of it is supplied.
The equivalence below records the exact remaining obligation, not a resolution.
-/

set_option autoImplicit false

namespace Collatz.RoundNine

open Collatz.SourceDeletion Collatz.MinimumFailure

def OrdinaryCollatz : Prop := ∀ n, 0 < n → Good n

def CertifiedSafe (q z : Nat) : Prop :=
  8 * z + 1 < 9 * q ∨ (z % 3 = 0 ∧ z < 3 * q)

/-- Both clocks refer to the actual shortcut map on ordinary natural numbers. -/
structure ReturnCertificate (q : Nat) where
  source : Nat
  positive : 0 < source
  safe : CertifiedSafe q source
  upperClock : Nat
  sourceClock : Nat
  meet : run upperClock (3 * q) = run sourceClock source

theorem safe_good {q z : Nat} (least : LeastDiscordance q)
    (positive : 0 < z) (safe : CertifiedSafe q z) : Good z := by
  rcases safe with cutoff | multiple
  · exact good_cutoff least z positive cutoff
  · exact smaller_multiples_good least z positive multiple.1 multiple.2

theorem certificate_refutes {q : Nat} (least : LeastDiscordance q)
    (certificate : ReturnCertificate q) : False := by
  have sourceGood := safe_good least certificate.positive certificate.safe
  have endpointGood := (good_run certificate.sourceClock certificate.source).mpr sourceGood
  rw [← certificate.meet] at endpointGood
  exact upper_bad least ((good_run certificate.upperClock (3 * q)).mp endpointGood)

/-- OPEN: every actual least discordance admits a certified ordinary return. -/
def CompleteReturnCover : Prop :=
  ∀ q, LeastDiscordance q → Nonempty (ReturnCertificate q)

theorem collatz_of_complete_return_cover (cover : CompleteReturnCover) :
    OrdinaryCollatz := by
  intro n positive
  by_contra bad
  obtain ⟨q, least⟩ := exists_least_discordance ⟨n, positive, bad⟩
  obtain ⟨certificate⟩ := cover q least
  exact certificate_refutes least certificate

/-- This states explicitly that the unproved cover is as strong as Collatz. -/
theorem complete_return_cover_iff_collatz : CompleteReturnCover ↔ OrdinaryCollatz := by
  constructor
  · exact collatz_of_complete_return_cover
  · intro collatz q least
    exact False.elim (upper_bad least (collatz (3 * q) (by have := least.positive; omega)))

theorem critical_run_eq (h n : Nat) : CriticalCycle.run h n = run h n := by
  induction h generalizing n with
  | zero => rfl
  | succ h ih => exact ih (step n)

theorem run_add (h j n : Nat) : run (h + j) n = run j (run h n) := by
  induction h generalizing n with
  | zero => simp only [Nat.zero_add, run]
  | succ h ih =>
    simpa only [Nat.succ_add, run] using ih (step n)

/-- A concrete certificate on every member of the stated ordinary progression. -/
def progressionCertificate (u : Nat) : ReturnCertificate (163815229 + 1377495072 * u) := by
  let z := 383076351 + 3221225472 * u
  let s := 245722843 + 2066242608 * u
  have ancestor := CriticalCycle.small_multiple (1 + 16 * u)
  dsimp only at ancestor
  have hz : 181749759 + 201326592 * (1 + 16 * u) = z := by dsimp [z]; omega
  have hs : 116582680 + 129140163 * (1 + 16 * u) = s := by dsimp [s]; omega
  rw [hz, hs] at ancestor
  have center := CriticalCycle.recentered_meeting (15357677 + 129140163 * u)
  have hs' : 11 + 16 * (15357677 + 129140163 * u) = s := by dsimp [s]; omega
  have hn : 23 + 32 * (15357677 + 129140163 * u) =
      3 * (163815229 + 1377495072 * u) := by omega
  rw [hs', hn] at center
  rw [critical_run_eq, critical_run_eq] at center
  have ancestry : run 26 z = s := by simpa only [critical_run_eq] using ancestor.1
  have joined : run 30 z = run 4 s := by
    rw [show 30 = 26 + 4 by decide, run_add, ancestry]
  refine ⟨z, ancestor.2.1, Or.inr ⟨ancestor.2.2.1, ?_⟩, 5, 30, ?_⟩
  · dsimp [z]
    omega
  · exact center.symm.trans joined.symm

theorem progression_excluded (u : Nat) :
    ¬LeastDiscordance (163815229 + 1377495072 * u) := by
  intro least
  exact certificate_refutes least (progressionCertificate u)

#check collatz_of_complete_return_cover
#check complete_return_cover_iff_collatz
#check progression_excluded

#print axioms safe_good
#print axioms certificate_refutes
#print axioms collatz_of_complete_return_cover
#print axioms complete_return_cover_iff_collatz
#print axioms critical_run_eq
#print axioms run_add
#print axioms progressionCertificate
#print axioms progression_excluded

end Collatz.RoundNine
