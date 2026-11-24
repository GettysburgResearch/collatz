module

public import Mathlib.Algebra.BigOperators.Group.Finset.Basic
public import Mathlib.Tactic.GCongr
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring

public section

/-! The optimal centered carry inequality, with a sharp charge at every strict edge. -/
namespace Collatz.StrictCarry

set_option autoImplicit false

/-- The two kinds of edge on which the optimal power estimate is an equality. -/
def strictEdge (c d : ℕ) : ℕ := if (c = 0 ∧ d = 0) ∨ d = 3*c+2 then 0 else 1

private theorem succ_le_three_pow (c : ℕ) : c+1 ≤ 3^c := by
  induction c with
  | zero => simp
  | succ c ih =>
    rw [pow_succ]
    omega

private theorem up_pow {i j : ℕ} (h : i ≤ j) : 3^i ≤ 3^j :=
  Nat.pow_le_pow_right (by decide) h

/-- The factor 4/3 at every strict edge, with no restrictions on the size of c. -/
theorem carry_slack (c d : ℕ) (hd : d ≤ 3*c+2) :
    4^(strictEdge c d) * (3^d * (c+1)^2) ≤
    3^(strictEdge c d) * (3^(3*c) * (d+1)^2) := by
  by_cases hz : c = 0 ∧ d = 0
  · obtain ⟨rfl,rfl⟩ := hz
    decide
  by_cases ht : d = 3*c+2
  · subst d
    simp only [strictEdge, or_true, ite_true, pow_zero, one_mul, pow_add]
    ring_nf
    omega
  simp only [strictEdge, hz, ht, or_self, ite_false, pow_one]
  by_cases hdc : d < c
  · have hb : (c+1)^2 ≤ 3^(2*c) := by
      calc
        _ ≤ (3^c)^2 := Nat.pow_le_pow_left (succ_le_three_pow c) 2
        _ = _ := by rw [← pow_mul, Nat.mul_comm]
    have hh : 3*(3^d*(c+1)^2) ≤ 3^(3*c) := calc
      _ ≤ 3*(3^d*3^(2*c)) := by gcongr
      _ = 3^(d+2*c+1) := by rw [pow_succ, pow_add]; ring
      _ ≤ _ := up_pow (by omega)
    have hne : 1 ≤ (d+1)^2 := Nat.one_le_pow _ _ (by omega)
    have hr : 3^(3*c) ≤ 3^(3*c)*(d+1)^2 := by
      simpa using Nat.mul_le_mul_left (3^(3*c)) hne
    omega
  have hcd : c+1 ≤ d+1 := by omega
  by_cases hlt : d < 3*c
  · have hh : 3*(3^d*(c+1)^2) ≤ 3^(3*c)*(d+1)^2 := calc
      _ = 3^(d+1)*(c+1)^2 := by rw [pow_succ]; ring
      _ ≤ _ := Nat.mul_le_mul (up_pow (by omega)) (Nat.pow_le_pow_left hcd 2)
    omega
  have hv : d = 3*c ∨ d = 3*c+1 := by omega
  rcases hv with rfl | rfl
  · have hc : 0 < c := by omega
    have hh : 4*(c+1)^2 ≤ 3*(3*c+1)^2 := by nlinarith
    nlinarith only [Nat.mul_le_mul_left (3^(3*c)) hh]
  · rw [pow_succ]
    have hh : 4*(c+1)^2 ≤ (3*c+1+1)^2 := by nlinarith
    nlinarith only [Nat.mul_le_mul_left (3^(3*c)*3) hh]

/-- Form exact integer clocks, so neither logarithms nor real powers enter. -/
theorem step_slack (a b c d : ℕ) (ha : 1 ≤ a) (hb : b ≤ 3)
    (edge : a+d=b+3*c) :
    4^(strictEdge c d) * 3^b * (c+1)^2 ≤ 3^(strictEdge c d) * 3^a * (d+1)^2 := by
  have hl := Nat.mul_le_mul_left (3^b) (carry_slack c d (by omega))
  apply Nat.le_of_mul_le_mul_left (c := 3^d)
  · calc
      _ = 3^b*(4^(strictEdge c d)*(3^d*(c+1)^2)) := by ring
      _ ≤ _ := hl
      _ = 3^(b+3*c)*(3^(strictEdge c d)*(d+1)^2) := by rw [pow_add]; ring
      _ = 3^(a+d)*(3^(strictEdge c d)*(d+1)^2) := by rw [edge]
      _ = _ := by rw [pow_add]; ring
  · positivity

/-- Each strict edge on the chosen interval contributes its own factor. -/
theorem interval_slack (a b c : ℕ → ℕ) (n : ℕ)
    (ha : ∀ i < n, 1 ≤ a i) (hb : ∀ i < n, b i ≤ 3)
    (edge : ∀ i < n, a i + c (i+1) = b i + 3*c i) :
    4^(∑ i ∈ Finset.range n, strictEdge (c i) (c (i+1))) *
      3^(∑ i ∈ Finset.range n, b i) * (c 0+1)^2 ≤
    3^(∑ i ∈ Finset.range n, strictEdge (c i) (c (i+1))) *
      3^(∑ i ∈ Finset.range n, a i) * (c n+1)^2 := by
  induction n with
  | zero => simp
  | succ n ih =>
    have h := ih (fun i hi => ha i (by omega)) (fun i hi => hb i (by omega))
      (fun i hi => edge i (by omega))
    have s := step_slack (a n) (b n) (c n) (c (n+1)) (ha n (by omega))
      (hb n (by omega)) (edge n (by omega))
    simp only [Finset.sum_range_succ, pow_add]
    calc
      _ = (4^(strictEdge (c n) (c (n+1))) * 3^(b n)) *
          (4^(∑ i ∈ Finset.range n, strictEdge (c i) (c (i+1))) *
          3^(∑ i ∈ Finset.range n, b i) * (c 0+1)^2) := by ring
      _ ≤ _ := Nat.mul_le_mul_left _ h
      _ = (3^(∑ i ∈ Finset.range n, strictEdge (c i) (c (i+1))) *
            3^(∑ i ∈ Finset.range n, a i)) *
            (4^(strictEdge (c n) (c (n+1))) * 3^(b n) * (c n+1)^2) := by ring
      _ ≤ _ := Nat.mul_le_mul_left _ s
      _ = _ := by ring

#print axioms carry_slack
#print axioms step_slack
#print axioms interval_slack
end Collatz.StrictCarry
