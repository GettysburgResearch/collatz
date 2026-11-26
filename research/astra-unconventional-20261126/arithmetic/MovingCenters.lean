import Mathlib.Tactic.Ring

/-! Affine word carries, their exact change under a local adjacent swap, and
the two integer numerators at a junction on an ordinary trajectory. -/
namespace Collatz.Unconventional.MovingCenters

/-- The integer coefficients of the affine map x ↦ (r*x+c)/d. -/
structure Block where
  r : ℤ
  d : ℤ
  c : ℤ

def empty : Block := ⟨1, 1, 0⟩

def step (e : ℕ) : Block := ⟨3, 2^e, 1⟩

/-- Chronological concatenation first applies u and then v. -/
def follow (u v : Block) : Block :=
  ⟨v.r * u.r, u.d * v.d, v.r * u.c + u.d * v.c⟩

def word : List ℕ → Block
  | [] => empty
  | e :: tail => follow (step e) (word tail)

theorem follow_assoc (u v w : Block) :
    follow (follow u v) w = follow u (follow v w) := by
  cases u
  cases v
  cases w
  simp [follow, mul_assoc, mul_add, add_assoc]
  ring

theorem word_append (u v : List ℕ) :
    word (u ++ v) = follow (word u) (word v) := by
  induction u with
  | nil => simp [word, empty, follow]
  | cons a tail ih => simp [word, ih, follow_assoc]

/-- A single transposition changes one carry summand regardless of either context. -/
theorem carry_swap (pref suff : List ℕ) (e f : ℕ) :
    (word (pref ++ e :: f :: suff)).c - (word (pref ++ f :: e :: suff)).c =
      (word suff).r * (word pref).d * ((2 : ℤ)^e - 2^f) := by
  simp only [word_append, word, follow, step]
  ring

theorem word_clocks (w : List ℕ) :
    (word w).r = (3 : ℤ)^w.length ∧ (word w).d = (2 : ℤ)^w.sum := by
  induction w with
  | nil => simp [word, empty]
  | cons e tail ih =>
    rcases ih with ⟨hr, hd⟩
    simp only [word, follow, step, List.length_cons, List.sum_cons, hr, hd, pow_succ, pow_add]
    simp

theorem carry_swap_one_two (pref suff : List ℕ) :
    (word (pref ++ 2 :: 1 :: suff)).c - (word (pref ++ 1 :: 2 :: suff)).c =
      (3 : ℤ)^suff.length * 2^pref.sum * 2 := by
  rw [carry_swap, (word_clocks suff).1, (word_clocks pref).2]
  norm_num

/-- All clocks and signs at the physical junction are retained. -/
theorem junction_numerators {r d cu cv tprev t tnext : ℤ}
    (hpast : d * t = r * tprev + cu) (hfuture : d * tnext = r * t + cv) :
    (d-r)*t-cu = r*(tprev-t) ∧ (d-r)*t-cv = d*(t-tnext) := by
  constructor
  · calc
      (d-r)*t-cu = d*t-cu-r*t := by ring
      _ = r*(tprev-t) := by rw [hpast]; ring
  · calc
      (d-r)*t-cv = d*t-(r*t+cv) := by ring
      _ = d*(t-tnext) := by rw [← hfuture]; ring

/-- Iterating an affine word preserves its centered integer equation even before
cancelling the fixed-point denominator. -/
theorem repeated_center {r d c : ℤ} {x : ℕ → ℤ}
    (hx : ∀ i, d*x (i+1) = r*x i+c) (n : ℕ) :
    d^n * ((d-r)*x n-c) = r^n * ((d-r)*x 0-c) := by
  induction n with
  | zero => simp
  | succ n ih =>
    have edge : d*((d-r)*x (n+1)-c) = r*((d-r)*x n-c) := by
      calc
        d*((d-r)*x (n+1)-c) = (d-r)*(d*x (n+1))-d*c := by ring
        _ = r*((d-r)*x n-c) := by rw [hx]; ring
    calc
      d^(n+1)*((d-r)*x (n+1)-c) = d^n*(d*((d-r)*x (n+1)-c)) := by
        rw [pow_succ, mul_assoc]
      _ = r*(d^n*((d-r)*x n-c)) := by rw [edge]; ring
      _ = r^(n+1)*((d-r)*x 0-c) := by rw [ih, pow_succ]; ring

#print axioms follow_assoc
#print axioms word_append
#print axioms word_clocks
#print axioms carry_swap
#print axioms carry_swap_one_two
#print axioms junction_numerators
#print axioms repeated_center

end Collatz.Unconventional.MovingCenters
