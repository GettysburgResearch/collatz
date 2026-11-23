module

public import Mathlib.Basic.Real.Basic
public import Mathlib.Order.Interval.Finset.Nat
public import Mathlib.Algebra.BigOperators.Group.Finset.Basic
public import Mathlib.Algebra.BigOperators.Ring.Finset
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring

@[expose] public section

/-!
# All-clock first-upcrossing bounds

This module uses the actual shortcut Collatz map.  A source below a floor
first crosses upwards, remains above that floor, and first hits a supplied
target.  Its hitting clock is unrestricted.  First hitting makes the clock
unique, including for periodic targets.

The entire late boundary is a finite set of physical sources in a narrow
height interval, and is contained in the native no-descent set.  The main
bound charges its word coefficients once per source.  It does not charge
an endpoint's unknown potential as though that potential were one.

The elementary external-to-this-module estimate for the cardinality of the
native no-descent set is a written input in the companion note, not a Lean
axiom.  The formal cardinality interface is explicit.
-/

namespace CollatzFirstCrossing

def step (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3*n+1)/2

def run : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => run k (step n)

def oddCount : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, n => (if n % 2 = 0 then 0 else 1) + oddCount k (step n)

noncomputable def coefficient (k n : Nat) : Real :=
  (3:Real)^(oddCount k n)/(2:Real)^k

def NoDescent (N n : Nat) : Prop :=
  ∀ k, k ≤ N → n ≤ run k n

structure FirstUpcrossing (H q n A : Nat) : Prop where
  source_pos : 0 < n
  source_lt : n < H
  clock_pos : 0 < A
  endpoint : run A n = q
  high : ∀ k, 0 < k → k ≤ A → H ≤ run k n
  first : ∀ k, k < A → run k n ≠ q

noncomputable def nativeSet (H N : Nat) : Finset Nat := by
  classical
  exact (Finset.Icc 1 H).filter (NoDescent N)

noncomputable def sources (H q : Nat) : Finset Nat := by
  classical
  exact (Finset.Icc 1 (H-1)).filter (fun n => ∃ A, FirstUpcrossing H q n A)

noncomputable def hitClock (H q n : Nat) : Nat := by
  classical
  exact if h : ∃ A, FirstUpcrossing H q n A then Classical.choose h else 0

noncomputable def lateSources (H q N : Nat) : Finset Nat := by
  classical
  exact (sources H q).filter (fun n => N ≤ hitClock H q n)

theorem run_eq_iterate (k n : Nat) : run k n = (step^[k]) n := by
  induction k generalizing n with
  | zero => simp [run]
  | succ k ih => simpa [run, Function.iterate_succ_apply] using ih (step n)

theorem step_upper (n : Nat) : 2*step n ≤ 3*n+1 := by
  unfold step
  split_ifs <;> omega

theorem step_shifted_growth (n : Nat) : 2*(step n+1) ≤ 3*(n+1) := by
  have h := step_upper n
  omega

theorem run_shifted_growth (k n : Nat) :
    2^k*(run k n+1) ≤ 3^k*(n+1) := by
  induction k generalizing n with
  | zero => simp [run]
  | succ k ih =>
      calc
        2^(k+1)*(run (k+1) n+1) = 2*(2^k*(run k (step n)+1)) := by
          simp only [run, pow_succ]
          ring
        _ ≤ 2*(3^k*(step n+1)) := Nat.mul_le_mul_left 2 (ih (step n))
        _ = 3^k*(2*(step n+1)) := by ring
        _ ≤ 3^k*(3*(n+1)) := Nat.mul_le_mul_left _ (step_shifted_growth n)
        _ = 3^(k+1)*(n+1) := by rw [pow_succ]; ring

