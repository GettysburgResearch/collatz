import Mathlib.Tactic.Ring

namespace LocalDenominator

section Shift

variable {R : Type*} [CommRing R]

private def geom (x : R) : ℕ → R
  | 0 => 0
  | n + 1 => x ^ n + geom x n

private theorem geom_mul (x : R) (n : ℕ) : geom x n * (x - 1) = x ^ n - 1 := by
  induction n with
  | zero => simp [geom]
  | succ n ih =>
    rw [geom, add_mul, ih, pow_succ]
    ring

/-- Use x=S^v and y=S^w on a doubled rank lattice with av+bw=p. -/
theorem seam_coprime (x y : R) (a b : ℕ) (seam : x ^ a * y ^ b = 2) :
    ∃ u v : R, u * (x - 1) + v * (y - 1) = 1 := by
  refine ⟨geom x a * y ^ b, geom y b, ?_⟩
  calc
    geom x a * y ^ b * (x - 1) + geom y b * (y - 1) =
        (geom x a * (x - 1)) * y ^ b + geom y b * (y - 1) := by ring
    _ = (x ^ a - 1) * y ^ b + (y ^ b - 1) := by rw [geom_mul, geom_mul]
    _ = x ^ a * y ^ b - 1 := by ring
    _ = 1 := by rw [seam]; ring

private theorem kill_powers (A B : R) (one : A + B = 1) (m n : ℕ) (z : R)
    (left : A ^ m * z = 0) (right : B ^ n * z = 0) : z = 0 := by
  induction m generalizing z with
  | zero => simpa using left
  | succ m ih =>
    have az : A * z = 0 := ih (A * z)
      (by rw [← mul_assoc, ← pow_succ]; exact left)
      (by calc
            B ^ n * (A * z) = A * (B ^ n * z) := by ring
            _ = 0 := by rw [right, mul_zero])
    have bz : B * z = z := by
      calc
        B * z = (A + B) * z := by rw [add_mul, az, zero_add]
        _ = z := by rw [one, one_mul]
    have fixed (k : ℕ) : B ^ k * z = z := by
      induction k with
      | zero => simp
      | succ k ihk => rw [pow_succ, mul_assoc, bz, ihk]
    rw [← fixed n]
    exact right

/-- Apply this in (ℤ/dℤ)[S]/(S^p−2) to the polynomial of cleared site numerators. -/
theorem recover_from_two_differences (x y z : R) (a b m n : ℕ)
    (seam : x ^ a * y ^ b = 2)
    (left : (x - 1) ^ m * z = 0) (right : (y - 1) ^ n * z = 0) : z = 0 := by
  obtain ⟨u, v, eq⟩ := seam_coprime x y a b seam
  apply kill_powers (u * (x-1)) (v * (y-1)) eq m n z
  · rw [mul_pow, mul_assoc, left, mul_zero]
  · rw [mul_pow, mul_assoc, right, mul_zero]

end Shift

