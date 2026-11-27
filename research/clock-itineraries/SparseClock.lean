module

public import TernaryItinerary

public section
namespace Collatz.Itinerary.Sparse

set_option autoImplicit false

/-- A list of exact gaps, in chronological order. -/
inductive Path : List Nat → Nat → Nat → Prop where
  | nil (x : Nat) : Path [] x x
  | cons {x y q e : Nat} {es : List Nat} (gap : Gap e x y) (rest : Path es y q) :
      Path (e::es) x q

def defects : List Nat → Nat
  | [] => 0
  | e::es => (if e=2 then 0 else 1) + defects es

def cost : List Nat → Nat
  | [] => 0
  | e::es => (if e=2 then 0 else e) + cost es

def ones : List Nat → Nat
  | [] => 0
  | e::es => (if e=1 then 1 else 0) + ones es

private theorem budget (es : List Nat) :
    es.sum + 2*defects es = 2*es.length + cost es := by
  induction es with
  | nil => rfl
  | cons e es ih =>
    by_cases h : e=2 <;> simp [List.sum_cons,defects,cost,h] <;> omega

private theorem Path.snoc {es : List Nat} {x y q e : Nat} (p : Path es x y)
    (g : Gap e y q) : Path (es++[e]) x q := by
  induction p with
  | nil => exact .cons g (.nil _)
  | cons edge _ ih => exact .cons edge (ih g)

private theorem path_of_route {q s a : Nat} {rs : List Bool} (r : Route q rs s a) :
    ∃ es, Path es a q ∧ es.sum=s ∧ es.length=rs.length := by
  induction r with
  | nil => exact ⟨[],.nil _,rfl,rfl⟩
  | @cons q y x e s mark rs edge _ _ ih =>
    obtain ⟨es,p,ht,hl⟩ := ih
    exact ⟨es++[e],p.snoc edge,by simp [List.sum_append,ht,Nat.add_comm],by simp [hl]⟩

private theorem Path.unit_budget {es : List Nat} {x q : Nat} (p : Path es x q) :
    2*es.length ≤ es.sum+ones es := by
  induction p with
  | nil => decide
  | @cons x y q e es edge _ ih =>
    have he := edge.pos
    by_cases h : e=1 <;> simp [ones,h] <;> omega

/-- A nonconverging gate supplies linearly many unit gaps in its own suffix. -/
theorem bad_suffix_unit_gaps {q s a : Nat} {rs : List Bool} (r : Route q rs s a)
    (bad : ¬ReachesOne a) (hq : 0<q) :
    ∃ es, Path es a q ∧ es.sum=s ∧ es.length=rs.length ∧
      2*rs.length ≤ 5*ones es+5*a := by
  obtain ⟨es,p,ht,hl⟩ := path_of_route r
  have h := r.clock_bound bad hq
  have hu := p.unit_budget
  exact ⟨es,p,ht,hl,by omega⟩

private theorem defect_cost {es : List Nat} {x q : Nat} (p : Path es x q) :
    3*defects es ≤ cost es + 2*ones es := by
  induction p with
  | nil => decide
  | @cons x y q e es g _ ih =>
    have he := g.pos
    by_cases h₂ : e=2 <;> by_cases h₁ : e=1 <;> simp [defects,cost,ones,h₁,h₂] <;> omega

/-- Every exceptional gap is paid for by a unit gap on a balanced row. -/
theorem Path.balanced {es : List Nat} {x q : Nat} (p : Path es x q)
    (bal : es.sum=2*es.length) : cost es=2*defects es ∧ defects es ≤ 2*ones es := by
  have h := budget es
  have t := defect_cost p
  omega

private theorem pow4mod (k : Nat) : 4^k%3=1 := by
  induction k with
  | zero => decide
  | succ k ih => rw [Nat.pow_succ,Nat.mul_mod,ih]

