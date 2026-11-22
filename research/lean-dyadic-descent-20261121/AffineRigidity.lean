import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Module.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Basic.Real.Basic
import Mathlib.Data.Fintype.Card
import Mathlib.Topology.DenseEmbedding
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# The affine translation behind the invariant-label rigidity argument

These are algebraic and finite-dimensional lemmas. They do not assert that
an ordinary Collatz component has a regular extension to a compact group.
The companion written argument keeps that separate analytic obligation.
-/

namespace CollatzShell.AffineRigidity

open Finset

variable {G A : Type*} [AddCommGroup G]

/-- A harmonic real function for the average of two finite permutations is
invariant under each permutation separately. The full quadratic energy is
retained; an average equation alone is not a pointwise branch inequality. -/
theorem finite_harmonic_invariant {I : Type*} [Fintype I]
    (f : I → ℝ) (p q : I → I) (hp : Function.Bijective p)
    (hq : Function.Bijective q)
    (harmonic : ∀ x, 2 * f x = f (p x) + f (q x)) :
    (∀ x, f (p x) = f x) ∧ (∀ x, f (q x) = f x) := by
  have ep : (∑ x, f (p x)^2) = ∑ x, f x^2 := hp.sum_comp (fun x => f x^2)
  have eq : (∑ x, f (q x)^2) = ∑ x, f x^2 := hq.sum_comp (fun x => f x^2)
  have ident (x : I) :
      (f (p x) - f (q x))^2 =
        2 * f (p x)^2 + 2 * f (q x)^2 - 4 * f x^2 := by
    nlinarith [sq_nonneg (f (p x) - f (q x)), harmonic x,
      congrArg (fun z : ℝ => z^2) (harmonic x)]
  have energy : (∑ x, (f (p x) - f (q x))^2) = 0 := by
    simp_rw [ident]
    rw [sum_sub_distrib, sum_add_distrib, ← mul_sum, ← mul_sum,
      ← mul_sum, ep, eq]
    ring
  have same (x : I) : f (p x) = f (q x) := by
    have zero := (sum_eq_zero_iff_of_nonneg
      (fun x (_ : x ∈ (univ : Finset I)) => sq_nonneg (f (p x) - f (q x)))).mp energy
    have e := zero x (mem_univ x)
    nlinarith [sq_nonneg (f (p x) - f (q x))]
  exact ⟨fun x => by linarith [harmonic x, same x],
    fun x => by linarith [harmonic x, same x]⟩

/-- Division by six makes both of the required affine maps onto. -/
theorem affine_surjective (w : G)
    (h6 : Function.Surjective (fun x : G => 6 • x)) :
    Function.Surjective (fun x : G => 2 • x) ∧
    Function.Surjective (fun x : G => 3 • x + w) := by
  constructor
  · intro y
    obtain ⟨x, hx⟩ := h6 y
    refine ⟨3 • x, ?_⟩
    dsimp only at hx ⊢
    calc
      2 • (3 • x) = 6 • x := by abel
      _ = y := hx
  · intro y
    obtain ⟨x, hx⟩ := h6 (y - w)
    refine ⟨2 • x, ?_⟩
    dsimp only at hx ⊢
    calc
      3 • (2 • x) + w = 6 • x + w := by abel
      _ = y := by rw [hx]; abel

/-- The two affine compositions differ by precisely the original translation. -/
theorem adjacent_affine_values (f : G → A) (w : G)
    (hd : ∀ x, f (2 • x) = f x)
    (ht : ∀ x, f (3 • x + w) = f x) (x : G) :
    f (6 • x + w) = f (6 • x + 2 • w) := by
  have left := ht (2 • x)
  have right := hd (3 • x + w)
  have tx := ht x
  have dx := hd x
  have a : 3 • (2 • x) + w = 6 • x + w := by abel
  have b : 2 • (3 • x + w) = 6 • x + 2 • w := by abel
  rw [a, dx] at left
  rw [b, tx] at right
  exact left.trans right.symm

/-- Surjectivity of multiplication by six converts the affine commutator
into invariance under translation by `w`. -/
theorem translation_invariant (f : G → A) (w : G)
    (h6 : Function.Surjective (fun x : G => 6 • x))
    (hd : ∀ x, f (2 • x) = f x)
    (ht : ∀ x, f (3 • x + w) = f x) :
    ∀ x, f (x + w) = f x := by
  intro x
  obtain ⟨y, hy⟩ := h6 (x - w)
  dsimp only at hy
  have a : 6 • y + w = x := by rw [hy]; abel
  have b : 6 • y + 2 • w = x + w := by rw [hy]; abel
  simpa only [a, b] using (adjacent_affine_values f w hd ht y).symm

/-- The exact translation conclusion can be iterated for any finite length. -/
theorem translate_nsmul (f : G → A) (w : G)
    (h : ∀ x, f (x + w) = f x) (x : G) (n : Nat) :
    f (x + n • w) = f x := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [succ_nsmul, ← add_assoc, h, ih]

