import Mathlib.NumberTheory.Divisors
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

/-! Height-restricted divisor counting for a finite family of physical affine rows. -/
set_option autoImplicit false
namespace Collatz.TruncatedDivisors

/-- Divisors of the positive row product which meet the physical size cap. -/
def capped (P Y : ℕ) : Finset ℕ := P.divisors.filter (· ≤ Y)

theorem capped_row (S : Finset ℕ) (q : ℕ → ℕ) (D B C P Y : ℕ)
    (hB : 0 < B) (hP : P ≠ 0)
    (row : ∀ x ∈ S, D * q x = B * x + C ∧ q x ∣ P ∧ q x ≤ Y) :
    S.card ≤ (capped P Y).card := by
  apply Finset.card_le_card_of_injOn q
  · intro x hx
    exact Finset.mem_filter.mpr ⟨Nat.mem_divisors.mpr ⟨(row x hx).2.1, hP⟩, (row x hx).2.2⟩
  · intro x hx y hy hxy
    have e : B*x+C = B*y+C := by rw [← (row x hx).1, ← (row y hy).1, hxy]
    exact Nat.eq_of_mul_eq_mul_left hB (Nat.add_right_cancel e)

/-- A word, a row, and its cap may be selected separately at each original source. -/
theorem capped_cover {ι : Type*} [DecidableEq ι] (I : Finset ι) (S : Finset ℕ)
    (q : ι → ℕ → ℕ) (D B C P Y : ι → ℕ)
    (positive : ∀ i ∈ I, 0 < B i ∧ P i ≠ 0)
    (cover : ∀ x ∈ S, ∃ i ∈ I,
      D i * q i x = B i * x + C i ∧ q i x ∣ P i ∧ q i x ≤ Y i) :
    S.card ≤ ∑ i ∈ I, (capped (P i) (Y i)).card := by
  classical
  let row := fun (i : ι) (x : ℕ) =>
    D i * q i x = B i * x + C i ∧ q i x ∣ P i ∧ q i x ≤ Y i
  let F := fun i => S.filter (row i)
  have sub : S ⊆ I.biUnion F := by
    intro x hx
    obtain ⟨i, hi, he⟩ := cover x hx
    exact Finset.mem_biUnion.mpr ⟨i, hi, Finset.mem_filter.mpr ⟨hx, he⟩⟩
  calc
    S.card ≤ (I.biUnion F).card := Finset.card_le_card sub
    _ ≤ ∑ i ∈ I, (F i).card := Finset.card_biUnion_le
    _ ≤ _ := by
      apply Finset.sum_le_sum
      intro i hi
      exact capped_row (F i) (q i) _ _ _ _ _ (positive i hi).1 (positive i hi).2
        (fun _ hx => (Finset.mem_filter.mp hx).2)

/-- Rankin's inequality with the full finite divisor sum and a real exponent. -/
theorem rankin (P Y : ℕ) (σ : ℝ) (hσ : 0 ≤ σ) :
    ((capped P Y).card : ℝ) ≤ (Y : ℝ)^σ * ∑ d ∈ P.divisors, ((d : ℝ)^σ)⁻¹ := by
  classical
  have hsub : capped P Y ⊆ P.divisors := Finset.filter_subset _ _
  calc
    ((capped P Y).card : ℝ) = ∑ _d ∈ capped P Y, (1 : ℝ) := by simp
    _ ≤ ∑ d ∈ capped P Y, (Y : ℝ)^σ * ((d : ℝ)^σ)⁻¹ := by
      apply Finset.sum_le_sum
      intro d hd
      have hpos : (0 : ℝ) < d := by exact_mod_cast Nat.pos_of_mem_divisors (hsub hd)
      have hle : (d : ℝ) ≤ Y := by exact_mod_cast (Finset.mem_filter.mp hd).2
      rw [← div_eq_mul_inv, one_le_div (Real.rpow_pos_of_pos hpos _)]
      exact Real.rpow_le_rpow hpos.le hle hσ
    _ ≤ ∑ d ∈ P.divisors, (Y : ℝ)^σ * ((d : ℝ)^σ)⁻¹ :=
      Finset.sum_le_sum_of_subset_of_nonneg hsub (by intros; positivity)
    _ = _ := by rw [Finset.mul_sum]

/-- Walking up the prime factors of a large divisor first crosses a fixed height. -/
theorem factor_crossing (Y : ℕ) (hY : 0 < Y) (d : ℕ) (hd : Y < d) :
    ∃ g p : ℕ, g ≤ Y ∧ p.Prime ∧ g*p ∣ d ∧ Y < g*p := by
  induction d using Nat.strong_induction_on with
  | h d ih =>
    obtain ⟨p, hp, k, hk⟩ := Nat.exists_prime_and_dvd (by omega : d ≠ 1)
    by_cases small : k ≤ Y
    · exact ⟨k, p, small, hp, by rw [hk, Nat.mul_comm], by simpa [Nat.mul_comm, hk] using hd⟩
    · have hkpos : 0 < k := by omega
      have hlt : k < d := by rw [hk]; nlinarith [hp.two_le]
      obtain ⟨g, u, hg, hu, divisor, crossed⟩ := ih k hlt (by omega)
      exact ⟨g, u, hg, hu, dvd_trans divisor (hk ▸ Nat.dvd_mul_left k p), crossed⟩

