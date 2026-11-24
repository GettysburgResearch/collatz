module

public import Mathlib.Algebra.Order.Field.Rat
public import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

/-!
Finite substitution algebra from GettysburgResearch/collatz PR 190 at
ba58227c5a047ff3859a148a5fdaac4fd1451e4c, with proofs and statements retained.
The regularity lemmas below clear a common odd denominator, recover the first
letter modulo two, and characterize vanishing along the physical weight orbit.
-/

@[expose] public section

namespace MahlerPhysical

def weight (x y : ℚ) : List Bool → ℚ
  | [] => 1
  | false :: w => x * weight x y w
  | true :: w => y * weight x y w

def zeroSum (x y : ℚ) : List Bool → ℚ
  | [] => 0
  | false :: w => 1 + x * zeroSum x y w
  | true :: w => y * zeroSum x y w

def oneSum (x y : ℚ) : List Bool → ℚ
  | [] => 0
  | false :: w => x * oneSum x y w
  | true :: w => 1 + y * oneSum x y w

theorem telescope (x y : ℚ) (w : List Bool) :
    (1-x) * zeroSum x y w + (1-y) * oneSum x y w =
      1 - weight x y w := by
  induction w with
  | nil => simp [zeroSum, oneSum, weight]
  | cons a w ih =>
    cases a
    · simp only [zeroSum, oneSum, weight]
      linear_combination x * ih
    · simp only [zeroSum, oneSum, weight]
      linear_combination y * ih

theorem weight_append (x y : ℚ) (u v : List Bool) :
    weight x y (u ++ v) = weight x y u * weight x y v := by
  induction u with
  | nil => simp [weight]
  | cons a u ih => cases a <;> simp [weight, ih, mul_assoc]

theorem oneSum_append (x y : ℚ) (u v : List Bool) :
    oneSum x y (u ++ v) =
      oneSum x y u + weight x y u * oneSum x y v := by
  induction u with
  | nil => simp [weight, oneSum]
  | cons a u ih => cases a <;> simp [weight, oneSum, ih] <;> ring

def substitute (u v : List Bool) : List Bool → List Bool
  | [] => []
  | false :: w => u ++ substitute u v w
  | true :: w => v ++ substitute u v w

theorem weight_substitute (x y : ℚ) (u v w : List Bool) :
    weight x y (substitute u v w) =
      weight (weight x y u) (weight x y v) w := by
  induction w with
  | nil => simp [substitute, weight]
  | cons a w ih =>
    cases a <;> simp [substitute, weight_append, weight, ih]

theorem oneSum_substitute (x y : ℚ) (u v w : List Bool) :
    oneSum x y (substitute u v w) =
      oneSum x y u * zeroSum (weight x y u) (weight x y v) w +
      oneSum x y v * oneSum (weight x y u) (weight x y v) w := by
  induction w with
  | nil => simp [substitute, oneSum, zeroSum]
  | cons a w ih =>
    cases a <;> simp [substitute, oneSum_append, oneSum, zeroSum, ih] <;> ring

theorem finite_mahler (x y : ℚ) (u v w : List Bool) :
    (1 - weight x y u) * oneSum x y (substitute u v w) =
      oneSum x y u * (1 - weight (weight x y u) (weight x y v) w) +
      ((1 - weight x y u) * oneSum x y v -
       (1 - weight x y v) * oneSum x y u) *
        oneSum (weight x y u) (weight x y v) w := by
  rw [oneSum_substitute]
  have h := telescope (weight x y u) (weight x y v) w
  linear_combination (oneSum x y u) * h

def affineWord (x y a e : ℚ) : List Bool → ℚ → ℚ
  | [], z => z
  | false :: w, z => a + x * affineWord x y a e w z
  | true :: w, z => e + y * affineWord x y a e w z

theorem affine_expand (x y a e : ℚ) (w : List Bool) (z : ℚ) :
    affineWord x y a e w z =
      a * zeroSum x y w + e * oneSum x y w + weight x y w * z := by
  induction w with
  | nil => simp [affineWord, zeroSum, oneSum, weight]
  | cons i w ih =>
    cases i <;> simp [affineWord, zeroSum, oneSum, weight, ih] <;> ring

theorem eliminate_zero (x y a e u v : ℚ)
    (hx : 1-x ≠ 0) (h : (1-x)*u + (1-y)*v = 1) :
    a*u + e*v = a/(1-x) + (e-a*(1-y)/(1-x))*v := by
  have hu : u = (1-(1-y)*v)/(1-x) := by
    apply (eq_div_iff hx).2
    linear_combination h
  rw [hu]
  ring


