import Std

set_option autoImplicit false

/-!
An exact integration target, not an unconditional proof of Collatz.
The final theorem requires a successful certificate at EVERY q > 1.
No finite search, average estimate, or unproved analytic assertion is
substituted for that coverage hypothesis.
-/
namespace UniversalProposal

def step (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3*n+1)/2

def run : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => run k (step n)

def Converges (n : Nat) : Prop := ∃ k, run k n = 1

def Collatz : Prop := ∀ n, 0 < n → Converges n

def Meets (n m : Nat) : Prop := ∃ i j, run i n = run j m

theorem converges_one : Converges 1 := ⟨0, rfl⟩

theorem converges_three : Converges 3 := ⟨5, by decide⟩

theorem converges_step (n : Nat) : Converges (step n) ↔ Converges n := by
  constructor
  · rintro ⟨k, hk⟩
    exact ⟨k+1, hk⟩
  · rintro ⟨k, hk⟩
    cases k with
    | zero =>
      have hn : n = 1 := hk
      rw [hn]
      exact ⟨1, by decide⟩
    | succ k => exact ⟨k, hk⟩

theorem converges_run (k n : Nat) :
    Converges (run k n) ↔ Converges n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact (ih (step n)).trans (converges_step n)

theorem converges_of_meets {n m : Nat}
    (h : Meets n m) (hm : Converges m) : Converges n := by
  obtain ⟨i, j, same⟩ := h
  apply (converges_run i n).mp
  rw [same]
  exact (converges_run j m).mpr hm

private theorem even_step (n : Nat) : step (2*n) = n := by
  unfold step
  split <;> omega

private theorem odd_step (n : Nat) : step (2*n+1) = 3*n+2 := by
  unfold step
  split <;> omega

private theorem lift_one (t : Nat) : run 6 (192*t+21) = 9*t+1 := by
  have a : step (192*t+21) = 288*t+32 := by unfold step; split <;> omega
  have b : step (288*t+32) = 144*t+16 := by unfold step; split <;> omega
  have c : step (144*t+16) = 72*t+8 := by unfold step; split <;> omega
  have d : step (72*t+8) = 36*t+4 := by unfold step; split <;> omega
  have e : step (36*t+4) = 18*t+2 := by unfold step; split <;> omega
  have f : step (18*t+2) = 9*t+1 := by unfold step; split <;> omega
  simp only [run, a, b, c, d, e, f]

private theorem lift_two (t : Nat) : run 5 (96*t+21) = 9*t+2 := by
  have a : step (96*t+21) = 144*t+32 := by unfold step; split <;> omega
  have b : step (144*t+32) = 72*t+16 := by unfold step; split <;> omega
  have c : step (72*t+16) = 36*t+8 := by unfold step; split <;> omega
  have d : step (36*t+8) = 18*t+4 := by unfold step; split <;> omega
  have e : step (18*t+4) = 9*t+2 := by unfold step; split <;> omega
  simp only [run, a, b, c, d, e]

private theorem lift_four (t : Nat) : run 4 (48*t+21) = 9*t+4 := by
  have a : step (48*t+21) = 72*t+32 := by unfold step; split <;> omega
  have b : step (72*t+32) = 36*t+16 := by unfold step; split <;> omega
  have c : step (36*t+16) = 18*t+8 := by unfold step; split <;> omega
  have d : step (18*t+8) = 9*t+4 := by unfold step; split <;> omega
  simp only [run, a, b, c, d]

private theorem lift_five (t : Nat) : run 1 (6*t+3) = 9*t+5 := by
  simp only [run]
  unfold step
  split <;> omega

private theorem lift_seven (t : Nat) : run 2 (12*t+9) = 9*t+7 := by
  have a : step (12*t+9) = 18*t+14 := by unfold step; split <;> omega
  have b : step (18*t+14) = 9*t+7 := by unfold step; split <;> omega
  simp only [run, a, b]

private theorem lift_eight (t : Nat) : run 3 (24*t+21) = 9*t+8 := by
  have a : step (24*t+21) = 36*t+32 := by unfold step; split <;> omega
  have b : step (36*t+32) = 18*t+16 := by unfold step; split <;> omega
  have c : step (18*t+16) = 9*t+8 := by unfold step; split <;> omega
  simp only [run, a, b, c]

