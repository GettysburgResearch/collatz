import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-! Finite integer identities for positive rational Collatz cycles, with
the reduced denominator retained explicitly in the odd-edge equation. -/
set_option autoImplicit false
namespace Collatz.DenominatorBudget

def clock (g : Nat → Nat) : Nat → Nat
  | 0 => 0
  | k+1 => clock g k + g k

def prod (f : Nat → Nat) : Nat → Nat
  | 0 => 1
  | k+1 => prod f k * f k

private theorem prod_pos {f : Nat → Nat} {k : Nat}
    (hf : ∀ i, i<k → 0<f i) : 0<prod f k := by
  induction k with
  | zero => simp [prod]
  | succ k ih =>
    exact Nat.mul_pos (ih (fun i hi => hf i (by omega))) (hf k (by omega))

/-- Telescoping before closing preserves both ordinary endpoints. -/
theorem product_path (n g : Nat → Nat) (d k : Nat)
    (edges : ∀ i, i<k → 2^(g i)*n (i+1)=3*n i+d) :
    2^(clock g k)*n k*prod n k =
      n 0*prod (fun i => 3*n i+d) k := by
  induction k with
  | zero => simp [clock,prod]
  | succ k ih =>
    have prev := ih (fun i hi => edges i (by omega))
    simp only [clock,prod,pow_add]
    calc
      _ = (2^(clock g k)*n k*prod n k)*(2^(g k)*n (k+1)) := by ring
      _ = _ := by rw [prev,edges k (by omega), Nat.mul_assoc]

/-- The ordinary positive cycle gives this exact multiplicative budget. -/
theorem product_lap (n g : Nat → Nat) (d k : Nat)
    (edges : ∀ i, i<k → 2^(g i)*n (i+1)=3*n i+d)
    (closed : n k=n 0) (positive : 0<n 0) :
    2^(clock g k)*prod n k=prod (fun i => 3*n i+d) k := by
  apply Nat.eq_of_mul_eq_mul_left positive
  calc
    n 0*(2^(clock g k)*prod n k) = 2^(clock g k)*n k*prod n k := by rw [closed]; ring
    _ = _ := product_path n g d k edges

/-- Entrywise lower bounds on positive numerators yield an upper bound on
the full correction product, with all denominators cleared. -/
theorem product_comparison (n u : Nat → Nat) (d k : Nat)
    (lower : ∀ i, i<k → u i≤n i) :
    prod (fun i => 3*n i+d) k * prod u k ≤
      prod (fun i => 3*u i+d) k * prod n k := by
  induction k with
  | zero => simp [prod]
  | succ k ih =>
    have prev := ih (fun i hi => lower i (by omega))
    have last : (3*n k+d)*u k≤(3*u k+d)*n k := by
      have hd := Nat.mul_le_mul_left d (lower k (by omega))
      calc
        _ = (3*n k*u k) + d*u k := by ring
        _ ≤ (3*n k*u k) + d*n k := Nat.add_le_add_left hd _
        _ = _ := by ring
    simp only [prod]
    calc
      _ = (prod (fun i => 3*n i+d) k*prod u k)*((3*n k+d)*u k) := by ring
      _ ≤ _ := Nat.mul_le_mul prev last
      _ = _ := by ring

/-- The inputs may be sorted or concatenated across several disjoint cycles.
Only their total exact product identity and the supplied pointwise floors enter. -/
theorem packed_clock (n u : Nat → Nat) (d k A : Nat)
    (identity : 2^A*prod n k = prod (fun i => 3*n i+d) k)
    (positive : ∀ i, i<k → 0<n i)
    (lower : ∀ i, i<k → u i≤n i) :
    2^A*prod u k ≤ prod (fun i => 3*u i+d) k := by
  have result := product_comparison n u d k lower
  rw [← identity] at result
  have regroup : 2^A*prod u k*prod n k ≤ prod (fun i => 3*u i+d) k*prod n k := by
    calc
      _ = (2^A*prod n k)*prod u k := by ring
      _ ≤ _ := result
  exact Nat.le_of_mul_le_mul_right regroup (prod_pos positive)

/-- At any signed affine cut, every divisor of the clock gap divides the
carry exactly when it divides the endpoint difference. The Bézout identity
is available for the coprime power clocks used by the shortcut map. -/
theorem center_divisor_iff (U V C x y t a b : Int)
    (edge : U*y=V*x+C) (bezout : a*U+b*(U-V)=1)
    (clockDivisor : t ∣ U-V) : t ∣ C ↔ t ∣ y-x := by
  obtain ⟨s, hs⟩ := clockDivisor
  have carry : C = (U-V)*x+U*(y-x) := by
    calc
      C = U*y-V*x := by omega
      _ = _ := by ring
  constructor
  · rintro ⟨z, hz⟩
    refine ⟨a*(z-s*x)+b*s*(y-x), ?_⟩
    calc
      y-x = (a*U+b*(U-V))*(y-x) := by rw [bezout]; ring
      _ = a*(C-(U-V)*x)+b*(U-V)*(y-x) := by rw [carry]; ring
      _ = t*(a*(z-s*x)+b*s*(y-x)) := by rw [hz,hs]; ring
  · rintro ⟨z, hz⟩
    exact ⟨s*x+U*z, by rw [carry,hs,hz]; ring⟩

/-- A common divisor of two nested clock gaps divides the gap on the
intervening interval, independently of the signs and all carries. -/
theorem nested_clock_divisor (U V W Z t a b : Int)
    (bezout : a*W+b*(W-Z)=1) (longGap : t ∣ U*W-V*Z)
    (shortGap : t ∣ W-Z) : t ∣ U-V := by
  exact (center_divisor_iff W Z (U*W-V*Z) V U t a b
    (by ring) bezout shortGap).mp longGap

/-- The carry of an earlier suffix reduced against a later clock gap. -/
theorem earlier_carry_residue (U V W Z d C m n : Int)
    (edge : d*C=U*W*m-V*Z*n) :
    d*C-W*(U*m-V*n)=(W-Z)*V*n := by
  rw [edge]
  ring

/-- The carry of a later suffix reduced against an earlier clock gap. -/
theorem later_carry_residue (U V W Z d C m n : Int)
    (edge : d*C=W*m-Z*n) :
    U*(d*C)-Z*(V*m-U*n)=(U*W-V*Z)*m := by
  rw [edge]
  ring

#print axioms product_path
#print axioms product_lap
#print axioms product_comparison
#print axioms packed_clock
#print axioms center_divisor_iff
#print axioms nested_clock_divisor
#print axioms earlier_carry_residue
#print axioms later_carry_residue
end Collatz.DenominatorBudget
