import Mathlib.Data.Finset.Card
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Basic.Real.Basic
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Linarith

/-!
Finite ordinary-source packing for the sibling pressure argument.

The graph theorems retain one deterministic map, one actual forward ray,
and off-ray roots that enter that ray in one step. The packing theorem
retains every source weight above the specified finite cutoff.

The infinite pressure construction, real-power interpolation, zeta tail,
and rearrangement asymptotics are written scope. No predecessor-density
input is used, and no Collatz convergence hypothesis is asserted here.
-/

set_option autoImplicit false

namespace CollatzBasinPacking

def Reaches (f : Nat → Nat) (x y : Nat) : Prop :=
  ∃ k : Nat, (f^[k]) x = y

/-- A smaller positive value cannot occur before the target of a basin minimum.
The hitting witness and the minimum property concern the same original source. -/
theorem descent_forces_earlier_hit (f : Nat → Nat) (m v h : Nat)
    (hit : Reaches f m v)
    (minimum : ∀ n, 0 < n → Reaches f n v → m ≤ n)
    (positive : 0 < (f^[h]) m) (descent : (f^[h]) m < m) :
    ∃ k ≤ h, (f^[k]) m = v := by
  obtain ⟨k, hk⟩ := hit
  by_cases early : k ≤ h
  · exact ⟨k, early, hk⟩
  · have hhk : h ≤ k := by omega
    have suffix : Reaches f ((f^[h]) m) v := by
      refine ⟨k - h, ?_⟩
      rw [← Function.iterate_add_apply]
      simpa [Nat.sub_add_cancel hhk, Nat.add_comm] using hk
    have := minimum ((f^[h]) m) positive suffix
    omega

