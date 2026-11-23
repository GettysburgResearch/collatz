import Mathlib.Tactic
import Mathlib.NumberTheory.Multiplicity

/-!
Rigidity of an ordinary affine merger that preserves its own parity cell.

All orbit, parity, and odd-count hypotheses below concern ordinary natural
numbers. The arithmetic conclusion does not apply to maps whose binary guards
are switched or whose two words have different odd counts.
-/

namespace CollatzSiblingRigidity

def step (n : Nat) : Nat := if n%2=0 then n/2 else (3*n+1)/2

def orbit : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => orbit k (step n)

def odds : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, n => odds k (step n) + n%2

def offset : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, n => 3^(odds k (step n))*(n%2) + 2*offset k (step n)

theorem step_formula (n : Nat) : 2*step n=3^(n%2)*n+n%2 := by
  by_cases he : n%2=0
  · simp [step, he]; omega
  · have ho : n%2=1 := by omega
    simp [step, ho]; omega

theorem affine_formula (k n : Nat) :
    2^k*orbit k n=3^(odds k n)*n+offset k n := by
  induction k generalizing n with
  | zero => simp [orbit, odds, offset]
  | succ k ih =>
    have h := ih (step n)
    have s := step_formula n
    simp only [orbit, odds, offset, pow_add, pow_one]
    nlinarith [congrArg (fun z => 2*z) h,
      congrArg (fun z => 3^(odds k (step n))*z) s]

theorem orbit_add (k a n : Nat) : orbit (k+a) n=orbit a (orbit k n) := by
  induction k generalizing n with
  | zero => simp [orbit]
  | succ k ih => simpa [Nat.succ_add, orbit] using ih (step n)

theorem odds_add (k a n : Nat) : odds (k+a) n=odds k n+odds a (orbit k n) := by
  induction k generalizing n with
  | zero => simp [orbit, odds]
  | succ k ih => simpa [Nat.succ_add, orbit, odds, Nat.add_assoc, Nat.add_comm,
      Nat.add_left_comm] using congrArg (fun z => z+n%2) (ih (step n))

theorem no_odds_scaling (a n : Nat) (h : odds a n=0) : n=2^a*orbit a n := by
  induction a generalizing n with
  | zero => simp [orbit]
  | succ a ih =>
    have tail : odds a (step n)=0 := by simp only [odds] at h; omega
    have ev : n%2=0 := by simp only [odds] at h; omega
    have twice : n=2*step n := by simp [step, ev]; omega
    calc
      n=2*step n := twice
      _=2*(2^a*orbit a (step n)) := congrArg (fun z => 2*z) (ih (step n) tail)
      _=2^(a+1)*orbit (a+1) n := by simp only [orbit, pow_add, pow_one]; ring

theorem step_shift (t n : Nat) : step (2*t+n)=3^(n%2)*t+step n := by
  by_cases he : n%2=0
  · simp [step, he, show (2*t+n)%2=0 by omega]; omega
  · have ho : n%2=1 := by omega
    simp [step, ho]; omega

theorem word_shift (k n t : Nat) :
    orbit k (2^k*t+n)=3^(odds k n)*t+orbit k n ∧
    odds k (2^k*t+n)=odds k n ∧
    offset k (2^k*t+n)=offset k n := by
  induction k generalizing n t with
  | zero => simp [orbit, odds, offset]
  | succ k ih =>
    rw [show 2^(k+1)*t+n=2*(2^k*t)+n by ring]
    have parity : (2*(2^k*t)+n)%2=n%2 := by omega
    simp only [orbit, odds, offset, step_shift, parity]
    rw [show 3^(n%2)*(2^k*t)+step n=2^k*(3^(n%2)*t)+step n by ring]
    obtain ⟨hit, count, off⟩ := ih (step n) (3^(n%2)*t)
    rw [hit, count, off]
    simp only [pow_add]
    constructor
    · ring
    · simp

theorem offset_zero_of_no_odds (k n : Nat) (h : odds k n=0) : offset k n=0 := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    have tail : odds k (step n)=0 := by simp only [odds] at h; omega
    have ev : n%2=0 := by simp only [odds] at h; omega
    simp [offset, ev, ih (step n) tail]

