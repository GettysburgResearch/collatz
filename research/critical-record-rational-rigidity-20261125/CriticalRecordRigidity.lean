import Mathlib

/-! Candidate finite consumers for critical-record rational rigidity.
UNCOMPILED in this checkpoint. The signed occupation, compactness, periodic
shadow selection, and Subspace Theorem are written arguments, not Lean axioms.
The final full-domain implication exposes its two unproved hypotheses. -/

namespace CriticalRecordRigidity

-- Signed shortcut numerator; d=1 is the ordinary shortcut on positive integers.
def step (d x : ℤ) : ℤ :=
  if x % 2 = 0 then x / 2 else (3*x+d)/2

def run (d : ℤ) : ℕ → ℤ → ℤ
  | 0, x => x
  | k+1, x => run d k (step d x)

theorem run_add (d : ℤ) (i j : ℕ) (x : ℤ) :
    run d (i+j) x = run d j (run d i x) := by
  induction i generalizing x with
  | zero => simp [run]
  | succ i ih =>
    rw [Nat.succ_add]
    change run d (i+j) (step d x) = run d j (run d i (step d x))
    exact ih (step d x)

theorem step_pos (x : ℤ) (hx : 0 < x) : 0 < step 1 x := by
  unfold step
  split <;> omega

theorem run_pos (i : ℕ) (x : ℤ) (hx : 0 < x) :
    0 < run 1 i x := by
  induction i generalizing x with
  | zero => exact hx
  | succ i ih => exact ih (step 1 x) (step_pos x hx)

-- Same physical parity at each step, not just the same odd count.
def Matches (d : ℤ) : ℕ → ℤ → ℤ → Prop
  | 0, _, _ => True
  | k+1, x, a => x % 2 = a % 2 ∧ Matches d k (step 1 x) (step d a)

theorem even_step (d x : ℤ) (h : x % 2 = 0) :
    2*step d x = x := by
  simp [step, h] <;> omega

theorem odd_step (d x : ℤ) (hd : d % 2 = 1) (h : x % 2 = 1) :
    2*step d x = 3*x+d := by
  have hn : x % 2 ≠ 0 := by omega
  simp [step, hn] <;> omega

theorem cancel_three (k : ℕ) (x : ℤ)
    (h : (2:ℤ)^k ∣ 3*x) : (2:ℤ)^k ∣ x := by
  induction k generalizing x with
  | zero => simp
  | succ k ih =>
    obtain ⟨v,hv⟩ := h
    have he : 3*x = 2*((2:ℤ)^k*v) := by
      calc
        3*x = (2:ℤ)^(k+1)*v := hv
        _ = 2*((2:ℤ)^k*v) := by rw [pow_succ]; ring
    have hx : x = 2*(x/2) := by omega
    have hh : 3*(x/2) = (2:ℤ)^k*v := by omega
    obtain ⟨u,hu⟩ := ih (x/2) ⟨v,hh⟩
    refine ⟨u,?_⟩
    calc
      x = 2*(x/2) := hx
      _ = (2:ℤ)^(k+1)*u := by rw [hu,pow_succ]; ring

theorem matching_divisibility (d : ℤ) (hd : d % 2 = 1)
    (k : ℕ) (x a : ℤ) (h : Matches d k x a) :
    (2:ℤ)^k ∣ d*x-a := by
  induction k generalizing x a with
  | zero => simp
  | succ k ih =>
    change x % 2 = a % 2 ∧ Matches d k (step 1 x) (step d a) at h
    obtain ⟨v,hv⟩ := ih (step 1 x) (step d a) h.2
    by_cases h0 : x % 2 = 0
    · have ha : a % 2 = 0 := by omega
      have hx' := even_step 1 x h0
      have ha' := even_step d a ha
      have he : 2*(d*step 1 x-step d a)=d*x-a := by
        linear_combination d*hx'-ha'
      refine ⟨v,?_⟩
      calc
        d*x-a = 2*(d*step 1 x-step d a) := he.symm
        _ = (2:ℤ)^(k+1)*v := by rw [hv,pow_succ]; ring
    · have hx : x % 2 = 1 := by omega
      have ha : a % 2 = 1 := by omega
      have hx' := odd_step 1 x (by decide) hx
      have ha' := odd_step d a hd ha
      have he : 2*(d*step 1 x-step d a)=3*(d*x-a) := by
        linear_combination d*hx'-ha'
      apply cancel_three (k+1) (d*x-a)
      refine ⟨v,?_⟩
      calc
        3*(d*x-a) = 2*(d*step 1 x-step d a) := he.symm
        _ = (2:ℤ)^(k+1)*v := by rw [hv,pow_succ]; ring

