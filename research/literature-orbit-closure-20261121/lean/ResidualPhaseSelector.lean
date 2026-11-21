module

public import ResidualPrefixErasure

@[expose] public section

/-!
# A phase selector for every odd-run length in the residual class

For each k ≥ 6, an explicit Chinese-remainder selector produces an entire
infinite source progression inside `34587 mod 73728`. All these progressions
have the physical partner `1024*x = 729*n+29`, with source clock k+15.
This is a partial selector, not a selector for every source in that class.
-/

namespace CollatzShell.ResidualPhaseSelector

open ResidualPrefixErasure

/-- CRT idempotents: 6400 is (1,0), and 14337 is (0,1), modulo (81,256). -/
def phaseSeed (k : Nat) : Nat :=
  (6400*2^(53*k+1)+14337*(147*3^(63*(k+1))))%20736

def oddParameter (k t : Nat) : Nat := phaseSeed k+20736*t
def runCore (k t : Nat) : Nat := 81*oddParameter k t
def sourceQuotient (k t : Nat) : Nat := 9*(2^k*oddParameter k t/81)
def seed (k t : Nat) : Nat := 128*sourceQuotient k t+27
def partner (k t : Nat) : Nat := 2^(k-3)*runCore k t-1

private theorem phase_mod81 (k t : Nat) :
    oddParameter k t%81=2^(53*k+1)%81 := by
  have raw : phaseSeed k%81=2^(53*k+1)%81 := by
    unfold phaseSeed
    rw [Nat.mod_mod_of_dvd _ (by decide : 81∣20736),Nat.add_mod,
      Nat.mul_mod 6400 _,Nat.mul_mod 14337 _]
    norm_num
  unfold oddParameter
  omega

private theorem phase_mod256 (k t : Nat) :
    oddParameter k t%256=(147*3^(63*(k+1)))%256 := by
  have raw : phaseSeed k%256=(147*3^(63*(k+1)))%256 := by
    unfold phaseSeed
    rw [Nat.mod_mod_of_dvd _ (by decide : 256∣20736),Nat.add_mod,
      Nat.mul_mod 6400 _,Nat.mul_mod 14337 _]
    norm_num
  unfold oddParameter
  omega

private theorem binary_carry (k t : Nat) :
    (2^k*oddParameter k t)%81=2 := by
  have period : 2^54%81=1 := by decide
  rw [Nat.mul_mod,phase_mod81,← Nat.mul_mod,← pow_add,
    show k+(53*k+1)=54*k+1 by omega,pow_add,pow_mul,Nat.mul_mod,
    Nat.pow_mod,period]
  simp

private theorem ternary_carry (k t : Nat) :
    (3^(k+1)*oddParameter k t)%256=147 := by
  have period : 3^64%256=1 := by decide
  rw [Nat.mul_mod,phase_mod256,← Nat.mul_mod]
  have eq : 3^(k+1)*(147*3^(63*(k+1)))=147*3^(64*(k+1)) := by
    rw [show 64*(k+1)=(k+1)+63*(k+1) by omega,pow_add]
    ring
  rw [eq,pow_mul,Nat.mul_mod,Nat.pow_mod,period]
  simp

private theorem parameter_positive (k t : Nat) : 0<oddParameter k t := by
  have carry := binary_carry k t
  by_contra fail
  have zero : oddParameter k t=0 := by omega
  simp only [zero,Nat.mul_zero,Nat.zero_mod] at carry
  omega

/-- The selector realizes the correct expanding-prefix endpoint for every k. -/
theorem source_endpoint (k t : Nat) :
    729*sourceQuotient k t+162=2^k*runCore k t := by
  have remainder := binary_carry k t
  have division := Nat.mod_add_div (2^k*oddParameter k t) 81
  unfold sourceQuotient runCore
  nlinarith only [remainder,division]

