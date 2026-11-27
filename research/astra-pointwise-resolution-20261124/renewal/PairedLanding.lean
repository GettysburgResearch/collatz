import Std

set_option maxRecDepth 10000

namespace PairedLanding

def step (x : Nat) : Nat :=
  if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def run : Nat → Nat → Nat
  | 0, x => x
  | h + 1, x => run h (step x)

theorem add_run (i j x : Nat) : run (i + j) x = run j (run i x) := by
  induction i generalizing x with
  | zero => simp [run]
  | succ i ih => rw [Nat.succ_add, run, run, ih]

private theorem even_row (s t n : Nat) :
    step ((2 * s) * n + 2 * t) = s * n + t := by
  unfold step
  rw [Nat.mul_assoc]
  split <;> omega

private theorem odd_row (s t n : Nat) :
    step ((2 * s) * n + (2 * t + 1)) = (3 * s) * n + (3 * t + 2) := by
  unfold step
  rw [Nat.mul_assoc, Nat.mul_assoc]
  split <;> omega

/-- One shared residue of the original parameter merges the two residual arms
    with their independent grades at a fixed physical clock. -/
theorem residual_cylinder (v : Nat) :
    run 6 (9 * (64 * v + 12) + 2) = 243 * v + 47 ∧
    run 6 (81 * (64 * v + 12) + 20) = 243 * v + 47 := by
  constructor
  · change run 6 (9 * (64 * v + 12) + 2) = _
    have h : 9 * (64 * v + 12) + 2 = 576 * v + 110 := by omega
    rw [h]
    change run 5 (step ((2 * 288) * v + 2 * 55)) = _
    rw [even_row]
    change run 4 (step ((2 * 144) * v + (2 * 27 + 1))) = _
    rw [odd_row]
    change run 3 (step ((2 * 216) * v + (2 * 41 + 1))) = _
    rw [odd_row]
    change run 2 (step ((2 * 324) * v + (2 * 62 + 1))) = _
    rw [odd_row]
    change run 1 (step ((2 * 486) * v + 2 * 94)) = _
    rw [even_row]
    exact even_row 243 47 v
  · have h : 81 * (64 * v + 12) + 20 = 5184 * v + 992 := by omega
    rw [h]
    change run 5 (step ((2 * 2592) * v + 2 * 496)) = _
    rw [even_row]
    change run 4 (step ((2 * 1296) * v + 2 * 248)) = _
    rw [even_row]
    change run 3 (step ((2 * 648) * v + 2 * 124)) = _
    rw [even_row]
    change run 2 (step ((2 * 324) * v + 2 * 62)) = _
    rw [even_row]
    change run 1 (step ((2 * 162) * v + 2 * 31)) = _
    rw [even_row]
    exact odd_row 81 15 v

