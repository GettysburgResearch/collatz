import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.Pigeonhole
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Push
import Mathlib.Tactic.Ring

/-! Finite pieces of the collision and height arguments for a modular
quotient of a positive rational shortcut cycle. The global projection,
the native input hypotheses and the logarithmic estimate are written
in MODULAR_QUOTIENTS.md. -/

namespace Collatz.ModularQuotient

/-- Opposite literal branches with the same source and target in the
residue ring can agree only at the unique critical source (for odd
modulus). This equality itself holds over every commutative ring. -/
theorem mixed_source {R : Type*} [CommRing R] {x y d : R}
    (even : 2*y = x) (odd : 2*y = 3*x+d) : 2*x+d=0 := by
  linear_combination even - odd

def grade : List Bool → ℕ
  | [] => 0
  | b :: w => b.toNat + grade w

def carry : List Bool → ℕ
  | [] => 0
  | _ :: w => 3^(grade w) + 2*carry w

theorem grade_le_length (w : List Bool) : grade w ≤ w.length := by
  induction w with
  | nil => simp [grade]
  | cons b w ih =>
    cases b <;> simp_all [grade, Bool.toNat] <;> omega

theorem carry_bound (w : List Bool) : carry w + 2^w.length ≤ 3^w.length := by
  induction w with
  | nil => simp [carry]
  | cons b w ih =>
    have hw : 3 ^ grade w ≤ 3 ^ w.length :=
      Nat.pow_le_pow_right (by decide) (grade_le_length w)
    simp only [carry, List.length_cons, pow_succ]
    omega

def CenterTrace {R : Type*} [CommRing R] (d : R) : R → List Bool → R → Prop
  | x, [], y => x=y
  | x, b::w, y => ∃ z, 2*z=3^b.toNat*x+d ∧ CenterTrace d z w y

theorem center_unroll {R : Type*} [CommRing R] {d x y : R} (w : List Bool)
    (trace : CenterTrace d x w y) :
    2^w.length*y = 3^(grade w)*x + d*(carry w : R) := by
  induction w generalizing x with
  | nil =>
    change x=y at trace
    simpa [grade, carry] using trace.symm
  | cons b w ih =>
    obtain ⟨z, hx, hz⟩ := trace
    have rest := ih hz
    simp only [List.length_cons, grade, carry, pow_succ, pow_add, Nat.cast_add,
      Nat.cast_pow, Nat.cast_ofNat, Nat.cast_mul]
    linear_combination 2*rest + 3^(grade w)*hx

/-- For the orbit of the zero centered residue modulo an odd compatible
modulus, the fixed tail alone supplies the vanishing scalar. -/
theorem critical_return {R : Type*} [CommRing R] {d : R} (b : Bool) (tail : List Bool)
    (trace : CenterTrace d 0 (b::tail) 0) :
    d*((3^(grade tail)+2*carry tail : ℕ) : R)=0 := by
  have h := center_unroll (b::tail) trace
  simpa only [zero_mul, mul_zero, zero_add, carry] using h.symm

def window (w : ℕ → ℤ) (a t : ℕ) : ℤ :=
  ∑ k ∈ Finset.range t, w (a+k)

theorem window_add (w : ℕ → ℤ) (a s t : ℕ) :
    window w a (s+t)=window w a s + window w (a+s) t := by
  simp only [window, Finset.sum_range_add, Nat.add_assoc]

theorem window_slide (w : ℕ → ℤ) (a s t : ℕ) :
    window w (a+s) t - window w a t = window w (a+t) s - window w a s := by
  have h := window_add w a s t
  have g := window_add w a t s
  rw [Nat.add_comm t s] at g
  omega

/-- A local bound on the range of all s-window counts controls every
suffix comparison at a multiple of the block clock. -/
theorem shifted_window_le (w : ℕ → ℤ) (s : ℕ) (r : ℤ)
    (rangeBound : ∀ x y, window w x s - window w y s ≤ r)
    (j a t : ℕ) :
    window w (a+j*s) t - window w a t ≤ j*r := by
  induction j with
  | zero => simp
  | succ j ih =>
    have h := window_slide w (a+j*s) s t
    have g := rangeBound ((a+j*s)+t) (a+j*s)
    rw [Nat.succ_mul, ← Nat.add_assoc]
    push_cast
    linarith

/-- Complete multiplication-free pigeonhole step. The index maps are
the actual cleared numerator and the dictionary label of the aligned
future. Equal labels supply the dyadic spacing from the native pair. -/
theorem local_packing (H L : ℕ) (X : Fin (H+1) → ℤ) (label : Fin (H+1) → Fin H)
    {bound : ℤ} (positive : ∀ i, 0<X i) (size : ∀ i, X i≤bound)
    (spacing : ∀ i j, i ≠ j → label i=label j → (2:ℤ)^L ≤ |X i-X j|) :
    (2:ℤ)^L < bound := by
  obtain ⟨i,j,hne,he⟩ := Fintype.exists_ne_map_eq_of_card_lt label (by simp)
  have h := spacing i j hne he
  have hp := positive i
  have hq := positive j
  have ha := size i
  have hb := size j
  have hab : |X i-X j| < bound := abs_lt.mpr ⟨by omega, by omega⟩
  exact lt_of_le_of_lt h hab

#print axioms mixed_source
#print axioms carry_bound
#print axioms center_unroll
#print axioms critical_return
#print axioms window_slide
#print axioms shifted_window_le
#print axioms local_packing

end Collatz.ModularQuotient
