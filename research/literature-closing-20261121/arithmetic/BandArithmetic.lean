module

public import BandRotation
public import BandDescent

@[expose] public section

/-!
# The exact ordinary arithmetic behind a marked band visit

The affine carry of an actual odd orbit is retained, including its prime-to-3
condition.  The natural three-coordinate S-adic linear-form product proposed
for a band visit is exactly its nonnegative integer offset.  In particular,
it cannot provide the height saving required by the Subspace Theorem.

This file formalizes ordinary integer identities and the resulting real
product.  The interpretation of its explicitly evaluated factors as local
norms is proved in ARITHMETIC_CLOSURE.md, not postulated as an axiom here.
No global convergence or eventual periodicity assertion is made.
-/

namespace CollatzShell.BandArithmetic

open ForwardSection BandRotation BandDescent

/-- The exact affine carry of the first `j` actual odd steps. -/
def affineCarry (n : Nat) : Nat → Nat
  | 0 => 0
  | j+1 => 3 * affineCarry n j + 2 ^ valuationSum n j

/-- The integer version of the logarithmic identity: neither the additive
carry nor the accumulated binary valuation is discarded. -/
theorem affine_identity (n j : Nat) :
    2 ^ valuationSum n j * oddOrbit n j = 3 ^ j * n + affineCarry n j := by
  induction j with
  | zero => simp [valuationSum, oddOrbit, affineCarry]
  | succ j ih =>
    have hstep :
        2 ^ twos (3 * oddOrbit n j + 1) * oddStep (oddOrbit n j) =
          3 * oddOrbit n j + 1 :=
      Nat.ordProj_mul_ordCompl_eq_self _ 2
    rw [valuationSum, oddOrbit, pow_add, mul_assoc, hstep, affineCarry]
    rw [mul_add, mul_one]
    rw [show 2 ^ valuationSum n j * (3 * oddOrbit n j) =
      3 * (2 ^ valuationSum n j * oddOrbit n j) by ring, ih]
    rw [pow_succ]
    ring

/-- A positive odd prefix has a positive affine carry. -/
theorem affine_carry_pos (n j : Nat) : 0 < affineCarry n (j+1) := by
  simp only [affineCarry]
  positivity

/-- The last carry term is a power of two, so no factor of three is available
to pay for the remaining real error. -/
theorem affine_carry_mod_three (n j : Nat) :
    affineCarry n (j+1) % 3 ≠ 0 := by
  have hp : (2 ^ valuationSum n j) % 3 ≠ 0 := by
    intro hz
    have hd : 3 ∣ 2 ^ valuationSum n j := Nat.dvd_of_mod_eq_zero hz
    have impossible : 3 ∣ 2 := Nat.prime_three.dvd_of_dvd_pow hd
    norm_num at impossible
  simpa [affineCarry, Nat.add_mod, Nat.mul_mod] using hp

/-- The two monomial coordinates are primitive; no common content is hidden
in a projective normalization. -/
theorem monomial_coordinates_coprime (j A d : Nat) :
    Nat.Coprime (3 ^ j) (2 ^ (A+d)) := by
  exact Nat.Coprime.pow j (A+d) (by decide : Nat.Coprime 3 2)

/-- The band error after an actual odd prefix is exactly the binary
denominator times the endpoint offset. -/
theorem exact_band_residual (n j d : Nat) :
    (n : ℝ) * (3 : ℝ) ^ j + affineCarry n j - (2 : ℝ) ^ (valuationSum n j+d) =
      (2 : ℝ) ^ valuationSum n j * ((oddOrbit n j : ℝ) - (2 : ℝ) ^ d) := by
  have h :
      (2 : ℝ) ^ valuationSum n j * (oddOrbit n j : ℝ) =
        (3 : ℝ) ^ j * n + affineCarry n j := by
    exact_mod_cast affine_identity n j
  rw [pow_add]
  nlinarith only [h]

/-- The evaluated local-factor product for the forms listed in the companion
note.  All factors, including the real height factors, are present. -/
noncomputable def bandProduct (n j d : Nat) : ℝ :=
  (3 : ℝ) ^ j * (2 : ℝ) ^ (valuationSum n j+d) *
    |(n : ℝ) * (3 : ℝ) ^ j + affineCarry n j -
      (2 : ℝ) ^ (valuationSum n j+d)| *
    ((2 : ℝ) ^ (valuationSum n j+d))⁻¹ *
    ((2 : ℝ) ^ valuationSum n j)⁻¹ * ((3 : ℝ) ^ j)⁻¹

/-- Exact cancellation, valid at every actual prefix, before imposing the
marked-band inequality. -/
theorem band_product_exact (n j d : Nat) :
    bandProduct n j d = |(oddOrbit n j : ℝ) - (2 : ℝ) ^ d| := by
  unfold bandProduct
  rw [exact_band_residual, abs_mul,
    abs_of_nonneg (by positivity : (0 : ℝ) ≤ (2 : ℝ) ^ valuationSum n j)]
  field_simp

/-- The only odd nonnegative integer which is a power of two is one. -/
theorem odd_power_two_eq_one {x d : Nat} (odd : x % 2 = 1)
    (eq : x = 2 ^ d) : x = 1 := by
  cases d with
  | zero => simpa using eq
  | succ d =>
    rw [eq, pow_succ] at odd
    omega

