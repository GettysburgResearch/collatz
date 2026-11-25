import AllDepthCenter
import MersenneBarrier

/-! Repeat the eleven-step negative cycle at two distinct phases, then
continue to a Mersenne and a power of two on the original positive arms. -/
namespace RationalCenterPump
open CollatzReverseBasin WordRank

private theorem entry (w L : Nat) (eq : 81*w+2399=128*L) :
    run 7 w+17=L ∧ run 7 (3*w)+55=3*L := by
  let q:=w/128
  have row : w=128*q+81 := by dsimp [q]; omega
  obtain ⟨low,_⟩ := liftPrefix 7 q 81
  obtain ⟨up,_⟩ := liftPrefix 7 (3*q) 243
  have w3 : 3*w=128*(3*q)+243 := by omega
  rw [show (2:Nat)^7=128 by decide,←row] at low
  rw [show (2:Nat)^7=128 by decide,←w3] at up
  change run 7 w=81*q+53 at low
  change run 7 (3*w)=81*(3*q)+155 at up
  omega

private theorem lap (c x t : Nat) (phase : c=17 ∨ c=55)
    (eq : x+c=2048*t) : run 11 x+c=2187*t ∧ odds 11 x=7 := by
  have pos : 0<t := by rcases phase with h|h <;> omega
  have split : x=2048*(t-1)+(2048-c) := by rcases phase with h|h <;> omega
  obtain ⟨endp,cnt⟩ := liftPrefix 11 (t-1) (2048-c)
  rw [show (2:Nat)^11=2048 by decide,←split] at endp cnt
  rcases phase with rfl|rfl
  · change run 11 x=2187*(t-1)+2170 at endp
    change odds 11 x=7 at cnt
    exact ⟨by omega,cnt⟩
  · change run 11 x=2187*(t-1)+2132 at endp
    change odds 11 x=7 at cnt
    exact ⟨by omega,cnt⟩

/-- No bound on the number of complete laps. All entries and exits are
ordinary, and one binary factor per physical clock is explicitly supplied. -/
theorem repeated_laps (n c x t : Nat) (phase : c=17 ∨ c=55)
    (eq : x+c=2^(11*n)*t) :
    run (11*n) x+c=3^(7*n)*t ∧ odds (11*n) x=7*n := by
  induction n generalizing x t with
  | zero => simpa [run,odds] using eq
  | succ n ih =>
    rw [show 11*(n+1)=11+11*n by omega,show 7*(n+1)=7*n+7 by omega,runAdd,oddsAdd,pow_add]
    rw [show 11*(n+1)=11+11*n by omega,pow_add,Nat.mul_assoc] at eq
    obtain ⟨e,p⟩ := lap c x (2^(11*n)*t) phase eq
    obtain ⟨endp,cnt⟩ := ih (run 11 x) (2187*t) (by rw [e]; ring)
    exact ⟨by rw [endp]; ring,by omega⟩

private theorem finish (Q N x y : Nat) (eq : 6561*Q=8192*N+101936)
    (lx : x+17=Q) (uy : y+55=3*Q) :
    run 11 x+1=4*N ∧ run 13 y=N ∧ odds 11 x=8 ∧ odds 13 y=7 := by
  let k:=Q/8192
  have qr : Q=8192*k+48 := by dsimp [k]; omega
  have nr : N=6561*k+26 := by omega
  obtain ⟨el,ol⟩ := liftPrefix 11 (4*k) 31
  obtain ⟨eu,ou⟩ := liftPrefix 13 (3*k) 89
  have a : 2^11*(4*k)+31=x := by omega
  have b : 2^13*(3*k)+89=y := by omega
  rw [a] at el ol
  rw [b] at eu ou
  change run 11 x=6561*(4*k)+103 at el
  change run 13 y=2187*(3*k)+26 at eu
  exact ⟨by omega,by omega,ol,ou⟩

