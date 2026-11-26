import WordRank

namespace OrdinaryWordRealization
open CollatzReverseBasin WordRank

/-- State and odd count through the original triple's three-odd macro. -/
theorem upper (b t z : Nat) (eq : 81*z+271=128*2^(b+2)*t) :
    run (9+b) (3*z)=t ∧ odds (9+b) (3*z)=3 := by
  let r := z/128
  have hr : z=128*r+33 := by dsimp [r]; rw [Nat.mul_assoc] at eq; omega
  let A := 864*r+224
  have Ae : 3*A+64=128*(2^b*t) := by
    dsimp [A]; rw [show 128*2^(b+2)*t=512*(2^b*t) by ring] at eq; omega
  let w := A/64
  have Aw : A=64*w := by dsimp [w]; omega
  have we : 3*w+1=2*(2^b*t) := by omega
  have wo : w%2=1 := by omega
  have sw : shortcut w=2^b*t := by unfold shortcut; split <;> omega
  have h0 : shortcut (3*z)=576*r+149 := by unfold shortcut; split <;> omega
  have h1 : shortcut (576*r+149)=A := by dsimp [A]; unfold shortcut; split <;> omega
  have u2 : run 2 (3*z)=A ∧ odds 2 (3*z)=2 := by
    have o0 : (3*z)%2=1 := by rw [hr]; omega
    have o1 : (576*r+149)%2=1 := by omega
    simp [run,odds,h0,h1,o0,o1]
  have hw := halves 6 w
  have r8 : run 8 (3*z)=w := by
    rw [show 8=2+6 by decide,runAdd,u2.1,Aw]; exact hw.1
  have o8 : odds 8 (3*z)=2 := by
    rw [show 8=2+6 by decide,oddsAdd,u2.1,u2.2,Aw]
    exact congrArg (2+·) hw.2
  have r9 : run 9 (3*z)=2^b*t := by rw [show 9=8+1 by decide,runAdd,r8]; exact sw
  have o9 : odds 9 (3*z)=3 := by
    rw [show 9=8+1 by decide,oddsAdd,r8,o8]; simp [odds,wo]
  rw [runAdd,oddsAdd,r9,o9,(halves b t).1,(halves b t).2]; simp

private theorem oddRun (q t x : Nat) (eq : x+1=2^q*t) :
    run q x+1=3^q*t ∧ odds q x=q := by
  induction q generalizing t x with
  | zero => simpa [run,odds] using eq
  | succ q ih =>
    have h : x+1=2*(2^q*t) := by rw [eq]; ring
    have bit : x%2=1 := by omega
    have step : shortcut x+1=2^q*(3*t) := by
      rw [show 2^q*(3*t)=3*(2^q*t) by ring]
      unfold shortcut; split <;> omega
    obtain ⟨v,c⟩ := ih (3*t) (shortcut x) step
    change run q (shortcut x)+1 = _ ∧ x%2+odds q (shortcut x)=_
    rw [v,c,bit]; constructor <;> ring

