import TernaryItinerary

/-! Infinite families of actual mergers for the least-smooth-base frontier.
All clocks use the repository's accelerated-by-one-bit step. -/

namespace Collatz.TensorBridge

open Collatz.Itinerary

/-- The positive sibling 64n+21 of any odd n meets n after six extra
shortcut steps. The endpoint need not itself be odd. -/
theorem three_sibling_meeting (n : Nat) (hn : n % 2 = 1) :
    run 7 (64*n+21) = run 1 n := by
  have h0 : step (64*n+21) = 32*(3*n+1) := by simp only [step]; split <;> omega
  have half (x : Nat) : step (2*x) = x := by simp [step]
  have h1 : step (32*(3*n+1)) = 16*(3*n+1) := by
    simpa only [← Nat.mul_assoc] using half (16*(3*n+1))
  have h2 : step (16*(3*n+1)) = 8*(3*n+1) := by
    simpa only [← Nat.mul_assoc] using half (8*(3*n+1))
  have h3 : step (8*(3*n+1)) = 4*(3*n+1) := by
    simpa only [← Nat.mul_assoc] using half (4*(3*n+1))
  have h4 : step (4*(3*n+1)) = 2*(3*n+1) := by
    simpa only [← Nat.mul_assoc] using half (2*(3*n+1))
  have h5 : step (2*(3*n+1)) = 3*n+1 := half _
  have h6 : step (3*n+1) = step n := by simp only [step]; split <;> split <;> omega
  simp only [run, h0, h1, h2, h3, h4, h5, h6]

/-- Every odd base 29 mod 81 has a genuine lower-base merger in the r=1
tower row. The comparison uses different clocks on the two sources. -/
theorem first_row_lower_base (t : Nat) :
    let w := 162*t+29
    let b := 128*t+23
    0 < b ∧ b < w ∧ run 7 (3^5*b) = run 1 (3*w) := by
  dsimp
  refine ⟨by omega, by omega, ?_⟩
  have h := three_sibling_meeting (3*(162*t+29)) (by omega)
  rw [show 243*(128*t+23) = 64*(3*(162*t+29))+21 by omega]
  exact h

/-- The low-clock guard of PR #192 survives on this entire infinite
subprogression. The rank-two mod-512 guard has a false premise at r=1. -/
theorem first_row_frontier_survivors (s : Nat) :
    let w := 324*s+191
    let a := 486*s+287
    let b := 256*s+151
    0 < w ∧ w%2=1 ∧ w%3≠0 ∧ 0 < a ∧ a%2=1 ∧ 3*w+1=2*a ∧
      0 < b ∧ b < w ∧ run 1 (3*w) = run 7 (3^5*b) := by
  dsimp
  have hm := first_row_lower_base (2*s+1)
  dsimp at hm
  have hw : 162*(2*s+1)+29 = 324*s+191 := by omega
  have hb : 128*(2*s+1)+23 = 256*s+151 := by omega
  rw [hw, hb] at hm
  exact ⟨by omega, by omega, by omega, by omega, by omega, by omega, hm.1, hm.2.1, hm.2.2.symm⟩

end Collatz.TensorBridge
