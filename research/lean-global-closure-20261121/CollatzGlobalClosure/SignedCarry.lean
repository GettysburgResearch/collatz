import CollatzGlobalClosure.EndpointSteering
import Collatz.GapMultiset

/-!
Exact signed carry transport for arbitrary supplied complete source words.
The negative shortcut is only an arithmetic parity scaffold. Every target
orbit in the main transport theorem is an ordinary nonnegative integer orbit.
No stopping or convergence assumption for negative integers is made.
-/

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzSignedCarry

open CollatzEndpointSteering
open CollatzWitness CollatzGapMultiset

def signedStep (n : Int) : Int :=
  if n % 2 = 0 then n / 2 else (3*n+1)/2

def negativeStep (z : Int) : Int :=
  if z % 2 = 0 then z / 2 else (3*z-1)/2

def signedOrbit : Nat → Int → Int
  | 0, n => n
  | k+1, n => signedOrbit k (signedStep n)

def signedOdds : Nat → Int → Nat
  | 0, _ => 0
  | k+1, n => signedOdds k (signedStep n) + if n%2=0 then 0 else 1

def negativeOrbit : Nat → Int → Int
  | 0, z => z
  | k+1, z => negativeOrbit k (negativeStep z)

def negativeOdds : Nat → Int → Nat
  | 0, _ => 0
  | k+1, z => negativeOdds k (negativeStep z) + if z%2=0 then 0 else 1

theorem signedStep_nat (n : Nat) : signedStep (n : Int) = (step n : Int) := by
  unfold signedStep step
  split <;> split <;> omega

theorem signedOrbit_nat (k n : Nat) : signedOrbit k (n : Int) = (orbit k n : Int) := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    simp only [signedOrbit,orbit,signedStep_nat,ih]

theorem signedOdds_nat (k n : Nat) : signedOdds k (n : Int) = odds k n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    simp only [signedOdds,odds,signedStep_nat,ih]
    split <;> omega

theorem one_step_complement (v z : Int) :
    signedStep (2*v-z) + negativeStep z =
      (3 : Int)^(if z%2=0 then 0 else 1) * v := by
  unfold signedStep negativeStep
  by_cases even : z%2=0
  · have other : (2*v-z)%2=0 := by omega
    simp only [even,other,ite_true,Int.pow_zero,Int.one_mul]
    omega
  · have other : ¬(2*v-z)%2=0 := by omega
    simp only [even,other,ite_false,Int.pow_one]
    omega

/-- Exact parity complement at every finite binary scale, with arbitrary
signed debt. There is no asymptotic estimate or prescribed illegal path. -/
theorem complement_transport (k : Nat) (v z : Int) :
    signedOrbit k ((2 : Int)^k*v-z) + negativeOrbit k z =
      (3 : Int)^negativeOdds k z * v := by
  induction k generalizing v z with
  | zero => simp [signedOrbit,negativeOrbit,negativeOdds]
  | succ k ih =>
    let b : Nat := if z%2=0 then 0 else 1
    have first := one_step_complement ((2 : Int)^k*v) z
    have form : signedStep ((2 : Int)^(k+1)*v-z) =
        (2 : Int)^k*((3 : Int)^b*v)-negativeStep z := by
      rw [Int.pow_succ]
      dsimp [b]
      grind
    simp only [signedOrbit,negativeOrbit,negativeOdds]
    rw [form,ih,Int.pow_add]
    dsimp [b]
    grind

/-- The scaffold reproduces the entire actual target parity count as well
as its endpoint. It is not a fresh or independently chosen parity law. -/
theorem complement_odds (k : Nat) (v z : Int) :
    signedOdds k ((2 : Int)^k*v-z) = negativeOdds k z := by
  induction k generalizing v z with
  | zero => rfl
  | succ k ih =>
    let b : Nat := if z%2=0 then 0 else 1
    have first := one_step_complement ((2 : Int)^k*v) z
    have form : signedStep ((2 : Int)^(k+1)*v-z) =
        (2 : Int)^k*((3 : Int)^b*v)-negativeStep z := by
      rw [Int.pow_succ]
      dsimp [b]
      grind
    have parity : ((2 : Int)^(k+1)*v-z)%2=0 ↔ z%2=0 := by
      rw [Int.pow_succ]
      have twice : (2 : Int)^k*2*v = 2*((2 : Int)^k*v) := by grind
      rw [twice]
      omega
    simp only [signedOdds,negativeOdds,form,ih,parity]

