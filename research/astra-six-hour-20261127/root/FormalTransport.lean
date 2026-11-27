import Mathlib.Data.Rat.Cast.Order
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
Finite arithmetic behind the corrected real-fibre transport.

`InverseTrace a es x` retains the same ordinary positive integer states and
the same ordered division exponents throughout. Its edge equality is the
literal odd Collatz equation; oddness of both endpoints and positivity of
the exponent ensure that the supplied division is complete.

No measure, density limit, or universal existence of a trace is postulated.
-/

namespace Collatz.SixHour.FormalTransport

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

def scale : List ℕ → K
  | [] => 1
  | e :: es => (3 / (2 : K)^e) * scale es

def offset : List ℕ → K
  | [] => 0
  | e :: es => 1 / (2 : K)^e + (3 / (2 : K)^e) * offset es

inductive InverseTrace : ℕ → List ℕ → ℕ → Prop where
  | nil (a : ℕ) (ha : 0 < a) (hoa : a % 2 = 1) : InverseTrace a [] a
  | cons {a x y e : ℕ} {es : List ℕ}
      (ha : 0 < a) (hoa : a % 2 = 1) (he : 0 < e)
      (edge : 2^e * a = 3*x+1) (tail : InverseTrace x es y) :
      InverseTrace a (e :: es) y

/- The recursive convention is the repository's `EscapeCore.oddCore`. -/
def oddCore (n : ℕ) : ℕ :=
  if h₀ : n = 0 then 0
  else if n % 2 = 0 then oddCore (n/2) else n
termination_by n
decreasing_by omega

theorem core_double (n : ℕ) : oddCore (2*n) = oddCore n := by
  by_cases hn : n = 0
  · simp [hn]
  · have h : 2*n ≠ 0 := by omega
    rw [oddCore.eq_def (2*n)]
    simp [h]

theorem core_power_two (e a : ℕ) : oddCore (2^e*a) = oddCore a := by
  induction e with
  | zero => simp
  | succ e ih =>
    calc
      oddCore (2^(e+1)*a) = oddCore (2*(2^e*a)) := by congr 1; ring
      _ = oddCore (2^e*a) := core_double _
      _ = oddCore a := ih

theorem core_odd {a : ℕ} (hoa : a % 2 = 1) : oddCore a = a := by
  have ha : a ≠ 0 := by omega
  rw [oddCore.eq_def a]
  simp [ha, hoa]

def oddStep (x : ℕ) : ℕ := oddCore (3*x+1)

theorem edge_odd_step {a x e : ℕ} (hoa : a % 2 = 1)
    (edge : 2^e * a = 3*x+1) : oddStep x = a := by
  unfold oddStep
  rw [← edge, core_power_two]
  exact core_odd hoa

theorem trace_root_pos {a x : ℕ} {es : List ℕ} (tr : InverseTrace a es x) :
    0 < a := by
  cases tr with
  | nil _ ha _ => exact ha
  | cons ha _ _ _ _ => exact ha

theorem trace_source_pos {a x : ℕ} {es : List ℕ} (tr : InverseTrace a es x) :
    0 < x := by
  induction tr with
  | nil _ ha _ => exact ha
  | cons _ _ _ _ _ ih => exact ih

theorem trace_source_odd {a x : ℕ} {es : List ℕ} (tr : InverseTrace a es x) :
    x % 2 = 1 := by
  induction tr with
  | nil _ _ hoa => exact hoa
  | cons _ _ _ _ _ ih => exact ih

