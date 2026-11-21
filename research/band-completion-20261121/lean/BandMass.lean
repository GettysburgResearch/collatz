module
public import SectionDynamics
public import Mathlib.Analysis.PSeries

@[expose] public section

/-!
# Source-weighted entrance into the shrinking dyadic section

The first entrance has a finite fourth logarithmic height moment under the
fixed source weight n⁻⁴. This is an unconditional consequence of the bounded
entrance theorem. The proof does not replace source weights by endpoint weights.
It supplies no estimate after an unbounded number of section returns.
-/

namespace CollatzShell.ForwardSection.BandMass

def entrance (n : ℕ) : ℕ := orbit (firstVisit n) n

theorem step_le_twice (n : ℕ) : step n ≤ 2 * n := by
  unfold step
  split <;> omega

theorem orbit_le_two_pow_mul (t n : ℕ) : orbit t n ≤ 2 ^ t * n := by
  induction t generalizing n with
  | zero => simp [orbit]
  | succ t ih =>
    calc
      orbit (t + 1) n = orbit t (step n) := rfl
      _ ≤ 2 ^ t * step n := ih (step n)
      _ ≤ 2 ^ t * (2 * n) := Nat.mul_le_mul_left _ (step_le_twice n)
      _ = 2 ^ (t + 1) * n := by ring

theorem orbit_pos {n : ℕ} (hn : 0 < n) (t : ℕ) : 0 < orbit t n := by
  induction t generalizing n with
  | zero => exact hn
  | succ t ih =>
    apply ih
    unfold step
    split <;> omega

theorem square_le_two_pow (s : ℕ) : (s + 1) * (s + 1) ≤ 2 ^ (2 * s + 1) := by
  induction s with
  | zero => norm_num
  | succ s ih =>
    calc
      (s + 1 + 1) * (s + 1 + 1) ≤ 4 * ((s + 1) * (s + 1)) := by nlinarith
      _ ≤ 4 * 2 ^ (2 * s + 1) := Nat.mul_le_mul_left 4 ih
      _ = 2 ^ (2 * (s + 1) + 1) := by
        rw [show 2 * (s + 1) + 1 = (2 * s + 1) + 2 by omega, pow_add]
        ring

