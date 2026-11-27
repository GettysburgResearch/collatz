import Std

/-! Integer proof of the clock-order input for moving octaves. -/
namespace MovingOctaveOrder

private theorem orderClock {h a b x y : Nat}
    (hx : h ≤ x) (hy : y < 2*h)
    (lt : 2^a*x < 2^b*y) : a ≤ b := by
  apply Classical.byContradiction
  intro no
  have p : 2^(b+1) ≤ 2^a := Nat.pow_le_pow_right (by decide) (by omega)
  have lo := Nat.mul_le_mul p hx
  have hi := Nat.mul_lt_mul_of_pos_left hy (Nat.two_pow_pos b)
  rw [Nat.pow_succ, Nat.mul_assoc] at lo
  omega

/-- A finite ordinary odd path, with each endpoint at its specified octave. -/
structure Path (H : Nat → Nat) (k : Nat) where
  x : Nat → Nat
  a : Nat → Nat
  clock : Nat → Nat
  start : clock 0 = 0
  advance : ∀ j, j < k → clock (j+1) = clock j + a j
  physical : ∀ j, j < k → 2^(a j) * x (j+1) = 3*x j+1
  band : ∀ j, j ≤ k → H j ≤ x j ∧ x j < 2*H j

def lift {H k} (P : Path H k) (j : Nat) := 2^(P.clock j) * P.x j

theorem lift_step {H k} (P : Path H k) (j : Nat) (hj : j<k) :
    lift P (j+1)=3*lift P j+2^(P.clock j) := by
  simp only [lift, P.advance j hj, Nat.pow_add, Nat.mul_assoc, P.physical j hj,
    Nat.mul_add, Nat.mul_one, Nat.mul_left_comm (2^P.clock j) 3]

private theorem order_at {H k} (P Q : Path H k) (j : Nat) (hj : j≤k)
    (lo : lift P j < lift Q j) (hi : lift Q j < 2*lift P j) :
    P.clock j ≤ Q.clock j ∧ Q.clock j ≤ P.clock j + 1 := by
  refine ⟨orderClock (P.band j hj).1 (Q.band j hj).2 lo, ?_⟩
  apply orderClock (Q.band j hj).1 (P.band j hj).2
  simpa only [lift, Nat.pow_succ, Nat.mul_right_comm _ 2, Nat.mul_comm _ 2, Nat.mul_assoc] using hi

/-- The clock vectors on one physical octave profile are componentwise
ordered and have width at most one in each coordinate. -/
theorem moving_clock_order {H k} (P Q : Path H k) (initial : P.x 0<Q.x 0)
    (j : Nat) (hj : j≤k) :
    P.clock j ≤ Q.clock j ∧ Q.clock j ≤ P.clock j+1 := by
  have enclosure : ∀ i≤k, lift P i < lift Q i ∧ lift Q i < 2*lift P i := by
    intro i bound
    induction i with
    | zero =>
      have p := (P.band 0 (by omega)).1
      have q := (Q.band 0 (by omega)).2
      simpa only [lift, P.start, Q.start, Nat.pow_zero, Nat.one_mul] using
        (show P.x 0<Q.x 0 ∧ Q.x 0<2*P.x 0 from ⟨initial, by omega⟩)
    | succ i ih =>
      have prev := ih (by omega)
      have rank := order_at P Q i (by omega) prev.1 prev.2
      have plo := Nat.pow_le_pow_right (by decide : 0<2) rank.1
      have phi := Nat.pow_le_pow_right (by decide : 0<2) rank.2
      rw [Nat.pow_succ] at phi
      rw [lift_step P i (by omega), lift_step Q i (by omega)]
      constructor <;> omega
  exact order_at P Q j hj (enclosure j hj).1 (enclosure j hj).2

/-- Equal clocks propagate the source difference exactly. -/
private theorem equal_clock_lift {H k} (P Q : Path H k) (D : Nat)
    (start : Q.x 0 = P.x 0 + D) (eqs : ∀ j≤k, P.clock j=Q.clock j)
    (j : Nat) (hj : j≤k) : lift Q j = lift P j + 3^j*D := by
  induction j with
  | zero => simpa only [lift, P.start, Q.start, Nat.pow_zero, Nat.one_mul] using start
  | succ j ih =>
    have prev := ih (by omega)
    rw [lift_step Q j (by omega), lift_step P j (by omega), prev, eqs j (by omega),
      Nat.mul_add, Nat.pow_succ]
    have mul : 3*(3^j*D) = 3^j*3*D := by ac_rfl
    omega

