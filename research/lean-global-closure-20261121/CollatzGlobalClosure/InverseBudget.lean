import CollatzGlobalClosure.EndpointSteering

/-!
# Exact inverse budgets and complete extraction of a ternary reserve

All statements concern actual finite ordinary shortcut Collatz trajectories.
They apply to every nonnegative source, with no convergence hypothesis.

The main theorem `extract_reserved_inverse` is a converse to the sufficient
reserved-rebasing construction in PR184. An inverse history whose odd count
fits the supplied ternary reserve automatically has a nonnegative shadow;
the shadow, its odd count and its endpoint are recovered constructively.

The exact quotient identity is stronger than the affine lower estimate:
`orbit t x / 3^(odds t x) = x / 2^t`.
-/

set_option autoImplicit false

namespace CollatzInverseBudget

open CollatzEndpointSteering

private theorem one_step_threshold (n v : Nat) :
    3^(n%2)*v ≤ step n ↔ 2*v ≤ n := by
  by_cases even : n%2=0
  · simp [step, even]
    omega
  · have odd : n%2=1 := by omega
    simp [step, odd]
    omega

/-- A finite Collatz prefix preserves every integral quotient threshold,
    after dividing its endpoint by its actual power of three and its source
    by its actual power of two. -/
theorem quotient_threshold (t x v : Nat) :
    3^(odds t x)*v ≤ orbit t x ↔ 2^t*v ≤ x := by
  induction t generalizing x v with
  | zero => simp [orbit, odds]
  | succ t ih =>
    simp only [orbit, odds, Nat.pow_add]
    rw [Nat.mul_assoc, ih]
    rw [show 2^t*(3^(x%2)*v)=3^(x%2)*(2^t*v) by ac_rfl]
    rw [one_step_threshold]
    congr 1
    grind [Nat.pow_succ]

/-- Exact equality of the normalized integral quotients. No additive-error
    estimate, asymptotic approximation, or prescribed parity word is used. -/
theorem normalized_quotient (t x : Nat) :
    orbit t x / 3^(odds t x) = x / 2^t := by
  have three : 0<3^(odds t x) := Nat.pow_pos (by decide)
  have two : 0<2^t := Nat.pow_pos (by decide)
  apply Nat.le_antisymm
  · apply (Nat.le_div_iff_mul_le two).mpr
    have low := Nat.div_mul_le_self (orbit t x) (3^(odds t x))
    rw [Nat.mul_comm] at low
    simpa [Nat.mul_comm] using (quotient_threshold t x _).mp low
  · apply (Nat.le_div_iff_mul_le three).mpr
    have low := Nat.div_mul_le_self x (2^t)
    rw [Nat.mul_comm] at low
    simpa [Nat.mul_comm] using (quotient_threshold t x _).mpr low

/-- Exact remaining horizon after any supplied ordinary ancestor prefix.
    The added binary length pays for its own clocks; each odd input also
    charges a factor of three against the original source budget. -/
theorem ancestor_horizon_exact (k h M n : Nat) (hit : orbit k M=n) :
    2^(k+h)≤M ↔ 3^(odds k M)*2^h≤n := by
  rw [Nat.pow_add,← quotient_threshold,hit]

/-- Ordinary ancestor padding cannot move a late meeting back inside its
    source's binary horizon. -/
theorem ancestor_padding_preserves_late (k h M n : Nat)
    (hit : orbit k M=n) (late : n<2^h) : M<2^(k+h) := by
  by_cases early : 2^(k+h)≤M
  · have bound := (ancestor_horizon_exact k h M n hit).mp early
    have one : 1≤3^(odds k M) := Nat.pow_pos (by decide)
    have product := Nat.mul_le_mul_right (2^h) one
    rw [Nat.one_mul] at product
    omega
  · omega

/-- The endpoint of a source below its binary prefix length is strictly
    below the corresponding actual power of three. -/
theorem short_source_iff_small_endpoint (t x : Nat) :
    x<2^t ↔ orbit t x<3^(odds t x) := by
  have threshold := quotient_threshold t x 1
  simp only [Nat.mul_one] at threshold
  omega

/-- Pulling back an integral endpoint block preserves nonnegativity and the
    entire actual binary word. The leading ternary exponent here is exactly
    the odd count of the supplied inverse history. -/