/-- The chosen run core is odd, so k is the exact initial odd-run length
of the source after the seven-step prefix. -/
theorem parameter_odd (k t : Nat) : oddParameter k t%2=1 := by
  have eq := phase_mod256 k t
  have reduced := congrArg (fun n : Nat => n%2) eq
  rw [Nat.mod_mod_of_dvd _ (by decide : 2∣256),
    Nat.mod_mod_of_dvd _ (by decide : 2∣256),Nat.mul_mod,Nat.pow_mod] at reduced
  simpa using reduced

/-- Each k selects exactly one complete arithmetic progression. -/
theorem source_progression (k t : Nat) :
    seed k t=seed k 0+9*2^(k+15)*t := by
  have a := source_endpoint k t
  have b := source_endpoint k 0
  have quotient : sourceQuotient k t=sourceQuotient k 0+2304*2^k*t := by
    unfold runCore oddParameter at a b
    nlinarith only [a,b]
  unfold seed
  rw [quotient,pow_add]
  ring

/-- The selected base is the least positive representative of its progression. -/
theorem source_base_bounds (k : Nat) :
    0<seed k 0 ∧ seed k 0<9*2^(k+15) := by
  have base : phaseSeed k<20736 := Nat.mod_lt _ (by decide)
  have p : 0<2^k := by positivity
  have bound := Nat.mul_lt_mul_of_pos_left base p
  have endpoint := source_endpoint k 0
  unfold runCore oddParameter at endpoint
  unfold seed
  rw [pow_add]
  constructor
  · omega
  · norm_num only [Nat.reducePow]
    nlinarith only [endpoint,bound]

/-- Every selected parameter discharges the eight-clock diamond phase. -/
theorem endpoint_phase (k t : Nat) (hk : 3≤k) :
    (3^(k-3)*runCore k t)%256=147 := by
  have exponent : 3^(k-3)*81=3^(k+1) := by
    rw [show (81:Nat)=3^4 by decide,← pow_add]
    congr 1
    omega
  unfold runCore
  rw [← Nat.mul_assoc,exponent]
  exact ternary_carry k t

/-- The clock k may be every integer ≥ 6, with a free progression parameter t. -/
theorem physical_merger (k t : Nat) (hk : 6≤k) :
    0<partner k t ∧ partner k t<seed k t ∧
      1024*partner k t=729*seed k t+29 ∧
      orbit (k+5) (partner k t)=orbit (k+15) (seed k t) := by
  exact prefix27_eighth_partner k (runCore k t) (sourceQuotient k t)
    (by omega) (by change 0<81*oddParameter k t; exact Nat.mul_pos (by decide) (parameter_positive k t))
    (source_endpoint k t) (endpoint_phase k t (by omega))

/-- Each selected source lies in one explicitly unresolved earlier cell. -/
theorem source_residue (k t : Nat) (hk : 6≤k) : seed k t%73728=34587 := by
  have endpoint := source_endpoint k t
  have binary : 64∣2^k := by
    rw [show k=6+(k-6) by omega,pow_add]
    exact ⟨2^(k-6),by ring⟩
  obtain ⟨a,ha⟩ := binary
  have ternary : sourceQuotient k t%9=0 := by unfold sourceQuotient; omega
  have mod64 : (729*sourceQuotient k t+162)%64=0 := by
    rw [endpoint,ha,Nat.mul_assoc]
    omega
  have source_mod64 : sourceQuotient k t%64=14 := by omega
  unfold seed
  omega

/-- These sources grow throughout the fixed prefix and their variable odd run. -/
theorem no_direct_descent_through_run (k t i : Nat) (hi : i≤k+7) :
    seed k t≤orbit i (seed k t) := by
  exact prefix27_no_descent_through_run k (runCore k t) (sourceQuotient k t) i
    (by change 0<81*oddParameter k t; exact Nat.mul_pos (by decide) (parameter_positive k t))
    (source_endpoint k t) (by omega)

/-- A direct orbit descent within the earlier source-clock budget cannot explain
any selected source. -/
theorem no_direct_descent_thirteen (k t i : Nat) (hk : 6≤k) (hi : i≤13) :
    seed k t≤orbit i (seed k t) := by
  apply no_direct_descent_through_run
  omega

