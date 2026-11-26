import Portal

namespace Collatz.TernaryPortal

/-- The lower reaches a Mersenne phase two clocks before the upper reaches
its power-of-two ray. The upper count is s, the lower count is s+1. -/
def MersenneRow (z h s n : Nat) : Prop :=
  run h z = 4*n-1 ∧ odds h z=s+1 ∧
  run (h+2) (3*z)=n ∧ odds (h+2) (3*z)=s

private theorem row_lift {b h s n : Nat} (hp : 0<n) (seed : MersenneRow b h s n) (t : Nat) :
    MersenneRow (b+2^(h+2)*t) h s (n+3^s*(3*t)) := by
  obtain ⟨l,ol,u,ou⟩ := seed
  obtain ⟨ll,oll⟩ := prefix_lift h b (4*t)
  obtain ⟨uu,ouu⟩ := prefix_lift (h+2) (3*b) (3*t)
  have lo : b+2^(h+2)*t=b+2^h*(4*t) := by ring
  have up : 3*(b+2^(h+2)*t)=3*b+2^(h+2)*(3*t) := by ring
  unfold MersenneRow
  rw [up,lo,ll,oll,uu,ouu,l,ol,u,ou,pow_succ]
  rw [show 3^s*3*(4*t)=4*(3^s*(3*t)) by ring]
  omega

theorem hard_mersenne_original {z n : Nat} (link : 81*z+271=512*n) :
    MersenneRow z 7 3 n := by
  have seed : MersenneRow 161 7 3 26 := by unfold MersenneRow; decide
  have hz : z%512=161 := by omega
  obtain ⟨t,ha,hb⟩ : ∃ t, z=161+512*t ∧ n=26+81*t :=
    ⟨z/512,by omega,by omega⟩
  simpa [ha,hb,←Nat.mul_assoc] using row_lift (by decide) seed t

theorem hard_mersenne_four {z n : Nat} (link : 243*z+623=1024*n) :
    MersenneRow z 8 4 n := by
  have seed : MersenneRow 107 8 4 26 := by unfold MersenneRow; decide
  have hz : z%1024=107 := by omega
  obtain ⟨t,ha,hb⟩ : ∃ t, z=107+1024*t ∧ n=26+243*t :=
    ⟨z/1024,by omega,by omega⟩
  simpa [ha,hb,←Nat.mul_assoc] using row_lift (by decide) seed t

theorem hard_mersenne_stable {z n : Nat} (link : 19683*z+1293643=2097152*n) :
    MersenneRow z 19 8 n ∧ z%8=7 := by
  have seed : MersenneRow 1711495 19 8 16064 := by unfold MersenneRow; decide
  have hz : z%2097152=1711495 := by omega
  obtain ⟨t,ha,hb⟩ : ∃ t, z=1711495+2097152*t ∧ n=16064+19683*t :=
    ⟨z/2097152,by omega,by omega⟩
  exact ⟨by simpa [ha,hb,←Nat.mul_assoc] using row_lift (by decide) seed t,by omega⟩

theorem hard_mersenne_canonical_one {z n : Nat} (link : 531441*z+2692031=1048576*n) :
    MersenneRow z 18 11 n ∧ z%16=1 := by
  have seed : MersenneRow 25937 18 11 13148 := by unfold MersenneRow; decide
  have hz : z%1048576=25937 := by omega
  obtain ⟨t,ha,hb⟩ : ∃ t, z=25937+1048576*t ∧ n=13148+531441*t :=
    ⟨z/1048576,by omega,by omega⟩
  exact ⟨by simpa [ha,hb,←Nat.mul_assoc] using row_lift (by decide) seed t,by omega⟩

theorem hard_mersenne_canonical_two {z n : Nat} (link : 531441*z+4970719=2097152*n) :
    MersenneRow z 19 11 n ∧ z%16=1 := by
  have seed : MersenneRow 1682993 19 11 426491 := by unfold MersenneRow; decide
  have hz : z%2097152=1682993 := by omega
  obtain ⟨t,ha,hb⟩ : ∃ t, z=1682993+2097152*t ∧ n=426491+531441*t :=
    ⟨z/2097152,by omega,by omega⟩
  exact ⟨by simpa [ha,hb,←Nat.mul_assoc] using row_lift (by decide) seed t,by omega⟩

