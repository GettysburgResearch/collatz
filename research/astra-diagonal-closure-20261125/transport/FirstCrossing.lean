import MinimumFailure

namespace Collatz.FirstCrossing
open Collatz.SourceDeletion Collatz.MinimumFailure

private theorem pos_step {x : Nat} (p : 0<x) : 0<step x := by
  unfold step; split <;> omega

private theorem pos_run {x : Nat} (p : 0<x) (h : Nat) : 0<run h x := by
  induction h generalizing x with
  | zero => exact p
  | succ h ih => exact ih (pos_step p)

private theorem run_add (a b x : Nat) : run (a+b) x=run b (run a x) := by
  induction a generalizing x with
  | zero => simp [run]
  | succ a ih => simpa [Nat.succ_add,run] using ih (step x)

private theorem odds_add (a b x : Nat) : odds (a+b) x=odds a x+odds b (run a x) := by
  induction a generalizing x with
  | zero => simp [odds,run]
  | succ a ih => simp only [Nat.succ_add,odds,run,ih]; omega

private theorem last_run (t z : Nat) : run (t+1) z=step (run t z) := run_add t 1 z
private theorem last_odds (t z : Nat) : odds (t+1) z=odds t z+(run t z)%2 := by
  rw [odds_add t 1]; simp [odds]

private theorem three_odd (k : Nat) : 3^k%2=1 := by
  induction k with
  | zero => decide
  | succ k ih => rw [pow_succ,Nat.mul_mod,ih]

private theorem scaled_step {x y k l : Nat} (strict : y<3^k*x)
    (grade : l+x%2=k+y%2) : step y<3^l*step x := by
  by_cases ex : x%2=0 <;> by_cases ey : y%2=0
  · have h : k=l := by omega
    subst l
    have sx : x=2*step x := by unfold step; split <;> omega
    have sy : y=2*step y := by unfold step; split <;> omega
    rw [sx,sy,show 3^k*(2*step x)=2*(3^k*step x) by ring] at strict
    omega
  · have h : l=k+1 := by omega
    have sx : x=2*step x := by unfold step; split <;> omega
    have sy : 2*step y=3*y+1 := by unfold step; split <;> omega
    rw [h,pow_succ]
    have z := Nat.mul_le_mul_left 3 (show y+1≤3^k*x by omega)
    rw [sx,show 3*(3^k*(2*step x))=2*(3^k*3*step x) by ring] at z
    omega
  · have h : k=l+1 := by omega
    have sx : 2*step x=3*x+1 := by unfold step; split <;> omega
    have sy : y=2*step y := by unfold step; split <;> omega
    rw [h,pow_succ,sy] at strict
    have pp : 0<3^l := Nat.pow_pos (by decide)
    have z := congrArg (fun m : Nat => 3^l*m) sx
    simp only [Nat.mul_add,Nat.mul_one] at z
    rw [show 3^l*(2*step x)=2*(3^l*step x) by ring,
        show 3^l*(3*x)=3^l*3*x by ring] at z
    omega
  · have h : k=l := by omega
    subst l
    have sx : 2*step x=3*x+1 := by unfold step; split <;> omega
    have sy : 2*step y=3*y+1 := by unfold step; split <;> omega
    have q := Nat.mul_lt_mul_of_pos_left strict (by decide : 0<3)
    have z := congrArg (fun m : Nat => 3^k*m) sx
    simp only [Nat.mul_add,Nat.mul_one] at z
    rw [show 3^k*(2*step x)=2*(3^k*step x) by ring,
        show 3^k*(3*x)=3*(3^k*x) by ring] at z
    have p : 0<3^k := Nat.pow_pos (by decide)
    omega

