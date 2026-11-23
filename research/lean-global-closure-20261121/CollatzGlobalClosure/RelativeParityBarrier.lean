import Mathlib.Tactic

/-!
# A deterministic relative-parity route to forward-five closure

This file proves an all-time barrier for every hypothetical positive orbit
which never reaches one.  The final closure theorem is conditional on the
explicit `RelativeBudgetReturns` statement; this statement is not proved here.
There are no probabilistic premises or invented axioms.
-/

set_option autoImplicit false
set_option maxHeartbeats 2000000

namespace CollatzRelativeParity

def step (n : ℕ) : ℕ :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def orbit (n : ℕ) : ℕ → ℕ
  | 0 => n
  | t + 1 => step (orbit n t)

def oddBit (n : ℕ) : ℕ := if n % 2 = 0 then 0 else 1

def oddCount (n : ℕ) : ℕ → ℕ
  | 0 => 0
  | t + 1 => oddCount n t + oddBit (orbit n t)

def ReachesOne (n : ℕ) : Prop := ∃ t, orbit n t = 1

theorem step_pos {n : ℕ} (hn : 0 < n) : 0 < step n := by
  unfold step
  split_ifs <;> omega

theorem orbit_pos {n : ℕ} (hn : 0 < n) (t : ℕ) : 0 < orbit n t := by
  induction t with
  | zero => exact hn
  | succ t ih => exact step_pos ih

theorem orbit_add (n s t : ℕ) : orbit n (s + t) = orbit (orbit n s) t := by
  induction t with
  | zero => simp [orbit]
  | succ t ih => simpa [orbit, Nat.add_assoc] using congrArg step ih

theorem oddCount_add (n s t : ℕ) :
    oddCount n (s + t) = oddCount n s + oddCount (orbit n s) t := by
  induction t with
  | zero => simp [oddCount]
  | succ t ih => simp [oddCount, orbit_add, ih, Nat.add_assoc]

theorem one_even (m : ℕ) : orbit 1 (2 * m) = 1 ∧ oddCount 1 (2 * m) = m := by
  induction m with
  | zero => simp [orbit, oddCount]
  | succ m ih =>
    have hh : 2 * (m + 1) = (2 * m + 1) + 1 := by omega
    rw [hh]
    norm_num [orbit, oddCount, oddBit, step, ih.1, ih.2]

theorem one_count_bound (t : ℕ) : 2 * oddCount 1 t ≤ t + 1 := by
  have hmod : t % 2 = 0 ∨ t % 2 = 1 := by omega
  rcases hmod with h | h
  · have ht : t = 2 * (t / 2) := by omega
    rw [ht, (one_even (t / 2)).2]
    omega
  · have ht : t = 2 * (t / 2) + 1 := by omega
    rw [ht]
    have hp := one_even (t / 2)
    norm_num [oddCount, oddBit, hp.1, hp.2]
    omega

theorem certified_source_count {x d : ℕ} (hd : orbit x d = 1) (m : ℕ) :
    oddCount x (d + 2 * m) = oddCount x d + m := by
  rw [oddCount_add, hd, (one_even m).2]

private theorem quartic_odd_bound {v : ℕ} (hv : 3 ≤ v) :
    (3 * v + 1) ^ 4 ≤ 128 * v ^ 4 := by
  obtain ⟨a, rfl⟩ := Nat.exists_eq_add_of_le hv
  have hpoly :
      128 * (3 + a) ^ 4 = (3 * (3 + a) + 1) ^ 4 +
        (47 * a ^ 4 + 456 * a ^ 3 + 1512 * a ^ 2 + 1824 * a + 368) := by ring
  rw [hpoly]
  omega

