import FanGeometry
import PopulationTransfer

/-!
The compiled composition: unbounded approximation scales, actual marked
inverse fans with bounded clocks, and the finite survivor-count criterion.
The count upper bound is the remaining global assertion, not a premise
hidden in the geometric construction.
-/

namespace CollatzShell.ForwardSection.Band

/-- Every small ternary unit has a whole binary fan in the actual forward
section. All clocks lie in one interval of length `4*Q+5`. -/
theorem marked_ancestors_with_clocks {Q : Nat} (hQ : GoodScale Q) :
    BoundedSectionFan Q := by
  intro a unit small
  obtain ⟨z,zu,zlo,zhi,⟨d,dl,du,hit⟩,phase⟩ := steered_root_with_clock hQ unit small
  have q16 := hQ.1
  have qp : 0<Q := by omega
  have z2 : 2≤z :=
    (show 2≤2^Q from Nat.le_self_pow (by omega) 2).trans zlo
  have marks := oddFan_marked_of_phase (Q:=Q) (z:=z) (by omega) zu zlo zhi phase
  refine ⟨fun w => oddFan Q w z,
    fun w => 6*Q-oddFanPadding Q w z+d,
    oddFan_injective Q z qp zu z2,?_⟩
  intro w
  have pad := (oddFan_spec Q qp w z zu).1
  refine ⟨(marks w).1,(marks w).2.1,by dsimp; omega,by dsimp; omega,?_⟩
  rw [orbit_add,oddFan_clock Q qp w z zu]
  exact hit

theorem marked_ancestors {Q : Nat} (hQ : GoodScale Q) : SectionFan Q :=
  (marked_ancestors_with_clocks hQ).toSectionFan

/-- A passing finite band count supplies a concrete ordinary hitting-time
bound for every represented unit, without any extra transport-clock loss. -/
theorem band_count_finite_certificate {Q t : Nat} (hQ : GoodScale Q)
    (budget : (sectionSurvivors Q t).card<2^Q) :
    ∀ a : Nat, a%3≠0 → a≤2^Q → HitBy (max 1 t) a := by
  exact section_count_certifies_small_units (marked_ancestors hQ) budget

/-- Full Collatz is equivalent to beating an exponentially large exception
allowance inside the mandatory density-zero section, at unbounded admissible
scales. No upper bound on this survivor count is supplied here. -/
theorem collatz_iff_band_survivor_count :
    Universal ↔ ∀ K : Nat, ∃ Q≥K, GoodScale Q ∧ ∃ t,
      (sectionSurvivors Q t).card<2^Q := by
  exact collatz_iff_unbounded_section_counts GoodScale goodScale_cofinal
    (fun _ h => marked_ancestors h)

/-- The actual section construction amplifies every finite ordinary
component population, with only the clock-window overlap loss. -/
theorem band_component_population {Q : Nat} (hQ : GoodScale Q)
    (S : Finset Nat) (P : Nat → Prop)
    (units : ∀ a∈S, a%3≠0) (small : ∀ a∈S, a≤2^Q)
    (label : ∀ a∈S, P a)
    (backward : ∀ {x a : Nat}, Hits x a → P a → P x) :
    (2^Q)*S.card ≤ (4*Q+5)*(markedProperty Q P).card := by
  exact component_population_transfer (by have := hQ.1; omega)
    (marked_ancestors_with_clocks hQ) S P units small label backward

/-- Every surviving unit population forces this lower bound at every clock,
so an upper estimate would rule out actual ordinary counterexamples. -/
theorem band_survivor_population {Q : Nat} (hQ : GoodScale Q)
    (S : Finset Nat) (units : ∀ a∈S, a%3≠0) (small : ∀ a∈S, a≤2^Q)
    (bad : ∀ a∈S, ¬ Basin a) (t : Nat) :
    (2^Q)*S.card ≤ (4*Q+5)*(sectionSurvivors Q t).card := by
  exact survivor_population_transfer (by have := hQ.1; omega)
    (marked_ancestors_with_clocks hQ) S units small bad t

/-- The population comparison is already valid for finite survivors at the
same clock; no assumption of an eternal counterexample is needed. -/
theorem band_finite_survivor_population {Q t : Nat} (hQ : GoodScale Q) (ht : 1≤t) :
    (2^Q)*(smallUnitSurvivors Q t).card ≤
      (4*Q+5)*(sectionSurvivors Q t).card := by
  exact finite_survivor_population_bound (by have := hQ.1; omega) ht
    (marked_ancestors_with_clocks hQ)

#print axioms marked_ancestors_with_clocks
#print axioms marked_ancestors
#print axioms band_count_finite_certificate
#print axioms collatz_iff_band_survivor_count
#print axioms band_component_population
#print axioms band_survivor_population
#print axioms band_finite_survivor_population

end CollatzShell.ForwardSection.Band
