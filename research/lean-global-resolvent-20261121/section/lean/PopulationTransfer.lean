import CountCriterion

/-! Quantitative transport of an entire ordinary component population into
    the shrinking marked section. The fan's exact clock interval controls
    overlap between fans attached to different source integers. -/

namespace CollatzShell.ForwardSection.Band

/-- The section fan with its ordinary shortcut clock retained. -/
def BoundedSectionFan (Q : Nat) : Prop :=
  ∀ a : Nat, a%3≠0 → a≤2^Q →
    ∃ f : (Fin Q → Bool) → Nat, ∃ k : (Fin Q → Bool) → Nat,
      Function.Injective f ∧ ∀ w,
        Marked (f w) ∧ f w<2^(10*Q) ∧
        7*Q-5≤k w ∧ k w<11*Q ∧ orbit (k w) (f w)=a

theorem BoundedSectionFan.toSectionFan {Q : Nat}
    (fan : BoundedSectionFan Q) : SectionFan Q := by
  intro a unit small
  obtain ⟨f,k,inj,spec⟩ := fan a unit small
  exact ⟨f,inj,fun w => ⟨(spec w).1,(spec w).2.1,k w,(spec w).2.2.2.2⟩⟩

/-- The marked points below the cutoff carrying the supplied component label. -/
noncomputable def markedProperty (Q : Nat) (P : Nat → Prop) : Finset Nat := by
  classical
  exact (Finset.range (2^(10*Q))).filter (fun x => Marked x ∧ P x)

theorem mem_markedProperty {Q x : Nat} {P : Nat → Prop} :
    x∈markedProperty Q P ↔ x<2^(10*Q) ∧ Marked x ∧ P x := by
  classical
  simp only [markedProperty,Finset.mem_filter,Finset.mem_range]

/-- Every source contributes `2^Q` distinct marked ancestors. A marked point
    can be charged at most once at each clock in the window of length `4Q+5`.
    This permits all the source fans to be counted together. -/
theorem component_population_transfer {Q : Nat} (positive : 1≤Q)
    (fan : BoundedSectionFan Q) (S : Finset Nat) (P : Nat → Prop)
    (units : ∀ a∈S, a%3≠0) (small : ∀ a∈S, a≤2^Q)
    (label : ∀ a∈S, P a)
    (backward : ∀ {x a : Nat}, Hits x a → P a → P x) :
    (2^Q)*S.card ≤ (4*Q+5)*(markedProperty Q P).card := by
  classical
  choose f k inj spec using
    (fun a : S => fan a.val (units a.val a.property) (small a.val a.property))
  let B := markedProperty Q P
  let C := Finset.Ico (7*Q-5) (11*Q)
  have membership (a : S) (w : Fin Q → Bool) : f a w∈B := by
    obtain ⟨mark,loc,_,_,hit⟩ := spec a w
    exact mem_markedProperty.mpr
      ⟨loc,mark,backward ⟨k a w,hit⟩ (label a.val a.property)⟩
  have clock_mem (a : S) (w : Fin Q → Bool) : k a w∈C :=
    Finset.mem_Ico.mpr ⟨(spec a w).2.2.1,(spec a w).2.2.2.1⟩
  let g : (S × (Fin Q → Bool)) → (B × C) := fun aw =>
    (⟨f aw.1 aw.2,membership aw.1 aw.2⟩,⟨k aw.1 aw.2,clock_mem aw.1 aw.2⟩)
  have injective : Function.Injective g := by
    rintro ⟨a,w⟩ ⟨b,v⟩ eq
    have values : f a w=f b v := congrArg (fun p : B × C => (p.1 : Nat)) eq
    have clocks : k a w=k b v := congrArg (fun p : B × C => (p.2 : Nat)) eq
    have sources : a=b := Subtype.ext (by
      calc a.val = orbit (k a w) (f a w) := (spec a w).2.2.2.2.symm
        _ = orbit (k b v) (f b v) := by rw [values,clocks]
        _ = b.val := (spec b v).2.2.2.2)
    subst b
    have words : w=v := inj a values
    subst v
    rfl
  have count := Fintype.card_le_of_injective g injective
  have count' : S.card*2^Q≤B.card*C.card := by simpa using count
  have clock_card : C.card=4*Q+5 := by dsimp [C]; rw [Nat.card_Ico]; omega
  rw [clock_card] at count'
  simpa [B,Nat.mul_comm] using count'

