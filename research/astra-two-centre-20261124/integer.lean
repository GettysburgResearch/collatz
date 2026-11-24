import Std

namespace Collatz.BinaryBoundary

/-- An odd-step history, recording the total number of divisions and odd steps.
    The odd target and the positive division count make every step exact. -/
inductive History : Nat → Nat → Nat → Nat → Prop where
  | nil (x : Nat) : History x x 0 0
  | cons {x y z a j e : Nat} (edge : 3*x+1 = 2^(e+1)*y)
      (odd : y%2 = 1) (rest : History y z a j) :
      History x z ((e+1)+a) (j+1)

/-- Exact transport of a separated high block along every legal history. -/
theorem transport {x y a j : Nat} (h : History x y a j) (u : Nat) :
    History (x + 2^a*(2*u)) (y + 3^j*(2*u)) a j := by
  induction h generalizing u with
  | nil x => simpa using History.nil (x + 2*u)
  | @cons x y z a j e edge odd rest ih =>
    have tail := ih (3*u)
    have src : 3*(x + 2^((e+1)+a)*(2*u))+1 =
        2^(e+1)*(y + 2^a*(2*(3*u))) := by
      rw [Nat.pow_add]
      grind
    have odd' : (y + 2^a*(2*(3*u)))%2 = 1 := by
      have he : 2^a*(2*(3*u)) = 2*(2^a*(3*u)) := by ac_rfl
      rw [he, Nat.add_mod]
      simp [odd]
    have dst : z+3^j*(2*(3*u)) = z+3^(j+1)*(2*u) := by
      rw [Nat.pow_succ]; ac_rfl
    rw [← dst]
    exact .cons src odd' tail

/-- A budget for accumulated exact divisions that requires only positivity. -/
theorem divisionBudget {x y a j : Nat} (h : History x y a j) (hx : 0 < x) :
    2^a*y ≤ 4^j*x := by
  induction h with
  | nil x => simp
  | @cons x y z a j e edge odd rest ih =>
    have hy : 0 < y := by omega
    have he : 2^(e+1)*y ≤ 4*x := by omega
    have h₁ := Nat.mul_le_mul_left (2^(e+1)) (ih hy)
    have h₂ := Nat.mul_le_mul_left (4^j) he
    rw [Nat.pow_add, Nat.pow_succ]
    calc
      2^(e+1)*2^a*z = 2^(e+1)*(2^a*z) := by ac_rfl
      _ ≤ 2^(e+1)*(4^j*y) := h₁
      _ = 4^j*(2^(e+1)*y) := by ac_rfl
      _ ≤ 4^j*(4*x) := h₂
      _ = 4^j*4*x := by ac_rfl

end Collatz.BinaryBoundary

namespace Collatz.MixedBoundary

/-- Rational inverse steps, with no local divisibility guard needed for the
    real inequalities. -/
inductive Reverse : Nat → Rat → Rat → Prop where
  | nil (x : Rat) : Reverse 0 x x
  | even {k : Nat} {x y : Rat} : Reverse k x y → Reverse (k+1) x (2*y)
  | odd {k : Nat} {x y z : Rat} :
      Reverse k x y → 3*z=2*y-1 → Reverse (k+1) x z

theorem negativeWall {k : Nat} {x z : Rat} (h : Reverse k x z) (h' : x ≤ -1) : z ≤ -1 := by
  induction h with
  | nil => exact h'
  | even _ ih => specialize ih h'; grind
  | odd _ edge ih => specialize ih h'; grind

/-- If the starting coordinate is no smaller than (3/2)^t - 1,
    each of at most t reverse steps spends at most one exponent of reserve. -/
theorem expenditure {k : Nat} {x y : Rat} (h : Reverse k x y) :
    ∀ r : Nat, (3/2 : Rat)^(r+k) ≤ x+1 → (3/2 : Rat)^r ≤ y+1 := by
  have hpow : ∀ n : Nat, 1 ≤ (3/2 : Rat)^n := by
    intro n
    induction n with
    | zero => simp [Rat.pow_zero]
    | succ n ih => rw [Rat.pow_succ]; grind
  induction h with
  | nil =>
    intro r h
    simpa using h
  | @even k x y _ ih =>
    intro r hx
    have hy := ih (r+1) (by simpa [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using hx)
    rw [Rat.pow_succ] at hy
    have hh := hpow r
    grind
  | @odd k x y z _ hedge ih =>
    intro r hx
    have hy := ih (r+1) (by simpa [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using hx)
    rw [Rat.pow_succ] at hy
    grind

/-- All inverse offsets have only powers of three as denominators. -/
theorem clearsDenominator {k : Nat} {x y : Rat} (h : Reverse k x y) :
    ∃ a b : Nat, (3 : Rat)^a*y+b = (2 : Rat)^k*x := by
  induction h with
  | nil =>
    exact ⟨0, 0, by simp [Rat.pow_zero]; grind⟩
  | @even k x y _ ih =>
    obtain ⟨a, b, hb⟩ := ih
    refine ⟨a, 2*b, ?_⟩
    rw [Rat.pow_succ]
    grind
  | @odd k x y z _ hz ih =>
    obtain ⟨a, b, hb⟩ := ih
    refine ⟨a+1, 2*b+3^a, ?_⟩
    rw [Rat.pow_succ, Rat.pow_succ]
    have hp : ((3^a : Nat) : Rat) = (3 : Rat)^a := by
      induction a with
      | zero => simp [Rat.pow_zero]
      | succ a h => simp [Nat.pow_succ, Rat.pow_succ]
    grind

end Collatz.MixedBoundary

#print axioms Collatz.BinaryBoundary.transport
#print axioms Collatz.BinaryBoundary.divisionBudget
#print axioms Collatz.MixedBoundary.negativeWall
#print axioms Collatz.MixedBoundary.expenditure
#print axioms Collatz.MixedBoundary.clearsDenominator
