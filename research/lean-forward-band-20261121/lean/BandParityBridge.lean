import BandTransport

/-!
The complementary long-block transfer is exactly the same-source odd psi
comparison from PR 180. The supplied smaller source establishes the target
side of that comparison; it does not lower the query's parity rank.
-/

namespace CollatzShell.BandParityBridge

open BandTransport

/-- The property used in PR 180's `CollatzPsiParity` module, stated with the
ordinary basin interface of the forward-section project. -/
def PsiComparison (n : Nat) : Prop := Basin n ↔ Basin (2*n-1)

def psiRank (n : Nat) : Nat := if n%2=0 then 2*n else n

theorem odd_inverse_lift (m : Nat) (hm : m%2=1) :
    Basin (4*m+1) ↔ Basin m := by
  let t := m/2
  have repr : m=2*t+1 := by dsimp [t]; omega
  have left : orbit 3 (4*m+1)=3*t+2 := by
    rw [repr,show 4*(2*t+1)+1=2^3*t+5 by ring,orbit_shift]
    norm_num [oddCount,orbit,step]
  have right : orbit 1 m=3*t+2 := by
    rw [repr,show 2*t+1=2^1*t+1 by ring,orbit_shift]
    norm_num [oddCount,orbit,step]
  exact (basin_at_hit (show Hits (4*m+1) (3*t+2) from ⟨3,left⟩)).trans
    (basin_at_hit (show Hits m (3*t+2) from ⟨1,right⟩)).symm

theorem half_comparison_is_same_odd_psi (m : Nat) (hm : m%2=1) :
    (Basin m ↔ Basin (2*m+1)) ↔ PsiComparison (2*m+1) := by
  have target : Basin (2*(2*m+1)-1) ↔ Basin m := by
    rw [show 2*(2*m+1)-1=4*m+1 by omega]
    exact odd_inverse_lift m hm
  constructor
  · intro h
    exact h.symm.trans target.symm
  · intro h
    exact target.symm.trans h.symm

private theorem source_pair (r u : Nat) (hr : 0<r) (hu : 0<u) :
    (2^r*u-1)%2=1 ∧
      2^(r+1)*u-1=2*(2^r*u-1)+1 := by
  have pos : 0<2^r*u := by positivity
  have repr : 2^r*u=2*(2^(r-1)*u) := by
    conv_lhs => arg 1; rw [show r=(r-1)+1 by omega,pow_succ]
    ring
  constructor
  · rw [repr]
    have p : 0<2^(r-1)*u := by positivity
    omega
  · rw [show 2^(r+1)*u=2*(2^r*u) by rw [pow_succ]; ring]
    omega

/-- The hard phase's two ordinary sources and its psi target are identified
with the residual pair. No comparison hypothesis is used here. -/
theorem complementary_identifications (r u z : Nat) (hr : 0<r) (hu : 0<u)
    (phase : 3^r*u=4*z+1) :
    (Basin (2^(r+1)*u-1) ↔ Basin (9*z+2)) ∧
    (Basin (2^r*u-1) ↔ Basin z) ∧
    (Basin (2*(2^(r+1)*u-1)-1) ↔ Basin z) := by
  have leftValue : 3^(r+1)*u-1=12*z+2 := by
    rw [show 3^(r+1)*u=3*(3^r*u) by rw [pow_succ]; ring,phase]
    omega
  have rightValue : 3^r*u-1=4*z := by omega
  have left : orbit (r+3) (2^(r+1)*u-1)=9*z+2 := by
    rw [show r+3=(r+1)+2 by omega,orbit_add (r+1) 2,
      (odd_run (r+1) u hu).1,leftValue]
    exact (complementary_fork z).1
  have right : orbit (r+2) (2^r*u-1)=z := by
    rw [orbit_add r 2,(odd_run r u hu).1,rightValue]
    exact (complementary_fork z).2
  have leftBasin := basin_at_hit (show Hits (2^(r+1)*u-1) (9*z+2) from ⟨r+3,left⟩)
  have rightBasin := basin_at_hit (show Hits (2^r*u-1) z from ⟨r+2,right⟩)
  obtain ⟨odd,pair⟩ := source_pair r u hr hu
  have target : Basin (2*(2^(r+1)*u-1)-1) ↔ Basin (2^r*u-1) := by
    rw [pair,show 2*(2*(2^r*u-1)+1)-1=4*(2^r*u-1)+1 by omega]
    exact odd_inverse_lift _ odd
  exact ⟨leftBasin,rightBasin,target.trans rightBasin⟩

/-- Transporting the residual back through the supplied source gives the
original odd psi query itself, rather than a smaller query. -/
theorem complementary_transfer_is_same_odd_psi
    (r u z : Nat) (hr : 0<r) (hu : 0<u) (phase : 3^r*u=4*z+1) :
    (Basin z ↔ Basin (9*z+2)) ↔ PsiComparison (2^(r+1)*u-1) := by
  obtain ⟨left,_,target⟩ := complementary_identifications r u z hr hu phase
  constructor
  · intro h
    exact left.trans (h.symm.trans target.symm)
  · intro h
    exact target.symm.trans (h.symm.trans left)

/-- Even its one-way form is exactly the reverse direction of the original
odd psi comparison; the inherited hit certificate supplies the antecedent. -/
theorem complementary_forward_is_reverse_same_psi
    (r u z : Nat) (hr : 0<r) (hu : 0<u) (phase : 3^r*u=4*z+1) :
    (Basin z → Basin (9*z+2)) ↔
      (Basin (2*(2^(r+1)*u-1)-1) → Basin (2^(r+1)*u-1)) := by
  obtain ⟨left,_,target⟩ := complementary_identifications r u z hr hu phase
  constructor
  · intro h hb
    exact left.mpr (h (target.mp hb))
  · intro h hb
    exact left.mp (h (target.mpr hb))

theorem complementary_query_rank (r u : Nat) (hr : 0<r) (hu : 0<u) :
    (2^(r+1)*u-1)%2=1 ∧ psiRank (2^(r+1)*u-1)=2^(r+1)*u-1 := by
  obtain ⟨_,pair⟩ := source_pair r u hr hu
  have odd : (2^(r+1)*u-1)%2=1 := by rw [pair]; omega
  exact ⟨odd,by simp [psiRank,odd]⟩

/-- The phase solved by the unbounded block exchange gives an unconditional
odd psi comparison, not merely a supplied-source implication. -/
theorem solved_phase_odd_psi (r u : Nat) (hr : 0<r) (hu : 0<u)
    (phase : (3^r*u)%4=3) : PsiComparison (2^(r+1)*u-1) := by
  obtain ⟨odd,pair⟩ := source_pair r u hr hu
  have comparison := (adjacent_odd_block_descent r u hu phase).2.symm
  rw [pair] at comparison ⊢
  exact (half_comparison_is_same_odd_psi _ odd).mp comparison

#print axioms complementary_identifications
#print axioms complementary_transfer_is_same_odd_psi
#print axioms complementary_forward_is_reverse_same_psi
#print axioms complementary_query_rank
#print axioms solved_phase_odd_psi

end CollatzShell.BandParityBridge
