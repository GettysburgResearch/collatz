import Mathlib.Tactic

/-! Finite ordinary block equations and the effective sparse-script window.
The infinite 2-adic irrationality proof remains in ARITHMETIC_TOWER.md. -/
namespace Collatz.CarryTowerRoundTen.ArithmeticTower

set_option autoImplicit false

def BlockEdge (paid : Bool) (q r : ℕ) : Prop :=
  0 < q ∧ Odd q ∧ 0 < r ∧ Odd r ∧
    if paid then 32 * r = 9 * q + 5 else 8 * r = 9 * q + 7

theorem unpaid_replays (q r : ℕ) (h : BlockEdge false q r) :
    ∃ u : ℕ, 0 < u ∧ Odd u ∧ 4 * u = 3 * q + 1 ∧ 2 * r = 3 * u + 1 := by
  have he : 8 * r = 9 * q + 7 := h.2.2.2.2
  let u := (3 * q + 1) / 4
  have hu : 4 * u = 3 * q + 1 := by dsimp [u]; omega
  have hr : 2 * r = 3 * u + 1 := by omega
  refine ⟨u, by have hq := h.1; omega, ?_, hu, hr⟩
  exact ⟨u / 2, by omega⟩

theorem paid_replays (q r : ℕ) (h : BlockEdge true q r) :
    ∃ u : ℕ, 0 < u ∧ Odd u ∧ 2 * u = 3 * q + 1 ∧ 16 * r = 3 * u + 1 := by
  have he : 32 * r = 9 * q + 5 := h.2.2.2.2
  let u := (3 * q + 1) / 2
  have hu : 2 * u = 3 * q + 1 := by dsimp [u]; omega
  have hr : 16 * r = 3 * u + 1 := by omega
  refine ⟨u, by have hq := h.1; omega, ?_, hu, hr⟩
  exact ⟨u / 2, by omega⟩

theorem unpaid_shift (q r : ℕ) (h : BlockEdge false q r) :
    8 * (r + 7) = 9 * (q + 7) := by
  have he : 8 * r = 9 * q + 7 := h.2.2.2.2
  omega

theorem paid_shift (q r : ℕ) (h : BlockEdge true q r) :
    32 * (r + 7) = 9 * (q + 7) + 166 := by
  have he : 32 * r = 9 * q + 5 := h.2.2.2.2
  omega

theorem block_height (paid : Bool) (q r : ℕ) (h : BlockEdge paid q r) :
    8 * (r + 7) ≤ 9 * (q + 7) := by
  cases paid with
  | false => exact (unpaid_shift q r h).le
  | true => have he := paid_shift q r h; omega

theorem prefix_height (q : ℕ → ℕ) (s : ℕ → Bool) (j : ℕ)
    (h : ∀ i < j, BlockEdge (s i) (q i) (q (i + 1))) :
    8 ^ j * (q j + 7) ≤ 9 ^ j * (q 0 + 7) := by
  induction j with
  | zero => simp
  | succ j ih =>
    have hp := ih (fun i hi => h i (by omega))
    have hs := block_height (s j) (q j) (q (j + 1)) (h j (by omega))
    calc
      8 ^ (j + 1) * (q (j + 1) + 7) =
          8 ^ j * (8 * (q (j + 1) + 7)) := by ring
      _ ≤ 8 ^ j * (9 * (q j + 7)) := Nat.mul_le_mul_left _ hs
      _ = 9 * (8 ^ j * (q j + 7)) := by ring
      _ ≤ 9 * (9 ^ j * (q 0 + 7)) := Nat.mul_le_mul_left _ hp
      _ = 9 ^ (j + 1) * (q 0 + 7) := by ring

theorem unpaid_run_identity (q : ℕ → ℕ) (j m : ℕ)
    (h : ∀ i < m, BlockEdge false (q (j + i)) (q (j + (i + 1)))) :
    8 ^ m * (q (j + m) + 7) = 9 ^ m * (q j + 7) := by
  induction m with
  | zero => simp
  | succ m ih =>
    have hp := ih (fun i hi => h i (by omega))
    have hs := unpaid_shift (q (j + m)) (q (j + (m + 1))) (h m (by omega))
    calc
      8 ^ (m + 1) * (q (j + (m + 1)) + 7) =
          8 ^ m * (8 * (q (j + (m + 1)) + 7)) := by ring
      _ = 8 ^ m * (9 * (q (j + m) + 7)) := by rw [hs]
      _ = 9 * (8 ^ m * (q (j + m) + 7)) := by ring
      _ = 9 * (9 ^ m * (q j + 7)) := by rw [hp]
      _ = 9 ^ (m + 1) * (q j + 7) := by ring