/-- Positive ordinary lower and upper traces for the parameterized pump.
Use N=2^(j−2); then their endpoints are 2^j−1 and 2^(j−2). -/
theorem physical (n t w N : Nat) (start : 81*w+2399=128*(2^(11*n)*t))
    (target : 6561*(3^(7*n)*t)=8192*N+101936) :
    run (18+11*n) w+1=4*N ∧ run (20+11*n) (3*w)=N ∧
    odds (18+11*n) w=12+7*n ∧ odds (20+11*n) (3*w)=11+7*n := by
  obtain ⟨le,ue⟩ := entry _ _ start
  let ar:=11*n
  obtain ⟨ll,lp⟩ := repeated_laps n 17 (run 7 w) t (Or.inl rfl) le
  obtain ⟨ul,up⟩ := repeated_laps n 55 (run 7 (3*w)) (3*t) (Or.inr rfl) (by rw [ue]; ring)
  obtain ⟨lo,hi,pl,pu⟩ := finish (3^(7*n)*t) N _ _ target ll (by rw [ul]; ring)
  obtain ⟨_,p7⟩ := liftPrefix 7 (w/128) 81
  obtain ⟨_,q7⟩ := liftPrefix 7 (3*(w/128)) 243
  have row : w=128*(w/128)+81 := by omega
  rw [show (2:Nat)^7=128 by decide,←row] at p7
  rw [show 2^7*(3*(w/128))+243=3*w by omega] at q7
  change odds 7 w=4 at p7
  change odds 7 (3*w)=4 at q7
  rw [show 18+11*n=7+(11*n+11) by omega,show 20+11*n=7+(11*n+13) by omega,
    runAdd,runAdd,runAdd 7,runAdd,oddsAdd,oddsAdd,oddsAdd 7,oddsAdd]
  exact ⟨lo,hi,by omega,by omega⟩

theorem smaller (n t w z N : Nat) (start : 81*w+2399=128*(2^(11*n)*t))
    (target : 6561*(3^(7*n)*t)=8192*N+101936) (parent : 81*z+271=512*N) :
    w<z := by
  have bound : 2^(11*n)≤3^(7*n) := by
    rw [pow_mul,pow_mul]
    exact Nat.pow_le_pow_left (by decide) n
  have cost := Nat.mul_le_mul_right t bound
  omega

private theorem run_basin (h x : Nat) : Basin (run h x) ↔ Basin x := by
  induction h generalizing x with
  | zero => rfl
  | succ h ih => exact (ih (shortcut x)).trans (SignedCycleDilation.basin_value 1 x)

private theorem dyadic (j : Nat) : Basin (2^j) := by
  rw [←run_basin j]
  have h := (halves j 1).1
  simpa only [Nat.mul_one] using (show Basin (run j (2^j*1)) by rw [h]; exact ⟨0,rfl⟩)

/-- A pump on the actual e=6 parent excludes that parent as a least defect. -/
theorem least_excluded (n t w z m : Nat) (wr : w%48=17)
    (start : 81*w+2399=128*(2^(11*n)*t))
    (target : 6561*(3^(7*n)*t)=8192*2^(9+162*m)+101936)
    (parent : 81*z+271=512*2^(9+162*m))
    (bad : CollatzTwoOdd.ReverseDefect z)
    (least : ∀ y, CollatzTwoOdd.ReverseDefect y → z≤y) : False := by
  let j:=11+162*m
  have ef : 4*2^(9+162*m)=2^j := by
    dsimp [j]; rw [show 11+162*m=2+(9+162*m) by omega,pow_add (2:Nat) 2 (9+162*m)]; rfl
  have old : 81*z+271=128*2^j := by rw [←ef]; omega
  obtain ⟨lo,hi,_,_⟩ := physical n t w _ start target
  have orig := (MersenneBarrier.mersenne_prefix z j old).1
  change run 7 z+1=2^j at orig
  have same : run (18+11*n) w=run 7 z := by rw [ef] at lo; omega
  apply Nat.not_le_of_gt (smaller n t w z _ start target parent) (least w ?_)
  refine ⟨wr,(run_basin _ _).mp (hi ▸ dyadic _),fun good => ?_⟩
  exact bad.2.2 ((run_basin 7 z).mp (same ▸ (run_basin _ _).mpr good))

#print axioms repeated_laps
#print axioms physical
#print axioms smaller
#print axioms least_excluded


