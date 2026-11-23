/-
Source-witness induction for directed Collatz comparisons.

Both global closing theorems are conditional on complete rule coverage.
The finite searches accompanying this module do not establish that coverage.
The clock and energy orders are separate; no union of their accepted rules is assumed.
-/
import Collatz.DirectedInduction
import Collatz.WitnessEnergy

open CollatzReverseBasin CollatzClosure CollatzDirected
open CollatzWitnessEnergy

namespace CollatzSourceWitness

/-- The listed states precede the endpoint in an ordinary forward orbit. -/
def Trace (s d : Nat) : List Nat → Prop
  | [] => s = d
  | x::xs => x = s ∧ Trace (shortcut s) d xs

theorem trace_basin {s d : Nat} {xs : List Nat} (h : Trace s d xs) :
    Basin s ↔ Basin d := by
  induction xs generalizing s with
  | nil => change s = d at h; subst s; exact Iff.rfl
  | cons x xs ih => exact (basin_step s).symm.trans (ih h.2)

/-- A certified forward prefix can be removed from any supplied witness, provided
it has not already visited the endpoint 1. No least hitting time is assumed. -/
theorem trace_peel {s d clock : Nat} {xs : List Nat}
    (h : Trace s d xs) (notOne : ∀ x ∈ xs, x ≠ 1) (hit : Hits s clock) :
    ∃ tail, clock = xs.length + tail ∧ Hits d tail := by
  induction xs generalizing s clock with
  | nil =>
    change s = d at h
    subst s
    exact ⟨clock,by simp,hit⟩
  | cons x xs ih =>
    obtain ⟨hx,ht⟩ := h
    have hn : s ≠ 1 := by
      have hh := notOne x (by simp)
      omega
    cases clock with
    | zero => exact False.elim (hn hit)
    | succ clock =>
      have nh : ∀ x ∈ xs, x ≠ 1 := fun y hy => notOne y (by simp [hy])
      obtain ⟨tail,he,hk⟩ := ih ht nh hit
      exact ⟨tail,by simp only [List.length_cons]; omega,hk⟩

theorem trace_prepend {s d tail : Nat} {xs : List Nat}
    (h : Trace s d xs) (hit : Hits d tail) : Hits s (xs.length+tail) := by
  induction xs generalizing s with
  | nil => change s = d at h; subst s; simpa using hit
  | cons x xs ih =>
    have hh := ih h.2
    simpa only [List.length_cons, Nat.succ_add, Hits] using hh

/-- A longer removed prefix than inserted prefix strictly decreases the actual
length of the transformed supplied certificate, even if the new value is larger. -/
theorem clock_replacement {parent child join clock : Nat} {old new : List Nat}
    (oldTrace : Trace parent join old) (newTrace : Trace child join new)
    (notOne : ∀ x ∈ old, x ≠ 1) (shorter : new.length < old.length)
    (hit : Hits parent clock) :
    ∃ next, next < clock ∧ Hits child next := by
  obtain ⟨tail,he,hk⟩ := trace_peel oldTrace notOne hit
  exact ⟨new.length+tail,by omega,trace_prepend newTrace hk⟩

/-- Natural-number energy of every ordinary state before the final 1. -/
def witnessEnergy (c n : Nat) : Nat → Nat
  | 0 => 0
  | k+1 => c^n + witnessEnergy c (shortcut n) k

theorem trace_energy {c s d : Nat} {xs : List Nat} (h : Trace s d xs) (tail : Nat) :
    witnessEnergy c s (xs.length+tail) =
      prefixEnergy c xs + witnessEnergy c d tail := by
  induction xs generalizing s with
  | nil => change s = d at h; subst s; simp [prefixEnergy]
  | cons x xs ih =>
    obtain ⟨hx,ht⟩ := h
    subst x
    simp only [List.length_cons,Nat.succ_add,witnessEnergy,prefixEnergy,ih ht]
    omega

