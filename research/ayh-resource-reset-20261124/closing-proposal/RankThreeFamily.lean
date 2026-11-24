import TwoOddCertificate

namespace CollatzRankThree
open CollatzReverseBasin CollatzTwoOdd

private theorem step_basin (n : Nat) : Basin (shortcut n) ↔ Basin n := by
  constructor
  · rintro ⟨k,h⟩; exact ⟨k+1,h⟩
  · rintro ⟨k,h⟩
    cases k with
    | zero => change n=1 at h; subst n; exact ⟨1,rfl⟩
    | succ k => exact ⟨k,h⟩

private theorem orbit_basin (k n : Nat) : Basin (value k n) ↔ Basin n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact (ih _).trans (step_basin n)

private theorem certificate (b k n : Nat) : Hits n (b+k) ↔ Hits (value b n) k := by
  induction b generalizing n with
  | zero => simp [value]
  | succ b ih => simpa only [Nat.succ_add,Hits,value] using ih (shortcut n)

private theorem total_odds (b k n : Nat) : odds (b+k) n=odds b n+odds k (value b n) := by
  induction b generalizing n with
  | zero => simp [odds,value]
  | succ b ih => simp [Nat.succ_add,odds,value,ih,Nat.add_assoc]

private theorem pow_end (k : Nat) : Hits (2^k) k ∧ odds k (2^k)=0 := by
  induction k with
  | zero => exact ⟨rfl,rfl⟩
  | succ k ih => simpa [Nat.pow_succ,Hits,odds,shortcut] using ih

private theorem oddM (u : Nat) (hu : 0<u) : shortcut (2*u-1)=3*u-1 := by
  unfold shortcut; split <;> omega

private theorem source (m : Nat) :
    ∃ z, z%48=17 ∧ 81*z+527 = 512*2^(98+162*m) := by
  induction m with
  | zero => exact ⟨2003200948508806955451580373921,by decide,by decide⟩
  | succ m ih =>
    obtain ⟨z,hz,he⟩ := ih
    let d := 38035129030784485821893427498344748215243281488801
    refine ⟨2^162*z+d,?_,?_⟩
    · dsimp [d]; rw [Nat.add_mod,Nat.mul_mod,hz]
    · calc 81*(2^162*z+d)+527 = 2^162*(81*z+527) := by dsimp [d]; ring
           _ = 512*2^(98+162*(m+1)) := by
             rw [he,show 98+162*(m+1)=(98+162*m)+162 by omega,Nat.pow_add 2 (98+162*m) 162]; ac_rfl

private theorem row (r : Nat) :
    value 10 (1024*r+929)=243*r+221 ∧ value 10 (3*(1024*r+929))=81*r+74 ∧
    odds 10 (3*(1024*r+929))=3 := by
  have s0 : shortcut (1024*r+929)=1536*r+1394 := by unfold shortcut; split <;> omega
  have s1 : shortcut (1536*r+1394)=768*r+697 := by unfold shortcut; split <;> omega
  have s2 : shortcut (768*r+697)=1152*r+1046 := by unfold shortcut; split <;> omega
  have s3 : shortcut (1152*r+1046)=576*r+523 := by unfold shortcut; split <;> omega
  have s4 : shortcut (576*r+523)=864*r+785 := by unfold shortcut; split <;> omega
  have s5 : shortcut (864*r+785)=1296*r+1178 := by unfold shortcut; split <;> omega
  have s6 : shortcut (1296*r+1178)=648*r+589 := by unfold shortcut; split <;> omega
  have s7 : shortcut (648*r+589)=972*r+884 := by unfold shortcut; split <;> omega
  have s8 : shortcut (972*r+884)=486*r+442 := by unfold shortcut; split <;> omega
  have s9 : shortcut (486*r+442)=243*r+221 := by unfold shortcut; split <;> omega
  have s10 : shortcut (3072*r+2787)=4608*r+4181 := by unfold shortcut; split <;> omega
  have s11 : shortcut (4608*r+4181)=6912*r+6272 := by unfold shortcut; split <;> omega
  have s12 : shortcut (6912*r+6272)=3456*r+3136 := by unfold shortcut; split <;> omega
  have s13 : shortcut (3456*r+3136)=1728*r+1568 := by unfold shortcut; split <;> omega
  have s14 : shortcut (1728*r+1568)=864*r+784 := by unfold shortcut; split <;> omega
  have s15 : shortcut (864*r+784)=432*r+392 := by unfold shortcut; split <;> omega
  have s16 : shortcut (432*r+392)=216*r+196 := by unfold shortcut; split <;> omega
  have s17 : shortcut (216*r+196)=108*r+98 := by unfold shortcut; split <;> omega
  have s18 : shortcut (108*r+98)=54*r+49 := by unfold shortcut; split <;> omega
  have s19 : shortcut (54*r+49)=81*r+74 := by unfold shortcut; split <;> omega
  rw [show 3*(1024*r+929)=3072*r+2787 by omega]
  simp only [value,odds,s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19]
  simp [Nat.add_mod,Nat.mul_mod]

set_option maxHeartbeats 1500000 in
/-- A genuine rank-three upper certificate; the lower source has the basin
membership of the Mersenne number with exponent 98+162m. -/
theorem rank_three_family (m : Nat) :
    ∃ z k, z%48=17 ∧ 81*z+527=512*2^(98+162*m) ∧
      Hits (3*z) k ∧ odds k (3*z)=3 ∧
      (Basin z ↔ Basin (2^(98+162*m)-1)) := by
  obtain ⟨z,hz,he⟩ := source m
  let b := 97+162*m
  let u := 2^b
  have up : 0<u := Nat.pow_pos (by decide)
  have pow : 2^(98+162*m)=2*u := by
    change 2^(98+162*m)=2*2^(97+162*m)
    rw [show 98+162*m=(97+162*m)+1 by omega,Nat.pow_succ,Nat.mul_comm]
  have h : 81*z+527=1024*u := by rw [he,pow]; omega
  let r := z/1024
  have zr : z=1024*r+929 := by dsimp [r]; omega
  have ur : u=81*r+74 := by omega
  obtain ⟨low,high,count⟩ := row r
  rw [←zr] at low high count
  have high' : value 10 (3*z)=u := high.trans ur.symm
  have identity (x : Nat) : 243*x+221=3*(81*x+74)-1 := by omega
  have lower : value 10 z=3*u-1 := low.trans ((identity r).trans (congrArg (fun x : Nat => 3*x-1) ur).symm)
  have first : shortcut (2^(98+162*m)-1)=3*u-1 := by rw [pow]; exact oddM u up
  refine ⟨z,10+b,hz,he,?_,?_,?_⟩
  · apply (certificate _ _ _).mpr
    exact high' ▸ (pow_end b).1
  · rw [total_odds,count,high']; exact congrArg (3+·) (pow_end b).2
  · rw [←orbit_basin 10 z,lower,←first]
    exact step_basin _

#print axioms rank_three_family
end CollatzRankThree