/-- The same identity for an actual ordinary source; the scaffold can be
negative, zero, or positive. -/
theorem ordinary_complement_transport (k n : Nat) (v z : Int)
    (source : (n : Int) = (2 : Int)^k*v-z) :
    (orbit k n : Int) + negativeOrbit k z =
      (3 : Int)^negativeOdds k z * v := by
  have h := complement_transport k v z
  rw [←source,signedOrbit_nat] at h
  exact h

theorem ordinary_complement_odds (k n : Nat) (v z : Int)
    (source : (n : Int) = (2 : Int)^k*v-z) :
    odds k n = negativeOdds k z := by
  have h := complement_odds k v z
  rw [←source,signedOdds_nat] at h
  exact h

/-- Any verified finite signed trajectory lifts to an actual ordinary
nonnegative binary ray, with both endpoint and entire odd count preserved.
This is a finite arithmetic statement, independent of negative convergence. -/
theorem finite_signed_lift (k n : Nat) (seed v : Int)
    (source : (n : Int) = (2 : Int)^k*v+seed) :
    (orbit k n : Int) = (3 : Int)^signedOdds k seed*v+signedOrbit k seed ∧
      odds k n=signedOdds k seed := by
  have origin := complement_transport k 0 (-seed)
  have originCount := complement_odds k 0 (-seed)
  simp only [Int.mul_zero,Int.zero_sub,Int.neg_neg] at origin originCount
  have form : (n : Int) = (2 : Int)^k*v-(-seed) := by omega
  have lifted := ordinary_complement_transport k n v (-seed) form
  have count := ordinary_complement_odds k n v (-seed) form
  rw [←originCount] at lifted count
  exact ⟨by omega,count⟩

/-- An actual source gap updates every affine carry, including negative debt.
In particular, `p=2,c=-2` is the new repository's carry `9*r+2`. -/
theorem source_gap_transport (a p r u n : Nat) (c : Int)
    (positive : 0<p) (gap : 3*r+1=2^a*u)
    (target : (n : Int) = (3 : Int)^p*r-c) :
    (orbit a n : Int) + negativeOrbit a ((3 : Int)^(p-1)+c) =
      (3 : Int)^(p-1+negativeOdds a ((3 : Int)^(p-1)+c))*u := by
  have exponent : p=(p-1)+1 := by omega
  have sourceGap : (3 : Int)*r+1=(2 : Int)^a*u := by exact_mod_cast gap
  have form : (n : Int) = (2 : Int)^a*((3 : Int)^(p-1)*u) -
      ((3 : Int)^(p-1)+c) := by
    rw [target,exponent,Int.pow_succ]
    grind
  have h := ordinary_complement_transport a n ((3 : Int)^(p-1)*u)
    ((3 : Int)^(p-1)+c) form
  rw [Int.pow_add]
  grind

theorem source_gap_odds (a p r u n : Nat) (c : Int)
    (positive : 0<p) (gap : 3*r+1=2^a*u)
    (target : (n : Int) = (3 : Int)^p*r-c) :
    odds a n = negativeOdds a ((3 : Int)^(p-1)+c) := by
  have exponent : p=(p-1)+1 := by omega
  have sourceGap : (3 : Int)*r+1=(2 : Int)^a*u := by exact_mod_cast gap
  have form : (n : Int) = (2 : Int)^a*((3 : Int)^(p-1)*u) -
      ((3 : Int)^(p-1)+c) := by
    rw [target,exponent,Int.pow_succ]
    grind
  exact ordinary_complement_odds a n _ _ form

structure Carry where
  power : Nat
  debt : Int
deriving DecidableEq, Repr

def advance (a : Nat) (s : Carry) : Carry :=
  let z := (3 : Int)^(s.power-1)+s.debt
  ⟨s.power-1+negativeOdds a z, negativeOrbit a z⟩

def run : Carry → List Nat → Carry
  | s, [] => s
  | s, a::word => run (advance a s) word

/-- The affine representation is valid while a power of three is available
to consume the actual source gap. The compiler stops if it reaches zero. -/
def Enabled : Carry → List Nat → Prop
  | _, [] => True
  | s, a::word => 0<s.power ∧ Enabled (advance a s) word

private def enabledDecision : (s : Carry) → (word : List Nat) → Decidable (Enabled s word)
  | _, [] => isTrue trivial
  | s, a::word =>
    haveI := enabledDecision (advance a s) word
    inferInstanceAs (Decidable (0<s.power ∧ Enabled (advance a s) word))