/-- The trace is an actual orbit segment of the completely accelerated odd map. -/
theorem trace_actual_iterate {a x : ℕ} {es : List ℕ} (tr : InverseTrace a es x) :
    oddStep^[es.length] x = a := by
  induction tr with
  | nil => rfl
  | cons _ hoa _ edge _ ih =>
    rw [List.length_cons, Function.iterate_succ_apply', ih]
    exact edge_odd_step hoa edge

theorem scale_pos (es : List ℕ) : 0 < scale (K := K) es := by
  induction es with
  | nil => simp [scale]
  | cons e es ih => exact mul_pos (by positivity) ih

theorem offset_nonneg (es : List ℕ) : 0 ≤ offset (K := K) es := by
  induction es with
  | nil => simp [offset]
  | cons e es ih =>
    exact add_nonneg (by positivity) (mul_nonneg (by positivity) ih)

theorem offset_pos {es : List ℕ} (h : es ≠ []) : 0 < offset (K := K) es := by
  cases es with
  | nil => exact False.elim (h rfl)
  | cons e es =>
    exact add_pos_of_pos_of_nonneg (by positivity)
      (mul_nonneg (by positivity) (offset_nonneg es))

theorem trace_affine {a x : ℕ} {es : List ℕ} (tr : InverseTrace a es x) :
    (a : K) = scale es * x + offset es := by
  induction tr with
  | nil => simp [scale, offset]
  | @cons a y x e es ha hoa he edge tail ih =>
    have hedge : (2 : K)^e * a = 3*(y : K)+1 := by exact_mod_cast edge
    have hn : (2 : K)^e ≠ 0 := by positivity
    dsimp only [scale, offset]
    rw [ih] at hedge
    field_simp
    nlinarith [hedge]

theorem offset_lt_root {a x : ℕ} {es : List ℕ} (tr : InverseTrace a es x) :
    offset (K := K) es < a := by
  have hx : (0 : K) < x := by exact_mod_cast trace_source_pos tr
  rw [trace_affine tr]
  exact lt_add_of_pos_left _ (mul_pos (scale_pos es) hx)

theorem trace_complement {a x : ℕ} {es : List ℕ} (tr : InverseTrace a es x) :
    1 - offset (K := K) es / a = scale es * x / a := by
  have ha : (a : K) ≠ 0 := ne_of_gt (by exact_mod_cast trace_root_pos tr)
  have h := trace_affine (K := K) tr
  field_simp
  linarith

def mark (f a r : K) : K := f * (1-r/a)

/-- Algebraic transport at the original source and target, before a limit is taken. -/
theorem exact_mark_transport {a x : ℕ} {es : List ℕ} (tr : InverseTrace a es x)
    (fa fx r : K) (hc : fx = fa * scale es * x / a) :
    mark fa a (offset es + scale es * r) = mark fx x r := by
  have ha : (a : K) ≠ 0 := ne_of_gt (by exact_mod_cast trace_root_pos tr)
  have hx : (x : K) ≠ 0 := ne_of_gt (by exact_mod_cast trace_source_pos tr)
  have h := trace_affine (K := K) tr
  dsimp only [mark]
  rw [hc]
  field_simp
  rw [h]
  ring

/-- A positive suffix mark is equivalent to a real suffix below that same integer. -/
theorem mark_pos_iff {f a r : K} (hf : 0 < f) (ha : 0 < a) :
    0 < mark f a r ↔ r < a := by
  unfold mark
  rw [mul_pos_iff_of_pos_left hf, sub_pos, div_lt_one ha]

theorem mark_neg_iff {f a r : K} (hf : 0 < f) (ha : 0 < a) :
    mark f a r < 0 ↔ a < r := by
  unfold mark
  rw [mul_neg_iff]
  simp only [hf, not_lt_of_gt hf, false_and, or_false, true_and,
    sub_neg, one_lt_div ha]

/-- Every nonempty positive ordinary return has a strictly contracting affine slope. -/
theorem return_scale_lt_one {a : ℕ} {es : List ℕ}
    (tr : InverseTrace a es a) (hne : es ≠ []) : scale (K := K) es < 1 := by
  have ha : (0 : K) < a := by exact_mod_cast trace_root_pos tr
  have hb := offset_pos (K := K) hne
  have h := trace_affine (K := K) tr
  nlinarith

end Collatz.SixHour.FormalTransport
