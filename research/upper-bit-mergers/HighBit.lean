import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace CollatzUpperBit

def step (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def orbit (x : ℕ) : ℕ → ℕ
  | 0 => x
  | h + 1 => step (orbit x h)

def odds (x : ℕ) : ℕ → ℕ
  | 0 => 0
  | h + 1 => if orbit x h % 2 = 0 then odds x h else odds x h + 1

def evens (x : ℕ) : ℕ → ℕ
  | 0 => 0
  | h + 1 => if orbit x h % 2 = 0 then evens x h + 1 else evens x h

def offset (x : ℕ) : ℕ → ℕ
  | 0 => 0
  | h + 1 =>
    if orbit x h % 2 = 0 then offset x h else 3 * offset x h + 2 ^ h

theorem counts (x h : ℕ) : odds x h + evens x h = h := by
  induction h with
  | zero => rfl
  | succ h ih =>
    by_cases he : orbit x h % 2 = 0 <;> simp [odds, evens, he] <;> omega

theorem affine (x h : ℕ) :
    2 ^ h * orbit x h = 3 ^ odds x h * x + offset x h := by
  induction h with
  | zero => simp [orbit, odds, offset]
  | succ h ih =>
    by_cases he : orbit x h % 2 = 0
    · have hs : 2 * step (orbit x h) = orbit x h := by
        simp only [step, ite_eq_left he]
        omega
      simp only [orbit, odds, offset, ite_eq_left he, pow_succ]
      rw [Nat.mul_assoc, hs, ih]
    · have hs : 2 * step (orbit x h) = 3 * orbit x h + 1 := by
        simp only [step, ite_eq_right he]
        omega
      simp only [orbit, odds, offset, ite_eq_right he, pow_succ]
      rw [Nat.mul_assoc, hs]
      calc
        2 ^ h * (3 * orbit x h + 1) = 3 * (2 ^ h * orbit x h) + 2 ^ h := by ring
        _ = _ := by rw [ih]; ring

theorem offset_budget (x h : ℕ) :
    offset x h + 2 ^ h ≤ 2 ^ evens x h * 3 ^ odds x h := by
  induction h with
  | zero => simp [offset, evens, odds]
  | succ h ih =>
    by_cases he : orbit x h % 2 = 0
    · simp only [offset, evens, odds, ite_eq_left he, pow_succ]
      calc
        offset x h + 2 ^ h * 2 ≤ 2 * (offset x h + 2 ^ h) := by omega
        _ ≤ 2 * (2 ^ evens x h * 3 ^ odds x h) := Nat.mul_le_mul_left 2 ih
        _ = _ := by ring
    · simp only [offset, evens, odds, ite_eq_right he, pow_succ]
      calc
        3 * offset x h + 2 ^ h + 2 ^ h * 2 = 3 * (offset x h + 2 ^ h) := by ring
        _ ≤ 3 * (2 ^ evens x h * 3 ^ odds x h) := Nat.mul_le_mul_left 3 ih
        _ = _ := by ring

private theorem step_add_even (x m : ℕ) :
    step (x + 2 * m) = step x + (if x % 2 = 0 then 1 else 3) * m := by
  have he : (x + 2 * m) % 2 = x % 2 := by omega
  by_cases hp : x % 2 = 0 <;> simp [step, he, hp] <;> omega

theorem high_bit (x h m : ℕ) :
    orbit (x + 2 ^ h * m) h = orbit x h + 3 ^ odds x h * m := by
  induction h generalizing m with
  | zero => simp [orbit, odds]
  | succ h ih =>
    simp only [orbit, pow_succ, Nat.mul_assoc]
    rw [ih]
    rw [show 3 ^ odds x h * (2 * m) = 2 * (3 ^ odds x h * m) by ring, step_add_even]
    by_cases he : orbit x h % 2 = 0
    · simp [odds, he]
    · simp [odds, he, pow_succ]
      ring

/-- A meeting with small nonnegative normalized offsets forces its starting
position into a short interval determined only by the ratio of slopes. -/
theorem meeting_window {v u w d R : ℝ} (hv : 0 < v) (hv' : v ≤ 9 / 8)
    (hu : 0 ≤ u) (hu' : u ≤ d) (hw : 0 ≤ w) (hw' : w ≤ d) (hd : d ≤ 1 / 8)
    (meet : R * (v + u) = v + 1 + w) :
    3 / 2 ≤ R ∧ |v - 1 / (R - 1)| ≤ 3 * d := by
  have hR : 3 / 2 ≤ R := by
    by_contra! h
    have hh := mul_lt_mul_of_pos_right h (add_pos_of_pos_of_nonneg hv hu)
    linarith
  have hden : 0 < R - 1 := by linarith
  have hd0 : 0 ≤ d := hu.trans hu'
  have hRu0 : 0 ≤ R * u := mul_nonneg (by linarith) hu
  have hRu : R * u ≤ R * d := mul_le_mul_of_nonneg_left hu' (by linarith)
  have h3 : R * d ≤ 3 * d * (R - 1) := by nlinarith [mul_nonneg hd0 (show 0 ≤ 2 * R - 3 by linarith)]
  have h1 : d ≤ 3 * d * (R - 1) := by nlinarith [mul_nonneg hd0 (show 0 ≤ 3 * R - 4 by linarith)]
  refine ⟨hR, abs_le.mpr ⟨?_, ?_⟩⟩
  · have hh : 1 / (R - 1) ≤ v + 3 * d := (div_le_iff₀ hden).2 (by nlinarith)
    linarith
  · have hh : v - 3 * d ≤ 1 / (R - 1) := (le_div_iff₀ hden).2 (by nlinarith)
    linarith

noncomputable def slope (x h : ℕ) : ℝ := (3 : ℝ) ^ odds x h / 2 ^ h

noncomputable def normalizedOffset (x h : ℕ) : ℝ := (offset x h : ℝ) / 3 ^ odds x h

theorem orbit_real (x h : ℕ) :
    (orbit x h : ℝ) = slope x h * ((x : ℝ) + normalizedOffset x h) := by
  have ha : (2 : ℝ) ^ h * (orbit x h : ℝ) =
      3 ^ odds x h * (x : ℝ) + (offset x h : ℝ) := by exact_mod_cast affine x h
  unfold slope normalizedOffset
  field_simp
  nlinarith

theorem normalized_budget (x h B : ℕ) (hb : evens x h ≤ B) :
    normalizedOffset x h ≤ (2 : ℝ) ^ B := by
  have hb' : (offset x h : ℝ) + (2 : ℝ) ^ h ≤
      2 ^ evens x h * 3 ^ odds x h := by exact_mod_cast offset_budget x h
  unfold normalizedOffset
  apply (div_le_iff₀ (by positivity : 0 < (3 : ℝ) ^ odds x h)).2
  calc
    (offset x h : ℝ) ≤ 2 ^ evens x h * 3 ^ odds x h := by linarith [show 0 < (2 : ℝ) ^ h by positivity]
    _ ≤ 2 ^ B * 3 ^ odds x h := by
      gcongr
      norm_num

/-- The exact scaled endpoint stays within a parity-dependent distance of
the initial point on its dyadic grid. -/
theorem prefix_position (r h : ℕ) :
    0 ≤ (orbit r h : ℝ) / 3 ^ odds r h - (r : ℝ) / 2 ^ h ∧
    (orbit r h : ℝ) / 3 ^ odds r h - (r : ℝ) / 2 ^ h ≤ 1 / 2 ^ odds r h := by
  have hr : (orbit r h : ℝ) / 3 ^ odds r h - (r : ℝ) / 2 ^ h =
      normalizedOffset r h / 2 ^ h := by
    rw [orbit_real]
    unfold slope
    field_simp
    ring
  rw [hr]
  have hp : (2 : ℝ) ^ h = 2 ^ odds r h * 2 ^ evens r h := by rw [← pow_add, counts]
  constructor
  · unfold normalizedOffset
    positivity
  · calc
      normalizedOffset r h / 2 ^ h ≤ (2 : ℝ) ^ evens r h / 2 ^ h :=
        div_le_div_of_nonneg_right (normalized_budget r h (evens r h) le_rfl) (by positivity)
      _ = 1 / 2 ^ odds r h := by rw [hp]; field_simp

/-- A certificate with two arbitrary clocks for actual positive orbits forces
the scaled start into the interval centered at the ratio of their slopes. -/
theorem orbit_meeting_window (x g i j B : ℕ) (hx : 0 < x) (hg : 0 < g)
    (hv : (x : ℝ) / g ≤ 9 / 8) (hb : (2 : ℝ) ^ B / g ≤ 1 / 8)
    (h1 : evens x i ≤ B) (h2 : evens (x + g) j ≤ B)
    (meet : orbit x i = orbit (x + g) j) :
    let R := slope x i / slope (x + g) j
    3 / 2 ≤ R ∧ |(x : ℝ) / g - 1 / (R - 1)| ≤ 3 * (2 ^ B / g) := by
  have hg' : (0 : ℝ) < g := by exact_mod_cast hg
  have hs : 0 < slope (x + g) j := by unfold slope; positivity
  have ha := congrArg (fun z : ℕ => (z : ℝ)) meet
  change (orbit x i : ℝ) = (orbit (x + g) j : ℝ) at ha
  rw [orbit_real x i, orbit_real (x + g) j, Nat.cast_add] at ha
  apply meeting_window (u := normalizedOffset x i / g)
      (w := normalizedOffset (x + g) j / g) (by positivity) hv
  · unfold normalizedOffset
    positivity
  · exact div_le_div_of_nonneg_right (normalized_budget x i B h1) hg'.le
  · unfold normalizedOffset
    positivity
  · exact div_le_div_of_nonneg_right (normalized_budget (x + g) j B h2) hg'.le
  · exact hb
  · field_simp [hs.ne', hg'.ne']
    linarith

/-- The auxiliary positive map induced by applying the shortcut map to -x. -/
def mirrorStep (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3 * x - 1) / 2

def mirrorOrbit (x : ℕ) : ℕ → ℕ
  | 0 => x
  | h + 1 => mirrorStep (mirrorOrbit x h)

def mirrorOdds (x : ℕ) : ℕ → ℕ
  | 0 => 0
  | h + 1 => if mirrorOrbit x h % 2 = 0 then mirrorOdds x h else mirrorOdds x h + 1

private theorem mirror_positive (x h : ℕ) (hx : 0 < x) : 0 < mirrorOrbit x h := by
  induction h with
  | zero => exact hx
  | succ h ih =>
    simp only [mirrorOrbit, mirrorStep]
    split <;> omega

private theorem mirror_step_sum (x y q : ℕ) (hy : 0 < y) (hs : x + y = 2 * q) :
    step x + mirrorStep y = (if y % 2 = 0 then 1 else 3) * q := by
  have he : x % 2 = y % 2 := by omega
  by_cases hp : y % 2 = 0 <;> simp [step, mirrorStep, he, hp] <;> omega

/-- Complementary starts follow the same parity word while their sum is
divisible by the corresponding power of two. -/
theorem mirror_lift (r p h m : ℕ) (hp : 0 < p) (hs : r + p = 2 ^ h * m) :
    orbit r h + mirrorOrbit p h = 3 ^ mirrorOdds p h * m ∧ odds r h = mirrorOdds p h := by
  induction h generalizing m with
  | zero => simpa [orbit, mirrorOrbit, odds, mirrorOdds] using hs
  | succ h ih =>
    obtain ⟨ha, ho⟩ := ih (2 * m) (by simpa [pow_succ, Nat.mul_assoc] using hs)
    have hsum : orbit r h + mirrorOrbit p h = 2 * (3 ^ mirrorOdds p h * m) := by
      rw [ha]
      ring
    have he : orbit r h % 2 = mirrorOrbit p h % 2 := by omega
    constructor
    · rw [orbit, mirrorOrbit, mirror_step_sum _ _ _ (mirror_positive p h hp) hsum]
      by_cases hh : mirrorOrbit p h % 2 = 0 <;> simp [mirrorOdds, hh, pow_succ]
      ring
    · simp [odds, mirrorOdds, he, ho]

theorem one_step_pair (m : ℕ) : step (4 * m + 1) = 6 * m + 2 ∧
    step (12 * m + 4) = 6 * m + 2 := by
  have ho : (4 * m + 1) % 2 ≠ 0 := by omega
  have he : (12 * m + 4) % 2 = 0 := by omega
  simp [step, ho, he]
  omega

def Meets (x y : ℕ) : Prop := ∃ i j, orbit x i = orbit y j

private theorem orbit_add (x i j : ℕ) : orbit x (i + j) = orbit (orbit x i) j := by
  induction j with
  | zero => rfl
  | succ j ih => exact congrArg step ih

private theorem meets_symm {x y : ℕ} (h : Meets x y) : Meets y x := by
  obtain ⟨i, j, hij⟩ := h
  exact ⟨j, i, hij.symm⟩

private theorem meets_trans {x y z : ℕ} (hxy : Meets x y) (hyz : Meets y z) : Meets x z := by
  obtain ⟨a, b, hab⟩ := hxy
  obtain ⟨c, d, hcd⟩ := hyz
  refine ⟨a + c, d + b, ?_⟩
  rw [orbit_add x, hab, ← orbit_add, Nat.add_comm b c, orbit_add y, hcd, ← orbit_add]

private theorem meets_step (x : ℕ) : Meets x (step x) := ⟨1, 0, rfl⟩

private theorem meets_one_iff (x : ℕ) : Meets x 1 ↔ ∃ i, orbit x i = 1 := by
  constructor
  · rintro ⟨i, j, hij⟩
    have hc : orbit 1 j = 1 ∨ orbit 1 j = 2 := by
      clear hij
      induction j with
      | zero => exact Or.inl rfl
      | succ j ih =>
        rcases ih with h | h
        · exact Or.inr (by rw [orbit, h]; decide)
        · exact Or.inl (by rw [orbit, h]; decide)
    rcases hc with ho | ht
    · exact ⟨i, hij.trans ho⟩
    · exact ⟨i + 1, by rw [orbit, hij, ht]; decide⟩
  · rintro ⟨i, hi⟩
    exact ⟨i, 0, hi⟩

/-- The full positive-integer conjecture is equivalent to merger of the
specified family, with no external density assumption. -/
theorem collatz_iff_binary_mergers :
    (∀ n : ℕ, 0 < n → ∃ i, orbit n i = 1) ↔
    (∀ j w : ℕ, w < 2 ^ j → Meets (1 + 3 * w) (1 + 3 * (w + 2 ^ j))) := by
  constructor
  · intro converges j w _
    exact meets_trans ((meets_one_iff _).2 (converges _ (by omega)))
      (meets_symm ((meets_one_iff _).2 (converges _ (by omega))))
  · intro edges
    have residues (n : ℕ) : Meets (1 + 3 * n) 1 := by
      induction n using Nat.strong_induction_on with
      | h n ih =>
        by_cases hn : n = 0
        · subst n
          exact ⟨0, 0, rfl⟩
        have hl := Nat.log2_self_le hn
        have hu := Nat.lt_log2_self (n := n)
        rw [pow_succ] at hu
        have hp : 0 < 2 ^ n.log2 := by positivity
        let w := n - 2 ^ n.log2
        have hw : w < 2 ^ n.log2 := by dsimp [w]; omega
        have hwn : w < n := by dsimp [w]; omega
        have he := edges n.log2 w hw
        rw [show w + 2 ^ n.log2 = n by dsimp [w]; omega] at he
        exact meets_trans (meets_symm he) (ih w hwn)
    have units (t : ℕ) (ht : t % 3 ≠ 0) : Meets t 1 := by
      by_cases h : t % 3 = 1
      · convert residues (t / 3) using 1
        omega
      · have ha : 2 * t = 1 + 3 * (2 * t / 3) := by omega
        have hb := residues (2 * t / 3)
        rw [← ha] at hb
        have hs := meets_step (2 * t)
        rw [show step (2 * t) = t by simp [step]] at hs
        exact meets_trans (meets_symm hs) hb
    intro n hn
    apply (meets_one_iff _).1
    induction n using Nat.strong_induction_on with
    | h n ih =>
      apply meets_trans (meets_step n)
      by_cases he : n % 2 = 0
      · rw [show step n = n / 2 by simp [step, he]]
        exact ih (n / 2) (by omega) (by omega)
      · apply units
        simp only [step, ite_eq_right he]
        omega

end CollatzUpperBit