theorem step_quartic_bound {v : ℕ} (hv : 0 < v) (hne : v ≠ 1) :
    16 * (step v) ^ 4 ≤ 2 ^ (7 * oddBit v) * v ^ 4 := by
  by_cases hpar : v % 2 = 0
  · have heq : 2 * step v = v := by simp [step, hpar]; omega
    have hp := congrArg (fun z : ℕ => z ^ 4) heq
    norm_num [mul_pow] at hp
    simpa [oddBit, hpar] using hp.le
  · have heq : 2 * step v = 3 * v + 1 := by
      simp [step, hpar]
      omega
    have hv3 : 3 ≤ v := by omega
    have hp := congrArg (fun z : ℕ => z ^ 4) heq
    norm_num [mul_pow] at hp
    simpa [oddBit, hpar, hp] using quartic_odd_bound hv3

theorem finite_no_hit_growth {n t : ℕ} (hn : 0 < n)
    (hno : ∀ j, j ≤ t → orbit n j ≠ 1) :
    2 ^ (4 * t) * (orbit n t) ^ 4 ≤ 2 ^ (7 * oddCount n t) * n ^ 4 := by
  induction t with
  | zero => simp [orbit, oddCount]
  | succ t ih =>
    have hi := ih (fun j hj => hno j (by omega))
    have hs := step_quartic_bound (orbit_pos hn t) (hno t (by omega))
    have ht : 4 * (t + 1) = 4 * t + 4 := by omega
    calc
      2 ^ (4 * (t + 1)) * (orbit n (t + 1)) ^ 4 =
          2 ^ (4 * t) * (16 * (step (orbit n t)) ^ 4) := by
            rw [ht, pow_add]
            norm_num [orbit]
            ring
      _ ≤ 2 ^ (4 * t) * (2 ^ (7 * oddBit (orbit n t)) * (orbit n t) ^ 4) :=
        Nat.mul_le_mul_left _ hs
      _ = 2 ^ (7 * oddBit (orbit n t)) *
          (2 ^ (4 * t) * (orbit n t) ^ 4) := by ring
      _ ≤ 2 ^ (7 * oddBit (orbit n t)) *
          (2 ^ (7 * oddCount n t) * n ^ 4) := Nat.mul_le_mul_left _ hi
      _ = 2 ^ (7 * oddCount n (t + 1)) * n ^ 4 := by
        rw [oddCount, Nat.mul_add, pow_add]
        ring

theorem nonconvergent_barrier {n : ℕ} (hn : 0 < n) (hbad : ¬ ReachesOne n)
    (t : ℕ) : 2 ^ (4 * t) ≤ 2 ^ (7 * oddCount n t) * n ^ 4 := by
  have hno : ∀ j, j ≤ t → orbit n j ≠ 1 := by
    intro j _ hj
    exact hbad ⟨j, hj⟩
  have hp := finite_no_hit_growth hn hno
  have hv : 0 < (orbit n t) ^ 4 := pow_pos (orbit_pos hn t) _
  exact (Nat.le_mul_of_pos_right _ (by omega)).trans hp

private theorem fourth_strict {a b : ℕ} (h : a < b) : a ^ 4 < b ^ 4 := by
  calc
    a ^ 4 < a ^ 4 + (4 * a ^ 3 + 6 * a ^ 2 + 4 * a + 1) := by omega
    _ = (a + 1) ^ 4 := by ring
    _ ≤ b ^ 4 := Nat.pow_le_pow_left (by omega) 4

theorem converges_of_parity_budget {n t B : ℕ} (hn : 0 < n)
    (hsize : n < 2 ^ B) (hbudget : 7 * oddCount n t + 4 * B ≤ 4 * t) :
    ReachesOne n := by
  by_contra hbad
  have hb := nonconvergent_barrier hn hbad t
  have hfour : n ^ 4 < 2 ^ (4 * B) := by
    have hh := fourth_strict hsize
    simpa [← pow_mul, Nat.mul_comm] using hh
  have hupper : 2 ^ (7 * oddCount n t) * n ^ 4 <
      2 ^ (7 * oddCount n t + 4 * B) := by
    rw [pow_add]
    exact Nat.mul_lt_mul_of_pos_left hfour (by positivity)
  have hlower : 2 ^ (7 * oddCount n t + 4 * B) ≤ 2 ^ (4 * t) :=
    Nat.pow_le_pow_right (by decide) hbudget
  exact (not_lt_of_ge hb) (hupper.trans_le hlower)

