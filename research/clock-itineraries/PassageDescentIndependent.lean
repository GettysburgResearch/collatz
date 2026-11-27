module

public import PassageDescentFirst
import all TernaryItinerary
import all ReturnDescent
import all TowerFrontierAffine

public section

namespace Collatz.Itinerary.PassageDescent

open ReturnDescent TowerFrontier
set_option autoImplicit false
set_option maxHeartbeats 4000000

private theorem grade_inc (h n e : Nat) :
    track h n (e+1)=((track h n e).1,(track h n e).2+1) := by
  induction h generalizing n e with
  | zero => rfl
  | succ h ih => simp only [track]; split <;> apply ih

private theorem grade_cap (h n e : Nat) : (track h n e).2≤h+e := by
  induction h generalizing n e with
  | zero => simp [track]
  | succ h ih =>
    simp only [track]
    split
    · have := ih (n/2) e
      omega
    · have := ih ((3*n+1)/2) (e+1)
      omega

private theorem affine_word (h n : Nat) :
    ∃ A, 2^h*run h n=3^(track h n 0).2*n+A ∧ A+2^h≤3^h ∧
      A+2^h≤2^(h-(track h n 0).2)*3^(track h n 0).2 := by
  induction h generalizing n with
  | zero => exact ⟨0,by simp [run,track]⟩
  | succ h ih =>
    by_cases even : n%2=0
    · let x := n/2
      obtain ⟨A,eq,bound,weighted⟩ := ih x
      refine ⟨2*A,?_,?_,?_⟩
      · have nval : 2*x=n := by dsimp only [x]; omega
        simp only [run,step,track,even,↓reduceIte,Nat.pow_succ]
        change 2^h*2*run h x=3^(track h x 0).2*n+2*A
        have mult := congrArg (fun v => 2*v) eq
        have move := congrArg (fun v => 3^(track h x 0).2*v) nval
        grind
      · rw [Nat.pow_succ,Nat.pow_succ]
        omega
      · let p := (track h x 0).2
        have cap : p≤h := by simpa only [Nat.add_zero] using grade_cap h x 0
        simp only [track,even,↓reduceIte]
        change 2*A+2^(h+1)≤2^(h+1-p)*3^p
        rw [show h+1-p=h-p+1 by omega,Nat.pow_succ,Nat.pow_succ]
        change A+2^h≤2^(h-p)*3^p at weighted
        grind
    · let x := (3*n+1)/2
      obtain ⟨A,eq,bound,weighted⟩ := ih x
      let p := (track h x 0).2
      have cap : p≤h := by simpa only [Nat.add_zero] using grade_cap h x 0
      have inc : track h x 1=((track h x 0).1,p+1) := grade_inc h x 0
      refine ⟨3^p+2*A,?_,?_,?_⟩
      · have nval : 2*x=3*n+1 := by dsimp only [x]; omega
        simp only [run,step,track,even,↓reduceIte,Nat.pow_succ 2 h]
        change 2^h*2*run h x=3^(track h x 1).2*n+(3^p+2*A)
        rw [inc,Nat.pow_succ]
        change 2^h*2*run h x=3^p*3*n+(3^p+2*A)
        change 2^h*run h x=3^p*x+A at eq
        have mult := congrArg (fun v => 2*v) eq
        have move := congrArg (fun v => 3^p*v) nval
        grind
      · have q := Nat.pow_le_pow_right (by decide : 0<3) cap
        rw [Nat.pow_succ,Nat.pow_succ]
        omega

      · simp only [track,even,↓reduceIte]
        change 3^p+2*A+2^(h+1)≤2^(h+1-(track h x 1).2)*3^(track h x 1).2
        rw [inc]
        change 3^p+2*A+2^(h+1)≤2^(h+1-(p+1))*3^(p+1)
        rw [show h+1-(p+1)=h-p by omega,Nat.pow_succ,Nat.pow_succ]
        change A+2^h≤2^(h-p)*3^p at weighted
        have big := Nat.mul_le_mul_right (3^p) (Nat.two_pow_pos (h-p))
        grind

