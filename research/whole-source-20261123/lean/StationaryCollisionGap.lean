import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
The quantitative sequence core of COLLISION_CORE.md. In the written application
H is block Shannon entropy and R is minus log of the ternary collision sum.
Stationarity supplies subadditivity, the actual mean-gap bound supplies the
linear cap, and equality in the geometric maximum-entropy inequality supplies
the last hypothesis of strict_rate_gap.

This file does not assert those probabilistic identifications as axioms or
formalize the extraction of the ordinary-source stationary limit. All inputs
appear as theorem parameters. The conclusion is an eventual exponential gap;
no existence of a Renyi entropy rate is assumed.
-/

namespace CollatzWholeSource.StationaryCollisionGap

/-- Break a subadditive block quantity into blocks of one fixed length. -/
theorem block_bound
    (H : ℕ → ℝ) (hsub : ∀ a b, H (a + b) ≤ H a + H b)
    (q k r : ℕ) : H (q * k + r) ≤ (q : ℝ) * H k + H r := by
  induction q with
  | zero => simp
  | succ q ih =>
      calc
        H ((q + 1) * k + r) = H (k + (q * k + r)) := by congr 1; ring
        _ ≤ H k + H (q * k + r) := hsub _ _
        _ ≤ H k + ((q : ℝ) * H k + H r) := add_le_add le_rfl ih
        _ = ((q + 1 : ℕ) : ℝ) * H k + H r := by push_cast; ring

/-- One strict Shannon block deficit persists at every larger block length.
The floor is retained exactly, rather than hidden in an asymptotic rate. -/
theorem deficit_at_all_lengths
    (H R : ℕ → ℝ) (phi : ℝ)
    (hsub : ∀ a b, H (a + b) ≤ H a + H b)
    (hcap : ∀ n, H n ≤ (n : ℝ) * phi)
    (hcompare : ∀ n, R n ≤ H n)
    (k n : ℕ) :
    R n ≤ (n : ℝ) * phi - (n / k : ℕ) * ((k : ℝ) * phi - H k) := by
  have hdecomp : n / k * k + n % k = n := by
    simpa [Nat.mul_comm] using Nat.div_add_mod n k
  have hblocks := block_bound H hsub (n / k) k (n % k)
  rw [hdecomp] at hblocks
  have hcast : ((n / k : ℕ) : ℝ) * (k : ℝ) + ((n % k : ℕ) : ℝ) = (n : ℝ) := by
    exact_mod_cast hdecomp
  calc
    R n ≤ H n := hcompare n
    _ ≤ (n / k : ℕ) * H k + H (n % k) := hblocks
    _ ≤ (n / k : ℕ) * H k + (n % k : ℕ) * phi :=
      add_le_add le_rfl (hcap (n % k))
    _ = (n : ℝ) * phi - (n / k : ℕ) * ((k : ℝ) * phi - H k) := by
      rw [← hcast]
      ring

/-- A positive finite-block deficit gives a fixed positive exponential gain.
Only the threshold 2*k is needed for the stated half-deficit rate. -/
theorem strict_gap_of_block_deficit
    (H R : ℕ → ℝ) (phi : ℝ)
    (hsub : ∀ a b, H (a + b) ≤ H a + H b)
    (hcap : ∀ n, H n ≤ (n : ℝ) * phi)
    (hcompare : ∀ n, R n ≤ H n)
    (k : ℕ) (hk : 0 < k) (hdeficit : H k < (k : ℝ) * phi) :
    ∃ epsilon > 0, ∀ n, 2 * k ≤ n →
      R n ≤ (n : ℝ) * (phi - epsilon) := by
  let delta : ℝ := (k : ℝ) * phi - H k
  have hdelta : 0 < delta := sub_pos.mpr hdeficit
  have hkreal : 0 < (k : ℝ) := Nat.cast_pos.mpr hk
  have hden : 0 < 2 * (k : ℝ) := by positivity
  refine ⟨delta / (2 * (k : ℝ)), div_pos hdelta hden, ?_⟩
  intro n hn
  have hbound := deficit_at_all_lengths H R phi hsub hcap hcompare k n
  change R n ≤ (n : ℝ) * phi - (n / k : ℕ) * delta at hbound
  have hmod : ((n % k : ℕ) : ℝ) < (k : ℝ) :=
    Nat.cast_lt.mpr (Nat.mod_lt n hk)
  have hlarge : 2 * (k : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
  have hdecomp : ((n / k : ℕ) : ℝ) * (k : ℝ) + ((n % k : ℕ) : ℝ) = (n : ℝ) := by
    have h := Nat.div_add_mod n k
    rw [Nat.mul_comm k (n / k)] at h
    exact_mod_cast h
  have hquot : (n : ℝ) ≤ 2 * ((n / k : ℕ) : ℝ) * (k : ℝ) := by linarith
  have hscaled := mul_le_mul_of_nonneg_right hquot (le_of_lt hdelta)
  have hgain : (n : ℝ) * (delta / (2 * (k : ℝ))) ≤ (n / k : ℕ) * delta := by
    rw [← mul_div_assoc]
    apply (div_le_iff₀ hden).2
    nlinarith [hscaled]
  nlinarith [hbound, hgain]

/-- Either there is a finite Shannon deficit, or maximum-entropy rigidity
supplies its own strictly smaller collision exponent. This proves an eventual
strict rate bound without asserting that the collision rate converges. -/
theorem strict_rate_gap
    (H R : ℕ → ℝ) (phi psi : ℝ)
    (hzero : H 0 = 0)
    (hsub : ∀ a b, H (a + b) ≤ H a + H b)
    (hcap : ∀ n, H n ≤ (n : ℝ) * phi)
    (hcompare : ∀ n, R n ≤ H n)
    (hrigid : (∀ n, H n = (n : ℝ) * phi) →
      ∀ n, R n ≤ (n : ℝ) * psi)
    (hstrict : psi < phi) :
    ∃ epsilon > 0, ∃ N : ℕ, ∀ n, N ≤ n →
      R n ≤ (n : ℝ) * (phi - epsilon) := by
  classical
  by_cases heq : ∀ n, H n = (n : ℝ) * phi
  · refine ⟨(phi - psi) / 2, by linarith, 0, ?_⟩
    intro n _
    have hn : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg n
    have h := hrigid heq n
    have hcoeff : psi ≤ phi - (phi - psi) / 2 := by linarith
    exact h.trans (mul_le_mul_of_nonneg_left hcoeff hn)
  · push Not at heq
    obtain ⟨k, hkne⟩ := heq
    have hk : 0 < k := by
      by_contra h
      have hkzero : k = 0 := by omega
      subst k
      simp [hzero] at hkne
    have hdeficit : H k < (k : ℝ) * phi := lt_of_le_of_ne (hcap k) hkne
    obtain ⟨epsilon, hpos, hbound⟩ :=
      strict_gap_of_block_deficit H R phi hsub hcap hcompare k hk hdeficit
    exact ⟨epsilon, hpos, 2 * k, hbound⟩

end CollatzWholeSource.StationaryCollisionGap
