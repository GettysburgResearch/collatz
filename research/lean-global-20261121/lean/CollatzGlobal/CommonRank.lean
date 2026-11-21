import CollatzGlobal.AdaptiveDescent

/-!
A common well-founded height/clock rank. Its intended rational value is
  (n+1) * (201/200)^d.
All definitions and proofs below use natural-number cross multiplication.
No rational library, real-number axiom, or assumed well-foundedness is used.
This is a rank on numerical states; sound transport of a mathematical goal
between states must be proved separately for each move.
-/

namespace CollatzGlobal

def rankNumerator (x : Nat × Nat) : Nat := (x.1+1)*201^x.2
def rankDenominator (x : Nat × Nat) : Nat := 200^x.2

/-- Strict comparison of the actual rational scores by positive denominators. -/
def ScoreLT (y x : Nat × Nat) : Prop :=
  rankNumerator y * rankDenominator x < rankNumerator x * rankDenominator y

def RankSublevel (B : Nat) (x : Nat × Nat) : Prop :=
  rankNumerator x ≤ B*rankDenominator x

theorem rank_denominator_positive (x : Nat × Nat) : 0 < rankDenominator x :=
  Nat.pow_pos (by decide)

/-- Integer form of Bernoulli's inequality for the chosen score. -/
theorem rank_bernoulli (d : Nat) : (200+d)*200^d ≤ 200*201^d := by
  induction d with
  | zero => decide
  | succ d ih =>
    have hp : 200^d ≤ 201^d := Nat.pow_le_pow_left (by decide) d
    have ha : (200+d)*200^d+200^d ≤ 200*201^d+201^d := by omega
    have hm := Nat.mul_le_mul_left 200 ha
    calc
      (200+(d+1))*200^(d+1) = 200*((200+d)*200^d+200^d) := by
        rw [Nat.pow_succ]
        grind
      _ ≤ 200*(200*201^d+201^d) := hm
      _ = 200*201^(d+1) := by rw [Nat.pow_succ]; grind

/-- Every fixed rational sublevel lies inside a finite explicit rectangle. -/
theorem rank_sublevel_bounds {B : Nat} {x : Nat × Nat} (hx : RankSublevel B x) :
    x.1+1 ≤ B ∧ x.2 ≤ 200*B := by
  have denpos := rank_denominator_positive x
  have hp : 200^x.2 ≤ 201^x.2 := Nat.pow_le_pow_left (by decide) x.2
  have hlo := Nat.mul_le_mul_left (x.1+1) hp
  unfold RankSublevel rankNumerator rankDenominator at hx
  have hvalue : x.1+1 ≤ B :=
    Nat.le_of_mul_le_mul_right (Nat.le_trans hlo hx) denpos
  have hn : 201^x.2 ≤ (x.1+1)*201^x.2 := by
    have h := Nat.mul_le_mul_right (201^x.2) (show 1≤x.1+1 by omega)
    simpa using h
  have hclock : (200+x.2)*200^x.2 ≤ (200*B)*200^x.2 := by
    calc
      (200+x.2)*200^x.2 ≤ 200*201^x.2 := rank_bernoulli x.2
      _ ≤ 200*((x.1+1)*201^x.2) := Nat.mul_le_mul_left 200 hn
      _ ≤ 200*(B*200^x.2) := Nat.mul_le_mul_left 200 hx
      _ = (200*B)*200^x.2 := by grind
  have hc := Nat.le_of_mul_le_mul_right hclock denpos
  exact ⟨hvalue, by omega⟩

/-- Strict score descent preserves every sublevel containing the source. -/
theorem rank_sublevel_preserved {B : Nat} {x y : Nat × Nat}
    (hstep : ScoreLT y x) (hx : RankSublevel B x) : RankSublevel B y := by
  have hmul : rankNumerator y*rankDenominator x <
      (B*rankDenominator y)*rankDenominator x := by
    calc
      rankNumerator y*rankDenominator x < rankNumerator x*rankDenominator y := hstep
      _ ≤ (B*rankDenominator x)*rankDenominator y := Nat.mul_le_mul_right _ hx
      _ = (B*rankDenominator y)*rankDenominator x := by grind
  exact Nat.le_of_lt (Nat.lt_of_mul_lt_mul_right hmul)

