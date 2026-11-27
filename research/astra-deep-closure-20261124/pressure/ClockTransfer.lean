import Std

namespace FixedTargetPressure

def step (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3*n+1)/2

def state (n : Nat) : Nat → Nat
  | 0 => n
  | h+1 => step (state n h)

def grade (n : Nat) : Nat → Nat
  | 0 => 0
  | h+1 => grade n h + (state n h % 2)

private theorem stepBounds (n : Nat) : n ≤ 2*step n ∧ step n ≤ 2*n := by
  unfold step
  split <;> omega

/-- Transfer the actual height and grade forward or backward by a clock gap. -/
theorem clockGap (n h d : Nat) :
    state n (h+d) ≤ 2^d * state n h ∧ state n h ≤ 2^d * state n (h+d) ∧
    grade n h ≤ grade n (h+d) ∧ grade n (h+d) ≤ grade n h + d := by
  induction d with
  | zero => simp
  | succ d ih =>
    obtain ⟨ha,hb,hc,hd⟩ := ih
    obtain ⟨he,hf⟩ := stepBounds (state n (h+d))
    simp only [Nat.add_succ, state, grade, Nat.pow_succ]
    refine ⟨?_, ?_, ?_, ?_⟩
    · calc
        _ ≤ 2 * (2^d * state n h) := Nat.le_trans hf (Nat.mul_le_mul_left 2 ha)
        _ = _ := by ac_rfl
    · calc
        _ ≤ 2^d * (2 * step (state n (h+d))) := Nat.le_trans hb (Nat.mul_le_mul_left _ he)
        _ = _ := by ac_rfl
    · change grade n h ≤ grade n (h+d) + state n (h+d) % 2
      omega
    · change grade n (h+d) + state n (h+d) % 2 ≤ (grade n h + d) + 1
      omega

/-- Every nearby clock has height at most exponentially larger and grade
within the clock gap. Both clocks refer to the same positive ordinary path. -/
theorem pullBackWitness (n e h R H P W : Nat) (near₁ : e ≤ h+R) (near₂ : h ≤ e+R)
    (height : state n h ≤ H) (low : P ≤ grade n h + W) (high : grade n h ≤ P+W) :
    state n e ≤ 2^R*H ∧ P ≤ grade n e + (W+R) ∧ grade n e ≤ P+(W+R) := by
  rcases Nat.le_total h e with he | eh
  · let d := e-h
    have eqn : h+d=e := by dsimp [d]; omega
    have dr : d ≤ R := by dsimp [d]; omega
    obtain ⟨ha,_,hc,hd⟩ := clockGap n h d
    rw [eqn] at ha hc hd
    have hp : 2^d ≤ 2^R := Nat.pow_le_pow_right (by decide) dr
    exact ⟨Nat.le_trans ha (Nat.mul_le_mul hp height), by omega, by omega⟩
  · let d := h-e
    have eqn : e+d=h := by dsimp [d]; omega
    have dr : d ≤ R := by dsimp [d]; omega
    obtain ⟨_,hb,hc,hd⟩ := clockGap n e d
    rw [eqn] at hb hc hd
    have hp : 2^d ≤ 2^R := Nat.pow_le_pow_right (by decide) dr
    exact ⟨Nat.le_trans hb (Nat.mul_le_mul hp height), by omega, by omega⟩

private def totalOccupancy : List Nat → List Nat → Nat
  | [], _ => 0
  | k::ks, samples => samples.count k + totalOccupancy ks samples

private theorem occupancyCons (keys samples : List Nat) (a : Nat) :
    totalOccupancy keys (a::samples) = totalOccupancy keys samples + keys.count a := by
  induction keys with
  | nil => simp [totalOccupancy]
  | cons k ks ih =>
    simp only [totalOccupancy, List.count_cons, ih]
    by_cases hk : k = a
    · subst k; simp; omega
    · have ha : a ≠ k := Ne.symm hk
      simp [hk, ha, Nat.add_assoc]

private theorem occupancyCovers (keys samples : List Nat)
    (covered : ∀ a ∈ samples, a ∈ keys) : samples.length ≤ totalOccupancy keys samples := by
  induction samples with
  | nil => simp
  | cons a tail ih =>
    have pos : 0 < keys.count a := List.count_pos_iff.mpr (covered a (by simp))
    have h := ih (fun z hz => covered z (List.mem_cons_of_mem a hz))
    rw [occupancyCons, List.length_cons]
    omega

private theorem occupancyUpper (keys samples : List Nat) (cap : Nat)
    (upper : ∀ k ∈ keys, samples.count k ≤ cap) :
    totalOccupancy keys samples ≤ keys.length * cap := by
  induction keys with
  | nil => simp [totalOccupancy]
  | cons k ks ih =>
    have h := ih (fun z hz => upper z (List.mem_cons_of_mem k hz))
    have hk := upper k (by simp)
    simp only [totalOccupancy, List.length_cons, Nat.succ_mul]
    omega

/-- Count one exact record per source, with arbitrary dependence across the
arms. More sources than the displayed capacity force one crowded record. -/
theorem exactRecordFiber (keys samples : List Nat) (cap : Nat)
    (covered : ∀ a ∈ samples, a ∈ keys) (excess : keys.length * cap < samples.length) :
    ∃ k ∈ keys, cap < samples.count k := by
  apply Classical.byContradiction
  intro hn
  have upper : ∀ k ∈ keys, samples.count k ≤ cap := by
    intro k hk
    apply Nat.le_of_not_gt
    intro h
    exact hn ⟨k,hk,h⟩
  have h₁ := occupancyCovers keys samples covered
  have h₂ := occupancyUpper keys samples cap upper
  omega

/-- A single legal local paired return can follow an anchored failed word.
The concatenation retains the old unequal endpoint. -/
theorem localVersusAnchored : state 72817 17 = 5 ∧ state (5*72817) 17 = 25 ∧
    grade 72817 17 = 2 ∧ grade (5*72817) 17 = 2 ∧
    state 72817 21 = 1 ∧ state (5*72817) 21 = 44 := by decide

#print axioms clockGap
#print axioms pullBackWitness
#print axioms exactRecordFiber
#print axioms localVersusAnchored
end FixedTargetPressure
