import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Data.Int.Basic
import Mathlib.Tactic

/-!
Finite cores for the actual-law pressure/collision attempt. No infinite
harmonic flow, pressure measure or collision upper bound is assumed as an
axiom. The repeated affine word hypothesis is supplied explicitly.
-/

open scoped BigOperators

namespace CollatzPressureCollision

/-- The pointwise comparison actually used to transfer a pair sum. -/
theorem bounded_density_pair {z₁ z₂ u₁ u₂ D : ℝ}
    (_hz₁ : 0 ≤ z₁) (hz₂ : 0 ≤ z₂)
    (hu₁ : 0 ≤ u₁) (hD : 0 ≤ D)
    (h₁ : z₁ ≤ D * u₁) (h₂ : z₂ ≤ D * u₂) :
    z₁ * z₂ ≤ D ^ 2 * (u₁ * u₂) := by
  calc
    z₁ * z₂ ≤ (D * u₁) * (D * u₂) :=
      mul_le_mul h₁ h₂ hz₂ (mul_nonneg hD hu₁)
    _ = D ^ 2 * (u₁ * u₂) := by ring

/-- No modular or diagonal conditions are discarded: the caller supplies
the literal finite pair set. -/
theorem bounded_density_pair_sum {α : Type*} (pairs : Finset (α × α))
    (z u : α → ℝ) (D : ℝ) (hD : 0 ≤ D)
    (hz : ∀ a, 0 ≤ z a) (hu : ∀ a, 0 ≤ u a)
    (hzu : ∀ a, z a ≤ D * u a) :
    (∑ ab ∈ pairs, z ab.1 * z ab.2) ≤
      D ^ 2 * ∑ ab ∈ pairs, u ab.1 * u ab.2 := by
  calc
    (∑ ab ∈ pairs, z ab.1 * z ab.2) ≤
        ∑ ab ∈ pairs, D ^ 2 * (u ab.1 * u ab.2) := by
      apply Finset.sum_le_sum
      intro ab hab
      exact bounded_density_pair (hz ab.1) (hz ab.2)
        (hu ab.1) hD (hzu ab.1) (hzu ab.2)
    _ = D ^ 2 * ∑ ab ∈ pairs, u ab.1 * u ab.2 := by
      rw [Finset.mul_sum]

/-- A retained atom and the ordinary pressure weight force the stated
density cost. Here h is the positive height weight q^s. -/
theorem retained_density_cost {z u D c S h N : ℝ}
    (hS : 0 < S) (hh : 0 < h) (hD : 0 ≤ D)
    (hretained : c / N ≤ z) (hweight : u ≤ 1 / (S * h))
    (hcompare : z ≤ D * u) :
    c * S * h / N ≤ D := by
  have hbetween : c / N ≤ D / (S * h) := by
    calc
      c / N ≤ z := hretained
      _ ≤ D * u := hcompare
      _ ≤ D * (1 / (S * h)) := mul_le_mul_of_nonneg_left hweight hD
      _ = D / (S * h) := by ring
  have hmul := (le_div_iff₀ (mul_pos hS hh)).mp hbetween
  calc
    c * S * h / N = (c / N) * (S * h) := by ring
    _ ≤ D := hmul

/-- Exact telescope for a repeated affine word, with all integer replay
states and the finite repetition horizon retained. -/
theorem affine_repeat_telescope (a b B : ℤ) (x : ℕ → ℤ) (k : ℕ)
    (hedge : ∀ i < k, b * x (i + 1) = a * x i + B) :
    b ^ k * ((b - a) * x k - B) =
      a ^ k * ((b - a) * x 0 - B) := by
  induction k with
  | zero => simp
  | succ k ih =>
      have hprefix : ∀ i < k, b * x (i + 1) = a * x i + B := by
        intro i hi
        exact hedge i (Nat.lt_trans hi (Nat.lt_succ_self k))
      have hstep : b * ((b - a) * x (k + 1) - B) =
          a * ((b - a) * x k - B) := by
        have he := hedge k (Nat.lt_succ_self k)
        calc
          b * ((b - a) * x (k + 1) - B) =
              (b - a) * (b * x (k + 1)) - b * B := by ring
          _ = (b - a) * (a * x k + B) - b * B := by rw [he]
          _ = a * ((b - a) * x k - B) := by ring
      calc
        b ^ (k + 1) * ((b - a) * x (k + 1) - B) =
            b ^ k * (b * ((b - a) * x (k + 1) - B)) := by
          rw [pow_succ]
          ring
        _ = b ^ k * (a * ((b - a) * x k - B)) := by rw [hstep]
        _ = a * (b ^ k * ((b - a) * x k - B)) := by ring
        _ = a * (a ^ k * ((b - a) * x 0 - B)) := by rw [ih hprefix]
        _ = a ^ (k + 1) * ((b - a) * x 0 - B) := by
          rw [pow_succ]
          ring