/-- Until the lower arm has *strictly exceeded* the total grade of the upper
arm at some earlier or current prefix, its scaled height is strictly larger
from clock one on. This includes arbitrarily many intervening grade ties. -/
theorem strict_before_overshoot {x j t : Nat} (ox : x%2=1) (rank : 0<j)
    (guard : ∀ i≤t+1, odds i x≤j+odds i (3^j*x)) :
    run (t+1) (3^j*x)<3^(j+odds (t+1) (3^j*x)-odds (t+1) x)*run (t+1) x := by
  induction t with
  | zero =>
    have oy : (3^j*x)%2=1 := by rw [Nat.mul_mod,three_odd,ox]
    simp only [odds,run,Nat.zero_add,ox,oy,Nat.add_sub_cancel]
    have sx : 2*step x=3*x+1 := by unfold step; split <;> omega
    have sy : 2*step (3^j*x)=3*(3^j*x)+1 := by unfold step; split <;> omega
    have z := congrArg (fun m : Nat => 3^j*m) sx
    simp only [Nat.mul_add,Nat.mul_one] at z
    rw [show 3^j*(2*step x)=2*(3^j*step x) by ring,
        show 3^j*(3*x)=3*(3^j*x) by ring] at z
    have p : 1<3^j := Nat.one_lt_pow (by omega) (by decide)
    omega
  | succ t ih =>
    have prev := ih (fun i h => guard i (by omega))
    have ga := guard (t+1) (by omega)
    have gb := guard (t+1+1) (by omega)
    rw [last_odds (t+1) x,last_odds (t+1) (3^j*x)] at gb
    rw [last_run (t+1),last_run (t+1),last_odds (t+1),last_odds (t+1)]
    apply scaled_step prev
    omega

/-- At a synchronous equal-grade merger some strictly earlier prefix has
already overshot. The first balance itself has a positive integral gap. -/
theorem meeting_requires_overshoot {x j t : Nat} (ox : x%2=1) (rank : 0<j)
    (balance : odds (t+1) x=j+odds (t+1) (3^j*x))
    (meet : run (t+1) x=run (t+1) (3^j*x)) :
    ∃ i<t+1, j+odds i (3^j*x)<odds i x := by
  by_contra n
  have guard : ∀ i≤t+1, odds i x≤j+odds i (3^j*x) := by
    intro i h; by_cases it : i=t+1
    · simpa [it] using balance.le
    · by_contra g; exact n ⟨i,by omega,by omega⟩
  have p := strict_before_overshoot ox rank guard
  rw [←balance,Nat.sub_self,pow_zero,one_mul,meet] at p
  omega

/-- A floor along the entire physical lower prefix bounds its accumulated
additive error by the number of odd inputs, independently of its even clock. -/
theorem floor_budget (h x M : Nat) (floor : ∀ i≤h, M≤run i x)
    (budget : odds h x<3*M) :
    (3*M-odds h x)*(2^h*run h x)≤3*M*(3^(odds h x)*x) := by
  induction h generalizing x with
  | zero => simp [odds,run]
  | succ h ih =>
    have hx : M≤x := floor 0 (by omega)
    have future (i : Nat) (le : i≤h) : M≤run i (step x) := floor (i+1) (by omega)
    let q := odds h (step x)
    change q+x%2<3*M at budget
    have next := ih (step x) future (by change q<3*M; omega)
    change (3*M-q)*(2^h*run h (step x))≤3*M*(3^q*step x) at next
    change (3*M-(q+x%2))*(2^(h+1)*run h (step x))≤3*M*(3^(q+x%2)*x)
    by_cases e : x%2=0
    · have sx : 2*step x=x := by unfold step; split <;> omega
      rw [e,Nat.add_zero,pow_succ]
      calc
        _ = 2*((3*M-q)*(2^h*run h (step x))) := by ring
        _ ≤ 2*(3*M*(3^q*step x)) := Nat.mul_le_mul_left 2 next
        _ = 3*M*(3^q*(2*step x)) := by ring
        _ = _ := by rw [sx]
    · have o : x%2=1 := by omega
      have sx : 2*step x=3*x+1 := by unfold step; split <;> omega
      rw [o,pow_succ,pow_succ]
      let d := 3*M-(q+1)
      let a := 3*M-q
      have da : d+1=a := by dsimp [d,a]; omega
      have daPos : 0<a := by omega
      have dsmall : d≤3*x := by dsimp [d]; omega
      have charge : d*(2*step x)≤a*(3*x) := by rw [sx,←da,Nat.mul_add,Nat.add_mul,Nat.mul_one,Nat.one_mul]; omega
      apply Nat.le_of_mul_le_mul_left _ daPos
      calc
        _ = (2*d)*(a*(2^h*run h (step x))) := by dsimp [a,d]; ring
        _ ≤ (2*d)*(3*M*(3^q*step x)) := Nat.mul_le_mul_left _ next
        _ = (3*M*3^q)*(d*(2*step x)) := by ring
        _ ≤ (3*M*3^q)*(a*(3*x)) := Nat.mul_le_mul_left _ charge
        _ = _ := by ring

