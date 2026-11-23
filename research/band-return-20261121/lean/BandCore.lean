/-!
Compatibility extraction of exact ordinary-orbit arithmetic from the repository's
checkpoint2 core development. Only the orbit/count definitions, concatenation,
even-shift identity, high-bit lift, and affine lower bound are copied here.

Original OrbitLift.lean SHA256:
7e878efd729252de6ca0aa983f1fe0fea85cf775bc9973ef823aeafdf7edba42
Original Expansion.lean SHA256:
e7fd9f2e1ac82e068a184df59228436671927116aec437673da469ac17b5b46e

Adaptation: namespace becomes CollatzBandCore; `shortcut` is named `step`.
The transitive PR146 notation/ring/strong-induction compatibility shim is not
imported, because its global names collide with Mathlib. No proof assumption
is substituted for an omitted dependency.
-/

namespace CollatzBandCore

def step (n : Nat) : Nat := if n%2=0 then n/2 else (3*n+1)/2

/-- Exactly `t` positive-step steps, with the usual extension at zero. -/
def orbit (n : Nat) : Nat → Nat
  | 0 => n
  | t+1 => orbit (step n) t

/-- Number of odd inputs among those `t` steps. -/
def oddCount (n : Nat) : Nat → Nat
  | 0 => 0
  | t+1 => n % 2 + oddCount (step n) t

theorem orbit_add (n s t : Nat) : orbit n (s+t) = orbit (orbit n s) t := by
  induction s generalizing n with
  | zero => simp [orbit]
  | succ s ih => simpa [orbit, Nat.succ_add] using ih (step n)

theorem step_add_even (n q : Nat) :
    step (n+2*q) = step n + (if n%2=0 then q else 3*q) := by
  unfold step
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
    have shifted := step_add_even n (2^t*q)
    rw [← pow2] at shifted
    rcases Nat.mod_two_eq_zero_or_one n with he | ho
    · have e : step (n+2^(t+1)*q) = step n + 2^t*q := by simpa [he] using shifted
      have h := ih (step n) q
      simpa [orbit, oddCount, par, he, e] using h
    · have e : step (n+2^(t+1)*q) = step n + 2^t*(3*q) := by
        calc step (n+2^(t+1)*q) = step n + 3*(2^t*q) := by simpa [ho] using shifted
             _ = _ := by grind
      have h := ih (step n) (3*q)
      constructor
      · simp only [orbit, e]
        rw [h.1]
        simp only [oddCount, ho]
        congr 1
        rw [Nat.pow_add]
        simp
        grind
      · simpa [oddCount, par, ho, e] using h.2

/-- The positive corrections in an actual step word cannot lower its
linear contribution. -/
theorem orbit_linear_lower (n t : Nat) :
    3^(oddCount n t)*n ≤ 2^t*orbit n t := by
  induction t generalizing n with
  | zero => simp [orbit, oddCount]
  | succ t ih =>
    have h := ih (step n)
    rcases Nat.mod_two_eq_zero_or_one n with he | ho
    · have hn : n=2*step n := by unfold step; split <;> omega
      simp only [orbit, oddCount, he, Nat.zero_add]
      have hm := Nat.mul_le_mul_left 2 h
      calc
        3^(oddCount (step n) t)*n = 3^(oddCount (step n) t)*(2*step n) :=
          congrArg (fun z => 3^(oddCount (step n) t)*z) hn
        _ = 2*(3^(oddCount (step n) t)*step n) := by grind
        _ ≤ 2*(2^t*orbit (step n) t) := hm
        _ = 2^(t+1)*orbit (step n) t := by grind
    · have hs : 3*n≤2*step n := by unfold step; split <;> omega
      have h1 := Nat.mul_le_mul_left (3^(oddCount (step n) t)) hs
      have h2 := Nat.mul_le_mul_left 2 h
      simp only [orbit, oddCount, ho]
      calc
        3^(1+oddCount (step n) t)*n = 3^(oddCount (step n) t)*(3*n) := by
          rw [Nat.pow_add]
          simp
          grind
        _ ≤ 3^(oddCount (step n) t)*(2*step n) := h1
        _ = 2*(3^(oddCount (step n) t)*step n) := by grind
        _ ≤ 2*(2^t*orbit (step n) t) := h2
        _ = 2^(t+1)*orbit (step n) t := by grind

end CollatzBandCore