/-- A finite population of nonconvergent units creates the same lower bound
    in every finite, completely decidable section-survivor experiment. -/
theorem survivor_population_transfer {Q : Nat} (positive : 1≤Q)
    (fan : BoundedSectionFan Q) (S : Finset Nat)
    (units : ∀ a∈S, a%3≠0) (small : ∀ a∈S, a≤2^Q)
    (bad : ∀ a∈S, ¬ Basin a) (t : Nat) :
    (2^Q)*S.card ≤ (4*Q+5)*(sectionSurvivors Q t).card := by
  classical
  have transferred := component_population_transfer positive fan S (fun a => ¬ Basin a)
    units small bad (by
      intro x a hit notA yesX
      exact notA ((basin_at_hit hit).mp yesX))
  have sub : markedProperty Q (fun a => ¬ Basin a) ⊆ sectionSurvivors Q t := by
    intro x hx
    obtain ⟨loc,mark,bad⟩ := mem_markedProperty.mp hx
    exact Finset.mem_filter.mpr ⟨Finset.mem_range.mpr loc,mark,fun i one => bad ⟨i.val,one⟩⟩
  exact transferred.trans (Nat.mul_le_mul_left _ (Finset.card_le_card sub))

/-- The population transport is already valid for finite survival through the
    same deadline, without a hypothesis of genuine nonconvergence. -/
theorem finite_survivor_population_transfer {Q t : Nat}
    (positiveQ : 1≤Q) (positiveT : 1≤t)
    (fan : BoundedSectionFan Q) (S : Finset Nat)
    (units : ∀ a∈S, a%3≠0) (small : ∀ a∈S, a≤2^Q)
    (alive : ∀ a∈S, ¬ HitBy t a) :
    (2^Q)*S.card ≤ (4*Q+5)*(sectionSurvivors Q t).card := by
  classical
  have transferred := component_population_transfer positiveQ fan S (fun a => ¬ HitBy t a)
    units small alive (by
      intro x a reach notA yesX
      exact notA (hitBy_at_hit positiveT reach yesX))
  have eq : markedProperty Q (fun a => ¬ HitBy t a)=sectionSurvivors Q t := by
    ext x
    simp only [mem_markedProperty,mem_sectionSurvivors]
  rwa [eq] at transferred

/-- Small ternary units surviving the supplied finite clock. -/
def smallUnitSurvivors (Q t : Nat) : Finset Nat :=
  (Finset.range (2^Q+1)).filter
    (fun a => a%3≠0 ∧ ∀ i : Fin (t+1), orbit i.val a≠1)

theorem mem_smallUnitSurvivors {Q t a : Nat} :
    a∈smallUnitSurvivors Q t ↔ a≤2^Q ∧ a%3≠0 ∧ ¬ HitBy t a := by
  simp only [smallUnitSurvivors,Finset.mem_filter,Finset.mem_range,
    Nat.lt_succ_iff,nohit_iff_not_hitBy]

/-- A comparison between two entirely finite, decidable experiments at the
    identical ordinary observation clock. -/
theorem finite_survivor_population_bound {Q t : Nat}
    (positiveQ : 1≤Q) (positiveT : 1≤t) (fan : BoundedSectionFan Q) :
    (2^Q)*(smallUnitSurvivors Q t).card ≤
      (4*Q+5)*(sectionSurvivors Q t).card := by
  apply finite_survivor_population_transfer positiveQ positiveT fan
    (smallUnitSurvivors Q t)
  · intro a ha
    exact (mem_smallUnitSurvivors.mp ha).2.1
  · intro a ha
    exact (mem_smallUnitSurvivors.mp ha).1
  · intro a ha
    exact (mem_smallUnitSurvivors.mp ha).2.2

#print axioms component_population_transfer
#print axioms survivor_population_transfer
#print axioms finite_survivor_population_transfer
#print axioms finite_survivor_population_bound

end CollatzShell.ForwardSection.Band
