import MinimumFailure

namespace Collatz.MovingOrigin
open Collatz.SourceDeletion Collatz.MinimumFailure

private theorem cat (a b n : Nat) : run (a+b) n = run b (run a n) := by
  induction a generalizing n with
  | zero => simp [run]
  | succ a ih => simpa [Nat.succ_add,run] using ih (step n)

private theorem counts (a b n : Nat) : odds (a+b) n = odds a n + odds b (run a n) := by
  induction a generalizing n with
  | zero => simp [run,odds]
  | succ a ih => simp only [Nat.succ_add,run,odds,ih]; omega

private theorem laps (k : Nat) : run (2*k) 1=1 ∧ odds (2*k) 1=k := by
  induction k with
  | zero => decide
  | succ k ih =>
    rw [show 2*(k+1)=2+2*k by ring,cat,counts]
    change run (2*k) 1=1 ∧ 1+odds (2*k) 1=k+1
    omega

private theorem parity_three (q : Nat) : 3^q%2=1 := by
  induction q with
  | zero => decide
  | succ q ih => rw [pow_succ,Nat.mul_mod,ih]

private theorem lift_count (h v u : Nat) : odds h (v+2^h*u)=odds h v := by
  induction h generalizing v u with
  | zero => rfl
  | succ h ih =>
    have p : (v+2^(h+1)*u)%2=v%2 := by rw [show 2^(h+1)*u=2*(2^h*u) by ring]; omega
    by_cases ev : v%2=0
    · have stepLift : step (v+2^(h+1)*u)=step v+2^h*u := by
        rw [show 2^(h+1)*u=2*(2^h*u) by ring]
        unfold step; split <;> omega
      simp only [odds,stepLift,ih,p]
    · have stepLift : step (v+2^(h+1)*u)=step v+2^h*(3*u) := by
        rw [show 2^(h+1)*u=2*(2^h*u) by ring,show 2^h*(3*u)=3*(2^h*u) by ring]
        unfold step; split <;> omega
      simp only [odds,stepLift,ih,p]

private theorem merger {u q : Nat} (odd : u%2=1) :
    step (1+3^(q+1)*u)=step (3^q*u) ∧ (3^q*u)%2=1 ∧ (1+3^(q+1)*u)%2=0 := by
  have eq : (3^q*u)%2=1 := by rw [Nat.mul_mod,parity_three,odd]
  rw [show 3^(q+1)*u=3*(3^q*u) by ring]
  unfold step; split <;> split <;> omega

/-- The shifted low representative of the lower arm can supply an actual
ternary source even when the carry itself has insufficient binary time. -/
theorem two_reference_return {v c e u p : Nat} (odd : u%2=1)
    (lower : run e (v+c)=1) (lowerGrade : odds e (v+c)=p+1) :
    Good (v+c+2^e*u) ↔ Good (3^p*u) := by
  have actual := lift e (v+c) u
  rw [lower,lowerGrade] at actual
  rw [←good_run e,actual,←good_step (1+3^(p+1)*u),(merger (q:=p) odd).1,good_step]

/-- At the new upper source the suffix is attached by a single odd departure.
The old prefix costs exactly r more odd departures than the replacement. -/
theorem original_upper_suffix {v e u r : Nat} (odd : u%2=1)
    (upper : run e v=1) (grade : odds e v=r+1) (K : Nat) :
    run ((e+1)+K) (v+2^e*u)=run (1+K) (3^r*u) ∧
    odds ((e+1)+K) (v+2^e*u)=r+odds (1+K) (3^r*u) := by
  have actual := lift e v u
  rw [upper,grade] at actual
  have prefixCount := lift_count e v u
  rw [grade] at prefixCount
  obtain ⟨meet,oa,ob⟩ := merger (q:=r) odd
  have eq : run (e+1) (v+2^e*u)=step (3^r*u) := by rw [cat,actual]; exact meet
  have co : odds (e+1) (v+2^e*u)=r+1 := by rw [counts,prefixCount,actual]; simp [odds,ob]
  rw [cat (e+1),cat 1,counts (e+1),counts 1,eq,co]
  simp [run,odds,oa,Nat.add_assoc]

