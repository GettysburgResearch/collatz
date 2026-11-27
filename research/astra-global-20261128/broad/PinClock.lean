import CoreBranching
import Mathlib.Data.Nat.Factorization.Basic

/-! Finite, ordinary arithmetic for the rational-approximant formulation.
For a word w, its eventually-all-odd rational initial value is -num w / den w.
Positive sources make the integer numerator of the difference nonzero. -/
set_option autoImplicit false
set_option warningAsError true

namespace PinClock
open CoreBranching

def twos (x : ℕ) : ℕ := x.factorization 2

def den : List Bool → ℕ
  | [] => 1
  | false :: w => den w
  | true :: w => 3 * den w

def num : List Bool → ℕ
  | [] => 1
  | false :: w => 2 * num w
  | true :: w => 2 * num w + den w

def code (w : List Bool) (n : ℕ) : ℕ := den w * n + num w

def depth : List Bool → ℕ → ℕ
  | [], n => twos (n+1)
  | false :: w, n => if n%2=0 then 1 + depth w (step n) else 0
  | true :: w, n => if n%2=0 then 0 else 1 + depth w (step n)

theorem den_odd (w : List Bool) : den w % 2 = 1 := by
  induction w with
  | nil => rfl
  | cons b w ih =>
    cases b
    · exact ih
    · rw [den, Nat.mul_mod, ih]

theorem num_pos (w : List Bool) : 0 < num w := by
  induction w with
  | nil => decide
  | cons b w ih => cases b <;> simp only [num] <;> omega

theorem code_pos (w : List Bool) (n : ℕ) : 0 < code w n := by
  have := num_pos w
  unfold code
  omega

private theorem twos_double (x : ℕ) (hx : 0<x) : twos (2*x)=1+twos x := by
  unfold twos
  rw [Nat.factorization_mul (by decide) (by omega), Finsupp.add_apply]
  rw [Nat.Prime.factorization_self Nat.prime_two]

private theorem twos_triple (x : ℕ) (hx : 0<x) : twos (3*x)=twos x := by
  unfold twos
  rw [Nat.factorization_mul (by decide) (by omega), Finsupp.add_apply]
  rw [Nat.factorization_eq_zero_of_not_dvd (by decide : ¬ 2 ∣ 3), zero_add]

private theorem twos_odd {x : ℕ} (hx : x%2=1) : twos x=0 := by
  exact Nat.factorization_eq_zero_of_not_dvd (by omega)

private theorem even_eq {n : ℕ} (h : n%2=0) : n=2*step n := by
  simp only [step, h, ite_true]
  omega

private theorem odd_eq {n : ℕ} (h : n%2≠0) : 3*n+1=2*step n := by
  simp only [step, h, ite_false]
  omega

/-- Cross multiplication of the actual affine step on a matching branch. -/
theorem even_code (w : List Bool) (n : ℕ) (h : n%2=0) :
    code (false::w) n = 2*code w (step n) := by
  simp only [code, den, num]
  conv_lhs => rw [even_eq h]
  ring

theorem odd_code (w : List Bool) (n : ℕ) (h : n%2≠0) :
    code (true::w) n = 2*code w (step n) := by
  calc
    code (true::w) n = den w * (3*n+1)+2*num w := by simp [code, den, num]; ring
    _ = 2*code w (step n) := by rw [odd_eq h]; unfold code; ring

/-- The complete dyadic valuation of a pin is its shared parity-prefix length. -/
theorem valuation_code (w : List Bool) (n : ℕ) : twos (code w n)=depth w n := by
  induction w generalizing n with
  | nil => simp [code, den, num, depth]
  | cons b w ih =>
    cases b
    · by_cases h : n%2=0
      · rw [even_code w n h, twos_double _ (code_pos w _), ih, depth, ite_eq_left h]
      · have h1 : n%2=1 := by omega
        rw [depth, ite_eq_right h]
        apply twos_odd
        simp [code, den, num, Nat.add_mod, Nat.mul_mod, den_odd, h1]
    · by_cases h : n%2=0
      · rw [depth, ite_eq_left h]
        apply twos_odd
        simp [code, den, num, Nat.add_mod, Nat.mul_mod, den_odd, h]
      · rw [odd_code w n h, twos_double _ (code_pos w _), ih, depth, ite_eq_right h]

