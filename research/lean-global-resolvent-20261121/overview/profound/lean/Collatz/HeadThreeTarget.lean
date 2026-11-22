import Collatz.SourceTargetInduction

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzHeadThreeTarget

open CollatzReverseBasin CollatzClosure CollatzWitness CollatzGapMultiset
open CollatzBoundedGapCofinal CollatzGapComparison
open CollatzSourceTargetInduction
open CollatzTerminalCarry (iterate iterate_add iterate_basin)

private theorem two_mul_iterate (a : Nat) : shortcut (2*a)=a := by
  unfold shortcut
  split <;> omega

private theorem odd_mul_iterate (a : Nat) : shortcut (2*a+1)=3*a+2 := by
  unfold shortcut
  split <;> omega

private theorem two_steps (n a b : Nat) (h0 : shortcut n=a) (h1 : shortcut a=b) :
    iterate n 2=b := by simp only [iterate,h0,h1]

/-- The actual shortcut ascent, with the endpoint written using addition
so no truncated subtraction enters its statement. -/
theorem mersenne_ascent {n k r : Nat} (start : n+1=2^k*r) :
    iterate n k+1=3^k*r := by
  induction k generalizing n r with
  | zero => simpa only [Nat.pow_zero,Nat.one_mul,iterate] using start
  | succ k ih =>
    have doubled : n+1=2*(2^k*r) := by
      simpa only [Nat.pow_succ,Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] using start
    have odd : n%2=1 := by omega
    have step : shortcut n+1=2^k*(3*r) := by
      have linear : shortcut n+1=3*(2^k*r) := by
        unfold shortcut
        split <;> omega
      simpa only [Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] using linear
    have next := ih step
    simpa only [iterate,Nat.pow_succ,Nat.mul_assoc,Nat.mul_left_comm,Nat.mul_comm] using next

/-- The ordinary half-merger diamond, credited to the existing PR184/185
physical merger and PR177 psi interfaces. The present use below keeps the
old complete source and decreases only its queried target. -/
theorem half_success {h r n x z : Nat}
    (large : n+1=2^(h+2)*r) (small : x+1=2^(h+1)*r)
    (phase : 3^(h+1)*r=4*z+3) :
    iterate n (h+4)=3*z+2 ∧ iterate x (h+3)=3*z+2 := by
  have sn := mersenne_ascent large
  have sx := mersenne_ascent small
  have pow : 3^(h+2)*r=3*(3^(h+1)*r) := by
    simp only [show h+2=(h+1)+1 by omega,Nat.pow_succ]
    simp only [Nat.mul_left_comm,Nat.mul_comm]
  have en : iterate n (h+2)=12*z+8 := by rw [pow,phase] at sn; omega
  have ex : iterate x (h+1)=4*z+2 := by rw [phase] at sx; omega
  have hn : iterate (12*z+8) 2=3*z+2 := by
    apply two_steps _ (6*z+4)
    · unfold shortcut; split <;> omega
    · unfold shortcut; split <;> omega
  have hx : iterate (4*z+2) 2=3*z+2 := by
    apply two_steps _ (2*z+1)
    · unfold shortcut; split <;> omega
    · exact odd_mul_iterate z
  constructor
  · rw [show h+4=(h+2)+2 by omega,iterate_add,en]; exact hn
  · rw [show h+3=(h+1)+2 by omega,iterate_add,ex]; exact hx

/-- The complementary phase is an exact transport to the positive-nine
carry. It is not asserted to be a successful merger. -/
theorem half_failure {h r n x z : Nat}
    (large : n+1=2^(h+2)*r) (small : x+1=2^(h+1)*r)
    (phase : 3^(h+1)*r=4*z+1) :
    iterate n (h+4)=9*z+2 ∧ iterate x (h+3)=z := by
  have sn := mersenne_ascent large
  have sx := mersenne_ascent small
  have pow : 3^(h+2)*r=3*(3^(h+1)*r) := by
    simp only [show h+2=(h+1)+1 by omega,Nat.pow_succ]
    simp only [Nat.mul_left_comm,Nat.mul_comm]
  have en : iterate n (h+2)=12*z+2 := by rw [pow,phase] at sn; omega
  have ex : iterate x (h+1)=4*z := by rw [phase] at sx; omega
  have hn : iterate (12*z+2) 2=9*z+2 := by
    apply two_steps _ (6*z+1)
    · unfold shortcut; split <;> omega
    · unfold shortcut; split <;> omega
  have hx : iterate (4*z) 2=z := by
    apply two_steps _ (2*z)
    · unfold shortcut; split <;> omega
    · exact two_mul_iterate z
  constructor
  · rw [show h+4=(h+2)+2 by omega,iterate_add,en]; exact hn
  · rw [show h+3=(h+1)+2 by omega,iterate_add,ex]; exact hx

