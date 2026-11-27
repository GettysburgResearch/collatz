import Std

/-! Finite arithmetic used in the Pólya-series test for the physical odd-gap word. -/
namespace Collatz.GapSeries

def gapSum (g : Nat → Nat) : Nat → Nat
  | 0 => 0
  | n+1 => gapSum g n + g n

def affineOffset (g : Nat → Nat) : Nat → Nat
  | 0 => 0
  | n+1 => 3 * affineOffset g n + 2 ^ gapSum g n

theorem physical_telescope (q g : Nat → Nat)
    (step : ∀ n, 2 ^ g n * q (n+1) = 3 * q n + 1) (n : Nat) :
    3 ^ n * q 0 + affineOffset g n = 2 ^ gapSum g n * q n := by
  induction n with
  | zero => simp [gapSum, affineOffset]
  | succ n ih =>
    calc
      3 ^ (n+1) * q 0 + affineOffset g (n+1) =
          3 * (3 ^ n * q 0 + affineOffset g n) + 2 ^ gapSum g n := by
            rw [affineOffset, Nat.pow_succ, Nat.mul_add]
            ac_rfl
      _ = 2 ^ gapSum g n * (3 * q n + 1) := by
        rw [ih, Nat.mul_add, Nat.mul_one]
        ac_rfl
      _ = 2 ^ gapSum g (n+1) * q (n+1) := by
        rw [← step n, gapSum, Nat.pow_add, Nat.mul_assoc]

theorem affine_slopes_ordered {c d u v : Nat}
    (h : ∀ k : Nat, c + k*u ≤ d + k*v) : u ≤ v := by
  apply Classical.byContradiction
  intro bad
  have lo := Nat.mul_le_mul_left (d+1) (show v+1 ≤ u by omega)
  have hi := h (d+1)
  simp only [Nat.mul_add, Nat.mul_one] at lo
  omega

/-- Interlaced nondecreasing affine progressions have one common slope.
    Any finite exceptional prefix can be removed before applying the result. -/
theorem slopes_synchronize {A c s : Nat → Nat} {p : Nat} (hp : 0 < p)
    (hmono : ∀ ⦃i j⦄, i ≤ j → A i ≤ A j)
    (lines : ∀ r < p, ∀ k : Nat, A (k*p+r) = c r + k*s r) :
    ∀ r < p, s r = s 0 := by
  intro r hr
  apply Nat.le_antisymm
  · apply affine_slopes_ordered (c := c r) (d := c 0 + s 0)
    intro k
    have h := hmono (show k*p+r ≤ (k+1)*p+0 by
      rw [Nat.add_mul]; omega)
    rw [lines r hr k, lines 0 hp (k+1)] at h
    simpa [Nat.add_mul, Nat.add_assoc, Nat.add_left_comm, Nat.add_comm] using h
  · apply affine_slopes_ordered (c := c 0) (d := c r)
    intro k
    have h := hmono (show k*p+0 ≤ k*p+r by omega)
    rwa [lines 0 hp k, lines r hr k] at h

theorem common_increment {A c s : Nat → Nat} {p : Nat} (hp : 0 < p)
    (hmono : ∀ ⦃i j⦄, i ≤ j → A i ≤ A j)
    (lines : ∀ r < p, ∀ k : Nat, A (k*p+r) = c r + k*s r) (n : Nat) :
    A (n+p) = A n + s 0 := by
  have hr := Nat.mod_lt n hp
  have split : n / p * p + n % p = n := by
    simpa only [Nat.mul_comm, Nat.add_comm] using Nat.mod_add_div n p
  have splitNext : (n / p + 1) * p + n % p = n + p := by
    rw [Nat.add_mul, Nat.one_mul]
    omega
  calc
    A (n+p) = c (n%p) + (n/p+1)*s (n%p) := by rw [← splitNext, lines _ hr]
    _ = c (n%p) + n/p*s (n%p) + s 0 := by
      rw [Nat.add_mul, Nat.one_mul, slopes_synchronize hp hmono lines _ hr]
      omega
    _ = A n + s 0 := by rw [← lines _ hr, split]

