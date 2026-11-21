/-
Exact least-forward-failure geometry, extending the ψ-closure development.
Source interface: PR #174, 7034109ed60a26bc49824e1ed43c239ceca81194,
Collatz/Closure.lean. Lean 4.34.1; dependency-free beyond that interface.

This file proves reductions and minimal-counterexample structure only.
It does not prove either equivalent global closure condition below.
-/
import Collatz.Closure

open CollatzReverseBasin

namespace CollatzGlobal

/-- An actual failure of closure under the odd-child map. -/
def ForwardFailure (m : Nat) : Prop :=
  0 < m ∧ Basin m ∧ ¬ Basin (2*m-1)

/-- The same ordinary minimum is used in every child closure call. -/
def LeastForwardFailure (m : Nat) : Prop :=
  ForwardFailure m ∧ ∀ k, 0 < k → k < m → ¬ ForwardFailure k

/-- An actual least positive integer outside the basin. -/
def LeastBad (n : Nat) : Prop :=
  0 < n ∧ ¬ Basin n ∧ ∀ k, 0 < k → k < n → Basin k

private theorem basin_one : Basin 1 := ⟨0, rfl⟩

/-- Every smaller ordinary integer is known, with no loss in the height floor. -/
theorem exact_floor_of_least_forward_failure (m : Nat)
    (h : LeastForwardFailure m) :
    ∀ n : Nat, 0 < n → n < 2*m-1 → Basin n := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    intro hn hnm
    by_cases h1 : n = 1
    · subst n; exact basin_one
    by_cases he : n % 2 = 0
    · have hp : 0 < n/2 := by omega
      have hs : n/2 < n := by omega
      have hb : n/2 < 2*m-1 := by omega
      have good := ih (n/2) hs hp hb
      have eq : n = 2*(n/2) := by omega
      rw [eq]
      exact (CollatzClosure.basin_twice _).mpr good
    · have hp : 0 < (n+1)/2 := by omega
      have hs : (n+1)/2 < n := by omega
      have hm : (n+1)/2 < m := by omega
      have hb : (n+1)/2 < 2*m-1 := by omega
      have good := ih ((n+1)/2) hs hp hb
      have close : Basin (2*((n+1)/2)-1) := by
        apply Classical.byContradiction
        intro bad
        exact h.2 _ hp hm ⟨hp, good, bad⟩
      have eq : 2*((n+1)/2)-1 = n := by omega
      rwa [eq] at close

/-- The odd child of a least closure failure is the globally least bad integer. -/
theorem least_bad_of_least_forward_failure (m : Nat)
    (h : LeastForwardFailure m) : LeastBad (2*m-1) := by
  exact ⟨by have := h.1.1; omega, h.1.2.2,
    exact_floor_of_least_forward_failure m h⟩

/-- An ordinary least bad integer is odd. -/
theorem least_bad_odd (n : Nat) (h : LeastBad n) : n % 2 = 1 := by
  apply Classical.byContradiction
  intro hn
  have he : n % 2 = 0 := by omega
  have hn1 : n ≠ 1 := by
    intro e; subst n; exact h.2.1 basin_one
  have good : Basin (n/2) := h.2.2 _ (by have := h.1; omega) (by have := h.1; omega)
  have eq : n = 2*(n/2) := by omega
  have good' : Basin n := by rw [eq]; exact (CollatzClosure.basin_twice _).mpr good
  exact h.2.1 good'

/-- The standard one-step contracting residue leaves only 3 modulo 4. -/
theorem least_bad_mod_four (n : Nat) (h : LeastBad n) : n % 4 = 3 := by
  have odd := least_bad_odd n h
  have hn1 : n ≠ 1 := by
    intro e; subst n; exact h.2.1 basin_one
  apply Classical.byContradiction
  intro hn
  have hmod : n % 4 = 1 := by omega
  have eq : n = 4*(n/4)+1 := by omega
  have hp : 0 < 3*(n/4)+1 := by omega
  have hs : 3*(n/4)+1 < n := by omega
  have good := h.2.2 _ hp hs
  exact h.2.1 ((CollatzClosure.basin_exch n (3*(n/4)+1) (n/4) eq rfl).mpr good)

/-- Therefore the least odd-child closure failure has an even member arm. -/
theorem least_forward_failure_even (m : Nat) (h : LeastForwardFailure m) :
    m % 2 = 0 := by
  have hmod := least_bad_mod_four (2*m-1) (least_bad_of_least_forward_failure m h)
  have hp := h.1.1
  omega

