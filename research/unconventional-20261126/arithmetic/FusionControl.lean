import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Ring

/-!
The canonical state is Y=3^h X+c, with either next bit of the anchor available.
The five moves are the indicated realizable parity choices only. The theorem
proves finite accessibility of the fused affine state on a refined cylinder.
-/

namespace FusionControl

abbrev State := ℕ × ℤ

inductive Move : State → State → Prop
  | halve (h : ℕ) (c : ℤ) : Move (h, 2*c) (h,c)
  | wake (h : ℕ) (v : ℤ) (eqn : 2*v=1-(3:ℤ)^(h+1)) : Move (h+1,0) (h+1,v)
  | down (h : ℕ) (u v : ℤ) (eqn : 2*v=u-(3:ℤ)^h) : Move (h+1,u) (h,v)
  | upPlus (u v : ℤ) (eqn : 2*v=3*u+1) : Move (0,u) (1,v)
  | upMinus (u v : ℤ) (eqn : 2*v=1-3*u) : Move (0,u) (1,v)

abbrev Reaches := Relation.ReflTransGen Move

def shortcut (x : ℤ) : ℤ := if x%2=0 then x/2 else (3*x+1)/2

private theorem even_step (a : ℤ) : shortcut (2*a)=a := by
  dsimp [shortcut]; split <;> omega

private theorem odd_step (a : ℤ) : shortcut (2*a+1)=3*a+2 := by
  dsimp [shortcut]; split <;> omega

/-- Every allowed move uses one freely chosen anchor parity. The third
alternative records the sole orientation swap used in the proof. -/
theorem physical {s t : State} (m : Move s t) :
    (∀ z : ℤ, shortcut (3^s.1*(2*z)+s.2) = 3^t.1*shortcut (2*z)+t.2) ∨
    (∀ z : ℤ, shortcut (3^s.1*(2*z+1)+s.2) = 3^t.1*shortcut (2*z+1)+t.2) ∨
    (∀ z : ℤ, shortcut (2*z+1) = 3^t.1*shortcut (3^s.1*(2*z+1)+s.2)+t.2) := by
  cases m with
  | halve h c =>
    left; intro z
    change shortcut (3^h*(2*z)+2*c) = 3^h*shortcut (2*z)+c
    rw [show (3:ℤ)^h*(2*z)+2*c=2*(3^h*z+c) by ring, even_step, even_step]
  | wake h v eqn =>
    right; left; intro z
    change shortcut (3^(h+1)*(2*z+1)+0) = 3^(h+1)*shortcut (2*z+1)+v
    have p : (3:ℤ)^(h+1)=1-2*v := by omega
    rw [p, show (1-2*v)*(2*z+1)+0=2*((1-2*v)*z-v)+1 by ring,
      odd_step, odd_step]
    ring
  | down h u v eqn =>
    right; left; intro z
    change shortcut (3^(h+1)*(2*z+1)+u) = 3^h*shortcut (2*z+1)+v
    have up : u=2*v+(3:ℤ)^h := by omega
    rw [up, show (3:ℤ)^(h+1)*(2*z+1)+(2*v+3^h)=2*(3^h*(3*z+2)+v) by
      rw [pow_succ]; ring, even_step, odd_step]
  | upPlus u v eqn =>
    left; intro z
    change shortcut (3^0*(2*z)+u) = 3^1*shortcut (2*z)+v
    rw [pow_zero, pow_one, one_mul, show 2*z+u=2*(z+u/2)+1 by omega,
      odd_step, even_step]
    omega
  | upMinus u v eqn =>
    right; right; intro z
    change shortcut (2*z+1) = 3^1*shortcut (3^0*(2*z+1)+u)+v
    rw [pow_zero, pow_one, one_mul, show 2*z+1+u=2*(z+(u+1)/2) by omega,
      even_step, odd_step]
    omega