private theorem rising {n : Nat} (big : 2<n) (e : Nat) (x : Nat)
    (atClock : run e x=n) {H : Nat} (hit : run H x=1) : e<H := by
  by_contra no
  obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le (show H≤e by omega)
  rw [hd,cat,hit] at atClock
  have small (j a : Nat) (ha : a=1 ∨ a=2) : run j a=1 ∨ run j a=2 := by
    induction j generalizing a with
    | zero => exact ha
    | succ j ih =>
      apply ih (step a)
      rcases ha with h|h <;> subst a <;> decide
  have s := small d 1 (Or.inl rfl)
  omega

/-- A true first or later upper hit automatically covers the matching clock
when the positive high term leaves its endpoint above the base cycle. -/
theorem paired_hit {v c e u p r H : Nat} (odd : u%2=1)
    (low : run e (v+c)=1) (up : run e v=1)
    (lp : odds e (v+c)=p+1) (ur : odds e v=r+1)
    (bad : ¬Good (v+c+2^e*u)) (hit : run H (v+2^e*u)=1) :
    ¬Good (3^p*u) ∧ ∃ K, H=e+1+K ∧ run (1+K) (3^r*u)=1 ∧
      odds H (v+2^e*u)=r+odds (1+K) (3^r*u) := by
  have actual := lift e v u
  rw [up,ur] at actual
  have pos : 0<3^r*u := Nat.mul_pos (Nat.pow_pos (by decide)) (by omega)
  have big : 2<1+3^(r+1)*u := by rw [show 3^(r+1)*u=3*(3^r*u) by ring]; omega
  have lt := rising big _ _ actual hit
  let K := H-(e+1)
  have clk : H=e+1+K := by dsimp [K]; omega
  obtain ⟨m,q⟩ := original_upper_suffix odd up ur K
  refine ⟨fun good => bad ((two_reference_return (v:=v) (c:=c) odd low lp).mpr good),
    K,clk,?_,?_⟩
  · rwa [clk,m] at hit
  · rwa [clk]

private theorem crossing_five (a : Nat) :
    run 5 (161+256*a)=137+216*a ∧ run 5 (3*(161+256*a))=136+216*a ∧
    (∀ i<5, odds i (161+256*a)<1+odds i (3*(161+256*a))) ∧
    odds 5 (161+256*a)=3 ∧ odds 5 (3*(161+256*a))=2 := by
  have l := lift 5 161 (8*a)
  have u := lift 5 483 (24*a)
  have lo := lift_count 5 161 (8*a)
  have uo := lift_count 5 483 (24*a)
  have eqL : 161+256*a=161+2^5*(8*a) := by ring
  have eqU : 3*(161+256*a)=483+2^5*(24*a) := by ring
  rw [eqL,eqU] at *
  refine ⟨?_,?_,?_,?_,?_⟩
  · change run 5 _=137+27*(8*a) at l; rw [l]; ring
  · change run 5 _=136+9*(24*a) at u; rw [u]; ring
  · intro i hi
    have partialCounts (j t n : Nat) (bound : j≤5) : odds j (n+2^5*t)=odds j n := by
      obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le bound
      rw [hd,pow_add,Nat.mul_assoc,lift_count]
    rw [partialCounts i _ _ (by omega),partialCounts i _ _ (by omega)]
    have cases : i=0 ∨ i=1 ∨ i=2 ∨ i=3 ∨ i=4 := by omega
    rcases cases with h|h|h|h|h <;> subst i <;> decide
  · exact lo
  · exact uo

private theorem origins (k : Nat) :
    run (13+2*k) 8=1 ∧ odds (13+2*k) 8=(4+k)+1 ∧
    run (13+2*k) 9=1 ∧ odds (13+2*k) 9=(5+k)+1 := by
  rw [cat,cat,counts,counts]
  change run (2*k) 1=1 ∧ 5+odds (2*k) 1=4+k+1 ∧ run (2*k) 1=1 ∧
    6+odds (2*k) 1=5+k+1
  obtain ⟨r,o⟩ := laps k
  omega

