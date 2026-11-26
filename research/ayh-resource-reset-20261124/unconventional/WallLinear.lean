import WallShifted

namespace WallLinear
open WallAffine WallRational WallOrbit WallGeneral WallRefinement WallUniform WallDensity WordRank

private theorem address_add (L p n a b : Nat) :
    address L p (address L p n a) b=address L p n (a+b) := by
  induction b with
  | zero => simp [address]
  | succ b ih => rw [address,show a+(b+1)=a+b+1 by omega,address,ih]

private theorem ancestor (L p d n b w q : Nat) (small : p<d) (den : d+1=2^L)
    (src : d*n+p=2^(L*b+w)*q) :
    ∃ a, d*a+p=2^w*q ∧ address L p a b=n := by
  let z := 2^w*q
  have mul : d*n+p=2^(L*b)*z := by rw [src,pow_add];dsimp [z];ring
  have mod : 2^L ≡ 1 [MOD d] := by rw [←den];simp [Nat.ModEq]
  have one : 2^(L*b) ≡ 1 [MOD d] := by simpa [pow_mul] using mod.pow b
  have rem : z%d=p := by
    have h := one.mul_right z
    change (2^(L*b)*z)%d=(1*z)%d at h
    rw [←mul] at h
    simpa [Nat.mod_eq_of_lt small] using h.symm
  have rep := Nat.mod_add_div z d
  rw [rem] at rep
  have eq : d*(z/d)+p=z := by omega
  have addr := address_eq L p (z/d) d b den
  rw [eq,←mul] at addr
  exact ⟨z/d,eq,Nat.eq_of_mul_eq_mul_left (by omega : 0<d) (by omega)⟩

private theorem from_ancestor (L p d w : Nat) (pos : 0<L) (den : d+1=2^L)
    (l : PositiveCycle d (-(p:Int))) (r : PositiveCycle d ((d:Int)-p)) :
    let α := l.period*2*lapGrade r
    let β := r.period*2*lapGrade l
    ∃ B, ∀ a q b, q%2=1 → d*a+p=2^w*q →
      ∃ i≥b, ∃ j≥b, i≤(α+β)*b+B ∧ j≤(α+β)*b+B ∧
        ∃ h t, run h (address L p a i)=run t (address L p a j+1) := by
  dsimp only
  have odd : (d:Int)%2=1 := by
    obtain ⟨i,eq⟩ : ∃ i,L=i+1 := ⟨L-1,by omega⟩
    rw [eq,pow_succ] at den;omega
  let K := l.entry+r.entry
  let H := L*K+w
  have kh : K≤H := by
    have le : K≤L*K := by simpa using Nat.mul_le_mul_right K pos
    dsimp [H];omega
  have lt : l.entry≤H := by dsimp [K] at kh;omega
  have rt : r.entry≤H := by dsimp [K] at kh;omega
  let m := lapGrade l
  let z := lapGrade r
  let g := m*z*L
  have mp : 0<m := l.positive
  have zp : 0<z := r.positive
  have gp : 0<g := Nat.mul_pos (Nat.mul_pos mp zp) pos
  let α := l.period*2*z
  let β := r.period*2*m
  have ap : 0<α := Nat.mul_pos (Nat.mul_pos (time_pos l) (by decide)) zp
  have bp : 0<β := Nat.mul_pos (Nat.mul_pos (time_pos r) (by decide)) mp
  let kL := fun i => K+α*i
  let kR := fun i => K+β*i
  obtain ⟨T,all⟩ := paired_bound (grade d H (-(p:Int))) (grade d H ((d:Int)-p))
    g gp d (runD d H (-(p:Int))) (runD d H ((d:Int)-p)) odd
  refine ⟨kL T+kR T,?_⟩
  intro a q b qo src
  let X := fun i => run (L*kL i+w) (address L p a (kL i))
  let Y := fun i => run (L*kR i+w) (address L p a (kR i)+1)
  have num (k : Nat) : (d:Int)*address L p a k+p=2^(L*k+w)*q := by
    have e := address_eq L p a d k den
    rw [src,←Nat.mul_assoc,←pow_add] at e
    exact_mod_cast e
  have left (i : Nat) : (d:Int)*(X i:Int)=
      3^(grade d H (-(p:Int)))*(q:Int)*9^(g*i)+runD d H (-(p:Int)) := by
    exact chart_arm d (-(p:Int)) q L w K m z (address L p a) odd
      (fun k => by have e := num k;omega) l lt rfl i
  have right (i : Nat) : (d:Int)*(Y i:Int)=
      3^(grade d H ((d:Int)-p))*(q:Int)*9^(g*i)+runD d H ((d:Int)-p) := by
    dsimp [g];rw [show m*z=z*m by ring]
    apply chart_arm d ((d:Int)-p) q L w K z m (fun k => address L p a k+1) odd _ r rt rfl i
    intro k;push_cast;rw [Int.mul_add,Int.mul_one];have e := num k;omega
  let unit : Int := (q:Int)*9^(g*b)
  have uo : unit%2=1 := by dsimp [unit];rw [Int.mul_emod,odd_power 9 (by decide)];omega
  obtain ⟨i,ib,h,t,meet⟩ := all unit (fun i => (X (b+i):Int)) (fun i => (Y (b+i):Int))
    uo (fun i => by rw [left,Nat.mul_add,pow_add];dsimp [unit];ring)
    (fun i => by rw [right,Nat.mul_add,pow_add];dsimp [unit];ring)
  rw [signed_nat,signed_nat] at meet
  have bounds (A : Nat) (hp : 0<A) : b≤K+A*(b+i) ∧ K+A*(b+i)≤A*b+(K+A*T) := by
    have lo : b≤A*b := by simpa using Nat.mul_le_mul_right b hp
    have hi := Nat.mul_le_mul_left A (show i≤T by omega)
    rw [Nat.mul_add];omega
  obtain ⟨la,ua⟩ := bounds α ap
  obtain ⟨lb,ub⟩ := bounds β bp
  refine ⟨kL (b+i),la,kR (b+i),lb,?_,?_,L*kL (b+i)+w+h,L*kR (b+i)+w+t,?_⟩
  · change K+α*(b+i)≤(α+β)*b+(K+α*T+(K+β*T))
    rw [Nat.add_mul];omega
  · change K+β*(b+i)≤(α+β)*b+(K+α*T+(K+β*T))
    rw [Nat.add_mul];omega
  · rw [runAdd (L*kL (b+i)+w),runAdd (L*kR (b+i)+w)]
    exact_mod_cast meet

