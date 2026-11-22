module

public import CarryLanguage
public import Mathlib.Data.Nat.Factorization.Basic

@[expose] public section

/-!
# A terminating negative-complement budget for arbitrary positive debt

The negative shortcut is an auxiliary arithmetic machine, not an assumed
convergent Collatz variant.  A bounded number of its even steps can always be
obtained above the explicit dyadic threshold.  This yields actual ordinary
target descent over sufficiently long supplied all-one source prefixes.
-/

namespace CollatzShell.NegativeCarry

open WitnessGlobal WitnessSynthesis

def negativeStep (d : Nat) : Nat :=
  if d % 2 = 0 then d / 2 else (3*d-1)/2

def negativeOrbit : Nat → Nat → Nat
  | 0,d => d
  | k+1,d => negativeOrbit k (negativeStep d)

def evenCount : Nat → Nat → Nat
  | 0,_ => 0
  | k+1,d => (if d % 2 = 0 then 1 else 0) + evenCount k (negativeStep d)

theorem negativeStep_positive {d : Nat} (positive : 0<d) :
    0<negativeStep d := by
  unfold negativeStep
  split <;> omega

theorem negativeOrbit_positive (k : Nat) {d : Nat} (positive : 0<d) :
    0<negativeOrbit k d := by
  induction k generalizing d with
  | zero => exact positive
  | succ k ih => exact ih (negativeStep_positive positive)

theorem evenCount_le (k d : Nat) : evenCount k d≤k := by
  induction k generalizing d with
  | zero => simp [evenCount]
  | succ k ih =>
    have bound := ih (negativeStep d)
    simp only [evenCount]
    split <;> omega

theorem negativeOrbit_add (a b d : Nat) :
    negativeOrbit (a+b) d=negativeOrbit b (negativeOrbit a d) := by
  induction a generalizing d with
  | zero => simp [negativeOrbit]
  | succ a ih => simpa only [Nat.succ_add,negativeOrbit] using ih (negativeStep d)

theorem evenCount_add (a b d : Nat) :
    evenCount (a+b) d=evenCount a d+evenCount b (negativeOrbit a d) := by
  induction a generalizing d with
  | zero => simp [evenCount,negativeOrbit]
  | succ a ih =>
    simp only [Nat.succ_add,evenCount,negativeOrbit,ih]
    omega

theorem complement_step {y d z : Nat} (positive : 0<d) (sum : y+d=2*z) :
    step y+negativeStep d=if d%2=0 then z else 3*z := by
  by_cases parity : d%2=0
  · have other : y%2=0 := by omega
    simp only [step,negativeStep,ite_eq_left parity,ite_eq_left other]
    omega
  · have other : y%2≠0 := by omega
    simp only [step,negativeStep,ite_eq_right parity,ite_eq_right other]
    omega

/-- Exact physical lift: target and positive complement have the same parity
while their sum contains the remaining power of two. -/
theorem complement_lift (k y d z : Nat) (positive : 0<d)
    (sum : y+d=2^k*z) :
    orbit k y+negativeOrbit k d=3^(k-evenCount k d)*z := by
  induction k generalizing y d z with
  | zero => simpa [orbit,negativeOrbit,evenCount] using sum
  | succ k ih =>
    have splitSum : y+d=2*(2^k*z) := by
      rw [pow_succ] at sum
      nlinarith [sum]
    have first := complement_step positive splitSum
    have nextPositive := negativeStep_positive positive
    have bound := evenCount_le k (negativeStep d)
    by_cases parity : d%2=0
    · simp only [ite_eq_left parity] at first
      have result := ih (step y) (negativeStep d) z nextPositive first
      simpa only [orbit,negativeOrbit,evenCount,ite_eq_left parity,
        show k+1-(1+evenCount k (negativeStep d))=
          k-evenCount k (negativeStep d) by omega] using result
    · simp only [ite_eq_right parity] at first
      have first' : step y+negativeStep d=2^k*(3*z) := by nlinarith [first]
      have result := ih (step y) (negativeStep d) (3*z) nextPositive first'
      simpa only [orbit,negativeOrbit,evenCount,ite_eq_right parity,Nat.zero_add,
        show k+1-evenCount k (negativeStep d)=
          (k-evenCount k (negativeStep d))+1 by omega,pow_succ,mul_assoc] using result

private theorem negativeStep_odd (v : Nat) : negativeStep (2*v+1)=3*v+1 := by
  unfold negativeStep
  have parity : (2*v+1)%2≠0 := by omega
  rw [ite_eq_right parity]
  omega

