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

private theorem mirror_seven_blocks (k : ℕ) :
    mirrorOrbit 7 (3 * k) = 7 ∧ mirrorOdds 7 (3 * k) = 2 * k := by
  induction k with
  | zero => simp [mirrorOrbit, mirrorOdds]
  | succ k ih =>
    rw [show 3 * (k + 1) = ((3 * k + 1) + 1) + 1 by omega]
    simp [mirrorOrbit, mirrorOdds, ih.1, ih.2, mirrorStep]
    omega

private theorem four_step_cell (r u : ℕ) (hr : r = 8 ∨ r = 10) :
    orbit (r + 16 * u) 4 = 3 * u + 2 ∧ odds (r + 16 * u) 4 = 1 := by
  have hy := high_bit r 4 u
  have hs := odds_high_bit r 4 u
  have base : orbit r 4 = 2 ∧ odds r 4 = 1 := by rcases hr with rfl | rfl <;> decide
  rw [base.1, base.2] at hy
  rw [base.2] at hs
  exact ⟨by simpa [Nat.add_comm] using hy, hs⟩

/-- The two phases -5 and -7 give an ordinary smaller partner four steps
after the checkpoint, uniformly in the number of expanding blocks. -/
theorem four_step_exit (m k t u : ℕ) (hn : m + 7 = 8 ^ k * t)
    (he : 9 ^ k * t = 16 * u + 15) :
    orbit (m + 2) (3 * k + 4) = 3 * u + 2 ∧ orbit m (3 * k + 4) = 3 * u + 2 ∧
    odds (m + 2) (3 * k + 4) = 2 * k + 1 ∧ odds m (3 * k + 4) = 2 * k + 1 := by
  obtain ⟨hy, ho⟩ := five_checkpoint (m + 2) k t (by omega)
  have hl := mirror_lift m 7 (3 * k) t (by decide) (by simpa [pow_mul] using hn)
  have hl' : orbit m (3 * k) + 7 = 9 ^ k * t ∧ odds m (3 * k) = 2 * k := by
    simpa [mirror_seven_blocks, pow_mul] using hl
  have hu : orbit (m + 2) (3 * k) = 10 + 16 * u := by omega
  have hv : orbit m (3 * k) = 8 + 16 * u := by omega
  have hf := four_step_cell 10 u (Or.inr rfl)
  have hg := four_step_cell 8 u (Or.inl rfl)
  simp only [orbit_add, odds_add, hu, hv, hf.1, hf.2, hg.1, hg.2, ho, hl'.2, and_self]

private theorem mirror_one_fixed (h : ℕ) : mirrorOrbit 1 h = 1 ∧ mirrorOdds 1 h = h := by
  induction h with
  | zero => simp [mirrorOrbit, mirrorOdds]
  | succ h ih => simp [mirrorOrbit, mirrorOdds, ih.1, ih.2, mirrorStep]

/-- An ordinary source from the phase at -1 can be synchronized with a
source emerging from any number of negative-five blocks. -/
theorem fixed_point_exit (m n k t u : ℕ) (hn : n + 5 = 8 ^ k * t)
    (hm : m + 1 = 2 ^ (2 * k + 1) * t) (he : 9 ^ k * t = 128 * u + 9) :
    orbit n (3 * k + 7) = 27 * u + 2 ∧
    orbit m (2 * k + 1 + 7) = 27 * u + 2 ∧
    odds n (3 * k + 7) = 2 * k + 3 ∧ odds m (2 * k + 1 + 7) = 2 * k + 3 := by
  obtain ⟨hy, hyo⟩ := five_checkpoint n k t hn
  obtain ⟨hmv, hmo⟩ := mirror_lift m 1 (2 * k + 1) t (by decide) hm
  simp only [(mirror_one_fixed (2 * k + 1)).1, (mirror_one_fixed (2 * k + 1)).2] at hmv hmo
  have hpow : 3 ^ (2 * k + 1) * t = 3 * (9 ^ k * t) := by
    rw [pow_succ, pow_mul]
    ring
  rw [hpow, he] at hmv
  have hupper : orbit n (3 * k) = 4 + 2 ^ 7 * u := by omega
  have hlower : orbit m (2 * k + 1) = 26 + 2 ^ 7 * (3 * u) := by omega
  have hab : orbit 4 7 = 2 ∧ odds 4 7 = 3 := by decide
  have hcd : orbit 26 7 = 2 ∧ odds 26 7 = 2 := by decide
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [orbit_add n (3 * k) 7, hupper, high_bit, hab.1, hab.2]
    omega
  · rw [orbit_add m (2 * k + 1) 7, hlower, high_bit, hcd.1, hcd.2]
    omega
  · rw [odds_add n (3 * k) 7, hyo, hupper, odds_high_bit, hab.2]
  · rw [odds_add m (2 * k + 1) 7, hmo, hlower, odds_high_bit, hcd.2]

theorem fixed_point_source_smaller (m n k t : ℕ) (hk : 2 ≤ k) (ht : 0 < t)
    (hn : n + 5 = 8 ^ k * t) (hm : m + 1 = 2 ^ (2 * k + 1) * t) : m < n := by
  obtain ⟨j, rfl⟩ := Nat.exists_eq_add_of_le hk
  have he : 2 ^ (2 * (2 + j) + 1) = 32 * 4 ^ j := by
    rw [show 2 * (2 + j) + 1 = 5 + 2 * j by omega, pow_add, pow_mul]
    rfl
  have hp : 8 ^ (2 + j) = 64 * 8 ^ j := by rw [pow_add]; rfl
  have hh : 4 ^ j * t ≤ 8 ^ j * t := Nat.mul_le_mul_right t (Nat.pow_le_pow_left (by decide) j)
  have hpos : 0 < 4 ^ j * t := by positivity
  rw [he, Nat.mul_assoc] at hm
  rw [hp, Nat.mul_assoc] at hn
  omega

theorem fixed_point_exit_k_one (n t u : ℕ) (hn : n + 5 = 8 * t)
    (he : 9 * t = 128 * u + 9) : orbit n 4 < n := by
  have ht : t % 2 = 1 := by omega
  have hres : n = 3 + 2 ^ 4 * (t / 2) := by omega
  have h0 : orbit 3 4 = 2 ∧ odds 3 4 = 2 := by decide
  rw [hres, high_bit, h0.1, h0.2]
  omega

private theorem meets_double (x : ℕ) : Meets x (2 * x) := by
  exact ⟨0, 1, by simp [orbit, step]⟩

/-- All affine edges of the single shape t,5t+1 suffice for full Collatz.
The iterated map on both arms is the positive 3x+1 shortcut map. -/
theorem collatz_iff_five_ray :
    (∀ n : ℕ, 0 < n → ∃ i, orbit n i = 1) ↔
    (∀ t : ℕ, 0 < t → Meets t (5 * t + 1)) := by
  constructor
  · intro hc t ht
    exact meets_trans ((meets_one_iff _).2 (hc t ht))
      (meets_symm ((meets_one_iff _).2 (hc (5 * t + 1) (by omega))))
  · intro edges n hn
    apply (meets_one_iff n).1
    induction n using Nat.strong_induction_on with
    | h n ih =>
      by_cases h1 : n = 1
      · subst n
        exact ⟨0, 0, rfl⟩
      by_cases he : n % 2 = 0
      · have hs : step n = n / 2 := by simp [step, he]
        apply meets_trans (meets_step n)
        rw [hs]
        exact ih _ (by omega) (by omega)
      have via (y : ℕ) (hy : Meets n y) (hr : y % 5 = 1) (hb : 5 < y)
          (hlt : y / 5 < n) : Meets n 1 := by
        have ht : 0 < y / 5 := by omega
        have edge := meets_symm (edges (y / 5) ht)
        rw [show 5 * (y / 5) + 1 = y by omega] at edge
        exact meets_trans (meets_trans hy edge) (ih _ hlt ht)
      have hs : step n = (3 * n + 1) / 2 := by simp [step, he]
      have twice : 2 * step n = 3 * n + 1 := by rw [hs]; omega
      have cases5 : n % 5 = 0 ∨ n % 5 = 1 ∨ n % 5 = 2 ∨ n % 5 = 3 ∨ n % 5 = 4 := by omega
      rcases cases5 with h | h | h | h | h
      · apply via (2 * step n) (meets_trans (meets_step n) (meets_double _)) <;> omega
      · apply via n ⟨0, 0, rfl⟩ <;> omega
      · apply via (step n) (meets_step n) <;> omega
      · apply via (2 * n) (meets_double n) <;> omega
      · apply via (2 * (2 * n)) (meets_trans (meets_double n) (meets_double _)) <;> omega


private theorem component_multipliers {α : Type*} (f : ℕ → α)
    (h2 : ∀ n, 0 < n → f (2 * n) = f n)
    (hs : ∀ n, 0 < n → f (step n) = f n)
    (N : ℕ) (hr : ∀ t, N ≤ t → 0 < t → f (5 * t + 1) = f t) :
    (∀ n, 0 < n → f (3 * n) = f n) ∧ (∀ n, 0 < n → f (5 * n) = f n) := by
  have powInv (b : ℕ) (hb : 0 < b) (h : ∀ n, 0 < n → f (b * n) = f n)
      (k n : ℕ) (hn : 0 < n) : f (b^k * n) = f n := by
    induction k with
    | zero => simp
    | succ k ih =>
      rw [pow_succ, show b^k * b * n = b * (b^k * n) by ring, h _ (by positivity), ih]
  have big (b k : ℕ) (hb : 2 ≤ b) : k < b^k := by
    induction k with
    | zero => simp
    | succ k ih =>
      rw [pow_succ]
      have := Nat.mul_le_mul_left (b^k) hb
      omega
  have h3 (n : ℕ) (hn : 0 < n) : f (3*n) = f n := by
    let u := 2^N*n
    have hu : N < u := by
      have := Nat.mul_le_mul_left (2^N) (show 1 ≤ n by omega)
      dsimp [u]
      have := big 2 N (by decide)
      omega
    have hhop := hs (5*(4*u)+1) (by omega)
    have hh : step (5*(4*u)+1) = 2*(5*(3*u)+1) := by
      rw [step, ite_eq_right (show (5*(4*u)+1)%2 ≠ 0 by omega)]
      omega
    rw [hh, h2 _ (by omega), hr _ (by omega) (by omega), hr _ (by omega) (by omega)] at hhop
    have h4 : f (4*u) = f u := by
      rw [show 4*u=2*(2*u) by ring, h2 _ (by omega), h2 _ (by omega)]
    rw [h4] at hhop
    change f (3*(2^N*n)) = f (2^N*n) at hhop
    rwa [show 3*(2^N*n)=2^N*(3*n) by ring, powInv 2 (by decide) h2 N _ (by omega),
      powInv 2 (by decide) h2 N n hn] at hhop
  refine ⟨h3, ?_⟩
  intro n hn
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases he : n%2=0
    · let a := n/2
      have ha : n = 2*a := by dsimp [a]; omega
      have hi := ih a (by omega) (by omega)
      calc
        f (5*n) = f (2*(5*a)) := by rw [ha]; ring_nf
        _ = f (5*a) := h2 _ (by omega)
        _ = f a := hi
        _ = f n := (ha ▸ h2 a (by omega)).symm
    · let u := 3^N*n
      have hu : N < u := by
        have := Nat.mul_le_mul_left (3^N) (show 1 ≤ n by omega)
        dsimp [u]
        have := big 3 N (by decide)
        omega
      have parity : u % 2 = 1 := by
        have hp : 3^N % 2 = 1 := by simp [Nat.pow_mod]
        dsimp [u]
        rw [Nat.mul_mod, hp]
        omega
      have hh : 2 * step (5*u) = 5*(3*u)+1 := by
        simp only [step]
        have hodd : 5*u%2 ≠ 0 := by omega
        rw [ite_eq_right hodd]
        omega
      have hstep := hs (5*u) (by omega)
      have htwo := h2 (step (5*u)) (by omega)
      rw [hh, hr _ (by omega) (by omega), h3 _ (by omega)] at htwo
      have res := hstep.symm.trans htwo.symm
      change f (5*(3^N*n)) = f (3^N*n) at res
      rwa [show 5*(3^N*n)=3^N*(5*n) by ring, powInv 3 (by decide) h3 N _ (by omega),
        powInv 3 (by decide) h3 N n hn] at res

/-- An eventual single affine invariance, together with three dilations
and the actual shortcut step, forces a function to be constant on positive inputs. -/
theorem eventual_five_ray_constant {α : Type*} (f : ℕ → α) (N : ℕ)
    (hstep : ∀ x : ℕ, 0 < x → f (step x) = f x)
    (h2 : ∀ x : ℕ, 0 < x → f (2 * x) = f x)
    (h3 : ∀ x : ℕ, 0 < x → f (3 * x) = f x)
    (h5 : ∀ x : ℕ, 0 < x → f (5 * x) = f x)
    (htail : ∀ t : ℕ, N ≤ t → f (5 * t + 1) = f t) :
    ∀ n : ℕ, 0 < n → f n = f 1 := by
  have h4 (x : ℕ) (hx : 0 < x) : f (4 * x) = f x := by
    rw [show 4 * x = 2 * (2 * x) by ring, h2 _ (by omega), h2 _ hx]
  have h8 (x : ℕ) (hx : 0 < x) : f (8 * x) = f x := by
    rw [show 8 * x = 2 * (4 * x) by ring, h2 _ (by omega), h4 _ hx]
  have odd (x : ℕ) (hx : 0 < x) (ho : x % 2 = 1) : f (3 * x + 1) = f x := by
    have he : 2 * step x = 3 * x + 1 := by simp [step, ho]; omega
    rw [← he, h2 _ (by omega), hstep _ hx]
  have g23 (h : ℕ) (hh : 0 < h) : f (2 * h - 1) = f (3 * h - 1) := by
    calc
      _ = f (3 * (2 * h - 1) + 1) := (odd _ (by omega) (by omega)).symm
      _ = f (2 * (3 * h - 1)) := by congr 1; omega
      _ = _ := h2 _ (by omega)
  have g89 (h : ℕ) (hh : 0 < h) : f (8 * h - 1) = f (9 * h - 1) := by
    calc
      _ = f (3 * (8 * h - 1)) := (h3 _ (by omega)).symm
      _ = f (3 * (3 * (8 * h - 1)) + 1) := (odd _ (by omega) (by omega)).symm
      _ = f (8 * (9 * h - 1)) := by congr 1; omega
      _ = _ := h8 _ (by omega)
  have g48 (h : ℕ) (hh : 0 < h) : f (4 * h - 1) = f (8 * h - 1) := by
    calc
      _ = f (6 * h - 1) := by simpa only [← Nat.mul_assoc] using g23 (2 * h) (by omega)
      _ = f (9 * h - 1) := by simpa only [← Nat.mul_assoc] using g23 (3 * h) (by omega)
      _ = _ := (g89 h hh).symm
  have transport (h j : ℕ) (hh : 0 < h) :
      f (4 * (2 ^ j * h) - 1) = f (4 * h - 1) ∧ f (4 * (2 ^ j * h)) = f (4 * h) := by
    induction j with
    | zero => simp
    | succ j ih =>
      have hp : 0 < 2 ^ j * h := by positivity
      rw [show 4 * (2 ^ (j + 1) * h) = 8 * (2 ^ j * h) by ring]
      have hs : f (8 * (2 ^ j * h)) = f (4 * (2 ^ j * h)) := by
        simpa only [← Nat.mul_assoc] using h2 (4 * (2 ^ j * h)) (by omega)
      exact ⟨(g48 _ hp).symm.trans ih.1, hs.trans ih.2⟩
  have adjacent (h : ℕ) (hh : 0 < h) (hu : h % 5 ≠ 0) : f (4 * h - 1) = f (4 * h) := by
    have big (l : ℕ) : ∃ z, 0 < z ∧ l ≤ z ∧ z % 5 = h % 5 ∧
        f (4 * z - 1) = f (4 * h - 1) ∧ f (4 * z) = f (4 * h) := by
      induction l with
      | zero => exact ⟨h, hh, by omega, rfl, rfl, rfl⟩
      | succ l ih =>
        obtain ⟨z, hz, hl, hc, hminus, hplus⟩ := ih
        obtain ⟨ha, hb⟩ := transport z 4 hz
        exact ⟨16 * z, by omega, by omega, by omega, ha.trans hminus, hb.trans hplus⟩
    obtain ⟨z, hz, hl, hc, hminus, hplus⟩ := big (5 * (N + 1))
    have hj : ∃ j : ℕ, (4 * (2 ^ j * z)) % 5 = 1 := by
      rcases (show z % 5 = 1 ∨ z % 5 = 2 ∨ z % 5 = 3 ∨ z % 5 = 4 by omega) with h | h | h | h
      · exact ⟨2, by omega⟩
      · exact ⟨1, by omega⟩
      · exact ⟨3, by omega⟩
      · exact ⟨0, by omega⟩
    obtain ⟨j, hj⟩ := hj
    have hz' : z ≤ 2 ^ j * z := by
      have hp : 1 ≤ 2 ^ j := Nat.succ_le_of_lt (by positivity : 0 < 2 ^ j)
      simpa using Nat.mul_le_mul_right z hp
    obtain ⟨ha, hb⟩ := transport z j hz
    let t := (4 * (2 ^ j * z)) / 5
    have he : 4 * (2 ^ j * z) = 5 * t + 1 := by dsimp [t]; omega
    calc
      f (4 * h - 1) = f (4 * (2 ^ j * z) - 1) := (ha.trans hminus).symm
      _ = f (5 * t) := by rw [he]; simp
      _ = f t := h5 _ (by omega)
      _ = f (5 * t + 1) := (htail _ (by omega)).symm
      _ = f (4 * h) := by rw [← he]; exact hb.trans hplus
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hn
    by_cases h1 : n = 1
    · rw [h1]
    by_cases he : n % 2 = 0
    · have hx : n = 2 * (n / 2) := by omega
      exact (congrArg f hx).trans ((h2 _ (by omega)).trans (ih _ (by omega) (by omega)))
    have ho : n % 2 = 1 := by omega
    by_cases hm : n % 4 = 1
    · let u := (3 * n + 1) / 4
      have hu : 3 * n + 1 = 4 * u := by dsimp [u]; omega
      calc
        f n = f (3 * n + 1) := (odd _ hn ho).symm
        _ = f u := by rw [hu, h4 _ (by omega)]
        _ = f 1 := ih _ (by omega) (by omega)
    let w := (n + 1) / 4
    have hw : n + 1 = 4 * w := by dsimp [w]; omega
    by_cases hu : w % 5 ≠ 0
    · calc
        f n = f (4 * w - 1) := by congr 1; omega
        _ = f (4 * w) := adjacent _ (by omega) hu
        _ = f w := h4 _ (by omega)
        _ = f 1 := ih _ (by omega) (by omega)
    · let v := (4 * n - 1) / 5
      have hv : 4 * n - 1 = 5 * v := by dsimp [v]; omega
      calc
        f n = f (4 * n) := (h4 _ hn).symm
        _ = f (4 * n - 1) := (adjacent n hn (by omega)).symm
        _ = f v := by rw [hv, h5 _ (by omega)]
        _ = f 1 := ih _ (by omega) (by omega)

/-- A finite exceptional set for the ordinary five-ray merger test can be removed.
The two arms are both iterated by the ordinary shortcut map. -/
theorem collatz_iff_eventual_five_ray :
    (∀ n : ℕ, 0 < n → ∃ j, orbit n j = 1) ↔
    (∃ N : ℕ, ∀ t : ℕ, N ≤ t → Meets t (5*t+1)) := by
  constructor
  · intro hall
    exact ⟨1, fun t ht => collatz_iff_five_ray.mp hall t ht⟩
  · rintro ⟨N, hN⟩
    let f : ℕ → Prop := fun x => Meets x 1
    have lifts {x y : ℕ} (h : Meets x y) : f x = f y :=
      propext ⟨fun hx => meets_trans (meets_symm h) hx, fun hy => meets_trans h hy⟩
    have hs (x : ℕ) (_ : 0 < x) : f (step x) = f x := (lifts (meets_step x)).symm
    have h2 (x : ℕ) (_ : 0 < x) : f (2*x) = f x := (lifts (meets_double x)).symm
    have hr (t : ℕ) (ht : N ≤ t) : f (5*t+1) = f t := (lifts (hN t ht)).symm
    obtain ⟨h3, h5⟩ := component_multipliers f h2 hs N (fun t ht _ => hr t ht)
    intro n hn
    have he := eventual_five_ray_constant f N hs h2 h3 h5 hr n hn
    apply (meets_one_iff n).mp
    change f n
    rw [he]
    exact ⟨0, 0, rfl⟩


private theorem triple_adjacent_ray (r t : ℕ) (he : orbit r 4 = orbit (r + 1) 4)
    (ho : odds r 4 = odds (r + 1) 4) : Meets (r + 16 * t) ((r + 1) + 16 * t) := by
  have hlo := high_bit r 4 t
  have hhi := high_bit (r + 1) 4 t
  norm_num only [Nat.reducePow] at hlo hhi
  rw [he, ho] at hlo
  exact ⟨4, 4, hlo.trans hhi.symm⟩

private theorem triple_residue (h : ℕ) (he : h % 2 ≠ 0) :
    ∃ j : ℕ, (9 * (3 ^ j * h)) % 16 = 3 ∨ (9 * (3 ^ j * h)) % 16 = 5 := by
  rcases (show h%16=1 ∨ h%16=3 ∨ h%16=5 ∨ h%16=7 ∨ h%16=9 ∨ h%16=11 ∨ h%16=13 ∨ h%16=15 by omega)
    with r | r | r | r | r | r | r | r
  · exact ⟨3, Or.inl (by omega)⟩
  · exact ⟨2, Or.inl (by omega)⟩
  · exact ⟨2, Or.inr (by omega)⟩
  · exact ⟨3, Or.inr (by omega)⟩
  · exact ⟨1, Or.inl (by omega)⟩
  · exact ⟨0, Or.inl (by omega)⟩
  · exact ⟨0, Or.inr (by omega)⟩
  · exact ⟨1, Or.inr (by omega)⟩

/-- Checking the single dilation by three on every positive source suffices.
A fixed finite exceptional set is immaterial, since both arms admit the same
initial binary dilation. -/
theorem collatz_iff_eventual_three_ray :
    (∀ n : ℕ, 0 < n → ∃ j, orbit n j = 1) ↔
    (∃ N : ℕ, ∀ x : ℕ, N ≤ x → Meets x (3 * x)) := by
  constructor
  · intro hall
    refine ⟨1, fun x hx => ?_⟩
    exact meets_trans ((meets_one_iff x).2 (hall x hx))
      (meets_symm ((meets_one_iff _).2 (hall _ (by omega))))
  rintro ⟨N, hN⟩
  let f : ℕ → Prop := fun x => Meets x 1
  have lifts {x y : ℕ} (h : Meets x y) : f x = f y :=
    propext ⟨fun hx => meets_trans (meets_symm h) hx, fun hy => meets_trans h hy⟩
  have hstep (x : ℕ) (_ : 0 < x) : f (step x) = f x := (lifts (meets_step x)).symm
  have h2 (x : ℕ) (_ : 0 < x) : f (2 * x) = f x := (lifts (meets_double x)).symm
  have h3 (x : ℕ) (hx : 0 < x) : f (3 * x) = f x := by
    have hp (n : ℕ) : n < 2 ^ n := by
      induction n with
      | zero => decide
      | succ n ih => rw [pow_succ]; omega
    have hbig : N ≤ 2 ^ N * x := by
      have := Nat.mul_le_mul_left (2 ^ N) (show 1 ≤ x by omega)
      have := hp N
      omega
    have res := (lifts (hN _ hbig)).symm
    have scale (y j : ℕ) : f (2 ^ j * y) = f y :=
      lifts (show Meets (2 ^ j * y) y from ⟨j, 0, strip_twos y j⟩)
    rwa [show 3 * (2 ^ N * x) = 2 ^ N * (3 * x) by ring, scale, scale] at res
  have h4 (x : ℕ) (hx : 0 < x) : f (4 * x) = f x := by
    rw [show 4 * x = 2 * (2 * x) by ring, h2 _ (by omega), h2 _ hx]
  have h8 (x : ℕ) (hx : 0 < x) : f (8 * x) = f x := by
    rw [show 8 * x = 2 * (4 * x) by ring, h2 _ (by omega), h4 _ hx]
  have odd (x : ℕ) (hx : 0 < x) (ho : x % 2 = 1) : f (3 * x + 1) = f x := by
    have he : 2 * step x = 3 * x + 1 := by simp [step, ho]; omega
    rw [← he, h2 _ (by omega), hstep _ hx]
  have g23 (h : ℕ) (hh : 0 < h) : f (2 * h - 1) = f (3 * h - 1) := by
    calc
      _ = f (3 * (2 * h - 1) + 1) := (odd _ (by omega) (by omega)).symm
      _ = f (2 * (3 * h - 1)) := by congr 1; omega
      _ = _ := h2 _ (by omega)
  have g89 (h : ℕ) (hh : 0 < h) : f (8 * h - 1) = f (9 * h - 1) := by
    calc
      _ = f (3 * (8 * h - 1)) := (h3 _ (by omega)).symm
      _ = f (3 * (3 * (8 * h - 1)) + 1) := (odd _ (by omega) (by omega)).symm
      _ = f (8 * (9 * h - 1)) := by congr 1; omega
      _ = _ := h8 _ (by omega)
  have g48 (h : ℕ) (hh : 0 < h) : f (4 * h - 1) = f (8 * h - 1) := by
    calc
      _ = f (6 * h - 1) := by simpa only [← Nat.mul_assoc] using g23 (2 * h) (by omega)
      _ = f (9 * h - 1) := by simpa only [← Nat.mul_assoc] using g23 (3 * h) (by omega)
      _ = _ := (g89 h hh).symm
  have g49 (h : ℕ) (hh : 0 < h) : f (4 * h - 1) = f (9 * h - 1) := (g48 h hh).trans (g89 h hh)
  have shift (h i : ℕ) (hh : 0 < h) :
      f (4 * (3 ^ i * h) - 1) = f (4 * h - 1) ∧ f (3 ^ i * h) = f h := by
    induction i with
    | zero => simp
    | succ i ih =>
      let z := 3 ^ i * h
      have hz : 0 < z := by dsimp [z]; positivity
      have hg : f (4 * z - 1) = f (12 * z - 1) := by
        calc
          _ = f (8 * z - 1) := g48 z hz
          _ = _ := by simpa only [← Nat.mul_assoc] using g23 (4 * z) (by omega)
      rw [show 3 ^ (i + 1) * h = 3 * z by dsimp [z]; ring]
      exact ⟨(by simpa only [← Nat.mul_assoc] using hg.symm : f (4 * (3 * z) - 1) = f (4 * z - 1)).trans ih.1,
        (h3 z hz).trans ih.2⟩
  have adjacent_cell (y : ℕ) (hcell : y % 16 = 3 ∨ y % 16 = 5) : f (y - 1) = f y := by
    rcases hcell with h | h
    · have hm := triple_adjacent_ray 2 (y / 16) (by decide) (by decide)
      rw [show 2 + 16 * (y / 16) = y - 1 by omega, show 2+1+16*(y/16) = y by omega] at hm
      exact lifts hm
    · have hm := triple_adjacent_ray 4 (y / 16) (by decide) (by decide)
      rw [show 4 + 16 * (y / 16) = y - 1 by omega, show 4+1+16*(y/16) = y by omega] at hm
      exact lifts hm
  have adjacent (h : ℕ) (hh : 0 < h) : f (4 * h - 1) = f (4 * h) := by
    induction h using Nat.strong_induction_on with
    | h h ih =>
      by_cases he : h % 2 = 0
      · let z := h / 2
        have hz : h = 2 * z := by dsimp [z]; omega
        have hi := ih z (by omega) (by omega)
        have h8z : 4 * h = 8 * z := by omega
        rw [h8z, ← g48 z (by omega), hi, h8 _ (by omega), h4 _ (by omega)]
      have hj := triple_residue h he
      obtain ⟨j, hcell⟩ := hj
      let z := 3 ^ j * h
      have hz : 0 < z := by dsimp [z]; positivity
      obtain ⟨hs, hf⟩ := shift h j hh
      calc
        f (4 * h - 1) = f (4 * z - 1) := hs.symm
        _ = f (9 * z - 1) := g49 z hz
        _ = f (9 * z) := adjacent_cell _ hcell
        _ = f z := by rw [show 9 * z = 3 * (3 * z) by ring, h3 _ (by omega), h3 _ hz]
        _ = f h := hf
        _ = f (4 * h) := (h4 h hh).symm
  have all (n : ℕ) (hn : 0 < n) : f n = f 1 := by
    induction n using Nat.strong_induction_on with
    | h n ih =>
      by_cases h1 : n = 1
      · rw [h1]
      by_cases he : n % 2 = 0
      · have hx : n = 2 * (n / 2) := by omega
        exact (congrArg f hx).trans ((h2 _ (by omega)).trans (ih _ (by omega) (by omega)))
      have ho : n % 2 = 1 := by omega
      by_cases hm : n % 4 = 1
      · let u := (3 * n + 1) / 4
        have hu : 3 * n + 1 = 4 * u := by dsimp [u]; omega
        calc
          f n = f (3 * n + 1) := (odd _ hn ho).symm
          _ = f u := by rw [hu, h4 _ (by omega)]
          _ = f 1 := ih _ (by omega) (by omega)
      let w := (n + 1) / 4
      have hw : n + 1 = 4 * w := by dsimp [w]; omega
      calc
        f n = f (4 * w - 1) := by congr 1; omega
        _ = f (4 * w) := adjacent _ (by omega)
        _ = f w := h4 _ (by omega)
        _ = f 1 := ih _ (by omega) (by omega)
  intro n hn
  apply (meets_one_iff n).mp
  change f n
  rw [all n hn]
  exact ⟨0, 0, rfl⟩

theorem collatz_iff_three_ray :
    (∀ n : ℕ, 0 < n → ∃ j, orbit n j = 1) ↔
    (∀ x : ℕ, 0 < x → Meets x (3 * x)) := by
  constructor
  · intro hall x hx
    exact meets_trans ((meets_one_iff x).2 (hall x hx))
      (meets_symm ((meets_one_iff _).2 (hall _ (by omega))))
  · intro hx
    exact collatz_iff_eventual_three_ray.mpr ⟨1, fun x h => hx x h⟩

/-- A failed multiplication by three at an odd positive input forces
another failure, at a strictly larger odd input bounded by 27 times the first. -/
theorem three_defect_successor {α : Type*} (f : ℕ → α)
    (hs : ∀ n, f (step n) = f n) (x : ℕ) (hx : x % 2 = 1) (hbad : f x ≠ f (3 * x)) :
    ∃ y : ℕ, x < y ∧ y ≤ 27 * x ∧ y % 2 = 1 ∧ f y ≠ f (3 * y) := by
  classical
  by_contra hnone
  have good (y : ℕ) (hy : x < y) (hb : y ≤ 27 * x) (ho : y % 2 = 1) : f y = f (3 * y) := by
    by_contra h
    exact hnone ⟨y, hy, hb, ho, h⟩
  have inv (n j : ℕ) : f (orbit n j) = f n := by
    induction j with
    | zero => rfl
    | succ j ih => exact (hs _).trans ih
  have h2 (n : ℕ) : f (2 * n) = f n := by
    have h := hs (2 * n)
    simpa [step] using h.symm
  have h4 (n : ℕ) : f (4 * n) = f n := by
    rw [show 4 * n = 2 * (2 * n) by ring, h2, h2]
  have h8 (n : ℕ) : f (8 * n) = f n := by
    rw [show 8 * n = 2 * (4 * n) by ring, h2, h4]
  have odd (n : ℕ) (ho : n % 2 = 1) : f n = f (3 * n + 1) := by
    have he : 2 * step n = 3 * n + 1 := by simp [step, ho]; omega
    rw [← he, h2, hs]
  have hx1 : 1 < x := by
    have h13 := inv 3 5
    have hv : orbit 3 5 = 1 := by decide
    rw [hv] at h13
    by_contra! h
    have he : x = 1 := by omega
    exact hbad (by simpa [he] using h13)
  apply hbad
  have J43 (u : ℕ) : f (4*u+1) = f (3*u+1) := by
    calc
      _ = f (3 * (4 * u + 1) + 1) := odd _ (by omega)
      _ = f (4 * (3 * u + 1)) := by congr 1; ring
      _ = _ := h4 _
  by_cases hz3 : x % 3 = 0
  · let s := x/3
    have hx3 : x = 3*s := by dsimp [s]; omega
    have join (a : ℕ) (hg : f (16*a+1) = f (3*(16*a+1))) :
        f (9*a+1) = f (18*a+1) := by
      have hb := high_bit 3 2 (12 * a)
      have hv : orbit 3 2 = 8 ∧ odds 3 2 = 2 := by decide
      rw [hv.1, hv.2] at hb
      have hr := inv (3 + 2 ^ 2 * (12 * a)) 2
      rw [hb] at hr
      calc
        _ = f (12*a+1) := by simpa only [← Nat.mul_assoc] using (J43 (3*a)).symm
        _ = f (16*a+1) := by simpa only [← Nat.mul_assoc] using (J43 (4*a)).symm
        _ = f (3*(16*a+1)) := hg
        _ = f (8+3^2*(12*a)) := (congrArg f (by ring : 3*(16*a+1) = 3+2^2*(12*a))).trans hr.symm
        _ = f (4*(27*a+2)) := by congr 1; ring
        _ = f (27*a+2) := h4 _
        _ = f (18*a+1) := by
          have hh := odd (18*a+1) (by omega)
          rw [show 3*(18*a+1)+1=2*(27*a+2) by ring, h2] at hh
          exact hh.symm
    have hA := join s (good _ (by omega) (by omega) (by omega))
    have hB := join (2*s) (good _ (by omega) (by omega) (by omega))
    have hC := J43 (9*s)
    calc
      f x = f (3*x+1) := odd x hx
      _ = f (9*s+1) := by congr 1; omega
      _ = f (18*s+1) := hA
      _ = f (36*s+1) := by simpa only [← Nat.mul_assoc] using hB
      _ = f (27*s+1) := by simpa only [← Nat.mul_assoc] using hC
      _ = f (3*x) := by
        have hh := odd (3*x) (by omega)
        rw [show 3*(3*x)+1=27*s+1 by omega] at hh
        exact hh.symm
  have g23 (u : ℕ) (hu : 0 < u) : f (2*u-1) = f (3*u-1) := by
    calc
      _ = f (3*(2*u-1)+1) := odd _ (by omega)
      _ = f (2*(3*u-1)) := by congr 1; omega
      _ = _ := h2 _
  have gp (u j : ℕ) (hu : 0 < u) : f (2^j*u-1) = f (3^j*u-1) := by
    induction j generalizing u with
    | zero => simp
    | succ j ih =>
      have hp : 0 < 2^j*u := by positivity
      rw [show 2^(j+1)*u=2*(2^j*u) by ring, g23 _ hp,
          show 3*(2^j*u)=2^j*(3*u) by ring, ih (3*u) (by omega), show 3^j*(3*u)=3^(j+1)*u by ring]
  have start (M j : ℕ) (hz : 3 * ((M*x-1)/3) = M*x-1)
      (ho : ((M*x-1)/3)%2=1) (hl : x < (M*x-1)/3) (hb : (M*x-1)/3 ≤ 27*x)
      (hm : M = 2^j) : f x = f (3^j*x-1) := by
    let z := (M*x-1)/3
    have hmpos : 0 < M*x := by rw [hm]; positivity
    have hodd := odd z ho
    have scale (j : ℕ) : f (2^j*x) = f x :=
      (inv (2^j*x) j).symm.trans (congrArg f (strip_twos x j))
    calc
      f x = f (M*x) := by rw [hm, scale]
      _ = f z := by rw [hodd, hz]; congr 1; omega
      _ = f (3*z) := good _ hl hb ho
      _ = f (2^j*x-1) := by rw [hz, hm]
      _ = _ := gp _ _ (by omega)
  have hstart : f x = f (9*x-1) ∨ f x = f (27*x-1) := by
    by_cases h : x%3 = 1
    · exact Or.inl (start 4 2 (by omega) (by omega) (by omega) (by omega) (by decide))
    · exact Or.inr (start 8 3 (by omega) (by omega) (by omega) (by omega) (by decide))
  have bridge (Q : ℕ) (hq : 0 < Q) (hg : f (8*Q-1) = f (3*(8*Q-1))) :
      f (9*Q-1) = f (27*Q-1) := by
    have hodd := odd (3*(8*Q-1)) (by omega)
    rw [show 3*(3*(8*Q-1))+1 = 8*(9*Q-1) by omega, h8] at hodd
    exact (hg.trans hodd).symm.trans (gp Q 3 hq)
  have A := bridge x (by omega) (good _ (by omega) (by omega) (by omega))
  have B : f (27*x-1) = f (81*x-1) := by
    simpa only [← Nat.mul_assoc] using bridge (3*x) (by omega) (good _ (by omega) (by omega) (by omega))
  have S : f x = f (9*x-1) := hstart.elim id (fun h => h.trans A.symm)
  have V : f (3*x) = f (9*x) := by
    simpa only [← Nat.mul_assoc] using good (3*x) (by omega) (by omega) (by omega)
  have W : f (9*x) = f (27*x) := by
    simpa only [← Nat.mul_assoc] using good (9*x) (by omega) (by omega) (by omega)
  have U : f (27*x) = f (81*x) := by
    simpa only [← Nat.mul_assoc] using good (27*x) (by omega) (by omega) (by omega)
  have pair (r h t : ℕ) (he : orbit r h = orbit (r+1) h) (ho : odds r h = odds (r+1) h) :
      f (r+2^h*t) = f (r+1+2^h*t) := by
    have h0 := high_bit r h t
    have h1 := high_bit (r+1) h t
    rw [he,ho] at h0
    exact (inv _ h).symm.trans ((congrArg f (h0.trans h1.symm)).trans (inv _ h))
  by_cases hxcell : x%16=1
  · have alt := pair 5 5 (3*(x/16)) (by decide) (by decide)
    rw [show 5+2^5*(3*(x/16))=6*x-1 by omega, show 5+1+2^5*(3*(x/16))=2*(3*x) by omega, h2] at alt
    have exch := g23 (3*x) (by omega)
    rw [show 3*(3*x)=9*x by ring, show 2*(3*x)=6*x by ring] at exch
    exact S.trans (exch.symm.trans alt)
  have cell (y : ℕ) (hc : y % 16 = 3 ∨ y % 8 = 5) : f (y-1) = f y := by
    rcases hc with h|h
    · have hres := pair 2 4 (y/16) (by decide) (by decide)
      rwa [show 2+2^4*(y/16)=y-1 by omega, show 2+1+2^4*(y/16)=y by omega] at hres
    · have hres := pair 4 3 (y/8) (by decide) (by decide)
      rwa [show 4+2^3*(y/8)=y-1 by omega, show 4+1+2^3*(y/8)=y by omega] at hres
  have options : (9*x%16=3 ∨ 9*x%8=5) ∨ (27*x%16=3 ∨ 27*x%8=5) ∨ (81*x%16=3 ∨ 81*x%8=5) := by
    rcases (show x%16=3 ∨ x%16=5 ∨ x%16=7 ∨ x%16=9 ∨ x%16=11 ∨ x%16=13 ∨ x%16=15 by omega)
      with h|h|h|h|h|h|h <;> omega
  rcases options with h | h | h
  · exact S.trans ((cell _ h).trans V.symm)
  · exact (S.trans A).trans ((cell _ h).trans (V.trans W).symm)
  · exact ((S.trans A).trans B).trans ((cell _ h).trans ((V.trans W).trans U).symm)

/-- It suffices that the orbits of x and 3x meet for all sufficiently large
odd x. -/
theorem collatz_iff_eventual_odd_three_ray :
    (∀ n : ℕ, 0 < n → ∃ j, orbit n j = 1) ↔
    (∃ N : ℕ, ∀ x : ℕ, N ≤ x → x % 2 = 1 → Meets x (3*x)) := by
  constructor
  · intro all
    exact ⟨1, fun x hx _ => collatz_iff_three_ray.mp all x hx⟩
  rintro ⟨N, H⟩
  apply collatz_iff_three_ray.mpr
  have odd_good (x : ℕ) (hx : x % 2 = 1) : Meets x (3*x) := by
    let f : ℕ → Prop := fun t => Meets t x
    have lift {a b : ℕ} (hab : Meets a b) : f a = f b :=
      propext ⟨fun ha => meets_trans (meets_symm hab) ha, fun hb => meets_trans hab hb⟩
    have hs (n : ℕ) : f (step n) = f n := (lift (meets_step n)).symm
    by_contra h
    have d : f x ≠ f (3*x) := by
      intro he
      have hx0 : f x := ⟨0,0,rfl⟩
      exact h (meets_symm (he ▸ hx0 : f (3*x)))
    have climb (j : ℕ) : ∃ y : ℕ, x+j ≤ y ∧ y%2 = 1 ∧ f y ≠ f (3*y) := by
      induction j with
      | zero => exact ⟨x, by omega, hx, d⟩
      | succ j ih =>
        obtain ⟨y,hy,ho,hd⟩ := ih
        obtain ⟨z,hz,_,hzodd,hdef⟩ := three_defect_successor f hs y ho hd
        exact ⟨z, by omega, hzodd, hdef⟩
    obtain ⟨y,hy,ho,hd⟩ := climb N
    exact hd (lift (H y (by omega) ho))
  intro n hn
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases ho : n%2 = 1
    · exact odd_good n ho
    let t := n / 2
    have he : n = 2*t := by dsimp [t]; omega
    have ht := ih t (by omega) (by omega)
    rw [he, show 3*(2*t) = 2*(3*t) by ring]
    exact meets_trans (meets_symm (meets_double t)) (meets_trans ht (meets_double (3*t)))

/-- A single defect puts an odd defect in every later multiplicative window. -/
theorem three_defect_in_every_window {α : Type*} (f : ℕ → α)
    (hs : ∀ n, f (step n) = f n) (x : ℕ) (ho : x%2=1) (hd : f x ≠ f (3*x))
    (R : ℕ) (hR : x ≤ R) :
    ∃ y : ℕ, R < y ∧ y ≤ 27*R ∧ y%2=1 ∧ f y ≠ f (3*y) := by
  by_contra hnone
  have climb (j : ℕ) : ∃ y : ℕ, x+j ≤ y ∧ y ≤ R ∧ y%2=1 ∧ f y ≠ f (3*y) := by
    induction j with
    | zero => exact ⟨x, by omega, hR, ho, hd⟩
    | succ j ih =>
      obtain ⟨y, hy, hyR, hyo, hyd⟩ := ih
      obtain ⟨z, hz, hb, hzo, hzd⟩ := three_defect_successor f hs y hyo hyd
      have hzR : z ≤ R := by
        by_contra! hRz
        exact hnone ⟨z,hRz,by omega,hzo,hzd⟩
      exact ⟨z,by omega,hzR,hzo,hzd⟩
  obtain ⟨_, hlow, hupp, _, _⟩ := climb (R+1)
  omega

/-- Arbitrarily far out, one clean multiplicative window of ratio 27 suffices. -/
theorem collatz_iff_clean_three_windows :
    (∀ n : ℕ, 0 < n → ∃ j, orbit n j = 1) ↔
    (∀ X : ℕ, ∃ R : ℕ, X ≤ R ∧
      ∀ y : ℕ, R < y → y ≤ 27*R → y%2=1 → Meets y (3*y)) := by
  constructor
  · intro all X
    exact ⟨X, le_rfl, fun y hy _ _ => collatz_iff_three_ray.mp all y (by omega)⟩
  intro H
  apply collatz_iff_eventual_odd_three_ray.mpr
  refine ⟨1, ?_⟩
  intro x _ hxo
  obtain ⟨R, hR, hgood⟩ := H x
  let f : ℕ → Prop := fun n => Meets n x
  have lift {a b : ℕ} (hab : Meets a b) : f a = f b :=
    propext ⟨fun ha => meets_trans (meets_symm hab) ha, fun hb => meets_trans hab hb⟩
  have hs (n : ℕ) : f (step n) = f n := (lift (meets_step n)).symm
  by_contra h
  have d : f x ≠ f (3*x) := by
    intro he
    have hxx : f x := ⟨0,0,rfl⟩
    exact h (meets_symm (he ▸ hxx : f (3*x)))
  obtain ⟨y,hy,hb,ho,hd⟩ := three_defect_in_every_window f hs x hxo d R hR
  exact hd (lift (hgood y hy hb ho))

/-- Every set containing one, constant along ordinary orbits, and closed under
the *forward* operation x ↦ 3x contains every positive integer. -/
theorem three_forward_generates (P : ℕ → Prop)
    (hs : ∀ n, P (step n) ↔ P n) (hm : ∀ n, 0 < n → P n → P (3*n))
    (h1 : P 1) : ∀ n, 0 < n → P n := by
  have it (n j : ℕ) : P (orbit n j) ↔ P n := by
    induction j with
    | zero => rfl
    | succ j ih => exact (hs _).trans ih
  have lift {a b : ℕ} (h : Meets a b) : P a ↔ P b := by
    obtain ⟨i,j,e⟩ := h
    exact (it a i).symm.trans (e ▸ it b j)
  have h2 (n : ℕ) : P (2*n) ↔ P n := (lift (meets_double n)).symm
  have mult (n k : ℕ) (hn : 0 < n) (hp : P n) : P (3^k*n) := by
    induction k with
    | zero => simpa using hp
    | succ k ih =>
      rw [show 3^(k+1)*n = 3*(3^k*n) by ring]
      exact hm _ (by positivity) ih
  have odd (x : ℕ) (hx : x%2=1) : P (3*x+1) ↔ P x := by
    have he : 2*step x = 3*x+1 := by simp [step,hx]; omega
    rw [← he]
    exact (h2 _).trans (hs _)
  have g23 (h : ℕ) (hh : 0<h) : P (2*h-1) ↔ P (3*h-1) := by
    have ho := (odd (2*h-1) (by omega)).symm
    rw [show 3*(2*h-1)+1=2*(3*h-1) by omega] at ho
    exact ho.trans (h2 _)
  have exch (i w : ℕ) (hw : 0<w) : P (2^i*w-1) ↔ P (3^i*w-1) := by
    induction i generalizing w with
    | zero => simp
    | succ i ih =>
      have e := g23 (2^i*w) (by positivity)
      rw [show 2^(i+1)*w=2*(2^i*w) by ring,
          show 3^(i+1)*w=3^i*(3*w) by ring]
      exact e.trans (by simpa only [Nat.mul_left_comm] using ih (3*w) (by omega))
  have g49 (h : ℕ) (hh : 0<h) : P (4*h-1) ↔ P (9*h-1) := exch 2 h hh
  have down (h : ℕ) (hh : 0<h) (hin : P (8*h-1)) : P (4*h-1) := by
    have htrip := hm (8*h-1) (by omega) hin
    have ho := (odd (3*(8*h-1)) (by omega)).mpr htrip
    rw [show 3*(3*(8*h-1))+1=8*(9*h-1) by omega] at ho
    apply (g49 h hh).mpr
    exact (lift (show Meets (8*(9*h-1)) (9*h-1) from ⟨3,0,strip_twos (9*h-1) 3⟩)).mp ho
  have shift (i h : ℕ) (hh : 0<h) : P (4*(3^i*h)-1) → P (4*h-1) := by
    induction i with
    | zero => simp
    | succ i ih =>
      let z := 3^i*h
      have hz : 0<z := by dsimp [z]; positivity
      intro hnext
      have hnext' : P (3*(4*z)-1) := by
        rwa [show 3*(4*z)=4*(3^(i+1)*h) by dsimp [z]; ring]
      have prev := (g23 (4*z) (by omega)).mpr hnext'
      exact ih (down z hz (by simpa only [← Nat.mul_assoc] using prev))
  have cell (y : ℕ) (hy : y%16=3 ∨ y%16=5) : P y → P (y-1) := by
    rcases hy with e | e
    · have h := triple_adjacent_ray 2 (y/16) (by decide) (by decide)
      rw [show 2+16*(y/16)=y-1 by omega, show 2+1+16*(y/16)=y by omega] at h
      exact (lift h).mpr
    · have h := triple_adjacent_ray 4 (y/16) (by decide) (by decide)
      rw [show 4+16*(y/16)=y-1 by omega, show 4+1+16*(y/16)=y by omega] at h
      exact (lift h).mpr
  have fac (n : ℕ) (hn : 0<n) : ∃ v u : ℕ, u%2=1 ∧ n=2^v*u := by
    induction n using Nat.strong_induction_on with
    | h n ih =>
      by_cases ho : n%2=1
      · exact ⟨0,n,ho,by simp⟩
      obtain ⟨v,u,hodd,eq⟩ := ih (n/2) (by omega) (by omega)
      exact ⟨v+1,u,hodd,by rw [show 2^(v+1)*u=2*(2^v*u) by ring, ← eq]; omega⟩
  have descent (h : ℕ) (hh : 0<h) (ph : P h) : P (4*h-1) := by
    obtain ⟨v,u,hu,he⟩ := fac h hh
    have hu0 : 0<u := by omega
    have pu := (lift (show Meets (2^v*u) u from ⟨v,0,strip_twos u v⟩)).mp (he ▸ ph)
    let w := 3^v*u
    have hw : 0<w := by dsimp [w]; positivity
    have oddpow : 3^v%2=1 := by simp [Nat.pow_mod]
    have wo : w%2≠0 := by dsimp [w]; rw [Nat.mul_mod, oddpow, hu]; decide
    obtain ⟨j,hcell⟩ := triple_residue w wo
    have zpos : 0<3^j*w := by positivity
    have pz := mult w j hw (mult u v hu0 pu)
    have py := mult (3^j*w) 2 zpos pz
    have phigh := cell (9*(3^j*w)) hcell py
    have pw4 := shift j w hw ((g49 (3^j*w) zpos).mpr phigh)
    have e := exch v (4*u) (by omega)
    have ee : P (4*h-1) ↔ P (4*w-1) := by
      dsimp [w]; rw [he]
      simpa only [Nat.mul_left_comm] using e
    exact ee.mpr pw4
  intro n hn
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases hone : n=1
    · simpa [hone] using h1
    by_cases he : n%2=0
    · have e : n=2*(n/2) := by omega
      exact e ▸ (h2 _).mpr (ih (n/2) (by omega) (by omega))
    by_cases hfour : n%4=1
    · let a := (3*n+1)/4
      have ha : 3*n+1=4*a := by dsimp [a]; omega
      have pa := ih a (by dsimp [a]; omega) (by dsimp [a]; omega)
      apply (odd n (by omega)).mp
      rw [ha]
      exact (lift (show Meets (4*a) a from ⟨2,0,strip_twos a 2⟩)).mpr pa
    let h := (n+1)/4
    have hh : 0<h := by dsimp [h]; omega
    have eq : 4*h-1=n := by dsimp [h]; omega
    exact eq ▸ descent h hh (ih h (by dsimp [h]; omega) hh)

/-- To settle all positive orbits it suffices to show that tripling each
start already known to reach 1 produces another start reaching 1. -/
theorem collatz_iff_basin_closed_under_three :
    (∀ n : ℕ, 0<n → ∃ j, orbit n j=1) ↔
    (∀ n : ℕ, 0<n → (∃ j, orbit n j=1) → ∃ k, orbit (3*n) k=1) := by
  constructor
  · intro hall n hn _
    exact hall (3*n) (by omega)
  · intro h
    let P : ℕ → Prop := fun n => Meets n 1
    have inv (n : ℕ) : P (step n) ↔ P n :=
      ⟨fun p => meets_trans (meets_step n) p, fun p => meets_trans (meets_symm (meets_step n)) p⟩
    have hm (n : ℕ) (hn : 0<n) (hp : P n) : P (3*n) :=
      (meets_one_iff _).mpr (h n hn ((meets_one_iff n).mp hp))
    intro n hn
    exact (meets_one_iff n).mp (three_forward_generates P inv hm ⟨0,0,rfl⟩ n hn)

/-- On the class 1 modulo 64, five shortcut steps convert tripling into an
adjacent-pair comparison, preserving both merger components. -/
theorem triple_cell64_adjacent (k : ℕ) :
    Meets (64*k+1) (3*(64*k+1)) ↔ Meets (54*k+1) (54*k+2) := by
  have h1 := high_bit 1 5 (2*k)
  have h3 := high_bit 3 5 (6*k)
  rw [show orbit 1 5 = 2 by decide, show odds 1 5 = 3 by decide] at h1
  rw [show orbit 3 5 = 1 by decide, show odds 3 5 = 2 by decide] at h3
  have a : Meets (64*k+1) (54*k+2) := ⟨5,0,by change orbit _ 5 = 54*k+2; rw [show 64*k+1 = 1+2^5*(2*k) by ring, h1]; ring⟩
  have b : Meets (3*(64*k+1)) (54*k+1) := ⟨5,0,by change orbit _ 5 = 54*k+1; rw [show 3*(64*k+1) = 3+2^5*(6*k) by ring, h3]; ring⟩
  exact ⟨fun h => meets_trans (meets_symm b) (meets_trans (meets_symm h) a),
    fun h => meets_trans a (meets_trans (meets_symm h) (meets_symm b))⟩

/-- Two ordinary steps convert the adjacent pair starting at 4u+1 into the
adjacent pair starting at 3u+1, on both complete affine families. -/
theorem adjacent_three_four (u : ℕ) :
    Meets (3*u+1) (3*u+2) ↔ Meets (4*u+1) (4*u+2) := by
  have h1 := high_bit 1 2 u
  have h2 := high_bit 2 2 u
  rw [show orbit 1 2 = 1 by decide, show odds 1 2 = 1 by decide] at h1
  rw [show orbit 2 2 = 2 by decide, show odds 2 2 = 1 by decide] at h2
  have a : Meets (4*u+1) (3*u+1) :=
    ⟨2,0,by change orbit _ 2 = 3*u+1; rw [show 4*u+1 = 1+2^2*u by ring, h1]; ring⟩
  have b : Meets (4*u+2) (3*u+2) :=
    ⟨2,0,by change orbit _ 2 = 3*u+2; rw [show 4*u+2 = 2+2^2*u by ring, h2]; ring⟩
  exact ⟨fun h => meets_trans a (meets_trans h (meets_symm b)),
    fun h => meets_trans (meets_symm a) (meets_trans h b)⟩

theorem triple_cell64_adjacent128 (k : ℕ) :
    Meets (64*k+1) (3*(64*k+1)) ↔ Meets (128*k+1) (128*k+2) := by
  have h1 := adjacent_three_four (18*k)
  have h2 := adjacent_three_four (24*k)
  have h3 := adjacent_three_four (32*k)
  simp only [← Nat.mul_assoc] at h1 h2 h3
  exact (triple_cell64_adjacent k).trans (h1.trans (h2.trans h3))

/-- On an odd residue class, both adjacent starts land on the corresponding
smaller adjacent starts in exactly seven shortcut steps. -/
theorem adjacent_odd_descent (k : ℕ) :
    orbit (54*(128*k+19)+1) 7 = 54*(27*k+4)+1 ∧
    orbit (54*(128*k+19)+2) 7 = 54*(27*k+4)+2 := by
  have a := high_bit 1027 7 (54*k)
  have b := high_bit 1028 7 (54*k)
  rw [show orbit 1027 7 = 217 by decide, show odds 1027 7 = 3 by decide] at a
  rw [show orbit 1028 7 = 218 by decide, show odds 1028 7 = 3 by decide] at b
  constructor
  · rw [show 54*(128*k+19)+1 = 1027+2^7*(54*k) by ring, a]; ring
  · rw [show 54*(128*k+19)+2 = 1028+2^7*(54*k) by ring, b]; ring

/-- A fixed pair of clock words transports the all-member test to a single
adjacent pair per block of 2^23 positive integers. -/
theorem triple_cell4096_adjacent_shifted (k : ℕ) :
    Meets (4096*k+1) (3*(4096*k+1)) ↔
    Meets (2^23*k+6464) (2^23*k+6465) := by
  have u := high_bit 6464 23 k
  have v := high_bit 6465 23 k
  have a := high_bit 1 7 (27*k)
  have b := high_bit 2 7 (27*k)
  rw [show orbit 6464 23 = 2 by decide, show odds 6464 23 = 7 by decide] at u
  rw [show orbit 6465 23 = 1 by decide, show odds 6465 23 = 6 by decide] at v
  rw [show orbit 1 7 = 2 by decide, show odds 1 7 = 4 by decide] at a
  rw [show orbit 2 7 = 1 by decide, show odds 2 7 = 3 by decide] at b
  have h1 : Meets (2^23*k+6464) (3456*k+1) := by
    refine ⟨23,7,?_⟩
    rw [Nat.add_comm (2^23*k), show 3456*k+1 = 1+2^7*(27*k) by ring, u, a]; ring
  have h2 : Meets (2^23*k+6465) (3456*k+2) := by
    refine ⟨23,7,?_⟩
    rw [Nat.add_comm (2^23*k), show 3456*k+2 = 2+2^7*(27*k) by ring, v, b]; ring
  have test := triple_cell64_adjacent (64*k)
  simp only [← Nat.mul_assoc] at test
  exact test.trans ⟨fun h => meets_trans h1 (meets_trans h (meets_symm h2)),
    fun h => meets_trans (meets_symm h1) (meets_trans h h2)⟩

/-- The directed tripling edge at 16k+1 has the same target component as 32k+1. -/
theorem triple_cell16_binary_extension (k : ℕ) : Meets (3*(16*k+1)) (32*k+1) := by
  have a := high_bit 3 4 (3*k)
  have b := high_bit 1 5 k
  rw [show orbit 3 4 = 2 by decide, show odds 3 4 = 2 by decide] at a
  rw [show orbit 1 5 = 2 by decide, show odds 1 5 = 3 by decide] at b
  refine ⟨4,5,?_⟩
  rw [show 3*(16*k+1) = 3+2^4*(3*k) by ring, show 32*k+1 = 1+2^5*k by ring, a, b]; ring

/-- A Mersenne start takes precisely h odd steps through the end of its
initial run, giving the shifted ternary power at the same clock. -/
theorem mersenne_forced_segment (h : ℕ) :
    orbit (2^h-1) h = 3^h-1 ∧ odds (2^h-1) h = h := by
  have cycle (j : ℕ) : mirrorOrbit 1 j = 1 ∧ mirrorOdds 1 j = j := by
    induction j with
    | zero => simp [mirrorOrbit, mirrorOdds]
    | succ j ih => simp [mirrorOrbit, mirrorOdds, ih.1, ih.2, mirrorStep]
  have hp : 0 < (2:ℕ)^h := by positivity
  obtain ⟨he,ho⟩ := mirror_lift (2^h-1) 1 h 1 (by decide) (by omega)
  rw [(cycle h).1, (cycle h).2, Nat.mul_one] at he
  exact ⟨by omega, ho.trans (cycle h).2⟩

private theorem rank_two_four (k : ℕ) :
    orbit (16*k+1) 4 = 9*k+1 ∧ odds (16*k+1) 4 = 2 := by
  have a := high_bit 1 4 k
  have b := odds_high_bit 1 4 k
  rw [show orbit 1 4 = 1 by decide, show odds 1 4 = 2 by decide] at a
  rw [show odds 1 4 = 2 by decide] at b
  rw [show 16*k+1 = 1+2^4*k by ring]
  exact ⟨a.trans (by ring), b⟩

private theorem rank_two_exponents (m : ℕ) : ∃ k : ℕ, 9*k+1 = 2^(6*m) := by
  induction m with
  | zero => exact ⟨0, rfl⟩
  | succ m ih =>
    obtain ⟨k,hk⟩ := ih
    exact ⟨64*k+7, by rw [show 6*(m+1) = 6*m+6 by ring, pow_add, ← hk]; ring⟩

/-- The one-sided basin implication contains a fully witnessed infinite family.
The source reaches 1 using two odd inputs, and the other arm reaches the
specified ternary checkpoint after a forced Mersenne run. -/
theorem rank_two_mersenne_witness (m : ℕ) : ∃ k : ℕ,
    9*k+1 = 2^(6*m) ∧
    orbit (16*k+1) (4+6*m) = 1 ∧ odds (16*k+1) (4+6*m) = 2 ∧
    orbit (32*k+1) 4 = 2^(6*m+1)-1 ∧
    orbit (32*k+1) (4+(6*m+1)) = 3^(6*m+1)-1 ∧
    odds (32*k+1) (4+(6*m+1)) = 2+(6*m+1) := by
  obtain ⟨k,hk⟩ := rank_two_exponents m
  obtain ⟨ax,ac⟩ := rank_two_four k
  obtain ⟨ay,bc⟩ := rank_two_four (2*k)
  rw [show 16*(2*k) = 32*k by ring] at ay bc
  have shift : 9*(2*k)+1 = 2^(6*m+1)-1 := by rw [pow_succ, ← hk]; omega
  rw [shift] at ay
  have coat : odds (2^(6*m)) (6*m) = 0 := by
    simpa using (odds_high_bit 0 (6*m) 1).trans (zero_prefix (6*m)).2
  have land : orbit (2^(6*m)) (6*m) = 1 := by simpa using strip_twos 1 (6*m)
  have endWord := mersenne_forced_segment (6*m+1)
  refine ⟨k,hk,?_,?_,ay,?_,?_⟩
  · rw [orbit_add, ax, hk, land]
  · rw [odds_add, ax, ac, hk, coat]
  · rw [orbit_add, ay, endWord.1]
  · rw [odds_add, ay, bc, endWord.2]

private theorem six_divides_exponent (j : ℕ) (hp : (2^j:ℕ)%9 = 1) :
    ∃ m : ℕ, j=6*m := by
  induction j using Nat.strong_induction_on with
  | h j ih =>
    by_cases small : j<6
    · have cases : j=0 ∨ j=1 ∨ j=2 ∨ j=3 ∨ j=4 ∨ j=5 := by omega
      rcases cases with f | f | f | f | f | f
      · exact ⟨0, by omega⟩
      all_goals subst j; norm_num at hp
    · let v := j-6
      have hv : j=v+6 := by dsimp [v]; omega
      have pw : (2:ℕ)^j = 64*2^v := by rw [hv,pow_add]; ring
      rw [pw] at hp
      obtain ⟨m,hm⟩ := ih v (by omega) (by omega)
      exact ⟨m+1, by omega⟩

/-- A two-odd-step witness on the antecedent is possible exactly in the
geometric progression parametrized by powers of 64. -/
theorem rank_two_antecedent_iff (k : ℕ) :
    (∃ h, orbit (16*k+1) h = 1 ∧ odds (16*k+1) h = 2) ↔
    ∃ m : ℕ, 9*k+1 = 2^(6*m) := by
  constructor
  · rintro ⟨h,hy,ho⟩
    by_cases short : h<4
    · have bound := affine (16*k+1) h
      rw [hy, ho] at bound
      have low : 2^h ≤ (2:ℕ)^3 := Nat.pow_le_pow_right (by decide) (by omega)
      exact ⟨0, by norm_num at bound low ⊢; omega⟩
    · let t := h-4
      have he : h=4+t := by dsimp [t]; omega
      obtain ⟨a,b⟩ := rank_two_four k
      rw [he, orbit_add, a] at hy
      rw [he, odds_add, a, b] at ho
      have odd : odds (9*k+1) t = 0 := by omega
      have ev : evens (9*k+1) t = t := by have := counts (9*k+1) t; omega
      have z := offset_budget (9*k+1) t
      rw [odd,ev] at z
      simp at z
      have af := affine (9*k+1) t
      rw [hy,odd,z] at af
      simp at af
      have md : (2^t:ℕ)%9 = 1 := by omega
      obtain ⟨m,hm⟩ := six_divides_exponent t md
      exact ⟨m, by rw [←hm]; omega⟩
  · rintro ⟨m,hm⟩
    obtain ⟨w,hw,hy,ho,_⟩ := rank_two_mersenne_witness m
    have e : w=k := by omega
    exact ⟨4+6*m, e ▸ hy, e ▸ ho⟩

/-- Exactly the two-odd-step layer of the directed criterion is equivalent
to convergence of every indicated shifted ternary power. -/
theorem rank_two_directed_iff_shifted_powers :
    (∀ k : ℕ, (∃ h, orbit (16*k+1) h = 1 ∧ odds (16*k+1) h = 2) →
      ∃ i, orbit (32*k+1) i = 1) ↔
    ∀ m : ℕ, ∃ i, orbit (3^(6*m+1)-1) i = 1 := by
  constructor
  · intro directed m
    obtain ⟨k,_,hy,ho,_,hu,_⟩ := rank_two_mersenne_witness m
    have link : Meets (32*k+1) (3^(6*m+1)-1) := ⟨4+(6*m+1),0,hu⟩
    exact (meets_one_iff _).mp (meets_trans (meets_symm link)
      ((meets_one_iff _).mpr (directed k ⟨4+6*m,hy,ho⟩)))
  · intro powers k h
    obtain ⟨m,hm⟩ := (rank_two_antecedent_iff k).mp h
    obtain ⟨w,hw,_,_,_,hu,_⟩ := rank_two_mersenne_witness m
    have e : w=k := by omega
    have link : Meets (32*k+1) (3^(6*m+1)-1) := ⟨4+(6*m+1),0,e ▸ hu⟩
    exact (meets_one_iff _).mp (meets_trans link ((meets_one_iff _).mpr (powers m)))

/-- Both arms have a common affine endpoint after four odd inputs on each
path, on the whole class k = 32w + 18. -/
theorem rank_four_lifted_prefix (w : ℕ) :
    orbit (16*(32*w+18)+1) 8 = 162*w+92 ∧ odds (16*(32*w+18)+1) 8 = 4 ∧
    orbit (32*(32*w+18)+1) 9 = 162*w+92 ∧ odds (32*(32*w+18)+1) 9 = 4 := by
  have a := high_bit 289 8 (2*w)
  have b := high_bit 577 9 (2*w)
  have c := odds_high_bit 289 8 (2*w)
  have d := odds_high_bit 577 9 (2*w)
  rw [show orbit 289 8 = 92 by decide, show odds 289 8 = 4 by decide] at a
  rw [show orbit 577 9 = 92 by decide, show odds 577 9 = 4 by decide] at b
  rw [show odds 289 8 = 4 by decide] at c
  rw [show odds 577 9 = 4 by decide] at d
  rw [show 16*(32*w+18)+1=289+2^8*(2*w) by ring,
      show 32*(32*w+18)+1=577+2^9*(2*w) by ring]
  exact ⟨a.trans (by ring),c,b.trans (by ring),d⟩

/-- An infinite family of actual four-odd-step witnesses for which the
companion is also certified with four odd inputs and one extra clock. -/
theorem rank_four_shared_power_witness (j : ℕ) : ∃ k : ℕ,
    orbit (16*k+1) 8 = 2^(13+54*j) ∧ orbit (32*k+1) 9 = 2^(13+54*j) ∧
    orbit (16*k+1) (8+(13+54*j)) = 1 ∧ odds (16*k+1) (8+(13+54*j)) = 4 ∧
    orbit (32*k+1) (9+(13+54*j)) = 1 ∧ odds (32*k+1) (9+(13+54*j)) = 4 := by
  have powers (n : ℕ) : ∃ w : ℕ, 162*w+92 = 2^(13+54*n) := by
    induction n with
    | zero => exact ⟨50,by decide⟩
    | succ n ih =>
      obtain ⟨w,hw⟩ := ih
      refine ⟨2^54*w+10230399153532978,?_⟩
      rw [show 13+54*(n+1) = (13+54*n)+54 by ring,pow_add,← hw]; ring
  obtain ⟨w,hw⟩ := powers j
  obtain ⟨a,ac,b,bc⟩ := rank_four_lifted_prefix w
  rw [hw] at a b
  have land : orbit (2^(13+54*j)) (13+54*j) = 1 := by simpa using strip_twos 1 (13+54*j)
  have count : odds (2^(13+54*j)) (13+54*j) = 0 := by
    simpa using (odds_high_bit 0 (13+54*j) 1).trans (zero_prefix (13+54*j)).2
  refine ⟨32*w+18,a,b,?_,?_,?_,?_⟩
  · rw [orbit_add,a,land]
  · rw [odds_add,a,ac,count]
  · rw [orbit_add,b,land]
  · rw [odds_add,b,bc,count]


/-- Every point in this entire binary class follows the specified odd run. -/
theorem odd_run_with_core (h w : ℕ) (hw : 0 < w) :
    orbit (2^h*w-1) h = 3^h*w-1 ∧ odds (2^h*w-1) h = h := by
  have cycle (i : ℕ) : mirrorOrbit 1 i = 1 ∧ mirrorOdds 1 i = i := by
    induction i with
    | zero => simp [mirrorOrbit, mirrorOdds]
    | succ i ih => simp [mirrorOrbit, mirrorOdds, ih.1, ih.2, mirrorStep]
  have hpos : 0 < 2^h*w := by positivity
  obtain ⟨he,ho⟩ := mirror_lift (2^h*w-1) 1 h w (by decide) (by omega)
  rw [(cycle h).1,(cycle h).2] at he
  exact ⟨by omega, ho.trans (cycle h).2⟩

private theorem exact_odd_block_count {x e y : ℕ} (he : 3*x+1=2^(e+1)*y) :
    odds x (e+1) = 1 := by
  have total : 3*x+1=2*(2^e*y) := he.trans (by ring)
  have hx : x%2≠0 := by omega
  have hx1 : odds x 1 = 1 := by simp [odds,orbit,hx]
  have hs : orbit x 1 = 2^e*y := by simp [orbit,step,hx,total]
  have zeros : odds (2^e*y) e = 0 := by
    simpa using (odds_high_bit 0 e y).trans (zero_prefix e).2
  rw [Nat.add_comm e 1, odds_add, hx1, hs, zeros]

/-- A rank-three inverse certificate and a signed word sending -(3^d+1)
to -1 give actual positive paths for both arms with explicit clock counts. -/
theorem rank_three_signed_transport (k u v t d a H b L : ℕ)
    (hvpos : 0 < v) (htpos : 0 < t)
    (hx : 3*(16*k+1)+1=4*u) (hu : 3*u+1=2^(d+2)*v)
    (hv : 3*v+1=2^(a+1)*t) (hlen : a+1=H+L)
    (hmir : mirrorOrbit (3^d+1) H = 1) (hodd : mirrorOdds (3^d+1) H = b) :
    orbit (16*k+1) (2+(d+2)+(a+1)) = t ∧
    odds (16*k+1) (2+(d+2)+(a+1)) = 3 ∧
    orbit (32*k+1) (4+(d+1)+H+L) = 3^(d+b+L)*t-1 ∧
    Meets (32*k+1) (2^(d+b+L)*t-1) := by
  have hxa : 3*(16*k+1)+1=2^(1+1)*u := hx
  have hxb := exact_odd_block hxa
  have hub := exact_odd_block (e:=d+1) hu
  have hvb := exact_odd_block hv
  have hpre : orbit (32*k+1) 4 = 2^(d+1)*v-1 := by
    have h := (rank_two_four (2*k)).1
    rw [show 16*(2*k)=32*k by ring] at h
    rw [show 2^(d+2)*v=2*(2^(d+1)*v) by ring] at hu
    omega
  have hmid := (odd_run_with_core (d+1) v hvpos).1
  have hp : 0<3^(d+1)*v := by positivity
  have sep : (3^(d+1)*v-1)+(3^d+1) = 2^H*(2^L*(3^d*t)) := by
    calc
      _ = 3^(d+1)*v+3^d := by omega
      _ = 3^d*(3*v+1) := by ring
      _ = _ := by rw [hv,hlen,pow_add]; ring
  have lift := (mirror_lift _ _ _ _ (by positivity) sep).1
  rw [hmir,hodd,show 3^b*(2^L*(3^d*t)) = 2^L*(3^(d+b)*t) by ring] at lift
  have next : orbit (3^(d+1)*v-1) H = 2^L*(3^(d+b)*t)-1 := by omega
  have finish := (odd_run_with_core L (3^(d+b)*t) (by positivity)).1
  have partner : orbit (32*k+1) (4+(d+1)+H+L) = 3^(d+b+L)*t-1 := by
    rw [orbit_add,orbit_add (32*k+1) _ H,orbit_add (32*k+1) 4 (d+1), hpre,hmid,next,finish]
    rw [show 3^L*(3^(d+b)*t)=3^(d+b+L)*t by ring]
  refine ⟨?_,?_,partner,?_⟩
  · rw [orbit_add,orbit_add (16*k+1) 2 (d+2),hxb,hub,hvb]
  · rw [odds_add,odds_add (16*k+1) 2 (d+2),orbit_add (16*k+1) 2 (d+2),hxb,hub,
        exact_odd_block_count hxa,exact_odd_block_count (e:=d+1) hu,exact_odd_block_count hv]
  · exact ⟨4+(d+1)+H+L,d+b+L,partner.trans ((odd_run_with_core (d+b+L) t htpos).1.symm)⟩

private def signedTrack (x b : ℕ) : ℕ → ℕ × ℕ
  | 0 => (x,b)
  | h+1 => signedTrack (mirrorStep x) (if x%2=0 then b else b+1) h

private theorem signedTrack_eq (x j h : ℕ) :
    signedTrack (mirrorOrbit x j) (mirrorOdds x j) h =
      (mirrorOrbit x (j+h), mirrorOdds x (j+h)) := by
  induction h generalizing j with
  | zero => rfl
  | succ h ih =>
    rw [show j+(h+1)=(j+1)+h by omega]
    exact ih (j+1)

private structure ThreeRow where
  d : ℕ
  H : ℕ
  b : ℕ
  deriving DecidableEq

private def threeRow : ℕ → ThreeRow
  | 0 => ⟨39,271,132⟩ | 1 => ⟨0,1,0⟩ | 2 => ⟨63,412,197⟩
  | 3 => ⟨1,2,0⟩ | 4 => ⟨38,271,133⟩ | 5 => ⟨57,355,167⟩
  | 6 => ⟨62,412,198⟩ | 7 => ⟨124,1027,524⟩ | 8 => ⟨78,569,281⟩
  | 9 => ⟨56,355,168⟩ | 10 => ⟨79,569,280⟩ | 11 => ⟨169,1298,650⟩
  | 12 => ⟨60,412,200⟩ | 13 => ⟨6,19,6⟩ | 14 => ⟨61,412,199⟩
  | 15 => ⟨7,19,5⟩ | 16 => ⟨81,569,278⟩ | _ => ⟨183,1298,636⟩

private def baseRowData (q : ℕ) : ℕ × ℕ × ℕ × ℕ × ℕ :=
  let row := threeRow (q%18)
  let L := q-row.d-row.b
  let a := row.H+L-1
  let v := (2^(a+1)-1)/3
  let u := (2^(row.d+2)*v-1)/3
  let k := ((4*u-1)/3-1)/16
  (L,a,v,u,k)

private def rowConditions (q : ℕ) : Prop :=
  let row := threeRow (q%18)
  let (L,a,v,u,k) := baseRowData q
  1 < v ∧ v%2=1 ∧ q=row.d+row.b+L ∧ a+1=row.H+L ∧
    3*(16*k+1)+1=4*u ∧ 3*u+1=2^(row.d+2)*v ∧ 3*v+1=2^(a+1) ∧
    signedTrack (3^row.d+1) 0 row.H=(1,row.b)

private instance (q : ℕ) : Decidable (rowConditions q) := by
  unfold rowConditions
  infer_instance

set_option exponentiation.threshold 10000 in
set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
private theorem checked_rank_three_rows : ∀ i : Fin 18, rowConditions (819+i.val) := by decide

private theorem exponent_eighteen_scale (j : ℕ) : ∃ w : ℕ, 2^(18*j)=27*w+1 := by
  induction j with
  | zero => exact ⟨0,rfl⟩
  | succ j ih =>
    obtain ⟨w,hw⟩ := ih
    exact ⟨262144*w+9709, by rw [show 18*(j+1)=18*j+18 by ring,pow_add,hw]; ring⟩

private theorem odd_factor_two_power {v d e : ℕ} (hv : v%2=1) (he : v*d=2^e) : v=1 := by
  induction e generalizing d with
  | zero => exact Nat.eq_one_of_mul_eq_one_right he
  | succ e ih =>
    have md : (v*d)%2=0 := by rw [he,pow_succ]; omega
    rw [Nat.mul_mod,hv,Nat.one_mul] at md
    have de : d=2*(d/2) := by omega
    have eq : 2*(v*(d/2))=2*2^e := by
      calc
        _ = v*(2*(d/2)) := by ring
        _ = v*d := by rw [←de]
        _ = _ := by rw [he,pow_succ]; ring
    exact ih (by omega : v*(d/2)=2^e)

set_option maxRecDepth 8000 in
set_option maxHeartbeats 1500000 in
/-- For every sufficiently large q, an actual input in the rank-three layer
has a partner merging with the Mersenne start at exponent q. -/
theorem rank_three_all_large_mersenne (q : ℕ) (hq : 819≤q) :
    ∃ k h : ℕ, orbit (16*k+1) h=1 ∧ odds (16*k+1) h=3 ∧
      (¬ ∃ s, orbit (16*k+1) s=1 ∧ odds (16*k+1) s=2) ∧
      Meets (32*k+1) (2^q-1) := by
  let i : Fin 18 := ⟨(q-819)%18,Nat.mod_lt _ (by decide)⟩
  let j := (q-819)/18
  let n := 819+i.val
  have qsplit : q=n+18*j := by dsimp [n,i,j]; omega
  let row := threeRow (n%18)
  obtain ⟨L,a,v,u,k,eqdata⟩ : ∃ L a v u k : ℕ, baseRowData n=(L,a,v,u,k) := by
    obtain ⟨L,a,v,u,k⟩ := baseRowData n
    exact ⟨L,a,v,u,k,rfl⟩
  have dat : rowConditions n := checked_rank_three_rows i
  unfold rowConditions at dat
  rw [eqdata] at dat
  obtain ⟨vgt,vodd,qbase,alen,hx,hu,hv,hs⟩ := dat
  change n=row.d+row.b+L at qbase
  change a+1=row.H+L at alen
  change 3*u+1=2^(row.d+2)*v at hu
  change signedTrack (3^row.d+1) 0 row.H=(1,row.b) at hs
  have tr := signedTrack_eq (3^row.d+1) 0 row.H
  change signedTrack (3^row.d+1) 0 row.H = _ at tr
  simp only [Nat.zero_add] at tr
  rw [hs] at tr
  have hmir := (congrArg Prod.fst tr).symm
  have hodd := (congrArg Prod.snd tr).symm
  obtain ⟨w,hw⟩ := exponent_eighteen_scale j
  let z := w*2^(a+1)
  let k' := k+2^row.d*z
  let u' := u+3*2^(row.d+2)*z
  let v' := v+9*z
  have hv' : 3*v'+1 = 2^(a+18*j+1)*1 := by
    rw [show a+18*j+1=(a+1)+(18*j) by omega,pow_add,hw]
    dsimp [v',z]
    nlinarith only [hv]
  have hu' : 3*u'+1=2^(row.d+2)*v' := by dsimp [u',v']; nlinarith only [hu]
  have hx' : 3*(16*k'+1)+1=4*u' := by dsimp [k',u']; rw [pow_add]; norm_num; nlinarith only [hx]
  have newLen : a+18*j+1=row.H+(L+18*j) := by omega
  have idx : row.d+row.b+(L+18*j)=q := by omega
  have good := rank_three_signed_transport k' u' v' 1 row.d (a+18*j) row.H row.b
    (L+18*j) (by dsimp [v']; omega) (by decide) hx' hu' hv' newLen hmir hodd
  rw [idx] at good
  simp only [Nat.mul_one] at good
  refine ⟨k',_,good.1,good.2.1,?_,good.2.2.2⟩
  intro ranktwo
  obtain ⟨m,hm⟩ := (rank_two_antecedent_iff k').mp ranktwo
  have powerForm : 9*k'+1 = 2^row.d*v' := by
    rw [show 2^(row.d+2)*v'=4*(2^row.d*v') by ring] at hu'
    omega
  have gt : 1 < v' := by dsimp [v']; omega
  have odd : v'%2=1 := by
    have even : 2^(a+18*j+1)*1=2*(2^(a+18*j)) := by ring
    rw [even] at hv'; omega
  have divPow : v' ∣ 2^(6*m) := ⟨2^row.d,by rw [←hm,powerForm]; ring⟩
  obtain ⟨c,hc⟩ := divPow
  have single : v'=1 := odd_factor_two_power odd hc.symm
  omega

end CollatzUpperBit
