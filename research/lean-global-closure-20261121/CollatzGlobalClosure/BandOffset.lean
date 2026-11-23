import CollatzGlobalClosure.EndpointSteering
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Data.Nat.Log

/-! Exact offset descent transfer and an unbounded thin-band clock obstruction.
The map and actual finite prefixes are imported from `CollatzEndpointSteering`.
No global convergence premise is asserted. -/

set_option autoImplicit false
set_option maxHeartbeats 1500000

namespace CollatzBandOffset

open CollatzEndpointSteering

def offset : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, n => 3^(odds k (step n))*(n%2) + 2*offset k (step n)

theorem step_formula (n : Nat) : 2*step n=3^(n%2)*n+n%2 := by
  by_cases he : n%2=0
  · simp [step,he]; omega
  · have ho : n%2=1 := by omega
    simp [step,ho]; omega

theorem affine_formula (k n : Nat) :
    2^k*orbit k n=3^(odds k n)*n+offset k n := by
  induction k generalizing n with
  | zero => simp [orbit,odds,offset]
  | succ k ih =>
    have h := ih (step n)
    have st := step_formula n
    simp only [orbit,odds,offset,pow_add,pow_one]
    nlinarith [congrArg (fun z => 2*z) h,
      congrArg (fun z => 3^(odds k (step n))*z) st]

theorem orbit_add (k a n : Nat) : orbit (k+a) n=orbit a (orbit k n) := by
  induction k generalizing n with
  | zero => simp [orbit]
  | succ k ih => simpa [Nat.succ_add,orbit] using ih (step n)

/-- Strict descent of a positive offset transfers to every larger input sharing
    the entire witnessing binary prefix. -/
theorem lift_descent {k a v : Nat} (ha : 0<a) (drop : orbit k a<a) :
    orbit k (2^k*v+a)<2^k*v+a := by
  have af := affine_formula k a
  have slope : 3^(odds k a)<2^k := by
    have product : 3^(odds k a)*a<2^k*a := by
      have ds := Nat.mul_lt_mul_of_pos_left drop (by positivity : 0<2^k)
      omega
    exact (Nat.mul_lt_mul_right ha).mp product
  rw [orbit_shift]
  have weak := Nat.mul_le_mul_right v slope.le
  omega

/-- A known offset descent before the high bit is consumed gives actual descent
    of the band point, at exactly that same clock. -/
theorem band_descent {d k a : Nat} (ha : 0<a) (kd : k≤d)
    (drop : orbit k a<a) : orbit k (2^d+a)<2^d+a := by
  have e : 2^d=2^k*2^(d-k) := by rw [←pow_add]; congr 1; omega
  rw [e]
  exact lift_descent ha drop

/-- A terminal source certificate supplies the preceding descent guard when
    its clock fits inside the available high-bit padding. -/
theorem band_descent_of_certificate {d k a : Nat} (ha : 1<a) (kd : k≤d)
    (hit : orbit k a=1) : orbit k (2^d+a)<2^d+a :=
  band_descent (by omega) kd (by simpa [hit] using ha)

/-- Failure of descent at every available clock propagates to the smaller
    offset, but only for those clocks. It does not give an infinite survivor. -/
theorem offset_survives {d a : Nat} (ha : 0<a)
    (survive : ∀ k≤d, 2^d+a≤orbit k (2^d+a)) :
    ∀ k≤d, a≤orbit k a := by
  intro k kd
  by_contra! drop
  have bad := band_descent ha kd drop
  have good := survive k kd
  omega

/-- The terminal offset one has a strict two-clock lift descent, even though
    its own orbit is periodic and has no strict descent below one. -/
theorem one_offset_descent {d : Nat} (hd : 2≤d) :
    orbit 2 (2^d+1)<2^d+1 := by
  have p : 0<(2:Nat)^(d-2) := by positivity
  have decomp : 2^d=2^2*2^(d-2) := by rw [←pow_add]; congr 1; omega
  rw [decomp,orbit_shift]
  norm_num [odds,orbit,step]

private theorem positive_pow (b : Nat) : 0<(2:Nat)^b := by positivity

