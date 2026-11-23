import Collatz.Closure

/-!
Ordinary source-rank normalization for forward-five failures.

This module proves reductions, not the remaining closure implication.
There are no added axioms or unfinished proofs.  It imports the core-only
ordinary-map toolbox pinned to PR174 in the accompanying note.
-/
open CollatzReverseBasin CollatzClosure

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzTerminalFive

def orbit (n : Nat) : Nat → Nat
  | 0 => n
  | t + 1 => shortcut (orbit n t)

theorem orbit_add (n s t : Nat) :
    orbit n (s + t) = orbit (orbit n s) t := by
  induction t with
  | zero => rfl
  | succ t ih => simpa [orbit, Nat.add_assoc] using congrArg shortcut ih

theorem orbit_step (n t : Nat) : orbit (shortcut n) t = orbit n (t + 1) := by
  have h := orbit_add n 1 t
  simpa [orbit, Nat.add_comm] using h.symm

theorem hits_iff_orbit (n d : Nat) : Hits n d ↔ orbit n d = 1 := by
  induction d generalizing n with
  | zero => rfl
  | succ d ih =>
    change Hits (shortcut n) d ↔ orbit n (d + 1) = 1
    rw [ih, orbit_step]

theorem basin_orbit (n t : Nat) : Basin (orbit n t) ↔ Basin n := by
  induction t with
  | zero => rfl
  | succ t ih => exact (basin_step _).trans ih

theorem shortcut_pos {n : Nat} (hn : 0 < n) : 0 < shortcut n := by
  unfold shortcut
  split <;> omega

theorem orbit_pos {n : Nat} (hn : 0 < n) (t : Nat) : 0 < orbit n t := by
  induction t with
  | zero => exact hn
  | succ t ih => exact shortcut_pos ih

theorem basin_pos {n : Nat} (hn : Basin n) : 0 < n := by
  rcases hn with ⟨d, hd⟩
  have hz : ∀ t, orbit 0 t = 0 := by
    intro t
    induction t with
    | zero => rfl
    | succ t ih => simp [orbit, ih, shortcut]
  have he := (hits_iff_orbit n d).mp hd
  by_cases h : n = 0
  · subst n
    rw [hz] at he
    omega
  · omega

theorem orbit_one_cycle (t : Nat) : orbit 1 t = 1 ∨ orbit 1 t = 2 := by
  induction t with
  | zero => exact Or.inl rfl
  | succ t ih =>
    rcases ih with h | h
    · right; simp [orbit, h, shortcut]
    · left; simp [orbit, h, shortcut]

theorem basin_five : Basin 5 := ⟨4, rfl⟩

theorem five_cycle (t : Nat) : Basin (5 * orbit 1 t) := by
  rcases orbit_one_cycle t with h | h
  · simpa [h] using basin_five
  · simpa [h] using (basin_twice 5).mpr basin_five

theorem orbit_after_hit {x d : Nat} (hd : Hits x d)
    {s : Nat} (hs : d ≤ s) : orbit x s = 1 ∨ orbit x s = 2 := by
  have hadd : d + (s - d) = s := by omega
  have he : orbit x s = orbit 1 (s - d) := by
    rw [← hadd, orbit_add, (hits_iff_orbit x d).mp hd]
    congr 1
    omega
  rw [he]
  exact orbit_one_cycle (s - d)

theorem five_after_hit {x d : Nat} (hd : Hits x d)
    {s : Nat} (hs : d ≤ s) : Basin (5 * orbit x s) := by
  rcases orbit_after_hit hd hs with h | h
  · simpa [h] using basin_five
  · simpa [h] using (basin_twice 5).mpr basin_five

/-- The ordinary forward-five closure statement. -/
def ForwardFive : Prop := ∀ x : Nat, 0 < x → Basin x → Basin (5 * x)

/-- An actual failed comparison, with a supplied finite source certificate. -/
def Failure (x : Nat) : Prop := Basin x ∧ ¬ Basin (5 * x)

/-- A source whose five-multiples at all strict future clocks are certified. -/
def SuccessorClosed (x : Nat) : Prop :=
  ∀ s : Nat, 0 < s → Basin (5 * orbit x s)

/-- No proportional return, even with independently chosen ordinary clocks. -/
def AsyncTerminal (x : Nat) : Prop :=
  ∀ s : Nat, 0 < s → ∀ t : Nat,
    orbit (5 * x) t ≠ 5 * orbit x s

/-- Failed comparisons have no proportional return at any source clock at
    or after a supplied hit of one.  Target clocks are independent. -/