private theorem until_odd (h : ℕ) (c : ℤ) (nonzero : c≠0) :
    ∃ u : ℤ, u%2=1 ∧ u.natAbs ≤ c.natAbs ∧ Reaches (h,c) (h,u) := by
  by_cases odd : c%2=1
  · exact ⟨c, odd, le_rfl, .refl⟩
  · have half : 2*(c/2)=c := by omega
    have nz : c/2≠0 := by omega
    obtain ⟨u, par, height, path⟩ := until_odd h (c/2) nz
    have first : Move (h,c) (h,c/2) := by
      simpa only [half] using (Move.halve h (c/2))
    exact ⟨u, par, by omega, (Relation.ReflTransGen.single first).trans path⟩
termination_by c.natAbs
decreasing_by omega

private theorem odd_pow (h : ℕ) : (3:ℤ)^h%2=1 := by
  have ha : Odd (3:ℤ) := ⟨1, by decide⟩
  obtain ⟨z, eqn⟩ := ha.pow (n := h)
  omega

/-- A single passage from the center through grade one strictly shrinks any
odd nonzero central offset, including the exact two terminal cases ±1. -/
theorem central_pass (c : ℤ) (odd : c%2=1) :
    ∃ g : ℤ, g.natAbs<c.natAbs ∧ Reaches (0,c) (0,g) := by
  let C := if c%4=1 then (3*c+1)/2 else (1-3*c)/2
  have move : Move (0,c) (1,C) := by
    dsimp [C]; split
    · apply Move.upPlus; omega
    · apply Move.upMinus; omega
  have choice : 2*C=3*c+1 ∨ 2*C=1-3*c := by dsimp [C]; split <;> omega
  have even : 2*(C/2)=C := by dsimp [C]; split <;> omega
  have nz : C/2≠0 := by dsimp [C]; split <;> omega
  obtain ⟨u, par, height, path⟩ := until_odd 1 (C/2) nz
  let g := (u-1)/2
  have ge : 2*g=u-1 := by dsimp [g]; omega
  have move2 : Move (1,C) (1,C/2) := by
    simpa only [even] using (Move.halve 1 (C/2))
  have move3 : Move (1,u) (0,g) := Move.down 0 u g (by simpa only [pow_zero] using ge)
  by_cases small : c.natAbs≤1
  · have base : C=2 := by dsimp [C]; split <;> omega
    have two : Move (1,C) (1,1) := by rw [base]; exact Move.halve 1 1
    have endMove : Move (1,1) (0,0) := Move.down 0 1 0 (by decide)
    exact ⟨0, by omega, ((Relation.ReflTransGen.single move).tail two).tail endMove⟩
  · have bound : 8*g.natAbs ≤ 3*c.natAbs+5 := by omega
    exact ⟨g, by omega,
      ((Relation.ReflTransGen.single move).tail move2).trans (path.tail move3)⟩

private theorem center (c : ℤ) : Reaches (0,c) (0,0) := by
  by_cases zero : c=0
  · rw [zero]
  · by_cases odd : c%2=1
    · obtain ⟨g, lower, path⟩ := central_pass c odd
      exact path.trans (center g)
    · have half : 2*(c/2)=c := by omega
      have move : Move (0,c) (0,c/2) := by
        simpa only [half] using (Move.halve 0 (c/2))
      exact (Relation.ReflTransGen.single move).trans (center (c/2))
termination_by c.natAbs
decreasing_by all_goals omega

private theorem nonzero_drop (h : ℕ) (c : ℤ) (nonzero : c≠0) :
    ∃ g : ℤ, Reaches (h+1,c) (h,g) := by
  obtain ⟨u, par, _, path⟩ := until_odd (h+1) c nonzero
  let g := (u-(3:ℤ)^h)/2
  have pp := odd_pow h
  have ge : 2*g=u-(3:ℤ)^h := by dsimp [g]; omega
  exact ⟨g, path.tail (Move.down h u g ge)⟩

