import AffinePairReturn

namespace CollatzShell.AffinePairReturn

/-- A finite script that reaches a terminal merger using either orientation. -/
inductive Accepts : Nat → Prop
  | terminal (v : Nat) : Accepts (4*v+2)
  | odd (v : Nat) : Accepts (3*v+2) → Accepts (2*v+1)
  | swap (v : Nat) : Accepts (9*v+8) → Accepts (64*v+56)

theorem accepted_positive {b : Nat} (h : Accepts b) : 0<b := by
  cases h <;> omega

theorem accepted_merger {b : Nat} (h : Accepts b) :
    ∃ t, orbit t b=orbit t (3*b+2) := by
  induction h with
  | terminal v =>
    refine ⟨2,?_⟩
    rw [show 3*(4*v+2)+2=2^2*(3*v)+8 by ring,show 4*v+2=2^2*v+2 by rfl]
    rw [OffsetDescent.affine_lift,OffsetDescent.affine_lift]
    change 3*v+2=1*(3*v)+2
    ring
  | odd v _ ih =>
    obtain ⟨t,e⟩ := ih
    refine ⟨1+t,?_⟩
    have a : orbit 1 (2*v+1)=3*v+2 := by
      simp only [orbit,step,show (2*v+1)%2≠0 by omega,ite_false]; omega
    have b : orbit 1 (3*(2*v+1)+2)=3*(3*v+2)+2 := by
      simp only [orbit,step,show (3*(2*v+1)+2)%2≠0 by omega,ite_false]; omega
    simpa only [orbit_add 1 t,a,b] using
      (show orbit t (3*v+2)=orbit t (3*(3*v+2)+2) from e)
  | swap v _ ih =>
    obtain ⟨t,e⟩ := ih
    exact ⟨6+t,by simpa only [orbit_add 6 t,(pair_return v).1,(pair_return v).2] using e.symm⟩

/-- For the canonical odd cofactor, acceptance gives a positive half-size
    partner and an actual common orbit vertex. -/
theorem accepted_half (k u : Nat) (odd : u%2=1)
    (h : Accepts (3^k*u-1)) :
    let x := 2^k*u-1
    let n := 2^(k+1)*u-1
    n=2*x+1 ∧ 0<x ∧ ∃ t, orbit (k+t) x=orbit ((k+1)+t) n := by
  dsimp only
  have hu : 0<u := by omega
  have pos := accepted_positive h
  have u2 : 0<2^k*u := by positivity
  have u3 : 0<3^k*u := by positivity
  have smaller : 1<2^k*u := by
    by_contra! small
    have h1 : 2^k*u=1 := by omega
    have hk := Nat.eq_one_of_mul_eq_one_right h1
    have hu' := Nat.eq_one_of_mul_eq_one_left h1
    have k0 : k=0 := by
      cases k with
      | zero => rfl
      | succ k => rw [pow_succ] at hk; omega
    subst k; subst u
    simp at pos
  have coeff : 2^(k+1)*u=2*(2^k*u) := by rw [pow_succ]; ring
  have tail : 3^(k+1)*u-1=3*(3^k*u-1)+2 := by
    rw [show 3^(k+1)*u=3*(3^k*u) by rw [pow_succ]; ring]
    omega
  obtain ⟨t,hit⟩ := accepted_merger h
  refine ⟨by omega,by omega,t,?_⟩
  rw [orbit_add k t,orbit_add (k+1) t,(odd_run k u hu).1,(odd_run (k+1) u hu).1,tail]
  exact hit

end CollatzShell.AffinePairReturn
