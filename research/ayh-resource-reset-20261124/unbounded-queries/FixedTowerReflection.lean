import DefectClockFloor

/-! Exact reflection of finite mergers from high phases back to an unchanged base. -/
namespace FixedTowerReflection
open CollatzReverseBasin WordRank

private theorem upper (i x : Nat) : run i x ≤ 2^i*x := by
  induction i generalizing x with
  | zero => simp [run]
  | succ i ih =>
    have step : shortcut x≤2*x := by unfold shortcut; split <;> omega
    exact (ih (shortcut x)).trans ((Nat.mul_le_mul_left _ step).trans_eq (by ring))

private theorem expand (H i x k : Nat) (hi : i≤H) :
    run i (2^H*k+x) = (2^(H-i)*3^(odds i x))*k+run i x := by
  have shift : 2^H*k = 2^i*(2^(H-i)*k) := by
    rw [←Nat.mul_assoc,←pow_add,show i+(H-i)=H by omega]
  rw [shift,(liftPrefix i (2^(H-i)*k) x).1]
  ring

theorem powers_unique (a b u v : Nat) (h : 2^a*3^u=2^b*3^v) :
    a=b ∧ u=v := by
  have first : a=b := by
    induction a generalizing b with
    | zero =>
      cases b with
      | zero => rfl
      | succ b =>
        have hu := powOdd u
        rw [pow_zero,one_mul,pow_succ,show 2^b*2*3^v=2*(2^b*3^v) by ring] at h
        omega
    | succ a ih =>
      cases b with
      | zero =>
        have hv := powOdd v
        rw [pow_zero,one_mul,pow_succ,show 2^a*2*3^u=2*(2^a*3^u) by ring] at h
        omega
      | succ b =>
        apply congrArg Nat.succ
        apply ih
        rw [pow_succ _ a,pow_succ _ b,show 2^a*2*3^u=2*(2^a*3^u) by ring,
            show 2^b*2*3^v=2*(2^b*3^v) by ring] at h
        omega
  subst b
  exact ⟨rfl,Nat.pow_right_injective (by decide : 2≤3)
    (Nat.eq_of_mul_eq_mul_left (Nat.two_pow_pos _) h)⟩

/-- At a large returning multiplier, independent-clock equality is equivalent
to a compensated common-clock merger on the original two ordinary arms. -/
theorem reflect_iff (z H r k i j : Nat) (pos : 0<z)
    (phase : 3^r=1+2^H*k) (high : 3*2^H<k) (hi : i≤H) (hj : j≤H) :
    run i (3^r*z)=run j (3^(r+1)*z) ↔
    i=j ∧ run i z=run j (3*z) ∧ odds i z=1+odds j (3*z) := by
  let K := k*z
  have low (a x : Nat) (ha : a≤H) (hx : x≤3*z) : run a x<K := by
    calc run a x ≤ 2^a*x := upper a x
         _ ≤ 2^H*(3*z) := Nat.mul_le_mul (Nat.pow_le_pow_right (by decide) ha) hx
         _ = (3*2^H)*z := by ring
         _ < K := Nat.mul_lt_mul_of_pos_right high pos
  have first : 3^r*z=2^H*K+z := by rw [phase]; dsimp [K]; ring
  have second : 3^(r+1)*z=2^H*(3*K)+3*z := by rw [pow_succ,phase]; dsimp [K]; ring
  have form : (2^(H-j)*3^(odds j (3*z)))*(3*K) =
      (2^(H-j)*3^(1+odds j (3*z)))*K := by rw [pow_add]; ring
  rw [first,second,expand _ _ _ _ hi,expand _ _ _ _ hj,form]
  constructor
  · intro meet
    have rem := congrArg (· % K) meet
    simp only [Nat.mul_add_mod_self_right,Nat.mod_eq_of_lt (low i z hi (by omega)),
      Nat.mod_eq_of_lt (low j (3*z) hj le_rfl)] at rem
    have coeff : 2^(H-i)*3^(odds i z)=2^(H-j)*3^(1+odds j (3*z)) := by
      apply Nat.eq_of_mul_eq_mul_right (Nat.mul_pos (by omega : 0<k) pos : 0<K)
      rw [rem] at meet
      exact Nat.add_right_cancel meet
    obtain ⟨time,grade⟩ := powers_unique _ _ _ _ coeff
    exact ⟨by omega,rem,grade⟩
  · rintro ⟨rfl,meet,grade⟩
    rw [meet,grade]

