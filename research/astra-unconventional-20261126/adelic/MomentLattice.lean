import Mathlib.Data.Nat.Choose.Lucas
import Mathlib.LinearAlgebra.Matrix.Block
import Mathlib.Tactic.LinearCombination

/-! Arithmetic kernels for fixed-clock polynomial evaluation on a Collatz inverse basin.
Lucas reduction keeps the modulus p^r at the sharp elementary threshold d < p^r.
A lifted sample grid then has binomial determinant one modulo p in arbitrary degree.
The actual common-clock routing and global integral span are in MOMENT_LATTICE.md. -/

namespace CollatzRound14.Adelic
open Matrix

/-- A complete source residue at precision p^r fixes every low binomial moment modulo p. -/
theorem chooseOfPrimePowerCongr {p : ℕ} [Fact p.Prime] (r : ℕ) {x y j : ℕ}
    (hxy : x ≡ y [MOD p ^ r]) (hj : j < p ^ r) :
    x.choose j ≡ y.choose j [MOD p] := by
  induction r generalizing x y j with
  | zero =>
    have : j = 0 := by simpa using hj
    simp [this, Nat.ModEq]
  | succ r ih =>
    have hp : 0 < p := (Fact.out : p.Prime).pos
    have hprod : x % (p * p ^ r) = y % (p * p ^ r) := by
      simpa only [Nat.ModEq, pow_succ'] using hxy
    have hlo : x % p = y % p :=
      hxy.of_dvd (show p ∣ p ^ r.succ by simp [pow_succ])
    have hhi : x / p ≡ y / p [MOD p ^ r] := by
      change x / p % p ^ r = y / p % p ^ r
      rw [← Nat.mod_mul_right_div_self, ← Nat.mod_mul_right_div_self, hprod]
    have hj' : j / p < p ^ r :=
      (Nat.div_lt_iff_lt_mul hp).mpr (by simpa [pow_succ] using hj)
    have hx := Choose.choose_modEq_choose_mod_mul_choose_div_nat (p := p) (n := x) (k := j)
    have hy := Choose.choose_modEq_choose_mod_mul_choose_div_nat (p := p) (n := y) (k := j)
    rw [hlo] at hx
    exact hx.trans (((ih hhi hj').mul_left _).trans hy.symm)

/-- The chosen ordinary representatives may be arbitrarily large. Only the residue of each
sample is used. The square determinant stays a unit in the degree-d binomial basis. -/
theorem sampleDeterminant {p : ℕ} [Fact p.Prime] {r d : ℕ} (hd : d < p ^ r)
    (point : Fin (d + 1) → ℕ) (hpoint : ∀ i, point i ≡ i.val [MOD p ^ r]) :
    Matrix.det (fun i j : Fin (d + 1) => ((point i).choose j.val : ZMod p)) = 1 := by
  let A : Matrix (Fin (d+1)) (Fin (d+1)) (ZMod p) :=
    fun i j => ((point i).choose j.val : ZMod p)
  change A.det = 1
  have entry (i j : Fin (d+1)) : A i j = (i.val.choose j.val : ZMod p) := by
    exact (ZMod.natCast_eq_natCast_iff _ _ _).mpr
      (chooseOfPrimePowerCongr r (hpoint i) (Nat.lt_of_le_of_lt (by omega) hd))
  have lower : A.IsLowerTriangular := by
    intro i j hij
    have h : i.val < j.val := hij
    rw [entry, Nat.choose_eq_zero_of_lt h, Nat.cast_zero]
  rw [A.det_of_isLowerTriangular lower]
  simp [entry]

/-- Difference ledger for the two-edge geometric family at a common terminal.
After reducing modulo a good prime the only possible collision factors are 64^j−1. -/
theorem geometricDifference {x : ℕ → ℤ} {w a : ℤ}
    (h : ∀ i, 9 * x i + 3 + a * 64 ^ i = w) (i j : ℕ) :
    9 * (x i - x (i+j)) = a * 64 ^ i * (64 ^ j - 1) := by
  have h' := h (i+j)
  rw [pow_add] at h'
  linear_combination h i - h'

/-- Compose two signed evaluations at genuine intermediate cut points.  The second
family may depend on its particular cut.  The product coefficient formula is the
inductive kernel for arbitrary numbers of marked segments in MULTIPLE_CUTS.md. -/
theorem composeSignedEvaluation {I A B : Type*} {X : I → Type*}
    [Fintype I] [∀ i, Fintype (X i)] (outer : I → A → ℤ)
    (inner : (i : I) → X i → B → ℤ) (a : A → ℤ) (b : B → ℤ)
    (hout : ∃ c : I → ℤ, ∀ j, ∑ i, c i * outer i j = a j)
    (hin : ∀ i, ∃ f : X i → ℤ, ∀ j, ∑ x, f x * inner i x j = b j) :
    ∃ weights : (i : I) → X i → ℤ, ∀ j l,
      (∑ i, ∑ x, weights i x * (outer i j * inner i x l)) = a j * b l := by
  classical
  obtain ⟨c, hc⟩ := hout
  choose f hf using hin
  refine ⟨fun i x => c i * f i x, fun j l => ?_⟩
  calc
    (∑ i, ∑ x, (c i * f i x) * (outer i j * inner i x l)) =
        ∑ i, (c i * outer i j) * (∑ x, f i x * inner i x l) := by
      apply Finset.sum_congr rfl
      intro i _
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro x _
      ring
    _ = a j * b l := by simp_rw [hf]; rw [← Finset.sum_mul, hc]

#print axioms composeSignedEvaluation
#print axioms chooseOfPrimePowerCongr
#print axioms sampleDeterminant
#print axioms geometricDifference
end CollatzRound14.Adelic
