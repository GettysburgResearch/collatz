import PostWords

/-! Finite ordinary word arithmetic for the chronological cut in SMALL_ANCHOR_WORDS.md.
The analytic Subspace Theorem and the position-group separation are written results.
The projection supplied below is the cleared, exact equality at the selected cut. -/

namespace Collatz.ReciprocalRigidity.ChronologicalAnchor

open RampShadow RampShadow.Postpeak

/-- The fixed-point relation allows both positive and negative rational word anchors. -/
def IsAnchor (w : Word) (c : ℚ) : Prop :=
  ((2 : ℚ)^w.length - 3^(weight w)) * c = (intercept w : ℚ)

/-- The slope after a prefix, inverted to normalize the next affine increment. -/
def scale (p r : ℕ) : ℚ := 2^p / 3^r

theorem scaled_piece {x y : ℤ} {c : ℚ} (w : Word) (p r : ℕ)
    (hword : (2 : ℤ)^w.length*y=3^(weight w)*x+intercept w)
    (hc : IsAnchor w c) :
    scale (p+w.length) (r+weight w) * ((y : ℚ)-c) =
    scale p r * ((x : ℚ)-c) := by
  have hw : (2 : ℚ)^w.length*(y : ℚ)=3^(weight w)*(x : ℚ)+(intercept w : ℚ) := by
    exact_mod_cast hword
  have hlocal : (2 : ℚ)^w.length*((y : ℚ)-c)=3^(weight w)*((x : ℚ)-c) := by
    unfold IsAnchor at hc
    linear_combination hw - hc
  unfold scale
  rw [pow_add, pow_add]
  calc
    2^p * 2^w.length / (3^r * 3^(weight w)) * ((y : ℚ)-c) =
        (2^p / (3^r * 3^(weight w))) * (2^w.length * ((y : ℚ)-c)) := by ring
    _ = (2^p / (3^r * 3^(weight w))) * (3^(weight w) * ((x : ℚ)-c)) := by rw [hlocal]
    _ = 2^p / 3^r * ((x : ℚ)-c) := by field_simp

/-- Projecting the initial segment's exact normalization onto the low positions
identifies the actual boundary value with the crossing piece's rational anchor.
Integrality of the resulting fixed word equation realizes every physical parity. -/
theorem projected_prefix_returns {x boundary : ℤ} {c : ℚ} (initial crossing : Word)
    (hprefix : (2 : ℤ)^initial.length*boundary=3^(weight initial)*x+intercept initial)
    (hprojected : (3 : ℚ)^(weight initial)*(x : ℚ)+(intercept initial : ℚ)=
      2^initial.length*c)
    (hc : IsAnchor crossing c) :
    (boundary : ℚ)=c ∧ Walk crossing.length (weight crossing) boundary boundary := by
  have hp : (2 : ℚ)^initial.length*(boundary : ℚ)=
      3^(weight initial)*(x : ℚ)+(intercept initial : ℚ) := by exact_mod_cast hprefix
  have heq : (boundary : ℚ)=c := by
    apply mul_left_cancel₀ (show (2 : ℚ)^initial.length ≠ 0 by positivity)
    exact hp.trans hprojected
  refine ⟨heq, walk_of_word crossing boundary boundary ?_⟩
  have hr : (2 : ℚ)^crossing.length*(boundary : ℚ)=
      3^(weight crossing)*(boundary : ℚ)+(intercept crossing : ℚ) := by
    unfold IsAnchor at hc
    rw [← heq] at hc
    linear_combination hc
  exact_mod_cast hr

#print axioms scaled_piece
#print axioms projected_prefix_returns

end Collatz.ReciprocalRigidity.ChronologicalAnchor