/-- Energy compares the entire supplied certificate after an exact prefix
replacement. Its remaining tail cancels; the new certificate may be longer. -/
theorem energy_replacement {c parent child join clock : Nat} {old new : List Nat}
    (oldTrace : Trace parent join old) (newTrace : Trace child join new)
    (notOne : ∀ x ∈ old, x ≠ 1)
    (decrease : prefixEnergy c new < prefixEnergy c old)
    (hit : Hits parent clock) :
    ∃ next, witnessEnergy c child next < witnessEnergy c parent clock ∧ Hits child next := by
  obtain ⟨tail,he,hk⟩ := trace_peel oldTrace notOne hit
  refine ⟨new.length+tail,?_,trace_prepend newTrace hk⟩
  rw [he,trace_energy oldTrace tail,trace_energy newTrace tail]
  omega

def known : Kind → Nat → Nat
  | .basin, _ => 1
  | .forward _, n => n
  | .reverse q, n => q*n

def wanted : Kind → Nat → Nat
  | .basin, n => n
  | .forward q, n => q*n
  | .reverse _, n => n

theorem claim_iff (kind : Kind) (n : Nat) :
    Claim kind n ↔ (Basin (known kind n) → Basin (wanted kind n)) := by
  cases kind with
  | basin => exact ⟨fun h _ => h,fun h => h ⟨0,rfl⟩⟩
  | forward _ => exact Iff.rfl
  | reverse _ => exact Iff.rfl

def ClockHyp (active : Active) (clock : Nat) : Prop :=
  ∀ q u next, 0 < u → active q (oddCore u) → next < clock →
    Hits (known q u) next → Basin (wanted q u)

def ClockComplete (active : Active) : Prop :=
  ∀ kind n clock, 0 < n → active kind (oddCore n) →
    Hits (known kind n) clock → ClockHyp active clock → Basin (wanted kind n)

/-- Every complete source-clock rule family terminates by the supplied witness's
length. There is no bound on the represented integer or output certificate. -/
theorem close_clock {active : Active} (complete : ClockComplete active) :
    ∀ kind n, 0 < n → active kind (oddCore n) → Claim kind n := by
  have all : ∀ clock kind n, 0 < n → active kind (oddCore n) →
      Hits (known kind n) clock → Basin (wanted kind n) := by
    intro clock
    induction clock using Nat.strong_induction_on with
    | h clock ih =>
      intro kind n hn ha hit
      apply complete kind n clock hn ha hit
      intro q u next hu hau hnext hhit
      exact ih next hnext q u hu hau hhit
  intro kind n hn ha
  apply (claim_iff kind n).mpr
  rintro ⟨clock,hit⟩
  exact all clock kind n hn ha hit

/-- A concrete one-query rule consumes a source prefix and transfers the child
result along two ordinary target prefixes meeting at a common endpoint. -/
theorem one_query_clock {active : Active} {kind q : Kind} {n u clock : Nat}
    {sourceJoin targetJoin : Nat} {oldSource newSource oldTarget newTarget : List Nat}
    (sourceOld : Trace (known kind n) sourceJoin oldSource)
    (sourceNew : Trace (known q u) sourceJoin newSource)
    (notOne : ∀ x ∈ oldSource, x ≠ 1)
    (shorter : newSource.length < oldSource.length)
    (targetOld : Trace (wanted kind n) targetJoin oldTarget)
    (targetNew : Trace (wanted q u) targetJoin newTarget)
    (positive : 0 < u) (activated : active q (oddCore u))
    (hit : Hits (known kind n) clock) (ih : ClockHyp active clock) :
    Basin (wanted kind n) := by
  obtain ⟨next,hn,hh⟩ := clock_replacement sourceOld sourceNew notOne shorter hit
  have child := ih q u next positive activated hn hh
  exact (trace_basin targetOld).mpr ((trace_basin targetNew).mp child)

