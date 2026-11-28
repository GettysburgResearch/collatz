import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Data.Rat.Cast.Order

namespace CollatzResearch.SharedBlockTails

def clock : List ℕ → ℕ
  | [] => 0
  | a::w => a + clock w

def carry : List ℕ → ℤ
  | [] => 0
  | a::w => 3^w.length + 2^a * carry w

inductive Native (q : ℤ) : ℤ → List ℕ → ℤ → Prop where
  | nil (x : ℤ) : Native q x [] x
  | cons {x y z : ℤ} {a : ℕ} {w : List ℕ}
      (step : (2:ℤ)^a*y = 3*x+q) (tail : Native q y w z) : Native q x (a::w) z

/-- Exact numerator identity for a chronological list of native odd steps. -/
theorem nativeAffine {q x z : ℤ} {w : List ℕ} (ht : Native q x w z) :
    (2:ℤ)^(clock w)*z = 3^w.length*x + q*carry w := by
  induction ht with
  | nil => simp [clock,carry]
  | @cons x y z a w step tail ih =>
    simp only [clock,carry,List.length_cons,pow_add,pow_succ]
    calc
      2^a*2^(clock w)*z = 2^a*(2^(clock w)*z) := by ring
      _ = 3^w.length*(2^a*y) + q*(2^a*carry w) := by rw [ih]; ring
      _ = 3^w.length*3*x + q*(3^w.length+2^a*carry w) := by rw [step]; ring

/-- The two distinct native sources differ by a nonzero multiple of the
    entire binary clock, also for a common rational denominator q. -/
theorem sharedQuotient {q x y X Y : ℤ} {w : List ℕ}
    (hx : Native q x w X) (hy : Native q y w Y) (hne : x ≠ y) :
    ∃ G : ℤ, G ≠ 0 ∧ x-y=(2:ℤ)^(clock w)*G := by
  have eqn : 3^w.length*(x-y) = (2:ℤ)^(clock w)*(X-Y) := by
    calc
      3^w.length*(x-y) = (3^w.length*x+q*carry w)-(3^w.length*y+q*carry w) := by ring
      _ = (2:ℤ)^(clock w)*(X-Y) := by rw [←nativeAffine hx,←nativeAffine hy]; ring
  have cop : IsCoprime (2:ℤ) 3 := ⟨-1,1,by decide⟩
  obtain ⟨G,hG⟩ := (cop.pow (m:=clock w) (n:=w.length)).dvd_of_dvd_mul_left ⟨X-Y,eqn⟩
  refine ⟨G,?_,hG⟩
  intro hz
  rw [hz,mul_zero] at hG
  exact hne (sub_eq_zero.mp hG)

/-- Inverse affine slope and preterminal sum of prefix slopes. -/
def slope : List ℕ → ℚ
  | [] => 1
  | a::w => ((2:ℚ)^a/3)*slope w

def mass : List ℕ → ℚ
  | [] => 0
  | a::w => 1+((2:ℚ)^a/3)*mass w

def source (q : ℚ) (w : List ℕ) (Y : ℚ) : ℚ := slope w*Y-(q/3)*mass w

private theorem slopeAppend (u v : List ℕ) : slope (u++v)=slope u*slope v := by
  induction u with
  | nil => simp [slope]
  | cons a w ih => simp only [List.cons_append,slope,ih]; ring

private theorem massAppend (u v : List ℕ) : mass (u++v)=mass u+slope u*mass v := by
  induction u with
  | nil => simp [slope,mass]
  | cons a w ih => simp only [List.cons_append,slope,mass,ih]; ring

/-- Two actual native words can have different terminal words and endpoints.
    Removing their equal prefix leaves just the two signed tail sums. -/
theorem signedTwoTails (q X Y : ℚ) (u v w : List ℕ) :
    source q (u++v) X - source q (u++w) Y - slope (u++v)*X + slope (u++w)*Y =
      (q/3)*slope u*(mass w-mass v) := by
  simp only [source,massAppend,slopeAppend]
  ring

/-- The native one-step inverse used by `source` is the exact integer branch. -/
theorem nativeSource {q x z : ℤ} {w : List ℕ} (ht : Native q x w z) :
    source q w z = (x:ℚ) := by
  induction ht with
  | nil => simp [source,slope,mass]
  | @cons x y z a w step tail ih =>
    have hq : (2:ℚ)^a*(y:ℚ)=3*(x:ℚ)+(q:ℚ) := by exact_mod_cast step
    calc
      source q (a::w) z = ((2:ℚ)^a/3)*source q w z-(q:ℚ)/3 := by
        simp only [source,mass,slope]; ring
      _ = (x:ℚ) := by rw [ih]; linear_combination hq/3

end CollatzResearch.SharedBlockTails
