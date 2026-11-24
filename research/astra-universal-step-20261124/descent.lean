import Std

namespace Collatz.PoweredInverse

/-- Chronological binary shortcut histories. An integral odd edge forces its source odd. -/
inductive Runs : List Bool → Int → Int → Prop where
  | nil (x : Int) : Runs [] x x
  | even {w x y} : Runs w x y → Runs (false :: w) (2*x) y
  | odd {w x z y} : 2*z = 3*x+1 → Runs w z y → Runs (true :: w) x y

def odds : List Bool → Nat
  | [] => 0
  | false :: w => odds w
  | true :: w => odds w + 1

def A (w : List Bool) : Int := 3 ^ odds w
def B (w : List Bool) : Int := 2 ^ w.length

def carry : List Bool → Int
  | [] => 0
  | false :: w => 2 * carry w
  | true :: w => A w + 2 * carry w

theorem affine {w x y} (h : Runs w x y) : B w * y = A w * x + carry w := by
  induction h with
  | nil x => simp [B, A, odds, carry]
  | @even w x y _ ih =>
    simp only [B, List.length_cons, Int.pow_succ] at *
    simp only [A, odds, carry] at *
    calc
      2 ^ w.length * 2 * y = 2 * (2 ^ w.length * y) := by ac_rfl
      _ = _ := by rw [ih]; grind
  | @odd w x z y he _ ih =>
    simp only [B, List.length_cons, Int.pow_succ] at *
    simp only [A, odds, carry, Int.pow_succ] at *
    calc
      2 ^ w.length * 2 * y = 2 * (2 ^ w.length * y) := by ac_rfl
      _ = 3 ^ odds w * (2*z) + 2 * carry w := by rw [ih]; grind
      _ = _ := by rw [he]; grind

def deviation (w : List Bool) (z : Int) := (B w - A w) * z - carry w

/-- Each copy uses the same chronological word on a literal intermediate integer. -/
def Powers (w : List Bool) : Nat → Int → Int → Prop
  | 0, x, y => x = y
  | r+1, x, y => ∃ z, Runs w x z ∧ Powers w r z y

private theorem one_transport {w x y} (h : Runs w x y) :
    B w * deviation w y = A w * deviation w x := by
  unfold deviation
  calc
    _ = (B w-A w)*(B w*y) - B w*carry w := by grind
    _ = _ := by rw [affine h]; grind

theorem powered_identity {w r x y} (h : Powers w r x y) :
    B w ^ r * deviation w y = A w ^ r * deviation w x := by
  induction r generalizing x with
  | zero => change x = y at h; simp [h]
  | succ r ih =>
    obtain ⟨z, hz, hrest⟩ := h
    rw [Int.pow_succ, Int.pow_succ]
    calc
      _ = B w * (B w ^ r * deviation w y) := by ac_rfl
      _ = A w ^ r * (B w * deviation w z) := by rw [ih hrest]; ac_rfl
      _ = _ := by rw [one_transport hz]; ac_rfl

/-- Includes the empty word, all-even words, zero copies, and stationary endpoints. -/
theorem powered_divides {w r x y} (h : Powers w r x y) :
    (3 ^ odds w) ^ r ∣ (deviation w y).natAbs := by
  have hh := congrArg Int.natAbs (powered_identity h)
  simp only [Int.natAbs_mul, Int.natAbs_pow, B, A] at hh
  change (2 ^ w.length) ^ r * (deviation w y).natAbs =
    (3 ^ odds w) ^ r * (deviation w x).natAbs at hh
  have cop := (Nat.Coprime.pow (odds w) w.length (by decide : Nat.Coprime 3 2)).pow r r
  exact cop.dvd_of_dvd_mul_left ⟨_, hh⟩

theorem nonstationary_bound {w r x y} (h : Powers w r x y)
    (hne : deviation w y ≠ 0) :
    (3 ^ odds w) ^ r ≤ (deviation w y).natAbs :=
  Nat.le_of_dvd (Int.natAbs_pos.mpr hne) (powered_divides h)