theorem unpaid_binary_divisor (start endpoint m : ℕ) (heven : Even endpoint)
    (h : 8 ^ m * endpoint = 9 ^ m * start) :
    2 ^ (3 * m + 1) ∣ start := by
  have hc : Nat.Coprime (2 ^ (3 * m + 1)) (9 ^ m) :=
    ((show Nat.Coprime 2 9 by decide).pow_left _).pow_right _
  apply hc.dvd_mul_left.mp
  rcases heven with ⟨u, hu⟩
  refine ⟨u, ?_⟩
  rw [← h, hu]
  have hp : (8 : ℕ) ^ m = 2 ^ (3 * m) := by rw [pow_mul]; norm_num
  rw [hp, pow_succ]
  ring

/-- A window for one unchanged actual positive ordinary source. -/
theorem same_source_window (q : ℕ → ℕ) (s : ℕ → Bool) (j m : ℕ)
    (hpref : ∀ i < j, BlockEdge (s i) (q i) (q (i + 1)))
    (hrun : ∀ i < m, BlockEdge false (q (j + i)) (q (j + (i + 1))))
    (hend : Odd (q (j + m))) :
    2 ^ (3 * m + 1) * 8 ^ j ≤ 9 ^ j * (q 0 + 7) := by
  have heven : Even (q (j + m) + 7) := by
    rcases hend with ⟨u, hu⟩
    exact ⟨u + 4, by omega⟩
  have hd := unpaid_binary_divisor (q j + 7) (q (j + m) + 7) m heven
    (unpaid_run_identity q j m hrun)
  have hlo : 2 ^ (3 * m + 1) ≤ q j + 7 := Nat.le_of_dvd (by omega) hd
  have hg := prefix_height q s j hpref
  calc
    2 ^ (3 * m + 1) * 8 ^ j ≤ (q j + 7) * 8 ^ j :=
      Nat.mul_le_mul_right _ hlo
    _ = 8 ^ j * (q j + 7) := by ring
    _ ≤ 9 ^ j * (q 0 + 7) := hg

theorem window_exponent_bound (x j m b : ℕ) (hx : x < 2 ^ b)
    (hw : 2 ^ (3 * m + 1) * 8 ^ j ≤ 9 ^ j * x) :
    33 * m + 11 < 2 * j + 11 * b := by
  have hp := Nat.pow_le_pow_left hw 11
  have hb : x ^ 11 < (2 ^ b) ^ 11 := Nat.pow_lt_pow_left hx (by decide)
  have ha : (9 ^ j) ^ 11 ≤ (2 ^ 35) ^ j := by
    have hh := Nat.pow_le_pow_left (show (9 : ℕ) ^ 11 ≤ 2 ^ 35 by norm_num) j
    simpa only [← pow_mul, Nat.mul_comm j 11] using hh
  have hu : (9 ^ j * x) ^ 11 < (2 ^ 35) ^ j * (2 ^ b) ^ 11 := by
    rw [mul_pow]
    exact lt_of_lt_of_le
      (Nat.mul_lt_mul_of_pos_left hb (by positivity))
      (Nat.mul_le_mul_right _ ha)
  have ht := lt_of_le_of_lt hp hu
  rw [show (8 : ℕ) = 2 ^ 3 by norm_num] at ht
  simp only [← pow_mul, ← pow_add] at ht
  have he := (Nat.pow_lt_pow_iff_right (by decide : 1 < 2)).mp ht
  omega

/-- The four explicit bit-cap scripts must differ within their supplied budget.
The displayed unpaid run is attached to those scripts in the written theorem. -/
theorem four_family_budget (x h b k : ℕ) (hk1 : 1 ≤ k) (hk4 : k ≤ 4)
    (hh : 0 < h) (hx : x < 2 ^ b)
    (hbudget : 11 * b + 24 ≤ (35 - 2 ^ (k + 1)) * h)
    (hwindow : 2 ^ (3 * (h - 1) + 1) * 8 ^ ((2 ^ k - 1) * h + 1) ≤
      9 ^ ((2 ^ k - 1) * h + 1) * x) : False := by
  have he := window_exponent_bound x ((2 ^ k - 1) * h + 1) (h - 1) b hx hwindow
  interval_cases k <;> norm_num at he hbudget <;> omega

theorem exact_lacunarity_boundary :
    (9 : ℕ) ^ 11 < 2 ^ 35 ∧ 9 ^ 15 < 8 ^ 16 ∧ 8 ^ 32 < 9 ^ 31 := by
  norm_num

end Collatz.CarryTowerRoundTen.ArithmeticTower
