module

public import Mathlib.Algebra.BigOperators.Intervals
public import Mathlib.Algebra.BigOperators.Ring.Finset
public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Algebra.Ring.Divisibility.Basic
public import Mathlib.Data.Int.Basic
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Ring

@[expose] public section

/-!
Effective dyadic separation in a supplied finite integer zero relation.
The deep S-unit theorem is not an axiom or an import. The coefficients
are bounded explicitly, and nondegeneracy is used only through the
nonvanishing of proper sorted prefixes. The written application sorts
the terms in the actual selected zero cluster.
-/

namespace CollatzDyadicCluster

def partialSum (c : ℕ → ℤ) (e : ℕ → ℕ) (j : ℕ) : ℤ :=
  ∑ i ∈ Finset.range j, c i * (2 : ℤ) ^ e i

/-- Nondegeneracy of the supplied finite relation, including repeated
binary exponents as separate indexed terms. -/
def Nondegenerate (c : ℕ → ℤ) (e : ℕ → ℕ) (m : ℕ) : Prop :=
  ∀ s : Finset ℕ, s ⊆ Finset.range m → s.Nonempty → s ≠ Finset.range m →
    (∑ i ∈ s, c i * (2 : ℤ) ^ e i) ≠ 0

/-- Full nondegeneracy supplies the only proper-subsum facts used by
the dyadic gap proof. -/
theorem nondegenerate_proper_prefix (c : ℕ → ℤ) (e : ℕ → ℕ) (m j : ℕ)
    (nd : Nondegenerate c e m) (hj : 0 < j) (hjm : j < m) :
    partialSum c e j ≠ 0 := by
  apply nd (Finset.range j)
  · exact Finset.range_subset_range.mpr (Nat.le_of_lt hjm)
  · exact ⟨0, Finset.mem_range.mpr hj⟩
  · intro heq
    have hcard := congrArg Finset.card heq
    simp only [Finset.card_range] at hcard
    omega

/-- A proper sorted prefix cannot be separated from the remaining zero
relation by a binary-exponent gap exceeding the coefficient budget. -/
theorem adjacent_exponent_bound (c : ℕ → ℤ) (e : ℕ → ℕ) (m b j : ℕ)
    (hj : 0 < j) (hjm : j < m)
    (mono : ∀ i k, i ≤ k → k < m → e i ≤ e k)
    (coeff : ∀ i < m, (c i).natAbs ≤ 2 ^ b)
    (total : partialSum c e m = 0)
    (proper : partialSum c e j ≠ 0) :
    e j ≤ e (j - 1) + m + b := by
  have htail : (2 : ℤ) ^ e j ∣
      ∑ i ∈ Finset.Ico j m, c i * (2 : ℤ) ^ e i := by
    apply Finset.dvd_sum
    intro i hi
    obtain ⟨hji, him⟩ := Finset.mem_Ico.mp hi
    exact dvd_mul_of_dvd_right (pow_dvd_pow (2 : ℤ) (mono j i hji him)) (c i)
  have hsplit : partialSum c e j +
      (∑ i ∈ Finset.Ico j m, c i * (2 : ℤ) ^ e i) = 0 := by
    rw [partialSum, Finset.sum_range_add_sum_Ico _ (Nat.le_of_lt hjm)]
    exact total
  have hprefix : (2 : ℤ) ^ e j ∣ partialSum c e j := by
    have hneg : partialSum c e j =
        -(∑ i ∈ Finset.Ico j m, c i * (2 : ℤ) ^ e i) := by omega
    rw [hneg]
    exact dvd_neg.mpr htail
  have hlower : 2 ^ e j ≤ (partialSum c e j).natAbs := by
    simpa only [Int.natAbs_pow, show (2 : ℤ).natAbs = 2 from rfl] using
      Int.natAbs_le_of_dvd_ne_zero hprefix proper
  have hterm (i : ℕ) (hi : i ∈ Finset.range j) :
      (c i * (2 : ℤ) ^ e i).natAbs ≤ 2 ^ (b + e (j - 1)) := by
    have hij : i < j := Finset.mem_range.mp hi
    have he : e i ≤ e (j - 1) := mono i (j - 1) (by omega) (by omega)
    rw [Int.natAbs_mul, Int.natAbs_pow,
      show (2 : ℤ).natAbs = 2 from rfl, pow_add]
    exact Nat.mul_le_mul (coeff i (by omega))
      (Nat.pow_le_pow_right (by decide : 0 < 2) he)
  have hupper : (partialSum c e j).natAbs ≤ j * 2 ^ (b + e (j - 1)) := by
    calc
      _ ≤ ∑ i ∈ Finset.range j, (c i * (2 : ℤ) ^ e i).natAbs :=
        Int.natAbs_sum_le _ _
      _ ≤ ∑ _i ∈ Finset.range j, 2 ^ (b + e (j - 1)) :=
        Finset.sum_le_sum hterm
      _ = _ := by simp
  have hjpow : j ≤ 2 ^ m :=
    Nat.le_trans (Nat.le_of_lt hjm)
      (Nat.le_of_lt (Nat.lt_pow_self (by decide : 1 < 2)))
  have hpow : 2 ^ e j ≤ 2 ^ (e (j - 1) + m + b) := by
    calc
      _ ≤ j * 2 ^ (b + e (j - 1)) := hlower.trans hupper
      _ ≤ 2 ^ m * 2 ^ (b + e (j - 1)) := Nat.mul_le_mul_right _ hjpow
      _ = _ := by rw [← pow_add]; congr 1; omega
  exact (Nat.pow_le_pow_iff_right (by decide : 1 < 2)).mp hpow