theorem run_coefficient_lower (k n : Nat) :
    3^(oddCount k n)*n ≤ 2^k*run k n := by
  induction k generalizing n with
  | zero => simp [run, oddCount]
  | succ k ih =>
      have tail := ih (step n)
      by_cases he : n % 2 = 0
      · have edge : 2*step n = n := by simp only [step]; split_ifs; omega
        have count : oddCount (k+1) n = oddCount k (step n) := by
          simp [oddCount, he]
        calc
          3^(oddCount (k+1) n)*n = 3^(oddCount k (step n))*(2*step n) := by
            rw [count, edge]
          _ = 2*(3^(oddCount k (step n))*step n) := by ring
          _ ≤ 2*(2^k*run k (step n)) := Nat.mul_le_mul_left 2 tail
          _ = 2^(k+1)*run (k+1) n := by simp only [run, pow_succ]; ring
      · have edge : 2*step n = 3*n+1 := by
          simp only [step]
          split_ifs
          omega
        have count : oddCount (k+1) n = 1 + oddCount k (step n) := by
          simp [oddCount, he]
        calc
          3^(oddCount (k+1) n)*n = 3^(oddCount k (step n))*(3*n) := by
            rw [count, pow_add, pow_one]
            ring
          _ ≤ 3^(oddCount k (step n))*(2*step n) :=
            Nat.mul_le_mul_left _ (by omega)
          _ = 2*(3^(oddCount k (step n))*step n) := by ring
          _ ≤ 2*(2^k*run k (step n)) := Nat.mul_le_mul_left 2 tail
          _ = 2^(k+1)*run (k+1) n := by simp only [run, pow_succ]; ring

theorem coefficient_nonneg (k n : Nat) : 0 ≤ coefficient k n := by
  unfold coefficient
  positivity

theorem coefficient_source_le (k n : Nat) :
    coefficient k n * (n:Real) ≤ (run k n:Real) := by
  have h : (3:Real)^(oddCount k n)*(n:Real) ≤ (2:Real)^k*(run k n:Real) := by
    exact_mod_cast run_coefficient_lower k n
  rw [coefficient, div_mul_eq_mul_div]
  apply (div_le_iff₀ (by positivity : 0 < (2:Real)^k)).2
  nlinarith

theorem run_shifted_ratio (k n : Nat) :
    (run k n:Real)+1 ≤ ((3:Real)/2)^k*((n:Real)+1) := by
  have h : (2:Real)^k*((run k n:Real)+1) ≤ (3:Real)^k*((n:Real)+1) := by
    exact_mod_cast run_shifted_growth k n
  calc
    (run k n:Real)+1 ≤ ((3:Real)^k*((n:Real)+1))/(2:Real)^k := by
      apply (le_div_iff₀ (by positivity : 0 < (2:Real)^k)).2
      nlinarith
    _ = ((3:Real)/2)^k*((n:Real)+1) := by rw [div_pow]; ring

theorem first_hit_clock_unique (H q n A B : Nat)
    (ha : FirstUpcrossing H q n A) (hb : FirstUpcrossing H q n B) : A = B := by
  by_contra hne
  rcases lt_or_gt_of_ne hne with hlt | hgt
  · exact hb.first A hlt ha.endpoint
  · exact ha.first B hgt hb.endpoint

theorem first_upcrossing_range (H q n A : Nat)
    (h : FirstUpcrossing H q n A) : 2*H ≤ 3*n+1 := by
  have hA := h.clock_pos
  have hi := h.high 1 (by omega) (by omega : 1 ≤ A)
  have hu := step_upper n
  simp only [run] at hi
  omega

theorem first_upcrossing_no_descent (H q n A N : Nat)
    (h : FirstUpcrossing H q n A) (hlate : N ≤ A) : NoDescent N n := by
  intro k hk
  by_cases hz : k = 0
  · subst k
    simp [run]
  · have hi := h.high k (by omega) (hk.trans hlate)
    have hlt := h.source_lt
    omega

theorem first_upcrossing_weight (H q n A : Nat) (hH : 2 ≤ H)
    (h : FirstUpcrossing H q n A) :
    coefficient A n ≤ 3*(q:Real)/(2*(H:Real)-1) := by
  have hc := coefficient_source_le A n
  rw [h.endpoint] at hc
  have hn : 2*(H:Real) ≤ 3*(n:Real)+1 := by
    exact_mod_cast first_upcrossing_range H q n A h
  have hnon := coefficient_nonneg A n
  have hpos : 0 < 2*(H:Real)-1 := by
    have hh : (2:Real) ≤ (H:Real) := by exact_mod_cast hH
    linarith
  apply (le_div_iff₀ hpos).2
  nlinarith

