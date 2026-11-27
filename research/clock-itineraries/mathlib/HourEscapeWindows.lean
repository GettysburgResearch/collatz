module

public import HourEscapeSigned
import all HourEscapeSigned
import all HourEscapeLimits
import all HourEscapeDrawdown
import all HourCycleShadow
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.HourEscape

open Collatz.HourCycleShadow
set_option autoImplicit false

/-- A finite ordinary window read backwards from a fixed ternary class, with
every site in one multiplicative height interval. The gaps are unrestricted
positive integers. -/
structure StripWindow (d : ℕ) (A : ℤ) (K N : ℕ) where
  m : ℕ
  x : ℕ → ℕ
  e : ℕ → ℕ
  positive : 0<m
  room : K*N≤m
  band : ∀ i, i≤N → m≤x i ∧ x i≤K*m
  edge : ∀ i,i<N → 0<e i ∧ 3*x (i+1)+1=2^(e i)*x i
  residue : (3:ℤ)^N∣(d:ℤ)*x 0-A

private theorem clock_cap {d K N i : ℕ} {A : ℤ} (z : StripWindow d A K N) (small : i<N) :
    z.e i<3*K+1 := by
  obtain ⟨_,e⟩ := z.edge i small
  have p := z.positive
  have calc₀ := Nat.mul_le_mul_left (2^(z.e i)) (z.band i small.le).1
  have calc₁ := Nat.mul_le_mul_left 3 (z.band (i+1) (by omega)).2
  rw [←e] at calc₀
  have cap : 2^(z.e i)*z.m≤(3*K+1)*z.m := by
    rw [Nat.add_mul,Nat.one_mul,Nat.mul_assoc]; omega
  have power := Nat.le_of_mul_le_mul_right cap p
  have low := Nat.lt_two_pow_self (n:=z.e i)
  omega

private theorem prefix_affine {x e : ℕ → ℕ} {n : ℕ}
    (edges : ∀ i,i<n → 3*x (i+1)+1=2^(e i)*x i) :
    (2:ℤ)^(prefixSum e n)*(x 0:ℤ) = 3^n*(x n:ℤ)+inverseCarry e n := by
  induction n with
  | zero => simp [prefixSum,inverseCarry]
  | succ n ih =>
    have prior := ih (fun i hi => edges i (by omega))
    have step : 3*(x (n+1):ℤ)+1=(2:ℤ)^(e n)*(x n:ℤ) := by exact_mod_cast edges n (by omega)
    rw [prefixSum,inverseCarry,pow_add,pow_succ (3:ℤ) n]
    linear_combination (2:ℤ)^(e n)*prior-(3:ℤ)^n*step

private theorem one_residue {d K N n : ℕ} {A : ℤ} {e : ℕ → ℕ}
    (z : StripWindow d A K N) (len : n≤N) (agree : ∀ i,i<n → z.e i=e i) :
    (3:ℤ)^n∣2^(prefixSum e n)*A-(d:ℤ)*inverseCarry e n := by
  have div := dvd_trans (pow_dvd_pow (3:ℤ) len) z.residue
  obtain ⟨c,hc⟩ := div
  have path := prefix_affine (e:=e) (x:=z.x) (n:=n) (fun i hi => by
    rw [←agree i hi]; exact (z.edge i (by omega)).2)
  refine ⟨(d:ℤ)*(z.x n:ℤ)-2^(prefixSum e n)*c,?_⟩
  linear_combination (d:ℤ)*path-(2:ℤ)^(prefixSum e n)*hc