/-- The full sorted binary-exponent span is bounded by the number of
gaps times the same explicit local budget. -/
theorem exponent_from_first (c : ℕ → ℤ) (e : ℕ → ℕ) (m b : ℕ)
    (mono : ∀ i k, i ≤ k → k < m → e i ≤ e k)
    (coeff : ∀ i < m, (c i).natAbs ≤ 2 ^ b)
    (total : partialSum c e m = 0)
    (proper : ∀ j, 0 < j → j < m → partialSum c e j ≠ 0) :
    ∀ i < m, e i ≤ e 0 + i * (m + b) := by
  intro i
  induction i with
  | zero => intro _; simp
  | succ i ih =>
    intro hi
    have hprev := ih (by omega)
    have hstep := adjacent_exponent_bound c e m b (i + 1)
      (by omega) hi mono coeff total (proper _ (by omega) hi)
    simp only [Nat.add_sub_cancel] at hstep
    rw [Nat.succ_mul]
    omega

/-- The gap calculation also applies from any offset. This local form
avoids charging for correction terms outside the interval of interest. -/
theorem exponent_from_index (c : ℕ → ℤ) (e : ℕ → ℕ) (m b j : ℕ)
    (mono : ∀ i k, i ≤ k → k < m → e i ≤ e k)
    (coeff : ∀ i < m, (c i).natAbs ≤ 2 ^ b)
    (total : partialSum c e m = 0)
    (proper : ∀ k, 0 < k → k < m → partialSum c e k ≠ 0) :
    ∀ d, j + d < m → e (j + d) ≤ e j + d * (m + b) := by
  intro d
  induction d with
  | zero => intro _; simp
  | succ d ih =>
    intro hd
    have hprev := ih (by omega)
    have hstep := adjacent_exponent_bound c e m b (j + (d + 1))
      (by omega) hd mono coeff total (proper _ (by omega) hd)
    have hindex : j + (d + 1) - 1 = j + d := by omega
    rw [hindex] at hstep
    rw [Nat.succ_mul]
    omega