/-- In a cyclic additive group the two affine invariances force constancy. -/
theorem cyclic_affine_constant (f : G → A) (w : G)
    (h6 : Function.Surjective (fun x : G => 6 • x))
    (gen : ∀ x : G, ∃ n : Nat, n • w = x)
    (hd : ∀ x, f (2 • x) = f x)
    (ht : ∀ x, f (3 • x + w) = f x) :
    ∀ x, f x = f 0 := by
  intro x
  obtain ⟨n, rfl⟩ := gen x
  simpa only [zero_add] using
    translate_nsmul f w (translation_invariant f w h6 hd ht) 0 n

/-- A finite cyclic affine walk has only constant real harmonic functions.
There is no claim of a conductor-independent spectral rate. -/
theorem finite_cyclic_harmonic_constant [Fintype G] (f : G → ℝ) (w : G)
    (h6 : Function.Surjective (fun x : G => 6 • x))
    (gen : ∀ x : G, ∃ n : Nat, n • w = x)
    (harmonic : ∀ x, 2 * f x = f (2 • x) + f (3 • x + w)) :
    ∀ x, f x = f 0 := by
  obtain ⟨h2, h3⟩ := affine_surjective w h6
  obtain ⟨hd, ht⟩ := finite_harmonic_invariant f _ _
    h2.bijective_of_finite h3.bijective_of_finite harmonic
  exact cyclic_affine_constant f w h6 gen hd ht

/-- The same algebra gives continuous rigidity on any group densely generated
by the nonnegative multiples of `w`. No probability law is asserted here. -/
theorem continuous_affine_constant [TopologicalSpace G] [TopologicalSpace A]
    [T2Space A] (f : G → A) (w : G) (hf : Continuous f)
    (h6 : Function.Surjective (fun x : G => 6 • x))
    (gen : DenseRange (fun n : Nat => n • w))
    (hd : ∀ x, f (2 • x) = f x)
    (ht : ∀ x, f (3 • x + w) = f x) :
    f = fun _ => f 0 := by
  apply gen.equalizer hf continuous_const
  funext n
  simpa only [Function.comp_apply, zero_add] using
    translate_nsmul f w (translation_invariant f w h6 hd ht) 0 n

/-- Exact transfer from the shortcut branches to the two forward affine
invariances. `half` is a genuine additive automorphism, not integer division. -/
theorem shortcut_to_affine (f : G → A) (w : G) (half : G ≃+ G)
    (twice : ∀ x, 2 • half x = x)
    (even : ∀ x, f (half x) = f x)
    (odd : ∀ x, f (half (3 • x + w)) = f x) :
    (∀ x, f (2 • x) = f x) ∧ (∀ x, f (3 • x + w) = f x) := by
  constructor
  · intro x
    have e := even (2 • x)
    rw [map_nsmul, twice] at e
    exact e.symm
  · intro x
    exact (even (3 • x + w)).symm.trans (odd x)

/-- The ordinary-looking shortcut branches force translation invariance on
an auxiliary group with actual division by two and six. -/
theorem shortcut_translation (f : G → A) (w : G) (half : G ≃+ G)
    (twice : ∀ x, 2 • half x = x)
    (h6 : Function.Surjective (fun x : G => 6 • x))
    (even : ∀ x, f (half x) = f x)
    (odd : ∀ x, f (half (3 • x + w)) = f x) :
    ∀ x, f (x + w) = f x := by
  obtain ⟨hd, ht⟩ := shortcut_to_affine f w half twice even odd
  exact translation_invariant f w h6 hd ht

/-- Continuous fixed labels on the auxiliary shortcut system are constant
when the ordinary translation has dense nonnegative orbit. -/
theorem continuous_shortcut_constant [TopologicalSpace G] [TopologicalSpace A]
    [T2Space A] (f : G → A) (w : G) (half : G ≃+ G)
    (hf : Continuous f) (twice : ∀ x, 2 • half x = x)
    (h6 : Function.Surjective (fun x : G => 6 • x))
    (gen : DenseRange (fun n : Nat => n • w))
    (even : ∀ x, f (half x) = f x)
    (odd : ∀ x, f (half (3 • x + w)) = f x) :
    f = fun _ => f 0 := by
  obtain ⟨hd, ht⟩ := shortcut_to_affine f w half twice even odd
  exact continuous_affine_constant f w hf h6 gen hd ht

/-- A finite cyclic shortcut walk has only constant real harmonic functions.
The averaging equation is exactly that for `x/2` and `(3*x+w)/2`. -/
theorem finite_shortcut_harmonic_constant [Fintype G] (f : G → ℝ) (w : G)
    (half : G ≃+ G) (twice : ∀ x, 2 • half x = x)
    (h6 : Function.Surjective (fun x : G => 6 • x))
    (gen : ∀ x : G, ∃ n : Nat, n • w = x)
    (harmonic : ∀ x, 2 * f x = f (half x) + f (half (3 • x + w))) :
    ∀ x, f x = f 0 := by
  have triple := (affine_surjective w h6).2.bijective_of_finite
  have oddBij : Function.Bijective (fun x : G => half (3 • x + w)) :=
    half.bijective.comp triple
  obtain ⟨even, odd⟩ := finite_harmonic_invariant f _ _
    half.bijective oddBij harmonic
  obtain ⟨hd, ht⟩ := shortcut_to_affine f w half twice even odd
  exact cyclic_affine_constant f w h6 gen hd ht

end CollatzShell.AffineRigidity
