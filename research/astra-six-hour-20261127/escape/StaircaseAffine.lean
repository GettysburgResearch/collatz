import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Finite affine identities for literal ordinary shortcut words and their
growing-run directives. The endpoint in the main result belongs to the same
actual finite trajectory as the source. -/

namespace StaircaseAffine

def inv : List Bool → ℚ → ℚ
  | [], y => y
  | false :: w, y => 2 * inv w y
  | true :: w, y => (2 * inv w y - 1) / 3

def slope : List Bool → ℚ
  | [] => 1
  | false :: w => 2 * slope w
  | true :: w => (2 / 3) * slope w

inductive Follows : List Bool → ℤ → ℤ → Prop
  | nil (x : ℤ) : Follows [] x x
  | even {w : List Bool} {u y : ℤ} : Follows w u y → Follows (false :: w) (2*u) y
  | odd {w : List Bool} {u y : ℤ} :
      Follows w (3*u-1) y → Follows (true :: w) (2*u-1) y

theorem inverse_ordinary {w : List Bool} {x y : ℤ} (h : Follows w x y) :
    (x : ℚ) = inv w y := by
  induction h with
  | nil => rfl
  | even h ih => simp only [Int.cast_mul, Int.cast_ofNat, inv, ih]
  | odd h ih =>
    push_cast at ih ⊢
    simp only [inv]
    linarith

theorem inverse_append (u v : List Bool) (x : ℚ) : inv (u ++ v) x = inv u (inv v x) := by
  induction u with
  | nil => rfl
  | cons b w ih => cases b <;> simp [inv, ih]

theorem centered (w : List Bool) (x b : ℚ) :
    inv w x - inv w b = slope w * (x-b) := by
  induction w with
  | nil => simp [inv, slope]
  | cons c w ih =>
    cases c <;> simp only [inv, slope] <;> linarith

def copies (w : List Bool) : ℕ → List Bool
  | 0 => []
  | n+1 => w ++ copies w n

theorem copies_at_fixed (w : List Bool) (b x : ℚ) (hb : inv w b = b) (n : ℕ) :
    inv (copies w n) x - b = slope w ^ n * (x-b) := by
  induction n with
  | zero => simp [copies, inv]
  | succ n ih =>
    rw [copies, inverse_append]
    have h := centered w (inv (copies w n) x) b
    rw [hb, ih] at h
    rw [h, pow_succ]
    ring

def tri : ℕ → ℕ
  | 0 => 0
  | n+1 => tri n + n

def directive (v u : List Bool) : ℕ → List Bool
  | 0 => []
  | n+1 => directive v u n ++ (copies v n ++ u)

theorem finite_tschakaloff (v u : List Bool) (b : ℚ) (hb : inv v b = b)
    (n : ℕ) (x : ℚ) :
    inv (directive v u n) x - b =
      (inv u b-b) * (∑ j ∈ Finset.range n, (slope v * slope u)^j * slope v^(tri j)) +
      slope u^n * slope v^(tri n) * (x-b) := by
  induction n generalizing x with
  | zero => simp [directive, inv, tri]
  | succ n ih =>
    rw [directive, inverse_append, inverse_append, ih, copies_at_fixed v b (inv u x) hb]
    have h := centered u x b
    have h' : inv u x - b = (inv u b-b) + slope u*(x-b) := by linarith
    rw [h', Finset.sum_range_succ, tri, pow_add, pow_succ, mul_pow]
    ring

theorem ordinary_finite_tschakaloff (v u : List Bool) (b : ℚ) (hb : inv v b = b)
    (n : ℕ) {x y : ℤ} (h : Follows (directive v u n) x y) :
    (x : ℚ) - b =
      (inv u b-b) * (∑ j ∈ Finset.range n, (slope v * slope u)^j * slope v^(tri j)) +
      slope u^n * slope v^(tri n) * ((y : ℚ)-b) := by
  rw [inverse_ordinary h]
  exact finite_tschakaloff v u b hb n y

end StaircaseAffine

#print axioms StaircaseAffine.inverse_ordinary
#print axioms StaircaseAffine.inverse_append
#print axioms StaircaseAffine.centered
#print axioms StaircaseAffine.copies_at_fixed
#print axioms StaircaseAffine.finite_tschakaloff
#print axioms StaircaseAffine.ordinary_finite_tschakaloff
