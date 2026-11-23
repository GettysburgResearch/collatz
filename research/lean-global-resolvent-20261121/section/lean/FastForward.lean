import BandSteering
import Integer306
import Batteries.Tactic.OpenPrivate

/-! Supplied rational grids force uniformly short actual band visits.
No Diophantine lower bound is assumed by the finite theorem.
-/
namespace CollatzShell.ForwardSection.Fast

open Real
open private part_pos part_odd split_twos orbit_pos orbit_odd size_orbit
  phase_orbit grid_point clock clock_exact clock_weight from ForwardSection

set_option maxHeartbeats 1000000
set_option exponentiation.threshold 200000

/-- A supplied rational approximation, with denominator at least the input
binary height, gives a drop below q^2 or a visit to the original marked band. -/
theorem grid_drop_or_mark (n a q : Nat) (hn : n%2=1) (qp : 0<q)
    (cap : n.log2≤q) (cop : a.Coprime q)
    (approx : |(q:ℝ)*alpha-a|≤1/(q:ℝ)) :
    ∃ j<q, oddOrbit n j<q*q ∨ Marked (oddOrbit n j) := by
  have np : 0<n := by omega
  have qr : (0:ℝ)<q := by exact_mod_cast qp
  by_cases floor : ∀ i<q, q*q≤oddOrbit n i
  · obtain ⟨j,jq,z,gl,gu⟩ := grid_point qp cop (height n)
    obtain ⟨A,e,el,eu,eq⟩ := phase_orbit np (Nat.mul_pos qp qp) j
      (fun i hi => floor i (hi.trans jq))
    have jr : (0:ℝ)≤j := by positivity
    have jqr : (j:ℝ)≤q := by exact_mod_cast jq.le
    have qe : (q:ℝ)*e≤1 := by
      have cost := mul_le_mul_of_nonneg_left eu qr.le
      push_cast at cost
      have bound : (q:ℝ)*((j:ℝ)/((q:ℝ)*q))≤1 := by
        rw [← mul_div_assoc]
        apply (div_le_one (mul_pos qr qr)).mpr
        nlinarith
      exact cost.trans bound
    have perturb : |(j:ℝ)*((q:ℝ)*alpha-a)|≤1 := by
      rw [abs_mul,abs_of_nonneg jr]
      calc _ ≤ j*(1/(q:ℝ)) := mul_le_mul_of_nonneg_left approx jr
           _ ≤ 1 := by rw [mul_one_div]; exact (div_le_one qr).mpr jqr
    have algebra : (q:ℝ)*(height (oddOrbit n j)-((z-(A:ℤ):ℤ):ℝ)) =
        q*(height n+j*((a:ℝ)/q)-z)+j*(q*alpha-a)+q*e := by
      rw [eq]; push_cast; field_simp; ring
    have lo : 0≤height (oddOrbit n j)-((z-(A:ℤ):ℤ):ℝ) := by
      apply nonneg_of_mul_nonneg_right (a := (q:ℝ)) _ qr
      rw [algebra]
      linarith [(abs_le.mp perturb).1,mul_nonneg qr.le el]
    have hi : (q:ℝ)*(height (oddOrbit n j)-((z-(A:ℤ):ℤ):ℝ))≤4 := by
      rw [algebra]; linarith [(abs_le.mp perturb).2]
    have nbound : n<2^(q+1) := Nat.lt_log2_self.trans_le
      (Nat.pow_le_pow_right (by decide) (by omega))
    have xbound : oddOrbit n j<2^(2*q) := by
      calc _ ≤ 2^j*n := size_orbit hn j
           _ < 2^j*2^(q+1) := Nat.mul_lt_mul_of_pos_left nbound (by positivity)
           _ ≤ 2^(2*q) := by
             rw [← pow_add]
             exact Nat.pow_le_pow_right (by decide) (by omega)
    have dl := (Nat.log2_lt (orbit_pos np j).ne').mpr xbound
    have du : ((oddOrbit n j).log2:ℝ)+1≤2*q := by
      exact_mod_cast (show (oddOrbit n j).log2+1≤2*q by omega)
    have close : (((oddOrbit n j).log2:ℝ)+1)*
        (height (oddOrbit n j)-((z-(A:ℤ):ℤ):ℝ))≤35 := by
      calc _ ≤ (2*q)*(height (oddOrbit n j)-((z-(A:ℤ):ℤ):ℝ)) :=
             mul_le_mul_of_nonneg_right du lo
           _ ≤ 35 := by nlinarith
    exact ⟨j,jq,Or.inr ⟨orbit_odd hn j,section_of_phase (orbit_pos np j) lo close⟩⟩
  · push Not at floor
    obtain ⟨j,jq,drop⟩ := floor
    exact ⟨j,jq,Or.inl drop⟩

/-- The clock includes every initial and intermediate halving, even in the
branch which descends below the auxiliary floor. -/
theorem bounded_visit_of_grid (n a q : Nat) (np : 0<n) (qp : 0<q)
    (cap : n.log2≤q) (cop : a.Coprime q)
    (approx : |(q:ℝ)*alpha-a|≤1/(q:ℝ)) :
    ∃ t<8*q+n.log2, Marked (orbit t n) := by
  let y := oddPart n
  have yp : 0<y := part_pos np
  have yo : y%2=1 := part_odd np
  have splitn : 2^(twos n)*y=n := split_twos n
  have yl : y≤n := by
    have h := Nat.mul_le_mul_right y (Nat.one_le_pow (twos n) 2 (by decide))
    omega
  have yc : y.log2≤q := ((Nat.le_log2 np.ne').mpr
    ((Nat.log2_self_le yp.ne').trans yl)).trans cap
  obtain ⟨j,jq,choice⟩ := grid_drop_or_mark y a q yo qp yc cop approx
  have hit : orbit (twos n) n=y := by
    simpa only [splitn] using orbit_pad (twos n) y
  let t := twos n+clock y j
  have exactHit : orbit t n=oddOrbit y j := by
    rw [show t=twos n+clock y j by rfl,orbit_add,hit,clock_exact yo]
  have upper : 2^t≤4^j*n := by
    have min1 := Nat.mul_le_mul_left (2^(clock y j)) (orbit_pos yp j)
    have one : 2^(clock y j)≤2^(clock y j)*oddOrbit y j := by simpa using min1
    calc 2^t = 2^(twos n)*2^(clock y j) := pow_add _ _ _
         _ ≤ 2^(twos n)*(4^j*y) :=
           Nat.mul_le_mul_left _ (one.trans (clock_weight yp j))
         _ = 4^j*(2^(twos n)*y) := by ring
         _ = 4^j*n := by rw [splitn]
  have bt : t<2*j+(n.log2+1) :=
    (Nat.pow_lt_pow_iff_right (by decide : 1<2)).mp (by
      calc 2^t ≤ 4^j*n := upper
           _ < 4^j*2^(n.log2+1) :=
             Nat.mul_lt_mul_of_pos_left Nat.lt_log2_self (by positivity)
           _ = 2^(2*j+(n.log2+1)) := by
             rw [pow_add 2 (2*j) (n.log2+1),pow_mul]; rfl)
  rcases choice with drop | mark
  · have xp : 0<oddOrbit y j := orbit_pos yp j
    obtain ⟨s,sb,sm⟩ := bounded_visit (oddOrbit y j) xp
    have sq : (oddOrbit y j).sqrt≤q := Nat.le_of_lt_succ
      (Nat.sqrt_lt.mpr (by nlinarith))
    have qpow : q≤2^q := (Nat.lt_two_pow_self (n:=q)).le
    have xpow : oddOrbit y j<2^(2*q) := by
      calc _ < q*q := drop
           _ ≤ 2^q*2^q := Nat.mul_le_mul qpow qpow
           _ = 2^(2*q) := by rw [← pow_add]; congr 1; omega
    have xl : (oddOrbit y j).log2<2*q := (Nat.log2_lt xp.ne').mpr xpow
    refine ⟨t+s,by omega,?_⟩
    rw [orbit_add,exactHit]
    exact sm
  · exact ⟨t,by omega,by rwa [exactHit]⟩

/-- Exact interface for a quantitative irrationality estimate. Excluding
all denominators below the source height supplies an actual short visit;
the exclusion is an explicit input, not an imported number-theory axiom. -/
theorem bounded_visit_of_separation (n N : Nat) (np : 0<n) (Np : 0<N)
    (sep : ∀ a q : Nat, 0<q → q<n.log2 →
      1/((N:ℝ)+1) < |(q:ℝ)*alpha-a|) :
    ∃ t<8*N+n.log2, Marked (orbit t n) := by
  obtain ⟨a,q,qp,qN,cop,_,err⟩ := rotation_grid N Np
  have cap : n.log2≤q := by
    by_contra h
    exact (not_lt_of_ge err) (sep a q qp (by omega))
  have near : |(q:ℝ)*alpha-a|≤1/(q:ℝ) := err.trans
    (one_div_le_one_div_of_le (by exact_mod_cast qp)
      (by exact_mod_cast (show q≤N+1 by omega)))
  obtain ⟨t,clock,mark⟩ := bounded_visit_of_grid n a q np qp cap cop near
  exact ⟨t,by omega,mark⟩

/-- At every admissible scale, every input in the whole exponential range
has an actual marked visit at a clock linear in that scale. -/
theorem uniform_visit_at_good_scale {q n : Nat} (good : Band.GoodScale q)
    (np : 0<n) (cap : n≤2^q) :
    ∃ t<9*q, Marked (orbit t n) := by
  obtain ⟨q16,a,cop,approx⟩ := good
  have lg : n.log2≤q := (Nat.pow_le_pow_iff_right (by decide : 1<2)).mp
    ((Nat.log2_self_le np.ne').trans cap)
  obtain ⟨t,lt,mark⟩ := bounded_visit_of_grid n a q np (by omega) lg cop approx
  exact ⟨t,by omega,mark⟩

/-- The ordinary endpoint bound keeps a forced mark below a prescribed
larger component source. -/
theorem orbit_growth (t n : Nat) : orbit t n≤2^t*n := by
  have step_le (v : Nat) : step v≤2*v := by
    unfold step
    split <;> omega
  induction t generalizing n with
  | zero => simp [orbit]
  | succ t ih =>
    calc orbit (t+1) n = orbit t (step n) := rfl
         _ ≤ 2^t*step n := ih _
         _ ≤ 2^t*(2*n) := Nat.mul_le_mul_left _ (step_le n)
         _ = 2^(t+1)*n := by ring

/-- The whole source range reaches marks below the same height ceiling used
by the earlier explicit inverse fans. -/
theorem uniform_visit_with_height {q n : Nat} (good : Band.GoodScale q)
    (np : 0<n) (cap : n≤2^q) :
    ∃ t<9*q, Marked (orbit t n) ∧ orbit t n<2^(10*q) := by
  obtain ⟨t,tq,mark⟩ := uniform_visit_at_good_scale good np cap
  refine ⟨t,tq,mark,?_⟩
  calc orbit t n ≤ 2^t*n := orbit_growth t n
       _ ≤ 2^t*2^q := Nat.mul_le_mul_left _ cap
       _ = 2^(t+q) := (pow_add _ _ _).symm
       _ < 2^(10*q) := (Nat.pow_lt_pow_iff_right (by decide : 1<2)).mpr (by omega)

/-- A supplied sufficiently small ordinary partner yields a genuinely smaller
marked partner, retaining the explicit merger clocks. No partner-existence
hypothesis is silently discharged. -/
theorem lower_marked_partner {q u n a b : Nat} (good : Band.GoodScale q)
    (up : 0<u) (cap : u≤2^q) (room : 2^(10*q)≤n)
    (merge : orbit a u=orbit b n) :
    ∃ t<9*q, ∃ y, Marked y ∧ y<n ∧ y=orbit t u ∧ orbit a y=orbit (b+t) n := by
  obtain ⟨t,tq,mark,small⟩ := uniform_visit_with_height good up cap
  refine ⟨t,tq,orbit t u,mark,small.trans_le room,rfl,?_⟩
  calc orbit a (orbit t u) = orbit (t+a) u := (orbit_add t a u).symm
       _ = orbit (a+t) u := by rw [Nat.add_comm t a]
       _ = orbit t (orbit a u) := orbit_add a t u
       _ = orbit t (orbit b n) := by rw [merge]
       _ = orbit (b+t) n := (orbit_add b t n).symm

/-- Integer powers can certify a supplied logarithmic grid, without using
an untrusted numerical logarithm. -/
theorem approximation_of_power_bracket (a q : Nat) (qp : 0<q) (aq : 0<a*q)
    (lower : 2^(a*q-1)≤3^(q*q)) (upper : 3^(q*q)≤2^(a*q+1)) :
    |(q:ℝ)*alpha-a|≤1/(q:ℝ) := by
  have qr : (0:ℝ)<q := by exact_mod_cast qp
  have lowerR : (2:ℝ)^(a*q-1)≤(3:ℝ)^(q*q) := by exact_mod_cast lower
  have upperR : (3:ℝ)^(q*q)≤(2:ℝ)^(a*q+1) := by exact_mod_cast upper
  have lo := logb_le_logb_of_le (by norm_num : (1:ℝ)<2) (by positivity) lowerR
  have hi := logb_le_logb_of_le (by norm_num : (1:ℝ)<2) (by positivity) upperR
  simp only [logb_pow,logb_two,mul_one] at lo hi
  change ((a*q-1:Nat):ℝ)≤((q*q:Nat):ℝ)*alpha at lo
  change ((q*q:Nat):ℝ)*alpha≤((a*q+1:Nat):ℝ) at hi
  have castsub : ((a*q-1:Nat):ℝ)=(a:ℝ)*q-1 := by
    rw [Nat.cast_sub (by omega : 1≤a*q),Nat.cast_mul,Nat.cast_one]
  rw [castsub] at lo
  push_cast at lo hi
  apply (le_div_iff₀ qr).mpr
  have bound : |((q:ℝ)*alpha-a)*(q:ℝ)|≤1 := by
    apply abs_le.mpr
    constructor <;> nlinarith
  simpa only [abs_mul,abs_of_pos qr] using bound

/-- One completely explicit good scale, checked by exact integer powers. -/
theorem good_scale_306 : Band.GoodScale 306 := by
  refine ⟨by decide,485,by decide,?_⟩
  exact approximation_of_power_bracket 485 306 (by decide) (by decide)
    CollatzBandCertificate.integer_bracket_306.1
    CollatzBandCertificate.integer_bracket_306.2

/-- A concrete range certificate for mandatory-band entrance, not for
convergence to one. -/
theorem band_visit_up_to_two_pow_306 {n : Nat} (np : 0<n) (cap : n≤2^306) :
    ∃ t<2754, Marked (orbit t n) ∧ orbit t n<2^3060 := by
  exact uniform_visit_with_height good_scale_306 np cap

#print axioms grid_drop_or_mark
#print axioms bounded_visit_of_grid
#print axioms bounded_visit_of_separation
#print axioms uniform_visit_at_good_scale
#print axioms orbit_growth
#print axioms uniform_visit_with_height
#print axioms lower_marked_partner
#print axioms approximation_of_power_bracket
#print axioms good_scale_306
#print axioms band_visit_up_to_two_pow_306

end CollatzShell.ForwardSection.Fast