/-- On this moving first-crossing row the upper has exactly three trailing
binary zeros. Both arms still return to actual neighboring tower ranks,
at any supplied upper hitting rank. The five-clock prefix is charged too. -/
theorem unaligned_crossing {z u k H : Nat} (odd : u%2=1)
    (seed : 27*z=251+2^(18+2*k)*u) (bad : ¬Good z) (hit : run H (3*z)=1) :
    ¬Good (3^(5+k)*u) ∧ ∃ K, H=5+(13+2*k)+1+K ∧
      run (1+K) (3^(4+k)*u)=1 ∧
      odds H (3*z)=(6+k)+odds (1+K) (3^(4+k)*u) := by
  let a := z/256
  let e := 13+2*k
  have power : 2^(18+2*k)=32*2^e := by
    rw [show 18+2*k=5+e by dsimp [e]; omega,pow_add]; rfl
  have div : 2^(18+2*k)=262144*2^(2*k) := by rw [pow_add]; rfl
  have row : z=161+256*a := by dsimp [a]; rw [div,Nat.mul_assoc] at seed; omega
  obtain ⟨lower,upper,_,_,cost⟩ := crossing_five a
  rw [←row] at lower upper cost
  rw [power,Nat.mul_assoc] at seed
  have l : run 5 z=9+2^e*u := by omega
  have h : run 5 (3*z)=8+2^e*u := by omega
  have big : 2<8+2^e*u := by omega
  have after := rising big _ _ h hit
  have clk : H=5+(H-5) := by omega
  have hh := hit
  rw [clk,cat,h] at hh
  have bb : ¬Good (8+1+2^e*u) := by
    change ¬Good (9+2^e*u)
    rw [←l,good_run]; exact bad
  obtain ⟨up,ur,low,lp⟩ := origins k
  obtain ⟨newBad,K,t,terminal,save⟩ := paired_hit odd low up lp ur bb hh
  refine ⟨newBad,K,by omega,terminal,?_⟩
  rw [clk,counts,cost,h,save]; omega

private theorem price (k : Nat) (large : 84≤k) :
    2^40*27*3^(5+k)<2^(18+2*k) := by
  obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le large
  subst k
  clear large
  induction d with
  | zero => decide
  | succ d ih =>
    have x : 5+(84+(d+1))=(5+(84+d))+1 := by omega
    have y : 18+2*(84+(d+1))=(18+2*(84+d))+2 := by omega
    rw [x,y,pow_succ (3:Nat) (5+(84+d)),pow_add (2:Nat) (18+2*(84+d)) 2]
    have h := Nat.mul_lt_mul_of_pos_right ih (by decide : 0<3)
    rw [show 2^40*27*(3^(5+(84+d))*3)=(2^40*27*3^(5+(84+d)))*3 by ring]
    change _<2^(18+2*(84+d))*4
    omega

/-- The bad representative from the unaligned crossing is strictly below
the quantitative return floor, uniformly over the remaining cofactor. -/
theorem unaligned_floor {z u k : Nat} (positive : 0<u)
    (seed : 27*z=251+2^(18+2*k)*u) (large : 84≤k) :
    2^40*(3^(5+k)*u)<z := by
  have s := Nat.mul_lt_mul_of_pos_right (price k large) positive
  have eq : 2^40*27*3^(5+k)*u=27*(2^40*(3^(5+k)*u)) := by ring
  rw [eq] at s
  omega

