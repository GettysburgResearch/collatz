import Std

namespace Collatz.BarrierExit

def step (n : Int) : Int :=
  if n % 2 = 0 then n / 2 else (3*n+1)/2

def run : Nat → Int → Int
  | 0, n => n
  | k+1, n => run k (step n)

private theorem step_odd (n : Int) : step (2*n-1) = 3*n-1 := by
  simp [step]
  omega

/-- At positive parameters these are positive ordinary shortcuts.
Each specified intermediate input and output is odd. -/
theorem ascent (k : Nat) (u : Int) :
    run k (4*(2:Int)^k*u-1) = 4*(3:Int)^k*u-1 := by
  induction k generalizing u with
  | zero => simp [run]
  | succ k ih =>
    have he : 4*(2:Int)^(k+1)*u = 2*(4*(2:Int)^k*u) := by
      rw [Int.pow_succ]; ac_rfl
    have he' : 3*(4*(2:Int)^k*u) = 4*(2:Int)^k*(3*u) := by ac_rfl
    rw [run, he, step_odd, he', ih, Int.pow_succ]
    ac_rfl

/-- From q=4A−1 for positive odd A=2v+1 through its first returning
shortcut value w=(9A−1)/2; the two intermediate values exceed q. -/
theorem three_steps (v : Int) :
    step (8*v+3) = 12*v+5 ∧ step (12*v+5) = 18*v+8 ∧
    step (18*v+8) = 9*v+4 := by
  simp [step]
  omega

theorem halvings (h : Nat) (y : Int) : run h ((2:Int)^h*y) = y := by
  induction h generalizing y with
  | zero => simp [run]
  | succ h ih =>
    have he : (2:Int)^(h+1)*y = 2*((2:Int)^h*y) := by
      rw [Int.pow_succ]; ac_rfl
    have hs (v : Int) : step (2*v) = v := by simp [step]
    rw [run, he, hs, ih]

#print axioms ascent
#print axioms three_steps
#print axioms halvings

end Collatz.BarrierExit
