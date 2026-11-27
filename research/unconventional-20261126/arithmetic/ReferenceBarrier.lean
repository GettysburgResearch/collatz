import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.Ring

/-!
Finite ordinary kernels for the inverse-leaf reference obstruction. The
real-density summation and finite-cylinder enumeration are written separately.
-/

namespace ReferenceBarrier

def step (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3*n+1)/2

def run : ℕ → ℕ → ℕ
  | 0, n => n
  | h+1, n => run h (step n)

def odds : ℕ → ℕ → ℕ
  | 0, _ => 0
  | h+1, n => odds h (step n) + n%2

-- The high-bit lift is the elementary PR192 SourceDeletion argument.
theorem lift (h n t : ℕ) : run h (n+2^h*t) = run h n + 3^(odds h n)*t := by
  induction h generalizing n t with
  | zero => simp [run, odds]
  | succ h ih =>
    have e : 2^(h+1)*t = 2*(2^h*t) := by ring
    by_cases par : n%2=0
    · have s : step (n+2^(h+1)*t) = step n + 2^h*t := by
        rw [e]; unfold step; split <;> omega
      simp only [run, odds]; rw [s, ih, par, Nat.add_zero]
    · have o : n%2=1 := by omega
      have s : step (n+2^(h+1)*t) = step n + 2^h*(3*t) := by
        rw [e, show 2^h*(3*t)=3*(2^h*t) by ring]; unfold step; split <;> omega
      simp only [run, odds]; rw [s, ih, o, pow_succ]; ring

theorem min_start (h n : ℕ) : n ≤ 2^h * run h n := by
  induction h generalizing n with
  | zero => simp [run]
  | succ h ih =>
    have one : n ≤ 2 * step n := by unfold step; split <;> omega
    calc n ≤ 2 * step n := one
         _ ≤ 2 * (2^h * run h (step n)) := Nat.mul_le_mul_left _ (ih _)
         _ = 2^(h+1) * run (h+1) n := by rw [run]; ring

theorem triple_clock {h m : ℕ} (hit : run h (3*m) = 1) : 5 ≤ h := by
  by_contra! hsmall
  have hpow : 2^h ≤ 16 := by interval_cases h <;> decide
  have mn := min_start h (3*m)
  rw [hit, Nat.mul_one] at mn
  have bound : m ≤ 5 := by omega
  interval_cases m <;> interval_cases h <;> revert hit <;> decide

theorem run_add (a b n : ℕ) : run (a+b) n = run b (run a n) := by
  induction a generalizing n with
  | zero => simp [run]
  | succ a ih => rw [Nat.succ_add, run, run, ih]

theorem run_power (a b : ℕ) : run a (2^(a+b)) = 2^b := by
  induction a with
  | zero => simp [run]
  | succ a ih =>
    rw [Nat.succ_add, pow_succ, run]
    have half (x : ℕ) : step (x*2) = x := by unfold step; split <;> omega
    rw [half, ih]

theorem five_steps (t : ℕ) :
    run 5 (32*t+23) = 27*t+20 ∧ run 5 (3*(32*t+23)) = 27*t+20 := by
  have lo := lift 5 23 t
  have hi := lift 5 69 (3*t)
  change run 5 (23+32*t) = 20+27*t at lo
  change run 5 (69+32*(3*t)) = 20+9*(3*t) at hi
  constructor
  · rw [show 32*t+23=23+32*t by omega, lo]; omega
  · rw [show 3*(32*t+23)=69+32*(3*t) by omega, hi]; omega