/-- An entire run of gaps two has both endpoints on a single progression. -/
theorem neutral_parameter {x q k : Nat} (p : Path (List.replicate k 2) x q) (pos : 0<q) :
    ∃ t, x=1+4^k*t ∧ q=1+3^k*t := by
  induction k generalizing x with
  | zero => cases p; exact ⟨q-1,by simp; omega,by simp; omega⟩
  | succ k ih =>
    rw [List.replicate_succ] at p
    cases p with
    | @cons _ y _ _ _ g rest =>
      obtain ⟨t,hy,hq⟩ := ih rest
      have eqn := g.eqn
      change 4*y=3*x+1 at eqn
      have et : 3*x = 3+4^(k+1)*t := by
        rw [hy,Nat.mul_add] at eqn
        rw [Nat.pow_succ,Nat.mul_comm (4^k) 4,Nat.mul_assoc]
        omega
      have modt : 4^(k+1)*t%3=0 := by omega
      rw [Nat.mul_mod,pow4mod,Nat.one_mul,Nat.mod_mod] at modt
      have ht : t=3*(t/3) := by omega
      refine ⟨t/3,?_,?_⟩
      · conv at et => rhs; rw [ht,Nat.mul_left_comm]
        omega
      · conv at hq => rhs; rw [ht,←Nat.mul_assoc,←Nat.pow_succ]
        exact hq

/-- All neutral lengths occur, including at the fixed point when z=0. -/
theorem neutral_realize (k z : Nat) :
    Path (List.replicate k 2) (1+2*(4^k*z)) (1+2*(3^k*z)) := by
  induction k generalizing z with
  | zero => exact .nil _
  | succ k ih =>
    let A := 4^k*z
    have sx : 4^(k+1)*z=4*A := by dsimp [A]; rw [Nat.pow_succ]; ac_rfl
    have sy : 4^k*(3*z)=3*A := by dsimp [A]; ac_rfl
    have sz : 3^(k+1)*z=3^k*(3*z) := by rw [Nat.pow_succ,Nat.mul_assoc]
    rw [List.replicate_succ,sx,sz]
    refine .cons (y:=1+2*(4^k*(3*z))) ?_ (ih (3*z))
    rw [sy]
    exact ⟨by decide,by omega,by omega,by omega⟩

/-- Offset for the coordinate x-1. A neutral gap contributes zero. -/
def shiftedOffset : List Nat → Int
  | [] => 0
  | e::es => (3:Int)^es.length*((2:Int)^e-4)+(2:Int)^e*shiftedOffset es

theorem Path.shifted_identity {x q : Nat} {es : List Nat} (p : Path es x q) :
    (3:Int)^es.length*((x:Int)-1) = (2:Int)^es.sum*((q:Int)-1)+shiftedOffset es := by
  induction p with
  | nil => simp [shiftedOffset]
  | @cons x y q e es g rest ih =>
    have hi := congrArg Int.ofNat g.eqn
    have edge : 3*((x:Int)-1)=(2:Int)^e*((y:Int)-1)+(2^e-4) := by
      change (2:Int)^e*(y:Int)=3*(x:Int)+1 at hi
      rw [Int.mul_sub,Int.mul_sub,Int.mul_one,Int.mul_one]; omega
    simp only [List.length_cons,List.sum_cons,Int.pow_succ,Int.pow_add,shiftedOffset]
    rw [Int.mul_assoc,edge,Int.mul_add,←Int.mul_assoc,Int.mul_comm _ ((2:Int)^e),
      Int.mul_assoc,ih,Int.mul_add]
    ac_rfl

/-- Select any subset of the internal terms in the shifted identity.
Use z=q-1 to retain its terminal term and z=0 to omit that term. -/
def subsum : List (Nat × Bool) → Int → Int
  | [], z => z
  | (e,on)::xs,z =>
      (if on then (3:Int)^xs.length*((2:Int)^e-4) else 0) + (2:Int)^e*subsum xs z

private theorem odd_three (k : Nat) : (3:Int)^k%2=1 := by
  induction k with
  | zero => decide
  | succ k ih => rw [Int.pow_succ,Int.mul_emod,ih]; decide

