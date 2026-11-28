import Mathlib.Tactic

namespace Collatz.OrdinaryMerge

private theorem fourPower {j : ℕ} : ∃ z : ℕ, 4^j = 3*z+1 := by
  induction j with
  | zero => exact ⟨0, rfl⟩
  | succ j ih =>
    obtain ⟨z, hz⟩ := ih
    exact ⟨4*z+1, by rw [pow_succ, hz]; ring⟩

/-- All ordinary positive predecessors of one fixed output above a given exponent
are its explicit siblings. Both affine constants are the ordinary integer one. -/
theorem orderedSiblings {m n y a e : ℕ} (hae : a ≤ e)
    (hm : 3*m+1=2^a*y) (hn : 3*n+1=2^e*y) :
    ∃ j : ℕ, e=a+2*j ∧ n=4^j*m+(4^j-1)/3 := by
  obtain ⟨d, hd⟩ := Nat.exists_eq_add_of_le hae
  obtain ⟨z, hz⟩ := fourPower (j := d/2)
  have hscale : 3*n+1=2^d*(3*m+1) := by
    rw [hn, hd, pow_add, hm]
    ring
  by_cases hEven : d=2*(d/2)
  · have hs : (2:ℕ)^d=4^(d/2) := by
      calc
        2^d = 2^(2*(d/2)) := congrArg (fun k : ℕ => (2:ℕ)^k) hEven
        _ = 4^(d/2) := pow_mul (2:ℕ) 2 (d/2)
    have hlin : 3*n+1=3*(4^(d/2)*m+z)+1 := by
      calc
        3*n+1 = 4^(d/2)*(3*m+1) := hscale.trans (by rw [hs])
        _ = 3*(4^(d/2)*m+z)+1 := by rw [hz]; ring
    have hdiv : (4^(d/2)-1)/3=z := by rw [hz]; omega
    exact ⟨d/2, by omega, by omega⟩
  · have hOdd : d=2*(d/2)+1 := by omega
    have hs : (2:ℕ)^d=2*4^(d/2) := by
      calc
        2^d = 2^(2*(d/2)+1) := congrArg (fun k : ℕ => (2:ℕ)^k) hOdd
        _ = 2*4^(d/2) := by rw [pow_succ, pow_mul]; exact Nat.mul_comm _ _
    have hbad : 3*n+1=3*(6*z*m+2*z+2*m)+2 := by
      calc
        3*n+1 = 2*4^(d/2)*(3*m+1) := hscale.trans (by rw [hs])
        _ = 3*(6*z*m+2*z+2*m)+2 := by rw [hz]; ring
    omega

/-- A reference middle-branch parent (3n>N) meeting the actual ordinary
output from (m≤N) has no smaller exponent. Its synchronized source lift
is at or above the true lift. The conclusion retains the exact sibling. -/
theorem noNegativeMeeting {N m n y a e : ℕ} (hmN : m≤N) (hNn : N<3*n)
    (hm : 3*m+1=2^a*y) (hn : 3*n+1=2^e*y) :
    a≤e ∧ ∃ j : ℕ, e=a+2*j ∧ n=4^j*m+(4^j-1)/3 ∧ 4^j*m≤n := by
  have hae : a≤e := by
    by_contra h
    obtain ⟨j, hj, hsource⟩ := orderedSiblings (by omega : e≤a) hn hm
    have hj1 : 1≤j := by omega
    have hpow : 4≤(4:ℕ)^j := by
      simpa using (Nat.pow_le_pow_right (by decide : 0<4) hj1)
    have hb := Nat.mul_le_mul_right n hpow
    omega
  obtain ⟨j, he, hsource⟩ := orderedSiblings hae hm hn
  exact ⟨hae, j, he, hsource, by omega⟩

#print axioms orderedSiblings
#print axioms noNegativeMeeting

end Collatz.OrdinaryMerge
