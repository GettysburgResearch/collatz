import UpDownRayBand

namespace CollatzResearch.GuardedHoles

open CollatzResearch.UpDownRayBand (up down)

/-- A gate marks the actual downward departures of an arbitrary permitted map. -/
def step (gate : Nat → Prop) [DecidablePred gate] (x : Nat) : Nat :=
  if gate x then down x else up x

/-- Spacing of the holes protects the two sites after any downward departure. -/
theorem separated_guards (H : Nat → Prop) (large : ∀ h, H h → 8 ≤ h)
    (gap : ∀ a b, H a → H b → a < b → 2*a < b) {h : Nat} (hh : H h) :
    ¬H (down h) ∧ ¬H (up (down h)) := by
  have hlarge := large h hh
  have bounds : h ≤ 2*down h ∧ down h < h ∧
      h ≤ 2*up (down h) ∧ up (down h) < h := by
    unfold up down
    omega
  constructor
  · intro hd
    have hgap := gap (down h) h hd hh bounds.2.1
    omega
  · intro hu
    have hgap := gap (up (down h)) h hu hh bounds.2.2.2
    omega

/-- Once each used downward departure has two protected successors, every
three-step block gains at least 9/8, even when the first step is upward. -/
theorem guarded_growth (gate : Nat → Prop) [DecidablePred gate]
    (guards : ∀ z, gate z → ¬gate (down z) ∧ ¬gate (up (down z))) (x : Nat) :
    9*x ≤ 8*step gate (step gate (step gate x)) := by
  by_cases g0 : gate x
  · obtain ⟨g1,g2⟩ := guards x g0
    simp only [step, ite_eq_left g0, ite_eq_right g1, ite_eq_right g2]
    unfold up down
    omega
  · by_cases g1 : gate (up x)
    · have g2 := (guards (up x) g1).1
      simp only [step, ite_eq_right g0, ite_eq_left g1, ite_eq_right g2]
      unfold up down
      omega
    · by_cases g2 : gate (up (up x))
      · simp only [step, ite_eq_right g0, ite_eq_right g1, ite_eq_left g2]
        unfold up down
        omega
      · simp only [step, ite_eq_right g0, ite_eq_right g1, ite_eq_right g2]
        unfold up
        omega

/-- Each superset of the forced-up set has the same lower multiplier. -/
theorem separated_growth (H gate : Nat → Prop) [DecidablePred gate]
    (large : ∀ h, H h → 8 ≤ h) (gap : ∀ a b, H a → H b → a < b → 2*a < b)
    (permitted : ∀ z, gate z → H z) (x : Nat) :
    9*x ≤ 8*step gate (step gate (step gate x)) := by
  apply guarded_growth gate _ x
  intro z gz
  obtain ⟨a,b⟩ := separated_guards H large gap (permitted z gz)
  exact ⟨fun gd => a (permitted _ gd), fun gu => b (permitted _ gu)⟩

/-- The integer estimates for the automatic hole bands [B,5B/4). -/
theorem band_guards {B h : Nat} (hB : 64 ≤ B) (lo : B ≤ h) (hi : 4*h < 5*B) :
    5*B < 16*down h ∧ down h < B ∧ 5*B < 16*up (down h) ∧ up (down h) < B := by
  unfold up down
  omega

/-- The explicit binary-regular hole set. -/
def bandHole (h : Nat) : Prop :=
  ∃ j : Nat, 3 ≤ j ∧ 4^j ≤ h ∧ 4*h < 5*4^j

private theorem between_bands {y j : Nat} (lo : 5*4^j < 16*y)
    (hi : y < 4^j) : ¬bandHole y := by
  intro hy
  obtain ⟨k,_,hk,hk'⟩ := hy
  by_cases hkj : k < j
  · have hp : (4 : Nat)^(k+1) ≤ 4^j := Nat.pow_le_pow_right (by decide) hkj
    rw [Nat.pow_succ] at hp
    omega
  · have hp : (4 : Nat)^j ≤ 4^k := Nat.pow_le_pow_right (by decide) (by omega)
    omega

/-- Both protected successors are outside every band, including all earlier bands. -/
theorem band_exclusion {h : Nat} (hh : bandHole h) :
    ¬bandHole (down h) ∧ ¬bandHole (up (down h)) := by
  obtain ⟨j,hj,lo,hi⟩ := hh
  have hB : (4 : Nat)^3 ≤ 4^j := Nat.pow_le_pow_right (by decide) hj
  obtain ⟨a,b,c,d⟩ := band_guards (B := 4^j) hB lo hi
  exact ⟨between_bands a b, between_bands c d⟩

/-- Every permitted map for the concrete automatic forced-up set grows by
at least 9/8 every three steps. -/
theorem band_growth (gate : Nat → Prop) [DecidablePred gate]
    (permitted : ∀ z, gate z → bandHole z) (x : Nat) :
    9*x ≤ 8*step gate (step gate (step gate x)) := by
  apply guarded_growth gate _ x
  intro z gz
  obtain ⟨a,b⟩ := band_exclusion (permitted z gz)
  exact ⟨fun gd => a (permitted _ gd), fun gu => b (permitted _ gu)⟩

/-- Along the continuation D then repeated U, either the third state is in
the current band, or the sixth is in the next band and the intervening three
states are in the gap. The preceding two guards are in `band_guards`. -/
theorem band_return {B h : Nat} (hB : 64 ≤ B) (lo : B ≤ h) (hi : 4*h < 5*B) :
    let z2 := up (up (down h))
    let z3 := up z2
    let z4 := up z3
    let z5 := up z4
    (B ≤ z2 ∧ 4*z2 < 5*B) ∨
    (5*B ≤ 4*z2 ∧ z2 < 4*B ∧ 5*B ≤ 4*z3 ∧ z3 < 4*B ∧
      5*B ≤ 4*z4 ∧ z4 < 4*B ∧ 4*B ≤ z5 ∧ z5 < 5*B) := by
  dsimp only
  by_cases hz : 4*up (up (down h)) < 5*B
  · left
    refine ⟨?_,hz⟩
    unfold up down
    omega
  · right
    unfold up down at hz ⊢
    omega

end CollatzResearch.GuardedHoles