/-- On a literal edge, zero deviation means that one copy fixes the endpoint. -/
theorem stationary_copy {w x y} (h : Runs w x y) (hz : deviation w y = 0) : x = y := by
  have edge := affine h
  unfold deviation at hz
  have identical : A w * x = A w * y := by grind
  have nonzero : A w ≠ 0 := Int.ne_of_gt (Int.pow_pos (by decide : (0 : Int) < 3))
  exact Int.eq_of_mul_eq_mul_left nonzero identical

/-- The actual positive shortcut map supplies a literal history at every length. -/
def step (x : Nat) : Nat := if x % 2 = 0 then x / 2 else (3*x+1)/2

def itinerary : Nat → Nat → List Bool
  | 0, _ => []
  | n+1, x => decide (x % 2 = 1) :: itinerary n (step x)

def walk : Nat → Nat → Nat
  | 0, x => x
  | n+1, x => walk n (step x)

theorem actual_runs (n x : Nat) :
    Runs (itinerary n x) (x : Int) ((walk n x : Nat) : Int) := by
  induction n generalizing x with
  | zero => exact Runs.nil _
  | succ n ih =>
    simp only [itinerary, walk]
    by_cases he : x % 2 = 0
    · have hh : decide (x % 2 = 1) = false := by simp [he]
      rw [hh]
      have eqx : (x : Int) = 2 * (step x : Int) := by simp [step, he]; omega
      exact eqx.symm ▸ Runs.even (ih (step x))
    · have ho : x % 2 = 1 := by omega
      simp only [ho, decide_true]
      exact Runs.odd (by simp [step, he]; omega) (ih (step x))

/-- Two potentially distinct chronological blocks with the same clock and odd count. -/
theorem pair_identity {w₁ w₂ x z y} (h₁ : Runs w₁ x z) (h₂ : Runs w₂ z y)
    (hc : B w₁ = B w₂) (hp : A w₁ = A w₂) :
    B w₂ ^ 2 * deviation w₂ y = A w₂ ^ 2 * deviation w₁ x
      + A w₂ * B w₂ * (carry w₁ - carry w₂) := by
  have e₁ := one_transport h₁
  rw [hc, hp] at e₁
  have e₂ := one_transport h₂
  have diff : deviation w₂ z = deviation w₁ z + (carry w₁ - carry w₂) := by
    unfold deviation
    rw [hc, hp]
    omega
  calc
    _ = B w₂ * (B w₂ * deviation w₂ y) := by grind
    _ = A w₂ * (B w₂ * deviation w₁ z) + A w₂ * B w₂ * (carry w₁-carry w₂) := by
      rw [e₂, diff]; grind
    _ = _ := by rw [e₁]; grind

theorem matching_pair_divides {w₁ w₂ x z y} (h₁ : Runs w₁ x z) (h₂ : Runs w₂ z y)
    (hc : B w₁ = B w₂) (hp : A w₁ = A w₂) (hm : A w₂ ∣ carry w₁ - carry w₂) :
    (3 ^ odds w₂) ^ 2 ∣ (deviation w₂ y).natAbs := by
  obtain ⟨k, hk⟩ := hm
  have id := pair_identity h₁ h₂ hc hp
  rw [hk] at id
  have factored : B w₂ ^ 2 * deviation w₂ y =
      A w₂ ^ 2 * (deviation w₁ x + B w₂*k) := by rw [id]; grind
  have ab := congrArg Int.natAbs factored
  simp only [Int.natAbs_mul, Int.natAbs_pow, B, A] at ab
  change (2 ^ w₂.length) ^ 2 * (deviation w₂ y).natAbs =
    (3 ^ odds w₂) ^ 2 * (deviation w₁ x + B w₂*k).natAbs at ab
  have cop := (Nat.Coprime.pow (odds w₂) w₂.length (by decide : Nat.Coprime 3 2)).pow 2 2
  exact cop.dvd_of_dvd_mul_left ⟨_, ab⟩

#print axioms Collatz.PoweredInverse.pair_identity
#print axioms Collatz.PoweredInverse.matching_pair_divides
#print axioms Collatz.PoweredInverse.stationary_copy
#print axioms Collatz.PoweredInverse.actual_runs
#print axioms Collatz.PoweredInverse.affine
#print axioms Collatz.PoweredInverse.powered_identity
#print axioms Collatz.PoweredInverse.powered_divides
#print axioms Collatz.PoweredInverse.nonstationary_bound
end Collatz.PoweredInverse
