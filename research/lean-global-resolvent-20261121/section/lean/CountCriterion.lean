import ForwardSection

/-! Finite survivor counts inside the actual shrinking dyadic section.

The arithmetic fan and unbounded admissible scales are explicit hypotheses in
this modular counting theorem. A caller must supply those constructions; no
ordinary-trajectory count estimate is assumed or proved here.
-/

namespace CollatzShell.ForwardSection.Band

/-- A whole binary fan of actual marked ancestors for each supplied small unit.
    The clocks of different ancestors may be completely different. -/
def SectionFan (Q : Nat) : Prop :=
  ∀ a : Nat, a%3≠0 → a≤2^Q →
    ∃ f : (Fin Q → Bool) → Nat, Function.Injective f ∧
      ∀ w, Marked (f w) ∧ f w<2^(10*Q) ∧ Hits (f w) a

/-- A hit at some ordinary clock no larger than the finite deadline. -/
def HitBy (t n : Nat) : Prop := ∃ i≤t, orbit i n=1

theorem HitBy.mono {s t n : Nat} (st : s≤t) (hit : HitBy s n) : HitBy t n := by
  obtain ⟨i,is,one⟩ := hit
  exact ⟨i,is.trans st,one⟩

/-- Once the deadline allows one clock, the final `1 -> 2 -> 1` cycle
    makes hitting by that deadline forward invariant. -/
theorem hitBy_step {t n : Nat} (positive : 1≤t) (hit : HitBy t n) :
    HitBy t (step n) := by
  obtain ⟨i,it,one⟩ := hit
  cases i with
  | zero =>
    change n=1 at one
    subst n
    exact ⟨1,positive,rfl⟩
  | succ j => exact ⟨j,by omega,one⟩

/-- The finite deadline is unchanged even when the meeting clock is later
    than that deadline. The cycle case is covered by `hitBy_step`. -/
theorem hitBy_at_hit {t x a : Nat} (positive : 1≤t)
    (reach : Hits x a) (hit : HitBy t x) : HitBy t a := by
  obtain ⟨k,rfl⟩ := reach
  induction k generalizing x with
  | zero => exact hit
  | succ k ih => exact ih (hitBy_step positive hit)

theorem nohit_iff_not_hitBy (t x : Nat) :
    (∀ i : Fin (t+1), orbit i.val x≠1) ↔ ¬ HitBy t x := by
  constructor
  · intro nohit ⟨i,it,one⟩
    exact nohit ⟨i,by omega⟩ one
  · intro nohit i one
    exact nohit ⟨i.val,by omega,one⟩

/-- Marked positive starts below the stage cutoff that have not hit one
    through the supplied finite ordinary shortcut clock. -/
def sectionSurvivors (Q t : Nat) : Finset Nat :=
  (Finset.range (2^(10*Q))).filter
    (fun x => Marked x ∧ ∀ i : Fin (t+1), orbit i.val x≠1)

theorem mem_sectionSurvivors {Q t x : Nat} :
    x∈sectionSurvivors Q t ↔ x<2^(10*Q) ∧ Marked x ∧ ¬ HitBy t x := by
  simp only [sectionSurvivors,Finset.mem_filter,Finset.mem_range,nohit_iff_not_hitBy]

theorem sectionSurvivors_mono (Q : Nat) {s t : Nat} (st : s≤t) :
    sectionSurvivors Q t ⊆ sectionSurvivors Q s := by
  intro x hx
  obtain ⟨loc,mark,nohit⟩ := Finset.mem_filter.mp hx
  exact Finset.mem_filter.mpr ⟨loc,mark,fun i => nohit ⟨i.val,by omega⟩⟩

/-- A budget below the fan size proves convergence of every represented unit.
    A meeting clock is not required to be before or after the finite test. -/
theorem recover_unit_from_section_count {Q t a : Nat}
    (fan : SectionFan Q) (unit : a%3≠0) (small : a≤2^Q)
    (budget : (sectionSurvivors Q t).card<2^Q) : Basin a := by
  obtain ⟨f,inj,inside⟩ := fan a unit small
  obtain ⟨w,missing⟩ := avoids_small f inj (sectionSurvivors Q t) budget
  obtain ⟨mark,loc,hit⟩ := inside w
  apply (basin_at_hit hit).mp
  by_contra notBasin
  apply missing
  refine Finset.mem_filter.mpr ⟨Finset.mem_range.mpr loc,mark,?_⟩
  intro i one
  exact notBasin ⟨i.val,one⟩

/-- A passing count is an actual finite certificate: every represented unit
    has hit one by `max 1 t`, regardless of the fan's meeting clocks. -/