theorem periodic_gaps_of_affine_classes {A c s g : Nat → Nat} {p : Nat} (hp : 0 < p)
    (hmono : ∀ ⦃i j⦄, i ≤ j → A i ≤ A j) (step : ∀ n, A (n+1) = A n + g n)
    (lines : ∀ r < p, ∀ k : Nat, A (k*p+r) = c r + k*s r) :
    ∀ n, g (n+p) = g n := by
  intro n
  have h := step (n+p)
  have h₀ := common_increment hp hmono lines n
  have h₁ := common_increment hp hmono lines (n+1)
  have h₂ := step n
  rw [show n+p+1=n+1+p by omega] at h
  omega

#print axioms physical_telescope
#print axioms affine_slopes_ordered
#print axioms slopes_synchronize
#print axioms common_increment
#print axioms periodic_gaps_of_affine_classes


theorem difference_divisibility (u v g : Nat → Nat)
    (hu : ∀ n, 2 ^ g n * u (n+1) = 3 * u n + 1)
    (hv : ∀ n, 2 ^ g n * v (n+1) = 3 * v n + 1) (k : Nat) :
    2 ^ gapSum g k ∣ u 0 - v 0 := by
  have hu' := physical_telescope u g hu k
  have hv' := physical_telescope v g hv k
  have h : 3 ^ k * (u 0 - v 0) = 2 ^ gapSum g k * (u k - v k) := by
    rw [Nat.mul_sub, Nat.mul_sub]
    omega
  have cop : Nat.Coprime (2 ^ gapSum g k) (3 ^ k) :=
    Nat.pow_gcd_pow_of_gcd_eq_one (by decide : Nat.gcd 2 3 = 1)
  exact cop.dvd_of_dvd_mul_left ⟨u k - v k, h⟩

private theorem le_of_same_gaps (u v g : Nat → Nat)
    (hg : ∀ n, 1 ≤ g n) (hu : ∀ n, 2 ^ g n * u (n+1) = 3 * u n + 1)
    (hv : ∀ n, 2 ^ g n * v (n+1) = 3 * v n + 1) : u 0 ≤ v 0 := by
  apply Classical.byContradiction
  intro hn
  let k := u 0 - v 0
  have hk : 0 < k := by dsimp [k]; omega
  have hsum (n : Nat) : n ≤ gapSum g n := by
    induction n with
    | zero => exact Nat.zero_le _
    | succ n ih => rw [gapSum]; have := hg n; omega
  have hd := Nat.le_of_dvd hk (difference_divisibility u v g hu hv k)
  have hp := Nat.pow_le_pow_right Nat.zero_lt_two (hsum k)
  have hlt : k < 2 ^ k := Nat.lt_two_pow_self
  omega

theorem equal_sources_of_same_gaps (u v g : Nat → Nat)
    (hg : ∀ n, 1 ≤ g n) (hu : ∀ n, 2 ^ g n * u (n+1) = 3 * u n + 1)
    (hv : ∀ n, 2 ^ g n * v (n+1) = 3 * v n + 1) : u 0 = v 0 :=
  Nat.le_antisymm (le_of_same_gaps u v g hg hu hv) (le_of_same_gaps v u g hg hv hu)

theorem gap_period_forces_orbit_period (q g : Nat → Nat) (hg : ∀ i, 1 ≤ g i)
    (step : ∀ i, 2 ^ g i * q (i+1) = 3 * q i + 1)
    {N p : Nat} (per : ∀ t, N ≤ t → g (t+p) = g t) (n : Nat) (hn : N ≤ n) :
    q n = q (n+p) := by
  apply equal_sources_of_same_gaps (fun k => q (n+k)) (fun k => q (n+k+p))
    (fun k => g (n+k)) (fun k => hg (n+k))
  · intro k
    simpa only [Nat.add_assoc] using step (n+k)
  · intro k
    have h := step (n+k+p)
    rw [per (n+k) (by omega)] at h
    rwa [show n+k+p+1=n+(k+1)+p by omega] at h

#print axioms difference_divisibility
#print axioms equal_sources_of_same_gaps
#print axioms gap_period_forces_orbit_period

end Collatz.GapSeries
