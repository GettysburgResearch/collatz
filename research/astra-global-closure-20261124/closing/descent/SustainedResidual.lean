import ResidualDescent

namespace SustainedResidual
open CycleShadows ResidualDescent
set_option maxRecDepth 12000
set_option maxHeartbeats 1000000

private theorem next_edge {D M C N K B x y q : Nat}
    (pre : D*x=M*q+C) (edge : N*y=B*x+K) :
    (D*N)*y=(B*M)*q+(B*C+D*K) := by
  calc
    D*N*y = D*(N*y) := by ac_rfl
    _ = B*(D*x) + D*K := by rw [edge,Nat.mul_add]; ac_rfl
    _ = _ := by rw [pre,Nat.mul_add]; ac_rfl

private def initialBits : List Bool := [true,true,true,true,false,true,true,true]

private theorem first (p a b q : Nat) (h1 : 8*a=9*p+7)
    (h2 : 32*b=9*a+5) (h3 : 32*q=9*b+5) (hqodd : q%2=1) :
    ∃ m y, 0<m ∧ m%2=1 ∧ m<q ∧ m<(3*q+1)/4 ∧
      64*m=3*p+101 ∧ run T 8 m=y ∧ 2*(y+10)=9*(q+7) := by
  have ab := next_edge h1 h2
  have aq := next_edge ab h3
  change 256*b=81*p+103 at ab
  change 8192*q=729*p+2207 at aq
  clear h1 h2 h3 ab
  have qrem : q%729=451 := calc
    q%729 = ((59*8192)%729*q)%729 := by rw [show (59*8192)%729=1 by decide,Nat.one_mul]
    _ = (59*8192*q)%729 := Nat.mod_mul_mod _ _ _
    _ = (59*(8192*q%729))%729 := by rw [Nat.mul_mod_mod,Nat.mul_assoc]
    _ = 451 := by rw [aq,Nat.mul_add_mod]
  let h := (q/729)/2
  have rq : q=1458*h+451 := by
    dsimp [h]
    have decomp := Nat.mod_add_div q 729
    omega
  have px : p=16384*h+5065 := by
    apply Nat.eq_of_mul_eq_mul_left (n:=729) (by decide)
    rw [rq,Nat.mul_add] at aq
    rw [Nat.mul_add]
    omega
  clear aq
  let m := 768*h+239
  let y := 6561*h+2051
  have eqn : 256*y=2187*m+2363 := by dsimp [y,m]; omega
  refine ⟨m,y,by dsimp [m]; omega,by dsimp [m]; omega,?_,?_,?_,?_,?_⟩
  · rw [rq]; dsimp [m]; omega
  · rw [rq]; dsimp [m]; omega
  · rw [px]; dsimp [m]; omega
  · exact WordCert.realize initialBits m y eqn
  · rw [rq]; dsimp [y]; omega
private theorem advance (q z y : Nat) (edge : 8*z=9*q+7) (odd : z%2=1)
    (start : 2*(y+10)=9*(q+7)) : 2*(run T 3 y+10)=9*(z+7) := by
  have h : y+10=8*((z+7)/2) := by omega
  have mid := lift 3 y 10 ((z+7)/2) (by decide) h
  change run T 3 y+10=9*((z+7)/2) at mid
  omega

private theorem last (g : Bool) (q a b d e w y : Nat)
    (h : Five (if g then .pllpp else .pllpl) q a b d e w)
    (hy : 2*(y+10)=9*(q+7)) : run T (if g then 20 else 18) y=w := by
  cases g <;> obtain ⟨h1,h2,h3,h4,h5⟩ := h
  all_goals
    have D := next_edge (next_edge (next_edge (next_edge h1 h2) h3) h4) h5
    clear h1 h2 h3 h4 h5
  · change 524288*w=59049*q+892165 at D
    have Z : 262144*w=6561*y+305021 := by omega
    let bs := targetWord .pllpl
    have hl : bs.length=18 := by decide
    have hs : WordCert.scale bs=6561 := by decide
    have hc : WordCert.carry bs=305021 := by decide
    change run T 18 y=w
    rw [←hl]
    apply WordCert.realize
    rw [hl,hs,hc]
    exact Z
  · change 2097152*w=59049*q+761093 at D
    have Z : 1048576*w=6561*y+239485 := by omega
    let bs := targetWord .pllpp
    have hl : bs.length=20 := by decide
    have hs : WordCert.scale bs=6561 := by decide
    have hc : WordCert.carry bs=239485 := by decide
    change run T 20 y=w
    rw [←hl]
    apply WordCert.realize
    rw [hl,hs,hc]
    exact Z

/-- Every ordinary prior LPP supplies the same smaller comparator for either
residual suffix at every light-run length. The comparator is below the two
prescribed floors after the past LPP, even when that past is very long. -/
theorem sustained_residual (g : Bool) (p a b : Nat) (q : Nat → Nat) (r : Nat)
    (h1 : 8*a=9*p+7) (h2 : 32*b=9*a+5) (h3 : 32*q 0=9*b+5)
    (odd : ∀ i, i≤r → q i%2=1)
    (light : ∀ i, i<r → 8*q (i+1)=9*q i+7)
    (suffix : Five (if g then .pllpp else .pllpl) (q r) (q (r+1))
      (q (r+2)) (q (r+3)) (q (r+4)) (q (r+5))) :
    ∃ m, 0<m ∧ m%2=1 ∧ m<q 0 ∧ m<(3*q 0+1)/4 ∧ 64*m=3*p+101 ∧
      run T (8+3*r+(if g then 20 else 18)) m=q (r+5) := by
  obtain ⟨m,y,hp,ho,hq,hf,he,hr,hy⟩ := first p a b (q 0) h1 h2 h3 (odd 0 (by omega))
  have middle (i : Nat) (hi : i≤r) :
      2*(run T (3*i) y+10)=9*(q i+7) := by
    induction i with
    | zero => exact hy
    | succ i ih =>
      rw [show 3*(i+1)=3*i+3 by omega,run_add]
      exact advance (q i) (q (i+1)) _ (light i (by omega)) (odd _ hi) (ih (by omega))
  refine ⟨m,hp,ho,hq,hf,he,?_⟩
  rw [run_add,run_add,hr]
  exact last g _ _ _ _ _ _ _ suffix (middle r (by omega))

#print axioms sustained_residual
end SustainedResidual
