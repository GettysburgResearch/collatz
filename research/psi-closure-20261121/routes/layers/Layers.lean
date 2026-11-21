/-
Layer structure of the closure statement (routes/layers).  Lean 4.34.1 core, no Mathlib.

Normalization as in `Collatz/Closure.lean`: `shortcut n = n/2` (n even), `(3n+1)/2` (n odd);
`Basin n` = some shortcut iterate of `n` equals 1; `S` = the `3x-1` shortcut map (`Shadow.lean`).

`Rank r n`   : the shortcut orbit of `n` reaches 1 with exactly `r` odd steps before its
               first visit to 1.
`FwdLayer r` : the closure statement `x ∈ Basin → 3x-1 ∈ Basin`, restricted to `x` of rank `r`.
`RevLayer r` : the reverse closure `3m-1 ∈ Basin → m ∈ Basin`, restricted to `3m-1` of rank `r`.

NOTHING HERE PROVES THE COLLATZ CONJECTURE.  Every theorem below is an equivalence between
open statements, or an ordinary (finite-orbit) identity.

Credit: `basin_pow_two_pred`, `basin_pow_four_succ`, `basin_jacobsthal`, `shadow_even` and the
closure frame are from `research/psi-closure-20261121/lean`.  The rank-0 instance of
`fwd_family_fold` (Mersenne / `3^a - 1` parity fold) is also in PR #176
(`ternary_even_exponent_fold`, `mersenne_even_exponent_fold`); exact step/odd-count profiles
of the two exponent ladders are also in PR #179 (`ones_block`, `twos_block`) and PR #181
(`power_four_profile`).
-/
import Collatz
open CollatzReverseBasin CollatzClosure

namespace CollatzLayers

/-! ## 1. Rank -/

inductive Rank : ℕ → ℕ → Prop
  | one : Rank 0 1
  | even (r n : ℕ) : 0 < n → Rank r n → Rank r (2*n)
  | odd (r n : ℕ) : n % 2 = 1 → 1 < n → Rank r (shortcut n) → Rank (r+1) n

theorem rank_pos {r n : ℕ} (h : Rank r n) : 0 < n := by
  induction h with
  | one => omega
  | even r n hn _ _ => omega
  | odd r n _ hgt _ _ => omega

theorem rank_basin {r n : ℕ} (h : Rank r n) : Basin n := by
  induction h with
  | one => exact ⟨0, rfl⟩
  | even r n _ _ ih => exact (basin_twice n).mpr ih
  | odd r n _ _ _ ih => exact (basin_step n).mp ih

