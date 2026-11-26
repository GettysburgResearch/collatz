import CriticalSection

namespace CollatzShell.TernaryStopping

/-- Exact all-odd compression joins a ternary lattice point including the
case in which the last output is even. -/
theorem mesh_orbit (s k : Nat) (hk : 0 < k) :
    orbit s (2^s*k - 1) = 3^s*k - 1 := by
  induction s generalizing k with
  | zero => simp [orbit]
  | succ s ih =>
    have hp : 0 < 2^s*k := Nat.mul_pos (by positivity) hk
    have hs : step (2^(s+1)*k-1) = 2^s*(3*k)-1 := by
      rw [show 2^(s+1)*k=2*(2^s*k) by ring,
          show 2^s*(3*k)=3*(2^s*k) by ring]
      simp only [step]
      split <;> omega
    change orbit s (step (2^(s+1)*k-1)) = _
    rw [hs,ih (3*k) (by omega)]
    congr 1
    ring

/-- Every target has a smaller positive all-odd witness meeting one of its
own forward states iff all positive targets converge. -/
theorem universal_iff_mesh :
    Universal ↔ ∀ q : Nat, 1 < q → ∃ s k : Nat,
      0 < k ∧ 0 < 2^s*k-1 ∧ 2^s*k-1 < q ∧ Hits q (3^s*k-1) := by
  constructor
  · intro all q hq
    exact ⟨0,2,by decide,by decide,by simpa using hq,by simpa [Hits,Basin] using all q (by omega)⟩
  · intro test q
    induction q using Nat.strong_induction_on with
    | h q ih =>
      intro hpos
      by_cases base : q = 1
      · exact ⟨0,by simp [orbit,base]⟩
      obtain ⟨s,k,hk,positive,lower,join⟩ := test q (by omega)
      have small := ih (2^s*k-1) lower positive
      have bridge : Hits (2^s*k-1) (3^s*k-1) := ⟨s,mesh_orbit s k hk⟩
      exact (basin_at_hit join).mpr ((basin_at_hit bridge).mp small)

#print axioms mesh_orbit
#print axioms universal_iff_mesh
end CollatzShell.TernaryStopping
