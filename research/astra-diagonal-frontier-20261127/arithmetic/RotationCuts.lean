import Mathlib.Tactic
import Mathlib.Order.Monotone.Defs

namespace Collatz.RotationCuts

/-- No strict inversion of the positive raw images in a factor-eight ordinary band. -/
theorem noInversion {n m k : ℕ} (_hn : 0 < n) (hm : m ≤ 8*n)
    (hk : 2^k * n < m) : 2^k * (3*n+1) ≤ 3*m+1 := by
  by_cases h : k ≤ 2
  · interval_cases k <;> norm_num at * <;> omega
  · have hk3 : 3 ≤ k := by omega
    have hp : 2^3 ≤ (2:ℕ)^k := Nat.pow_le_pow_right (by decide) hk3
    have hmn := Nat.mul_le_mul_right n hp
    norm_num at hmn
    omega

/-- A lift commuting with one period commutes with all nonnegative translates. -/
theorem multiTranslate (f : ℤ → ℤ) (N : ℤ) (h : ∀ x, f (x+N)=f x+N)
    (k : ℕ) (x : ℤ) : f (x+(k:ℤ)*N)=f x+k*N := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Nat.cast_succ, add_mul, one_mul, ← add_assoc, h, ih]
    ring

theorem iterateTranslate (f : ℤ → ℤ) (N : ℤ) (h : ∀ x, f (x+N)=f x+N)
    (n : ℕ) (x : ℤ) : f^[n] (x+N) = f^[n] x+N := by
  induction n generalizing x with
  | zero => rfl
  | succ n ih =>
    rw [Function.iterate_succ_apply', Function.iterate_succ_apply', ih, h]

/-- Repeating a real orbit period gives the exact multiple returned clock. -/
theorem repeatClock (f : ℤ → ℤ) (N : ℤ) (h : ∀ x, f (x+N)=f x+N)
    (p A t : ℕ) (x : ℤ) (hx : f^[p] x=x+A*N) :
    f^[p*t] x = x+(t:ℤ)*(A*N) := by
  induction t with
  | zero => simp
  | succ t ih =>
    rw [Nat.mul_succ, Nat.add_comm, Function.iterate_add_apply, ih]
    rw [← mul_assoc, ← Nat.cast_mul, multiTranslate (f^[p]) N (iterateTranslate f N h p), hx]
    push_cast
    ring

/-- Two distinct phases of a common monotone lift have the same reduced clock.
The phases are positioned in a common fundamental interval. -/
theorem commonClock (f : ℤ → ℤ) (N : ℤ) (hN : 0 < N) (hm : Monotone f)
    (h : ∀ x, f (x+N)=f x+N) (p q A B : ℕ) (x y : ℤ)
    (hxy : x ≤ y) (hyx : y ≤ x+N)
    (hx : f^[p] x=x+A*N) (hy : f^[q] y=y+B*N) : q*A=p*B := by
  have ex : f^[p*(2*q)] x = x+2*((q*A:ℕ):ℤ)*N := by
    rw [repeatClock f N h p A (2*q) x hx]
    push_cast
    ring
  have ey : f^[p*(2*q)] y = y+2*((p*B:ℕ):ℤ)*N := by
    rw [show p*(2*q)=q*(2*p) by ring, repeatClock f N h q B (2*p) y hy]
    push_cast
    ring
  have lb := (hm.iterate (p*(2*q))) hxy
  have ub := (hm.iterate (p*(2*q))) hyx
  rw [ex, ey] at lb
  rw [ey, iterateTranslate f N h, ex] at ub
  have e : (q*A:ℕ)=(p*B:ℕ) := by
    by_contra hn
    rcases lt_or_gt_of_ne hn with hl | hg
    · have hd : ((q*A:ℕ):ℤ)+1 ≤ ((p*B:ℕ):ℤ) := by exact_mod_cast hl
      nlinarith [mul_le_mul_of_nonneg_right hd hN.le]
    · have hd : ((p*B:ℕ):ℤ)+1 ≤ ((q*A:ℕ):ℤ) := by exact_mod_cast hg
      nlinarith [mul_le_mul_of_nonneg_right hd hN.le]
  exact e

#print axioms noInversion
#print axioms multiTranslate
#print axioms iterateTranslate
#print axioms repeatClock
#print axioms commonClock

end Collatz.RotationCuts