private theorem same_twos {a b u v : Nat} (oddU : u%2=1) (oddV : v%2=1)
    (eq : 2^a*u=2^b*v) : a=b := by
  induction a generalizing b with
  | zero =>
    cases b with
    | zero => rfl
    | succ b =>
      rw [Nat.pow_zero,Nat.one_mul,Nat.pow_succ] at eq
      have repr : 2^b*2*v=2*(2^b*v) := by ac_rfl
      rw [repr] at eq
      omega
  | succ a ih =>
    cases b with
    | zero =>
      rw [Nat.pow_zero,Nat.one_mul,Nat.pow_succ] at eq
      have repr : 2^a*2*u=2*(2^a*u) := by ac_rfl
      rw [repr] at eq
      omega
    | succ b =>
      rw [Nat.pow_succ,Nat.pow_succ] at eq
      have cut : 2^a*u=2^b*v := by
        rw [show 2^a*2*u=2*(2^a*u) by ac_rfl,show 2^b*2*v=2*(2^b*v) by ac_rfl] at eq
        omega
      exact congrArg Nat.succ (ih cut)

private theorem three_odd (n : Nat) : 3^n%2=1 := by rw [Nat.pow_mod]; simp

/-- The carry budget of two ordinary words leading to the paired native cuts.
    The exponents count their true even and odd departures. -/
@[expose] def pairCost (l p u r : Nat) :=
  max (2^(u-r)*3^(p+r)) (2^(l-p)*3^(p+r+1))

/-- A small two-word budget forces both the native lag and the native grade
    relation. No price, canonical residue, or restriction on the original
    Mersenne exponent enters this synchronization theorem. -/
theorem synchronize_or_cost {m l u y r : Nat} (ml : 2≤m) (umin : 2≤u)
    (lower : run l y=M m) (upper : track u (3*y) 0=(2^(m-2),r)) :
    let p := (track l y 0).2
    (l+2=u ∧ p=r+1) ∨ 2^m≤pairCost l p u r := by
  intro p0
  by_cases costly : 2^m≤pairCost l p0 u r
  · exact Or.inr costly
  left
  have earth : max (2^(u-r)*3^(p0+r)) (2^(l-p0)*3^(p0+r+1))<2^m :=
    Nat.lt_of_not_ge costly
  let w := u-2
  have wu : w+2=u := by dsimp only [w]; omega
  let p := (track l y 0).2
  let D := 3^(r+1)
  obtain ⟨A,a,_,ac⟩ := affine_word l y
  obtain ⟨B,b,_,bc⟩ := affine_word u (3*y)
  change 2^l*run l y=3^p*y+A at a
  rw [lower] at a
  have uv : run u (3*y)=2^(m-2) := by rw [←track_run u (3*y) 0,upper]
  rw [uv,upper] at b
  change 2^u*2^(m-2)=3^r*(3*y)+B at b
  have power : 2^u*2^(m-2)=2^m*2^w := by
    rw [←Nat.pow_add,←Nat.pow_add]
    congr 1
    omega
  rw [power,show 3^r*(3*y)=D*y by dsimp only [D]; rw [Nat.pow_succ]; ac_rfl] at b
  have eqL : 2^l*2^m=3^p*y+A+2^l := by
    unfold M at a
    have nz := Nat.two_pow_pos m
    have decomp : 2^m=(2^m-1)+1 := by omega
    calc
      2^l*2^m=2^l*((2^m-1)+1) := congrArg (fun v => 2^l*v) decomp
      _ = _ := by rw [Nat.mul_add,a,Nat.mul_one]
  have balance : 3^p*B+(2^l*D)*2^m=D*(A+2^l)+(2^w*3^p)*2^m := by
    have l1 := congrArg (fun v => D*v) eqL
    have u1 := congrArg (fun v => 3^p*v) b
    grind
  change A+2^l≤2^(l-p)*3^p at ac
  rw [upper] at bc
  change B+2^u≤2^(u-r)*3^r at bc
  have bsmall : 3^p*B<2^m := by
    have inz := Nat.two_pow_pos u
    have lim : B<2^(u-r)*3^r := by omega
    have v0 := Nat.mul_lt_mul_of_pos_left lim (Nat.pow_pos (by decide : 0<3) (n:=p))
    have product : 3^p*(2^(u-r)*3^r)=2^(u-r)*3^(p+r) := by rw [Nat.pow_add]; ac_rfl
    rw [product] at v0
    exact Nat.lt_trans v0 (Nat.lt_of_le_of_lt (Nat.le_max_left _ _) earth)
  have asmall : D*(A+2^l)<2^m := by
    have v0 := Nat.mul_le_mul_left D ac
    have product : D*(2^(l-p)*3^p)=2^(l-p)*3^(p+r+1) := by
      dsimp only [D]
      rw [show p+r+1=p+(r+1) by omega,Nat.pow_add 3 p]
      ac_rfl
    rw [product] at v0
    exact Nat.lt_of_le_of_lt v0 (Nat.lt_of_le_of_lt (Nat.le_max_right _ _) earth)
  have offsets : 3^p*B=D*(A+2^l) := by
    have ne := congrArg (fun n => n%2^m) balance
    simpa only [Nat.add_mul_mod_self_right,Nat.mod_eq_of_lt bsmall,Nat.mod_eq_of_lt asmall] using ne
  rw [offsets] at balance
  have coeff : 2^l*D=2^w*3^p :=
    Nat.eq_of_mul_eq_mul_right (Nat.two_pow_pos m) (Nat.add_left_cancel balance)
  have limb : l=w := same_twos (three_odd _) (three_odd _) coeff
  have gp : D=3^p := by
    rw [limb] at coeff
    exact Nat.eq_of_mul_eq_mul_left (Nat.two_pow_pos w) coeff
  have grade : p=r+1 := by
    by_cases below : p<r+1
    · have v := Nat.pow_lt_pow_right (by decide : 1<3) below
      change 3^(r+1)=3^p at gp
      omega
    by_cases above : r+1<p
    · have v := Nat.pow_lt_pow_right (by decide : 1<3) above
      change 3^(r+1)=3^p at gp
      omega
    omega
  exact ⟨by omega,grade⟩

