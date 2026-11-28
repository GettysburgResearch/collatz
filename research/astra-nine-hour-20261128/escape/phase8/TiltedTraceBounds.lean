import Init.Omega

/-! Integer product bounds for the positive trace and its genuine negative control.
A supplied certified gap gives the displayed exact signed Collatz step. -/

namespace Collatz.TiltedTraceBounds

def gapTotal (gap : Nat → Nat) : Nat → Nat
  | 0 => 0
  | j+1 => gapTotal gap j + gap j

theorem scaledProduct (m : Nat) (state gap : Nat → Nat)
    (step : ∀ i, m * state i ≤ 2^(gap i) * state (i+1)) (j : Nat) :
    m^j * state 0 ≤ 2^(gapTotal gap j) * state j := by
  induction j with
  | zero => simp [gapTotal]
  | succ j ih =>
    calc
      m^(j+1) * state 0 = m * (m^j * state 0) := by rw [Nat.pow_succ]; ac_rfl
      _ ≤ m * (2^(gapTotal gap j) * state j) := Nat.mul_le_mul_left _ ih
      _ = 2^(gapTotal gap j) * (m * state j) := by ac_rfl
      _ ≤ 2^(gapTotal gap j) * (2^(gap j) * state (j+1)) :=
        Nat.mul_le_mul_left _ (step j)
      _ = 2^(gapTotal gap (j+1)) * state (j+1) := by
        rw [gapTotal, Nat.pow_add]; ac_rfl

theorem positiveCorrection (state gap : Nat → Nat)
    (step : ∀ i, 2^(gap i) * state (i+1) = 3 * state i + 1) (j : Nat) :
    3^j * state 0 ≤ 2^(gapTotal gap j) * state j := by
  apply scaledProduct
  intro i
  rw [step i]
  omega

theorem negativeNormalizedCorrection (state gap : Nat → Nat)
    (pos : ∀ i, 0 < state i)
    (step : ∀ i, 2^(gap i) * state (i+1) + 1 = 3 * state i) (j : Nat) :
    2^j * state 0 ≤ 2^(gapTotal gap j) * state j := by
  apply scaledProduct
  intro i
  have h := step i
  have p := pos i
  omega

theorem negativeStrictGap {x y d : Nat} (large : 3 ≤ x)
    (step : 2^d * y + 1 = 3*x) :
    8*x ≤ 3*(2^d*y) := by omega

theorem growth (state gap : Nat → Nat) (cost : ∀ i, 1 ≤ gap i)
    (step : ∀ i, 2^(gap i) * state (i+1) ≤ 3 * state i + 1) (j : Nat) :
    2^j * (state j + 1) ≤ 3^j * (state 0 + 1) := by
  induction j with
  | zero => simp
  | succ j ih =>
    have factor : 2 ≤ 2^(gap j) := by
      have h := Nat.pow_le_pow_right (by decide : 0 < 2) (cost j)
      simpa using h
    have bound := Nat.le_trans (Nat.mul_le_mul_right (state (j+1)) factor) (step j)
    have tick : 2*(state (j+1)+1) ≤ 3*(state j+1) := by omega
    calc
      2^(j+1) * (state (j+1)+1) = 2^j*(2*(state (j+1)+1)) := by
        rw [Nat.pow_succ]; ac_rfl
      _ ≤ 2^j*(3*(state j+1)) := Nat.mul_le_mul_left _ tick
      _ = 3*(2^j*(state j+1)) := by ac_rfl
      _ ≤ 3*(3^j*(state 0+1)) := Nat.mul_le_mul_left _ ih
      _ = 3^(j+1)*(state 0+1) := by rw [Nat.pow_succ]; ac_rfl

#print axioms positiveCorrection
#print axioms negativeNormalizedCorrection
#print axioms growth

end Collatz.TiltedTraceBounds
