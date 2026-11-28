import StoppedRecord
import Mathlib.Tactic.Ring

/-! Finite native cylinder identities for the grade difference of two odd affine sources. -/
set_option autoImplicit false
set_option warningAsError true
namespace Collatz.MixedParity
open CoreBranching Collatz.CofactorDescent Collatz.StoppedRecord

private theorem step_lift (x m : ℕ) :
    step (x + 2*m) = step x + 3^(x%2)*m := by
  have hb : (x + 2*m)%2=x%2 := by omega
  by_cases hx : x%2=0
  · simp only [step, hb, hx, ite_true, pow_zero, one_mul]
    omega
  · have ho : x%2=1 := by omega
    simp only [step, hb, ho, pow_one]
    split <;> omega

theorem native_lift (t x m : ℕ) :
    run t (x+2^t*m)=run t x+3^(odds t x)*m ∧
    odds t (x+2^t*m)=odds t x := by
  induction t generalizing x m with
  | zero => simp [run, odds]
  | succ t ih =>
    have he : 2^(t+1)*m = 2*(2^t*m) := by ring
    have hp : (x+2*(2^t*m))%2=x%2 := by omega
    have ha : 3^(x%2)*(2^t*m)=2^t*(3^(x%2)*m) := by ring
    obtain ⟨hs,hg⟩ := ih (step x) (3^(x%2)*m)
    rw [he]
    constructor
    · simp only [run, step_lift, ha, hs, odds, pow_add]
      ring
    · simp only [odds, hp, step_lift, ha, hg]

def source (A a n : ℕ) : ℕ := A*n+a

def gradeGap (t A a B b n : ℕ) : ℤ :=
  (odds t (source A a n) : ℤ) - (odds t (source B b n) : ℤ)

def bit (t A a n : ℕ) : ℕ := run t (source A a n)%2

def mixed (t A a B b n : ℕ) : ℤ :=
  if bit t A a n = bit t B b n then 0 else 1

private theorem source_shift (t A a n : ℕ) :
    source A a (n+2^t)=source A a n+2^t*A := by
  unfold source
  ring

theorem sibling_grade (t A a B b n : ℕ) :
    gradeGap t A a B b (n+2^t)=gradeGap t A a B b n := by
  simp only [gradeGap, source_shift, (native_lift _ _ _).2]

theorem sibling_bits (t A a n : ℕ) (hA : A%2=1) :
    bit t A a n + bit t A a (n+2^t) = 1 := by
  unfold bit
  rw [source_shift, (native_lift _ _ _).1, Nat.add_mod, Nat.mul_mod, hA]
  have ho : 3^(odds t (source A a n))%2=1 := by
    simp [Nat.pow_mod]
  rw [ho]
  omega

theorem gap_next (t A a B b n : ℕ) :
    gradeGap (t+1) A a B b n =
      gradeGap t A a B b n + (bit t A a n : ℤ) - (bit t B b n : ℤ) := by
  unfold gradeGap bit
  rw [odds_add t 1, odds_add t 1]
  simp only [odds, add_zero, Nat.cast_add]
  ring

/-- Raw two-child sums give the true martingale step and its mixed-date variance. -/
theorem sibling_moments (t A a B b n : ℕ) (hA : A%2=1) (hB : B%2=1) :
    gradeGap (t+1) A a B b n + gradeGap (t+1) A a B b (n+2^t) =
        2*gradeGap t A a B b n ∧
    (gradeGap (t+1) A a B b n)^2 + (gradeGap (t+1) A a B b (n+2^t))^2 =
        2*(gradeGap t A a B b n)^2 + 2*mixed t A a B b n := by
  have ha := sibling_bits t A a n hA
  have hb := sibling_bits t B b n hB
  have ha0 : bit t A a n < 2 := Nat.mod_lt _ (by decide)
  have hb0 : bit t B b n < 2 := Nat.mod_lt _ (by decide)
  simp only [gap_next,sibling_grade,mixed]
  interval_cases e : bit t A a n <;> interval_cases f : bit t B b n
  all_goals
    have ea : bit t A a (n+2^t) = 1-bit t A a n := by omega
    have eb : bit t B b (n+2^t) = 1-bit t B b n := by omega
    simp only [ea,eb,e,f]
    norm_num
    constructor <;> ring

end Collatz.MixedParity
