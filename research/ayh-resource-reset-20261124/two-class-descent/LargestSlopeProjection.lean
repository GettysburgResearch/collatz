import Mathlib

/-! Projection of simultaneous affine records to a largest-slope coordinate. -/

namespace Collatz.LargestSlopeProjection

/-- Once the largest-slope endpoint is fixed, the offset of each remaining
endpoint from the projected center lies between minus and plus L. -/
theorem endpoint_in_band {H n lam anchor c ca e ea L y ya : ℝ}
    (hH : 0 < H) (ha : 0 < anchor) (hl : 0 ≤ lam) (hla : lam ≤ anchor)
    (he : 0 ≤ e) (heL : e ≤ L) (hea : 0 ≤ ea) (heaL : ea ≤ L)
    (hy : y = lam * n / H + c + e)
    (hya : ya = anchor * n / H + ca + ea) :
    |y - ((lam / anchor) * (ya-ca) + c)| ≤ L := by
  have hid : y - ((lam/anchor) * (ya-ca) + c) = e - (lam/anchor)*ea := by
    rw [hy, hya]
    field_simp [ne_of_gt hH, ne_of_gt ha]
    ring
  rw [hid, abs_le]
  have hr₀ : 0 ≤ lam/anchor := div_nonneg hl ha.le
  have hr₁ : lam/anchor ≤ 1 := (div_le_one ha).mpr hla
  have hm := mul_le_mul_of_nonneg_right hr₁ hea
  have hn := mul_nonneg hr₀ hea
  constructor <;> linarith

/-- An identical anchor endpoint at two inputs bounds their separation in
the original parameter, independently of all the other coordinates. -/
theorem same_anchor_span {H n n' anchor ca e e' L : ℝ}
    (hH : 0 < H) (ha : 0 < anchor)
    (he : 0 ≤ e) (heL : e ≤ L) (he' : 0 ≤ e') (heL' : e' ≤ L)
    (hmatch : anchor*n/H + ca + e = anchor*n'/H + ca + e') :
    |n-n'| ≤ L*H/anchor := by
  have hid : anchor * (n-n') = (e'-e)*H := by
    field_simp [ne_of_gt hH] at hmatch
    linarith
  have habs := congrArg abs hid
  rw [abs_mul, abs_mul, abs_of_pos ha, abs_of_pos hH] at habs
  have herr : |e'-e| ≤ L := abs_le.mpr ⟨by linarith, by linarith⟩
  apply (le_div_iff₀ ha).mpr
  rw [mul_comm, habs]
  exact mul_le_mul_of_nonneg_right herr hH.le

/-- A joint record consists of the distinguished integer endpoint and m
remaining integer endpoints. Each coordinate's interval may depend on the
anchor. The count pays for the anchor width only once. N and D are inclusive
integer widths, with arbitrary signed interval locations. -/
theorem integer_record_census {m N D : ℕ}
    (records : Finset (ℤ × (Fin m → ℤ))) (a : ℤ)
    (low : ℤ → Fin m → ℤ)
    (ha : ∀ r ∈ records, a ≤ r.1 ∧ r.1 ≤ a + (N : ℤ))
    (hd : ∀ r ∈ records, ∀ i, low r.1 i ≤ r.2 i ∧ r.2 i ≤ low r.1 i + (D : ℤ)) :
    records.card ≤ (N+1)*(D+1)^m := by
  classical
  let code : {r // r ∈ records} → Fin (N+1) × (Fin m → Fin (D+1)) :=
    fun r =>
      (⟨(r.1.1-a).toNat, by have h := ha r.1 r.2; omega⟩,
        fun i => ⟨(r.1.2 i - low r.1.1 i).toNat,
          by have h := hd r.1 r.2 i; omega⟩)
  have hinj : Function.Injective code := by
    intro r s hrs
    have hfst := congrArg (fun p : Fin (N+1) × (Fin m → Fin (D+1)) => p.1.val) hrs
    change (r.1.1-a).toNat = (s.1.1-a).toNat at hfst
    have hr := ha r.1 r.2
    have hs := ha s.1 s.2
    have han : r.1.1 = s.1.1 := by omega
    apply Subtype.ext
    apply Prod.ext han
    funext i
    have hi := congrArg (fun p : Fin (N+1) × (Fin m → Fin (D+1)) => (p.2 i).val) hrs
    change (r.1.2 i - low r.1.1 i).toNat = (s.1.2 i - low s.1.1 i).toNat at hi
    have hri := hd r.1 r.2 i
    have hsi := hd s.1 s.2 i
    rw [han] at hi hri
    omega
  simpa using Fintype.card_le_of_injective code hinj

end Collatz.LargestSlopeProjection

#print axioms Collatz.LargestSlopeProjection.endpoint_in_band
#print axioms Collatz.LargestSlopeProjection.same_anchor_span
#print axioms Collatz.LargestSlopeProjection.integer_record_census
