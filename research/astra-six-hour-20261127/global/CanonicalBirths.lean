import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-! Exact signed shortcut translation, same-threshold comparison,
and the dyadic representative window for canonical births. -/
namespace CanonicalBirths

def bit (x : ℤ) : ℕ := if x % 2 = 0 then 0 else 1

def step (x : ℤ) : ℤ := if x % 2 = 0 then x / 2 else (3*x+1) / 2

def endpoint : ℕ → ℤ → ℤ
  | 0, x => x
  | h+1, x => endpoint h (step x)

def oddCount : ℕ → ℤ → ℕ
  | 0, _ => 0
  | h+1, x => oddCount h (step x) + bit x

theorem bit_shift (x z : ℤ) : bit (x+2*z) = bit x := by
  unfold bit
  have h : (x+2*z)%2 = x%2 := by omega
  rw [h]

theorem step_shift (x z : ℤ) :
    step (x+2*z) = step x + (3:ℤ)^(bit x) * z := by
  unfold step bit
  by_cases he : x%2=0
  · have ht : (x+2*z)%2=0 := by omega
    simp [he, ht]
    omega
  · simp [he]
    omega

theorem translate (h : ℕ) (x z : ℤ) :
    oddCount h (x+(2:ℤ)^h*z) = oddCount h x ∧
    endpoint h (x+(2:ℤ)^h*z) = endpoint h x + (3:ℤ)^(oddCount h x)*z := by
  induction h generalizing x z with
  | zero => simp [oddCount, endpoint]
  | succ h ih =>
    have hi := ih (step x) ((3:ℤ)^(bit x)*z)
    have ht : x+(2:ℤ)^(h+1)*z = x+2*((2:ℤ)^h*z) := by rw [pow_succ]; ring
    have hu : step (x+(2:ℤ)^(h+1)*z) =
        step x+(2:ℤ)^h*((3:ℤ)^(bit x)*z) := by
      rw [ht, step_shift]
      ring
    constructor
    · change oddCount h (step (x+2^(h+1)*z)) + bit (x+2^(h+1)*z) = _
      rw [hu, hi.1, ht, bit_shift]
      rfl
    · change endpoint h (step (x+2^(h+1)*z)) = endpoint h (step x) + 3^(oddCount h (step x)+bit x)*z
      rw [hu, hi.2, pow_add]
      ring

theorem step_sign (x : ℤ) : 0 ≤ step x ↔ 0 ≤ x := by
  unfold step
  split <;> omega

theorem endpoint_sign (h : ℕ) (x : ℤ) : 0 ≤ endpoint h x ↔ 0 ≤ x := by
  induction h generalizing x with
  | zero => rfl
  | succ h ih => exact (ih (step x)).trans (step_sign x)

theorem same_threshold (h : ℕ) (x z : ℤ) :
    (3:ℤ)^(oddCount h x)*z ≤ endpoint h x ↔ (2:ℤ)^h*z ≤ x := by
  have ht := (translate h x (-z)).2
  have hs := endpoint_sign h (x+(2:ℤ)^h*(-z))
  rw [ht] at hs
  simp only [mul_neg] at hs
  omega

theorem same_strict_threshold (h : ℕ) (x z : ℤ) :
    endpoint h x < (3:ℤ)^(oddCount h x)*z ↔ x < (2:ℤ)^h*z := by
  exact lt_iff_lt_of_le_iff_le (same_threshold h x z)

theorem same_quotient (h : ℕ) (x Q : ℤ) (hQ : 0<Q) :
    endpoint h x / ((3:ℤ)^(oddCount h x)*Q) = x / ((2:ℤ)^h*Q) := by
  have hp : 0 < (3:ℤ)^(oddCount h x)*Q := mul_pos (by positivity) hQ
  have hq : 0 < (2:ℤ)^h*Q := mul_pos (by positivity) hQ
  apply le_antisymm
  · by_contra! hz
    have hleft : (x/((2:ℤ)^h*Q)+1)*((3:ℤ)^(oddCount h x)*Q) ≤ endpoint h x :=
      (Int.le_ediv_iff_mul_le hp).mp (by omega)
    have hright : (x/((2:ℤ)^h*Q)+1)*((2:ℤ)^h*Q) ≤ x := by
      have hc := (same_threshold h x (Q*(x/((2:ℤ)^h*Q)+1))).mp (by
        convert hleft using 1; ring)
      convert hc using 1; ring
    exact (by have := (Int.le_ediv_iff_mul_le hq).mpr hright; omega)
  · by_contra! hz
    have hright : (endpoint h x/((3:ℤ)^(oddCount h x)*Q)+1)*((2:ℤ)^h*Q) ≤ x :=
      (Int.le_ediv_iff_mul_le hq).mp (by omega)
    have hleft : (endpoint h x/((3:ℤ)^(oddCount h x)*Q)+1)*((3:ℤ)^(oddCount h x)*Q) ≤ endpoint h x := by
      have hc := (same_threshold h x (Q*(endpoint h x/((3:ℤ)^(oddCount h x)*Q)+1))).mpr (by
        convert hright using 1; ring)
      convert hc using 1; ring
    exact (by have := (Int.le_ediv_iff_mul_le hp).mpr hleft; omega)

theorem row_window (h : ℕ) (a q l : ℤ) (hq : 0<q) (ha : 0≤a) (hb : a<2*q) :
    endpoint h (a+2*q*l) < 2*q*(3:ℤ)^(oddCount h (a+2*q*l)) ↔ l<(2:ℤ)^h := by
  rw [mul_comm (2*q) ((3:ℤ)^(oddCount h (a+2*q*l))), same_strict_threshold]
  constructor
  · intro hl
    by_contra! h
    have := mul_le_mul_of_nonneg_left h (show 0≤2*q by omega)
    nlinarith
  · intro hl
    have h := mul_le_mul_of_nonneg_left (show l+1≤(2:ℤ)^h by omega)
      (show 0≤2*q by omega)
    nlinarith

end CanonicalBirths
