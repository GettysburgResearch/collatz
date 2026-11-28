import AffineOrbit
import Mathlib.Data.Nat.Prime.Basic

/-! Finite identities for semiprime first passage, with the original integer
shortcut map from the pinned PR 214 source. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.SemiprimeFactorClock
open Collatz.PoweredAffine

def oddCount (n : ℕ) : ℕ → ℕ
  | 0 => 0
  | t + 1 =>
    if n % 2 = 0 then oddCount (step n) t else oddCount (step n) t + 1

/-- Bounds the affine correction until and including the first crossing
below q. The floor hypothesis applies only to inputs before the terminal date. -/
theorem floor_product (n q t : ℕ) (floor : ∀ j < t, q ≤ orbit n j) :
    3^(oddCount n t)*n ≤ 2^t*orbit n t ∧
    q^(oddCount n t)*(2^t*orbit n t) ≤ (3*q+1)^(oddCount n t)*n := by
  induction t generalizing n with
  | zero => simp [oddCount, orbit]
  | succ t ih =>
    have hentry : q ≤ n := floor 0 (Nat.zero_lt_succ t)
    have htail : ∀ j < t, q ≤ orbit (step n) j := by
      intro j hj
      exact floor (j+1) (Nat.succ_lt_succ hj)
    obtain ⟨hl, hu⟩ := ih (step n) htail
    by_cases he : n % 2 = 0
    · have hs := even_step he
      simp only [oddCount, he, ite_true, orbit]
      constructor
      · calc
          _ = 2 * (3^(oddCount (step n) t)*step n) := by
            rw [show 2*(3^(oddCount (step n) t)*step n) = 3^(oddCount (step n) t)*(2*step n) by ring, hs]
          _ ≤ 2 * (2^t * orbit (step n) t) := Nat.mul_le_mul_left _ hl
          _ = _ := by rw [pow_succ]; ring
      · calc
          _ = 2 * (q^(oddCount (step n) t)*(2^t*orbit (step n) t)) := by rw [pow_succ]; ring
          _ ≤ 2 * ((3*q+1)^(oddCount (step n) t)*step n) := Nat.mul_le_mul_left _ hu
          _ = _ := by
              rw [show 2*((3*q+1)^(oddCount (step n) t)*step n) = (3*q+1)^(oddCount (step n) t)*(2*step n) by ring, hs]
    · have hs := odd_step (show n % 2 = 1 by omega)
      have hratio : q*(2*step n) ≤ (3*q+1)*n := by rw [hs]; nlinarith
      simp only [oddCount, he, ite_false, orbit]
      constructor
      · calc
          _ = 3^(oddCount (step n) t)*(3*n) := by rw [pow_succ]; ring
          _ ≤ 3^(oddCount (step n) t)*(2*step n) := Nat.mul_le_mul_left _ (by omega)
          _ = 2*(3^(oddCount (step n) t)*step n) := by ring
          _ ≤ 2*(2^t*orbit (step n) t) := Nat.mul_le_mul_left _ hl
          _ = _ := by rw [pow_succ]; ring
      · calc
          _ = (2*q)*(q^(oddCount (step n) t)*(2^t*orbit (step n) t)) := by
              rw [pow_succ, pow_succ]; ring
          _ ≤ (2*q)*((3*q+1)^(oddCount (step n) t)*step n) := Nat.mul_le_mul_left _ hu
          _ = (3*q+1)^(oddCount (step n) t)*(q*(2*step n)) := by ring
          _ ≤ (3*q+1)^(oddCount (step n) t)*((3*q+1)*n) := Nat.mul_le_mul_left _ hratio
          _ = _ := by rw [pow_succ]; ring

private theorem all_odd_endpoint (m k : ℕ) (hm : 0 < m) :
    orbit (2^k*m-1) k + 1 = 3^k*m := by
  induction k generalizing m with
  | zero => simp [orbit]; omega
  | succ k ih =>
    have hx : 0 < 2^k*m := by positivity
    have hstep : step (2^(k+1)*m-1) = 2^k*(3*m)-1 := by
      rw [pow_succ]
      have heq : 2^k * 2 * m = 2*(2^k*m) := by ring
      have hmul : 2^k*(3*m) = 3*(2^k*m) := by ring
      rw [heq, hmul]
      unfold step
      split_ifs <;> omega
    rw [orbit, hstep, ih (3*m) (by omega), pow_succ]
    ring