/-- Integer numerator after moving to one fixed common denominator. -/
def scaledRank (E : Nat) (x : Nat × Nat) : Nat :=
  rankNumerator x*200^(E-x.2)

theorem scaledRank_strict {E : Nat} {x y : Nat × Nat}
    (hstep : ScoreLT y x) (hx : x.2≤E) (hy : y.2≤E) :
    scaledRank E y < scaledRank E x := by
  have hxp : rankDenominator x*200^(E-x.2)=200^E := by
    unfold rankDenominator
    rw [← Nat.pow_add]
    congr 1
    omega
  have hyp : rankDenominator y*200^(E-y.2)=200^E := by
    unfold rankDenominator
    rw [← Nat.pow_add]
    congr 1
    omega
  have hpos : 0 < 200^(E-x.2)*200^(E-y.2) :=
    Nat.mul_pos (Nat.pow_pos (by decide)) (Nat.pow_pos (by decide))
  have hmul : scaledRank E y*200^E < scaledRank E x*200^E := by
    calc
      scaledRank E y*200^E =
          (rankNumerator y*rankDenominator x)*(200^(E-x.2)*200^(E-y.2)) := by
        rw [← hxp]
        unfold scaledRank
        grind
      _ < (rankNumerator x*rankDenominator y)*(200^(E-x.2)*200^(E-y.2)) :=
        Nat.mul_lt_mul_of_pos_right hstep hpos
      _ = scaledRank E x*200^E := by
        rw [← hyp]
        unfold scaledRank
        grind
  exact Nat.lt_of_mul_lt_mul_right hmul

/-- Accessibility follows by ordinary natural induction on a fixed common
denominator numerator. All predecessors stay in this same sublevel. -/
theorem scoreLT_accessible_on_sublevel (B : Nat) (x : Nat × Nat)
    (hx : RankSublevel B x) : Acc ScoreLT x := by
  have all : ∀ k : Nat, ∀ y : Nat × Nat,
      RankSublevel B y → scaledRank (200*B) y=k → Acc ScoreLT y := by
    intro k
    induction k using Nat.strong_induction_on with
    | h k ih =>
      intro y hy heq
      apply Acc.intro y
      intro z hstep
      have hz := rank_sublevel_preserved hstep hy
      have hsmall := scaledRank_strict hstep (rank_sublevel_bounds hy).2
        (rank_sublevel_bounds hz).2
      rw [heq] at hsmall
      exact ih (scaledRank (200*B) z) hsmall z hz rfl
  exact all (scaledRank (200*B) x) x hx rfl

/-- The rational height/clock order is actually well-founded on all natural
source/clock pairs. This is a proved theorem, not a ranking hypothesis. -/
theorem scoreLT_wellFounded : WellFounded ScoreLT := by
  constructor
  intro x
  apply scoreLT_accessible_on_sublevel (rankNumerator x) x
  have hpos := rank_denominator_positive x
  have h := Nat.mul_le_mul_left (rankNumerator x)
    (show 1≤rankDenominator x by omega)
  simpa [RankSublevel] using h

/-- Simultaneous induction for arbitrary goal kinds. Every premise crossing
to another kind must itself have a strictly smaller numerical score; changing
kind alone supplies no implication and does not discharge a proof obligation. -/
theorem common_rank_induction {ι : Sort u} (P : ι → Nat → Nat → Prop)
    (step : ∀ i n d,
      (∀ j m e, ScoreLT (m,e) (n,d) → P j m e) → P i n d) :
    ∀ i n d, P i n d := by
  have all : ∀ x : Nat × Nat, ∀ i, P i x.1 x.2 := by
    intro x
    induction x using scoreLT_wellFounded.induction with
    | h x ih =>
      intro i
      apply step i x.1 x.2
      intro j m e hsmall
      exact ih (m,e) hsmall j
  exact fun i n d => all (n,d) i

end CollatzGlobal