private theorem minus_odd (k u : Nat) (hu : 0<u) :
    run k (2^k*u-1)=3^k*u-1 ∧ odds k (2^k*u-1)=k := by
  induction k generalizing u with
  | zero => simp [run,odds]
  | succ k ih =>
    have pp := Nat.mul_pos (Nat.two_pow_pos k) hu
    have form : 2^(k+1)*u=2*(2^k*u) := by ring
    have first : step (2^(k+1)*u-1)=2^k*(3*u)-1 := by
      rw [form,show 2^k*(3*u)=3*(2^k*u) by ring]
      unfold step
      split <;> omega
    have odd : (2^(k+1)*u-1)%2=1 := by rw [form]; omega
    obtain ⟨r,o⟩ := ih (3*u) (by omega)
    rw [run,odds,first,odd,r,o,pow_succ]
    constructor
    · congr 1
      ring
    · omega

private theorem triple_open (s : Nat) (hs : 0<s) :
    run 3 (3*(8*s-1))=9*s-1 ∧ odds 3 (3*(8*s-1))=1 := by
  have he : s=(s-1)+1 := by omega
  have link : 3*(8*s-1)=21+8*(3*(s-1)) := by omega
  obtain ⟨hh,ho⟩ := prefix_lift 3 21 (3*(s-1))
  rw [link]
  change run 3 (21+8*(3*(s-1)))=9*s-1 ∧ odds 3 (21+8*(3*(s-1)))=1
  rw [show (2:Nat)^3=8 by decide] at hh ho
  rw [hh,ho,show run 3 21=8 by decide,show odds 3 21=1 by decide]
  omega

/-- The compact paired predecessor spends k additional odd steps while
reducing the ordinary Mersenne representative by a factor near (2/3)^k. -/
theorem hard_mersenne_paid {z n k t : Nat} (ht : 0<t)
    (seed : 19683*z+1293643=2097152*n) (lap : z+1=3^k*(8*t)) :
    let w := 2^k*(8*t)-1
    run (k+19) w=4*n-1 ∧ odds (k+19) w=k+9 ∧
    run (k+21) (3*w)=n ∧ odds (k+21) (3*w)=k+8 := by
  dsimp only
  obtain ⟨⟨hl,ol,hu,ou⟩,_⟩ := hard_mersenne_stable seed
  have ⟨wl,owl⟩ := minus_odd k (8*t) (by omega)
  rw [←lap] at wl
  simp only [Nat.add_sub_cancel] at wl
  have zexpr : z=8*(3^k*t)-1 := by
    rw [show 3^k*(8*t)=8*(3^k*t) by ring] at lap
    omega
  have wexpr : 2^k*(8*t)-1=8*(2^k*t)-1 := by ring_nf
  have pos3 := Nat.mul_pos (Nat.pow_pos (by decide : 0<3) (n:=k)) ht
  have pos2 := Nat.mul_pos (Nat.two_pow_pos k) ht
  obtain ⟨az,aoz⟩ := triple_open (3^k*t) pos3
  rw [←zexpr] at az aoz
  obtain ⟨aw,aow⟩ := triple_open (2^k*t) pos2
  rw [←wexpr] at aw aow
  obtain ⟨mid,omid⟩ := minus_odd k (9*t) (by omega)
  rw [show 2^k*(9*t)=9*(2^k*t) by ring] at mid omid
  rw [show 3^k*(9*t)=9*(3^k*t) by ring] at mid
  have eq : run (3+k) (3*(2^k*(8*t)-1))=run 3 (3*z) := by
    rw [run_add,aw,mid,az]
  have od : odds (3+k) (3*(2^k*(8*t)-1))=1+k := by
    rw [odds_add,aw,aow,omid]
  refine ⟨by rw [run_add,wl,hl],by rw [odds_add,owl,wl,ol],?_,?_⟩
  · rw [show k+21=(3+k)+18 by omega,run_add,eq,←run_add]
    exact hu
  · rw [show k+21=(3+k)+18 by omega,odds_add,eq,od]
    rw [show 19+2=3+18 by decide,odds_add,aoz] at ou
    omega

private theorem seed_bound {z n : Nat} (h : 19683*z+1293643=2097152*n) :
    19683*(z+1)<524288*(4*n) := by omega

private theorem original_bound {z n : Nat} (h : 81*z+271=512*n) : 4*n≤z := by omega