private theorem self_lt_two_pow (n : ℕ) : n < 2 ^ n := by
  induction n with
  | zero => norm_num
  | succ n ih => rw [pow_succ]; omega

/-- A single deterministic source-relative budget check suffices. -/
theorem five_converges_of_relative_budget {x d m : ℕ} (hx : 0 < x)
    (hd : orbit x d = 1)
    (hlarge : 56 * oddCount x d + 160 * x ≤ m)
    (hbudget : 16 * oddCount (5 * x) (d + 2 * m) ≤
      16 * oddCount x (d + 2 * m) + (d + 2 * m)) :
    ReachesOne (5 * x) := by
  apply converges_of_parity_budget (t := d + 2 * m) (by omega) (self_lt_two_pow (5 * x))
  rw [certified_source_count hd m] at hbudget
  omega

/-- The remaining universal statement: repeated relative-budget returns
    along the actual ordinary pair, with its supplied source witness. -/
def RelativeBudgetReturns : Prop :=
  ∀ x d, 0 < x → orbit x d = 1 → ∀ H, ∃ m, H ≤ m ∧
    16 * oddCount (5 * x) (d + 2 * m) ≤
      16 * oddCount x (d + 2 * m) + (d + 2 * m)

def ForwardFiveClosure : Prop :=
  ∀ x, 0 < x → ReachesOne x → ReachesOne (5 * x)

theorem forward_five_of_relative_budget_returns
    (hreturns : RelativeBudgetReturns) : ForwardFiveClosure := by
  intro x hx hcert
  obtain ⟨d, hd⟩ := hcert
  obtain ⟨m, hm, hb⟩ := hreturns x d hx hd (56 * oddCount x d + 160 * x)
  exact five_converges_of_relative_budget hx hd hm hb

theorem relative_budget_returns_of_forward_five
    (hfive : ForwardFiveClosure) : RelativeBudgetReturns := by
  intro x d hx hd H
  obtain ⟨e, he⟩ := hfive x hx ⟨d, hd⟩
  let q := oddCount (5 * x) e
  let m := H + e + 16 * (q + d + 1)
  refine ⟨m, by omega, ?_⟩
  have ht : e ≤ d + 2 * m := by dsimp [m]; omega
  obtain ⟨s, hs⟩ := Nat.exists_eq_add_of_le ht
  have hcount : oddCount (5 * x) (d + 2 * m) = q + oddCount 1 s := by
    rw [hs, oddCount_add, he]
  have htail := one_count_bound s
  rw [hcount, certified_source_count hd m]
  dsimp [m]
  omega

theorem forward_five_iff_relative_budget_returns :
    ForwardFiveClosure ↔ RelativeBudgetReturns := by
  exact ⟨relative_budget_returns_of_forward_five, forward_five_of_relative_budget_returns⟩

#print axioms step_pos
#print axioms orbit_pos
#print axioms orbit_add
#print axioms oddCount_add
#print axioms one_even
#print axioms one_count_bound
#print axioms certified_source_count
#print axioms quartic_odd_bound
#print axioms step_quartic_bound
#print axioms finite_no_hit_growth
#print axioms nonconvergent_barrier
#print axioms fourth_strict
#print axioms converges_of_parity_budget
#print axioms self_lt_two_pow
#print axioms five_converges_of_relative_budget
#print axioms forward_five_of_relative_budget_returns
#print axioms relative_budget_returns_of_forward_five
#print axioms forward_five_iff_relative_budget_returns

end CollatzRelativeParity