theorem offset_unit (k n : Nat) (h : 0<odds k n) : (offset k n)%3≠0 := by
  induction k generalizing n with
  | zero => simp [odds] at h
  | succ k ih =>
    by_cases tail : odds k (step n)=0
    · have odd : n%2=1 := by simp only [odds, tail] at h; omega
      simp [offset, tail, odd, offset_zero_of_no_odds k (step n) tail]
    · have pos : 0<odds k (step n) := by omega
      have unit := ih (step n) pos
      have mult : 3 ∣ 3^(odds k (step n)) := by
        obtain ⟨r, eq⟩ := Nat.exists_eq_succ_of_ne_zero tail
        simp [eq, pow_succ]
      have residue : (offset (k+1) n)%3=(2*offset k (step n))%3 := by
        rw [offset, Nat.add_mod, Nat.mod_eq_zero_of_dvd (dvd_mul_of_dvd_left mult (n%2))]
        simp
      rw [residue]
      omega

/-- A fixed affine prefix and an all-even suffix leave exactly one possible
translation. This algebraic lemma does not infer the ordinary word guards. -/
theorem affine_identity (k a p n c C u v : Nat)
    (first : 2^k*u=3^p*n+C)
    (second : 2^k*v=3^p*(2^a*n+c)+C)
    (same : v=2^a*u) :
    3^p*c+C=2^a*C := by
  rw [same] at second
  nlinarith [congrArg (fun z => 2^a*z) first]

/-- The source and its affine image share the whole supplied parity prefix;
their actual merger has the indicated clocks and equal total odd counts. -/
theorem invariant_prefix_identity (k a n c t : Nat)
    (cell : 2^a*n+c=2^k*t+n)
    (hit : orbit (k+a) (2^a*n+c)=orbit k n)
    (count : odds (k+a) (2^a*n+c)=odds k n) :
    3^(odds k n)*c+offset k n=2^a*offset k n := by
  obtain ⟨hs, hc, ho⟩ := word_shift k n t
  have extra : odds a (orbit k (2^a*n+c))=0 := by
    rw [odds_add] at count
    have shared : odds k (2^a*n+c)=odds k n := by rw [cell]; exact hc
    rw [shared] at count
    omega
  have evenTail := no_odds_scaling a (orbit k (2^a*n+c)) extra
  rw [←orbit_add, hit] at evenTail
  have second := affine_formula k (2^a*n+c)
  rw [cell, hc, ho] at second
  exact affine_identity k a (odds k n) n c (offset k n) (orbit k n)
    (orbit k (2^a*n+c)) (affine_formula k n)
    (by simpa only [←cell] using second) evenTail

theorem identity_divisibility (p a c C : Nat)
    (unit : Nat.Coprime (3^p) C)
    (eq : 3^p*c+C=2^a*C) : 3^p ∣ 2^a-1 := by
  have product : 3^p ∣ (2^a-1)*C := by
    refine ⟨c, ?_⟩
    rw [Nat.sub_mul, one_mul]
    omega
  exact unit.dvd_of_dvd_mul_right product

theorem prefix_divisibility (k a n c t : Nat)
    (positiveOddCount : 0<odds k n)
    (cell : 2^a*n+c=2^k*t+n)
    (hit : orbit (k+a) (2^a*n+c)=orbit k n)
    (count : odds (k+a) (2^a*n+c)=odds k n) :
    3^(odds k n) ∣ 2^a-1 := by
  have unit : Nat.Coprime 3 (offset k n) := by
    apply (Nat.prime_three.coprime_iff_not_dvd).mpr
    exact fun hd => offset_unit k n positiveOddCount (Nat.mod_eq_zero_of_dvd hd)
  exact identity_divisibility _ _ _ _ (unit.pow_left _)
    (invariant_prefix_identity k a n c t cell hit count)

