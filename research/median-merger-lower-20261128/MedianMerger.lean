import AffineOrbit

/-! Exact first meetings and the two incoming branches of the positive shortcut cycle. -/

open Collatz.PoweredAffine
open scoped BigOperators

namespace Collatz.MedianMerger

def hits (a b : ℕ) : ℕ := if a = b then 1 else 0

def sibling (a b : ℕ) : ℕ := if a % 2 = 1 ∧ b = 3*a + 1 then 1 else 0

theorem hits_step (a b : ℕ) :
    hits (step a) (step b) = hits a b + sibling a b + sibling b a := by
  unfold hits sibling step
  split_ifs <;> omega

theorem orbit_last (n t : ℕ) : orbit n (t + 1) = step (orbit n t) := by
  induction t generalizing n with
  | zero => rfl
  | succ t ih => exact ih (step n)

theorem first_meeting_count (n m t : ℕ) :
    hits (orbit n t) (orbit m t) = hits n m +
      ∑ k ∈ Finset.range t,
        (sibling (orbit n k) (orbit m k) + sibling (orbit m k) (orbit n k)) := by
  induction t with
  | zero => simp [orbit]
  | succ t ih =>
    rw [orbit_last n t, orbit_last m t, hits_step, ih, Finset.sum_range_succ]
    omega

private theorem step_eq_one (x : ℕ) : step x = 1 ↔ x = 2 := by
  unfold step
  split_ifs <;> omega

private theorem step_eq_two (x : ℕ) : step x = 2 ↔ x = 1 ∨ x = 4 := by
  unfold step
  split_ifs <;> omega

def arrivals (starts : Finset ℕ) (t y : ℕ) : ℕ :=
  (starts.filter (fun n => orbit n t = y)).card

theorem arrivals_one (starts : Finset ℕ) (t : ℕ) :
    arrivals starts (t+1) 1 = arrivals starts t 2 := by
  simp only [arrivals, orbit_last, step_eq_one]

theorem arrivals_two (starts : Finset ℕ) (t : ℕ) :
    arrivals starts (t+1) 2 = arrivals starts t 1 + arrivals starts t 4 := by
  classical
  unfold arrivals
  have hd : Disjoint (starts.filter fun n => orbit n t = 1)
      (starts.filter fun n => orbit n t = 4) := by
    rw [Finset.disjoint_left]
    intro n hn hm
    have h1 := (Finset.mem_filter.mp hn).2
    have h4 := (Finset.mem_filter.mp hm).2
    omega
  rw [← Finset.card_union_of_disjoint hd]
  apply congrArg Finset.card
  ext n
  simp only [Finset.mem_filter, Finset.mem_union, orbit_last, step_eq_two]
  tauto

/-- Counts ordered first meetings through the branches 1 and 4, with the
equal-entry cohorts retained as an exact finite correction. -/
theorem cycle_gate_identity (starts : Finset ℕ) (h : ℕ) :
    (arrivals starts h 1)^2 + (arrivals starts h 2)^2 =
      (arrivals starts 0 1)^2 + (arrivals starts 0 2)^2 +
        ∑ t ∈ Finset.range h,
          (2 * arrivals starts t 1 * arrivals starts t 4 + (arrivals starts t 4)^2) := by
  induction h with
  | zero => simp
  | succ h ih =>
    rw [arrivals_one, arrivals_two, Finset.sum_range_succ]
    calc
      _ = ((arrivals starts h 1)^2 + (arrivals starts h 2)^2) +
          (2 * arrivals starts h 1 * arrivals starts h 4 + (arrivals starts h 4)^2) := by ring
      _ = _ := by rw [ih]; omega

/-- An odd upper lift keeps a genuine matching endpoint at every positive date.
The two new starts lie in widely separated blocks. -/
theorem separated_lift {B n m t : ℕ} (hlo : B ≤ n) (hhi : n < 2*B)
    (hmlo : B ≤ m) (hmhi : m < 2*B) (hodd : m % 2 = 1)
    (ht : 0 < t) (hmeet : orbit n t = orbit m t) :
    n + B ≤ 3*m + 1 ∧ 3*m + 1 ≤ 6*B ∧ B ≤ n ∧ orbit n t = orbit (3*m+1) t := by
  have hs : step (3*m+1) = step m := by
    unfold step
    split_ifs <;> omega
  refine ⟨by omega, by omega, hlo, ?_⟩
  obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : t ≠ 0)
  simpa only [orbit, hs] using hmeet

private theorem orbit_add' (n t u : ℕ) :
    orbit n (t + u) = orbit (orbit n t) u := by
  induction t generalizing n with
  | zero => simp [orbit]
  | succ t ih => simpa only [Nat.succ_add, orbit] using ih (step n)

