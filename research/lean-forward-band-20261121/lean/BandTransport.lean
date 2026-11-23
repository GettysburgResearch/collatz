import ForwardSection

/-!
Exact transport after binary precision has been exhausted.

For a ternary unit q, an arbitrary difference 3^p*u can be carried backwards
through p genuine odd inverse steps, with between p and 4*p ordinary clocks.
The output difference is exactly 2^A*u. The clocks are selected from the
reference value modulo nine and are shared by the entire affine family.
-/

namespace CollatzShell.BandTransport

def oddCount : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, n => oddCount k (step n) + n%2

private theorem step_shift (a b : Nat) :
    step (2*a+b) = 3^(b%2)*a + step b := by
  by_cases ev : b%2=0
  · simp [step,ev,show (2*a+b)%2=0 by omega]; omega
  · have odd : b%2=1 := by omega
    simp [step,odd]; omega

theorem orbit_shift (k b u : Nat) :
    orbit k (2^k*u+b)=3^(oddCount k b)*u+orbit k b := by
  induction k generalizing b u with
  | zero => simp [orbit,oddCount]
  | succ k ih =>
    rw [show 2^(k+1)*u+b=2*(2^k*u)+b by ring]
    simp only [orbit,oddCount,step_shift,pow_add]
    rw [show 3^(b%2)*(2^k*u)+step b=2^k*(3^(b%2)*u)+step b by ring,ih]
    ring

theorem oddCount_shift (k b u : Nat) :
    oddCount k (2^k*u+b)=oddCount k b := by
  have h := orbit_shift k b (u+1)
  rw [show 2^k*(u+1)+b=2^k*1+(2^k*u+b) by ring,
    orbit_shift,orbit_shift] at h
  simp only [Nat.mul_add,Nat.mul_one] at h
  have powers : 3^(oddCount k (2^k*u+b))=3^(oddCount k b) := by omega
  exact Nat.pow_right_injective (by decide : 2≤3) powers

def inverseClock (q : Nat) : Nat :=
  match q%9 with
  | 1 => 2 | 2 => 1 | 4 => 2 | 5 => 3 | 7 => 4 | _ => 1

def inverseSource (q : Nat) : Nat :=
  match q%9 with
  | 1 => 12*(q/9)+1
  | 2 => 6*(q/9)+1
  | 4 => 12*(q/9)+5
  | 5 => 24*(q/9)+13
  | 7 => 48*(q/9)+37
  | _ => 6*(q/9)+5

private theorem unit_residues (q : Nat) (hu : q%3≠0) :
    q%9=1 ∨ q%9=2 ∨ q%9=4 ∨ q%9=5 ∨ q%9=7 ∨ q%9=8 := by omega

theorem inverse_clock_bounds (q : Nat) (hu : q%3≠0) :
    1 ≤ inverseClock q ∧ inverseClock q≤4 := by
  rcases unit_residues q hu with h|h|h|h|h|h <;> simp [inverseClock,h]

theorem inverse_source_unit (q : Nat) (hu : q%3≠0) : inverseSource q%3≠0 := by
  rcases unit_residues q hu with h|h|h|h|h|h <;> simp [inverseSource,h] <;> omega

theorem inverse_source_affine (q : Nat) (hu : q%3≠0) :
    3*inverseSource q+1=2^(inverseClock q)*q := by
  rcases unit_residues q hu with h|h|h|h|h|h <;>
    simp only [inverseClock,inverseSource,h] <;> norm_num <;> omega

private theorem affine_word (h c r u : Nat) (hc : oddCount h c=1)
    (hr : orbit h c=r) :
    orbit h (2^h*u+c)=3*u+r := by rw [orbit_shift,hc,hr]; simp