def parityPrefix : ℕ → ℕ → List Bool
  | 0, _ => []
  | k+1, n => (if n%2=0 then false else true) :: parityPrefix k (step n)

/-- The actual prefix cross-multiplies to a shifted ordinary terminal value. -/
theorem actual_code (k n : ℕ) :
    code (parityPrefix k n) n = 2^k * (run k n+1) := by
  induction k generalizing n with
  | zero => simp [parityPrefix, code, den, num, run]
  | succ k ih =>
    by_cases h : n%2=0
    · simp only [parityPrefix, h, ite_true, run]
      rw [even_code _ _ h, ih, pow_succ]
      ring
    · simp only [parityPrefix, h, ite_false, run]
      rw [odd_code _ _ h, ih, pow_succ]
      ring

private theorem even_twos {n : ℕ} (h : n%2=0) : twos (n+1)=0 :=
  twos_odd (by omega)

private theorem odd_twos {n : ℕ} (h : n%2≠0) :
    twos (n+1)=1+twos (step n+1) := by
  have hmul : 3*(n+1)=2*(step n+1) := by have := odd_eq h; omega
  rw [←twos_triple (n+1) (by omega), hmul, twos_double _ (by omega)]

/-- Start immediately after the next even input. -/
def afterEven (n : ℕ) : ℕ := step (run (twos (n+1)) n)

private theorem afterEven_odd {n : ℕ} (h : n%2≠0) :
    afterEven n = afterEven (step n) := by
  unfold afterEven
  rw [odd_twos h, Nat.add_comm 1, run]

def addRun : ℕ → List Bool → List Bool
  | 0, w => false :: w
  | g+1, w => true :: addRun g w

def word : List ℕ → List Bool
  | [] => []
  | g::gs => addRun g (word gs)

theorem depth_addRun (g n : ℕ) (w : List Bool) :
    depth (addRun g w) n =
    if g=twos (n+1) then g+1+depth w (afterEven n) else min g (twos (n+1)) := by
  induction g generalizing n with
  | zero =>
    by_cases h : n%2=0
    · simp [addRun, depth, h, even_twos h, afterEven, run]
    · have hpos := odd_twos h
      have hn : 0≠twos (n+1) := by omega
      simp [addRun, depth, h, hn]
  | succ g ih =>
    by_cases h : n%2=0
    · simp [addRun, depth, h, even_twos h]
    · rw [addRun, depth, ite_eq_right h, ih, odd_twos h, afterEven_odd h]
      by_cases hg : g=twos (step n+1)
      · simp [hg, Nat.add_comm, Nat.add_left_comm]
      · have hne : g+1 ≠ 1+twos (step n+1) := by omega
        rw [ite_eq_right hg, ite_eq_right hne]
        omega

def greedy : ℕ → ℕ → List ℕ
  | 0, _ => []
  | e+1, n => twos (n+1) :: greedy e (afterEven n)

/-- The greedy tuple has strictly better valuation than every different
tuple with the same number of even symbols. Entries are odd-run lengths. -/
theorem greedy_unique (gs : List ℕ) (n : ℕ) :
    gs ≠ greedy gs.length n →
    twos (code (word gs) n) < twos (code (word (greedy gs.length n)) n) := by
  induction gs generalizing n with
  | nil => simp [greedy]
  | cons g gs ih =>
    intro h
    simp only [List.length_cons, greedy, word, valuation_code, depth_addRun, ite_true]
    by_cases he : g=twos (n+1)
    · rw [ite_eq_left he]
      have ht : gs ≠ greedy gs.length (afterEven n) := by
        intro htail
        apply h
        exact congrArg₂ List.cons he htail
      have hlt := ih (afterEven n) ht
      rw [valuation_code, valuation_code] at hlt
      omega
    · rw [ite_eq_right he]
      omega

#print axioms valuation_code
#print axioms actual_code
#print axioms depth_addRun
#print axioms greedy_unique

end PinClock
