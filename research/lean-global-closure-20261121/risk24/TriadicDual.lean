import Std
import Init.Data.Dyadic.Basic

/-!
A terminating verifier for a proposed signed triadic complementary orbit.

The ordinary map is the shortcut Collatz map.  A proposed dual is represented
by `a / 3^r`, with `a : Int`; the representation need not be reduced.  The
universal existence of a valid triadic dual is NOT assumed or proved here.

This file uses Lean core/Std only.  It has no custom axioms, `sorry`,
`native_decide`, or imported Collatz convergence theorem.
-/

namespace Collatz.TriadicDual

def step (x : Nat) : Nat :=
  if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def intStep (a : Int) : Int :=
  if a % 2 = 0 then a / 2 else (3 * a + 1) / 2

def opposite (x : Nat) (a : Int) : Prop :=
  (x : Int) % 2 + a % 2 = 1

instance (x : Nat) (a : Int) : Decidable (opposite x a) :=
  inferInstanceAs (Decidable ((x : Int) % 2 + a % 2 = 1))

def oddRank (x : Nat) : Nat :=
  Int.trailingZeros ((x : Int) + 1)

theorem step_pos (x : Nat) (hx : 0 < x) : 0 < step x := by
  unfold step
  split <;> omega

theorem trailingZeros_three_mul (n : Nat) (hn : 0 < n) :
    Int.trailingZeros (3 * (n : Int)) = Int.trailingZeros (n : Int) := by
  induction n using Nat.strongRecOn with
  | ind n ih =>
    by_cases hmod : n % 2 = 0
    · have hsmall : n / 2 < n := by omega
      have hpos : 0 < n / 2 := by omega
      have heq : (n : Int) = 2 * ((n / 2 : Nat) : Int) := by omega
      have hmul : 3 * (n : Int) = 2 * (3 * ((n / 2 : Nat) : Int)) := by omega
      rw [hmul, Int.trailingZeros_two_mul (by omega), heq,
        Int.trailingZeros_two_mul (by omega)]
      exact congrArg Nat.succ (ih (n / 2) hsmall hpos)
    · rw [Int.trailingZeros_eq_zero_of_mod_eq (by omega),
        Int.trailingZeros_eq_zero_of_mod_eq (by omega)]

theorem oddRank_step (x : Nat) (hx : 0 < x) (hodd : x % 2 = 1) :
    oddRank (step x) + 1 = oddRank x := by
  have hhalf : 0 < (x + 1) / 2 := by omega
  have hxeq : (x : Int) + 1 = 2 * (((x + 1) / 2 : Nat) : Int) := by omega
  have hstep : (step x : Int) + 1 = 3 * (((x + 1) / 2 : Nat) : Int) := by
    simp only [step, show x % 2 ≠ 0 by omega, ↓reduceIte]
    omega
  unfold oddRank
  rw [hstep, hxeq, Int.trailingZeros_two_mul (by omega), trailingZeros_three_mul _ hhalf]

theorem intStep_ne_zero (a : Int) (ha : a ≠ 0) : intStep a ≠ 0 := by
  unfold intStep
  split <;> omega

def energy (x : Nat) (a : Int) : Nat :=
  2 * x * a.natAbs + if a = 1 then 1 else 0

-- These symbolic product inequalities use exact factors, not sampling.
theorem product_drop_odd (x b x' b' : Nat)
    (hx : 1 < x) (hb : 0 < b) (hx' : 2 * x' = 3 * x + 1)
    (hb' : 2 * b' = b) : x' * b' < x * b := by
  have hlt : (3 * x + 1) * b < (4 * x) * b :=
    Nat.mul_lt_mul_of_pos_right (by omega) hb
  have heq : (3 * x + 1) * b = 4 * (x' * b') := by
    rw [← hx', ← hb']
    simp [Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]
  rw [heq, Nat.mul_assoc] at hlt
  omega