theorem extract_endpoint_block (t x w y : Nat)
    (hit : orbit t x=3^(odds t x)*w+y) :
    ∃ u, x=2^t*w+u ∧ odds t u=odds t x ∧ orbit t u=y := by
  have below : 3^(odds t x)*w≤orbit t x := by rw [hit]; omega
  have source : 2^t*w≤x := (quotient_threshold t x w).mp below
  let u := x-2^t*w
  have split : x=2^t*w+u := by dsimp [u]; omega
  have counts : odds t u=odds t x := by rw [split, odds_shift]
  have endpoint : orbit t u=y := by
    have lift := orbit_shift t u w
    rw [← split, counts, hit] at lift
    omega
  exact ⟨u,split,counts,endpoint⟩

/-- Every affordable actual inverse history has the exact nonnegative
    reserved form. This constructs the shadow instead of assuming it.

    The recovered shadow can be zero; the full source is positive whenever
    the reserved coefficient `v` is positive. -/
theorem extract_reserved_inverse (t x P v y : Nat)
    (hit : orbit t x=3^P*v+y) (budget : odds t x≤P) :
    ∃ u, x=2^t*3^(P-odds t x)*v+u ∧
      odds t u=odds t x ∧ orbit t u=y := by
  let a := odds t x
  let w := 3^(P-a)*v
  have ternary : 3^a*w=3^P*v := by
    dsimp [w]
    rw [← Nat.mul_assoc, ← Nat.pow_add, Nat.add_sub_of_le budget]
  have block : orbit t x=3^(odds t x)*w+y := by
    change orbit t x=3^a*w+y
    rw [ternary,hit]
  obtain ⟨u,split,counts,endpoint⟩ := extract_endpoint_block t x w y block
  refine ⟨u,?_,counts,endpoint⟩
  simpa [w,a,Nat.mul_assoc] using split

/-- The retained source coefficient after consuming an arbitrary odd count.
    When `a≤P` this is the previous reserved coefficient. When `P<a`, the
    exhausted ternary digits are carried into the shadow endpoint. -/
def retainedCoefficient (P v a : Nat) : Nat :=
  3^(P-a)*(v/3^(a-P))

def carriedEndpoint (P v y a : Nat) : Nat :=
  3^P*(v%3^(a-P))+y

theorem carry_partition (P v y a : Nat) :
    3^P*v+y=3^a*retainedCoefficient P v a+carriedEndpoint P v y a := by
  have exponent : a+(P-a)=P+(a-P) := by omega
  have powers : 3^a*3^(P-a)=3^P*3^(a-P) := by
    rw [← Nat.pow_add,← Nat.pow_add,exponent]
  have division := Nat.mod_add_div v (3^(a-P))
  unfold retainedCoefficient carriedEndpoint
  rw [← Nat.mul_assoc,powers]
  calc 3^P*v+y = 3^P*(v%3^(a-P)+3^(a-P)*(v/3^(a-P)))+y := by rw [division]
       _ = 3^P*3^(a-P)*(v/3^(a-P))+(3^P*(v%3^(a-P))+y) := by grind

/-- Complete continuation across an exhausted odd-count reserve. No upper
    bound on the new history's odd count or clock is required. The exact
    ternary remainder is retained instead of silently discarded. -/
theorem extract_inverse_with_carry (t x P v y : Nat)
    (hit : orbit t x=3^P*v+y) :
    ∃ u, x=2^t*retainedCoefficient P v (odds t x)+u ∧
      odds t u=odds t x ∧
      orbit t u=carriedEndpoint P v y (odds t x) := by
  apply extract_endpoint_block
  rw [hit,carry_partition]

theorem carry_below_budget (P v y a : Nat) (budget : a≤P) :
    retainedCoefficient P v a=3^(P-a)*v ∧ carriedEndpoint P v y a=y := by
  simp [retainedCoefficient,carriedEndpoint,Nat.sub_eq_zero_of_le budget,Nat.mod_one]

