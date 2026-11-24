import OffsetDescent
import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-! Exact first-entrance and finite group-averaging steps for the ordinary
head-pair grade law. The grid and Diophantine estimates are written arguments. -/

namespace CollatzShell.EntranceGrades

open OffsetDescent

/-- The clock counts inputs strictly before the displayed entrance. -/
def FirstAt (S : Nat → Prop) (n t v : Nat) : Prop :=
  orbit t n = v ∧ S v ∧ ∀ i < t, ¬ S (orbit i n)

private theorem first_after (S : Nat → Prop) (n a t v : Nat)
    (safe : ∀ i < a, ¬S (orbit i n)) :
    FirstAt S n (a+t) v ↔ FirstAt S (orbit a n) t v := by
  simp only [FirstAt, orbit_add]
  constructor
  · rintro ⟨hit, mem, earliest⟩
    refine ⟨hit, mem, ?_⟩
    intro i hi
    simpa only [orbit_add] using earliest (a+i) (by omega)
  · rintro ⟨hit, mem, earliest⟩
    refine ⟨hit, mem, ?_⟩
    intro i hi
    by_cases before : i<a
    · exact safe i before
    · obtain ⟨j,rfl⟩ := Nat.exists_eq_add_of_le (by omega : a≤i)
      rw [orbit_add]
      exact earliest j (by omega)

/-- An entrance set below a physical floor cannot be hit in this prefix. -/
theorem safe_prefix {n h Y : Nat} (floor : 2^h*Y<n) (S : Nat → Prop)
    (bounded : ∀ z, S z → z≤Y) : ∀ i ≤ h, ¬ S (orbit i n) := by
  intro i hi mem
  have lower := linear_lower i n
  have pos : 1 ≤ 3^(oddCount i n) := Nat.one_le_pow _ _ (by decide)
  have src : n ≤ 3^(oddCount i n)*n := by
    simpa using Nat.mul_le_mul_right n pos
  have cap : 2^i*orbit i n ≤ 2^h*Y :=
    Nat.mul_le_mul (Nat.pow_le_pow_right (by decide) hi) (bounded _ mem)
  omega

/-- A literal unequal-clock fusion before either entrance preserves the exact
landing state and transfers the two odd counts with only their prefix shift. -/
theorem first_transfer (S : Nat → Prop) {n m a b : Nat}
    (fusion : orbit a n = orbit b m) (left : ∀ i<a, ¬ S (orbit i n))
    (right : ∀ i<b, ¬ S (orbit i m)) (t v : Nat) :
    (FirstAt S n (a+t) v ↔ FirstAt S m (b+t) v) ∧
    (oddCount (a+t) n : Int) - oddCount (b+t) m =
      (oddCount a n : Int) - oddCount b m := by
  constructor
  · rw [first_after S n a t v left, first_after S m b t v right, fusion]
  · rw [oddCount_add,oddCount_add,fusion]
    omega

/-- The same fusion preserves the symbol for a path with no finite entrance. -/
theorem no_entrance_transfer (S : Nat → Prop) {n m a b : Nat}
    (fusion : orbit a n = orbit b m) (left : ∀ i<a, ¬ S (orbit i n))
    (right : ∀ i<b, ¬ S (orbit i m)) :
    (∀ i, ¬S (orbit i n)) ↔ (∀ j, ¬S (orbit j m)) := by
  constructor
  · intro never j
    by_cases hj : j<b
    · exact right j hj
    · obtain ⟨t,rfl⟩ := Nat.exists_eq_add_of_le (by omega : b≤j)
      rw [orbit_add,←fusion,←orbit_add]
      exact never _
  · intro never i
    by_cases hi : i<a
    · exact left i hi
    · obtain ⟨t,rfl⟩ := Nat.exists_eq_add_of_le (by omega : a≤i)
      rw [orbit_add,fusion,←orbit_add]
      exact never _

open scoped BigOperators

/-- Uniform variation control for *every* group translation averages to a
product law with the original retained-label marginal, with no factor equal
to the number of modular bins after normalization by the group order. -/
theorem translate_average_l1 {K G : Type*} [Fintype K] [Fintype G] [AddGroup G]
    (mass : K → G → ℝ) (E : ℝ)
    (translation : ∀ g : G, ∑ k, ∑ x, |mass k x - mass k (x+g)| ≤ E) :
    ∑ k, ∑ x, |(Fintype.card G : ℝ) * mass k x - ∑ y, mass k y| ≤
      (Fintype.card G : ℝ) * E := by
  classical
  have point (k : K) (x : G) :
      |(Fintype.card G : ℝ) * mass k x - ∑ y, mass k y| ≤
        ∑ g, |mass k x - mass k (x+g)| := by
    have reindex : (∑ g, mass k (x+g)) = ∑ y, mass k y :=
      Fintype.sum_equiv (Equiv.addLeft x) _ _ (fun _ => rfl)
    calc
      _ = |∑ g : G, (mass k x - mass k (x+g))| := by
        rw [Finset.sum_sub_distrib,reindex]
        simp
      _ ≤ _ := Finset.abs_sum_le_sum_abs _ _
  calc
    _ ≤ ∑ k, ∑ x, ∑ g, |mass k x - mass k (x+g)| :=
      Finset.sum_le_sum fun k _ => Finset.sum_le_sum fun x _ => point k x
    _ = ∑ g, ∑ k, ∑ x, |mass k x - mass k (x+g)| := by
      simp_rw [Finset.sum_comm (s:=Finset.univ) (t:=Finset.univ)
        (f:=fun (x g : G) => |mass _ x - mass _ (x+g)|)]
      exact Finset.sum_comm
    _ ≤ ∑ _g : G, E := Finset.sum_le_sum fun g _ => translation g
    _ = _ := by simp

#print axioms safe_prefix
#print axioms first_transfer
#print axioms no_entrance_transfer
#print axioms translate_average_l1

end CollatzShell.EntranceGrades