/-- The entire odd segment of the auxiliary machine is explicit. -/
theorem negative_odd_run (k v : Nat) :
    negativeOrbit k (2^k*v+1)=3^k*v+1 ∧ evenCount k (2^k*v+1)=0 := by
  induction k generalizing v with
  | zero => simp [negativeOrbit,evenCount]
  | succ k ih =>
    have source : 2^(k+1)*v+1=2*(2^k*v)+1 := by rw [pow_succ]; ring
    have next : negativeStep (2^(k+1)*v+1)=2^k*(3*v)+1 := by
      rw [source,negativeStep_odd]
      ring
    have parity : (2^(k+1)*v+1)%2≠0 := by rw [source]; omega
    obtain ⟨path,count⟩ := ih (3*v)
    constructor
    · rw [negativeOrbit,next,path,pow_succ]
      ring
    · simp only [evenCount,ite_eq_right parity,Nat.zero_add,next,count]

/-- Every positive auxiliary value other than one reaches an even value
after finitely many odd steps; those steps never decrease its value. -/
theorem negative_even_block {d : Nat} (large : 2≤d) :
    ∃ k v, negativeOrbit k d=2*v ∧ evenCount k d=0 ∧ d≤2*v := by
  obtain ⟨k,u,odd,eq⟩ := Nat.exists_eq_two_pow_mul_odd (show d-1≠0 by omega)
  have source : d=2^k*u+1 := by omega
  obtain ⟨path,count⟩ := negative_odd_run k u
  have oddPower : Odd (3^k*u) := Odd.mul (Odd.pow (by decide : Odd (3:Nat))) odd
  obtain ⟨v,hv⟩ := oddPower
  have order : 2^k≤3^k := Nat.pow_le_pow_left (by decide) k
  refine ⟨k,v+1,?_,?_,?_⟩
  · rw [source,path]
    omega
  · rw [source]
    exact count
  · rw [source]
    nlinarith [Nat.mul_le_mul_right u order]

/-- A bounded halving budget always completes above the dyadic threshold.
This does not assert convergence of the negative shortcut. -/
theorem finite_even_budget (p : Nat) {d : Nat} (large : 2^p≤d) :
    ∃ k, evenCount k d=p := by
  induction p generalizing d with
  | zero => exact ⟨0,rfl⟩
  | succ p ih =>
    have large' : 2≤d := by
      have base : 0<2^p := by positivity
      rw [pow_succ] at large
      nlinarith [large]
    obtain ⟨a,v,path,count,growth⟩ := negative_even_block large'
    have vBound : 2^p≤v := by
      rw [pow_succ] at large
      omega
    obtain ⟨b,rest⟩ := ih vBound
    refine ⟨a+(b+1),?_⟩
    rw [evenCount_add,count,path,evenCount]
    have parity : (2*v)%2=0 := by omega
    have next : negativeStep (2*v)=v := by simp [negativeStep]
    simp only [ite_eq_left parity,next,rest,Nat.zero_add]
    omega

private theorem negative_even_block_bound {d L : Nat} (large : 2≤d)
    (small : d≤2^L) :
    ∃ k v, negativeOrbit k d=2*v ∧ evenCount k d=0 ∧ d≤2*v ∧
      k+1≤L ∧ v≤2^(2*L) := by
  obtain ⟨k,u,odd,eq⟩ := Nat.exists_eq_two_pow_mul_odd (show d-1≠0 by omega)
  have source : d=2^k*u+1 := by omega
  have uPositive : 0<u := by obtain ⟨w,hw⟩ := odd; omega
  have exponent : k<L := by
    apply (Nat.pow_lt_pow_iff_right (by decide : 1<2)).mp
    nlinarith [Nat.le_mul_of_pos_right (2^k) uPositive]
  obtain ⟨path,count⟩ := negative_odd_run k u
  have oddPower : Odd (3^k*u) := Odd.mul (Odd.pow (by decide : Odd (3:Nat))) odd
  obtain ⟨v,hv⟩ := oddPower
  have lower : 2^k≤3^k := Nat.pow_le_pow_left (by decide) k
  have upper : 3^k≤2^k*2^k := by
    have bound : 3^k≤4^k := Nat.pow_le_pow_left (by decide) k
    simpa only [show (4:Nat)=2*2 by decide,mul_pow] using bound
  have one : 1≤2^k := by
    have positive : 0<2^k := by positivity
    omega
  have endpointBound : 2*(v+1)≤2^k*d := by
    have sumBound := Nat.add_le_add (Nat.mul_le_mul_right u upper) one
    rw [source]
    nlinarith [sumBound]
  have kBound : 2^k≤2^L := pow_le_pow_right₀ (by decide) (by omega)
  have productBound := Nat.mul_le_mul kBound small
  have doublePower : 2^(2*L)=2^L*2^L := by
    rw [show 2*L=L+L by omega,pow_add]
  refine ⟨k,v+1,?_,?_,?_,by omega,?_⟩
  · rw [source,path]
    omega
  · rw [source]
    exact count
  · rw [source]
    nlinarith [Nat.mul_le_mul_right u lower]
  · rw [doublePower]
    omega

