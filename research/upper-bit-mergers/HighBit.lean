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

def indexedStart (w : ℕ) : ℕ := 1 + 3 * w

def SamePrefix (h r v : ℕ) : Prop :=
  odds (indexedStart r) h = odds (indexedStart v) h ∧
  orbit (indexedStart r) h = orbit (indexedStart v) h

def FirstPrefix (h r : ℕ) : Prop := ∀ v < r, ¬ SamePrefix h v r

theorem indexed_tail (h r m : ℕ) :
    orbit (indexedStart (r + 2 ^ h * m)) h =
      orbit (indexedStart r) h + 3 ^ (odds (indexedStart r) h + 1) * m := by
  rw [show indexedStart (r + 2 ^ h * m) = indexedStart r + 2 ^ h * (3 * m) by
    unfold indexedStart
    ring, high_bit, pow_succ]
  ring

theorem prefix_tail_equal {h r v : ℕ} (hp : SamePrefix h r v) (m : ℕ) :
    orbit (indexedStart (r + 2 ^ h * m)) h = orbit (indexedStart (v + 2 ^ h * m)) h := by
  rw [indexed_tail, indexed_tail, hp.1, hp.2]

theorem indexed_endpoint_bound {h r : ℕ} (hr : r < 2 ^ h) :
    orbit (indexedStart r) h < 4 * 3 ^ odds (indexedStart r) h := by
  have hs : indexedStart r < 3 * 2 ^ h := by unfold indexedStart; omega
  have hh : (0 : ℝ) < 2 ^ h := by positivity
  have ha : (1 : ℝ) ≤ 2 ^ odds (indexedStart r) h := one_le_pow₀ (by norm_num)
  have hg : (0 : ℝ) < 3 ^ odds (indexedStart r) h := by positivity
  have hpos := (prefix_position (indexedStart r) h).2
  have hleft : (indexedStart r : ℝ) / 2 ^ h < 3 := (div_lt_iff₀ hh).2 (by exact_mod_cast hs)
  have hright : (1 : ℝ) / 2 ^ odds (indexedStart r) h ≤ 1 := by
    apply (div_le_iff₀ (by positivity)).2
    simpa using ha
  have hnorm : (orbit (indexedStart r) h : ℝ) / 3 ^ odds (indexedStart r) h < 4 := by linarith
  exact_mod_cast (div_lt_iff₀ hg).1 hnorm

theorem prefix_pair_iff {h r v : ℕ} (hp : SamePrefix h r v) (m n : ℕ) :
    Meets (indexedStart (r + 2 ^ h * m)) (indexedStart (r + 2 ^ h * n)) ↔
    Meets (indexedStart (v + 2 ^ h * m)) (indexedStart (v + 2 ^ h * n)) := by
  have hm : Meets (indexedStart (r + 2 ^ h * m)) (indexedStart (v + 2 ^ h * m)) :=
    ⟨h, h, prefix_tail_equal hp m⟩
  have hn : Meets (indexedStart (r + 2 ^ h * n)) (indexedStart (v + 2 ^ h * n)) :=
    ⟨h, h, prefix_tail_equal hp n⟩
  exact ⟨fun H => meets_trans (meets_symm hm) (meets_trans H hn),
    fun H => meets_trans hm (meets_trans H (meets_symm hn))⟩

/-- A single least representative per endpoint and odd count covers every
original binary-merger obligation at that depth. -/
theorem collatz_iff_first_representatives :
    (∀ n : ℕ, 0 < n → ∃ i, orbit n i = 1) ↔
    (∀ j r : ℕ, r < 2 ^ j → FirstPrefix j r →
      Meets (indexedStart r) (indexedStart (r + 2 ^ j))) := by
  rw [collatz_iff_binary_mergers]
  constructor
  · exact fun all j r hr _ => all j r hr
  · intro roots j r hr
    induction r using Nat.strong_induction_on with
    | h r ih =>
      by_cases hf : FirstPrefix j r
      · exact roots j r hr hf
      · unfold FirstPrefix at hf
        push Not at hf
        obtain ⟨v, hv, hp⟩ := hf
        have he := prefix_pair_iff hp 0 1
        simp only [Nat.mul_zero, Nat.add_zero, Nat.mul_one] at he
        exact he.mp (ih v hv (lt_trans hv hr))

private theorem orbit_first (x h : ℕ) : orbit x (h + 1) = orbit (step x) h := by
  rw [Nat.add_comm h 1, orbit_add]
  rfl

theorem strip_twos (x h : ℕ) : orbit (2 ^ h * x) h = x := by
  induction h with
  | zero => simp [orbit]
  | succ h ih =>
    rw [orbit_first, show 2 ^ (h + 1) * x = 2 * (2 ^ h * x) by ring,
      show step (2 * (2 ^ h * x)) = 2 ^ h * x by simp [step]]
    exact ih

private theorem exact_odd_block {x y e : ℕ} (he : 3 * x + 1 = 2 ^ (e + 1) * y) :
    orbit x (e + 1) = y := by
  have ha : 3 * x + 1 = 2 * (2 ^ e * y) := he.trans (by ring)
  have ho : x % 2 ≠ 0 := by omega
  rw [orbit_first, show step x = 2 ^ e * y by simp [step, ho, ha]]
  exact strip_twos _ _

/-- Blocks are listed last first. An entry e represents one odd step and
e subsequent halvings. -/
def routeTime : List ℕ → ℕ
  | [] => 0
  | e :: es => routeTime es + (e + 1)