/-- Eighty paid inverse odds put the ordinary lower strictly below the
quantitative two-to-the-fortieth height threshold. -/
theorem hard_mersenne_height_eighty {original z n t : Nat} (ht : 0<t)
    (old : 81*original+271=512*n)
    (seed : 19683*z+1293643=2097152*n)
    (lap : z+1=3^80*(8*t)) :
    0 < 2^80*(8*t)-1 ∧ 2^40*(2^80*(8*t)-1)<original := by
  have pos : 0 < 8*t := Nat.mul_pos (by decide) ht
  have gt : 1<8*t := Nat.lt_of_lt_of_le (by decide : 1<8*1) (Nat.mul_le_mul_left 8 ht)
  have atleast := Nat.mul_le_mul_right (8*t) (by decide : 1≤(2:Nat)^80)
  simp only [Nat.one_mul] at atleast
  refine ⟨Nat.sub_pos_of_lt (gt.trans_le atleast),?_⟩
  have scaled : (2:Nat)^120*(8*t)<4*n := by
    apply (Nat.mul_lt_mul_left (by decide : 0 < (2:Nat)^19)).mp
    calc
      _ = (2:Nat)^139*(8*t) := by rw [←Nat.mul_assoc,←pow_add]
      _ < (3:Nat)^89*(8*t) := Nat.mul_lt_mul_of_pos_right (by decide) pos
      _ = 19683*(z+1) := by
        rw [lap,←Nat.mul_assoc,show (3:Nat)^89=19683*3^80 by decide]
        ac_rfl
      _ < (2:Nat)^19*(4*n) := seed_bound seed
  calc
    _ ≤ (2:Nat)^40*(2^80*(8*t)) := Nat.mul_le_mul_left _ (Nat.sub_le _ _)
    _ = (2:Nat)^120*(8*t) := by rw [←Nat.mul_assoc,←pow_add]
    _ < 4*n := scaled
    _ ≤ original := original_bound old

theorem hard_mersenne_four_smaller {original z n : Nat}
    (old : 81*original+271=512*n) (new : 243*z+623=1024*n) :
    0<z ∧ z<original := by omega

private theorem cycle_small (k x : Nat) (hx : x=1 ∨ x=2) : run k x=1 ∨ run k x=2 := by
  induction k generalizing x with
  | zero => exact hx
  | succ k ih =>
    apply ih
    rcases hx with rfl | rfl <;> decide

private theorem enough_time {v n h H : Nat} (large : 2<n) (early : run h v=n)
    (hit : run H v=1) : h≤H := by
  by_contra small
  have split : h=H+(h-H) := by omega
  rw [split,run_add,hit] at early
  have cy := cycle_small (h-H) 1 (Or.inl rfl)
  omega

/-- Every supplied original upper hit transfers to the paid representative
with exactly k+12 additional clocks and k+5 additional odd departures. -/
theorem hard_mersenne_certificate {original z n k t H : Nat} (ht : 0<t) (large : 2<n)
    (old : 81*original+271=512*n) (seed : 19683*z+1293643=2097152*n)
    (lap : z+1=3^k*(8*t)) (hit : run H (3*original)=1) :
    let w := 2^k*(8*t)-1
    run (H+k+12) (3*w)=1 ∧ odds (H+k+12) (3*w)=odds H (3*original)+k+5 := by
  dsimp only
  obtain ⟨_,_,uo,oo⟩ := hard_mersenne_original old
  obtain ⟨_,_,un,on⟩ := hard_mersenne_paid ht seed lap
  change run 9 (3*original)=n at uo
  change odds 9 (3*original)=3 at oo
  have enough : 9≤H := enough_time large uo hit
  clear old seed lap ht
  obtain ⟨s,rfl⟩ := Nat.exists_eq_add_of_le enough
  rw [run_add 9 s (3*original),uo] at hit
  rw [show 9+s+k+12=(k+21)+s by omega,
      run_add (k+21) s,odds_add (k+21) s,un,on,
      odds_add 9 s,uo,oo,hit]
  omega

#print axioms hard_mersenne_original
#print axioms hard_mersenne_four
#print axioms hard_mersenne_stable
#print axioms hard_mersenne_canonical_one
#print axioms hard_mersenne_canonical_two
#print axioms hard_mersenne_paid
#print axioms hard_mersenne_height_eighty
#print axioms hard_mersenne_four_smaller
#print axioms hard_mersenne_certificate

end Collatz.TernaryPortal