/-- A closed clock bound for the halving budget. It follows by doubling a
binary height bound after each odd block, with no orbit convergence premise. -/
theorem bounded_even_budget (p L : Nat) {d : Nat}
    (large : 2^p≤d) (small : d≤2^L) :
    ∃ k, evenCount k d=p ∧ k≤(2^p-1)*L := by
  induction p generalizing d L with
  | zero => exact ⟨0,rfl,by simp⟩
  | succ p ih =>
    have large' : 2≤d := by
      have base : 0<2^p := by positivity
      rw [pow_succ] at large
      nlinarith [large]
    obtain ⟨a,v,path,count,growth,clock,height⟩ := negative_even_block_bound large' small
    have vBound : 2^p≤v := by rw [pow_succ] at large; omega
    obtain ⟨b,rest,time⟩ := ih (2*L) vBound height
    refine ⟨a+(b+1),?_,?_⟩
    · rw [evenCount_add,count,path,evenCount]
      have parity : (2*v)%2=0 := by omega
      have next : negativeStep (2*v)=v := by simp [negativeStep]
      simp only [ite_eq_left parity,next,rest,Nat.zero_add]
      omega
    · have base : 0<2^p := by positivity
      have exponent : 2^(p+1)-1=2*(2^p-1)+1 := by rw [pow_succ]; omega
      rw [exponent]
      nlinarith [time,clock]

/-- The bounded-budget machine is total on every positive input. It stops
either on completing its budget or at the exceptional fixed value one. -/
theorem budget_or_one (p : Nat) {d : Nat} (positive : 0<d) :
    ∃ k, evenCount k d≤p ∧ (evenCount k d=p ∨ negativeOrbit k d=1) := by
  induction p generalizing d with
  | zero => exact ⟨0,by simp [evenCount],Or.inl rfl⟩
  | succ p ih =>
    by_cases one : d=1
    · exact ⟨0,by simp [evenCount],Or.inr one⟩
    · obtain ⟨a,v,path,count,growth⟩ := negative_even_block (by omega : 2≤d)
      have vp : 0<v := by omega
      obtain ⟨b,bound,stop⟩ := ih vp
      have parity : (2*v)%2=0 := by omega
      have next : negativeStep (2*v)=v := by simp [negativeStep]
      have counts : evenCount (a+(b+1)) d=1+evenCount b v := by
        rw [evenCount_add,count,path,evenCount]
        simp only [ite_eq_left parity,next,Nat.zero_add]
      have endpoint : negativeOrbit (a+(b+1)) d=negativeOrbit b v := by
        rw [negativeOrbit_add,path,negativeOrbit,next]
      refine ⟨a+(b+1),by omega,?_⟩
      rcases stop with stop|stop
      · exact Or.inl (by omega)
      · exact Or.inr (by rw [endpoint,stop])

theorem evenCount_mono {a b : Nat} (order : a≤b) (d : Nat) :
    evenCount a d≤evenCount b d := by
  obtain ⟨c,rfl⟩ := Nat.exists_eq_add_of_le order
  rw [evenCount_add]
  omega

/-- A completed complement budget pays the multiplier of an arbitrary
positive affine target. The clocks are actual ordinary shortcut clocks. -/
theorem paid_complement_bound {k p A d u y : Nat}
    (complementPositive : 0<d) (corePositive : 0<u)
    (source : y+d=2^k*(A*u))
    (multiplier : A≤3^p) (paid : p≤evenCount k d) :
    orbit k y≤orbit k (2^k*u-1) := by
  have countBound := evenCount_le k d
  have powerOrder : p+(k-evenCount k d)≤k := by omega
  have powerBound : 3^(p+(k-evenCount k d))≤3^k :=
    pow_le_pow_right₀ (by decide) powerOrder
  have lifted := complement_lift k y d (A*u) complementPositive source
  have upper : orbit k y+negativeOrbit k d≤3^k*u := by
    rw [lifted]
    calc
      3^(k-evenCount k d)*(A*u)≤3^(k-evenCount k d)*(3^p*u) := by
        exact Nat.mul_le_mul_left _ (Nat.mul_le_mul_right u multiplier)
      _ =3^(p+(k-evenCount k d))*u := by rw [pow_add]; ring
      _ ≤3^k*u := Nat.mul_le_mul_right u powerBound
  have negativePositive := negativeOrbit_positive k complementPositive
  rw [(odd_run k u corePositive).1]
  omega

