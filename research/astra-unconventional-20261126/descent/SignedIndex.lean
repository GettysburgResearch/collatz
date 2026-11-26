import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic.Ring

namespace Collatz.SignedMersenneIndex

/-- The base 2^162 makes one nonzero ternary change at its first unfixed digit. -/
private theorem jump (k : Nat) :
    ∃ u : Nat, ((2:Nat)^162)^(3^k)=1+3^(5+k)*u ∧ u%3=1 := by
  induction k with
  | zero =>
    exact ⟨(2^162-1)/243,by decide,by decide⟩
  | succ k ih =>
    obtain ⟨u,hu,hmod⟩ := ih
    let w : Nat := 3^(4+k)
    have m : (3:Nat)^(5+k)=3*w := by dsimp [w]; rw [show 5+k=(4+k)+1 by omega,pow_succ]; ring
    refine ⟨u+3*w*u^2+3*w^2*u^3,?_,?_⟩
    · rw [pow_succ (3:Nat) k,pow_mul,hu,show 5+(k+1)=(5+k)+1 by omega,pow_succ,m]
      ring
    · rw [show u+3*w*u^2+3*w^2*u^3=u+3*(w*u^2+w^2*u^3) by ring]
      omega

private theorem choose_digit (v a u m : Nat) (ha : a%3=1) (hu : u%3=1) (hm : m%3=0) :
    ∃ d ≤ 2, ∃ c, (1+m*u)^d=1+m*c ∧ (v+a*c)%3=0 := by
  have am : a ≡ 1 [MOD 3] := ha
  have um : u ≡ 1 [MOD 3] := hu
  have mm : m ≡ 0 [MOD 3] := hm
  rcases (show v%3=0 ∨ v%3=1 ∨ v%3=2 by omega) with h | h | h
  · exact ⟨0,by decide,0,by simp,by simpa using h⟩
  · refine ⟨2,by decide,2*u+m*u*u,by ring,?_⟩
    have vm : v ≡ 1 [MOD 3] := h
    exact (vm.add (am.mul (((Nat.ModEq.refl 2).mul um).add ((mm.mul um).mul um)))).trans (by decide : 3 ≡ 0 [MOD 3])
  · refine ⟨1,by decide,u,by simp,?_⟩
    have vm : v ≡ 2 [MOD 3] := h
    exact (vm.add (am.mul um)).trans (by decide : 3 ≡ 0 [MOD 3])

/-- Every requested ternary precision has a representative in the hard index
family. The witness is a nonnegative ordinary integer below its period. -/
theorem compatible_index (k : Nat) :
    ∃ j < 3^k, ∃ v : Nat, 2^(30+162*j)=1273960+3^(5+k)*v := by
  induction k with
  | zero =>
    exact ⟨0,by decide,(2^30-1273960)/243,by decide⟩
  | succ k ih =>
    obtain ⟨j,hj,v,hv⟩ := ih
    obtain ⟨u,jumpEq,hu⟩ := jump k
    let a : Nat := 2^(30+162*j)
    let m : Nat := 3^(5+k)
    have hm : m%3=0 := by
      dsimp [m]
      rw [show 5+k=(4+k)+1 by omega,pow_succ]
      omega
    have ha : a%3=1 := by
      change (2^(30+162*j))%3=1
      rw [hv]
      change (1273960+m*v)%3=1
      rw [Nat.add_mod,Nat.mul_mod m v,hm]
      simp
    obtain ⟨d,hd,c,hc,hmod⟩ := choose_digit v a u m ha hu hm
    refine ⟨j+3^k*d,?_,(v+a*c)/3,?_⟩
    · have le:=Nat.mul_le_mul_left ((3:Nat)^k) hd
      rw [pow_succ]
      omega
    · have exp : 30+162*(j+3^k*d)=(30+162*j)+(162*3^k)*d := by ring
      have fixv : v+a*c=3*((v+a*c)/3) := by omega
      calc
        _ = a * (((2:Nat)^162)^(3^k))^d := by rw [exp,pow_add,pow_mul,pow_mul]
        _ = a*(1+m*c) := by rw [jumpEq,hc]
        _ = a+m*(a*c) := by ring
        _ = 1273960+m*(v+a*c) := by
          conv_lhs => lhs; change 2^(30+162*j); rw [hv]
          dsimp [m]
          ring
        _ = 1273960+3^(5+(k+1))*((v+a*c)/3) := by
          nth_rw 1 [fixv]
          rw [show 5+(k+1)=(5+k)+1 by omega,pow_succ]
          dsimp [m]
          ring

