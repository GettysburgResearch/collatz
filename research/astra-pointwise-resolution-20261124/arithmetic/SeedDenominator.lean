import Std

/-! Finite affine-word identities over the rationals for the two shortcut
coordinates. The Subspace Theorem and the asymptotic estimates are written proofs. -/
namespace SeedDenominator

structure Aff where
  slope : Rat
  off : Rat
  deriving DecidableEq, Repr

/-- Apply the first block, followed by the second. -/
def join (a b : Aff) : Aff :=
  ⟨b.slope * a.slope, b.slope * a.off + b.off⟩

def comm (a b : Aff) : Rat :=
  (a.slope - 1) * b.off - (b.slope - 1) * a.off

theorem right_block_rules (a b : Aff) :
    comm a (join a b) = comm a b ∧
    comm a (join b a) = a.slope * comm a b := by
  unfold comm join
  simp
  grind

theorem swap_blocks (a b : Aff) : comm b a = -comm a b := by
  unfold comm
  grind

def eval (a b : Aff) : List Bool → Aff
  | [] => ⟨1, 0⟩
  | e :: es => join (if e then b else a) (eval a b es)

/-- Sums of suffix slopes immediately after the occurrences of the second block. -/
def onesWeight (a b : Aff) : List Bool → Rat
  | [] => 0
  | e :: es => (if e then (eval a b es).slope else 0) + onesWeight a b es

theorem suffix_carry (a b : Aff) (w : List Bool) :
    (a.slope - 1) * (eval a b w).off =
      a.off * ((eval a b w).slope - 1) + comm a b * onesWeight a b w := by
  induction w with
  | nil => simp [eval, onesWeight]; grind
  | cons e es ih =>
    cases e <;> simp only [eval, join, onesWeight, Bool.false_eq_true, ↓reduceIte]
    all_goals unfold comm at *
    all_goals grind

/-- The determinant controlling escape from every fixed translated subtorus. -/
theorem clock_transversality (l p k q a b r s : Int) :
    (r*l+s*k)*(a*p+b*q)-(r*p+s*q)*(a*l+b*k) =
      (r*b-s*a)*(l*q-p*k) := by grind

def physicalEven : Aff := ⟨1/2, 0⟩
def physicalOdd : Aff := ⟨3/2, 1/2⟩
def companionEven : Aff := ⟨3/2, 0⟩
def companionOdd : Aff := ⟨3/4, 1/4⟩

theorem base_commutators :
    comm physicalEven physicalOdd = -1/4 ∧
    comm companionEven companionOdd = 1/8 := by
  unfold comm physicalEven physicalOdd companionEven companionOdd
  grind

/-- A list of complete physical windows covered by k+1 possible words
cannot come from k+2 distinct small states if equal windows force dyadic
agreement. The conclusion clears the real height inequality in (1). -/
theorem mechanical_window_budget {α : Type} (k y : Nat)
    (windows catalog : List α) (state : Nat → Nat)
    (long : k+2 ≤ windows.length) (few : catalog.length ≤ k+1)
    (covered : windows ⊆ catalog)
    (distinct : ∀ i j, i < windows.length → j < windows.length →
      state i = state j → i=j)
    (shared : ∀ i j (hi : i < windows.length) (hj : j < windows.length),
      windows[i] = windows[j] → state i % 2^k = state j % 2^k)
    (height : ∀ i, i < windows.length →
      2^(k+1) * state i ≤ 3^(k+1)*(y+1)) :
    2^(k+1)*2^k ≤ 3^(k+1)*(y+1) := by
  apply Classical.byContradiction
  intro h
  have small : ∀ i, i < windows.length → state i < 2^k := by
    intro i hi
    apply Nat.lt_of_not_ge
    intro large
    exact h (Nat.le_trans (Nat.mul_le_mul_left _ large) (height i hi))
  have nd : windows.Nodup := by
    apply List.nodup_iff_eq_of_getElem_eq.mpr
    intro i j hi hj same
    have eq := shared i j hi hj same
    rw [Nat.mod_eq_of_lt (small i hi), Nat.mod_eq_of_lt (small j hj)] at eq
    exact distinct i j hi hj eq
  have := nd.length_le_of_subset covered
  omega

#print axioms mechanical_window_budget
#print axioms right_block_rules
#print axioms swap_blocks
#print axioms suffix_carry
#print axioms clock_transversality
#print axioms base_commutators

end SeedDenominator