private theorem narrow_multiples {a b u Y : ℕ} (hu : Y < u) (ha : u ∣ a) (hb : u ∣ b)
    (ab : a ≤ b+Y) (ba : b ≤ a+Y) : a = b := by
  rcases lt_trichotomy a b with lt | eq | gt
  · have lo := Nat.le_of_dvd (show 0 < b-a by omega) (Nat.dvd_sub hb ha)
    omega
  · exact eq
  · have lo := Nat.le_of_dvd (show 0 < a-b by omega) (Nat.dvd_sub ha hb)
    omega

/-- The root interval may have arbitrary translation. Every divisor past Y has a
canonicalizable two-factor certificate with at most one possible multiple in S. -/
theorem shifted_divisors (S : Finset ℕ) (P Y : ℕ) (hP : P ≠ 0) (hY : 0 < Y)
    (divisor : ∀ d ∈ S, d ∣ P) (width : ∀ a ∈ S, ∀ b ∈ S, a ≤ b+Y) :
    S.card ≤ (capped P Y).card * (1 + P.primeFactors.card) := by
  classical
  let J := (capped P Y) ×ˢ P.primeFactors
  let F := fun (v : ℕ × ℕ) => S.filter (fun d => Y < v.1*v.2 ∧ v.1*v.2 ∣ d)
  have sub : S ⊆ (capped P Y) ∪ J.biUnion F := by
    intro d hd
    by_cases small : d ≤ Y
    · exact Finset.mem_union_left _ (Finset.mem_filter.mpr
        ⟨Nat.mem_divisors.mpr ⟨divisor d hd, hP⟩, small⟩)
    · obtain ⟨g, p, hg, hp, hgp, above⟩ := factor_crossing Y hY d (by omega)
      have dp : g*p ∣ P := dvd_trans hgp (divisor d hd)
      have hgP := dvd_trans (Nat.dvd_mul_right g p) dp
      have hpP := dvd_trans (Nat.dvd_mul_left p g) dp
      apply Finset.mem_union_right
      apply Finset.mem_biUnion.mpr
      refine ⟨(g, p), Finset.mem_product.mpr ⟨?_, ?_⟩, Finset.mem_filter.mpr ⟨hd, above, hgp⟩⟩
      · exact Finset.mem_filter.mpr ⟨Nat.mem_divisors.mpr ⟨hgP, hP⟩, hg⟩
      · exact Nat.mem_primeFactors.mpr ⟨hp, hpP, hP⟩
  have card (v) : (F v).card ≤ 1 := by
    apply Finset.card_le_one.mpr
    intro a ha b hb
    obtain ⟨aS, habove, ha'⟩ := Finset.mem_filter.mp ha
    obtain ⟨bS, _, hb'⟩ := Finset.mem_filter.mp hb
    exact narrow_multiples habove ha' hb' (width a aS b bS) (width b bS a aS)
  calc
    S.card ≤ ((capped P Y) ∪ J.biUnion F).card := Finset.card_le_card sub
    _ ≤ (capped P Y).card + (J.biUnion F).card := Finset.card_union_le _ _
    _ ≤ (capped P Y).card + ∑ v ∈ J, (F v).card := Nat.add_le_add_left Finset.card_biUnion_le _
    _ ≤ (capped P Y).card + ∑ _v ∈ J, 1 :=
      Nat.add_le_add_left (Finset.sum_le_sum (fun v _ => card v)) _
    _ = _ := by simp [J, Nat.mul_add]

/-- Push the width of an arbitrarily translated set of original ordinary sources
through the actual row, then count its possible divisor images. -/
theorem shifted_row (S : Finset ℕ) (q : ℕ → ℕ) (D B C P L Y : ℕ)
    (hD : 0 < D) (hB : 0 < B) (hP : P ≠ 0) (hY : 0 < Y) (span : B*L ≤ D*Y)
    (width : ∀ x ∈ S, ∀ y ∈ S, x ≤ y+L)
    (row : ∀ x ∈ S, D*q x = B*x+C ∧ q x ∣ P) :
    S.card ≤ (capped P Y).card * (1 + P.primeFactors.card) := by
  classical
  have injective : Set.InjOn q S := by
    intro x hx y hy hxy
    have e : B*x+C = B*y+C := by rw [← (row x hx).1, ← (row y hy).1, hxy]
    exact Nat.eq_of_mul_eq_mul_left hB (Nat.add_right_cancel e)
  rw [← Finset.card_image_of_injOn injective]
  apply shifted_divisors (S.image q) P Y hP hY
  · intro a ha
    obtain ⟨x, hx, rfl⟩ := Finset.mem_image.mp ha
    exact (row x hx).2
  · intro a ha b hb
    obtain ⟨x, hx, rfl⟩ := Finset.mem_image.mp ha
    obtain ⟨y, hy, rfl⟩ := Finset.mem_image.mp hb
    apply Nat.le_of_mul_le_mul_left _ hD
    have mul := Nat.mul_le_mul_left B (width x hx y hy)
    rw [Nat.mul_add] at mul ⊢
    rw [(row x hx).1, (row y hy).1]
    omega

#print axioms factor_crossing
#print axioms shifted_divisors
#print axioms shifted_row
#print axioms capped_row
#print axioms capped_cover
#print axioms rankin
end Collatz.TruncatedDivisors