/-- The lower arm's exact seven-step take-off, entire ascent, and single
halving. The count in the ascent is q. -/
theorem lower (q t z : Nat) (ot : t%2=1) (eq : 81*z+271=128*2^q*t) :
    run 7 z+1=2^q*t ∧ odds q (run 7 z)=q ∧
    2*run (q+8) z+1=3^q*t := by
  let r := z/128
  have hr : z=128*r+33 := by dsimp [r]; rw [show 128*2^q*t=128*(2^q*t) by ring] at eq; omega
  have h0 : shortcut (128*r+33)=192*r+50 := by unfold shortcut; split <;> omega
  have h1 : shortcut (192*r+50)=96*r+25 := by unfold shortcut; split <;> omega
  have h2 : shortcut (96*r+25)=144*r+38 := by unfold shortcut; split <;> omega
  have h3 : shortcut (144*r+38)=72*r+19 := by unfold shortcut; split <;> omega
  have h4 : shortcut (72*r+19)=108*r+29 := by unfold shortcut; split <;> omega
  have h5 : shortcut (108*r+29)=162*r+44 := by unfold shortcut; split <;> omega
  have h6 : shortcut (162*r+44)=81*r+22 := by unfold shortcut; split <;> omega
  have r7 : run 7 z=81*r+22 := by rw [hr]; simp only [run,h0,h1,h2,h3,h4,h5,h6]
  have r7' : run 7 z+1=2^q*t := by rw [r7]; rw [Nat.mul_assoc] at eq; omega
  obtain ⟨v,c⟩ := oddRun q t _ r7'
  refine ⟨r7',c,?_⟩
  have odd : (3^q*t)%2=1 := by rw [Nat.mul_mod,powOdd,ot]
  rw [show q+8=(7+q)+1 by omega,runAdd,runAdd]
  change 2*shortcut (run q (run 7 z))+1=_
  unfold shortcut; split <;> omega

def FirstHit (x J : Nat) : Prop := run J x=1 ∧ ∀ i<J, run i x≠1

private theorem small (k x : Nat) (h : x=1 ∨ x=2) : run k x=1 ∨ run k x=2 := by
  induction k generalizing x with
  | zero => exact h
  | succ k ih => apply ih; rcases h with rfl|rfl <;> decide

theorem powerFinish (k x e : Nat) (he : 2≤e) (ep : run k x=2^e) :
    FirstHit x (k+e) ∧ odds (k+e) x=odds k x := by
  have tail := halves e 1
  simp only [Nat.mul_one] at tail
  have hp : 2<2^e := by
    have := Nat.pow_le_pow_right (by decide : 0<2) he; omega
  refine ⟨⟨by rw [runAdd,ep,tail.1],?_⟩,by rw [oddsAdd,ep,tail.2,Nat.add_zero]⟩
  intro i il stop
  by_cases before : i≤k
  · obtain ⟨v,rfl⟩ := Nat.exists_eq_add_of_le before
    rw [runAdd,stop] at ep
    rcases small v 1 (Or.inl rfl) with s|s <;> omega
  · let d := i-k
    have id : i=k+d := by dsimp [d]; omega
    obtain ⟨v,hv⟩ := Nat.exists_eq_add_of_le (show d+1≤e by omega)
    have split : 2^e=2^d*2^(v+1) := by rw [←Nat.pow_add]; congr 1; omega
    rw [id,runAdd,ep,split,(halves d _).1,Nat.pow_succ] at stop; omega

