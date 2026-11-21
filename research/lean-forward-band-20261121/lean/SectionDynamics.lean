import ForwardSection

/-! The first positive return to the odd dyadic section. -/

namespace CollatzShell.ForwardSection

private theorem step_positive {n : Nat} (hn : 0<n) : 0<step n := by
  unfold step
  split <;> omega

private theorem visit_exists (n : Nat) (hn : 0<n) : ∃ t, Marked (orbit t n) := by
  obtain ⟨t,_,m⟩ := bounded_visit n hn
  exact ⟨t,m⟩

/-- First visit at or after time zero. -/
def firstVisit (n : Nat) := if hn : 0<n then Nat.find (visit_exists n hn) else 0

theorem firstVisit_spec (n : Nat) (hn : 0<n) : Marked (orbit (firstVisit n) n) := by
  simpa [firstVisit,hn] using Nat.find_spec (visit_exists n hn)

theorem firstVisit_min {n t : Nat} (hn : 0<n) (m : Marked (orbit t n)) : firstVisit n≤t := by
  simpa [firstVisit,hn] using Nat.find_min' (visit_exists n hn) m

theorem firstVisit_bound (n : Nat) (hn : 0<n) : firstVisit n<4*n.sqrt+n.log2 := by
  obtain ⟨t,b,m⟩ := bounded_visit n hn
  exact (firstVisit_min hn m).trans_lt b

/-- Taking an initial step makes this a strictly positive return clock. -/
def returnTime (n : Nat) := firstVisit (step n)+1
def next (n : Nat) := orbit (returnTime n) n

theorem next_marked (n : Nat) (hn : 0<n) : Marked (next n) :=
  firstVisit_spec _ (step_positive hn)

theorem returnTime_min {n t : Nat} (hn : 0<n) (tp : 0<t) (m : Marked (orbit t n)) :
    returnTime n≤t := by
  obtain ⟨i,rfl⟩ := Nat.exists_eq_succ_of_ne_zero tp.ne'
  exact Nat.succ_le_succ (firstVisit_min (step_positive hn) m)

def returns (n : Nat) : Nat → Nat
  | 0 => n
  | k+1 => returns (next n) k

private theorem returns_hit (n k : Nat) : Hits n (returns n k) := by
  induction k generalizing n with
  | zero => exact ⟨0,rfl⟩
  | succ k ih => exact Hits.trans (y:=next n) ⟨returnTime n,rfl⟩ (ih _)

private theorem returns_marked {n : Nat} (m : Marked n) (k : Nat) : Marked (returns n k) := by
  induction k generalizing n with
  | zero => exact m
  | succ k ih => exact ih (next_marked n (by have := m.1; omega))

/-- Every marked endpoint at an ordinary clock appears in the induced dynamics. -/
theorem captures {n : Nat} (hn : 0<n) (t : Nat) (m : Marked (orbit t n)) :
    ∃ k, returns n k=orbit t n := by
  induction t using Nat.strong_induction_on generalizing n with
  | h t ih =>
    by_cases z : t=0
    · exact ⟨0,by subst t; rfl⟩
    have le := returnTime_min hn (Nat.pos_of_ne_zero z) m
    let d := t-returnTime n
    have eq : returnTime n+d=t := by dsimp [d]; omega
    have drop : d<t := by dsimp [d,returnTime]; omega
    have target : orbit d (next n)=orbit t n := by
      change orbit d (orbit (returnTime n) n)=_
      rw [← orbit_add,eq]
    have pos : 0<next n := by have := (next_marked n hn).1; omega
    obtain ⟨k,h⟩ := ih d drop pos (target ▸ m)
    exact ⟨k+1,h.trans target⟩

/-- Global convergence is equivalent to strict descent after some number of complete
    positive returns from every marked start above one. -/
theorem collatz_iff_return_descent : Universal ↔
    ∀ n, Marked n → 1<n → ∃ k, returns n k<n := by
  constructor
  · intro all n _ hn
    obtain ⟨t,one⟩ := all n (by omega)
    have markOne : Marked 1 := by decide
    obtain ⟨k,h⟩ := captures (n:=n) (by omega) t (one ▸ markOne)
    exact ⟨k,by simpa [h,one] using hn⟩
  · intro dec
    apply collatz_iff_marked.mpr
    intro n m
    induction n using Nat.strong_induction_on with
    | h n ih =>
      by_cases hn : 1<n
      · obtain ⟨k,drop⟩ := dec n m hn
        exact (returns_hit n k).trans (ih _ drop (returns_marked m k))
      · have one : n=1 := by have := m.1; omega
        exact ⟨0,one⟩

#print axioms collatz_iff_return_descent

end CollatzShell.ForwardSection
