/-
Finite arithmetic consumers for the all-template selection investigation.
The global two-power gap is a WRITTEN consequence of Matveev plus an exact
continued-fraction certificate. It is not assumed as a custom axiom here.
The inequalities below remain explicit hypotheses of these finite results.
-/
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum
import AdaptiveLattice

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzTemplateSelection
open CollatzLatticeDescent CollatzAdaptiveLattice

/-- The maximum-carry inequality and the cleared two-power gap bound the
complete carry; no structural factor cancellation occurs. -/
theorem carry_gap_bound (m P Q D C : Int)
    (hm : 0 < m) (hQ : 0 < Q)
    (carry : m*C ≤ Q*(P-m))
    (gap : 3*(P-m) < 2*m*D) : 3*C < 2*Q*D := by
  have h := mul_lt_mul_of_pos_left gap hQ
  by_contra bad
  have back := mul_le_mul_of_nonneg_left (le_of_not_gt bad) hm.le
  nlinarith

/-- Passing to a reduced or unreduced positive denominator preserves the
strict real center bound once its exact fixed-point equation is retained. -/
theorem fixed_center_bound (D Q C d c : Int)
    (hD : 0 < D) (hd : 0 < d)
    (fixed : d*C = D*c) (carry : 3*C < 2*Q*D) :
    3*c < 2*Q*d := by
  have h := mul_lt_mul_of_pos_left carry hd
  by_contra bad
  have back := mul_le_mul_of_nonneg_left (le_of_not_gt bad) hD.le
  nlinarith

/-- Once the complete carry bound is known, every actual contracting
prefix in the displayed native binary window strictly descends. -/
theorem contracting_window_descent (P Q C x y : Int)
    (hQ : 0 < Q) (contracting : P < Q)
    (carry : 3*C < 2*Q*(Q-P)) (window : 2*Q ≤ 3*x)
    (edge : Q*y=P*x+C) : y < x := by
  have weighted := mul_le_mul_of_nonneg_right window (show 0 ≤ Q-P by omega)
  by_contra bad
  have above := mul_le_mul_of_nonneg_left (le_of_not_gt bad) hQ.le
  nlinarith

/-- Primitivity prevents a nonintegral rational center from being an
ordinary integer source, so the nonzero source lattice is available. -/
theorem primitive_displacement_ne_zero (d x : Nat) (c : Int)
    (hd : 1 < d) (primitive : Nat.Coprime d c.natAbs) :
    (d:Int)*x-c ≠ 0 := by
  intro zero
  have dvd : (d:Int) ∣ c := ⟨x, by omega⟩
  have ndvd : d ∣ c.natAbs := Int.ofNat_dvd_left.mp dvd
  have hg : Nat.gcd d c.natAbs = d := Nat.gcd_eq_left ndvd
  have hp : Nat.gcd d c.natAbs = 1 := primitive
  omega

/-- For a center below 2Q/3, odd nonintegral denominators (hence d>=3)
and the actual source lattice exclude every sub-height displacement. -/
theorem nonintegral_rank_above_source (Q d x : Nat) (c : Int)
    (hd : 3 ≤ d) (nonzero : (d:Int)*x-c ≠ 0)
    (lattice : (Q:Int) ∣ (d:Int)*x-c)
    (center : 3*c < 2*(Q:Int)*d) :
    x < ((d:Int)*x-c).natAbs := by
  by_cases high : Q ≤ x
  · have qx : (Q:Int) ≤ x := by exact_mod_cast high
    have d3 : (3:Int) ≤ d := by exact_mod_cast hd
    have one := mul_le_mul_of_nonneg_right qx (show 0 ≤ (2:Int)*d by positivity)
    have two := mul_le_mul_of_nonneg_right d3 (show 0 ≤ (x:Int) by positivity)
    have signed : (x:Int) < (d:Int)*x-c := by nlinarith
    have absolute : (d:Int)*x-c ≤ ((((d:Int)*x-c).natAbs:Nat):Int) := Int.le_natAbs
    omega
  · have lower := lattice_size Q ((d:Int)*x-c) (by omega) nonzero lattice
    omega

/-- Literal ordinary prefix supplies the lattice needed by every consumer. -/
theorem ordinary_anchor_lattice (u : List Bool) (d x : Nat) (c y : Int)
    (fixed : (d:Int)*wordCarry u =
      (((2^u.length:Nat):Int)-wordMultiplier u)*c)
    (trace : WordTrace u x y) :
    (((2^u.length:Nat):Int)) ∣ (d:Int)*x-c := by
  have run : Repeat (wordMultiplier u) (2^u.length) (wordCarry u) 1 x y :=
    ⟨y, word_affine u x y trace, rfl⟩
  have h := anchor_lattice (wordMultiplier u) (2^u.length)
    (wordCarry u) d c x y 1 (word_coprime u) fixed run
  simpa using h

