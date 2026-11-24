import ActualScalar
import StrictCarry
import Mathlib.Algebra.Order.Floor.Semiring


/-! The centered carries and canonical digits of the literal infinite odd-orbit scalar. -/
namespace Collatz.StrictCarry.Actual
open Collatz.CarryTowerRoundTen.ActualScalar
open Collatz.StrictCarry

set_option autoImplicit false

noncomputable def carry (q : ℕ) : ℕ := ⌈scalar q - 1/2⌉₊ - 1
noncomputable def phase (q : ℕ) : ℝ := scalar q - carry q
/-- The digit plus one on the right-closed ternary interval. It uses only the current phase. -/
noncomputable def canonical (q : ℕ) : ℕ := ⌈3 * (phase q - 1/2)⌉₊

theorem phase_bounds (q : ℕ) (hq : 0 < q) (ho : Odd q) :
    1/2 < phase q ∧ phase q ≤ 3/2 := by
  have hp : 0 < scalar q - 1/2 := sub_pos.mpr (scalar_strict_lower q hq ho)
  have hc : 1 ≤ ⌈scalar q-1/2⌉₊ := Nat.ceil_pos.mpr hp
  have hl := Nat.le_ceil (scalar q-1/2)
  have hu := Nat.ceil_lt_add_one hp.le
  unfold phase carry
  rw [Nat.cast_sub hc]
  push_cast
  constructor <;> linarith

theorem canonical_bounds (q : ℕ) (hq : 0 < q) (ho : Odd q) :
    1 ≤ canonical q ∧ canonical q ≤ 3 := by
  obtain ⟨hl,hu⟩ := phase_bounds q hq ho
  exact ⟨Nat.ceil_pos.mpr (by linarith),
    Nat.ceil_le.mpr (by push_cast; linarith)⟩

theorem actual_edge (q : ℕ) (hq : 0 < q) (ho : Odd q) :
    gap q + carry (oddMap q) = canonical q + 3*carry q := by
  let e := gap q + carry (oddMap q)
  let k := 3*carry q
  have es : (e : ℝ) - k = 3*phase q - phase (oddMap q) := by
    dsimp [e,k,phase]
    push_cast
    rw [scalar_recurrence q hq]
    ring
  obtain ⟨hl,hu⟩ := phase_bounds q hq ho
  obtain ⟨hl',hu'⟩ := phase_bounds (oddMap q) (oddMap_pos q) (oddMap_odd q)
  have hk : k < e := by
    have : (k : ℝ) < e := by linarith
    exact_mod_cast this
  have hc : canonical q = e-k := by
    apply (Nat.ceil_eq_iff (by omega : e-k ≠ 0)).mpr
    rw [Nat.cast_sub (by omega : 1 ≤ e-k), Nat.cast_sub hk.le]
    push_cast
    constructor <;> linarith
  change e = canonical q + k
  omega

/-- An extremal carry birth uses the largest canonical digit and a physical gap of one. -/
theorem saturated_gap (q : ℕ) (hq : 0 < q) (ho : Odd q)
    (hs : carry (oddMap q) = 3*carry q+2) :
    gap q = 1 ∧ canonical q = 3 := by
  have h := actual_edge q hq ho
  have hg := gap_pos q ho
  have hb := (canonical_bounds q hq ho).2
  omega

/-- A positive carry on an ordinary orbit must eventually incur a strict edge charge. -/
theorem positive_carry_forces_strict (q : ℕ) (hq : 0 < q) (ho : Odd q)
    (hc : 0 < carry q) :
    ∃ i : ℕ, strictEdge (carry (orbit q i)) (carry (orbit q (i+1))) = 1 := by
  by_contra! hn
  have grow (i : ℕ) (hp : 0 < carry (orbit q i)) :
      carry (orbit q (i+1)) = 3*carry (orbit q i)+2 := by
    have h := hn i
    by_contra! he
    simp [strictEdge, he, Nat.ne_of_gt hp] at h
  have pos (i : ℕ) : 0 < carry (orbit q i) := by
    induction i with
    | zero => exact hc
    | succ i ih => rw [grow i ih]; omega
  apply not_all_gaps_one q
  intro i
  exact (saturated_gap (orbit q i) (orbit_pos q i hq) (orbit_odd q i ho)
    (grow i (pos i))).1