theorem recover_unit_finite {Q t a : Nat}
    (fan : SectionFan Q) (unit : a%3≠0) (small : a≤2^Q)
    (budget : (sectionSurvivors Q t).card<2^Q) : HitBy (max 1 t) a := by
  obtain ⟨f,inj,inside⟩ := fan a unit small
  obtain ⟨w,missing⟩ := avoids_small f inj (sectionSurvivors Q t) budget
  obtain ⟨mark,loc,reach⟩ := inside w
  have seen : HitBy t (f w) := by
    by_contra nohit
    exact missing (mem_sectionSurvivors.mpr ⟨loc,mark,nohit⟩)
  exact hitBy_at_hit (Nat.le_max_left _ _) reach
    (HitBy.mono (Nat.le_max_right _ _) seen)

theorem section_count_certifies_small_units {Q t : Nat}
    (fan : SectionFan Q) (budget : (sectionSurvivors Q t).card<2^Q) :
    ∀ a : Nat, a%3≠0 → a≤2^Q → HitBy (max 1 t) a := by
  intro a unit small
  exact recover_unit_finite fan unit small budget

/-- One surviving ordinary component forces at least the entire fan population
    to survive every finite observation time inside the marked section. -/
theorem counterexample_section_population {Q a : Nat}
    (fan : SectionFan Q) (unit : a%3≠0) (small : a≤2^Q)
    (bad : ¬ Basin a) (t : Nat) : 2^Q≤(sectionSurvivors Q t).card := by
  by_contra! below
  exact bad (recover_unit_from_section_count fan unit small below)

private theorem finite_one_deadline (S : Finset Nat) (all : Universal) :
    ∃ t : Nat, ∀ x∈S, 0<x → ∃ i≤t, orbit i x=1 := by
  induction S using Finset.induction_on with
  | empty => exact ⟨0,by simp⟩
  | @insert a S _ ih =>
    obtain ⟨t,prev⟩ := ih
    by_cases ap : 0<a
    · obtain ⟨j,hit⟩ := all a ap
      refine ⟨max t j,?_⟩
      intro x hx xp
      rcases Finset.mem_insert.mp hx with eq | hs
      · exact ⟨j,Nat.le_max_right _ _,eq ▸ hit⟩
      · obtain ⟨i,it,one⟩ := prev x hs xp
        exact ⟨i,it.trans (Nat.le_max_left _ _),one⟩
    · refine ⟨t,?_⟩
      intro x hx xp
      rcases Finset.mem_insert.mp hx with eq | hs
      · omega
      · exact prev x hs xp

theorem empty_section_survivors (all : Universal) (Q : Nat) :
    ∃ t, sectionSurvivors Q t=∅ := by
  obtain ⟨t,cover⟩ := finite_one_deadline (Finset.range (2^(10*Q))) all
  refine ⟨t,Finset.eq_empty_iff_forall_notMem.mpr ?_⟩
  intro x hx
  obtain ⟨loc,mark,nohit⟩ := Finset.mem_filter.mp hx
  have xp : 0<x := by have odd := mark.1; omega
  obtain ⟨i,it,one⟩ := cover x loc xp
  exact nohit ⟨i,by omega⟩ one

/-- On any unbounded family of scales with the actual marked-ancestor fan,
    a finite error allowance of `2^Q-1` is exactly sufficient for full Collatz. -/
theorem collatz_iff_unbounded_section_counts
    (Good : Nat → Prop)
    (unbounded : ∀ K : Nat, ∃ Q≥K, Good Q)
    (fan : ∀ Q, Good Q → SectionFan Q) :
    Universal ↔ ∀ K : Nat, ∃ Q≥K, Good Q ∧ ∃ t,
      (sectionSurvivors Q t).card<2^Q := by
  constructor
  · intro all K
    obtain ⟨Q,KQ,good⟩ := unbounded K
    obtain ⟨t,empty⟩ := empty_section_survivors all Q
    exact ⟨Q,KQ,good,t,by rw [empty,Finset.card_empty]; positivity⟩
  · intro tests
    apply universal_of_units
    intro a unit
    obtain ⟨Q,aQ,good,t,budget⟩ := tests a
    have small : a≤2^Q := aQ.trans Nat.lt_two_pow_self.le
    exact recover_unit_from_section_count (fan Q good) unit small budget

#print axioms recover_unit_from_section_count
#print axioms hitBy_at_hit
#print axioms section_count_certifies_small_units
#print axioms counterexample_section_population
#print axioms collatz_iff_unbounded_section_counts

end CollatzShell.ForwardSection.Band