/-- Every canonical integer grade and offset admits a finite forced extension
to the exactly fused grade-zero state. -/
theorem accessible (h : ℕ) (c : ℤ) : Reaches (h,c) (0,0) := by
  induction h generalizing c with
  | zero => exact center c
  | succ h ih =>
    by_cases zero : c=0
    · let v := (1-(3:ℤ)^(h+1))/2
      have pp := odd_pow (h+1)
      have eqv : 2*v=1-(3:ℤ)^(h+1) := by dsimp [v]; omega
      have pos : ∀ j : ℕ, 1 ≤ (3:ℤ)^j := by
        intro j
        induction j with
        | zero => decide
        | succ j hj => rw [pow_succ]; omega
      have greater : (1:ℤ)<3^(h+1) := by
        have := pos h
        rw [pow_succ]
        omega
      have nz : v≠0 := by omega
      have wake : Move (h+1,c) (h+1,v) := by rw [zero]; exact Move.wake h v eqv
      obtain ⟨g, drop⟩ := nonzero_drop h v nz
      exact (Relation.ReflTransGen.single wake).trans (drop.trans (ih g))
    · obtain ⟨g, drop⟩ := nonzero_drop h c zero
      exact drop.trans (ih g)

private theorem select_parity (A L e : ℤ) (odd : L%2=1) :
    ∃ r k : ℤ, ∀ z : ℤ, A+L*(r+2*z)=2*(k+L*z)+e := by
  have choices : (A-e)%2=0 ∨ (A+L-e)%2=0 := by omega
  rcases choices with h | h
  · refine ⟨0, (A-e)/2, ?_⟩
    intro z
    have hh : A-e=2*((A-e)/2) := by omega
    calc
      A+L*(0+2*z) = (A-e)+2*(L*z)+e := by ring
      _ = _ := by rw [mul_add]; omega
  · refine ⟨1, (A+L-e)/2, ?_⟩
    intro z
    have hh : A+L-e=2*((A+L-e)/2) := by omega
    calc
      A+L*(1+2*z) = (A+L-e)+2*(L*z)+e := by ring
      _ = _ := by rw [mul_add]; omega

private theorem affine_step (A L : ℤ) (odd : L%2=1) :
    ∃ B M : ℤ, M%2=1 ∧ ∀ z : ℤ, shortcut (A+2*L*z)=B+M*z := by
  by_cases even : A%2=0
  · have eqn : 2*(A/2)=A := by omega
    refine ⟨A/2, L, odd, ?_⟩
    intro z
    rw [show A+2*L*z=2*(A/2+L*z) by rw [mul_add, eqn]; ring, even_step]
  · have eqn : 2*(A/2)+1=A := by omega
    refine ⟨3*(A/2)+2, 3*L, by omega, ?_⟩
    intro z
    rw [show A+2*L*z=2*(A/2+L*z)+1 by
      calc A+2*L*z=(2*(A/2)+1)+2*L*z := congrArg (fun a : ℤ => a+2*L*z) eqn.symm
           _=_ := by ring, odd_step]
    ring

private def cylinder (s : State) : Prop :=
  ∀ A L : ℤ, L%2=1 → ∃ (n : ℕ) (b : ℤ), ∀ z : ℤ,
    let x := A+L*(b+2^n*z)
    shortcut^[n] x = shortcut^[n] (3^s.1*x+s.2)

