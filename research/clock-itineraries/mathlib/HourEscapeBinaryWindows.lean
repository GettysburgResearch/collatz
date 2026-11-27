module
public import HourEscapeBinary
import all HourEscapeBinary
import all HourEscapeDrawdown
import all HourEscapeLimits
import all HourCycleShadow
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.HourEscape
open Collatz.HourCycleShadow
set_option autoImplicit false

structure ForwardWindow (d : ℕ) (A : ℤ) (K N : ℕ) where
  m : ℕ
  x : ℕ → ℕ
  e : ℕ → ℕ
  positive : 0<m
  room : K*N≤m
  band : ∀ i, i≤N → m≤x i ∧ x i≤K*m
  edge : ∀ i,i<N → 0<e i ∧ 3*x i+1=2^(e i)*x (i+1)
  residue : (2:ℤ)^N∣(d:ℤ)*x 0-A

private def forwardCarry (e : ℕ → ℕ) : ℕ → ℤ
  | 0 => 0
  | n+1 => 3*forwardCarry e n+2^(prefixSum e n)

private theorem affine_forward {x e : ℕ → ℕ} {n : ℕ}
    (edge : ∀ i,i<n → 3*x i+1=2^(e i)*x (i+1)) :
    (2:ℤ)^(prefixSum e n)*(x n:ℤ)=3^n*(x 0:ℤ)+forwardCarry e n := by
  induction n with
  | zero => simp [prefixSum,forwardCarry]
  | succ n ih =>
    have prev := ih (fun i hi => edge i (by omega))
    have step : 3*(x n:ℤ)+1=(2:ℤ)^(e n)*(x (n+1):ℤ) := by exact_mod_cast edge n (by omega)
    rw [prefixSum,forwardCarry,pow_add,pow_succ (3:ℤ) n]
    linear_combination 3*prev-(2:ℤ)^(prefixSum e n)*step

private theorem reverse_weight (e : ℕ → ℕ) (n : ℕ) :
    weight (fun j => e (n-(j+1))) n=weight e n := by
  have summ (u : ℕ → ℕ) (b : ℕ) : total u b=∑ i∈Finset.range b,u i := by
    induction b with
    | zero => simp [total]
    | succ b ih => simp [total,Finset.sum_range_succ,ih]
  rw [weight_formula,weight_formula,summ,summ]
  have eqn : (∑ i∈Finset.range n,e (n-(i+1)))=∑ i∈Finset.range n,e i := by
    simpa only [Nat.sub_add_eq,Nat.sub_right_comm] using Finset.sum_range_reflect e n
  rw [eqn]

/-- For any fixed rational dyadic coordinate and fixed multiplicative width,
one finite precision excludes that coordinate at the input of every
sufficiently high ordinary forward window, with unrestricted positive gaps. -/
theorem dyadic_window_exclusion (d K : ℕ) (A : ℤ) (odd : d%2=1) (kp : 0<K) :
    ∃ N, ¬Nonempty (ForwardWindow d A K N) := by
  by_contra! all
  let z := fun n => Classical.choice (all n)
  let w := fun n i => if i<n then (z n).e i else 1
  have bound (n i : ℕ) : w n i<3*K+2 := by
    dsimp [w]
    split
    · rename_i small
      have g := ((z n).edge i small).2
      have p := (z n).positive
      have m := Nat.mul_le_mul_left (2^((z n).e i)) ((z n).band (i+1) (by omega)).1
      have h := Nat.mul_le_mul_left 3 ((z n).band i (by omega)).2
      rw [←g] at m
      have cap : 2^((z n).e i)*(z n).m≤(3*K+1)*(z n).m := by
        rw [Nat.add_mul,Nat.one_mul,Nat.mul_assoc]; omega
      have pw := Nat.le_of_mul_le_mul_right cap p
      have l := Nat.lt_two_pow_self (n:=(z n).e i)
      omega
    · omega
  obtain ⟨e,limit⟩ := trace_compact w bound
  have chooseWindow (n T : ℕ) : ∃ N, n+T≤N ∧ ∀ i,i<n → (z N).e i=e i := by
    obtain ⟨N,late,agree⟩ := limit n (n+T)
    refine ⟨N,late,fun i hi => ?_⟩
    have h : i<N := by omega
    simpa [w,h] using agree i hi
  have pos (i : ℕ) : 0<e i := by
    obtain ⟨N,late,agree⟩ := chooseWindow (i+1) 0
    rw [←agree i (by omega)]
    exact ((z N).edge i (by omega)).1
  have digits (n : ℕ) : (2:ℤ)^(prefixSum e n)∣3^n*A+(d:ℤ)*forwardCarry e n := by
    obtain ⟨N,late,agree⟩ := chooseWindow n (prefixSum e n)
    have sub := dvd_trans (pow_dvd_pow (2:ℤ) (show prefixSum e n≤N by omega)) (z N).residue
    obtain ⟨c,hc⟩ := sub
    have path := affine_forward (n:=n) (x:=(z N).x) (e:=e) (fun i hi => by
      rw [←agree i hi]; exact ((z N).edge i (by omega)).2)
    refine ⟨(d:ℤ)*((z N).x n:ℤ)-3^n*c,?_⟩
    linear_combination -(d:ℤ)*path-(3:ℤ)^n*hc
  let y := fun n => Classical.choose (digits n)
  have rep (n : ℕ) : 3^n*A+(d:ℤ)*forwardCarry e n=2^(prefixSum e n)*y n :=
    Classical.choose_spec (digits n)
  have signed : ForwardShadow d e y := by
    intro n
    have small := rep n
    have large := rep (n+1)
    rw [prefixSum,pow_add (2:ℤ),forwardCarry,pow_succ (3:ℤ) n] at large
    apply mul_left_cancel₀ (by positivity : (2:ℤ)^(prefixSum e n)≠0)
    linear_combination 3*small-large
  apply no_rational_forward_balanced odd pos signed
  refine ⟨2*K,weight e,by omega,fun n => ?_⟩
  obtain ⟨N,late,agree⟩ := chooseWindow n 0
  let ex := fun j => e (n-(j+1))
  let xx := fun j => (z N).x (n-j)
  have edge (j : ℕ) (hj : j<n) : 3*xx (j+1)+1=2^(ex j)*xx j := by
    have small : n-(j+1)<n := by omega
    have g := ((z N).edge (n-(j+1)) (by omega)).2
    rw [agree _ small,show n-(j+1)+1=n-j by omega] at g
    exact g
  have bounds := window_strip (e:=ex) (x:=xx) (m:=(z N).m) (K:=K) (N:=n)
    (z N).positive (Nat.le_trans (Nat.mul_le_mul_left K (by omega)) (z N).room)
    (fun i hi => (z N).band (n-i) (by omega)) edge
  change 1≤((2*K:ℕ):ℝ)*weight (fun j => e (n-(j+1))) n ∧
    weight (fun j => e (n-(j+1))) n≤K at bounds
  rw [reverse_weight] at bounds
  refine ⟨bounds.1,?_,weight_step e n⟩
  have upper := bounds.2
  push_cast
  linarith only [upper,Nat.cast_nonneg (α:=ℝ) K]

