import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Ring

/-! The ordinary Collatz dynamics as the 1932 Collatz permutation with one
    compressed residue class. All maps use natural numbers, including zero. -/

namespace Collatz.Diagonal.Amusical

def perm (m : ℕ) : ℕ :=
  if m % 3 = 0 then 2 * (m / 3)
  else if m % 3 = 1 then 4 * (m / 3) + 1 else 4 * (m / 3) + 3

def back (m : ℕ) : ℕ :=
  if m % 2 = 0 then 3 * (m / 2)
  else if m % 4 = 1 then 3 * (m / 4) + 1 else 3 * (m / 4) + 2

def fold (m : ℕ) : ℕ := if m % 3 = 2 then m / 3 + 1 else m

def slow (m : ℕ) : ℕ := fold (back m)

def oddPart (n : ℕ) : ℕ := ordCompl[2] n

def accel (m : ℕ) : ℕ := (oddPart (6 * m - 2) + 1) / 2

def full (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else 3 * n + 1

def Reaches (f : ℕ → ℕ) (m n : ℕ) : Prop := ∃ k : ℕ, f^[k] m = n

theorem perm_back (m : ℕ) : perm (back m) = m := by
  unfold back perm
  repeat' split
  all_goals omega

theorem back_perm (m : ℕ) : back (perm m) = m := by
  unfold perm back
  repeat' split
  all_goals omega

theorem slow_formula (m : ℕ) : slow m =
    if m % 2 = 0 then 3 * (m / 2)
    else if m % 4 = 1 then 3 * (m / 4) + 1 else m / 4 + 1 := by
  unfold slow fold back
  repeat' split
  all_goals omega

theorem slow_pos {m : ℕ} (hm : 0 < m) : 0 < slow m := by
  rw [slow_formula]
  repeat' split
  all_goals omega

theorem back_hole (m : ℕ) : back m % 3 = 2 ↔ m % 4 = 3 := by
  unfold back
  repeat' split
  all_goals omega

theorem reaches_trans {f : ℕ → ℕ} {m n t : ℕ}
    (a : Reaches f m n) (b : Reaches f n t) : Reaches f m t := by
  obtain ⟨i, hi⟩ := a
  obtain ⟨j, hj⟩ := b
  exact ⟨j + i, by rw [Function.iterate_add_apply, hi, hj]⟩

theorem reaches_step (f : ℕ → ℕ) (m : ℕ) : Reaches f m (f m) :=
  ⟨1, rfl⟩

theorem basin_step {f : ℕ → ℕ} {m : ℕ} (hf : f 1 = 1) :
    Reaches f m 1 ↔ Reaches f (f m) 1 := by
  constructor
  · rintro ⟨k, hk⟩
    cases k with
    | zero => exact ⟨0, by simpa using (congrArg f hk).trans hf⟩
    | succ k => exact ⟨k, by rwa [Function.iterate_succ_apply] at hk⟩
  · exact fun h => reaches_trans (reaches_step _ _) h

theorem basin_transport {f : ℕ → ℕ} {p : ℕ → Prop} {a b : ℕ}
    (hp : ∀ x, p x ↔ p (f x)) (h : Reaches f a b) : p a ↔ p b := by
  obtain ⟨k, rfl⟩ := h
  induction k with
  | zero => rfl
  | succ k ih => rw [Function.iterate_succ_apply']; exact ih.trans (hp _)

private theorem oddPart_of_odd {n : ℕ} (hn : n % 2 = 1) : oddPart n = n := by
  apply (Nat.ordCompl_eq_self_iff_zero_or_not_dvd n Nat.prime_two).2
  exact Or.inr (by rw [Nat.dvd_iff_mod_eq_zero]; omega)

private theorem part_two_mul (n : ℕ) : oddPart (2 * n) = oddPart n := by
  exact Nat.ordCompl_self_pow_mul n 1 Nat.prime_two

private theorem part_four_mul (n : ℕ) : oddPart (4 * n) = oddPart n := by
  rw [show 4 * n = 2 * (2 * n) by omega, part_two_mul, part_two_mul]

theorem accel_edges {m : ℕ} (hm : 0 < m) :
    (m % 4 ≠ 3 → accel m = slow m) ∧
    (m % 4 = 3 → accel m = accel (slow m) ∧ slow m < m) := by
  constructor
  · intro h
    rw [slow_formula]
    by_cases he : m % 2 = 0
    · rw [ite_eq_left he]
      unfold accel
      rw [show 6 * m - 2 = 2 * (6 * (m / 2) - 1) by omega,
        part_two_mul, oddPart_of_odd (by omega)]
      omega
    · rw [ite_eq_right he, ite_eq_left (by omega : m % 4 = 1)]
      unfold accel
      rw [show 6 * m - 2 = 4 * (6 * (m / 4) + 1) by omega,
        part_four_mul, oddPart_of_odd (by omega)]
      omega
  · intro h
    rw [slow_formula, ite_eq_right (by omega : ¬ m % 2 = 0),
        ite_eq_right (by omega : ¬ m % 4 = 1)]
    constructor
    · unfold accel
      rw [show 6 * m - 2 = 4 * (6 * (m / 4 + 1) - 2) by omega,
        part_four_mul]
    · omega

theorem reaches_accel {m : ℕ} (hm : 0 < m) : Reaches slow m (accel m) := by
  induction m using Nat.strong_induction_on with
  | h m ih =>
    by_cases hc : m % 4 = 3
    · obtain ⟨he, hl⟩ := (accel_edges hm).2 hc
      rw [he]
      exact reaches_trans (reaches_step _ _) (ih _ hl (slow_pos hm))
    · rw [(accel_edges hm).1 hc]
      exact reaches_step _ _

private theorem accel_one : accel 1 = 1 := by
  unfold accel
  rw [show 6 * 1 - 2 = 4 * 1 by decide, part_four_mul,
    oddPart_of_odd (by decide : 1 % 2 = 1)]

private theorem accel_pos {m : ℕ} (hm : 0 < m) : 0 < accel m := by
  have h := Nat.ordCompl_pos 2 (by omega : 6 * m - 2 ≠ 0)
  change 0 < oddPart (6 * m - 2) at h
  unfold accel
  omega

theorem slow_basin_iff_accel_basin {m : ℕ} (hm : 0 < m) :
    Reaches slow m 1 ↔ Reaches accel m 1 := by
  constructor
  · intro hs
    have edge (x : ℕ) : (0 < x → Reaches accel x 1) ↔
        (0 < slow x → Reaches accel (slow x) 1) := by
      by_cases hx : 0 < x
      · simp only [hx, slow_pos hx, true_implies]
        by_cases hc : x % 4 = 3
        · have he := (accel_edges hx).2 hc
          exact (basin_step accel_one).trans
            (he.1 ▸ (basin_step accel_one).symm)
        · simpa [(accel_edges hx).1 hc] using
            (basin_step (m := x) accel_one)
      · have he : x = 0 := by omega
        subst x
        simp [slow_formula]
    exact ((basin_transport edge hs).2 (fun _ => ⟨0, rfl⟩)) hm
  · rintro ⟨k, hk⟩
    have path (j : ℕ) : Reaches slow m (accel^[j] m) ∧ 0 < accel^[j] m := by
      induction j with
      | zero => exact ⟨⟨0, rfl⟩, hm⟩
      | succ j ih =>
        rw [Function.iterate_succ_apply']
        exact ⟨reaches_trans ih.1 (reaches_accel ih.2), accel_pos ih.2⟩
    exact hk ▸ (path k).1

/-- Until the first output hole each slow step follows the actual permutation
    backwards. No recurrence or return-time bound for the permutation is needed. -/
theorem follows_until_hole (m k : ℕ)
    (h : ∀ j < k, back^[j + 1] m % 3 ≠ 2) : slow^[k] m = back^[k] m := by
  induction k with
  | zero => rfl
  | succ k ih =>
    rw [Function.iterate_succ_apply', Function.iterate_succ_apply' back,
      ih (fun j hj => h j (by omega))]
    have ht := h k (by omega)
    rw [Function.iterate_succ_apply'] at ht
    exact ite_eq_right ht

theorem first_hole_fold (m k : ℕ)
    (h : ∀ j < k, back^[j + 1] m % 3 ≠ 2)
    (hit : back^[k + 1] m % 3 = 2) :
    slow^[k + 1] m = back^[k + 1] m / 3 + 1 := by
  rw [Function.iterate_succ_apply', follows_until_hole m k h,
      Function.iterate_succ_apply' back] at *
  exact ite_eq_left hit

def coord (n : ℕ) : ℕ := (oddPart n + 1) / 2

private theorem part_odd {n : ℕ} (hn : 0 < n) : oddPart n % 2 = 1 := by
  have h := Nat.not_dvd_ordCompl Nat.prime_two (Nat.ne_of_gt hn)
  change ¬ 2 ∣ oddPart n at h
  rw [Nat.dvd_iff_mod_eq_zero] at h
  omega

private theorem coord_pos {n : ℕ} (hn : 0 < n) : 0 < coord n := by
  have h := part_odd hn
  unfold coord
  omega

theorem halving_run (e n : ℕ) : full^[e] (2 ^ e * n) = n := by
  induction e with
  | zero => simp
  | succ e ih =>
    rw [pow_succ, show 2 ^ e * 2 * n = 2 * (2 ^ e * n) by ring,
      Function.iterate_succ_apply]
    suffices h : full (2 * (2 ^ e * n)) = 2 ^ e * n by rwa [h]
    simp [full]

theorem full_to_part (n : ℕ) : Reaches full n (oddPart n) := by
  refine ⟨n.factorization 2, ?_⟩
  have h := halving_run (n.factorization 2) (oddPart n)
  rw [show 2 ^ n.factorization 2 * oddPart n = n from
    Nat.ordProj_mul_ordCompl_eq_self n 2] at h
  exact h

theorem full_to_accel {m : ℕ} (hm : 0 < m) :
    Reaches full (2 * m - 1) (2 * accel m - 1) := by
  have h := part_odd (by omega : 0 < 6 * m - 2)
  rw [show 2 * accel m - 1 = oddPart (6 * m - 2) by unfold accel; omega]
  refine reaches_trans (n := 6 * m - 2) ?_ (full_to_part _)
  refine ⟨1, ?_⟩
  change full (2 * m - 1) = 6 * m - 2
  rw [full, ite_eq_right (by omega)]
  omega

private theorem full_edge_coord {n : ℕ} (hn : 0 < n) :
    coord (full n) = coord n ∨ coord (full n) = accel (coord n) := by
  by_cases h : n % 2 = 0
  · left
    rw [full, ite_eq_left h]
    unfold coord
    nth_rw 2 [show n = 2 * (n / 2) by omega]
    rw [part_two_mul]
  · right
    have ho : n % 2 = 1 := by omega
    rw [full, ite_eq_right h]
    unfold coord accel
    rw [oddPart_of_odd ho, show 6 * ((n + 1) / 2) - 2 = 3 * n + 1 by omega]

theorem ordinary_basin_iff {n : ℕ} (hn : 0 < n) :
    Reaches full n 1 ↔ Reaches slow (coord n) 1 := by
  rw [slow_basin_iff_accel_basin (coord_pos hn)]
  constructor
  · intro h
    have edge (x : ℕ) : (0 < x → Reaches accel (coord x) 1) ↔
        (0 < full x → Reaches accel (coord (full x)) 1) := by
      by_cases hx : 0 < x
      · have hp : 0 < full x := by
          unfold full
          split <;> omega
        simp only [hx, hp, true_implies]
        rcases full_edge_coord hx with he | he
        · rw [he]
        · rw [he]
          exact basin_step accel_one
      · have he : x = 0 := by omega
        subst x
        simp [full]
    have h1 : coord 1 = 1 := by
      unfold coord
      rw [oddPart_of_odd (by decide : 1 % 2 = 1)]
    exact ((basin_transport edge h).2 (fun _ => ⟨0, h1⟩)) hn
  · rintro ⟨k, hk⟩
    have p (j : ℕ) : Reaches full n (2 * accel^[j] (coord n) - 1) ∧
        0 < accel^[j] (coord n) := by
      induction j with
      | zero =>
        refine ⟨?_, coord_pos hn⟩
        change Reaches full n (2 * coord n - 1)
        have ho := part_odd hn
        rw [show 2 * coord n - 1 = oddPart n by unfold coord; omega]
        exact full_to_part n
      | succ j ih =>
        rw [Function.iterate_succ_apply']
        exact ⟨reaches_trans ih.1 (full_to_accel ih.2), accel_pos ih.2⟩
    have h := (p k).1
    rw [hk] at h
    exact h

end Collatz.Diagonal.Amusical
