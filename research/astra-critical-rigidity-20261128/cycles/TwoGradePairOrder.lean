import Mathlib.RingTheory.Polynomial.Eisenstein.Basic
import Mathlib.RingTheory.Polynomial.GaussLemma
import Mathlib.RingTheory.Int.Basic
import Mathlib.FieldTheory.Minpoly.Field
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Integer pair comparisons on an octave-periodic spatial grid. -/

set_option autoImplicit false
namespace Collatz.TwoGradePairOrder
open Polynomial
open scoped BigOperators

private theorem octave_irreducible (p : ℕ) (hp : 0 < p) :
    Irreducible (X ^ p - C 2 : ℚ[X]) := by
  let f : ℤ[X] := X ^ p - C 2
  let I : Ideal ℤ := Ideal.span {2}
  have hm : f.Monic := monic_X_pow_sub_C 2 (by omega)
  have hi : I.IsPrime := Ideal.isPrime_span_singleton_of_prime
    (Int.prime_iff_natAbs_prime.mpr (by decide))
  have he : f.IsEisensteinAt I := hm.isEisensteinAt_of_mem_of_notMem hi.ne_top
    (by
      intro k hk
      have hk' : k < p := by
        change k < (X ^ p - C (2 : ℤ)).natDegree at hk
        rwa [natDegree_X_pow_sub_C] at hk
      change f.coeff k ∈ Ideal.span {2}
      rw [Ideal.mem_span_singleton]
      by_cases hz : k = 0
      · subst k
        simp only [f, coeff_sub, coeff_X_pow, coeff_C, hp.ne, ite_false, ite_true]
        norm_num
      · simp only [f, coeff_sub, coeff_X_pow, coeff_C, hz, Nat.ne_of_lt hk',
          ite_false, sub_zero, dvd_zero])
    (by
      change f.coeff 0 ∉ (Ideal.span {(2 : ℤ)}) ^ 2
      rw [Ideal.span_singleton_pow, Ideal.mem_span_singleton]
      simp only [f, coeff_sub, coeff_X_pow, coeff_C, hp.ne, ite_false, ite_true]
      norm_num)
  have hf : Irreducible f := he.irreducible hi hm.isPrimitive (by
    change 0 < (X ^ p - C (2 : ℤ)).natDegree
    rwa [natDegree_X_pow_sub_C])
  have h := (IsPrimitive.Int.irreducible_iff_irreducible_map_cast hm.isPrimitive).mp hf
  dsimp only [f] at h
  norm_num at h ⊢
  exact h

private theorem small_polynomial_nonzero (p : ℕ) (hp : 0 < p) (ξ : ℝ)
    (hξ : ξ ^ p = 2) (P : ℚ[X]) (hP : P ≠ 0) (hd : P.natDegree < p) :
    aeval ξ P ≠ 0 := by
  have root : aeval ξ (X ^ p - C 2 : ℚ[X]) = 0 := by simp [hξ]
  have eq := minpoly.eq_of_irreducible_of_monic (octave_irreducible p hp) root
    (monic_X_pow_sub_C 2 (by omega))
  intro hz
  have dvd := minpoly.dvd ℚ ξ hz
  rw [←eq] at dvd
  have lower := natDegree_le_of_dvd dvd hP
  simp only [natDegree_X_pow_sub_C] at lower
  omega

private theorem positive_step (x y d : ℤ) (b : ℕ)
    (hx : 0 < x) (hd : -2 ≤ d) (edge : 2 ^ b * y = 3 * x + d) : 0 < y := by
  have hn : 0 < 3 * x + d := by omega
  rw [←edge] at hn
  exact pos_of_mul_pos_right hn (by positivity)

private theorem negative_step (x y d : ℤ) (b : ℕ)
    (hx : x < 0) (hd : d ≤ 2) (edge : 2 ^ b * y = 3 * x + d) : y < 0 := by
  have hn : 3 * x + d < 0 := by omega
  rw [←edge] at hn
  exact neg_of_mul_neg_right hn (by positivity)

private noncomputable def weighted (p : ℕ) (ξ : ℝ) (Z : ℕ → ℤ) (a : ℕ) : ℝ :=
  ∑ r ∈ Finset.range p, (ξ⁻¹) ^ r * (Z (r + a) : ℝ)