private theorem baseClass (q : Nat) :
    ∃ c v : Nat, c%2=1 ∧ c%3≠0 ∧ 128*2^q*c=1648+243*v := by
  obtain ⟨e,k,lb,eq⟩ := TernaryPowerLift.cofinal 4 1 (q+7) (by decide)
  have e' : e=(q+7)+(e-(q+7)) := by omega
  let d := 2^(e-(q+7))
  have prod : 128*2^q*d=1+243*k := by
    calc 128*2^q*d=2^((q+7)+(e-(q+7))) := by dsimp [d]; ring
         _ = _ := by rwa [←e']
  let c := 1648*d+243
  have id : 128*2^q*c=1648+243*(1648*k+128*2^q) := by
    calc _ = 1648*(128*2^q*d)+243*(128*2^q) := by dsimp [c]; ring
         _ = _ := by rw [prod]; ring
  refine ⟨c,1648*k+128*2^q,by dsimp [c];omega,?_,id⟩
  intro bad
  have := congrArg (·%3) id
  rw [Nat.mul_mod,bad] at this; simp at this
  omega

private theorem count_le (h v : Nat) : odds h v≤h := by
  induction h generalizing v with
  | zero => exact Nat.le_refl _
  | succ h ih => change v%2+odds h (shortcut v)≤_; have := ih (shortcut v); omega

/-- Every post-ascent word occurs at every sufficiently large exact
first-hit upper rank, on arbitrarily large positive z in the required row. -/
theorem realization (q : Nat) (hq : 2≤q) (W : List Bool) :
    ∃ s : Nat, 1≤s ∧ s≤W.length+1 ∧ ∀ R L : Nat, ∃ z t J : Nat,
      L≤z ∧ z%48=17 ∧ t%2=1 ∧ 81*z+271=128*2^q*t ∧
      run 7 z+1=2^q*t ∧ odds q (run 7 z)=q ∧
      2*run (q+8) z+1=3^q*t ∧ word W.length (run (q+8) z)=W ∧
      FirstHit (3*z) J ∧ odds J (3*z)=3+s+R := by
  obtain ⟨c,v,co,cu,eqc⟩ := baseClass q
  let A := 3^q*243
  let u := (3^q*c)/2
  have cc : (3^q*c)%2=1 := by rw [Nat.mul_mod,powOdd,co]
  have ue : 3^q*c=2*u+1 := by dsimp [u]; omega
  have Ao : A%2=1 := by dsimp [A]; rw [Nat.mul_mod,powOdd]
  obtain ⟨m,hm⟩ := wordRow W A u Ao
  let b := 486*m+c
  have bo : b%2=1 := by dsimp [b]; omega
  have bu : b%3≠0 := by dsimp [b]; omega
  let s := odds (W.length+1) b
  refine ⟨s,?_,count_le _ _,?_⟩
  · dsimp [s]; change 1≤b%2+odds W.length (shortcut b); omega
  intro R L
  obtain ⟨k,e,hk,he,ep,oc⟩ := exactRankRow (W.length+1) b R (L+1) bu
  let p := 2^W.length*k+m
  let t := 486*p+c
  have tc : t=2^(W.length+1)*(243*k)+b := by dsimp [t,p,b]; ring
  have ot : t%2=1 := by dsimp [t]; omega
  rw [←tc] at ep oc
  let z := 17+3*(v+2*(128*2^q)*p)
  have eq : 81*z+271=128*2^q*t := by
    calc _ = (1648+243*v)+128*2^q*(486*p) := by dsimp [z]; ring
         _ = _ := by rw [←eqc]; dsimp [t]; ring
  have ze : z%48=17 := by
    rw [show 128*2^q*t=16*(8*(2^q*t)) by ring] at eq
    have z3 : z%3=2 := by dsimp [z]; omega
    omega
  have zk : L≤z := by
    have pw := Nat.le_mul_of_pos_left k (Nat.pow_pos (by decide):0<2^W.length)
    have pos : 0<2*(128*2^q) := Nat.mul_pos (by decide) (Nat.mul_pos (by decide) (Nat.pow_pos (by decide)))
    have pp := Nat.le_mul_of_pos_left p pos
    dsimp [z,p] at *; omega
  obtain ⟨l1,l2,l3⟩ := lower q t z ot eq
  have lo : run (q+8) z=A*p+u := by
    have mult : 3^q*t=2*(A*p)+(3^q*c) := by dsimp [A,t]; ring
    rw [mult,ue] at l3; omega
  obtain ⟨j,hj⟩ := Nat.exists_eq_add_of_le hq
  have qj : q=j+2 := by omega
  have up := upper j t z (by rwa [←qj])
  let K := (9+j)+(W.length+1+R)
  have rK : run K (3*z)=2^e := by dsimp [K]; rw [runAdd,up.1,ep]
  have oK : odds K (3*z)=3+s+R := by dsimp [K]; rw [oddsAdd,up.1,up.2,oc]; dsimp [s]; omega
  obtain ⟨first,last⟩ := powerFinish K (3*z) e he rK
  exact ⟨z,t,K+e,zk,ze,ot,eq,l1,l2,l3,lo ▸ hm k,first,last.trans oK⟩

end OrdinaryWordRealization
