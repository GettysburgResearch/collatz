/-
A complete integer shadow chart, including crossings through zero relative
odd-step count. This extends the positive-exponent chart in PR174.
No assertion of universal convergence is made.
-/
import Collatz.Closure

open CollatzReverseBasin

namespace CollatzCrossShadow

/-- One step, expressed without division. -/
theorem shortcut_balance (n : Nat) :
    2 * shortcut n = 3 ^ (n % 2) * n + n % 2 := by
  rcases Nat.mod_two_eq_zero_or_one n with h | h <;> simp [shortcut, h] <;> omega

/-- The coefficients may have either relative order; the debt is signed. -/
structure Frame where
  left : Int
  right : Int
  debt : Int
  deriving Repr

/-- `left*x - right*y = debt`, in ordinary integer values. -/
def Holds (s : Frame) (x y : Nat) : Prop :=
  s.left * (x : Int) - s.right * (y : Int) = s.debt

/-- One simultaneous step. A common factor of three need not be canceled. -/
def advance (s : Frame) (e f : Nat) : Frame where
  left := (3 : Int)^f * s.left
  right := (3 : Int)^e * s.right
  debt := ((3 : Int)^(e+f) * s.debt +
    (3 : Int)^f * s.left * (e : Int) -
    (3 : Int)^e * s.right * (f : Int)) / 2

private theorem balance_int (n : Nat) :
    2 * (shortcut n : Int) = (3 : Int)^(n % 2) * (n : Int) + (n % 2 : Nat) := by
  exact_mod_cast shortcut_balance n

/-- The unreduced shadow remains exact even when one odd count overtakes the other. -/
theorem advance_holds (s : Frame) (x y : Nat) (h : Holds s x y) :
    Holds (advance s (x%2) (y%2)) (shortcut x) (shortcut y) := by
  have hx := balance_int x
  have hy := balance_int y
  have he : (3 : Int)^(x%2+y%2) = (3 : Int)^(x%2) * (3 : Int)^(y%2) := by
    rw [Int.pow_add]
  unfold Holds at h ⊢
  unfold advance
  dsimp only
  rw [he]
  have hnum :
      (3 : Int)^(x%2) * (3 : Int)^(y%2) * s.debt +
        (3 : Int)^(y%2) * s.left * (x%2 : Nat) -
        (3 : Int)^(x%2) * s.right * (y%2 : Nat) =
      2 * ((3 : Int)^(y%2) * s.left * (shortcut x : Int) -
        (3 : Int)^(x%2) * s.right * (shortcut y : Int)) := by
    rw [← h]
    calc
      _ = (3 : Int)^(y%2) * s.left *
          ((3 : Int)^(x%2) * (x : Int) + (x%2 : Nat)) -
          (3 : Int)^(x%2) * s.right *
          ((3 : Int)^(y%2) * (y : Int) + (y%2 : Nat)) := by grind
      _ = _ := by rw [← hx, ← hy]; grind
  rw [hnum]
  omega

/-- Ordinary shortcut iteration. -/
def iter : Nat → Nat → Nat
  | 0, n => n
  | t+1, n => iter t (shortcut n)

/-- A whole simultaneous ordinary trajectory of frames. -/
def trace (s : Frame) (x y : Nat) : Nat → Frame
  | 0 => s
  | t+1 => trace (advance s (x%2) (y%2)) (shortcut x) (shortcut y) t

/-- The exact trace theorem requires no positivity or relative-count hypothesis. -/
theorem trace_holds (s : Frame) (x y t : Nat) (h : Holds s x y) :
    Holds (trace s x y t) (iter t x) (iter t y) := by
  induction t generalizing s x y with
  | zero => exact h
  | succ t ih => exact ih _ _ _ (advance_holds s x y h)

/-- Initial frame for the `3m-1` closure pair. -/
def psiFrame : Frame := ⟨3, 1, 1⟩

theorem psi_frame_holds (m : Nat) (hm : 0 < m) :
    Holds psiFrame m (3*m-1) := by
  unfold Holds psiFrame
  dsimp only
  omega

/-- A certificate on the member arm gives an exact terminal Diophantine equation. -/
theorem psi_terminal_equation (m t : Nat) (hm : 0 < m)
    (hc : iter t (3*m-1) = 1) :
    let s := trace psiFrame m (3*m-1) t
    s.left * (iter t m : Int) = s.right + s.debt := by
  have h := trace_holds psiFrame m (3*m-1) t (psi_frame_holds m hm)
  unfold Holds at h
  rw [hc] at h
  simp only [Int.natCast_one, Int.mul_one] at h
  dsimp only
  omega