/-- Conversely the parent of a least bad odd integer is a least closure failure. -/
theorem least_forward_failure_of_least_bad (n : Nat) (h : LeastBad n) :
    LeastForwardFailure ((n+1)/2) := by
  have odd := least_bad_odd n h
  have hn1 : n ≠ 1 := by
    intro e; subst n; exact h.2.1 basin_one
  have hp : 0 < (n+1)/2 := by have := h.1; omega
  have hs : (n+1)/2 < n := by have := h.1; omega
  have good := h.2.2 _ hp hs
  have eq : 2*((n+1)/2)-1 = n := by omega
  constructor
  · refine ⟨hp, good, ?_⟩
    rw [eq]
    exact h.2.1
  · intro k hk hkm fail
    have p : 0 < 2*k-1 := by omega
    have small : 2*k-1 < n := by omega
    exact fail.2.2 (h.2.2 _ p small)

/-- The two exact minimizations are equivalent, not merely boundedly comparable. -/
theorem least_forward_failure_iff (m : Nat) (hm : 0 < m) :
    LeastForwardFailure m ↔ LeastBad (2*m-1) := by
  constructor
  · exact least_bad_of_least_forward_failure m
  · intro h
    have hh := least_forward_failure_of_least_bad (2*m-1) h
    have eq : ((2*m-1)+1)/2 = m := by omega
    rwa [eq] at hh

/-- Existence of any ordinary counterexample gives this exact minimal closure state. -/
theorem exists_least_forward_failure
    (bad : ∃ n : Nat, 0 < n ∧ ¬ Basin n) :
    ∃ m : Nat, LeastForwardFailure m ∧ m % 2 = 0 := by
  classical
  have minimum : ∀ n : Nat, 0 < n → ¬ Basin n → ∃ k, LeastBad k := by
    intro n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro hn hbad
      by_cases hs : ∀ k, 0 < k → k < n → Basin k
      · exact ⟨n, hn, hbad, hs⟩
      · have smaller : ∃ k, 0 < k ∧ k < n ∧ ¬ Basin k := by
          apply Classical.byContradiction
          intro none
          apply hs
          intro k hk hkn
          apply Classical.byContradiction
          intro badk
          exact none ⟨k, hk, hkn, badk⟩
        obtain ⟨k, hk, hkn, badk⟩ := smaller
        exact ih k hkn hk badk
  obtain ⟨w, hw, bw⟩ := bad
  obtain ⟨n, least⟩ := minimum w hw bw
  have hf := least_forward_failure_of_least_bad n least
  exact ⟨(n+1)/2, hf, least_forward_failure_even _ hf⟩

/-- This is the remaining even state, transported without any conjectural closure. -/
theorem even_failure_normal_form (t : Nat) (ht : 0 < t) :
    ForwardFailure (2*t) ↔ (Basin t ∧ ¬ Basin (9*t-1)) := by
  have left := CollatzClosure.basin_twice t
  have right := CollatzClosure.basin_pow_two_pred 2 t ht
  have eq2 : 2^2*t-1 = 2*(2*t)-1 := by omega
  have eq3 : 3^2*t-1 = 9*t-1 := by omega
  rw [eq2, eq3] at right
  unfold ForwardFailure
  rw [left, right]
  constructor
  · exact fun h => h.2
  · intro h; exact ⟨by omega, h⟩

/-- Exact inverse-edge transport of the unrestricted forward closure question.
The higher ternary multiplier is retained, rather than treated as a known basin operation. -/
theorem odd_edge_forward_transport (x t a : Nat)
    (hx : x % 2 = 1) (ht : 0 < t) (ha : 0 < a)
    (edge : 3*x+1 = 2^a*t) :
    Basin (3*x-1) ↔ Basin (3^(a-1)*t-1) := by
  have ePow : 2^a = 2*2^(a-1) := by
    have e : a = (a-1)+1 := by omega
    calc
      2^a = 2^((a-1)+1) := congrArg (fun z => 2^z) e
      _ = 2^(a-1)*2 := Nat.pow_succ ..
      _ = 2*2^(a-1) := Nat.mul_comm ..
  have pos : 0 < 2^(a-1)*t := Nat.mul_pos (Nat.pow_pos (by omega)) ht
  have hxpos : 0 < x := by omega
  have eq : 3*x-1 = 2*(2^(a-1)*t-1) := by
    rw [ePow] at edge
    have eqmul : (2*2^(a-1))*t = 2*(2^(a-1)*t) := by grind
    rw [eqmul] at edge
    omega
  rw [eq]
  exact (CollatzClosure.basin_twice _).trans
    (CollatzClosure.basin_pow_two_pred (a-1) t ht)