theorem rank_inv {r n : ℕ} (h : Rank r n) :
    (r = 0 ∧ n = 1) ∨ (∃ k, n = 2*k ∧ 0 < k ∧ Rank r k) ∨
      (∃ r', r = r'+1 ∧ n % 2 = 1 ∧ 1 < n ∧ Rank r' (shortcut n)) := by
  cases h with
  | one => exact Or.inl ⟨rfl, rfl⟩
  | even r k hk h => exact Or.inr (Or.inl ⟨k, rfl, hk, h⟩)
  | odd r n ho hgt h => exact Or.inr (Or.inr ⟨r, rfl, ho, hgt, h⟩)

theorem rank_odd_inv {r u : ℕ} (h : Rank r u) (ho : u % 2 = 1) :
    (r = 0 ∧ u = 1) ∨ (∃ r', r = r'+1 ∧ 1 < u ∧ Rank r' (shortcut u)) := by
  rcases rank_inv h with h0 | ⟨k, hk, _, _⟩ | ⟨r', hr, _, hgt, hs⟩
  · exact Or.inl h0
  · exfalso; omega
  · exact Or.inr ⟨r', hr, hgt, hs⟩

/-- The rank is a function of the number. -/
theorem rank_unique {r n : ℕ} (h : Rank r n) : ∀ r', Rank r' n → r = r' := by
  induction h with
  | one =>
    intro r' h'
    rcases rank_inv h' with ⟨h0, _⟩ | ⟨k, hk, _, _⟩ | ⟨r'', _, _, hgt, _⟩
    · omega
    · omega
    · omega
  | even r n hn h ih =>
    intro r' h'
    rcases rank_inv h' with ⟨_, h1⟩ | ⟨k, hk, _, hr⟩ | ⟨r'', _, ho, _, _⟩
    · omega
    · have hkn : k = n := by omega
      subst hkn
      exact ih r' hr
    · omega
  | odd r n ho hgt h ih =>
    intro r' h'
    rcases rank_inv h' with ⟨_, h1⟩ | ⟨k, hk, _, _⟩ | ⟨r'', hr', _, _, hr⟩
    · omega
    · omega
    · have := ih r'' hr
      omega

theorem hits_rank : ∀ (k n : ℕ), Hits n k → ∃ r, Rank r n := by
  intro k
  induction k with
  | zero =>
    intro n h
    have h1 : n = 1 := h
    subst h1
    exact ⟨0, Rank.one⟩
  | succ k ih =>
    intro n h
    have h' : Hits (shortcut n) k := h
    obtain ⟨r, hr⟩ := ih (shortcut n) h'
    have hp := rank_pos hr
    by_cases he : n % 2 = 0
    · have hs : shortcut n = n / 2 := by simp [shortcut, he]
      rw [hs] at hr hp
      have e : n = 2 * (n/2) := by omega
      rw [e]
      exact ⟨r, Rank.even r (n/2) hp hr⟩
    · by_cases h1 : n = 1
      · subst h1; exact ⟨0, Rank.one⟩
      · exact ⟨r+1, Rank.odd r n (by omega) (by omega) hr⟩

/-- Membership in the basin is exactly: having a rank. -/
theorem basin_iff_exists_rank (n : ℕ) : Basin n ↔ ∃ r, Rank r n :=
  ⟨fun ⟨k, hk⟩ => hits_rank k n hk, fun ⟨_, hr⟩ => rank_basin hr⟩

/-! ## 2. Exact stratification of the two closure statements -/

def FwdLayer (r : ℕ) : Prop := ∀ x : ℕ, Rank r x → Basin (3*x-1)
def RevLayer (r : ℕ) : Prop := ∀ m : ℕ, 0 < m → Rank r (3*m-1) → Basin m

theorem collatz_iff_fwd_layers : (∀ n : ℕ, 0 < n → Basin n) ↔ ∀ r : ℕ, FwdLayer r := by
  constructor
  · intro all r x hx
    have := rank_pos hx
    exact all _ (by omega)
  · intro H
    rw [collatz_iff_three_minus_one_closure]
    intro x _ hb
    obtain ⟨r, hr⟩ := (basin_iff_exists_rank x).mp hb
    exact H r x hr

theorem collatz_iff_rev_layers : (∀ n : ℕ, 0 < n → Basin n) ↔ ∀ r : ℕ, RevLayer r := by
  constructor
  · intro all r m hm _
    exact all m hm
  · intro H
    apply collatz_of_open_lemma
    intro k _ hy
    obtain ⟨r, hr⟩ := (basin_iff_exists_rank _).mp hy
    exact H r (27*k+1) (by omega) hr

/-! ## 3. Odd parts; the layer families for every rank -/

theorem rank_pow_two_mul {r u : ℕ} (h : Rank r u) (b : ℕ) : Rank r (2^b*u) := by
  induction b with
  | zero => simpa using h
  | succ b ih =>
    have e : 2^(b+1)*u = 2*(2^b*u) := by grind
    rw [e]
    exact Rank.even r _ (rank_pos ih) ih

theorem rank_four_pow_mul {r u : ℕ} (h : Rank r u) (i : ℕ) : Rank r (4^i*u) := by
  induction i with
  | zero => simpa using h
  | succ i ih =>
    have e : 4^(i+1)*u = 2*(2*(4^i*u)) := by grind
    rw [e]
    have hp := rank_pos ih
    exact Rank.even r _ (by omega) (Rank.even r _ hp ih)

theorem rank_odd_part {r x : ℕ} (h : Rank r x) :
    ∃ b u, x = 2^b*u ∧ u % 2 = 1 ∧ Rank r u := by
  induction h with
  | one => exact ⟨0, 1, by simp, by omega, Rank.one⟩
  | even r n hn h ih =>
    obtain ⟨b, u, e, ho, hr⟩ := ih
    refine ⟨b+1, u, ?_, ho, hr⟩
    rw [e]; grind
  | odd r n ho hgt h _ =>
    exact ⟨0, n, by simp, ho, Rank.odd r n ho hgt h⟩

theorem basin_three_mul_pred (b u : ℕ) (hu : 0 < u) :
    Basin (3*(2^b*u) - 1) ↔ Basin (3^(b+1)*u - 1) := by
  have h := basin_pow_two_pred b (3*u) (by omega)
  have e1 : 3*(2^b*u) = 2^b*(3*u) := by grind
  have e2 : 3^(b+1)*u = 3^b*(3*u) := by grind
  rw [e1, e2]
  exact h

/-- Forward layer `r` ⟺ `3^(b+1)·u - 1 ∈ Basin` for every `b` and every odd `u` of rank `r`. -/
theorem fwd_layer_iff (r : ℕ) :
    FwdLayer r ↔ ∀ b u : ℕ, u % 2 = 1 → Rank r u → Basin (3^(b+1)*u - 1) := by
  constructor
  · intro H b u _ hr
    exact (basin_three_mul_pred b u (rank_pos hr)).mp (H _ (rank_pow_two_mul hr b))
  · intro H x hx
    obtain ⟨b, u, e, ho, hr⟩ := rank_odd_part hx
    subst e
    exact (basin_three_mul_pred b u (rank_pos hr)).mpr (H b u ho hr)

theorem four_pow_mul_mod_three (i v : ℕ) : (4^i*v) % 3 = v % 3 := by
  rw [Nat.mul_mod, four_pow_mod_three]
  simp

theorem pow_two_cases (e : ℕ) : (∃ j, 2^e = 4^j) ∨ (∃ j, 2^e = 2*4^j) := by
  induction e with
  | zero => exact Or.inl ⟨0, rfl⟩
  | succ e ih =>
    rcases ih with ⟨j, h⟩ | ⟨j, h⟩
    · exact Or.inr ⟨j, by rw [Nat.pow_succ, h]; omega⟩
    · exact Or.inl ⟨j+1, by rw [Nat.pow_succ, h, Nat.pow_succ]; omega⟩

theorem rev_arm_iff (m X : ℕ) (h : 3*m = 2*X + 1) : Basin m ↔ Basin (X+1) := by
  have hs : shortcut m = X + 1 := by unfold shortcut; split <;> omega
  rw [← hs]
  exact (basin_step m).symm

/-- Reverse layer `r` ⟺ three families over the odd `u` of rank `r`:
`(u+1)/3` (when `3 ∣ u+1`), `3^i·u + 1` (`u ≡ 1 mod 3`), `2·3^i·u + 1` (`u ≡ 2 mod 3`). -/
theorem rev_layer_iff (r : ℕ) :
    RevLayer r ↔
      (∀ u m : ℕ, u % 2 = 1 → Rank r u → 3*m = u + 1 → Basin m) ∧
      (∀ i u : ℕ, u % 2 = 1 → Rank r u → u % 3 = 1 → Basin (3^i*u + 1)) ∧
      (∀ i u : ℕ, u % 2 = 1 → Rank r u → u % 3 = 2 → Basin (3^i*(2*u) + 1)) := by
  constructor
  · intro H
    have arm : ∀ X : ℕ, X % 3 = 1 → Rank r (2*X) → Basin (X+1) := by
      intro X hX hr
      have hm : 3*((2*X+1)/3) = 2*X+1 := by omega
      have e : 3*((2*X+1)/3) - 1 = 2*X := by omega
      have hb : Basin ((2*X+1)/3) := H _ (by omega) (by rw [e]; exact hr)
      exact (rev_arm_iff _ X hm).mp hb
    refine ⟨?_, ?_, ?_⟩
    · intro u m _ hr hm
      have e : 3*m - 1 = u := by omega
      exact H m (by omega) (by rw [e]; exact hr)
    · intro i u _ hr h3
      have hmod := four_pow_mul_mod_three i u
      have hr4 := rank_four_pow_mul hr i
      have hb := arm (4^i*u) (by omega) (Rank.even r _ (rank_pos hr4) hr4)
      exact (basin_pow_four_succ i u).mp hb
    · intro i u _ hr h3
      have hmod := four_pow_mul_mod_three i (2*u)
      have hr2 : Rank r (2*u) := Rank.even r u (rank_pos hr) hr
      have hr4 := rank_four_pow_mul hr2 i
      have hb := arm (4^i*(2*u)) (by omega) (Rank.even r _ (rank_pos hr4) hr4)
      exact (basin_pow_four_succ i (2*u)).mp hb
  · rintro ⟨A, B, C⟩ m hm hr
    obtain ⟨b, u, e, ho, hru⟩ := rank_odd_part hr
    cases b with
    | zero =>
      rw [Nat.pow_zero, Nat.one_mul] at e
      exact A u m ho hru (by omega)
    | succ a =>
      have e2 : 2^(a+1)*u = 2*(2^a*u) := by grind
      rw [e2] at e
      have h3m : 3*m = 2*(2^a*u) + 1 := by omega
      rw [rev_arm_iff m (2^a*u) h3m]
      rcases pow_two_cases a with ⟨i, hi⟩ | ⟨i, hi⟩
      · rw [hi] at h3m ⊢
        have hmod := four_pow_mul_mod_three i u
        exact (basin_pow_four_succ i u).mpr (B i u ho hru (by omega))
      · have e3 : 2^a*u = 4^i*(2*u) := by rw [hi]; grind
        rw [e3] at h3m ⊢
        have hmod := four_pow_mul_mod_three i (2*u)
        exact (basin_pow_four_succ i (2*u)).mpr (C i u ho hru (by omega))

/-- Tripling form of the second reverse family: `3^(i+1)·u + 1` is one step above `3^i·u`. -/
theorem basin_triple_form (i u : ℕ) (ho : u % 2 = 1) :
    Basin (3^(i+1)*u + 1) ↔ Basin (3^i*u) := by
  have hodd : (3^i*u) % 2 = 1 := by
    rw [Nat.mul_mod, three_pow_odd, ho]
  have e : 3^(i+1)*u = 3*(3^i*u) := by grind
  rw [e]
  exact basin_odd _ hodd

/-! ## 4. The odd numbers of rank 0, 1, 2 -/

theorem rank_zero_odd {u : ℕ} (h : Rank 0 u) (ho : u % 2 = 1) : u = 1 := by
  rcases rank_odd_inv h ho with ⟨_, h1⟩ | ⟨r', hr, _, _⟩
  · exact h1
  · omega

theorem rank_zero_pow {r x : ℕ} (h : Rank r x) : r = 0 → ∃ a, x = 2^a := by
  induction h with
  | one => intro _; exact ⟨0, rfl⟩
  | even r n hn h ih =>
    intro hr
    obtain ⟨a, ha⟩ := ih hr
    exact ⟨a+1, by rw [ha, Nat.pow_succ]; omega⟩
  | odd r n ho hgt h ih => intro hr; exact absurd hr (by omega)

theorem rank_zero_four_pow (j : ℕ) : Rank 0 (4^j) := by
  induction j with
  | zero => exact Rank.one
  | succ j ih =>
    have e : 4^(j+1) = 2*(2*4^j) := by rw [Nat.pow_succ]; omega
    rw [e]
    have hp := rank_pos ih
    exact Rank.even 0 _ (by omega) (Rank.even 0 _ hp ih)

theorem four_pow_two (j : ℕ) : 4^(j+2) = 16*4^j := by
  rw [Nat.pow_succ, Nat.pow_succ]; omega

/-- Odd numbers of rank 1 are exactly `u = (4^(j+2) - 1)/3`. -/
theorem rank_one_odd {u : ℕ} (h : Rank 1 u) (ho : u % 2 = 1) : ∃ j, 3*u + 1 = 4^(j+2) := by
  rcases rank_odd_inv h ho with ⟨hr, _⟩ | ⟨r', hr, hgt, hs⟩
  · exact absurd hr (by omega)
  · have hr0 : r' = 0 := by omega
    subst hr0
    obtain ⟨a, ha⟩ := rank_zero_pow hs rfl
    have hsu : 2 * shortcut u = 3*u + 1 := by unfold shortcut; split <;> omega
    rw [ha] at hsu
    rcases pow_two_cases a with ⟨j, hj⟩ | ⟨j, hj⟩
    · have hm := four_pow_mod_three j
      rw [hj] at hsu
      exfalso; omega
    · rw [hj] at hsu
      cases j with
      | zero =>
        rw [Nat.pow_zero] at hsu
        exfalso; omega
      | succ j =>
        refine ⟨j, ?_⟩
        rw [four_pow_two]
        rw [Nat.pow_succ] at hsu
        omega

theorem rank_one_of_eq {u j : ℕ} (h : 3*u + 1 = 4^(j+2)) : Rank 1 u ∧ u % 2 = 1 := by
  rw [four_pow_two] at h
  have hpos : 0 < 4^j := Nat.pow_pos (by omega)
  have ho : u % 2 = 1 := by omega
  have hs : shortcut u = 2*(2*(2*4^j)) := by unfold shortcut; split <;> omega
  refine ⟨Rank.odd 0 u ho (by omega) ?_, ho⟩
  rw [hs]
  exact Rank.even 0 _ (by omega) (Rank.even 0 _ (by omega)
    (Rank.even 0 _ hpos (rank_zero_four_pow j)))

/-- Odd numbers of rank 2 are exactly `u = (2^(e+1)·y - 1)/3` with `y` odd of rank 1. -/
theorem rank_two_odd {u : ℕ} (h : Rank 2 u) (ho : u % 2 = 1) :
    ∃ e j y, 3*y + 1 = 4^(j+2) ∧ 3*u + 1 = 2^(e+1)*y := by
  rcases rank_odd_inv h ho with ⟨hr, _⟩ | ⟨r', hr, hgt, hs⟩
  · exact absurd hr (by omega)
  · have hr1 : r' = 1 := by omega
    subst hr1
    obtain ⟨e, y, he, hyo, hy⟩ := rank_odd_part hs
    obtain ⟨j, hj⟩ := rank_one_odd hy hyo
    refine ⟨e, j, y, hj, ?_⟩
    have hsu : 2 * shortcut u = 3*u + 1 := by unfold shortcut; split <;> omega
    rw [he] at hsu
    have e2 : 2^(e+1)*y = 2*(2^e*y) := by grind
    rw [e2]
    omega

theorem rank_two_of_eq {u e j y : ℕ} (hy : 3*y + 1 = 4^(j+2)) (hu : 3*u + 1 = 2^(e+1)*y) :
    Rank 2 u ∧ u % 2 = 1 := by
  obtain ⟨hr, _⟩ := rank_one_of_eq hy
  have e2 : 2^(e+1)*y = 2*(2^e*y) := by grind
  rw [e2] at hu
  rw [four_pow_two] at hy
  have hpos : 0 < 4^j := Nat.pow_pos (by omega)
  have h1 : 1 ≤ 2^e := Nat.pow_pos (by omega)
  have h2 : 1*y ≤ 2^e*y := Nat.mul_le_mul_right y h1
  have ho : u % 2 = 1 := by omega
  have hs : shortcut u = 2^e*y := by unfold shortcut; split <;> omega
  refine ⟨Rank.odd 1 u ho (by omega) ?_, ho⟩
  rw [hs]
  exact rank_pow_two_mul hr e

/-! ## 5. Forward layers 0, 1, 2 as explicit exponential families -/

theorem fwd_form (b u Z : ℕ) (h : 3*u + 1 = Z) : 3^(b+1)*u - 1 = 3^b*Z - (3^b + 1) := by
  subst h
  have e1 : 3^(b+1)*u = 3^b*(3*u) := by grind
  have e2 : 3^b*(3*u+1) = 3^b*(3*u) + 3^b := by grind
  rw [e1, e2]
  omega

/-- Forward rank 0 ⟺ every `3^(b+1) - 1` converges. -/
theorem fwd_layer_zero_iff : FwdLayer 0 ↔ ∀ b : ℕ, Basin (3^(b+1) - 1) := by
  rw [fwd_layer_iff]
  constructor
  · intro H b
    have h := H b 1 (by omega) Rank.one
    rw [Nat.mul_one] at h
    exact h
  · intro H b u ho hr
    have h1 := rank_zero_odd hr ho
    subst h1
    rw [Nat.mul_one]
    exact H b

/-- Forward rank 0 ⟺ every Mersenne number converges. -/
theorem fwd_layer_zero_iff_mersenne : FwdLayer 0 ↔ ∀ a : ℕ, Basin (2^(a+1) - 1) := by
  rw [fwd_layer_zero_iff]
  have key (a : ℕ) : Basin (2^(a+1) - 1) ↔ Basin (3^(a+1) - 1) := by
    have h := basin_pow_two_pred (a+1) 1 (by omega)
    rw [Nat.mul_one, Nat.mul_one] at h
    exact h
  exact ⟨fun H a => (key a).mpr (H a), fun H b => (key b).mp (H b)⟩

/-- Forward rank 1 ⟺ the two-parameter family `3^b·4^(j+2) - (3^b + 1)`. -/
theorem fwd_layer_one_iff :
    FwdLayer 1 ↔ ∀ b j : ℕ, Basin (3^b*4^(j+2) - (3^b + 1)) := by
  rw [fwd_layer_iff]
  constructor
  · intro H b j
    have hmod := four_pow_mod_three (j+2)
    have hpos : 0 < 4^(j+2) := Nat.pow_pos (by omega)
    have hu : 3*((4^(j+2)-1)/3) + 1 = 4^(j+2) := by omega
    obtain ⟨hr, ho⟩ := rank_one_of_eq hu
    have h := H b _ ho hr
    rw [fwd_form b _ _ hu] at h
    exact h
  · intro H b u ho hr
    obtain ⟨j, hj⟩ := rank_one_odd hr ho
    rw [fwd_form b u _ hj]
    exact H b j

/-- Forward rank 2 ⟺ the three-parameter family `3^b·2^(e+1)·y_j - (3^b + 1)`,
`y_j = (4^(j+2)-1)/3`, on the exponents with `2^(e+1)·y_j ≡ 1 (mod 3)`. -/
theorem fwd_layer_two_iff :
    FwdLayer 2 ↔ ∀ b e j y : ℕ, 3*y + 1 = 4^(j+2) → (2^(e+1)*y) % 3 = 1 →
      Basin (3^b*(2^(e+1)*y) - (3^b + 1)) := by
  rw [fwd_layer_iff]
  constructor
  · intro H b e j y hy hmod
    have hu : 3*((2^(e+1)*y - 1)/3) + 1 = 2^(e+1)*y := by omega
    obtain ⟨hr, ho⟩ := rank_two_of_eq hy hu
    have h := H b _ ho hr
    rw [fwd_form b _ _ hu] at h
    exact h
  · intro H b u ho hr
    obtain ⟨e, j, y, hj, hu⟩ := rank_two_odd hr ho
    rw [fwd_form b u _ hu]
    exact H b e j y hj (by omega)

/-! ## 6. Reverse layers 0, 1, 2 -/

/-- Reverse rank 0 ⟺ every power of three converges (cf. `first_layer_iff_pow_three`). -/
theorem rev_layer_zero_iff : RevLayer 0 ↔ ∀ i : ℕ, Basin (3^i) := by
  rw [rev_layer_iff]
  constructor
  · rintro ⟨_, B, _⟩ i
    have h := B (i+1) 1 (by omega) Rank.one (by omega)
    have e : 3^(i+1)*1 + 1 = 3*3^i + 1 := by rw [Nat.pow_succ]; omega
    rw [e] at h
    exact (basin_odd (3^i) (three_pow_odd i)).mp h
  · intro P
    refine ⟨?_, ?_, ?_⟩
    · intro u m ho hr hm
      have h1 := rank_zero_odd hr ho
      exfalso; omega
    · intro i u ho hr _
      have h1 := rank_zero_odd hr ho
      subst h1
      cases i with
      | zero => exact ⟨1, rfl⟩
      | succ i =>
        have e : 3^(i+1)*1 + 1 = 3*3^i + 1 := by rw [Nat.pow_succ]; omega
        rw [e]
        exact (basin_odd (3^i) (three_pow_odd i)).mpr (P i)
    · intro i u ho hr h3
      have h1 := rank_zero_odd hr ho
      exfalso; omega

theorem rev_form_one (k u Z : ℕ) (h : 3*u + 1 = Z) :
    3^(k+1)*u + 1 = 3^k*Z - (3^k - 1) := by
  subst h
  have e1 : 3^(k+1)*u = 3^k*(3*u) := by grind
  have e2 : 3^k*(3*u+1) = 3^k*(3*u) + 3^k := by grind
  have hp : 0 < 3^k := Nat.pow_pos (by omega)
  rw [e1, e2]
  omega

theorem rev_form_two (k u Z : ℕ) (h : 3*u + 1 = Z) :
    3^(k+1)*(2*u) + 1 = 3^k*(2*Z) - (2*3^k - 1) := by
  subst h
  have e1 : 3^(k+1)*(2*u) = 2*(3^k*(3*u)) := by grind
  have e2 : 3^k*(2*(3*u+1)) = 2*(3^k*(3*u)) + 2*3^k := by grind
  have hp : 0 < 3^k := Nat.pow_pos (by omega)
  rw [e1, e2]
  omega

/-- Even arm of reverse rank 1: `m = (4^(i+3)+2)/9` converges iff `3^i` does. -/
theorem rev_one_even (i u m : ℕ) (hu : 3*u + 1 = 4^(i+3)) (hm : 3*m = u + 1) :
    Basin m ↔ Basin (3^i) := by
  have e : 4^(i+3) = 16*4^(i+1) := by rw [Nat.pow_succ, Nat.pow_succ]; omega
  rw [e] at hu
  obtain ⟨m', rfl⟩ : ∃ m', m = 2*m' := ⟨m/2, by omega⟩
  obtain ⟨m'', hm''⟩ : ∃ m'', 3*m' + 1 = 4*m'' := ⟨(3*m'+1)/4, by omega⟩
  have hJ : 3*m'' = 2*4^(i+1) + 1 := by omega
  have hs : shortcut m' = 2*m'' := by unfold shortcut; split <;> omega
  have h1 := basin_twice m'
  have h2 := basin_step m'
  rw [hs] at h2
  have h3 := basin_twice m''
  exact h1.trans (h2.symm.trans (h3.trans (basin_jacobsthal i m'' hJ)))

theorem rev_one_base (j u : ℕ) (hu : 3*u + 1 = 4^(j+2)) : Basin (u + 1) ↔ Basin (3^j) := by
  have e : 4^(j+2) = 4*4^(j+1) := by rw [Nat.pow_succ]; omega
  rw [e] at hu
  obtain ⟨m, hm⟩ : ∃ m, u + 1 = 2*m := ⟨(u+1)/2, by omega⟩
  have hJ : 3*m = 2*4^(j+1) + 1 := by omega
  rw [hm]
  exact (basin_twice m).trans (basin_jacobsthal j m hJ)

theorem rev_one_base_two (j u : ℕ) (hu : 3*u + 1 = 4^(j+2)) :
    Basin (2*u + 1) ↔ Basin (3^(j+1)) := by
  have h : 3*(2*u+1) = 2*4^(j+2) + 1 := by omega
  exact basin_jacobsthal (j+1) (2*u+1) h

/-- Reverse rank 1 ⟺ powers of three (three sub-progressions of exponents) together with
the two two-parameter families `3^k·4^n - (3^k - 1)` and `3^k·2·4^n - (2·3^k - 1)`. -/
theorem rev_layer_one_iff :
    RevLayer 1 ↔
      (∀ i m : ℕ, 9*m = 4^(i+3) + 2 → Basin (3^i)) ∧
      (∀ j u : ℕ, 3*u + 1 = 4^(j+2) → u % 3 = 1 → Basin (3^j)) ∧
      (∀ k j u : ℕ, 3*u + 1 = 4^(j+2) → u % 3 = 1 → Basin (3^k*4^(j+2) - (3^k - 1))) ∧
      (∀ j u : ℕ, 3*u + 1 = 4^(j+2) → u % 3 = 2 → Basin (3^(j+1))) ∧
      (∀ k j u : ℕ, 3*u + 1 = 4^(j+2) → u % 3 = 2 →
        Basin (3^k*(2*4^(j+2)) - (2*3^k - 1))) := by
  rw [rev_layer_iff]
  constructor
  · rintro ⟨A, B, C⟩
    refine ⟨?_, ?_, ?_, ?_, ?_⟩
    · intro i m hm
      have hu : 3*(3*m-1) + 1 = 4^(i+3) := by
        generalize 4^(i+3) = X at hm ⊢
        omega
      have hu' : 3*(3*m-1) + 1 = 4^(i+1+2) := hu
      obtain ⟨hr, ho⟩ := rank_one_of_eq hu'
      have h3m : 3*m = (3*m-1) + 1 := by omega
      exact (rev_one_even i _ m hu h3m).mp (A _ m ho hr h3m)
    · intro j u hu h3
      obtain ⟨hr, ho⟩ := rank_one_of_eq hu
      have h := B 0 u ho hr h3
      rw [Nat.pow_zero, Nat.one_mul] at h
      exact (rev_one_base j u hu).mp h
    · intro k j u hu h3
      obtain ⟨hr, ho⟩ := rank_one_of_eq hu
      have h := B (k+1) u ho hr h3
      rw [rev_form_one k u _ hu] at h
      exact h
    · intro j u hu h3
      obtain ⟨hr, ho⟩ := rank_one_of_eq hu
      have h := C 0 u ho hr h3
      rw [Nat.pow_zero, Nat.one_mul] at h
      exact (rev_one_base_two j u hu).mp h
    · intro k j u hu h3
      obtain ⟨hr, ho⟩ := rank_one_of_eq hu
      have h := C (k+1) u ho hr h3
      rw [rev_form_two k u _ hu] at h
      exact h
  · rintro ⟨E, B0, B1, C0, C1⟩
    refine ⟨?_, ?_, ?_⟩
    · intro u m ho hr hm
      obtain ⟨j, hj⟩ := rank_one_odd hr ho
      cases j with
      | zero =>
        have h16 : (4:ℕ)^(0+2) = 16 := by decide
        rw [h16] at hj
        have hm2 : m = 2 := by omega
        subst hm2
        exact ⟨1, rfl⟩
      | succ i =>
        have hj' : 3*u + 1 = 4^(i+3) := hj
        exact (rev_one_even i u m hj' hm).mpr (E i m (by omega))
    · intro i u ho hr h3
      obtain ⟨j, hj⟩ := rank_one_odd hr ho
      cases i with
      | zero =>
        rw [Nat.pow_zero, Nat.one_mul]
        exact (rev_one_base j u hj).mpr (B0 j u hj h3)
      | succ k =>
        rw [rev_form_one k u _ hj]
        exact B1 k j u hj h3
    · intro i u ho hr h3
      obtain ⟨j, hj⟩ := rank_one_odd hr ho
      cases i with
      | zero =>
        rw [Nat.pow_zero, Nat.one_mul]
        exact (rev_one_base_two j u hj).mpr (C0 j u hj h3)
      | succ k =>
        rw [rev_form_two k u _ hj]
        exact C1 k j u hj h3

/-- Reverse rank 2, in terms of the rank-2 odd numbers `u = (2^(e+1)·y_j - 1)/3`. -/
theorem rev_layer_two_iff :
    RevLayer 2 ↔
      (∀ e j y u m : ℕ, 3*y + 1 = 4^(j+2) → 3*u + 1 = 2^(e+1)*y → 3*m = u + 1 → Basin m) ∧
      (∀ i e j y u : ℕ, 3*y + 1 = 4^(j+2) → 3*u + 1 = 2^(e+1)*y → u % 3 = 1 →
        Basin (3^i*u + 1)) ∧
      (∀ i e j y u : ℕ, 3*y + 1 = 4^(j+2) → 3*u + 1 = 2^(e+1)*y → u % 3 = 2 →
        Basin (3^i*(2*u) + 1)) := by
  rw [rev_layer_iff]
  constructor
  · rintro ⟨A, B, C⟩
    refine ⟨?_, ?_, ?_⟩
    · intro e j y u m hy hu hm
      obtain ⟨hr, ho⟩ := rank_two_of_eq hy hu
      exact A u m ho hr hm
    · intro i e j y u hy hu h3
      obtain ⟨hr, ho⟩ := rank_two_of_eq hy hu
      exact B i u ho hr h3
    · intro i e j y u hy hu h3
      obtain ⟨hr, ho⟩ := rank_two_of_eq hy hu
      exact C i u ho hr h3
  · rintro ⟨A, B, C⟩
    refine ⟨?_, ?_, ?_⟩
    · intro u m ho hr hm
      obtain ⟨e, j, y, hy, hu⟩ := rank_two_odd hr ho
      exact A e j y u m hy hu hm
    · intro i u ho hr h3
      obtain ⟨e, j, y, hy, hu⟩ := rank_two_odd hr ho
      exact B i e j y u hy hu h3
    · intro i u ho hr h3
      obtain ⟨e, j, y, hy, hu⟩ := rank_two_odd hr ho
      exact C i e j y u hy hu h3

/-! ## 7. Iterated shadow law: `2^t·w - c` follows the `3x-1` orbit of `c` -/

/-- `t`-fold iterate of the `3x-1` shortcut map `S`. -/
def Sit : ℕ → ℕ → ℕ
  | 0, c => c
  | t+1, c => Sit t (S c)

/-- Number of odd points among `c, S c, …, S^(t-1) c`. -/
def Sodd : ℕ → ℕ → ℕ
  | 0, _ => 0
  | t+1, c => c % 2 + Sodd t (S c)

theorem shortcut_shadow (Y c : ℕ) (hc : c < 2*Y) :
    shortcut (2*Y - c) = 3^(c%2)*Y - S c := by
  rcases Nat.mod_two_eq_zero_or_one c with h | h
  · have hS : S c = c / 2 := by simp [S, h]
    rw [h, hS, Nat.pow_zero, Nat.one_mul]
    unfold shortcut; split <;> omega
  · have hS : S c = (3*c - 1) / 2 := by simp [S, h]
    rw [h, hS, Nat.pow_one]
    unfold shortcut; split <;> omega

theorem S_lt (c X : ℕ) (hc : c < 2*X) : S c < 3^(c%2)*X := by
  rcases Nat.mod_two_eq_zero_or_one c with h | h
  · have hS : S c = c / 2 := by simp [S, h]
    rw [h, hS, Nat.pow_zero, Nat.one_mul]
    omega
  · have hS : S c = (3*c - 1) / 2 := by simp [S, h]
    rw [h, hS, Nat.pow_one]
    omega

/-- Landing law: `2^t·w - c` and `3^(odd count)·w - S^t(c)` are in the same component. -/
theorem basin_shadow_iter (t : ℕ) : ∀ w c : ℕ, c < 2^t*w →
    (Basin (2^t*w - c) ↔ Basin (3^(Sodd t c)*w - Sit t c)) := by
  induction t with
  | zero => intro w c _; simp [Sodd, Sit]
  | succ t ih =>
    intro w c hc
    have e1 : 2^(t+1)*w = 2*(2^t*w) := by grind
    rw [e1] at hc ⊢
    have hstep := shortcut_shadow (2^t*w) c hc
    have e2 : 3^(c%2)*(2^t*w) = 2^t*(3^(c%2)*w) := Nat.mul_left_comm _ _ _
    have hlt : S c < 2^t*(3^(c%2)*w) := by
      rw [← e2]; exact S_lt c (2^t*w) hc
    have hih := ih (3^(c%2)*w) (S c) hlt
    have e4 : 3^(Sodd t (S c))*(3^(c%2)*w) = 3^(c%2 + Sodd t (S c))*w := by
      rw [Nat.pow_add]; grind
    rw [e4] at hih
    have hb := basin_step (2*(2^t*w) - c)
    rw [hstep, e2] at hb
    exact hb.symm.trans hih

theorem Sit_add (s t : ℕ) : ∀ c : ℕ, Sit (s+t) c = Sit t (Sit s c) := by
  induction s with
  | zero => intro c; simp [Sit]
  | succ s ih =>
    intro c
    have e : s + 1 + t = (s + t) + 1 := by omega
    rw [e]
    exact ih (S c)

theorem Sodd_add (s t : ℕ) : ∀ c : ℕ, Sodd (s+t) c = Sodd s c + Sodd t (Sit s c) := by
  induction s with
  | zero => intro c; simp [Sodd, Sit]
  | succ s ih =>
    intro c
    have e : s + 1 + t = (s + t) + 1 := by omega
    rw [e]
    show c % 2 + Sodd (s+t) (S c) = c % 2 + Sodd s (S c) + Sodd t (Sit s (S c))
    rw [ih (S c)]
    omega

theorem S_one : S 1 = 1 := by decide

theorem Sit_one (t : ℕ) : Sit t 1 = 1 := by
  induction t with
  | zero => rfl
  | succ t ih =>
    show Sit t (S 1) = 1
    rw [S_one]; exact ih

theorem Sodd_one (t : ℕ) : Sodd t 1 = t := by
  induction t with
  | zero => rfl
  | succ t ih =>
    show 1 % 2 + Sodd t (S 1) = t + 1
    rw [S_one, ih]; omega

/-- Landing of the forward rank-1 family: after `2(j+2)` steps the member `3^b·4^(j+2)-(3^b+1)`
sits at `3^K - c`, where `(K, c)` is the decorated `3x-1` orbit point of `3^b + 1`. -/
theorem fwd_one_landing (b j : ℕ) :
    Basin (3^b*4^(j+2) - (3^b + 1)) ↔
      Basin (3^(b + Sodd (2*(j+2)) (3^b+1)) - Sit (2*(j+2)) (3^b+1)) := by
  have e : 3^b*4^(j+2) = 2^(2*(j+2))*3^b := by
    rw [Nat.pow_mul]; exact Nat.mul_comm _ _
  have hlt : 3^b + 1 < 2^(2*(j+2))*3^b := by
    rw [← e, four_pow_two]
    have hp : 0 < 4^j := Nat.pow_pos (by omega)
    have hq : 0 < 3^b := Nat.pow_pos (by omega)
    have h1 : 3^b*16 ≤ 3^b*(16*4^j) := Nat.mul_le_mul_left _ (by omega)
    omega
  have h := basin_shadow_iter (2*(j+2)) (3^b) (3^b+1) hlt
  rw [← e] at h
  have e5 : 3^(Sodd (2*(j+2)) (3^b+1))*3^b = 3^(b + Sodd (2*(j+2)) (3^b+1)) := by
    rw [Nat.pow_add]; exact Nat.mul_comm _ _
  rw [e5] at h
  exact h

/-- Forward rank 1 in landing form. -/
theorem fwd_layer_one_iff_landing :
    FwdLayer 1 ↔ ∀ b j : ℕ,
      Basin (3^(b + Sodd (2*(j+2)) (3^b+1)) - Sit (2*(j+2)) (3^b+1)) := by
  rw [fwd_layer_one_iff]
  exact ⟨fun H b j => (fwd_one_landing b j).mp (H b j),
         fun H b j => (fwd_one_landing b j).mpr (H b j)⟩

/-- Cone rule: once the `3x-1` orbit of `3^b + 1` has reached 1 (at time `s`), every member
with `2(j+2) ≥ s` is in the component of a number `3^K - 1`. -/
theorem fwd_one_cone (b j s : ℕ) (hs : Sit s (3^b+1) = 1) (hle : s ≤ 2*(j+2)) :
    Basin (3^b*4^(j+2) - (3^b + 1)) ↔
      Basin (3^(b + Sodd s (3^b+1) + (2*(j+2) - s)) - 1) := by
  have h := fwd_one_landing b j
  obtain ⟨d, hd⟩ : ∃ d, 2*(j+2) = s + d := ⟨2*(j+2) - s, by omega⟩
  rw [hd, Sit_add, Sodd_add, hs, Sit_one, Sodd_one] at h
  have e : s + d - s = d := by omega
  rw [hd, e]
  have e2 : b + (Sodd s (3^b+1) + d) = b + Sodd s (3^b+1) + d := by omega
  rw [e2] at h
  exact h

/-- General landing law for a power-of-two multiple of a power of three. -/
theorem basin_landing (k t c : ℕ) (hc : c < 2^t*3^k) :
    Basin (2^t*3^k - c) ↔ Basin (3^(k + Sodd t c) - Sit t c) := by
  have h := basin_shadow_iter t (3^k) c hc
  have e5 : 3^(Sodd t c)*3^k = 3^(k + Sodd t c) := by
    rw [Nat.pow_add]; exact Nat.mul_comm _ _
  rw [e5] at h
  exact h

theorem two_le_pow_succ (e : ℕ) : 2 ≤ 2^(e+1) := by
  have hp : 0 < 2^e := Nat.pow_pos (by omega)
  rw [Nat.pow_succ]; omega

/-- First stage of the forward rank-2 family: the `e+1` halvings of `2^(e+1)·y` move the
constant `3^b + 1` along its `3x-1` orbit. -/
theorem fwd_two_stage (b e y : ℕ) (hy : 1 < y) :
    Basin (3^b*(2^(e+1)*y) - (3^b + 1)) ↔
      Basin (3^(b + Sodd (e+1) (3^b+1))*y - Sit (e+1) (3^b+1)) := by
  have hq : 0 < 3^b := Nat.pow_pos (by omega)
  have h1 : 3^b*2 ≤ 3^b*y := Nat.mul_le_mul_left _ (by omega)
  have h2 : 2*(3^b*y) ≤ 2^(e+1)*(3^b*y) := Nat.mul_le_mul_right _ (two_le_pow_succ e)
  have hlt : 3^b + 1 < 2^(e+1)*(3^b*y) := by
    generalize 2^(e+1)*(3^b*y) = Q at h2 ⊢
    generalize 3^b*y = P at h1 h2
    generalize 3^b = A at hq h1 ⊢
    omega
  have h := basin_shadow_iter (e+1) (3^b*y) (3^b+1) hlt
  have e1 : 3^b*(2^(e+1)*y) = 2^(e+1)*(3^b*y) := Nat.mul_left_comm _ _ _
  have e2 : 3^(Sodd (e+1) (3^b+1))*(3^b*y) = 3^(b + Sodd (e+1) (3^b+1))*y := by
    rw [Nat.pow_add]; grind
  rw [e1]
  rw [e2] at h
  exact h

/-- Rank-2 cone: if the `3x-1` orbit of `3^b + 1` is at 1 after the `e+1` halvings, the
rank-2 member is in the component of a member of the rank-1 family (not of a one-parameter
family). -/
theorem fwd_two_cone (b e j y k : ℕ) (hy : 3*y + 1 = 4^(j+2))
    (hs : Sit (e+1) (3^b+1) = 1) (hk : b + Sodd (e+1) (3^b+1) = k+1) :
    Basin (3^b*(2^(e+1)*y) - (3^b + 1)) ↔ Basin (3^k*4^(j+2) - (3^k + 1)) := by
  have hy1 : 1 < y := by
    have h16 := four_pow_two j
    have hp : 0 < 4^j := Nat.pow_pos (by omega)
    generalize 4^(j+2) = X at hy h16
    generalize 4^j = Z at h16 hp
    omega
  have h := fwd_two_stage b e y hy1
  rw [hs, hk] at h
  rw [← fwd_form k y _ hy]
  exact h

theorem Sit_period (p c : ℕ) (hp : Sit p c = c) : ∀ i : ℕ, Sit (p*i) c = c := by
  intro i
  induction i with
  | zero => simp [Sit]
  | succ i ih =>
    have e : p*(i+1) = p*i + p := Nat.mul_succ p i
    rw [e, Sit_add, ih]
    exact hp

theorem Sodd_period (p c : ℕ) (hp : Sit p c = c) : ∀ i : ℕ, Sodd (p*i) c = i * Sodd p c := by
  intro i
  induction i with
  | zero => simp [Sodd]
  | succ i ih =>
    have e : p*(i+1) = p*i + p := Nat.mul_succ p i
    rw [e, Sodd_add, ih, Sit_period p c hp i, Nat.add_one_mul]

/-- General cone rule: if the `3x-1` orbit of `3^b + 1` is periodic from time `s` on, with
period `p`, then the whole `j`-family of that `b` lies in at most `p` one-parameter families
`3^(K₀ + i·q) - c_d` with `c_d` on the cycle.  No list of cycles is assumed. -/
theorem fwd_one_cone_cycle (b j s p i d : ℕ)
    (hper : Sit p (Sit s (3^b+1)) = Sit s (3^b+1)) (ht : 2*(j+2) = s + p*i + d) :
    Basin (3^b*4^(j+2) - (3^b + 1)) ↔
      Basin (3^(b + (Sodd s (3^b+1) + i * Sodd p (Sit s (3^b+1)) + Sodd d (Sit s (3^b+1))))
        - Sit d (Sit s (3^b+1))) := by
  have h := fwd_one_landing b j
  rw [ht] at h
  rw [Sit_add (s + p*i) d, Sit_add s (p*i), Sit_period p _ hper i] at h
  rw [Sodd_add (s + p*i) d, Sodd_add s (p*i), Sit_add s (p*i), Sit_period p _ hper i,
    Sodd_period p _ hper i] at h
  exact h

/-- A concrete instance of the cone rule: for `b = 6` the `3x-1` orbit of `3^6 + 1 = 730`
reaches 1 in 19 steps, 6 of them odd. -/
theorem fwd_one_b6 (j : ℕ) (h : 19 ≤ 2*(j+2)) :
    Basin (3^6*4^(j+2) - (3^6 + 1)) ↔ Basin (3^(6 + 6 + (2*(j+2) - 19)) - 1) := by
  have hs : Sit 19 (3^6+1) = 1 := by decide
  have ho : Sodd 19 (3^6+1) = 6 := by decide
  have hc := fwd_one_cone 6 j 19 hs h
  rw [ho] at hc
  exact hc

theorem landing_of_lt (k t c : ℕ) (hc : c < 3^k) : c < 2^t*3^k := by
  have h1 : 1 ≤ 2^t := Nat.pow_pos (by omega)
  have h2 : 1*3^k ≤ 2^t*3^k := Nat.mul_le_mul_right _ h1
  generalize 2^t*3^k = Q at h2 ⊢
  generalize 3^k = A at hc h2
  omega

theorem two_pow_double (n : ℕ) : 2^(2*n) = 4^n := Nat.pow_mul 2 2 n

/-- Landing of the first reverse rank-1 family `3^k·4^n - (3^k - 1)`. -/
theorem rev_one_a_landing (k j : ℕ) :
    Basin (3^k*4^(j+2) - (3^k - 1)) ↔
      Basin (3^(k + Sodd (2*(j+2)) (3^k-1)) - Sit (2*(j+2)) (3^k-1)) := by
  have e : 3^k*4^(j+2) = 2^(2*(j+2))*3^k := by
    rw [two_pow_double]; exact Nat.mul_comm _ _
  have hq : 0 < 3^k := Nat.pow_pos (by omega)
  have h := basin_landing k (2*(j+2)) (3^k-1) (landing_of_lt k _ _ (Nat.sub_lt hq (by omega)))
  rw [← e] at h
  exact h

/-- Landing of the second reverse rank-1 family `3^k·2·4^n - (2·3^k - 1)`. -/
theorem rev_one_b_landing (k j : ℕ) :
    Basin (3^k*(2*4^(j+2)) - (2*3^k - 1)) ↔
      Basin (3^(k + Sodd (2*(j+2)+1) (2*3^k-1)) - Sit (2*(j+2)+1) (2*3^k-1)) := by
  have e0 : 2^(2*(j+2)+1) = 2^(2*(j+2))*2 := Nat.pow_succ _ _
  have e : 3^k*(2*4^(j+2)) = 2^(2*(j+2)+1)*3^k := by
    rw [e0, two_pow_double]; grind
  have hq : 0 < 3^k := Nat.pow_pos (by omega)
  have h2 : 2*3^k ≤ 2^(2*(j+2)+1)*3^k := Nat.mul_le_mul_right _ (two_le_pow_succ _)
  have hlt : 2*3^k - 1 < 2^(2*(j+2)+1)*3^k := by
    generalize 2^(2*(j+2)+1)*3^k = Q at h2 ⊢
    generalize 3^k = A at hq h2 ⊢
    omega
  have h := basin_landing k (2*(j+2)+1) (2*3^k-1) hlt
  rw [← e] at h
  exact h

/-- The `k = 0` slice of the second reverse rank-1 family is the odd-index Mersenne numbers.
(On `j+2 ≡ 5 (mod 6)` this slice is the unbounded family of PR #177.) -/
theorem rev_one_b_k0 (j : ℕ) : 3^0*(2*4^(j+2)) - (2*3^0 - 1) = 2^(2*(j+2)+1) - 1 := by
  have e0 : 2^(2*(j+2)+1) = 2^(2*(j+2))*2 := Nat.pow_succ _ _
  rw [e0, two_pow_double, Nat.pow_zero]
  generalize 4^(j+2) = X
  omega

/-! ## 8. Parity fold of the forward families -/

/-- For `x ≡ 3 (mod 4)`: `x - 1` and `3x - 1` are in the same component. -/
theorem basin_pred_fold (x : ℕ) (h : x % 4 = 3) : Basin (x - 1) ↔ Basin (3*x - 1) := by
  obtain ⟨t, rfl⟩ : ∃ t, x = 4*t+3 := ⟨x/4, by omega⟩
  have h1 := basin_twice (2*t+1)
  have h2 := basin_step (2*t+1)
  have hs : shortcut (2*t+1) = 3*t+2 := by unfold shortcut; split <;> omega
  rw [hs] at h2
  have h3 := basin_twice (2*(3*t+2))
  have h4 := basin_twice (3*t+2)
  have e1 : 4*t+3-1 = 2*(2*t+1) := by omega
  have e2 : 3*(4*t+3)-1 = 2*(2*(3*t+2)) := by omega
  rw [e1, e2]
  exact h1.trans (h2.symm.trans (h4.symm.trans h3.symm))

/-- Consecutive exponents of a forward family merge when `3^k·u ≡ 3 (mod 4)`.
For `u = 1` this is the fold of PR #176 (`ternary_even_exponent_fold`). -/
theorem fwd_family_fold (k u : ℕ) (h : (3^k*u) % 4 = 3) :
    Basin (3^k*u - 1) ↔ Basin (3^(k+1)*u - 1) := by
  have e : 3^(k+1)*u = 3*(3^k*u) := by grind
  rw [e]
  exact basin_pred_fold _ h

theorem three_pow_odd_mod_four (n : ℕ) : 3^(2*n+1) % 4 = 3 := by
  induction n with
  | zero => rfl
  | succ n ih =>
    have e : 3^(2*(n+1)+1) = 9*3^(2*n+1) := by
      have e0 : 2*(n+1)+1 = (2*n+1)+1+1 := by omega
      rw [e0, Nat.pow_succ, Nat.pow_succ]; omega
    rw [e]; omega

/-- The forward rank-1 family folds two-to-one in `b`. -/
theorem fwd_one_fold (n j : ℕ) :
    Basin (3^(2*n)*4^(j+2) - (3^(2*n) + 1)) ↔
      Basin (3^(2*n+1)*4^(j+2) - (3^(2*n+1) + 1)) := by
  have hmod := four_pow_mod_three (j+2)
  have hpos : 0 < 4^(j+2) := Nat.pow_pos (by omega)
  have hu : 3*((4^(j+2)-1)/3) + 1 = 4^(j+2) := by omega
  have h4 : ((4^(j+2)-1)/3) % 4 = 1 := by
    have := four_pow_two j
    omega
  have h3 := three_pow_odd_mod_four n
  have hm : (3^(2*n+1)*((4^(j+2)-1)/3)) % 4 = 3 := by
    rw [Nat.mul_mod, h3, h4]
  have hf := fwd_family_fold (2*n+1) _ hm
  rw [fwd_form (2*n) _ _ hu, fwd_form (2*n+1) _ _ hu] at hf
  exact hf

theorem three_pow_even_mod_eight (n : ℕ) : 3^(2*n) % 8 = 1 := by
  induction n with
  | zero => rfl
  | succ n ih =>
    have e : 3^(2*(n+1)) = 9*3^(2*n) := by
      have e0 : 2*(n+1) = 2*n+1+1 := by omega
      rw [e0, Nat.pow_succ, Nat.pow_succ]; omega
    rw [e]; omega

theorem fold_three_steps (A P : ℕ) (hA : A % 8 = 1) (hP : A ≤ P) :
    Basin (16*P - (A+1)) ↔ Basin (18*P - (9*A-1)/8) := by
  have h1 := basin_twice (8*P - (A+1)/2)
  have e1 : 16*P - (A+1) = 2*(8*P - (A+1)/2) := by omega
  have h2 := basin_step (8*P - (A+1)/2)
  have hs2 : shortcut (8*P - (A+1)/2) = 12*P - (3*A+1)/4 := by
    unfold shortcut; split <;> omega
  have h3 := basin_step (12*P - (3*A+1)/4)
  have hs3 : shortcut (12*P - (3*A+1)/4) = 18*P - (9*A-1)/8 := by
    unfold shortcut; split <;> omega
  rw [hs2] at h2
  rw [hs3] at h3
  rw [e1]
  exact h1.trans (h2.symm.trans h3.symm)

/-- The folded rank-1 family in canonical form: `F1(2n, j)` (and `F1(2n+1, j)`, by
`fwd_one_fold`) is in the component of
`18·9^n·4^j - (9^(n+1) - 1)/8 = 9^(n+1)·2^(2j+1) - (9^(n+1) - 1)/8`. -/
theorem fwd_one_fold_landing (n j : ℕ) :
    Basin (3^(2*n)*4^(j+2) - (3^(2*n) + 1)) ↔
      Basin (18*(3^(2*n)*4^j) - (9*3^(2*n) - 1)/8) := by
  have hA := three_pow_even_mod_eight n
  have hp : 1 ≤ 4^j := Nat.pow_pos (by omega)
  have hP : 3^(2*n)*1 ≤ 3^(2*n)*4^j := Nat.mul_le_mul_left _ hp
  rw [Nat.mul_one] at hP
  have e : 3^(2*n)*4^(j+2) = 16*(3^(2*n)*4^j) := by
    rw [four_pow_two]; exact Nat.mul_left_comm _ _ _
  rw [e]
  exact fold_three_steps _ _ hA hP

end CollatzLayers

open CollatzLayers in
#print axioms collatz_iff_fwd_layers
open CollatzLayers in
#print axioms collatz_iff_rev_layers
open CollatzLayers in
#print axioms rank_unique
open CollatzLayers in
#print axioms fwd_layer_iff
open CollatzLayers in
#print axioms rev_layer_iff
open CollatzLayers in
#print axioms fwd_layer_zero_iff_mersenne
open CollatzLayers in
#print axioms fwd_layer_one_iff
open CollatzLayers in
#print axioms fwd_layer_two_iff
open CollatzLayers in
#print axioms rev_layer_zero_iff
open CollatzLayers in
#print axioms rev_layer_one_iff
open CollatzLayers in
#print axioms rev_layer_two_iff
open CollatzLayers in
#print axioms basin_shadow_iter
open CollatzLayers in
#print axioms fwd_layer_one_iff_landing
open CollatzLayers in
#print axioms fwd_one_cone
open CollatzLayers in
#print axioms fwd_one_fold
open CollatzLayers in
#print axioms basin_triple_form
open CollatzLayers in
#print axioms basin_landing
open CollatzLayers in
#print axioms fwd_two_stage
open CollatzLayers in
#print axioms fwd_two_cone
open CollatzLayers in
#print axioms basin_iff_exists_rank
open CollatzLayers in
#print axioms fwd_family_fold
open CollatzLayers in
#print axioms fwd_one_cone_cycle
open CollatzLayers in
#print axioms fwd_one_b6
open CollatzLayers in
#print axioms rev_one_a_landing
open CollatzLayers in
#print axioms rev_one_b_landing
open CollatzLayers in
#print axioms rev_one_b_k0
open CollatzLayers in
#print axioms fwd_one_fold_landing
