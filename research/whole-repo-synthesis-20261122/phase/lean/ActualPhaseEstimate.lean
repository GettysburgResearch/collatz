import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.NumberTheory.Harmonic.Bounds
import Mathlib.Data.Finset.Max
import Mathlib.Tactic

/-!
Finite ordinary logarithmic-phase estimates. No global Collatz assertion
is assumed or proved. The final estimate uses a finite list of positive
ordinary states, distinct on its first N entries, and its exact edges.
-/

open scoped BigOperators

noncomputable section

namespace CollatzActualPhase

/-- The small positive logarithmic correction in an odd Collatz edge. -/
def logError (n : ℕ) : ℝ :=
  Real.log (1 + 1 / (3 * (n : ℝ))) / Real.log 2

/-- The additive circle character, represented as a complex unit. -/
def unitPhase (t : ℝ) : ℂ := Complex.exp (Complex.I * (2 * Real.pi * t : ℝ))

/-- Distinct positive integer denominators have at most harmonic reciprocal mass. -/
theorem reciprocal_finset_le_harmonic (s : Finset ℕ)
    (hpos : ∀ n ∈ s, 0 < n) :
    ∑ n ∈ s, (1 : ℝ) / n ≤ (harmonic s.card : ℝ) := by
  induction s using Finset.induction_on_max with
  | empty => simp
  | @insert a s hmax ih =>
    have ha : 0 < a := hpos a (Finset.mem_insert_self a s)
    have hs : ∀ n ∈ s, 0 < n := fun n hn => hpos n (Finset.mem_insert_of_mem hn)
    have ha_not : a ∉ s := by
      intro ha_mem
      exact (lt_irrefl a) (hmax a ha_mem)
    have hz_not : 0 ∉ s := by
      intro hz
      exact (lt_irrefl 0) (hs 0 hz)
    have hsub : insert 0 s ⊆ Finset.range a := by
      intro n hn
      rcases Finset.mem_insert.mp hn with rfl | hn
      · exact Finset.mem_range.mpr ha
      · exact Finset.mem_range.mpr (hmax n hn)
    have hcard : s.card + 1 ≤ a := by
      have hh := Finset.card_le_card hsub
      simpa [Finset.card_insert_of_notMem hz_not] using hh
    have hrec : (1 : ℝ) / a ≤ 1 / (s.card + 1 : ℕ) := by
      apply one_div_le_one_div_of_le
      · positivity
      · exact_mod_cast hcard
    rw [Finset.sum_insert ha_not, Finset.card_insert_of_notMem ha_not]
    calc
      (1 : ℝ) / a + ∑ n ∈ s, (1 : ℝ) / n
          ≤ 1 / (s.card + 1 : ℕ) + (harmonic s.card : ℝ) :=
        add_le_add hrec (ih hs)
      _ = (harmonic (s.card + 1) : ℝ) := by
        simp [harmonic_succ, one_div, add_comm]

/-- The reciprocal estimate on an actual finite sequence, without sorting it. -/
theorem reciprocal_range_le_harmonic (q : ℕ → ℕ) (N : ℕ)
    (hpos : ∀ i < N, 0 < q i)
    (hdist : ∀ i < N, ∀ j < N, q i = q j → i = j) :
    ∑ i ∈ Finset.range N, (1 : ℝ) / q i ≤ (harmonic N : ℝ) := by
  have hinj : Set.InjOn q (↑(Finset.range N) : Set ℕ) := by
    intro i hi j hj hij
    exact hdist i (Finset.mem_range.mp hi) j (Finset.mem_range.mp hj) hij
  have hh := reciprocal_finset_le_harmonic ((Finset.range N).image q) (by
    intro n hn
    rcases Finset.mem_image.mp hn with ⟨i, hi, rfl⟩
    exact hpos i (Finset.mem_range.mp hi))
  rw [Finset.sum_image hinj, Finset.card_image_iff.mpr hinj, Finset.card_range] at hh
  exact hh

theorem logError_nonneg (n : ℕ) (hn : 0 < n) : 0 ≤ logError n := by
  apply div_nonneg
  · apply Real.log_nonneg
    have hp : 0 ≤ (1 : ℝ) / (3 * n) := by positivity
    linarith
  · exact (Real.log_pos (by norm_num : (1 : ℝ) < 2)).le