theorem carry_above_budget (P v y a : Nat) (exhausted : P≤a) :
    retainedCoefficient P v a=v/3^(a-P) ∧
      carriedEndpoint P v y a=3^P*(v%3^(a-P))+y := by
  simp [retainedCoefficient,carriedEndpoint,Nat.sub_eq_zero_of_le exhausted]

/-- Once the original shadow is a genuine ternary remainder, crossing the
    reserve produces another genuine remainder for the larger odd count. -/
theorem carried_endpoint_lt (P v y a : Nat)
    (exhausted : P≤a) (remainder : y<3^P) :
    carriedEndpoint P v y a<3^a := by
  have modulus : 0<3^(a-P) := Nat.pow_pos (by decide)
  have rem := Nat.mod_lt v modulus
  have power : 3^P*3^(a-P)=3^a := by
    rw [← Nat.pow_add,Nat.add_sub_of_le exhausted]
  have high : 3^P*(v%3^(a-P)+1)≤3^a := by
    rw [← power]
    exact Nat.mul_le_mul_left _ (by omega)
  unfold carriedEndpoint
  have strict : 3^P*(v%3^(a-P))+y<3^P*(v%3^(a-P)+1) := by
    rw [Nat.mul_add,Nat.mul_one]
    exact Nat.add_lt_add_left remainder _
  exact Nat.lt_of_lt_of_le strict high

/-- Above the old odd-count budget, the extracted shadow is precisely the
    low binary word of the actual smaller history. -/
theorem extract_inverse_with_canonical_carry (t x P v y : Nat)
    (hit : orbit t x=3^P*v+y) (exhausted : P≤odds t x)
    (remainder : y<3^P) :
    x=2^t*(v/3^(odds t x-P))+x%2^t ∧
      odds t (x%2^t)=odds t x ∧
      orbit t (x%2^t)=carriedEndpoint P v y (odds t x) := by
  obtain ⟨u,source,count,endpoint⟩ := extract_inverse_with_carry t x P v y hit
  have small : u<2^t := by
    apply (short_source_iff_small_endpoint t u).mpr
    rw [count,endpoint]
    exact carried_endpoint_lt P v y (odds t x) exhausted remainder
  have canonical : x%2^t=u := by
    rw [source]
    simp [Nat.add_mod,Nat.mul_mod_right,Nat.mod_eq_of_lt small]
  rw [← canonical] at source count endpoint
  rw [(carry_above_budget P v y (odds t x) exhausted).1] at source
  exact ⟨source,count,endpoint⟩

/-- Even after the old budget is exceeded, a nonzero retained coefficient
    still gives the same finite binary clock bound. -/
theorem retained_coefficient_clock (t x P v y : Nat)
    (hit : orbit t x=3^P*v+y)
    (retained : 0<retainedCoefficient P v (odds t x)) : 2^t≤x := by
  obtain ⟨u,source,_,_⟩ := extract_inverse_with_carry t x P v y hit
  have low := Nat.mul_le_mul_left (2^t) (show 1≤retainedCoefficient P v (odds t x) by omega)
  rw [Nat.mul_one] at low
  omega

/-- The carry mechanism can retain high source information beyond the old
    reserve whenever the remaining quotient has enough ternary magnitude.
    Divisibility of `v` by this power of three is not required. -/
theorem retained_coefficient_positive_iff (P v a : Nat) :
    0<retainedCoefficient P v a ↔ 3^(a-P)≤v := by
  have power : 0<3^(P-a) := Nat.pow_pos (by decide)
  have modulus : 0<3^(a-P) := Nat.pow_pos (by decide)
  unfold retainedCoefficient
  constructor
  · intro positive
    have quotient : 0<v/3^(a-P) := by
      by_cases vanish : v/3^(a-P)=0
      · rw [vanish,Nat.mul_zero] at positive
        omega
      · exact Nat.pos_of_ne_zero vanish
    have product := Nat.mul_le_mul_left (3^(a-P)) (show 1≤v/3^(a-P) by omega)
    have below := Nat.div_mul_le_self v (3^(a-P))
    rw [Nat.mul_one] at product
    rw [Nat.mul_comm] at below
    exact Nat.le_trans product below
  · intro enough
    have divrem := Nat.mod_add_div v (3^(a-P))
    have rem := Nat.mod_lt v modulus
    have quotient : 0<v/3^(a-P) := by
      by_cases vanish : v/3^(a-P)=0
      · rw [vanish,Nat.mul_zero,Nat.add_zero] at divrem
        omega
      · exact Nat.pos_of_ne_zero vanish
    exact Nat.mul_pos power quotient

