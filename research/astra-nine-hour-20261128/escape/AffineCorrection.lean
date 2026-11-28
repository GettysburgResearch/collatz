import MinimumWindow
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Max
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

/-! Exact affine correction and a positive simple-path product bound. -/

namespace Collatz.MinimumWindow

def correction (n : ℕ) : ℚ :=
  if n % 2 = 0 then 1 else (3*(n:ℚ)+1)/(3*n)

def accumulated (k n : ℕ) : ℚ :=
  ∏ i ∈ Finset.range k, correction (orbit i n)

theorem step_positive {n : ℕ} (hn : 0 < n) : 0 < step n := by
  unfold step
  split <;> omega

theorem orbit_positive (i : ℕ) {n : ℕ} (hn : 0 < n) : 0 < orbit i n := by
  induction i generalizing n with
  | zero => exact hn
  | succ i ih => exact ih (step_positive hn)

theorem correction_bounds {n : ℕ} (hn : 0 < n) :
    1 ≤ correction n ∧ correction n ≤ ((n:ℚ)+1)/n := by
  have hp : (0:ℚ) < n := by exact_mod_cast hn
  unfold correction
  split
  · constructor
    · rfl
    · apply (le_div_iff₀ hp).2
      linarith
  · constructor
    · apply (le_div_iff₀ (by positivity)).2
      linarith
    · apply (div_le_div_iff₀ (by positivity) hp).2
      nlinarith

theorem one_step_product {n : ℕ} (hn : 0 < n) :
    2 * (step n : ℚ) =
      (3:ℚ)^(if oddMark n then 1 else 0) * n * correction n := by
  have hp : (n:ℚ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hn)
  by_cases he : n % 2 = 0
  · have eq : 2*((n/2:ℕ):ℚ) = n := by exact_mod_cast (show 2*(n/2)=n by omega)
    simpa [step, oddMark, correction, he]
  · have ho : n % 2 = 1 := by omega
    have eq : 2*(((3*n+1)/2:ℕ):ℚ) = 3*n+1 := by
      exact_mod_cast (show 2*((3*n+1)/2)=3*n+1 by omega)
    simp [step, oddMark, correction, ho]
    rw [eq]
    field_simp

theorem accumulated_succ (k n : ℕ) :
    accumulated (k+1) n = correction n * accumulated k (step n) := by
  rw [accumulated, Finset.prod_range_succ']
  simp [accumulated, orbit, mul_comm]

theorem arithmetic_product (k n : ℕ) (hn : 0 < n) :
    (2:ℚ)^k * (orbit k n : ℚ) =
      (3:ℚ)^(count oddMark k n) * n * accumulated k n := by
  induction k generalizing n with
  | zero => simp [orbit, count, accumulated]
  | succ k ih =>
    rw [accumulated_succ, count, orbit, pow_add, pow_succ]
    simp only [pow_zero, one_mul]
    have htail := ih (step n) (step_positive hn)
    have hone := one_step_product hn
    calc
      2^k * 2 * (orbit k (step n) : ℚ) = 2*(2^k * (orbit k (step n) : ℚ)) := by ring
      _ = 2*(3^(count oddMark k (step n)) * (step n : ℚ) * accumulated k (step n)) := by rw [htail]
      _ = (2*(step n : ℚ))*3^(count oddMark k (step n)) * accumulated k (step n) := by ring
      _ = _ := by rw [hone]; ring

theorem distinct_before_first {k n m : ℕ} (hit : orbit k n = m)
    (earlier : ∀ j < k, orbit j n ≠ m) :
    Set.InjOn (fun i => orbit i n) (Finset.range k : Set ℕ) := by
  have impossible : ∀ i j : ℕ, i < j → j < k → orbit i n = orbit j n → False := by
    intro i j hij hj h
    have eq : orbit (i+(k-j)) n = m := by
      rw [orbit_add, h, ← orbit_add]
      convert hit using 2
      omega
    exact earlier _ (by omega) eq
  intro i hi j hj h
  have hi' : i < k := Finset.mem_range.mp hi
  have hj' : j < k := Finset.mem_range.mp hj
  rcases lt_trichotomy i j with hlt | heq | hgt
  · exact False.elim (impossible _ _ hlt hj' h)
  · exact heq
  · exact False.elim (impossible _ _ hgt hi' h.symm)

private theorem set_product_bound (s : Finset ℕ) (pos : ∀ x ∈ s, 0 < x) :
    (∏ x ∈ s, correction x) ≤ (s.card:ℚ)+1 := by
  induction s using Finset.strongInductionOn with
  | _ s ih =>
    by_cases hs : s.Nonempty
    · let m := s.max' hs
      have hm : m ∈ s := Finset.max'_mem s hs
      have hmpos := pos m hm
      have subs : s ⊆ Finset.Icc 1 m := by
        intro x hx
        exact Finset.mem_Icc.mpr ⟨pos x hx, Finset.le_max' _ _ hx⟩
      have hc : s.card ≤ m := by simpa using Finset.card_le_card subs
      have ht := ih (s.erase m) (Finset.erase_ssubset hm) (fun x hx => pos x (Finset.mem_of_mem_erase hx))
      have hcard : (s.erase m).card + 1 = s.card := Finset.card_erase_add_one hm
      have hcardq : ((s.erase m).card:ℚ)+1 = s.card := by exact_mod_cast hcard
      rw [hcardq] at ht
      have hmq : (0:ℚ) < m := by exact_mod_cast hmpos
      have hcm : (s.card:ℚ) ≤ m := by exact_mod_cast hc
      calc
        (∏ x ∈ s, correction x) = (∏ x ∈ s.erase m, correction x)*correction m :=
          (Finset.prod_erase_mul s correction hm).symm
        _ ≤ (s.card:ℚ)*correction m := mul_le_mul_of_nonneg_right ht
          (le_trans (by norm_num) (correction_bounds hmpos).1)
        _ ≤ (s.card:ℚ)*(((m:ℚ)+1)/m) := mul_le_mul_of_nonneg_left
          (correction_bounds hmpos).2 (by positivity)
        _ ≤ _ := by rw [← mul_div_assoc]; apply (div_le_iff₀ hmq).2; nlinarith
    · simp [Finset.not_nonempty_iff_eq_empty.mp hs]

theorem simple_product_bound {k n : ℕ} (hn : 0 < n)
    (simple : Set.InjOn (fun i => orbit i n) (Finset.range k : Set ℕ)) :
    accumulated k n ≤ (k:ℚ)+1 := by
  let s := (Finset.range k).image (fun i => orbit i n)
  have hs : ∀ x ∈ s, 0 < x := by
    intro x hx
    obtain ⟨i, _, rfl⟩ := Finset.mem_image.mp hx
    exact orbit_positive i hn
  have hp := set_product_bound s hs
  have heq : (∏ x ∈ s, correction x) = accumulated k n := Finset.prod_image simple
  have hc : s.card = k := by
    change ((Finset.range k).image (fun i => orbit i n)).card = k
    rw [Finset.card_image_of_injOn simple, Finset.card_range]
  rwa [heq, hc] at hp

theorem first_hit_product_bound {k n m : ℕ} (hn : 0 < n) (hit : orbit k n = m)
    (earlier : ∀ j < k, orbit j n ≠ m) : accumulated k n ≤ (k:ℚ)+1 :=
  simple_product_bound hn (distinct_before_first hit earlier)

#print axioms arithmetic_product
#print axioms simple_product_bound
#print axioms first_hit_product_bound

end Collatz.MinimumWindow