theorem logError_le_reciprocal (n : ℕ) (hn : 0 < n) :
    logError n ≤ (1 / (3 * Real.log 2)) * (1 / (n : ℝ)) := by
  have hnR : (0 : ℝ) < n := by exact_mod_cast hn
  have hL : 0 < Real.log 2 := Real.log_pos (by norm_num)
  have hlog : Real.log (1 + 1 / (3 * (n : ℝ))) ≤ 1 / (3 * (n : ℝ)) := by
    have hh := Real.log_le_sub_one_of_pos
      (by positivity : (0 : ℝ) < 1 + 1 / (3 * (n : ℝ)))
    linarith
  calc
    logError n ≤ (1 / (3 * (n : ℝ))) / Real.log 2 :=
      div_le_div_of_nonneg_right hlog hL.le
    _ = (1 / (3 * Real.log 2)) * (1 / (n : ℝ)) := by
      field_simp

/-- The complete logarithmic correction budget for a distinct ordinary segment. -/
theorem logError_sum_le_harmonic (q : ℕ → ℕ) (N : ℕ)
    (hpos : ∀ i < N, 0 < q i)
    (hdist : ∀ i < N, ∀ j < N, q i = q j → i = j) :
    ∑ i ∈ Finset.range N, logError (q i)
      ≤ (harmonic N : ℝ) / (3 * Real.log 2) := by
  have hc : 0 ≤ 1 / (3 * Real.log 2) := by
    have : 0 < Real.log 2 := Real.log_pos (by norm_num)
    positivity
  calc
    ∑ i ∈ Finset.range N, logError (q i)
        ≤ ∑ i ∈ Finset.range N, (1 / (3 * Real.log 2)) * (1 / (q i : ℝ)) := by
      apply Finset.sum_le_sum
      intro i hi
      exact logError_le_reciprocal _ (hpos i (Finset.mem_range.mp hi))
    _ = (1 / (3 * Real.log 2)) * ∑ i ∈ Finset.range N, (1 : ℝ) / q i := by
      rw [Finset.mul_sum]
    _ ≤ (1 / (3 * Real.log 2)) * (harmonic N : ℝ) :=
      mul_le_mul_of_nonneg_left (reciprocal_range_le_harmonic q N hpos hdist) hc
    _ = (harmonic N : ℝ) / (3 * Real.log 2) := by ring

