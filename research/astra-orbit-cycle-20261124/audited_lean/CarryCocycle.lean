import Mathlib.Tactic.GCongr
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Candidate formalization of the finite carry amortization kernel.
Compilation and axiom audit are pending; no universal phase bound is assumed. -/
namespace Collatz.ScalarCarryCocycle

set_option autoImplicit false

private theorem succ_le_two_pow (n : ℕ) : n + 1 ≤ 2 ^ n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ]
    omega

private theorem fourth_bound (n : ℕ) : (n + 1)^4 ≤ 8^(2*n) := by
  have h := succ_le_two_pow n
  calc
    (n + 1)^4 ≤ (2^n)^4 := by gcongr
    _ = 16^n := by
      rw [← pow_mul, Nat.mul_comm n 4, pow_mul]
      norm_num
    _ ≤ 64^n := by gcongr; norm_num
    _ = 8^(2*n) := by rw [pow_mul]; norm_num

/-- All possible carry changes, including arbitrarily large carries.
    The fourth-power potential pays for the cubed clock multiplier. -/
theorem carry_power (c d : ℕ) (hd : d ≤ 3*c+2) :
    8^d * (c+1)^4 ≤ 8^(3*c) * (d+1)^4 := by
  by_cases hdc : d ≤ c
  · have hc := fourth_bound c
    have hp : (1 : ℕ) ≤ (d+1)^4 := by
      have : 0 < (d+1)^4 := by positivity
      omega
    calc
      8^d * (c+1)^4 ≤ 8^c * 8^(2*c) := by gcongr
      _ = 8^(3*c) := by rw [← pow_add]; congr 1; omega
      _ ≤ 8^(3*c) * (d+1)^4 := by
        simpa using Nat.mul_le_mul_left (8^(3*c)) hp
  · by_cases h3 : d ≤ 3*c
    · have hcd : c+1 ≤ d+1 := by omega
      gcongr
    · have hs : d = 3*c+1 ∨ d = 3*c+2 := by omega
      rcases hs with hs | hs
      · rw [hs]
        have hsmall : 2*(c+1) ≤ 3*c+1+1 := by omega
        have hfour : 8*(c+1)^4 ≤ (3*c+1+1)^4 := by
          calc
            8*(c+1)^4 ≤ 16*(c+1)^4 :=
              Nat.mul_le_mul_right _ (by norm_num)
            _ = (2*(c+1))^4 := by ring
            _ ≤ (3*c+1+1)^4 := by gcongr
        calc
          8^(3*c+1)*(c+1)^4 = 8^(3*c)*(8*(c+1)^4) := by
            rw [pow_succ]; ring
          _ ≤ 8^(3*c)*(3*c+1+1)^4 := Nat.mul_le_mul_left _ hfour
      · rw [hs]
        have hfour : 64*(c+1)^4 ≤ (3*c+2+1)^4 := by
          calc
            64*(c+1)^4 ≤ 81*(c+1)^4 :=
              Nat.mul_le_mul_right _ (by norm_num)
            _ = (3*c+2+1)^4 := by ring
        calc
          8^(3*c+2)*(c+1)^4 = 8^(3*c)*(64*(c+1)^4) := by
            rw [pow_add]; norm_num; ring
          _ ≤ 8^(3*c)*(3*c+2+1)^4 := Nat.mul_le_mul_left _ hfour

/-- a = actual gap, b = canonical centered ternary gap, c,d = carries. -/
theorem clock_step (a b c d : ℕ) (ha : 1 ≤ a) (hb : b ≤ 3)
    (he : a+d = b+3*c) :
    8^b * (c+1)^4 ≤ 8^a * (d+1)^4 := by
  have hd : d ≤ 3*c+2 := by omega
  have h := Nat.mul_le_mul_left (8^b) (carry_power c d hd)
  have hl : 8^b*(8^d*(c+1)^4) = 8^d*(8^b*(c+1)^4) := by ring
  have hr : 8^b*(8^(3*c)*(d+1)^4) = 8^d*(8^a*(d+1)^4) := by
    calc
      _ = 8^(b+3*c)*(d+1)^4 := by rw [pow_add]; ring
      _ = 8^(d+a)*(d+1)^4 := by rw [show b+3*c = d+a by omega]
      _ = _ := by rw [pow_add]; ring
  rw [hl, hr] at h
  by_contra hn
  have ht : 8^a*(d+1)^4 < 8^b*(c+1)^4 := lt_of_not_ge hn
  have hm := Nat.mul_lt_mul_of_pos_left ht (show 0 < 8^d by positivity)
  exact (not_lt_of_ge h) hm

def clock (f : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | n+1 => clock f n + f n

/-- No bound on the carries, horizon, or number of resets. -/
theorem clock_amortized (a b c : ℕ → ℕ)
    (ha : ∀ i, 1 ≤ a i) (hb : ∀ i, b i ≤ 3)
    (he : ∀ i, a i+c (i+1) = b i+3*c i) (n : ℕ) :
    8^(clock b n)*(c 0+1)^4 ≤ 8^(clock a n)*(c n+1)^4 := by
  induction n with
  | zero => simp [clock]
  | succ n ih =>
    have hs := clock_step (a n) (b n) (c n) (c (n+1))
      (ha n) (hb n) (he n)
    calc
      8^(clock b (n+1))*(c 0+1)^4 =
          8^(b n)*(8^(clock b n)*(c 0+1)^4) := by
            simp only [clock, pow_add]; ring
      _ ≤ 8^(b n)*(8^(clock a n)*(c n+1)^4) :=
          Nat.mul_le_mul_left _ ih
      _ = 8^(clock a n)*(8^(b n)*(c n+1)^4) := by ring
      _ ≤ 8^(clock a n)*(8^(a n)*(c (n+1)+1)^4) :=
          Nat.mul_le_mul_left _ hs
      _ = 8^(clock a (n+1))*(c (n+1)+1)^4 := by
            simp only [clock, pow_add]; ring

/-- The same theorem with any prescribed starting clock. -/
theorem clock_amortized_shift (a b c : ℕ → ℕ)
    (ha : ∀ i, 1 ≤ a i) (hb : ∀ i, b i ≤ 3)
    (he : ∀ i, a i+c (i+1) = b i+3*c i) (j n : ℕ) :
    8^(clock (fun i => b (j+i)) n)*(c j+1)^4 ≤
      8^(clock (fun i => a (j+i)) n)*(c (j+n)+1)^4 := by
  have h := clock_amortized (fun i => a (j+i)) (fun i => b (j+i))
    (fun i => c (j+i)) (fun i => ha (j+i)) (fun i => hb (j+i))
    (fun i => by simpa only [Nat.add_assoc] using he (j+i)) n
  simpa using h

#print axioms clock_amortized_shift
end Collatz.ScalarCarryCocycle

#print axioms Collatz.ScalarCarryCocycle.succ_le_two_pow
#print axioms Collatz.ScalarCarryCocycle.fourth_bound
#print axioms Collatz.ScalarCarryCocycle.carry_power
#print axioms Collatz.ScalarCarryCocycle.clock_step
#print axioms Collatz.ScalarCarryCocycle.clock_amortized
