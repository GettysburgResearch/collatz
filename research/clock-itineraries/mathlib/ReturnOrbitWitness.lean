module
public import HourEscapeLookback
import all FixedGate
import all EscapeRecords
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.HourEscape
open FixedGate EscapeRecords
set_option autoImplicit false

/-- The exact reduced denominator formula for the fixed point obtained by
periodizing a literal strict-record prefix (PR 201, closing audit, §1). -/
def periodizedDen (a k : ℕ) : ℕ :=
  let D := 3^k-2^(elapsed k a)
  D / D.gcd (after k a-a)

/-- Reducing the literal periodized affine fixed point, with numerator
minus its positive carry and denominator the clock difference, gives the
same gcd as reducing against the change in the ordinary state. -/
theorem periodized_carry_gcd {a q k s C : ℕ} (up : a≤q) (large : 2^s≤3^k)
    (edge : 2^s*q=3^k*a+C) :
    (3^k-2^s).gcd C=(3^k-2^s).gcd (q-a) := by
  let D := 3^k-2^s
  have cop : D.Coprime (2^s) := (Nat.coprime_sub_self_left large).mpr
    (((by decide : Nat.Coprime 3 2).pow_left k).pow_right s)
  have ma : a*D+a*2^s=a*3^k := by rw [←Nat.mul_add]; dsimp [D]; rw [Nat.sub_add_cancel large]
  have mb : 2^s*(q-a)+2^s*a=2^s*q := by rw [←Nat.mul_add,Nat.sub_add_cancel up]
  have balance : C+a*D=2^s*(q-a) := by nlinarith only [ma,mb,edge]
  calc
    _ = D.gcd (C+a*D) := (Nat.gcd_add_mul_right_right D C a).symm
    _ = D.gcd (2^s*(q-a)) := by rw [balance]
    _ = _ := cop.symm.gcd_mul_left_cancel_right _

private theorem ordinary_growth {a : ℕ} {c : Bool} (odd : a%2=1) (color : a%3=digit c)
    (k : ℕ) : 2^k*(after k a+1)≤3^k*(a+1) := by
  induction k with
  | zero => simp [after]
  | succ k ih =>
    have oi := (route_exists k a odd color).choose_spec.2.2.1
    have g := next_gap oi
    let t := (next (after k a)).1
    have min : 2≤2^t := by simpa using Nat.pow_le_pow_right (by decide : 0<2) g.pos
    have nxt : after (k+1) a=(next (after k a)).2 := by rw [after_add]; rfl
    have le := Nat.mul_le_mul_right ((next (after k a)).2) min
    have eqn := g.eqn
    change 2^t*(next (after k a)).2=3*after k a+1 at eqn
    have edge : 2*(after (k+1) a+1)≤3*(after k a+1) := by rw [nxt]; omega
    have one := Nat.mul_le_mul_left (2^k) edge
    have two := Nat.mul_le_mul_left 3 ih
    rw [Nat.pow_succ,Nat.pow_succ]
    nlinarith only [one,two]

/-- Along records of one fixed ordinary source, even the *reduced* denominator
of the periodized exact moving witness grows at least exponentially in the
odd-step count. The earlier record fixes every factor on the right except
the denominator itself. -/
theorem periodized_denominator_exponential {a h k : ℕ} {c : Bool}
    (odd : a%2=1) (color : a%3=digit c) (hp : 0<h) (later : h<k)
    (first : Critical a h) (last : Critical a k) :
    2^k≤3^h*(a+1)*periodizedDen a k := by
  let q := after k a
  let D := 3^k-2^(elapsed k a)
  let g := D.gcd (q-a)
  let d := periodizedDen a k
  have prior : 2^(elapsed h a)<3^h := by simpa [elapsed] using first 0 hp
  have pr : 2^(elapsed k a)<3^k := by simpa [elapsed] using last 0 (by omega : 0<k)
  have comp := last h later
  have ga : 3^k≤3^h*D := by
    dsimp [D]
    rw [Nat.mul_sub]
    have h₁ := Nat.mul_le_mul_left (3^k) (Nat.succ_le_of_lt prior)
    rw [Nat.mul_comm (2^(elapsed k a)) (3^h)] at comp
    rw [Nat.mul_succ] at h₁
    rw [Nat.mul_comm (3^h) (3^k)]
    omega
  have aq : a<q := by simpa [q,after] using critical_height odd color last (i:=0) (by omega)
  have gq : g≤q-a := Nat.le_of_dvd (by omega) (Nat.gcd_dvd_right D (q-a))
  have recov : g*d=D := Nat.mul_div_cancel' (Nat.gcd_dvd_left D (q-a))
  have height := ordinary_growth odd color k
  have small : 2^k*g≤3^k*(a+1) := (Nat.mul_le_mul_left _ (show g≤q+1 by omega)).trans height
  apply Nat.le_of_mul_le_mul_right (c:=3^k) _ (Nat.pow_pos (by decide))
  calc
    _ ≤ 2^k*(3^h*D) := Nat.mul_le_mul_left _ ga
    _ = (3^h*d)*(2^k*g) := by rw [←recov]; ring
    _ ≤ (3^h*d)*(3^k*(a+1)) := Nat.mul_le_mul_left _ small
    _ = _ := by change _=(3^h*(a+1)*d)*3^k; ring

#print axioms periodized_denominator_exponential
#print axioms periodized_carry_gcd
end Collatz.Itinerary.HourEscape
