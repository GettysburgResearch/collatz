module

public import PassageDescentRank
import all PassageDescentDelayed
import all ReturnDescent
import all TernaryItinerary

public section

namespace Collatz.Itinerary.PassageDescent

open TowerFrontier ReturnDescent
set_option autoImplicit false
set_option maxHeartbeats 2000000
set_option exponentiation.threshold 1000000

@[expose] def First (h x q : Nat) : Prop := run h x=q ∧ ∀ i, i<h → run i x≠q

private theorem bounded_cycle (t : Nat) (x : Nat) (small : x=1 ∨ x=2) : run t x≤2 := by
  induction t generalizing x with
  | zero => simpa only [run] using (show x≤2 by omega)
  | succ t ih =>
    rw [run]
    apply ih
    rcases small with rfl|rfl <;> decide

private theorem halves (a b : Nat) : run a (2^(a+b))=2^b := by
  induction a with
  | zero => simp [run]
  | succ a ih =>
    rw [Nat.succ_add,Nat.pow_succ,run]
    have stepEq (u : Nat) : step (u*2)=u := by simp [step]
    rw [stepEq,ih]

private theorem first_of_no_return {x q h : Nat} (hit : run h x=q)
    (safe : ∀ d, 0<d → d≤h → run d q≠q) : First h x q := by
  refine ⟨hit,?_⟩
  intro i lt found
  have again := safe (h-i) (by omega) (by omega)
  apply again
  rw [←found,←run_add,show i+(h-i)=h by omega,hit,found]

private theorem mersenne_first {h x m : Nat} (hit : run h x=M m) (bound : h≤m) :
    First h x (M m) := by
  apply first_of_no_return hit
  intro d pos le
  have e : d+(m-d)=m := by omega
  have a : 0<2^(m-d) := Nat.two_pow_pos _
  have lift : run d (2^d*2^(m-d)-1)=3^d*2^(m-d)-1 := by
    simpa only [Nat.zero_add,Nat.pow_zero,Nat.one_mul,run] using
      BasinTransport.affine_rays d 0 0 (2^(m-d)) a
  have gt := Nat.mul_lt_mul_of_pos_right
    (Nat.pow_lt_pow_left (by decide : 2<3) (show d≠0 by omega)) a
  have npos : 0<2^d*2^(m-d) := Nat.mul_pos (Nat.two_pow_pos _) a
  unfold M
  rw [←e,Nat.pow_add,lift]
  omega

private theorem power_first {h x v : Nat} (hit : run h x=2^v) (bound : h≤v) :
    First h x (2^v) := by
  apply first_of_no_return hit
  intro d pos le
  have part := halves d (v-d)
  rw [show d+(v-d)=v by omega] at part
  rw [part]
  exact Nat.ne_of_lt (Nat.pow_lt_pow_right (by decide : 1<2) (by omega))

private theorem first_one {h x v : Nat} (hit : run h x=2^v) (vbig : 2≤v) :
    First (h+v) x 1 := by
  refine ⟨?_,?_⟩
  · rw [run_add,hit]
    simpa using halves v 0
  · intro i lt one
    by_cases before : i<h
    · have span : i+(h-i)=h := by omega
      have atH : run h x=run (h-i) 1 := by rw [←span,run_add,one,span]
      have two := bounded_cycle (h-i) 1 (Or.inl rfl)
      have vpos := Nat.pow_le_pow_right (by decide : 0<2) vbig
      omega
    · let d := i-h
      have s0 : h+d=i := by dsimp only [d]; omega
      have s1 : d+(v-d)=v := by dsimp only [d]; omega
      have power := halves d (v-d)
      rw [s1] at power
      rw [←s0,run_add,hit,power] at one
      have more : 2^1≤2^(v-d) := Nat.pow_le_pow_right (by decide) (by omega)
      omega

private theorem chart_bounds : ∀ i : Fin 33, 0<delayedCharts[i.val]!.row.residue ∧
    delayedCharts[i.val]!.row.lower≤32 := by decide +kernel

/-- Both prepeak contacts are first visits on both canonical sources. The
    displayed terminal upper clocks are first hits of one as well. -/