private theorem returns (h : Nat) : ∃ k, 3^(2^(h+1))=1+2^(h+3)*k := by
  induction h with
  | zero => exact ⟨1,by decide⟩
  | succ h ih =>
    obtain ⟨k,hk⟩ := ih
    refine ⟨k+2^(h+2)*k*k, ?_⟩
    rw [pow_succ 2 (h+1),pow_mul,hk]
    rw [show h+1+3=h+3+1 by omega,pow_succ 2 (h+3),show h+3=h+2+1 by omega,pow_succ 2 (h+2)]
    ring

private theorem lift_power (M k u : Nat) : ∃ v, (1+M*k)^u=1+M*v := by
  induction u with
  | zero => exact ⟨0,by simp⟩
  | succ u ih =>
    obtain ⟨v,hv⟩ := ih
    exact ⟨v+k+M*v*k,by rw [pow_succ,hv]; ring⟩

/-- Rank period 2^(H-2) for H≥3; the explicit size test only discards
a finite prefix and is independent of the ordinary base. -/
theorem returning_multiplier (h u : Nat)
    (large : 1+3*2^(h+3)*2^(h+3)<3^(2^(h+1)*u)) :
    ∃ k, 3^(2^(h+1)*u)=1+2^(h+3)*k ∧ 3*2^(h+3)<k := by
  obtain ⟨t,ht⟩ := returns h
  obtain ⟨k,hk⟩ := lift_power (2^(h+3)) t u
  have phase : 3^(2^(h+1)*u)=1+2^(h+3)*k := by rw [pow_mul,ht,hk]
  refine ⟨k,phase,?_⟩
  rw [phase] at large
  by_contra! small
  have prod := Nat.mul_le_mul_right (2^(h+3)) small
  rw [Nat.mul_comm k] at prod
  omega

/-- Every sufficiently high member of an explicit progression on this same
tower reflects a finite meeting back to the original source. -/
theorem defect_delay (z h u : Nat) (bad : CollatzTwoOdd.ReverseDefect z)
    (large : 1+3*2^(h+3)*2^(h+3)<3^(2^(h+1)*u)) :
    ∀ i≤h+3, ∀ j≤h+3,
      run i (3^(2^(h+1)*u)*z)≠run j (3^(2^(h+1)*u+1)*z) := by
  obtain ⟨k,phase,high⟩ := returning_multiplier h u large
  have pos : 0<z := by have := bad.1; omega
  intro i hi j hj meet
  obtain ⟨_,base,_⟩ := (reflect_iff z (h+3) _ k i j pos phase high hi hj).mp meet
  exact bad.2.2 ((PositiveWordDescent.basinRun i z).mp
    (base ▸ (PositiveWordDescent.basinRun j (3*z)).mpr bad.2.1))

private theorem balanced_extension (i t x : Nat)
    (meet : run i x=run i (3*x)) (grade : odds i x=1+odds i (3*x)) :
    run (i+t) x=run (i+t) (3*x) ∧ odds (i+t) x=1+odds (i+t) (3*x) := by
  rw [runAdd,runAdd,oddsAdd,oddsAdd,meet,grade,Nat.add_assoc]
  exact ⟨rfl,rfl⟩

private theorem unbalanced_17 (i : Nat) :
    ¬(run i 17=run i 51 ∧ odds i 17=1+odds i 51) := by
  rintro ⟨meet,grade⟩
  have h := (balanced_extension i 17 17 meet grade).2
  have path : run 17 17=run 17 51 := by decide
  have parity : odds 17 17=odds 17 51 := by decide
  change odds (i+17) 17=1+odds (i+17) 51 at h
  rw [Nat.add_comm i 17,oddsAdd,oddsAdd,parity,path] at h
  omega

/-- The very same obstruction holds at the convergent residue-17 control;
absence of early mergers in these rank returns cannot detect basin change. -/
theorem convergent_control (h u : Nat)
    (large : 1+3*2^(h+3)*2^(h+3)<3^(2^(h+1)*u)) :
    Basin 17 ∧ Basin 51 ∧ ∀ i≤h+3, ∀ j≤h+3,
      run i (3^(2^(h+1)*u)*17)≠run j (3^(2^(h+1)*u+1)*17) := by
  refine ⟨⟨9,(PositiveWordDescent.hitsRun 9 17).mpr (by decide)⟩,
    ⟨17,(PositiveWordDescent.hitsRun 17 51).mpr (by decide)⟩,?_⟩
  obtain ⟨k,phase,high⟩ := returning_multiplier h u large
  intro i hi j hj meet
  obtain ⟨rfl,base,g⟩ := (reflect_iff 17 (h+3) _ k i j (by decide) phase high hi hj).mp meet
  exact unbalanced_17 i ⟨base,g⟩

#print axioms reflect_iff
#print axioms returning_multiplier
#print axioms defect_delay
#print axioms convergent_control
end FixedTowerReflection
