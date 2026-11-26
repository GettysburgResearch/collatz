import WallAffine
import WallPeriodic

namespace WallOrbit
open WallAffine

theorem odd_power (a : Int) (odd : a%2=1) (j : Nat) : a^j%2=1 := by
  induction j with
  | zero => simp
  | succ j ih => rw [pow_succ,Int.mul_emod,ih,odd]; decide

/-- Squaring gains exactly one binary digit once the multiplier is 1 modulo 4. -/
theorem bit (B u : Int) (e k : Nat) (large : 2≤e) (unit : u%2=1)
    (base : B=1+2^e*u) : ∃ w : Int, w%2=1 ∧ B^(2^k)=1+2^(e+k)*w := by
  induction k with
  | zero => exact ⟨u,unit,by simpa using base⟩
  | succ k ih =>
    obtain ⟨w,odd,power⟩ := ih
    let z : Int := 2^(e+k-2)
    have m : (2:Int)^(e+k)=4*z := by
      rw [show e+k=(e+k-2)+2 by omega,pow_add]
      change 2^(e+k-2)*4=4*z
      dsimp [z]; ring
    refine ⟨w+2*(z*w^2),by omega,?_⟩
    calc
      _ = (B^(2^k))^2 := by rw [pow_succ,pow_mul]
      _ = (1+4*z*w)^2 := by rw [power,m]
      _ = 1+(2^(e+k)*2)*(w+2*(z*w^2)) := by rw [m];ring
      _ = _ := by rw [show e+(k+1)=(e+k)+1 by omega,pow_succ (2:Int) (e+k)]

/-- Every odd coefficient times the powers of B covers each lift of its
initial low e bits. The chosen exponent is bounded by the subgroup order. -/
theorem cover (B a y u : Int) (e k : Nat) (large : 2≤e) (unit : u%2=1)
    (base : B=1+2^e*u) (aodd : a%2=1) (start : ∃v:Int,a=2^e*v+y) :
    ∃ j<2^k, ∃ z : Int, a*B^j=2^(e+k)*z+y := by
  have Bodd : B%2=1 := by
    rw [base,show e=(e-1)+1 by omega,pow_succ]
    rw [show 2^(e-1)*2*u=2*(2^(e-1)*u) by ring]
    omega
  induction k with
  | zero =>
    obtain ⟨v,ev⟩ := start
    exact ⟨0,by decide,v,by simpa using ev⟩
  | succ k ih =>
    obtain ⟨j,small,z,ez⟩ := ih
    let M : Int := 2^(e+k)
    have mp : (2:Int)^(e+(k+1))=2*M := by dsimp [M]; rw [show e+(k+1)=e+k+1 by omega,pow_succ];ring
    by_cases zp : z%2=0
    · refine ⟨j,by rw [pow_succ];omega,z/2,?_⟩
      rw [mp,show (2*M)*(z/2)=M*(2*(z/2)) by ring,show 2*(z/2)=z by omega]
      exact ez
    · obtain ⟨w,wodd,wb⟩ := bit B u e k large unit base
      let x := a*B^j
      have xOdd : x%2=1 := by dsimp [x];rw [Int.mul_emod,aodd,odd_power B Bodd j];decide
      have wx : (w*x)%2=1 := by rw [Int.mul_emod,wodd,xOdd];decide
      have parity : 2*((z+w*x)/2)=z+w*x := by omega
      refine ⟨j+2^k,by rw [pow_succ];omega,(z+w*x)/2,?_⟩
      rw [pow_add,wb,mp,show (2*M)*((z+w*x)/2)=M*(2*((z+w*x)/2)) by ring,parity]
      change a*(B^j*(1+M*w))=M*(z+w*x)+y
      have ex : x=M*z+y := ez
      calc _ = x+M*(w*x) := by dsimp [x]; ring
           _ = _ := by rw [ex];ring

theorem cancel (d x z : Int) (h : Nat) (odd : d%2=1) (eq : d*x=2^h*z) :
    ∃ t : Int, x=2^h*t := by
  obtain ⟨u,v,inv⟩ := solve_unit d 0 1 odd h
  simp only [Int.add_zero] at inv
  refine ⟨u*z-v*x,?_⟩
  calc
    x = (d*u-2^h*v)*x := by rw [inv];ring
    _ = u*(d*x)-2^h*(v*x) := by ring
    _ = _ := by rw [eq];ring

