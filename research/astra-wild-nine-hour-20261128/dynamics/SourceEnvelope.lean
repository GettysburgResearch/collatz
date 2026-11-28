import OrdinaryPhaseBound

/-! A source-size bound independent of every terminal height and every future mark. -/
namespace Collatz.OrdinaryPhase

theorem stepNumerator (n : Nat) :
    2 * step n = 3^mark n * n + mark n := by
  by_cases he : n % 2 = 0
  · simp only [step, mark, ite_eq_left he, Nat.pow_zero, Nat.one_mul, Nat.add_zero]
    omega
  · simp only [step, mark, ite_eq_right he, Nat.pow_one]
    omega

theorem sourceEnvelope (n t : Nat) :
    ∃ d : Nat, 2^t * orbit t n = 3^count t n * n + d ∧
      3*d + 3^count t n ≤ 3^count t n * 2^t := by
  induction t generalizing n with
  | zero => exact ⟨0, by simp [orbit, count], by simp [count]⟩
  | succ t ih =>
    obtain ⟨d, hd, hb⟩ := ih (step n)
    refine ⟨3^count t (step n) * mark n + 2*d, ?_, ?_⟩
    · change 2^(t+1) * orbit t (step n) = _
      calc
        _ = 2 * (2^t * orbit t (step n)) := by ring
        _ = 2 * (3^count t (step n) * step n + d) := by rw [hd]
        _ = 3^count t (step n) * (2*step n) + 2*d := by ring
        _ = _ := by rw [stepNumerator, count, pow_add]; ring
    · rw [count, pow_add, pow_succ (2:Nat)]
      by_cases he : n % 2 = 0
      · simp only [mark, ite_eq_left he, Nat.pow_zero, Nat.one_mul, Nat.mul_zero,
          Nat.zero_add]
        calc
          _ ≤ 3 * (2 * d) + (3 ^ count t (step n) + 3 ^ count t (step n)) :=
            Nat.add_le_add_left (Nat.le_add_right _ _) _
          _ = 2 * (3 * d + 3 ^ count t (step n)) := by ring
          _ ≤ 2 * (3 ^ count t (step n) * 2 ^ t) := Nat.mul_le_mul_left 2 hb
          _ = _ := by ring
      · simp only [mark, ite_eq_right he, Nat.pow_one, Nat.mul_one]
        calc
          _ ≤ 6 * (3 * d + 3 ^ count t (step n)) := by omega
          _ ≤ 6 * (3 ^ count t (step n) * 2 ^ t) := Nat.mul_le_mul_left 6 hb
          _ = _ := by ring

#print axioms sourceEnvelope
end Collatz.OrdinaryPhase