theorem inverse_word (q : Nat) (hu : q%3≠0) (u : Nat) :
    orbit (inverseClock q) (2^(inverseClock q)*u+inverseSource q)=3*u+q := by
  rcases unit_residues q hu with h|h|h|h|h|h
  all_goals simp only [inverseClock,inverseSource,h]
  · rw [show 2^2*u+(12*(q/9)+1)=2^2*(u+3*(q/9))+1 by ring]
    rw [affine_word 2 1 1 _ (by decide) (by decide)]; omega
  · rw [show 2^1*u+(6*(q/9)+1)=2^1*(u+3*(q/9))+1 by ring]
    rw [affine_word 1 1 2 _ (by decide) (by decide)]; omega
  · rw [show 2^2*u+(12*(q/9)+5)=2^2*(u+3*(q/9))+5 by ring]
    rw [affine_word 2 5 4 _ (by decide) (by decide)]; omega
  · rw [show 2^3*u+(24*(q/9)+13)=2^3*(u+3*(q/9))+13 by ring]
    rw [affine_word 3 13 5 _ (by decide) (by decide)]; omega
  · rw [show 2^4*u+(48*(q/9)+37)=2^4*(u+3*(q/9))+37 by ring]
    rw [affine_word 4 37 7 _ (by decide) (by decide)]; omega
  · rw [show 2^1*u+(6*(q/9)+5)=2^1*(u+3*(q/9))+5 by ring]
    rw [affine_word 1 5 8 _ (by decide) (by decide)]; omega

def restoredClock : Nat → Nat → Nat
  | 0, _ => 0
  | p+1, q => restoredClock p (inverseSource q)+inverseClock q

def restoredSource : Nat → Nat → Nat
  | 0, q => q
  | p+1, q => restoredSource p (inverseSource q)

theorem restored_bounds (p q : Nat) (hu : q%3≠0) :
    p≤restoredClock p q ∧ restoredClock p q≤4*p ∧ restoredSource p q%3≠0 := by
  induction p generalizing q with
  | zero => simp [restoredClock,restoredSource,hu]
  | succ p ih =>
    obtain ⟨lower,upper,unit⟩ := ih (inverseSource q) (inverse_source_unit q hu)
    obtain ⟨rl,ru⟩ := inverse_clock_bounds q hu
    simp only [restoredClock,restoredSource]
    omega

/-- Arbitrary ternary precision can be restored to exact binary precision.
The two inputs lie on actual ordinary forward orbits, with the same clock. -/
theorem restored_word (p q : Nat) (hu : q%3≠0) (u : Nat) :
    orbit (restoredClock p q) (2^(restoredClock p q)*u+restoredSource p q)=
      3^p*u+q := by
  induction p generalizing q u with
  | zero => simp [restoredClock,restoredSource,orbit]
  | succ p ih =>
    simp only [restoredClock,restoredSource,pow_add,orbit_add]
    rw [show 2^(restoredClock p (inverseSource q))*2^(inverseClock q)*u+
        restoredSource p (inverseSource q)=
        2^(restoredClock p (inverseSource q))*(2^(inverseClock q)*u)+
        restoredSource p (inverseSource q) by ring,
      ih (inverseSource q) (inverse_source_unit q hu) (2^(inverseClock q)*u)]
    rw [show 3^p*(2^(inverseClock q)*u)+inverseSource q=
        2^(inverseClock q)*(3^p*u)+inverseSource q by ring,inverse_word q hu]
    ring

theorem restored_basin_iff (p q u : Nat) (hu : q%3≠0) :
    Basin (2^(restoredClock p q)*u+restoredSource p q) ↔ Basin (3^p*u+q) :=
  basin_at_hit ⟨restoredClock p q,restored_word p q hu u⟩

theorem restored_forward (p q : Nat) (hu : q%3≠0) :
    orbit (restoredClock p q) (restoredSource p q)=q := by
  simpa using restored_word p q hu 0

theorem restored_odd_count (p q : Nat) (hu : q%3≠0) :
    oddCount (restoredClock p q) (restoredSource p q)=p := by
  have h := restored_word p q hu 1
  rw [orbit_shift,restored_forward p q hu] at h
  simp only [Nat.mul_one] at h
  have powers : 3^(oddCount (restoredClock p q) (restoredSource p q))=3^p := by omega
  exact Nat.pow_right_injective (by decide : 2≤3) powers