/-- Only the number of terms between two chosen coordinates is needed,
not the cardinality of the entire zero cluster. -/
theorem exponent_nearby_bound (c : ℕ → ℤ) (e : ℕ → ℕ) (m b i j K : ℕ)
    (hi : i < m) (hj : j < m) (near : i ≤ j + K)
    (mono : ∀ u v, u ≤ v → v < m → e u ≤ e v)
    (coeff : ∀ u < m, (c u).natAbs ≤ 2 ^ b)
    (total : partialSum c e m = 0)
    (proper : ∀ k, 0 < k → k < m → partialSum c e k ≠ 0) :
    e i ≤ e j + K * (m + b) := by
  by_cases hij : i ≤ j
  · exact (mono i j hij hj).trans (Nat.le_add_right _ _)
  · have hji : j ≤ i := by omega
    have hindex : j + (i - j) = i := Nat.add_sub_of_le hji
    have hlocal := exponent_from_index c e m b j mono coeff total proper (i - j)
      (by omega)
    rw [hindex] at hlocal
    have hmul : (i - j) * (m + b) ≤ K * (m + b) :=
      Nat.mul_le_mul_right _ (by omega : i - j ≤ K)
    omega

/-- Any two exponents in the supplied sorted zero cluster are within
the explicit total span; no height theorem for S-unit solutions is used. -/
theorem exponent_pair_bound (c : ℕ → ℤ) (e : ℕ → ℕ) (m b i j : ℕ)
    (hi : i < m) (hj : j < m)
    (mono : ∀ u v, u ≤ v → v < m → e u ≤ e v)
    (coeff : ∀ u < m, (c u).natAbs ≤ 2 ^ b)
    (total : partialSum c e m = 0)
    (proper : ∀ k, 0 < k → k < m → partialSum c e k ≠ 0) :
    e i ≤ e j + (m - 1) * (m + b) := by
  have hfirst := exponent_from_first c e m b mono coeff total proper i hi
  have hzero : e 0 ≤ e j := mono 0 j (by omega) hj
  have hmul : i * (m + b) ≤ (m - 1) * (m + b) :=
    Nat.mul_le_mul_right _ (by omega : i ≤ m - 1)
  omega

/-- Explicit denominator for the ratio of a correction monomial to an
initial endpoint monomial inside the same selected cluster. -/
theorem mixed_monomial_comparison
    (c : ℕ → ℤ) (e : ℕ → ℕ) (m h i j r : ℕ)
    (hi : i < m) (hj : j < m)
    (mono : ∀ u v, u ≤ v → v < m → e u ≤ e v)
    (coeff : ∀ u < m, (c u).natAbs ≤ 2 ^ (2 * h))
    (total : partialSum c e m = 0)
    (proper : ∀ k, 0 < k → k < m → partialSum c e k ≠ 0) :
    3 ^ h * 2 ^ e i ≤
      (3 ^ h * 2 ^ ((m - 1) * (m + 2 * h))) * (3 ^ r * 2 ^ e j) := by
  have he := exponent_pair_bound c e m (2 * h) i j hi hj
    mono coeff total proper
  have hp : 2 ^ e i ≤ 2 ^ e j * 2 ^ ((m - 1) * (m + 2 * h)) := by
    rw [← pow_add]
    exact Nat.pow_le_pow_right (by decide : 0 < 2) he
  have hr : 1 ≤ 3 ^ r := Nat.one_le_pow _ _ (by decide)
  calc
    _ ≤ 3 ^ h * (2 ^ e j * 2 ^ ((m - 1) * (m + 2 * h))) :=
      Nat.mul_le_mul_left _ hp
    _ = (3 ^ h * 2 ^ ((m - 1) * (m + 2 * h))) * 2 ^ e j := by ring
    _ ≤ (3 ^ h * 2 ^ ((m - 1) * (m + 2 * h))) * (3 ^ r * 2 ^ e j) :=
      Nat.mul_le_mul_left _ (by
        simpa only [Nat.one_mul] using (Nat.mul_le_mul_right (2 ^ e j) hr))