theorem sixteen_delay (n t : ℕ) : orbit (16*n) (4+t) = orbit n t := by
  have he (x : ℕ) : step (2*x) = x := by simp [step]
  have h4 : orbit (16*n) 4 = n := by
    change step (step (step (step (16*n)))) = n
    rw [show 16*n = 2*(2*(2*(2*n))) by ring, he, he, he, he]
  rw [orbit_add', h4]

private theorem one_even (k : ℕ) : orbit 1 (2*k) = 1 := by
  induction k with
  | zero => rfl
  | succ k ih =>
    rw [Nat.mul_succ, orbit_add', ih]
    rfl

/-- If the later first hit of 1 occurs an even positive number of dates
after the earlier one, the first merger is on the branches 1 and 4. -/
theorem distinct_dates_gate {n m t k : ℕ} (hn : orbit n t = 1)
    (hm : orbit m (t+2*k+2) = 1) (hbefore : orbit m (t+2*k) ≠ 1) :
    orbit n (t+2*k) = 1 ∧ orbit m (t+2*k) = 4 ∧
    (∀ j ≤ t+2*k, orbit n j ≠ orbit m j) ∧
    orbit n (t+2*k+1) = orbit m (t+2*k+1) := by
  have h1 : orbit n (t+2*k) = 1 := by rw [orbit_add', hn, one_even]
  have h2 : step (orbit m (t+2*k)) = 2 := by
    rw [← orbit_last]
    apply (step_eq_one _).mp
    simpa only [← orbit_last] using hm
  have h4 := ((step_eq_two _).mp h2).resolve_left hbefore
  refine ⟨h1, h4, ?_, ?_⟩
  · intro j hj hjm
    obtain ⟨d, hd⟩ := Nat.exists_eq_add_of_le hj
    have heq : orbit n (t+2*k) = orbit m (t+2*k) := by
      rw [hd, orbit_add', orbit_add', hjm]
    omega
  · rw [orbit_last, orbit_last, h1, h4]
    rfl

/-- A four-step tie is oriented by time, but its unordered endpoints cross
the bipartition determined by the parity of the four-step time block. -/
theorem four_step_ties (seeds : Finset ℕ) (time : ℕ → ℕ) :
    ((seeds.product seeds).filter (fun p => time p.1 = time p.2 + 4)).card ≤
      (seeds.filter (fun n => time n / 4 % 2 = 0)).card *
      (seeds.filter (fun n => time n / 4 % 2 = 1)).card := by
  classical
  let left := seeds.filter (fun n => time n / 4 % 2 = 0)
  let right := seeds.filter (fun n => time n / 4 % 2 = 1)
  let orient (p : ℕ × ℕ) := if time p.1 / 4 % 2 = 0 then p else p.swap
  change _ ≤ left.card * right.card
  rw [← Finset.card_product]
  apply Finset.card_le_card_of_injOn orient
  · rintro ⟨u, v⟩ hp
    obtain ⟨hm, ht⟩ := Finset.mem_filter.mp hp
    obtain ⟨hu, hv⟩ := Finset.mem_product.mp hm
    change time u = time v + 4 at ht
    change (if time u / 4 % 2 = 0 then (u, v) else (v, u)) ∈ left.product right
    by_cases h : time u / 4 % 2 = 0
    · rw [ite_eq_left h]
      exact Finset.mem_product.mpr ⟨Finset.mem_filter.mpr ⟨hu, h⟩,
        Finset.mem_filter.mpr ⟨hv, by change time v / 4 % 2 = 1; omega⟩⟩
    · rw [ite_eq_right h]
      exact Finset.mem_product.mpr ⟨Finset.mem_filter.mpr ⟨hv, by change time v / 4 % 2 = 0; omega⟩,
        Finset.mem_filter.mpr ⟨hu, by change time u / 4 % 2 = 1; omega⟩⟩
  · rintro ⟨u, v⟩ hp ⟨w, z⟩ hq heq
    have ht : time u = time v + 4 := (Finset.mem_filter.mp hp).2
    have hs : time w = time z + 4 := (Finset.mem_filter.mp hq).2
    change (if time u / 4 % 2 = 0 then (u, v) else (v, u)) =
      (if time w / 4 % 2 = 0 then (w, z) else (z, w)) at heq
    split_ifs at heq
    · exact heq
    · obtain ⟨rfl, rfl⟩ := Prod.mk.inj heq
      omega
    · obtain ⟨rfl, rfl⟩ := Prod.mk.inj heq
      omega
    · obtain ⟨rfl, rfl⟩ := Prod.mk.inj heq
      rfl

/-- After splitting by hit-time parity, each tie graph loses at most
one quarter of that parity's square. This gives the uniform three-eighths. -/
theorem three_eighths (a b c d u v : ℕ) (hu : u ≤ a*b) (hv : v ≤ c*d) :
    3*(a+b+c+d)^2 + 8*(u+v) ≤ 8*((a+b)^2+(c+d)^2) := by
  zify at *
  nlinarith [sq_nonneg ((a : ℤ) - b), sq_nonneg ((c : ℤ) - d),
    sq_nonneg (((a : ℤ) + b) - (c + d))]

end Collatz.MedianMerger
