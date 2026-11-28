import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! A physical closed odd trace with a rational clock margin has an explicit floor cap. -/

namespace Collatz.InfiniteDescent.ClockFloor

inductive Trace (m : ℕ) : ℕ → List ℕ → ℕ → Prop where
  | nil (x : ℕ) : Trace m x [] x
  | step {x y z e : ℕ} {es : List ℕ} (floor : m ≤ x)
      (physical : 2^e*y = 3*x+1) (rest : Trace m y es z) :
      Trace m x (e::es) z

theorem trace_floor {m x z : ℕ} {es : List ℕ} (tr : Trace m x es z) :
    2^es.sum * m^es.length * z ≤ (3*m+1)^es.length*x := by
  induction tr with
  | nil => simp
  | @step x y z e es floor physical rest ih =>
    simp only [List.sum_cons, List.length_cons, pow_add, pow_succ]
    calc
      _ = (2^e*m)*(2^es.sum*m^es.length*z) := by ring
      _ ≤ (2^e*m)*((3*m+1)^es.length*y) := Nat.mul_le_mul_left _ ih
      _ = (3*m+1)^es.length * (m*(2^e*y)) := by ring
      _ ≤ (3*m+1)^es.length * ((3*m+1)*x) := by
        rw [physical]
        exact Nat.mul_le_mul_left _ (by nlinarith)
      _ = _ := by ring

theorem slope_floor {m h p A B : ℕ} (hp : p ≠ 0)
    (cycle : 2^h*m^p ≤ (3*m+1)^p) (slope : A*p ≤ h*B) :
    2^A*m^B ≤ (3*m+1)^B := by
  apply (Nat.pow_le_pow_iff_left hp).mp
  have hgrade : (2^A)^p ≤ (2^h)^B := by
    simp only [← pow_mul]
    exact Nat.pow_le_pow_right (by decide) slope
  calc
    (2^A*m^B)^p = (2^A)^p * (m^p)^B := by simp only [mul_pow, ← pow_mul, Nat.mul_comm B p]
    _ ≤ (2^h)^B * (m^p)^B := Nat.mul_le_mul_right _ hgrade
    _ = (2^h*m^p)^B := (mul_pow ..).symm
    _ ≤ ((3*m+1)^p)^B := Nat.pow_le_pow_left cycle B
    _ = ((3*m+1)^B)^p := by simp only [← pow_mul, Nat.mul_comm B p]

theorem enlarged_power (m n : ℕ) (hm : 0 < m) :
    (3*m+1)^(n+1) + 3^(n+1)*m^n ≤
      3^(n+1)*m^(n+1) + 4^(n+1)*m^n := by
  induction n with
  | zero => simp
  | succ n ih =>
    have aux : (3*m+1)^(n+1) ≤ 4^(n+1)*m^(n+1) := by
      rw [← mul_pow]
      exact Nat.pow_le_pow_left (by omega) _
    have mult := Nat.mul_le_mul_left (3*m) ih
    simp only [pow_succ] at aux mult ⊢
    nlinarith only [aux, mult]

/-- Uses B=n+1 to keep the positive denominator explicit. -/
theorem actual_minimum_cutoff {m x A n : ℕ} {es : List ℕ}
    (tr : Trace m x es x) (hx : 0 < x) (hm : 0 < m) (hp : es.length ≠ 0)
    (slope : A*es.length ≤ es.sum*(n+1)) (sep : 3^(n+1) < 2^A) :
    m ≤ (4^(n+1)-3^(n+1)) / (2^A-3^(n+1)) := by
  have prod := Nat.le_of_mul_le_mul_right (trace_floor tr) hx
  have cur := slope_floor hp prod slope
  have cap := enlarged_power m n hm
  have h4 : 3^(n+1) ≤ (4:ℕ)^(n+1) := Nat.pow_le_pow_left (by decide) _
  have hd := Nat.sub_add_cancel (Nat.le_of_lt sep)
  have he := Nat.sub_add_cancel h4
  apply (Nat.le_div_iff_mul_le (Nat.sub_pos_of_lt sep)).mpr
  apply Nat.le_of_mul_le_mul_right (c := m^n) _ (by positivity)
  rw [pow_succ m n] at cur cap
  have aux := Nat.mul_le_mul_right (m*m^n) (le_of_eq hd)
  have aux2 := congrArg (fun q : ℕ => q * m^n) he
  nlinarith only [cur,cap,aux,aux2]

#print axioms trace_floor
#print axioms slope_floor
#print axioms enlarged_power
#print axioms actual_minimum_cutoff

end Collatz.InfiniteDescent.ClockFloor