/-- The remaining PR177 head-three psi target reaches 4v-1, while the
candidate 2v-1 is strictly below the original target. No new source or
convergence certificate is required to assert this arithmetic fact. -/
theorem head_three_prepare {q u n v x : Nat}
    (_positive : 0<q) (edge : 3*q+1=8*u)
    (target : n+1=8*q) (vdef : v+1=9*u) (partner : x+1=2*v) :
    0<x ∧ x<n ∧ iterate n 4+1=4*v := by
  have a3 : iterate n 3+1=27*q := by
    simpa only [show (2:Nat)^3=8 by decide,show (3:Nat)^3=27 by decide] using
      (mersenne_ascent (k:=3) target)
  have a4 : shortcut (iterate n 3)+1=4*v := by
    unfold shortcut
    split <;> omega
  have it : iterate n 4=shortcut (iterate n 3) := by
    rw [show 4=3+1 by decide,iterate_add]
    rfl
  exact ⟨by omega,by omega,by rw [it]; exact a4⟩

/-- Whole unbounded success family in the head-three branch. This repairs
the certificate-rank objection in PR177's head-three note by providing a
smaller TARGET at the same supplied source. -/
theorem head_three_success_merger {q u n v x h r z : Nat}
    (positive : 0<q) (edge : 3*q+1=8*u)
    (target : n+1=8*q) (vdef : v+1=9*u) (partner : x+1=2*v)
    (factor : v=2^h*r) (phase : 3^(h+1)*r=4*z+3) :
    0<x ∧ x<n ∧ iterate n (h+8)=iterate x (h+3) := by
  obtain ⟨xp,small,entry⟩ := head_three_prepare positive edge target vdef partner
  have large : iterate n 4+1=2^(h+2)*r := by
    rw [entry,factor,Nat.pow_add]
    simp only [show (2:Nat)^2=4 by decide,Nat.mul_assoc,Nat.mul_comm]
  have smaller : x+1=2^(h+1)*r := by
    rw [partner,factor,Nat.pow_succ]
    simp only [Nat.mul_left_comm,Nat.mul_comm]
  obtain ⟨hn,hx⟩ := half_success large smaller phase
  refine ⟨xp,small,?_⟩
  rw [show h+8=4+(h+4) by omega,iterate_add,hn,hx]

/-- The success family is a branch of the previously checked combined
source-grade/target induction for every activated original source. -/
theorem head_three_success_rule {source q u n v x h r z : Nat}
    (positive : 0<q) (edge : 3*q+1=8*u)
    (target : n+1=8*q) (vdef : v+1=9*u) (partner : x+1=2*v)
    (factor : v=2^h*r) (phase : 3^(h+1)*r=4*z+3)
    (active : Interval source n) (inner : SameSourceHyp source n) : Basin n := by
  obtain ⟨xp,small,meeting⟩ :=
    head_three_success_merger positive edge target vdef partner factor phase
  exact same_source_merger active xp small meeting.symm inner

/-- Exact opposite phase. The smaller partner's existing same-source
proof yields Basin z, but no inference Basin z -> Basin (9z+2) is made. -/
theorem head_three_failure_transport {q u n v x h r z : Nat}
    (positive : 0<q) (edge : 3*q+1=8*u)
    (target : n+1=8*q) (vdef : v+1=9*u) (partner : x+1=2*v)
    (factor : v=2^h*r) (phase : 3^(h+1)*r=4*z+1) :
    0<x ∧ x<n ∧ iterate n (h+8)=9*z+2 ∧ iterate x (h+3)=z := by
  obtain ⟨xp,small,entry⟩ := head_three_prepare positive edge target vdef partner
  have large : iterate n 4+1=2^(h+2)*r := by
    rw [entry,factor,Nat.pow_add]
    simp only [show (2:Nat)^2=4 by decide,Nat.mul_assoc,Nat.mul_comm]
  have smaller : x+1=2^(h+1)*r := by
    rw [partner,factor,Nat.pow_succ]
    simp only [Nat.mul_left_comm,Nat.mul_comm]
  obtain ⟨hn,hx⟩ := half_failure large smaller phase
  refine ⟨xp,small,?_,hx⟩
  rw [show h+8=4+(h+4) by omega,iterate_add,hn]