/-- Linear block-depth control for the initial run of every word with
positive-grade periodic shadows, including cases of unequal densities. -/
theorem linear_depth (L p d : Nat) (pos : 0<L) (small : p<d) (den : d+1=2^L)
    (l : PositiveCycle d (-(p:Int))) (r : PositiveCycle d ((d:Int)-p)) :
    ∃ A B, ∀ n v q, q%2=1 → d*n+p=2^v*q →
      ∃ i≤A*v+B, ∃ j≤A*v+B, ∃ h t,
        run h (address L p n i)=run t (address L p n j+1) := by
  let α := l.period*2*lapGrade r
  let β := r.period*2*lapGrade l
  let P := fun w B => ∀ a q b, q%2=1 → d*a+p=2^w*q →
    ∃ i≥b, ∃ j≥b, i≤(α+β)*b+B ∧ j≤(α+β)*b+B ∧
      ∃ h t, run h (address L p a i)=run t (address L p a j+1)
  have rows : ∀ w<L, ∃ B, P w B := fun w _ => from_ancestor L p d w pos den l r
  obtain ⟨B,bank⟩ := finite_bound L P rows
  refine ⟨α+β,B,?_⟩
  intro n v q qo src
  let b := v/L
  let w := v%L
  have rep : L*b+w=v := by rw [Nat.add_comm];exact Nat.mod_add_div _ _
  obtain ⟨a,ar,an⟩ := ancestor L p d n b w q small den (by rw [rep];exact src)
  obtain ⟨B₀,be,row⟩ := bank w (Nat.mod_lt _ pos)
  obtain ⟨i,il,j,jl,iu,ju,h,t,e⟩ := row a q b qo ar
  have lo := Nat.mul_le_mul_left (α+β) (show b≤v by exact Nat.div_le_self _ _)
  refine ⟨i-b,(Nat.sub_le i b).trans (iu.trans (Nat.add_le_add lo be)),
    j-b,(Nat.sub_le j b).trans (ju.trans (Nat.add_le_add lo be)),h,t,?_⟩
  rw [←an,address_add,address_add,show b+(i-b)=i by omega,show b+(j-b)=j by omega]
  exact e

end WallLinear
