import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Exact change of binary precision under exponential rotations with
a specified first nonzero binary digit. All statements concern ordinary
nonnegative exponents. -/
namespace DyadicPowerPrecision

private theorem even_pow (n : Nat) : (2:Nat)^(n+1)%2=0 := by
  rw [pow_succ]; omega

private theorem odd_power (c n : Nat) (odd : c%2=1) : c^n%2=1 := by
  induction n with
  | zero => rfl
  | succ n ih => rw [pow_succ,Nat.mul_mod,ih,odd]

private theorem repeated_square (c e u : Nat) (form : c=1+2^(e+2)*u)
    (odd : u%2=1) (p : Nat) : ∃ a : Nat,
    c^(2^p)=1+2^(e+p+2)*a ∧ a%2=1 := by
  induction p with
  | zero => exact ⟨u,by simpa using form,odd⟩
  | succ p ih =>
    obtain ⟨a,eq,ao⟩:=ih
    let z:=2^(e+p+1)
    have ez : 2^(e+p+2)=z*2 := by rw [show e+p+2=e+p+1+1 by omega,pow_succ]
    refine ⟨a+z*a^2,?_,?_⟩
    · rw [pow_succ (2:Nat) p,pow_mul,eq,show e+(p+1)+2=(e+p+2)+1 by omega,
          pow_succ (2:Nat) (e+p+2),ez]; ring
    · have ze : z%2=0 := even_pow _
      rw [Nat.add_mod,Nat.mul_mod,ze,ao]; simp

private theorem any_multiple (c e u p t : Nat) (form : c=1+2^(e+2)*u)
    (odd : u%2=1) : ∃ a : Nat,
    c^(2^p*t)=1+2^(e+p+2)*a ∧ a%2=t%2 := by
  obtain ⟨a,eq,ao⟩:=repeated_square c e u form odd p
  induction t with
  | zero => exact ⟨0,by simp,rfl⟩
  | succ t ih =>
    obtain ⟨b,be,bo⟩:=ih
    let z:=2^(e+p+2)
    refine ⟨b+a+z*b*a,?_,?_⟩
    · rw [Nat.mul_succ,pow_add,be,eq]; dsimp [z]; ring
    · have ze : z%2=0 := even_pow _
      rw [Nat.add_mod,Nat.mul_mod,Nat.mul_mod z b,ze,zero_mul,Nat.zero_mod,zero_mul,Nat.zero_mod,
        Nat.add_mod b a,bo,ao]
      omega

private theorem change_digit (c e u a p t : Nat) (form : c=1+2^(e+2)*u)
    (odd : u%2=1) : ∃ b : Nat,
    c^(a+2^p*t)=c^a+2^(e+p+2)*b ∧ b%2=t%2 := by
  obtain ⟨b,be,bo⟩:=any_multiple c e u p t form odd
  have co : c%2=1 := by
    rw [form,Nat.add_mod,Nat.mul_mod,even_pow]; simp
  refine ⟨c^a*b,by rw [pow_add,be]; ring,?_⟩
  rw [Nat.mul_mod,odd_power c a co,bo,Nat.one_mul,Nat.mod_mod]

/-- Scaling of the valuation, valid for every pair a,a+t and every
finite requested precision, without density hypotheses. -/
theorem precision (c e u a t k : Nat) (form : c=1+2^(e+2)*u)
    (odd : u%2=1) : 2^(e+k+2) ∣ c^(a+t)-c^a ↔ 2^k ∣ t := by
  induction k with
  | zero =>
    obtain ⟨b,eq,_⟩:=change_digit c e u a 0 t form odd
    simp only [pow_zero,Nat.one_mul] at eq
    rw [eq,Nat.add_sub_cancel_left]; simp
  | succ k ih =>
    by_cases div : 2^k ∣ t
    · obtain ⟨v,hv⟩:=div
      obtain ⟨b,eq,bo⟩:=change_digit c e u a k v form odd
      rw [hv,eq,Nat.add_sub_cancel_left,show e+(k+1)+2=e+k+2+1 by omega,
          pow_succ (2:Nat) (e+k+2),pow_succ (2:Nat) k]
      rw [Nat.mul_dvd_mul_iff_left (by positivity : 0<(2:Nat)^(e+k+2)),
          Nat.mul_dvd_mul_iff_left (by positivity : 0<(2:Nat)^k)]
      omega
    · have nleft : ¬2^(e+(k+1)+2) ∣ c^(a+t)-c^a := fun d =>
        div (ih.mp ((pow_dvd_pow 2 (show e+k+2≤e+(k+1)+2 by omega)).trans d))
      have nright : ¬2^(k+1) ∣ t := fun d => div ((pow_dvd_pow 2 (by omega)).trans d)
      simp [nleft,nright]

#print axioms precision
end DyadicPowerPrecision