instance (s : Carry) (word : List Nat) : Decidable (Enabled s word) :=
  enabledDecision s word

theorem orbit_add (a b n : Nat) : orbit (a+b) n = orbit b (orbit a n) := by
  induction a generalizing n with
  | zero => simp [orbit]
  | succ a ih => simpa only [Nat.succ_add,orbit] using ih (step n)

theorem odds_add (a b n : Nat) : odds (a+b) n = odds a n+odds b (orbit a n) := by
  induction a generalizing n with
  | zero => simp [odds,orbit]
  | succ a ih =>
    simp only [Nat.succ_add,odds,orbit,ih]
    omega

/-- Every enabled word preserves the actual supplied complete suffix and
tracks the original ordinary target at the exact supplied source clock. -/
theorem complete_word_transport (s : Carry) (front tail : List Nat) (r n : Nat)
    (enabled : Enabled s front) (cert : Certificate r (front++tail))
    (target : (n : Int) = (3 : Int)^s.power*r-s.debt) :
    ∃ u, Certificate u tail ∧
      (orbit (total front) n : Int) =
        (3 : Int)^(run s front).power*u-(run s front).debt := by
  induction front generalizing s r n with
  | nil => exact ⟨r,cert,by simpa [total,orbit,run] using target⟩
  | cons a front ih =>
    obtain ⟨positive,nextEnabled⟩ := enabled
    obtain ⟨_,u,gap,child⟩ := (certificate_cons_iff r a (front++tail)).mp cert
    have first := source_gap_transport a s.power r u n s.debt positive gap target
    have target' : (orbit a n : Int) =
        (3 : Int)^(advance a s).power*u-(advance a s).debt := by
      simp only [advance]
      omega
    obtain ⟨v,tailCert,result⟩ := ih (advance a s) u (orbit a n)
      nextEnabled child target'
    refine ⟨v,tailCert,?_⟩
    simpa only [total,orbit_add,run] using result

/-- The updated exponent is exactly the initial exponent plus the actual
target odd count minus the number of consumed source odd gaps. -/
theorem complete_word_budget (s : Carry) (front tail : List Nat) (r n : Nat)
    (enabled : Enabled s front) (cert : Certificate r (front++tail))
    (target : (n : Int) = (3 : Int)^s.power*r-s.debt) :
    (run s front).power+front.length = s.power+odds (total front) n := by
  induction front generalizing s r n with
  | nil => simp [run,total,odds]
  | cons a front ih =>
    obtain ⟨positive,nextEnabled⟩ := enabled
    obtain ⟨_,u,gap,child⟩ := (certificate_cons_iff r a (front++tail)).mp cert
    have first := source_gap_transport a s.power r u n s.debt positive gap target
    have counts := source_gap_odds a s.power r u n s.debt positive gap target
    have target' : (orbit a n : Int) =
        (3 : Int)^(advance a s).power*u-(advance a s).debt := by
      simp only [advance]
      omega
    have budget := ih (advance a s) u (orbit a n) nextEnabled child target'
    have spent : (advance a s).power+1=s.power+odds a n := by
      simp only [advance]
      omega
    simp only [run,total,List.length_cons,odds_add]
    omega

/-- This constructive split always terminates because it consumes a finite
supplied word. It either reaches power zero or consumes the entire word.
The second alternative is deliberately retained as an unresolved carry. -/
theorem maximal_enabled_prefix (s : Carry) (word : List Nat) :
    ∃ front rest, word=front++rest ∧ Enabled s front ∧
      ((run s front).power=0 ∨ rest=[]) := by
  induction word generalizing s with
  | nil => exact ⟨[],[],rfl,trivial,Or.inr rfl⟩
  | cons a word ih =>
    by_cases zero : s.power=0
    · exact ⟨[],a::word,rfl,trivial,Or.inl zero⟩
    · obtain ⟨front,rest,eq,enabled,stop⟩ := ih (advance a s)
      exact ⟨a::front,rest,by simp [eq],⟨by omega,enabled⟩,stop⟩

theorem negativeStep_nonnegative (z : Int) (nonnegative : 0≤z) :
    0≤negativeStep z := by
  unfold negativeStep
  split <;> omega