/-- Every exponent and every nonnegative subtractive carry is resolved by a
sufficiently long actual source odd run. The stopping clock depends only on
the affine state, not on the high source parameter or its supplied tail. -/
theorem arbitrary_debt_reset (p c : Nat) :
    ∃ K, 0<K ∧ ∀ k, K≤k → ∀ u y, 0<u →
      y+c=3^p*(2^k*u-1) →
      orbit k y≤orbit k (2^k*u-1) := by
  have powerOrder : 2^p≤3^p := Nat.pow_le_pow_left (by decide) p
  obtain ⟨a,paid⟩ := finite_even_budget p (d := 3^p+c) (by omega)
  refine ⟨max 1 a,by omega,?_⟩
  intro k large u y corePositive target
  have paid' : p≤evenCount k (3^p+c) := by
    have monotone := evenCount_mono (show a≤k by omega) (3^p+c)
    omega
  have core : 0<2^k*u := by positivity
  have source : y+(3^p+c)=2^k*(3^p*u) := by
    have split : 2^k*u=(2^k*u-1)+1 := by omega
    calc
      y+(3^p+c)=3^p*(2^k*u-1)+3^p := by omega
      _ =3^p*((2^k*u-1)+1) := by ring
      _ =2^k*(3^p*u) := by rw [← split]; ring
  exact paid_complement_bound (by positivity) corePositive source (by rfl) paid'

/-- Explicit sufficient clock for the all-parameter debt reset. One may take
L to be the binary length of 3^p+c. -/
theorem explicit_debt_reset {p c L k u y : Nat}
    (height : 3^p+c≤2^L) (clock : (2^p-1)*L≤k)
    (corePositive : 0<u) (target : y+c=3^p*(2^k*u-1)) :
    orbit k y≤orbit k (2^k*u-1) := by
  have powerOrder : 2^p≤3^p := Nat.pow_le_pow_left (by decide) p
  obtain ⟨a,paid,time⟩ := bounded_even_budget p L (d := 3^p+c) (by omega) height
  have paid' : p≤evenCount k (3^p+c) := by
    have monotone := evenCount_mono (show a≤k by omega) (3^p+c)
    omega
  have core : 0<2^k*u := by positivity
  have source : y+(3^p+c)=2^k*(3^p*u) := by
    have split : 2^k*u=(2^k*u-1)+1 := by omega
    calc
      y+(3^p+c)=3^p*(2^k*u-1)+3^p := by omega
      _ =3^p*((2^k*u-1)+1) := by ring
      _ =2^k*(3^p*u) := by rw [← split]; ring
  exact paid_complement_bound (by positivity) corePositive source (by rfl) paid'

theorem one_prefix_grade_drop {k : Nat} (positive : 0<k) (tail : List Nat) :
    GradeDrop (sourceGrades 0 tail)
      (sourceGrades 0 (List.replicate k 1++tail)) := by
  refine ⟨2,?_,?_⟩
  · simpa [sourceGrades,List.map_append,List.count_append] using positive
  · intro b high
    have zero : (List.replicate k 2).count b=0 := by
      apply List.count_eq_zero.mpr
      intro mem
      have eq := (List.mem_replicate.mp mem).2
      omega
    simp [sourceGrades,List.map_append,List.count_append,zero]

private theorem positive_orbit (k : Nat) {n : Nat} (positive : 0<n) :
    0<orbit k n := by
  induction k generalizing n with
  | zero => exact positive
  | succ k ih =>
    apply ih
    unfold step
    split <;> omega

