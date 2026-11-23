module

public import ShellCover
public import Mathlib.Basic.Real.Basic

@[expose] public section

/-!
# Accumulating finite inverse-density block errors

This module proves only the finite algebra used in
`POLYLOGARITHMIC_INVERSE_HORIZONS.md`. The analytic block comparison and
the initial small-depth estimate remain explicit hypotheses. No declaration
imports or asserts Tao's mixing theorem, an infinite-depth bound, or Collatz
convergence.
-/

namespace CollatzFiniteBlockTelescope

/-- A decrement by `m` accumulates linearly growing local errors within a
quadratic budget. The exact induction slack is `ε * m * (s - m)`. -/
theorem scaled_bound (f : ℕ → ℝ) (m : ℕ) (hm : 0 < m)
    (B ε : ℝ) (hε : 0 ≤ ε)
    (hbase : ∀ s, s ≤ 2 * m → f s ≤ B)
    (hstep : ∀ s, 2 * m < s →
      f s ≤ f (s - m) + ε * ((s : ℝ) + 2))
    (s : ℕ) :
    (m : ℝ) * f s ≤ (m : ℝ) * B + ε * (s : ℝ) * ((s : ℝ) + 2) := by
  induction s using Nat.strong_induction_on with
  | h s ih =>
      have hm0 : (0 : ℝ) ≤ m := Nat.cast_nonneg m
      by_cases hs : s ≤ 2 * m
      · have hb := mul_le_mul_of_nonneg_left (hbase s hs) hm0
        have hs0 : (0 : ℝ) ≤ s := Nat.cast_nonneg s
        have ht : 0 ≤ ε * (s : ℝ) * ((s : ℝ) + 2) :=
          mul_nonneg (mul_nonneg hε hs0) (by linarith)
        exact hb.trans (le_add_of_nonneg_right ht)
      · have hlarge : 2 * m < s := Nat.lt_of_not_ge hs
        have hms : m ≤ s := by omega
        have hlt : s - m < s := by omega
        have hi := ih (s - m) hlt
        have hlocal := mul_le_mul_of_nonneg_left (hstep s hlarge) hm0
        have hslack : 0 ≤ ε * (m : ℝ) * ((s - m : ℕ) : ℝ) :=
          mul_nonneg (mul_nonneg hε hm0) (Nat.cast_nonneg (s - m))
        calc
          (m : ℝ) * f s ≤
              (m : ℝ) * f (s - m) + (m : ℝ) * ε * ((s : ℝ) + 2) := by
                nlinarith only [hlocal]
          _ ≤ (m : ℝ) * B +
              ε * ((s - m : ℕ) : ℝ) * (((s - m : ℕ) : ℝ) + 2) +
              (m : ℝ) * ε * ((s : ℝ) + 2) := by
                linarith only [hi]
          _ = (m : ℝ) * B + ε * (s : ℝ) * ((s : ℝ) + 2) -
              ε * (m : ℝ) * ((s - m : ℕ) : ℝ) := by
                rw [Nat.cast_sub hms]
                ring
          _ ≤ (m : ℝ) * B + ε * (s : ℝ) * ((s : ℝ) + 2) :=
                sub_le_self _ hslack

/-- The corresponding pointwise bound, with the positive divisor explicit. -/
theorem bound (f : ℕ → ℝ) (m : ℕ) (hm : 0 < m)
    (B ε : ℝ) (hε : 0 ≤ ε)
    (hbase : ∀ s, s ≤ 2 * m → f s ≤ B)
    (hstep : ∀ s, 2 * m < s →
      f s ≤ f (s - m) + ε * ((s : ℝ) + 2))
    (s : ℕ) :
    f s ≤ ((m : ℝ) * B + ε * (s : ℝ) * ((s : ℝ) + 2)) / m := by
  have hmR : (0 : ℝ) < m := by exact_mod_cast hm
  apply (le_div_iff₀ hmR).2
  simpa only [mul_comm] using scaled_bound f m hm B ε hε hbase hstep s

