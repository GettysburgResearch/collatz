import Mathlib.Data.Nat.Basic
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Convert
import Mathlib.Tactic.Ring

/-! Finite identities for the persistent dyadic interface of a Boolean Collatz label. -/
namespace DyadicBoundary

def Changes (c : ℕ → Bool) (n : ℕ) : Prop := c n ≠ c (n + 1)

def child (c : ℕ → Bool) (n : ℕ) : ℕ :=
  if c (2 * n + 1) = c n then 2 * n + 1 else 2 * n

variable (c : ℕ → Bool)
variable (ev : ∀ n, c (2 * n) = c n)
variable (od : ∀ n, c (2 * n + 1) = c (3 * n + 2))

include ev in
theorem rightColor (n : ℕ) : c (2 * n + 2) = c (n + 1) := by
  simpa only [Nat.mul_add, Nat.mul_one] using ev (n + 1)

include ev in
theorem childColors (n : ℕ) (boundary : Changes c n) :
    c (child c n) = c n ∧ c (child c n + 1) = c (n + 1) := by
  have hL := ev n
  have hR := rightColor c ev n
  have h := boundary
  unfold Changes at h
  cases h₁ : c n <;> cases h₂ : c (n + 1) <;> cases h₃ : c (2 * n + 1) <;>
    simp_all [child, Nat.add_assoc]

include ev in
theorem uniqueChangingChild (n : ℕ) (boundary : Changes c n) :
    Changes c (2 * n) ↔ ¬ Changes c (2 * n + 1) := by
  have hL := ev n
  have hR := rightColor c ev n
  unfold Changes at *
  cases h₁ : c n <;> cases h₂ : c (n + 1) <;> cases h₃ : c (2 * n + 1) <;>
    simp_all [Nat.add_assoc]

include ev in
theorem colorEightFour (q : ℕ) : c (8 * q + 4) = c (2 * q + 1) := by
  calc
    _ = c (2 * (2 * q + 1)) := by convert ev (2 * (2 * q + 1)) using 2; omega
    _ = _ := ev _

include ev od in
theorem colorEightFive (q : ℕ) : c (8 * q + 5) = c (2 * q + 1) := by
  calc
    _ = c (3 * (4 * q + 2) + 2) := by convert od (4 * q + 2) using 2; omega
    _ = c (2 * (3 * q + 2)) := by convert ev (2 * (3 * q + 2)) using 2; omega
    _ = c (3 * q + 2) := ev _
    _ = _ := (od q).symm

include ev od in
theorem forbidden100 (q : ℕ) : ¬ Changes c (8 * q + 4) := by
  unfold Changes
  have h₁ := colorEightFour c ev q
  have h₂ := colorEightFive c ev od q
  exact not_not_intro (h₁.trans h₂.symm)

/-- On the surviving left endpoints the lowest set bit is either one or two. -/
def lift (n : ℕ) : ℕ := (3 * n + (if n % 2 = 0 then 2 else 1)) / 2

@[simp] theorem liftOdd (q : ℕ) : lift (2 * q + 1) = 3 * q + 2 := by
  unfold lift
  split <;> omega

@[simp] theorem liftEven (q : ℕ) : lift (4 * q + 2) = 6 * q + 4 := by
  unfold lift
  split <;> omega

include od in
theorem liftOddColor (q : ℕ) : c (lift (2 * q + 1)) = c (2 * q + 1) := by
  rw [liftOdd, od]

include ev od in
theorem liftEvenColor (q : ℕ) : c (lift (4 * q + 2)) = c (4 * q + 2) := by
  rw [liftEven]
  calc
    _ = c (3 * q + 2) := by convert ev (3 * q + 2) using 2; omega
    _ = c (2 * q + 1) := (od q).symm
    _ = _ := by convert (ev (2 * q + 1)).symm using 2; omega

include ev od in
theorem liftEvenBoundary (q : ℕ) (boundary : Changes c (4 * q + 2)) :
    Changes c (lift (4 * q + 2)) := by
  unfold Changes at *
  have h₁ := liftEvenColor c ev od q
  have h₂ := liftOddColor c od (2 * q + 1)
  have h : 2 * (2 * q + 1) + 1 = 4 * q + 2 + 1 := by omega
  rw [h] at h₂
  have h' : lift (4 * q + 2 + 1) = lift (4 * q + 2) + 1 := by
    rw [← h, liftOdd, liftEven]
    omega
  rwa [← h₁, ← h₂, h'] at boundary

/-- The two output zero transitions and the one output one transition are
    logical AND of the previous and current source digits. -/
theorem digitTransitions (q : ℕ) :
    lift (2 * (4 * q + 2) + 1) = 2 * lift (4 * q + 2) ∧
    lift (2 * (2 * q + 1)) = 2 * lift (2 * q + 1) ∧
    lift (2 * (2 * q + 1) + 1) = 2 * lift (2 * q + 1) + 1 := by
  have h : 2 * (2 * q + 1) = 4 * q + 2 := by omega
  constructor
  · rw [liftOdd, liftEven]
    omega
  constructor
  · rw [h, liftEven, liftOdd]
    omega
  · rw [liftOdd, liftOdd]
    omega

/-- A right endpoint whose color can block scaling is exactly a tripling test. -/
theorem criticalMidpoint (q : ℕ) :
    2 * lift (4 * q + 2) + 1 = 3 * (4 * q + 3) := by
  rw [liftEven]
  omega

include ev od in
/-- Long runs force an actual tripling disagreement at their right endpoint. -/
theorem tripledSeven (q : ℕ) : c (3 * (8 * q + 7)) = c (8 * q + 6) := by
  have h₁ := colorEightFive c ev od (3 * q + 2)
  have h₂ := od (2 * q + 1)
  have h₃ := ev (4 * q + 3)
  have h₄ : 3 * (8 * q + 7) = 8 * (3 * q + 2) + 5 := by omega
  have h₅ : 2 * (3 * q + 2) + 1 = 3 * (2 * q + 1) + 2 := by omega
  have h₆ : 2 * (2 * q + 1) + 1 = 4 * q + 3 := by omega
  have h₇ : 2 * (4 * q + 3) = 8 * q + 6 := by omega
  rw [h₄, h₁, h₅, ← h₂, h₆, ← h₃, h₇]

include od in
theorem shiftedSingle (n : ℕ) (hn : 0 < n) : c (2 * n - 1) = c (3 * n - 1) := by
  obtain ⟨a, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : n ≠ 0)
  convert od a using 2 <;> omega

