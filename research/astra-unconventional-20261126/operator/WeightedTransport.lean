import Mathlib.LinearAlgebra.Finsupp.LinearCombination
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Algebra.Module.BigOperators
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-! Finite rational witnesses for weighted transport on the positive shortcut graph. -/

namespace Collatz.WeightedTransport

set_option autoImplicit false

variable {α : Type*}

noncomputable def atom (x : α) : α →₀ ℚ := Finsupp.single x 1

noncomputable def push (f : α → α) (w : α → ℚ) : (α →₀ ℚ) →ₗ[ℚ] (α →₀ ℚ) :=
  Finsupp.linearCombination ℚ (fun x => w x • atom (f x))

noncomputable def boundary (f : α → α) (w : α → ℚ) : (α →₀ ℚ) →ₗ[ℚ] (α →₀ ℚ) :=
  LinearMap.id - push f w

@[simp] theorem boundary_atom (f : α → α) (w : α → ℚ) (x : α) :
    boundary f w (atom x) = atom x - w x • atom (f x) := by
  simp [boundary, push, atom, Finsupp.linearCombination_single]

def product (f : α → α) (w : α → ℚ) : ℕ → α → ℚ
  | 0, _ => 1
  | n + 1, x => w x * product f w n (f x)

/-- This finite edge chain carries the initial unit charge through exactly `n` steps. -/
noncomputable def pathChain (f : α → α) (w : α → ℚ) : ℕ → α → (α →₀ ℚ)
  | 0, _ => 0
  | n + 1, x => atom x + w x • pathChain f w n (f x)

theorem path_boundary (f : α → α) (w : α → ℚ) (n : ℕ) (x : α) :
    boundary f w (pathChain f w n x) = atom x - product f w n x • atom (f^[n] x) := by
  induction n generalizing x with
  | zero => simp [pathChain, product]
  | succ n ih =>
    simp only [pathChain, product, map_add, map_smul, boundary_atom, ih,
      Function.iterate_succ_apply, smul_sub, smul_smul]
    abel

/-- A finite family reaching one vertex with cancelling arrivals has an explicit primitive. -/
theorem finite_collision {ι : Type*} (f : α → α) (w : α → ℚ) (sources : Finset ι)
    (x : ι → α) (k : ι → ℕ) (c : ι → ℚ) (v : α)
    (arrives : ∀ i ∈ sources, f^[k i] (x i) = v)
    (cancels : ∑ i ∈ sources, c i * product f w (k i) (x i) = 0) :
    boundary f w (∑ i ∈ sources, c i • pathChain f w (k i) (x i)) =
      ∑ i ∈ sources, c i • atom (x i) := by
  classical
  simp only [map_sum, map_smul, path_boundary, smul_sub, smul_smul, Finset.sum_sub_distrib]
  have heq : (∑ i ∈ sources, (c i * product f w (k i) (x i)) • atom (f^[k i] (x i))) =
      (∑ i ∈ sources, c i * product f w (k i) (x i)) • atom v := by
    rw [Finset.sum_smul]
    exact Finset.sum_congr rfl fun i hi => by rw [arrives i hi]
  rw [heq, cancels, zero_smul, sub_zero]

/-- One full circuit with product different from one has an explicit finite inverse. -/
theorem cycle_primitive (f : α → α) (w : α → ℚ) {p : ℕ} {v : α}
    (returns : f^[p] v = v) (contracts : product f w p v ≠ 1) :
    boundary f w ((1 - product f w p v)⁻¹ • pathChain f w p v) = atom v := by
  rw [map_smul, path_boundary, returns]
  have hne : 1 - product f w p v ≠ 0 := sub_ne_zero.mpr (Ne.symm contracts)
  rw [show atom v - product f w p v • atom v = (1 - product f w p v) • atom v by
    rw [sub_smul, one_smul]]
  exact inv_smul_smul₀ hne _

def Hits (f : α → α) (x y : α) : Prop := ∃ k : ℕ, f^[k] x = y

def Meets (f : α → α) (x a : α) : Prop := ∃ i j : ℕ, f^[i] x = f^[j] a

/-- An initial source belongs to the entire sufficiently late tail exactly when it meets it. -/
theorem eventual_hits (f : α → α) (x a : α) :
    ∃ N, ∀ n ≥ N, Hits f x (f^[n] a) ↔ Meets f x a := by
  by_cases h : Meets f x a
  · obtain ⟨i, j, hij⟩ := h
    refine ⟨j, ?_⟩
    intro n hn
    constructor
    · intro _
      exact ⟨i, j, hij⟩
    · intro _
      obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hn
      refine ⟨d + i, ?_⟩
      rw [Function.iterate_add_apply, hij, Nat.add_comm j d, Function.iterate_add_apply]
  · refine ⟨0, ?_⟩
    intro n _
    exact ⟨fun ⟨k, hk⟩ => ⟨k, n, hk⟩, fun ha => (h ha).elim⟩