/-- Every positive ordinary value has an ordinary multiple-of-three
ancestor, with a literal shortcut clock of at most six. -/
theorem multiple_ancestor (n : Nat) (hn : 0 < n) :
    ∃ q k, 0 < q ∧ k ≤ 6 ∧ run k (3*q) = n := by
  by_cases h : n % 3 = 0
  · refine ⟨n/3, 0, by omega, by omega, ?_⟩
    simp only [run]
    omega
  · have residues : n%9=1 ∨ n%9=2 ∨ n%9=4 ∨
        n%9=5 ∨ n%9=7 ∨ n%9=8 := by omega
    rcases residues with r | r | r | r | r | r
    · refine ⟨64*(n/9)+7, 6, by omega, by omega, ?_⟩
      have e : 3*(64*(n/9)+7) = 192*(n/9)+21 := by omega
      rw [e, lift_one]
      omega
    · refine ⟨32*(n/9)+7, 5, by omega, by omega, ?_⟩
      have e : 3*(32*(n/9)+7) = 96*(n/9)+21 := by omega
      rw [e, lift_two]
      omega
    · refine ⟨16*(n/9)+7, 4, by omega, by omega, ?_⟩
      have e : 3*(16*(n/9)+7) = 48*(n/9)+21 := by omega
      rw [e, lift_four]
      omega
    · refine ⟨2*(n/9)+1, 1, by omega, by omega, ?_⟩
      have e : 3*(2*(n/9)+1) = 6*(n/9)+3 := by omega
      rw [e, lift_five]
      omega
    · refine ⟨4*(n/9)+3, 2, by omega, by omega, ?_⟩
      have e : 3*(4*(n/9)+3) = 12*(n/9)+9 := by omega
      rw [e, lift_seven]
      omega
    · refine ⟨8*(n/9)+7, 3, by omega, by omega, ?_⟩
      have e : 3*(8*(n/9)+7) = 24*(n/9)+21 := by omega
      rw [e, lift_eight]
      omega

/-- The unresolved pointwise requirement. Both clocks are free, but the
same supplied source and a strictly smaller multiple must actually meet. -/
def TripleMergerDescent : Prop :=
  ∀ q, 1 < q → ∃ v, 0 < v ∧ v < q ∧ Meets (3*q) (3*v)

theorem collatz_of_triple_descent (descent : TripleMergerDescent) : Collatz := by
  have all_triples : ∀ q, 0 < q → Converges (3*q) := by
    intro q
    induction q using Nat.strongRecOn with
    | ind q ih =>
      intro hq
      by_cases base : q = 1
      · simpa only [base] using converges_three
      · obtain ⟨v, hv, hlt, hm⟩ := descent q (by omega)
        exact converges_of_meets hm (ih v hlt hv)
  intro n hn
  obtain ⟨q, k, hq, _, reaches⟩ := multiple_ancestor n hn
  rw [← reaches]
  exact (converges_run k (3*q)).mpr (all_triples q hq)

theorem collatz_iff_triple_descent : Collatz ↔ TripleMergerDescent := by
  constructor
  · intro full q hq
    obtain ⟨k, hk⟩ := full (3*q) (by omega)
    refine ⟨1, by omega, hq, k, 5, ?_⟩
    exact hk
  · exact collatz_of_triple_descent

structure Certificate where
  smaller : Nat
  sourceClock : Nat
  smallerClock : Nat
deriving Repr, DecidableEq

/-- A terminating, exact checker of one finite ordinary descent witness. -/
def check (q : Nat) (c : Certificate) : Bool :=
  decide (0 < c.smaller ∧ c.smaller < q ∧
    run c.sourceClock (3*q) = run c.smallerClock (3*c.smaller))

theorem check_sound (q : Nat) (c : Certificate) (h : check q c = true) :
    0 < c.smaller ∧ c.smaller < q ∧ Meets (3*q) (3*c.smaller) := by
  have valid : 0 < c.smaller ∧ c.smaller < q ∧
      run c.sourceClock (3*q) = run c.smallerClock (3*c.smaller) :=
    of_decide_eq_true h
  exact ⟨valid.1, valid.2.1, c.sourceClock, c.smallerClock, valid.2.2⟩

/-- Final integration theorem. The coverage argument is not supplied
in this packet; writing a selector without proving coverage is insufficient. -/
theorem certified_collatz (selector : Nat → Certificate)
    (coverage : ∀ q, 1 < q → check q (selector q) = true) :
    ∀ n, 0 < n → ∃ k, run k n = 1 := by
  apply collatz_of_triple_descent
  intro q hq
  exact ⟨(selector q).smaller, check_sound q (selector q) (coverage q hq)⟩

#print axioms converges_one
#print axioms converges_three
#print axioms converges_step
#print axioms converges_run
#print axioms converges_of_meets
#print axioms multiple_ancestor
#print axioms collatz_of_triple_descent
#print axioms collatz_iff_triple_descent
#print axioms check_sound
#print axioms certified_collatz

end UniversalProposal