private theorem odd_run (b u : Nat) (hu : 0<u) :
    orbit b (2^b*u-1)+1=3^b*u := by
  induction b generalizing u with
  | zero => simp only [pow_zero,one_mul,orbit]; omega
  | succ b ih =>
    have hp : 0<2^b*u := Nat.mul_pos (positive_pow b) hu
    have repr : 2^(b+1)*u=2*(2^b*u) := by ring
    have par : (2^(b+1)*u-1)%2=1 := by rw [repr]; omega
    have st : step (2^(b+1)*u-1)=2^b*(3*u)-1 := by
      simp only [step,par,show (1:Nat)≠0 by decide,ite_false]
      rw [repr,show 2^b*(3*u)=3*(2^b*u) by ring]
      omega
    rw [orbit,st]
    simpa [pow_succ,Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] using ih (3*u) (by omega)

private theorem prefix_value {b j u : Nat} (ju : j≤b) (hu : 0<u) :
    orbit j (2^b*u-1)+1=3^j*(2^(b-j)*u) := by
  have decomp : 2^b*u=2^j*(2^(b-j)*u) := by rw [←Nat.mul_assoc,←pow_add]; congr 2; omega
  rw [decomp]
  exact odd_run j _ (by positivity)

private theorem prefix_nondecrease {b j u : Nat} (ju : j≤b) (hu : 0<u) :
    2^b*u-1≤orbit j (2^b*u-1) := by
  have val := prefix_value ju hu
  have powers : (2:Nat)^j≤3^j := Nat.pow_le_pow_left (by decide) _
  have prod := Nat.mul_le_mul_right (2^(b-j)*u) powers
  have id : 2^j*(2^(b-j)*u)=2^b*u := by rw [←Nat.mul_assoc,←pow_add]; congr 2; omega
  rw [id] at prod
  omega

private theorem halving_floor (k n : Nat) : n≤2^k*orbit k n := by
  have af := affine_formula k n
  have p : 1≤(3:Nat)^(odds k n) := Nat.one_le_pow _ _ (by decide)
  have mp := Nat.mul_le_mul_right n p
  omega

/-- Once an initial all-odd run provides enough multiplicative surplus, even
    the worst possible all-halving suffix cannot bring the source below itself.
    This is a bound for every actual intermediate clock, not a chosen endpoint. -/
theorem no_descent_through {b h u : Nat} (hu : 0<u)
    (surplus : 2^(b+h)≤3^b) :
    ∀ j≤b+h, 2^b*u-1≤orbit j (2^b*u-1) := by
  intro j bound
  by_cases jb : j≤b
  · exact prefix_nondecrease jb hu
  · have bj : b≤j := by omega
    let s := j-b
    have sh : s≤h := by dsimp [s]; omega
    have js : j=b+s := by dsimp [s]; omega
    have full := odd_run b u hu
    have half := halving_floor s (orbit b (2^b*u-1))
    have small : (2:Nat)^s≤2^h := Nat.pow_le_pow_right (by decide) sh
    have floor : 2^s*(2^b*u)≤3^b*u := by
      calc _ ≤ 2^h*(2^b*u) := Nat.mul_le_mul_right _ small
           _ = 2^(b+h)*u := by rw [←Nat.mul_assoc,←pow_add]; congr 2; omega
           _ ≤ _ := Nat.mul_le_mul_right u surplus
    have p : 0<2^s := by positivity
    have npos : 0<2^b*u := by positivity
    have adj : 2^s*(2^b*u-1)+2^s=2^s*(2^b*u) := by
      calc _ = 2^s*((2^b*u-1)+1) := by ring
           _ = _ := by congr 1; omega
    have endpoint : 2^s*(2^b*u-1)≤2^s*orbit s (orbit b (2^b*u-1)) := by omega
    rw [js,orbit_add]
    exact Nat.le_of_mul_le_mul_left endpoint p

/-- A full infinite family of marked thin-band sources. -/
def thinSeed (m : Nat) : Nat := 2^(5*m)+2^(4*m)-1

def thinOffset (m : Nat) : Nat := 2^(4*m)-1

theorem thinSeed_split (m : Nat) : thinSeed m=2^(5*m)+thinOffset m := by
  unfold thinSeed thinOffset
  exact Nat.add_sub_assoc (Nat.one_le_pow (4*m) 2 (by decide)) (2^(5*m))

theorem thin_surplus (m : Nat) : 2^(4*m+m)≤3^(4*m) := by
  rw [show 4*m+m=5*m by omega,pow_mul,pow_mul]
  exact Nat.pow_le_pow_left (by norm_num) _

/-- The small offset has no strict descent during the entire binary length of
    its associated marked input, uniformly in the parameter. -/
