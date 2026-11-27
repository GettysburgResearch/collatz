import OldHeadFirstFailure
import PermanentSafeOrdinary

/-! Adapter to the exact executable state and valuation of PR200, frozen at
eb91086951b66923787f696801f0c3ca52a0077d. See OLD_HEAD_FIRST_FAILURE.md. -/
set_option autoImplicit false
set_option warningAsError true
namespace OldHeadOrdinary

open OldHeadBudget

def actual (m : ℕ) (odd : m%2=1) : Orbit where
  x := PermanentSafeOrdinary.state m
  e t := PermanentSafeOrdinary.valuation (PermanentSafeOrdinary.state m t)
  odd := PermanentSafeOrdinary.state_odd m odd
  edge i := PermanentSafeOrdinary.exact_step (PermanentSafeOrdinary.state m i)

theorem same_clock (m : ℕ) (odd : m%2=1) (n : ℕ) :
    OldHeadBudget.clock (actual m odd) n=PermanentSafeOrdinary.clock m n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [OldHeadBudget.clock,Finset.sum_range_succ] at ih ⊢
    change _ = PermanentSafeOrdinary.clock m n+PermanentSafeOrdinary.valuation (PermanentSafeOrdinary.state m n)
    rw [←ih]
    rfl

/-- Literal terminal-clock test for every eligible positive odd principal or
nonprincipal source, using the original ordinary 2-adic valuation at each date. -/
theorem actual_terminal_test (m n h : ℕ) (odd : m%2=1) (hn : 0<n)
    (small : Cleared m n) (alive : ∀ j≤n, 4*PermanentSafeOrdinary.clock m j≤7*j) :
    (∃ j≤h, 7*j<4*PermanentSafeOrdinary.clock m j) ↔ 7*h<4*PermanentSafeOrdinary.clock m h := by
  have old (j : ℕ) (hj : j≤n) : ¬Failed (actual m odd) j := by
    unfold Failed
    rw [same_clock]
    exact Nat.not_lt_of_le (alive j hj)
  have ht := terminal_test (actual m odd) n h hn small old
  simpa only [Failed,same_clock] using ht

theorem actual_first_failure_entry (m n t : ℕ) (odd : m%2=1) (hn : 0<n)
    (nt : n≤t) (small : Cleared m n) (fail : 7*t<4*PermanentSafeOrdinary.clock m t)
    (before : ∀ j<t, 4*PermanentSafeOrdinary.clock m j≤7*j) :
    ∃ i<t, PermanentSafeOrdinary.state m i=1 ∧ t+4*PermanentSafeOrdinary.clock m i=8*i+1 ∧ t%4=1 := by
  have first : FirstFailure (actual m odd) t := by
    refine ⟨?_,?_⟩
    · simpa only [Failed,same_clock] using fail
    · intro j hj
      simpa only [Failed,same_clock,not_lt] using before j hj
  obtain ⟨i,hi,one⟩ := first_failure_after_clearance (actual m odd) n t hn nt small first
  have eq := first_failure_clock _ first hi one
  rw [same_clock] at eq
  exact ⟨i,hi,one,eq⟩

#print axioms same_clock
#print axioms actual_terminal_test
#print axioms actual_first_failure_entry
end OldHeadOrdinary