/-- The ordinary trajectory never leaves the positive integers. -/
theorem iter_pos (t n : Nat) (hn : 0 < n) : 0 < iter t n := by
  induction t generalizing n with
  | zero => exact hn
  | succ t ih =>
    apply ih
    unfold shortcut
    split <;> omega

/-- Bridge to the source project's exact ordinary-time certificate. -/
theorem hits_iff_iter (t n : Nat) : Hits n t ↔ iter t n = 1 := by
  induction t generalizing n with
  | zero => rfl
  | succ t ih => exact ih (shortcut n)

/-- Taking any fixed number of ordinary steps preserves membership in the basin. -/
theorem basin_iter (t n : Nat) : Basin (iter t n) ↔ Basin n := by
  induction t generalizing n with
  | zero => rfl
  | succ t ih => exact (ih (shortcut n)).trans (CollatzClosure.basin_step n)

def oddCount : Nat → Nat → Nat
  | 0, _ => 0
  | t+1, n => n%2 + oddCount t (shortcut n)

/-- The left coefficient counts odd steps on the other arm. -/
theorem trace_left (s : Frame) (x y t : Nat) :
    (trace s x y t).left = (3 : Int)^(oddCount t y) * s.left := by
  induction t generalizing s x y with
  | zero => simp [trace, oddCount]
  | succ t ih =>
    rw [trace, ih]
    simp only [advance, oddCount, Int.pow_add]
    grind

/-- The right coefficient counts odd steps on the source arm. -/
theorem trace_right (s : Frame) (x y t : Nat) :
    (trace s x y t).right = (3 : Int)^(oddCount t x) * s.right := by
  induction t generalizing s x y with
  | zero => simp [trace, oddCount]
  | succ t ih =>
    rw [trace, ih]
    simp only [advance, oddCount, Int.pow_add]
    grind

/-- Positive coefficients stay positive at every clock. -/
theorem trace_left_pos (s : Frame) (x y t : Nat) (ha : 0 < s.left) :
    0 < (trace s x y t).left := by
  rw [trace_left]
  exact Int.mul_pos (Int.pow_pos (by decide)) ha

/-- The terminal equation in odd-step coordinates, with both count orders allowed. -/
theorem psi_terminal_counts (m t : Nat) (hm : 0 < m)
    (hc : iter t (3*m-1) = 1) :
    (3 : Int)^(oddCount t (3*m-1)+1) * (iter t m : Int) =
      (3 : Int)^(oddCount t m) + (trace psiFrame m (3*m-1) t).debt := by
  have h := psi_terminal_equation m t hm hc
  dsimp only at h
  rw [trace_left, trace_right] at h
  simp only [psiFrame, Int.mul_one] at h
  rw [Int.pow_succ]
  exact h

/-- A strict terminal debt bound gives an actual smaller ordinary iterate.
The guard is deliberately explicit: it is not proved for every member certificate. -/
theorem psi_terminal_descent (m t : Nat) (hm : 0 < m)
    (hc : iter t (3*m-1) = 1)
    (hguard : let s := trace psiFrame m (3*m-1) t
      s.right + s.debt < s.left * (m : Int)) :
    iter t m < m := by
  let s := trace psiFrame m (3*m-1) t
  have he : s.left * (iter t m : Int) = s.right + s.debt :=
    psi_terminal_equation m t hm hc
  have ha : 0 < s.left := trace_left_pos psiFrame m (3*m-1) t (by decide)
  dsimp only at hguard
  apply Classical.byContradiction
  intro hn
  have hn' : (m : Int) ≤ (iter t m : Int) := by omega
  have hh := Int.mul_le_mul_of_nonneg_left hn' (show 0 ≤ s.left by omega)
  change s.right + s.debt < s.left * (m : Int) at hguard
  omega

/-- The explicit guard closes the required well-founded induction step. -/
theorem psi_close_of_terminal_guard (m t : Nat) (hm : 0 < m)
    (smaller : ∀ n : Nat, 0 < n → n < m → Basin n)
    (hc : iter t (3*m-1) = 1)
    (hguard : let s := trace psiFrame m (3*m-1) t
      s.right + s.debt < s.left * (m : Int)) : Basin m := by
  exact (basin_iter t m).mp
    (smaller (iter t m) (iter_pos t m hm) (psi_terminal_descent m t hm hc hguard))

/-- The first certified member clock alone does not give the strict guard,
even on the exceptional class in PR174's OpenLemma. -/
theorem terminal_clock_counterexample :
    82 = 27*3+1 ∧ 3%4 ≠ 0 ∧ iter 16 (3*82-1) = 1 ∧
      (∀ j : Fin 16, iter j.val (3*82-1) ≠ 1) ∧ iter 16 82 = 233 ∧ 82 < 233 := by
  decide

end CollatzCrossShadow
