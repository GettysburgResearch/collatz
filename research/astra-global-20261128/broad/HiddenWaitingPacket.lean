import Mathlib.Data.Rat.Cast.Order
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Fintype.BigOperators

/-! A waiting-time obstruction for every finite randomized controller. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.HiddenWaitingPacket
open Finset

variable {ι : Type*} [Fintype ι] {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- Probability of one specified label followed by a hidden transition. -/
def step (A : ι → ι → R) (g : ι → R) (i : ι) : R := ∑ j, A i j * g j

/-- Probability of exactly k repetitions followed by the specified exit label. -/
def wait (A : ι → ι → R) (v : ι → R) : ℕ → ι → R
  | 0 => v
  | k+1 => step A (wait A v k)

omit [LinearOrder R] [IsStrictOrderedRing R] in
private theorem wait_add (A : ι → ι → R) (v : ι → R) (k l : ℕ) :
    wait A v (k+l) = wait A (wait A v l) k := by
  induction k with
  | zero => simp [wait]
  | succ k ih => simp only [Nat.succ_add, wait, ih]

private theorem wait_nonneg (A : ι → ι → R) (g : ι → R)
    (hA : ∀ i j, 0 ≤ A i j) (hg : ∀ i, 0 ≤ g i) (k : ℕ) :
    ∀ i, 0 ≤ wait A g k i := by
  induction k with
  | zero => exact hg
  | succ k ih => exact fun i => sum_nonneg fun j _ => mul_nonneg (hA i j) (ih j)

private theorem wait_le (A : ι → ι → R) (g : ι → R)
    (hA : ∀ i j, 0 ≤ A i j) (hrow : ∀ i, ∑ j, A i j ≤ 1)
    (c : R) (hc : 0 ≤ c) (hg : ∀ i, g i ≤ c) (k : ℕ) :
    ∀ i, wait A g k i ≤ c := by
  induction k with
  | zero => exact hg
  | succ k ih =>
    intro i
    calc
      _ ≤ ∑ j, A i j * c := sum_le_sum fun j _ => mul_le_mul_of_nonneg_left (ih j) (hA i j)
      _ = (∑ j, A i j)*c := (sum_mul _ _ _).symm
      _ ≤ 1*c := mul_le_mul_of_nonneg_right (hrow i) hc
      _ = _ := one_mul c

/-- The probabilities of exiting after different waiting times are disjoint. -/
theorem exit_mass_le_one (A : ι → ι → R) (v : ι → R)
    (hA : ∀ i j, 0 ≤ A i j) (hexit : ∀ i, v i + ∑ j, A i j ≤ 1)
    (n : ℕ) : ∀ i, ∑ k ∈ range n, wait A v k i ≤ 1 := by
  induction n with
  | zero => simp
  | succ n ih =>
    intro i
    rw [sum_range_succ']
    calc
      _ = (∑ j, A i j*(∑ k ∈ range n, wait A v k j)) + v i := by
        simp only [wait, step, mul_sum]
        rw [sum_comm]
      _ ≤ (∑ j, A i j*1) + v i := by
        exact add_le_add (sum_le_sum fun j _ => mul_le_mul_of_nonneg_left (ih j) (hA i j)) le_rfl
      _ ≤ _ := by simpa only [mul_one, add_comm] using hexit i

/-- A homogeneous M-state controller cannot time M repetitions and an exit
with probability greater than M/(M+1), uniformly over initial hidden states. -/
theorem waiting_packet (A : ι → ι → R) (v : ι → R)
    (hA : ∀ i j, 0 ≤ A i j) (hv : ∀ i, 0 ≤ v i)
    (hexit : ∀ i, v i + ∑ j, A i j ≤ 1) (n : ℕ) (i : ι) :
    (n+1 : R)*wait A v n i ≤ Fintype.card ι := by
  have hr (j : ι) : ∑ l, A j l ≤ 1 := (le_add_of_nonneg_left (hv j)).trans (hexit j)
  have split (k : ℕ) (hk : k ∈ range (n+1)) :
      wait A v n i ≤ ∑ j, wait A v k j := by
    have hkn : k ≤ n := Nat.le_of_lt_succ (mem_range.mp hk)
    let g := wait A v k
    have hg : ∀ j, 0 ≤ g j := wait_nonneg A v hA hv k
    have he := wait_le A g hA hr (∑ j, g j)
      (sum_nonneg fun j _ => hg j) (fun j => single_le_sum (fun l _ => hg l) (mem_univ j)) (n-k) i
    rw [← wait_add, Nat.sub_add_cancel hkn] at he
    exact he
  calc
    _ = ∑ k ∈ range (n+1), wait A v n i := by simp
    _ ≤ ∑ k ∈ range (n+1), ∑ j, wait A v k j := sum_le_sum split
    _ = ∑ j, ∑ k ∈ range (n+1), wait A v k j := sum_comm
    _ ≤ ∑ _j : ι, (1 : R) := sum_le_sum fun j _ => exit_mass_le_one A v hA hexit (n+1) j
    _ = _ := by simp

end Collatz.HiddenWaitingPacket