/-- Each fixed rational ternary class is excluded at a finite precision
from every sufficiently high ordinary window of bounded multiplicative
width. No upper bound on the individual positive gaps is assumed. -/
theorem arbitrary_gap_window_exclusion (d K : ℕ) (A : ℤ) (dp : 0<d) (kp : 0<K) :
    ∃ N, ¬Nonempty (StripWindow d A K N) := by
  by_contra! all
  let z := fun n => Classical.choice (all n)
  let w := fun n i => if i<n then (z n).e i else 1
  have bound (n i : ℕ) : w n i<3*K+2 := by
    dsimp [w]
    split
    · exact Nat.lt_trans (clock_cap _ (by omega)) (by omega)
    · omega
  obtain ⟨e,limit⟩ := trace_compact w bound
  have chooseWindow (n : ℕ) : ∃ N, n≤N ∧ ∀ i,i<n → (z N).e i=e i := by
    obtain ⟨N,large,agreement⟩ := limit n n
    refine ⟨N,large,fun i hi => ?_⟩
    have good : i<N := by omega
    simpa [w,good] using agreement i hi
  have trace : RationalTrace d A e := by
    intro n
    obtain ⟨N,late,agree⟩ := chooseWindow n
    exact one_residue (z N) late agree
  have pos (i : ℕ) : 0<e i := by
    obtain ⟨N,late,agree⟩ := chooseWindow (i+1)
    rw [←agree i (by omega)]
    exact ((z N).edge i (by omega)).1
  have balanced : BoundedClock e := by
    refine ⟨2*K,weight e,by omega,fun n => ?_⟩
    obtain ⟨N,late,agree⟩ := chooseWindow n
    have localClock := window_strip (e:=e) (x:=(z N).x) (m:=(z N).m) (K:=K) (N:=n)
      (z N).positive (Nat.le_trans (Nat.mul_le_mul_left K late) (z N).room)
      (fun i hi => (z N).band i (by omega))
      (fun i hi => by rw [←agree i hi]; exact ((z N).edge i (by omega)).2)
    refine ⟨localClock.1,?_,weight_step e n⟩
    have high := localClock.2
    push_cast
    linarith only [high,Nat.cast_nonneg (α:=ℝ) K]
  obtain ⟨y,shadow⟩ := shadow_of_trace trace
  exact no_rational_balanced_shadow dp pos shadow balanced

/-- For a fixed width factor and rational class, one finite depth uniformly
excludes that class at every phase of all sufficiently high positive cycles,
independently of their periods and gap alphabet. -/
theorem arbitrary_gap_cycle_phase_exclusion (d K : ℕ) (A : ℤ) (dp : 0<d) (kp : 0<K) :
    ∃ N, ∀ (x g : ℕ → ℕ) (m p : ℕ), 0<p → 0<m → K*N≤m →
    (∀ j,m≤x j ∧ x j≤K*m) → (∀ j,0<g j ∧ 3*x j+1=2^(g j)*x (j+1)) →
    (∀ j,x (j+p)=x j) → ∀ t, ¬(3:ℤ)^N∣(d:ℤ)*x t-A := by
  obtain ⟨N,empty⟩ := arbitrary_gap_window_exclusion d K A dp kp
  refine ⟨N,fun x g m p pp mp room band edge period t congr => ?_⟩
  have laps (n : ℕ) : x (t+n*p)=x t := by
    induction n with
    | zero => simp
    | succ n ih => rw [Nat.succ_mul,←Nat.add_assoc,period,ih]
  let back := fun j => t+N*p-j
  have big : N≤N*p := by simpa using Nat.mul_le_mul_left N pp
  apply empty
  refine ⟨⟨m,fun j => x (back j),fun j => g (back (j+1)),mp,room,fun j _ => band _,?_,?_⟩⟩
  · intro j hj
    have nxt : back (j+1)+1=back j := by dsimp [back]; omega
    obtain ⟨positive,eqn⟩ := edge (back (j+1))
    exact ⟨positive,by simpa only [nxt] using eqn⟩
  · simpa [back,laps] using congr

#print axioms arbitrary_gap_window_exclusion
#print axioms arbitrary_gap_cycle_phase_exclusion
end Collatz.Itinerary.HourEscape