private theorem cylinder_head {s t : State} (move : Move s t) (remainder : cylinder t) :
    cylinder s := by
  intro A L lOdd
  have orient :
      (∃ e : ℤ, ∀ k : ℤ, shortcut (3^s.1*(2*k+e)+s.2)=3^t.1*shortcut (2*k+e)+t.2) ∨
      (∃ e : ℤ, ∀ k : ℤ, shortcut (2*k+e)=3^t.1*shortcut (3^s.1*(2*k+e)+s.2)+t.2) := by
    rcases physical move with he | ho | hs
    · exact Or.inl ⟨0, by simpa using he⟩
    · exact Or.inl ⟨1, ho⟩
    · exact Or.inr ⟨1, hs⟩
  let X (r z : ℤ) := A+L*(r+2*z)
  let Y (r z : ℤ) := 3^s.1*X r z+s.2
  have getX (r : ℤ) : ∃ B M : ℤ, M%2=1 ∧ ∀ z, shortcut (X r z)=B+M*z := by
    obtain ⟨B,M,odd,eqn⟩ := affine_step (A+L*r) L lOdd
    exact ⟨B,M,odd,fun z => by rw [←eqn]; congr 1; dsimp [X]; ring⟩
  have getY (r : ℤ) : ∃ B M : ℤ, M%2=1 ∧ ∀ z, shortcut (Y r z)=B+M*z := by
    have odd : ((3:ℤ)^s.1*L)%2=1 := by rw [Int.mul_emod, odd_pow, lOdd]; decide
    obtain ⟨B,M,odd',eqn⟩ := affine_step (3^s.1*(A+L*r)+s.2) (3^s.1*L) odd
    exact ⟨B,M,odd',fun z => by rw [←eqn]; congr 1; dsimp [X,Y]; ring⟩
  have after : ∃ (r : ℤ) (n : ℕ) (b : ℤ), ∀ z : ℤ,
      shortcut^[n] (shortcut (X r (b+2^n*z))) =
      shortcut^[n] (shortcut (Y r (b+2^n*z))) := by
    rcases orient with ⟨e,eqn⟩ | ⟨e,eqn⟩
    · obtain ⟨r,k,forced⟩ := select_parity A L e lOdd
      obtain ⟨B,M,odd,aff⟩ := getX r
      obtain ⟨n,b,eqLater⟩ := remainder B M odd
      refine ⟨r,n,b,?_⟩
      intro z
      have today (v : ℤ) : shortcut (Y r v)=3^t.1*shortcut (X r v)+t.2 := by
        dsimp [Y,X]; rw [forced]; exact eqn _
      rw [today,aff]
      exact eqLater z
    · obtain ⟨r,k,forced⟩ := select_parity A L e lOdd
      obtain ⟨B,M,odd,aff⟩ := getY r
      obtain ⟨n,b,eqLater⟩ := remainder B M odd
      refine ⟨r,n,b,?_⟩
      intro z
      have today (v : ℤ) : shortcut (X r v)=3^t.1*shortcut (Y r v)+t.2 := by
        dsimp [Y,X]; rw [forced]; exact eqn _
      rw [today,aff]
      exact (eqLater z).symm
  obtain ⟨r,n,b,eqn⟩ := after
  refine ⟨n+1,r+2*b,?_⟩
  intro z
  dsimp only
  rw [Function.iterate_succ_apply, Function.iterate_succ_apply]
  have lift : A+L*(r+2*b+2^(n+1)*z)=X r (b+2^n*z) := by
    dsimp [X]; rw [pow_succ]; ring
  rw [lift]
  exact eqn z

/-- After any fixed original bits, the current anchor has an odd free slope.
In that parameter there is a whole binary cylinder on which both original
integer trajectories synchronize after exactly the same finite number of
additional shortcut steps. -/
theorem synchronized_cylinder (h : ℕ) (c A L : ℤ) (odd : L%2=1) :
    ∃ (n : ℕ) (b : ℤ), ∀ z : ℤ,
      let x := A+L*(b+2^n*z)
      shortcut^[n] x = shortcut^[n] (3^h*x+c) := by
  have base : cylinder (0,0) := by
    intro B M _
    exact ⟨0,0,fun z => by simp⟩
  have all : cylinder (h,c) := (accessible h c).head_induction_on
    (motive := fun s _ => cylinder s) base (fun move _ ih => cylinder_head move ih)
  exact all A L odd

end FusionControl

#print axioms FusionControl.physical
#print axioms FusionControl.central_pass
#print axioms FusionControl.accessible
#print axioms FusionControl.synchronized_cylinder

#print axioms FusionControl.even_step

#print axioms FusionControl.odd_step

#print axioms FusionControl.until_odd

#print axioms FusionControl.odd_pow

#print axioms FusionControl.center

#print axioms FusionControl.nonzero_drop

#print axioms FusionControl.select_parity

#print axioms FusionControl.affine_step

#print axioms FusionControl.cylinder_head