theorem negativeOrbit_nonnegative (k : Nat) (z : Int) (nonnegative : 0≤z) :
    0≤negativeOrbit k z := by
  induction k generalizing z with
  | zero => exact nonnegative
  | succ k ih => exact ih _ (negativeStep_nonnegative z nonnegative)

theorem run_debt_nonnegative (s : Carry) (word : List Nat) (nonnegative : 0≤s.debt) :
    0≤(run s word).debt := by
  induction word generalizing s with
  | nil => exact nonnegative
  | cons a word ih =>
    apply ih (advance a s)
    have pow : (0 : Int)≤3^(s.power-1) := Int.pow_nonneg (by decide)
    exact negativeOrbit_nonnegative a _ (by omega)

theorem negative_one (k : Nat) : negativeOrbit k 1=1 ∧ negativeOdds k 1=k := by
  induction k with
  | zero => simp [negativeOrbit,negativeOdds]
  | succ k ih => simpa [negativeOrbit,negativeOdds,negativeStep] using ih

/-- The original carry has signed debt minus two. Its first actual source
gap enters positive debt one, with no restriction on the gap. -/
theorem initial_carry (a : Nat) : advance a ⟨2,-2⟩ = ⟨a+1,1⟩ := by
  have h := negative_one a
  simp only [advance]
  change Carry.mk (1+negativeOdds a 1) (negativeOrbit a 1)=Carry.mk (a+1) 1
  rw [h.1,h.2,Nat.add_comm]

theorem initial_carry_debt (a : Nat) (word : List Nat) :
    0≤(run ⟨2,-2⟩ (a::word)).debt := by
  simp only [run,initial_carry]
  exact run_debt_nonnegative ⟨a+1,1⟩ word (by simp)

theorem orbit_positive (k n : Nat) (positive : 0<n) : 0<orbit k n := by
  induction k generalizing n with
  | zero => exact positive
  | succ k ih =>
    apply ih (step n)
    unfold step
    split <;> omega

/-- A nonempty consumed prefix strictly decreases the existing source grade;
the literal suffix cancels, independently of its length and values. -/
theorem consumed_prefix_rank (front tail : List Nat) (nonempty : front≠[]) :
    Less (grades 0 tail) (grades 0 (front++tail)) := by
  have mapped : front.map (2*·) ≠ [] := by
    intro empty
    have h := congrArg List.length empty
    simp only [List.length_map,List.length_nil] at h
    exact nonempty (List.eq_nil_of_length_eq_zero h)
  have drop : Less [] (front.map (2*·)) :=
    replace_many _ _ mapped (by simp)
  have full := (less_append_right_iff [] (front.map (2*·)) (tail.map (2*·))).mpr drop
  simpa [grades,List.map_append] using full

/-- If the carry power reaches zero, its nonnegative debt gives an active
interval query on the actual complete suffix with strictly smaller grade. -/
theorem zero_power_interval (s : Carry) (front tail : List Nat) (r n : Nat)
    (enabled : Enabled s front) (cert : Certificate r (front++tail))
    (target : (n : Int) = (3 : Int)^s.power*r-s.debt)
    (nonempty : front≠[]) (zero : (run s front).power=0)
    (debt : 0≤(run s front).debt) :
    ∃ u, Certificate u tail ∧ orbit (total front) n≤u ∧
      Less (grades 0 tail) (grades 0 (front++tail)) := by
  obtain ⟨u,tailCert,result⟩ := complete_word_transport s front tail r n enabled cert target
  rw [zero] at result
  simp only [Int.pow_zero,Int.one_mul] at result
  exact ⟨u,tailCert,by omega,consumed_prefix_rank front tail nonempty⟩