def shortcut (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

theorem shortcut_positive (n : Nat) (positive : 0 < n) :
    0 < shortcut n := by
  unfold shortcut
  split <;> omega

theorem shortcut_height (n : Nat) :
    2 * (shortcut n + 1) ≤ 3 * (n + 1) := by
  unfold shortcut
  split <;> omega

theorem shortcut_iterate_height (n k : Nat) :
    2 ^ k * ((shortcut^[k]) n + 1) ≤ 3 ^ k * (n + 1) := by
  induction k with
  | zero => simp
  | succ k ih =>
    have step := Nat.mul_le_mul_left (2 ^ k) (shortcut_height ((shortcut^[k]) n))
    have old := Nat.mul_le_mul_left 3 ih
    rw [Function.iterate_succ_apply']
    simp only [pow_succ]
    nlinarith

theorem two_hits_comparable (f : Nat → Nat) (x y z : Nat)
    (hy : Reaches f x y) (hz : Reaches f x z) :
    Reaches f y z ∨ Reaches f z y := by
  obtain ⟨a, ha⟩ := hy
  obtain ⟨b, hb⟩ := hz
  rcases le_total a b with hab | hba
  · left
    refine ⟨b - a, ?_⟩
    rw [← ha, ← Function.iterate_add_apply]
    simpa [Nat.sub_add_cancel hab, Nat.add_comm] using hb
  · right
    refine ⟨a - b, ?_⟩
    rw [← hb, ← Function.iterate_add_apply]
    simpa [Nat.sub_add_cancel hba, Nat.add_comm] using ha

theorem iterate_on_ray (f : Nat → Nat) (q : Nat → Nat)
    (next : ∀ j, f (q j) = q (j + 1)) (a k : Nat) :
    (f^[k]) (q a) = q (a + k) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Function.iterate_succ_apply', ih, next]
    simp [Nat.add_assoc]

theorem off_ray_roots_incomparable {ι : Type*}
    (f : Nat → Nat) (q : Nat → Nat) (v : ι → Nat) (attach : ι → Nat)
    (next : ∀ j, f (q j) = q (j + 1))
    (edge : ∀ i, f (v i) = q (attach i))
    (off : ∀ i j, v i ≠ q j) (inj : Function.Injective v)
    (i j : ι) (hit : Reaches f (v i) (v j)) : i = j := by
  obtain ⟨k, hk⟩ := hit
  cases k with
  | zero => exact inj (by simpa using hk)
  | succ k =>
    rw [Function.iterate_succ_apply, edge,
      iterate_on_ray f q next] at hk
    exact False.elim (off j (attach i + k) hk.symm)

theorem predecessor_roots_unique {ι : Type*}
    (f : Nat → Nat) (q : Nat → Nat) (v : ι → Nat) (attach : ι → Nat)
    (next : ∀ j, f (q j) = q (j + 1))
    (edge : ∀ i, f (v i) = q (attach i))
    (off : ∀ i j, v i ≠ q j) (inj : Function.Injective v)
    (x : Nat) (i j : ι)
    (hi : Reaches f x (v i)) (hj : Reaches f x (v j)) : i = j := by
  rcases two_hits_comparable f x (v i) (v j) hi hj with hij | hji
  · exact off_ray_roots_incomparable f q v attach next edge off inj i j hij
  · exact (off_ray_roots_incomparable f q v attach next edge off inj j i hji).symm

theorem finite_predecessor_basins_disjoint {ι : Type*}
    (f : Nat → Nat) (q : Nat → Nat) (v : ι → Nat) (attach : ι → Nat)
    (next : ∀ j, f (q j) = q (j + 1))
    (edge : ∀ i, f (v i) = q (attach i))
    (off : ∀ i j, v i ≠ q j) (inj : Function.Injective v)
    (B : ι → Finset Nat)
    (realized : ∀ i n, n ∈ B i → Reaches f n (v i)) :
    Pairwise (fun i j => Disjoint (B i) (B j)) := by
  intro i j hij
  apply Finset.disjoint_left.mpr
  intro n hni hnj
  exact hij (predecessor_roots_unique f q v attach next edge off inj
    n i j (realized i n hni) (realized j n hnj))

theorem touched_card_le {ι : Type*} [DecidableEq ι]
    (F : Finset ι) (B : ι → Finset Nat) (low : Finset Nat)
    (disjoint : Set.PairwiseDisjoint (↑F) B) :
    (F.filter (fun i => ¬ Disjoint (B i) low)).card ≤ low.card := by
  classical
  let pick (i : ι) : Nat :=
    if h : ∃ n, n ∈ B i ∧ n ∈ low then Classical.choose h else 0
  have picked : ∀ i ∈ F.filter (fun i => ¬ Disjoint (B i) low),
      pick i ∈ B i ∧ pick i ∈ low := by
    intro i hi
    have hnot := (Finset.mem_filter.mp hi).2
    have hex : ∃ n, n ∈ B i ∧ n ∈ low := by
      by_contra hn
      apply hnot
      apply Finset.disjoint_left.mpr
      intro n hbi hli
      exact hn ⟨n, hbi, hli⟩
    simpa [pick, hex] using Classical.choose_spec hex
  apply Finset.card_le_card_of_injOn pick
  · intro i hi
    exact (picked i hi).2
  · intro i hi j hj heq
    by_contra hij
    have hd := disjoint (Finset.mem_filter.mp hi).1
      (Finset.mem_filter.mp hj).1 hij
    exact Finset.disjoint_left.mp hd (picked i hi).1
      (heq ▸ (picked j hj).1)

theorem untouched_mass_le_tail {ι : Type*} [DecidableEq ι]
    (F : Finset ι) (B : ι → Finset Nat) (low pool : Finset Nat)
    (w : Nat → Real) (nonneg : ∀ n, 0 ≤ w n)
    (disjoint : Set.PairwiseDisjoint (↑F) B)
    (inside : ∀ i ∈ F, B i ⊆ pool) :
    ∑ i ∈ F.filter (fun i => Disjoint (B i) low), ∑ n ∈ B i, w n
      ≤ ∑ n ∈ pool \ low, w n := by
  classical
  let untouched := F.filter (fun i => Disjoint (B i) low)
  have hd : Set.PairwiseDisjoint (↑untouched) B := by
    intro i hi j hj hij
    exact disjoint (Finset.mem_filter.mp hi).1 (Finset.mem_filter.mp hj).1 hij
  have hsub : untouched.biUnion B ⊆ pool \ low := by
    intro n hn
    obtain ⟨i, hi, hni⟩ := Finset.mem_biUnion.mp hn
    have hfi := (Finset.mem_filter.mp hi).1
    have hdi := (Finset.mem_filter.mp hi).2
    refine Finset.mem_sdiff.mpr ⟨inside i hfi hni, ?_⟩
    intro hl
    exact Finset.disjoint_left.mp hdi hni hl
  change (∑ i ∈ untouched, ∑ n ∈ B i, w n) ≤ _
  rw [← Finset.sum_biUnion hd]
  exact Finset.sum_le_sum_of_subset_of_nonneg hsub (fun n _ _ => nonneg n)

/-- The full finite source-cutoff charge. Every omitted ordinary atom is
retained in the right-hand tail. The left uses natural truncated subtraction. -/
theorem finite_source_cutoff_with_capacity {ι : Type*} [DecidableEq ι]
    (F : Finset ι) (B : ι → Finset Nat) (low pool : Finset Nat)
    (w : Nat → Real) (epsilon : Real) (capacity : Nat)
    (nonneg : ∀ n, 0 ≤ w n) (heps : 0 ≤ epsilon)
    (disjoint : Set.PairwiseDisjoint (↑F) B)
    (inside : ∀ i ∈ F, B i ⊆ pool)
    (touched : (F.filter (fun i => ¬ Disjoint (B i) low)).card ≤ capacity)
    (heavy : ∀ i ∈ F, epsilon ≤ ∑ n ∈ B i, w n) :
    ((F.card - capacity : Nat) : Real) * epsilon
      ≤ ∑ n ∈ pool \ low, w n := by
  classical
  let untouched := F.filter (fun i => Disjoint (B i) low)
  have partition := F.card_filter_add_card_filter_not (fun i => Disjoint (B i) low)
  have hc : F.card - capacity ≤ untouched.card := by
    change F.card - capacity ≤ (F.filter (fun i => Disjoint (B i) low)).card
    omega
  have hr : ((F.card - capacity : Nat) : Real) ≤ (untouched.card : Real) :=
    Nat.cast_le.mpr hc
  calc
    _ ≤ (untouched.card : Real) * epsilon := mul_le_mul_of_nonneg_right hr heps
    _ = ∑ i ∈ untouched, epsilon := by simp
    _ ≤ ∑ i ∈ untouched, ∑ n ∈ B i, w n := by
      apply Finset.sum_le_sum
      intro i hi
      exact heavy i (Finset.mem_filter.mp hi).1
    _ ≤ ∑ n ∈ pool \ low, w n :=
      untouched_mass_le_tail F B low pool w nonneg disjoint inside

/-- The unconditional finite cutoff, using only one distinct small source
per touched basin. A sharper minimum count enters through the preceding theorem. -/
theorem finite_source_cutoff {ι : Type*} [DecidableEq ι]
    (F : Finset ι) (B : ι → Finset Nat) (low pool : Finset Nat)
    (w : Nat → Real) (epsilon : Real)
    (nonneg : ∀ n, 0 ≤ w n) (heps : 0 ≤ epsilon)
    (disjoint : Set.PairwiseDisjoint (↑F) B)
    (inside : ∀ i ∈ F, B i ⊆ pool)
    (heavy : ∀ i ∈ F, epsilon ≤ ∑ n ∈ B i, w n) :
    ((F.card - low.card : Nat) : Real) * epsilon
      ≤ ∑ n ∈ pool \ low, w n :=
  finite_source_cutoff_with_capacity F B low pool w epsilon low.card
    nonneg heps disjoint inside (touched_card_le F B low disjoint) heavy

#print axioms two_hits_comparable
#print axioms descent_forces_earlier_hit
#print axioms shortcut_positive
#print axioms shortcut_height
#print axioms shortcut_iterate_height
#print axioms iterate_on_ray
#print axioms off_ray_roots_incomparable
#print axioms predecessor_roots_unique
#print axioms finite_predecessor_basins_disjoint
#print axioms touched_card_le
#print axioms untouched_mass_le_tail
#print axioms finite_source_cutoff_with_capacity
#print axioms finite_source_cutoff

end CollatzBasinPacking
