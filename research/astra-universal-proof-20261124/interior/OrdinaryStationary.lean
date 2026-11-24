import Std

namespace OrdinaryStationary

def step (x : Nat) := if x % 2 = 0 then x / 2 else (3*x+1)/2

def run : Nat → Nat → Nat
  | 0, x => x
  | t+1, x => run t (step x)

def multiple (x : Nat) : Nat := if x % 3 = 0 then 1 else 0
def root (x : Nat) : Nat := if x % 2 = 1 ∧ x % 3 = 0 then 1 else 0

/-- The count at clocks 0 through t-1 of odd multiples of three. -/
def visits : Nat → Nat → Nat
  | 0, _ => 0
  | t+1, x => root x + visits t (step x)

theorem coboundary (x : Nat) : multiple x = root x + multiple (step x) := by
  unfold multiple root step
  split <;> split <;> split <;> split <;> omega

theorem empirical (t x : Nat) : visits t x + multiple (run t x) = multiple x := by
  induction t generalizing x with
  | zero => simp [visits, run]
  | succ t ih =>
    simp only [run, visits, Nat.add_assoc, ih]
    exact (coboundary x).symm

theorem nonreturn {x : Nat} (h : x % 3 ≠ 0) (t : Nat) : run t x % 3 ≠ 0 := by
  have e := empirical t x
  simp only [multiple, ite_eq_right h] at e
  split at e <;> omega

theorem after_odd {x : Nat} (h : x % 2 = 1) (t : Nat) :
    run (t+1) x % 3 ≠ 0 := by
  apply nonreturn (x := step x)
  simp only [step, ite_eq_right (by omega : ¬x % 2 = 0)]
  omega

/-- Each positive multiple reaches an odd multiple by successive halvings.
    All earlier states are multiples of three and all later states are units. -/
theorem exit {x : Nat} (hp : 0 < x) (hm : x % 3 = 0) :
    ∃ k, (∀ i, i ≤ k → run i x = x / 2^i ∧ run i x % 3 = 0) ∧
      run k x % 2 = 1 ∧ (∀ t, run (k+1+t) x % 3 ≠ 0) := by
  induction x using Nat.strongRecOn with
  | ind x ih =>
    by_cases he : x % 2 = 0
    · have hs : step x = x / 2 := by simp [step, he]
      obtain ⟨k, hb, ho, ha⟩ := ih (x/2) (by omega) (by omega) (by omega)
      refine ⟨k+1, ?_, ?_, ?_⟩
      · intro i hi
        cases i with
        | zero => simp [run, hm]
        | succ j =>
          obtain ⟨hj, h3⟩ := hb j (by omega)
          simp only [run, hs, hj] at *
          exact ⟨by rw [Nat.div_div_eq_div_mul, Nat.pow_succ'], h3⟩
      · simpa [run, hs] using ho
      · intro t
        have eq : k+1+1+t = (k+1+t)+1 := by omega
        simpa only [eq, run, hs] using ha t
    · refine ⟨0, ?_, by simpa [run] using (by omega : x % 2 = 1), ?_⟩
      · intro i hi
        have : i = 0 := by omega
        simp [this, run, hm]
      · intro t
        have eq : 0+1+t = t+1 := by omega
        rw [eq]
        exact after_odd (by omega) t

/-- Starting at a defect root 3q with q odd, every nonempty empirical window
    from clock zero sees precisely one odd multiple of three. -/
theorem visits_from_root {x : Nat} (ho : x % 2 = 1) (hm : x % 3 = 0) (t : Nat) :
    visits (t+1) x = 1 := by
  have e := empirical (t+1) x
  simpa [multiple, after_odd ho t, hm] using e

end OrdinaryStationary
