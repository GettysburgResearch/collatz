import EarlierOffsets
import Mathlib.Data.Nat.Find
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-! An explicit finite harmonic criterion for the actual positive Collatz map.
The remaining hypothesis is an inequality for a defined, finite rational sum.
It is not proved in this file. -/
set_option autoImplicit false
set_option warningAsError true

namespace BinaryPrefixCriterion
open CoreBranching PeakRigidity FloorCounting
open EarlierOffsets (Good good_run)
open scoped BigOperators

def Gate (N x : ℕ) : Prop :=
  ∀ j ∈ Finset.range (N+1), 5*j ≤ 8*grade j x

instance (N x : ℕ) : Decidable (Gate N x) := by
  unfold Gate
  infer_instance

def survivors (N : ℕ) : Finset ℕ :=
  (Finset.range (2^N)).filter (fun x => 0<x ∧ Gate N x)

def mass (N : ℕ) : ℚ := ∑ x ∈ survivors N, 1/(x:ℚ)

/-- Expected surviving reserve after one fair binary digit at debt d.
An odd digit adds three; an even digit subtracts five and is killed below zero. -/
def nextReserve (d : ℕ) : ℚ :=
  ((d:ℚ)+8)/2 + if 5≤d then (d:ℚ)/2 else 0

theorem debt_reserve_step (d : ℕ) : 1+nextReserve d ≤ (d:ℚ)+5 := by
  unfold nextReserve
  split_ifs with h
  · linarith
  · have nonneg : (0:ℚ)≤d := Nat.cast_nonneg d
    linarith

private def smallClock : ℕ → ℕ
  | 1 => 0 | 2 => 1 | 3 => 5 | 4 => 2
  | 5 => 4 | 6 => 6 | 7 => 11 | 8 => 3
  | 9 => 13 | 10 => 5 | 11 => 10 | 12 => 7
  | 13 => 7 | 14 => 12 | 15 => 12 | 16 => 4
  | 17 => 9 | 18 => 14 | 19 => 14 | 20 => 6
  | 21 => 6 | 22 => 11 | 23 => 11 | 24 => 8
  | 25 => 16 | 26 => 8 | 27 => 70 | 28 => 13
  | 29 => 13 | 30 => 13 | 31 => 67 | 32 => 5
  | _ => 0

private theorem small_good (x : ℕ) (hp : 0<x) (hb : x≤32) : Good x := by
  refine ⟨smallClock x, ?_⟩
  interval_cases x <;> decide +kernel

private theorem step_positive (x : ℕ) (hx : 0<x) : 0<step x := by
  by_cases h : x%2=0
  · simp only [step,h,ite_true]
    omega
  · simp only [step,h,ite_false]
    omega

private theorem run_positive (n x : ℕ) (hx : 0<x) : 0<run n x := by
  induction n generalizing x with
  | zero => exact hx
  | succ n ih => exact ih (step x) (step_positive x hx)

/-- Every hypothetical bad input has a least positive bad input no larger
than itself, and the complete actual forward orbit stays above that minimum. -/
theorem least_bad (x : ℕ) (hx : 0<x) (bad : ¬ Good x) :
    ∃ m, 33≤m ∧ m≤x ∧ ¬ Good m ∧ (∀ j, m≤run j m) := by
  classical
  have exists_bad : ∃ m : ℕ, 0<m ∧ ¬ Good m := ⟨x,hx,bad⟩
  let m := Nat.find exists_bad
  have hm : 0<m ∧ ¬ Good m := Nat.find_spec exists_bad
  have least (y : ℕ) (hy : 0<y ∧ ¬ Good y) : m≤y := Nat.find_min' exists_bad hy
  have high : 33≤m := by
    by_contra! low
    exact hm.2 (small_good m hm.1 (by omega))
  refine ⟨m,high,least x ⟨hx,bad⟩,hm.2,?_⟩
  intro j
  exact least (run j m) ⟨run_positive j m hm.1,
    fun h => hm.2 ((good_run j m).mp h)⟩

private theorem one_step_power (x : ℕ) (hx : 33≤x) :
    2^5*(step x)^5 ≤ 2^(8*(x%2))*x^5 := by
  by_cases h : x%2=0
  · have split : x=2*(x/2) := by omega
    rw [h,show 8*0=0 by omega,pow_zero,one_mul,split,step_double,mul_pow]
  · have odd : x%2=1 := by omega
    have eq : 2*step x=3*x+1 := by simp [step,h]; omega
    obtain ⟨v,hv⟩ := Nat.exists_eq_add_of_le hx
    have polynomial (v : ℕ) :
        (3*(33+v)+1)^5+
          (13*v^5+1740*v^4+87840*v^3+1998720*v^2+17978880*v+18660608)
          =256*(33+v)^5 := by ring
    have bound : (3*x+1)^5 ≤ 256*x^5 := by
      rw [hv]
      have ident := polynomial v
      omega
    rw [odd,show 8*1=8 by omega]
    calc
      2^5*(step x)^5 = (2*step x)^5 := (mul_pow _ _ _).symm
      _ = (3*x+1)^5 := by rw [eq]
      _ ≤ 256*x^5 := bound
      _ = 2^8*x^5 := by norm_num

private theorem run_last (j x : ℕ) : run (j+1) x=step (run j x) := by
  simpa [run] using run_add j 1 x

