import WallRun

namespace WallBank
open WordRank WallRefinement WallShadow WallPeriodic

/-- A finite binary cover. A leaf compares the left and right endpoints after
different numbers of repeated four-bit blocks. An exempt leaf is available
only on the class whose preceding word was already 1011. -/
inductive Certificate where
  | exempt
  | pair (left right : Nat)
  | branch (low high : Certificate)

def valid (K : Nat) : Certificate → Nat → Nat → Bool
  | .exempt,h,r => decide (4≤h ∧ r%16=11)
  | .pair l t,h,r => decide (l≤K ∧ t≤K ∧
      run (h+4*l) (block r l)=run (h+4*t) (block r t+1) ∧
      odds (h+4*l) (block r l)=odds (h+4*t) (block r t+1))
  | .branch low high,h,r => valid K low (h+1) r && valid K high (h+1) (2^h+r)

private theorem block_lift (z r k : Nat) : block (z+r) k=2^(4*k)*z+block r k := by
  induction k with
  | zero => simp [block]
  | succ k ih =>
    rw [block,ih,block,show 4*(k+1)=4*k+4 by omega,pow_add]
    ring

/-- A verified tree puts any positive lift of a mismatching preceding word
on two genuinely intersecting ordinary orbits. -/
theorem sound (C : Certificate) (K h r : Nat) (ok : valid K C h r=true) (z : Nat)
    (reset : (2^h*z+r)%16≠11) :
    ∃ l≤K, ∃ t≤K, ∃ a b, run a (block (2^h*z+r) l)=run b (block (2^h*z+r) t+1) := by
  induction C generalizing h r z with
  | exempt =>
    obtain ⟨ge,r0⟩ := of_decide_eq_true ok
    have p : 2^h=16*2^(h-4) := by
      nth_rw 1 [show h=4+(h-4) by omega]
      rw [pow_add]; rfl
    rw [p,Nat.mul_assoc] at reset
    omega
  | pair l t =>
    obtain ⟨bl,bt,value,count⟩ := of_decide_eq_true ok
    refine ⟨l,bl,t,bt,h+4*l,h+4*t,?_⟩
    rw [block_lift,block_lift,show 2^(4*l)*(2^h*z)=2^(h+4*l)*z by rw [pow_add]; ring,
      show 2^(4*t)*(2^h*z)=2^(h+4*t)*z by rw [pow_add]; ring,Nat.add_assoc,
      (liftPrefix (h+4*l) z (block r l)).1,(liftPrefix (h+4*t) z (block r t+1)).1,value,count]
  | branch low high il ir =>
    obtain ⟨lo,hi⟩ := Bool.and_eq_true_iff.mp ok
    by_cases odd : z%2=1
    · have rep : 2^h*z+r=2^(h+1)*(z/2)+(2^h+r) := by
        have e : z=2*(z/2)+1 := by omega
        nth_rw 1 [e]
        rw [pow_succ]; ring
      rw [rep] at reset ⊢
      exact ir _ _ hi _ reset
    · have rep : 2^h*z+r=2^(h+1)*(z/2)+r := by
        have e : z=2*(z/2) := by omega
        nth_rw 1 [e]
        rw [pow_succ]; ring
      rw [rep] at reset ⊢
      exact il _ _ lo _ reset

theorem forbids (C : Certificate) (K : Nat) (ok : valid K C 0 0=true)
    (col : Coloring) {n : Nat} (cut : Mixed col n) (j : Nat)
    (reset : index col n j%16≠11) : ¬ Copies col n j K := by
  let m := index col n j
  have clean : (2^0*m+0)%16≠11 := by simpa [m] using reset
  obtain ⟨l,bl,t,bt,a,b,e⟩ := sound C K 0 0 ok m clean
  simp only [pow_zero,one_mul,Nat.add_zero] at e
  intro copies
  have el := from_copies col (n:=n) (j:=j) (k:=l) (fun i hi => copies i (by omega))
  have er := from_copies col (n:=n) (j:=j) (k:=t) (fun i hi => copies i (by omega))
  have lhs := (index_eq col cut (j+4*l)).1
  have rhs := (index_eq col cut (j+4*t)).2
  rw [el] at lhs
  rw [er] at rhs
  exact cut (lhs.symm.trans (((propagated_run col a _).symm.trans
    ((congrArg col.color e).trans (propagated_run col b _))).trans rhs))

end WallBank
