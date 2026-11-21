import Collatz.Closure174

/-!
Exact ordinary-source lifting. Every variable below ranges over natural integers;
the conclusions are equalities of actual finite shortcut orbits. No Haar-almost-
everywhere statement or completed binary source is used.
-/

open CollatzReverseBasin CollatzClosure

namespace CollatzGlobal

/-- Exactly `t` positive-shortcut steps, with the usual extension at zero. -/
def orbit (n : Nat) : Nat → Nat
  | 0 => n
  | t+1 => orbit (shortcut n) t

/-- Number of odd inputs among those `t` steps. -/
def oddCount (n : Nat) : Nat → Nat
  | 0 => 0
  | t+1 => n % 2 + oddCount (shortcut n) t

theorem orbit_basin (n t : Nat) : Basin (orbit n t) ↔ Basin n := by
  induction t generalizing n with
  | zero => exact Iff.rfl
  | succ t ih => exact (ih (shortcut n)).trans (basin_step n)

theorem orbit_add (n s t : Nat) : orbit n (s+t) = orbit (orbit n s) t := by
  induction s generalizing n with
  | zero => simp [orbit]
  | succ s ih => simpa [orbit, Nat.succ_add] using ih (shortcut n)

theorem shortcut_add_even (n q : Nat) :
    shortcut (n+2*q) = shortcut n + (if n%2=0 then q else 3*q) := by
  unfold shortcut
  split <;> split <;> omega

/-- Every binary cylinder has the exact affine forward image, and the odd count
is unchanged throughout the whole cylinder. -/
theorem high_bit_lift (n t q : Nat) :
    orbit (n + 2^t*q) t = orbit n t + 3^(oddCount n t)*q ∧
    oddCount (n + 2^t*q) t = oddCount n t := by
  induction t generalizing n q with
  | zero => simp [orbit, oddCount]
  | succ t ih =>
    have pow2 : 2^(t+1)*q = 2*(2^t*q) := by grind
    have par : (n + 2^(t+1)*q)%2 = n%2 := by rw [pow2]; omega
    have step := shortcut_add_even n (2^t*q)
    rw [← pow2] at step
    rcases Nat.mod_two_eq_zero_or_one n with he | ho
    · have e : shortcut (n+2^(t+1)*q) = shortcut n + 2^t*q := by simpa [he] using step
      have h := ih (shortcut n) q
      simpa [orbit, oddCount, par, he, e] using h
    · have e : shortcut (n+2^(t+1)*q) = shortcut n + 2^t*(3*q) := by
        calc shortcut (n+2^(t+1)*q) = shortcut n + 3*(2^t*q) := by simpa [ho] using step
             _ = _ := by grind
      have h := ih (shortcut n) (3*q)
      constructor
      · simp only [orbit, e]
        rw [h.1]
        simp only [oddCount, ho]
        congr 1
        rw [Nat.pow_add]
        simp
        grind
      · simpa [oddCount, par, ho, e] using h.2

/-- A complete finite source certificate is transferred to the exact affine
endpoint, for every ordinary member of its binary cylinder. -/
theorem basin_high_bit_lift (n t q : Nat) :
    Basin (n+2^t*q) ↔ Basin (orbit n t + 3^(oddCount n t)*q) := by
  have h := orbit_basin (n+2^t*q) t
  rw [(high_bit_lift n t q).1] at h
  exact h.symm

/-- A balanced root return has matching odd counts and an exact ratio-five
endpoint. Both requirements concern the supplied finite ordinary paths. -/
def BalancedFive (n t : Nat) : Prop :=
  oddCount (5*n) t = oddCount n t ∧ orbit (5*n) t = 5*orbit n t

/-- A balanced return propagates through every ordinary member of its cylinder. -/
theorem balanced_five_lift {n t : Nat} (h : BalancedFive n t) (q : Nat) :
    BalancedFive (n+2^t*q) t := by
  have e : 5*(n+2^t*q) = 5*n+2^t*(5*q) := by grind
  obtain ⟨a,b⟩ := h
  constructor
  · rw [e, (high_bit_lift (5*n) t (5*q)).2, (high_bit_lift n t q).2]
    exact a
  · rw [e, (high_bit_lift (5*n) t (5*q)).1, (high_bit_lift n t q).1, a, b]
    grind

/-- Actual five-comparison failure at an ordinary input. -/
def FiveFailure (n : Nat) : Prop := Basin n ∧ ¬ Basin (5*n)

/-- Exact preservation of the actual failure label across every balanced return.
This theorem supplies no assertion that an arbitrary input has such a return. -/
theorem five_failure_return {n t : Nat} (h : BalancedFive n t) :
    FiveFailure n ↔ FiveFailure (orbit n t) := by
  unfold FiveFailure
  rw [← orbit_basin n t, ← orbit_basin (5*n) t, h.2]

theorem five_failure_cylinder {n t : Nat} (h : BalancedFive n t) (q : Nat) :
    FiveFailure (n+2^t*q) ↔ FiveFailure (orbit n t + 3^(oddCount n t)*q) := by
  have r := five_failure_return (balanced_five_lift h q)
  rwa [(high_bit_lift n t q).1] at r

end CollatzGlobal
