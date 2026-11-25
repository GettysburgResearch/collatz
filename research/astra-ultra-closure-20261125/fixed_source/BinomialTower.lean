import TowerDescent
import Mathlib.Data.Fintype.Powerset

/-! Exact binomial tails for the exponent-dependent lower-base budget. -/

namespace TowerDescent
open PhysicalEcho
open scoped BigOperators

private def oddPositions (h n : ℕ) : Finset (Fin h) :=
  Finset.univ.filter (fun j => orbit j.val n % 2 = 1)

private theorem oddPositions_card (h n : ℕ) : (oddPositions h n).card = odds h n := by
  unfold oddPositions
  simp only [Finset.card_eq_sum_ones, Finset.sum_filter]
  induction h generalizing n with
  | zero => simp [odds]
  | succ h ih =>
    rw [Fin.sum_univ_succ]
    change (if n%2=1 then 1 else 0) +
      (∑ i : Fin h, if orbit i.val (step n)%2=1 then 1 else 0) = _
    rw [ih]
    change _ = (if n%2=0 then 0 else 1) + _
    by_cases e : n%2=0 <;> simp [e]

private theorem oddPositions_injective (h offset r : ℕ) :
    Function.Injective (fun i : Fin (2^h) => oddPositions h (3^r*(offset+i.val))) := by
  intro i j same
  apply (code_bijective h offset r).1
  funext k
  apply Fin.ext
  have eq := Finset.ext_iff.mp same k
  simp only [oddPositions, Finset.mem_filter, Finset.mem_univ, true_and] at eq
  change (orbit k.val (3^r*(offset+i.val)))%2 = (orbit k.val (3^r*(offset+j.val)))%2
  omega

/-- All counts at which the elementary endpoint budget can fail at this
particular exponent. Each word of a given count occurs once per block. -/
def possibleCounts (h r : ℕ) : Finset ℕ :=
  (Finset.range (h+1)).filter (fun p => 2^h ≤ 3^p*(3^r+1))

def tailCount (h r : ℕ) : ℕ :=
  ∑ p ∈ possibleCounts h r, Nat.choose h p

theorem failure_tail_bound {h offset r : ℕ} (start : 2^h ≤ offset) :
    (failures h offset r).card ≤ tailCount h r := by
  let family := fun p : ℕ => Finset.powersetCard p (Finset.univ : Finset (Fin h))
  let encode := fun i : Fin (2^h) => oddPositions h (3^r*(offset+i.val))
  calc
    _ ≤ ((possibleCounts h r).biUnion family).card := by
      apply Finset.card_le_card_of_injOn encode ?_ (oddPositions_injective h offset r).injOn
      intro i hi
      let p := odds h (3^r*(offset+i.val))
      have bound := odds_le h (3^r*(offset+i.val))
      have fail := (Finset.mem_filter.mp hi).2
      have cost : 2^h ≤ 3^p*(3^r+1) := by
        by_contra! cheap
        exact (Nat.not_le_of_lt (below_base_of_budget (by omega : 2^h≤offset+i.val)
          (le_refl r) (le_refl p) cheap)) fail
      apply Finset.mem_biUnion.mpr
      refine ⟨p, Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (by dsimp [p]; omega), cost⟩, ?_⟩
      exact Finset.mem_powersetCard.mpr ⟨Finset.subset_univ _, oddPositions_card _ _⟩
    _ ≤ ∑ p ∈ possibleCounts h r, (family p).card := Finset.card_biUnion_le
    _ = _ := by simp [family, tailCount, Finset.card_powersetCard]

theorem simultaneous_tail_bound {h offset R : ℕ} (start : 2^h≤offset) :
    (exceptional h offset R).card ≤ ∑ r ∈ Finset.range (R+1), tailCount h r :=
  Finset.card_biUnion_le.trans (Finset.sum_le_sum (fun _ _ => failure_tail_bound start))

/-- Any strict upper bound for the displayed finite sum proves simultaneous
ordinary descent at some base in every full dyadic block. -/
theorem exists_of_tail {h offset R : ℕ} (start : 2^h≤offset)
    (numerical : (∑ r ∈ Finset.range (R+1), tailCount h r) < 2^h) :
    ∃ i : Fin (2^h), ∀ r ≤ R, ∃ b : ℕ, 0<b ∧ b<offset+i.val ∧
      orbit h (3^r*(offset+i.val))=orbit 0 (3^0*b) := by
  have card := (simultaneous_tail_bound start).trans_lt numerical
  have outside : ∃ i : Fin (2^h), i ∉ exceptional h offset R := by
    by_contra! all
    rw [Finset.eq_univ_of_forall all, Finset.card_univ, Fintype.card_fin] at card
    exact Nat.lt_irrefl _ card
  obtain ⟨i,hi⟩ := outside
  exact ⟨i, good_block_merger (lt_of_lt_of_le (by positivity : 0<2^h) start) hi⟩

/-- The bases in a fixed odd residue class modulo six. In particular, taking
the starting residue 1 or 5 restricts every candidate to a unit at 2 and 3. -/
def rayFailures (l a r : ℕ) : Finset (Fin (2^l)) :=
  Finset.univ.filter (fun i => a+6*i.val ≤ orbit (l+1) (3^r*(a+6*i.val)))

def rayExceptional (l a R : ℕ) : Finset (Fin (2^l)) :=
  (Finset.range (R+1)).biUnion (rayFailures l a)

def rayTail (l r : ℕ) : ℕ :=
  ∑ q ∈ (Finset.range (l+1)).filter (fun q => 2^(l+1) ≤ 3^(q+1)*(3^r+1)), Nat.choose l q

