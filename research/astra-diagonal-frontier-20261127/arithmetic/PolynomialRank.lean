import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Roots

namespace Collatz.PolynomialRank

/-- Degree is positive. The nonnegative critical allowance is degree minus one. -/
theorem treeBudget (live : ℕ → ℕ) (critical : ℕ)
    (h0 : live 0 ≤ 1)
    (hstep : ∀ k, live (k + 1) ≤ 2 * live k + critical) (k : ℕ) :
    live k + critical ≤ (critical + 1) * 2 ^ k := by
  induction k with
  | zero => simp; omega
  | succ k ih =>
    rw [pow_succ, ← Nat.mul_assoc]
    have hs := hstep k
    omega

/-- Exception credits never multiply under refinement of a finite collection of nodes. -/
theorem sumCredits {α β : Type*} [DecidableEq β] (parents : Finset α)
    (children : α → Finset β) (credit : β → ℕ) (budget : α → ℕ)
    (h : ∀ a ∈ parents, ∑ b ∈ children a, credit b ≤ budget a) :
    ∑ a ∈ parents, ∑ b ∈ children a, credit b ≤ ∑ a ∈ parents, budget a :=
  Finset.sum_le_sum h

/-- Three lifts, of which two at most are allowed at every uncertified-exception-free node. -/
theorem liveStep (s : Finset ℕ) (children : ℕ → ℕ) (bad : ℕ → Bool)
    (goodStep : ∀ a ∈ s, bad a = false → children a ≤ 2)
    (allStep : ∀ a ∈ s, children a ≤ 3) (D : ℕ)
    (badBudget : (s.filter (fun a => bad a)).card ≤ D) :
    ∑ a ∈ s, children a ≤ 2 * s.card + D := by
  classical
  calc
    ∑ a ∈ s, children a ≤ ∑ a ∈ s, (2 + if bad a then 1 else 0) := by
      apply Finset.sum_le_sum
      intro a ha
      cases h : bad a <;> simp [h, goodStep a ha, allStep a ha]
    _ = 2 * s.card + (s.filter (fun a => bad a)).card := by
      simp [Finset.sum_add_distrib, Nat.mul_comm]
    _ ≤ _ := by omega

/-- A union over all native lowbit tags may be bounded without assuming disjointness. -/
theorem tagBudget {α : Type*} [DecidableEq α] (a b c : Finset α) (B : ℕ)
    (ha : a.card ≤ B) (hb : b.card ≤ B) (hc : c.card ≤ B) :
    ((a ∪ b) ∪ c).card ≤ 3 * B := by
  have h1 := Finset.card_union_le a b
  have h2 := Finset.card_union_le (a ∪ b) c
  omega

/-- Strict dominance of a scaled linear term over all higher divided differences. -/
theorem signedLinearDominance (u rest : ℤ) (h : ¬ 3 ∣ u) (hr : 3 ∣ rest) :
    ¬ 3 ∣ u + rest := by
  intro hsum
  exact h ((dvd_add_left hr).mp hsum)

/-- Newton expansions imply actual integer polynomial agreement on an interval
when every (d+1)-st consecutive difference vanishes there.  This separate
finite calculus interface states the uniqueness step in the recurrence. -/
theorem differencesUnique {A : Type*} [AddCommGroup A] (x y : ℕ → A) (n : ℕ)
    (h0 : x 0 = y 0)
    (hs : ∀ j < n, x (j + 1) - x j = y (j + 1) - y j) :
    ∀ k ≤ n, x k = y k := by
  intro k
  induction k with
  | zero => exact fun _ => h0
  | succ k ih =>
    intro hk
    have hx := ih (by omega)
    have hd := hs k (by omega)
    rwa [hx, sub_left_inj] at hd

