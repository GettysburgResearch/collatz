import Mathlib.Data.Finset.Prod
import Mathlib.Data.Finset.Card
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp

/-!
# Untrimmed residue collisions at the original ordinary source height

Every ordered collision pair is retained, including the diagonal.  The
injection keeps the first ordinary source and the complete quotient of
the second source.  Equality of the residue and that quotient recovers
the second source exactly.  No stationarity, independence, or discarded
exceptional set is used.

The normalized consequence is the finite inequality
  Col_Q(uniform S) ≤ (H / Q + 1) / |S|.
The analytic comparison with a stationary limit, its convergence rate,
and the Collatz conclusion are not asserted by this module.
-/

namespace CollatzShell.CollisionClosure

set_option autoImplicit false

/-- Ordered pairs of the original sources with the same residue. -/
def orderedResidueCollisions (S : Finset Nat) (Q : Nat) : Finset (Nat × Nat) :=
  (S ×ˢ S).filter (fun p => p.1 % Q = p.2 % Q)

/-- A residue and its full ordinary quotient recover the integer. -/
theorem source_eq_of_residue_and_quotient {a b Q : Nat}
    (hr : a % Q = b % Q) (hq : a / Q = b / Q) : a = b := by
  calc
    a = a % Q + Q * (a / Q) := (Nat.mod_add_div a Q).symm
    _ = b % Q + Q * (b / Q) := by rw [hr, hq]
    _ = b := Nat.mod_add_div b Q

/-- Full pair counting at the actual height.  The denominator `Q` may be
zero in this arithmetic statement; applications use `Q = 3^m > 0`. -/
theorem orderedResidueCollisions_card_le (S : Finset Nat) (Q H : Nat)
    (hh : ∀ n ∈ S, n ≤ H) :
    (orderedResidueCollisions S Q).card ≤ S.card * (H / Q + 1) := by
  have hc : (orderedResidueCollisions S Q).card ≤
      (S ×ˢ Finset.range (H / Q + 1)).card := by
    apply Finset.card_le_card_of_injOn (fun p : Nat × Nat => (p.1, p.2 / Q))
    · intro p hp
      have hpS : p.1 ∈ S ∧ p.2 ∈ S :=
        Finset.mem_product.mp (Finset.mem_filter.mp hp).1
      apply Finset.mem_product.mpr
      refine ⟨hpS.1, Finset.mem_range.mpr ?_⟩
      exact Nat.lt_succ_of_le (Nat.div_le_div_right (hh p.2 hpS.2))
    · intro p hp q hq he
      change (p.1, p.2 / Q) = (q.1, q.2 / Q) at he
      have hfirst : p.1 = q.1 := (Prod.mk.inj he).1
      have hquot : p.2 / Q = q.2 / Q := (Prod.mk.inj he).2
      have hpmod : p.1 % Q = p.2 % Q := (Finset.mem_filter.mp hp).2
      have hqmod : q.1 % Q = q.2 % Q := (Finset.mem_filter.mp hq).2
      apply Prod.ext hfirst
      apply source_eq_of_residue_and_quotient (Q := Q) _ hquot
      calc
        p.2 % Q = p.1 % Q := hpmod.symm
        _ = q.1 % Q := congrArg (fun n : Nat => n % Q) hfirst
        _ = q.2 % Q := hqmod
  simpa only [Finset.card_product, Finset.card_range] using hc

/-- Collision probability of two independent draws from the complete
uniform empirical law on `S`; the path producing `S` need not be random. -/
def residueCollision (S : Finset Nat) (Q : Nat) : ℚ :=
  ((orderedResidueCollisions S Q).card : ℚ) / (S.card : ℚ) ^ 2

theorem residueCollision_le_of_height (S : Finset Nat) (Q H : Nat)
    (hne : S.Nonempty) (hh : ∀ n ∈ S, n ≤ H) :
    residueCollision S Q ≤ ((H / Q + 1 : Nat) : ℚ) / (S.card : ℚ) := by
  have hn : (0 : ℚ) < (S.card : ℚ) := by
    exact_mod_cast Finset.card_pos.mpr hne
  have hc : ((orderedResidueCollisions S Q).card : ℚ) ≤
      (S.card : ℚ) * ((H / Q + 1 : Nat) : ℚ) := by
    exact_mod_cast orderedResidueCollisions_card_le S Q H hh
  unfold residueCollision
  calc
    ((orderedResidueCollisions S Q).card : ℚ) / (S.card : ℚ) ^ 2 ≤
        ((S.card : ℚ) * ((H / Q + 1 : Nat) : ℚ)) / (S.card : ℚ) ^ 2 :=
      div_le_div_of_nonneg_right hc (sq_nonneg _)
    _ = ((H / Q + 1 : Nat) : ℚ) / (S.card : ℚ) := by
      field_simp

/-- Below the modulus, a collision pair is exactly an ordinary diagonal.
This also displays the unavoidable `1/|S|` sampling contribution. -/
theorem orderedResidueCollisions_eq_diagonal (S : Finset Nat) (Q : Nat)
    (hh : ∀ n ∈ S, n < Q) :
    orderedResidueCollisions S Q = S.diag := by
  ext p
  rcases p with ⟨a, b⟩
  simp only [orderedResidueCollisions, Finset.mem_filter, Finset.mem_product,
    Finset.mem_diag]
  constructor
  · rintro ⟨⟨ha, hb⟩, hr⟩
    have hab : a = b := by
      simpa only [Nat.mod_eq_of_lt (hh a ha), Nat.mod_eq_of_lt (hh b hb)] using hr
    exact ⟨ha, hab⟩
  · rintro ⟨ha, hab⟩
    subst b
    exact ⟨⟨ha, ha⟩, rfl⟩

end CollatzShell.CollisionClosure
