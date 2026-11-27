import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Algebra.GCDMonoid.Nat
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
Finite integer identities for the odd-step shared-background denominator
argument. The multivariable S-unit estimate and the asymptotic theorem
are written mathematics.
-/

namespace Collatz.SharedBackground

set_option autoImplicit false

/-- Each block has the same odd slope and positive intercept. The
dyadic divisor can vary from block to block. -/
inductive Run (p c : ℕ) : List ℕ → ℕ → ℕ → Prop where
  | nil (x : ℕ) : Run p c [] x x
  | cons {b x y z : ℕ} {bs : List ℕ}
      (edge : b * y = p * x + c) (tail : Run p c bs y z) : Run p c (b :: bs) x z

def markerCarry (p : ℕ) : List ℕ → ℕ
  | [] => 0
  | b :: bs => p ^ bs.length + b * markerCarry p bs

/-- Unrolling a real integer-coordinate run preserves its single common
intercept as an exact factor of the complete carry. -/
theorem unroll {p c x y : ℕ} {bs : List ℕ} (run : Run p c bs x y) :
    bs.prod * y = p ^ bs.length * x + c * markerCarry p bs := by
  induction run with
  | nil x => simp [markerCarry]
  | @cons b x y z bs edge tail ih =>
    simp only [List.prod_cons, List.length_cons, pow_succ, markerCarry]
    calc
      b * bs.prod * z = b * (bs.prod * z) := by ring
      _ = b * (p ^ bs.length * y + c * markerCarry p bs) := by rw [ih]
      _ = p ^ bs.length * (b * y) + b * (c * markerCarry p bs) := by ring
      _ = _ := by rw [edge]; ring

/-- Complete determinant divisibility, retaining the common physical
denominator q in the underlying integer coordinates. -/
theorem closed_divides {p q c x : ℕ} {bs : List ℕ} (run : Run p (q*c) bs x x) :
    bs.prod - p ^ bs.length ∣ q * c * markerCarry p bs := by
  refine ⟨x, ?_⟩
  rw [Nat.sub_mul, unroll run]
  omega

/-- For two shared blocks whose dyadic divisors differ by a factor
u+1, the odd numerator at the start of the shorter block must contain
(p+n) up to the single gcd with u. -/
theorem half_turn_divides {p n u c x y : ℕ} (cop : Nat.Coprime p n)
    (first : n * y = p * x + c) (second : (u+1) * n * x = p * y + c) :
    p+n ∣ (p+n).gcd u * x := by
  have eqn : (p+n) * y = (p+n) * x + n * (u*x) := by
    ring_nf at first second ⊢
    omega
  have dv : p+n ∣ n * (u*x) :=
    (Nat.dvd_add_iff_right (dvd_mul_right (p+n) x)).mpr (eqn ▸ dvd_mul_right (p+n) y)
  have red : p+n ∣ u*x := (Nat.coprime_add_self_left.mpr cop).dvd_of_dvd_mul_left dv
  have bound := gcd_mul_dvd_mul_gcd (p+n) u x
  simp only [gcd_eq_nat_gcd] at bound
  rw [Nat.gcd_eq_left red] at bound
  exact bound.trans (Nat.mul_dvd_mul_left _ (Nat.gcd_dvd_right _ _))

#print axioms unroll
#print axioms closed_divides
#print axioms half_turn_divides

end Collatz.SharedBackground
