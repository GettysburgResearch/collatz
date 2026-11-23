/-!
An ordinary-source budget for independently repeated affine Collatz blocks.

The final theorem applies to the actual shortcut orbit.  Its certificate
hypotheses are the exact repeated-block affine identities, nonzero defects,
and a common bound on the block coefficients.  No cycle-exclusion premise,
logarithmic-form theorem, or Collatz conjecture is an axiom here.

The companion ARITHMETIC_CLOSURE.md derives these identities for arbitrary
fixed parity blocks and combines this finite integral budget with an external
explicit two-logarithm bound.  That analytic combination is a written theorem,
not a claim about the scope of this Lean module.
-/

namespace CollatzIndependentBlockBudget

def step (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def orbit : Nat → Nat → Nat
  | 0, n => n
  | k + 1, n => orbit k (step n)

private theorem step_height (n : Nat) : 2 * (step n + 1) ≤ 3 * (n + 1) := by
  unfold step
  split <;> omega

private theorem orbit_height (n k : Nat) :
    2 ^ k * (orbit k n + 1) ≤ 3 ^ k * (n + 1) := by
  induction k generalizing n with
  | zero => simp [orbit]
  | succ k ih =>
    calc
      2 ^ (k + 1) * (orbit (k + 1) n + 1) =
          2 * (2 ^ k * (orbit k (step n) + 1)) := by
        simp [orbit, Nat.pow_succ, Nat.mul_left_comm, Nat.mul_comm]
      _ ≤ 2 * (3 ^ k * (step n + 1)) := Nat.mul_le_mul_left 2 (ih (step n))
      _ = 3 ^ k * (2 * (step n + 1)) := by
        simp [Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]
      _ ≤ 3 ^ k * (3 * (n + 1)) := Nat.mul_le_mul_left _ (step_height n)
      _ = 3 ^ (k + 1) * (n + 1) := by simp [Nat.pow_succ, Nat.mul_assoc]

/-- A nonfixed repeated affine block spends binary divisibility from its
actual incoming ordinary source.  `m` is its total shortcut clock and `k`
its total odd-step count. -/
theorem nonfixed_block_cap {m k n y C : Nat} {D : Int}
    (identity : (2 : Int) ^ m * (D * y - C) =
      (3 : Int) ^ k * (D * n - C))
    (nonfixed : D * n - C ≠ 0) :
    2 ^ m ≤ (D.natAbs + C) * (n + 1) := by
  have div : (2 : Int) ^ m ∣ (3 : Int) ^ k * (D * n - C) := by
    exact ⟨D * y - C, identity.symm⟩
  have absdiv : 2 ^ m ∣ 3 ^ k * (D * n - C).natAbs := by
    simpa [Int.natAbs_mul, Int.natAbs_pow] using Int.natAbs_dvd_natAbs.mpr div
  have cop : Nat.Coprime (2 ^ m) (3 ^ k) :=
    Nat.Coprime.pow_left m (Nat.Coprime.pow_right k (by decide : Nat.Coprime 2 3))
  have d : 2 ^ m ∣ (D * n - C).natAbs := cop.dvd_of_dvd_mul_left absdiv
  have lower : 2 ^ m ≤ (D * n - C).natAbs :=
    Nat.le_of_dvd (Int.natAbs_pos.mpr nonfixed) d
  have upper : (D * n - C).natAbs ≤ D.natAbs * n + C := by
    simpa [Int.natAbs_mul] using Int.natAbs_sub_le (D * n) (C : Int)
  have finish : D.natAbs * n + C ≤ (D.natAbs + C) * (n + 1) := by
    simp only [Nat.add_mul, Nat.mul_add, Nat.mul_one]
    omega
  exact Nat.le_trans lower (Nat.le_trans upper finish)

/-- A segment whose binary clock is paid by its source can at most square
the common scaled height.  This concerns the actual ordinary map. -/
theorem ordinary_segment_quadratic {K n m : Nat}
    (cap : 2 ^ m ≤ K * (n + 1)) :
    K * (orbit m n + 1) ≤ (K * (n + 1)) ^ 2 := by
  have two_pos : 0 < 2 ^ m := Nat.pow_pos (by decide : 0 < 2)
  have coarse : 3 ^ m ≤ 2 ^ m * 2 ^ m := by
    calc
      3 ^ m ≤ 4 ^ m := Nat.pow_le_pow_left (by decide : 3 ≤ 4) m
      _ = 2 ^ m * 2 ^ m := by rw [show (4 : Nat) = 2 * 2 by decide, Nat.mul_pow]
  have mulbound : 2 ^ m * (orbit m n + 1) ≤ 2 ^ m * (2 ^ m * (n + 1)) := by
    exact Nat.le_trans (orbit_height n m)
      (by simpa [Nat.mul_assoc] using Nat.mul_le_mul_right (n + 1) coarse)
  have height : orbit m n + 1 ≤ 2 ^ m * (n + 1) :=
    Nat.le_of_mul_le_mul_left mulbound two_pos
  calc
    K * (orbit m n + 1) ≤ K * (2 ^ m * (n + 1)) := Nat.mul_le_mul_left K height
    _ ≤ K * (K * (n + 1) * (n + 1)) :=
      Nat.mul_le_mul_left K (Nat.mul_le_mul_right (n + 1) cap)
    _ = (K * (n + 1)) ^ 2 := by
      simp [Nat.pow_succ, Nat.mul_left_comm, Nat.mul_comm]

def clockSum : List Nat → Nat
  | [] => 0
  | m :: ms => m + clockSum ms

def ClockBudget (K : Nat) : List Nat → Nat → Prop
  | [], _ => True
  | m :: ms, n => 2 ^ m ≤ K * (n + 1) ∧ ClockBudget K ms (orbit m n)

private def slots : Nat → Nat
  | 0 => 0
  | r + 1 => 1 + 2 * slots r

private theorem slots_succ (r : Nat) : slots r + 1 = 2 ^ r := by
  induction r with
  | zero => simp [slots]
  | succ r ih =>
    simp only [slots, Nat.pow_succ]
    omega

private theorem budget_slots {K n : Nat} {ms : List Nat}
    (budget : ClockBudget K ms n) :
    2 ^ clockSum ms ≤ (K * (n + 1)) ^ slots ms.length := by
  induction ms generalizing n with
  | nil => simp [clockSum, slots]
  | cons m ms ih =>
    obtain ⟨cap, tail⟩ := budget
    have suffix := ih tail
    have square := ordinary_segment_quadratic cap
    calc
      2 ^ clockSum (m :: ms) = 2 ^ m * 2 ^ clockSum ms := by
        simp [clockSum, Nat.pow_add]
      _ ≤ (K * (n + 1)) * (K * (orbit m n + 1)) ^ slots ms.length :=
        Nat.mul_le_mul cap suffix
      _ ≤ (K * (n + 1)) * ((K * (n + 1)) ^ 2) ^ slots ms.length :=
        Nat.mul_le_mul_left _ (Nat.pow_le_pow_left square _)
      _ = (K * (n + 1)) ^ slots (m :: ms).length := by
        simp [slots, Nat.pow_add, Nat.pow_mul]

/-- Every independently certified block is paid from one original source.
The exponent grows with the number of blocks, not their repetition counts. -/
theorem source_clock_budget {K n : Nat} {ms : List Nat}
    (budget : ClockBudget K ms n) :
    2 ^ clockSum ms ≤ (K * (n + 1)) ^ (2 ^ ms.length - 1) := by
  have e : slots ms.length = 2 ^ ms.length - 1 := by
    have h := slots_succ ms.length
    omega
  simpa [e] using budget_slots budget

/-- A list of ordinary segments carrying the exact repeated-block identities.
The coefficient bound is common; the blocks and repetitions may differ. -/
inductive CertifiedChain (K : Nat) : List Nat → Nat → Prop
  | nil (n : Nat) : CertifiedChain K [] n
  | cons {m : Nat} {ms : List Nat} {n C k : Nat} {D : Int}
      (coefficient : D.natAbs + C ≤ K)
      (identity : (2 : Int) ^ m * (D * orbit m n - C) =
        (3 : Int) ^ k * (D * n - C))
      (nonfixed : D * n - C ≠ 0)
      (tail : CertifiedChain K ms (orbit m n)) :
      CertifiedChain K (m :: ms) n

/-- The full integral resource theorem from actual-source block certificates.
No asymptotic bound, cycle claim, or ordinary-realization axiom is assumed. -/
theorem independent_block_budget {K n : Nat} {ms : List Nat}
    (certificate : CertifiedChain K ms n) :
    2 ^ clockSum ms ≤ (K * (n + 1)) ^ (2 ^ ms.length - 1) := by
  apply source_clock_budget
  induction certificate with
  | nil => trivial
  | cons coefficient identity nonfixed tail ih =>
    exact ⟨Nat.le_trans (nonfixed_block_cap identity nonfixed)
      (Nat.mul_le_mul_right _ coefficient), ih⟩

#print axioms nonfixed_block_cap
#print axioms ordinary_segment_quadratic
#print axioms source_clock_budget
#print axioms independent_block_budget

end CollatzIndependentBlockBudget