theorem product_drop_even_positive (x b x' b' : Nat)
    (hx : 0 < x) (hb : 1 < b) (hx' : 2 * x' = x)
    (hb' : 2 * b' = 3 * b + 1) : x' * b' < x * b := by
  have hlt : x * (3 * b + 1) < x * (4 * b) :=
    Nat.mul_lt_mul_of_pos_left (by omega) hx
  have heq : x * (3 * b + 1) = 4 * (x' * b') := by
    rw [← hx', ← hb']
    simp [Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]
  have hright : x * (4 * b) = 4 * (x * b) := by
    simp [Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]
  rw [heq, hright] at hlt
  omega

theorem product_drop_even_negative (x b x' b' : Nat)
    (hx : 0 < x) (hb : 0 < b) (hx' : 2 * x' = x)
    (hb' : 2 * b' + 1 = 3 * b) : x' * b' < x * b := by
  have hlt : x * (2 * b') < x * (4 * b) :=
    Nat.mul_lt_mul_of_pos_left (by omega) hx
  have heq : x * (2 * b') = 4 * (x' * b') := by
    rw [← hx']
    simp [Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]
  have hright : x * (4 * b) = 4 * (x * b) := by
    simp [Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]
  rw [heq, hright] at hlt
  omega

theorem energy_of_product_drop (x x' : Nat) (a a' : Int)
    (hprod : x' * a'.natAbs < x * a.natAbs) :
    energy x' a' < energy x a := by
  unfold energy
  simp only [Nat.mul_assoc]
  split <;> split <;> omega

theorem energy_step (x : Nat) (a : Int) (hx : 1 < x)
    (ha : a ≠ 0) (hop : opposite x a) :
    energy (step x) (intStep a) < energy x a := by
  have hb : 0 < a.natAbs := Int.natAbs_pos.mpr ha
  unfold opposite at hop
  by_cases hmod : x % 2 = 0
  · have hodd : a % 2 = 1 := by omega
    have hxstep : 2 * step x = x := by simp only [step, hmod, ↓reduceIte]; omega
    have hastep : 2 * intStep a = 3 * a + 1 := by
      simp only [intStep, show a % 2 ≠ 0 by omega, ↓reduceIte]
      omega
    by_cases hone : a = 1
    · subst a
      simp [intStep, energy]
      omega
    · by_cases hpos : 0 < a
      · have han : (a.natAbs : Int) = a := Int.natAbs_of_nonneg (by omega)
        have hsn : ((intStep a).natAbs : Int) = intStep a :=
          Int.natAbs_of_nonneg (by omega)
        have hbgt : 1 < a.natAbs := by omega
        have hbnext : 2 * (intStep a).natAbs = 3 * a.natAbs + 1 := by omega
        exact energy_of_product_drop _ _ _ _
          (product_drop_even_positive _ _ _ _ (by omega) hbgt hxstep hbnext)
      · have han : (a.natAbs : Int) = -a := Int.ofNat_natAbs_of_nonpos (by omega)
        have hsn : ((intStep a).natAbs : Int) = -intStep a :=
          Int.ofNat_natAbs_of_nonpos (by omega)
        have hbnext : 2 * (intStep a).natAbs + 1 = 3 * a.natAbs := by omega
        exact energy_of_product_drop _ _ _ _
          (product_drop_even_negative _ _ _ _ (by omega) hb hxstep hbnext)
  · have hodd : x % 2 = 1 := by omega
    have haeven : a % 2 = 0 := by omega
    have hxstep : 2 * step x = 3 * x + 1 := by
      simp only [step, hmod, ↓reduceIte]
      omega
    have hastep : 2 * intStep a = a := by
      simp only [intStep, haeven, ↓reduceIte]
      omega
    have hbnext : 2 * (intStep a).natAbs = a.natAbs := by
      have h := congrArg Int.natAbs hastep
      simpa [Int.natAbs_mul] using h
    exact energy_of_product_drop _ _ _ _
      (product_drop_odd _ _ _ _ hx hb hxstep hbnext)

def intRank (x : Nat) (a : Int) : Nat :=
  if a = 0 then oddRank x else energy x a

theorem intRank_step (x : Nat) (a : Int) (hx : 1 < x)
    (hop : opposite x a) :
    intRank (step x) (intStep a) < intRank x a := by
  by_cases ha : a = 0
  · subst a
    have hodd : x % 2 = 1 := by unfold opposite at hop; omega
    have hrank := oddRank_step x (by omega) hodd
    simp [intRank, intStep]
    omega
  · have hnext := intStep_ne_zero a ha
    simp only [intRank, ha, hnext, ↓reduceIte]
    exact energy_step x a hx ha hop

structure State where
  x : Nat
  a : Int
  r : Nat
  deriving Repr

/-- Exact numerator update for the represented rational `a / 3^r`.
At positive denominator exponent the complementary odd branch cancels
one power of 3.  Its numerator is integral because both summands are odd. -/
def numeratorStep (x : Nat) (a : Int) (r : Nat) : Int :=
  if x % 2 = 0 then
    if r = 0 then intStep a else (a + 3 ^ (r - 1)) / 2
  else a / 2

def denominatorStep (x r : Nat) : Nat :=
  if x % 2 = 0 then r - 1 else r

def next (s : State) : State :=
  ⟨step s.x, numeratorStep s.x s.a s.r, denominatorStep s.x s.r⟩

def secondary (s : State) : Nat :=
  if s.r = 0 then intRank s.x s.a else oddRank s.x

def rank (s : State) : Nat × Nat := (s.r, secondary s)

theorem numeratorStep_zero (x : Nat) (a : Int) (hop : opposite x a) :
    numeratorStep x a 0 = intStep a := by
  unfold numeratorStep
  split
  · simp
  · have ha : a % 2 = 0 := by unfold opposite at hop; omega
    simp [intStep, ha]

theorem three_pow_odd (r : Nat) : (3 : Int) ^ r % 2 = 1 := by
  induction r with
  | zero => decide
  | succ r ih => rw [Int.pow_succ]; omega

theorem three_pow_mod_three (r : Nat) (hr : 0 < r) :
    (3 : Int) ^ r % 3 = 0 := by
  cases r with
  | zero => omega
  | succ r => rw [Int.pow_succ]; omega

/-- Exact cancellation of one denominator power, including a possibly
negative numerator.  No reduced-fraction hypothesis is needed. -/
theorem denominator_drop_identity (x : Nat) (a : Int) (r : Nat)
    (hx : x % 2 = 0) (hr : 0 < r) (hop : opposite x a) :
    denominatorStep x r + 1 = r ∧
      2 * numeratorStep x a r = a + 3 ^ (r - 1) := by
  have ha : a % 2 = 1 := by unfold opposite at hop; omega
  have hp := three_pow_odd (r - 1)
  constructor
  · simp only [denominatorStep, hx, ↓reduceIte]
    omega
  · simp only [numeratorStep, hx, show r ≠ 0 by omega, ↓reduceIte]
    omega

/-- When the starting fraction is reduced and a denominator remains, the
represented denominator drop is the exact reduced denominator drop. -/
theorem reduced_denominator_drop (x : Nat) (a : Int) (r : Nat)
    (hx : x % 2 = 0) (hr : 1 < r) (hop : opposite x a) (ha : a % 3 ≠ 0) :
    numeratorStep x a r % 3 ≠ 0 := by
  have hstep := (denominator_drop_identity x a r hx (by omega) hop).2
  have hp := three_pow_mod_three (r - 1) (by omega)
  omega

theorem rank_step (s : State) (hx : 1 < s.x) (hop : opposite s.x s.a) :
    Prod.Lex (· < ·) (· < ·) (rank (next s)) (rank s) := by
  by_cases hr : s.r = 0
  · have hnext : (next s).r = 0 := by
      simp [next, denominatorStep, hr]
    simp only [rank, hnext, hr]
    apply Prod.Lex.right
    simp only [secondary, hr, hnext, ↓reduceIte]
    change intRank (step s.x) (numeratorStep s.x s.a s.r) < intRank s.x s.a
    rw [hr, numeratorStep_zero s.x s.a hop]
    exact intRank_step s.x s.a hx hop
  · by_cases hmod : s.x % 2 = 0
    · apply Prod.Lex.left
      simp only [rank, next, denominatorStep, hmod, ↓reduceIte]
      omega
    · have hnext : (next s).r = s.r := by simp [next, denominatorStep, hmod]
      simp only [rank, hnext]
      apply Prod.Lex.right
      simp only [secondary, hr, hnext, ↓reduceIte]
      change oddRank (step s.x) < oddRank s.x
      have h := oddRank_step s.x (by omega) (by omega)
      omega

def run : Nat → State → State
  | 0, s => s
  | k + 1, s => run k (next s)

def orbit : Nat → Nat → Nat
  | 0, x => x
  | k + 1, x => orbit k (step x)

theorem run_x (k : Nat) (s : State) : (run k s).x = orbit k s.x := by
  induction k generalizing s with
  | zero => rfl
  | succ k ih => simpa only [run, orbit, next] using ih (next s)

/-- Total stopping clock: either the ordinary orbit has reached 1, or the
proposed triadic dual has failed opposite parity.  This function terminates
for every signed numerator and every denominator exponent. -/
def stopClock (s : State) (hx : 0 < s.x) : Nat :=
  if h1 : s.x = 1 then 0
  else if hop : opposite s.x s.a then
    stopClock (next s) (step_pos s.x hx) + 1
  else 0
termination_by rank s
decreasing_by exact rank_step s (by omega) hop

theorem stopClock_spec (s : State) (hx : 0 < s.x) :
    (run (stopClock s hx) s).x = 1 ∨
      ¬opposite (run (stopClock s hx) s).x (run (stopClock s hx) s).a := by
  fun_induction stopClock s hx with
  | case1 s hx h1 => simpa [run] using Or.inl h1
  | case2 s hx h1 hop ih => simpa only [run] using ih
  | case3 s hx h1 hop => simpa [run] using Or.inr hop

/-- A practical finite certificate.  The checking horizon is a total
computable function of the candidate; no all-time premise appears. -/
theorem finite_valid_triadic_reaches_one (s : State) (hx : 0 < s.x)
    (hvalid : ∀ k, k ≤ stopClock s hx →
      opposite (run k s).x (run k s).a) :
    orbit (stopClock s hx) s.x = 1 := by
  obtain h | h := stopClock_spec s hx
  · exact (run_x _ _).symm.trans h
  · exact False.elim (h (hvalid _ (Nat.le_refl _)))

/-- A parity-valid signed triadic complementary orbit certifies ordinary
Collatz convergence.  Its universal existence is an additional open claim. -/
theorem valid_triadic_reaches_one (s : State) (hx : 0 < s.x)
    (hvalid : ∀ k, opposite (run k s).x (run k s).a) :
    ∃ k, orbit k s.x = 1 := by
  exact ⟨stopClock s hx, finite_valid_triadic_reaches_one s hx (fun k _ => hvalid k)⟩

def prefixNumerator (r : Nat) : Int := 2 * 3 ^ r - 2 * 4 ^ r

theorem four_pow_mod_three (r : Nat) : (4 : Int) ^ r % 3 = 1 := by
  induction r with
  | zero => decide
  | succ r ih => rw [Int.pow_succ]; omega

/-- The zero-tail finite complementary sections of input 1 have full
denominator `3^r`, even though their 2-adic limit is the integer 2. -/
theorem prefixNumerator_mod_three (r : Nat) (hr : 0 < r) :
    prefixNumerator r % 3 = 1 := by
  have hthree := three_pow_mod_three r hr
  have hfour := four_pow_mod_three r
  unfold prefixNumerator
  omega

#print axioms rank_step
#print axioms stopClock_spec
#print axioms finite_valid_triadic_reaches_one
#print axioms valid_triadic_reaches_one
#print axioms prefixNumerator_mod_three

end Collatz.TriadicDual