/-- Apply the cluster ratio bound to a supplied positive affine identity's
endpoint term and total correction. Their arithmetic identification stays
an explicit premise; the S-unit selection is a written theorem. -/
theorem correction_denominator
    (c : ℕ → ℤ) (e : ℕ → ℕ) (m h i j r n C : ℕ)
    (hi : i < m) (hj : j < m)
    (mono : ∀ u v, u ≤ v → v < m → e u ≤ e v)
    (coeff : ∀ u < m, (c u).natAbs ≤ 2 ^ (2 * h))
    (total : partialSum c e m = 0)
    (proper : ∀ k, 0 < k → k < m → partialSum c e k ≠ 0)
    (endpoint : n ≤ 2 ^ e i)
    (correction : 3 ^ r * 2 ^ e j ≤ C) :
    3 ^ h * n ≤ (3 ^ h * 2 ^ ((m - 1) * (m + 2 * h))) * C := by
  exact (Nat.mul_le_mul_left _ endpoint).trans
    ((mixed_monomial_comparison c e m h i j r hi hj mono coeff total proper).trans
      (Nat.mul_le_mul_left _ correction))

/-- The application-ready finite cluster bound: all signed ternary
coefficients have height at most `3 ^ h`, and no proper nonempty indexed
subsum vanishes. Sorting and identifying the actual selected endpoint
and correction terms remain explicit premises. -/
theorem ternary_cluster_correction_denominator
    (c : ℕ → ℤ) (e : ℕ → ℕ) (m h i j r n C : ℕ)
    (hi : i < m) (hj : j < m)
    (mono : ∀ u v, u ≤ v → v < m → e u ≤ e v)
    (coeff : ∀ u < m, (c u).natAbs ≤ 3 ^ h)
    (total : partialSum c e m = 0)
    (nd : Nondegenerate c e m)
    (endpoint : n ≤ 2 ^ e i)
    (correction : 3 ^ r * 2 ^ e j ≤ C) :
    3 ^ h * n ≤ (3 ^ h * 2 ^ ((m - 1) * (m + 2 * h))) * C := by
  have hcoeff : ∀ u < m, (c u).natAbs ≤ 2 ^ (2 * h) := by
    intro u hu
    apply (coeff u hu).trans
    calc
      3 ^ h ≤ (2 ^ 2) ^ h := Nat.pow_le_pow_left (by decide : 3 ≤ 2 ^ 2) h
      _ = _ := (pow_mul 2 2 h).symm
  exact correction_denominator c e m h i j r n C hi hj mono hcoeff total
    (fun k hk hkm => nondegenerate_proper_prefix c e m k nd hk hkm)
    endpoint correction

/-- A nearby correction gives the stronger denominator used for the
logarithmic occupation bound. The actual endpoint/correction labeling
is supplied, and the offset `K` counts only intervening endpoint terms. -/
theorem nearby_ternary_cluster_correction_denominator
    (c : ℕ → ℤ) (e : ℕ → ℕ) (m h i j r n C K : ℕ)
    (hi : i < m) (hj : j < m) (near : i ≤ j + K)
    (mono : ∀ u v, u ≤ v → v < m → e u ≤ e v)
    (coeff : ∀ u < m, (c u).natAbs ≤ 3 ^ h)
    (total : partialSum c e m = 0)
    (nd : Nondegenerate c e m)
    (endpoint : n ≤ 2 ^ e i)
    (correction : 3 ^ r * 2 ^ e j ≤ C) :
    3 ^ h * n ≤ (3 ^ h * 2 ^ (K * (m + 2 * h))) * C := by
  have hcoeff : ∀ u < m, (c u).natAbs ≤ 2 ^ (2 * h) := by
    intro u hu
    apply (coeff u hu).trans
    calc
      3 ^ h ≤ (2 ^ 2) ^ h := Nat.pow_le_pow_left (by decide : 3 ≤ 2 ^ 2) h
      _ = _ := (pow_mul 2 2 h).symm
  have he := exponent_nearby_bound c e m (2 * h) i j K hi hj near mono hcoeff total
    (fun k hk hkm => nondegenerate_proper_prefix c e m k nd hk hkm)
  have hp : 2 ^ e i ≤ 2 ^ e j * 2 ^ (K * (m + 2 * h)) := by
    rw [← pow_add]
    exact Nat.pow_le_pow_right (by decide : 0 < 2) he
  have hr : 1 ≤ 3 ^ r := Nat.one_le_pow _ _ (by decide)
  have hsmall : 2 ^ e j ≤ 3 ^ r * 2 ^ e j := by
    simpa only [Nat.one_mul] using (Nat.mul_le_mul_right (2 ^ e j) hr)
  have hc : 2 ^ e j ≤ C := hsmall.trans correction
  calc
    _ ≤ 3 ^ h * 2 ^ e i := Nat.mul_le_mul_left _ endpoint
    _ ≤ 3 ^ h * (2 ^ e j * 2 ^ (K * (m + 2 * h))) := Nat.mul_le_mul_left _ hp
    _ = (3 ^ h * 2 ^ (K * (m + 2 * h))) * 2 ^ e j := by ring
    _ ≤ _ := Nat.mul_le_mul_left _ hc