theorem clock_lower_of_large_target (H q n A N : Nat)
    (h : FirstUpcrossing H q n A)
    (hlarge : (H:Real)*((3:Real)/2)^N < (q:Real)+1) : N ≤ A := by
  by_contra hshort
  have hAN : A ≤ N := by omega
  have hp : ((3:Real)/2)^A ≤ ((3:Real)/2)^N :=
    pow_le_pow_right₀ (by norm_num) hAN
  have hlt := h.source_lt
  have hn : (n:Real)+1 ≤ (H:Real) := by exact_mod_cast (by omega : n+1 ≤ H)
  have hg := run_shifted_ratio A n
  rw [h.endpoint] at hg
  have hmul := mul_le_mul hp hn (by positivity : 0 ≤ (n:Real)+1)
    (by positivity : 0 ≤ ((3:Real)/2)^N)
  nlinarith

theorem family_card_le_native (H q N : Nat) (F : Finset Nat) (clock : Nat → Nat)
    (hcross : ∀ n ∈ F, FirstUpcrossing H q n (clock n))
    (hlate : ∀ n ∈ F, N ≤ clock n) : F.card ≤ (nativeSet H N).card := by
  classical
  apply Finset.card_le_card
  intro n hn
  have h := hcross n hn
  have hlt := h.source_lt
  simp only [nativeSet, Finset.mem_filter, Finset.mem_Icc]
  exact ⟨⟨h.source_pos, by omega⟩,
    first_upcrossing_no_descent H q n (clock n) N h (hlate n hn)⟩

theorem family_weight_le_native (H q N : Nat) (F : Finset Nat) (clock : Nat → Nat)
    (hH : 2 ≤ H)
    (hcross : ∀ n ∈ F, FirstUpcrossing H q n (clock n))
    (hlate : ∀ n ∈ F, N ≤ clock n) :
    (∑ n ∈ F, coefficient (clock n) n) ≤
      (3*(q:Real)/(2*(H:Real)-1))*((nativeSet H N).card:Real) := by
  have hcard : (F.card:Real) ≤ ((nativeSet H N).card:Real) := by
    exact_mod_cast family_card_le_native H q N F clock hcross hlate
  have hpos : 0 ≤ 3*(q:Real)/(2*(H:Real)-1) := by
    apply div_nonneg (by positivity)
    have hh : (2:Real) ≤ (H:Real) := by exact_mod_cast hH
    linarith
  calc
    (∑ n ∈ F, coefficient (clock n) n) ≤
        ∑ _n ∈ F, 3*(q:Real)/(2*(H:Real)-1) :=
      Finset.sum_le_sum (fun n hn => first_upcrossing_weight H q n (clock n) hH (hcross n hn))
    _ = (3*(q:Real)/(2*(H:Real)-1))*(F.card:Real) := by simp [mul_comm]
    _ ≤ (3*(q:Real)/(2*(H:Real)-1))*((nativeSet H N).card:Real) :=
      mul_le_mul_of_nonneg_left hcard hpos

theorem source_has_canonical_clock (H q n : Nat) (hn : n ∈ sources H q) :
    FirstUpcrossing H q n (hitClock H q n) := by
  classical
  have hex : ∃ A, FirstUpcrossing H q n A := (Finset.mem_filter.mp hn).2
  simpa only [hitClock, dite_eq_left hex] using Classical.choose_spec hex

theorem all_late_boundary_bound (H q N : Nat) (hH : 2 ≤ H) :
    (∑ n ∈ lateSources H q N, coefficient (hitClock H q n) n) ≤
      (3*(q:Real)/(2*(H:Real)-1))*((nativeSet H N).card:Real) := by
  classical
  apply family_weight_le_native H q N (lateSources H q N) (hitClock H q) hH
  · intro n hn
    exact source_has_canonical_clock H q n (Finset.mem_filter.mp hn).1
  · intro n hn
    exact (Finset.mem_filter.mp hn).2

theorem all_boundary_bound_of_large_target (H q N : Nat) (hH : 2 ≤ H)
    (hlarge : (H:Real)*((3:Real)/2)^N < (q:Real)+1) :
    (∑ n ∈ sources H q, coefficient (hitClock H q n) n) ≤
      (3*(q:Real)/(2*(H:Real)-1))*((nativeSet H N).card:Real) := by
  apply family_weight_le_native H q N (sources H q) (hitClock H q) hH
  · exact source_has_canonical_clock H q
  · intro n hn
    exact clock_lower_of_large_target H q n (hitClock H q n) N
      (source_has_canonical_clock H q n hn) hlarge