/-- At low upper grade, independent clocks can avoid the synchronous
    obstruction only after a linearly long lower prefix at the fixed parent. -/
theorem independent_clock_floor {j l u y r : Nat} (positive : 0<j)
    (cls : y%48=17) (small : y<hardParent (11+162*j)) (rank : r≤10)
    (lower : run l y=M (11+162*j))
    (upper : track u (3*y) 0=(2^(11+162*j-2),r)) :
    u≤20 ∧ 2^(11+162*j)<3^(l+20) := by
  let m := 11+162*j
  change y<hardParent m at small
  change run l y=M m at lower
  change track u (3*y) 0=(2^(m-2),r) at upper
  have ml : 173≤m := by dsimp only [m]; omega
  have twice : 2^(m-2)=2*2^(m-3) := by
    rw [show m-2=(m-3)+1 by omega,Nat.pow_succ,Nat.mul_comm]
  have umin : 2≤u := by
    by_cases ok : 2≤u
    · exact ok
    rcases (show u=0 ∨ u=1 by omega) with e|e <;> subst u
    · change (3*y,0)=(2^(m-2),r) at upper
      have := congrArg Prod.fst upper
      simp only at this
      omega
    · have b : (3*y)%2≠0 := by omega
      simp only [track,b,↓reduceIte] at upper
      have := congrArg Prod.fst upper
      simp only at this
      omega
  let w := u-2
  have wu : w+2=u := by dsimp only [w]; omega
  have ub := upper_cut_clock_bound (h:=w) ml small rank (by simpa only [wu] using upper)
  have u20 : u≤20 := by omega
  let p := (track l y 0).2
  have pc : p≤l := by simpa only [Nat.add_zero] using grade_cap l y 0
  have rc : r≤u := by
    have v := grade_cap u (3*y) 0
    rw [upper] at v
    simpa only [Nat.add_zero] using v
  rcases synchronize_or_cost (l:=l) (u:=u) (y:=y) (by omega : 2≤m) umin lower upper with sync|cost
  · have native : track (l+2) (3*y) 0=(2^(m-2),r) := by rw [sync.1,upper]
    have impossible := eleven_required positive cls small lower native
    omega
  · change 2^m≤pairCost l p u r at cost
    have mono (a : Nat) : 2^a≤3^a := Nat.pow_le_pow_left (by decide) a
    have one : 2^(u-r)*3^(p+r)≤3^(l+20) := by
      have b := Nat.mul_le_mul_right (3^(p+r)) (mono (u-r))
      rw [←Nat.pow_add] at b
      exact Nat.le_trans b (Nat.pow_le_pow_right (by decide) (by omega))
    have two : 2^(l-p)*3^(p+r+1)≤3^(l+20) := by
      have b := Nat.mul_le_mul_right (3^(p+r+1)) (mono (l-p))
      rw [←Nat.pow_add] at b
      exact Nat.le_trans b (Nat.pow_le_pow_right (by decide) (by omega))
    have cap : 2^m≤3^(l+20) := Nat.le_trans cost (Nat.max_le.mpr ⟨one,two⟩)
    have unequal : 2^m≠3^(l+20) := by
      intro equality
      have even : 2^m=2*2^(m-1) := by
        rw [show m=(m-1)+1 by omega,Nat.pow_succ]; grind
      have odd := three_odd (l+20)
      omega
    exact ⟨u20,Nat.lt_of_le_of_ne cap unequal⟩

#print axioms synchronize_or_cost
#print axioms independent_clock_floor

end Collatz.Itinerary.PassageDescent
