import UpperClock

/-! A physical lower clock, together with an upper power-of-two tail,
must use linear time to improve the canonical rank-three row. -/
set_option autoImplicit false
set_option warningAsError true
namespace ClockBarrier
open CoreBranching PeakRigidity FloorCounting UpperClock

private theorem two_power_unique (a b c d : ℕ)
    (eq : 2^a*3^b=2^c*3^d) : a=c ∧ b=d := by
  have imposs (x y u v : ℕ) (less : x<y) (h : 2^x*3^u=2^y*3^v) : False := by
    obtain ⟨k,hk⟩:=Nat.exists_eq_add_of_le (show x+1≤y by omega)
    rw [hk,show x+1+k=x+(1+k) by omega,pow_add,mul_assoc] at h
    have e:=Nat.eq_of_mul_eq_mul_left (by positivity : 0<(2:ℕ)^x) h
    have odd : (3:ℕ)^u%2=1 := by simp [Nat.pow_mod]
    rw [e,pow_add,pow_one,show 2*2^k*3^v=2*(2^k*3^v) by ring] at odd
    omega
  have ab : a=c := by
    rcases lt_trichotomy a c with hi|hi|hi
    · exact False.elim (imposs _ _ _ _ hi eq)
    · exact hi
    · exact False.elim (imposs _ _ _ _ hi eq.symm)
  rw [ab] at eq
  exact ⟨ab,Nat.pow_right_injective (by decide : 2≤3)
    (Nat.eq_of_mul_eq_mul_left (by positivity : 0<(2:ℕ)^c) eq)⟩

theorem halve (k v : ℕ) : run k (2^k*v)=v := by
  induction k generalizing v with
  | zero => simp [run]
  | succ k ih =>
    rw [pow_succ,show 2^k*2*v=2*(2^k*v) by ring,run,step_double,ih]

theorem hard_prefixes (H z : ℕ) (row : 81*z+271=2^H) (hh : 9≤H) :
    run 7 z+1=2^(H-7) ∧ run 9 (3*z)=2^(H-9) := by
  have p9 : 2^H=512*2^(H-9) := by
    rw [←show (2:ℕ)^9=512 by decide,←pow_add]
    congr 1
    omega
  have p7 : 2^H=128*2^(H-7) := by
    rw [←show (2:ℕ)^7=128 by decide,←pow_add]
    congr 1
    omega
  have l := (lift_prefix 7 0 33 (z/128)).1
  have u := (lift_prefix 9 0 483 ((3*z)/512)).1
  norm_num [show run 7 33=22 by decide,show grade 7 33=4 by decide] at l
  norm_num [show run 9 483=26 by decide,show grade 9 483=3 by decide] at u
  rw [show 33+128*(z/128)=z by omega] at l
  rw [show 483+512*(3*z/512)=3*z by omega] at u
  omega

theorem lower_native (H z I : ℕ) (row : 81*z+271=2^H) (hh : 9≤H)
    (lo : 7≤I) (hi : I≤H) : run I z+1=2^(H-I)*3^(I-7) := by
  have p:=(hard_prefixes H z row hh).1
  have split : 2^(H-7)=2^(I-7)*2^(H-I) := by rw [←pow_add]; congr 1; omega
  rw [split] at p
  have e : run 7 z=2^(I-7)*2^(H-I)-1 := by omega
  have a:=EarlierOffsets.ascent (I-7) (2^(H-I)) (by positivity)
  have k : 0<3^(I-7)*2^(H-I) := by positivity
  calc run I z+1 = run (I-7) (run 7 z)+1 := by
         conv_lhs => rw [show I=7+(I-7) by omega,run_add]
       _ = _ := by rw [e,a,Nat.sub_add_cancel (by omega : 1≤3^(I-7)*2^(H-I)),mul_comm]

theorem upper_native (H z K : ℕ) (row : 81*z+271=2^H) (hh : 9≤H)
    (lo : 9≤K) (hi : K≤H) : run K (3*z)=2^(H-K) := by
  have p:=(hard_prefixes H z row hh).2
  have split : 2^(H-9)=2^(K-9)*2^(H-K) := by rw [←pow_add]; congr 1; omega
  have k : K=9+(K-9) := by omega
  calc run K (3*z) = run (K-9) (run 9 (3*z)) := by conv_lhs => rw [k,run_add]
       _ = _ := by rw [p,split,halve]