/-- The dyadic forbidden class applies at every phase of every sufficiently
high ordinary positive cycle with the fixed width factor. -/
theorem dyadic_cycle_phase_exclusion (d K : ℕ) (A : ℤ) (odd : d%2=1) (kp : 0<K) :
    ∃ N, ∀ (x e : ℕ → ℕ) (m : ℕ), 0<m → K*N≤m →
      (∀ j,m≤x j ∧ x j≤K*m) →
      (∀ j,0<e j ∧ 3*x j+1=2^(e j)*x (j+1)) →
      ∀ t, ¬(2:ℤ)^N∣(d:ℤ)*x t-A := by
  obtain ⟨N,no⟩ := dyadic_window_exclusion d K A odd kp
  refine ⟨N,fun x e m mp enough band edge t congr => ?_⟩
  apply no
  exact ⟨⟨m,fun j => x (t+j),fun j => e (t+j),mp,enough,fun j _ => band _,
    fun j _ => edge (t+j),by simpa using congr⟩⟩

#print axioms dyadic_window_exclusion
#print axioms dyadic_cycle_phase_exclusion

/-- One precision simultaneously excludes a prescribed rational coordinate
in each completion, at every phase of every high bounded-width cycle. -/
theorem simultaneous_cycle_phase_exclusion (d₂ d₃ K : ℕ) (A₂ A₃ : ℤ)
    (odd : d₂%2=1) (positive : 0<d₃) (kp : 0<K) :
    ∃ N, ∀ (x e : ℕ → ℕ) (m p : ℕ), 0<p → 0<m → K*N≤m →
      (∀ j,m≤x j ∧ x j≤K*m) → (∀ j,0<e j ∧ 3*x j+1=2^(e j)*x (j+1)) →
      (∀ j,x (j+p)=x j) → ∀ t,
        (¬(2:ℤ)^N∣(d₂:ℤ)*x t-A₂) ∧ (¬(3:ℤ)^N∣(d₃:ℤ)*x t-A₃) := by
  obtain ⟨u,du⟩ := dyadic_cycle_phase_exclusion d₂ K A₂ odd kp
  obtain ⟨v,tv⟩ := arbitrary_gap_cycle_phase_exclusion d₃ K A₃ positive kp
  refine ⟨max u v,fun x e m p pp mp enough band edge period t => ?_⟩
  have small := du x e m mp (Nat.le_trans (Nat.mul_le_mul_left K (Nat.le_max_left ..)) enough)
    band edge t
  have large := tv x e m p pp mp (Nat.le_trans (Nat.mul_le_mul_left K (Nat.le_max_right ..)) enough)
    band edge period t
  exact ⟨fun h => small (dvd_trans (pow_dvd_pow (2:ℤ) (Nat.le_max_left ..)) h),
    fun h => large (dvd_trans (pow_dvd_pow (3:ℤ) (Nat.le_max_right ..)) h)⟩

#print axioms simultaneous_cycle_phase_exclusion
end Collatz.Itinerary.HourEscape