/-- The certified smaller companion in the failure phase can rise above
the original target. This theorem carries only its valid Basin conclusion,
not a newly ranked complete certificate or a larger interval hypothesis. -/
theorem failure_companion_basin {source q u n v x h r z : Nat}
    (positive : 0<q) (edge : 3*q+1=8*u)
    (target : n+1=8*q) (vdef : v+1=9*u) (partner : x+1=2*v)
    (factor : v=2^h*r) (phase : 3^(h+1)*r=4*z+1)
    (active : Interval source n) (inner : SameSourceHyp source n) :
    Basin z ∧ (Basin (9*z+2) ↔ Basin n) := by
  obtain ⟨xp,small,hn,hx⟩ :=
    head_three_failure_transport positive edge target vdef partner factor phase
  have known := inner x (interval_downward active xp (Nat.le_of_lt small)) small
  constructor
  · have reached := (iterate_basin x (h+3)).mpr known
    simpa only [hx] using reached
  · simpa only [hn] using iterate_basin n (h+8)

private theorem odd_two_factor {v : Nat} (positive : 0<v) :
    ∃ h r, 0<r ∧ r%2=1 ∧ v=2^h*r := by
  induction v using Nat.strong_induction_on with
  | h v ih =>
    by_cases odd : v%2=1
    · exact ⟨0,v,positive,odd,by simp⟩
    · have even : v%2=0 := by omega
      have vp : 0<v/2 := by omega
      have smaller : v/2<v := by omega
      obtain ⟨h,r,rp,ro,factor⟩ := ih (v/2) smaller vp
      refine ⟨h+1,r,rp,ro,?_⟩
      calc
        v=2*(v/2) := by omega
        _=2*(2^h*r) := by rw [factor]
        _=2^(h+1)*r := by
          simp only [Nat.pow_succ,Nat.mul_left_comm,Nat.mul_comm]

private theorem pow_three_odd (h : Nat) : 3^h%2=1 := by
  induction h with
  | zero => decide
  | succ h ih => rw [Nat.pow_succ]; omega

/-- Exhaustive normalization of EVERY ordinary head-three target. The
second disjunct preserves the actual failed carry and its positive
companion. It is not replaced by a convergence assumption. -/
theorem head_three_dichotomy {q u n v x : Nat}
    (positive : 0<q) (edge : 3*q+1=8*u) (odd : u%2=1)
    (target : n+1=8*q) (vdef : v+1=9*u) (partner : x+1=2*v) :
    0<x ∧ x<n ∧ ∃ h r, 0<h ∧ r%2=1 ∧ v=2^h*r ∧
      ((∃ z, 3^(h+1)*r=4*z+3 ∧ iterate n (h+8)=iterate x (h+3)) ∨
       (∃ z, 0<z ∧ 3^(h+1)*r=4*z+1 ∧
         iterate n (h+8)=9*z+2 ∧ iterate x (h+3)=z)) := by
  obtain ⟨xp,small,_⟩ := head_three_prepare positive edge target vdef partner
  have vp : 0<v := by omega
  have ve : v%2=0 := by omega
  obtain ⟨h,r,rp,ro,factor⟩ := odd_two_factor vp
  have hp : 0<h := by
    cases h with
    | zero => simp only [Nat.pow_zero,Nat.one_mul] at factor; omega
    | succ h => omega
  have bo : (3^(h+1)*r)%2=1 := by
    rw [Nat.mul_mod,pow_three_odd,ro]
  have phases : (3^(h+1)*r)%4=3 ∨ (3^(h+1)*r)%4=1 := by omega
  refine ⟨xp,small,h,r,hp,ro,factor,?_⟩
  rcases phases with success | failure
  · have phase : 3^(h+1)*r=4*((3^(h+1)*r)/4)+3 := by omega
    obtain ⟨_,_,meeting⟩ :=
      head_three_success_merger positive edge target vdef partner factor phase
    exact Or.inl ⟨(3^(h+1)*r)/4,phase,meeting⟩
  · have phase : 3^(h+1)*r=4*((3^(h+1)*r)/4)+1 := by omega
    obtain ⟨_,_,hn,hx⟩ :=
      head_three_failure_transport positive edge target vdef partner factor phase
    have zp := CollatzTerminalCarry.iterate_positive xp (h+3)
    rw [hx] at zp
    exact Or.inr ⟨(3^(h+1)*r)/4,zp,phase,hn,hx⟩

