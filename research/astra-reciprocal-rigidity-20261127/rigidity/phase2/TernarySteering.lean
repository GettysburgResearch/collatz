import FiniteTrace

/-! Positive targets on a ternary arithmetic progression via powers of two. -/
namespace Collatz.ReciprocalRigidity.TernarySteering

private theorem period_shape (p : ℕ) :
    ∃ u : ℤ, 2^(2*3^p)=1+3^(p+1)*(1+3*u) := by
  induction p with
  | zero => exact ⟨0,by norm_num⟩
  | succ p ih =>
    obtain ⟨u,hu⟩ := ih
    let w : ℤ := 1+3*u
    refine ⟨u+3^p*w^2+(3^p)^2*w^3, ?_⟩
    rw [show 2*3^(p+1)=(2*3^p)*3 by rw [pow_succ]; ring, pow_mul, hu]
    dsimp [w]
    rw [pow_succ (3 : ℤ) (p+1),pow_succ (3 : ℤ) p]
    ring

private theorem even_power_shape (k : ℕ) : ∃ u : ℤ, (2:ℤ)^(2*k)=1+3*u := by
  induction k with
  | zero => exact ⟨0,by norm_num⟩
  | succ k ih =>
    obtain ⟨u,hu⟩ := ih
    exact ⟨4*u+1,by rw [show 2*(k+1)=2*k+2 by omega,pow_add,hu];ring⟩

/-- Exponents may begin arbitrarily far out; the target residue is 1 modulo 3. -/
theorem power_steering (p L v : ℕ) (z : ℤ) (hv : v%3≠0) :
    ∃ e : ℕ, L≤e ∧ ∃ c : ℤ, (2:ℤ)^e*v=3*z+1+3^(p+1)*c := by
  induction p with
  | zero =>
    obtain ⟨w,hw⟩ := even_power_shape L
    by_cases hv1 : v%3=1
    · have hdiv : (v:ℤ)=3*(v/3:ℕ)+1 := by omega
      refine ⟨2*L,by omega, w*v+(v/3:ℕ)-z, ?_⟩
      rw [hw]; simp only [Nat.zero_add,pow_one];rw [hdiv];ring
    · have hdiv : (v:ℤ)=3*(v/3:ℕ)+2 := by omega
      refine ⟨2*L+1,by omega, 2*w*v+2*(v/3:ℕ)+1-z, ?_⟩
      rw [pow_succ,hw];simp only [Nat.zero_add,pow_one];rw [hdiv];ring
  | succ p ih =>
    obtain ⟨e,hLe,c,hc⟩ := ih
    obtain ⟨w,hw⟩ := period_shape p
    let r : ℕ := 2*3^p
    let N : ℤ := 3^(p+1)
    have hn : N=3*(3:ℤ)^p := by dsimp [N];rw [pow_succ];ring
    change (2:ℤ)^r = 1+N*(1+3*w) at hw
    change (2:ℤ)^e*v = 3*z+1+N*c at hc
    have advance (f : ℕ) (q : ℤ) (hf : (2:ℤ)^f*v=3*z+1+N*q) :
        ∃ t : ℤ, (2:ℤ)^(f+r)*v=3*z+1+N*(q+1+3*t) := by
      refine ⟨z+3^p*q+w*(2^f*v), ?_⟩
      rw [pow_add,hw,mul_right_comm _ _ (v:ℤ),hf,hn]
      ring
    have finish (f : ℕ) (q : ℤ) (hLf : L≤f) (hq : q%3=0)
        (hf : (2:ℤ)^f*v=3*z+1+N*q) :
        ∃ e : ℕ, L≤e ∧ ∃ c : ℤ, (2:ℤ)^e*v=3*z+1+3^(p+1+1)*c := by
      refine ⟨f,hLf,q/3,?_⟩
      have he : q=3*(q/3) := by omega
      calc
        (2:ℤ)^f*v=3*z+1+N*q := hf
        _=3*z+1+3^(p+1+1)*(q/3) := by
          rw [pow_succ (3:ℤ) (p+1)];change 3*z+1+N*q=3*z+1+(N*3)*(q/3)
          conv_lhs => rw [he]
          ring
    by_cases hz : c%3=0
    · exact finish e c hLe hz hc
    obtain ⟨t,ht⟩ := advance e c hc
    by_cases hz' : (c+1+3*t)%3=0
    · exact finish (e+r) (c+1+3*t) (by omega) hz' ht
    obtain ⟨t',ht'⟩ := advance (e+r) (c+1+3*t) ht
    exact finish (e+r+r) (c+1+3*t+1+3*t') (by omega) (by omega) ht'

#print axioms power_steering
end Collatz.ReciprocalRigidity.TernarySteering