def routeNumerator (x : ℕ) : List ℕ → ℕ
  | [] => x
  | _ :: es => 3 * routeNumerator x es + 2 ^ routeTime es

/-- An integral affine certificate forces all intermediate divisions to be
legal and proves the claimed orbit endpoint for an arbitrary block list. -/
theorem route_from_numerator (x : ℕ) (es : List ℕ) (t : ℕ)
    (h : routeNumerator x es = 2 ^ routeTime es * t) : orbit x (routeTime es) = t := by
  induction es generalizing t with
  | nil => simpa [routeNumerator, routeTime, orbit] using h
  | cons e es ih =>
    have ha : 3 * routeNumerator x es + 2 ^ routeTime es =
        2 ^ routeTime es * (2 ^ (e + 1) * t) := by
      simpa only [routeNumerator, routeTime, pow_add, Nat.mul_assoc] using h
    have hd : 2 ^ routeTime es ∣ 3 * routeNumerator x es :=
      (Nat.dvd_add_iff_left (dvd_refl _)).mpr ⟨_, ha⟩
    have hc : Nat.Coprime (2 ^ routeTime es) 3 :=
      Nat.Coprime.pow_left _ (by decide : Nat.Coprime 2 3)
    obtain ⟨y, hy⟩ := hc.dvd_of_dvd_mul_left hd
    have hb : 3 * y + 1 = 2 ^ (e + 1) * t := by
      apply Nat.eq_of_mul_eq_mul_left (show 0 < 2 ^ routeTime es by positivity)
      calc
        2 ^ routeTime es * (3 * y + 1) = 3 * routeNumerator x es + 2 ^ routeTime es := by
          rw [hy]
          ring
        _ = _ := ha
    rw [routeTime, orbit_add, ih y hy]
    exact exact_odd_block hb

private theorem cycle_counts (q : ℕ) : orbit 1 (2 * q) = 1 ∧ odds 1 (2 * q) = q := by
  induction q with
  | zero => simp [orbit, odds]
  | succ q ih =>
    rw [show 2 * (q + 1) = (2 * q + 1) + 1 by omega]
    simp [orbit, odds, ih.1, ih.2, step]

/-- Once the lower arm hits 1, every sufficiently high additional binary
digit follows the cycle exactly until the available precision runs out. -/
theorem after_one_tail (x d q m : ℕ) (hx : orbit x d = 1) :
    orbit (x + 2 ^ (d + 2 * q) * m) (d + 2 * q) =
      1 + 3 ^ (odds x d + q) * m := by
  have ht : orbit (x + 2 ^ (d + 2 * q) * m) d =
      1 + 2 ^ (2 * q) * (3 ^ odds x d * m) := by
    rw [pow_add, Nat.mul_assoc, high_bit, hx]
    ring
  rw [orbit_add, ht, high_bit, (cycle_counts q).1, (cycle_counts q).2, pow_add]
  ring

private theorem twice_step (x : ℕ) :
    2 * step x = if x % 2 = 0 then x else 3 * x + 1 := by
  by_cases he : x % 2 = 0 <;> simp [step, he] <;> omega

theorem source_profile_bound (x h : ℕ) :
    2 ^ h * orbit x h ≤ 4 ^ odds x h * x := by
  induction h with
  | zero => simp [orbit, odds]
  | succ h ih =>
    rw [orbit, pow_succ, Nat.mul_assoc, twice_step]
    by_cases he : orbit x h % 2 = 0
    · simpa [he, odds] using ih
    · simp only [ite_eq_right he, odds, pow_succ]
      calc
        2 ^ h * (3 * orbit x h + 1) ≤ 2 ^ h * (4 * orbit x h) :=
          Nat.mul_le_mul_left _ (by omega)
        _ = 4 * (2 ^ h * orbit x h) := by ring
        _ ≤ 4 * (4 ^ odds x h * x) := Nat.mul_le_mul_left 4 ih
        _ = _ := by ring

private theorem stays_power (b h : ℕ) : ∃ k : ℕ, orbit (2 ^ b) h = 2 ^ k := by
  induction h with
  | zero => exact ⟨b, rfl⟩
  | succ h ih =>
    obtain ⟨k, hk⟩ := ih
    rw [orbit, hk]
    cases k with
    | zero => exact ⟨1, by decide⟩
    | succ k => exact ⟨k, by simp [pow_succ, step]⟩

private theorem power_profile_eq (b h : ℕ) :
    2 ^ h * orbit (2 ^ b) h = 4 ^ odds (2 ^ b) h * 2 ^ b := by
  induction h with
  | zero => simp [orbit, odds]
  | succ h ih =>
    rw [orbit, pow_succ, Nat.mul_assoc, twice_step]
    by_cases he : orbit (2 ^ b) h % 2 = 0
    · simpa [he, odds] using ih
    · have ho : orbit (2 ^ b) h = 1 := by
        obtain ⟨k, hk⟩ := stays_power b h
        cases k with
        | zero => simpa using hk
        | succ k => simp [hk, pow_succ] at he
      simp only [ite_eq_right he, odds, pow_succ]
      calc
        2 ^ h * (3 * orbit (2 ^ b) h + 1) = 4 * (2 ^ h * orbit (2 ^ b) h) := by rw [ho]; ring
        _ = _ := by rw [ih]; ring