private theorem small_period (m : Nat) : ∃ v : Nat, 2^(162*m)=1+243*v := by
  induction m with
  | zero => exact ⟨0,by decide⟩
  | succ m ih =>
    obtain ⟨v,hv⟩ := ih
    let a:Nat:=(2^162-1)/243
    have ha : (2:Nat)^162=1+243*a := by decide
    refine ⟨v+a+243*v*a,?_⟩
    rw [Nat.mul_succ,pow_add,hv,ha]; ring

private theorem exponent_class (e : Nat) (h : 2^e%243=77) : e%162=29 := by
  have eq : e=162*(e/162)+e%162 := (Nat.div_add_mod ..).symm
  obtain ⟨v,hv⟩ := small_period (e/162)
  have val : 2^e%243=2^(e%162)%243 := by
    conv_lhs => rw [eq,pow_add,hv,Nat.mul_mod]
    rw [show (1+243*v)%243=1 by omega,one_mul,Nat.mod_mod]
  have tbl : ∀ i : Fin 162, 2^i.val%243=77 → i.val=29 := by decide +kernel
  exact tbl ⟨e%162,Nat.mod_lt _ (by decide)⟩ (val ▸ h)

/-- Every lap count n occurs on cofinally many ordinary e=6 parameters,
with the common physical start and target used above. -/
theorem cofinal_pumps (n L : Nat) : ∃ m t w : Nat, L≤m ∧ w%48=17 ∧
    81*w+2399=128*(2^(11*n)*t) ∧
    6561*(3^(7*n)*t)=8192*2^(9+162*m)+101936 := by
  let g:=7*n
  let h:=11*n
  let D:Nat:=3^(8+g)
  let K:Nat:=2561*2^(161*h)
  let B:Nat:=D*K-13047808
  have drow : D=6561*3^g := by dsimp [D]; rw [pow_add]; rfl
  have dh : 6561≤D := by
    rw [drow]; have := (show 0<(3:Nat)^g by positivity); omega
  have kh : 2561≤K := by
    dsimp [K]; have := (show 0<(2:Nat)^(161*h) by positivity); omega
  have off : B+13047808=D*K := by
    have := Nat.mul_le_mul dh kh
    dsimp [B]; omega
  have bunit : B%3≠0 := by
    have eq : D*K=3*(2187*(3^g*K)) := by rw [drow]; ring
    rw [eq] at off; omega
  obtain ⟨e,k,large,ex⟩ := TernaryPowerLift.cofinal (12+g) B (29+162*L) bunit
  have stride : 3^(12+g+1)=D*243 := by
    dsimp [D]; rw [show 12+g+1=(8+g)+5 by omega,pow_add]; rfl
  let q:=K+243*k
  have qe : 2^e+13047808=D*q := by
    rw [ex,stride]; dsimp [q]; rw [Nat.add_right_comm B _ 13047808,off]; ring
  have h243 : 2^e%243=77 := by
    rw [drow] at qe
    have dm : 6561*3^g*q=243*(27*(3^g*q)) := by ring
    rw [dm] at qe; omega
  have cl := exponent_class e h243
  let m:=e/162
  have eRow : e=29+162*m := by dsimp [m]; omega
  have multiple : (128:Nat) ∣ D*q := by
    refine ⟨2^(22+162*m)+101936,?_⟩
    rw [←qe,eRow,show 29+162*m=7+(22+162*m) by omega,pow_add]; ring
  have cp : Nat.Coprime 128 D := Nat.Coprime.pow_right _ (by decide : Nat.Coprime 128 3)
  obtain ⟨t,qt⟩ := cp.dvd_of_dvd_mul_left multiple
  obtain ⟨y,hy⟩ := small_period h
  have scale : 2^h*q=2561+243*(2561*y+2^h*k) := by
    dsimp [q,K]
    rw [show 2^h*(2561*2^(161*h)+243*k)=2561*(2^h*2^(161*h))+243*(2^h*k) by ring,
      ←pow_add,show h+161*h=162*h by omega,hy]; ring
  let w:=2+3*(2561*y+2^h*k)
  have start : 81*w+2399=128*(2^(11*n)*t) := by
    change 81*w+2399=128*(2^h*t)
    rw [qt] at scale
    dsimp [w]; linarith only [scale]
  have wr : w%48=17 := by
    have r3 : w%3=2 := by dsimp [w]; omega
    omega
  refine ⟨m,t,w,by omega,wr,start,?_⟩
  rw [qt,eRow,drow,show 29+162*m=20+(9+162*m) by omega,pow_add] at qe
  change 6561*(3^g*t)=8192*2^(9+162*m)+101936
  linarith only [qe]