private theorem finite_power_bound (m n : ℕ)
    (floor : ∀ j≤n, 33≤run j m) :
    2^(5*n)*(run n m)^5 ≤ 2^(8*grade n m)*m^5 := by
  induction n with
  | zero => simp [run,grade]
  | succ n ih =>
    have old := ih (fun j hj => floor j (by omega))
    have edge := one_step_power (run n m) (floor n (by omega))
    rw [run_last,grade]
    calc
      2^(5*(n+1))*(step (run n m))^5 =
          2^(5*n)*(2^5*(step (run n m))^5) := by
            rw [show 5*(n+1)=5*n+5 by omega,pow_add]; ring
      _ ≤ 2^(5*n)*(2^(8*(run n m%2))*(run n m)^5) :=
          Nat.mul_le_mul_left _ edge
      _ = 2^(8*(run n m%2))*(2^(5*n)*(run n m)^5) := by ring
      _ ≤ 2^(8*(run n m%2))*(2^(8*grade n m)*m^5) :=
          Nat.mul_le_mul_left _ old
      _ = 2^(8*(grade n m+run n m%2))*m^5 := by
          rw [show 8*(grade n m+run n m%2)=8*(run n m%2)+8*grade n m by ring,
              pow_add]; ring

/-- The same fixed least bad integer passes every finite binary prefix gate. -/
theorem minimum_gate (m : ℕ) (hm : 33≤m) (least : ∀ j, m≤run j m) :
    ∀ N, Gate N m := by
  intro N j hj
  have b := finite_power_bound m j (fun i _ => hm.trans (least i))
  have mono : m^5 ≤ (run j m)^5 := Nat.pow_le_pow_left (least j) 5
  have power : 2^(5*j)*m^5 ≤ 2^(8*grade j m)*m^5 :=
    (Nat.mul_le_mul_left _ mono).trans b
  have pos : 0<m^5 := by positivity
  have order : 2^(5*j) ≤ 2^(8*grade j m) := Nat.le_of_mul_le_mul_right power pos
  exact (Nat.pow_le_pow_iff_right (by decide)).mp order

private theorem odd_minimum (m : ℕ) (hp : 0<m) (least : m≤step m) : m%2=1 := by
  by_cases h : m%2=0
  · simp [step,h] at least
    omega
  · omega

/-- Reducing the ordinary source modulo its full binary prefix modulus retains
every prefix grade and gives an actual positive source no larger than it. -/
theorem principal_member (N m : ℕ) (hN : 0<N) (hm : m%2=1) (gate : Gate N m) :
    ∃ r ∈ survivors N, r≤m := by
  let r := m%2^N
  have pow : 2^N=2*2^(N-1) := by
    rw [←pow_succ']; congr 1; omega
  have remodd : r%2=1 := by
    dsimp [r]
    rw [pow,Nat.mod_mul_right_mod]
    exact hm
  have rp : 0<r := by omega
  have rsmall : r<2^N := Nat.mod_lt _ (by positivity)
  have representation : m=r+2^N*(m/2^N) := (Nat.mod_add_div _ _).symm
  have g : Gate N r := by
    intro j hj
    have jN : j≤N := by
      have := Finset.mem_range.mp hj
      omega
    have js : j+(N-j)=N := by omega
    have same := (lift_prefix j (N-j) r (m/2^N)).2
    rw [js,←representation] at same
    rw [←same]
    exact gate j hj
  refine ⟨r,?_,Nat.mod_le _ _⟩
  exact Finset.mem_filter.mpr ⟨Finset.mem_range.mpr rsmall,rp,g⟩

theorem member_reciprocal (N r : ℕ) (hr : r∈survivors N) :
    1/(r:ℚ) ≤ mass N := by
  unfold mass
  exact Finset.single_le_sum (f := fun x : ℕ => (1:ℚ)/(x:ℚ))
    (fun x _ => div_nonneg (by norm_num) (Nat.cast_nonneg x)) hr

/-- A strict inequality for this explicit finite rational sum is a certificate
for every positive ordinary input up to the supplied bound. -/
theorem finite_cutoff (N B : ℕ) (hN : 0<N) (cert : mass N < 1/(B:ℚ)) :
    ∀ x, 0<x → x≤B → Good x := by
  intro x hx hB
  by_contra bad
  obtain ⟨m,hm,hmx,hbad,least⟩ := least_bad x hx bad
  have odd := odd_minimum m (by omega) (by simpa [run] using least 1)
  obtain ⟨r,hr,hrm⟩ := principal_member N m hN odd (minimum_gate m hm least N)
  have rp : 0<r := (Finset.mem_filter.mp hr).2.1
  have rB : (r:ℚ)≤B := by exact_mod_cast hrm.trans (hmx.trans hB)
  have rpq : (0:ℚ)<r := by exact_mod_cast rp
  have lower : 1/(B:ℚ) ≤ 1/(r:ℚ) := one_div_le_one_div_of_le rpq rB
  exact (not_lt_of_ge (lower.trans (member_reciprocal N r hr))) cert

/-- The sole remaining analytic/combinatorial hypothesis is the displayed
family of finite rational inequalities. This file does not prove it. -/
theorem collatz_of_small_finite_mass
    (small : ∀ B : ℕ, 0<B → ∃ N : ℕ, 0<N ∧ mass N < 1/(B:ℚ)) :
    ∀ x : ℕ, 0<x → ∃ h : ℕ, run h x=1 := by
  intro x hx
  obtain ⟨N,hN,cert⟩ := small x hx
  exact finite_cutoff N x hN cert x hx le_rfl

#print axioms least_bad
#print axioms debt_reserve_step
#print axioms minimum_gate
#print axioms principal_member
#print axioms member_reciprocal
#print axioms finite_cutoff
#print axioms collatz_of_small_finite_mass
end BinaryPrefixCriterion