/-- Start the removable odd run four steps earlier for a substantially
smaller source on the same selector. -/
def smallPartner (k t : Nat) : Nat := 2^(k+1)*oddParameter k t-1

private theorem three_step_prefix (z : Nat) : orbit 3 (128*z+27)=144*z+31 := by
  have he (x : Nat) (h : x%2=0) : step x=x/2 := by simp [step,h]
  have ho (x : Nat) (h : x%2≠0) : step x=(3*x+1)/2 := by simp [step,h]
  have e0 : step (128*z+27)=192*z+41 := by rw [ho _ (by omega)]; omega
  have e1 : step (192*z+41)=288*z+62 := by rw [ho _ (by omega)]; omega
  have e2 : step (288*z+62)=144*z+31 := by rw [he _ (by omega)]; omega
  simp only [orbit,e0,e1,e2]

/-- The prefix-three version improves the partner slope from729/1024 to9/64.
The common endpoint and original source clock remain the same. -/
theorem smaller_physical_merger (k t : Nat) :
    0<smallPartner k t ∧ smallPartner k t<seed k t ∧
      64*smallPartner k t+51=9*seed k t ∧
      orbit (k+9) (smallPartner k t)=orbit (k+15) (seed k t) := by
  have phase : (3^((k+4)-3)*oddParameter k t)%256=147 := by
    simpa only [show k+4-3=k+1 by omega] using ternary_carry k t
  obtain ⟨positive,scale,_,merge⟩ := rising_eighth_source_partner (k+4)
    (oddParameter k t) (by omega) (parameter_positive k t) phase
  have endpoint := source_endpoint k t
  unfold runCore at endpoint
  have raw_prefix : 144*sourceQuotient k t+32=2^k*16*oddParameter k t := by
    nlinarith only [endpoint]
  have head_endpoint : orbit 3 (seed k t)=2^(k+4)*oddParameter k t-1 := by
    unfold seed
    rw [three_step_prefix,pow_add]
    norm_num only [Nat.reducePow]
    omega
  have head_relation : 8*orbit 3 (seed k t)=9*seed k t+5 := by
    unfold seed
    rw [three_step_prefix]
    ring
  rw [head_endpoint] at head_relation
  have relation : 64*smallPartner k t+51=9*seed k t := by
    rw [show k+4-3=k+1 by omega] at scale
    unfold smallPartner
    omega
  have positive' : 0<smallPartner k t := by
    simpa only [smallPartner,show k+4-3=k+1 by omega] using positive
  refine ⟨positive',by omega,relation,?_⟩
  rw [show k+15=3+(k+12) by omega,orbit_add 3 (k+12),head_endpoint]
  simpa only [smallPartner,show k+4-3=k+1 by omega,
    show k+4+5=k+9 by omega,show k+4+8=k+12 by omega] using merge

private theorem diamond_tail_minimum (a i : Nat) (hi : i≤8) :
    2*a+1≤orbit i (256*a+128) := by
  have he (x : Nat) (h : x%2=0) : step x=x/2 := by simp [step,h]
  have ho (x : Nat) (h : x%2≠0) : step x=(3*x+1)/2 := by simp [step,h]
  have e0 : step (256*a+128)=128*a+64 := by rw [he _ (by omega)]; omega
  have e1 : step (128*a+64)=64*a+32 := by rw [he _ (by omega)]; omega
  have e2 : step (64*a+32)=32*a+16 := by rw [he _ (by omega)]; omega
  have e3 : step (32*a+16)=16*a+8 := by rw [he _ (by omega)]; omega
  have e4 : step (16*a+8)=8*a+4 := by rw [he _ (by omega)]; omega
  have e5 : step (8*a+4)=4*a+2 := by rw [he _ (by omega)]; omega
  have e6 : step (4*a+2)=2*a+1 := by rw [he _ (by omega)]; omega
  have e7 : step (2*a+1)=3*a+2 := by rw [ho _ (by omega)]; omega
  interval_cases i <;> simp only [orbit,e0,e1,e2,e3,e4,e5,e6,e7] <;> omega

