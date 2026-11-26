module
public import ReturnOrbitBinary
import all ReturnOrbitBinary
import all HourEscapeBinaryWindows
import all HourEscapeBinary
import all HourEscapeDrawdown
import all HourCycleShadow
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.HourEscape
open Collatz.HourCycleShadow
set_option autoImplicit false

/-- Uniform dyadic precision for ordinary windows of physical width K. -/
def dyadicWindowPrecision (d K : ℕ) (A : ℤ) : ℕ :=
  (3*K+2)*(rationalHorizon d (2*K) A+1)

/-- At every ordinary positive starting phase, congruence to the rational
numerator at the explicit precision forces the orbit out of the indicated
height interval. No assumption on cycles, divergence or the gap alphabet. -/
theorem effective_dyadic_window_exclusion (d K : ℕ) (A : ℤ) (odd : d%2=1)
    (kp : 0<K) : ¬Nonempty (ForwardWindow d A K (dyadicWindowPrecision d K A)) := by
  rintro ⟨z⟩
  let T := rationalHorizon d (2*K) A
  let N := dyadicWindowPrecision d K A
  have fits : T+1≤N := by
    have one : 1≤3*K+2 := by omega
    simpa only [Nat.one_mul,N,dyadicWindowPrecision,T] using Nat.mul_le_mul_right (T+1) one
  let e := fun i => max 1 (z.e i)
  have ep (i : ℕ) : 0<e i := by dsimp [e]; omega
  have agree (i : ℕ) (hi : i<N) : e i=z.e i := by
    exact max_eq_right (z.edge i hi).1
  have step (i : ℕ) (hi : i<N) : 3*z.x i+1=2^(e i)*z.x (i+1) := by
    rw [agree i hi]; exact (z.edge i hi).2
  have gap (i : ℕ) (hi : i<N) : e i≤3*K+2 := by
    have physics := step i hi
    have p := z.positive
    have l := Nat.mul_le_mul_left (2^(e i)) (z.band (i+1) (by change i+1≤N; omega)).1
    have r := Nat.mul_le_mul_left 3 (z.band i hi.le).2
    rw [←physics] at l
    have scaled : 2^(e i)*z.m≤(3*K+1)*z.m := by
      rw [Nat.add_mul,Nat.one_mul,Nat.mul_assoc]; omega
    have h := Nat.le_of_mul_le_mul_right scaled p
    have growth := Nat.lt_two_pow_self (n:=e i)
    omega
  have clock (k : ℕ) (hk : k≤T+1) : prefixSum e k≤(3*K+2)*k := by
    induction k with
    | zero => simp [prefixSum]
    | succ k ih =>
      have l := ih (by omega)
      have r := gap k (by omega)
      rw [prefixSum,Nat.mul_succ]; omega
  have digits (k : ℕ) (hk : k≤T+1) :
      (2:ℤ)^(prefixSum e k)∣3^k*A+(d:ℤ)*forwardCarry e k := by
    have bound : prefixSum e k≤N := (clock k hk).trans (Nat.mul_le_mul_left _ hk)
    obtain ⟨c,hc⟩ := dvd_trans (pow_dvd_pow (2:ℤ) bound) z.residue
    have physical := affine_forward (n:=k) (x:=z.x) (e:=e) (fun i hi => step i (by omega))
    refine ⟨(d:ℤ)*(z.x k:ℤ)-3^k*c,?_⟩
    linear_combination -(d:ℤ)*physical-(3:ℤ)^k*hc
  let y := fun k => if hk : k≤T+1 then Classical.choose (digits k hk) else 0
  have rep (k : ℕ) (hk : k≤T+1) :
      3^k*A+(d:ℤ)*forwardCarry e k=2^(prefixSum e k)*y k := by
    simpa only [y,dite_eq_left hk] using Classical.choose_spec (digits k hk)
  have y0 : y 0=A := by simpa [prefixSum,forwardCarry] using (rep 0 (by omega)).symm
  have path (i : ℕ) (hi : i<T+1) : (2:ℤ)^(e i)*y (i+1)=3*y i+d := by
    have small := rep i (by omega)
    have large := rep (i+1) (by omega)
    rw [prefixSum,pow_add (2:ℤ),forwardCarry,pow_succ (3:ℤ) i] at large
    apply mul_left_cancel₀ (by positivity : (2:ℤ)^(prefixSum e i)≠0)
    linear_combination 3*small-large
  apply finite_dyadic_rational_rigidity (d:=d) (K:=2*K) (y:=y) (by omega) (by omega) ep
  · rw [y0]; exact fun i hi => path i (by omega)
  · rw [y0]; intro i hi
    obtain ⟨r,eqn⟩ := Nat.exists_eq_add_of_le (show 1≤e i from ep i)
    have rel := path i (by change i≤T at hi; omega)
    rw [eqn,pow_add] at rel
    have h : 2*(2^r*y (i+1))=3*y i+d := by simpa only [pow_one,mul_assoc] using rel
    have dc : (d:ℤ)%2=1 := by exact_mod_cast odd
    omega
  · rw [y0]; intro i hi
    let ex := fun j => e (i-(j+1))
    let xx := fun j => z.x (i-j)
    have edge (j : ℕ) (hj : j < i) : 3*xx (j+1)+1=2^(ex j)*xx j := by
      have g := step (i-(j+1)) (by change i≤T at hi; omega)
      rw [show i-(j+1)+1=i-j by omega] at g
      exact g
    have bounds := window_strip (e:=ex) (x:=xx) (m:=z.m) (K:=K) (N:=i)
      z.positive (Nat.le_trans (Nat.mul_le_mul_left K (by change i≤N; change i≤T at hi; omega)) z.room)
      (fun j hj => z.band (i-j) (by change i-j≤N; change i≤T at hi; omega)) edge
    change 1≤((2*K:ℕ):ℝ)*weight (fun j => e (i-(j+1))) i ∧
      weight (fun j => e (i-(j+1))) i≤K at bounds
    rw [reverse_weight] at bounds
    refine ⟨bounds.1,?_⟩
    have high := bounds.2
    push_cast
    linarith only [high,Nat.cast_nonneg (α:=ℝ) K]

