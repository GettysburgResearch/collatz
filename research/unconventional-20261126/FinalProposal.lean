import CoreBranching

/-! The exact final target and the two still-open mathematical obligations.
NoEscape and CycleUnique below are definitions of propositions, not axioms
and not proved claims. The final theorem explicitly takes both as hypotheses.
The analytic research packet proposes ways to approach them; it does not
discharge either universal hypothesis. -/
namespace FinalProposal

open CoreBranching

def ReachesOne (n : ℕ) : Prop := ∃ k : ℕ, run k n=1

def Collatz : Prop := ∀ n : ℕ, 0<n → ReachesOne n

/-- Some actual native state repeats, with one fixed positive source. -/
def NoEscape : Prop := ∀ n : ℕ, 0<n →
  ∃ i j : ℕ, i<j ∧ run i n=run j n

/-- Every actual positive periodic point is in the basin of 1. -/
def CycleUnique : Prop := ∀ n p : ℕ, 0<n → 0<p → run p n=n → ReachesOne n

theorem step_positive (n : ℕ) (hn : 0<n) : 0<step n := by
  unfold step
  split <;> omega

theorem run_positive (k n : ℕ) (hn : 0<n) : 0<run k n := by
  induction k generalizing n with
  | zero => exact hn
  | succ k ih => exact ih (step n) (step_positive n hn)

theorem convergence_from_two_obligations (hescape : NoEscape)
    (hcycles : CycleUnique) : Collatz := by
  intro n hn
  obtain ⟨i,j,hij,heq⟩ := hescape n hn
  have hp : 0<j-i := Nat.sub_pos_of_lt hij
  have hcycle : run (j-i) (run i n)=run i n := by
    rw [← run_add]
    have hi : i+(j-i)=j := Nat.add_sub_of_le hij.le
    rw [hi, ← heq]
  obtain ⟨k,hk⟩ := hcycles (run i n) (j-i) (run_positive i n hn) hp hcycle
  exact ⟨i+k, by rw [run_add, hk]⟩

theorem convergence_implies_no_escape (hc : Collatz) : NoEscape := by
  intro n hn
  obtain ⟨k,hk⟩ := hc n hn
  refine ⟨k,k+2,by omega,?_⟩
  rw [run_add, hk]
  decide

theorem convergence_implies_cycle_unique (hc : Collatz) : CycleUnique := by
  intro n _ hn _ _
  exact hc n hn

theorem exact_final_obligations : Collatz ↔ NoEscape ∧ CycleUnique := by
  constructor
  · intro hc
    exact ⟨convergence_implies_no_escape hc, convergence_implies_cycle_unique hc⟩
  · rintro ⟨he,hc⟩
    exact convergence_from_two_obligations he hc

#print axioms step_positive
#print axioms run_positive
#print axioms convergence_from_two_obligations
#print axioms convergence_implies_no_escape
#print axioms convergence_implies_cycle_unique
#print axioms exact_final_obligations

end FinalProposal
