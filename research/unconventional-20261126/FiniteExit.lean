import FinalProposal
import Mathlib.Data.Fintype.Pigeonhole
import Mathlib.Data.Finset.Lattice.Fold

/-! A finite trapping test on the actual positive-integer shortcut map.
Each supplied test terminates. Existence of a successful test for every
positive source remains unproved. No weighted analytic gate estimate is
formalized by this file. -/
namespace FiniteExit

open CoreBranching FinalProposal

def Trapped (X n : ℕ) : Prop := ∀ k : Fin (X+1), run k.val n < X

def trap (X n : ℕ) : Bool := decide (∀ k : Fin (X+1), run k.val n < X)

theorem trap_correct (X n : ℕ) : trap X n = true ↔ Trapped X n := by
  simp only [trap, decide_eq_true_eq, Trapped]

theorem certificate_implies_repeat {X n : ℕ} (h : Trapped X n) :
    ∃ i j : ℕ, i<j ∧ run i n=run j n := by
  let f : Fin (X+1) → Fin X := fun k => ⟨run k.val n, h k⟩
  obtain ⟨a,b,hab,heq⟩ := Fintype.exists_ne_map_eq_of_card_lt f (by simp)
  have hn : a.val ≠ b.val := fun he => hab (Fin.ext he)
  have hv : run a.val n=run b.val n := congrArg Fin.val heq
  rcases lt_or_gt_of_ne hn with hlt | hgt
  · exact ⟨a.val,b.val,hlt,hv⟩
  · exact ⟨b.val,a.val,hgt,hv.symm⟩

theorem repeat_implies_bounded {n i j : ℕ} (hij : i<j)
    (heq : run i n=run j n) : ∃ X : ℕ, ∀ k : ℕ, run k n<X := by
  refine ⟨(Finset.range j).sup (fun k => run k n)+1, ?_⟩
  intro k
  induction k using Nat.strong_induction_on with
  | h k ih =>
      by_cases hkj : k<j
      · have hle : run k n ≤ (Finset.range j).sup (fun t => run t n) :=
          Finset.le_sup (f := fun t : ℕ => run t n) (Finset.mem_range.mpr hkj)
        omega
      · let l := i+(k-j)
        have hl : l<k := by dsimp [l]; omega
        have hk : k=j+(k-j) := by omega
        have hrun : run k n=run l n := by
          calc
            run k n = run (j+(k-j)) n := congrArg (fun t => run t n) hk
            _ = run (k-j) (run j n) := run_add j (k-j) n
            _ = run (k-j) (run i n) := by rw [heq]
            _ = run l n := (run_add i (k-j) n).symm
        rw [hrun]
        exact ih l hl

theorem repeat_iff_finite_certificate (n : ℕ) :
    (∃ i j : ℕ, i<j ∧ run i n=run j n) ↔ ∃ X : ℕ, trap X n=true := by
  constructor
  · rintro ⟨i,j,hij,heq⟩
    obtain ⟨X,hX⟩ := repeat_implies_bounded hij heq
    exact ⟨X,(trap_correct X n).mpr (fun k => hX k.val)⟩
  · rintro ⟨X,hX⟩
    exact certificate_implies_repeat ((trap_correct X n).mp hX)

/-- Open: a successful finite trapping test exists for every positive source. -/
def FiniteTrapping : Prop := ∀ n : ℕ, 0<n → ∃ X : ℕ, trap X n=true

theorem no_escape_iff_finite_trapping : NoEscape ↔ FiniteTrapping := by
  constructor
  · intro h n hn
    exact (repeat_iff_finite_certificate n).mp (h n hn)
  · intro h n hn
    exact (repeat_iff_finite_certificate n).mpr (h n hn)

theorem exact_finite_proposal : Collatz ↔ FiniteTrapping ∧ CycleUnique := by
  rw [exact_final_obligations, no_escape_iff_finite_trapping]

theorem exit_gate_arithmetic {X z : ℕ} (hz : 0<z) (hsmall : z<X)
    (hexit : X≤step z) : step z % 3=2 ∧ 2*step z≤3*X-2 := by
  by_cases h : z%2=0
  · simp only [step,h,ite_true] at hexit
    omega
  · simp only [step,h,ite_false] at hexit ⊢
    omega

#print axioms trap_correct
#print axioms certificate_implies_repeat
#print axioms repeat_implies_bounded
#print axioms repeat_iff_finite_certificate
#print axioms no_escape_iff_finite_trapping
#print axioms exact_finite_proposal
#print axioms exit_gate_arithmetic

end FiniteExit