private theorem selected_ne {e k : Nat} {v : Int} (he : 0<e) (hne : e≠2) (hv : v%2=0) :
    (3:Int)^k*((2:Int)^e-4)+(2:Int)^e*v ≠ 0 := by
  have h₃ := odd_three k
  by_cases one : e=1
  · subst e
    simp only [Int.pow_one]
    omega
  · obtain ⟨i,hi⟩ := Nat.exists_eq_add_of_le (show 3≤e by omega)
    rw [hi,Int.pow_add]
    change (3:Int)^k*(8*2^i-4)+(8*2^i)*v ≠ 0
    have eqn : (3:Int)^k*(8*2^i-4)+(8*2^i)*v =
        8*(3^k*2^i+2^i*v)-4*3^k := by grind
    rw [eqn]
    omega

/-- The only zero subsum of the right-hand terms omits every exception
and has zero terminal coefficient. This is the nondegeneracy used in the
fixed-arity S-unit estimate. -/
theorem subsum_zero {xs : List (Nat × Bool)} {z : Int} (hz : z%2=0)
    (legal : ∀ a ∈ xs, 0<a.1 ∧ (a.2=true → a.1≠2)) :
    subsum xs z%2=0 ∧ (subsum xs z=0 → z=0 ∧ ∀ a ∈ xs, a.2=false) := by
  induction xs with
  | nil => simp [subsum,hz]
  | cons a xs ih =>
    obtain ⟨e,on⟩ := a
    have ⟨he,hn⟩ := legal (e,on) (by simp)
    obtain ⟨even,zero⟩ := ih (fun b hb => legal b (by simp [hb]))
    have ep : (2:Int)^e % 2=0 := by
      obtain ⟨k,hk⟩ := Nat.exists_eq_add_of_le (show 1≤e from he)
      rw [hk,Int.pow_add,Int.pow_one]; omega
    cases on with
    | false =>
      simp only [subsum,Bool.false_eq_true,if_false,Int.zero_add]
      constructor
      · rw [Int.mul_emod,ep]; simp
      · intro h
        have ⟨h₁,h₂⟩ := zero (by have := (show (0:Int)<2^e from Int.pow_pos (by decide : (0:Int)<2)); exact (Int.mul_eq_zero.mp h).resolve_left (by omega))
        exact ⟨h₁,by simpa using h₂⟩
    | true =>
      simp only [subsum,if_true]
      constructor
      · rw [Int.add_emod,Int.mul_emod,Int.sub_emod,ep,Int.mul_emod ((2:Int)^e),ep]; simp
      · intro h
        exact False.elim (selected_ne he (hn rfl) even h)

private theorem not_one {e x y : Nat} (g : Gap e x y) (hy : 1<y) : 1<x := by
  have ho := g.oddSource
  by_cases hx : x=1
  · rw [hx] at g
    have he := g.eqn
    have hed : 2 ≤ 2^e := by
      simpa using Nat.pow_le_pow_right (by decide : 0<2) (show 1≤e from g.pos)
    have hyo := g.oddTarget
    have hh := Nat.mul_le_mul hed (show 3≤y by omega)
    omega
  · omega

private theorem neutral_size {x q k H : Nat} (p : Path (List.replicate k 2) x q)
    (hq : 1<q) (upper : q≤2^H) : k≤H ∧ 1<x ∧ x≤2^(2*H) := by
  obtain ⟨t,hx,hy⟩ := neutral_parameter p (by omega)
  have ht : 1≤t := by
    by_cases h : t=0
    · simp [h] at hy; omega
    · omega
  have pow₂₃ : 2^k ≤ 3^k := Nat.pow_le_pow_left (by decide) _
  have h₃ : 3^k ≤ 3^k*t := by simpa using Nat.mul_le_mul_left (3^k) ht
  have hk : k≤H := (Nat.pow_le_pow_iff_right (by decide : 1<2)).1 (by omega)
  have positive := Nat.one_le_pow k 4 (by decide)
  have hprod := Nat.mul_le_mul positive ht
  refine ⟨hk,by omega,?_⟩
  have pow₄₆ : 4^k ≤ 2^k*3^k := by
    rw [←Nat.mul_pow]; exact Nat.pow_le_pow_left (by decide) _
  have hu : x ≤ 2^k*q := by
    rw [hx,hy,Nat.mul_add,Nat.mul_one,←Nat.mul_assoc]
    have := Nat.mul_le_mul_right t pow₄₆
    have := Nat.one_le_pow k 2 (by decide)
    omega
  calc
    x ≤ 2^k*q := hu
    _ ≤ 2^H*2^H := Nat.mul_le_mul (Nat.pow_le_pow_right (by decide) hk) upper
    _ = 2^(2*H) := by rw [show 2*H=H+H by omega,Nat.pow_add]

