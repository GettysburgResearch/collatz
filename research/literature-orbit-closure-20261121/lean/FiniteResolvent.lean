module

public import Mathlib.Basic.Real.Basic
public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Algebra.BigOperators.Ring.Finset
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Ring

@[expose] public section

/-!
# Finite source-preserving bounds for a quadratic resolvent

Every theorem in this module concerns an explicitly finite sum. In the
clock-lift application, `b j` is actual incoming killed mass at depth `j`,
`S` bounds the original total mass, and `a` is one original surviving atom.
The transport inequality remains an explicit hypothesis; no theorem assumes
or proves a universal Collatz norm improvement.
-/

namespace CollatzFiniteResolvent

open scoped BigOperators

noncomputable def coefficient (j : ℕ) : ℝ := 1 / (((j : ℝ) + 1) * ((j : ℝ) + 2))

noncomputable def growth (j : ℕ) : ℝ := (((j : ℝ) + 1) * ((j : ℝ) + 2)) / 2

theorem coefficient_pos (j : ℕ) : 0 < coefficient j := by
  unfold coefficient
  positivity

theorem growth_nonneg (j : ℕ) : 0 ≤ growth j := by
  unfold growth
  positivity

theorem coefficient_zero : coefficient 0 = 1 / 2 := by
  norm_num [coefficient]

/-- Exact ratio control; the residual numerator factors as
`i*r*(i*r+3*i+3*r+5)`. -/
theorem coefficient_ratio (i r : ℕ) :
    coefficient i ≤ growth r * coefficient (i + r) := by
  have hi : (0 : ℝ) ≤ i := Nat.cast_nonneg i
  have hr : (0 : ℝ) ≤ r := Nat.cast_nonneg r
  have hprod : 0 ≤ (i : ℝ) * r * ((i : ℝ) * r + 3 * i + 3 * r + 5) := by
    positivity
  unfold coefficient growth
  simp only [Nat.cast_add]
  rw [div_mul_div_comm, mul_one]
  apply (div_le_div_iff₀ (by positivity) (by positivity)).2
  nlinarith only [hprod]

/-- The geometric quadratic sum has an exact finite tail. -/
theorem geometric_growth_sum_exact (k : ℕ) :
    (∑ r ∈ Finset.range (k + 1), (1 / 2 : ℝ) ^ r * growth r) +
      (1 / 2 : ℝ) ^ (k + 1) * ((k : ℝ)^2 + 7 * k + 14) = 8 := by
  induction k with
  | zero => norm_num [growth]
  | succ k ih =>
      calc
        (∑ r ∈ Finset.range (k + 1 + 1), (1 / 2 : ℝ) ^ r * growth r) +
            (1 / 2 : ℝ) ^ (k + 1 + 1) *
              (((k + 1 : ℕ) : ℝ)^2 + 7 * (k + 1 : ℕ) + 14) =
            (∑ r ∈ Finset.range (k + 1), (1 / 2 : ℝ) ^ r * growth r) +
              (1 / 2 : ℝ) ^ (k + 1) * ((k : ℝ)^2 + 7 * k + 14) := by
          rw [Finset.sum_range_succ, pow_succ]
          simp only [growth, Nat.cast_add, Nat.cast_one]
          ring
        _ = 8 := ih

theorem geometric_growth_sum_le_eight (k : ℕ) :
    (∑ r ∈ Finset.range (k + 1), (1 / 2 : ℝ) ^ r * growth r) ≤ 8 := by
  have ht : 0 ≤ (1 / 2 : ℝ) ^ (k + 1) * ((k : ℝ)^2 + 7 * k + 14) := by
    positivity
  have he := geometric_growth_sum_exact k
  linarith

noncomputable def budget (b : ℕ → ℝ) (k : ℕ) : ℝ :=
  ∑ r ∈ Finset.range (k + 1), coefficient (k - r) * (1 / 2 : ℝ)^r * b (k - r)