/-- Clear one common odd denominator at every letter. -/
private def scaledOnes (d a b : ℤ) : List Bool → ℤ
  | [] => 0
  | false :: w => a * scaledOnes d a b w
  | true :: w => d ^ (w.length + 1) + b * scaledOnes d a b w

private theorem scaledOnes_eq (d a b : ℤ) (hd : d ≠ 0) (w : List Bool) :
    (scaledOnes d a b w : ℚ) =
      (d : ℚ) ^ w.length * oneSum ((a : ℚ) / d) ((b : ℚ) / d) w := by
  have hd' : (d : ℚ) ≠ 0 := by exact_mod_cast hd
  induction w with
  | nil => simp [scaledOnes, oneSum]
  | cons i w ih =>
    cases i <;> simp only [scaledOnes, oneSum, List.length_cons, Int.cast_add,
      Int.cast_mul, Int.cast_pow, pow_succ, ih] <;> field_simp

private theorem scaledOnes_injective (d a b : ℤ)
    (hd : (d : ZMod 2) = 1) (ha : (a : ZMod 2) = 0) (hb : (b : ZMod 2) = 0)
    (ha' : a ≠ 0) (hb' : b ≠ 0)
    (u v : List Bool) (hlen : u.length = v.length)
    (he : scaledOnes d a b u = scaledOnes d a b v) : u = v := by
  induction u generalizing v with
  | nil =>
    cases v <;> simp_all
  | cons i u ih =>
    cases v with
    | nil => simp at hlen
    | cons j v =>
      have hlen' : u.length = v.length := by simpa using hlen
      have hmod := congrArg (fun z : ℤ => (z : ZMod 2)) he
      cases i <;> cases j
      · apply congrArg (List.cons false)
        apply ih v hlen'
        exact mul_left_cancel₀ ha' he
      · simp [scaledOnes, hd, ha, hb] at hmod
      · simp [scaledOnes, hd, ha, hb] at hmod
      · apply congrArg (List.cons true)
        apply ih v hlen'
        apply mul_left_cancel₀ hb'
        simpa [scaledOnes, hlen'] using he

/-- On a fixed word length, the prefix-one sum determines every letter. -/
theorem oneSum_injective_odd_denominator (d a b : ℤ)
    (hd : (d : ZMod 2) = 1) (ha : (a : ZMod 2) = 0) (hb : (b : ZMod 2) = 0)
    (ha' : a ≠ 0) (hb' : b ≠ 0)
    (u v : List Bool) (hlen : u.length = v.length)
    (he : oneSum ((a : ℚ) / d) ((b : ℚ) / d) u =
          oneSum ((a : ℚ) / d) ((b : ℚ) / d) v) : u = v := by
  have hd' : d ≠ 0 := by
    intro h
    simp [h] at hd
  apply scaledOnes_injective d a b hd ha hb ha' hb' u v hlen
  have hq : (scaledOnes d a b u : ℚ) = (scaledOnes d a b v : ℚ) := by
    rw [scaledOnes_eq d a b hd' u, scaledOnes_eq d a b hd' v, hlen, he]
  exact_mod_cast hq

/-- For arbitrary image lengths, the finite Mahler coefficient vanishes exactly
when the two substitution images commute as words. -/
theorem determinant_zero_iff_commute (d a b : ℤ)
    (hd : (d : ZMod 2) = 1) (ha : (a : ZMod 2) = 0) (hb : (b : ZMod 2) = 0)
    (ha' : a ≠ 0) (hb' : b ≠ 0) (u v : List Bool) :
    let x := (a : ℚ) / d
    let y := (b : ℚ) / d
    (1 - weight x y u) * oneSum x y v - (1 - weight x y v) * oneSum x y u = 0 ↔
      u ++ v = v ++ u := by
  dsimp only
  let x := (a : ℚ) / d
  let y := (b : ℚ) / d
  change (1 - weight x y u) * oneSum x y v - (1 - weight x y v) * oneSum x y u = 0 ↔ _
  have hdet : (1 - weight x y u) * oneSum x y v - (1 - weight x y v) * oneSum x y u =
      oneSum x y (v ++ u) - oneSum x y (u ++ v) := by
    rw [oneSum_append, oneSum_append]
    ring
  rw [hdet, sub_eq_zero]
  constructor
  · intro h
    apply oneSum_injective_odd_denominator d a b hd ha hb ha' hb' (u ++ v) (v ++ u)
    · simp [Nat.add_comm]
    · exact h.symm
  · intro h
    rw [h]

/-- Physical accelerator slopes have a positive binary clock and ternary
denominator. The two odd-step counts may be different. -/
theorem physical_determinant_zero_iff_commute (A B p q : ℕ) (u v : List Bool) :
    let x := (2 : ℚ) ^ (A + 1) / 3 ^ p
    let y := (2 : ℚ) ^ (B + 1) / 3 ^ q
    (1 - weight x y u) * oneSum x y v - (1 - weight x y v) * oneSum x y u = 0 ↔
      u ++ v = v ++ u := by
  let d : ℤ := 3 ^ p * 3 ^ q
  let a : ℤ := 2 ^ (A + 1) * 3 ^ q
  let b : ℤ := 2 ^ (B + 1) * 3 ^ p
  have h2 : (2 : ZMod 2) = 0 := by decide
  have h3 : (3 : ZMod 2) = 1 := by decide
  have hd : (d : ZMod 2) = 1 := by simp [d, h3]
  have ha : (a : ZMod 2) = 0 := by simp [a, h2, pow_succ]
  have hb : (b : ZMod 2) = 0 := by simp [b, h2, pow_succ]
  have ha' : a ≠ 0 := by dsimp [a]; positivity
  have hb' : b ≠ 0 := by dsimp [b]; positivity
  have hx : (a : ℚ) / d = (2 : ℚ) ^ (A + 1) / 3 ^ p := by
    dsimp [a, d]
    push_cast
    field_simp
  have hy : (b : ℚ) / d = (2 : ℚ) ^ (B + 1) / 3 ^ q := by
    dsimp [b, d]
    push_cast
    field_simp
  simpa only [hx, hy] using determinant_zero_iff_commute d a b hd ha hb ha' hb' u v


/-- A positive binary clock and a nonnegative ternary clock. -/
def IsPhysicalSlope (x : ℚ) : Prop :=
  ∃ a p : ℕ, x = (2 : ℚ) ^ (a + 1) / 3 ^ p

private theorem physicalSlope_mul {x y : ℚ}
    (hx : IsPhysicalSlope x) (hy : IsPhysicalSlope y) : IsPhysicalSlope (x * y) := by
  obtain ⟨a, p, rfl⟩ := hx
  obtain ⟨b, q, rfl⟩ := hy
  refine ⟨a + b + 1, p + q, ?_⟩
  rw [div_mul_div_comm, ← pow_add, ← pow_add]
  congr 2
  omega

/-- A nonempty image word still has a strictly positive binary clock. -/
theorem physicalSlope_weight {x y : ℚ} (hx : IsPhysicalSlope x) (hy : IsPhysicalSlope y)
    (w : List Bool) (hw : w ≠ []) : IsPhysicalSlope (weight x y w) := by
  induction w with
  | nil => exact (hw rfl).elim
  | cons i w ih =>
    by_cases he : w = []
    · subst w
      cases i <;> simp [weight, hx, hy]
    · have ht := ih he
      cases i
      · exact physicalSlope_mul hx ht
      · exact physicalSlope_mul hy ht

/-- Simultaneous substitution of the two word weights at each clock. -/
def weightOrbit (u v : List Bool) (x y : ℚ) : ℕ → ℚ × ℚ
  | 0 => (x, y)
  | n + 1 =>
    let a := weightOrbit u v x y n
    (weight a.1 a.2 u, weight a.1 a.2 v)

/-- Vanishing at any physical evaluation point of the substitution orbit is
equivalent to the same explicit equality of finite words. -/
theorem determinant_at_every_iterate (u v : List Bool) (hu : u ≠ []) (hv : v ≠ [])
    {x y : ℚ} (hx : IsPhysicalSlope x) (hy : IsPhysicalSlope y) (n : ℕ) :
    let z := weightOrbit u v x y n
    (1 - weight z.1 z.2 u) * oneSum z.1 z.2 v -
      (1 - weight z.1 z.2 v) * oneSum z.1 z.2 u = 0 ↔ u ++ v = v ++ u := by
  have hall (k : ℕ) : IsPhysicalSlope (weightOrbit u v x y k).1 ∧
      IsPhysicalSlope (weightOrbit u v x y k).2 := by
    induction k with
    | zero => exact ⟨hx, hy⟩
    | succ k ih =>
      exact ⟨physicalSlope_weight ih.1 ih.2 u hu, physicalSlope_weight ih.1 ih.2 v hv⟩
  obtain ⟨⟨a, p, ha⟩, ⟨b, q, hb⟩⟩ := hall n
  dsimp only
  rw [ha, hb]
  exact physical_determinant_zero_iff_commute a b p q u v


#print axioms telescope
#print axioms weight_append
#print axioms oneSum_append
#print axioms weight_substitute
#print axioms oneSum_substitute
#print axioms finite_mahler
#print axioms affine_expand
#print axioms eliminate_zero
#print axioms oneSum_injective_odd_denominator
#print axioms determinant_zero_iff_commute
#print axioms physical_determinant_zero_iff_commute
#print axioms physicalSlope_weight
#print axioms determinant_at_every_iterate

end MahlerPhysical