theorem delayed_first_hits (i : Fin 33) (s : Nat) :
    let a := delayedCharts[i.val]!
    let r := a.row
    let k := r.residue+r.period*s
    let m := delayedExponent k
    let z := hardParent m
    ∃ Y, Y%48=17 ∧ a.gain*Y<z ∧ Y<z ∧
      First r.lower Y (M m) ∧ First 7 z (M m) ∧
      First (r.lower+2) (3*Y) (2^(m-2)) ∧ First 9 (3*z) (2^(m-2)) ∧
      First (m+r.lower) (3*Y) 1 ∧ First (m+7) (3*z) 1 := by
  intro a r k m z
  obtain ⟨Y,cls,sm,gain,_,L,Z,U,V,_⟩ := delayed_two_arm i s
  obtain ⟨k0,lim⟩ := chart_bounds i
  change 0<r.residue at k0
  change r.lower≤32 at lim
  have kp : 1≤k := by dsimp only [k]; omega
  have up : 2^18≤2^(18*k) := Nat.pow_le_pow_right (by decide) (by omega)
  have bound : 100≤m := by dsimp only [m,delayedExponent]; omega
  have lo : run r.lower Y=M m := by rw [←track_run r.lower Y 0,L]
  have upper : run (r.lower+2) (3*Y)=2^(m-2) := by rw [←track_run (r.lower+2) (3*Y) 0,U]
  have orig : run 9 (3*z)=2^(m-2) := by rw [←track_run 9 (3*z) 0,V]
  have a1 := first_one upper (by omega)
  have b1 := first_one orig (by omega)
  rw [show r.lower+2+(m-2)=m+r.lower by omega] at a1
  rw [show 9+(m-2)=m+7 by omega] at b1
  exact ⟨Y,cls,gain,sm,mersenne_first lo (by omega),mersenne_first Z (by omega),
    power_first upper (by omega),power_first orig (by omega),a1,b1⟩

private def avoiding : Nat → Nat → Bool
  | 0,x => x==1
  | h+1,x => x==1 || (x != 2047 && avoiding h (step x))

private theorem avoiding_sound {h x : Nat} (test : avoiding h x=true) (t : Nat) :
    run t x≠2047 := by
  induction h generalizing x t with
  | zero =>
    have eq : x=1 := by simpa [avoiding] using test
    have bound := bounded_cycle t x (Or.inl eq)
    omega
  | succ h ih =>
    by_cases eq : x=1
    · have bound := bounded_cycle t x (Or.inl eq)
      omega
    · obtain ⟨avoid,next⟩ := Bool.and_eq_true_iff.mp
        (show (x != 2047 && avoiding h (step x))=true by simpa [avoiding,eq] using test)
      cases t with
      | zero => simpa [run] using avoid
      | succ t => exact ih next t

private theorem small_row : ∀ i : Fin 67, avoiding 100 (48*i.val+17)=true := by decide +kernel

/-- The rank lower bound includes the initial actual parent at m=11. -/
theorem eleven_required_all {j h y r : Nat} (cls : y%48=17)
    (small : y<hardParent (11+162*j)) (lower : run h y=M (11+162*j))
    (upper : track (h+2) (3*y) 0=(2^(11+162*j-2),r)) : 11≤r := by
  by_cases p : 0<j
  · exact eleven_required p cls small lower upper
  · have zero : j=0 := by omega
    subst j
    change y<3233 at small
    change run h y=2047 at lower
    have repr := Nat.mod_add_div y 48
    rw [cls] at repr
    have row := small_row ⟨y/48,by omega⟩
    have arg : 48*(y/48)+17=y := by omega
    change avoiding 100 (48*(y/48)+17)=true at row
    rw [arg] at row
    exact False.elim ((avoiding_sound row h) lower)

/-- A supplied infinite delayed progression attains rank eleven with a
    smaller canonical source of less than one third the original height. -/
theorem eleven_attained (s : Nat) :
    let m := delayedExponent (3130+6561*s)
    ∃ Y, Y%48=17 ∧ 3*Y<hardParent m ∧
      track 18 Y 0=(M m,12) ∧ track 20 (3*Y) 0=(2^(m-2),11) := by
  intro m
  obtain ⟨Y,cls,_,gain,_,L,_,U,_⟩ := delayed_two_arm ⟨0,by decide⟩ s
  exact ⟨Y,cls,gain,L,U⟩

#print axioms delayed_first_hits
#print axioms eleven_required_all
#print axioms eleven_attained

end Collatz.Itinerary.PassageDescent