private theorem affine_lower (h x : Nat) : 3^(odds h x)*x≤2^h*run h x := by
  induction h generalizing x with
  | zero => simp [run,odds]
  | succ h ih =>
    have next := Nat.mul_le_mul_left 2 (ih (step x))
    have num : 3^(x%2)*x≤2*step x := by
      by_cases e : x%2=0
      · simp [e,step]; omega
      · have o : x%2=1 := by omega
        simp [o,step]; omega
    simp only [odds,run,pow_add,pow_succ]
    calc
      _ = 3^(odds h (step x))*(3^(x%2)*x) := by ring
      _ ≤ 3^(odds h (step x))*(2*step x) := Nat.mul_le_mul_left _ num
      _ = 2*(3^(odds h (step x))*step x) := by ring
      _ ≤ _ := by simpa only [Nat.mul_left_comm,Nat.mul_comm,Nat.mul_assoc] using next

/-- A test on the two original finite traces, at the actual supplied upper
hit. A modest lower odd count with modest surplus gives a *literal earlier
or current physical value* below the requested floor. -/
theorem descent_at_supplied_hit {x j H M D : Nat} (px : 0<x)
    (hit : run H (3^j*x)=1) (cost : odds H x≤M)
    (surplus : odds H x≤j+odds H (3^j*x)+D) (scale : 3*3^D<2*M) :
    ∃ i≤H, 0<run i x ∧ run i x<M := by
  by_contra no
  have floor (i : Nat) (le : i≤H) : M≤run i x := by
    by_contra large; exact no ⟨i,le,pos_run px i,by omega⟩
  let q := odds H x
  let a := j+odds H (3^j*x)
  have bd : q<3*M := by dsimp [q]; omega
  have bound := floor_budget H x M floor bd
  have up := affine_lower H (3^j*x)
  rw [hit,Nat.mul_one] at up
  change (3*M-q)*(2^H*run H x)≤3*M*(3^q*x) at bound
  have high : 3^a*x≤2^H := by dsimp [a]; rw [pow_add]; simpa only [Nat.mul_comm,Nat.mul_left_comm,Nat.mul_assoc] using up
  have power : 3^q≤3^a*3^D := by rw [←pow_add]; exact Nat.pow_le_pow_right (by decide : 0<3) surplus
  have low : 2*M≤3*M-q := by dsimp [q]; omega
  have line : (3^a*x*M)*(2*M)≤(3^a*x*M)*(3*3^D) := calc
    _ = (2*M)*((3^a*x)*M) := by ring
    _ ≤ (3*M-q)*(2^H*run H x) := Nat.mul_le_mul low (Nat.mul_le_mul high (floor H (by omega)))
    _ ≤ 3*M*(3^q*x) := bound
    _ ≤ 3*M*((3^a*3^D)*x) := Nat.mul_le_mul_left _ (Nat.mul_le_mul_right _ power)
    _ = _ := by ring
  have pos : 0<3^a*x*M := Nat.mul_pos (Nat.mul_pos (Nat.pow_pos (by decide)) px) (by omega)
  have down := Nat.le_of_mul_le_mul_left line pos
  omega

