import CollatzGlobal.AdaptiveDescent

/-!
An exact obstruction to combining inverse balanced returns with last-return
normalization. The two operations return a finite residual certificate to
itself. This concerns arbitrary ordinary paths and arbitrary supplied clocks,
not a bounded search or an assumption of eventual return.
-/

namespace CollatzGlobal

/-- Once a balanced return has occurred, later balanced returns are precisely
the balanced returns of its ordinary endpoint. -/
theorem balanced_five_suffix_iff {n s t : Nat} (hs : BalancedFive n s) :
    BalancedFive n (s+t) ↔ BalancedFive (orbit n s) t := by
  constructor
  · intro h
    constructor
    · have hc := h.1
      rw [oddCount_add, oddCount_add, hs.1, hs.2] at hc
      exact Nat.add_left_cancel hc
    · have he := h.2
      rw [orbit_add, orbit_add, hs.2] at he
      exact he
  · exact balanced_five_append hs

/-- An incoming balanced word ending at a finite residual is the last return
in the extended certificate. No earlier returns need to be classified. -/
theorem lastReturn_of_residual_endpoint {n s d : Nat}
    (hs : BalancedFive n s) (hr : FiniteResidual (orbit n s) d) :
    lastReturn n (s+d) = s := by
  have hlo := lastReturn_maximal n (s+d) s (by omega) hs
  have hhi := lastReturn_le n (s+d)
  have hb := lastReturn_balanced n (s+d)
  by_cases he : lastReturn n (s+d) = s
  · exact he
  · have ht : 0 < lastReturn n (s+d)-s := by omega
    have hd : lastReturn n (s+d)-s ≤ d := by omega
    have eq : s+(lastReturn n (s+d)-s) = lastReturn n (s+d) := by omega
    have ha : BalancedFive n (s+(lastReturn n (s+d)-s)) := by rwa [eq]
    have suffix := (balanced_five_suffix_iff hs).mp ha
    exact False.elim (hr _ ht hd suffix)

/-- Last-return normalization retracts every balanced inverse extension of a
finite residual to the exact same source and remaining certificate clock. -/
theorem normalize_inverse_extension {n s d : Nat}
    (hs : BalancedFive n s) (hr : FiniteResidual (orbit n s) d) :
    residualSource n (s+d) = orbit n s ∧ residualClock n (s+d) = d := by
  have last := lastReturn_of_residual_endpoint hs hr
  constructor
  · simp only [residualSource, last]
  · simp only [residualClock, last]
    omega

/-- Therefore no natural-valued rank can strictly decrease on both the
inverse extension and its subsequent complete normalization. -/
theorem no_rank_decrease_both_ways {n s d : Nat}
    (hs : BalancedFive n s) (hr : FiniteResidual (orbit n s) d)
    (rank : Nat → Nat → Nat) :
    ¬ (rank n (s+d) < rank (orbit n s) d ∧
       rank (residualSource n (s+d)) (residualClock n (s+d)) < rank n (s+d)) := by
  obtain ⟨source, clock⟩ := normalize_inverse_extension hs hr
  rw [source, clock]
  omega

/-- A well-founded relation cannot contain a directed two-cycle. -/
theorem wellFounded_no_two_cycle {α : Sort u} {r : α → α → Prop}
    (wf : WellFounded r) (a b : α) : ¬ (r b a ∧ r a b) := by
  have stop : ∀ x, ∀ y, r y x → r x y → False := by
    intro x
    induction x using wf.induction with
    | h x ih =>
      intro y hy hx
      exact ih y hy x hx hy
  intro h
  exact stop a b h.1 h.2

/-- The obstruction holds for every well-founded ranking relation, including
ordinal or lexicographic ranks, on the source/clock certificate state. -/
theorem no_wellFounded_rank_both_ways {α : Sort u} {r : α → α → Prop}
    (wf : WellFounded r) {n s d : Nat}
    (hs : BalancedFive n s) (hr : FiniteResidual (orbit n s) d)
    (rank : Nat → Nat → α) :
    ¬ (r (rank n (s+d)) (rank (orbit n s) d) ∧
       r (rank (residualSource n (s+d)) (residualClock n (s+d)))
         (rank n (s+d))) := by
  obtain ⟨source, clock⟩ := normalize_inverse_extension hs hr
  rw [source, clock]
  exact wellFounded_no_two_cycle wf _ _

end CollatzGlobal
