module

public import StrictCarry

public section

namespace Collatz.StrictCarry
set_option autoImplicit false

private theorem square_growth (d t : ℕ) (hd : 1 ≤ d) :
    (d+t+1)^2 ≤ 3^t*(d+1)^2 := by
  induction t with
  | zero => simp
  | succ t ih =>
    have hs : (d+(t+1)+1)^2 ≤ 3*(d+t+1)^2 := by
      have hp : 1 ≤ d+t := by omega
      nlinarith only [hp, Nat.zero_le ((d+t)^2)]
    rw [pow_succ]
    calc
      _ ≤ 3*(d+t+1)^2 := hs
      _ ≤ 3*(3^t*(d+1)^2) := Nat.mul_le_mul_left _ ih
      _ = _ := by ring

/-- When the actual gap exceeds the canonical gap, the optimal uniform loss is 27/4. -/
theorem debit_slack (c d : ℕ) (hd : d < 3*c) :
    27*(3^d*(c+1)^2) ≤ 4*(3^(3*c)*(d+1)^2) := by
  have hc : 1 ≤ c := by omega
  cases d with
  | zero =>
    cases c with
    | zero => omega
    | succ c =>
      have h := square_growth 1 c (by decide)
      have hx : (c+1+1)^2 ≤ 3^c*4 := by simpa [Nat.add_comm 1 c] using h
      have ht : 3^c ≤ 3^(3*c) := Nat.pow_le_pow_right (by decide) (by omega)
      have hm : (c+1+1)^2 ≤ 3^(3*c)*4 := hx.trans (Nat.mul_le_mul_right 4 ht)
      have he : 3*(c+1) = 3*c+3 := by omega
      simp only [pow_zero, one_mul, zero_add, one_pow, mul_one, he, pow_add]
      nlinarith only [hm]
  | succ d =>
    let t := 3*c - (d+2)
    have ht : (d+1)+t+1=3*c := by dsimp [t]; omega
    have hsq := square_growth (d+1) t (by omega)
    rw [ht] at hsq
    have hrat : 27*(c+1)^2 ≤ 12*(3*c)^2 := by
      have h := Nat.pow_le_pow_left (by omega : c+1 ≤ 2*c) 2
      nlinarith only [h]
    have hpow : 3*c = (d+1)+t+1 := ht.symm
    simp only [hpow, pow_add, pow_one]
    have hm := Nat.mul_le_mul_left (3^(d+1)) (hrat.trans (Nat.mul_le_mul_left 12 hsq))
    simp only [pow_add, pow_one] at hm
    nlinarith only [hm]

#print axioms debit_slack
end Collatz.StrictCarry
