import ResidualDescent

/-! A seven-letter ordinary past forces a smaller predecessor of the next
two-clock intermediate, with no condition on its future trajectory. -/
set_option maxRecDepth 12000
set_option maxHeartbeats 1500000
namespace PastCylinder
open CycleShadows WordCert

private theorem next_edge {D M C N K B x y q : Nat}
    (pre : D*x=M*q+C) (edge : N*y=B*x+K) :
    (D*N)*y=(B*M)*q+(B*C+D*K) := by
  calc
    D*N*y = D*(N*y) := by ac_rfl
    _ = B*(D*x) + D*K := by rw [edge,Nat.mul_add]; ac_rfl
    _ = _ := by rw [pre,Nat.mul_add]; ac_rfl

private def bits : List Bool :=
  [true,true,true,true,true,true,true,true,false,true,true,true,false,true,
   false,true,false,false,true,false,false,false]

private theorem source_partner (p b : Nat) (ab : 64*b=81*p+119) :
    ∃ m, 0<m ∧ m%2=1 ∧ m<p ∧ m<(3*p+1)/4 ∧ 32*m+11=3*p := by
  have R : (81*p)%64=9 := calc
    _ = ((81*p+119)+9)%64 := by
      rw [Nat.add_assoc]
      exact (Nat.add_mul_mod_self_left (81*p) 64 2).symm
    _ = (64*b+9)%64 := by rw [ab]
    _ = 9 := Nat.mul_add_mod _ _ _
  have pr : p%64=57 := calc
    p%64=((49*81)%64*p)%64 := by rw [show (49*81)%64=1 by decide,Nat.one_mul]
    _=(49*81*p)%64 := Nat.mod_mul_mod _ _ _
    _=(49*(81*p%64))%64 := by rw [Nat.mul_mod_mod,Nat.mul_assoc]
    _=57 := by rw [R]
  let k := p/64
  have pk : p=64*k+57 := by
    have dec := Nat.mod_add_div p 64
    rw [pr] at dec
    exact dec.symm.trans (Nat.add_comm _ _)
  let m := 6*k+5
  have eqm : 32*m+11=3*p := by rw [pk]; dsimp [m]; omega
  have odd : m%2=1 := by dsimp [m]; omega
  refine ⟨m,by dsimp [m]; omega,odd,?_,?_,eqm⟩
  · rw [pk]; dsimp [m]; omega
  · rw [pk]; dsimp [m]; omega

private theorem path_eq (p m f : Nat) (G : 134217728*f=14348907*p+116769005)
    (eqm : 32*m+11=3*p) : 4194304*f=4782969*m+5293177 := by
  rw [show 14348907*p=4782969*(3*p) from Nat.mul_assoc 4782969 3 p,←eqm,Nat.mul_add] at G
  apply Nat.eq_of_mul_eq_mul_left (n:=32) (by decide)
  rw [Nat.mul_add,←Nat.mul_assoc,←Nat.mul_assoc]
  rw [←Nat.mul_assoc,Nat.add_assoc] at G
  exact G

private theorem realization (m f : Nat) (path : 4194304*f=4782969*m+5293177) :
    run T 22 m=f := by
  have hlen : bits.length=22 := by decide
  have hs : scale bits=4782969 := by decide
  have hc : carry bits=5293177 := by decide
  rw [←hlen]
  apply realize
  rw [hlen,hs,hc]
  exact path

/-- The ordinary history is LLLLPLP; the last equality supplies exactly
the next two shortcut clocks, whether or not there is a full light block. -/
theorem past_descent (p a b c d e u q f : Nat)
    (h1 : 8*a=9*p+7) (h2 : 8*b=9*a+7) (h3 : 8*c=9*b+7)
    (h4 : 8*d=9*c+7) (h5 : 32*e=9*d+5) (h6 : 8*u=9*e+7)
    (h7 : 32*q=9*u+5) (mid : 4*f=3*q+1) :
    ∃ m, 0<m ∧ m%2=1 ∧ m<f ∧ m<q ∧ m<p ∧ m<(3*p+1)/4 ∧ 32*m+11=3*p ∧ run T 22 m=f := by
  have ab := next_edge h1 h2
  change 64*b=81*p+119 at ab
  obtain ⟨m,hp,ho,hx,hi,eqm⟩ := source_partner p b ab
  have G := next_edge (next_edge (next_edge (next_edge (next_edge
    (next_edge (next_edge h1 h2) h3) h4) h5) h6) h7) mid
  change 134217728*f=14348907*p+116769005 at G
  have path := path_eq p m f G eqm
  have lf : m<f := by
    apply Nat.lt_of_mul_lt_mul_left (a:=4194304)
    rw [path]
    exact Nat.lt_of_le_of_lt (Nat.mul_le_mul_right m (by decide : 4194304≤4782969))
      (Nat.lt_add_of_pos_right (by decide))
  refine ⟨m,hp,ho,lf,?_,hx,hi,eqm,realization m f path⟩
  clear ab h1 h2 h3 h4 h5 h6 h7 hx hi eqm G path hp ho
  omega

#print axioms past_descent
end PastCylinder
