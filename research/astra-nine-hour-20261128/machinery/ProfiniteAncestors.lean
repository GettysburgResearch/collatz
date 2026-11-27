import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Push
import Mathlib.Tactic.Ring

namespace AstraNine.ProfiniteAncestors

/-- The two true odd valuation maps on a quotient where two is invertible. -/
def first {q : ℕ} (half x : ZMod q) : ZMod q := (3 * x + 1) * half

def second {q : ℕ} (half x : ZMod q) : ZMod q := (3 * x + 1) * half ^ 2

theorem swap_gain {q : ℕ} (half : ZMod q) (h : 2 * half = 1) (x : ZMod q) :
    first half (second half x) = second half (first half x) + half ^ 2 := by
  unfold first second
  linear_combination -half * h

theorem second_fixes_one {q : ℕ} (half : ZMod q) (h : 2 * half = 1) :
    second half 1 = 1 := by
  unfold second
  linear_combination (2 * half + 1) * h

private theorem first_injective {q : ℕ} (half third : ZMod q)
    (h₂ : 2 * half = 1) (h₃ : 3 * third = 1) :
    Function.Injective (first half) := by
  apply Function.LeftInverse.injective (g := fun x => (2 * x - 1) * third)
  intro x
  unfold first
  linear_combination (3 * x + 1) * third * h₂ + x * h₃

private theorem second_injective {q : ℕ} (half third : ZMod q)
    (h₂ : 2 * half = 1) (h₃ : 3 * third = 1) :
    Function.Injective (second half) := by
  apply Function.LeftInverse.injective (g := fun x => (4 * x - 1) * third)
  intro x
  unfold second
  linear_combination (3 * x + 1) * third * (2 * half + 1) * h₂ + x * h₃

/-- A closed finite subset of the genuine two-letter walk has all residues
as soon as it has one. The proof uses the chronological word swap. -/
theorem closed_fibre_is_all {q : ℕ} [NeZero q] (half third : ZMod q)
    (h₂ : 2 * half = 1) (h₃ : 3 * third = 1)
    (A : Set (ZMod q)) (hne : A.Nonempty)
    (h₁ : ∀ x ∈ A, first half x ∈ A)
    (h₂' : ∀ x ∈ A, second half x ∈ A) :
    ∀ y, y ∈ A := by
  classical
  let back : A → A := fun x =>
    ⟨second half (first half x), h₂' _ (h₁ _ x.property)⟩
  have hinj : Function.Injective back := by
    intro x y h
    have hh : second half (first half x) = second half (first half y) :=
      congrArg Subtype.val h
    exact Subtype.ext (first_injective half third h₂ h₃ (second_injective half third h₂ h₃ hh))
  have honto : Function.Surjective back := Finite.surjective_of_injective hinj
  have hstep (x : ZMod q) (hx : x ∈ A) : x + half ^ 2 ∈ A := by
    obtain ⟨v, hv⟩ := honto ⟨x, hx⟩
    have hh : second half (first half v) = x := congrArg Subtype.val hv
    rw [← hh, ← swap_gain half h₂]
    exact h₁ _ (h₂' _ v.property)
  obtain ⟨x, hx⟩ := hne
  have hprogress (n : ℕ) : x + (n : ZMod q) * half ^ 2 ∈ A := by
    induction n with
    | zero => simpa using hx
    | succ n ih =>
      convert hstep _ ih using 1
      push_cast
      ring
  intro y
  let shift : ZMod q := (y - x) * 4
  have hs := hprogress shift.val
  rw [ZMod.natCast_zmod_val] at hs
  have hfinal : x + shift * half ^ 2 = y := by
    dsimp [shift]
    linear_combination (y - x) * (2 * half + 1) * h₂
  rwa [hfinal] at hs

/-- The hypotheses above hold on every modulus prime to six. -/
theorem every_residue {q : ℕ} [NeZero q] (cop : Nat.Coprime 6 q)
    (A : Set (ZMod q)) (hne : A.Nonempty)
    (h₁ : ∀ x ∈ A, first ((ZMod.unitOfCoprime 2
      (Nat.Coprime.of_dvd_left (by decide : 2 ∣ 6) cop))⁻¹ : (ZMod q)ˣ) x ∈ A)
    (h₂ : ∀ x ∈ A, second ((ZMod.unitOfCoprime 2
      (Nat.Coprime.of_dvd_left (by decide : 2 ∣ 6) cop))⁻¹ : (ZMod q)ˣ) x ∈ A) :
    ∀ y, y ∈ A := by
  let a := ZMod.unitOfCoprime 2 (Nat.Coprime.of_dvd_left (by decide : 2 ∣ 6) cop)
  let b := ZMod.unitOfCoprime 3 (Nat.Coprime.of_dvd_left (by decide : 3 ∣ 6) cop)
  apply closed_fibre_is_all (↑a⁻¹) (↑b⁻¹) _ _ A hne h₁ h₂
  · have ha : (↑a : ZMod q) = 2 := rfl
    rw [← ha]
    exact Units.mul_inv a
  · have hb : (↑b : ZMod q) = 3 := rfl
    rw [← hb]
    exact Units.mul_inv b

end AstraNine.ProfiniteAncestors