/-- Coprimality converts literal finite replay into a divisibility
condition on the original source, not on a replacement endpoint. -/
theorem affine_repeat_divisibility (a b B : ℤ) (x : ℕ → ℤ) (k : ℕ)
    (hcoprime : IsCoprime b a)
    (hedge : ∀ i < k, b * x (i + 1) = a * x i + B) :
    b ^ k ∣ (b - a) * x 0 - B := by
  have hpow : IsCoprime (b ^ k) (a ^ k) := hcoprime.pow
  apply hpow.dvd_of_dvd_mul_left
  rw [← affine_repeat_telescope a b B x k hedge]
  exact dvd_mul_right _ _

/-- The actual Collatz powers in the repeated-word condition. -/
theorem collatz_repeat_divisibility (A m k : ℕ) (B : ℤ) (x : ℕ → ℤ)
    (hedge : ∀ i < k, (2 : ℤ) ^ A * x (i + 1) =
      3 ^ m * x i + B) :
    (2 : ℤ) ^ (A * k) ∣ (2 ^ A - 3 ^ m) * x 0 - B := by
  have h23 : IsCoprime (2 : ℤ) 3 := ⟨-1, 1, by norm_num⟩
  have hpow : IsCoprime ((2 : ℤ) ^ A) (3 ^ m) := h23.pow
  simpa only [← pow_mul] using
    affine_repeat_divisibility (3 ^ m) (2 ^ A) B x k hpow hedge

/-- A nonzero original displacement must be at least the full repeated
two-adic modulus. -/
theorem collatz_repeat_displacement_bound (A m k : ℕ) (B : ℤ) (x : ℕ → ℤ)
    (hedge : ∀ i < k, (2 : ℤ) ^ A * x (i + 1) =
      3 ^ m * x i + B)
    (hne : (2 ^ A - 3 ^ m) * x 0 - B ≠ 0) :
    2 ^ (A * k) ≤ Int.natAbs ((2 ^ A - 3 ^ m) * x 0 - B) := by
  have hdiv := collatz_repeat_divisibility A m k B x hedge
  simpa using Int.natAbs_le_of_dvd_ne_zero hdiv hne

/-- A literal odd accelerated edge. Oddness of the endpoint ensures that
the displayed exponent is the exact division exponent. -/
def exactEdge (n e q : ℕ) : Prop :=
  0 < n ∧ 0 < e ∧ 0 < q ∧ n % 2 = 1 ∧ q % 2 = 1 ∧
    3 * n + 1 = 2 ^ e * q

def replay : List ℕ → List ℕ → Prop
  | [_], [] => True
  | n :: q :: ns, e :: es => exactEdge n e q ∧ replay (q :: ns) es
  | _, _ => False

instance replayDecidable (ns es : List ℕ) : Decidable (replay ns es) := by
  induction ns generalizing es with
  | nil => simp only [replay]; infer_instance
  | cons n ns ih =>
      cases ns with
      | nil => cases es <;> simp only [replay] <;> infer_instance
      | cons q qs =>
          cases es with
          | nil => simp only [replay]; infer_instance
          | cons e es =>
              simp only [replay]
              have : Decidable (replay (q :: qs) es) := ih es
              unfold exactEdge
              infer_instance

def orbit41 : List ℕ :=
  [41, 31, 47, 71, 107, 161, 121, 91, 137, 103, 155, 233, 175,
   263, 395, 593, 445, 167, 251, 377, 283, 425, 319, 479, 719,
   1079, 1619, 2429, 911]

def gaps41 : List ℕ :=
  [2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 3,
   1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 3]

theorem common_source_replay : replay orbit41 gaps41 := by decide

theorem common_source_distinct_units : orbit41.Nodup ∧
    ∀ n ∈ orbit41, 0 < n ∧ n % 2 = 1 ∧ n % 3 ≠ 0 := by decide

/-- Both different words occur in this same certified source prefix. -/
theorem critical_word_collision :
    orbit41[21]? = some 425 ∧ orbit41[28]? = some 911 ∧
    (gaps41.drop 17).take 4 = [1, 1, 2, 1] ∧
    (gaps41.drop 24).take 4 = [1, 1, 1, 3] ∧
    (425 : ℕ) % 3 ^ 4 = 911 % 3 ^ 4 ∧
    ([1, 1, 2, 1] : List ℕ) ≠ [1, 1, 1, 3] ∧
    (2 : ℕ) ^ 5 < 3 ^ 4 ∧ 2 ^ 6 < 3 ^ 4 := by decide

end CollatzPressureCollision