/-- A source-preserving projection at a true first equal-grade crossing. The
two finite low-reference hits have grades one and two. The exact eight-odd
saving refers to the supplied hit, even when it is the first one. -/
theorem canonical_to_canonical (a : Nat) :
    let z := 89585+48*2^19*a
    let w := 1121+48*3^8*a
    z%48=17 ∧ w%48=17 ∧ 0<w ∧ w<z ∧
    (∀ i<14, odds i z<1+odds i (3*z)) ∧ odds 14 z=1+odds 14 (3*z) ∧
    run 14 z=10+2^5*w ∧ run 14 (3*z)=3+2^5*w ∧
    (Good z ↔ Good w) ∧
    ∀ H, run H (3*z)=1 → ∃ K, H=20+K ∧ run (1+K) (3*w)=1 ∧
      odds H (3*z)=8+odds (1+K) (3*w) := by
  dsimp only
  let z := 89585+48*2^19*a
  let w := 1121+48*3^8*a
  have zl : z=89585+2^14*(32*48*a) := by dsimp [z]; ring
  have zu : 3*z=268755+2^14*(3*32*48*a) := by dsimp [z]; ring
  have l : run 14 z=10+2^5*w := by
    rw [zl,lift]; change 35882+6561*(32*48*a)=10+2^5*w; dsimp [w]; ring
  have u : run 14 (3*z)=3+2^5*w := by
    rw [zu,lift]; change 35875+2187*(3*32*48*a)=3+2^5*w; dsimp [w]; ring
  have cL : odds 14 z=8 := by rw [zl,lift_count]; decide
  have cU : odds 14 (3*z)=7 := by rw [zu,lift_count]; decide
  have past (j t n : Nat) (b : j≤14) : odds j (n+2^14*t)=odds j n := by
    obtain ⟨d,eq⟩ := Nat.exists_eq_add_of_le b
    rw [eq,pow_add,Nat.mul_assoc,lift_count]
  have first : ∀ j<14, odds j z<1+odds j (3*z) := by
    intro j b
    rw [zl,show 3*(89585+2^14*(32*48*a))=268755+2^14*(3*32*48*a) by ring,
      past _ _ _ (by omega),past _ _ _ (by omega)]
    have small : ∀ i : Fin 14, odds i.val 89585<1+odds i.val 268755 := by decide
    exact small ⟨j,b⟩
  have mw : w%48=17 := by dsimp [w]; omega
  have ow : w%2=1 := by omega
  have lx : Good (10+2^5*w) ↔ Good w := by
    simpa using (two_reference_return (v:=3) (c:=7) (e:=5) (u:=w) (p:=0)
      ow (by decide) (by decide))
  refine ⟨by omega,mw,by dsimp [w]; omega,by dsimp [w,z]; omega,first,
    by rw [cL,cU],l,u,?_,?_⟩
  · change Good z ↔ Good w
    rw [←good_run 14 z,l]; exact lx
  · intro H hit
    change run H (3*z)=1 at hit
    have b := rising (by omega : 2<3+2^5*w) 14 (3*z) u hit
    let J := H-14
    have h : H=14+J := by dsimp [J]; omega
    have suffix := hit
    rw [h,cat,u] at suffix
    have atFive := lift 5 3 w
    change run 5 (3+2^5*w)=1+9*w at atFive
    have pw : 0<w := by dsimp [w]; omega
    have j := rising (by omega : 2<1+9*w) _ _ atFive suffix
    let K := J-6
    have clock : J=6+K := by dsimp [K]; omega
    obtain ⟨endp,work⟩ := original_upper_suffix (u:=w) (v:=3) (e:=5) (r:=1)
      ow (by decide) (by decide) K
    change run (6+K) _=run (1+K) (3*w) at endp
    change odds (6+K) _=1+odds (1+K) (3*w) at work
    refine ⟨K,by omega,?_,?_⟩
    · rwa [clock,endp] at suffix
    · change odds H (3*z)=8+odds (1+K) (3*w)
      rw [h,counts,cU,u,clock,work]; omega

#print axioms canonical_to_canonical
#print axioms two_reference_return
#print axioms original_upper_suffix
#print axioms paired_hit
#print axioms unaligned_crossing
#print axioms unaligned_floor
end Collatz.MovingOrigin