theorem failure_no_late_return {x d : Nat} (hd : Hits x d)
    (hbad : ¬ Basin (5 * x)) {s : Nat} (hs : d ≤ s) (t : Nat) :
    orbit (5 * x) t ≠ 5 * orbit x s := by
  intro he
  have hb : Basin (orbit (5 * x) t) := by
    rw [he]
    exact five_after_hit hd hs
  exact hbad ((basin_orbit _ _).mp hb)

/-- Every failed pair has an asynchronously terminal descendant in the same
    two ordinary components.  The remaining source certificate loses exactly
    the consumed source clock.  No bound on target search time is asserted. -/
theorem failure_has_async_terminal_descendant {x d : Nat}
    (hd : Hits x d) (hbad : ¬ Basin (5 * x)) :
    ∃ q s t e : Nat, s + e = d ∧ Hits q e ∧ AsyncTerminal q ∧
      orbit x s = q ∧ orbit (5 * x) t = 5 * q ∧ ¬ Basin (5 * q) := by
  induction d using Nat.strong_induction_on generalizing x with
  | h d ih =>
    by_cases hex : ∃ s : Nat, 0 < s ∧ ∃ t : Nat,
        orbit (5 * x) t = 5 * orbit x s
    · obtain ⟨s, hs, t, he⟩ := hex
      have hsd : s < d := by
        by_cases hle : d ≤ s
        · exact False.elim (failure_no_late_return hd hbad hle t he)
        · omega
      have htail : Hits (orbit x s) (d - s) := by
        apply (hits_iff_orbit _ _).mpr
        rw [← orbit_add, show s + (d-s) = d by omega]
        exact (hits_iff_orbit x d).mp hd
      have hchild : ¬ Basin (5 * orbit x s) := by
        intro hb
        apply hbad
        apply (basin_orbit _ _).mp
        rwa [he]
      obtain ⟨q, u, v, e, hue, hq, ht, hu, hv, hbq⟩ :=
        ih (d-s) (by omega) htail hchild
      refine ⟨q, s+u, t+v, e, by omega, hq, ht, ?_, ?_, hbq⟩
      · rw [orbit_add, hu]
      · rw [orbit_add, he, hv]
    · refine ⟨x, 0, 0, d, by omega, hd, ?_, rfl, rfl, hbad⟩
      intro s hs t he
      exact hex ⟨s, hs, t, he⟩

/-- Minimality here is over certificate clocks, not the numerical size of x. -/
def RankMinimalFailure (x d : Nat) : Prop :=
  Hits x d ∧ ¬ Basin (5 * x) ∧
    ∀ e : Nat, e < d → ∀ y : Nat, Hits y e → Basin (5 * y)

theorem failure_has_rank_minimal {x d : Nat}
    (hx : Hits x d) (hbad : ¬ Basin (5 * x)) :
    ∃ y e : Nat, e ≤ d ∧ RankMinimalFailure y e := by
  induction d using Nat.strong_induction_on generalizing x with
  | h d ih =>
    by_cases he : ∃ e : Nat, e < d ∧ ∃ y : Nat,
        Hits y e ∧ ¬ Basin (5 * y)
    · obtain ⟨e, hed, y, hy, hby⟩ := he
      obtain ⟨z, f, hfe, hf⟩ := ih e hed hy hby
      exact ⟨z, f, by omega, hf⟩
    · refine ⟨x, d, Nat.le_refl d, hx, hbad, ?_⟩
      intro e hed y hy
      apply Classical.byContradiction
      intro hby
      exact he ⟨e, hed, y, hy, hby⟩

theorem rank_minimal_successor_closed {x d : Nat}
    (hm : RankMinimalFailure x d) : SuccessorClosed x := by
  intro s hs
  by_cases hsd : s ≤ d
  · have hadd : s + (d - s) = d := by omega
    have htail : Hits (orbit x s) (d - s) := by
      apply (hits_iff_orbit _ _).mpr
      rw [← orbit_add, hadd]
      exact (hits_iff_orbit x d).mp hm.1
    exact hm.2.2 (d - s) (by omega) (orbit x s) htail
  · have hadd : d + (s - d) = s := by omega
    have hx1 := (hits_iff_orbit x d).mp hm.1
    have he : orbit x s = orbit 1 (s - d) := by
      rw [← hadd, orbit_add, hx1]
      congr 1
      omega
    rw [he]
    exact five_cycle (s - d)

