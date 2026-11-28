import Std

/-! Product estimate on a finite ordinary odd path with a fixed floor.
The values, local gap exponents and clocks are those of the same path. -/

namespace ComponentLoss

theorem edge_bound (m x y a : Nat) (hfloor : m ≤ x)
    (hedge : 2^a * y = 3*x + 1) :
    m * (2^a * y) ≤ (3*m+1)*x := by
  rw [hedge, Nat.mul_add, Nat.add_mul]
  simpa [Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm] using
    (Nat.add_le_add_left hfloor (3*(m*x)))

theorem path_bound (m : Nat) (state gap clock : Nat → Nat)
    (hzero : clock 0 = 0) (hclock : ∀ i, clock (i+1) = clock i + gap i)
    (n : Nat) (hfloor : ∀ i < n, m ≤ state i)
    (hedge : ∀ i < n, 2^gap i * state (i+1) = 3*state i+1) :
    m^n * (2^clock n * state n) ≤ (3*m+1)^n * state 0 := by
  induction n with
  | zero => simp [hzero]
  | succ n ih =>
    have prev := ih (fun i hi => hfloor i (by omega)) (fun i hi => hedge i (by omega))
    have edge := edge_bound m (state n) (state (n+1)) (gap n)
      (hfloor n (by omega)) (hedge n (by omega))
    calc
      m^(n+1)*(2^clock (n+1)*state (n+1))
          = (m^n*2^clock n)*(m*(2^gap n*state (n+1))) := by
              rw [hclock, Nat.pow_succ m n, Nat.pow_add 2 (clock n) (gap n)]
              simp only [Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]
      _ ≤ (m^n*2^clock n)*((3*m+1)*state n) := Nat.mul_le_mul_left _ edge
      _ = (3*m+1)*(m^n*(2^clock n*state n)) := by
            simp only [Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]
      _ ≤ (3*m+1)*((3*m+1)^n*state 0) := Nat.mul_le_mul_left _ prev
      _ = (3*m+1)^(n+1)*state 0 := by
            rw [Nat.pow_succ]
            simp only [Nat.mul_left_comm, Nat.mul_comm]

theorem uniform_base (m : Nat) (hm : 3 ≤ m) : 3*(3*m+1) ≤ 10*m := by omega

theorem floor_three_strict : 10^4 < 128*3^4 := by decide +kernel

#print axioms edge_bound
#print axioms path_bound
#print axioms uniform_base
#print axioms floor_three_strict

end ComponentLoss