/-- Reconstruction using an arbitrary shadow word, including a word that
    consumes more odd steps than the old reserve. -/
def carriedRebase (P v u t : Nat) : Nat :=
  2^t*retainedCoefficient P v (odds t u)+u

theorem carried_rebase_hits (P v y u t : Nat)
    (shadow : orbit t u=carriedEndpoint P v y (odds t u)) :
    orbit t (carriedRebase P v u t)=3^P*v+y := by
  unfold carriedRebase
  rw [orbit_shift,shadow]
  exact (carry_partition P v y (odds t u)).symm

/-- The carried grammar describes every actual inverse history. There is no
    missing high-odd-count branch and no assumed terminal certificate. -/
theorem complete_carried_rebase (t x P v y : Nat) :
    orbit t x=3^P*v+y ↔
      ∃ u, x=carriedRebase P v u t ∧
        orbit t u=carriedEndpoint P v y (odds t u) := by
  constructor
  · intro hit
    obtain ⟨u,source,count,endpoint⟩ := extract_inverse_with_carry t x P v y hit
    refine ⟨u,?_,?_⟩
    · simpa [carriedRebase,count] using source
    · simpa [count] using endpoint
  · rintro ⟨u,source,shadow⟩
    rw [source]
    exact carried_rebase_hits P v y u t shadow

/-- A history longer than the smaller source's binary horizon has consumed
    the complete retained coefficient, even in the unrestricted carry grammar.
    Its endpoint shadow is then the original full endpoint. -/
theorem long_inverse_exhausts_carry (t x P v y B : Nat)
    (hit : orbit t x=3^P*v+y) (smaller : x<B)
    (long : (B-1).log2<t) :
    retainedCoefficient P v (odds t x)=0 ∧
      carriedEndpoint P v y (odds t x)=3^P*v+y := by
  have zero : retainedCoefficient P v (odds t x)=0 := by
    by_cases zero : retainedCoefficient P v (odds t x)=0
    · exact zero
    have retained : 0<retainedCoefficient P v (odds t x) := by omega
    have power := retained_coefficient_clock t x P v y hit retained
    have lower : 2^t≤B-1 := by omega
    have positive : 0<B-1 := Nat.lt_of_lt_of_le (Nat.pow_pos (by decide)) lower
    have bound : t≤(B-1).log2 := (Nat.le_log2 (Nat.ne_of_gt positive)).mpr lower
    omega
  refine ⟨zero,?_⟩
  have partition := carry_partition P v y (odds t x)
  rw [zero,Nat.mul_zero,Nat.zero_add] at partition
  exact partition.symm

/-- The extracted shadow is unique because its leading coefficient is fixed
    by the actual inverse history's odd count. -/