private theorem halve_run (j y : Nat) : run j (2 ^ j * y) = y := by
  induction j with
  | zero => simp [run]
  | succ j ih =>
    rw [Nat.pow_succ', Nat.mul_assoc, run]
    have h : step (2 * (2 ^ j * y)) = 2 ^ j * y := by unfold step; split <;> omega
    rw [h, ih]

private theorem odd_predecessor (j x y : Nat)
    (eqn : 3 * x + 1 = 2 ^ (j + 1) * y) : run (j + 1) x = y := by
  rw [Nat.pow_succ', Nat.mul_assoc] at eqn
  have h : step x = 2 ^ j * y := by unfold step; split <;> omega
  rw [run, h, halve_run]

private theorem two_pow_unit (j : Nat) : (2 ^ j) % 3 = 1 ∨ (2 ^ j) % 3 = 2 := by
  induction j with
  | zero => decide
  | succ j ih =>
    rw [Nat.pow_succ, Nat.mul_mod]
    rcases ih with h | h <;> rw [h] <;> decide

/-- The single full two-gap affine equation forces both ordinary predecessors.
    The two gaps are positive; their sum can be prescribed before drawing a source. -/
theorem two_gap_router (u v y m : Nat)
    (row : 9 * m + 2 ^ (v + 1) + 3 = 2 ^ (v + 1) * (2 ^ (u + 1) * y)) :
    run ((v + 1) + (u + 1)) m = y := by
  let P := 2 ^ (v + 1)
  let Q := 2 ^ (u + 1) * y
  change 9 * m + P + 3 = P * Q at row
  have modrow : P % 3 = ((P % 3) * (Q % 3)) % 3 := by
    rw [← Nat.mul_mod]
    omega
  have qmod : Q % 3 = 1 := by
    rcases two_pow_unit (v + 1) with h | h
    · change P % 3 = 1 at h
      rw [h] at modrow
      omega
    · change P % 3 = 2 at h
      rw [h] at modrow
      omega
  let z := Q / 3
  have qeq : Q = 3 * z + 1 := by dsimp [z]; omega
  have peq : 3 * m + 1 = P * z := by
    rw [qeq, Nat.mul_add, Nat.mul_one, Nat.mul_left_comm P 3 z] at row
    omega
  rw [add_run, odd_predecessor v m z peq]
  exact odd_predecessor u z y qeq.symm

private def smallTrace : List Nat :=
  [29, 44, 22, 11, 17, 26, 13, 20, 10, 5, 8, 4, 2, 1]

private def largeTrace : List Nat :=
  [263, 395, 593, 890, 445, 668, 334, 167, 251, 377, 566, 283, 425, 638, 319,
   479, 719, 1079, 1619, 2429, 3644, 1822, 911, 1367, 2051, 3077, 4616, 2308,
   1154, 577, 866, 433, 650, 325, 488, 244, 122, 61, 92, 46, 23, 35, 53, 80,
   40, 20, 10, 5, 8, 4, 2, 1]

private theorem stays_in (xs : List Nat) (hc : xs.all (fun x => xs.contains (step x)) = true)
    (x h : Nat) (hx : x ∈ xs) : run h x ∈ xs := by
  induction h generalizing x with
  | zero => exact hx
  | succ h ih =>
    apply ih
    simpa using (List.all_eq_true.mp hc x hx)

/-- An ordered pair occurring at k=3 has incomparable forward targets,
    even though each actually reaches 1. -/
theorem concrete_incomparable :
    (∀ h, run h 29 ≠ 263) ∧ (∀ h, run h 263 ≠ 29) ∧
    run 13 29 = 1 ∧ run 51 263 = 1 := by
  constructor
  · intro h hit
    have hm := stays_in smallTrace (by decide) 29 h (by decide)
    rw [hit] at hm
    exact (by decide : 263 ∉ smallTrace) hm
  constructor
  · intro h hit
    have hm := stays_in largeTrace (by decide) 263 h (by decide)
    rw [hit] at hm
    exact (by decide : 29 ∉ largeTrace) hm
  decide

/-- A visit on either arm after common-clock fusion forces comparability
    with every independently timed target visit of the other arm. -/
theorem ordered_after_fusion {x y a b h i j : Nat}
    (merged : run h x = run h y) (hi : h ≤ i)
    (ha : run i x = a) (hb : run j y = b) :
    (∃ t, run t a = b) ∨ (∃ t, run t b = a) := by
  have fromx : run i y = a := by
    have decomp : i = h + (i - h) := by omega
    calc
      run i y = run (i - h) (run h y) := by conv => lhs; rw [decomp, add_run]
      _ = run (i - h) (run h x) := by rw [merged]
      _ = a := by rw [← add_run, ← decomp, ha]
  by_cases ij : i ≤ j
  · left
    refine ⟨j-i, ?_⟩
    rw [← fromx, ← add_run]
    have e : i + (j - i) = j := by omega
    rw [e, hb]
  · right
    refine ⟨i-j, ?_⟩
    rw [← hb, ← add_run]
    have e : j + (i - j) = i := by omega
    rw [e, fromx]



set_option maxRecDepth 20000
set_option maxHeartbeats 10000000

/-- Integer lower weights for $(3/2^e)^{2/5}$, scaled by 10,000. -/
def weights : Array Nat :=
  #[8913, 6754, 5119, 3879, 2940, 2228, 1688, 1279, 969, 735,
    557, 422, 319, 242, 183, 139, 105, 79, 60]

/-- One exact inverse generation at residue r. The preceding table uses one less trit. -/
def numerator (prev : Array Nat) (r : Nat) : Nat :=
  if r % 3 = 0 then 0 else
    (List.range 19).foldl (fun acc j =>
      let n := (2 ^ (j + 2)) * r - 1
      if n % 3 = 0 then acc + weights[j]! * prev[(n / 3) % prev.size]!
      else acc) 0

def row (prev : Array Nat) : Array Nat :=
  (Array.range (3 * prev.size)).map (numerator prev)

def lettersUnder : Bool := (List.range 19).all fun j =>
  decide ((weights[j]!) ^ 5 * 2 ^ (2 * (j + 2)) ≤ 9 * (10000 : Nat) ^ 5)

def fourStep : Bool := Id.run do
  let initial := #[0, 1, 1]
  let mut prev := initial
  for _ in [:4] do
    prev := row prev
  return prev.size == 243 && (List.range 243).all (fun r =>
    r % 3 == 0 || decide (10261932046877717 ≤ prev[r]!))

/-- The rationally rounded four-generation sum is above one on every unit. -/
theorem weights_and_four_step : lettersUnder = true ∧ fourStep = true := by
  decide +kernel


#print axioms weights_and_four_step
#print axioms add_run
#print axioms residual_cylinder
#print axioms two_gap_router
#print axioms concrete_incomparable
#print axioms ordered_after_fusion

end PairedLanding