private theorem weighted_shift (p : ℕ) (ξ : ℝ) (hξ : ξ ^ p = 2)
    (hpos : 0 < ξ) (Z : ℕ → ℤ) (hd : ∀ r, Z (p + r) = 2 * Z r)
    (a : ℕ) : weighted p ξ Z a = ξ ^ a * weighted p ξ Z 0 := by
  have hi : (ξ⁻¹) ^ p * 2 = 1 := by rw [inv_pow, hξ]; norm_num
  have step (a : ℕ) : ξ⁻¹ * weighted p ξ Z (a + 1) = weighted p ξ Z a := by
    have hs := Finset.sum_range_succ' (fun r => (ξ⁻¹) ^ r * (Z (r + a) : ℝ)) p
    rw [Finset.sum_range_succ] at hs
    have he : (ξ⁻¹) ^ p * (Z (p + a) : ℝ) = (Z a : ℝ) := by
      rw [hd a]
      push_cast
      rw [← mul_assoc, hi, one_mul]
    rw [he] at hs
    simp only [zero_add, pow_zero, one_mul] at hs
    have hm : (∑ r ∈ Finset.range p, (ξ⁻¹) ^ (r + 1) * (Z (r + 1 + a) : ℝ)) =
        ξ⁻¹ * weighted p ξ Z (a + 1) := by
      simp only [weighted, Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro r _
      rw [show r + 1 + a = r + (a + 1) by omega, pow_succ]
      ring
    rw [hm] at hs
    exact (add_right_cancel hs).symm
  induction a with
  | zero => simp
  | succ a ih =>
    have hs := step a
    rw [ih] at hs
    have hn : ξ ≠ 0 := ne_of_gt hpos
    calc
      weighted p ξ Z (a + 1) = ξ * (ξ⁻¹ * weighted p ξ Z (a + 1)) := by
        rw [← mul_assoc, mul_inv_cancel₀ hn, one_mul]
      _ = ξ * (ξ ^ a * weighted p ξ Z 0) := by rw [hs]
      _ = ξ ^ (a + 1) * weighted p ξ Z 0 := by rw [pow_succ]; ring

private theorem pair_polynomial_nonzero (i j k l : ℕ) (hij : i ≤ j) (hkl : k ≤ l)
    (different : i ≠ k ∨ j ≠ l) :
    (X ^ i + X ^ j - X ^ k - X ^ l : ℚ[X]) ≠ 0 := by
  intro hz
  have he : (X ^ i + X ^ j : ℚ[X]) = X ^ k + X ^ l := by
    linear_combination hz
  have hik : i = k := by
    by_contra hn
    rcases lt_or_gt_of_ne hn with h | h
    · have hc := congrArg (fun P : ℚ[X] => P.coeff i) he
      have hil : i ≠ l := by omega
      simp only [coeff_add, coeff_X_pow, ite_true, h.ne, hil, ite_false] at hc
      split_ifs at hc <;> norm_num at hc
    · have hc := congrArg (fun P : ℚ[X] => P.coeff k) he
      have hkj : k ≠ j := by omega
      simp only [coeff_add, coeff_X_pow, ite_true, h.ne, hkj, ite_false] at hc
      split_ifs at hc <;> norm_num at hc
  subst k
  have he' : (X ^ j : ℚ[X]) = X ^ l := add_left_cancel he
  have hjl : j = l := by
    have := congrArg Polynomial.natDegree he'
    simpa only [natDegree_X_pow] using this
  exact different.elim (fun h => h rfl) (fun h => h hjl)

private theorem pair_polynomial_degree (p i j k l : ℕ)
    (hi : i < p) (hj : j < p) (hk : k < p) (hl : l < p) :
    (X ^ i + X ^ j - X ^ k - X ^ l : ℚ[X]).natDegree < p := by
  apply lt_of_le_of_lt (natDegree_sub_le _ _) (max_lt ?_ ?_)
  · apply lt_of_le_of_lt (natDegree_sub_le _ _) (max_lt ?_ ?_)
    · apply lt_of_le_of_lt (natDegree_add_le _ _) (max_lt ?_ ?_)
      · simpa only [natDegree_X_pow] using hi
      · simpa only [natDegree_X_pow] using hj
    · simpa only [natDegree_X_pow] using hk
  · simpa only [natDegree_X_pow] using hl

private theorem sign_trichotomy {α : Type*} (H : α → ℤ) (σ : α → α)
    (reach : ∀ r s, ∃ n : ℕ, (σ^[n]) r = s) (b : α → ℕ) (d : α → ℤ)
    (lower : ∀ r, -2 ≤ d r) (upper : ∀ r, d r ≤ 2)
    (edge : ∀ r, 2 ^ b r * H (σ r) = 3 * H r + d r) :
    (∀ r, 0 < H r) ∨ (∀ r, H r = 0) ∨ (∀ r, H r < 0) := by
  classical
  by_cases hz : ∀ r, H r = 0
  · exact Or.inr (Or.inl hz)
  push Not at hz
  obtain ⟨r, hr⟩ := hz
  rcases lt_or_gt_of_ne hr with hn | hp
  · right; right
    intro s
    obtain ⟨n, hn'⟩ := reach r s
    have iter (n : ℕ) : H ((σ^[n]) r) < 0 := by
      induction n with
      | zero => simpa using hn
      | succ n ih =>
        rw [Function.iterate_succ_apply']
        exact negative_step _ _ _ _ ih (upper _) (edge _)
    simpa only [hn'] using iter n
  · left
    intro s
    obtain ⟨n, hn'⟩ := reach r s
    have iter (n : ℕ) : 0 < H ((σ^[n]) r) := by
      induction n with
      | zero => simpa using hp
      | succ n ih =>
        rw [Function.iterate_succ_apply']
        exact positive_step _ _ _ _ ih (lower _) (edge _)
    simpa only [hn'] using iter n

private theorem weighted_pair (p : ℕ) (ξ : ℝ) (hξ : ξ ^ p = 2)
    (hpos : 0 < ξ) (Z : ℕ → ℤ) (hd : ∀ r, Z (p + r) = 2 * Z r)
    (i j k l : ℕ) :
    weighted p ξ (fun r => Z (r+i) + Z (r+j) - Z (r+k) - Z (r+l)) 0 =
      (ξ^i + ξ^j - ξ^k - ξ^l) * weighted p ξ Z 0 := by
  unfold weighted
  simp only [Nat.add_zero, Int.cast_sub, Int.cast_add, mul_sub, mul_add,
    Finset.sum_sub_distrib, Finset.sum_add_distrib]
  change weighted p ξ Z i + weighted p ξ Z j - weighted p ξ Z k -
      weighted p ξ Z l = _
  rw [weighted_shift p ξ hξ hpos Z hd i, weighted_shift p ξ hξ hpos Z hd j,
    weighted_shift p ξ hξ hpos Z hd k, weighted_shift p ξ hξ hpos Z hd l]
  simp only [weighted, Nat.add_zero]
  ring

/-- An integer octave with its complete common rank transition and actual tags.
The physical Collatz chart construction is not assumed as a theorem of Lean. -/
structure IntegerOctave (p W : ℕ) where
  label : ℕ → ℤ
  tag : ℕ → ℤ
  shift : Fin p → Fin p
  winding : Fin p → ℕ
  doubling : ∀ r, label (p+r) = 2 * label r
  positive : ∀ r, r < p → 0 < label r
  tags : ∀ r, r < p → ∀ j, j ≤ W → 1 ≤ tag (r+j) ∧ tag (r+j) ≤ 2
  edge : ∀ r : Fin p, ∀ j, j ≤ W →
    2 ^ winding r * label ((shift r).val+j) = 3 * label (r.val+j) + tag (r.val+j)
  transitive : ∀ r s, ∃ n : ℕ, (shift^[n]) r = s

/-- Every distinct ordered pair comparison has its geometric sign throughout
the entire integer rank cycle, including pairs with repeated entries. -/
theorem comparison_sign (p W : ℕ) (hp : 0 < p) (hW : W < p)
    (grid : IntegerOctave p W) (ξ : ℝ) (hξ : ξ^p = 2) (hpos : 0 < ξ)
    (i j k l : ℕ) (hij : i ≤ j) (hj : j ≤ W) (hkl : k ≤ l) (hl : l ≤ W)
    (different : i ≠ k ∨ j ≠ l) (r : Fin p) :
    let H := grid.label (r.val+i) + grid.label (r.val+j) -
      grid.label (r.val+k) - grid.label (r.val+l)
    let Q := ξ^i + ξ^j - ξ^k - ξ^l
    (0 < H ↔ 0 < Q) ∧ (H < 0 ↔ Q < 0) ∧ H ≠ 0 := by
  let H : ℕ → ℤ := fun r => grid.label (r+i) + grid.label (r+j) -
    grid.label (r+k) - grid.label (r+l)
  let d : Fin p → ℤ := fun r => grid.tag (r.val+i) + grid.tag (r.val+j) -
    grid.tag (r.val+k) - grid.tag (r.val+l)
  let Q : ℝ := ξ^i + ξ^j - ξ^k - ξ^l
  change (0 < H r.val ↔ 0 < Q) ∧ (H r.val < 0 ↔ Q < 0) ∧ H r.val ≠ 0
  have hi : i ≤ W := hij.trans hj
  have hk : k ≤ W := hkl.trans hl
  have dbounds (s : Fin p) : -2 ≤ d s ∧ d s ≤ 2 := by
    have h₁ := grid.tags s.val s.isLt i hi
    have h₂ := grid.tags s.val s.isLt j hj
    have h₃ := grid.tags s.val s.isLt k hk
    have h₄ := grid.tags s.val s.isLt l hl
    dsimp only [d]
    omega
  have edge (s : Fin p) :
      2 ^ grid.winding s * H (grid.shift s).val = 3 * H s.val + d s := by
    have h₁ := grid.edge s i hi
    have h₂ := grid.edge s j hj
    have h₃ := grid.edge s k hk
    have h₄ := grid.edge s l hl
    dsimp only [H, d]
    linear_combination h₁ + h₂ - h₃ - h₄
  have qne : Q ≠ 0 := by
    have hd := pair_polynomial_degree p i j k l (hi.trans_lt hW) (hj.trans_lt hW)
      (hk.trans_lt hW) (hl.trans_lt hW)
    have hn := small_polynomial_nonzero p hp ξ hξ _
      (pair_polynomial_nonzero i j k l hij hkl different) hd
    simpa [Q] using hn
  have basepos : 0 < weighted p ξ grid.label 0 := by
    unfold weighted
    apply Finset.sum_pos
    · intro s hs
      have ht : 0 < (grid.label (s+0) : ℝ) := by
        exact_mod_cast grid.positive s (Finset.mem_range.mp hs)
      exact mul_pos (pow_pos (inv_pos.mpr hpos) _) ht
    · exact Finset.nonempty_range_iff.mpr hp.ne'
  have mean : weighted p ξ H 0 = Q * weighted p ξ grid.label 0 :=
    weighted_pair p ξ hξ hpos grid.label grid.doubling i j k l
  rcases sign_trichotomy (fun s : Fin p => H s.val) grid.shift grid.transitive
      grid.winding d (fun s => (dbounds s).1) (fun s => (dbounds s).2) edge with
      pos | zero | neg
  · have sumpos : 0 < weighted p ξ H 0 := by
      unfold weighted
      apply Finset.sum_pos
      · intro s hs
        have h : 0 < (H (s+0) : ℝ) := by
          exact_mod_cast pos ⟨s, Finset.mem_range.mp hs⟩
        exact mul_pos (pow_pos (inv_pos.mpr hpos) _) h
      · exact Finset.nonempty_range_iff.mpr hp.ne'
    rw [mean] at sumpos
    have hQ : 0 < Q := (mul_pos_iff_of_pos_right basepos).mp sumpos
    exact ⟨iff_of_true (pos r) hQ,
      iff_of_false (not_lt_of_ge (pos r).le) (not_lt_of_ge hQ.le), ne_of_gt (pos r)⟩
  · have hs : weighted p ξ H 0 = 0 := by
      unfold weighted
      apply Finset.sum_eq_zero
      intro s hs
      have h := zero ⟨s, Finset.mem_range.mp hs⟩
      simp only [Nat.add_zero, h, Int.cast_zero, mul_zero]
    rw [mean] at hs
    exact False.elim ((mul_ne_zero qne (ne_of_gt basepos)) hs)
  · have sumneg : weighted p ξ H 0 < 0 := by
      unfold weighted
      apply Finset.sum_neg
      · intro s hs
        have h : (H (s+0) : ℝ) < 0 := by
          exact_mod_cast neg ⟨s, Finset.mem_range.mp hs⟩
        exact mul_neg_of_pos_of_neg (pow_pos (inv_pos.mpr hpos) _) h
      · exact Finset.nonempty_range_iff.mpr hp.ne'
    rw [mean] at sumneg
    have hQ : Q < 0 := neg_of_mul_neg_left sumneg basepos.le
    exact ⟨iff_of_false (not_lt_of_ge (neg r).le) (not_lt_of_ge hQ.le),
      iff_of_true (neg r) hQ, ne_of_lt (neg r)⟩

/-- In a short interval of the integer octave, equality of unordered pair sums
determines both entries after sorting, with no geometric parameter supplied. -/
theorem pair_sum_injective (p W : ℕ) (hp : 0 < p) (hW : W < p)
    (grid : IntegerOctave p W) (i j k l : ℕ)
    (hij : i ≤ j) (hj : j ≤ W) (hkl : k ≤ l) (hl : l ≤ W) (r : Fin p)
    (equal : grid.label (r.val+i) + grid.label (r.val+j) =
      grid.label (r.val+k) + grid.label (r.val+l)) : i = k ∧ j = l := by
  classical
  by_contra different
  push Not at different
  have hd : i ≠ k ∨ j ≠ l := by
    by_cases h : i = k
    · exact Or.inr (different h)
    · exact Or.inl h
  let ξ : ℝ := (2 : ℝ) ^ ((p : ℝ)⁻¹)
  have hpos : 0 < ξ := by dsimp [ξ]; positivity
  have hξ : ξ ^ p = 2 := Real.rpow_inv_natCast_pow (by norm_num) hp.ne'
  have hn := (comparison_sign p W hp hW grid ξ hξ hpos i j k l hij hj hkl hl hd r).2.2
  apply hn
  omega

#print axioms comparison_sign
#print axioms pair_sum_injective
end Collatz.TwoGradePairOrder
