/-!
# A finite positive-row obstruction to excessive residue profiles

This is the ordered-ring, finite algebraic core of the written all-resolution
asymptotic-envelope theorem. It does not formalize regularly varying limits,
real powers, or the modular enumeration in the accompanying note.

The distinguished row entry is a self-transition with coefficient greater
than one. Every other entry is nonnegative. A row that reaches every
profile coordinate with positive weight cannot lie below its self value
unless the whole profile is zero. The quantitative version retains an
explicit lower bound for the drift at every coordinate.
-/

set_option autoImplicit false

namespace CollatzGlobalClosure.FiniteProfileDrift

open Lean.Grind

universe u
variable {K : Type u} [CommRing K] [LE K] [LT K]
  [Std.LawfulOrderLT K] [Std.IsLinearOrder K] [OrderedRing K]

def weightedSum : List (K × K) → K
  | [] => 0
  | (w,a)::xs => w*a + weightedSum xs

theorem weightedSum_nonneg (xs : List (K × K))
    (h : ∀ x ∈ xs, 0 ≤ x.1 ∧ 0 ≤ x.2) : 0 ≤ weightedSum xs := by
  induction xs with
  | nil => simp [weightedSum]
  | cons x xs ih =>
    have hx := h x (by simp)
    have ht : ∀ y ∈ xs, 0 ≤ y.1 ∧ 0 ≤ y.2 := by
      intro y hy
      exact h y (by simp [hy])
    have hp := OrderedRing.mul_nonneg hx.1 hx.2
    have hi := ih ht
    simp only [weightedSum]
    grind

theorem term_le_weightedSum (xs : List (K × K))
    (h : ∀ x ∈ xs, 0 ≤ x.1 ∧ 0 ≤ x.2)
    (x : K × K) (hx : x ∈ xs) : x.1*x.2 ≤ weightedSum xs := by
  induction xs with
  | nil => simp at hx
  | cons y ys ih =>
    have hy := h y (by simp)
    have ht : ∀ z ∈ ys, 0 ≤ z.1 ∧ 0 ≤ z.2 := by
      intro z hz
      exact h z (by simp [hz])
    have rest := weightedSum_nonneg ys ht
    have first := OrderedRing.mul_nonneg hy.1 hy.2
    simp only [List.mem_cons] at hx
    rcases hx with same | later
    · subst x
      simp only [weightedSum]
      grind
    · have bound := ih ht later
      simp only [weightedSum]
      grind

theorem excessive_positive_row_zero (s b : K) (xs : List (K × K))
    (hs : 1 < s) (hb : 0 ≤ b)
    (h : ∀ x ∈ xs, 0 < x.1 ∧ 0 ≤ x.2)
    (excessive : s*b + weightedSum xs ≤ b) :
    b=0 ∧ ∀ x ∈ xs, x.2=0 := by
  have hn : ∀ x ∈ xs, 0 ≤ x.1 ∧ 0 ≤ x.2 := by
    intro x hx
    exact ⟨Std.le_of_lt (h x hx).1, (h x hx).2⟩
  have hsum := weightedSum_nonneg xs hn
  have hbzero : b=0 := by
    by_cases zero : b=0
    · exact zero
    · have bp : 0 < b := by grind
      have sp : 0 < s-1 := by grind
      have product := OrderedRing.mul_pos sp bp
      grind
  refine ⟨hbzero, ?_⟩
  rw [hbzero] at excessive
  simp only [Semiring.mul_zero, AddCommMonoid.zero_add] at excessive
  intro x hx
  have bound := term_le_weightedSum xs hn x hx
  have hxpos := h x hx
  by_cases zero : x.2=0
  · exact zero
  · have ap : 0 < x.2 := by grind
    have product := OrderedRing.mul_pos hxpos.1 ap
    grind

/-- The same positive drift pays for every profile coordinate, including
the distinguished coordinate. No maximizer or finite search is needed. -/
theorem quantitative_row_drift (s b epsilon : K) (xs : List (K × K))
    (hb : 0 ≤ b) (he : 0 ≤ epsilon) (hs : 1+epsilon ≤ s)
    (h : ∀ x ∈ xs, epsilon ≤ x.1 ∧ 0 ≤ x.2) :
    epsilon*b ≤ s*b+weightedSum xs-b ∧
    ∀ x ∈ xs, epsilon*x.2 ≤ s*b+weightedSum xs-b := by
  have hn : ∀ x ∈ xs, 0 ≤ x.1 ∧ 0 ≤ x.2 := by
    intro x hx
    exact ⟨Std.le_trans he (h x hx).1, (h x hx).2⟩
  have hsum := weightedSum_nonneg xs hn
  have self := OrderedRing.mul_le_mul_of_nonneg_right hs hb
  have se : 0 ≤ s-1 := by grind
  have base := OrderedRing.mul_nonneg se hb
  constructor
  · grind
  · intro x hx
    have term := term_le_weightedSum xs hn x hx
    have val := h x hx
    have lower := OrderedRing.mul_le_mul_of_nonneg_right val.1 val.2
    grind

#print axioms excessive_positive_row_zero
#print axioms quantitative_row_drift

end CollatzGlobalClosure.FiniteProfileDrift