/-- Each compatible precision admits arbitrarily large ordinary indices. -/
theorem compatible_above (k minimum : Nat) :
    ∃ j ≥ minimum, ∃ v : Nat, 2^(30+162*j)=1273960+3^(5+k)*v := by
  obtain ⟨j,_,v,base⟩ := compatible_index k
  obtain ⟨u,stepEq,_⟩ := jump k
  have multiples (n : Nat) : ∃ w : Nat,
      2^(30+162*(j+n*3^k))=1273960+3^(5+k)*w := by
    induction n with
    | zero => simpa using (show ∃ w : Nat, 2^(30+162*j)=1273960+3^(5+k)*w from ⟨v,base⟩)
    | succ n ih =>
      obtain ⟨w,hw⟩ := ih
      refine ⟨w+(1273960+3^(5+k)*w)*u,?_⟩
      rw [show 30+162*(j+(n+1)*3^k)=(30+162*(j+n*3^k))+162*3^k by ring,
          pow_add,pow_mul,hw,stepEq]
      ring
  obtain ⟨w,hw⟩ := multiples minimum
  have pos := Nat.pow_pos (by decide : 0<3) (n:=k)
  have lower := Nat.mul_le_mul_left minimum (show 1≤3^k by omega)
  exact ⟨j+minimum*3^k,by simp only [Nat.mul_one] at lower; omega,w,hw⟩

/-- The free high ternary digits also permit a prescribed shifted target. -/
theorem compatible_target (k minimum target : Nat) (ht : target%243=154) :
    ∃ j ≥ minimum, ∃ v : Nat, 2^(30+162*j)=target+3^(5+k)*v := by
  induction k with
  | zero =>
    obtain ⟨j,hj,v,hv⟩ := compatible_above 0 (max minimum target)
    have jt : target≤j := le_trans (le_max_right _ _) hj
    have bound : target≤2^(30+162*j) := by
      apply le_trans (jt.trans (Nat.le_of_lt (show j<2^j from Nat.lt_two_pow_self)))
      apply Nat.pow_le_pow_right (by decide)
      omega
    change 2^(30+162*j)=1273960+243*v at hv
    exact ⟨j,le_trans (le_max_left _ _) hj,(2^(30+162*j)-target)/243,by
      change 2^(30+162*j)=target+243*((2^(30+162*j)-target)/243)
      omega⟩
  | succ k ih =>
    obtain ⟨j,hj,v,hv⟩ := ih
    obtain ⟨u,jumpEq,hu⟩ := jump k
    let a : Nat := 2^(30+162*j)
    let m : Nat := 3^(5+k)
    have hm : m%3=0 := by
      dsimp [m]
      rw [show 5+k=(4+k)+1 by omega,pow_succ]
      omega
    have ha : a%3=1 := by
      change (2^(30+162*j))%3=1
      rw [hv]
      change (target+m*v)%3=1
      rw [Nat.add_mod,Nat.mul_mod m v,hm]
      have h3 : target%3=1 := by omega
      simp [h3]
    obtain ⟨d,_,c,hc,hmod⟩ := choose_digit v a u m ha hu hm
    have exp : 30+162*(j+3^k*d)=(30+162*j)+(162*3^k)*d := by ring
    have fixv : v+a*c=3*((v+a*c)/3) := by omega
    refine ⟨j+3^k*d,by omega,(v+a*c)/3,?_⟩
    calc
      _ = a * (((2:Nat)^162)^(3^k))^d := by rw [exp,pow_add,pow_mul,pow_mul]
      _ = a*(1+m*c) := by rw [jumpEq,hc]
      _ = a+m*(a*c) := by ring
      _ = target+m*(v+a*c) := by
        conv_lhs => lhs; change 2^(30+162*j); rw [hv]
        dsimp [m]
        ring
      _ = target+3^(5+(k+1))*((v+a*c)/3) := by
        nth_rw 1 [fixv]
        rw [show 5+(k+1)=(5+k)+1 by omega,pow_succ]
        dsimp [m]
        ring

#print axioms compatible_index
#print axioms compatible_above
#print axioms compatible_target

end Collatz.SignedMersenneIndex