/-- The exact order obstruction follows from the proved odd-prime LTE theorem. -/
theorem clock_order (p a : Nat) (hp : 0<p) (ha : 0<a)
    (hdiv : 3^p ∣ 2^a-1) : 2*3^(p-1) ∣ a ∧ 2*3^(p-1) ≤ a := by
  have h3 : 3 ∣ 2^a-1 := by
    apply dvd_trans _ hdiv
    obtain ⟨j, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : p≠0)
    simp [pow_succ]
  have even : Even a := by
    rcases Nat.even_or_odd a with he|ho
    · exact he
    · obtain ⟨b, hb⟩ := ho
      have residue : 2^a%3=2 := by
        rw [hb, pow_add, pow_mul]
        norm_num only [Nat.reducePow, pow_one]
        rw [Nat.mul_mod, Nat.pow_mod]
        norm_num
      have lower : 1≤2^a := Nat.one_le_pow _ _ (by decide)
      have rem : (2^a-1)%3=0 := Nat.mod_eq_zero_of_dvd h3
      omega
  obtain ⟨b, hb⟩ := even
  have aeq : a=2*b := by omega
  have bne : b≠0 := by omega
  have dv4 : 3^p ∣ 4^b-1 := by simpa [aeq, pow_mul] using hdiv
  let : Fact (Nat.Prime 3) := ⟨Nat.prime_three⟩
  have lte : padicValNat 3 (4^b-1)=1+padicValNat 3 b := by
    simpa using padicValNat.pow_sub_pow (p:=3) (x:=4) (y:=1)
      (by decide : Odd 3) (by decide) (by decide) (by decide) bne
  have diffne : 4^b-1≠0 := by
    have lower : 1<4^b := one_lt_pow₀ (by decide) bne
    omega
  have val : p≤padicValNat 3 (4^b-1) := (padicValNat_dvd_iff_le diffne).mp dv4
  have divb : 3^(p-1) ∣ b := (padicValNat_dvd_iff_le bne).mpr (by rw [lte] at val; omega)
  have diva : 2*3^(p-1) ∣ a := by
    obtain ⟨j, hj⟩ := divb
    refine ⟨j, ?_⟩
    rw [aeq, hj]
    ring
  exact ⟨diva, Nat.le_of_dvd ha diva⟩

theorem invariant_prefix_clock_lower_bound (k a n c t : Nat)
    (positiveOddCount : 0<odds k n) (positiveClock : 0<a)
    (cell : 2^a*n+c=2^k*t+n)
    (hit : orbit (k+a) (2^a*n+c)=orbit k n)
    (count : odds (k+a) (2^a*n+c)=odds k n) :
    2*3^(odds k n-1) ≤ a :=
  (clock_order _ _ positiveOddCount positiveClock
    (prefix_divisibility k a n c t positiveOddCount cell hit count)).2

theorem invariant_prefix_expansion_lower_bound (k a n c t : Nat)
    (positiveOddCount : 0<odds k n) (positiveClock : 0<a)
    (cell : 2^a*n+c=2^k*t+n)
    (hit : orbit (k+a) (2^a*n+c)=orbit k n)
    (count : odds (k+a) (2^a*n+c)=odds k n) :
    2^(2*3^(odds k n-1))*n ≤ 2^a*n+c := by
  have clock := invariant_prefix_clock_lower_bound k a n c t
    positiveOddCount positiveClock cell hit count
  have powers : 2^(2*3^(odds k n-1))≤2^a :=
    pow_le_pow_right₀ (by decide : 1≤(2:Nat)) clock
  have product := Nat.mul_le_mul_right n powers
  omega

theorem positive_sources_of_positive_odds (k a n c : Nat)
    (positiveOddCount : 0<odds k n) : 0<n ∧ 0<2^a*n+c := by
  have zero : ∀ j, odds j 0=0 := by
    intro j
    induction j with
    | zero => rfl
    | succ j ih => simpa [odds, step] using ih
  have hn : 0<n := by
    by_contra! h
    have : n=0 := by omega
    rw [this, zero] at positiveOddCount
    omega
  exact ⟨hn, by have : 0<2^a*n := Nat.mul_pos (by positivity) hn; omega⟩

end CollatzSiblingRigidity

#print axioms CollatzSiblingRigidity.step_formula
#print axioms CollatzSiblingRigidity.affine_formula
#print axioms CollatzSiblingRigidity.orbit_add
#print axioms CollatzSiblingRigidity.odds_add
#print axioms CollatzSiblingRigidity.no_odds_scaling
#print axioms CollatzSiblingRigidity.step_shift
#print axioms CollatzSiblingRigidity.word_shift
#print axioms CollatzSiblingRigidity.offset_zero_of_no_odds
#print axioms CollatzSiblingRigidity.offset_unit
#print axioms CollatzSiblingRigidity.affine_identity
#print axioms CollatzSiblingRigidity.invariant_prefix_identity
#print axioms CollatzSiblingRigidity.identity_divisibility
#print axioms CollatzSiblingRigidity.prefix_divisibility
#print axioms CollatzSiblingRigidity.clock_order
#print axioms CollatzSiblingRigidity.invariant_prefix_clock_lower_bound
#print axioms CollatzSiblingRigidity.invariant_prefix_expansion_lower_bound
#print axioms CollatzSiblingRigidity.positive_sources_of_positive_odds
