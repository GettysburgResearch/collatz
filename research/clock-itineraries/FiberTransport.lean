module

public import TowerFrontierAffine
import all TernaryItinerary

public section
namespace Collatz.Itinerary.FiberTransport

set_option autoImplicit false

private theorem power_lift (n : Nat) :
    ∃ u, 2^(2*3^n) = 1+3^(n+1)*u ∧ u%3=1 := by
  induction n with
  | zero => exact ⟨1,by decide,by decide⟩
  | succ n ih =>
    obtain ⟨u,hu,unit⟩ := ih
    let m := 3^(n+1)
    refine ⟨u+m*u*u+3^n*m*u*u*u,?_,?_⟩
    · have h : 2*3^(n+1)=(2*3^n)*3 := by rw [Nat.pow_succ]; ac_rfl
      rw [h,Nat.pow_mul,hu]
      simp only [m,Nat.pow_succ,Nat.pow_zero,Nat.one_mul]
      grind
    · have z : m%3=0 := by simp [m,Nat.pow_succ]
      simp [Nat.add_mod,Nat.mul_mod,z,unit]

private theorem unit_pow_two (n x : Nat) (hx : x%3≠0) : (2^n*x)%3≠0 := by
  induction n with
  | zero => simpa
  | succ n ih =>
    rw [Nat.pow_succ,Nat.mul_right_comm]
    omega

private theorem other_unit (a b : Nat) (ha : a%3≠0) (hb : b%3≠0)
    (ne : a%3≠b%3) : (2*a)%3=b%3 := by
  have A : a%3=1 ∨ a%3=2 := by omega
  have B : b%3=1 ∨ b%3=2 := by omega
  rcases A with h | h <;> rcases B with j | j <;> simp_all [Nat.mul_mod]

private theorem three_digits (a z : Nat) (hz : z%3≠0) :
    a%3=0 ∨ (a+z)%3=0 ∨ (a+z+z)%3=0 := by
  have A : a%3=0 ∨ a%3=1 ∨ a%3=2 := by omega
  have Z : z%3=1 ∨ z%3=2 := by omega
  rcases A with h | h | h <;> rcases Z with j | j <;> simp [Nat.add_mod,h,j]

private theorem from_residue (a b : Nat) (le : b≤a) (eq : a%3=b%3) :
    a=b+3*((a-b)/3) := by omega