theorem successor_closed_terminal {x : Nat}
    (hbad : ¬ Basin (5 * x)) (hc : SuccessorClosed x) : AsyncTerminal x := by
  intro s hs t he
  have ht : Basin (orbit (5 * x) t) := by rw [he]; exact hc s hs
  exact hbad ((basin_orbit (5 * x) t).mp ht)

theorem failure_has_terminal {x : Nat} (hf : Failure x) :
    ∃ q : Nat, Failure q ∧ SuccessorClosed q ∧ AsyncTerminal q := by
  obtain ⟨d, hd⟩ := hf.1
  obtain ⟨q, e, _, hm⟩ := failure_has_rank_minimal hd hf.2
  have hc := rank_minimal_successor_closed hm
  exact ⟨q, ⟨⟨e, hm.1⟩, hm.2.1⟩, hc,
    successor_closed_terminal hm.2.1 hc⟩

theorem forward_five_iff_async_terminals :
    ForwardFive ↔ ∀ x : Nat, 0 < x → Basin x → AsyncTerminal x → Basin (5 * x) := by
  constructor
  · exact fun h x hx hb _ => h x hx hb
  · intro h x hx hb
    apply Classical.byContradiction
    intro hbad
    obtain ⟨q, hq, _, ht⟩ := failure_has_terminal ⟨hb, hbad⟩
    exact hq.2 (h q (basin_pos hq.1) hq.1 ht)

theorem forward_five_iff_successor_closed :
    ForwardFive ↔ ∀ x : Nat, 0 < x → Basin x →
      SuccessorClosed x → Basin (5 * x) := by
  constructor
  · exact fun h x hx hb _ => h x hx hb
  · intro h x hx hb
    apply Classical.byContradiction
    intro hbad
    obtain ⟨q, hq, hc, _⟩ := failure_has_terminal ⟨hb, hbad⟩
    exact hq.2 (h q (basin_pos hq.1) hq.1 hc)

/-! A fixed-offset local repair criterion, with both antecedents explicit. -/

def OneOffsetRepair : Prop :=
  ∀ k : Nat, Basin (3*k+1) → Basin (15*k+5) → Basin (15*k+4)

def TwoOffsetRepair : Prop :=
  ∀ k : Nat, Basin (6*k+5) → Basin (30*k+25) → Basin (30*k+23)

theorem basin_five_one (k : Nat) :
    Basin (5*(4*k+1)) ↔ Basin (15*k+4) := by
  have h := basin_exch (20*k+5) (15*k+4) (5*k+1) (by omega) (by omega)
  simpa [Nat.mul_add, ← Nat.mul_assoc] using h

theorem basin_five_three (k : Nat) :
    Basin (5*(4*k+3)) ↔ Basin (30*k+23) := by
  have h := basin_step (5*(4*k+3))
  have hs : shortcut (5*(4*k+3)) = 30*k+23 := by
    unfold shortcut
    split <;> omega
  simpa [hs] using h.symm

theorem offsets_of_forward_five (h : ForwardFive) :
    OneOffsetRepair ∧ TwoOffsetRepair := by
  constructor
  · intro k hu _
    have hq : Basin (4*k+1) :=
      (basin_exch (4*k+1) (3*k+1) k (by omega) (by omega)).mpr hu
    exact (basin_five_one k).mp (h _ (by omega) hq)
  · intro k hu _
    have hs : shortcut (4*k+3) = 6*k+5 := by
      unfold shortcut
      split <;> omega
    have hq : Basin (4*k+3) := (basin_step _).mp (by rwa [hs])
    exact (basin_five_three k).mp (h _ (by omega) hq)

theorem five_even_step {x : Nat} (he : x % 2 = 0) :
    shortcut (5*x) = 5*shortcut x := by
  unfold shortcut
  split <;> omega