/-- A complete structural subfamily: EVERY source starting with [3,3]
has the uniform affine merger, irrespective of its remaining tail.
The clocks 10 and 5 refer to actual shortcut steps. -/
theorem head_three_three_merger {q u w n v x : Nat}
    (positive : 0<q) (edge : 3*q+1=8*u) (next : 3*u+1=8*w)
    (odd : w%2=1) (target : n+1=8*q) (vdef : v+1=9*u) (partner : x+1=2*v) :
    0<x ∧ x<n ∧ iterate n 10=iterate x 5 := by
  have uform : u=16*(u/16)+13 := by omega
  have factor : v=2^2*(36*(u/16)+29) := by
    simp only [show (2:Nat)^2=4 by decide]
    omega
  have phase : 3^(2+1)*(36*(u/16)+29)=4*(243*(u/16)+195)+3 := by
    simp only [show (3:Nat)^(2+1)=27 by decide]
    omega
  simpa only [show (2:Nat)+8=10 by decide,show (2:Nat)+3=5 by decide] using
    head_three_success_merger positive edge target vdef partner factor phase

/-- This entire [3,3] family supplies an actual branch of MixedCover at
the original source grade. It does not re-extract the partner's certificate. -/
theorem head_three_three_mixed {q u w n v x : Nat}
    (positive : 0<q) (edge : 3*q+1=8*u) (next : 3*u+1=8*w)
    (odd : w%2=1) (target : n+1=8*q) (vdef : v+1=9*u) (partner : x+1=2*v)
    (source : Nat) (old : List Nat) : MixedWitness source n old := by
  obtain ⟨xp,small,meeting⟩ :=
    head_three_three_merger positive edge next odd target vdef partner
  exact MixedWitness.smaller xp small meeting.symm

/-- The complete original-source arithmetic survives the normalization.
In particular, a residual cannot be reassigned to an unrelated source
merely because it has the same positive-nine carry shape. -/
theorem head_three_source_identity {q u n v h r : Nat}
    (edge : 3*q+1=8*u) (target : n+1=8*q) (vdef : v+1=9*u)
    (factor : v=2^h*r) :
    27*q+1=8*(2^h*r) ∧ 27*n+35=64*(2^h*r) := by
  constructor <;> omega

private theorem power_ratio (h : Nat) (large : 3≤h) :
    2^(h+8)<3^(h+4) := by
  obtain ⟨k,rfl⟩ := Nat.exists_eq_add_of_le large
  induction k with
  | zero => decide
  | succ k ih =>
    rw [show 3+(k+1)+8=(3+k+8)+1 by omega,
      show 3+(k+1)+4=(3+k+4)+1 by omega,
      Nat.pow_succ (2:Nat) (3+k+8),Nat.pow_succ (3:Nat) (3+k+4)]
    omega

/-- Sharp warning for the failed phase: once h>=3, its certified forward
companion z is ALWAYS larger than the original target. Its Basin proof is
valid by orbit transport from the smaller partner; numerical inner descent
and a newly paid source interval do not follow from that proof. -/
theorem failure_large_companion {q u n v h r z : Nat}
    (edge : 3*q+1=8*u) (target : n+1=8*q) (vdef : v+1=9*u)
    (factor : v=2^h*r) (positive : 0<r) (large : 3≤h)
    (phase : 3^(h+1)*r=4*z+1) : n<z := by
  obtain ⟨_,sourceEq⟩ := head_three_source_identity edge target vdef factor
  have left : 108*n+140=2^(h+8)*r := by
    rw [Nat.pow_add]
    have algebra : (2^h*2^8)*r=256*(2^h*r) := by
      simp only [show (2:Nat)^8=256 by decide,Nat.mul_assoc,Nat.mul_comm]
    rw [algebra]
    omega
  have right : 108*z+27=3^(h+4)*r := by
    rw [show h+4=(h+1)+3 by omega,Nat.pow_add]
    have algebra : (3^(h+1)*3^3)*r=27*(3^(h+1)*r) := by
      simp only [show (3:Nat)^3=27 by decide,Nat.mul_assoc,Nat.mul_comm]
    rw [algebra]
    omega
  have growth := Nat.mul_lt_mul_of_pos_right (power_ratio h large) positive
  omega

end CollatzHeadThreeTarget
