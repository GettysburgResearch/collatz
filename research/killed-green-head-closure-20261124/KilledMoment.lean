import Mathlib

/-!
Finite killed-moment core for the companion written argument.
This file is a proposed Lean source, NOT compiled in the authoring session.
No probability or Collatz convergence hypothesis is installed as an axiom.
-/

namespace Collatz.KilledGreenHead

theorem sqrt_majorant_certificate :
    (1/2 : ℚ) ≤ (71/100)^2 ∧
    (3/2 : ℚ) ≤ (123/100)^2 ∧
    ((71/100 : ℚ) + 123/100)/2 = 97/100 ∧
    (97/100 : ℚ) < 1 := by
  norm_num

/-- Monotonicity of a nonnegative survival sequence over a shifted block. -/
theorem survival_block (p : ℕ → ℝ)
    (hp : ∀ i, p (i+1) ≤ p i) (n k : ℕ) :
    p (n+k) ≤ p n := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Nat.add_succ]
    exact (hp (n+k)).trans ih

/-- A killed-moment recursion is controlled by the survival probability
at the beginning of any block. The factor p is retained in the forcing;
replacing it by one loses the summable late occupation estimate. -/
theorem killed_moment_block (m p : ℕ → ℝ) (c b : ℝ)
    (hc0 : 0 ≤ c) (hc1 : c < 1) (hb : 0 ≤ b)
    (hp0 : ∀ i, 0 ≤ p i)
    (hp : ∀ i, p (i+1) ≤ p i)
    (hr : ∀ i, m (i+1) ≤ c*m i+b*p i)
    (n k : ℕ) :
    m (n+k) ≤ c^k*m n + (b/(1-c))*p n := by
  have hd : 0 < 1-c := sub_pos.mpr hc1
  have hcoef : c*(b/(1-c))+b = b/(1-c) := by
    field_simp [ne_of_gt hd] <;> ring
  induction k with
  | zero =>
    have hnon : 0 ≤ (b/(1-c))*p n :=
      mul_nonneg (div_nonneg hb (le_of_lt hd)) (hp0 n)
    simp only [Nat.add_zero, pow_zero, one_mul]
    linarith
  | succ k ih =>
    have hstep := hr (n+k)
    have hmon := survival_block p hp n k
    calc
      m (n+(k+1)) = m ((n+k)+1) := by rw [Nat.add_assoc]
      _ ≤ c*m (n+k)+b*p (n+k) := hstep
      _ ≤ c*(c^k*m n+(b/(1-c))*p n)+b*p n :=
        add_le_add (mul_le_mul_of_nonneg_left ih hc0)
          (mul_le_mul_of_nonneg_left hmon hb)
      _ = (c^k*c)*m n+(c*(b/(1-c))+b)*p n := by ring
      _ = c^(k+1)*m n+(b/(1-c))*p n := by rw [pow_succ, hcoef]

/-- Abstract finite Green-function charging: expected future cost is
bounded by alive mass plus its killed moment. -/
theorem green_charge (K a p m v : ℝ)
    (hK : 0 ≤ K) (ha : 0 ≤ a)
    (hp : 0 ≤ p) (hm : 0 ≤ m)
    (h : v ≤ K*(p+m))
    (hp' : p ≤ a) (hm' : m ≤ a) :
    v ≤ 2*K*a := by
  calc
    v ≤ K*(p+m) := h
    _ ≤ K*(a+a) := mul_le_mul_of_nonneg_left (add_le_add hp' hm') hK
    _ = 2*K*a := by ring

end Collatz.KilledGreenHead

#print axioms Collatz.KilledGreenHead.sqrt_majorant_certificate
#print axioms Collatz.KilledGreenHead.survival_block
#print axioms Collatz.KilledGreenHead.killed_moment_block
#print axioms Collatz.KilledGreenHead.green_charge