/-- Total all-word compilation of the original carry. Every nonempty supplied
complete word yields an actual positive transported target, an unchanged
complete suffix and a strict decrease of the original source grade. Either
power zero supplies the small interval, or the whole supplied word has been
consumed and the remaining signed carry is explicitly retained. -/
theorem initial_complete_compiler (word tail : List Nat) (r : Nat)
    (cert : Certificate r (word++tail)) (nonempty : word≠[]) :
    ∃ front rest u, word=front++rest ∧ front≠[] ∧
      Enabled ⟨2,-2⟩ front ∧ Certificate u (rest++tail) ∧
      0<orbit (total front) (9*r+2) ∧
      (orbit (total front) (9*r+2) : Int) =
        (3 : Int)^(run ⟨2,-2⟩ front).power*u-(run ⟨2,-2⟩ front).debt ∧
      0≤(run ⟨2,-2⟩ front).debt ∧
      (run ⟨2,-2⟩ front).power+front.length=2+odds (total front) (9*r+2) ∧
      Less (grades 0 (rest++tail)) (grades 0 (word++tail)) ∧
      ((run ⟨2,-2⟩ front).power=0 ∨ rest=[]) := by
  obtain ⟨front,rest,eq,enabled,stop⟩ := maximal_enabled_prefix ⟨2,-2⟩ word
  have nonemptyFront : front≠[] := by
    intro nil
    subst front
    simp only [run] at stop
    rcases stop with zero | done
    · contradiction
    · simp only [done,List.append_nil] at eq
      exact nonempty eq
  have source : Certificate r (front++(rest++tail)) := by
    simpa only [eq,List.append_assoc] using cert
  have target : ((9*r+2 : Nat) : Int) = (3 : Int)^(2:Nat)*r-(-2) := by omega
  obtain ⟨u,tailCert,result⟩ := complete_word_transport ⟨2,-2⟩ front (rest++tail)
    r (9*r+2) enabled source target
  have debt : 0≤(run ⟨2,-2⟩ front).debt := by
    cases front with
    | nil => contradiction
    | cons a front => exact initial_carry_debt a front
  refine ⟨front,rest,u,eq,nonemptyFront,enabled,tailCert,
    orbit_positive _ _ (by omega),result,debt,?_,?_,stop⟩
  · exact complete_word_budget ⟨2,-2⟩ front (rest++tail) r (9*r+2) enabled source target
  · simpa only [eq,List.append_assoc] using consumed_prefix_rank front (rest++tail) nonemptyFront

theorem orbit_basin (k n : Nat) :
    CollatzReverseBasin.Basin (orbit k n) ↔ CollatzReverseBasin.Basin n := by
  induction k generalizing n with
  | zero => exact Iff.rfl
  | succ k ih => exact (ih (step n)).trans (CollatzClosure.basin_step n)

/-- General exact interval guard. The displayed induction hypothesis is the
usual lower-grade complete-source interval query; it is an explicit premise,
not a theorem asserting global interval coverage. -/
theorem interval_query_rule (s : Carry) (front tail : List Nat) (r n : Nat)
    (enabled : Enabled s front) (cert : Certificate r (front++tail))
    (target : (n : Int) = (3 : Int)^s.power*r-s.debt)
    (nonempty : front≠[]) (positive : 0<n)
    (guard : ∀ u, Certificate u tail →
      (3 : Int)^(run s front).power*u-(run s front).debt≤2*u+1)
    (ih : ∀ u t word, Certificate u word →
      Less (grades 0 word) (grades 0 (front++tail)) →
      0<t → t≤2*u+1 → CollatzReverseBasin.Basin t) :
    CollatzReverseBasin.Basin n := by
  obtain ⟨u,tailCert,result⟩ := complete_word_transport s front tail r n enabled cert target
  have upper := guard u tailCert
  have child : CollatzReverseBasin.Basin (orbit (total front) n) :=
    ih u _ tail tailCert (consumed_prefix_rank front tail nonempty)
      (orbit_positive _ _ positive) (by omega)
  exact (orbit_basin _ _).mp child

/-- A useful sufficient guard, but not a total dispatcher: zero power and
nonnegative debt make the child target at most the supplied source. -/
theorem zero_power_query_rule (s : Carry) (front tail : List Nat) (r n : Nat)
    (enabled : Enabled s front) (cert : Certificate r (front++tail))
    (target : (n : Int) = (3 : Int)^s.power*r-s.debt)
    (nonempty : front≠[]) (positive : 0<n)
    (zero : (run s front).power=0) (debt : 0≤(run s front).debt)
    (ih : ∀ u t word, Certificate u word →
      Less (grades 0 word) (grades 0 (front++tail)) →
      0<t → t≤2*u+1 → CollatzReverseBasin.Basin t) :
    CollatzReverseBasin.Basin n := by
  apply interval_query_rule s front tail r n enabled cert target nonempty positive ?_ ih
  intro u _
  rw [zero]
  simp only [Int.pow_zero,Int.one_mul]
  omega