theorem one_step_repair (h₁ : OneOffsetRepair) (h₂ : TwoOffsetRepair)
    {x : Nat} (hx : Basin x) (hs : Basin (5*shortcut x)) : Basin (5*x) := by
  by_cases he : x % 2 = 0
  · apply (basin_step _).mp
    rwa [five_even_step he]
  · have hmod : x % 4 = 1 ∨ x % 4 = 3 := by omega
    rcases hmod with hmod | hmod
    · let k := x / 4
      have hex : x = 4*k+1 := by dsimp [k]; omega
      rw [hex] at hx hs ⊢
      have hsource : Basin (3*k+1) :=
        (basin_exch (4*k+1) (3*k+1) k (by omega) (by omega)).mp hx
      have hstep : shortcut (4*k+1) = 2*(3*k+1) := by
        unfold shortcut
        split <;> omega
      have h5 : Basin (15*k+5) := by
        rw [hstep, show 5*(2*(3*k+1))=2*(15*k+5) by omega] at hs
        exact (basin_twice _).mp hs
      exact (basin_five_one k).mpr (h₁ k hsource h5)
    · let k := x / 4
      have hex : x = 4*k+3 := by dsimp [k]; omega
      rw [hex] at hx hs ⊢
      have hstep : shortcut (4*k+3) = 6*k+5 := by
        unfold shortcut
        split <;> omega
      have hsource : Basin (6*k+5) := by
        rw [← hstep]
        exact (basin_step _).mpr hx
      have h5 : Basin (30*k+25) := by
        rwa [hstep, show 5*(6*k+5)=30*k+25 by omega] at hs
      exact (basin_five_three k).mpr (h₂ k hsource h5)

theorem forward_five_of_offsets (h₁ : OneOffsetRepair) (h₂ : TwoOffsetRepair) :
    ForwardFive := by
  intro x _ hx
  obtain ⟨d, hd⟩ := hx
  induction d generalizing x with
  | zero =>
    change x = 1 at hd
    subst x
    exact basin_five
  | succ d ih =>
    apply one_step_repair h₁ h₂ ⟨d+1, hd⟩
    exact ih (shortcut x) (shortcut_pos (basin_pos ⟨d+1, hd⟩)) hd

theorem forward_five_iff_offsets :
    ForwardFive ↔ OneOffsetRepair ∧ TwoOffsetRepair := by
  exact ⟨offsets_of_forward_five,
    fun h => forward_five_of_offsets h.1 h.2⟩

theorem rank_minimal_odd {x d : Nat} (hm : RankMinimalFailure x d) : x % 2 = 1 := by
  have hc := rank_minimal_successor_closed hm
  by_cases he : x % 2 = 0
  · have hs : Basin (5*shortcut x) := by simpa [orbit] using hc 1 (by omega)
    have hh : Basin (5*x) := (basin_step _).mp (by rwa [five_even_step he])
    exact False.elim (hm.2.1 hh)
  · omega

/-! Small exact controls for the new terminal notion. -/

/-- The source 5 is balanced-terminal in PR146's rank-one family, but it is
    removed by asynchronous normalization: source clock 4, target clock 12. -/
theorem five_not_async_terminal : ¬ AsyncTerminal 5 := by
  intro h
  exact h 4 (by omega) 12 rfl

/-- The stronger terminal set is still nonempty, even among successful pairs. -/
theorem seventeen_async_terminal : AsyncTerminal 17 := by
  have hx : Hits 17 9 := rfl
  have hy : Hits (5*17) 8 := rfl
  have hfinite : ∀ s : Fin 9, 0 < s.val → ∀ t : Fin 8,
      orbit (5*17) t.val ≠ 5 * orbit 17 s.val := by decide
  have htail : ∀ t : Fin 8,
      orbit (5*17) t.val ≠ 5 ∧ orbit (5*17) t.val ≠ 10 := by decide
  intro s hs t he
  have hpos := orbit_pos (n := 17) (by omega) s
  by_cases ht : 8 ≤ t
  · rcases orbit_after_hit hy ht with h | h <;> omega
  · have hlt : t < 8 := by omega
    by_cases hs9 : 9 ≤ s
    · rcases orbit_after_hit hx hs9 with h | h
      · have hh := (htail ⟨t, hlt⟩).1
        simp only at hh
        rw [h] at he
        exact hh he
      · have hh := (htail ⟨t, hlt⟩).2
        simp only at hh
        rw [h] at he
        exact hh he
    · exact hfinite ⟨s, by omega⟩ hs ⟨t, hlt⟩ he

theorem seventeen_successful_terminal :
    Basin 17 ∧ Basin (5*17) ∧ AsyncTerminal 17 :=
  ⟨⟨9, rfl⟩, ⟨8, rfl⟩, seventeen_async_terminal⟩

#print axioms failure_no_late_return
#print axioms failure_has_async_terminal_descendant
#print axioms failure_has_rank_minimal
#print axioms rank_minimal_successor_closed
#print axioms failure_has_terminal
#print axioms forward_five_iff_async_terminals
#print axioms forward_five_iff_successor_closed
#print axioms forward_five_iff_offsets
#print axioms five_not_async_terminal
#print axioms seventeen_successful_terminal

end CollatzTerminalFive