/-- This concludes the original global problem once the source-clock rules cover
all active inputs and include the reverse comparison on odd multiples of nine. -/
theorem collatz_of_clock_complete {active : Active} (h : ClockComplete active)
    (coverage : ∀ n, n % 18 = 9 → active (.reverse 3) n) :
    ∀ n, 0 < n → Basin n := by
  apply deep_reverse_generates ⟨basin_twice,basin_odd,?_⟩
    (show Basin 1 from ⟨0,rfl⟩)
  intro n hn hb
  have ho : n % 2 = 1 := by omega
  have ha := coverage n hn
  rw [← oddCore_of_odd n ho] at ha
  exact close_clock h (.reverse 3) n (by omega) ha hb

/-! Clock and energy are distinct induction orders; rules from the two programs
are never combined without a common decrease proof. -/

def EnergyHyp (c : Nat) (active : Active) (energy : Nat) : Prop :=
  ∀ q u next, 0 < u → active q (oddCore u) →
    witnessEnergy c (known q u) next < energy →
    Hits (known q u) next → Basin (wanted q u)

def EnergyComplete (c : Nat) (active : Active) : Prop :=
  ∀ kind n clock, 0 < n → active kind (oddCore n) →
    Hits (known kind n) clock →
    EnergyHyp c active (witnessEnergy c (known kind n) clock) → Basin (wanted kind n)

theorem close_energy {c : Nat} {active : Active} (complete : EnergyComplete c active) :
    ∀ kind n, 0 < n → active kind (oddCore n) → Claim kind n := by
  have all : ∀ energy kind n clock, witnessEnergy c (known kind n) clock = energy →
      0 < n → active kind (oddCore n) → Hits (known kind n) clock → Basin (wanted kind n) := by
    intro energy
    induction energy using Nat.strong_induction_on with
    | h energy ih =>
      intro kind n clock he hn ha hit
      apply complete kind n clock hn ha hit
      intro q u next hu hau hnext hhit
      exact ih _ (by omega) q u next rfl hu hau hhit
  intro kind n hn ha
  apply (claim_iff kind n).mpr
  rintro ⟨clock,hit⟩
  exact all _ kind n clock rfl hn ha hit

theorem one_query_energy {c : Nat} {active : Active} {kind q : Kind} {n u clock : Nat}
    {sourceJoin targetJoin : Nat} {oldSource newSource oldTarget newTarget : List Nat}
    (sourceOld : Trace (known kind n) sourceJoin oldSource)
    (sourceNew : Trace (known q u) sourceJoin newSource)
    (notOne : ∀ x ∈ oldSource, x ≠ 1)
    (decrease : prefixEnergy c newSource < prefixEnergy c oldSource)
    (targetOld : Trace (wanted kind n) targetJoin oldTarget)
    (targetNew : Trace (wanted q u) targetJoin newTarget)
    (positive : 0 < u) (activated : active q (oddCore u))
    (hit : Hits (known kind n) clock)
    (ih : EnergyHyp c active (witnessEnergy c (known kind n) clock)) :
    Basin (wanted kind n) := by
  obtain ⟨next,hn,hh⟩ := energy_replacement sourceOld sourceNew notOne decrease hit
  have child := ih q u next positive activated hn hh
  exact (trace_basin targetOld).mpr ((trace_basin targetNew).mp child)

theorem collatz_of_energy_complete {c : Nat} {active : Active}
    (h : EnergyComplete c active)
    (coverage : ∀ n, n % 18 = 9 → active (.reverse 3) n) :
    ∀ n, 0 < n → Basin n := by
  apply deep_reverse_generates ⟨basin_twice,basin_odd,?_⟩
    (show Basin 1 from ⟨0,rfl⟩)
  intro n hn hb
  have ho : n % 2 = 1 := by omega
  have ha := coverage n hn
  rw [← oddCore_of_odd n ho] at ha
  exact close_energy h (.reverse 3) n (by omega) ha hb

end CollatzSourceWitness