theorem reserved_shadow_unique (t x P v u u' : Nat)
    (first : x=2^t*3^(P-odds t x)*v+u)
    (second : x=2^t*3^(P-odds t x)*v+u') : u=u' := by
  omega

/-- Exact converse and forward direction in one statement. The count in the
    reconstruction is the actual count of the supplied source `x`. -/
theorem reserved_inverse_iff (t x P v y : Nat) (budget : odds t x≤P) :
    orbit t x=3^P*v+y ↔
      ∃ u, x=2^t*3^(P-odds t x)*v+u ∧
        odds t u=odds t x ∧ orbit t u=y := by
  constructor
  · intro hit
    exact extract_reserved_inverse t x P v y hit budget
  · rintro ⟨u,source,count,endpoint⟩
    have ternary : 3^(odds t x)*3^(P-odds t x)=3^P := by
      rw [← Nat.pow_add, Nat.add_sub_of_le budget]
    have source' : x=2^t*(3^(P-odds t x)*v)+u := by
      simpa only [Nat.mul_assoc] using source
    calc orbit t x = orbit t (2^t*(3^(P-odds t x)*v)+u) := congrArg (orbit t) source'
         _ = 3^(odds t u)*(3^(P-odds t x)*v)+orbit t u := orbit_shift t u _
         _ = 3^P*v+y := by rw [count,endpoint,← Nat.mul_assoc,ternary]

/-- Positive reserve forces the inverse clock below the binary size of its
    source. This is a completeness bound, not an externally chosen search cap. -/
theorem affordable_inverse_clock (t x P v y : Nat)
    (positive : 0<v) (hit : orbit t x=3^P*v+y)
    (budget : odds t x≤P) : 2^t≤x := by
  obtain ⟨u,source,_,_⟩ := extract_reserved_inverse t x P v y hit budget
  have coefficient : 1≤3^(P-odds t x)*v := Nat.mul_pos (Nat.pow_pos (by decide)) positive
  have bound := Nat.mul_le_mul_left (2^t) coefficient
  rw [Nat.mul_one] at bound
  rw [source]
  simpa [Nat.mul_assoc] using Nat.le_trans bound (Nat.le_add_right _ u)

theorem affordable_inverse_clock_log (t x P v y : Nat)
    (positive : 0<v) (hit : orbit t x=3^P*v+y)
    (budget : odds t x≤P) : t≤x.log2 := by
  have bound := affordable_inverse_clock t x P v y positive hit budget
  have xp : 0<x := Nat.lt_of_lt_of_le (Nat.pow_pos (by decide)) bound
  exact (Nat.le_log2 (Nat.ne_of_gt xp)).mpr bound

/-- If the affordable inverse tree contains a partner below `B`, the complete
    tree is finite through `floor(log2(B-1))`. -/
theorem smaller_affordable_inverse_clock (t x P v y B : Nat)
    (positive : 0<v) (hit : orbit t x=3^P*v+y)
    (budget : odds t x≤P) (smaller : x<B) : t≤(B-1).log2 := by
  have bound := affordable_inverse_clock t x P v y positive hit budget
  have lower : 2^t≤B-1 := by omega
  have bp : 0<B-1 := Nat.lt_of_lt_of_le (Nat.pow_pos (by decide)) lower
  exact (Nat.le_log2 (Nat.ne_of_gt bp)).mpr lower

/-- Any smaller inverse history longer than the intrinsic finite bound must
    exceed the available ternary odd-count reserve. -/
theorem long_smaller_inverse_exceeds_budget (t x P v y B : Nat)
    (positive : 0<v) (hit : orbit t x=3^P*v+y)
    (smaller : x<B) (long : (B-1).log2<t) : P<odds t x := by
  by_cases more : P<odds t x
  · exact more
  · have budget : odds t x≤P := by omega
    have bound := smaller_affordable_inverse_clock t x P v y B positive hit budget smaller
    omega

end CollatzInverseBudget

#print axioms CollatzInverseBudget.quotient_threshold
#print axioms CollatzInverseBudget.normalized_quotient
#print axioms CollatzInverseBudget.ancestor_horizon_exact
#print axioms CollatzInverseBudget.ancestor_padding_preserves_late
#print axioms CollatzInverseBudget.short_source_iff_small_endpoint
#print axioms CollatzInverseBudget.extract_endpoint_block
#print axioms CollatzInverseBudget.extract_reserved_inverse
#print axioms CollatzInverseBudget.carry_partition
#print axioms CollatzInverseBudget.extract_inverse_with_carry
#print axioms CollatzInverseBudget.carried_endpoint_lt
#print axioms CollatzInverseBudget.extract_inverse_with_canonical_carry
#print axioms CollatzInverseBudget.retained_coefficient_clock
#print axioms CollatzInverseBudget.retained_coefficient_positive_iff
#print axioms CollatzInverseBudget.carried_rebase_hits
#print axioms CollatzInverseBudget.complete_carried_rebase
#print axioms CollatzInverseBudget.long_inverse_exhausts_carry
#print axioms CollatzInverseBudget.reserved_shadow_unique
#print axioms CollatzInverseBudget.reserved_inverse_iff
#print axioms CollatzInverseBudget.affordable_inverse_clock
#print axioms CollatzInverseBudget.affordable_inverse_clock_log
#print axioms CollatzInverseBudget.smaller_affordable_inverse_clock
#print axioms CollatzInverseBudget.long_smaller_inverse_exceeds_budget