/-- The complete ordinary nonintegral-template consumer. The real center
estimate imported from the written gap argument is an explicit hypothesis. -/
theorem ordinary_nonintegral_rank_above_source
    (u : List Bool) (d x : Nat) (c y : Int)
    (hd : 3 ≤ d) (primitive : Nat.Coprime d c.natAbs)
    (fixed : (d:Int)*wordCarry u =
      (((2^u.length:Nat):Int)-wordMultiplier u)*c)
    (trace : WordTrace u x y)
    (center : 3*c < 2*(((2^u.length:Nat):Int))*d) :
    x < ((d:Int)*x-c).natAbs := by
  exact nonintegral_rank_above_source (2^u.length) d x c hd
    (primitive_displacement_ne_zero d x c (by omega) primitive)
    (ordinary_anchor_lattice u d x c y fixed trace) center

/-- All nonzero templates capable of meeting score M have a finite word
horizon, independently of their rational denominator. -/
theorem finite_template_horizon (u : List Bool) (d x M : Nat) (c y : Int)
    (fixed : (d:Int)*wordCarry u =
      (((2^u.length:Nat):Int)-wordMultiplier u)*c)
    (trace : WordTrace u x y) (nonzero : (d:Int)*x-c ≠ 0)
    (score : ((d:Int)*x-c).natAbs ≤ M) : 2^u.length ≤ M := by
  have lattice := ordinary_anchor_lattice u d x c y fixed trace
  exact (lattice_size (2^u.length) ((d:Int)*x-c)
    (Nat.pow_pos (by decide)) nonzero lattice).trans score

theorem word_multiplier_bound (u : List Bool) : wordMultiplier u ≤ 3^u.length := by
  induction u with
  | nil => simp [wordMultiplier]
  | cons b bs ih =>
      cases b <;> simp only [wordMultiplier, Bool.false_eq_true, ite_false,
        ite_true, List.length_cons, Nat.pow_succ, one_mul] <;> omega

theorem word_carry_bound (u : List Bool) : wordCarry u < 3^u.length := by
  induction u with
  | nil => simp [wordCarry]
  | cons b bs ih =>
      have bound := word_multiplier_bound bs
      cases b <;> simp only [wordCarry, Bool.false_eq_true, ite_false,
        ite_true, List.length_cons, Nat.pow_succ, mul_zero, mul_one,
        zero_add] <;> omega

/-- Primitive reduction gives |c|<=C. Together with the finite horizon,
this proves an explicit finite sublevel bound for the optimized rank. -/
theorem template_sublevel_height (u : List Bool) (d x M K : Nat) (c : Int)
    (hd : 0 < d) (reduced : c.natAbs ≤ wordCarry u)
    (score : ((d:Int)*x-c).natAbs ≤ M) (horizon : u.length ≤ K) :
    x < M+3^K := by
  have carry := (word_carry_bound u).trans_le
    (Nat.pow_le_pow_right (by decide : 0 < 3) horizon)
  have triangle := Int.natAbs_add_le ((d:Int)*x-c) c
  simp only [sub_add_cancel, Int.natAbs_mul, Int.natAbs_natCast] at triangle
  have dx : x ≤ d*x := by nlinarith
  omega

/-- A supplied complete word x->1 automatically pays one changing-center
macro, after padding the exceptional word 2->1 if necessary. -/
theorem terminal_word_paid (P Q x C : Int)
    (hp : 1 ≤ P) (hx : 2 ≤ x) (hq : 2 < Q) (hc : 0 ≤ C)
    (terminal : Q=P*x+C) :
    P+|C-(Q-P)| = P*x ∧ P*x ≤ Q ∧ Q < Q*(Q-P) := by
  have d : 2 ≤ Q-P := by nlinarith
  have carry : C-(Q-P) = -P*(x-1) := by nlinarith
  have negative : C-(Q-P) ≤ 0 := by nlinarith
  rw [abs_of_nonpos negative]
  constructor
  · nlinarith
  constructor
  · omega
  · nlinarith

theorem terminal_source_rank (P Q x C : Int) (terminal : Q=P*x+C) :
    (Q-P)*x-C=Q*(x-1) := by nlinarith

end CollatzTemplateSelection

#print axioms CollatzTemplateSelection.carry_gap_bound
#print axioms CollatzTemplateSelection.fixed_center_bound
#print axioms CollatzTemplateSelection.contracting_window_descent
#print axioms CollatzTemplateSelection.primitive_displacement_ne_zero
#print axioms CollatzTemplateSelection.nonintegral_rank_above_source
#print axioms CollatzTemplateSelection.ordinary_anchor_lattice
#print axioms CollatzTemplateSelection.ordinary_nonintegral_rank_above_source
#print axioms CollatzTemplateSelection.finite_template_horizon
#print axioms CollatzTemplateSelection.word_multiplier_bound
#print axioms CollatzTemplateSelection.word_carry_bound
#print axioms CollatzTemplateSelection.template_sublevel_height
#print axioms CollatzTemplateSelection.terminal_word_paid
#print axioms CollatzTemplateSelection.terminal_source_rank