theorem power_first_prefix (b h r : ℕ) (hr : indexedStart r = 2 ^ b) : FirstPrefix h r := by
  intro v hv hp
  have ha := source_profile_bound (indexedStart v) h
  rw [hp.1, hp.2, hr, power_profile_eq] at ha
  have hs : 2 ^ b ≤ indexedStart v :=
    Nat.le_of_mul_le_mul_left ha (by positivity)
  rw [← hr] at hs
  unfold indexedStart at hs
  omega

/-- Squared magnitude with the correction that makes both odd edges of
the signed five-cycle attain equality. -/
def mirrorWeight (x : ℕ) : ℕ := if x = 7 then 50 else x ^ 2

private theorem sq_le_mirrorWeight (x : ℕ) : x ^ 2 ≤ mirrorWeight x := by
  by_cases h : x = 7
  · subst x
    decide
  · simp [mirrorWeight, h]

private theorem mirror_small {x : ℕ} (hx : x < 5) : mirrorStep x < 5 := by
  unfold mirrorStep
  split <;> omega

private theorem mirror_weight_step (x : ℕ) (hx : 5 ≤ x) :
    (if x % 2 = 0 then 1 else 8) * mirrorWeight x ≤ 4 * mirrorWeight (mirrorStep x) := by
  by_cases he : x % 2 = 0
  · have hs : 2 * mirrorStep x = x := by simp [mirrorStep, he]; omega
    have hn : x ≠ 7 := by omega
    simp only [he, ite_true, one_mul, mirrorWeight, ite_eq_right hn]
    change x ^ 2 ≤ 4 * mirrorWeight (mirrorStep x)
    calc
      x ^ 2 = (2 * mirrorStep x) ^ 2 := congrArg (fun z : ℕ => z ^ 2) hs.symm
      _ = 4 * (mirrorStep x) ^ 2 := by ring
      _ ≤ _ := Nat.mul_le_mul_left _ (sq_le_mirrorWeight _)
  · by_cases h5 : x = 5
    · subst x
      decide
    by_cases h7 : x = 7
    · subst x
      decide
    have hs : 2 * mirrorStep x + 1 = 3 * x := by simp [mirrorStep, he]; omega
    have hs2 := congrArg (fun z : ℕ => z ^ 2) hs
    have hx6 : 6 ≤ x := by omega
    have hsq := Nat.mul_le_mul_left x hx6
    simp only [ite_eq_right he, mirrorWeight, ite_eq_right h7]
    change 8 * x ^ 2 ≤ 4 * mirrorWeight (mirrorStep x)
    calc
      8 * x ^ 2 ≤ 4 * (mirrorStep x) ^ 2 := by
        nlinarith only [hs2, hs, hsq]
      _ ≤ _ := Nat.mul_le_mul_left _ (sq_le_mirrorWeight _)

private theorem mirror_path_weight (x h : ℕ) (hy : 5 ≤ mirrorOrbit x h) :
    8 ^ mirrorOdds x h * mirrorWeight x ≤ 4 ^ h * mirrorWeight (mirrorOrbit x h) := by
  induction h with
  | zero => simp [mirrorOdds, mirrorOrbit]
  | succ h ih =>
    have hx : 5 ≤ mirrorOrbit x h := by
      by_contra! hn
      exact (Nat.not_lt_of_ge hy) (mirror_small hn)
    have hw := mirror_weight_step (mirrorOrbit x h) hx
    have bound := ih hx
    by_cases he : mirrorOrbit x h % 2 = 0
    · simp only [he, ite_true, one_mul] at hw
      simp only [mirrorOdds, he, ite_true, mirrorOrbit, pow_succ]
      calc
        _ ≤ _ := bound
        _ ≤ 4 ^ h * (4 * mirrorWeight (mirrorStep (mirrorOrbit x h))) := Nat.mul_le_mul_left _ hw
        _ = _ := by ring
    · simp only [ite_eq_right he] at hw
      simp only [mirrorOdds, ite_eq_right he, mirrorOrbit, pow_succ]
      calc
        8 ^ mirrorOdds x h * 8 * mirrorWeight x = 8 * (8 ^ mirrorOdds x h * mirrorWeight x) := by ring
        _ ≤ 8 * (4 ^ h * mirrorWeight (mirrorOrbit x h)) := Nat.mul_le_mul_left _ bound
        _ = 4 ^ h * (8 * mirrorWeight (mirrorOrbit x h)) := by ring
        _ ≤ 4 ^ h * (4 * mirrorWeight (mirrorStep (mirrorOrbit x h))) := Nat.mul_le_mul_left _ hw
        _ = _ := by ring

/-- Every actual signed predecessor of five obeys the sharp clock bound.
The squared form uses natural numbers throughout. -/
theorem mirror_five_cost (x h : ℕ) (he : mirrorOrbit x h = 5) :
    8 ^ mirrorOdds x h * x ^ 2 ≤ 4 ^ h * 25 := by
  have hw := mirror_path_weight x h (by omega)
  rw [he] at hw
  exact (Nat.mul_le_mul_left _ (sq_le_mirrorWeight x)).trans hw

private theorem mirror_five_blocks (k : ℕ) :
    mirrorOrbit 5 (3 * k) = 5 ∧ mirrorOdds 5 (3 * k) = 2 * k := by
  induction k with
  | zero => simp [mirrorOrbit, mirrorOdds]
  | succ k ih =>
    rw [show 3 * (k + 1) = ((3 * k + 1) + 1) + 1 by omega]
    simp [mirrorOrbit, mirrorOdds, ih.1, ih.2, mirrorStep]
    omega