private theorem ray_odd (a r i : ℕ) (odd : a%2=1) : (3^r*(a+6*i))%2=1 := by
  have h : (3^r)%2=1 := by
    induction r with
    | zero => decide
    | succ r ih => rw [pow_succ,Nat.mul_mod,ih]
  rw [Nat.mul_mod, h, show (a+6*i)%2=1 by omega]

private theorem ray_injective (l a r : ℕ) (odd : a%2=1) :
    Function.Injective (fun i : Fin (2^l) => oddPositions l (step (3^r*(a+6*i.val)))) := by
  intro i j same
  have ag : agree (l+1) (3^r*(a+6*i.val)) (3^r*(a+6*j.val)) := by
    intro k hk
    cases k with
    | zero => exact (ray_odd a r i.val odd).trans (ray_odd a r j.val odd).symm
    | succ k =>
      have eq := Finset.ext_iff.mp same ⟨k, by omega⟩
      simp only [oddPositions, Finset.mem_filter, Finset.mem_univ, true_and] at eq
      change (orbit k (step (3^r*(a+6*i.val))))%2 = (orbit k (step (3^r*(a+6*j.val))))%2
      omega
  have hc : Nat.Coprime (2^(l+1)) (3^r) :=
    ((show Nat.Coprime 2 3 by decide).pow_left _).pow_right _
  have e := Nat.ModEq.add_left_cancel' a
    (Nat.ModEq.cancel_left_of_coprime hc (agree_congruent (l+1) _ _ ag))
  rw [show 6*i.val=2*(3*i.val) by ring, show 6*j.val=2*(3*j.val) by ring, pow_succ'] at e
  have f := Nat.ModEq.mul_left_cancel' (by decide : 2≠0) e
  have hc' : Nat.Coprime (2^l) 3 := (show Nat.Coprime 2 3 by decide).pow_left _
  exact Fin.ext ((Nat.ModEq.cancel_left_of_coprime hc' f).eq_of_lt_of_lt i.isLt j.isLt)

theorem ray_failure_bound {l a r : ℕ} (start : 2^(l+1)≤a) (odd : a%2=1) :
    (rayFailures l a r).card ≤ rayTail l r := by
  let counts := (Finset.range (l+1)).filter (fun q => 2^(l+1) ≤ 3^(q+1)*(3^r+1))
  let family := fun q : ℕ => Finset.powersetCard q (Finset.univ : Finset (Fin l))
  let encode := fun i : Fin (2^l) => oddPositions l (step (3^r*(a+6*i.val)))
  calc
    _ ≤ (counts.biUnion family).card := by
      apply Finset.card_le_card_of_injOn encode ?_ (ray_injective l a r odd).injOn
      intro i hi
      let n := 3^r*(a+6*i.val)
      let q := odds l (step n)
      have parity : n%2=1 := ray_odd a r i.val odd
      have ord : odds (l+1) n=q+1 := by
        change (if n%2=0 then 0 else 1) + q = q+1
        simp [parity, Nat.add_comm]
      have fail := (Finset.mem_filter.mp hi).2
      have cost : 2^(l+1) ≤ 3^(q+1)*(3^r+1) := by
        by_contra! cheap
        exact (Nat.not_le_of_lt (below_base_of_budget (by omega : 2^(l+1)≤a+6*i.val)
          (le_refl r) ord.le cheap)) fail
      apply Finset.mem_biUnion.mpr
      refine ⟨q, Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (Nat.lt_succ_of_le (odds_le _ _)), cost⟩, ?_⟩
      exact Finset.mem_powersetCard.mpr ⟨Finset.subset_univ _, oddPositions_card _ _⟩
    _ ≤ ∑ q ∈ counts, (family q).card := Finset.card_biUnion_le
    _ = _ := by simp [family, counts, rayTail, Finset.card_powersetCard]

theorem ray_simultaneous_bound {l a R : ℕ} (start : 2^(l+1)≤a) (odd : a%2=1) :
    (rayExceptional l a R).card ≤ ∑ r ∈ Finset.range (R+1), rayTail l r :=
  Finset.card_biUnion_le.trans (Finset.sum_le_sum (fun _ _ => ray_failure_bound start odd))

theorem ray_exists_of_tail {l a R : ℕ} (start : 2^(l+1)≤a) (odd : a%2=1)
    (numerical : (∑ r ∈ Finset.range (R+1), rayTail l r) < 2^l) :
    ∃ i : Fin (2^l), ∀ r ≤ R,
      0<orbit (l+1) (3^r*(a+6*i.val)) ∧ orbit (l+1) (3^r*(a+6*i.val))<a+6*i.val := by
  have card := (ray_simultaneous_bound start odd).trans_lt numerical
  have outside : ∃ i : Fin (2^l), i ∉ rayExceptional l a R := by
    by_contra! all
    rw [Finset.eq_univ_of_forall all, Finset.card_univ, Fintype.card_fin] at card
    exact Nat.lt_irrefl _ card
  obtain ⟨i,hi⟩ := outside
  have ha : 0<a := by omega
  refine ⟨i, fun r hr => ⟨orbit_pos _ _ (by positivity), ?_⟩⟩
  by_contra! fail
  apply hi
  exact Finset.mem_biUnion.mpr ⟨r, Finset.mem_range.mpr (by omega), Finset.mem_filter.mpr
    ⟨Finset.mem_univ _,fail⟩⟩

#print axioms ray_failure_bound
#print axioms ray_simultaneous_bound
#print axioms ray_exists_of_tail
#print axioms failure_tail_bound
#print axioms simultaneous_tail_bound
#print axioms exists_of_tail

end TowerDescent
