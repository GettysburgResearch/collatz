import SignedMersenne
import SignedIndex

namespace Collatz.TernaryPortal

private theorem residue26 (j : Nat) : (2:Nat)^(9+162*j)%243=26 := by
  have a : (2:Nat)^162 ≡ 1 [MOD 243] := by decide
  have b := a.pow j
  have c := (Nat.ModEq.refl (2^9)).mul b
  rw [pow_add,pow_mul]
  simp only [one_pow,Nat.mul_one] at c
  change _ ≡ 26 [MOD 243]
  exact c.trans (by decide : (2:Nat)^9 ≡ 26 [MOD 243])

theorem prepare_signed {j k v : Nat}
    (jump : 2^(30+162*j)=1273960+3^(9+k)*v) :
    ∃ original z t : Nat, 0<t ∧ original%48=17 ∧
      81*original+271=512*2^(9+162*j) ∧
      19683*z+1293643=2097152*2^(9+162*j) ∧ z+1=3^k*(8*t) ∧ v=8*t := by
  let n : Nat := 2^(9+162*j)
  have modulus := residue26 j
  change n%243=26 at modulus
  have shift : 2^(30+162*j)=2097152*n := by
    change 2^(30+162*j)=2097152*2^(9+162*j)
    rw [show 30+162*j=21+(9+162*j) by omega,pow_add,show (2:Nat)^21=2097152 by decide]
  rw [shift] at jump
  have small : 512≤n := by
    exact Nat.pow_le_pow_right (by decide : 0<2) (show 9≤9+162*j by omega)
  have hv : 0<v := by
    by_contra hh
    have : v=0 := by omega
    rw [this,Nat.mul_zero,Nat.add_zero] at jump
    omega
  have dz : 8 ∣ 3^(9+k)*v := by
    refine ⟨262144*n-159245,?_⟩
    omega
  have cop : Nat.Coprime 8 (3^(9+k)) := (by decide : Nat.Coprime 8 3).pow_right _
  obtain ⟨t,ht⟩ := cop.dvd_of_dvd_mul_left dz
  have pt : 0<t := by omega
  let w : Nat := 3^k*(8*t)
  have wp : 0<w := Nat.mul_pos (Nat.pow_pos (by decide) (n:=k)) (Nat.mul_pos (by decide) pt)
  have changePow : (3:Nat)^(9+k)*v=19683*w := by rw [pow_add,ht,show (3:Nat)^9=19683 by decide,Nat.mul_assoc]
  rw [changePow] at jump
  refine ⟨161+1536*(n/243),w-1,t,pt,?_,?_,?_,?_,ht⟩
  · omega
  · change 81*(161+1536*(n/243))+271=512*n
    omega
  · change 19683*(w-1)+1293643=2097152*n
    omega
  · exact Nat.sub_add_cancel wp

/-- Unconditional ordinary hard-family witnesses at every prescribed
depth and above every exponent cutoff, with both physical outcomes and
every supplied hitting certificate retained. -/
theorem hard_family_paid (k minimum : Nat) :
    ∃ j ≥ minimum, ∃ original w : Nat, 0<w ∧ original%48=17 ∧
      81*original+271=2^(18+162*j) ∧
      run (k+19) w=2^(11+162*j)-1 ∧ odds (k+19) w=k+9 ∧
      run (k+21) (3*w)=2^(9+162*j) ∧ odds (k+21) (3*w)=k+8 ∧
      (k=80 → 2^40*w<original) ∧
      ∀ H, run H (3*original)=1 →
        run (H+k+12) (3*w)=1 ∧ odds (H+k+12) (3*w)=odds H (3*original)+k+5 := by
  obtain ⟨j,hj,v,link⟩ := Collatz.SignedMersenneIndex.compatible_above (k+4) minimum
  rw [show 5+(k+4)=9+k by omega] at link
  obtain ⟨original,z,t,ht,canonical,old,seed,lap,_⟩ := prepare_signed link
  obtain ⟨lower,ol,upper,ou⟩ := hard_mersenne_paid ht seed lap
  let w := 2^k*(8*t)-1
  have one : 1<8*t := Nat.lt_of_lt_of_le (by decide : 1<8*1) (Nat.mul_le_mul_left 8 ht)
  have atLeast := Nat.mul_le_mul_right (8*t) (Nat.pow_pos (by decide : 0<2) (n:=k))
  simp only [Nat.one_mul] at atLeast
  have pos : 0<w := Nat.sub_pos_of_lt (one.trans_le atLeast)
  have large : 2<2^(9+162*j) := Nat.lt_of_lt_of_le (by decide : 2<2^9)
      (Nat.pow_le_pow_right (by decide : 0<2) (show 9≤9+162*j by omega))
  refine ⟨j,hj,original,w,pos,canonical,?_,?_,ol,upper,ou,?_,?_⟩
  · rw [show 18+162*j=9+(9+162*j) by omega,pow_add]
    exact old
  · rw [show 11+162*j=2+(9+162*j) by omega,pow_add]
    exact lower
  · intro same
    subst k
    exact (hard_mersenne_height_eighty ht old seed lap).2
  · intro H hit
    exact hard_mersenne_certificate ht large old seed lap hit

#print axioms prepare_signed
#print axioms hard_family_paid

end Collatz.TernaryPortal