/-- For the whole infinite synchronized family, no smaller ordinary upper
anchor that reaches 1 can preserve even one extra low source bit. -/
theorem no_spare_bit {t k m h l : ℕ} (power : 27*t+20=2^k)
    (positive : 0<l) (same : 32*t+23 = m + 2^(h+1)*l)
    (hit : run h (3*m)=1) : False := by
  have h5 := triple_clock hit
  obtain ⟨j,rfl⟩ := Nat.exists_eq_add_of_le h5
  have up : 32*t+23 < 2^(5+k) := by
    rw [pow_add, ← power]; omega
  have low : 2^(5+j) < 32*t+23 := by
    have one : 2^(5+j+1) ≤ 2^(5+j+1)*l := Nat.le_mul_of_pos_right _ positive
    rw [pow_succ] at one same
    have pos : 0 < 2^(5+j) := Nat.two_pow_pos _
    omega
  have jk0 : (2:ℕ)^(5+j) < 2^(5+k) := lt_trans low up
  have jk : j<k := by
    by_contra! wrong
    have := Nat.pow_le_pow_right (by decide : 0 < 2) (Nat.add_le_add_left wrong 5)
    omega
  obtain ⟨b,kb⟩ := Nat.exists_eq_add_of_le jk
  have even : run (5+j) (3*(32*t+23)) = 2^b * 2 := by
    rw [run_add, (five_steps _).2, power, kb, show j+1+b=j+(b+1) by omega, run_power,
      pow_succ]
  have mixed := lift (5+j) (3*m) (6*l)
  have src : 3*(32*t+23) = 3*m + 2^(5+j)*(6*l) := by rw [same, pow_succ]; ring
  rw [← src, even, hit, show 3^(odds (5+j) (3*m))*(6*l)
      = 2*(3^(odds (5+j) (3*m))*(3*l)) by ring] at mixed
  omega

/-- Number of completions of a budget of reverse shortcut bits that have
already hit an odd triple. The odd predecessor 1 is deleted to enforce first
arrival at 1 on the forward path. -/
def leafCount : ℕ → ℕ → ℕ
  | 0, y => if y%3=0 ∧ y%2=1 then 1 else 0
  | h+1, y =>
      if y%3=0 ∧ y%2=1 then 2^(h+1)
      else leafCount h (2*y) +
        (if y%3=2 ∧ (2*y-1)/3≠1 then leafCount h ((2*y-1)/3) else 0)

theorem leafCount_cap (h y : ℕ) : leafCount h y ≤ 2^h := by
  induction h generalizing y with
  | zero => simp only [leafCount, pow_zero]; split <;> omega
  | succ h ih =>
    simp only [leafCount]
    split
    · omega
    · have e := ih (2*y)
      have o := ih ((2*y-1)/3)
      split <;> rw [pow_succ] <;> omega

theorem one_mod_three_cap (h y : ℕ) (unit : y%3=1) : 3*leafCount h y ≤ 2^h := by
  induction h using Nat.twoStepInduction generalizing y with
  | zero => simp [leafCount, unit]
  | one =>
    have evenResidue : (2*y)%3=2 := by omega
    simp [leafCount, unit, evenResidue]
  | more h ih _ =>
    have evenResidue : (2*y)%3=2 := by omega
    have back : (2*(2*y))%3=1 := by omega
    have recursive := ih (2*(2*y)) back
    have other := leafCount_cap h ((2*(2*y)-1)/3)
    simp only [leafCount, unit, evenResidue, pow_succ]
    simp only [Nat.reduceEqDiff, false_and, true_and, ite_false, Nat.add_zero]
    split <;> omega

/-- Every depth truncation satisfies the 1/12 upper mass bound. -/
theorem root_leaf_cap (h : ℕ) : 12*leafCount h 1 ≤ 2^h := by
  cases h with
  | zero => decide
  | succ h =>
    cases h with
    | zero => decide
    | succ h =>
      have bound := one_mod_three_cap h 4 (by decide)
      simpa [leafCount, pow_succ] using
        (show 12*leafCount h 4 ≤ 2^h*2*2 by omega)

end ReferenceBarrier

#print axioms ReferenceBarrier.no_spare_bit

#print axioms ReferenceBarrier.root_leaf_cap

#print axioms ReferenceBarrier.lift

#print axioms ReferenceBarrier.min_start

#print axioms ReferenceBarrier.triple_clock

#print axioms ReferenceBarrier.run_add

#print axioms ReferenceBarrier.run_power

#print axioms ReferenceBarrier.five_steps

#print axioms ReferenceBarrier.leafCount_cap

#print axioms ReferenceBarrier.one_mod_three_cap
