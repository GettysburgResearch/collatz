import Std

namespace Collatz.TraceKernel

def step (x : Nat) : Nat := if x % 2 = 0 then x / 2 else (3*x+1)/2

def run : Nat → Nat → Nat
  | 0, x => x
  | h+1, x => run h (step x)

def oddCount : Nat → Nat → Nat
  | 0, _ => 0
  | h+1, x => oddCount h (step x) + x%2

private theorem step_lift (v r : Nat) :
    step (2*v+r) = 3^(r%2)*v+step r := by
  by_cases hr : r%2=0
  · simp [step, hr, Nat.add_mod]
    omega
  · have ho : r%2=1 := by omega
    simp [step, ho, Nat.add_mod]
    omega

/-- The exact progression after all h binary digits of the source are fixed. -/
theorem row (h u r : Nat) :
    run h (2^h*u+r) = 3^(oddCount h r)*u + run h r := by
  induction h generalizing u r with
  | zero => simp [run, oddCount]
  | succ h ih =>
    have a : 2^(h+1)*u = 2*(2^h*u) := by rw [Nat.pow_succ]; ac_rfl
    have b : 3^(r%2)*(2^h*u) = 2^h*(3^(r%2)*u) := by ac_rfl
    rw [run, a, step_lift, b, ih, oddCount, Nat.pow_add, run, Nat.mul_assoc]

private theorem one_height (x : Nat) : 3^(x%2)*x ≤ 2*step x := by
  by_cases hx : x%2=0
  · simp [step, hx]; omega
  · have ho : x%2=1 := by omega
    simp [step, ho]; omega

/-- A bounded terminal state restricts the number of odd inputs. -/
theorem height (h x : Nat) : 3^(oddCount h x)*x ≤ 2^h * run h x := by
  induction h generalizing x with
  | zero => simp [oddCount, run]
  | succ h ih =>
    rw [oddCount, Nat.pow_add, run]
    calc
      _ = 3^(oddCount h (step x)) * (3^(x%2)*x) := by ac_rfl
      _ ≤ 3^(oddCount h (step x)) * (2*step x) := Nat.mul_le_mul_left _ (one_height x)
      _ = 2*(3^(oddCount h (step x))*step x) := by ac_rfl
      _ ≤ 2*(2^h * run h (step x)) := Nat.mul_le_mul_left _ (ih (step x))
      _ = _ := by rw [Nat.pow_succ]; ac_rfl

/-- With newest bit first, this is the numerator of the composed affine map
at denominator 2^w.length. It is defined for either ternary starting lift. -/
def numerator : List Bool → Int → Int
  | [], x => x
  | false::w, x => numerator w x
  | true::w, x => 3*numerator w x+(2:Int)^w.length

def ones : List Bool → Nat
  | [] => 0
  | false::w => ones w
  | true::w => ones w+1

/-- Every incoming ternary digit below the number of odd steps is erased. -/
theorem suffix_difference (w : List Bool) (x y : Int) :
    numerator w x - numerator w y = (3:Int)^(ones w)*(x-y) := by
  induction w with
  | nil => simp [numerator, ones]
  | cons b w ih =>
    cases b with
    | false => exact ih
    | true =>
      simp only [numerator, ones, Int.pow_succ]
      rw [show 3*numerator w x+2^w.length-(3*numerator w y+2^w.length) =
        3*(numerator w x-numerator w y) by omega, ih]
      ac_rfl

#print axioms row
#print axioms height
#print axioms suffix_difference

end Collatz.TraceKernel