/-- The alternative to a physical drop preserves the actual upper suffix and
strictly saves odd work. The lower endpoint is above the upper endpoint by a
positive integral carry. It need not be an integer multiple of it. -/
theorem drop_or_exact_suffix {x j H M D : Nat} (ox : x%2=1) (rank : 0<j)
    (hit : run H (3^j*x)=1) (cost : j+odds H (3^j*x)+D≤M)
    (scale : 3*3^D<2*M) :
    (∃ i≤H, 0<run i x ∧ run i x<M) ∨
    (j+odds H (3^j*x)+D<odds H x ∧
    ∃ t K, 0<t ∧ 0<K ∧ H=t+K ∧
      (∀ i<t, odds i x<j+odds i (3^j*x)) ∧
      odds t x=j+odds t (3^j*x) ∧ run t (3^j*x)<run t x ∧
      run K (run t (3^j*x))=1 ∧
      odds H (3^j*x)=odds t (3^j*x)+odds K (run t (3^j*x)) ∧
      odds K (run t (3^j*x))<odds H (3^j*x)) := by
  classical
  by_cases less : odds H x≤j+odds H (3^j*x)+D
  · exact Or.inl (descent_at_supplied_hit (by omega) hit (less.trans cost) less scale)
  right
  refine ⟨by omega,?_⟩
  let y := 3^j*x
  let P := fun i => j+odds i y≤odds i x
  have reached : ∃ i, P i := ⟨H,by dsimp [P,y]; omega⟩
  let t := Nat.find reached
  have atT : P t := Nat.find_spec reached
  have earlier (i : Nat) (h : i<t) : odds i x<j+odds i y := by
    have min := Nat.find_min reached h
    change ¬ j+odds i y≤odds i x at min
    omega
  have le : t≤H := Nat.find_min' reached (show P H by dsimp [P,y]; omega)
  have pos : t≠0 := by intro e; rw [e] at atT; change j+0≤0 at atT; omega
  obtain ⟨k,hk⟩ := Nat.exists_eq_succ_of_ne_zero pos
  change t=k+1 at hk
  have bk := earlier k (by omega)
  change j+odds t y≤odds t x at atT
  have increments (n : Nat) : odds t n=odds k n+(run k n)%2 := by rw [hk,last_odds]
  have bal : odds t x=j+odds t y := by rw [increments x,increments y] at atT ⊢; omega
  have guard : ∀ i≤k+1, odds i x≤j+odds i y := by
    intro i bound; by_cases it : i=t
    · rw [it]; exact bal.le
    · exact (earlier i (by omega)).le
  have sep := strict_before_overshoot ox rank guard
  rw [←hk] at sep
  change run t y<3^(j+odds t y-odds t x)*run t x at sep
  rw [←bal,Nat.sub_self,pow_zero,one_mul] at sep
  have lt : t<H := by
    by_contra no
    have et : t=H := by omega
    rw [et] at bal
    change odds H x=j+odds H (3^j*x) at bal
    omega
  have split : H=t+(H-t) := by omega
  have suff : run (H-t) (run t y)=1 := by rw [←run_add,←split]; exact hit
  have count : odds H y=odds t y+odds (H-t) (run t y) := by rw [←odds_add,←split]
  have oy : y%2=1 := by dsimp [y]; rw [Nat.mul_mod,three_odd,ox]
  have save : 0<odds t y := by rw [hk]; simp only [odds,oy]; omega
  have finalCost : odds (H-t) (run t y)<odds H y := by omega
  exact ⟨t,H-t,by omega,by omega,split,earlier,bal,sep,suff,count,finalCost⟩

