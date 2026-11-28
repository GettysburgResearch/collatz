import Std

/-! Finite kernels for the positive carries and polynomial coefficient cone in
`MERSENNE_ANCHOR.md`. The surrounding Collatz theorem is a written proof. -/
namespace Collatz.MersenneAnchor

/-- One merge advances two equal bits by one place, cyclically. -/
inductive Carries (period : Nat) : Nat → List Nat → List Nat → Prop where
  | done (xs) : Carries period 0 xs xs
  | move {x rest xs ys count}
      (positions : xs.Perm (x :: x :: rest))
      (later : Carries period count (((x + 1) % period) :: rest) ys) :
      Carries period (count + 1) xs ys

theorem Carries.length {k r : Nat} {xs ys : List Nat} (h : Carries k r xs ys) :
    r + ys.length = xs.length := by
  induction h with
  | done xs => simp
  | move hp _ ih =>
    have heq := hp.length_eq
    simp only [List.length_cons] at heq ih
    omega

/-- Every initial bit can be tracked to a surviving bit with at most one
    forward position per merge. -/
theorem Carries.ancestor {k r : Nat} {xs ys : List Nat} (h : Carries k r xs ys) :
    ∀ a ∈ xs, ∃ b ∈ ys, ∃ j ≤ r, b % k = (a + j) % k := by
  induction h with
  | done xs =>
    intro a ha
    exact ⟨a, ha, 0, Nat.le_refl _, by simp⟩
  | @move x rest xs ys r hp _ ih =>
    intro a ha
    have hm := hp.mem_iff.mp ha
    simp only [List.mem_cons, or_self_left] at hm
    rcases hm with same | old
    · subst a
      obtain ⟨b, hb, j, hj, heq⟩ := ih ((x + 1) % k) (by simp)
      refine ⟨b, hb, j + 1, by omega, ?_⟩
      rw [Nat.mod_add_mod] at heq
      simpa only [Nat.add_assoc, Nat.add_comm 1 j] using heq
    · obtain ⟨b, hb, j, hj, heq⟩ := ih a (List.mem_cons_of_mem _ old)
      exact ⟨b, hb, j, by omega, heq⟩

/-- The pairs below the leading degree are (degree, cleared coefficient).
    At one half every such coefficient acquires a factor of at least two
    after clearing the leading denominator. -/
def raw (terms : List (Nat × Nat)) : Nat :=
  (terms.map Prod.snd).sum

def shifted (degree : Nat) (terms : List (Nat × Nat)) : Nat :=
  (terms.map fun term => 2 ^ (degree - term.1) * term.2).sum

theorem doubled_lower_mass {degree : Nat} {terms : List (Nat × Nat)}
    (h : ∀ term ∈ terms, term.1 < degree) :
    2 * raw terms ≤ shifted degree terms := by
  induction terms with
  | nil => simp [raw, shifted]
  | cons term rest ih =>
    have hlt : term.1 < degree := h term (by simp)
    have hh := ih (fun u hu => h u (List.mem_cons_of_mem _ hu))
    have hpow : 2 ^ 1 ≤ 2 ^ (degree - term.1) :=
      Nat.pow_le_pow_right (by decide) (by omega)
    have hm := Nat.mul_le_mul_right term.2 hpow
    simp only [raw, shifted, List.map_cons, List.sum_cons] at hh ⊢
    rw [Nat.mul_add]
    exact Nat.add_le_add hm hh

/-- Cleared evaluations P(1)=d=2P(1/2) force degree one and no
    lower coefficient when d is positive and the coefficients have the
    physical endpoint signs. -/
theorem anchored_cone {degree d lead : Nat} {terms : List (Nat × Nat)}
    (hd : 0 < d) (hdeg : 0 < degree)
    (hterms : ∀ term ∈ terms, term.1 < degree)
    (at_one : lead = d + raw terms)
    (at_half : 2 * lead = 2 ^ degree * d + 2 * shifted degree terms) :
    degree = 1 ∧ raw terms = 0 := by
  have hm := doubled_lower_mass hterms
  have hsmall : degree ≤ 1 := by
    apply Classical.byContradiction
    intro hlarge
    have hp : 2 ^ 2 ≤ 2 ^ degree :=
      Nat.pow_le_pow_right (by decide) (by omega)
    have hp' := Nat.mul_le_mul_right d hp
    change 4 * d ≤ 2 ^ degree * d at hp'
    omega
  have heq : degree = 1 := by omega
  subst degree
  simp only [Nat.pow_one] at at_half
  exact ⟨rfl, by omega⟩

end Collatz.MersenneAnchor