include od in
theorem shiftedPowers (k n : ℕ) (hn : 0 < n) :
    c (2 ^ k * n - 1) = c (3 ^ k * n - 1) := by
  induction k generalizing n with
  | zero => simp
  | succ k ih =>
    have h : 0 < 2 ^ k * n := Nat.mul_pos (Nat.pow_pos (by decide)) hn
    calc
      _ = c (2 * (2 ^ k * n) - 1) := by rw [pow_succ]; congr 2; ring
      _ = c (3 * (2 ^ k * n) - 1) := shiftedSingle c od _ h
      _ = c (2 ^ k * (3 * n) - 1) := by congr 2; ring
      _ = c (3 ^ k * (3 * n) - 1) := ih _ (by omega)
      _ = _ := by rw [pow_succ]; congr 2; ring

include ev od in
theorem plusSingle (n : ℕ) : c (4 * n + 1) = c (3 * n + 1) := by
  calc
    _ = c (3 * (2 * n) + 2) := by convert od (2 * n) using 2; omega
    _ = _ := by convert ev (3 * n + 1) using 2; omega

include ev od in
theorem plusPowers (k n : ℕ) : c (4 ^ k * n + 1) = c (3 ^ k * n + 1) := by
  induction k generalizing n with
  | zero => simp
  | succ k ih =>
    calc
      _ = c (4 * (4 ^ k * n) + 1) := by rw [pow_succ]; congr 2; ring
      _ = c (3 * (4 ^ k * n) + 1) := plusSingle c ev od _
      _ = c (4 ^ k * (3 * n) + 1) := by congr 2; ring
      _ = c (3 ^ k * (3 * n) + 1) := ih _
      _ = _ := by rw [pow_succ]; congr 2; ring

include ev od in
theorem evenDepthRightResidueTwo (k p a : ℕ) (h : 3 * (2 * a + 1) = 4 ^ (k + 1) * p + 1) :
    c (2 * a + 1) = c (3 ^ (k + 1) * p + 2) := by
  rw [pow_succ] at h ⊢
  have hstep : 3 * a + 2 = 4 ^ k * (2 * p) + 1 := by
    have hsource : 4 ^ k * 4 * p = 4 * (4 ^ k * p) := by ring
    have htarget : 4 ^ k * (2 * p) = 2 * (4 ^ k * p) := by ring
    rw [hsource] at h
    rw [htarget]
    omega
  rw [od, hstep, plusPowers c ev od]
  have hdouble : 3 ^ k * (2 * p) = 2 * (3 ^ k * p) := by ring
  rw [hdouble, od]
  congr 2
  ring

/-- Signed dynamics only track the fixed displacement. The marked source may
    simultaneously be a very large genuine positive integer. -/
def signedT (x : ℤ) : ℤ := if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def departures : ℕ → ℤ → ℕ
  | 0, _ => 0
  | k + 1, x => departures k (signedT x) + (if x % 2 = 0 then 0 else 1)

theorem signedStep (u d : ℤ) :
    signedT (2 * u + d) = (if d % 2 = 0 then u else 3 * u) + signedT d := by
  unfold signedT
  split_ifs <;> omega

theorem magnifiedEndpoint (k : ℕ) (p d : ℤ) :
    signedT^[k] (2 ^ k * p + d) = 3 ^ departures k d * p + signedT^[k] d := by
  induction k generalizing p d with
  | zero => simp [departures]
  | succ k ih =>
    rw [Function.iterate_succ_apply, Function.iterate_succ_apply, pow_succ]
    have hscale : 2 ^ k * 2 * p = 2 * (2 ^ k * p) := by ring
    rw [hscale, signedStep]
    by_cases h : d % 2 = 0
    · simpa [departures, h] using ih p (signedT d)
    · have htr : 3 * (2 ^ k * p) = 2 ^ k * (3 * p) := by ring
      simp only [h, ↓reduceIte, htr, ih, departures, pow_succ]
      ring

#print axioms childColors
#print axioms forbidden100
#print axioms liftEvenBoundary
#print axioms digitTransitions
#print axioms tripledSeven
#print axioms shiftedPowers
#print axioms plusPowers
#print axioms evenDepthRightResidueTwo
#print axioms magnifiedEndpoint

end DyadicBoundary