private theorem bad_growth {x : Nat} (px : 0<x) (bad : ¬Good x) (h : Nat) :
    (2^h*run h x)*2^(odds h x)≤7^(odds h x)*x := by
  induction h generalizing x with
  | zero => simp [run,odds]
  | succ h ih =>
    have bx : ¬Good (step x) := fun good => bad ((good_step x).mp good)
    have nx := ih (pos_step px) bx
    have one : x≠1 := by intro e; exact bad (e ▸ good_one)
    have sz : 2≤x := by omega
    have localStep : (2*step x)*2^(x%2)≤7^(x%2)*x := by
      by_cases e : x%2=0
      · simp [e,step]; omega
      · have o : x%2=1 := by omega
        simp [o,step]; omega
    simp only [run,odds,pow_add,pow_succ]
    calc
      _ = (2*2^(x%2))*((2^h*run h (step x))*2^(odds h (step x))) := by ring
      _ ≤ (2*2^(x%2))*(7^(odds h (step x))*step x) := Nat.mul_le_mul_left _ nx
      _ = 7^(odds h (step x))*((2*step x)*2^(x%2)) := by ring
      _ ≤ 7^(odds h (step x))*(7^(x%2)*x) := Nat.mul_le_mul_left _ localStep
      _ = _ := by ring

private theorem binomial (k : Nat) : 7^k*(k+7)≤7*8^k := by
  induction k with
  | zero => decide
  | succ k ih =>
    rw [pow_succ,pow_succ]
    calc
      _ = 7^k*(7*(k+1+7)) := by ring
      _ ≤ 7^k*(8*(k+7)) := Nat.mul_le_mul_left _ (by omega)
      _ = 8*(7^k*(k+7)) := by ring
      _ ≤ 8*(7*8^k) := Nat.mul_le_mul_left _ ih
      _ = _ := by ring

private theorem bad_surplus {x : Nat} (px : 0<x) (bad : ¬Good x) (s : Nat) :
    ∃ k, k+s<odds (2*k) x := by
  let k := 7*(7^s*x)
  let q := odds (2*k) x
  refine ⟨k,?_⟩
  change k+s<q
  by_contra slack
  let d := k+s-q
  have sum : q+d=k+s := by dsimp [d]; omega
  have g := bad_growth px bad (2*k)
  change (2^(2*k)*run (2*k) x)*2^q≤7^q*x at g
  have pos := pos_run px (2*k)
  have le : 2^(2*k)*2^q≤7^q*x :=
    (Nat.mul_le_mul_right _ (show 2^(2*k)≤2^(2*k)*run (2*k) x by
      simpa only [Nat.mul_one] using Nat.mul_le_mul_left (2^(2*k)) (show 1≤run (2*k) x by omega))).trans g
  have two : 8^k*2^s=(2^(2*k)*2^q)*2^d := by
    rw [show 8^k=(2:Nat)^(3*k) by rw [show (8:Nat)=2^3 by decide,←pow_mul],←pow_add,←pow_add,←pow_add]
    congr 1; omega
  have lim : 8^k≤7^k*(7^s*x) := calc
    _ ≤ 8^k*2^s := by simpa only [Nat.mul_one] using Nat.mul_le_mul_left (8^k) (Nat.two_pow_pos s)
    _ = _ := two
    _ ≤ (7^q*x)*7^d := Nat.mul_le_mul le (Nat.pow_le_pow_left (by decide : 2≤7) d)
    _ = 7^(q+d)*x := by rw [pow_add]; ring
    _ = _ := by rw [sum,pow_add]; ring
  have comp : 7^k*(k+7)≤7^k*(7*(7^s*x)) := calc
    _ ≤ 7*8^k := binomial k
    _ ≤ 7*(7^k*(7^s*x)) := Nat.mul_le_mul_left 7 lim
    _ = _ := by ring
  have done := Nat.le_of_mul_le_mul_left comp (Nat.pow_pos (by decide : 0<7))
  change k+7≤k at done
  omega

private theorem laps (k : Nat) : run (2*k) 1=1 ∧ odds (2*k) 1=k := by
  induction k with
  | zero => decide
  | succ k ih =>
    rw [show 2*(k+1)=2*k+2 by omega,run_add,odds_add,ih.1,ih.2]
    exact ⟨by decide,rfl⟩

