import Mathlib.Data.Fintype.Fin
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

/-! Three-dimensional positive-polynomial digit maps pump from two to four iterations. -/
namespace PolynomialPump

/-- This describes all nonzero polynomials with nonnegative integer coefficients,
after omitting zero terms, on strictly positive inputs. -/
inductive Expr where
  | one
  | var (i : Fin 3)
  | add (p q : Expr)
  | mul (p q : Expr)

abbrev State := Fin 3 → ℕ
def eval : Expr → State → ℕ
  | .one, _ => 1
  | .var i, s => s i
  | .add p q, s => eval p s + eval q s
  | .mul p q, s => eval p s * eval q s

def uses : Expr → Fin 3 → Prop
  | .one, _ => False
  | .var j, i => i = j
  | .add p q, i | .mul p q, i => uses p i ∨ uses q i

theorem positive (p : Expr) (s : State) (hs : ∀ i, 0 < s i) : 0 < eval p s := by
  induction p with
  | one => exact Nat.zero_lt_one
  | var i => exact hs i
  | add p q hp hq => exact add_pos hp hq
  | mul p q hp hq => exact Nat.mul_pos hp hq

theorem support_mono (p : Expr) (s t : State)
    (h : ∀ i, uses p i → s i ≤ t i) : eval p s ≤ eval p t := by
  induction p with
  | one => exact le_rfl
  | var i => exact h i rfl
  | add p q hp hq =>
    exact Nat.add_le_add (hp (fun i hi => h i (Or.inl hi))) (hq (fun i hi => h i (Or.inr hi)))
  | mul p q hp hq =>
    exact Nat.mul_le_mul (hp (fun i hi => h i (Or.inl hi))) (hq (fun i hi => h i (Or.inr hi)))

theorem dominates (p : Expr) (s : State) (hs : ∀ j, 0 < s j)
    (i : Fin 3) (h : uses p i) : s i ≤ eval p s := by
  induction p with
  | one => exact False.elim h
  | var j => rw [h]; exact le_rfl
  | add p q hp hq =>
    rcases h with h | h
    · exact (hp h).trans (Nat.le_add_right _ _)
    · exact (hq h).trans (Nat.le_add_left _ _)
  | mul p q hp hq =>
    rcases h with h | h
    · exact (hp h).trans (Nat.le_mul_of_pos_right _ (positive q s hs))
    · exact (hq h).trans (Nat.le_mul_of_pos_left _ (positive p s hs))

/-- Every pair of free coordinates has depth at most two after regarding the
first coordinate as already increasing. This lemma is symmetric in Y and Z. -/
theorem free_coordinate (Y Z : ℕ → ℕ) (yy zy yz zz : Prop)
    (hy : yy → ∀ n, Y n ≤ Y (n+1)) (hzy : zy → ∀ n, Z n ≤ Y (n+1))
    (hyz : yz → ∀ n, Y n ≤ Z (n+1)) (hz : zz → ∀ n, Z n ≤ Z (n+1))
    (nextY : ∀ n, (yy → Y n ≤ Y (n+2)) → (zy → Z n ≤ Z (n+2)) →
        Y (n+1) ≤ Y (n+3))
    (nextZ : ∀ n, (yz → Y n ≤ Y (n+2)) → (zz → Z n ≤ Z (n+2)) →
        Z (n+1) ≤ Z (n+3)) : Y 2 ≤ Y 4 := by
  by_cases hyy : yy
  · exact (hy hyy 2).trans (hy hyy 3)
  apply nextY 1 (fun h => (hyy h).elim)
  intro hZY
  by_cases hYZ : yz
  · exact (hzy hZY 1).trans (hyz hYZ 2)
  apply nextZ 0 (fun h => (hYZ h).elim)
  intro hZZ
  exact (hz hZZ 0).trans (hz hZZ 1)

def step (f : Fin 3 → Expr) (s : State) : State := fun i => eval (f i) s
def orbit (f : Fin 3 → Expr) (s : State) : ℕ → State
  | 0 => s
  | n+1 => step f (orbit f s n)

theorem used_of_strict (p : Expr)
    (strict : ∀ (s t : State), (∀ i, 0 < s i) → (∀ i, s i ≤ t i) →
      s 0 < t 0 → eval p s < eval p t) : uses p 0 := by
  by_contra hu
  let s : State := fun _ => 1
  let t : State := fun i => if i = 0 then 2 else 1
  have hl : eval p s < eval p t := strict s t (fun _ => by decide)
      (fun i => by dsimp [s,t]; split <;> decide) (by decide)
  have hle := support_mono p t s (fun i hi => by
    by_cases h : i = 0
    · subst i; exact (hu hi).elim
    · simp [s,t,h])
  omega

/-- The concrete inequality needed for the AYH all-rule 41-to-161 derivation. -/
theorem pump (f : Fin 3 → Expr) (hf : uses (f 0) 0)
    (s : State) (hs : ∀ i, 0 < s i) : ∀ i, orbit f s 2 i ≤ orbit f s 4 i := by
  let u := orbit f s
  have hpos : ∀ n i, 0 < u n i := by
    intro n
    induction n with
    | zero => exact hs
    | succ n ih => exact fun i => positive (f i) _ ih
  have edge (i j : Fin 3) (h : uses (f i) j) (n : ℕ) : u n j ≤ u (n+1) i :=
    dominates (f i) _ (hpos n) j h
  have root (n : ℕ) : u n 0 ≤ u (n+2) 0 :=
    (edge 0 0 hf n).trans (edge 0 0 hf (n+1))
  have transfer (i : Fin 3) (n : ℕ)
      (h1 : uses (f i) 1 → u n 1 ≤ u (n+2) 1)
      (h2 : uses (f i) 2 → u n 2 ≤ u (n+2) 2) :
      u (n+1) i ≤ u (n+3) i := by
    apply support_mono (f i) (u n) (u (n+2))
    intro j h
    fin_cases j
    · exact root n
    · exact h1 h
    · exact h2 h
  intro i
  fin_cases i
  · exact root 2
  · exact free_coordinate (fun n => u n 1) (fun n => u n 2) _ _ _ _
      (edge 1 1) (edge 1 2) (edge 2 1) (edge 2 2)
      (transfer 1) (transfer 2)
  · exact free_coordinate (fun n => u n 2) (fun n => u n 1) _ _ _ _
      (edge 2 2) (edge 2 1) (edge 1 2) (edge 1 1)
      (fun n h2 h1 => transfer 2 n h1 h2) (fun n h2 h1 => transfer 1 n h1 h2)
end PolynomialPump