theorem all_boundary_bound_of_native_card (H q N : Nat) (hH : 2 ≤ H)
    (hlarge : (H:Real)*((3:Real)/2)^N < (q:Real)+1)
    (C : Real) (hcount : ((nativeSet H N).card:Real) ≤ C) :
    (∑ n ∈ sources H q, coefficient (hitClock H q n) n) ≤
      (3*(q:Real)/(2*(H:Real)-1))*C := by
  apply (all_boundary_bound_of_large_target H q N hH hlarge).trans
  apply mul_le_mul_of_nonneg_left hcount
  apply div_nonneg (by positivity)
  have hh : (2:Real) ≤ (H:Real) := by exact_mod_cast hH
  linarith

theorem dyadic_all_boundary_bound (m q : Nat) (hm : 1 ≤ m) (hq : 3^m ≤ q) :
    (∑ n ∈ sources (2^m) q, coefficient (hitClock (2^m) q n) n) ≤
      (3*(q:Real)/(2*((2^m:Nat):Real)-1))*((nativeSet (2^m) m).card:Real) := by
  have hH : 2 ≤ (2:Nat)^m := by
    obtain ⟨k, hk⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : m ≠ 0)
    rw [hk, pow_succ]
    have hp : 0 < (2:Nat)^k := by positivity
    omega
  have heq : ((2^m:Nat):Real)*((3:Real)/2)^m = (3:Real)^m := by
    simp only [Nat.cast_pow, Nat.cast_ofNat]
    rw [← mul_pow]
    norm_num
  have hlarge : ((2^m:Nat):Real)*((3:Real)/2)^m < (q:Real)+1 := by
    rw [heq]
    have hh : (3:Real)^m ≤ (q:Real) := by exact_mod_cast hq
    linarith
  exact all_boundary_bound_of_large_target (2^m) q m hH hlarge

theorem bounded_potential_boundary (H q N : Nat) (hH : 2 ≤ H)
    (hlarge : (H:Real)*((3:Real)/2)^N < (q:Real)+1)
    (f : Nat → Real) (M : Real) (hM : 0 ≤ M)
    (hbound : ∀ n ∈ sources H q, f n ≤ M) :
    (∑ n ∈ sources H q, coefficient (hitClock H q n) n * f n) ≤
      ((3*(q:Real)/(2*(H:Real)-1))*((nativeSet H N).card:Real))*M := by
  calc
    (∑ n ∈ sources H q, coefficient (hitClock H q n) n * f n) ≤
        ∑ n ∈ sources H q, coefficient (hitClock H q n) n * M :=
      Finset.sum_le_sum (fun n hn =>
        mul_le_mul_of_nonneg_left (hbound n hn) (coefficient_nonneg (hitClock H q n) n))
    _ = (∑ n ∈ sources H q, coefficient (hitClock H q n) n)*M := by
      rw [Finset.sum_mul]
    _ ≤ ((3*(q:Real)/(2*(H:Real)-1))*((nativeSet H N).card:Real))*M :=
      mul_le_mul_of_nonneg_right (all_boundary_bound_of_large_target H q N hH hlarge) hM

#print axioms run_eq_iterate
#print axioms step_upper
#print axioms step_shifted_growth
#print axioms run_shifted_growth
#print axioms run_coefficient_lower
#print axioms coefficient_nonneg
#print axioms coefficient_source_le
#print axioms run_shifted_ratio
#print axioms first_hit_clock_unique
#print axioms first_upcrossing_range
#print axioms first_upcrossing_no_descent
#print axioms first_upcrossing_weight
#print axioms clock_lower_of_large_target
#print axioms family_card_le_native
#print axioms family_weight_le_native
#print axioms source_has_canonical_clock
#print axioms all_late_boundary_bound
#print axioms all_boundary_bound_of_large_target
#print axioms all_boundary_bound_of_native_card
#print axioms dyadic_all_boundary_bound
#print axioms bounded_potential_boundary

end CollatzFirstCrossing