/-- The concrete nonaccelerated map is the shortcut map, with one division in an odd step. -/
def shortcut (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

def distortion (x : ℕ) : ℚ := if x % 2 = 0 then 1 else (3 * (x : ℚ)) / (3 * x + 1)

private theorem shortcut_pos {x : ℕ} (hx : 0 < x) : 0 < shortcut x := by
  unfold shortcut
  split <;> omega

private theorem distortion_bounds {x : ℕ} (hx : 0 < x) :
    0 < distortion x ∧ distortion x ≤ 1 := by
  unfold distortion
  split
  · exact ⟨by decide, le_rfl⟩
  · have hq : (0 : ℚ) < x := by exact_mod_cast hx
    have hd : 0 < 3 * (x : ℚ) + 1 := by linarith
    exact ⟨div_pos (by linarith) hd, (div_le_one₀ hd).mpr (by linarith)⟩

private theorem product_bounds (k : ℕ) {x : ℕ} (hx : 0 < x) :
    0 < product shortcut distortion k x ∧ product shortcut distortion k x ≤ 1 := by
  induction k generalizing x with
  | zero => simp [product]
  | succ k ih =>
    obtain ⟨hd, hd1⟩ := distortion_bounds hx
    obtain ⟨hp, hp1⟩ := ih (shortcut_pos hx)
    exact ⟨mul_pos hd hp, le_trans (mul_le_mul_of_nonneg_right hd1 hp.le) (by simpa using hp1)⟩

private theorem progress_if_product_one (k : ℕ) {x : ℕ} (hx : 0 < x)
    (hw : product shortcut distortion k x = 1) :
    shortcut^[k] x ≤ x ∧ (0 < k → shortcut^[k] x < x) := by
  induction k generalizing x with
  | zero => simp
  | succ k ih =>
    obtain ⟨hp, hp1⟩ := product_bounds k (shortcut_pos hx)
    obtain ⟨hd, hd1⟩ := distortion_bounds hx
    change distortion x * product shortcut distortion k (shortcut x) = 1 at hw
    have he : distortion x = 1 := by nlinarith
    have htail : product shortcut distortion k (shortcut x) = 1 := by simpa [he] using hw
    have heven : x % 2 = 0 := by
      by_contra h
      have hq : (0 : ℚ) < x := by exact_mod_cast hx
      have hlt : distortion x < 1 := by
        simp [distortion, h]
        exact (div_lt_one₀ (by linarith : (0 : ℚ) < 3 * x + 1)).mpr (by linarith)
      exact (ne_of_lt hlt) he
    have hxlt : shortcut x < x := by
      simp only [shortcut, heven, ↓reduceIte]
      exact Nat.div_lt_self hx (by decide)
    have hfinal := lt_of_le_of_lt (ih (shortcut_pos hx) htail).1 hxlt
    simpa only [Function.iterate_succ_apply] using And.intro hfinal.le (fun _ => hfinal)

theorem positive_cycle_contracts {v p : ℕ} (hv : 0 < v) (hp : 0 < p)
    (returns : shortcut^[p] v = v) : product shortcut distortion p v < 1 := by
  apply lt_of_le_of_ne (product_bounds p hv).2
  intro he
  have hlt := (progress_if_product_one p hv he).2 hp
  rw [returns] at hlt
  exact (Nat.lt_irrefl _ hlt)

theorem ordinary_cycle_primitive {v p : ℕ} (hv : 0 < v) (hp : 0 < p)
    (returns : shortcut^[p] v = v) :
    boundary shortcut distortion
      ((1 - product shortcut distortion p v)⁻¹ • pathChain shortcut distortion p v) = atom v :=
  cycle_primitive _ _ returns (ne_of_lt (positive_cycle_contracts hv hp returns))

end Collatz.WeightedTransport

#print axioms Collatz.WeightedTransport.boundary_atom
#print axioms Collatz.WeightedTransport.path_boundary
#print axioms Collatz.WeightedTransport.finite_collision
#print axioms Collatz.WeightedTransport.cycle_primitive
#print axioms Collatz.WeightedTransport.eventual_hits
#print axioms Collatz.WeightedTransport.positive_cycle_contracts
#print axioms Collatz.WeightedTransport.ordinary_cycle_primitive
