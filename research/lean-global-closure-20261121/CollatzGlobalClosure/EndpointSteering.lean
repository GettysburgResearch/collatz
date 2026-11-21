import Mathlib.Tactic

/-!
Exact arithmetic for adaptive endpoint steering.

This file proves ordinary integer identities for every finite shortcut Collatz
word.  It does not assert that a suitable word or endpoint exponent always
exists.  In particular, exposing more binary digits increases, rather than
removes, the ternary precision in a prescribed-endpoint condition.
-/

namespace CollatzEndpointSteering

def step (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3*n+1)/2

def orbit : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => orbit k (step n)

def odds : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, n => odds k (step n) + n % 2

theorem step_shift (a n : Nat) :
    step (2*a+n) = 3^(n%2)*a + step n := by
  by_cases he : n%2=0
  · simp [step, he, show (2*a+n)%2=0 by omega]
    omega
  · have ho : n%2=1 := by omega
    simp [step, ho]
    omega

theorem orbit_shift (k n t : Nat) :
    orbit k (2^k*t+n) = 3^(odds k n)*t + orbit k n := by
  induction k generalizing n t with
  | zero => simp [orbit, odds]
  | succ k ih =>
    rw [show 2^(k+1)*t+n = 2*(2^k*t)+n by ring]
    simp only [orbit, odds, step_shift, pow_add]
    rw [show 3^(n%2)*(2^k*t)+step n = 2^k*(3^(n%2)*t)+step n by ring, ih]
    ring

theorem odds_shift (k n t : Nat) : odds k (2^k*t+n) = odds k n := by
  induction k generalizing n t with
  | zero => rfl
  | succ k ih =>
    rw [show 2^(k+1)*t+n = 2*(2^k*t)+n by ring]
    simp only [odds, step_shift]
    rw [show 3^(n%2)*(2^k*t)+step n = 2^k*(3^(n%2)*t)+step n by ring, ih]
    congr 1
    omega

/-- Every binary lift of a supplied word is an actual ordinary trajectory.
The endpoint stride has exactly the old ternary exponent plus the new odd count. -/
theorem ternary_precision (p k n t : Nat) :
    orbit k (n+2^k*3^p*t) = orbit k n + 3^(p+odds k n)*t := by
  rw [show n+2^k*3^p*t = 2^k*(3^p*t)+n by ring, orbit_shift]
  ring

/-- A target lies on this legal endpoint ray exactly when it is above its
base endpoint and satisfies the full remaining ternary congruence. -/
theorem target_on_ray_iff (p k n y : Nat) :
    (∃ t : Nat, orbit k (n+2^k*3^p*t)=y) ↔
      orbit k n ≤ y ∧ 3^(p+odds k n) ∣ y-orbit k n := by
  constructor
  · rintro ⟨t, hit⟩
    rw [ternary_precision] at hit
    constructor
    · omega
    · refine ⟨t, ?_⟩
      omega
  · rintro ⟨hle, t, ht⟩
    refine ⟨t, ?_⟩
    rw [ternary_precision]
    omega

/-- The remaining integer is a real source on the prescribed binary ray;
no modular point is substituted for an ordinary integer. Positivity follows
from a positive base source, as in `construct_positive_source` below. -/
theorem construct_source (p k n y : Nat)
    (hle : orbit k n ≤ y)
    (hdiv : 3^(p+odds k n) ∣ y-orbit k n) :
    orbit k (n+2^k*3^p*((y-orbit k n)/3^(p+odds k n)))=y := by
  rw [ternary_precision, Nat.mul_div_cancel' hdiv]
  omega

theorem construct_positive_source (p k n y : Nat) (hn : 0<n)
    (hle : orbit k n ≤ y)
    (hdiv : 3^(p+odds k n) ∣ y-orbit k n) :
    0<n+2^k*3^p*((y-orbit k n)/3^(p+odds k n)) ∧
    orbit k (n+2^k*3^p*((y-orbit k n)/3^(p+odds k n)))=y := by
  exact ⟨by omega, construct_source p k n y hle hdiv⟩

/-- Adding any further actual suffix retains all old ternary constraints.
This is the exact obligation a proposed adaptive selector must solve. -/
theorem prescribed_endpoint_iff (p k n b q : Nat) :
    (∃ t : Nat, orbit k (n+2^k*3^p*t)=2^b*q) ↔
      orbit k n ≤ 2^b*q ∧ 3^(p+odds k n) ∣ 2^b*q-orbit k n :=
  target_on_ray_iff p k n (2^b*q)

end CollatzEndpointSteering

#print axioms CollatzEndpointSteering.step_shift
#print axioms CollatzEndpointSteering.orbit_shift
#print axioms CollatzEndpointSteering.odds_shift
#print axioms CollatzEndpointSteering.ternary_precision
#print axioms CollatzEndpointSteering.target_on_ray_iff
#print axioms CollatzEndpointSteering.construct_source
#print axioms CollatzEndpointSteering.construct_positive_source
#print axioms CollatzEndpointSteering.prescribed_endpoint_iff
