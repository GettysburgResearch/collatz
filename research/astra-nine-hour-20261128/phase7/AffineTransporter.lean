import Mathlib.NumberTheory.Padics.PadicVal.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Data.List.Induction

/-! Exact rational arithmetic behind the finite affine-transporter search.
The analytic measure classification is not a hypothesis or conclusion here.
Positive gap words use A_e(z) = (1 + 3z) / 2^e, in composition order.
-/

namespace Collatz.AffineTransporter

instance : Fact (Nat.Prime 2) := ⟨Nat.prime_two⟩

def Valid (w : List ℕ) : Prop := ∀ e ∈ w, 0 < e

def slope (w : List ℕ) : ℚ := 3 ^ w.length / 2 ^ w.sum

def offset : List ℕ → ℚ
  | [] => 0
  | e :: w => (1 + 3 * offset w) / 2 ^ e

theorem slope_ne_zero (w : List ℕ) : slope w ≠ 0 := by
  unfold slope
  positivity

theorem offset_nonneg (w : List ℕ) : 0 ≤ offset w := by
  induction w with
  | nil => rfl
  | cons e w ih =>
    dsimp [offset]
    positivity

theorem offset_pos {w : List ℕ} (hne : w ≠ []) : 0 < offset w := by
  cases w with
  | nil => contradiction
  | cons e w =>
    have := offset_nonneg w
    dsimp [offset]
    positivity

theorem valid_tail {e : ℕ} {w : List ℕ} (h : Valid (e :: w)) : Valid w := by
  intro x hx
  exact h x (List.mem_cons_of_mem e hx)

theorem valid_sum_pos {w : List ℕ} (h : Valid w) (hne : w ≠ []) : 0 < w.sum := by
  cases w with
  | nil => contradiction
  | cons e w =>
    have he := h e (by simp)
    simp only [List.sum_cons]
    omega

theorem two_value : padicValRat 2 (2 : ℚ) = 1 := by
  exact padicValRat.self (by decide)

theorem three_value : padicValRat 2 (3 : ℚ) = 0 := by
  change padicValRat 2 ((3 : ℕ) : ℚ) = 0
  rw [padicValRat.of_nat]
  have h : padicValNat 2 3 = 0 := padicValNat.eq_zero_of_not_dvd (by decide)
  exact_mod_cast h

theorem slope_value (w : List ℕ) : padicValRat 2 (slope w) = -(w.sum : ℤ) := by
  rw [slope, padicValRat.div (by positivity) (by positivity),
    padicValRat.pow, padicValRat.pow, three_value, two_value]
  ring

/-- Every nonempty positive-gap offset has exact reduced dyadic denominator. -/
theorem offset_value {w : List ℕ} (h : Valid w) (hne : w ≠ []) :
    padicValRat 2 (offset w) = -(w.sum : ℤ) := by
  induction w with
  | nil => contradiction
  | cons e w ih =>
    have he := h e (by simp)
    have ht := valid_tail h
    cases w with
    | nil =>
      simp only [offset, mul_zero, add_zero, List.sum_cons, List.sum_nil,
        add_zero, one_div, padicValRat.inv, padicValRat.pow, two_value, mul_one]
    | cons f v =>
      have hw : f :: v ≠ [] := by simp
      have hv := ih ht hw
      have hp := offset_pos hw
      have hs := valid_sum_pos ht hw
      have hm : padicValRat 2 (3 * offset (f :: v)) = -((f :: v).sum : ℤ) := by
        rw [padicValRat.mul (by norm_num) (ne_of_gt hp), three_value, hv, zero_add]
      have hn : 1 + 3 * offset (f :: v) ≠ 0 := by positivity
      have ha := padicValRat.add_eq_min hn (by norm_num : (1 : ℚ) ≠ 0)
        (by positivity : 3 * offset (f :: v) ≠ 0)
        (show padicValRat 2 (1 : ℚ) ≠ padicValRat 2 (3 * offset (f :: v)) by
          rw [padicValRat.one, hm]
          omega)
      rw [padicValRat.one, hm, min_eq_right (by omega)] at ha
      rw [offset, padicValRat.div hn (by positivity), ha,
        padicValRat.pow, two_value, mul_one]
      simp only [List.sum_cons, Nat.cast_add]
      ring

theorem slope_cons (e : ℕ) (w : List ℕ) :
    slope (e :: w) = 3 * slope w / 2 ^ e := by
  simp only [slope, List.length_cons, List.sum_cons, pow_succ, pow_add]
  ring