/-- At a nontrivial marked endpoint the complete product is a positive
integer, rather than a negative power of the projective height. -/
theorem marked_band_product_ge_one {n j : Nat}
    (mark : Marked (oddOrbit n j)) (nontrivial : 1 < oddOrbit n j) :
    1 ≤ bandProduct n j (oddOrbit n j).log2 := by
  let x := oddOrbit n j
  have xp : 0 < x := by dsimp [x]; omega
  have lower : 2 ^ x.log2 ≤ x := Nat.log2_self_le xp.ne'
  have neq : x ≠ 2 ^ x.log2 := by
    intro h
    have one := odd_power_two_eq_one mark.1 h
    omega
  have gap : 1 ≤ x - 2 ^ x.log2 := by omega
  have nonneg : (0 : ℝ) ≤ (x : ℝ) - (2 : ℝ) ^ x.log2 := by
    have low : (2 : ℝ) ^ x.log2 ≤ (x : ℝ) := by exact_mod_cast lower
    linarith
  rw [band_product_exact, abs_of_nonneg nonneg]
  have real_gap : (2 : ℝ) ^ x.log2 + 1 ≤ (x : ℝ) := by
    exact_mod_cast (show 2 ^ x.log2 + 1 ≤ x by omega)
  linarith

/-- A putative Subspace application whose required product is less than one
is ruled out for this explicit form system. -/
theorem marked_band_product_not_small {n j : Nat}
    (mark : Marked (oddOrbit n j)) (nontrivial : 1 < oddOrbit n j)
    {threshold : ℝ} (small : threshold < 1) :
    ¬ bandProduct n j (oddOrbit n j).log2 ≤ threshold := by
  have bound := marked_band_product_ge_one mark nontrivial
  linarith

/-- Keeping any fixed finite number of marked returns as independent blocks
does not create a Subspace saving: the full product is still at least one. -/
theorem finite_return_product_ge_one {n r : Nat} (visits : Nat → Nat)
    (marks : ∀ i < r, Marked (oddOrbit n (visits i)))
    (nontrivial : ∀ i < r, 1 < oddOrbit n (visits i)) :
    1 ≤ ∏ i ∈ Finset.range r,
      bandProduct n (visits i) (oddOrbit n (visits i)).log2 := by
  exact Finset.one_le_prod₀ fun i hi =>
    marked_band_product_ge_one (marks i (Finset.mem_range.mp hi))
      (nontrivial i (Finset.mem_range.mp hi))

/-- A leading dyadic translate leaves every parity inside its binary horizon
unchanged.  Thus narrow leading bands alone do not forbid finite low-bit
itineraries. -/
theorem offset_parity_inside {d k : Nat} (u : Nat) (clock : k < d) :
    orbit k (2 ^ d + u) % 2 = orbit k u % 2 := by
  rw [offset_lift u clock.le]
  have dp : 0 < d-k := by omega
  obtain ⟨a, ha⟩ : ∃ a, d-k = a+1 := ⟨d-k-1, by omega⟩
  rw [ha, pow_succ]
  simp [Nat.add_mod, Nat.mul_mod]

/-- Two distinct ordinary integers separated by less than `2^L` must have
different parity itineraries before clock `L`.  The witness is the exact
two-adic order of their ordinary difference. -/
theorem parity_separates_close_sources {x y L : Nat} (xy : x < y)
    (room : y-x < 2 ^ L) :
    ∃ k < L, orbit k x % 2 ≠ orbit k y % 2 := by
  let D := y-x
  let d := twos D
  let t := oddPart D
  have Dp : 0 < D := by dsimp [D]; omega
  have tp : 0 < t := Nat.ordCompl_pos 2 Dp.ne'
  have split : 2 ^ d * t = D := Nat.ordProj_mul_ordCompl_eq_self D 2
  have oddt : t % 2 = 1 := by
    have ht : ¬ 2 ∣ t := Nat.not_dvd_ordCompl Nat.prime_two Dp.ne'
    omega
  have power_le : 2 ^ d ≤ D := by
    calc 2 ^ d = 2 ^ d * 1 := by omega
         _ ≤ 2 ^ d * t := Nat.mul_le_mul_left _ tp
         _ = D := split
  have early : d < L := by
    by_contra! late
    have hp := Nat.pow_le_pow_right (by decide : 0 < 2) late
    dsimp [D] at power_le
    omega
  have lift : y = 2 ^ d * t + x := by dsimp [D] at split; omega
  refine ⟨d, early, ?_⟩
  rw [lift, prefix_lift]
  have odd_coeff : 3 ^ oddCount d x % 2 = 1 := by simp [Nat.pow_mod]
  have odd_prod : (3 ^ oddCount d x * t) % 2 = 1 := by
    simp [Nat.mul_mod, odd_coeff, oddt]
  omega

/-- The source-height condition needed by a periodic-shadow or repeated-word
argument.  A narrow phase interval does not supply the repeated-word premise. -/
theorem repeated_parity_requires_displacement {x y L : Nat} (ne : x ≠ y)
    (same : ∀ k < L, orbit k x % 2 = orbit k y % 2) :
    2 ^ L ≤ (x-y) + (y-x) := by
  by_contra! small
  rcases lt_or_gt_of_ne ne with h | h
  · obtain ⟨k, hk, different⟩ := parity_separates_close_sources (L := L) h (by omega)
    exact different (same k hk)
  · obtain ⟨k, hk, different⟩ := parity_separates_close_sources (L := L) h (by omega)
    exact different (same k hk).symm

/-- An exact finite certificate for equality, and hence for a cycle whenever
the two sources are states on one ordinary trajectory. -/
theorem equal_of_repeated_parity_and_small_displacement {x y L : Nat}
    (same : ∀ k < L, orbit k x % 2 = orbit k y % 2)
    (small : (x-y) + (y-x) < 2 ^ L) : x = y := by
  by_contra ne
  have large := repeated_parity_requires_displacement ne same
  omega

end CollatzShell.BandArithmetic