/-- If every index after a chosen correction up to the initial term is
an endpoint index, the endpoint count bounds the needed index distance. -/
theorem index_distance_from_endpoint_count (E : Finset ℕ) (i j K : ℕ)
    (between : Finset.Ioc j i ⊆ E) (count : E.card ≤ K) :
    i ≤ j + K := by
  have hcard := (Finset.card_le_card between).trans count
  simp only [Nat.card_Ioc] at hcard
  omega

/-- A correction denominator is incompatible with the ordinary
finite-floor correction estimate at the displayed explicit floor. -/
theorem finite_floor_contradiction (Q C N b : ℕ)
    (hQ : 0 < Q) (hC : 0 < C)
    (denominator : N ≤ Q * C)
    (floor_estimate : 3 * (b * Q) * C ≤ (b - 1) * N)
    (hb : 0 < b) : False := by
  have hup : 3 * b * (Q * C) ≤ (b - 1) * (Q * C) := by
    calc
      _ = 3 * (b * Q) * C := by ring
      _ ≤ (b - 1) * N := floor_estimate
      _ ≤ (b - 1) * (Q * C) := Nat.mul_le_mul_left _ denominator
  have hprod : 0 < Q * C := Nat.mul_pos hQ hC
  have hbound : 3 * b ≤ b - 1 := Nat.le_of_mul_le_mul_right hup hprod
  omega

/-- Given the actual finite-floor correction estimate, the explicit
denominator forces one input below `2 ^ h * Q`. This theorem does not
postulate a global Collatz assertion or an S-unit result. -/
theorem finite_floor_descent (q : ℕ → ℕ) (h Q C N : ℕ)
    (hQ : 0 < Q) (hC : 0 < C)
    (denominator : N ≤ Q * C)
    (floor_estimate : ∀ Y : ℕ, (∀ i < h, Y ≤ q i) →
      3 * Y * C ≤ (2 ^ h - 1) * N) :
    ∃ i < h, q i < 2 ^ h * Q := by
  by_contra hn
  have hlarge : ∀ i < h, 2 ^ h * Q ≤ q i := by
    intro i hi
    by_contra hlt
    exact hn ⟨i, hi, by omega⟩
  exact finite_floor_contradiction Q C N (2 ^ h) hQ hC denominator
    (floor_estimate (2 ^ h * Q) hlarge) (Nat.two_pow_pos h)

/-- The cardinality-only packing step: subtracting one anchor injects
all marked times into zero together with the exceptional differences.
The largest exceptional difference is not needed. -/
theorem cardinality_from_anchor_differences (E H : Finset ℕ) (a : ℕ)
    (lower : ∀ x ∈ E, a ≤ x)
    (differences : ∀ x ∈ E, x ≠ a → x - a ∈ H) :
    E.card ≤ H.card + 1 := by
  calc
    _ ≤ (insert 0 H).card := by
      apply Finset.card_le_card_of_injOn (fun x => x - a)
      · intro x hx
        by_cases hxa : x = a
        · subst x
          simp
        · exact Finset.mem_insert_of_mem (differences x hx hxa)
      · intro x hx y hy heq
        change x - a = y - a at heq
        have hax := lower x hx
        have hay := lower y hy
        omega
    _ ≤ _ := Finset.card_insert_le 0 H

end CollatzDyadicCluster
