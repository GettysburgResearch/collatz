module

public import FiberTransport
import all FiberTransport
import all TernaryItinerary
import all TowerFrontierAffine

public section
namespace Collatz.Itinerary.UniformTowerRouting

open FiberTransport TowerFrontier
set_option autoImplicit false

/-- A common affine endpoint on a single binary progression gives one
ordinary clock for all ternary-unit targets, and every later clock works.
Both the maximum clock and the chosen progression precede the target. -/
theorem uniform_from_cylinder (multipliers : Nat → Nat) (R H W a k : Nat)
    (pos : 0<W) (unit : a%3≠0)
    (row : ∀ t r, r≤R → run H (multipliers r*(W+2^H*t))=a+3^k*t) :
    ∃ D, ∀ S, D≤S → ∀ b, b%3≠0 → ∃ x, 0<x ∧
      ∀ r≤R, run S (multipliers r*x)=b := by
  have bounded (N : Nat) : ∃ D, ∀ z<N, z%3≠0 →
      ∃ e≤D, ∃ v, 2^e*z=a+3^(k+1)*v := by
    induction N with
    | zero => exact ⟨0,by omega⟩
    | succ N ih =>
      obtain ⟨D,old⟩ := ih
      by_cases uz : N%3=0
      · refine ⟨D,?_⟩
        intro z small nz
        exact old z (by omega) nz
      · obtain ⟨e,v,_,eq⟩ := large_dyadic_lift k N a 0 uz unit
        refine ⟨D+e,?_⟩
        intro z small nz
        by_cases endpt : z=N
        · subst z; exact ⟨e,by omega,v,eq⟩
        · obtain ⟨j,le,t,hit⟩ := old z (by omega) nz
          exact ⟨j,by omega,t,hit⟩
  let M := 3^(k+1)
  obtain ⟨D,find⟩ := bounded M
  refine ⟨H+D,?_⟩
  intro S late b ub
  have modpos : 0<M := Nat.pow_pos (by decide)
  have three : 3∣M := ⟨3^k,by simp only [M,Nat.pow_succ]; ac_rfl⟩
  have rb : b%M%3≠0 := by rwa [Nat.mod_mod_of_dvd _ three]
  obtain ⟨e,le,v,eq⟩ := find (b%M) (Nat.mod_lt b modpos) rb
  let t := 3*(v+2^e*(b/M))
  have scale : 2^e*b=a+3^k*t := by
    calc
      2^e*b = 2^e*(b%M+M*(b/M)) := congrArg (2^e*·) (Nat.mod_add_div b M).symm
      _ = a+3^k*t := by rw [Nat.mul_add,eq]; simp only [M,t,Nat.pow_succ]; grind
  let p := S-(H+e)
  let z := W+2^H*t
  refine ⟨2^p*z,Nat.mul_pos (Nat.two_pow_pos _) (by dsimp [z]; omega),?_⟩
  intro r hr
  rw [show S=p+(H+e) by dsimp [p]; omega,
    show multipliers r*(2^p*z)=2^p*(multipliers r*z) by ac_rfl,
    run_add,halve,run_add,row t r hr,←scale,halve]

private theorem run_upper (h n : Nat) : run h n≤2^h*n := by
  induction h generalizing n with
  | zero => simp [run]
  | succ h ih =>
    have single : step n≤2*n := by unfold step; split <;> omega
    calc
      run (h+1) n ≤ 2^h*step n := ih _
      _ ≤ 2^h*(2*n) := Nat.mul_le_mul_left _ single
      _ = 2^(h+1)*n := by rw [Nat.pow_succ]; ac_rfl

private theorem same_slope {a b p q t : Nat} (ha : a<t) (hb : b<t)
    (eq : a+p*t=b+q*t) : p=q := by
  by_cases lt : p<q
  · have le := Nat.mul_le_mul_right t (Nat.succ_le_of_lt lt)
    rw [Nat.succ_mul] at le
    omega
  by_cases gt : q<p
  · have le := Nat.mul_le_mul_right t (Nat.succ_le_of_lt gt)
    rw [Nat.succ_mul] at le
    omega
  omega

