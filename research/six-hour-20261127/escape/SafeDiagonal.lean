import Mathlib.Algebra.Order.Group.Unbundled.Int
import Mathlib.Data.Finset.Lattice.Fold
import Mathlib.Data.Fintype.Fin
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Ordinary compression, affine height budget, finite-source compactness,
and one-step arithmetic used in the trace and translated diagonal arguments.
The covering and posterior estimates are written mathematics. -/
namespace EscapeSafeDiagonal

inductive Token where
  | a | b
  deriving DecidableEq

def p : Token → ℕ | .a => 3 | .b => 9
def q : Token → ℕ | .a => 2 | .b => 8
def c : Token → ℕ | .a => 0 | .b => 1

def Edge (s : Token) (x y : ℕ) : Prop := q s * y = p s * x + c s

theorem a_domain (x : ℕ) : (∃ y, Edge .a x y) ↔ x % 2 = 0 := by
  simp only [Edge, p, q, c, Nat.add_zero]
  constructor
  · rintro ⟨y, h⟩
    omega
  · intro h
    exact ⟨3*x/2, by omega⟩

theorem b_domain (x : ℕ) : (∃ y, Edge .b x y) ↔ x % 8 = 7 := by
  simp only [Edge, p, q, c]
  constructor
  · rintro ⟨y, h⟩
    omega
  · intro h
    exact ⟨(9*x+1)/8, by omega⟩

theorem a_range (y : ℕ) : (∃ x, Edge .a x y) ↔ y % 3 = 0 := by
  simp only [Edge, p, q, c, Nat.add_zero]
  constructor
  · rintro ⟨x, h⟩
    omega
  · intro h
    exact ⟨2*y/3, by omega⟩

theorem b_range (y : ℕ) : (∃ x, Edge .b x y) ↔ y % 9 = 8 := by
  simp only [Edge, p, q, c]
  constructor
  · rintro ⟨x, h⟩
    omega
  · intro h
    exact ⟨(8*y-1)/9, by omega⟩

def P : List Token → ℕ
  | [] => 1
  | s :: rest => p s * P rest

def Q : List Token → ℕ
  | [] => 1
  | s :: rest => q s * Q rest

def Runs : List Token → ℕ → ℕ → Prop
  | [], x, y => x = y
  | s :: rest, x, y => ∃ z, Edge s x z ∧ Runs rest z y

theorem edge_height (s : Token) (x y : ℕ) (h : Edge s x y) :
    p s * x ≤ q s * y ∧ q s * (y+1) ≤ p s * (x+1) := by
  cases s <;> simp only [Edge, p, q, c] at * <;> omega

theorem word_height (w : List Token) (x y : ℕ) (h : Runs w x y) :
    P w * x ≤ Q w * y ∧ Q w * (y+1) ≤ P w * (x+1) := by
  induction w generalizing x with
  | nil =>
    change x = y at h
    simp [h, P, Q]
  | cons s rest ih =>
    obtain ⟨z, hs, hr⟩ := h
    obtain ⟨hl, hu⟩ := edge_height s x z hs
    obtain ⟨hL, hU⟩ := ih z hr
    constructor
    · calc
        P (s :: rest) * x = P rest * (p s * x) := by simp [P]; ring
        _ ≤ P rest * (q s * z) := Nat.mul_le_mul_left _ hl
        _ = q s * (P rest * z) := by ring
        _ ≤ q s * (Q rest * y) := Nat.mul_le_mul_left _ hL
        _ = Q (s :: rest) * y := by simp [Q]; ring
    · calc
        Q (s :: rest) * (y+1) = q s * (Q rest * (y+1)) := by simp [Q]; ring
        _ ≤ q s * (P rest * (z+1)) := Nat.mul_le_mul_left _ hU
        _ = P rest * (q s * (z+1)) := by ring
        _ ≤ P rest * (p s * (x+1)) := Nat.mul_le_mul_left _ hu
        _ = P (s :: rest) * (x+1) := by simp [P]; ring

theorem finite_source_compactness (good : ℕ → ℕ → Prop) (C : ℕ)
    (down : ∀ x n m, n ≤ m → good x m → good x n)
    (coverage : ∀ n, ∃ x ≤ C, good x n) :
    ∃ x ≤ C, ∀ n, good x n := by
  classical
  by_contra! fail
  have hf : ∀ i : Fin (C+1), ∃ n, ¬ good i.val n := fun i => fail i.val (by omega)
  choose bad hb using hf
  let limit := Finset.univ.sup bad
  obtain ⟨x, hx, hg⟩ := coverage limit
  let i : Fin (C+1) := ⟨x, by omega⟩
  have hi : bad i ≤ limit := Finset.le_sup (f := bad) (Finset.mem_univ i)
  exact hb i (down x (bad i) limit hi hg)

theorem half_height_at_jump (B Q m y : ℕ) (b : ℕ) (hb : b ≤ 4)
    (hQ : 0 < Q) (hj : 2*B < m) (hsize : Q*m ≤ b*B*y) :
    Q < 2*y := by
  have h₁ := Nat.mul_lt_mul_of_pos_left hj hQ
  have h₂ := Nat.mul_le_mul_right (B*y) hb
  nlinarith

theorem parameter_stabilizes (old next modulus : ℤ)
    (hdiv : modulus ∣ next-old) (hsmall : |next-old| < modulus) : next = old := by
  exact sub_eq_zero.mp (Int.eq_zero_of_abs_lt_dvd hdiv hsmall)

#print axioms a_domain
#print axioms b_domain
#print axioms a_range
#print axioms b_range
#print axioms word_height
#print axioms finite_source_compactness
#print axioms half_height_at_jump
#print axioms parameter_stabilizes
end EscapeSafeDiagonal