theorem thinOffset_no_descent (m j : Nat) (hj : j≤5*m) :
    thinOffset m≤orbit j (thinOffset m) := by
  simpa [thinOffset] using
    no_descent_through (b:=4*m) (h:=m) (u:=1) (by decide) (thin_surplus m) j (by omega)

/-- The marked source itself has the same all-clock obstruction. -/
theorem thinSeed_no_descent (m j : Nat) (hj : j≤5*m) :
    thinSeed m≤orbit j (thinSeed m) := by
  have repr : thinSeed m=2^(4*m)*(2^m+1)-1 := by
    unfold thinSeed
    rw [Nat.mul_add,Nat.mul_one,←pow_add,show 4*m+m=5*m by omega]
  rw [repr]
  exact no_descent_through (by positivity) (thin_surplus m) j (by omega)


/-- The binary exponent is exact, so the section bound below uses the same
    integer test as PR #173, not a nearby asymptotic band. -/
theorem thinSeed_log2 (m : Nat) : (thinSeed m).log2=5*m := by
  have p : 0<(2:Nat)^(5*m) := by positivity
  have q : 0<(2:Nat)^(4*m) := by positivity
  have le : (2:Nat)^(4*m)≤2^(5*m) := Nat.pow_le_pow_right (by decide) (by omega)
  have lo : 2^(5*m)≤thinSeed m := by unfold thinSeed; omega
  have hi : thinSeed m<2^(5*m+1) := by unfold thinSeed; rw [pow_succ]; omega
  exact (Nat.log2_eq_iff (by omega : thinSeed m≠0)).mpr ⟨lo,hi⟩

/-- Every positive-parameter source lies in the actual odd marked section.
    Its relative offset is smaller than 2^(-m), far narrower than the source
    theorem's inverse-logarithmic band. -/
theorem thinSeed_marked (m : Nat) (hm : 0<m) :
    thinSeed m%2=1 ∧
    ((thinSeed m).log2+1)*(thinSeed m-2^(thinSeed m).log2)≤70*2^(thinSeed m).log2 := by
  have p : 2≤(2:Nat)^(4*m) := by
    simpa using Nat.pow_le_pow_right (by decide : 0<(2:Nat)) (show 1≤4*m by omega)
  have positive5 : 0<(2:Nat)^(5*m) := by positivity
  have p5 : ((2:Nat)^(5*m))%2=0 := by
    rw [Nat.pow_mod]; simp [show 5*m≠0 by omega]
  have p4 : ((2:Nat)^(4*m))%2=0 := by
    rw [Nat.pow_mod]; simp [show 4*m≠0 by omega]
  constructor
  · unfold thinSeed
    omega
  · rw [thinSeed_log2]
    have sub : thinSeed m-2^(5*m)=2^(4*m)-1 := by unfold thinSeed; omega
    rw [sub]
    have linear : 5*m+1≤70*2^m := by have := Nat.lt_two_pow_self (n:=m); omega
    calc (5*m+1)*(2^(4*m)-1) ≤ (5*m+1)*2^(4*m) := Nat.mul_le_mul_left _ (by omega)
         _ ≤ (70*2^m)*2^(4*m) := Nat.mul_le_mul_right _ linear
         _ = 70*2^(5*m) := by rw [Nat.mul_assoc,←pow_add]; congr 2; omega

/-- Exact relative thinness, without logarithms or real rounding. -/
theorem thinSeed_width (m : Nat) :
    2^m*(thinSeed m-2^(thinSeed m).log2)<2^(thinSeed m).log2 := by
  rw [thinSeed_log2,thinSeed_split]
  have p : 0<(2:Nat)^(4*m) := by positivity
  have s : (2:Nat)^(4*m)-1<2^(4*m) := by omega
  simpa [thinOffset,←pow_add,show m+4*m=5*m by omega] using
    Nat.mul_lt_mul_of_pos_left s (by positivity : 0<(2:Nat)^m)

end CollatzBandOffset

#print axioms CollatzBandOffset.lift_descent
#print axioms CollatzBandOffset.band_descent
#print axioms CollatzBandOffset.band_descent_of_certificate
#print axioms CollatzBandOffset.no_descent_through
#print axioms CollatzBandOffset.thinOffset_no_descent
#print axioms CollatzBandOffset.thinSeed_no_descent

#print axioms CollatzBandOffset.thinSeed_log2
#print axioms CollatzBandOffset.thinSeed_marked
#print axioms CollatzBandOffset.thinSeed_width

#print axioms CollatzBandOffset.offset_survives
#print axioms CollatzBandOffset.one_offset_descent
