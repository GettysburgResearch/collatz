import Std

namespace Collatz.OctaveProfiles

/-- Sum of the first k cumulative clocks. On an ordered one-octave family,
this integer separates distinct clock profiles. -/
def mass (u : Nat → Nat) : Nat → Nat
  | 0 => 0
  | k + 1 => mass u k + u k

theorem mass_mono (u v : Nat → Nat) (k : Nat)
    (h : ∀ i < k, u i ≤ v i) : mass u k ≤ mass v k := by
  induction k with
  | zero => simp [mass]
  | succ k ih =>
    have h₁ := ih (fun i hi => h i (by omega))
    have h₂ := h k (by omega)
    simp only [mass]
    omega

theorem mass_strict (u v : Nat → Nat) (k : Nat)
    (h : ∀ i < k, u i ≤ v i) (different : ∃ i < k, u i < v i) :
    mass u k < mass v k := by
  induction k with
  | zero => obtain ⟨i,hi,_⟩ := different; omega
  | succ k ih =>
    have h₁ := mass_mono u v k (fun i hi => h i (by omega))
    have h₂ := h k (by omega)
    obtain ⟨i,hi,hu⟩ := different
    simp only [mass]
    by_cases e : i = k
    · subst i; omega
    · have hb := ih (fun j hj => h j (by omega)) ⟨i,by omega,hu⟩
      omega

theorem mass_span (u v : Nat → Nat) (k : Nat)
    (h : ∀ i < k, v i ≤ u i + 1) : mass v k ≤ mass u k + k := by
  induction k with
  | zero => simp [mass]
  | succ k ih =>
    have h₁ := ih (fun i hi => h i (by omega))
    have h₂ := h k (by omega)
    simp only [mass]
    omega

/-- If n+1 distinct ordered profiles occupy a unit-width range in each
of k clock coordinates, there are at most k+1 profiles. -/
theorem profile_count (x : Nat → Nat → Nat) (n k : Nat)
    (ordered : ∀ j < n, ∀ i < k, x j i ≤ x (j+1) i)
    (different : ∀ j < n, ∃ i < k, x j i < x (j+1) i)
    (span : ∀ i < k, x n i ≤ x 0 i + 1) : n ≤ k := by
  have steps : ∀ j ≤ n, mass (x 0) k + j ≤ mass (x j) k := by
    intro j hj
    induction j with
    | zero => simp
    | succ j ih =>
      have prev := ih (by omega)
      have next := mass_strict _ _ k (ordered j (by omega)) (different j (by omega))
      omega
  have lower := steps n (by omega)
  have upper := mass_span _ _ k span
  omega

/-- Common affine carry and odd endpoints force the complete odd-source
cylinder spacing, including the additional terminal parity bit. -/
theorem odd_cylinder (k B x y u v carry : Nat) (hxy : x ≤ y)
    (hx : 3^k * x + carry = 2^B * (2*u+1))
    (hy : 3^k * y + carry = 2^B * (2*v+1)) : 2^(B+1) ∣ y-x := by
  have h₁ := Nat.mul_le_mul_left (3^k) hxy
  have huv : u ≤ v := by
    apply Classical.byContradiction
    intro hr
    have hvu : 2*v+1 < 2*u+1 := by omega
    have ht := Nat.mul_lt_mul_of_pos_left hvu (by exact Nat.two_pow_pos B)
    omega
  have identity : 3^k * (y-x) = 2^(B+1)*(v-u) := by
    rw [Nat.mul_sub, Nat.mul_sub, Nat.pow_succ]
    simp only [Nat.mul_add, Nat.mul_one, ← Nat.mul_assoc] at hx hy
    omega
  have hd : 2^(B+1) ∣ 3^k * (y-x) := ⟨v-u,identity⟩
  have hc : Nat.Coprime (2^(B+1)) (3^k) :=
    ((by decide : Nat.Coprime 2 3).pow_left (B+1)).pow_right k
  exact hc.dvd_of_dvd_mul_left hd

/-- A once-forced cyclic integer gap has the entire binomial denominator
when the forcing coefficient is a unit modulo that binomial. -/
theorem unit_forcing (D d gap unit : Nat) (hd : d ∣ D)
    (h : D*gap=d*unit) (hc : Nat.Coprime D unit) : d=D := by
  have dd : D ∣ d*unit := ⟨gap,h.symm⟩
  exact Nat.dvd_antisymm hd (hc.dvd_of_dvd_mul_right dd)

/-- Compare two dyadic lifts using their common scale as the unit. An
inversion of their images yields the narrow physical crossing interval. -/
theorem crossing_iff (r u v : Nat) (h : r*u < v) :
    3*v+1 < r*(3*u+1) ↔ 3*(v-r*u) < r-1 := by
  have he : r*(3*u+1) = 3*(r*u)+r := by
    rw [Nat.mul_add, Nat.mul_one, Nat.mul_left_comm]
  rw [he, Nat.mul_sub]
  have hle : 3*(r*u) ≤ 3*v := Nat.mul_le_mul_left 3 (Nat.le_of_lt h)
  omega

theorem crossing_requires_three_levels (s u v : Nat) (h : 2^s*u < v)
    (crossing : 3*v+1 < 2^s*(3*u+1)) : 3 ≤ s := by
  have hgap := (crossing_iff (2^s) u v h).mp crossing
  have hp : 1 ≤ v-2^s*u := by omega
  by_cases hs : 3 ≤ s
  · exact hs
  · have cases_s : s=0 ∨ s=1 ∨ s=2 := by omega
    rcases cases_s with hs | hs | hs <;> subst s <;> simp at hgap hp <;> omega

/-- The backward odd-predecessor branch gives the opposite-sided triadic
crossing interval. The earlier predecessor parity is e. -/
theorem triadic_crossing_iff (r u v e : Nat) (hu : 0 < u) (hv : 0 < v)
    (he : e ≤ 1) (h : u < r*v) :
    r*(2*v-1) < 2*u-e ↔ 2*(r*v-u) < r-e := by
  rw [Nat.mul_sub, Nat.mul_one, Nat.mul_left_comm, Nat.mul_sub]
  have huv : 2*u ≤ 2*(r*v) := Nat.mul_le_mul_left 2 (by omega)
  have hrv : r ≤ r*v := by
    have hh := Nat.mul_le_mul_left r (by omega : 1 ≤ v)
    simpa using hh
  omega

#print axioms triadic_crossing_iff
#print axioms crossing_iff
#print axioms crossing_requires_three_levels
#print axioms profile_count
#print axioms odd_cylinder
#print axioms unit_forcing
end Collatz.OctaveProfiles
