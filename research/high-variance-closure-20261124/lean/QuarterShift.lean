import Std

/-! Exact ordinary shortcut identity and its finite product along arbitrary paths.
The statements use natural numbers with denominators cleared. -/

namespace QuarterShift

def step (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

theorem balanced_step (n : Nat) :
    4 * step n + 1 = 3 ^ (n % 2) * (2 * n + 1) := by
  by_cases he : n % 2 = 0
  · simp [step, he]
    omega
  · have ho : n % 2 = 1 := by omega
    simp [step, ho]
    omega

def endpoint : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => endpoint k (step n)

def oddCount : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, n => n % 2 + oddCount k (step n)

def pathProduct (f : Nat → Nat) : Nat → Nat → Nat
  | 0, _ => 1
  | k+1, n => f n * pathProduct f k (step n)

/-- Multiplying the step identities, with every factor positive even at zero. -/
theorem balanced_path (k n : Nat) :
    (4 * endpoint k n + 1) * pathProduct (fun m => 4*m+1) k n =
    (4*n+1) * 3 ^ oddCount k n * pathProduct (fun m => 2*m+1) k n := by
  induction k generalizing n with
  | zero => simp [endpoint, oddCount, pathProduct]
  | succ k ih =>
    simp only [endpoint, oddCount, pathProduct, Nat.pow_add]
    calc
      _ = (4*n+1) * ((4 * endpoint k (step n) + 1) *
          pathProduct (fun m => 4*m+1) k (step n)) := by ac_rfl
      _ = _ := by rw [ih (step n), balanced_step n]; ac_rfl

/-- An arbitrary ordinary all-odd prefix, including the exact physical endpoint. -/
theorem odd_run (k x d : Nat) (hx : x+1 = 2^k * d) :
    endpoint k x + 1 = 3^k * d ∧ oddCount k x = k := by
  induction k generalizing x d with
  | zero => simpa [endpoint, oddCount] using hx
  | succ k ih =>
    have hx2 : x+1 = 2 * (2^k * d) := by
      rw [hx, Nat.pow_succ]; ac_rfl
    have hp : x % 2 = 1 := by omega
    have hstep : 2 * (step x + 1) = 3 * (x+1) := by
      simp [step, hp]; omega
    have hs : step x + 1 = 2^k * (3 * d) := by
      calc
        _ = 3 * (2^k * d) := by omega
        _ = _ := by ac_rfl
    obtain ⟨hy, hc⟩ := ih (step x) (3*d) hs
    constructor
    · simp only [endpoint, hy, Nat.pow_succ]; ac_rfl
    · simp [oddCount, hp, hc, Nat.add_comm]

/-- Every even ray is inside the predecessor basin of its original vertex. -/
theorem even_run (k m : Nat) :
    endpoint k (2^k * m) = m ∧ oddCount k (2^k * m) = 0 := by
  induction k with
  | zero => simp [endpoint, oddCount]
  | succ k ih =>
    have hh : 2^(k+1) * m = 2 * (2^k * m) := by rw [Nat.pow_succ]; ac_rfl
    have he : step (2 * (2^k * m)) = 2^k * m := by simp [step]
    simpa [endpoint, oddCount, hh, he] using ih

/-- Finite ordinary base for the numerical threshold at B=20. -/
theorem below_twenty :
    ∀ n : Fin 20, 0 < n.val → ∃ j : Fin 32, endpoint j.val n.val = 1 := by
  decide

#print axioms balanced_step
#print axioms balanced_path
#print axioms odd_run
#print axioms even_run
#print axioms below_twenty

end QuarterShift
