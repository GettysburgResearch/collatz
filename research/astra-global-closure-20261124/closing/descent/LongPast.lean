import ResidualDescent

/-! A twelve-block past with isolated Ls gives a smaller odd predecessor of
the following two-clock light intermediate, for arbitrary continuations. -/
set_option maxHeartbeats 1500000
namespace LongPast
open CycleShadows WordCert

private theorem append_edge {D M C N K B x y q : Nat}
    (pre : D*x=M*q+C) (edge : N*y=B*x+K) :
    (D*N)*y=(B*M)*q+(B*C+D*K) := by
  calc
    D*N*y = D*(N*y) := by ac_rfl
    _ = B*(D*x) + D*K := by rw [edge,Nat.mul_add]; ac_rfl
    _ = _ := by rw [pre,Nat.mul_add]; ac_rfl

private def bits : List Bool :=
  [true, true, true, true, true, true, false, true, true, true, true, true, false, true, true, true, true, false, true, true, false, false, false, true, true, true, true, false, false, false, true, false, false, false, true, false, true, false]

/-- Physical endpoint certificate for the displayed PLPPPLPPLPPP history.
The last equality requires exactly the following two-clock intermediate. -/
theorem isolated_lights (x : Nat → Nat) (f : Nat)
    (h1 : 32*x 1=9*x 0+5)
    (h2 : 8*x 2=9*x 1+7)
    (h3 : 32*x 3=9*x 2+5)
    (h4 : 32*x 4=9*x 3+5)
    (h5 : 32*x 5=9*x 4+5)
    (h6 : 8*x 6=9*x 5+7)
    (h7 : 32*x 7=9*x 6+5)
    (h8 : 32*x 8=9*x 7+5)
    (h9 : 8*x 9=9*x 8+7)
    (h10 : 32*x 10=9*x 9+5)
    (h11 : 32*x 11=9*x 10+5)
    (h12 : 32*x 12=9*x 11+5)
    (mid : 4*f=3*x 12+1) :
    ∃ m, 0<m ∧ m%2=1 ∧ m<f ∧ run T 38 m=f := by
  have a2 := append_edge h1 h2
  have a3 := append_edge a2 h3
  have a4 := append_edge a3 h4
  have a5 := append_edge a4 h5
  have a6 := append_edge a5 h6
  have a7 := append_edge a6 h7
  have a8 := append_edge a7 h8
  have a9 := append_edge a8 h9
  have a10 := append_edge a9 h10
  have a11 := append_edge a10 h11
  have a12 := append_edge a11 h12
  have full := append_edge a12 mid
  change 72057594037927936*f=847288609443*x 0+30946375547751703 at full
  clear h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 mid a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12
  have allocation : 282429536481 ∣ 72057594037927936*(f+218491190612) := by
    refine ⟨3*x 0+55744699050175735,?_⟩
    rw [Nat.mul_add, full]
    omega
  have cop : Nat.Coprime 282429536481 72057594037927936 := by decide
  obtain ⟨j,hj⟩ := cop.dvd_of_dvd_mul_left allocation
  clear full allocation cop
  cases j with
  | zero => simp at hj
  | succ j =>
    rw [Nat.mul_succ] at hj
    have fval : f=282429536481*j+63938345869 := by omega
    let m := 274877906944*j+62228755903
    refine ⟨m,?_,?_,?_,?_⟩
    · dsimp [m]; omega
    · dsimp [m]; omega
    · dsimp [m]; omega
    · have hl : bits.length=38 := by decide
      have hs : scale bits=282429536481 := by decide
      have hc : carry bits=458686216993 := by decide
      rw [←hl]
      apply realize
      rw [hl,hs,hc]
      dsimp [m]
      omega

#print axioms isolated_lights
end LongPast