/-- Even a terminal carry representing the already convergent target one
need not reach power zero. Gap-two padding leaves this state unchanged. -/
theorem terminal_one_fixed (p : Nat) (positive : 0<p) :
    advance 2 ⟨p,(3 : Int)^p-1⟩ = ⟨p,(3 : Int)^p-1⟩ := by
  let s : Carry := ⟨p,(3 : Int)^p-1⟩
  have target : ((1 : Nat) : Int) = (3 : Int)^p*(1 : Nat)-s.debt := by
    simp only [s]
    omega
  have counts := source_gap_odds 2 p 1 1 1 s.debt positive (by decide) target
  have power : (advance 2 s).power=p := by
    have one : odds 2 1=1 := by decide
    change p-1+negativeOdds 2 ((3 : Int)^(p-1)+s.debt)=p
    rw [←counts,one]
    omega
  have path := source_gap_transport 2 p 1 1 1 s.debt positive (by decide) target
  have debt : (advance 2 s).debt=(3 : Int)^p-1 := by
    change (orbit 2 1 : Int)+(advance 2 s).debt=(3 : Int)^(advance 2 s).power*(1 : Nat) at path
    rw [power] at path
    have one : orbit 2 1=1 := by decide
    rw [one] at path
    omega
  change advance 2 s = s
  cases eq : advance 2 s
  simp only [eq] at power debt
  simp [s,power,debt]

/-- The ordinary two-cycle phase two gives the other stationary terminal
carry, so debt must remain part of any proposed stopping criterion. -/
theorem terminal_two_fixed (p : Nat) (positive : 0<p) :
    advance 2 ⟨p,(3 : Int)^p-2⟩ = ⟨p,(3 : Int)^p-2⟩ := by
  let s : Carry := ⟨p,(3 : Int)^p-2⟩
  have target : ((2 : Nat) : Int) = (3 : Int)^p*(1 : Nat)-s.debt := by
    simp only [s]
    omega
  have counts := source_gap_odds 2 p 1 1 2 s.debt positive (by decide) target
  have power : (advance 2 s).power=p := by
    have one : odds 2 2=1 := by decide
    change p-1+negativeOdds 2 ((3 : Int)^(p-1)+s.debt)=p
    rw [←counts,one]
    omega
  have path := source_gap_transport 2 p 1 1 2 s.debt positive (by decide) target
  have debt : (advance 2 s).debt=(3 : Int)^p-2 := by
    change (orbit 2 2 : Int)+(advance 2 s).debt=(3 : Int)^(advance 2 s).power*(1 : Nat) at path
    rw [power] at path
    have two : orbit 2 2=2 := by decide
    rw [two] at path
    omega
  change advance 2 s = s
  cases eq : advance 2 s
  simp only [eq] at power debt
  simp [s,power,debt]

end CollatzSignedCarry

#print axioms CollatzSignedCarry.signedStep_nat
#print axioms CollatzSignedCarry.signedOrbit_nat
#print axioms CollatzSignedCarry.one_step_complement
#print axioms CollatzSignedCarry.complement_transport
#print axioms CollatzSignedCarry.ordinary_complement_transport
#print axioms CollatzSignedCarry.source_gap_transport
#print axioms CollatzSignedCarry.signedOdds_nat
#print axioms CollatzSignedCarry.complement_odds
#print axioms CollatzSignedCarry.ordinary_complement_odds
#print axioms CollatzSignedCarry.finite_signed_lift
#print axioms CollatzSignedCarry.source_gap_odds
#print axioms CollatzSignedCarry.orbit_add
#print axioms CollatzSignedCarry.odds_add
#print axioms CollatzSignedCarry.complete_word_transport
#print axioms CollatzSignedCarry.complete_word_budget
#print axioms CollatzSignedCarry.maximal_enabled_prefix
#print axioms CollatzSignedCarry.negativeStep_nonnegative
#print axioms CollatzSignedCarry.negativeOrbit_nonnegative
#print axioms CollatzSignedCarry.run_debt_nonnegative
#print axioms CollatzSignedCarry.negative_one
#print axioms CollatzSignedCarry.initial_carry
#print axioms CollatzSignedCarry.initial_carry_debt
#print axioms CollatzSignedCarry.orbit_positive
#print axioms CollatzSignedCarry.consumed_prefix_rank
#print axioms CollatzSignedCarry.zero_power_interval
#print axioms CollatzSignedCarry.initial_complete_compiler
#print axioms CollatzSignedCarry.orbit_basin
#print axioms CollatzSignedCarry.interval_query_rule
#print axioms CollatzSignedCarry.zero_power_query_rule
#print axioms CollatzSignedCarry.terminal_one_fixed
#print axioms CollatzSignedCarry.terminal_two_fixed