theorem log2_le_twice_sqrt {n : ℕ} (hn : 0 < n) : n.log2 ≤ 2 * n.sqrt := by
  have hlt : n < 2 ^ (2 * n.sqrt + 1) :=
    (Nat.lt_succ_sqrt n).trans_le (square_le_two_pow n.sqrt)
  have hlog := (Nat.log2_lt hn.ne').mpr hlt
  omega

theorem orbit_log2_le {n : ℕ} (hn : 0 < n) (t : ℕ) :
    (orbit t n).log2 ≤ t + n.log2 := by
  have hlt : orbit t n < 2 ^ (t + n.log2 + 1) := by
    calc
      orbit t n ≤ 2 ^ t * n := orbit_le_two_pow_mul t n
      _ < 2 ^ t * 2 ^ (n.log2 + 1) :=
        Nat.mul_lt_mul_of_pos_left Nat.lt_log2_self (by positivity)
      _ = 2 ^ (t + n.log2 + 1) := by rw [← pow_add, Nat.add_assoc]
  have hlog := (Nat.log2_lt (orbit_pos hn t).ne').mpr hlt
  omega

/-- The current source, rather than the entrance endpoint, pays for the clock. -/
theorem firstVisit_lt_six_sqrt {n : ℕ} (hn : 0 < n) : firstVisit n < 6 * n.sqrt := by
  have hc := firstVisit_bound n hn
  have hl := log2_le_twice_sqrt hn
  omega

theorem entrance_log_height_le {n : ℕ} (hn : 0 < n) :
    (entrance n).log2 + 1 ≤ 8 * n.sqrt := by
  have ht := firstVisit_lt_six_sqrt hn
  have hl := log2_le_twice_sqrt hn
  have he := orbit_log2_le hn (firstVisit n)
  change (orbit (firstVisit n) n).log2 + 1 ≤ _
  omega

/-- The fourth logarithmic entrance moment is paid for by a quadratic source
moment. No injectivity of the entrance map is assumed. -/
theorem entrance_log_four_le {n : ℕ} (hn : 0 < n) :
    ((entrance n).log2 + 1) ^ 4 ≤ 4096 * n ^ 2 := by
  have h := entrance_log_height_le hn
  have hs := Nat.sqrt_le n
  have hsq : ((entrance n).log2 + 1) * ((entrance n).log2 + 1) ≤ 64 * n := by
    have hm := Nat.mul_le_mul h h
    nlinarith
  calc
    ((entrance n).log2 + 1) ^ 4 =
        (((entrance n).log2 + 1) * ((entrance n).log2 + 1)) *
          (((entrance n).log2 + 1) * ((entrance n).log2 + 1)) := by ring
    _ ≤ (64 * n) * (64 * n) := Nat.mul_le_mul hsq hsq
    _ = 4096 * n ^ 2 := by ring

noncomputable def entranceLogTerm (k : ℕ) : ℝ :=
  (((entrance (k + 1)).log2 + 1 : ℕ) : ℝ) ^ 4 *
    (((k + 1 : ℕ) : ℝ) ^ 4)⁻¹

theorem entranceLogTerm_bound (k : ℕ) :
    entranceLogTerm k ≤ 4096 * (((k + 1 : ℕ) : ℝ) ^ 2)⁻¹ := by
  have hk : (0 : ℝ) < ((k + 1 : ℕ) : ℝ) := by positivity
  have h : (((entrance (k + 1)).log2 + 1 : ℕ) : ℝ) ^ 4 ≤
      4096 * (((k + 1 : ℕ) : ℝ) ^ 2) := by
    exact_mod_cast entrance_log_four_le (by omega : 0 < k + 1)
  unfold entranceLogTerm
  calc
    _ ≤ (4096 * (((k + 1 : ℕ) : ℝ) ^ 2)) *
        (((k + 1 : ℕ) : ℝ) ^ 4)⁻¹ :=
      mul_le_mul_of_nonneg_right h (by positivity)
    _ = 4096 * (((k + 1 : ℕ) : ℝ) ^ 2)⁻¹ := by
      field_simp [ne_of_gt hk]

/-- A global first-entrance estimate over all positive ordinary sources.
The source weights are fixed fourth powers, including all entrance fibers. -/
theorem entranceLogTerm_summable : Summable entranceLogTerm := by
  have hp : Summable (fun k : ℕ => (((k + 1 : ℕ) : ℝ) ^ 2)⁻¹) :=
    (summable_nat_add_iff 1).mpr
      (Real.summable_nat_pow_inv.mpr (by decide : 1 < 2))
  exact Summable.of_nonneg_of_le (fun _ => by unfold entranceLogTerm; positivity)
    entranceLogTerm_bound (hp.mul_left 4096)

theorem entranceLogTerm_sum_le :
    (∑' k : ℕ, entranceLogTerm k) ≤
      4096 * ∑' k : ℕ, (((k + 1 : ℕ) : ℝ) ^ 2)⁻¹ := by
  have hp : Summable (fun k : ℕ => (((k + 1 : ℕ) : ℝ) ^ 2)⁻¹) :=
    (summable_nat_add_iff 1).mpr
      (Real.summable_nat_pow_inv.mpr (by decide : 1 < 2))
  have h := Summable.tsum_le_tsum entranceLogTerm_bound entranceLogTerm_summable
    (hp.mul_left 4096)
  simpa only [tsum_mul_left] using h

/-- Finite packet conservation, with every many-to-one entrance fiber retained.
In particular, sparsity of the image alone gives no decrease of source mass. -/
theorem sum_entrance_packets (S : Finset ℕ) (w : ℕ → ℝ) :
    ∑ m ∈ S.image entrance, (∑ n ∈ S, if entrance n = m then w n else 0) =
      ∑ n ∈ S, w n := by
  classical
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro n hn
  simp [Finset.mem_image.mpr ⟨n, hn, rfl⟩]

end CollatzShell.ForwardSection.BandMass

#print axioms CollatzShell.ForwardSection.BandMass.entrance_log_four_le
#print axioms CollatzShell.ForwardSection.BandMass.entranceLogTerm_summable
#print axioms CollatzShell.ForwardSection.BandMass.entranceLogTerm_sum_le
#print axioms CollatzShell.ForwardSection.BandMass.sum_entrance_packets
