import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Ring

namespace AstraNine.CountedBlockCopy

def step (z : ℤ) : ℤ := if z % 2 = 0 then z / 2 else (3*z+1)/2

def bit (z : ℤ) : ℕ := if z % 2 = 0 then 0 else 1

def endpoint : ℕ → ℤ → ℤ
  | 0, z => z
  | t+1, z => endpoint t (step z)

def odds : ℕ → ℤ → ℕ
  | 0, _ => 0
  | t+1, z => bit z + odds t (step z)

private theorem bit_shift (z h : ℤ) : bit (z + 2*h) = bit z := by
  have hm : (z + 2*h) % 2 = z % 2 := by omega
  simp only [bit, hm]

private theorem step_shift (z h : ℤ) :
    step (z + 2*h) = step z + 3^(bit z)*h := by
  have hm : (z + 2*h) % 2 = z % 2 := by omega
  by_cases hz : z % 2 = 0
  · simp only [step, bit, hm, hz, ite_true, pow_zero, one_mul]
    omega
  · simp only [step, bit, hm, hz, ite_false, pow_one]
    omega

/-- Copy a complete shortcut prefix with its actual ordinary count and endpoint.
The displacement is signed, permitting a lower positive endpoint to be copied. -/
theorem prefix_copy (t : ℕ) (z h : ℤ) :
    endpoint t (z + 2^t*h) = endpoint t z + 3^(odds t z)*h ∧
    odds t (z + 2^t*h) = odds t z := by
  induction t generalizing z h with
  | zero => simp [endpoint, odds]
  | succ t ih =>
    have hs : z + 2^(t+1)*h = z + 2*(2^t*h) := by rw [pow_succ]; ring
    have he : step (z + 2*(2^t*h)) = step z + 2^t*(3^(bit z)*h) := by
      rw [step_shift]
      ring
    obtain ⟨hval, hodd⟩ := ih (step z) (3^(bit z)*h)
    rw [hs]
    constructor
    · simp only [endpoint, odds, he, hval, pow_add]
      ring
    · simp only [odds, bit_shift, he, hodd]

private theorem nonpositive_endpoint (t : ℕ) (z : ℤ) (hz : z ≤ 0) :
    endpoint t z ≤ 0 := by
  induction t generalizing z with
  | zero => exact hz
  | succ t ih =>
    apply ih
    unfold step
    split <;> omega

/-- Every ordinary member of a counted-fused consecutive block transports
to the new positive endpoint, including the intervening even sources. -/
theorem translated_block {t k width : ℕ} {b y : ℤ}
    (template : ∀ i : ℕ, i < width →
      endpoint t (b+i) = y ∧ odds t (b+i) = k)
    (h : ℤ) (positive : 0 < y + 3^k*h) :
    ∀ i : ℕ, i < width →
      0 < b + 2^t*h + i ∧
      endpoint t (b + 2^t*h + i) = y + 3^k*h ∧
      odds t (b + 2^t*h + i) = k := by
  intro i hi
  have hshift : b + 2^t*h + i = (b+i) + 2^t*h := by ring
  obtain ⟨hy, hk⟩ := template i hi
  obtain ⟨he, hc⟩ := prefix_copy t (b+i) h
  rw [hy, hk] at he
  rw [hk] at hc
  rw [hshift]
  refine ⟨?_, he, hc⟩
  apply lt_of_not_ge
  intro hn
  have hnon := nonpositive_endpoint t ((b+i) + 2^t*h) hn
  omega

end AstraNine.CountedBlockCopy