private theorem merger_power_margin (k : Nat) (hk : 8≤k) :
    16384*2^k≤729*3^k := by
  have p := Nat.pow_le_pow_left (by decide : 2≤3) (k-8)
  rw [show k=8+(k-8) by omega,pow_add,pow_add]
  norm_num only [Nat.reducePow]
  calc
    16384*(256*2^(k-8))=4194304*2^(k-8) := by ring
    _ ≤4782969*3^(k-8) := Nat.mul_le_mul (by decide) p
    _ =729*(6561*3^(k-8)) := by ring

/-- For every k≥8 the source stays above its starting height all the way to
the displayed common endpoint. The smaller partner is therefore available
before any direct descent of the original source. -/
theorem no_direct_descent_through_merger (k t i : Nat) (hk : 8≤k)
    (hi : i≤k+15) : seed k t≤orbit i (seed k t) := by
  by_cases early : i≤7+k
  · exact no_direct_descent_through_run k t i (by omega)
  · have hu : 0<runCore k t := by
      exact Nat.mul_pos (by decide : 0<81) (parameter_positive k t)
    have endpoint := source_endpoint k t
    have head_endpoint : orbit 7 (seed k t)=2^k*runCore k t-1 := by
      unfold seed
      rw [prefix27]
      omega
    have atRun : orbit (7+k) (seed k t)=3^k*runCore k t-1 := by
      rw [orbit_add 7 k,head_endpoint,(odd_run k (runCore k t) hu).1]
    have source_eq : 9*seed k t+13=128*2^k*oddParameter k t := by
      unfold seed
      unfold runCore at endpoint
      nlinarith only [endpoint]
    have scaled := Nat.mul_le_mul_right (oddParameter k t) (merger_power_margin k hk)
    have lower_raw : 128*seed k t+1≤3^k*runCore k t := by
      unfold runCore
      nlinarith only [source_eq,scaled]
    have phase := ternary_carry k t
    have phase_eq : 3^k*runCore k t=27*(3^(k+1)*oddParameter k t) := by
      unfold runCore
      rw [pow_succ]
      ring
    have phase_mod : (3^k*runCore k t)%256=129 := by
      rw [phase_eq,Nat.mul_mod,phase]
    have tail_form : 3^k*runCore k t-1=
        256*((3^k*runCore k t)/256)+128 := by omega
    have minimum : seed k t≤2*((3^k*runCore k t)/256)+1 := by omega
    rw [show i=7+k+(i-(7+k)) by omega,orbit_add (7+k) (i-(7+k)),atRun,tail_form]
    exact minimum.trans (diamond_tail_minimum _ _ (by omega))

/-- A genuine smaller-source induction certificate, with no convergence claim
for arbitrary smaller partners added as an axiom. -/
theorem basin_by_smaller_induction (k t : Nat) (hk : 6≤k)
    (ih : ∀ x, 0<x → x<seed k t → Basin x) : Basin (seed k t) := by
  obtain ⟨positive,smaller,_,merge⟩ := physical_merger k t hk
  have bx := ih _ positive smaller
  have same : Basin (partner k t) ↔ Basin (seed k t) := by
    apply (basin_at_hit (x := partner k t)
      (q := orbit (k+5) (partner k t)) ⟨_,rfl⟩).trans
    apply Iff.symm
    exact basin_at_hit (x := seed k t)
      (q := orbit (k+5) (partner k t)) ⟨_,merge.symm⟩
  exact same.mp bx

#print axioms parameter_odd
#print axioms source_progression
#print axioms source_base_bounds
#print axioms source_endpoint
#print axioms endpoint_phase
#print axioms physical_merger
#print axioms source_residue
#print axioms no_direct_descent_through_run
#print axioms no_direct_descent_thirteen
#print axioms smaller_physical_merger
#print axioms no_direct_descent_through_merger
#print axioms basin_by_smaller_induction

end CollatzShell.ResidualPhaseSelector