/-- All merger fibers and their original source weights may be included in
`b`; only positivity and the same fixed original mass bound are used. -/
theorem budget_le (b : ℕ → ℝ) (k : ℕ) (S : ℝ)
    (hS : 0 ≤ S)
    (hb : ∀ j ≤ k, 0 ≤ b j ∧ b j ≤ S) :
    budget b k ≤ 8 * coefficient k * S := by
  have hcoef : 0 ≤ coefficient k := le_of_lt (coefficient_pos k)
  calc
    budget b k ≤
        ∑ r ∈ Finset.range (k + 1),
          (coefficient k * S) * ((1 / 2 : ℝ)^r * growth r) := by
      unfold budget
      apply Finset.sum_le_sum
      intro r hr
      have hrk : r ≤ k := Nat.le_of_lt_succ (Finset.mem_range.mp hr)
      have hbr := hb (k - r) (Nat.sub_le k r)
      have hc := coefficient_ratio (k - r) r
      rw [Nat.sub_add_cancel hrk] at hc
      have hpow : 0 ≤ (1 / 2 : ℝ)^r := by positivity
      have hgr : 0 ≤ growth r := growth_nonneg r
      calc
        coefficient (k - r) * (1 / 2 : ℝ)^r * b (k - r) ≤
            (growth r * coefficient k) * (1 / 2 : ℝ)^r * b (k - r) :=
          mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_right hc hpow) hbr.1
        _ ≤ (growth r * coefficient k) * (1 / 2 : ℝ)^r * S :=
          mul_le_mul_of_nonneg_left hbr.2 (by positivity)
        _ = (coefficient k * S) * ((1 / 2 : ℝ)^r * growth r) := by ring
    _ = (coefficient k * S) *
        (∑ r ∈ Finset.range (k + 1), (1 / 2 : ℝ)^r * growth r) := by
      rw [Finset.mul_sum]
    _ ≤ (coefficient k * S) * 8 :=
      mul_le_mul_of_nonneg_left (geometric_growth_sum_le_eight k) (by positivity)
    _ = 8 * coefficient k * S := by ring

/-- The finite clock-slice transport estimate extracts a bound on the mass
of any one fixed surviving source. -/
theorem survivor_atom_bound (b : ℕ → ℝ) (k : ℕ) (S a L : ℝ)
    (hS : 0 ≤ S) (hL : 0 ≤ L)
    (hb : ∀ j ≤ k, 0 ≤ b j ∧ b j ≤ S)
    (ha : a ≤ b k)
    (htransport : coefficient 0 * b k ≤ L * budget b k) :
    a ≤ 16 * L * coefficient k * S := by
  have hupper := mul_le_mul_of_nonneg_left (budget_le b k S hS hb) hL
  rw [coefficient_zero] at htransport
  nlinarith only [hupper, htransport, ha]

/-- Denominator-cleared form, convenient for exact rational certificates. -/
theorem survivor_atom_bound_cleared (b : ℕ → ℝ) (k : ℕ) (S a L : ℝ)
    (hS : 0 ≤ S) (hL : 0 ≤ L)
    (hb : ∀ j ≤ k, 0 ≤ b j ∧ b j ≤ S)
    (ha : a ≤ b k)
    (htransport : coefficient 0 * b k ≤ L * budget b k) :
    (((k : ℝ) + 1) * ((k : ℝ) + 2)) * a ≤ 16 * L * S := by
  have hh := survivor_atom_bound b k S a L hS hL hb ha htransport
  have hd : 0 < ((k : ℝ) + 1) * ((k : ℝ) + 2) := by positivity
  have hh' : a ≤ (16 * L * S) / (((k : ℝ) + 1) * ((k : ℝ) + 2)) := by
    simpa only [coefficient, div_eq_mul_inv, one_mul, mul_assoc, mul_comm,
      mul_left_comm] using hh
  have hm := (le_div_iff₀ hd).mp hh'
  nlinarith only [hm]

