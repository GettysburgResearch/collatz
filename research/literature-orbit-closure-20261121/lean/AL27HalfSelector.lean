module

public import ResidualPrefixErasure

@[expose] public section

/-!
# A variable-clock physical partner selector on half of the AL27 branch

For every k,t≥0 an explicit CRT selector produces a source n≡27 mod128 and
partner x with16*x+3=9*n. Their ordinary paths merge at source clockk+9 and
partner clockk+5. The original source does not descend through its entire
merger clock. The selected disjoint progressions have relative density1/2
inside the AL27 branch; this is partial coverage, not a proof for the branch.
-/

namespace CollatzShell.AL27HalfSelector

/-- CRT idempotents modulo9 and4 are28 and9. -/
def phaseSeed (k : Nat) : Nat := (28*2^(5*k+1)+9*3^k)%36
def oddParameter (k t : Nat) : Nat := phaseSeed k+36*t
def sourceQuotient (k t : Nat) : Nat := 2^k*oddParameter k t/9
def seed (k t : Nat) : Nat := 128*sourceQuotient k t+27
def partner (k t : Nat) : Nat := 2^(k+3)*oddParameter k t-1

private theorem phase_mod9 (k t : Nat) :
    oddParameter k t%9=2^(5*k+1)%9 := by
  have raw : phaseSeed k%9=2^(5*k+1)%9 := by
    unfold phaseSeed
    rw [Nat.mod_mod_of_dvd _ (by decide : 9∣36),Nat.add_mod,
      Nat.mul_mod 28 _,Nat.mul_mod 9 _]
    norm_num
  unfold oddParameter
  omega

private theorem phase_mod4 (k t : Nat) : oddParameter k t%4=3^k%4 := by
  have raw : phaseSeed k%4=3^k%4 := by
    unfold phaseSeed
    rw [Nat.mod_mod_of_dvd _ (by decide : 4∣36),Nat.add_mod,
      Nat.mul_mod 28 _,Nat.mul_mod 9 _]
    norm_num
  unfold oddParameter
  omega

private theorem binary_carry (k t : Nat) :
    (2^k*oddParameter k t)%9=2 := by
  have period : 2^6%9=1 := by decide
  rw [Nat.mul_mod,phase_mod9,← Nat.mul_mod,← pow_add,
    show k+(5*k+1)=6*k+1 by omega,pow_add,pow_mul,Nat.mul_mod,
    Nat.pow_mod,period]
  simp

private theorem parameter_positive (k t : Nat) : 0<oddParameter k t := by
  have carry := binary_carry k t
  by_contra fail
  have zero : oddParameter k t=0 := by omega
  simp only [zero,Nat.mul_zero,Nat.zero_mod] at carry
  omega

/-- Exact source arithmetic, with no division remainder hypothesis left open. -/
theorem source_endpoint (k t : Nat) :
    9*sourceQuotient k t+2=2^k*oddParameter k t := by
  have remainder := binary_carry k t
  have division := Nat.mod_add_div (2^k*oddParameter k t) 9
  unfold sourceQuotient
  omega

/-- The short endpoint diamond is admissible for every selected parameter. -/
theorem endpoint_phase (k t : Nat) :
    (3^(k+3)*oddParameter k t)%4=3 := by
  rw [Nat.mul_mod,phase_mod4,← Nat.mul_mod,← pow_add,
    show k+3+k=2*k+3 by omega,pow_add,pow_mul,Nat.mul_mod,Nat.pow_mod]
  norm_num

/-- Thus k is the exact valuation of9*z+2, making the k-progressions disjoint. -/
theorem parameter_odd (k t : Nat) : oddParameter k t%2=1 := by
  have reduced := congrArg (fun n : Nat => n%2) (phase_mod4 k t)
  rw [Nat.mod_mod_of_dvd _ (by decide : 2∣4),
    Nat.mod_mod_of_dvd _ (by decide : 2∣4),Nat.pow_mod] at reduced
  simpa using reduced