theorem restored_height (p q : Nat) (hu : q%3≠0) :
    3^p*restoredSource p q≤2^(restoredClock p q)*q := by
  induction p generalizing q with
  | zero => simp [restoredSource,restoredClock]
  | succ p ih =>
    have h := ih (inverseSource q) (inverse_source_unit q hu)
    have single := inverse_source_affine q hu
    simp only [restoredSource,restoredClock,pow_succ,pow_add]
    nlinarith [Nat.mul_le_mul_left 3 h,
      Nat.mul_le_mul_left (2^(restoredClock p (inverseSource q))) (show
        3*inverseSource q≤2^(inverseClock q)*q by omega)]

/-- An exact integer box bound: all additive errors are absorbed by the strict
upper endpoint, so no rational affine estimate is needed. -/
theorem orbit_box (d n C : Nat) (hn : n<2^d*C) :
    orbit d n<3^(oddCount d n)*C := by
  induction d generalizing n C with
  | zero => simpa [orbit,oddCount] using hn
  | succ d ih =>
    by_cases ev : n%2=0
    · have hs : step n<2^d*C := by
        simp only [step,ev,ite_true]
        have h : n<2*(2^d*C) := by
          simpa [pow_succ,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using hn
        omega
      simpa [orbit,oddCount,ev] using ih (step n) C hs
    · have odd : n%2=1 := by omega
      have hs : step n<2^d*(3*C) := by
        simp only [step,show n%2≠0 by omega,ite_false]
        rw [pow_succ] at hn
        nlinarith only [hn,Nat.div_mul_le_self (3*n+1) 2]
      simpa [orbit,oddCount,odd,pow_succ,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm]
        using ih (step n) (3*C) hs

theorem orbit_scaled_lower (d n : Nat) :
    3^(oddCount d n)*n≤2^d*orbit d n := by
  induction d generalizing n with
  | zero => simp [orbit,oddCount]
  | succ d ih =>
    have hs : 3^(n%2)*n≤2*step n := by
      by_cases ev : n%2=0
      · simp [step,ev]; omega
      · have odd : n%2=1 := by omega
        simp [step,odd]; omega
    simp only [orbit,oddCount,pow_add]
    calc 3^(oddCount d (step n))*3^(n%2)*n
        =3^(oddCount d (step n))*(3^(n%2)*n) := by ring
      _ ≤3^(oddCount d (step n))*(2*step n) := Nat.mul_le_mul_left _ hs
      _ =2*(3^(oddCount d (step n))*step n) := by ring
      _ ≤2*(2^d*orbit d (step n)) := Nat.mul_le_mul_left 2 (ih (step n))
      _ =2^(d+1)*orbit d (step n) := by ring

/-- Saving one ordinary clock while preserving the odd count places a common
ancestor strictly below the original dyadic floor. -/
theorem compressed_source_below_floor {d n A b : Nat}
    (upper : n<2^(d+1)) (shorter : A<d)
    (sameOdd : oddCount A b=oddCount d n)
    (sameEnd : orbit A b=orbit d n) : b<2^d := by
  have box := orbit_box d n 2 (by simpa [pow_succ,Nat.mul_comm] using upper)
  have lower := orbit_scaled_lower A b
  rw [sameOdd,sameEnd] at lower
  have clock : 2^A*2≤2^d := by
    rw [← pow_succ]
    exact Nat.pow_le_pow_right (by decide : 0<2) (by omega)
  have mult : 3^(oddCount d n)*b<3^(oddCount d n)*2^d := by
    calc _ ≤2^A*orbit d n := lower
      _ <2^A*(3^(oddCount d n)*2) := Nat.mul_lt_mul_of_pos_left box (by positivity)
      _ =3^(oddCount d n)*(2^A*2) := by ring
      _ ≤3^(oddCount d n)*2^d := Nat.mul_le_mul_left _ clock
  exact (Nat.mul_lt_mul_left (by positivity : 0<3^(oddCount d n))).mp mult

theorem compressed_component_descent {d n A b : Nat}
    (floor : 2^d≤n) (upper : n<2^(d+1)) (shorter : A<d)
    (sameOdd : oddCount A b=oddCount d n)
    (sameEnd : orbit A b=orbit d n) :
    b<n ∧ (Basin n ↔ Basin b) := by
  refine ⟨(compressed_source_below_floor upper shorter sameOdd sameEnd).trans_le floor,?_⟩
  exact (basin_at_hit (show Hits n (orbit d n) from ⟨d,rfl⟩)).trans
    (basin_at_hit (show Hits b (orbit d n) from ⟨A,sameEnd⟩)).symm

/-- This is an executable sufficient condition. The inverse algorithm itself is
total on ternary units; the strict clock comparison is a separate condition. -/
theorem restored_component_descent {d n : Nat}
    (floor : 2^d≤n) (upper : n<2^(d+1)) (hu : (orbit d n)%3≠0)
    (shorter : restoredClock (oddCount d n) (orbit d n)<d) :
    restoredSource (oddCount d n) (orbit d n)<n ∧
      (Basin n ↔ Basin (restoredSource (oddCount d n) (orbit d n))) := by
  exact compressed_component_descent floor upper shorter
    (restored_odd_count _ _ hu) (restored_forward _ _ hu)

/-- Apply the shared inverse path to an exhausted high-bit comparison. -/
theorem restored_tail_descent {d a : Nat} (small : a<2^d)
    (hu : (orbit d a)%3≠0)
    (shorter : restoredClock (oddCount d a) (orbit d a)<d) :
    let A := restoredClock (oddCount d a) (orbit d a)
    let b := restoredSource (oddCount d a) (orbit d a)
    2^A+b<2^d ∧ (Basin (2^d+a) ↔ Basin (2^A+b)) := by
  dsimp only
  let p := oddCount d a
  let q := orbit d a
  let A := restoredClock p q
  let b := restoredSource p q
  have source_count : oddCount d (2^d+a)=p := by
    simpa [p] using oddCount_shift d a 1
  have target_count : oddCount A (2^A+b)=p := by
    have shift := oddCount_shift A b 1
    simpa [A,b,restored_odd_count p q hu] using shift
  have endpt : orbit A (2^A+b)=orbit d (2^d+a) := by
    have h₁ := restored_word p q hu 1
    have h₂ := orbit_shift d a 1
    simpa [A,b,p,q] using h₁.trans h₂.symm
  have upper : 2^d+a<2^(d+1) := by rw [pow_succ]; omega
  refine ⟨compressed_source_below_floor upper shorter
      (target_count.trans source_count.symm) endpt,?_⟩
  exact (basin_at_hit (show Hits (2^d+a) (orbit d (2^d+a)) from ⟨d,rfl⟩)).trans
    (basin_at_hit (show Hits (2^A+b) (orbit d (2^d+a)) from ⟨A,endpt⟩)).symm

private theorem even_fork (z : Nat) :
    orbit 2 (12*z+8)=3*z+2 ∧ orbit 2 (4*z+2)=3*z+2 := by
  constructor
  · rw [show 12*z+8=2^2*(3*z+2) by ring,orbit_pad]
  · change step (step (4*z+2))=3*z+2
    rw [show 4*z+2=2*(2*z+1) by ring,step_double]
    simp [step]
    omega

/-- The complementary phase is retained explicitly; it is not a solved case. -/
theorem complementary_fork (z : Nat) :
    orbit 2 (12*z+2)=9*z+2 ∧ orbit 2 (4*z)=z := by
  constructor
  · change step (step (12*z+2))=9*z+2
    rw [show 12*z+2=2*(6*z+1) by ring,step_double]
    simp [step,show (6*z+1)%2≠0 by omega]
    omega
  · rw [show 4*z=2^2*z by ring,orbit_pad]

/-- A complete odd block can be shortened by one clock, even when the block
has arbitrarily many expanding odd steps. -/
theorem adjacent_odd_block (r u : Nat) (hu : 0<u)
    (phase : (3^r*u)%4=3) :
    orbit (r+3) (2^(r+1)*u-1)=orbit (r+2) (2^r*u-1) := by
  have eq : 3^r*u=4*((3^r*u)/4)+3 := by omega
  have left : 3^(r+1)*u-1=12*((3^r*u)/4)+8 := by
    rw [show 3^(r+1)*u=3*(3^r*u) by rw [pow_succ]; ring,eq]
    omega
  have right : 3^r*u-1=4*((3^r*u)/4)+2 := by omega
  rw [show r+3=(r+1)+2 by omega,orbit_add (r+1) 2,orbit_add r 2,
    (odd_run (r+1) u hu).1,(odd_run r u hu).1,left,right]
  exact (even_fork _).1.trans (even_fork _).2.symm

theorem adjacent_odd_block_descent (r u : Nat) (hu : 0<u)
    (phase : (3^r*u)%4=3) :
    2^r*u-1<2^(r+1)*u-1 ∧
      (Basin (2^(r+1)*u-1) ↔ Basin (2^r*u-1)) := by
  have pos : 0<2^r*u := by positivity
  constructor
  · rw [show 2^(r+1)*u=2*(2^r*u) by rw [pow_succ]; ring]
    omega
  · have common := adjacent_odd_block r u hu phase
    exact (basin_at_hit (show Hits (2^(r+1)*u-1)
        (orbit (r+3) (2^(r+1)*u-1)) from ⟨r+3,rfl⟩)).trans
      (basin_at_hit (show Hits (2^r*u-1)
        (orbit (r+3) (2^(r+1)*u-1)) from ⟨r+2,common.symm⟩)).symm

def bandSource (k : Nat) := 2^(3*k)+2^(2*k)-1
def bandSmaller (k : Nat) := 2^(3*k-1)+2^(2*k-1)-1

private theorem band_factors (k : Nat) (hk : 2≤k) :
    bandSource k=2^((2*k-1)+1)*(2^k+1)-1 ∧
      bandSmaller k=2^(2*k-1)*(2^k+1)-1 := by
  have a : (2*k-1)+1=2*k := by omega
  have b : (2*k-1)+k=3*k-1 := by omega
  constructor
  · rw [a,Nat.mul_add,Nat.mul_one,← pow_add,show 2*k+k=3*k by omega]
    rfl
  · rw [Nat.mul_add,Nat.mul_one,← pow_add,b]
    rfl

private theorem band_phase (k : Nat) (hk : 2≤k) :
    (3^(2*k-1)*(2^k+1))%4=3 := by
  have odd : 2*k-1=2*(k-1)+1 := by omega
  have h3 : 3^(2*k-1)%4=3 := by
    rw [odd,pow_add,pow_mul]
    simp [Nat.mul_mod,Nat.pow_mod]
  have even : k=2+(k-2) := by omega
  have h2 : 2^k%4=0 := by rw [even,pow_add]; simp
  simp [Nat.mul_mod,Nat.add_mod,h3,h2]

/-- The two actual trajectories have an exactly one-clock difference. -/
theorem band_common_endpoint (k : Nat) (hk : 2≤k) :
    orbit (2*k+2) (bandSource k)=orbit (2*k+1) (bandSmaller k) := by
  have h := adjacent_odd_block (2*k-1) (2^k+1) (by positivity) (band_phase k hk)
  obtain ⟨left,right⟩ := band_factors k hk
  rw [← left,← right] at h
  simpa only [show (2*k-1)+3=2*k+2 by omega,
    show (2*k-1)+2=2*k+1 by omega] using h

theorem band_dyadic_common_endpoint (k : Nat) (hk : 2≤k) :
    orbit (3*k) (bandSource k)=orbit (3*k-1) (bandSmaller k) := by
  have h := congrArg (orbit (k-2)) (band_common_endpoint k hk)
  rw [← orbit_add,← orbit_add] at h
  simpa only [show (2*k+2)+(k-2)=3*k by omega,
    show (2*k+1)+(k-2)=3*k-1 by omega] using h

theorem band_half (k : Nat) (hk : 2≤k) :
    bandSource k=2*bandSmaller k+1 := by
  obtain ⟨left,right⟩ := band_factors k hk
  rw [left,right,show 2^((2*k-1)+1)*(2^k+1)=2*(2^(2*k-1)*(2^k+1)) by
    rw [pow_succ]; ring]
  have pos : 0<2^(2*k-1)*(2^k+1) := by positivity
  omega

private theorem band_bounds (k : Nat) :
    2^(3*k)≤bandSource k ∧ bandSource k<2^(3*k+1) := by
  have pos : 0<2^(2*k) := by positivity
  have le : 2^(2*k)≤2^(3*k) :=
    Nat.pow_le_pow_right (by decide : 0<2) (by omega)
  unfold bandSource
  rw [pow_succ]
  omega

theorem band_marked (k : Nat) (hk : 2≤k) : ForwardSection.Marked (bandSource k) := by
  obtain ⟨lower,upper⟩ := band_bounds k
  have pos : 0<bandSource k := (by positivity : 0<2^(3*k)).trans_le lower
  have lg : (bandSource k).log2=3*k := (Nat.log2_eq_iff pos.ne').mpr ⟨lower,upper⟩
  have offset : bandSource k-2^(3*k)=2^(2*k)-1 := by
    unfold bandSource
    have h : 0<2^(2*k) := by positivity
    omega
  refine ⟨by rw [band_half k hk]; omega,?_⟩
  unfold ForwardSection.InSection
  rw [lg,offset]
  have coeff : 3*k+1≤70*2^k := by have := Nat.lt_two_pow_self (n:=k); omega
  calc (3*k+1)*(2^(2*k)-1)
      ≤(3*k+1)*2^(2*k) := Nat.mul_le_mul_left _ (Nat.sub_le _ _)
    _ ≤(70*2^k)*2^(2*k) := Nat.mul_le_mul_right _ coeff
    _ =70*2^(3*k) := by rw [Nat.mul_assoc,← pow_add,show k+2*k=3*k by omega]

theorem band_component_descent (k : Nat) (hk : 2≤k) :
    bandSmaller k<bandSource k ∧ (Basin (bandSource k) ↔ Basin (bandSmaller k)) := by
  have eq := band_half k hk
  have common := band_common_endpoint k hk
  refine ⟨by omega,?_⟩
  exact (basin_at_hit (show Hits (bandSource k) (orbit (2*k+2) (bandSource k)) from
      ⟨2*k+2,rfl⟩)).trans
    (basin_at_hit (show Hits (bandSmaller k) (orbit (2*k+2) (bandSource k)) from
      ⟨2*k+1,common.symm⟩)).symm

theorem band_family_unbounded (B : Nat) :
    ∃ k, 2≤k ∧ B<bandSource k ∧ ForwardSection.Marked (bandSource k) ∧
      bandSmaller k<bandSource k ∧ (Basin (bandSource k) ↔ Basin (bandSmaller k)) := by
  let k := B+2
  have hk : 2≤k := by dsimp [k]; omega
  have less : B<bandSource k := by
    have power := Nat.lt_two_pow_self (n:=3*k)
    have lower := (band_bounds k).1
    dsimp [k] at power lower ⊢
    omega
  exact ⟨k,hk,less,band_marked k hk,band_component_descent k hk⟩

#print axioms restored_word
#print axioms restored_basin_iff
#print axioms restored_height
#print axioms compressed_component_descent
#print axioms restored_tail_descent
#print axioms band_common_endpoint
#print axioms band_dyadic_common_endpoint
#print axioms band_marked
#print axioms band_component_descent
#print axioms band_family_unbounded

end CollatzShell.BandTransport