theorem five_checkpoint (n k t : ℕ) (he : n + 5 = 8 ^ k * t) :
    orbit n (3 * k) + 5 = 9 ^ k * t ∧ odds n (3 * k) = 2 * k := by
  have hm := mirror_lift n 5 (3 * k) t (by decide) (by simpa [pow_mul] using he)
  simpa [mirror_five_blocks, pow_mul] using hm

private theorem odds_add (x i j : ℕ) :
    odds x (i + j) = odds x i + odds (orbit x i) j := by
  induction j with
  | zero => simp [odds]
  | succ j ih =>
    change odds x ((i + j) + 1) = odds x i + odds (orbit x i) (j + 1)
    by_cases he : orbit (orbit x i) j % 2 = 0 <;>
      simp [odds, ih, orbit_add, he, Nat.add_assoc]

private theorem one_multiplier (h : ℕ) : 3 ^ odds 1 h ≤ 2 * 2 ^ h := by
  let q := h / 2
  have hd : h = 2 * q + h % 2 := by dsimp [q]; omega
  have hp : 3 ^ q ≤ 4 ^ q := Nat.pow_le_pow_left (by decide) q
  have hf : (2 : ℕ) ^ (2 * q) = 4 ^ q := by rw [pow_mul]; rfl
  rcases Nat.mod_two_eq_zero_or_one h with he | ho
  · rw [he, Nat.add_zero] at hd
    rw [hd, (cycle_counts q).2, hf]
    omega
  · rw [ho] at hd
    rw [hd, odds, (cycle_counts q).1]
    simp only [Nat.reduceMod, Nat.one_ne_zero, ite_false, pow_succ, (cycle_counts q).2, hf]
    omega