/-- Exact real logarithmic identity from one literal ordinary odd edge. -/
theorem log_edge (n m g : ℕ) (hn : 0 < n) (hm : 0 < m)
    (hedge : 2 ^ g * m = 3 * n + 1) :
    Real.log (m : ℝ) / Real.log 2 =
      Real.log (n : ℝ) / Real.log 2 + Real.log 3 / Real.log 2 - g + logError n := by
  have hnR : (0 : ℝ) < n := by exact_mod_cast hn
  have hmR : (0 : ℝ) < m := by exact_mod_cast hm
  have hL : Real.log 2 ≠ 0 := ne_of_gt (Real.log_pos (by norm_num))
  have he : (2 : ℝ) ^ g * (m : ℝ) =
      (3 * (n : ℝ)) * (1 + 1 / (3 * (n : ℝ))) := by
    have he' : (2 : ℝ) ^ g * (m : ℝ) = 3 * (n : ℝ) + 1 := by exact_mod_cast hedge
    rw [he']
    field_simp
  have hlog := congrArg Real.log he
  rw [Real.log_mul (by positivity) hmR.ne', Real.log_pow,
    Real.log_mul (by positivity) (by positivity),
    Real.log_mul (by norm_num) hnR.ne'] at hlog
  unfold logError
  apply (mul_right_cancel₀ hL)
  simp only [add_mul, sub_mul, div_mul_cancel₀ _ hL]
  linarith

private theorem phase_norm (t : ℝ) : ‖unitPhase t‖ = 1 := by
  exact Complex.norm_exp_I_mul_ofReal _

private theorem phase_add (s t : ℝ) : unitPhase (s + t) = unitPhase s * unitPhase t := by
  unfold unitPhase
  rw [← Complex.exp_add]
  congr 1
  push_cast
  ring

private theorem phase_int (k : ℤ) : unitPhase k = 1 := by
  unfold unitPhase
  calc
    Complex.exp (Complex.I * (2 * Real.pi * (k : ℝ) : ℝ))
        = Complex.exp ((k : ℂ) * (2 * (Real.pi : ℂ) * Complex.I)) := by
      congr 1
      push_cast
      ring
    _ = 1 := Complex.exp_int_mul_two_pi_mul_I k

private theorem phase_error (t : ℝ) : ‖unitPhase t - 1‖ ≤ 2 * Real.pi * |t| := by
  have hh := Real.norm_exp_I_mul_ofReal_sub_one_le (x := 2 * Real.pi * t)
  simpa [unitPhase, Real.norm_eq_abs, abs_mul, abs_of_nonneg Real.pi_pos.le] using hh

/-- A finite Fourier telescope, with the supplied local errors retained explicitly. -/
theorem fourier_telescope (z : ℕ → ℂ) (a : ℂ) (b : ℕ → ℝ) (N : ℕ)
    (hunit : ∀ i, ‖z i‖ = 1)
    (herr : ∀ i < N, ‖z (i + 1) - a * z i‖ ≤ b i) :
    ‖a - 1‖ * ‖∑ i ∈ Finset.range N, z i‖ ≤
      2 + ∑ i ∈ Finset.range N, b i := by
  have hid : ∀ M : ℕ,
      (a - 1) * (∑ i ∈ Finset.range M, z i) =
        (z M - z 0) - ∑ i ∈ Finset.range M, (z (i + 1) - a * z i) := by
    intro M
    induction M with
    | zero => simp
    | succ M ih =>
      rw [Finset.sum_range_succ, Finset.sum_range_succ, mul_add, ih]
      ring
  rw [← norm_mul, hid N]
  calc
    ‖(z N - z 0) - ∑ i ∈ Finset.range N, (z (i + 1) - a * z i)‖
        ≤ ‖z N - z 0‖ + ‖∑ i ∈ Finset.range N, (z (i + 1) - a * z i)‖ :=
      norm_sub_le _ _
    _ ≤ (‖z N‖ + ‖z 0‖) + ∑ i ∈ Finset.range N, ‖z (i + 1) - a * z i‖ :=
      add_le_add (norm_sub_le _ _) (norm_sum_le _ _)
    _ ≤ 2 + ∑ i ∈ Finset.range N, b i := by
      rw [hunit N, hunit 0]
      norm_num only
      apply add_le_add le_rfl
      apply Finset.sum_le_sum
      intro i hi
      exact herr i (Finset.mem_range.mp hi)

private theorem phase_integer_error (x theta eps : ℝ) (k : ℤ) :
    unitPhase (x + theta - k + eps) =
      unitPhase theta * unitPhase x * unitPhase eps := by
  have hk : unitPhase (-(k : ℝ)) = 1 := by
    simpa only [Int.cast_neg] using phase_int (-k)
  simp only [sub_eq_add_neg, phase_add, hk, mul_one]
  ring

/-- The local complex phase error follows from the exact ordinary edge itself. -/
theorem phase_edge_error (n m g : ℕ) (h : ℤ)
    (hn : 0 < n) (hm : 0 < m) (hedge : 2 ^ g * m = 3 * n + 1) :
    ‖unitPhase ((h : ℝ) * (Real.log (m : ℝ) / Real.log 2)) -
      unitPhase ((h : ℝ) * (Real.log 3 / Real.log 2)) *
      unitPhase ((h : ℝ) * (Real.log (n : ℝ) / Real.log 2))‖
      ≤ (2 * Real.pi * |(h : ℝ)|) * logError n := by
  have hlog := log_edge n m g hn hm hedge
  have hmultip : (h : ℝ) * (Real.log (m : ℝ) / Real.log 2) =
      (h : ℝ) * (Real.log (n : ℝ) / Real.log 2) +
      (h : ℝ) * (Real.log 3 / Real.log 2) -
      ((h * (g : ℤ) : ℤ) : ℝ) + (h : ℝ) * logError n := by
    rw [hlog]
    push_cast
    ring
  rw [hmultip, phase_integer_error]
  have hid :
      unitPhase ((h : ℝ) * (Real.log 3 / Real.log 2)) *
          unitPhase ((h : ℝ) * (Real.log (n : ℝ) / Real.log 2)) *
          unitPhase ((h : ℝ) * logError n) -
        unitPhase ((h : ℝ) * (Real.log 3 / Real.log 2)) *
          unitPhase ((h : ℝ) * (Real.log (n : ℝ) / Real.log 2)) =
      (unitPhase ((h : ℝ) * (Real.log 3 / Real.log 2)) *
          unitPhase ((h : ℝ) * (Real.log (n : ℝ) / Real.log 2))) *
        (unitPhase ((h : ℝ) * logError n) - 1) := by ring
  rw [hid, norm_mul, norm_mul, phase_norm, phase_norm, one_mul, one_mul]
  calc
    ‖unitPhase ((h : ℝ) * logError n) - 1‖
        ≤ 2 * Real.pi * |(h : ℝ) * logError n| := phase_error _
    _ = (2 * Real.pi * |(h : ℝ)|) * logError n := by
      rw [abs_mul, abs_of_nonneg (logError_nonneg n hn)]
      ring

/--
Composed finite estimate for exact ordinary edges. Positivity is needed
through the terminal state; distinctness is needed only on the N sources
whose logarithmic corrections are charged. No phase recurrence is assumed.
-/
theorem actual_fourier_harmonic_bound
    (q gap : ℕ → ℕ) (N : ℕ) (h : ℤ)
    (hpos : ∀ i ≤ N, 0 < q i)
    (hdist : ∀ i < N, ∀ j < N, q i = q j → i = j)
    (hedge : ∀ i < N, 2 ^ gap i * q (i + 1) = 3 * q i + 1) :
    ‖unitPhase ((h : ℝ) * (Real.log 3 / Real.log 2)) - 1‖ *
        ‖∑ i ∈ Finset.range N,
          unitPhase ((h : ℝ) * (Real.log (q i : ℝ) / Real.log 2))‖
      ≤ 2 + ((2 * Real.pi * |(h : ℝ)|) / (3 * Real.log 2)) *
        (harmonic N : ℝ) := by
  let z : ℕ → ℂ := fun i =>
    unitPhase ((h : ℝ) * (Real.log (q i : ℝ) / Real.log 2))
  let a := unitPhase ((h : ℝ) * (Real.log 3 / Real.log 2))
  let c := 2 * Real.pi * |(h : ℝ)|
  have hc : 0 ≤ c := by dsimp [c]; positivity
  have ht := fourier_telescope z a (fun i => c * logError (q i)) N
    (fun i => phase_norm _) (by
      intro i hi
      exact phase_edge_error (q i) (q (i + 1)) (gap i) h
        (hpos i (Nat.le_of_lt hi)) (hpos (i + 1) (Nat.succ_le_of_lt hi)) (hedge i hi))
  calc
    ‖a - 1‖ * ‖∑ i ∈ Finset.range N, z i‖
        ≤ 2 + ∑ i ∈ Finset.range N, c * logError (q i) := ht
    _ = 2 + c * ∑ i ∈ Finset.range N, logError (q i) := by rw [Finset.mul_sum]
    _ ≤ 2 + c * ((harmonic N : ℝ) / (3 * Real.log 2)) := by
      apply add_le_add le_rfl
      exact mul_le_mul_of_nonneg_left
        (logError_sum_le_harmonic q N (fun i hi => hpos i (Nat.le_of_lt hi)) hdist) hc
    _ = 2 + (c / (3 * Real.log 2)) * (harmonic N : ℝ) := by ring

/-- The explicit logarithmic version of the composed finite Fourier estimate. -/
theorem actual_fourier_log_bound
    (q gap : ℕ → ℕ) (N : ℕ) (h : ℤ)
    (hpos : ∀ i ≤ N, 0 < q i)
    (hdist : ∀ i < N, ∀ j < N, q i = q j → i = j)
    (hedge : ∀ i < N, 2 ^ gap i * q (i + 1) = 3 * q i + 1) :
    ‖unitPhase ((h : ℝ) * (Real.log 3 / Real.log 2)) - 1‖ *
        ‖∑ i ∈ Finset.range N,
          unitPhase ((h : ℝ) * (Real.log (q i : ℝ) / Real.log 2))‖
      ≤ 2 + ((2 * Real.pi * |(h : ℝ)|) / (3 * Real.log 2)) *
        (1 + Real.log N) := by
  apply (actual_fourier_harmonic_bound q gap N h hpos hdist hedge).trans
  apply add_le_add le_rfl
  apply mul_le_mul_of_nonneg_left (harmonic_le_one_add_log N)
  have : 0 < Real.log 2 := Real.log_pos (by norm_num)
  positivity

end CollatzActualPhase