/-- The finite window carry in the natural temporal order of the rotation. -/
def total (b : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | n+1 => total b n + b n

def carry (b : ℕ → ℕ) (j : ℕ → ℤ) : ℕ → ℤ
  | 0 => 0
  | n+1 => 3 * carry b j n + 2 ^ total b n * j n

theorem unroll (b : ℕ → ℕ) (j n : ℕ → ℤ) (d : ℤ) (L : ℕ)
    (step : ∀ i < L, 2 ^ b i * n (i+1) = 3 * n i + d * j i) :
    2 ^ total b L * n L = 3 ^ L * n 0 + d * carry b j L := by
  induction L with
  | zero => simp [total, carry]
  | succ L ih =>
    have prev := ih (fun i hi => step i (by omega))
    have last := step L (by omega)
    calc
      2 ^ total b (L+1) * n (L+1) = 2 ^ total b L * (2 ^ b L * n (L+1)) := by
        rw [total, pow_add, mul_assoc]
      _ = 2 ^ total b L * (3 * n L + d * j L) := by rw [last]
      _ = 3 * (2 ^ total b L * n L) + d * (2 ^ total b L * j L) := by ring
      _ = 3 ^ (L+1) * n 0 + d * carry b j (L+1) := by rw [prev, carry, pow_succ]; ring

theorem small_edge (M scale x y J : ℤ) (congr : M ∣ scale * y - 3 * x - J)
    (bound : (scale * y - 3 * x - J).natAbs < M.natAbs) :
    scale * y = 3 * x + J := by
  have h := Int.eq_zero_of_dvd_of_natAbs_lt_natAbs congr bound
  omega

/-- Once all decoded edges are equalities, any competing solution differs by a
homogeneous lap with two unequal multipliers. -/
theorem lap_rigid (x y a b : ℤ) (lap : a * (x-y) = b * (x-y))
    (ne : a ≠ b) : x = y := by
  have h : (a-b)*(x-y) = 0 := by rw [sub_mul, lap, sub_self]
  rcases mul_eq_zero.mp h with e | e
  · exact False.elim (ne (sub_eq_zero.mp e))
  · exact sub_eq_zero.mp e

/-- Residues obtained from the same rational array agree on adjacent windows,
including when the denominator is a proper factor of the full lap determinant. -/
theorem overlap {M d u v A n n' x y J : ℤ} (bez : u*d+v*M=1)
    (step : A*n'=3*n+d*J) (first : M ∣ d*x-n) (last : M ∣ d*y-n') :
    M ∣ A*y-3*x-J := by
  obtain ⟨a, ha⟩ := first
  obtain ⟨b, hb⟩ := last
  let e := A*y-3*x-J
  have scaled : d*e = M*(A*b-3*a) := by
    calc
      d*e = A*(d*y-n')-3*(d*x-n)+(A*n'-3*n-d*J) := by dsimp [e]; ring
      _ = M*(A*b-3*a) := by rw [ha, hb, step]; ring
  change M ∣ e
  refine ⟨u*(A*b-3*a)+v*e, ?_⟩
  calc
    e = (u*d+v*M)*e := by rw [bez, one_mul]
    _ = u*(d*e) + v*M*e := by ring
    _ = M*(u*(A*b-3*a)+v*e) := by rw [scaled]; ring

/-- Exact finite decoder. The rational array is supplied as n/d. Each local
candidate is congruent to that value at the modulus specified in the theorem. -/
theorem decode_lap (b : ℕ → ℕ) (j n y : ℕ → ℤ) (d M u v : ℤ) (p : ℕ)
    (bez : u*d+v*M=1) (closed_n : n p = n 0) (closed_y : y p = y 0)
    (input : ∀ i < p, 2 ^ b i * n (i+1) = 3*n i + d*j i)
    (residue : ∀ i ≤ p, M ∣ d*y i-n i)
    (small : ∀ i < p, (2 ^ b i * y (i+1) - 3*y i-j i).natAbs < M.natAbs)
    (ne : (2:ℤ)^total b p ≠ 3^p) : ∀ i ≤ p, n i = d*y i := by
  let f := fun i => n i-d*y i
  have fstep (i : ℕ) (hi : i < p) :
      2 ^ b i * f (i+1) = 3*f i + 0*(0:ℤ) := by
    have edge := small_edge M (2 ^ b i) (y i) (y (i+1)) (j i)
      (overlap bez (input i hi) (residue i (by omega)) (residue (i+1) (by omega)))
      (small i hi)
    calc
      2 ^ b i * f (i+1) = 2 ^ b i * n (i+1) - d * (2 ^ b i * y (i+1)) := by
        dsimp [f]; ring
      _ = 3*f i + 0*0 := by rw [input i hi, edge]; dsimp [f]; ring
  have fclosed : f p = f 0 := by dsimp [f]; rw [closed_n, closed_y]
  have lap := unroll b (fun _ => 0) f 0 p fstep
  rw [fclosed, zero_mul, add_zero] at lap
  have zero_prod : ((2:ℤ)^total b p-3^p)*f 0 = 0 := by rw [sub_mul, lap, sub_self]
  have fzero : f 0 = 0 := (mul_eq_zero.mp zero_prod).resolve_left (sub_ne_zero.mpr ne)
  intro i hi
  have pref := unroll b (fun _ => 0) f 0 i (fun k hk => fstep k (by omega))
  rw [fzero, mul_zero, zero_mul, add_zero] at pref
  have two_ne : (2:ℤ)^total b i ≠ 0 := pow_ne_zero _ (by decide)
  exact sub_eq_zero.mp ((mul_eq_zero.mp pref).resolve_left two_ne)

#print axioms seam_coprime
#print axioms recover_from_two_differences
#print axioms unroll
#print axioms small_edge
#print axioms lap_rigid
#print axioms overlap
#print axioms decode_lap

end LocalDenominator
