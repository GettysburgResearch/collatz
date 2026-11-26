import InverseBudget

/-! Every positive inverse source smaller than the Mersenne start first
crosses a translated dyadic multiple of that same start. The complete
initial staircase is allowed. -/
namespace InversePhase
open InverseBudget

private theorem above (r s n b y : Nat) (np : 0<n) (cap : b≤2^s)
    (disp : y+b=3^r*2^s*n) : 2^r*n≤y+1 := by
  have pow : (2:Nat)^r≤3^r := Nat.pow_le_pow_left (by decide) r
  have base : 1≤(2:Nat)^s := Nat.one_le_pow _ _ (by decide)
  have pos : 1≤2^r*n := Nat.mul_pos (Nat.pow_pos (by decide)) np
  have mul := Nat.mul_le_mul_right (2^s*n) pow
  have left:=Nat.mul_le_mul_left (2^r*n-1) base
  have exact_sub : 2^r*n-1+1=2^r*n := by omega
  have decomp : 2^s*((2^r*n-1)+1)=2^s*(2^r*n) := congrArg (fun t => 2^s*t) exact_sub
  nlinarith only [mul,cap,disp,left,decomp,exact_sub]

private def Gate (w : List Bool) (r s n z : Nat) : Prop :=
  ∃ S b x : Nat, ∃ tail : List Bool, s≤S ∧ 0<b ∧ b≤2^S ∧
    x+b=2^S*(2^r*n) ∧ run tail x=some z ∧ grade w=r+grade tail ∧
    w.length+s=r+S+tail.length

private theorem separate (w : List Bool) (r s n b y z : Nat) (np : 0<n)
    (bp : 0<b) (cap : b≤2^s) (disp : y+b=3^r*2^s*n) (leg : run w y=some z) :
    2^r*n≤z+1 ∨ Gate w r s n z := by
  induction w generalizing r s n b y with
  | nil =>
    have yz : y=z := by simpa [run] using leg
    exact Or.inl (yz ▸ above r s n b y np cap disp)
  | cons bit w ih =>
    cases r with
    | zero =>
      right
      exact ⟨s,b,y,bit::w,by omega,bp,cap,by simpa using disp,leg,by simp,by simp; omega⟩
    | succ r =>
      cases bit with
      | false =>
        have eq : 2*y+2*b=3^(r+1)*2^(s+1)*n := calc
          _=2*(y+b) := by ring
          _=_ := by rw [disp,pow_succ (2:Nat) s]; ring
        have lim : 2*b≤2^(s+1) := by rw [pow_succ]; omega
        rcases ih (r+1) (s+1) n (2*b) (2*y) np (by omega) lim eq leg with good|gate
        · exact Or.inl good
        · obtain ⟨S,B,x,t,le,po,bu,rel,ok,gr,cl⟩:=gate
          exact Or.inr ⟨S,B,x,t,by omega,po,bu,rel,ok,gr,by simp; omega⟩
      | true =>
        unfold run at leg
        split at leg
        next legal =>
          let v:=(2*y-1)/3
          let c:=(2*b+1)/3
          have md : y+b=3*(3^r*2^s*n) := by rw [disp,pow_succ]; ring
          have uc : b%3=1 := by omega
          have ve : 3*v+1=2*y := by dsimp [v]; omega
          have ce : 3*c=2*b+1 := by dsimp [c]; omega
          have eq : v+c=3^r*2^s*(2*n) := by nlinarith only [md,ve,ce]
          rcases ih r s (2*n) c v (by omega) (by omega) (by omega) eq leg with good|gate
          · left; rw [pow_succ]; nlinarith only [good]
          · obtain ⟨S,B,x,t,le,po,bu,rel,ok,gr,cl⟩:=gate
            refine Or.inr ⟨S,B,x,t,le,po,bu,?_,ok,?_,?_⟩
            · rw [rel,pow_succ]; ring
            · change grade w+1=r+1+grade t; omega
            · simp; omega
        next => contradiction

/-- At any original phase u≤j, every strictly smaller ordinary inverse
source leaves the initial comparison grade via one of at most 2^s labels
for its s extra doublings. The surplus odds and clocks are exact. -/
theorem all_phase_gate (w : List Bool) (j u y z : Nat) (phase : u≤j)
    (point : y+1=3^u*2^(j-u)) (legal : run w y=some z) (cheap : z<2^j-1) :
    ∃ s b x : Nat, ∃ tail : List Bool, 0<b ∧ b≤2^s ∧ x+b=2^s*2^j ∧
      run tail x=some z ∧ grade w=u+grade tail ∧ w.length=u+s+tail.length := by
  have eq : 2^u*2^(j-u)=(2:Nat)^j := by rw [←pow_add]; congr 1; omega
  rcases separate w u 0 (2^(j-u)) 1 y z (by positivity) (by decide) (by decide)
      (by simpa using point) legal with large|gate
  · rw [eq] at large; omega
  · obtain ⟨s,b,x,t,_,pos,bd,e,ok,gr,cl⟩:=gate
    exact ⟨s,b,x,t,pos,bd,by rwa [eq] at e,ok,gr,by simpa using cl⟩

#print axioms all_phase_gate
end InversePhase
