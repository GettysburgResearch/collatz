import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Lean.Elab.Tactic.Omega

/-!
Finite circle estimate for a periodic profile with a one-sided slope cap.
Indices are arbitrary natural-number lifts, so duplicate sampled residues
and a circular seam require no separate convention.
-/

namespace ClockMesh

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

def shiftCost (H : ℕ → K) (p lag : ℕ) : K :=
  ∑ i ∈ Finset.range p, |H (lag + i) - H i|

/-- Periodic finite-sum rotation, as in ToricWindow.rotated_sum. -/
theorem periodic_sum (f : ℕ → K) (p t : ℕ) (h : ∀ i, f (p + i) = f i) :
    ∑ i ∈ Finset.range p, f (t + i) = ∑ i ∈ Finset.range p, f i := by
  have hsum := Finset.sum_range_add f t p
  rw [Nat.add_comm t p, Finset.sum_range_add, show
    (∑ i ∈ Finset.range t, f (p + i)) = ∑ i ∈ Finset.range t, f i by simp [h]] at hsum
  exact add_left_cancel (by simpa only [add_comm (∑ i ∈ Finset.range p, f i)] using hsum.symm)

theorem shiftCost_add (H : ℕ → K) (p a b : ℕ) (hper : ∀ i, H (p + i) = H i) :
    shiftCost H p (a + b) ≤ shiftCost H p a + shiftCost H p b := by
  let f (i : ℕ) := |H (a + i) - H i|
  have hp : ∀ i, f (p + i) = f i := by
    intro i
    dsimp [f]
    rw [show a + (p + i) = p + (a + i) by omega, hper, hper]
  calc
    shiftCost H p (a + b) ≤
        ∑ i ∈ Finset.range p, (f (b + i) + |H (b + i) - H i|) := by
          apply Finset.sum_le_sum
          intro i hi
          dsimp [f]
          rw [show a + b + i = a + (b + i) by omega]
          calc
            |H (a + (b + i)) - H i| =
                |(H (a + (b + i)) - H (b + i)) + (H (b + i) - H i)| := by
                  congr 1
                  ring
            _ ≤ _ := abs_add_le _ _
    _ = _ := by rw [Finset.sum_add_distrib, periodic_sum f p b hp]; rfl

theorem shiftCost_multiple (H : ℕ → K) (p v k : ℕ) (hper : ∀ i, H (p + i) = H i) :
    shiftCost H p (k * v) ≤ (k : K) * shiftCost H p v := by
  induction k with
  | zero => simp [shiftCost]
  | succ k ih =>
    rw [Nat.succ_mul, Nat.cast_succ, add_mul, one_mul]
    exact (shiftCost_add H p (k * v) v hper).trans (add_le_add_left ih _ : _)

theorem forward_slope (H : ℕ → K) (cap : K) (start n : ℕ)
    (hstep : ∀ i, H (i + 1) - H i ≤ cap) :
    H (start + n) - H start ≤ (n : K) * cap := by
  induction n with
  | zero => simp
  | succ n ih =>
    have h := hstep (start + n)
    rw [Nat.cast_succ, add_mul, one_mul]
    rw [show start + (n + 1) = start + n + 1 by omega]
    linarith

/-- The measured interval of r indices is placed immediately before a peak;
g is the extra backward distance to the sampled k-th rotation. -/
theorem finite_mesh (H : ℕ → K) (cap : K) (p v k r g : ℕ)
    (hr : r ≤ p) (hper : ∀ i, H (p + i) = H i)
    (hstep : ∀ i, H (i + 1) - H i ≤ cap) :
    (r : K) * (H (k * v + (r + g)) - H 0 - ((r + g : ℕ) : K) * cap) ≤
      (k : K) * shiftCost H p v := by
  let s := k * v + (r + g)
  let base := H s - H 0 - ((r + g : ℕ) : K) * cap
  have heach : ∀ i < r, base ≤ |H (k * v + i) - H i| := by
    intro i hi
    have hlow := forward_slope H cap 0 i hstep
    simp only [Nat.zero_add] at hlow
    have hhigh := forward_slope H cap (k * v + i) (r + g - i) hstep
    have hidx : k * v + i + (r + g - i) = s := by dsimp [s]; omega
    rw [hidx, Nat.cast_sub (by omega : i ≤ r + g)] at hhigh
    apply le_trans _ (le_abs_self _)
    dsimp [base]
    nlinarith
  have hsmall : (r : K) * base ≤ ∑ i ∈ Finset.range r, |H (k * v + i) - H i| := by
    calc
      (r : K) * base = ∑ _i ∈ Finset.range r, base := by simp
      _ ≤ _ := Finset.sum_le_sum (fun i hi => heach i (Finset.mem_range.mp hi))
  have hwhole : (∑ i ∈ Finset.range r, |H (k * v + i) - H i|) ≤
      shiftCost H p (k * v) := by
    apply Finset.sum_le_sum_of_subset_of_nonneg (Finset.range_mono hr)
    exact fun i _ _ => abs_nonneg _
  exact hsmall.trans (hwhole.trans (shiftCost_multiple H p v k hper))

#print axioms periodic_sum
#print axioms shiftCost_add
#print axioms shiftCost_multiple
#print axioms forward_slope
#print axioms finite_mesh

end ClockMesh