/-- The paid comparison consumes the literal all-one prefix and asks exactly
one lower-grade interval question on the original supplied suffix. -/
theorem paid_debt_interval_rule {p c k u y : Nat} (tail : List Nat)
    (clockPositive : 0<k) (corePositive : 0<u) (targetPositive : 0<y)
    (target : y+c=3^p*(2^k*u-1))
    (paid : p≤evenCount k (3^p+c))
    (cert : GapTrace (2^k*u-1) 1 (List.replicate k 1++tail))
    (ih : IntervalHyp (sourceGrades 0 (List.replicate k 1++tail))) : Basin y := by
  obtain ⟨q,front,rest⟩ :=
    (trace_append_iff (2^k*u-1) 1 (List.replicate k 1) tail).mp cert
  have sourcePath : orbit k (2^k*u-1)=q := by
    simpa using trace_orbit front
  have core : 0<2^k*u := by positivity
  have complement : y+(3^p+c)=2^k*(3^p*u) := by
    have split : 2^k*u=(2^k*u-1)+1 := by omega
    calc
      y+(3^p+c)=3^p*(2^k*u-1)+3^p := by omega
      _ =3^p*((2^k*u-1)+1) := by ring
      _ =2^k*(3^p*u) := by rw [← split]; ring
  have bound := paid_complement_bound (by positivity : 0<3^p+c)
    corePositive complement (by rfl : 3^p≤3^p) paid
  rw [sourcePath] at bound
  have childPositive := positive_orbit k targetPositive
  have qPositive : 0<q := by omega
  have supplied : PoweredTrace q 0 tail := ⟨q,qPositive,by simp,rest⟩
  have child := ih q (orbit k y) 0 tail ⟨childPositive,by omega⟩ supplied
    (one_prefix_grade_drop clockPositive tail)
  exact (basin_at_hit (x := y) (q := orbit k y) ⟨k,rfl⟩).mpr child

/-- Every actual supplied source gap has a legal signed-affine transition.
Unlike the old two-state language, this transition has no alphabet or debt
exponent cutoff. A terminal positive debt is retained as an obligation. -/
theorem gap_carry_transport {r u a p c y : Nat} (debt : 1≤p)
    (gap : 3*r+1=2^a*u) (target : y+c=3^p*r) :
    orbit a y+negativeOrbit a (c+3^(p-1))=
      3^((p-1)+(a-evenCount a (c+3^(p-1))))*u := by
  have power : 3^p=3^(p-1)*3 := by
    simpa only [show p-1+1=p by omega] using (pow_succ (3:Nat) (p-1))
  have sum : y+(c+3^(p-1))=2^a*(3^(p-1)*u) := by
    calc
      y+(c+3^(p-1))=3^p*r+3^(p-1) := by omega
      _ =3^(p-1)*(3*r+1) := by rw [power]; ring
      _ =2^a*(3^(p-1)*u) := by rw [gap]; ring
  have lift := complement_lift a y (c+3^(p-1)) (3^(p-1)*u)
    (by positivity) sum
  rw [lift,pow_add]
  ring

theorem negative_one (k : Nat) : negativeOrbit k 1=1 ∧ evenCount k 1=0 := by
  simpa only [mul_zero,Nat.zero_add] using negative_odd_run k 0

/-- A genuine remaining boundary: complement one never earns even credit.
The associated positive multiplier stays above the source for every odd-run
length. This prevents treating the budget machine as a universal dispatcher. -/
theorem unit_complement_overshoot {k A u y : Nat} (multiplier : 2≤A)
    (corePositive : 0<u) (source : y+1=2^k*(A*u)) :
    orbit k (2^k*u-1)<orbit k y := by
  have lift := complement_lift k y 1 (A*u) (by decide) source
  obtain ⟨fixed,count⟩ := negative_one k
  rw [fixed,count,Nat.sub_zero] at lift
  have core : 0<3^k*u := by positivity
  have growth : 3^k*u<3^k*(A*u) := by
    have factor : 3^k*(A*u)=A*(3^k*u) := by ring
    rw [factor]
    nlinarith
  rw [(odd_run k u corePositive).1]
  omega

#print axioms negativeStep_positive
#print axioms negativeOrbit_positive
#print axioms evenCount_le
#print axioms negativeOrbit_add
#print axioms evenCount_add
#print axioms complement_step
#print axioms complement_lift
#print axioms negative_odd_run
#print axioms negative_even_block
#print axioms finite_even_budget
#print axioms bounded_even_budget
#print axioms budget_or_one
#print axioms evenCount_mono
#print axioms paid_complement_bound
#print axioms arbitrary_debt_reset
#print axioms explicit_debt_reset
#print axioms one_prefix_grade_drop
#print axioms paid_debt_interval_rule
#print axioms gap_carry_transport
#print axioms negative_one
#print axioms unit_complement_overshoot

end CollatzShell.NegativeCarry
