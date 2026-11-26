import TowerSuffixSharp
/-! On the fixed positive tower at 17, arbitrarily delayed asynchronous
mergers coexist with a fixed five-clock repair on selected rank returns. -/
set_option maxHeartbeats 800000
namespace DelayedTowerMerger
open CollatzReverseBasin WordRank

private theorem toggle (n : Nat) : ∃ c, c%2=1 ∧ 3^(2^(n+1))=1+2^(n+3)*c := by
  induction n with
  | zero => exact ⟨1,by decide,by decide⟩
  | succ n ih =>
    obtain ⟨c,odd,old⟩ := ih
    refine ⟨c+2^(n+2)*c*c,?_,?_⟩
    · rw [show n+2=n+1+1 by omega,pow_succ]
      rw [show 2^(n+1)*2*c*c=2*(2^(n+1)*c*c) by ring]
      omega
    · rw [pow_succ 2 (n+1),pow_mul,old]
      rw [show n+1+3=n+3+1 by omega,pow_succ 2 (n+3),show n+3=n+2+1 by omega,pow_succ 2 (n+2)]
      ring

private theorem digit (d c u : Nat) :
    ∃ a, (1+(32*d)*c)^u=1+(32*d)*(u*c+32*a) := by
  induction u with
  | zero => exact ⟨0,by simp⟩
  | succ u ih =>
    obtain ⟨a,old⟩ := ih
    exact ⟨a+d*c*(u*c+32*a),by rw [pow_succ,old]; ring⟩

private theorem odd_inverse (b : Nat) (hb : b%2=1) : b^8%32=1 := by
  have h : b%32<32 := Nat.mod_lt _ (by decide)
  have d : (b%32)%2=1 := by omega
  have table : ∀ v : Fin 32, v.val%2=1 → v.val^8%32=1 := by decide
  simpa only [Nat.pow_mod b 8 32] using table ⟨b%32,h⟩ d

private theorem ones (n : Nat) : run (2*n) 1=1 := by
  induction n with
  | zero => rfl
  | succ n ih =>
    rw [Nat.mul_succ,runAdd,ih]
    decide

private theorem base (n : Nat) : run (17+2*n) 17=1 ∧ run (17+2*n) 51=1 ∧
    odds (17+2*n) 17=odds (17+2*n) 51 := by
  have a : run 17 17=1 := by decide
  have b : run 17 51=1 := by decide
  have c : odds 17 17=odds 17 51 := by decide
  simp only [runAdd,oddsAdd,a,b,c,ones,true_and]

/-- For each odd H=17+2n and rank cutoff L, some later edge on this
same fixed tower has its first asynchronous deadline exactly at H+5.
The supplied rank is a multiple of 2^(H-2). -/
theorem delayed_merger (n L : Nat) : let H := 17+2*n
    ∃ u, L≤2^(H-2)*u ∧
    (∀ i≤H+4, ∀ j≤H+4, run i (3^(2^(H-2)*u)*17)≠run j (3^(2^(H-2)*u+1)*17)) ∧
    run (H+5) (3^(2^(H-2)*u)*17)=run (H+5) (3^(2^(H-2)*u+1)*17) := by
  let H := 17+2*n
  change ∃ u, L≤2^(H-2)*u ∧ _ ∧ _
  obtain ⟨c,co,phase⟩ := toggle (H-3)
  have h3 : H-3+3=H := by dsimp [H];omega
  have h1 : H-3+1=H-2 := by dsimp [H];omega
  rw [h3,h1] at phase
  let A := 3^(odds H 17)*17
  let b := A*c
  let u := 5*b^7+32*(L+3*2^H+1)
  let r := 2^(H-2)*u
  have bigU : 3*2^H<u ∧ L≤u := by dsimp [u];omega
  have bo : b%2=1 := by
    change ((3^(odds H 17)*17)*c)%2=1
    rw [Nat.mul_mod,Nat.mul_mod (3^(odds H 17)) 17,powOdd,co]
  have div32 : 2^H=32*2^(H-5) := by
    rw [show (32:Nat)=2^5 by decide,←pow_add,show 5+(H-5)=H by dsimp [H];omega]
  obtain ⟨v,eqv⟩ := digit (2^(H-5)) c u
  rw [←div32] at eqv
  let k := u*c+32*v
  have ep : 3^r=1+2^H*k := by dsimp [r];rw [pow_mul,phase];exact eqv
  have ck : u≤u*c := Nat.le_mul_of_pos_right _ (by omega)
  have high : 3*2^H<k := by dsimp [k];omega
  have shift : (A*k)%32=5 := by
    have e : A*k=5*b^8+32*(A*(L+3*2^H+1)*c+A*v) := by dsimp [k,u,b];ring
    rw [e,Nat.add_mul_mod_self_left,Nat.mul_mod,odd_inverse b bo]
  obtain ⟨left,right,counts⟩ := base n
  change run H 17=1 at left
  change run H 51=1 at right
  change odds H 17=odds H 51 at counts
  have stepL : run H (3^r*17)=A*k+1 := by
    rw [ep,show (1+2^H*k)*17=2^H*(k*17)+17 by ring,(liftPrefix H (k*17) 17).1,left]
    dsimp [A];ring
  have stepR : run H (3^(r+1)*17)=3*(A*k)+1 := by
    rw [pow_succ,ep,show ((1+2^H*k)*3)*17=2^H*(k*51)+51 by ring,
      (liftPrefix H (k*51) 51).1,right,←counts]
    dsimp [A];ring
  have size : u≤r := Nat.le_mul_of_pos_left _ (Nat.two_pow_pos _)
  have rankHigh : H+4≤r := by
    have growth := Nat.lt_two_pow_self (n:=H)
    have minimum : 17≤H := by dsimp [H];omega
    omega
  have bound : 1+3*2^H*2^H<3^r := by
    rw [ep]; have m := Nat.mul_lt_mul_of_pos_right high (Nat.two_pow_pos H)
    rw [Nat.mul_comm k] at m
    omega
  have d := (FixedTowerReflection.convergent_control (H-3) u
    (by simpa only [h1,h3,r] using bound)).2.2
  have early : ∀ i≤H, ∀ j≤H, run i (3^r*17)≠run j (3^(r+1)*17) := by
    simpa only [h1,h3,r] using d
  exact ⟨u,bigU.2.trans size,
    TowerSuffixSharp.exact_deadline 17 r H (A*k) (by decide) rankHigh shift stepL stepR early⟩

#print axioms delayed_merger
end DelayedTowerMerger
