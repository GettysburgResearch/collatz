import Lean.Elab.Tactic.Omega

/-!
The finite integer-window estimate behind stationary-seed replacement.
`f n` is a zero/one membership indicator. No probability, stationary law,
analytic limit, or Collatz convergence statement is formalized here.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.StationaryWindow

def window (f : Nat → Nat) (start : Nat) : Nat → Nat
  | 0 => 0
  | len + 1 => window f start len + f (start + len)

/-- Splitting an interval retains the exact same membership function. -/
theorem window_add (f : Nat → Nat) (start left right : Nat) :
    window f start (left + right) =
      window f start left + window f (start + left) right := by
  induction right with
  | zero => simp [window]
  | succ right ih => simp [window, ih, Nat.add_assoc]

/-- A membership indicator counts at most one point at each integer. -/
theorem window_le (f : Nat → Nat) (hf : ∀ n, f n ≤ 1)
    (start len : Nat) : window f start len ≤ len := by
  induction len with
  | zero => simp [window]
  | succ len ih =>
    have hlast := hf (start + len)
    simp only [window]
    omega

private theorem shift_balance (f : Nat → Nat) (shift len : Nat) :
    window f 0 len + window f len shift =
      window f 0 shift + window f shift len := by
  have hleft := window_add f 0 len shift
  have hright := window_add f 0 shift len
  simp only [Nat.zero_add] at hleft hright
  have hsame : window f 0 (len + shift) = window f 0 (shift + len) := by
    rw [Nat.add_comm len shift]
  omega

/--
The absolute difference of two length-`len` integer-window counts is at most
`min shift len`. The two directed inequalities avoid subtraction conventions.
-/
theorem window_shift_bound (f : Nat → Nat) (hf : ∀ n, f n ≤ 1)
    (shift len : Nat) :
    window f shift len ≤ window f 0 len + min shift len ∧
      window f 0 len ≤ window f shift len + min shift len := by
  have hbalance := shift_balance f shift len
  have hleft := window_le f hf 0 shift
  have hright := window_le f hf len shift
  have hsource := window_le f hf 0 len
  have htarget := window_le f hf shift len
  by_cases hsmall : shift ≤ len
  · simp only [Nat.min_eq_left hsmall]
    omega
  · have hlarge : len ≤ shift := by omega
    simp only [Nat.min_eq_right hlarge]
    omega

end Collatz.StationaryWindow