theorem slope_append (u v : List ℕ) : slope (u ++ v) = slope u * slope v := by
  simp only [slope, List.length_append, List.sum_append, pow_add]
  ring

theorem offset_append (u v : List ℕ) :
    offset (u ++ v) = offset u + slope u * offset v := by
  induction u with
  | nil => simp [offset, slope]
  | cons e u ih =>
    simp only [List.cons_append, offset, ih, slope_cons]
    ring

/-- The last-letter offsets cancel when the two full slopes match. -/
theorem last_letter_cancellation (u v : List ℕ) (e f : ℕ) (L : ℚ)
    (hs : slope (u ++ [e]) = L * slope (v ++ [f])) :
    offset (u ++ [e]) - L * offset (v ++ [f]) = offset u - L * offset v := by
  rw [slope_append, slope_append] at hs
  have single (j : ℕ) : slope [j] = 3 / 2 ^ j := by simp [slope]
  rw [single e, single f] at hs
  have hc : (3 : ℚ) ≠ 0 := by norm_num
  have hd : slope u / 2 ^ e = L * (slope v / 2 ^ f) := by
    apply (mul_right_inj' hc).mp
    convert hs using 1 <;> ring
  simp only [offset_append, offset, mul_zero, add_zero, one_div]
  calc
    _ = offset u - L * offset v + (slope u / 2 ^ e - L * (slope v / 2 ^ f)) := by ring
    _ = offset u - L * offset v := by rw [hd]; ring

theorem multiplier_value (a b : ℤ) :
    padicValRat 2 ((2 : ℚ)^a * (3 : ℚ)^b) = a := by
  rw [padicValRat.mul (zpow_ne_zero _ (by norm_num)) (zpow_ne_zero _ (by norm_num)),
    padicValRat.zpow, padicValRat.zpow, two_value, three_value]
  ring

theorem equal_offset_budget (u v : List ℕ) (hu : Valid u) (hv : Valid v)
    (h : offset u = offset v) : u.sum = v.sum := by
  by_cases he : u = []
  · subst u
    by_cases hf : v = []
    · subst v; rfl
    · have hp := offset_pos hf
      rw [← h] at hp
      exact (lt_irrefl 0 hp).elim
  · by_cases hf : v = []
    · subst v
      have hp := offset_pos he
      rw [h] at hp
      exact (lt_irrefl 0 hp).elim
    · have hh := congrArg (padicValRat 2) h
      rw [offset_value hu he, offset_value hv hf] at hh
      have : (u.sum : ℤ) = v.sum := by omega
      exact_mod_cast this

/-- The genuine rational positive-gap maps form a free monoid.
This proof uses their exact dyadic denominators and removes final letters. -/
theorem word_freeness (u v : List ℕ) (hu : Valid u) (hv : Valid v)
    (hs : slope u = slope v) (ho : offset u = offset v) : u = v := by
  induction u using List.reverseRecOn generalizing v with
  | nil =>
    by_cases he : v = []
    · exact he.symm
    · have hp := offset_pos he
      rw [← ho] at hp
      exact (lt_irrefl 0 hp).elim
  | append_singleton u e ih =>
    rcases List.eq_nil_or_concat' v with rfl | ⟨v,f,rfl⟩
    · have hp := offset_pos (show u ++ [e] ≠ [] by simp)
      rw [ho] at hp
      exact (lt_irrefl 0 hp).elim
    · have hu' : Valid u := by
        intro x hx
        exact hu x (List.mem_append_left [e] hx)
      have hv' : Valid v := by
        intro x hx
        exact hv x (List.mem_append_left [f] hx)
      have hl := last_letter_cancellation u v e f 1 (by simpa using hs)
      have ho' : offset u = offset v := by
        have hz : offset u - offset v = 0 := by simpa [ho] using hl.symm
        exact sub_eq_zero.mp hz
      have hb := equal_offset_budget u v hu' hv' ho'
      have hp := congrArg (padicValRat 2) hs
      rw [slope_value, slope_value] at hp
      simp only [List.sum_append, List.sum_singleton, hb] at hp
      have hef : e = f := by omega
      subst f
      have hs' : slope u = slope v := by
        rw [slope_append, slope_append] at hs
        exact mul_right_cancel₀ (slope_ne_zero [e]) hs
      exact congrArg (fun w => w ++ [e]) (ih v hu' hv' hs' ho')

/-- Unequal dyadic valuations give the finite bounds for both prefix budgets.
Empty prefixes are retained, including when the rational offset has positive
2-adic valuation. -/
theorem prefix_bounds (u v : List ℕ) (hu : Valid u) (hv : Valid v)
    (L c : ℚ) (a : ℤ) (hL : L ≠ 0) (hval : padicValRat 2 L = a)
    (hc : c = offset u - L * offset v) (hc0 : c ≠ 0)
    (hd : a + (u.sum : ℤ) - (v.sum : ℤ) ≠ 0) :
    (u.sum : ℤ) ≤ max 0 (-padicValRat 2 c) ∧
      (v.sum : ℤ) ≤ max 0 (-padicValRat 2 c + a) := by
  by_cases heu : u = []
  · subst u
    have hev : v ≠ [] := by intro h; subst v; simp [offset] at hc; exact hc0 hc
    have hp := offset_pos hev
    have he : padicValRat 2 c = a - (v.sum : ℤ) := by
      rw [hc]
      simp only [offset, zero_sub, padicValRat.neg]
      rw [padicValRat.mul hL (ne_of_gt hp), hval, offset_value hv hev]
      ring
    simp only [List.sum_nil, Nat.cast_zero]
    rw [he]
    constructor <;> omega
  · by_cases hev : v = []
    · subst v
      have he : padicValRat 2 c = -(u.sum : ℤ) := by
        rw [hc]
        simp only [offset, mul_zero, sub_zero]
        exact offset_value hu heu
      simp only [List.sum_nil, Nat.cast_zero]
      rw [he]
      constructor <;> omega
    · have hpu := offset_pos heu
      have hpv := offset_pos hev
      have hm : padicValRat 2 (-(L * offset v)) = a - (v.sum : ℤ) := by
        rw [padicValRat.neg, padicValRat.mul hL (ne_of_gt hpv),
          hval, offset_value hv hev]
        ring
      have ha := padicValRat.add_eq_min
        (show offset u + -(L * offset v) ≠ 0 by simpa [hc, sub_eq_add_neg] using hc0)
        (ne_of_gt hpu) (neg_ne_zero.mpr (mul_ne_zero hL (ne_of_gt hpv)))
        (show padicValRat 2 (offset u) ≠ padicValRat 2 (-(L * offset v)) by
          rw [offset_value hu heu, hm]
          omega)
      rw [offset_value hu heu, hm] at ha
      have he : padicValRat 2 c = min (-(u.sum : ℤ)) (a - (v.sum : ℤ)) := by
        simpa only [← sub_eq_add_neg, ← hc] using ha
      rw [he]
      constructor <;> omega

/-- Any matching pair with different final gaps lies in the finite search
box determined only by the requested affine transformation. -/
theorem reduced_match_bounds (u v : List ℕ) (hu : Valid u) (hv : Valid v)
    (e f : ℕ) (hef : e ≠ f) (a b : ℤ) (c : ℚ) (hc0 : c ≠ 0)
    (hs : slope (u ++ [e]) = ((2 : ℚ)^a * (3 : ℚ)^b) * slope (v ++ [f]))
    (hc : c = offset (u ++ [e]) - ((2 : ℚ)^a * (3 : ℚ)^b) * offset (v ++ [f])) :
    (u.sum : ℤ) ≤ max 0 (-padicValRat 2 c) ∧
      (v.sum : ℤ) ≤ max 0 (-padicValRat 2 c + a) := by
  let L : ℚ := 2^a * 3^b
  have hL : L ≠ 0 := mul_ne_zero (zpow_ne_zero _ (by norm_num))
    (zpow_ne_zero _ (by norm_num))
  have hval : padicValRat 2 L = a := multiplier_value a b
  have hc' : c = offset u - L * offset v :=
    hc.trans (last_letter_cancellation u v e f L hs)
  have hp := congrArg (padicValRat 2) hs
  rw [slope_value, padicValRat.mul hL (slope_ne_zero _), hval, slope_value] at hp
  simp only [List.sum_append, List.sum_singleton, Nat.cast_add] at hp
  have hd : a + (u.sum : ℤ) - (v.sum : ℤ) ≠ 0 := by
    intro hz
    have : (e : ℤ) = f := by omega
    exact hef (by exact_mod_cast this)
  exact prefix_bounds u v hu hv L c a hL hval hc' hc0 hd

end Collatz.AffineTransporter
