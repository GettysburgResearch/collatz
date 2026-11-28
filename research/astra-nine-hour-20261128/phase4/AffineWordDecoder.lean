import AffineReachability

namespace Collatz.AffineReachability

/-- The first chronological letter is recovered from the offset's parity.
The final exact verification in `decode` rejects invalid encodings. -/
def decodeRaw : ℕ → ℕ → ℕ → List Bool
  | 0, _, _ => []
  | t+1, a, c =>
    if c % 2 = 0 then false :: decodeRaw t a (c / 2)
    else true :: decodeRaw t (a / 3) ((c - a / 3) / 2)

theorem decodeRaw_length (t a c : ℕ) : (decodeRaw t a c).length = t := by
  induction t generalizing a c with
  | zero => rfl
  | succ t ih =>
    simp only [decodeRaw]
    split <;> simp only [List.length_cons, ih]

theorem decodeRaw_roundtrip (w : List Bool) :
    decodeRaw w.length (scale w) (offset w) = w := by
  induction w with
  | nil => rfl
  | cons b w ih =>
    cases b <;>
      simp [decodeRaw, scale, offset, Nat.add_mod, scale_odd, ih]

/-- A complete decision procedure for the cleared affine code. -/
def decode (t a c : ℕ) : Option (List Bool) :=
  let w := decodeRaw t a c
  if scale w = a ∧ offset w = c then some w else none

theorem decode_roundtrip (w : List Bool) :
    decode w.length (scale w) (offset w) = some w := by
  simp [decode, decodeRaw_roundtrip]

theorem decode_sound {t a c : ℕ} {w : List Bool}
    (h : decode t a c = some w) :
    w.length = t ∧ scale w = a ∧ offset w = c := by
  unfold decode at h
  dsimp only at h
  split at h
  next good =>
    have hw : decodeRaw t a c = w := Option.some.inj h
    subst w
    exact ⟨decodeRaw_length t a c, good⟩
  next => contradiction

theorem decode_complete (t a c : ℕ) :
    (∃ w, decode t a c = some w) ↔
      ∃ w : List Bool, w.length = t ∧ scale w = a ∧ offset w = c := by
  constructor
  · rintro ⟨w, hw⟩
    exact ⟨w, decode_sound hw⟩
  · rintro ⟨w, ht, ha, hc⟩
    refine ⟨w, ?_⟩
    rw [← ht, ← ha, ← hc]
    exact decode_roundtrip w

theorem affine_code_injective {v w : List Bool}
    (ht : v.length = w.length) (ha : scale v = scale w)
    (hc : offset v = offset w) : v = w := by
  have h : decodeRaw v.length (scale v) (offset v) =
      decodeRaw w.length (scale w) (offset w) := by rw [ht, ha, hc]
  simpa only [decodeRaw_roundtrip] using h

end Collatz.AffineReachability