/-- At every ternary precision, powers of two send any supplied unit into
any prescribed unit class, with an arbitrarily large positive lift. -/
theorem large_dyadic_lift (k b z M : Nat) (hb : b%3≠0) (hz : z%3≠0) :
    ∃ e v, M≤e ∧ 2^e*b=z+3^(k+1)*v := by
  induction k with
  | zero =>
    let e := M+z
    let y := 2^e*b
    have big : z≤y := by
      have h := Nat.lt_two_pow_self (n:=e)
      have bpos : 0<b := by omega
      have h' := Nat.le_mul_of_pos_right (2^e) bpos
      dsimp [y,e] at *
      omega
    have h := unit_pow_two e b hb
    change y%3≠0 at h
    by_cases eq : y%3=z%3
    · exact ⟨e,(y-z)/3,by dsimp [e]; omega,by change y=z+3*((y-z)/3); omega⟩
    · refine ⟨e+1,(2*y-z)/3,by dsimp [e]; omega,?_⟩
      have eq' : 2^(e+1)*b=2*y := by simp only [y,Nat.pow_succ]; ac_rfl
      rw [eq']
      change 2*y=z+3*((2*y-z)/3)
      exact from_residue _ _ (by omega) (other_unit y z h hz eq)
  | succ k ih =>
    obtain ⟨e,v,he,eq⟩ := ih
    obtain ⟨u,hu,unit⟩ := power_lift k
    let m := 3^(k+1)
    let p := 2*3^k
    have advance (d v : Nat) (eq : 2^d*b=z+m*v) :
        ∃ v', 2^(d+p)*b=z+m*v' ∧ v'%3=(v+z)%3 := by
      refine ⟨v+u*(2^d*b),?_,?_⟩
      · have rule : 2^p=1+m*u := hu
        rw [Nat.pow_add,rule]
        grind
      · have mz : m%3=0 := by simp [m,Nat.pow_succ]
        rw [eq]
        simp [Nat.add_mod,Nat.mul_mod,unit,mz]
    have pick : ∃ d w, M≤d ∧ 2^d*b=z+m*w ∧ w%3=0 := by
      by_cases done : v%3=0
      · exact ⟨e,v,he,eq,done⟩
      obtain ⟨v',eq',hv'⟩ := advance e v eq
      by_cases done' : v'%3=0
      · exact ⟨e+p,v',by omega,eq',done'⟩
      obtain ⟨v'',eq'',hv''⟩ := advance (e+p) v' eq'
      have last := (three_digits v z hz).resolve_left done
      have sum := last.resolve_left (fun h => done' (hv'.trans h))
      have endmod : (v'+z)%3=(v+z+z)%3 := by
        rw [Nat.add_mod v',hv',Nat.mod_add_mod]
        simp
      exact ⟨e+p+p,v'',by omega,eq'',hv''.trans (endmod.trans sum)⟩
    obtain ⟨d,w,hd,eqw,hw⟩ := pick
    refine ⟨d,w/3,hd,?_⟩
    have split : w=3*(w/3) := by omega
    calc
      2^d*b = z+m*w := eqw
      _ = z+3^((k+1)+1)*(w/3) := by
        conv => lhs; rw [split]
        simp only [m,Nat.pow_succ 3 (k+1)]; ac_rfl

#print axioms large_dyadic_lift

/-- Exact odd gaps, listed backwards from the supplied ordinary endpoint. -/
inductive Row : List Nat → Nat → Nat → Prop where
  | nil (q : Nat) : Row [] q q
  | cons {e q y x es} (edge : Gap e y q) (tail : Row es x y) :
      Row (e::es) x q

theorem Row.follow {es : List Nat} {x q : Nat} (p : Row es x q) :
    run es.sum x=q := by
  induction p with
  | nil => rfl
  | @cons e q y x es edge tail ih =>
    rw [List.sum_cons,Nat.add_comm,run_add,ih,edge.follow]

private theorem gap_up {e y q : Nat} (g : Gap e y q) (t : Nat) :
    Gap e (y+2^e*(2*t)) (q+3*(2*t)) := by
  refine ⟨g.pos,?_,?_,?_⟩
  · have ev : 2^e*(2*t)=2*(2^e*t) := by ac_rfl
    rw [ev]; have := g.oddSource; omega
  · have := g.oddTarget; omega
  · have eq := g.eqn
    rw [Nat.mul_add,eq]
    grind

private theorem gap_down {e y' q t : Nat} (pos : 0<q)
    (g : Gap e y' (q+3*(2*t))) :
    ∃ y, Gap e y q ∧ y'=y+2^e*(2*t) := by
  let D := 2^e*(2*t)
  have eq : 2^e*q+3*D=3*y'+1 := by
    calc
      2^e*q+3*D = 2^e*(q+3*(2*t)) := by simp only [D,Nat.mul_add]; ac_rfl
      _ = 3*y'+1 := g.eqn
  have positive := Nat.mul_pos (Nat.two_pow_pos e) pos
  have large : D≤y' := by omega
  refine ⟨y'-D,⟨g.pos,?_,?_,by omega⟩,by change y'=y'-D+D; omega⟩
  · have ev : D=2*(2^e*t) := by dsimp [D]; ac_rfl
    have dz : D%2=0 := by rw [ev]; simp
    have join : y'-D+D=y' := Nat.sub_add_cancel large
    have h : (y'-D+D)%2=1 := (congrArg (·%2) join).trans g.oddSource
    simpa [Nat.add_mod,dz] using h
  · have := g.oddTarget; omega

/-- On a fixed clock and odd depth the entire inverse fiber is translated,
including absent words. The theorem holds word by word at arbitrary costs. -/
theorem whole_row (es : List Nat) (q t x' : Nat) (hq : 0<q) :
    Row es x' (q+2*3^es.length*t) ↔
      ∃ x, Row es x q ∧ x'=x+2*2^es.sum*t := by
  induction es generalizing q t x' with
  | nil =>
    simp only [List.length_nil,List.sum_nil,Nat.pow_zero,Nat.mul_one]
    constructor
    · intro p; cases p; exact ⟨q,.nil q,rfl⟩
    · rintro ⟨x,p,eq⟩; cases p; rw [eq]; exact .nil _
  | cons e es ih =>
    have target : q+2*3^(e::es).length*t=q+3*(2*(3^es.length*t)) := by
      simp only [List.length_cons,Nat.pow_succ]; ac_rfl
    have middle (y : Nat) :
        y+2^e*(2*(3^es.length*t))=y+2*3^es.length*(2^e*t) := by ac_rfl
    have source (x : Nat) :
        x+2*2^es.sum*(2^e*t)=x+2*2^(e::es).sum*t := by
      simp only [List.sum_cons,Nat.pow_add]; ac_rfl
    rw [target]
    constructor
    · intro p
      cases p with
      | cons edge tail =>
        obtain ⟨y,g,eq⟩ := gap_down hq edge
        rw [eq,middle] at tail
        have yp : 0<y := by have := g.oddSource; omega
        obtain ⟨x,rest,src⟩ := (ih y (2^e*t) x' yp).mp tail
        exact ⟨x,.cons g rest,src.trans (source x)⟩
    · rintro ⟨x,p,eq⟩
      cases p with
      | cons edge rest =>
        have up := gap_up edge (3^es.length*t)
        rw [middle] at up
        have yp := edge.oddSource
        exact .cons up ((ih _ _ _ (by omega)).mpr ⟨x,rest,eq.trans (source x).symm⟩)

#print axioms whole_row

/-- Parity bits in chronological order for the ordinary shortcut map. -/
def parityPrefix : Nat → Nat → List Nat
  | 0, _ => []
  | h+1, x => x%2 :: parityPrefix h (step x)

private theorem same_prefix (h n t : Nat) :
    parityPrefix h (n+2^h*t)=parityPrefix h n := by
  induction h generalizing n t with
  | zero => rfl
  | succ h ih =>
    have double : 2^(h+1)*t=2*(2^h*t) := by rw [Nat.pow_succ]; ac_rfl
    rw [parityPrefix,parityPrefix,double]
    have parity : (n+2*(2^h*t))%2=n%2 := by omega
    rw [parity]
    congr 1
    by_cases even : n%2=0
    · have eq : step (n+2*(2^h*t))=step n+2^h*t := by
        simp only [step,parity,even,↓reduceIte]; omega
      rw [eq,ih]
    · have eq : step (n+2*(2^h*t))=step n+2^h*(3*t) := by
        have reorder : 2^h*(3*t)=3*(2^h*t) := by ac_rfl
        simp only [step,parity,even,↓reduceIte,reorder]; omega
      rw [eq,ih]

private theorem run_unit (h x : Nat) (unit : x%3≠0) : run h x%3≠0 := by
  induction h generalizing x with
  | zero => exact unit
  | succ h ih =>
    apply ih
    unfold step
    split <;> omega

private theorem track_value (h x k : Nat) : (TowerFrontier.track h x k).1=run h x := by
  induction h generalizing x k with
  | zero => rfl
  | succ h ih =>
    simp only [TowerFrontier.track,run,step]
    split <;> apply ih

/-- An arbitrarily large copy of a forward prefix can be sent to any
prescribed unit target. The free parameter preserves the entire inverse
fiber at every odd depth up to K, even at unbounded total clock. -/
theorem copy_to_target (q b H K B : Nat) (hq : q%3≠0) (hb : b%3≠0) :
    ∃ u, B<u ∧ ∃ d,
      let q' := q+2^(H+1)*3^K*u
      parityPrefix (H+1) q'=parityPrefix (H+1) q ∧
      run (H+1) q'=2^d*b ∧ run (H+1+d) q'=b ∧
      ∀ (es : List Nat), es.length≤K → ∀ x',
        Row es x' q' ↔ ∃ x, Row es x q ∧
          x'=x+2*2^es.sum*(2^H*3^(K-es.length)*u) := by
  let h := H+1
  let z := run h q
  let g := (TowerFrontier.track h q K).2
  let M := z+3^(g+1)*B
  obtain ⟨d,v,hd,eq⟩ := large_dyadic_lift g b z M hb (run_unit h q hq)
  have powerbig := Nat.lt_two_pow_self (n:=d)
  have bpos : 0<b := by omega
  have scale := Nat.le_mul_of_pos_right (2^d) bpos
  have large : B<v := by
    apply Classical.byContradiction
    intro small
    have le := Nat.mul_le_mul_left (3^(g+1)) (show v≤B by omega)
    dsimp [M] at hd
    omega
  let u := 3*v
  let q' := q+2^h*3^K*u
  have top : run h q'=2^d*b := by
    rw [show run h q'=z+3^g*u by
      simpa only [q',z,g,track_value] using TowerFrontier.affine h q K u]
    rw [eq,Nat.pow_succ]
    dsimp [u]
    ac_rfl
  refine ⟨u,by dsimp [u]; omega,d,?_,top,?_,?_⟩
  · simpa only [Nat.mul_assoc,h] using same_prefix h q (3^K*u)
  · rw [run_add,top,halve]
  · intro es short x'
    have split : K=es.length+(K-es.length) := by omega
    have origin : q'=q+2*3^es.length*(2^H*3^(K-es.length)*u) := by
      dsimp [q',h]
      conv => lhs; rw [split,Nat.pow_add 3,Nat.pow_succ 2 H]
      ac_rfl
    change Row es x' q' ↔ _
    rw [origin]
    exact whole_row es q _ x' (by omega)

#print axioms copy_to_target

end Collatz.Itinerary.FiberTransport
