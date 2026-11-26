import WallGeneral

namespace WallUniform
open WallRational WallAffine WallOrbit WallGeneral WallRefinement WordRank

theorem finite_bound (N : Nat) (P : Nat → Nat → Prop) (h : ∀i<N, ∃b, P i b) :
    ∃ B, ∀ i<N, ∃ b≤B, P i b := by
  induction N with
  | zero => exact ⟨0,fun i hi => False.elim (by omega)⟩
  | succ N ih =>
    obtain ⟨B,old⟩ := ih (fun i hi => h i (by omega))
    obtain ⟨b,last⟩ := h N (by omega)
    refine ⟨B+b,?_⟩
    intro i hi
    by_cases eq : i=N
    · subst i;exact ⟨b,by omega,last⟩
    · obtain ⟨a,sm,ok⟩ := old i (by omega)
      exact ⟨a,by omega,ok⟩

/-- For fixed affine mates and fixed nontrivial exponential multiplier,
one turn bound works uniformly over all odd source coefficients a. -/
theorem exponential_bound (s e : Nat) (D d c B u : Int) (large : 2≤e)
    (unit : u%2=1) (base : B=1+2^e*u) (dodd : d%2=1) :
    ∃ T, ∀ (a : Int) (X : Nat → Int), a%2=1 → (∀i, d*X i=a*B^i+c) →
      ∃ i<T, Meets (X i) (3^s*X i+D) := by
  let P := fun (j h : Nat) => ∃ r : Int, ∀ z : Int,
    Meets (2^e*(2^h*z+r)+j) (3^s*(2^e*(2^h*z+r)+j)+D)
  have supply : ∀ j<2^e, ∃ h, P j h := fun j _ => in_class s e D (j:Int)
  obtain ⟨H,bank⟩ := finite_bound (2^e) P supply
  refine ⟨2^H,?_⟩
  intro a X aodd law
  let M : Int := 2^e
  let j := ((X 0)%M).toNat
  let t := (X 0)/M
  have mp : 0<M := by dsimp [M];positivity
  have jr : (j:Int)=X 0%M := Int.toNat_of_nonneg (Int.emod_nonneg _ (by omega))
  have jb : j<2^e := by
    have z : (j:Int)<(2:Int)^e := by rw [jr];exact Int.emod_lt_of_pos _ mp
    exact_mod_cast z
  have x0 : X 0=M*t+j := by rw [jr];exact (Int.mul_ediv_add_emod _ _).symm
  obtain ⟨h,hle,r,merge⟩ := bank j jb
  let center := M*r+j
  let target := d*center-c
  have ez : d*X 0=a+c := by simpa using law 0
  have same : a=2^e*(d*(t-r))+target := by
    dsimp [target,center]
    rw [x0] at ez
    change a=M*(d*(t-r))+(d*(M*r+j)-c)
    grind
  obtain ⟨i,small,z,hit⟩ := cover B a target u e h large unit base aodd ⟨_,same⟩
  have eq : d*(X i-center)=2^(e+h)*z := by rw [Int.mul_sub,law,hit];dsimp [target];ring
  obtain ⟨v,div⟩ := cancel d (X i-center) z (e+h) dodd eq
  have point : X i=2^e*(2^h*v+r)+j := by
    dsimp [center,M] at div;rw [pow_add] at div;grind
  refine ⟨i,lt_of_lt_of_le small (Nat.pow_le_pow_right (by decide) hle),?_⟩
  rw [point]
  exact merge v

private theorem paired_order (P Q g : Nat) (sg : 0<g) (ord : P≤Q)
    (d c f : Int) (dodd : d%2=1) :
    ∃ T, ∀ (q : Int) (X Y : Nat → Int), q%2=1 →
      (∀i, d*X i=3^P*q*9^(g*i)+c) → (∀i, d*Y i=3^Q*q*9^(g*i)+f) →
      ∃i<T, Meets (X i) (Y i) := by
  let s := Q-P
  let D := (f-3^s*c)/d
  have level : (3:Int)^Q=3^s*3^P := by rw [←pow_add];congr 1;dsimp [s];omega
  obtain ⟨e,u,large,unit,base⟩ := exp_unit g sg
  obtain ⟨T,all⟩ := exponential_bound s e D d c (9^g) u large unit base dodd
  refine ⟨T,?_⟩
  intro q X Y qo lx ly
  have d0 : d≠0 := by omega
  have ao : (3^P*q)%2=1 := by rw [Int.mul_emod,odd_power 3 (by decide),qo];decide
  obtain ⟨i,small,hit⟩ := all (3^P*q) X ao (fun i => by simpa [pow_mul] using lx i)
  have rel : d*(Y i-3^s*X i)=f-3^s*c := by
    rw [Int.mul_sub,show d*(3^s*X i)=3^s*(d*X i) by ring,lx,ly,level]
    ring
  have eq : Y i=3^s*X i+D := by
    dsimp [D]
    rw [←rel,Int.mul_ediv_cancel_left _ d0]
    ring
  refine ⟨i,small,?_⟩
  rw [eq]
  exact hit

theorem paired_bound (P Q g : Nat) (sg : 0<g) (d c f : Int) (dodd : d%2=1) :
    ∃ T, ∀ (q : Int) (X Y : Nat → Int), q%2=1 →
      (∀i, d*X i=3^P*q*9^(g*i)+c) → (∀i, d*Y i=3^Q*q*9^(g*i)+f) →
      ∃i<T, Meets (X i) (Y i) := by
  by_cases le : P≤Q
  · exact paired_order P Q g sg le d c f dodd
  · obtain ⟨T,all⟩ := paired_order Q P g sg (by omega) d f c dodd
    refine ⟨T,?_⟩
    intro q X Y qo lx ly
    obtain ⟨i,sm,a,b,eq⟩ := all q Y X qo ly lx
    exact ⟨i,sm,b,a,eq.symm⟩