/-- At the actual reverse disagreement every prescribed cumulative odd-count
surplus is exceeded. The original supplied hit may be extended only by
actual laps at one. This result supplies no earlier-suffix guarantee. -/
theorem unbounded_after_supplied_hit {x y H : Nat} (px : 0<x) (bad : ¬Good x)
    (hit : run H y=1) (D : Nat) :
    ∃ k, run (H+2*k) y=1 ∧ odds (H+2*k) y+D<odds (H+2*k) x := by
  have bx : ¬Good (run H x) := fun g => bad ((good_run H x).mp g)
  obtain ⟨k,more⟩ := bad_surplus (pos_run px H) bx (odds H y+D)
  refine ⟨k,?_,?_⟩
  · rw [run_add,hit,(laps k).1]
  · rw [odds_add,odds_add,hit,(laps k).2]; omega

private theorem half_run (m u : Nat) : run m (2^m*u)=u ∧ odds m (2^m*u)=0 := by
  induction m with
  | zero => simp [run,odds]
  | succ m ih =>
    rw [show 2^(m+1)*u=2*(2^m*u) by ring]
    simpa [run,odds,step] using ih

/-- A physical ordinary equality using the carry's own supplied hit. -/
theorem positive_carry_meeting {c u h k R : Nat} (oc : run h c=1) (odd : u%2=1)
    (grade : odds h c+k=R+1) :
    step (run (h+2*k) (c+2^(h+2*k)*u))=step (3^R*u) := by
  have atC := lift h c (2^(2*k)*u)
  rw [oc,show 2^h*(2^(2*k)*u)=2^(h+2*k)*u by rw [pow_add]; ring] at atC
  have align := lift (2*k) 1 (3^(odds h c)*u)
  rw [(laps k).1,(laps k).2] at align
  have both : run (h+2*k) (c+2^(h+2*k)*u)=1+3^(R+1)*u := by
    rw [run_add,atC,show 3^(odds h c)*(2^(2*k)*u)=2^(2*k)*(3^(odds h c)*u) by ring,align]
    rw [←grade,pow_add]; ring
  have ox : (3^R*u)%2=1 := by rw [Nat.mul_mod,three_odd,odd]
  have meet : step (1+3^(R+1)*u)=step (3^R*u) := by
    rw [show 1+3^(R+1)*u=1+3*(3^R*u) by ring]
    unfold step; split <;> split <;> omega
  rwa [both]

/-- A source-adaptive return to an actual ternary multiple. The carry c is
computed at the crossing and may have any supplied ordinary hit of its own.
Both clocks spent here lie on the original upper suffix. -/
theorem align_positive_carry {c u h k R K : Nat} (oc : run h c=1) (odd : u%2=1)
    (grade : odds h c+k=R+1) (bad : ¬Good (c+2^(h+2*k)*u))
    (hit : run ((h+2*k)+K) (2^(h+2*k)*u)=1) :
    ¬Good (3^R*u) ∧ run K u=1 ∧
      odds ((h+2*k)+K) (2^(h+2*k)*u)=odds K u := by
  have meeting := positive_carry_meeting oc odd grade
  obtain ⟨halved,zeroOdds⟩ := half_run (h+2*k) u
  refine ⟨?_,?_,?_⟩
  · intro good
    apply bad
    apply (good_run (h+2*k) _).mp
    apply (good_step _).mp
    rw [meeting]; exact (good_step _).mpr good
  · rwa [run_add,halved] at hit
  · rw [odds_add,zeroOdds,halved,Nat.zero_add]

#print axioms positive_carry_meeting
#print axioms align_positive_carry
#print axioms unbounded_after_supplied_hit
#print axioms drop_or_exact_suffix
#print axioms descent_at_supplied_hit
#print axioms strict_before_overshoot
#print axioms meeting_requires_overshoot
#print axioms floor_budget
end Collatz.FirstCrossing