/-- Root multiplicities on the three actual trits share the polynomial degree budget. -/
theorem tritRootCredits (Q : Polynomial (ZMod 3)) :
    ∑ e : ZMod 3, Polynomial.rootMultiplicity e Q ≤ Q.natDegree := by
  have h : (∑ e : ZMod 3, Multiset.count e Q.roots) = Q.roots.card :=
    Multiset.sum_count_eq_card (fun _ _ => Finset.mem_univ _)
  simpa only [Polynomial.count_roots] using h.le.trans (Polynomial.card_roots' Q)

/-- The coefficient of the first surviving shifted derivative term controls the
degree after primitive normalization: later indices exceed its valuation. -/
theorem childCoefficientOrder (v m i : ℕ) (hv : v ≤ m) (hi : m < i)
    (coefficientOrder : ℕ) (hc : i ≤ coefficientOrder) :
    v < coefficientOrder := by omega

/-- An m-fold unit difference and a larger stride on integer labels. -/
def diffN (t : ℕ) : ℕ → (ℕ → ℤ) → ℕ → ℤ
  | 0, f, r => f r
  | m + 1, f, r => diffN t m f (r+t) - diffN t m f r

def boxSum (t : ℕ) : ℕ → (ℕ → ℤ) → ℕ → ℤ
  | 0, f, r => f r
  | m + 1, f, r => ∑ i ∈ Finset.range t, boxSum t m f (r+i)

theorem boxSub (t m : ℕ) (f g : ℕ → ℤ) (r : ℕ) :
    boxSum t m (fun i => f i - g i) r = boxSum t m f r - boxSum t m g r := by
  induction m generalizing r with
  | zero => rfl
  | succ m ih =>
    simp only [boxSum, ih, Finset.sum_sub_distrib]

theorem boxShift (t m a : ℕ) (f : ℕ → ℤ) (r : ℕ) :
    boxSum t m (fun i => f (i+a)) r = boxSum t m f (r+a) := by
  induction m generalizing r with
  | zero => rfl
  | succ m ih =>
    simp only [boxSum, ih]
    apply Finset.sum_congr rfl
    intro i _
    congr 1
    omega

theorem unitTelescoping (t : ℕ) (f : ℕ → ℤ) (r : ℕ) :
    ∑ i ∈ Finset.range t, (f (r+i+1)-f (r+i)) = f (r+t)-f r := by
  simpa only [Nat.add_assoc, Nat.add_zero] using Finset.sum_range_sub (fun j => f (r+j)) t

/-- Expansion of a larger-stride m-th difference as the nonnegative-weight
convolution of actual unit m-th differences. -/
theorem largeStride (t m : ℕ) (f : ℕ → ℤ) (r : ℕ) :
    diffN t m f r = boxSum t m (diffN 1 m f) r := by
  induction m generalizing r with
  | zero => rfl
  | succ m ih =>
    simp only [diffN, boxSum]
    rw [ih (r+t), ih r, ← unitTelescoping t (boxSum t m (diffN 1 m f)) r]
    apply Finset.sum_congr rfl
    intro i _
    rw [boxSub, boxShift]

theorem strideUpper (t m : ℕ) (f : ℕ → ℤ) (X : ℤ)
    (hf : ∀ r, |f r| ≤ X) (r : ℕ) : |diffN t m f r| ≤ 2^m*X := by
  induction m generalizing r with
  | zero => simpa [diffN] using hf r
  | succ m ih =>
    calc
      |diffN t (m+1) f r| ≤ |diffN t m f (r+t)| + |diffN t m f r| := abs_sub _ _
      _ ≤ 2^m*X + 2^m*X := add_le_add (ih _) (ih _)
      _ = 2^(m+1)*X := by ring

#print axioms tritRootCredits
#print axioms childCoefficientOrder
#print axioms largeStride
#print axioms strideUpper

#print axioms treeBudget
#print axioms sumCredits
#print axioms liveStep
#print axioms tagBudget
#print axioms signedLinearDominance
#print axioms differencesUnique

end Collatz.PolynomialRank