/-- A rationally scaled, exponentially sampled affine family has an actual
meeting provided its multiplier generates an open class of dyadic units. -/
theorem exponential_merger (s e : Nat) (D d a c B u : Int) (large : 2≤e)
    (unit : u%2=1) (base : B=1+2^e*u) (dodd : d%2=1) (aodd : a%2=1)
    (X : Nat → Int) (law : ∀ i, d*X i=a*B^i+c) :
    ∃ i, Meets (X i) (3^s*X i+D) := by
  obtain ⟨h,r,merge⟩ := in_class s e D (X 0)
  let center := 2^e*r+X 0
  let target := d*center-c
  have ez : d*X 0=a+c := by simpa using law 0
  have same : a=2^e*(-d*r)+target := by
    dsimp [target,center]
    rw [Int.mul_add,ez]
    ring
  obtain ⟨j,_,z,hit⟩ := cover B a target u e h large unit base aodd ⟨_,same⟩
  have eq : d*(X j-center)=2^(e+h)*z := by
    rw [Int.mul_sub,law,hit]; dsimp [target];ring
  obtain ⟨v,div⟩ := cancel d (X j-center) z (e+h) dodd eq
  have point : X j=2^e*(2^h*v+r)+X 0 := by
    dsimp [center] at div
    rw [pow_add] at div
    grind
  exact ⟨j,point ▸ merge v⟩

theorem exp_unit (g : Nat) (positive : 0<g) :
    ∃ e : Nat, ∃ u : Int, 2≤e ∧ u%2=1 ∧ (9:Int)^g=1+2^e*u := by
  have gt : 1<(9:Nat)^g := by
    obtain ⟨j,rfl⟩ : ∃ j, g=j+1 := ⟨g-1,by omega⟩
    have p : 0<(9:Nat)^j := by positivity
    rw [pow_succ];omega
  obtain ⟨e,u,odd,eq⟩ := WallPeriodic.split_twos (9^g-1) (by omega)
  have low : 9^g%4=1 := by
    clear gt positive eq
    induction g with
    | zero => decide
    | succ j ih => rw [pow_succ,Nat.mul_mod,ih]
  have le : 2≤e := by
    by_contra! small
    have cases : e=0 ∨ e=1 := by omega
    rcases cases with rfl|rfl <;> norm_num at eq <;> omega
  have en : (9:Nat)^g=1+2^e*u := by omega
  refine ⟨e,(u:Int),le,by omega,?_⟩
  exact_mod_cast en

private theorem paired_ordered (P Q g : Nat) (sg : 0<g) (ord : P≤Q)
    (d q c f : Int) (dodd : d%2=1) (qodd : q%2=1) (X Y : Nat → Int)
    (lx : ∀ i, d*X i=3^P*q*9^(g*i)+c)
    (ly : ∀ i, d*Y i=3^Q*q*9^(g*i)+f) : ∃ i, Meets (X i) (Y i) := by
  let s := Q-P
  let a : Int := 3^P*q
  let B : Int := 9^g
  let D := Y 0-3^s*X 0
  have aodd : a%2=1 := by dsimp [a];rw [Int.mul_emod,odd_power 3 (by decide),qodd];decide
  have level : (3:Int)^Q=3^s*3^P := by rw [←pow_add];congr 1;dsimp [s];omega
  obtain ⟨e,u,large,unit,base⟩ := exp_unit g sg
  obtain ⟨i,hit⟩ := exponential_merger s e D d a c B u large unit base dodd aodd X
    (fun i => by simpa [a,B,pow_mul] using lx i)
  have d0 : d≠0 := by omega
  have eq : Y i=3^s*X i+D := by
    apply mul_left_cancel₀ d0
    have x0 := lx 0
    have y0 := ly 0
    simp only [Nat.mul_zero,pow_zero,mul_one] at x0 y0
    dsimp [D]
    rw [Int.mul_add,Int.mul_sub,show d*(3^s*X i)=3^s*(d*X i) by ring,
        show d*(3^s*X 0)=3^s*(d*X 0) by ring,lx,ly,x0,y0,level]
    ring
  refine ⟨i,?_⟩
  rw [eq]
  exact hit

/-- Two rational affine rows with a common positive grade gain necessarily
have a physical meeting somewhere along the same exponential parameter. -/
theorem paired (P Q g : Nat) (sg : 0<g) (d q c f : Int)
    (dodd : d%2=1) (qodd : q%2=1) (X Y : Nat → Int)
    (lx : ∀ i, d*X i=3^P*q*9^(g*i)+c)
    (ly : ∀ i, d*Y i=3^Q*q*9^(g*i)+f) : ∃ i, Meets (X i) (Y i) := by
  by_cases ord : P≤Q
  · exact paired_ordered P Q g sg ord d q c f dodd qodd X Y lx ly
  · obtain ⟨i,a,b,h⟩ := paired_ordered Q P g sg (by omega) d q f c dodd qodd Y X ly lx
    exact ⟨i,b,a,h.symm⟩

end WallOrbit
