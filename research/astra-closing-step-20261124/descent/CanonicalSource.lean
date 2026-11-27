import Std

namespace Collatz.CanonicalSource

def step (n : Nat) : Nat := if n%2 = 0 then n/2 else (3*n+1)/2

def run (n : Nat) : Nat → Nat
  | 0 => n
  | t+1 => run (step n) t

theorem run_add (n a b : Nat) : run n (a+b) = run (run n a) b := by
  induction a generalizing n with
  | zero => simp [run]
  | succ a ih =>
    rw [Nat.succ_add]
    exact ih (step n)

theorem all_odd (j w : Nat) (hw : 0 < w) :
    run (2^j*w-1) j = 3^j*w-1 := by
  induction j generalizing w with
  | zero => simp [run]
  | succ j ih =>
    have hpos : 0 < 2^j*w := Nat.mul_pos (Nat.pow_pos (by decide)) hw
    have edge (x : Nat) (hx : 0 < x) : step (2*x-1)=3*x-1 := by
      unfold step
      split <;> omega
    have hs : 2^(j+1)*w = 2*(2^j*w) := by rw [Nat.pow_succ]; grind
    have hr : 3*(2^j*w)=2^j*(3*w) := by grind
    rw [hs, run, edge _ hpos, hr, ih (3*w) (by omega), Nat.pow_succ]
    grind

/-- The normalized extra-edge input physically reaches the actual child. -/
theorem normalized_reaches_child (h w u : Nat) (hw : 0 < w)
    (hp : 9*(3^h*w)=4*u+1) :
    run (8*(2^h*w)-1) ((h+3)+2) = 9*u+2 := by
  have form : 8*(2^h*w)=2^(h+3)*w := by rw [Nat.pow_add]; grind
  have land : 3^(h+3)*w-1=12*u+2 := by
    rw [Nat.pow_add]
    have hx : 3^h*3^3*w=27*(3^h*w) := by grind
    rw [hx]
    omega
  have first : step (12*u+2)=6*u+1 := by unfold step; split <;> omega
  have second : step (6*u+1)=9*u+2 := by unfold step; split <;> omega
  rw [form, run_add, all_odd _ _ hw, land]
  simp [run, first, second]

/-- The extra edge on a Mersenne source lands in its smaller exponent's component. -/
theorem adjacent_mersenne (k : Nat) :
    run (2^(k+2)-1) 2 = 9*2^k-1 := by
  have z := all_odd 2 (2^k) (Nat.pow_pos (by decide))
  have he : 2^(k+2)=2^2*(2^k) := by rw [Nat.pow_add, Nat.mul_comm]
  rw [he]
  exact z

#print axioms run_add
#print axioms all_odd
#print axioms normalized_reaches_child
#print axioms adjacent_mersenne

end Collatz.CanonicalSource
