module
public import ReturnOrbitTernary
public import ReturnOrbitWindows
import all ReturnOrbitTernary
import all ReturnOrbitBinary
import all HourEscapeWindows
import all HourEscapeSigned
import all HourEscapeDrawdown
import all HourCycleShadow
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.HourEscape
open Collatz.HourCycleShadow
set_option autoImplicit false

/-- Uniform ternary precision for ordinary positive windows of width K. -/
def ternaryWindowPrecision (d K : ℕ) (A : ℤ) : ℕ := inverseRationalHorizon d (2*K) A

/-- Direct ternary exclusion for an actual window specified by its clock
products, independent of the physical size of the ordinary sites. -/
theorem ordinary_ternary_clock_exclusion {d K : ℕ} {A : ℤ} {e x : ℕ → ℕ}
    (dp : 0<d) (kp : 0<K) (pos : ∀ i,0<e i)
    (edge : ∀ i, i < inverseRationalHorizon d K A → 3*x (i+1)+1=2^(e i)*x i)
    (strip : FiniteWeightStrip e K (inverseRationalHorizon d K A)) :
    ¬(3:ℤ)^(inverseRationalHorizon d K A) ∣ (d:ℤ)*x 0-A := by
  intro congruent
  let N := inverseRationalHorizon d K A
  have digits (k : ℕ) (hk : k≤N) :
      (3:ℤ)^k∣2^(prefixSum e k)*A-(d:ℤ)*inverseCarry e k := by
    obtain ⟨c,hc⟩ := dvd_trans (pow_dvd_pow (3:ℤ) hk) congruent
    have path := prefix_affine (e:=e) (x:=x) (n:=k) (fun i hi => edge i (hi.trans_le hk))
    refine ⟨(d:ℤ)*(x k:ℤ)-2^(prefixSum e k)*c,?_⟩
    linear_combination (d:ℤ)*path-(2:ℤ)^(prefixSum e k)*hc
  let y := fun k => if hk : k≤N then Classical.choose (digits k hk) else 0
  have rep (k : ℕ) (hk : k≤N) :
      2^(prefixSum e k)*A-(d:ℤ)*inverseCarry e k=3^k*y k := by
    simpa only [y,dite_eq_left hk] using Classical.choose_spec (digits k hk)
  have y0 : y 0=A := by simpa [prefixSum,inverseCarry] using (rep 0 (by omega)).symm
  apply finite_ternary_rational_rigidity (d:=d) (K:=K) (y:=y) kp dp pos
  · rw [y0]; intro i hi
    change i<N at hi
    have small := rep i (by omega)
    have large := rep (i+1) (by omega)
    rw [prefixSum,inverseCarry,pow_add,pow_succ (3:ℤ) i] at large
    apply mul_left_cancel₀ (by positivity : (3:ℤ)^i≠0)
    linear_combination (2:ℤ)^(e i)*small-large
  · rwa [y0]

/-- A high ordinary backward window with bounded physical width has an
explicit forbidden ternary residue for each rational numerator/denominator. -/
theorem effective_ternary_window_exclusion (d K : ℕ) (A : ℤ) (dp : 0<d)
    (kp : 0<K) : ¬Nonempty (StripWindow d A K (ternaryWindowPrecision d K A)) := by
  rintro ⟨z⟩
  let N := ternaryWindowPrecision d K A
  let e := fun i => max 1 (z.e i)
  have pos (i : ℕ) : 0<e i := by dsimp [e]; omega
  have agree (i : ℕ) (hi : i<N) : z.e i=e i := (max_eq_right (z.edge i hi).1).symm
  apply ordinary_ternary_clock_exclusion (K:=2*K) (x:=z.x) dp (by omega) pos _ _ z.residue
  · intro i hi
    rw [←agree i hi]
    exact (z.edge i hi).2
  · intro i hi
    change i≤N at hi
    have bounds := window_strip (e:=e) (x:=z.x) (m:=z.m) (K:=K) (N:=i)
      z.positive (Nat.le_trans (Nat.mul_le_mul_left K hi) z.room)
      (fun j hj => z.band j (hj.trans hi))
      (fun j hj => by rw [←agree j (by omega)]; exact (z.edge j (by omega)).2)
    refine ⟨bounds.1,?_⟩
    have upper := bounds.2
    push_cast
    linarith only [upper,Nat.cast_nonneg (α:=ℝ) K]

