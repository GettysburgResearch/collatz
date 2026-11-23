import ForwardSection

/-!
# A finite survivor criterion on the actual forward section

`DenseBandFans` is the explicitly supplied population hypothesis.  Its analytic
proof is in `MARKED_PREDECESSOR_POPULATIONS.md`; that argument and its analytic
input have not been formalized here.  No axiom asserts this hypothesis.

This module checks the finite counting and ordinary-orbit transfer from that
hypothesis to the precise all-sufficiently-large-octaves criterion.  The survivor
upper bound itself remains open.
-/

namespace CollatzShell.ForwardSection.Population

def band (d : Nat) : Finset Nat :=
  (Finset.Ico (2^d) (2^(d+1))).filter Marked

def survivors (d t : Nat) : Finset Nat :=
  (band d).filter (fun n => ∀ j < t+1, orbit j n ≠ 1)

/-- The same positive integer constant works for every unit target.  The octave,
    finite set, and common clock may depend on both the target and the cutoff. -/
def DenseBandFans : Prop :=
  ∃ C : Nat, 0<C ∧ ∀ q : Nat, q%3≠0 → ∀ D : Nat,
    ∃ d≥D, ∃ clock : Nat, ∃ P : Finset Nat,
      P ⊆ band d ∧ (∀ n ∈ P, orbit clock n=q) ∧
        2^d ≤ C*(d+1)^2*P.card

/-- The clock may vary with the octave.  Every sufficiently large octave must
    pass; an arbitrary unbounded subsequence is not substituted here. -/
def CubicSurvivorBound : Prop :=
  ∃ D : Nat, ∀ d≥D, ∃ t : Nat, (d+1)^3*(survivors d t).card < 2^d

theorem band_positive {d n : Nat} (h : n ∈ band d) : 0<n := by
  have low := (Finset.mem_Ico.mp (Finset.mem_filter.mp h).1).1
  have pos : 0<(2:Nat)^d := by positivity
  omega

theorem predecessor_subset_survivors {q d clock : Nat} {P : Finset Nat}
    (outside : ¬ Basin q) (inside : P ⊆ band d)
    (hits : ∀ n ∈ P, orbit clock n=q) (t : Nat) : P ⊆ survivors d t := by
  intro n hn
  apply Finset.mem_filter.mpr
  refine ⟨inside hn, ?_⟩
  intro j _ one
  apply outside
  exact (basin_at_hit (show Hits n q from ⟨clock, hits n hn⟩)).mp ⟨j,one⟩

theorem empty_survivors_of_universal (all : Universal) (d : Nat) :
    ∃ t, survivors d t=∅ := by
  classical
  let clock (n : Nat) := if hn : 0<n then Nat.find (all n hn) else 0
  let t := (band d).sup clock
  refine ⟨t, Finset.eq_empty_iff_forall_notMem.mpr ?_⟩
  intro n hn
  obtain ⟨hb, stays⟩ := Finset.mem_filter.mp hn
  have hp : 0<n := band_positive hb
  have hit : orbit (clock n) n=1 := by
    simp only [clock, dite_eq_left hp]
    exact Nat.find_spec (all n hp)
  have le : clock n≤t := Finset.le_sup hb
  exact (stays (clock n) (by omega)) hit

theorem cubic_bound_of_universal (all : Universal) : CubicSurvivorBound := by
  refine ⟨0, fun d _ => ?_⟩
  obtain ⟨t,empty⟩ := empty_survivors_of_universal all d
  refine ⟨t, ?_⟩
  simp only [empty,Finset.card_empty,Nat.mul_zero]
  positivity

theorem universal_of_cubic_bound (fans : DenseBandFans)
    (bound : CubicSurvivorBound) : Universal := by
  obtain ⟨C,_,fans⟩ := fans
  obtain ⟨D,bound⟩ := bound
  apply universal_of_units
  intro q hq
  by_contra outside
  obtain ⟨d,large,clock,P,inside,hits,many⟩ := fans q hq (max D C)
  have dD : D≤d := (le_max_left D C).trans large
  have dC : C≤d+1 := by have := (le_max_right D C).trans large; omega
  obtain ⟨t,few⟩ := bound d dD
  have pop : P.card≤(survivors d t).card :=
    Finset.card_le_card (predecessor_subset_survivors outside inside hits t)
  have inc : C*(d+1)^2*P.card≤(d+1)^3*(survivors d t).card := by
    calc C*(d+1)^2*P.card
        ≤ (d+1)*(d+1)^2*P.card := Nat.mul_le_mul_right _ (Nat.mul_le_mul_right _ dC)
      _ ≤ (d+1)*(d+1)^2*(survivors d t).card := Nat.mul_le_mul_left _ pop
      _ = (d+1)^3*(survivors d t).card := by ring
  exact (many.trans inc).not_gt few

theorem universal_iff_cubic_bound (fans : DenseBandFans) :
    Universal ↔ CubicSurvivorBound :=
  ⟨cubic_bound_of_universal, universal_of_cubic_bound fans⟩

#print axioms predecessor_subset_survivors
#print axioms universal_iff_cubic_bound

end CollatzShell.ForwardSection.Population