private def BoundedMeet (L p n B : Nat) : Prop :=
  ∃ l≤B, ∃ r≤B, ∃ a b, run a (address L p n l)=run b (address L p n r+1)

private theorem fixed_valuation (L p d v : Nat) (pos : 0<L) (den : d+1=2^L)
    (l : PositiveCycle d (-(p:Int))) (r : PositiveCycle d ((d:Int)-p)) :
    ∃ B, ∀ n q, q%2=1 → d*n+p=2^v*q → BoundedMeet L p n B := by
  have dint : (d:Int)%2=1 := by
    obtain ⟨b,eq⟩ : ∃ b,L=b+1 := ⟨L-1,by omega⟩
    rw [eq,pow_succ] at den;omega
  let K := l.entry+r.entry
  let H := L*K+v
  have kh : K≤H := by
    dsimp [H]
    have mul : K≤L*K := by simpa using Nat.mul_le_mul_right K pos
    omega
  have ltime : l.entry≤H := by dsimp [K] at kh;omega
  have rtime : r.entry≤H := by dsimp [K] at kh;omega
  let m := grade d l.period (runD d l.entry (-(p:Int)))
  let z := grade d r.period (runD d r.entry ((d:Int)-p))
  have mp : 0<m := l.positive
  have zp : 0<z := r.positive
  obtain ⟨T,all⟩ := paired_bound (grade d H (-(p:Int))) (grade d H ((d:Int)-p))
    (m*z*L) (by positivity) d (runD d H (-(p:Int))) (runD d H ((d:Int)-p)) dint
  let kL := fun i => K+l.period*2*z*i
  let kR := fun i => K+r.period*2*m*i
  refine ⟨kL T+kR T,?_⟩
  intro n q odd src
  let X := fun i => run (L*kL i+v) (address L p n (kL i))
  let Y := fun i => run (L*kR i+v) (address L p n (kR i)+1)
  have num (k : Nat) : (d:Int)*address L p n k+p=2^(L*k+v)*q := by
    have e := address_eq L p n d k den
    rw [src,←Nat.mul_assoc,←pow_add] at e
    exact_mod_cast e
  have left (i : Nat) : (d:Int)*(X i:Int)=
      3^(grade d H (-(p:Int)))*(q:Int)*9^((m*z*L)*i)+runD d H (-(p:Int)) := by
    exact chart_arm d (-(p:Int)) q L v K m z (address L p n) dint
      (fun k => by have e := num k;omega) l ltime rfl i
  have right (i : Nat) : (d:Int)*(Y i:Int)=
      3^(grade d H ((d:Int)-p))*(q:Int)*9^((m*z*L)*i)+runD d H ((d:Int)-p) := by
    rw [show m*z=z*m by ring]
    apply chart_arm d ((d:Int)-p) q L v K z m (fun k => address L p n k+1) dint _ r rtime rfl i
    intro k;push_cast;rw [Int.mul_add,Int.mul_one];have e := num k;omega
  obtain ⟨i,bound,a,b,hit⟩ := all q (fun i => (X i:Int)) (fun i => (Y i:Int))
    (by omega) left right
  rw [signed_nat,signed_nat] at hit
  have dl : kL i≤kL T := by dsimp [kL]; exact Nat.add_le_add_left (Nat.mul_le_mul_left _ (by omega)) _
  have dr : kR i≤kR T := by dsimp [kR]; exact Nat.add_le_add_left (Nat.mul_le_mul_left _ (by omega)) _
  refine ⟨kL i,by omega,kR i,by omega,L*kL i+v+a,L*kR i+v+b,?_⟩
  rw [runAdd (L*kL i+v),runAdd (L*kR i+v)]
  exact_mod_cast hit

/-- The physical block-depth bound now depends on the word only, for every
ordinary starting integer whose last L bits differ from that word. -/
theorem after_mismatch (L p d : Nat) (pos : 0<L) (pp : 0<p) (fits : p<2^L)
    (den : d+1=2^L)
    (l : PositiveCycle d (-(p:Int))) (r : PositiveCycle d ((d:Int)-p)) :
    ∃ B, ∀ n, n%2^L≠p →
      ∃ j≤B, ∃ k≤B, ∃ a b, run a (address L p n j)=run b (address L p n k+1) := by
  let P := fun v B => ∀ n q, q%2=1 → d*n+p=2^v*q → BoundedMeet L p n B
  have choose : ∀v<L, ∃B, P v B := fun v _ => fixed_valuation L p d v pos den l r
  obtain ⟨B,all⟩ := finite_bound L P choose
  refine ⟨B,?_⟩
  intro n reset
  obtain ⟨v,q,odd,src⟩ := WallPeriodic.split_twos (d*n+p) (by omega)
  have small : v<L := by
    by_contra! big
    have e : 2^v=2^L*2^(v-L) := by rw [←pow_add];congr 1;omega
    have a : d*n+p+n=2^L*n+p := by rw [←den];ring
    rw [src,e,Nat.mul_assoc] at a
    have eq := congrArg (fun x => x%(2^L)) a
    have hh : n%2^L=p%2^L := by simpa using eq
    exact reset (hh.trans (Nat.mod_eq_of_lt fits))
  obtain ⟨b,bl,cert⟩ := all v small
  obtain ⟨j,bj,k,bk,a,t,meet⟩ := cert n q odd src
  exact ⟨j,by omega,k,by omega,a,t,meet⟩

end WallUniform
