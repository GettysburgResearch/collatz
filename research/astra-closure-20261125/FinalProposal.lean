import UniversalProposal
import TowerDeadline
import NineteenMerger
import PeriodicColor

set_option autoImplicit false

/-!
The final proof interface for this pass. It is intentionally conditional:
`SourceClosure` is OPEN, not an axiom or a theorem supplied by this packet.
The new clock, word and rational-cycle results do not prove it.

This module specializes the resident certificate checker to the actual least
bad multiple of three. It also records why replacing a source-dependent
certificate by a single fixed two-arm deadline is invalid.
-/
namespace FinalProposal
open UniversalProposal

/-- The actual least bad triple, with every smaller positive triple good. -/
def FirstFailure (q : Nat) : Prop :=
  1 < q ∧ ¬ Converges (3*q) ∧
    ∀ v, 0 < v → v < q → Converges (3*v)

/-- OPEN. A finite, checked merger for the supplied least bad source.
    The smaller source and both clocks may depend on that source. -/
def SourceClosure : Prop :=
  ∀ q, FirstFailure q → ∃ c : Certificate, check q c = true

/-- Fully checked implication, not a proof of its explicit premise. -/
theorem collatz_of_source_closure (closure : SourceClosure) : Collatz := by
  have triples : ∀ q, 0 < q → Converges (3*q) := by
    intro q
    induction q using Nat.strongRecOn with
    | ind q ih =>
      intro hq
      by_cases hgood : Converges (3*q)
      · exact hgood
      · have hne : q ≠ 1 := by
          intro eq
          subst q
          exact hgood converges_three
        have first : FirstFailure q := ⟨by omega, hgood, fun v hv hlt => ih v hlt hv⟩
        obtain ⟨c, hc⟩ := closure q first
        obtain ⟨hv, hlt, hm⟩ := check_sound q c hc
        exact converges_of_meets hm (ih c.smaller hlt hv)
  intro n hn
  obtain ⟨q, k, hq, _, reaches⟩ := multiple_ancestor n hn
  rw [← reaches]
  exact (converges_run k (3*q)).mpr (triples q hq)

/-- The open premise has exactly the strength claimed in the README. -/
theorem source_closure_iff_collatz : SourceClosure ↔ Collatz := by
  constructor
  · exact collatz_of_source_closure
  · intro full q first
    exact False.elim (first.2.1 (full (3*q) (by have := first.1; omega)))

/-- Final Lean proposal. No selector or proof of this coverage is supplied. -/
theorem final_lean_proposal (selector : Nat → Certificate)
    (coverage : ∀ q, FirstFailure q → check q (selector q) = true) :
    ∀ n, 0 < n → ∃ k, run k n = 1 := by
  apply collatz_of_source_closure
  intro q hq
  exact ⟨selector q, coverage q hq⟩

private theorem merger_run_eq (k n : Nat) :
    NineteenMerger.run k n = run k n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    change NineteenMerger.run k (step n) = run k (step n)
    exact ih (step n)

/-- The new whole residue certificate excludes an actual least bad triple
    whenever that same bad component contains the supplied site s.
    The basin hypothesis is retained; finite rational guards do not imply it. -/
theorem exclude_nineteen_residue (q s : Nat) (first : FirstFailure q)
    (scale : 3*q = 2*s+1) (same_component : Meets (3*q) s)
    (odd : s % 2 = 1) (residue : s % 1162261467 = 187605073) : False := by
  obtain ⟨y, positive, multiple, smaller, hit⟩ :=
    NineteenMerger.whole_residue odd residue
  obtain ⟨v, y_eq⟩ := multiple
  have v_bounds : 0 < v ∧ v < q := by
    clear first same_component odd residue hit
    omega
  have y_good : Converges y := by
    rw [y_eq]
    exact first.2.2 v v_bounds.1 v_bounds.2
  have hit' : run 30 y = step s := by
    rw [← merger_run_eq 30 y]
    exact hit
  have next_good : Converges (step s) := by
    rw [← hit']
    exact (converges_run 30 y).mpr y_good
  have s_good : Converges s := (converges_step s).mp next_good
  exact first.2.1 (converges_of_meets same_component s_good)

/-- Even the pure-power rank-one slice has no uniform two-arm deadline.
    This is an ordinary finite-clock theorem, not a bad-orbit assertion. -/
theorem no_uniform_tower_deadline :
    ¬ ∃ H : Nat, ∀ r : Nat, 0 < r → r % 3 = 1 →
      ∃ s i j : Nat, s < r ∧ i ≤ H ∧ j ≤ H ∧
        TowerDeadline.orbit i (3^r) = TowerDeadline.orbit j (3^s) := by
  rintro ⟨H, covers⟩
  obtain ⟨r, large, residue, avoids⟩ := TowerDeadline.cofinal_deadline H 1
  obtain ⟨s, i, j, smaller, hi, hj, same⟩ := covers r (by omega) residue
  exact avoids s i j smaller hi hj same

/-- The arithmetic consumer of the written Fourier criterion. The missing
    analytic bound has not been asserted: eventual periodicity of the actual
    across-start convergence predicate remains an explicit premise. -/
theorem collatz_iff_eventually_periodic_convergence : Collatz ↔
    ∃ d N : Nat, 0 < d ∧ ∀ n, N ≤ n →
      (Converges (n+d) ↔ Converges n) := by
  constructor
  · intro full
    exact ⟨1, 1, by omega, fun n hn => ⟨fun _ => full n (by omega),
      fun _ => full (n+1) (by omega)⟩⟩
  · intro eventual
    have double : ∀ n, Converges (2*n) = Converges n := by
      intro n
      have hs : step (2*n) = n := by unfold step; split <;> omega
      exact propext (by simpa only [hs] using (converges_step (2*n)).symm)
    have odd : ∀ n, Converges (2*n+1) = Converges (3*n+2) := by
      intro n
      have hs : step (2*n+1) = 3*n+2 := by unfold step; split <;> omega
      exact propext (by simpa only [hs] using (converges_step (2*n+1)).symm)
    obtain ⟨d, N, hd, tail⟩ := eventual
    have same := PeriodicColor.eventually_periodic_invariant Converges double odd
      ⟨d, N, hd, fun n hn => propext (tail n hn)⟩
    intro n hn
    rw [same n hn]
    exact converges_one

#print axioms collatz_of_source_closure
#print axioms source_closure_iff_collatz
#print axioms final_lean_proposal
#print axioms exclude_nineteen_residue
#print axioms no_uniform_tower_deadline
#print axioms collatz_iff_eventually_periodic_convergence
end FinalProposal