/-- Endpoint spacing alone separates actual sources with the same word. -/
theorem words_differ {H k} (P Q : Path H k) (initial : P.x 0<Q.x 0)
    (terminal : H k ≤ 3^k) : ¬(∀ j≤k, P.clock j=Q.clock j) := by
  intro eqs
  let D := Q.x 0-P.x 0
  have hd : 0<D := by dsimp [D]; omega
  have diff := equal_clock_lift P Q D (by dsimp [D]; omega) eqs k (by omega)
  simp only [lift, eqs k (by omega)] at diff
  have hpos : 0 < 3^k*D := Nat.mul_pos (Nat.pow_pos (by decide : 0<3)) hd
  have lt : P.x k < Q.x k := Nat.lt_of_mul_lt_mul_left (by omega :
      2^Q.clock k*P.x k < 2^Q.clock k*Q.x k)
  have hdvd : 3^k ∣ 2^Q.clock k*(Q.x k-P.x k) := by
    refine ⟨D, ?_⟩
    rw [Nat.mul_sub]
    omega
  have cop : Nat.Coprime (3^k) (2^Q.clock k) :=
    ((by decide : Nat.Coprime 3 2).pow_left k).pow_right _
  have wide := Nat.le_of_dvd (by omega : 0<Q.x k-P.x k) (cop.dvd_of_dvd_mul_left hdvd)
  have inside := (P.band k (by omega)).1
  have outside := (Q.band k (by omega)).2
  omega

private def mass (f : Nat → Nat) : Nat → Nat
  | 0 => 0
  | j+1 => mass f j + f (j+1)

private theorem mass_bounds (f g : Nat → Nat) (k : Nat)
    (h : ∀ i≤k, f i≤g i ∧ g i≤f i+1) (base : f 0=g 0) :
    mass f k ≤ mass g k ∧ mass g k ≤ mass f k + k ∧
    (mass f k=mass g k → ∀ i≤k, f i=g i) := by
  induction k with
  | zero =>
    simp only [mass, Nat.add_zero, Nat.le_refl, true_and]
    intro _ i hi
    have eq : i=0 := by omega
    simpa only [eq] using base
  | succ k ih =>
    obtain ⟨lo,hi,eq⟩ := ih (fun i hi => h i (by omega))
    have last := h (k+1) (by omega)
    simp only [mass]
    refine ⟨by omega, by omega, ?_⟩
    intro he i hi
    by_cases top : i=k+1
    · subst i; omega
    · exact eq (by omega) i (by omega)

/-- The complete per-profile capacity: an increasing family of n+1 actual
sources has size at most k+1 when the terminal octave width is at most 3^k. -/
theorem capacity {H k} (P : Nat → Path H k) (n : Nat)
    (ordered : ∀ i j, i<j → j≤n → (P i).x 0 < (P j).x 0)
    (terminal : H k≤3^k) : n≤k := by
  have comparison (i j : Nat) (lt : i<j) (b : j≤n) :=
    mass_bounds (P i).clock (P j).clock k
      (moving_clock_order _ _ (ordered i j lt b)) ((P i).start.trans (P j).start.symm)
  have lower : ∀ j≤n, mass (P 0).clock k+j ≤ mass (P j).clock k := by
    intro j hj
    induction j with
    | zero => omega
    | succ j ih =>
      have prev := ih (by omega)
      have c := comparison j (j+1) (by omega) hj
      have ne := words_differ (P j) (P (j+1)) (ordered _ _ (by omega) hj) terminal
      have strict : mass (P j).clock k ≠ mass (P (j+1)).clock k := fun eq => ne (c.2.2 eq)
      omega
  by_cases hn : n=0
  · omega
  · have upper := (comparison 0 n (by omega) (by omega)).2.1
    have low := lower n (by omega)
    omega

#print axioms moving_clock_order
#print axioms capacity
end MovingOctaveOrder
