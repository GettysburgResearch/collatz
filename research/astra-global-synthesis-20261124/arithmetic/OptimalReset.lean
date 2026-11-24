import Std

namespace Collatz.OptimalReset

/-- Finite arithmetic at a corrected clock two. The incoming clock one
puts n+1 in 3Z, the target is a ternary unit, and a target 8 modulo 9
would have legal unit predecessor clock one. The rational deficit bound
is kept in its integer form. -/
theorem paid_edge (n y : Int) (previous : 3 ∣ n+1)
    (unitTarget : y % 3 ≠ 0) (noShort : y % 9 ≠ 8)
    (lo : -54 ≤ 11 * (3*(n+1)-4*(y+1)))
    (hi : 11 * (3*(n+1)-4*(y+1)) ≤ 32) (oddN : n % 2 = 1) :
    3*n+1=4*y := by
  obtain ⟨h,hh⟩ := previous
  let q := 3*(n+1)-4*(y+1)
  let w := 7*h-3*(y+1)
  have hform : y = 9*w-7*q-1 := by dsimp [w,q]; omega
  have hq : q = -4 ∨ q = -2 ∨ q = 0 ∨ q = 2 := by dsimp [q]; omega
  rcases hq with hq | hq | hq | hq
  · rw [hq] at hform; omega
  · dsimp [q] at hq; omega
  · rw [hq] at hform; omega
  · rw [hq] at hform; omega

/-- A genuine odd clock-one edge supplies its successor's exact residue. -/
theorem one_edge_next (x n : Nat) (h : 2*n=3*x+1) (hx : x%2=1) :
    3 ∣ n+1 := by
  refine ⟨(x+1)/2, ?_⟩
  omega

/-- At a target 8 mod 9 the clock-one inverse is an odd ternary unit. -/
theorem inverse_one_eight (y : Nat) (h : y%9=8) (hy : y%2=1) :
    ∃ u : Nat, 3*u+1=2*y ∧ u%2=1 ∧ u%3≠0 := by
  refine ⟨(2*y-1)/3, ?_⟩
  omega

#print axioms paid_edge
#print axioms one_edge_next
#print axioms inverse_one_eight
end Collatz.OptimalReset
