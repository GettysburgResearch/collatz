import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.Floor.Ring
import Mathlib.Tactic

/-!
The deterministic finite geometry in ENTROPY_ARITHMETIC.md. The source
boundary dimension, Borel--Cantelli step and solenoid topology remain written
mathematics; none of them is postulated as a Lean axiom here.
-/

namespace CollatzProfound.ScaleAvoidance

/-- First crossing of any threshold overshoots by at most one allowed upward
factor. Downward jumps and arbitrary waiting times are permitted. -/
theorem bounded_upward_first_crossing
    (scale : ℕ → ℝ) (N : ℕ) (L T : ℝ) (hL : 0 < L)
    (hstep : ∀ j, scale (j + 1) ≤ L * scale j)
    (hstart : scale N < T)
    (hattain : ∃ k : ℕ, T ≤ scale (N + k)) :
    ∃ j : ℕ, N < j ∧ T ≤ scale j ∧ scale j < L * T := by
  classical
  let k := Nat.find hattain
  have hk : T ≤ scale (N + k) := Nat.find_spec hattain
  have hk0 : k ≠ 0 := by
    intro hz
    simp only [hz, Nat.add_zero] at hk
    exact (not_le_of_gt hstart) hk
  have hkpos : 0 < k := Nat.pos_of_ne_zero hk0
  have hprev : scale (N + (k - 1)) < T := by
    have hlt : k - 1 < k := by omega
    exact lt_of_not_ge (Nat.find_min hattain hlt)
  have hind : N + (k - 1) + 1 = N + k := by omega
  refine ⟨N + k, by omega, hk, ?_⟩
  calc
    scale (N + k) = scale (N + (k - 1) + 1) := by rw [hind]
    _ ≤ L * scale (N + (k - 1)) := hstep _
    _ < L * T := mul_lt_mul_of_pos_left hprev hL

/-- An explicit integer translate of a prescribed unit-periodic open interval
fits inside every interval whose scaled width is at least four. -/
theorem periodic_interval_hole
    (u v scale c eta : ℝ) (hscale : 0 < scale)
    (heta : 0 < eta) (heta1 : eta < 1)
    (hwidth : 4 ≤ scale * (v - u)) :
    ∃ k : ℤ,
      u < ((k : ℝ) + c) / scale ∧
      ((k : ℝ) + c + eta) / scale < v ∧
      ((k : ℝ) + c) / scale < ((k : ℝ) + c + eta) / scale ∧
      ((k : ℝ) + c + eta) / scale - ((k : ℝ) + c) / scale = eta / scale := by
  let k : ℤ := ⌊scale * u - c⌋ + 2
  have hlo := Int.floor_le (scale * u - c)
  have hhi := Int.lt_floor_add_one (scale * u - c)
  have hk : (k : ℝ) = (⌊scale * u - c⌋ : ℝ) + 2 := by
    simp [k]
  refine ⟨k, ?_, ?_, ?_, ?_⟩
  · apply (lt_div_iff₀ hscale).2
    rw [hk]
    nlinarith
  · apply (div_lt_iff₀ hscale).2
    rw [hk]
    nlinarith
  · exact div_lt_div_of_pos_right (by linarith) hscale
  · ring

/-- The first-crossing scale bound gives a hole of fixed relative size. -/
theorem relative_hole_width
    (w scale L eta : ℝ) (hw : 0 < w) (hscale : 0 < scale)
    (hL : 0 < L) (heta : 0 ≤ eta)
    (hupper : scale ≤ 4 * L / w) :
    eta * w / (4 * L) ≤ eta / scale := by
  have hmul : scale * w ≤ 4 * L := (le_div_iff₀ hw).1 hupper
  apply (div_le_div_iff₀ (by positivity : 0 < 4 * L) hscale).2
  nlinarith

/-- Missing one child at every fixed-depth refinement gives an all-depth
covering-count bound. This is the finite induction used for upper box
dimension strictly below one. -/
theorem covering_count_iterate
    (count : ℕ → ℕ) (m h B : ℕ)
    (hstep : ∀ n, m ≤ n → count (n + h) ≤ (B - 1) * count n) :
    ∀ t : ℕ, count (m + t * h) ≤ (B - 1) ^ t * count m := by
  intro t
  induction t with
  | zero => simp
  | succ t ih =>
      have hm : m ≤ m + t * h := Nat.le_add_right _ _
      calc
        count (m + (t + 1) * h) = count (m + t * h + h) := by congr 1; ring
        _ ≤ (B - 1) * count (m + t * h) := hstep _ hm
        _ ≤ (B - 1) * ((B - 1) ^ t * count m) := Nat.mul_le_mul_left _ ih
        _ = (B - 1) ^ (t + 1) * count m := by rw [pow_succ]; ring

end CollatzProfound.ScaleAvoidance
