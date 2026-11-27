import GlobalFloor

namespace GoodNeighbors
open GlobalFloor

private theorem upper_equivalence {x y : ℕ} (ox : Odd x) (oy : Odd y)
    (edge : 4*y=3*x+1) : Good (x+1) ↔ Good (y+1) := by
  obtain ⟨a,ha⟩ := ox
  obtain ⟨b,hb⟩ := oy
  let m := x/8
  have xx : x=8*m+1 := by dsimp [m]; omega
  have yy : y=6*m+1 := by omega
  rw [show x+1=2*(4*m+1) by omega,good_even,
    show 4*m+1=2*(2*m)+1 by ring,good_odd,
    show 3*(2*m)+2=y+1 by omega]

/-- Applies to any infinite bounded path satisfying the displayed
hypotheses. No return or initial good neighbor is required. -/
theorem all_upper_neighbors {q : ℕ} (qbig : 3<q)
    (triples : ∀ u>0, u<q → Good (3*u))
    (xs : ℕ → ℕ) (large : ∀ i, 1<xs i) (bounded : ∀ i, xs i<8*q)
    (units : ∀ i, Odd (xs i))
    (edges : ∀ i, 2*xs (i+1)=3*xs i+1 ∨ 4*xs (i+1)=3*xs i+1)
    (i : ℕ) : Good (xs i+1) := by
  suffices all : ∀ m j, xs j=m → Good (xs j+1) by exact all _ i rfl
  intro m
  induction m using Nat.strong_induction_on with
  | h m ih =>
    intro j hj
    rcases edges j with one|two
    · obtain ⟨v,hv⟩ := units (j+1)
      let u := (xs j+1)/4
      have eq : xs j+1=4*u := by dsimp [u]; omega
      have up : 0<u := by have := large j; omega
      have small : 2*u+1<3*q := by have := bounded (j+1); omega
      have gu : Good u := by
        by_contra bad
        have := floor_of_small_triples triples up bad
        omega
      rw [eq,show 4*u=2*(2*u) by ring,good_even,good_even]
      exact gu
    · have dec : xs (j+1)<m := by have := large j; omega
      exact (upper_equivalence (units j) (units (j+1)) two).mpr (ih _ dec (j+1) rfl)

/-- The other affine neighbor descends through a decreasing string of
exponent-two edges to a known good lower neighbor. -/
theorem all_doubled_lower_neighbors (xs : ℕ → ℕ) (large : ∀ i, 1<xs i)
    (lower : ∀ i, Good (xs i-1))
    (edges : ∀ i, 2*xs (i+1)=3*xs i+1 ∨ 4*xs (i+1)=3*xs i+1)
    (i : ℕ) : Good (2*xs i-1) := by
  suffices all : ∀ m j, xs j=m → Good (2*xs j-1) by exact all _ i rfl
  intro m
  induction m using Nat.strong_induction_on with
  | h m ih =>
    intro j hj
    have pos := large j
    rw [show 2*xs j-1=2*(xs j-1)+1 by omega,good_odd]
    rcases edges j with one|two
    · rw [show 3*(xs j-1)+2=2*(xs (j+1)-1) by omega,good_even]
      exact lower _
    · have dec : xs (j+1)<m := by omega
      rw [show 3*(xs j-1)+2=2*(2*xs (j+1)-1) by omega,good_even]
      exact ih _ dec (j+1) rfl

#print axioms all_upper_neighbors
#print axioms all_doubled_lower_neighbors
end GoodNeighbors