/-- Among starts 1, 2 and 3 the only forward multiplier above two is
the two-step prefix from 3, which reaches 8. -/
theorem small_seed_multiplier (x h : ℕ) (hx : 0 < x) (hx' : x ≤ 3) :
    3 ^ odds x h ≤ 2 * 2 ^ h ∨ (x = 3 ∧ h = 2 ∧ orbit x h = 8) := by
  have from_one (z b i : ℕ) (hz : orbit z b = 1) (hb : 3 ^ odds z b ≤ 2 ^ b) :
      3 ^ odds z (b + i) ≤ 2 * 2 ^ (b + i) := by
    rw [odds_add, hz, pow_add, pow_add]
    calc
      _ ≤ 2 ^ b * (2 * 2 ^ i) := Nat.mul_le_mul hb (one_multiplier i)
      _ = _ := by ring
  rcases (show x = 1 ∨ x = 2 ∨ x = 3 by omega) with rfl | rfl | rfl
  · exact Or.inl (one_multiplier h)
  · cases h with
    | zero => decide
    | succ i =>
      exact Or.inl (by simpa [Nat.add_comm] using from_one 2 1 i (by decide) (by decide))
  · by_cases hh : 5 ≤ h
    · obtain ⟨i, rfl⟩ := Nat.exists_eq_add_of_le hh
      exact Or.inl (from_one 3 5 i (by decide) (by decide))
    · rcases (show h = 0 ∨ h = 1 ∨ h = 2 ∨ h = 3 ∨ h = 4 by omega) with rfl | rfl | rfl | rfl | rfl <;> decide

private theorem mirror_from_five_min (x h : ℕ) (he : mirrorOrbit x h = 5) : 5 ≤ x := by
  have low (z j : ℕ) (hz : z < 5) : mirrorOrbit z j < 5 := by
    induction j with
    | zero => exact hz
    | succ j ih => exact mirror_small ih
  by_contra! hb
  have := low x h hb
  omega

private theorem mirror_slope_scaled (M L q k : ℕ) (hq : q ≤ 2 * k)
    (hw : 8 ^ q * M ^ 2 ≤ 4 ^ L * 25) :
    M * 8 ^ k ≤ 5 * 2 ^ L * 3 ^ (2 * k - q) := by
  let d := 2 * k - q
  have hd : q + d = 2 * k := by dsimp [d]; omega
  have hp : 8 ^ d ≤ 9 ^ d := Nat.pow_le_pow_left (by decide) d
  have hs : (M * 8 ^ k) ^ 2 ≤ (5 * 2 ^ L * 3 ^ d) ^ 2 := by
    calc
      (M * 8 ^ k) ^ 2 = (8 ^ q * M ^ 2) * 8 ^ d := by
        rw [mul_pow, ← pow_mul, Nat.mul_comm k 2, ← hd, pow_add]
        ring
      _ ≤ (4 ^ L * 25) * 9 ^ d := Nat.mul_le_mul hw hp
      _ = (5 * 2 ^ L * 3 ^ d) ^ 2 := by
        rw [show (4 : ℕ) ^ L = (2 ^ L) ^ 2 by rw [← pow_mul, Nat.mul_comm L 2, pow_mul]; rfl,
          show (9 : ℕ) ^ d = (3 ^ d) ^ 2 by rw [← pow_mul, Nat.mul_comm d 2, pow_mul]; rfl]
        ring
  exact (Nat.pow_le_pow_iff_left (by decide : 2 ≠ 0)).mp hs

/-- Lifting a competitor with at most 2k odds to the signed cycle gives
an ordinary signed magnitude and the lower bound on its clock. -/
theorem checkpoint_suffix (z L k t : ℕ) (he : orbit z L + 5 = 9 ^ k * t)
    (hq : odds z L ≤ 2 * k) :
    ∃ M, 5 ≤ M ∧ z + M = 2 ^ L * 3 ^ (2 * k - odds z L) * t ∧
      M * 8 ^ k ≤ 5 * 2 ^ L * 3 ^ (2 * k - odds z L) := by
  let q := odds z L
  let d := 2 * k - q
  let v := 3 ^ d * t
  have hd : q + d = 2 * k := by dsimp [d, q]; omega
  have hterm : 3 ^ q * v = 9 ^ k * t := by
    dsimp [v]
    rw [← Nat.mul_assoc, ← pow_add, hd, pow_mul]
    rfl
  have ha := affine z L
  change 2 ^ L * orbit z L = 3 ^ q * z + offset z L at ha
  have hdiff : 3 ^ q * z < 3 ^ q * (2 ^ L * v) := by
    calc
      3 ^ q * z ≤ 2 ^ L * orbit z L := by omega
      _ < 2 ^ L * (orbit z L + 5) := Nat.mul_lt_mul_of_pos_left (by omega) (by positivity)
      _ = _ := by rw [he, ← hterm]; ring
  have hz := Nat.lt_of_mul_lt_mul_left hdiff
  let M := 2 ^ L * v - z
  have hM : 0 < M := by dsimp [M]; omega
  have hsum : z + M = 2 ^ L * v := by dsimp [M]; omega
  obtain ⟨hend, hodd⟩ := mirror_lift z M L v hM hsum
  change orbit z L + mirrorOrbit M L = 3 ^ (mirrorOdds M L) * v at hend
  rw [← hodd, hterm] at hend
  have hm : mirrorOrbit M L = 5 := by omega
  refine ⟨M, mirror_from_five_min _ _ hm, ?_, ?_⟩
  · simpa only [v, d, q, Nat.mul_assoc] using hsum
  · apply mirror_slope_scaled M L (odds z L) k hq
    rw [hodd]
    exact mirror_five_cost _ _ hm

private theorem offset_lower (x J : ℕ) : 3 ^ odds x J ≤ offset x J + 2 ^ J := by
  induction J with
  | zero => simp [odds, offset]
  | succ J ih =>
    by_cases hp : orbit x J % 2 = 0 <;>
      simp only [odds, offset, hp, ite_true, ite_false, pow_succ] <;> omega

private theorem odds_high_bit (x h m : ℕ) : odds (x + 2 ^ h * m) h = odds x h := by
  induction h generalizing m with
  | zero => rfl
  | succ h ih =>
    have hs : x + 2 ^ (h + 1) * m = x + 2 ^ h * (2 * m) := by ring
    rw [hs, odds, odds, ih, high_bit]
    have hh : (orbit x h + 3 ^ odds x h * (2 * m)) % 2 = orbit x h % 2 := by
      rw [show 3 ^ odds x h * (2 * m) = 2 * (3 ^ odds x h * m) by ring]
      omega
    rw [hh]

private theorem zero_prefix (h : ℕ) : orbit 0 h = 0 ∧ odds 0 h = 0 := by
  induction h with
  | zero => simp [orbit, odds]
  | succ h ih => simp [orbit, odds, ih.1, ih.2, step]

/-- A prefix ending a multiple of its ternary scale above a nonnegative
endpoint has a positive ordinary companion when the prefix has an odd step. -/
private theorem positive_prefix (m J D c : ℕ) (hd : 0 < odds m J)
    (he : orbit m J = 3 ^ odds m J * D + c) :
    ∃ β, 0 < β ∧ m = 2 ^ J * D + β ∧ orbit β J = c ∧ odds β J = odds m J := by
  have hm : 2 ^ J * D < m := by
    by_contra! hle
    by_cases h : m = 2 ^ J * D
    · have hz : m = 0 + 2 ^ J * D := by omega
      have ho := odds_high_bit 0 J D
      rw [← hz, (zero_prefix J).2] at ho
      omega
    · let p := 2 ^ J * D - m
      have hp : 0 < p := by dsimp [p]; omega
      have hs : m + p = 2 ^ J * D := by dsimp [p]; omega
      obtain ⟨hr, ho⟩ := mirror_lift m p J D hp hs
      rw [← ho, he] at hr
      have := mirror_positive p J hp
      omega
  let β := m - 2 ^ J * D
  have hb : 0 < β := by dsimp [β]; omega
  have hs : m = β + 2 ^ J * D := by dsimp [β]; omega
  have ho := odds_high_bit β J D
  have hy := high_bit β J D
  rw [← hs] at ho hy
  rw [← ho] at hy
  exact ⟨β, hb, by omega, by omega, ho.symm⟩

private theorem short_suffix_above (z n L k t : ℕ) (hn : n + 5 = 8 ^ k * t)
    (he : orbit z L + 5 = 9 ^ k * t) (hq : odds z L ≤ 2 * k) : n ≤ z := by
  obtain ⟨M, hm, hsum, hbound⟩ := checkpoint_suffix z L k t he hq
  have hc : M * (n + 5) ≤ 5 * (z + M) := by
    calc
      M * (n + 5) = (M * 8 ^ k) * t := by rw [hn]; ring
      _ ≤ _ := Nat.mul_le_mul_right t hbound
      _ = 5 * (z + M) := by rw [hsum]; ring
  have hm' := Nat.mul_le_mul_right n hm
  nlinarith only [hc, hm']

private theorem equal_suffix_form (z n L k t : ℕ) (hn : n + 5 = 8 ^ k * t)
    (he : orbit z L + 5 = 9 ^ k * t) (hq : odds z L = 2 * k) :
    ∃ b c M, 5 ≤ M ∧ c + M = 5 * 2 ^ b ∧ z = 2 ^ b * n + c := by
  obtain ⟨M, hm, hsum, hbound⟩ := checkpoint_suffix z L k t he hq.le
  simp only [hq, Nat.sub_self, pow_zero, Nat.mul_one] at hsum hbound
  have hlen : 3 * k ≤ L := by
    have hh : 5 * 8 ^ k ≤ 5 * 2 ^ L :=
      (Nat.mul_le_mul_right _ hm).trans hbound
    have hp : 2 ^ (3 * k) ≤ 2 ^ L := by
      simpa [pow_mul] using Nat.le_of_mul_le_mul_left hh (by decide : 0 < 5)
    exact (Nat.pow_le_pow_iff_right (by decide : 1 < 2)).mp hp
  let b := L - 3 * k
  have hb : L = 3 * k + b := by dsimp [b]; omega
  have hpow : 2 ^ L = 8 ^ k * 2 ^ b := by rw [hb, pow_add, pow_mul]; rfl
  have hM : M ≤ 5 * 2 ^ b := by
    rw [hpow, ← Nat.mul_left_comm, Nat.mul_comm M (8 ^ k)] at hbound
    exact Nat.le_of_mul_le_mul_left hbound (by positivity)
  let c := 5 * 2 ^ b - M
  have hc : c + M = 5 * 2 ^ b := by dsimp [c]; omega
  refine ⟨b, c, M, hm, hc, ?_⟩
  have hs : z + M = 2 ^ b * (n + 5) := by rw [hsum, hpow, hn]; ring
  nlinarith only [hs, hc]

private theorem ordinary_positive (x h : ℕ) (hx : 0 < x) : 0 < orbit x h := by
  induction h with
  | zero => exact hx
  | succ h ih => simp only [orbit, step]; split <;> omega

private theorem small_seed_bound (β J d b c M : ℕ)
    (hodd : odds β J = d) (hy : orbit β J = c)
    (hM : 5 ≤ M) (hc : c + M = 5 * 2 ^ b) :
    3 ^ d * (β + 1) < 5 * (2 ^ J * 2 ^ b) := by
  have ha := affine β J
  have hlo := offset_lower β J
  rw [hy, hodd] at ha
  rw [hodd] at hlo
  calc
    3 ^ d * (β + 1) = 3 ^ d * β + 3 ^ d := by ring
    _ ≤ 2 ^ J * c + 2 ^ J := by omega
    _ = 2 ^ J * (c + 1) := by ring
    _ < 2 ^ J * (c + M) := Nat.mul_lt_mul_of_pos_left (by omega) (by positivity)
    _ = 5 * (2 ^ J * 2 ^ b) := by rw [hc]; ring

private theorem prefix_exclusion (m n J b c M : ℕ) (hlt : m < n) (hd : 0 < odds m J)
    (hv : 3 ^ odds m J ∣ n) (hM : 5 ≤ M) (hc : c + M = 5 * 2 ^ b)
    (he : orbit m J = 2 ^ b * n + c) : False := by
  obtain ⟨s, hs⟩ := hv
  let d := odds m J
  have hz : orbit m J = 3 ^ d * (2 ^ b * s) + c := by rw [he, hs]; dsimp [d]; ring
  obtain ⟨β, hβ, hm, hβc, hβd⟩ := positive_prefix m J (2 ^ b * s) c hd hz
  change odds β J = d at hβd
  have hmul : (2 ^ J * 2 ^ b) * s < 3 ^ d * s := by
    rw [Nat.mul_assoc, ← hs]
    omega
  have hsmall := Nat.lt_of_mul_lt_mul_right hmul
  have hβs : 3 ^ d * (β + 1) < 3 ^ d * 5 := by
    calc
      _ < _ := small_seed_bound β J d b c M hβd hβc hM hc
      _ < _ := by simpa [Nat.mul_comm] using Nat.mul_lt_mul_of_pos_left hsmall (by decide : 0 < 5)
  have hβ3 : β ≤ 3 := by have := Nat.lt_of_mul_lt_mul_left hβs; omega
  rcases small_seed_multiplier β J hβ hβ3 with hr | ⟨h3, hJ, h8⟩
  · rw [hβd] at hr
    have hB : 2 ^ b < 2 := by
      apply Nat.lt_of_mul_lt_mul_left (Nat.lt_of_lt_of_le hsmall _)
      simpa [Nat.mul_comm] using hr
    have hp : 0 < 2 ^ b := by positivity
    have hcp := ordinary_positive β J hβ
    omega
  · have hdd : d = 2 := by rw [← hβd, h3, hJ]; decide
    rw [hJ, hdd] at hsmall
    norm_num at hsmall
    omega

private theorem odds_hits (m H d : ℕ) (hd : d ≤ odds m H) :
    ∃ J, J ≤ H ∧ odds m J = d := by
  induction H with
  | zero =>
    have hh : d = 0 := by simpa [odds] using hd
    exact ⟨0, le_rfl, hh.symm⟩
  | succ H ih =>
    by_cases h : d ≤ odds m H
    · obtain ⟨J, hJ, ho⟩ := ih h
      exact ⟨J, by omega, ho⟩
    · refine ⟨H + 1, le_rfl, ?_⟩
      simp only [odds] at hd ⊢
      split at hd <;> split <;> omega

theorem checkpoint_odd_budget (m n H k A t : ℕ) (hm : m < n)
    (hn : n + 5 = 8 ^ k * t) (hv : 3 ^ A ∣ n) (he : orbit m H + 5 = 9 ^ k * t) :
    2 * k + A < odds m H := by
  by_contra! hbudget
  by_cases low : odds m H ≤ 2 * k
  · exact (Nat.not_le_of_gt hm) (short_suffix_above m n H k t hn he low)
  let d := odds m H - 2 * k
  have hd : 0 < d := by dsimp [d]; omega
  have hdA : d ≤ A := by dsimp [d]; omega
  obtain ⟨J, hJ, hodd⟩ := odds_hits m H d (by dsimp [d]; omega)
  let L := H - J
  have hL : J + L = H := by dsimp [L]; omega
  have hq := odds_add m J L
  rw [hL, hodd] at hq
  have hq' : odds (orbit m J) L = 2 * k := by dsimp [d] at hq; omega
  have ht : orbit (orbit m J) L + 5 = 9 ^ k * t := by rwa [← orbit_add, hL]
  obtain ⟨b, c, M, hM, hc, hz⟩ := equal_suffix_form (orbit m J) n L k t hn ht hq'
  apply prefix_exclusion m n J b c M hm (by omega) _ hM hc hz
  rw [hodd]
  exact dvd_trans (Nat.pow_dvd_pow 3 hdA) hv

/-- Every smaller ordinary source meeting before the checkpoint has to
spend more than A extra odd steps, with no limit on its own clock. -/
theorem early_meeting_odd_budget (m n i j k A t : ℕ) (hm : m < n)
    (hn : n + 5 = 8 ^ k * t) (hv : 3 ^ A ∣ n) (hi : i ≤ 3 * k)
    (meet : orbit m j = orbit n i) : odds n i + A < odds m j := by
  let L := 3 * k - i
  have hL : i + L = 3 * k := by dsimp [L]; omega
  obtain ⟨hy, hq⟩ := five_checkpoint n k t hn
  have he : orbit m (j + L) + 5 = 9 ^ k * t := by
    rwa [orbit_add, meet, ← orbit_add, hL]
  have hh := checkpoint_odd_budget m n (j + L) k A t hm hn hv he
  rw [odds_add, meet] at hh
  have hq' := odds_add n i L
  rw [hL, hq] at hq'
  omega

private theorem odd_growth (x h : ℕ) :
    2 ^ odds x h * (orbit x h + 1) ≤ 3 ^ odds x h * (x + 1) := by
  induction h with
  | zero => simp [orbit, odds]
  | succ h ih =>
    by_cases he : orbit x h % 2 = 0
    · simp only [odds, he, ite_true, orbit]
      have hs : step (orbit x h) + 1 ≤ orbit x h + 1 := by simp [step, he]; omega
      exact (Nat.mul_le_mul_left _ hs).trans ih
    · have hs : 2 * (step (orbit x h) + 1) = 3 * (orbit x h + 1) := by simp [step, he]; omega
      simp only [odds, ite_eq_right he, orbit, pow_succ]
      calc
        _ = 2 ^ odds x h * (3 * (orbit x h + 1)) := by rw [Nat.mul_assoc, hs]
        _ = 3 * (2 ^ odds x h * (orbit x h + 1)) := by ring
        _ ≤ 3 * (3 ^ odds x h * (x + 1)) := Nat.mul_le_mul_left _ ih
        _ = _ := by ring

/-- A merger only e odds beyond the ternary valuation yields a bounded
ordinary start that realizes A odd steps with a multiplier bounded below. -/
theorem checkpoint_small_witness (m n H k A e t : ℕ) (hm : m < n) (hA : 0 < A)
    (hn : n + 5 = 8 ^ k * t) (hv : 3 ^ A ∣ n) (he : orbit m H + 5 = 9 ^ k * t)
    (ho : odds m H = 2 * k + A + e) :
    ∃ β J, 0 < β ∧ 2 ^ e * (β + 1) < 5 * 3 ^ e ∧
      odds β J = A ∧ 2 ^ e * 2 ^ J < 3 ^ e * 3 ^ A := by
  obtain ⟨I, hI, hIo⟩ := odds_hits m H e (by omega)
  let v := orbit m I
  let N := H - I
  have hIN : I + N = H := by dsimp [N]; omega
  have hNv := odds_add m I N
  rw [hIN, hIo, ho] at hNv
  have hN : odds v N = 2 * k + A := by dsimp [v]; omega
  have hve : orbit v N + 5 = 9 ^ k * t := by unfold v; rwa [← orbit_add, hIN]
  obtain ⟨J, hJ, hJo⟩ := odds_hits v N A (by omega)
  let L := N - J
  have hJL : J + L = N := by dsimp [L]; omega
  have hLo := odds_add v J L
  rw [hJL, hJo, hN] at hLo
  have hz : orbit (orbit v J) L + 5 = 9 ^ k * t := by rwa [← orbit_add, hJL]
  obtain ⟨b, c, M, hM, hc, hzc⟩ := equal_suffix_form (orbit v J) n L k t hn hz (by omega)
  obtain ⟨s, hs⟩ := hv
  have hzc' : orbit v J = 3 ^ odds v J * (2 ^ b * s) + c := by rw [hzc, hs, hJo]; ring
  obtain ⟨β, hβ, hform, hβc, hβo⟩ := positive_prefix v J (2 ^ b * s) c (by omega) hzc'
  rw [hJo] at hβo
  have hbound := small_seed_bound β J A b c M hβo hβc hM hc
  have hg := odd_growth m I
  rw [hIo] at hg
  change 2 ^ e * (v + 1) ≤ 3 ^ e * (m + 1) at hg
  have hscale : 2 ^ e * (2 ^ J * 2 ^ b) < 3 ^ e * 3 ^ A := by
    apply Nat.lt_of_mul_lt_mul_right (a := s)
    calc
      (2 ^ e * (2 ^ J * 2 ^ b)) * s = 2 ^ e * (2 ^ J * (2 ^ b * s)) := by ring
      _ < 2 ^ e * (v + 1) := Nat.mul_lt_mul_of_pos_left (by omega) (by positivity)
      _ ≤ _ := hg
      _ ≤ 3 ^ e * n := Nat.mul_le_mul_left _ (by omega)
      _ = _ := by rw [hs]; ring
  refine ⟨β, J, hβ, ?_, hβo, ?_⟩
  · apply Nat.lt_of_mul_lt_mul_left (a := 3 ^ A)
    calc
      3 ^ A * (2 ^ e * (β + 1)) = 2 ^ e * (3 ^ A * (β + 1)) := by ring
      _ < 2 ^ e * (5 * (2 ^ J * 2 ^ b)) := Nat.mul_lt_mul_of_pos_left hbound (by positivity)
      _ = 5 * (2 ^ e * (2 ^ J * 2 ^ b)) := by ring
      _ < 5 * (3 ^ e * 3 ^ A) := Nat.mul_lt_mul_of_pos_left hscale (by decide)
      _ = _ := by ring
  · have hb : 1 ≤ 2 ^ b := Nat.succ_le_of_lt (by positivity : 0 < 2 ^ b)
    have hJb : 2 ^ J ≤ 2 ^ J * 2 ^ b := by simpa using Nat.mul_le_mul_left (2 ^ J) hb
    exact (Nat.mul_le_mul_left _ hJb).trans_lt hscale

private theorem small_cycle_odds (y q : ℕ) (hy : y = 1 ∨ y = 2) : odds y (2 * q) = q := by
  rcases hy with rfl | rfl
  · exact (cycle_counts q).2
  · have both : orbit 2 (2 * q) = 2 ∧ odds 2 (2 * q) = q := by
      induction q with
      | zero => simp [orbit, odds]
      | succ q ih =>
        rw [show 2 * (q + 1) = (2 * q + 1) + 1 by omega]
        simp [orbit, odds, ih.1, ih.2, step]
    exact both.2

private theorem first_six_after_six (x J : ℕ) (hx : 0 < x) (hx' : x ≤ 6) (hJ : 6 ≤ J) :
    3 * 3 ^ odds x J ≤ 2 * 2 ^ J := by
  let b := 6 + J % 2
  let q := (J - b) / 2
  have hdecomp : J = b + 2 * q := by dsimp [b, q]; omega
  have hb : b = 6 ∨ b = 7 := by dsimp [b]; omega
  have base : (orbit x b = 1 ∨ orbit x b = 2) ∧ 3 * 3 ^ odds x b ≤ 2 * 2 ^ b := by
    have choices : x = 1 ∨ x = 2 ∨ x = 3 ∨ x = 4 ∨ x = 5 ∨ x = 6 := by omega
    rcases choices with rfl | rfl | rfl | rfl | rfl | rfl <;>
      rcases hb with hb | hb <;> rw [hb] <;> decide
  have hp : 3 ^ q ≤ 4 ^ q := Nat.pow_le_pow_left (by decide) q
  rw [hdecomp, odds_add, small_cycle_odds _ _ base.1, pow_add, pow_add, pow_mul]
  calc
    _ = (3 * 3 ^ odds x b) * 3 ^ q := by ring
    _ ≤ (2 * 2 ^ b) * 4 ^ q := Nat.mul_le_mul base.2 hp
    _ = _ := by ring

/-- When A is at least six, one extra odd step is still insufficient. -/
theorem early_meeting_large_odd_budget (m n i j k A t : ℕ) (hm : m < n) (hA : 6 ≤ A)
    (hn : n + 5 = 8 ^ k * t) (hv : 3 ^ A ∣ n) (hi : i ≤ 3 * k)
    (meet : orbit m j = orbit n i) : odds n i + A + 1 < odds m j := by
  have hlow := early_meeting_odd_budget m n i j k A t hm hn hv hi meet
  by_contra! hupper
  let L := 3 * k - i
  have hL : i + L = 3 * k := by dsimp [L]; omega
  obtain ⟨hy, hq⟩ := five_checkpoint n k t hn
  have he : orbit m (j + L) + 5 = 9 ^ k * t := by rwa [orbit_add, meet, ← orbit_add, hL]
  have hq' := odds_add n i L
  rw [hL, hq] at hq'
  have hodd : odds m (j + L) = 2 * k + A + 1 := by rw [odds_add, meet]; omega
  obtain ⟨β, J, hβ, hb, hj, hh⟩ :=
    checkpoint_small_witness m n (j + L) k A 1 t hm (by omega) hn hv he hodd
  norm_num at hb hh
  have hcounts := counts β J
  have bound := first_six_after_six β J hβ (by omega) (by omega)
  rw [hj] at bound
  omega

end CollatzUpperBit