theorem source_residue (k t : Nat) : seed k t%128=27 := by
  unfold seed
  omega

/-- A complete binary progression, with no missing small exceptions. -/
theorem source_progression (k t : Nat) :
    seed k t=seed k 0+2^(k+9)*t := by
  have a := source_endpoint k t
  have b := source_endpoint k 0
  have quotient : sourceQuotient k t=sourceQuotient k 0+4*2^k*t := by
    unfold oddParameter at a b
    nlinarith only [a,b]
  unfold seed
  rw [quotient,pow_add]
  ring

theorem source_base_bounds (k : Nat) : 0<seed k 0 ∧ seed k 0<2^(k+9) := by
  have base : phaseSeed k<36 := Nat.mod_lt _ (by decide)
  have p : 0<2^k := by positivity
  have bound := Nat.mul_lt_mul_of_pos_left base p
  have endpoint := source_endpoint k 0
  unfold oddParameter at endpoint
  unfold seed
  rw [pow_add]
  constructor
  · omega
  · norm_num only [Nat.reducePow]
    nlinarith only [endpoint,bound]

private theorem three_step_prefix (z : Nat) : orbit 3 (128*z+27)=144*z+31 := by
  have he (x : Nat) (h : x%2=0) : step x=x/2 := by simp [step,h]
  have ho (x : Nat) (h : x%2≠0) : step x=(3*x+1)/2 := by simp [step,h]
  have e0 : step (128*z+27)=192*z+41 := by rw [ho _ (by omega)]; omega
  have e1 : step (192*z+41)=288*z+62 := by rw [ho _ (by omega)]; omega
  have e2 : step (288*z+62)=144*z+31 := by rw [he _ (by omega)]; omega
  simp only [orbit,e0,e1,e2]

private theorem at_prefix (k t : Nat) :
    orbit 3 (seed k t)=2^(k+4)*oddParameter k t-1 := by
  have endpoint := source_endpoint k t
  have raw : 144*sourceQuotient k t+32=2^k*16*oddParameter k t := by
    nlinarith only [endpoint]
  unfold seed
  rw [three_step_prefix,pow_add]
  norm_num only [Nat.reducePow]
  omega

/-- Positive strictly smaller source with an actual ordinary common future. -/
theorem physical_merger (k t : Nat) :
    0<partner k t ∧ partner k t<seed k t ∧16*partner k t+3=9*seed k t ∧
      orbit (k+5) (partner k t)=orbit (k+9) (seed k t) := by
  have phase : (3^((k+4)-1)*oddParameter k t)%4=3 := by
    simpa only [show k+4-1=k+3 by omega] using endpoint_phase k t
  obtain ⟨positive,scale,_,merge⟩ := rising_half_source_partner (k+4)
    (oddParameter k t) (by omega) (parameter_positive k t) phase
  have prefix_relation : 8*orbit 3 (seed k t)=9*seed k t+5 := by
    unfold seed
    rw [three_step_prefix]
    ring
  rw [at_prefix] at prefix_relation
  have relation : 16*partner k t+3=9*seed k t := by
    rw [show k+4-1=k+3 by omega] at scale
    unfold partner
    omega
  have positive' : 0<partner k t := by
    simpa only [partner,show k+4-1=k+3 by omega] using positive
  refine ⟨positive',by omega,relation,?_⟩
  rw [show k+9=3+(k+6) by omega,orbit_add 3 (k+6),at_prefix]
  simpa only [partner,show k+4-1=k+3 by omega,
    show k+4+1=k+5 by omega,show k+4+2=k+6 by omega] using merge

private theorem two_halving_minimum (a i : Nat) (hi : i≤2) : a≤orbit i (4*a) := by
  have e0 : step (4*a)=2*a := by unfold step; split <;> omega
  have e1 : step (2*a)=a := by unfold step; split <;> omega
  interval_cases i <;> simp only [orbit,e0,e1] <;> omega

