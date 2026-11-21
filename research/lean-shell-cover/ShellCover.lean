import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace CollatzShell

def step (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3*n+1)/2

def orbit : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => orbit k (step n)

def Basin (n : Nat) : Prop := ∃ k, orbit k n = 1

def Universal : Prop := ∀ n : Nat, 0 < n → Basin n

theorem orbit_add (i j n : Nat) : orbit (i+j) n = orbit j (orbit i n) := by
  induction i generalizing n with
  | zero => simp [orbit]
  | succ i ih => simpa [Nat.succ_add, orbit] using ih (step n)

theorem step_double (n : Nat) : step (2*n) = n := by simp [step]

theorem orbit_pad (b n : Nat) : orbit b (2^b*n) = n := by
  induction b with
  | zero => simp [orbit]
  | succ b ih =>
    rw [show 2^(b+1)*n = 2*(2^b*n) by ring]
    simpa [orbit, step_double] using ih

/-- The residue modulo nine selects an exact four-clock inverse with unit output. -/
def inv4 (q : Nat) : Nat :=
  48*(q/9) + (match q % 9 with
    | 1 => 4 | 2 => 8 | 4 => 20 | 5 => 26 | 7 => 37 | _ => 40)

private theorem step_even {x y : Nat} (h : x=2*y) : step x = y := h ▸ step_double y

private theorem step_odd {x y : Nat} (ho : x%2=1) (h : 3*x+1=2*y) : step x = y := by
  simp [step, show x%2 ≠ 0 by omega, h]

private theorem affine_four (t : Nat) :
    orbit 4 (48*t+4) = 9*t+1 ∧
    orbit 4 (48*t+8) = 9*t+2 ∧
    orbit 4 (48*t+20) = 9*t+4 ∧
    orbit 4 (48*t+26) = 9*t+5 ∧
    orbit 4 (48*t+37) = 9*t+7 ∧
    orbit 4 (48*t+40) = 9*t+8 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · simp only [orbit]
    rw [show step (48*t+4) = 24*t+2 from step_even (by omega)]
    rw [show step (24*t+2) = 12*t+1 from step_even (by omega)]
    rw [show step (12*t+1) = 18*t+2 from step_odd (by omega) (by omega)]
    rw [show step (18*t+2) = 9*t+1 from step_even (by omega)]
  · simp only [orbit]
    rw [show step (48*t+8) = 24*t+4 from step_even (by omega)]
    rw [show step (24*t+4) = 12*t+2 from step_even (by omega)]
    rw [show step (12*t+2) = 6*t+1 from step_even (by omega)]
    rw [show step (6*t+1) = 9*t+2 from step_odd (by omega) (by omega)]
  · simp only [orbit]
    rw [show step (48*t+20) = 24*t+10 from step_even (by omega)]
    rw [show step (24*t+10) = 12*t+5 from step_even (by omega)]
    rw [show step (12*t+5) = 18*t+8 from step_odd (by omega) (by omega)]
    rw [show step (18*t+8) = 9*t+4 from step_even (by omega)]
  · simp only [orbit]
    rw [show step (48*t+26) = 24*t+13 from step_even (by omega)]
    rw [show step (24*t+13) = 36*t+20 from step_odd (by omega) (by omega)]
    rw [show step (36*t+20) = 18*t+10 from step_even (by omega)]
    rw [show step (18*t+10) = 9*t+5 from step_even (by omega)]
  · simp only [orbit]
    rw [show step (48*t+37) = 72*t+56 from step_odd (by omega) (by omega)]
    rw [show step (72*t+56) = 36*t+28 from step_even (by omega)]
    rw [show step (36*t+28) = 18*t+14 from step_even (by omega)]
    rw [show step (18*t+14) = 9*t+7 from step_even (by omega)]
  · simp only [orbit]
    rw [show step (48*t+40) = 24*t+20 from step_even (by omega)]
    rw [show step (24*t+20) = 12*t+10 from step_even (by omega)]
    rw [show step (12*t+10) = 6*t+5 from step_even (by omega)]
    rw [show step (6*t+5) = 9*t+8 from step_odd (by omega) (by omega)]

theorem inv4_spec (q : Nat) (hu : q % 3 ≠ 0) :
    orbit 4 (inv4 q) = q ∧ inv4 q % 3 ≠ 0 ∧
    16*q ≤ 3*inv4 q + 8 ∧ 3*inv4 q ≤ 16*q := by
  obtain ⟨h1,h2,h4,h5,h7,h8⟩ := affine_four (q/9)
  have choices : q%9=1 ∨ q%9=2 ∨ q%9=4 ∨ q%9=5 ∨ q%9=7 ∨ q%9=8 := by omega
  rcases choices with e|e|e|e|e|e <;> simp only [inv4, e] <;> omega

def lift : Nat → Nat → Nat
  | 0, q => q
  | p+1, q => inv4 (lift p q)

theorem lift_spec (p q : Nat) (hu : q%3 ≠ 0) :
    orbit (4*p) (lift p q) = q ∧ lift p q % 3 ≠ 0 ∧
    16^p*q + 3^p ≤ 3^p*lift p q + 16^p ∧ 3^p*lift p q ≤ 16^p*q := by
  induction p with
  | zero => simp [lift, orbit, hu]
  | succ p ih =>
    obtain ⟨hit, unit, lower, upper⟩ := ih
    obtain ⟨hit', unit', lower', upper'⟩ := inv4_spec (lift p q) unit
    refine ⟨?_, unit', ?_, ?_⟩
    · rw [show 4*(p+1)=4+4*p by omega, orbit_add]
      exact hit' ▸ hit
    · simp only [lift, pow_succ]
      have h₁ := Nat.mul_le_mul_left (3^p) lower'
      have h₂ := Nat.mul_le_mul_left 16 lower
      ring_nf at h₁ h₂ ⊢
      omega
    · simp only [lift, pow_succ]
      nlinarith [Nat.mul_le_mul_left (3^p) upper', Nat.mul_le_mul_left 16 upper]
end CollatzShell
