import Std

namespace MinimumRunClock

def step (x : Nat) : Nat :=
  if x % 2 = 0 then x / 2 else (3*x+1)/2

def five (x : Nat) : Nat := step (step (step (step (step x))))

theorem block (u : Nat) :
    let x := 32*u+15
    step x = 48*u+23 ∧
    step (step x) = 72*u+35 ∧
    step (step (step x)) = 108*u+53 ∧
    step (step (step (step x))) = 162*u+80 ∧
    five x = 81*u+40 := by
  dsimp only
  have a : step (32*u+15) = 48*u+23 := by
    simp only [step]; split <;> omega
  have b : step (48*u+23) = 72*u+35 := by
    simp only [step]; split <;> omega
  have c : step (72*u+35) = 108*u+53 := by
    simp only [step]; split <;> omega
  have d : step (108*u+53) = 162*u+80 := by
    simp only [step]; split <;> omega
  have e : step (162*u+80) = 81*u+40 := by
    simp only [step]; split <;> omega
  simp only [five, a, b, c, d, e, and_self]

def Runs : Nat → Nat → Prop
  | 0, _ => True
  | k+1, x => x%32=15 ∧ x < five x ∧ Runs k (five x)

/-- A sufficient exact budget for k physical expanding runs. -/
theorem runs_of_dvd (k x : Nat) (h : 32^k ∣ 49*x+65) : Runs k x := by
  induction k generalizing x with
  | zero => trivial
  | succ k ih =>
    obtain ⟨w, hw⟩ := h
    rw [Nat.pow_succ, Nat.mul_right_comm] at hw
    have hr : x%32=15 := by omega
    let u := x/32
    have hx : x=32*u+15 := by dsimp [u]; omega
    have hf : five x=81*u+40 :=
      (congrArg five hx).trans (block u).2.2.2.2
    refine ⟨hr, by omega, ih _ ⟨81*w, ?_⟩⟩
    rw [Nat.mul_left_comm]
    omega

private theorem cancel81 (k a : Nat) (h : 32^k ∣ 81*a) : 32^k ∣ a := by
  induction k generalizing a with
  | zero => simp
  | succ k ih =>
    obtain ⟨w, hw⟩ := h
    rw [Nat.pow_succ, Nat.mul_right_comm] at hw
    have ha : a=32*(a/32) := by omega
    have hdiv : 32^k ∣ 81*(a/32) := ⟨w, by omega⟩
    obtain ⟨v, hv⟩ := ih _ hdiv
    refine ⟨v, ?_⟩
    rw [Nat.pow_succ, Nat.mul_right_comm, ← hv]
    omega

/-- A fixed source can finance only as many repeated blocks as its own
    divisibility permits, even when K different sources can finance K blocks. -/
theorem dvd_of_runs (k x : Nat) (h : Runs k x) : 32^k ∣ 49*x+65 := by
  induction k generalizing x with
  | zero => simp
  | succ k ih =>
    obtain ⟨hr, _, tail⟩ := h
    let u := x/32
    have hx : x = 32*u+15 := by dsimp [u]; omega
    have hf : five x=81*u+40 :=
      (congrArg five hx).trans (block u).2.2.2.2
    have hd := ih _ tail
    have he : 49*(five x)+65=81*(49*u+25) := by omega
    rw [he] at hd
    obtain ⟨w, hw⟩ := cancel81 _ _ hd
    refine ⟨w, ?_⟩
    rw [Nat.pow_succ, Nat.mul_right_comm, ← hw]
    omega

theorem clock_iff (k x : Nat) : Runs k x ↔ 32^k ∣ 49*x+65 :=
  ⟨dvd_of_runs k x, runs_of_dvd k x⟩

theorem each_source_exits (x : Nat) : ∃ k, ¬Runs k x := by
  have growth (k : Nat) : k < 32^k := by
    induction k with
    | zero => decide
    | succ k ih => rw [Nat.pow_succ]; omega
  refine ⟨49*x+65, ?_⟩
  intro hr
  have upper := Nat.le_of_dvd (by omega : 0 < 49*x+65)
    ((clock_iff _ _).mp hr)
  exact (Nat.not_le_of_gt (growth (49*x+65))) upper

#print axioms clock_iff
#print axioms each_source_exits
end MinimumRunClock