/-- An explicit barrier for every multiplier outside the powers of three at
one fixed common clock. A single sufficiently high meeting forces the form. -/
theorem large_meeting_requires_power {h m x : Nat} (pm : 0<m)
    (large : (m+1)*2^h*2^h<x/2^h) (hit : run h x=run h (m*x)) :
    ∃ j, m=3^j := by
  let d := 2^h
  let r := x%d
  let t := x/d
  let p := (track h r 0).2
  let q := (track h (m*r) 0).2
  have split : r+d*t=x := Nat.mod_add_div x d
  have ar : run h x=run h r+3^p*t := by
    have rule := affine h r 0 t
    rw [←split]
    simpa only [p,d,Nat.pow_zero,Nat.mul_one,track_value] using rule
  have br : run h (m*x)=run h (m*r)+3^q*(m*t) := by
    have repr : m*x=m*r+d*(m*t) := by
      conv => lhs; rw [←split]
      rw [Nat.mul_add,Nat.mul_left_comm m d]
    rw [repr]
    simpa only [q,d,Nat.pow_zero,Nat.mul_one,track_value] using affine h (m*r) 0 (m*t)
  have small : r≤d := Nat.le_of_lt (Nat.mod_lt _ (Nat.two_pow_pos h))
  have cap : d*r≤d*d := Nat.mul_le_mul_left d small
  have cap' : m*(d*r)≤m*(d*d) := Nat.mul_le_mul_left m cap
  have max : m*(d*d)+d*d<t := by
    simpa only [t,d,Nat.add_mul,Nat.one_mul,Nat.mul_assoc] using large
  have ha := run_upper h r
  have hb := run_upper h (m*r)
  change run h r≤d*r at ha
  change run h (m*r)≤d*(m*r) at hb
  rw [Nat.mul_left_comm d m] at hb
  rw [ar,br,←Nat.mul_assoc] at hit
  have slopes : 3^p=3^q*m := same_slope (by omega) (by omega) hit
  have mono : q≤p := by
    apply Classical.byContradiction
    intro wrong
    have strict := Nat.pow_lt_pow_right (by decide : 1<3) (show p<q by omega)
    have lower := Nat.le_mul_of_pos_right (3^q) pm
    omega
  refine ⟨p-q,Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide : 0<3) (n:=q)) ?_⟩
  rw [←slopes,←Nat.pow_add,show q+(p-q)=p by omega]

/-- Bounded simultaneous coverage of all ordinary unit targets with an
anchoring arm x forces every other multiplier to be a pure power of three. -/
theorem universal_multiplier_requires_power {h m : Nat} (pm : 0<m)
    (all : ∀ b, b%3≠0 → ∃ x, run h x=b ∧ run h (m*x)=b) :
    ∃ j, m=3^j := by
  let d := 2^h
  let B := (m+1)*d*d
  let L := d*(B+1)
  let b := 3*(d*L)+1
  obtain ⟨x,a,c⟩ := all b (by dsimp [b]; omega)
  have le := run_upper h x
  rw [a] at le
  have big : L<x := by
    apply Classical.byContradiction
    intro no
    have bound := Nat.mul_le_mul_left d (show x≤L by omega)
    change b≤d*x at le
    dsimp [b] at le
    omega
  apply large_meeting_requires_power pm _ (a.trans c.symm)
  change B<x/d
  have quotient : B+1≤x/d := (Nat.le_div_iff_mul_le (Nat.two_pow_pos h)).mpr
    (by change (B+1)*d≤x; rw [Nat.mul_comm]; exact Nat.le_of_lt big)
  omega

#print axioms uniform_from_cylinder
#print axioms large_meeting_requires_power
#print axioms universal_multiplier_requires_power
end Collatz.Itinerary.UniformTowerRouting
