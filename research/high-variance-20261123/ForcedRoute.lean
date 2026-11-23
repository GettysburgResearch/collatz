import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Forced cap-four inverse routes at every finite horizon

The edges retain positive odd ordinary states prime to three.  For every
supplied depth B the explicit positive source 2 * 3^(B+2) - 1 has only
unit-preserving gap-one choices through that depth, and no route through
that depth reaches 7 modulo 729.  Sources vary with B.  No fixed positive
all-time avoider is asserted.
-/

namespace CollatzShell.ForcedRoute

set_option autoImplicit false

/-- An exact inverse equation, with exponent cap four and a positive odd
unit output. The input is not separately guarded here; the constructed
routes below prove positivity, oddness and unit status at every vertex. -/
def Edge (a x y : ℕ) : Prop :=
  1 ≤ a ∧ a ≤ 4 ∧ 0 < y ∧ y % 2 = 1 ∧ y % 3 ≠ 0 ∧
    3 * y + 1 = 2 ^ a * x

/-- A finite actual inverse path; words are in inverse traversal order. -/
inductive Route : ℕ → List ℕ → ℕ → Prop
  | nil (x : ℕ) : Route x [] x
  | cons {a x y z : ℕ} {w : List ℕ} :
      Edge a x y → Route y w z → Route x (a :: w) z

/-- Only the first B+1 entries are used; the subtraction is natural. -/
def value (B i : ℕ) : ℕ := 9 * (2 ^ (i + 1) * 3 ^ (B - i)) - 1

theorem value_add_one (B i : ℕ) :
    value B i + 1 = 9 * (2 ^ (i + 1) * 3 ^ (B - i)) := by
  have hp : 0 < 2 ^ (i + 1) * 3 ^ (B - i) :=
    Nat.mul_pos (Nat.pow_pos (by decide)) (Nat.pow_pos (by decide))
  unfold value
  omega

theorem value_positive (B i : ℕ) : 0 < value B i := by
  have hp : 0 < 2 ^ (i + 1) * 3 ^ (B - i) :=
    Nat.mul_pos (Nat.pow_pos (by decide)) (Nat.pow_pos (by decide))
  have hv := value_add_one B i
  omega

theorem value_residues (B i : ℕ) :
    value B i % 9 = 8 ∧ value B i % 2 = 1 ∧ value B i % 3 ≠ 0 := by
  have hv := value_add_one B i
  have he : value B i + 1 = 18 * (2 ^ i * 3 ^ (B - i)) := by
    rw [value_add_one, pow_succ]
    ring
  omega

theorem unit_gap_is_one {a x y : ℕ}
    (hx : x % 9 = 8) (h : Edge a x y) : a = 1 := by
  rcases h with ⟨ha, hb, _, _, hy, he⟩
  have hc : a = 1 ∨ a = 2 ∨ a = 3 ∨ a = 4 := by omega
  rcases hc with h1 | h2 | h3 | h4
  · exact h1
  · subst a
    norm_num at he
    omega
  · subst a
    norm_num at he
    omega
  · subst a
    norm_num at he
    omega

theorem value_step {B i : ℕ} (hi : i < B) :
    3 * value B (i + 1) + 1 = 2 * value B i := by
  have hb : B - i = (B - (i + 1)) + 1 := by omega
  have hh : 3 * (value B (i + 1) + 1) = 2 * (value B i + 1) := by
    rw [value_add_one, value_add_one, hb]
    simp only [pow_succ]
    ring
  omega

theorem value_edge {B i : ℕ} (hi : i < B) :
    Edge 1 (value B i) (value B (i + 1)) := by
  refine ⟨by decide, by decide, value_positive B (i + 1),
    (value_residues B (i + 1)).2.1,
    (value_residues B (i + 1)).2.2, ?_⟩
  simpa using value_step hi

theorem value_route {B i k : ℕ} (hi : i + k ≤ B) :
    Route (value B i) (List.replicate k 1) (value B (i + k)) := by
  induction k generalizing i with
  | zero => simpa using Route.nil (value B i)
  | succ k ih =>
    have hib : i < B := by omega
    have ht := ih (i := i + 1) (by omega)
    have ht' : Route (value B (i + 1)) (List.replicate k 1)
        (value B (i + (k + 1))) := by
      simpa only [Nat.add_assoc, Nat.add_comm 1] using ht
    simpa only [List.replicate_succ] using Route.cons (value_edge hib) ht'

theorem value_edge_unique {B i a y : ℕ} (hi : i < B)
    (he : Edge a (value B i) y) :
    a = 1 ∧ y = value B (i + 1) := by
  have ha := unit_gap_is_one (value_residues B i).1 he
  have heq := he.2.2.2.2.2
  have hs := value_step hi
  norm_num [ha] at heq
  exact ⟨ha, by omega⟩

theorem route_is_forced {B i z : ℕ} {w : List ℕ}
    (hi : i + w.length ≤ B) (hr : Route (value B i) w z) :
    w = List.replicate w.length 1 ∧ z = value B (i + w.length) := by
  induction w generalizing i z with
  | nil =>
    cases hr
    simp
  | cons a w ih =>
    cases hr with
    | cons he ht =>
      have hib : i < B := by simp only [List.length_cons] at hi; omega
      obtain ⟨ha, hy⟩ := value_edge_unique hib he
      subst a
      rw [hy] at ht
      have hh := ih (i := i + 1) (by simp only [List.length_cons] at hi; omega) ht
      constructor
      · simp only [List.length_cons, List.replicate_succ]
        exact congrArg (List.cons 1) hh.1
      · simpa only [List.length_cons, Nat.add_assoc, Nat.add_comm 1] using hh.2

theorem no_target_through_depth {B z : ℕ} {w : List ℕ}
    (hlen : w.length ≤ B) (hr : Route (value B 0) w z) : z % 729 ≠ 7 := by
  have hh := route_is_forced (i := 0) (by simpa using hlen) hr
  have hz : z % 9 = 8 := by
    rw [hh.2]
    exact (value_residues B (0 + w.length)).1
  omega

theorem initial_value (B : ℕ) : value B 0 = 2 * 3 ^ (B + 2) - 1 := by
  unfold value
  simp only [Nat.sub_zero, Nat.zero_add, pow_one, pow_add]
  congr 1
  ring

/-- The depth is arbitrary, but the initial ordinary source depends on it. -/
theorem arbitrary_depth_control (B : ℕ) :
    ∃ q : ℕ, q = 2 * 3 ^ (B + 2) - 1 ∧ 0 < q ∧ q % 2 = 1 ∧
      q % 3 ≠ 0 ∧ ∀ (w : List ℕ) (z : ℕ),
        w.length ≤ B → Route q w z → z % 729 ≠ 7 := by
  refine ⟨value B 0, initial_value B, value_positive B 0,
    (value_residues B 0).2.1, (value_residues B 0).2.2, ?_⟩
  intro w z hl hr
  exact no_target_through_depth hl hr

end CollatzShell.ForcedRoute