theorem pow_two_gt (k : ℕ) : (k:ℤ) < (2:ℤ)^k := by
  induction k with
  | zero => norm_num
  | succ k ih =>
    push_cast
    rw [pow_succ]
    omega

theorem no_infinite_negative_match (d x a : ℤ) (hd : 0 < d)
    (hdodd : d % 2 = 1) (hx : 0 < x) (ha : a < 0)
    (h : ∀ k : ℕ, Matches d k x a) : False := by
  have hprod : 0 < d*x := mul_pos hd hx
  have hpos : 0 < d*x-a := by omega
  let k : ℕ := (d*x-a).toNat
  have hk : (k:ℤ)=d*x-a := Int.toNat_of_nonneg (le_of_lt hpos)
  have hpow : d*x-a < (2:ℤ)^k := by rw [←hk]; exact pow_two_gt k
  have hdiv := matching_divisibility d hdodd k x a (h k)
  have hle : (2:ℤ)^k ≤ d*x-a := Int.le_of_dvd hpos hdiv
  omega

-- Finite rational residue transport, after clearing an odd denominator.
theorem signed_inverse_difference (d q z q' z' C : ℤ) (A b : ℕ)
    (hq : 2^A*q=3^b*q'+C)
    (hz : 2^A*z=3^b*z'+d*C) :
    3^b*(z'-d*q')=2^A*(z-d*q) := by
  linear_combination d*hq-hz

-- Sign of the complete cyclic multiplier; this uses the full carry.
theorem negative_cycle_multiplier (A P C a : ℤ)
    (ha : a < 0) (hC : 0 < C)
    (h : A*a=P*a+C) : A < P := by
  by_contra hn
  have hm : 0 ≤ (A-P)*(-a) :=
    mul_nonneg (by omega) (by omega)
  nlinarith only [h,hm,hC]

theorem positive_cycle_multiplier (A P C a : ℤ)
    (ha : 0 < a) (hC : 0 < C)
    (h : A*a=P*a+C) : P < A := by
  by_contra hn
  have hm : 0 ≤ (P-A)*a :=
    mul_nonneg (by omega) (le_of_lt ha)
  nlinarith only [h,hm,hC]

/- The full-statement proposal is conditional. RecordLock is the missing
fixed-source conclusion suggested by rational confinement + bounded record gaps.
CycleExclusion is the separate positive-cycle obligation. Neither is proved. -/
def EventuallyPeriodic (x : ℤ) : Prop :=
  ∃ i p : ℕ, 0 < p ∧ run 1 (i+p) x = run 1 i x

def RecordLock : Prop :=
  ∀ x : ℤ, 0 < x → ¬EventuallyPeriodic x →
    ∃ (s : ℕ) (d a : ℤ), 0 < d ∧ d % 2 = 1 ∧ a < 0 ∧
      ∀ k : ℕ, Matches d k (run 1 s x) a

def CycleExclusion : Prop :=
  ∀ x : ℤ, 0 < x → ∀ p : ℕ, 0 < p → run 1 p x=x →
    ∃ t : ℕ, run 1 t x=1

theorem collatz_of_record_lock_and_cycles
    (lock : RecordLock) (cycles : CycleExclusion) :
    ∀ x : ℤ, 0 < x → ∃ t : ℕ, run 1 t x=1 := by
  intro x hx
  classical
  by_cases hp : EventuallyPeriodic x
  · obtain ⟨i,p,hp,he⟩ := hp
    have hr : run 1 p (run 1 i x)=run 1 i x := by
      rw [←run_add,he]
    obtain ⟨t,ht⟩ := cycles (run 1 i x) (run_pos i x hx) p hp hr
    exact ⟨i+t,by rw [run_add,ht]⟩
  · obtain ⟨s,d,a,hd,ho,ha,hm⟩ := lock x hx hp
    exact False.elim (no_infinite_negative_match d (run 1 s x) a
      hd ho (run_pos s x hx) ha hm)

end CriticalRecordRigidity

#print axioms CriticalRecordRigidity.run_add
#print axioms CriticalRecordRigidity.run_pos
#print axioms CriticalRecordRigidity.cancel_three
#print axioms CriticalRecordRigidity.matching_divisibility
#print axioms CriticalRecordRigidity.no_infinite_negative_match
#print axioms CriticalRecordRigidity.signed_inverse_difference
#print axioms CriticalRecordRigidity.negative_cycle_multiplier
#print axioms CriticalRecordRigidity.positive_cycle_multiplier
#print axioms CriticalRecordRigidity.collatz_of_record_lock_and_cycles
