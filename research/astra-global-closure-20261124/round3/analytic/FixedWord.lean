import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic

/-! Finite arithmetic behind the covered-position divisor count. All clocks
are read from one actual trajectory segment, and no uniform clock cap is assumed. -/
set_option autoImplicit false
namespace Collatz.FixedWord

def scale (g : ℕ → ℕ) : ℕ → ℕ
  | 0 => 1
  | n+1 => scale g n * 2 ^ g n

def carry (g : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | n+1 => 3 * carry g n + scale g n

theorem physical_affine (q g : ℕ → ℕ)
    (step : ∀ i, 2^g i * q (i+1) = 3*q i+1) (n : ℕ) :
    scale g n * q n = 3^n * q 0 + carry g n := by
  induction n with
  | zero => simp [scale, carry]
  | succ n ih =>
    rw [scale, Nat.mul_assoc, step, Nat.mul_add, Nat.mul_one,
      show scale g n * (3 * q n) = 3 * (scale g n * q n) by ring, ih, carry, pow_succ]
    ring

theorem physical_gcd (q g : ℕ → ℕ)
    (step : ∀ i, 2^g i * q (i+1) = 3*q i+1) (n : ℕ) :
    Nat.gcd (q 0) (q n) ∣ carry g n := by
  have h := Nat.dvd_mul_left_of_dvd (Nat.gcd_dvd_right (q 0) (q n)) (scale g n)
  rw [physical_affine q g step n] at h
  exact (Nat.dvd_add_iff_right
    (Nat.dvd_mul_left_of_dvd (Nat.gcd_dvd_left (q 0) (q n)) (3^n))).mpr h

theorem adjacent_carry (g : ℕ → ℕ) : carry g 1 = 1 := by simp [carry, scale]

theorem physical_size (q g : ℕ → ℕ) (hq : ∀ i, 0 < q i)
    (step : ∀ i, 2^g i * q (i+1) = 3*q i+1) (n : ℕ) :
    scale g n * q n ≤ 4^n * q 0 := by
  induction n with
  | zero => simp [scale]
  | succ n ih =>
    rw [scale, Nat.mul_assoc, step, pow_succ]
    calc
      scale g n * (3*q n+1) ≤ scale g n * (4*q n) := by
        exact Nat.mul_le_mul_left _ (by have := hq n; omega)
      _ = 4*(scale g n*q n) := by ring
      _ ≤ 4*(4^n*q 0) := Nat.mul_le_mul_left _ ih
      _ = _ := by ring

theorem floor_carry (q g : ℕ → ℕ) (hq : ∀ i, 0 < q i)
    (step : ∀ i, 2^g i * q (i+1) = 3*q i+1) (m n : ℕ)
    (floor : ∀ i < n, m ≤ q i) :
    m * carry g n + 3^n * q 0 ≤ 4^n * q 0 := by
  induction n with
  | zero => simp [carry]
  | succ n ih =>
    have prev := ih (fun i hi => floor i (by omega))
    have budget := (Nat.mul_le_mul_left (scale g n) (floor n (by omega))).trans
      (physical_size q g hq step n)
    rw [carry, pow_succ, pow_succ]
    calc
      m*(3*carry g n+scale g n) + 3^n*3*q 0 =
          3*(m*carry g n+3^n*q 0) + scale g n*m := by ring
      _ ≤ 3*(4^n*q 0) + 4^n*q 0 := Nat.add_le_add (Nat.mul_le_mul_left _ prev) budget
      _ = _ := by ring

private theorem cap_cover {ι : Type*} (s : Finset ι) (v : ι → ℕ) (w : ℕ)
    (h : w ≤ ∑ i ∈ s, v i) : w ≤ ∑ i ∈ s, min w (v i) := by
  by_cases hit : ∃ i ∈ s, w ≤ v i
  · obtain ⟨i, hi, hwi⟩ := hit
    calc
      w = min w (v i) := (min_eq_left hwi).symm
      _ ≤ _ := Finset.single_le_sum (fun k _ => Nat.zero_le (min w (v k))) hi
  · apply h.trans
    apply Finset.sum_le_sum
    intro i hi
    exact le_min (le_of_not_ge (fun hwi => hit ⟨i, hi, hwi⟩)) le_rfl

/-- The valuation-cover assumption is only required for primes. The conclusion
is divisibility by the actual product, prior to any bound on that product. -/
theorem covered_divisor {ι : Type*} (s : Finset ι) (a : ℕ) (q c : ι → ℕ)
    (ha : a ≠ 0) (hq : ∀ i ∈ s, q i ≠ 0)
    (cover : ∀ p, Nat.Prime p → a.factorization p ≤ ∑ i ∈ s, (q i).factorization p)
    (pair : ∀ i ∈ s, Nat.gcd a (q i) ∣ c i) :
    a ∣ ∏ i ∈ s, c i := by
  have hg : ∀ i ∈ s, Nat.gcd a (q i) ≠ 0 := fun _ _ => Nat.gcd_ne_zero_left ha
  apply dvd_trans _ (Finset.prod_dvd_prod_of_dvd (fun i => Nat.gcd a (q i)) c pair)
  apply (Nat.factorization_le_iff_dvd ha (Finset.prod_ne_zero_iff.mpr hg)).mp
  intro p
  rw [Nat.factorization_prod_apply hg]
  by_cases prime : Nat.Prime p
  · have cap := cap_cover s (fun i => (q i).factorization p) (a.factorization p) (cover p prime)
    apply cap.trans
    apply Finset.sum_le_sum
    intro i hi
    rw [Nat.factorization_gcd ha (hq i hi), Finsupp.inf_apply]
  · simp [Nat.factorization_eq_zero_of_not_prime a prime]

/-- Multiply the floor estimates after omitting an adjacent carry equal to one. -/
theorem floor_product {ι : Type*} (s : Finset ι) (c : ι → ℕ) (m a B : ℕ)
    (hc : ∀ i ∈ s, 0 < c i) (ma : m ≤ a) (divisor : a ∣ ∏ i ∈ s, c i)
    (est : ∀ i ∈ s, m*c i ≤ B) : m^(s.card+1) ≤ B^s.card := by
  have hsize := ma.trans (Nat.le_of_dvd (Finset.prod_pos hc) divisor)
  calc
    m^(s.card+1) ≤ m^s.card * ∏ i ∈ s, c i := by
      rw [pow_succ]
      exact Nat.mul_le_mul_left _ hsize
    _ = ∏ i ∈ s, (m*c i) := by simp [Finset.prod_mul_distrib]
    _ ≤ ∏ _i ∈ s, B := Finset.prod_le_prod est
    _ = _ := by simp

#print axioms physical_affine
#print axioms physical_gcd
#print axioms adjacent_carry
#print axioms physical_size
#print axioms floor_carry
#print axioms covered_divisor
#print axioms floor_product

end Collatz.FixedWord
