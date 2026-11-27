import OrdinaryGapWord
import Mathlib.Tactic.FieldSimp

/-! Finite carry cutoff and two-gap routing for the exact-clock escape analysis. -/
namespace Collatz.OrdinaryGapWord

def Word.beta (u : Word) : ℚ := u.carry / (2:ℚ)^u.clock

theorem beta_snoc (u : Word) (e : ℕ) :
    (u.snoc e).beta = (3*u.beta+1)/2^(e+1) := by
  simp only [Word.beta, Word.clock, Word.carry, Int.cast_add, Int.cast_mul, Int.cast_pow,
    Int.cast_ofNat, pow_add]
  field_simp

theorem beta_nonneg (u : Word) : 0 ≤ u.beta := by
  induction u with
  | nil => simp [Word.beta, Word.carry, Word.clock]
  | snoc u e ih =>
    rw [beta_snoc]
    positivity

/-- A cutoff for enumeration at every finite word length. -/
theorem beta_le (u : Word) : u.beta ≤ (3/2:ℚ)^u.depth-1 := by
  induction u with
  | nil => simp [Word.beta, Word.carry, Word.clock, Word.depth]
  | snoc u e ih =>
    have hpow : 1 ≤ (2:ℚ)^e := one_le_pow₀ (by norm_num)
    have hd : 2 ≤ (2:ℚ)^(e+1) := by rw [pow_succ]; linarith
    have hn : 0 ≤ 3*u.beta+1 := by linarith [beta_nonneg u]
    rw [beta_snoc, Word.depth, pow_succ (3/2:ℚ)]
    calc
      _ ≤ (3*u.beta+1)/2 := div_le_div_of_nonneg_left hn (by norm_num) hd
      _ ≤ _ := by linarith

/-- A rational threshold times an endpoint is bounded by the same word cutoff. -/
theorem target_cutoff {u : Word} {q ε : ℚ} (hε : 0 < ε) (h : ε*q ≤ u.beta) :
    q ≤ ((3/2:ℚ)^u.depth-1)/ε := by
  apply (le_div_iff₀ hε).2
  simpa [mul_comm] using h.trans (beta_le u)

def twoGapWord (a b : ℕ) : Word := (Word.nil.snoc a).snoc b

/-- Input the residue for the first gap f=a+1 at total t=(a+1)+(b+1).
The resulting explicit quotient is the actual unit source at clock t. -/
theorem two_gap_router (a b K : ℕ) (z r : ℤ) (hz : PositiveOdd z) (hr : ¬ (3:ℤ) ∣ r)
    (h : (3:ℤ)^(2+(K+1)) ∣ 2^((a+1)+(b+1))*z-3-9*r-2^(a+1)) :
    let t := (a+1)+(b+1)
    let x := (2^t*z-2^(a+1)-3)/9
    PositiveOdd x ∧ ¬ (3:ℤ) ∣ x ∧ (3:ℤ)^(K+1) ∣ x-r ∧
      Path (twoGapWord a b) x z ∧ shortcut^[t] x=z := by
  let u := twoGapWord a b
  have hc : u.clock = (a+1)+(b+1) := by simp [u, twoGapWord, Word.clock]
  have hd : u.depth = 2 := rfl
  have hcarry : u.carry = 3+2^(a+1) := by simp [u, twoGapWord, Word.clock, Word.carry]
  have hcong : (3:ℤ)^(u.depth+(K+1)) ∣ 2^u.clock*z-u.carry-3^u.depth*r := by
    rw [hc, hd, hcarry]
    convert h using 1; ring
  obtain ⟨x, hx, _⟩ := (unit_source_class_iff u hz r hr K).1 hcong
  obtain ⟨hu, hclass, hp, hrun⟩ := hx
  have he := hp.affine
  rw [hc, hd, hcarry] at he
  norm_num at he
  have hx' : (2^((a+1)+(b+1))*z-2^(a+1)-3)/9 = x := by omega
  dsimp only
  rw [hx']
  exact ⟨hp.endpoints.1, hu, hclass, hp, hc ▸ hrun⟩

#print axioms beta_snoc
#print axioms beta_nonneg
#print axioms beta_le
#print axioms target_cutoff
#print axioms two_gap_router

end Collatz.OrdinaryGapWord