private theorem intercept_separation (H y I J E h M : ℕ) (hr : 2^H%27=1)
    (can : y%48=17) (short : h<H) (lo : 7≤I) (ee : 2≤E)
    (ec : E≤M) (jc : J≤M) (ic : I≤H)
    (room : 4*M+3≤H-I) (room' : 4*M+3≤h)
    (lower : run J y+1=2^(H-I)*3^(I-7))
    (upper : 3^(grade E (3*y))*(3*y)+intercept E (3*y)=2^h) : False := by
  let p:=grade J y
  let r:=grade E (3*y)
  let A:=intercept J y
  let D:=intercept E (3*y)
  have ya : 3^(r+1)*y+D=2^h := by simpa only [p,r,D,pow_succ,mul_assoc] using upper
  have la : 3^p*y+(A+2^J)=2^(J+(H-I))*3^(I-7) := by
    calc _ = 2^J*(run J y+1) := by
           rw [mul_add,mul_one,affine]
           dsimp only [A,p]
           ring
         _ = _ := by rw [lower,pow_add]; ring
  have balance : 2^h*3^p + 3^(r+1)*(A+2^J) =
      2^(J+(H-I))*3^(r+1+(I-7)) + 3^p*D := by
    calc _ = 3^(r+1)*(3^p*y+(A+2^J))+3^p*D := by rw [←ya]; ring
         _ = _ := by rw [la,pow_add 3]; ring
  let cut:=4*M+3
  have ab : A+2^J≤3^J := intercept_bound J y
  have db : D≤3^E := by
    exact (Nat.le_add_right D (2^E)).trans (intercept_bound E (3*y))
  have pm : p≤M := (grade_le J y).trans jc
  have rm : r≤M := (grade_le E (3*y)).trans ec
  have bs : (3:ℕ)^(2*M+1)<2^cut := by
    calc (3:ℕ)^(2*M+1) ≤ 4^(2*M+1) := Nat.pow_le_pow_left (by decide) _
         _ = 2^(4*M+2) := by
           change ((2:ℕ)^2)^(2*M+1)=_
           rw [←pow_mul]
           congr 1
           omega
         _ < _ := Nat.pow_lt_pow_right (by decide) (by dsimp [cut]; omega)
  have s1 : 3^(r+1)*(A+2^J)<2^cut := by
    calc _ ≤ 3^(r+1)*3^J := Nat.mul_le_mul_left _ ab
         _ = 3^(r+1+J) := (pow_add ..).symm
         _ ≤ 3^(2*M+1) := Nat.pow_le_pow_right (by decide) (by omega)
         _ < _ := bs
  have s2 : 3^p*D<2^cut := by
    calc _ ≤ 3^p*3^E := Nat.mul_le_mul_left _ db
         _ = 3^(p+E) := (pow_add ..).symm
         _ ≤ 3^(2*M+1) := Nat.pow_le_pow_right (by decide) (by omega)
         _ < _ := bs
  have head (u v : ℕ) (hu : cut≤u) : (2^u*3^v)%(2^cut)=0 := by
    obtain ⟨w,rfl⟩:=Nat.exists_eq_add_of_le hu
    rw [pow_add,mul_assoc,Nat.mul_mod_right]
  have modEq:=congrArg (fun x : ℕ => x%2^cut) balance
  change (_+_)%2^cut=(_+_)%2^cut at modEq
  rw [Nat.add_mod,Nat.add_mod (2^(J+(H-I))*_),head _ _ room',
    head _ _ (by dsimp [cut]; omega),Nat.zero_add,Nat.zero_add,
    Nat.mod_eq_of_lt s1,Nat.mod_eq_of_lt s2,Nat.mod_eq_of_lt s1,Nat.mod_eq_of_lt s2] at modEq
  have slope : 2^h*3^p=2^(J+(H-I))*3^(r+1+(I-7)) := by omega
  obtain ⟨hg,pg⟩:=two_power_unique _ _ _ _ slope
  have c:=canonical_prefix y can
  have re:=word_extension 2 (E-2) (3*y)
  rw [show 2+(E-2)=E by omega,c.1] at re
  change 2≤r ∧ _ at re
  have rr:=re.1
  have pf : 3≤p := by omega
  have four : 4≤J := by
    by_contra! sg
    have w:=(word_extension J (4-J) y).1
    rw [show J+(4-J)=4 by omega,c.2.2.1] at w
    change p≤2 at w
    omega
  have ev := word_extension 4 (J-4) y
  rw [show 4+(J-4)=J by omega,c.2.2.1,c.2.2.2] at ev
  change 2≤p ∧ p≤2+(J-4) ∧ _ at ev
  have even3 : p+3≤J := by
    by_contra! fail
    have same : grade J y=2+(J-4) := by change p=2+(J-4); omega
    have lowA:=ev.2.2.2 same
    change A+2^J=3^(J-4)*(7+2^4) at lowA
    have pp : p=J-4+2 := by omega
    rw [lowA,pp,pow_add (3:ℕ) (J-4)] at modEq
    have cancel : 3^(J-4)*(3^(r+1)*23)=3^(J-4)*(9*D) := by
      calc _ = _ := (show 3^(J-4)*(3^(r+1)*23)=3^(r+1)*(3^(J-4)*(7+2^4)) by ring)
           _ = _ := modEq
           _ = _ := by ring
    have rd:=Nat.eq_of_mul_eq_mul_left (by positivity : 0<(3:ℕ)^(J-4)) cancel
    have rrw : r+1=3+(r-2) := by omega
    rw [rrw,pow_add] at rd
    have divD : D=3*(3^(r-2)*23) := by rw [show (3:ℕ)^3*3^(r-2)*23=9*(3*(3^(r-2)*23)) by ring] at rd; omega
    have unit : (2:ℕ)^h%3≠0 := by
      have all (v : ℕ) : (2:ℕ)^v%3=1 ∨ 2^v%3=2 := by
        induction v with
        | zero => decide
        | succ k ih => rw [pow_succ,Nat.mul_mod]; rcases ih with a|a <;> rw [a] <;> decide
      rcases all h with un|un <;> omega
    have hd : (2:ℕ)^h%3=0 := by
      rw [←ya,pow_succ,divD,show 3^r*3*y=3*(3^r*y) by ring]
      omega
    exact unit hd
  have two : r=2 := by omega
  have flat:=re.2.2.1 (by exact two)
  change D=intercept 2 (3*y) at flat
  rw [c.2.1] at flat
  have h1 : H=h+1 := by omega
  rw [two,flat] at ya
  rw [h1,pow_succ,←ya] at hr
  norm_num at hr
  omega

private theorem affine_tail {y E v : ℕ} (tail : run E (3*y)=2^v) :
    3^(grade E (3*y))*(3*y)+intercept E (3*y)=2^(E+v) := by
  rw [←affine,tail,pow_add]

private theorem grow (j x : ℕ) : run j x≤2^j*x := by
  induction j generalizing x with
  | zero => simp [run]
  | succ j ih =>
    have st : step x≤2*x := by unfold step; split <;> omega
    calc run (j+1) x = run j (step x) := rfl
         _ ≤ 2^j*(step x) := ih _
         _ ≤ 2^j*(2*x) := Nat.mul_le_mul_left _ st
         _ = _ := by rw [pow_succ,mul_assoc]

/-- Even with no prescribed meeting of the two upper arms, an actual
early power-of-two tail for the upper of the proposed replacement and a
physical comparison of its lower arm to the row cannot both use short clocks. -/
theorem short_upper_tail_barrier (t z y i j e v B : ℕ)
    (row : 81*z+271=2^(18+162*t)) (can : y%48=17)
    (lower : run i z=run j y) (upper : run e (3*y)=2^v)
    (short : e+v<18+162*t) (ee : 2≤e) (bi : i≤B) (bj : j≤B) (be : e≤B) :
    18+162*t<6*(B+7)+4 := by
  let H:=18+162*t
  let M:=B+7
  let I:=i+(7-i)
  let J:=j+(7-i)
  change H<6*M+4
  by_contra! wide
  have ic : I≤M := by dsimp [I,M]; omega
  have jc : J≤M := by dsimp [J,M]; omega
  have leI : 7≤I := by dsimp [I]; omega
  have nn:=lower_native H z I row (by dsimp [H]; omega) leI (by omega)
  have eq : run I z=run J y := by dsimp only [I,J]; rw [run_add i,run_add j,lower]
  rw [eq] at nn
  have up:=affine_tail upper
  have yy : y≤2^(e+v) := by
    have powpos : 1≤(3:ℕ)^(grade e (3*y)) := Nat.one_le_pow _ _ (by decide)
    have mul:=Nat.mul_le_mul_right (3*y) powpos
    simp only [one_mul] at mul
    omega
  have xx : run J y≤2^(J+(e+v)) := by
    rw [pow_add]
    exact (grow J y).trans (Nat.mul_le_mul_left _ yy)
  have pp : 2^(H-I)≤run J y+1 := by
    rw [nn]
    exact Nat.le_mul_of_pos_right _ (by positivity)
  have hr : 4*M+3≤e+v := by
    by_contra! small
    have le : 2^(J+(e+v)+1)≤(2:ℕ)^(H-I) :=
      Nat.pow_le_pow_right (by decide) (by omega)
    have gg : 1<(2:ℕ)^(J+(e+v)) := by
      exact Nat.one_lt_pow (by omega) (by decide)
    rw [pow_succ] at le
    omega
  exact intercept_separation H y I J e (e+v) M (hard_mod t) can short leI ee
    (by dsimp [M]; omega) jc (by omega) (by omega) hr nn up

private theorem at_one (d : ℕ) : run d 1=1 ∨ run d 1=2 := by
  induction d with
  | zero => left; rfl
  | succ d ih =>
    rw [last]
    rcases ih with h|h <;> rw [h] <;> decide

private theorem tail_before_hit {x E v h : ℕ} (large : 1<v)
    (tail : run E x=2^v) (hit : run h x=1) : E+v≤h := by
  have he : E≤h := by
    by_contra! small
    have s: run E x=run (E-h) (run h x) := by
      conv_lhs => rw [show E=h+(E-h) by omega,run_add]
    rw [hit,tail] at s
    have cyc:=at_one (E-h)
    have ll : (2:ℕ)^1<2^v := Nat.pow_lt_pow_right (by decide) large
    omega
  by_contra! small
  let d:=h-E
  have ss : h=E+d := by dsimp [d]; omega
  have dv : d<v := by dsimp [d]; omega
  have pp : 2^v=2^d*2^(v-d) := by rw [←pow_add]; congr 1; omega
  rw [ss,run_add,tail,pp,halve] at hit
  have : 1<(2:ℕ)^(v-d) := Nat.one_lt_pow (by omega) (by decide)
  omega

/-- Every canonical candidate whose upper reaches one sooner than the hard
row and whose two arms physically meet the corresponding row arms has at
least one long ordinary clock, uniformly in all four independent clocks. -/
theorem paired_clock_barrier (t z y i j k l h B : ℕ)
    (row : 81*z+271=2^(18+162*t)) (can : y%48=17)
    (lower : run i z=run j y) (upper : run k (3*z)=run l (3*y))
    (hit : run h (3*y)=1) (short : h<18+162*t)
    (bi : i≤B) (bj : j≤B) (bk : k≤B) (bl : l≤B) :
    18+162*t<5*(B+9)+4 := by
  let H:=18+162*t
  let M:=B+9
  let I:=i+(7-i)
  let J:=j+(7-i)
  let d:=max (9-k) 2
  let K:=k+d
  let E:=l+d
  change H<5*M+4
  by_contra! wide
  have ic : I≤M := by dsimp [I,M]; omega
  have jc : J≤M := by dsimp [J,M]; omega
  have kc : K≤M := by dsimp [K,d,M]; omega
  have ec : E≤M := by dsimp [E,d,M]; omega
  have ee : 2≤E := by dsimp [E,d]; omega
  have lo : 7≤I := by dsimp [I]; omega
  have nine : 9≤K := by dsimp [K,d]; omega
  have nn:=lower_native H z I row (by dsimp [H]; omega) lo (by omega)
  have zz:=upper_native H z K row (by dsimp [H]; omega) nine (by omega)
  have cmp : run I z=run J y := by dsimp only [I,J]; rw [run_add i,run_add j,lower]
  have cmu : run K (3*z)=run E (3*y) := by dsimp only [K,E]; rw [run_add k,run_add l,upper]
  rw [cmp] at nn
  rw [cmu] at zz
  have first:=tail_before_hit (by omega : 1<H-K) zz hit
  apply intercept_separation H y I J E (E+(H-K)) M (hard_mod t) can
    (by change h<H at short; omega) lo ee ec jc (by omega) (by omega) (by omega) nn
    (affine_tail zz)

/-- The displayed exponent is exactly the first upper hit of one. -/
theorem hard_first_hit (t z : ℕ) (row : 81*z+271=2^(18+162*t)) :
    run (18+162*t) (3*z)=1 ∧ ∀ h<18+162*t, run h (3*z)≠1 := by
  let H:=18+162*t
  change run H (3*z)=1 ∧ ∀ h<H, run h (3*z)≠1
  have hh : 9≤H := by dsimp [H]; omega
  constructor
  · simpa using upper_native H z H row hh hh le_rfl
  · intro h ht hit
    by_cases h9 : 9≤h
    · have pure:=upper_native H z h row hh h9 (by omega)
      have : 1<(2:ℕ)^(H-h) := Nat.one_lt_pow (by omega) (by decide)
      omega
    · have tiny : 2^h≤(2:ℕ)^8 := Nat.pow_le_pow_right (by decide) (by omega)
      have huge : (2:ℕ)^18≤2^H := Nat.pow_le_pow_right (by decide) (by dsimp [H]; omega)
      have slope:=affine h (3*z)
      rw [hit,mul_one] at slope
      have g : 1≤(3:ℕ)^(grade h (3*z)) := Nat.one_le_pow _ _ (by decide)
      have v:=Nat.mul_le_mul_right (3*z) g
      change 81*z+271=2^H at row
      omega

#print axioms hard_first_hit
#print axioms hard_prefixes
#print axioms lower_native
#print axioms upper_native
#print axioms short_upper_tail_barrier
#print axioms paired_clock_barrier
end ClockBarrier
