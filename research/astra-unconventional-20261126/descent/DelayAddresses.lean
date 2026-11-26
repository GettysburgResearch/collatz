import SignedIndex
import SignedDelay

namespace Collatz.SignedPeakDelay

private theorem base_shift (a : Nat) : ∃ c<9, (2^(29+18*c)*(2+27*a))%243=154 := by
  have table : ∀ b : Fin 9, ∃ c : Fin 9, (2^(29+18*(c:Nat))*(2+27*(b:Nat)))%243=154 := by decide
  obtain ⟨c,hc⟩ := table ⟨a%9,by omega⟩
  refine ⟨c,c.isLt,?_⟩
  have d : 2+27*a ≡ 2+27*(a%9) [MOD 243] := by
    change (2+27*a)%243=(2+27*(a%9))%243
    omega
  have b := (Nat.ModEq.refl (2^(29+18*(c:Nat)))).mul d
  change _ % 243 = _ at b
  exact b.trans hc

/-- Every ordinary hard-index residue has cofinally many parents on the
explicit family whose lower peak misses all earlier peaks through the deadline. -/
theorem hard_delays_every_address (d a minimum : Nat) :
    ∃ k ≥ minimum, ∃ v : Nat,
      12*2^(18*k)-1=11+162*(a+3^d*v) ∧
      ∀ t i l : Nat, t<12*2^(18*k)-1 → i≤18*k+4 → l≤18*k+4 →
        TernaryPortal.run i (3^(12*2^(18*k)-1)-1) ≠ TernaryPortal.run l (3^t-1) := by
  obtain ⟨c,hc,low⟩ := base_shift a
  let F := 2^(29+18*c)
  obtain ⟨e,he,v,hv⟩ := SignedMersenneIndex.compatible_target d (minimum+10) (F*(2+27*a)) low
  let k := 9*e-c
  have positive : 0<F := Nat.two_pow_pos _
  have ep : 30+162*e=(29+18*c)+(1+18*k) := by dsimp [k]; omega
  rw [ep,pow_add] at hv
  change F*2^(1+18*k)=F*(2+27*a)+3^(5+d)*v at hv
  have ge : 2+27*a≤2^(1+18*k) := by
    exact Nat.le_of_mul_le_mul_left (show F*(2+27*a)≤F*2^(1+18*k) by omega) positive
  have multiple : 3^(5+d) ∣ F*(2^(1+18*k)-(2+27*a)) := by
    exact ⟨v,by rw [Nat.mul_sub,hv]; omega⟩
  have cop : Nat.Coprime (3^(5+d)) F := ((by decide : Nat.Coprime 3 2).pow_left _).pow_right _
  obtain ⟨w,hw⟩ := cop.dvd_of_dvd_mul_left multiple
  have eq : 2^(1+18*k)=2+27*a+3^(5+d)*w := by omega
  have h3 : (3:Nat)^(5+d)=27*(3^d*9) := by rw [pow_add]; ring
  rw [pow_add,pow_one,h3] at eq
  refine ⟨k,by dsimp [k]; omega,9*w,?_,?_⟩
  · have hh : 2*2^(18*k)=2+27*(a+3^d*(9*w)) := by linear_combination eq
    omega
  · intro t i l ht hi hl
    exact explicit_delayed (18*k) t i l ht hi hl

#print axioms hard_delays_every_address
end Collatz.SignedPeakDelay
