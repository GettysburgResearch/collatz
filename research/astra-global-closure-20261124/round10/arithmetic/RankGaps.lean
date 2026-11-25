import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace OrderedBandGaps

/-- A rank offset in a list already extended by doubling at each lap. -/
def gap (z : ℕ → ℤ) (t r : ℕ) : ℤ := z (r + t) - z r

theorem lifted_gap {z c : ℕ → ℤ} {h p : ℕ}
    (dbl : ∀ r, z (r + p) = 2 * z r)
    (edge : ∀ r, z (r + h) = 3 * z r + c r) (r t : ℕ) :
    gap z t (r + p) = 2 * gap z t r ∧
    gap z t (r + h) = 3 * gap z t r + gap c t r := by
  unfold gap
  constructor
  · rw [show r + p + t = r + t + p by omega, dbl, dbl]
    ring
  · rw [show r + h + t = r + t + h by omega, edge, edge]
    ring

/-- When a common power of two is removed from the output gap, the upper
endpoint may have crossed an additional cut.  Doubling on the lift handles it. -/
theorem base_gap (g : ℕ → ℤ) {p : ℕ} (dbl : ∀ r, g (r + p) = 2 * g r)
    (n : ℕ) : g n = 2 ^ (n / p) * g (n % p) := by
  have it (q r : ℕ) : g (r + p*q) = 2 ^ q * g r := by
    induction q with
    | zero => simp
    | succ q ih =>
      rw [Nat.mul_succ, ← Nat.add_assoc, dbl, ih, pow_succ]
      ring
  simpa only [Nat.mod_add_div] using it (n / p) (n % p)

theorem common_edge {x x' y y' j : ℤ} {b : ℕ}
    (hx : 2 ^ b * x' = 3 * x + j)
    (hy : 2 ^ b * y' = 3 * y + j) :
    2 ^ b * (x' - y') = 3 * (x - y) := by
  rw [mul_sub, hx, hy]
  ring

def total (b : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | n+1 => total b n + b n

theorem propagate (b : ℕ → ℕ) (d : ℕ → ℤ) (n : ℕ)
    (steps : ∀ i < n, 2 ^ b i * d (i + 1) = 3 * d i) :
    2 ^ total b n * d n = 3 ^ n * d 0 := by
  induction n with
  | zero => simp [total]
  | succ n ih =>
    have left := ih (fun i hi => steps i (by omega))
    have right := steps n (by omega)
    calc
      2 ^ total b (n+1) * d (n+1) = 2 ^ total b n * (2 ^ b n * d (n+1)) := by
        rw [total, pow_add, mul_assoc]
      _ = 3 * (2 ^ total b n * d n) := by rw [right]; ring
      _ = 3 ^ (n+1) * d 0 := by rw [left, pow_succ]; ring

private theorem coprime23 : IsCoprime (2 : ℤ) 3 := ⟨-1, 1, by norm_num⟩

/-- The central difference is constrained by the entire product. Both input
identities concern that same integer, and may come from different word lengths. -/
theorem middle_modulus {x d y : ℤ} {a f bm bp : ℕ}
    (past : 2 ^ bm * d = 3 ^ a * x) (future : 2 ^ bp * y = 3 ^ f * d) :
    (3 : ℤ) ^ a * 2 ^ bp ∣ d := by
  have d3 : (3 : ℤ) ^ a ∣ (2 : ℤ) ^ bm * d := ⟨x, past⟩
  have d2 : (2 : ℤ) ^ bp ∣ (3 : ℤ) ^ f * d := ⟨y, future.symm⟩
  exact (coprime23.symm.pow).mul_dvd
    (coprime23.symm.pow.dvd_of_dvd_mul_left d3)
    (coprime23.pow.dvd_of_dvd_mul_left d2)

theorem middle_zero {x d y : ℤ} {a f bm bp : ℕ}
    (past : 2 ^ bm * d = 3 ^ a * x) (future : 2 ^ bp * y = 3 ^ f * d)
    (small : d.natAbs < ((3 : ℤ) ^ a * 2 ^ bp).natAbs) : d = 0 :=
  Int.eq_zero_of_dvd_of_natAbs_lt_natAbs (middle_modulus past future) small

#print axioms lifted_gap
#print axioms base_gap
#print axioms common_edge
#print axioms propagate
#print axioms middle_modulus
#print axioms middle_zero

end OrderedBandGaps