/-- A unit one below a multiple of 2^k has the prescribed growing
ordinary trajectory through every one of its first k shortcut dates. -/
theorem all_odd_prefix (m k j : ℕ) (hm : 0 < m) (hj : j ≤ k) :
    orbit (2^k*m-1) j + 1 = 2^(k-j)*3^j*m := by
  have hsize : 2^k * m = 2^j*(2^(k-j)*m) := by
    rw [← Nat.mul_assoc, ← pow_add, Nat.add_sub_of_le hj]
  rw [hsize, all_odd_endpoint (2^(k-j)*m) j (by positivity)]
  ring


private theorem odd_le_length (w : List Bool) : ones w ≤ w.length := by
  induction w with
  | nil => decide
  | cons b w ih => cases b <;> simp [ones] <;> omega

private theorem correction_bound (w : List Bool) :
    numerator w + 2^w.length ≤ 3^w.length := by
  induction w with
  | nil => decide
  | cons b w ih =>
    have hg : 3^(ones w) ≤ 3^w.length :=
      Nat.pow_le_pow_right (by decide) (odd_le_length w)
    cases b <;> simp only [numerator, Bool.false_eq_true, ↓reduceIte, mul_zero, zero_add,
      mul_one, List.length_cons, pow_succ] <;> omega

private theorem padded_correction (w : List Bool) (h : ℕ) (hw : w.length ≤ h) :
    2^(h-w.length)*numerator w + 2^h ≤ 3^h := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hw
  simp only [Nat.add_sub_cancel_left]
  calc
    _ = 2^k*(numerator w + 2^w.length) := by rw [pow_add]; ring
    _ ≤ 2^k*3^w.length := Nat.mul_le_mul_left _ (correction_bound w)
    _ ≤ 3^k*3^w.length := Nat.mul_le_mul_right _ (Nat.pow_le_pow_left (by decide) k)
    _ = _ := by rw [pow_add]; ring

private theorem coeff_size (k l q a b : ℕ) (hne : k ≠ l)
    (h : k*q+a=l*q+b) : q ≤ max a b := by
  rcases lt_or_gt_of_ne hne with hi | hi
  · have hm := Nat.mul_le_mul_right q (show k+1 ≤ l by omega)
    nlinarith only [h, hm, Nat.le_max_left a b, Nat.zero_le b]
  · have hm := Nat.mul_le_mul_right q (show l+1 ≤ k by omega)
    nlinarith only [h, hm, Nat.le_max_right a b, Nat.zero_le a]

/-- Any common vertex at possibly different clocks for pq and q with
prime p>3 requires q at most 3^h-2^h, where h bounds both clocks. -/
theorem factor_merger_height {p q h : ℕ} {w v : List Bool}
    (hp : p.Prime) (hp3 : 3 < p) (hw : Realizes (p*q) w) (hv : Realizes q v)
    (hi : w.length ≤ h) (hj : v.length ≤ h)
    (meet : orbit (p*q) w.length = orbit q v.length) : q + 2^h ≤ 3^h := by
  have A := actual_word_affine hw
  have B := actual_word_affine hv
  have ai : 2^(h-w.length) * 2^w.length = 2^h := by
    rw [← pow_add, Nat.sub_add_cancel hi]
  have aj : 2^(h-v.length) * 2^v.length = 2^h := by
    rw [← pow_add, Nat.sub_add_cancel hj]
  have prod :
      (2^(h-w.length)*3^(ones w)*p)*q + 2^(h-w.length)*numerator w =
      (2^(h-v.length)*3^(ones v))*q + 2^(h-v.length)*numerator v := by
    calc
      _ = 2^(h-w.length)*(3^(ones w)*(p*q)+numerator w) := by ring
      _ = 2^h*orbit (p*q) w.length := by rw [← A, ← Nat.mul_assoc, ai]
      _ = 2^h*orbit q v.length := by rw [meet]
      _ = 2^(h-v.length)*(3^(ones v)*q+numerator v) := by rw [← B, ← Nat.mul_assoc, aj]
      _ = _ := by ring
  have ne : 2^(h-w.length)*3^(ones w)*p ≠ 2^(h-v.length)*3^(ones v) := by
    intro eq
    have div : p ∣ 2^(h-v.length)*3^(ones v) := by
      rw [← eq]; exact dvd_mul_left _ _
    rcases hp.dvd_mul.mp div with hd | hd
    · have hz := Nat.le_of_dvd (by decide : 0 < 2) (hp.dvd_of_dvd_pow hd)
      omega
    · have hz := Nat.le_of_dvd (by decide : 0 < 3) (hp.dvd_of_dvd_pow hd)
      omega
  have hn := coeff_size _ _ q _ _ ne prod
  have hu := padded_correction w h hi
  have hv' := padded_correction v h hj
  omega

end Collatz.SemiprimeFactorClock