/-- An ordinary forward segment ending in a highly approximated ternary
rational class must leave its height interval at an explicitly bounded depth. -/
theorem effective_ternary_orbit_exit {d K m : ℕ} {A : ℤ} (dp : 0<d) (kp : 0<K)
    (mp : 0<m) (room : K*ternaryWindowPrecision d K A≤m)
    (x e : ℕ → ℕ) (edge : ∀ j,0<e j ∧ 3*x j+1=2^(e j)*x (j+1)) (t : ℕ)
    (congruent : (3:ℤ)^(ternaryWindowPrecision d K A) ∣
      (d:ℤ)*x (t+ternaryWindowPrecision d K A)-A) :
    ∃ j, j≤ternaryWindowPrecision d K A ∧ (x (t+j)<m ∨ K*m<x (t+j)) := by
  let N := ternaryWindowPrecision d K A
  by_contra! stays
  apply effective_ternary_window_exclusion d K A dp kp
  refine ⟨⟨m,fun j => x (t+(N-j)),fun j => e (t+(N-(j+1))),mp,room,
    fun j _ => stays (N-j) (by omega),?_,by simpa [N] using congruent⟩⟩
  intro j hj
  have h := edge (t+(N-(j+1)))
  have eqn : t+(N-(j+1))+1=t+(N-j) := by change j<N at hj; omega
  simpa only [eqn] using h

/-- Every phase of every high bounded-width ordinary cycle excludes both
rational residues at the stated, independently computable precisions. -/
theorem effective_cycle_phase_exclusion (d₂ d₃ K : ℕ) (A₂ A₃ : ℤ)
    (odd : d₂%2=1) (positive : 0<d₃) (kp : 0<K)
    (x e : ℕ → ℕ) (m p : ℕ) (pp : 0<p) (mp : 0<m)
    (room : K*max (dyadicWindowPrecision d₂ K A₂) (ternaryWindowPrecision d₃ K A₃)≤m)
    (band : ∀ j,m≤x j ∧ x j≤K*m)
    (edge : ∀ j,0<e j ∧ 3*x j+1=2^(e j)*x (j+1))
    (period : ∀ j,x (j+p)=x j) (t : ℕ) :
    (¬(2:ℤ)^(dyadicWindowPrecision d₂ K A₂)∣(d₂:ℤ)*x t-A₂) ∧
    (¬(3:ℤ)^(ternaryWindowPrecision d₃ K A₃)∣(d₃:ℤ)*x t-A₃) := by
  let N := ternaryWindowPrecision d₃ K A₃
  constructor
  · intro cong
    obtain ⟨i,_,h⟩ := effective_dyadic_orbit_exit odd kp mp
      ((Nat.mul_le_mul_left K (Nat.le_max_left ..)).trans room) x e edge t cong
    obtain ⟨lo,hi⟩ := band (t+i)
    omega
  · intro cong
    have laps (n : ℕ) : x (t+n*p)=x t := by
      induction n with
      | zero => simp
      | succ n ih => rw [Nat.succ_mul,←Nat.add_assoc,period,ih]
    have enough : N≤N*p := by simpa using Nat.mul_le_mul_left N pp
    let start := t+N*p-N
    have back : x (start+N)=x t := by
      rw [show start+N=t+N*p by dsimp [start]; omega]; exact laps N
    obtain ⟨i,_,h⟩ := effective_ternary_orbit_exit positive kp mp
      ((Nat.mul_le_mul_left K (Nat.le_max_right ..)).trans room) x e edge start (by
        change (3:ℤ)^N ∣ (d₃:ℤ)*x (start+N)-A₃; rwa [back])
    obtain ⟨lo,hi⟩ := band (start+i)
    omega

#print axioms effective_ternary_window_exclusion
#print axioms effective_ternary_orbit_exit
#print axioms effective_cycle_phase_exclusion
end Collatz.Itinerary.HourEscape