/-- The even member arms alone already contain every possible least failure. -/
theorem collatz_iff_nine_minus_one_closure :
    (∀ n : Nat, 0 < n → Basin n) ↔
    (∀ t : Nat, 0 < t → Basin t → Basin (9*t-1)) := by
  constructor
  · intro all t ht _
    exact all _ (by omega)
  · intro close n hn
    apply Classical.byContradiction
    intro bad
    obtain ⟨m, hmin, he⟩ := exists_least_forward_failure ⟨n, hn, bad⟩
    have hm : 0 < m := hmin.1.1
    have ht : 0 < m/2 := by omega
    have eq : m = 2*(m/2) := by omega
    have fail : ForwardFailure (2*(m/2)) := by rw [← eq]; exact hmin.1
    have reduced := (even_failure_normal_form (m/2) ht).mp fail
    exact reduced.2 (close _ ht reduced.1)

/-- Exact global floor for the remaining even state. This is an equivalence of
minimal counterexample configurations, not a proof that either side is inhabited. -/
theorem least_even_failure_iff (t : Nat) (ht : 0 < t) :
    LeastForwardFailure (2*t) ↔
      (¬ Basin (9*t-1) ∧ ∀ n : Nat, 0 < n → n < 4*t-1 → Basin n) := by
  have e : 2*(2*t)-1 = 4*t-1 := by omega
  have transport := CollatzClosure.basin_pow_two_pred 2 t ht
  have e2 : 2^2*t-1 = 4*t-1 := by omega
  have e3 : 3^2*t-1 = 9*t-1 := by omega
  rw [e2, e3] at transport
  rw [least_forward_failure_iff (2*t) (by omega), e]
  unfold LeastBad
  rw [transport]
  constructor
  · exact fun h => h.2
  · intro h; exact ⟨by omega, h⟩

/-- Full convergence is equivalent to filling this one precise gap above each
known initial interval. The right side is left as an explicit open obligation. -/
theorem collatz_iff_exact_even_gap :
    (∀ n : Nat, 0 < n → Basin n) ↔
      (∀ t : Nat, 0 < t →
        (∀ n : Nat, 0 < n → n < 4*t-1 → Basin n) → Basin (9*t-1)) := by
  constructor
  · intro all t ht _
    exact all _ (by omega)
  · intro gap n hn
    apply Classical.byContradiction
    intro bad
    obtain ⟨m, hmin, he⟩ := exists_least_forward_failure ⟨n, hn, bad⟩
    have hm : 0 < m := hmin.1.1
    have ht : 0 < m/2 := by omega
    have eq : m = 2*(m/2) := by omega
    rw [eq] at hmin
    have reduced := (least_even_failure_iff (m/2) ht).mp hmin
    exact reduced.1 (gap _ ht reduced.2)

theorem basin_two_pow (s : Nat) : Basin (2^s) := by
  induction s with
  | zero => exact basin_one
  | succ s ih =>
    have e : 2^(s+1) = 2*(2^s) := by grind
    rw [e]
    exact (CollatzClosure.basin_twice _).mpr ih

/-- Exhausting a source certificate consisting only of halvings does not make
the transported target trivial: its exact residual is a ternary power minus one. -/
theorem power_two_forward_failure_iff (s : Nat) :
    ForwardFailure (2^s) ↔ ¬ Basin (3^(s+1)-1) := by
  have hp : 0 < 2^s := Nat.pow_pos (by omega)
  have good := basin_two_pow s
  have e : 2*(2^s)-1 = 2^(s+1)*1-1 := by grind
  have transport := CollatzClosure.basin_pow_two_pred (s+1) 1 (by omega)
  have e3 : 3^(s+1)*1-1 = 3^(s+1)-1 := by omega
  rw [e3] at transport
  unfold ForwardFailure
  rw [e, transport]
  exact ⟨fun h => h.2.2, fun h => ⟨hp, good, h⟩⟩

/-- The same unbounded terminal family occurs in the reduced even-source target. -/
theorem nine_on_powers_two (s : Nat) :
    Basin (9*2^s-1) ↔ Basin (3^(s+2)-1) := by
  have transport := CollatzClosure.basin_pow_two_pred s 9 (by omega)
  have e2 : 2^s*9-1 = 9*2^s-1 := by grind
  have e3 : 3^s*9-1 = 3^(s+2)-1 := by grind
  rwa [e2, e3] at transport

end CollatzGlobal
