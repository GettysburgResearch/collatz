module

public import Mathlib.Algebra.Group.Commute.Basic
public import Mathlib.Algebra.Order.Ring.Int
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
Finite kernel statements and unchanged proofs from PR 191, commit
37b3916633cd32a0c173b20bb18ec3a7ec290a63, in Lean module mode.
The cyclic extremum selection, cyclotomic determinant, and full ordinary
parity attachment are supplied separately in the written proof.
-/

@[expose] public section

namespace Collatz.TwoSidedPacking

/-- The two actual edges into a cyclic minimum and maximum suffice. -/
theorem cycle_spread_bound
    (N M d lo hi cmin cmax u v cu cv : ℤ)
    (hM : 0 ≤ M) (hd : 0 ≤ d)
    (hu : lo ≤ u) (hv : v ≤ hi)
    (hcu : cmin ≤ cu) (hcv : cv ≤ cmax)
    (edgeLo : N * lo = M * u + d * cu)
    (edgeHi : N * hi = M * v + d * cv) :
    (N-M)*(hi-lo) ≤ d*(cmax-cmin) := by
  have h1 := mul_le_mul_of_nonneg_left hu hM
  have h2 := mul_le_mul_of_nonneg_left hv hM
  have h3 := mul_le_mul_of_nonneg_left hcu hd
  have h4 := mul_le_mul_of_nonneg_left hcv hd
  nlinarith only [h1,h2,h3,h4,edgeLo,edgeHi]

/-- Consecutive sorted distinct numerators in a G-lattice cost at
least G each. The finite ordering is a separate consumer. -/
theorem lattice_step (G x y z : ℤ) (hG : 0 < G)
    (hxy : x < y) (hz : y-x = G*z) : G ≤ y-x := by
  have hzpos : 0 < z := by
    by_contra! hn
    have hprod := mul_nonpos_of_nonneg_of_nonpos (le_of_lt hG) hn
    linarith only [hxy,hz,hprod]
  have hz1 : 1 ≤ z := by omega
  have hh := mul_le_mul_of_nonneg_left hz1 (le_of_lt hG)
  nlinarith only [hh,hz]

theorem spaced_span (G : ℤ) (x : ℕ → ℤ) (r : ℕ)
    (h : ∀ i < r, G ≤ x (i+1)-x i) :
    G*(r : ℤ) ≤ x r-x 0 := by
  induction r with
  | zero => simp
  | succ r ih =>
    have hp : ∀ i < r, G ≤ x (i+1)-x i := by
      intro i hi
      exact h i (Nat.lt_trans hi (Nat.lt_succ_self r))
    have hprev := ih hp
    have hlast := h r (Nat.lt_succ_self r)
    rw [Nat.cast_succ]
    nlinarith only [hprev,hlast]

/-- Exact cancellation of the common binary/ternary lattice factor. -/
theorem denominator_packing_core (D G d delta span : ℤ) (r : ℕ)
    (hD : 0 ≤ D) (hG : 0 < G)
    (hspan : G*(r : ℤ) ≤ span)
    (hcarry : D*span ≤ d*G*delta) :
    D*(r : ℤ) ≤ d*delta := by
  have hh := mul_le_mul_of_nonneg_left hspan hD
  have hc : G*(D*(r : ℤ)) ≤ G*(d*delta) := by
    nlinarith only [hh,hcarry]
  by_contra! hbad
  have hstrict := mul_lt_mul_of_pos_left hbad hG
  linarith only [hc,hstrict]

/-- Common prefix and suffix cancel exactly from carry differences. -/
theorem composed_carry_difference
    (Mmid Msuf Npre Nmid Cpre Cmid1 Cmid2 Csuf : ℤ) :
    (Mmid*Msuf*Cpre+Npre*Msuf*Cmid1+Npre*Nmid*Csuf) -
    (Mmid*Msuf*Cpre+Npre*Msuf*Cmid2+Npre*Nmid*Csuf) =
    Npre*Msuf*(Cmid1-Cmid2) := by ring

/-- Integer-coordinate shadow of the L block. -/
theorem shadow_L (q r y z : ℤ)
    (edge : 8*r=9*q+7)
    (hq : 83*y=60*q+5) (hr : 83*z=60*r+5) :
    8*z=9*y+5 := by omega

/-- Integer-coordinate shadow of the P block. -/
theorem shadow_P (q r y z : ℤ)
    (edge : 32*r=9*q+5)
    (hq : 83*y=60*q+5) (hr : 83*z=60*r+5) :
    32*z=9*y+5 := by omega

theorem shadow_smaller_odd (q y : ℤ) (hq : 0 < q)
    (hy : 83*y=60*q+5) : 0 < y ∧ 4*y<3*q+1 ∧ y%2=1 := by
  omega

theorem shadow_exists (q : ℤ) (h : ∃ k : ℤ, q+7=83*k) :
    ∃ y : ℤ, 83*y=60*q+5 := by
  obtain ⟨k,hk⟩ := h
  exact ⟨60*k-5, by omega⟩

theorem shifted83_L (q r : ℤ) (edge : 8*r=9*q+7)
    (h : 83 ∣ q+7) : 83 ∣ r+7 := by omega

theorem shifted83_P (q r : ℤ) (edge : 32*r=9*q+5)
    (h : 83 ∣ q+7) : 83 ∣ r+7 := by omega

/-- Full odd endpoints of either shadow block force its first gap
to be exactly one. The next quotient is the literal odd endpoint. -/
theorem shadow_first_gap (y z N : ℤ)
    (hN : N=8 ∨ N=32) (hy : y%2=1) (hz : z%2=1)
    (h : N*z=9*y+5) :
    (3*y+1)%4=2 ∧ ∃ mid : ℤ,
      2*mid=3*y+1 ∧ mid%2=1 ∧ N*z=2*(3*mid+1) := by
  rcases hN with hN | hN
  · subst N
    refine ⟨by omega, (3*y+1)/2, ?_, ?_, ?_⟩ <;> omega
  · subst N
    refine ⟨by omega, (3*y+1)/2, ?_, ?_, ?_⟩ <;> omega

/-- Finite Bezout torus identity for the noncoprime norm.
Use x,y as units modulo the full cyclotomic gcd, not a field. -/
theorem bezout_torus {G : Type*} [CommGroup G]
    (x y : G) (a b u v : ℤ) (h : b*u-a*v=1) :
    (x^u*y^(-v))^b=x*(x^a*y^(-b))^v ∧
    (x^u*y^(-v))^a=y*(x^a*y^(-b))^u := by
  have h1 : u*b=1+a*v := by nlinarith only [h]
  have h2 : (-v)*b=(-b)*v := by ring
  have h3 : u*a=a*u := by ring
  have h4 : (-v)*a=1+(-b)*u := by nlinarith only [h]
  constructor
  · simp only [mul_zpow, ← zpow_mul, h1, h2, zpow_add, zpow_one, mul_assoc]
  · simp only [mul_zpow, ← zpow_mul, h3, h4, zpow_add, zpow_one]
    ac_rfl

#print axioms cycle_spread_bound
#print axioms lattice_step
#print axioms spaced_span
#print axioms denominator_packing_core
#print axioms composed_carry_difference
#print axioms shadow_L
#print axioms shadow_P
#print axioms shadow_smaller_odd
#print axioms shadow_exists
#print axioms shifted83_L
#print axioms shifted83_P
#print axioms shadow_first_gap
#print axioms bezout_torus

end Collatz.TwoSidedPacking