/-- Quantitative escape of a finite positive orbit from a prescribed height
strip at any starting phase with the required dyadic rational approximation. -/
theorem effective_dyadic_orbit_exit {d K m : ℕ} {A : ℤ} (odd : d%2=1) (kp : 0<K)
    (mp : 0<m) (room : K*dyadicWindowPrecision d K A≤m)
    (x e : ℕ → ℕ) (edge : ∀ j,0<e j ∧ 3*x j+1=2^(e j)*x (j+1)) (t : ℕ)
    (congruent : (2:ℤ)^(dyadicWindowPrecision d K A)∣(d:ℤ)*x t-A) :
    ∃ j, j≤dyadicWindowPrecision d K A ∧ (x (t+j)<m ∨ K*m<x (t+j)) := by
  by_contra! stays
  apply effective_dyadic_window_exclusion d K A odd kp
  exact ⟨⟨m,fun j => x (t+j),fun j => e (t+j),mp,room,fun j hj => stays j hj,
    fun j _ => edge (t+j),by simpa using congruent⟩⟩

#print axioms effective_dyadic_window_exclusion
#print axioms effective_dyadic_orbit_exit

/-- On one fixed injective ordinary orbit, a multiplicative height strip
must be left even when its lower endpoint is too small for the geometric
estimate. Distinct sites then exhaust the strip directly. -/
theorem simple_dyadic_orbit_exit {d K m : ℕ} {A : ℤ} (odd : d%2=1) (kp : 0<K)
    (mp : 0<m) (x e : ℕ → ℕ) (simple : Function.Injective x)
    (edge : ∀ j,0<e j ∧ 3*x j+1=2^(e j)*x (j+1)) (t : ℕ)
    (congruent : (2:ℤ)^(dyadicWindowPrecision d K A)∣(d:ℤ)*x t-A) :
    ∃ j, j≤(K^2+1)*dyadicWindowPrecision d K A ∧ (x (t+j)<m ∨ K*m<x (t+j)) := by
  let N := dyadicWindowPrecision d K A
  let B := (K^2+1)*N
  have nb : N≤B := by dsimp [B]; rw [Nat.add_mul,Nat.one_mul]; omega
  by_cases high : K*N≤m
  · obtain ⟨j,hj,exit⟩ := effective_dyadic_orbit_exit odd kp mp high x e edge t congruent
    exact ⟨j,hj.trans nb,exit⟩
  · by_contra! all
    have count (i : Fin (B+1)) : x (t+i.val)<K*m+1 := by
      have h := (all i.val (by change i.val≤B; omega)).2
      omega
    let enc := fun i : Fin (B+1) => (⟨x (t+i.val),count i⟩ : Fin (K*m+1))
    have inj : Function.Injective enc := by
      intro i j eqn
      have same : x (t+i.val)=x (t+j.val) := congrArg Fin.val eqn
      exact Fin.ext (Nat.add_left_cancel (simple same))
    have bound := Fintype.card_le_of_injective enc inj
    simp only [Fintype.card_fin] at bound
    have sl := Nat.mul_lt_mul_of_pos_left (Nat.lt_of_not_ge high) kp
    dsimp only [B] at bound
    nlinarith only [bound,sl,Nat.zero_le N]

#print axioms simple_dyadic_orbit_exit
end Collatz.Itinerary.HourEscape