/-- Split into neutral runs separated by single exceptional gaps. The last
three indices count all gaps, exceptional gaps, and their total clock. -/
private inductive Blocks : Nat → Nat → Nat → Nat → Nat → Prop where
  | last {x q k : Nat} (p : Path (List.replicate k 2) x q) : Blocks x q k 0 0
  | more {x y z q k e n d S : Nat} (p : Path (List.replicate k 2) x y)
      (g : Gap e y z) (tail : Blocks z q n d S) :
      Blocks x q (k+1+n) (d+1) (e+S)

private theorem encode {x q : Nat} {es : List Nat} (p : Path es x q) :
    Blocks x q es.length (defects es) (cost es) := by
  induction p with
  | nil => exact .last (.nil _)
  | @cons x y q e es g _ ih =>
    by_cases he : e=2
    · subst e
      simp [defects,cost]
      generalize hn : es.length=n, hd : defects es=d, hc : cost es=S at ih ⊢
      cases ih with
      | @last _ _ k r =>
        exact .last (by rw [List.replicate_succ]; exact .cons g r)
      | @more _ y' z _ k e' n' d' S' r g' tail =>
        have r' : Path (List.replicate (k+1) 2) x y' := by
          rw [List.replicate_succ]; exact .cons g r
        simpa only [Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using Blocks.more r' g' tail
    · simpa [defects,cost,he,Nat.add_comm,Nat.add_left_comm] using
        (Blocks.more (k:=0) (.nil x) g ih)

private theorem Blocks.size {x q n d S : Nat} (p : Blocks x q n d S) (hq : 1<q)
    {H : Nat} (upper : q≤2^H) :
    1<x ∧ x≤2^(2^(d+1)*(H+S)) ∧ n≤2^(d+1)*(H+S)+d := by
  induction p with
  | last r =>
    obtain ⟨hk,hx,hsize⟩ := neutral_size r hq upper
    exact ⟨hx,by simpa using hsize,by simp; omega⟩
  | @more x y z q k e n d S r g tail ih =>
    obtain ⟨hz,hs,hn⟩ := ih hq upper
    let P := 2^(d+1)*(H+S)
    change z ≤ 2^P at hs
    have hy : y≤2^(P+e) := by
      have he := g.eqn
      have := Nat.mul_le_mul_left (2^e) hs
      rw [Nat.pow_add,Nat.mul_comm (2^P)]
      omega
    obtain ⟨hk,hx,hsize⟩ := neutral_size r (not_one g hz) hy
    have hP : 2*(P+e) ≤ 2^(d+1+1)*(H+(e+S)) := by
      have hp := Nat.one_le_pow (d+1) 2 (by decide)
      have he := Nat.mul_le_mul_right e hp
      simp only [Nat.one_mul] at he
      calc
        2*(P+e) ≤ 2*(P+2^(d+1)*e) := by omega
        _ = 2^(d+1+1)*(H+(e+S)) := by
          dsimp [P]
          rw [show H+(e+S)=(H+S)+e by omega,Nat.pow_succ 2 (d+1)]
          simp only [Nat.mul_add]
          ac_rfl
    exact ⟨hx,Nat.le_trans hsize (Nat.pow_le_pow_right (by decide) hP),by change n≤P+d at hn; omega⟩

/-- A long balanced row ending below 2^H requires many gaps of length one. -/
theorem sparse_bound {x q H : Nat} {es : List Nat} (p : Path es x q)
    (hq : 1<q) (upper : q≤2^H) (bal : es.sum = 2*es.length) :
    es.length ≤ 2^(2*ones es+1)*(H+4*ones es)+2*ones es := by
  obtain ⟨hs,hd⟩ := p.balanced bal
  have hn := ((encode p).size hq upper).2.2
  have bound := Nat.mul_le_mul
    (Nat.pow_le_pow_right (by decide : 0<2) (show defects es+1≤2*ones es+1 by omega))
    (show H+cost es≤H+4*ones es by omega)
  omega

private theorem add_cap (e h : Nat) (he : 0<e) (hh : 0<h) :
    3*(2^h-1)+1 ≤ 2^e*(2^(h+(if e=1 then 1 else 0))-1) := by
  have ph := Nat.one_le_pow h 2 (by decide)
  by_cases one : e=1
  · subst e
    simp [Nat.pow_succ]; omega
  · have pe : 4 ≤ 2^e :=
      Nat.pow_le_pow_right (by decide : 0<2) (show 2≤e by omega)
    have ph₂ : 2≤2^h := Nat.pow_le_pow_right (by decide : 0<2) hh
    have hm := Nat.mul_le_mul_right (2^h-1) pe
    simp [one]
    omega

private theorem Path.envelope {es : List Nat} {x q : Nat} (p : Path es x q)
    (h C A : Nat) (hh : 0<h) (initial : C*x ≤ A+C*(2^h-1)) :
    (C*2^es.sum)*q ≤ 3^es.length*A+(C*2^es.sum)*(2^(h+ones es)-1) := by
  induction p generalizing h C A with
  | nil => simpa [ones] using initial
  | @cons x y q e es g tail ih =>
    let u := if e=1 then 1 else 0
    have next : (C*2^e)*y ≤ 3*A+(C*2^e)*(2^(h+u)-1) := by
      calc
        (C*2^e)*y = 3*(C*x)+C := by rw [Nat.mul_assoc,g.eqn,Nat.mul_add,Nat.mul_one]; ac_rfl
        _ ≤ 3*(A+C*(2^h-1))+C := Nat.add_le_add_right (Nat.mul_le_mul_left _ initial) _
        _ = 3*A + C*(3*(2^h-1)+1) := by simp only [Nat.mul_add,Nat.mul_one]; ac_rfl
        _ ≤ 3*A + C*(2^e*(2^(h+u)-1)) :=
          Nat.add_le_add_left (Nat.mul_le_mul_left _ (add_cap e h g.pos hh)) _
        _ = _ := by rw [Nat.mul_assoc C]
    have applyTail := ih (h+u) (C*2^e) (3*A) (by omega) next
    simpa only [List.sum_cons,List.length_cons,Nat.pow_add,Nat.pow_succ,
      ones,u,Nat.add_assoc,Nat.mul_assoc] using applyTail

/-- The hypotheses use only the recorded endpoint, source and gap list.
At relative carry at least 2^(-j), a bounded count of unit gaps gives
an explicit uniform upper bound on the entire balanced row length. -/
theorem sparse_high_carry {es : List Nat} {x q j : Nat} (p : Path es x q)
    (hq : 1<q) (bal : es.sum=2*es.length)
    (high : 2^es.sum*q ≤ 2^j*(2^es.sum*q-3^es.length*x)) :
    es.length ≤ 2^(2*ones es+1)*(j+5*ones es+1)+2*ones es := by
  have env := p.envelope 1 1 x (by decide) (by simp)
  simp only [Nat.one_mul] at env
  have gap : 2^es.sum*q-3^es.length*x ≤ 2^es.sum*(2^(1+ones es)-1) := by omega
  have hi := Nat.le_trans high (Nat.mul_le_mul_left (2^j) gap)
  have loosen := Nat.mul_le_mul_left (2^j*2^es.sum) (Nat.sub_le (2^(1+ones es)) 1)
  rw [←Nat.mul_assoc] at hi
  have hi' := Nat.le_trans hi loosen
  rw [Nat.mul_comm (2^j) (2^es.sum),Nat.mul_assoc,←Nat.pow_add] at hi'
  have height := Nat.le_of_mul_le_mul_left hi' (Nat.two_pow_pos _)
  have bound := sparse_bound p hq height bal
  have he : j+(1+ones es)+4*ones es = j+5*ones es+1 := by omega
  rwa [he] at bound

#print axioms Path.balanced
#print axioms bad_suffix_unit_gaps
#print axioms neutral_parameter
#print axioms neutral_realize
#print axioms Path.shifted_identity
#print axioms subsum_zero
#print axioms sparse_bound
#print axioms sparse_high_carry
end Collatz.Itinerary.Sparse