/-- A strictly smaller finite norm budget is incompatible with that fixed
atom surviving to this clock. The small budget is an explicit hypothesis. -/
theorem excludes_transport_of_strict_budget
    (b : ℕ → ℝ) (k : ℕ) (S a L : ℝ)
    (hS : 0 ≤ S) (hL : 0 ≤ L)
    (hb : ∀ j ≤ k, 0 ≤ b j ∧ b j ≤ S)
    (ha : a ≤ b k)
    (hsmall : 16 * L * S < (((k : ℝ) + 1) * ((k : ℝ) + 2)) * a) :
    ¬ coefficient 0 * b k ≤ L * budget b k := by
  intro htransport
  have hh := survivor_atom_bound_cleared b k S a L hS hL hb ha htransport
  linarith

/-- Almost constant incoming fibers force the full quadratic norm order,
even when those fibers arise from changing finite terminating sources. -/
theorem norm_floor_of_comparable_fibers
    (b : ℕ → ℝ) (k : ℕ) (C L : ℝ)
    (hC : 0 ≤ C) (hL : 0 ≤ L) (hbk : 0 < b k)
    (hb : ∀ j ≤ k, 0 ≤ b j ∧ b j ≤ C * b k)
    (htransport : coefficient 0 * b k ≤ L * budget b k) :
    growth k ≤ 8 * C * L := by
  have hh := survivor_atom_bound_cleared b k (C * b k) (b k) L
    (mul_nonneg hC (le_of_lt hbk)) hL hb le_rfl htransport
  have hmul : (((k : ℝ) + 1) * ((k : ℝ) + 2)) * b k ≤
      (16 * L * C) * b k := by
    convert hh using 1
    ring
  have hden := (mul_le_mul_iff_left₀ hbk).mp hmul
  unfold growth
  nlinarith only [hden]

theorem coefficient_antitone {i j : ℕ} (hij : i ≤ j) :
    coefficient j ≤ coefficient i := by
  have hij' : (i : ℝ) ≤ j := Nat.cast_le.mpr hij
  unfold coefficient
  apply one_div_le_one_div_of_le (by positivity)
  exact mul_le_mul (by linarith) (by linarith) (by positivity) (by positivity)

/-- A polynomial spatial seed is nearly constant on a sufficiently high
finite interval. This supplies the terminating-shift countermodel. -/
theorem coefficient_shift_bound (y k : ℕ) (hky : k ≤ y) :
    coefficient y ≤ 4 * coefficient (y + k) := by
  have hky' : (k : ℝ) ≤ y := Nat.cast_le.mpr hky
  have hy : (0 : ℝ) ≤ y := Nat.cast_nonneg y
  have hk : (0 : ℝ) ≤ k := Nat.cast_nonneg k
  have hm : ((y : ℝ) + k + 1) * ((y : ℝ) + k + 2) ≤
      (2 * ((y : ℝ) + 1)) * (2 * ((y : ℝ) + 2)) :=
    mul_le_mul (by linarith) (by linarith) (by positivity) (by positivity)
  unfold coefficient
  simp only [Nat.cast_add]
  rw [← mul_div_assoc, mul_one]
  apply (div_le_div_iff₀ (by positivity) (by positivity)).2
  nlinarith only [hm]

/-- For the map `n -> max(n-1,0)`, a nonterminal endpoint `y` has incoming
mass `b_j = coefficient (y+j)` from the unique depth-j ancestor.
Although every source terminates, these finite fibers force a quadratic
clock-resolvent norm. Only the finite fiber statement is formalized here. -/
theorem terminating_shift_fiber_floor (y k : ℕ) (hky : k ≤ y)
    (L : ℝ) (hL : 0 ≤ L)
    (htransport : coefficient 0 * coefficient (y + k) ≤
      L * budget (fun j => coefficient (y + j)) k) :
    growth k ≤ 32 * L := by
  have hb : ∀ j ≤ k,
      0 ≤ coefficient (y + j) ∧ coefficient (y + j) ≤ 4 * coefficient (y + k) := by
    intro j _hj
    constructor
    · exact le_of_lt (coefficient_pos (y + j))
    · exact (coefficient_antitone (Nat.le_add_right y j)).trans
        (coefficient_shift_bound y k hky)
  have hh := norm_floor_of_comparable_fibers
    (fun j => coefficient (y + j)) k 4 L (by norm_num) hL
    (coefficient_pos (y + k)) hb htransport
  nlinarith only [hh]

end CollatzFiniteResolvent