/-- At each prescribed depth infinitely many parent parameters are actually
excluded as possible least defects. -/
theorem cofinal_exclusions (n L : Nat) : ∃ m, L≤m ∧ ∀ z : Nat,
    81*z+271=512*2^(9+162*m) → CollatzTwoOdd.ReverseDefect z →
    (∀ y, CollatzTwoOdd.ReverseDefect y → z≤y) → False := by
  obtain ⟨m,t,w,large,res,sta,tar⟩ := cofinal_pumps n L
  exact ⟨m,large,fun z parent bad least => least_excluded n t w z m res sta tar parent bad least⟩

#print axioms cofinal_pumps
#print axioms cofinal_exclusions


set_option maxRecDepth 10000 in
private theorem growth (n : Nat) : (2048+n)*2048^n ≤ 2048*2187^n := by
  induction n with
  | zero => decide
  | succ n ih =>
    rw [pow_succ (2048:Nat),pow_succ (2187:Nat)]
    have sc := Nat.mul_le_mul_right 2187 ih
    calc
      (2048+(n+1))*(2048^n*2048) ≤ ((2048+n)*2048^n)*2187 := by
        have m := Nat.mul_le_mul_right (2048^n) (show (2048+(n+1))*2048≤(2048+n)*2187 by omega)
        simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using m
      _ ≤ _ := by simpa only [Nat.mul_assoc] using sc

private theorem size_guard (Q N : Nat) (h : 6561*Q=8192*N+101936) (low : 512≤N) :
    128*Q+271<512*N := by omega

set_option maxRecDepth 10000 in
/-- At any prescribed multiplicative saving one can choose arbitrarily large
ordinary parameters with a strictly smaller query achieving that saving.
The same query has both actual terminal values. -/
theorem arbitrary_saving (F L : Nat) : ∃ m n w z : Nat, L≤m ∧ w%48=17 ∧
    81*z+271=512*2^(9+162*m) ∧ F*w<z ∧
    run (18+11*n) w+1=2^(11+162*m) ∧ run (20+11*n) (3*w)=2^(9+162*m) := by
  let n:=2048*F
  obtain ⟨m,t,w,large,res,sta,tar⟩:=cofinal_pumps n L
  obtain ⟨z,_,par,_,_⟩:=MersenneBarrier.mersenne_family m
  let N:=2^(9+162*m)
  have pf : 4*N=2^(11+162*m) := by
    dsimp [N]; rw [show 11+162*m=2+(9+162*m) by omega,pow_add (2:Nat) 2 (9+162*m)]; rfl
  have eq : 81*z+271=512*N := by rw [Nat.add_comm (162*m) 11,←pf] at par; omega
  have qlt : 128*(3^(7*n)*t)+271<512*N := by
    have lower : 512≤N := Nat.pow_le_pow_right (by decide : 0<2) (show 9≤9+162*m by omega)
    exact size_guard _ N tar lower
  have g := growth n
  have eff : F*2^(11*n)≤3^(7*n) := by
    rw [pow_mul (2:Nat) 11 n,pow_mul (3:Nat) 7 n]
    change F*2048^n≤2187^n
    have e : (2048+n)*2048^n=2048*(2048^n+F*2048^n) := by dsimp [n]; ring
    rw [e] at g
    exact Nat.le_trans (Nat.le_add_left ..) (Nat.le_of_mul_le_mul_left g (by decide))
  have ac := Nat.mul_le_mul_right t eff
  have started := congrArg (fun v : Nat => F*v) sta
  change F*(81*w+2399)=F*(128*(2^(11*n)*t)) at started
  have small : F*w<z := by linarith only [ac,started,qlt,eq,Nat.zero_le F]
  obtain ⟨low,up,_,_⟩ := physical n t w _ sta tar
  exact ⟨m,n,w,z,large,res,eq,small,low.trans pf,up⟩

#print axioms arbitrary_saving
end RationalCenterPump