/-- One common quadratic bound holds simultaneously at every depth in a
fixed finite horizon. The horizon cannot be replaced by infinity here. -/
theorem scaled_bound_on_horizon (f : ℕ → ℝ) (m : ℕ) (hm : 0 < m)
    (B ε : ℝ) (hε : 0 ≤ ε)
    (hbase : ∀ s, s ≤ 2 * m → f s ≤ B)
    (hstep : ∀ s, 2 * m < s →
      f s ≤ f (s - m) + ε * ((s : ℝ) + 2))
    (K s : ℕ) (hsK : s ≤ K) :
    (m : ℝ) * f s ≤ (m : ℝ) * B + ε * (K : ℝ) * ((K : ℝ) + 2) := by
  have hs0 : (0 : ℝ) ≤ s := Nat.cast_nonneg s
  have hK0 : (0 : ℝ) ≤ K := Nat.cast_nonneg K
  have hsKR : (s : ℝ) ≤ K := by exact_mod_cast hsK
  have hpoly : (s : ℝ) * ((s : ℝ) + 2) ≤ (K : ℝ) * ((K : ℝ) + 2) := by
    nlinarith only [hs0, hK0, hsKR]
  have he := mul_le_mul_of_nonneg_left hpoly hε
  have hb := scaled_bound f m hm B ε hε hbase hstep s
  nlinarith only [hb, he]

/-- The same estimate requires recurrence and base hypotheses only through
the stated finite horizon. This is the version for a predecessor floor
known only through depth `K`; no recurrence at a larger depth is assumed. -/
theorem scaled_bound_of_finite_hypotheses (f : ℕ → ℝ) (m : ℕ) (hm : 0 < m)
    (B ε : ℝ) (hε : 0 ≤ ε) (K : ℕ)
    (hbase : ∀ s, s ≤ K → s ≤ 2 * m → f s ≤ B)
    (hstep : ∀ s, s ≤ K → 2 * m < s →
      f s ≤ f (s - m) + ε * ((s : ℝ) + 2))
    (s : ℕ) (hsK : s ≤ K) :
    (m : ℝ) * f s ≤ (m : ℝ) * B + ε * (s : ℝ) * ((s : ℝ) + 2) := by
  revert hsK
  induction s using Nat.strong_induction_on with
  | h s ih =>
      intro hsK
      have hm0 : (0 : ℝ) ≤ m := Nat.cast_nonneg m
      by_cases hs : s ≤ 2 * m
      · have hb := mul_le_mul_of_nonneg_left (hbase s hsK hs) hm0
        have hs0 : (0 : ℝ) ≤ s := Nat.cast_nonneg s
        have ht : 0 ≤ ε * (s : ℝ) * ((s : ℝ) + 2) :=
          mul_nonneg (mul_nonneg hε hs0) (by linarith)
        exact hb.trans (le_add_of_nonneg_right ht)
      · have hlarge : 2 * m < s := Nat.lt_of_not_ge hs
        have hms : m ≤ s := by omega
        have hlt : s - m < s := by omega
        have hrK : s - m ≤ K := (Nat.sub_le s m).trans hsK
        have hi := ih (s - m) hlt hrK
        have hlocal := mul_le_mul_of_nonneg_left (hstep s hsK hlarge) hm0
        have hslack : 0 ≤ ε * (m : ℝ) * ((s - m : ℕ) : ℝ) :=
          mul_nonneg (mul_nonneg hε hm0) (Nat.cast_nonneg (s - m))
        calc
          (m : ℝ) * f s ≤
              (m : ℝ) * f (s - m) + (m : ℝ) * ε * ((s : ℝ) + 2) := by
                nlinarith only [hlocal]
          _ ≤ (m : ℝ) * B +
              ε * ((s - m : ℕ) : ℝ) * (((s - m : ℕ) : ℝ) + 2) +
              (m : ℝ) * ε * ((s : ℝ) + 2) := by
                linarith only [hi]
          _ = (m : ℝ) * B + ε * (s : ℝ) * ((s : ℝ) + 2) -
              ε * (m : ℝ) * ((s - m : ℕ) : ℝ) := by
                rw [Nat.cast_sub hms]
                ring
          _ ≤ (m : ℝ) * B + ε * (s : ℝ) * ((s : ℝ) + 2) :=
                sub_le_self _ hslack

end CollatzFiniteBlockTelescope

#print axioms CollatzFiniteBlockTelescope.scaled_bound
#print axioms CollatzFiniteBlockTelescope.bound
#print axioms CollatzFiniteBlockTelescope.scaled_bound_on_horizon
#print axioms CollatzFiniteBlockTelescope.scaled_bound_of_finite_hypotheses
