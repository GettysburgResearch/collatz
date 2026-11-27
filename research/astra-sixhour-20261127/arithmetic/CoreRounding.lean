import Mathlib.Data.Nat.Find
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
The control applies an externally prescribed optional tripling, then
a ceiling halving at each step. Its integral fixed points exist for
every positive-defect word. Its tripling commands need not coincide
with the parity commands of the ordinary shifted Collatz map.
-/

namespace Collatz.CoreRounding

set_option autoImplicit false

def multiplier : Bool → ℕ
  | false => 1
  | true => 3

def scale : List Bool → ℕ
  | [] => 1
  | b :: w => multiplier b * scale w

def step (b : Bool) (x : ℕ) : ℕ := (multiplier b * x + 1) / 2

def lap : List Bool → ℕ → ℕ
  | [], x => x
  | b :: w, x => lap w (step b x)

private theorem step_mono (b : Bool) : Monotone (step b) := by
  intro x y h
  exact Nat.div_le_div_right (Nat.add_le_add_right (Nat.mul_le_mul_left _ h) _)

private theorem lap_mono (w : List Bool) : Monotone (lap w) := by
  induction w with
  | nil => exact monotone_id
  | cons b w ih => exact ih.comp (step_mono b)

private theorem lap_zero (w : List Bool) : lap w 0 = 0 := by
  induction w with
  | nil => rfl
  | cons b w ih => simpa [lap, step] using ih

private theorem lap_pos {x : ℕ} (hx : 0 < x) (w : List Bool) : 0 < lap w x := by
  induction w generalizing x with
  | nil => exact hx
  | cons b w ih =>
    apply ih
    cases b <;> simp [step, multiplier] <;> omega

private theorem step_translate (b : Bool) (x k : ℕ) :
    step b (x + 2 * k) = step b x + multiplier b * k := by
  unfold step
  rw [show multiplier b * (x + 2 * k) + 1 =
      (multiplier b * x + 1) + (multiplier b * k) * 2 by ring]
  exact Nat.add_mul_div_right _ _ (by decide)

/-- A full dyadic translation traverses any externally commanded lap exactly. -/
theorem lap_translate (w : List Bool) (x k : ℕ) :
    lap w (x + 2 ^ w.length * k) = lap w x + scale w * k := by
  induction w generalizing x k with
  | nil => simp [lap, scale]
  | cons b w ih =>
    simp only [List.length_cons, pow_succ, lap, scale]
    rw [show 2 ^ w.length * 2 * k = 2 * (2 ^ w.length * k) by ring,
      step_translate, show multiplier b * (2 ^ w.length * k) =
      2 ^ w.length * (multiplier b * k) by ring, ih]
    ring

private theorem fixed_between {F : ℕ → ℕ} (mono : Monotone F) {K : ℕ}
    (one : 1 ≤ F 1) (big : 1 ≤ K) (cap : F K ≤ K) :
    ∃ x, 1 ≤ x ∧ x ≤ K ∧ F x = x := by
  let P := fun n => 1 ≤ n ∧ F n ≤ n
  have existsP : ∃ n, P n := ⟨K, big, cap⟩
  let x := Nat.find existsP
  have hx : P x := Nat.find_spec existsP
  have xmax : x ≤ K := Nat.find_min' existsP ⟨big, cap⟩
  refine ⟨x, hx.1, xmax, le_antisymm hx.2 ?_⟩
  by_cases hx1 : x = 1
  · simpa [hx1] using one
  · have hpos := hx.1
    have last : x - 1 < x := by omega
    have fail := Nat.find_min existsP last
    have hprev : x - 1 < F (x - 1) := by
      by_contra! h
      exact fail ⟨by omega, h⟩
    exact (show x ≤ F (x - 1) by omega).trans (mono (Nat.sub_le _ _))

/-- The actual integral control has a positive fixed point for every
contracting one-lap homogeneous multiplier. -/
theorem positive_fixed_point (w : List Bool) (defect : scale w < 2 ^ w.length) :
    ∃ x, 1 ≤ x ∧ x ≤ 2 ^ w.length ∧ lap w x = x := by
  have atTop : lap w (2 ^ w.length) = scale w := by
    simpa [lap_zero] using lap_translate w 0 1
  exact fixed_between (lap_mono w) (lap_pos (by decide : 0 < 1) w)
    (Nat.one_le_pow _ _ (by decide)) (atTop.le.trans defect.le)

/-- With one tripling and up to two halvings, neither pre-halving input
is 1 modulo 3. In particular every charged odd index has the physical
companion residue restriction. -/
theorem macro_residues (x : ℕ) : (3 * x) % 3 ≠ 1 ∧ (step true x) % 3 ≠ 1 := by
  simp only [step, multiplier]
  omega

/-- An integer cell keeps length one at a prescribed step exactly
when its left endpoint takes the genuine ordinary shortcut branch. -/
theorem adjacent_step (b : Bool) (x : ℕ) :
    step b (x + 1) = step b x + 1 ↔ (if b then 1 else 0) = x % 2 := by
  cases b <;> simp [step, multiplier] <;> omega

#print axioms lap_translate
#print axioms positive_fixed_point
#print axioms macro_residues
#print axioms adjacent_step

end Collatz.CoreRounding
