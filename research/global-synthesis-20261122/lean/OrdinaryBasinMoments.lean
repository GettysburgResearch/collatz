import Std

/-!
Finite disjoint-basin accounting with unchanged original source weights.

All weights are natural numbers, so a common denominator can encode any
finite family of nonnegative rational weights. `owns j n` records whether
the original source `n` lies in the selected basin `j`. The disjointness
hypothesis is checked at each original source, not merely at endpoints.

This module does not assume Collatz convergence or introduce a population
axiom. Its population and minimum-floor premises are explicit. The written
note ORDINARY_MASS.md supplies the ordinary geometry and retains PDU as a
source-qualified analytic input. In that application A = 3 and K = 64.
-/

namespace CollatzOrdinaryBasinMoments

def sumTo : Nat → (Nat → Nat) → Nat
  | 0, _ => 0
  | k + 1, f => sumTo k f + f k

private theorem sumTo_add (N : Nat) (f g : Nat → Nat) :
    sumTo N (fun i => f i + g i) = sumTo N f + sumTo N g := by
  induction N with
  | zero => rfl
  | succ N ih =>
    simp [sumTo, ih, Nat.add_comm, Nat.add_left_comm]

private theorem sumTo_mul_left (N a : Nat) (f : Nat → Nat) :
    sumTo N (fun i => a * f i) = a * sumTo N f := by
  induction N with
  | zero => simp [sumTo]
  | succ N ih => simp [sumTo, ih, Nat.mul_add]

private theorem sumTo_const (N a : Nat) :
    sumTo N (fun _ => a) = N * a := by
  induction N with
  | zero => simp [sumTo]
  | succ N ih => simp [sumTo, ih, Nat.succ_mul]

private theorem sumTo_mono (N : Nat) (f g : Nat → Nat)
    (h : ∀ i, i < N → f i ≤ g i) : sumTo N f ≤ sumTo N g := by
  induction N with
  | zero => exact Nat.le_refl _
  | succ N ih =>
    exact Nat.add_le_add
      (ih (fun i hi => h i (Nat.lt_trans hi (Nat.lt_succ_self N))))
      (h N (Nat.lt_succ_self N))

private theorem sumTo_comm (J X : Nat) (f : Nat → Nat → Nat) :
    sumTo J (fun j => sumTo X (f j)) =
      sumTo X (fun n => sumTo J (fun j => f j n)) := by
  induction J with
  | zero => simp [sumTo, sumTo_const]
  | succ J ih =>
    simp only [sumTo]
    rw [sumTo_add, ih]

private theorem mask_sum (J z : Nat) (b : Nat → Bool) :
    sumTo J (fun j => if b j then z else 0) =
      sumTo J (fun j => if b j then 1 else 0) * z := by
  induction J with
  | zero => simp [sumTo]
  | succ J ih =>
    cases hb : b J <;> simp [sumTo, hb, ih, Nat.add_mul]

/-- Summing selected basin moments never duplicates an original source. -/
theorem retained_source_accounting
    (J X : Nat) (owns : Nat → Nat → Bool) (weight cost : Nat → Nat)
    (disjoint : ∀ n, n < X →
      sumTo J (fun j => if owns j n then 1 else 0) ≤ 1) :
    sumTo J (fun j => sumTo X
      (fun n => if owns j n then weight n * cost n else 0)) ≤
      sumTo X (fun n => weight n * cost n) := by
  rw [sumTo_comm]
  apply sumTo_mono
  intro n hn
  rw [mask_sum]
  exact Nat.le_trans (Nat.mul_le_mul_right _ (disjoint n hn))
    (Nat.le_of_eq (Nat.one_mul _))

/--
`J` disjoint basins each supply a population-weighted minimum contribution.
The same `weight n` appears in the population and the final source moment.
`A * root j ≤ K * minimum n` is the denominator-cleared minimum floor.
-/
theorem disjoint_basin_minimum_moment
    (J X A K T : Nat) (owns : Nat → Nat → Bool)
    (weight minimum root : Nat → Nat)
    (disjoint : ∀ n, n < X →
      sumTo J (fun j => if owns j n then 1 else 0) ≤ 1)
    (floor : ∀ j, j < J → ∀ n, n < X → owns j n = true →
      A * root j ≤ K * minimum n)
    (population : ∀ j, j < J →
      T ≤ root j * sumTo X (fun n => if owns j n then weight n else 0)) :
    A * (J * T) ≤ K * sumTo X (fun n => weight n * minimum n) := by
  have perBasin : ∀ j, j < J →
      A * T ≤ K * sumTo X
        (fun n => if owns j n then weight n * minimum n else 0) := by
    intro j hj
    calc
      A * T ≤ A * (root j * sumTo X
          (fun n => if owns j n then weight n else 0)) :=
        Nat.mul_le_mul_left A (population j hj)
      _ = sumTo X (fun n => (A * root j) *
          (if owns j n then weight n else 0)) := by
        rw [sumTo_mul_left, Nat.mul_assoc]
      _ ≤ sumTo X (fun n => K *
          (if owns j n then weight n * minimum n else 0)) := by
        apply sumTo_mono
        intro n hn
        cases hown : owns j n with
        | false => simp
        | true =>
          have h := Nat.mul_le_mul_right (weight n) (floor j hj n hn hown)
          simpa [hown, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using h
      _ = K * sumTo X
          (fun n => if owns j n then weight n * minimum n else 0) :=
        sumTo_mul_left _ _ _
  have aggregate := sumTo_mono J (fun _ => A * T)
    (fun j => K * sumTo X
      (fun n => if owns j n then weight n * minimum n else 0)) perBasin
  rw [sumTo_const, sumTo_mul_left] at aggregate
  have retained := retained_source_accounting J X owns weight minimum disjoint
  have result := Nat.le_trans aggregate (Nat.mul_le_mul_left K retained)
  simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using result

#print axioms retained_source_accounting
#print axioms disjoint_basin_minimum_moment

end CollatzOrdinaryBasinMoments