/-- Large physical gaps can only occur on strictly charged edges. -/
theorem large_gap_strict (q : ℕ) (hq : 0 < q) (ho : Odd q)
    (hg : 4 ≤ gap q) :
    strictEdge (carry q) (carry (oddMap q)) = 1 := by
  have h := actual_edge q hq ho
  have hb := (canonical_bounds q hq ho).2
  have hz : ¬ (carry q = 0 ∧ carry (oddMap q) = 0) := by omega
  have hs : carry (oddMap q) ≠ 3*carry q+2 := by omega
  simp [strictEdge, hz, hs]

/-- An entire physical tail over the alphabet {1,2,3} has zero centered carry. -/
theorem zero_carry_of_small_gaps (q : ℕ) (hq : 0 < q)
    (hs : ∀ i, gap (orbit q i) ≤ 3) : carry q = 0 := by
  have maj : ∀ i : ℕ, term q i ≤ 3 * (1 / (3 : ℝ)^(i+1)) := by
    intro i
    unfold term
    have hi : (gap (orbit q i) : ℝ) ≤ 3 := by exact_mod_cast hs i
    calc
      _ ≤ 3 / (3 : ℝ)^(i+1) := div_le_div_of_nonneg_right hi (by positivity)
      _ = _ := by ring
  have hb := Summable.tsum_le_tsum maj (scalar_summable q hq) (baseline_summable.mul_left 3)
  rw [tsum_mul_left, baseline_sum] at hb
  change scalar q ≤ 3 * (1/2) at hb
  have hle : ⌈scalar q - 1/2⌉₊ ≤ 1 := Nat.ceil_le.mpr (by push_cast; linarith)
  unfold carry
  omega

private theorem orbit_add (q j k : ℕ) : orbit (orbit q j) k = orbit q (j+k) := by
  induction k with
  | zero => rfl
  | succ k ih => exact congrArg oddMap ih

/-- The infinite zero-charge tails are precisely the tails with bounded physical gap 3. -/
theorem no_strict_iff_small_gaps (q : ℕ) (hq : 0 < q) (ho : Odd q) :
    (∀ i, strictEdge (carry (orbit q i)) (carry (orbit q (i+1))) = 0) ↔
    (∀ i, gap (orbit q i) ≤ 3) := by
  constructor
  · intro hz i
    by_contra! hg
    have h := large_gap_strict _ (orbit_pos q i hq) (orbit_odd q i ho) (by omega)
    have h1 : strictEdge (carry (orbit q i)) (carry (orbit q (i+1))) = 1 := h
    have h0 := hz i
    omega
  · intro hs i
    have hz (j : ℕ) : carry (orbit q j) = 0 := by
      apply zero_carry_of_small_gaps _ (orbit_pos q j hq)
      intro k
      simpa [orbit_add] using hs (j+k)
    simp [hz, strictEdge]

/-- All three powers are formed from this one fixed positive odd source. -/
theorem actual_interval_slack (q j n : ℕ) (hq : 0 < q) (ho : Odd q) :
    let x := fun i => orbit q (j+i)
    let J := ∑ i ∈ Finset.range n, strictEdge (carry (x i)) (carry (x (i+1)))
    4^J * 3^(∑ i ∈ Finset.range n, canonical (x i)) * (carry (x 0)+1)^2 ≤
    3^J * 3^(∑ i ∈ Finset.range n, gap (x i)) * (carry (x n)+1)^2 := by
  dsimp only
  apply interval_slack (fun i => gap (orbit q (j+i))) (fun i => canonical (orbit q (j+i)))
    (fun i => carry (orbit q (j+i))) n
  · intro i _
    exact gap_pos _ (orbit_odd q (j+i) ho)
  · intro i _
    exact (canonical_bounds _ (orbit_pos q (j+i) hq) (orbit_odd q (j+i) ho)).2
  · intro i _
    exact actual_edge _ (orbit_pos q (j+i) hq) (orbit_odd q (j+i) ho)

#print axioms phase_bounds
#print axioms canonical_bounds
#print axioms actual_edge
#print axioms saturated_gap
#print axioms positive_carry_forces_strict
#print axioms large_gap_strict
#print axioms zero_carry_of_small_gaps
#print axioms no_strict_iff_small_gaps
#print axioms actual_interval_slack
end Collatz.StrictCarry.Actual