/-- This family never descends before or at its displayed common endpoint.
The merger therefore gives a lower source before direct descent is available. -/
theorem no_direct_descent_through_merger (k t i : Nat) (hi : i≤k+9) :
    seed k t≤orbit i (seed k t) := by
  have hu := parameter_positive k t
  have first : seed k t≤orbit 3 (seed k t) :=
    ResidualPrefixErasure.prefix27_initial_growth (sourceQuotient k t) 3 (by decide)
  have before_run (j : Nat) (hj : j≤k+7) : seed k t≤orbit j (seed k t) := by
    by_cases early : j≤3
    · exact ResidualPrefixErasure.prefix27_initial_growth (sourceQuotient k t) j (by omega)
    · have growth := (odd_run (k+4) (oddParameter k t) hu).2 (j-3) (by omega)
      have start := first
      rw [at_prefix] at start
      rw [show j=3+(j-3) by omega,orbit_add 3 (j-3),at_prefix]
      exact start.trans growth
  by_cases early : i≤k+7
  · exact before_run i early
  · have atRun : orbit (k+7) (seed k t)=3^(k+4)*oddParameter k t-1 := by
      rw [show k+7=3+(k+4) by omega,orbit_add 3 (k+4),at_prefix,
        (odd_run (k+4) (oddParameter k t) hu).1]
    have endpoint := source_endpoint k t
    have source_eq : 9*seed k t+13=128*2^k*oddParameter k t := by
      unfold seed
      nlinarith only [endpoint]
    have margin : 512*2^k≤729*3^k := Nat.mul_le_mul (by decide)
      (Nat.pow_le_pow_left (by decide : 2≤3) k)
    have scaled := Nat.mul_le_mul_right (oddParameter k t) margin
    have lower : 4*seed k t+1≤3^(k+4)*oddParameter k t := by
      rw [pow_add]
      norm_num only [Nat.reducePow]
      nlinarith only [source_eq,scaled]
    have phase := endpoint_phase k t
    have eq : 3^(k+4)*oddParameter k t=3*(3^(k+3)*oddParameter k t) := by
      rw [show k+4=(k+3)+1 by omega,pow_succ]
      ring
    have phase_mod : (3^(k+4)*oddParameter k t)%4=1 := by
      rw [eq,Nat.mul_mod,phase]
    have form : 3^(k+4)*oddParameter k t-1=
        4*((3^(k+4)*oddParameter k t)/4) := by omega
    have minimum : seed k t≤(3^(k+4)*oddParameter k t)/4 := by omega
    rw [show i=(k+7)+(i-(k+7)) by omega,orbit_add (k+7) (i-(k+7)),atRun,form]
    exact minimum.trans (two_halving_minimum _ _ (by omega))

/-- Correct smaller-source induction use; family membership of the partner
is not assumed. -/
theorem basin_by_smaller_induction (k t : Nat)
    (ih : ∀ x, 0<x → x<seed k t → Basin x) : Basin (seed k t) := by
  obtain ⟨positive,smaller,_,merge⟩ := physical_merger k t
  have bx := ih _ positive smaller
  have same : Basin (partner k t) ↔ Basin (seed k t) := by
    apply (basin_at_hit (x := partner k t)
      (q := orbit (k+5) (partner k t)) ⟨_,rfl⟩).trans
    apply Iff.symm
    exact basin_at_hit (x := seed k t)
      (q := orbit (k+5) (partner k t)) ⟨_,merge.symm⟩
  exact same.mp bx

#print axioms source_endpoint
#print axioms endpoint_phase
#print axioms parameter_odd
#print axioms source_residue
#print axioms source_progression
#print axioms source_base_bounds
#print axioms physical_merger
#print axioms no_direct_descent_through_merger
#print axioms basin_by_smaller_induction

end CollatzShell.AL27HalfSelector
