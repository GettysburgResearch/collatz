import Mathlib.Tactic

/-! Finite algebra and order kernels for physical residue-defect filters. -/
namespace Collatz.CycleDefectFilters

set_option autoImplicit false

/-- A positive literal gap on a nonwrapping residue step forces this inequality. -/
theorem noWrapDown (a k k' : ℤ) (h : a + k = 1 + k') (ha : 0 < a) : k ≤ k' := by
  omega

/-- A supported interval cannot enter the upper part of the residue circle. -/
theorem intervalEnd (s u v : ℕ) (hu : 0 < u) (huv : u < v)
    (closed : ∀ r, u ≤ r → r < v → s ≤ r → u ≤ r-s) (hs : 0 < s) : v ≤ s := by
  by_contra! h
  by_cases hus : u ≤ s
  · have := closed s hus h (by omega)
    omega
  · have := closed u (by omega) huv (by omega)
    omega

/-- If a finite parity progression contains a high point, it starts at residue one. -/
theorem highStrideTwo (u m s j : ℕ) (hu : 0 < u) (hs : 0 < s)
    (hhi : s ≤ u + 2*j) (hj : j < m)
    (closed : ∀ i < m, s ≤ u + 2*i → ∃ k < m, u+2*i-s=u+2*k) : u=1 := by
  obtain ⟨k, _, hk⟩ := closed j hj hhi
  have hsj : s ≤ 2*j := by omega
  have he : s = 2*(j-k) := by omega
  have hm : j-k < m := by omega
  have hlow : u < s := by
    by_contra! hh
    obtain ⟨d, _, hd⟩ := closed 0 (by omega) (by omega)
    omega
  by_contra! h
  have hstep : 0 < j-k := by omega
  have hh : s ≤ u + 2*(j-k-1) := by omega
  obtain ⟨d, _, hd⟩ := closed (j-k-1) (by omega) hh
  omega

variable {R : Type*} [CommRing R]

def geom (x : R) : ℕ → R
  | 0 => 0
  | n+1 => geom x n + x^n

theorem geomStep (x : R) (n : ℕ) : (x-1)*geom x n = x^n-1 := by
  induction n with
  | zero => simp [geom]
  | succ n ih => simp only [geom, mul_add, ih, pow_succ]; ring

/-- Sparse boundary filter for equally spaced blocks, of arbitrary count. -/
theorem repeatedIntervalFilter (x : R) (p u w t m : ℕ) (hp : x^p=2) :
    (1-x^t)*(x-1)*(geom x p+x^u*geom x w*geom (x^t) m) =
       (1-x^t)+x^u*(x^w-1)*(1-x^(t*m)) := by
  have h0 : (x-1)*geom x p=1 := by rw [geomStep, hp]; ring
  have ht : (1-x^t)*geom (x^t) m = 1-x^(t*m) := by
    rw [pow_mul]
    linear_combination -(geomStep (x^t) m)
  calc
    _ = (1-x^t)*((x-1)*geom x p) + x^u*((x-1)*geom x w)*((1-x^t)*geom (x^t) m) := by ring
    _ = _ := by rw [h0, geomStep, ht]; ring

/-- The four-term filter for the full stride-two family. -/
theorem strideTwoFilter (x : R) (p u m : ℕ) (hp : x^p=2) :
    (x^2-1)*(geom x p+x^u*geom (x^2) m)=1+x+x^(u+2*m)-x^u := by
  have h0 : (x-1)*geom x p=1 := by rw [geomStep, hp]; ring
  have ht := geomStep (x^2) m
  rw [pow_add, pow_mul]
  calc
    _ = (x+1)*((x-1)*geom x p)+x^u*((x^2-1)*geom (x^2) m) := by ring
    _ = _ := by rw [h0, ht]; ring

/-- Entire dyadic range for the fixed exponential floor, by induction on bit length. -/
theorem dyadicMargin (n : ℕ) : 42000*(20+n+2) < 2^(20+n) := by
  induction n with
  | zero => decide
  | succ n ih =>
    rw [show 20+(n+1)=(20+n)+1 by omega, pow_succ]
    omega

#print axioms noWrapDown
#print axioms intervalEnd
#print axioms highStrideTwo
#print axioms repeatedIntervalFilter
#print axioms strideTwoFilter
#print axioms dyadicMargin
end Collatz.CycleDefectFilters
