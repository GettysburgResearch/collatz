import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Algebra.Order.Ring.Abs

/-! An integer edge flux with jumps of size at most one has a quadratic
cost across any two extrema on a circle. -/
set_option autoImplicit false
namespace Collatz.CyclicFlux

private def potential (x : Int) : Int := x * |x|

private theorem increment (x : Int) :
    potential (x+1) - potential x = |x|+|x+1| := by
  unfold potential
  by_cases h : 0≤x
  · rw [abs_of_nonneg h, abs_of_nonneg (show 0≤x+1 by omega)]
    ring
  · rw [abs_of_nonpos (show x≤0 by omega), abs_of_nonpos (show x+1≤0 by omega)]
    ring

private theorem step_up (x y : Int) (hl : x-1 ≤ y) (hu : y ≤ x+1) :
    potential y - potential x ≤ |x|+|y| := by
  have options : y=x-1 ∨ y=x ∨ y=x+1 := by omega
  rcases options with down | same | up
  · have eq := increment y
    rw [show y+1=x by omega] at eq
    have hx := abs_nonneg x
    have hy := abs_nonneg y
    omega
  · rw [same]
    have hx := abs_nonneg x
    omega
  · rw [up]
    exact (increment x).le

private theorem square_le (x y : Int) (h : x≤y) :
    (y-x)^2 ≤ 2*(potential y-potential x) := by
  unfold potential
  by_cases hx : 0≤x
  · rw [abs_of_nonneg hx, abs_of_nonneg (show 0≤y by omega)]
    nlinarith [mul_nonneg (show 0≤y-x by omega) (show 0≤y+3*x by omega)]
  · rw [abs_of_nonpos (show x≤0 by omega)]
    by_cases hy : 0≤y
    · rw [abs_of_nonneg hy]
      nlinarith [sq_nonneg (y+x)]
    · rw [abs_of_nonpos (show y≤0 by omega)]
      nlinarith [mul_nonneg (show 0≤y-x by omega) (show 0≤ -3*y-x by omega)]

/-- Sum of edge-flux magnitudes over the half-open arc [s,s+n). -/
def mass (f : Nat → Int) (s : Nat) : Nat → Int
  | 0 => 0
  | k+1 => mass f s k + |f (s+k)|

private theorem arc (f : Nat → Int) (s n : Nat)
    (jumps : ∀ i, s≤i → i<s+n → f i-1 ≤ f (i+1) ∧ f (i+1) ≤ f i+1) :
    potential (f (s+n))-potential (f s) ≤
        2*mass f s n + |f (s+n)| - |f s| ∧
    potential (f s)-potential (f (s+n)) ≤
        2*mass f s n + |f (s+n)| - |f s| := by
  induction n with
  | zero => simp [mass]
  | succ n ih =>
    have prev := ih (fun i hi hj => jumps i hi (by omega))
    obtain ⟨lo, hi⟩ := jumps (s+n) (by omega) (by omega)
    have up := step_up (f (s+n)) (f (s+n+1)) lo hi
    have down := step_up (f (s+n+1)) (f (s+n)) (by omega) (by omega)
    simp only [mass]
    rw [show s+(n+1)=s+n+1 by omega]
    constructor <;> omega

/-- Split a closed flux walk at any point attaining at least its initial
value. K can be the number of swaps, since it pays every net edge flux. -/
theorem cyclic_range_sq_le (f : Nat → Int) (a b : Nat) (K : Int)
    (closed : f (a+b)=f 0) (ordered : f 0≤f a)
    (jumps : ∀ i, i<a+b → f i-1 ≤ f (i+1) ∧ f (i+1) ≤ f i+1)
    (budget : mass f 0 a + mass f a b ≤ K) : (f a-f 0)^2 ≤ 2*K := by
  have first := (arc f 0 a (fun i _ hi => jumps i (by omega))).1
  have second := (arc f a b (fun i _ hi => jumps i hi)).2
  simp only [Nat.zero_add] at first
  rw [closed] at second
  have gap := square_le (f 0) (f a) ordered
  omega

#print axioms cyclic_range_sq_le
end Collatz.CyclicFlux
