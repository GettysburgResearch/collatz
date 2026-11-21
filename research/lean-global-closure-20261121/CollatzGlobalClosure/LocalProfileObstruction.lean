import Mathlib.Tactic
import Mathlib.FieldTheory.Finite.Basic
import Mathlib.Data.Nat.Digits.Lemmas

/-!
# An all-width obstruction to strict local-profile Collatz ranks

The profile below is the multiset of binary windows of length `r + 1`, with
`r` zero bits padded at both ends.  Bits are scanned from least significant
to most significant.  The context is encoded modulo `2^r`; reversing the
windows gives the equivalent most-significant-first convention.

This file constructs arbitrarily large positive odd integers `n > m` with
`3*n + 1 = 4*m` and exactly the same profile.  Consequently no rank depending
only on a fixed finite-window histogram can strictly decrease on every
accelerated odd Collatz step.  This does not exclude variable-length block
ranks or position-sensitive ranks.
-/

namespace LocalProfileObstruction

abbrev Context (r : ℕ) := ZMod (2 ^ r)

def state (r : ℕ) : Context r → List ℕ → Context r
  | q, [] => q
  | q, b :: w => state r (2 * q + b) w

def edges (r : ℕ) : Context r → List ℕ → Multiset (Context r × ℕ)
  | _, [] => 0
  | q, b :: w => {(q, b)} + edges r (2 * q + b) w

theorem state_append (r : ℕ) (q : Context r) (u v : List ℕ) :
    state r q (u ++ v) = state r (state r q u) v := by
  induction u generalizing q with
  | nil => rfl
  | cons b u ih => simpa [state] using ih (2 * q + b)

theorem edges_append (r : ℕ) (q : Context r) (u v : List ℕ) :
    edges r q (u ++ v) = edges r q u + edges r (state r q u) v := by
  induction u generalizing q with
  | nil => simp [state, edges]
  | cons b u ih => simp [state, edges, ih]

theorem state_zeros (r g : ℕ) (q : Context r) :
    state r q (List.replicate g 0) = 2 ^ g * q := by
  induction g generalizing q with
  | zero => simp [state]
  | succ g ih =>
    simp only [List.replicate_succ, state, Nat.cast_zero, add_zero, ih, pow_succ]
    ring

theorem context_power_zero (r : ℕ) : (2 : Context r) ^ r = 0 := by
  have h := ZMod.natCast_self (2 ^ r)
  simpa only [Nat.cast_pow, Nat.cast_ofNat] using h

theorem state_reset (r g : ℕ) (h : r ≤ g) (q : Context r) :
    state r q (List.replicate g 0) = 0 := by
  obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le h
  rw [state_zeros, pow_add, context_power_zero]
  simp

def wordProfile (r : ℕ) (w : List ℕ) : Multiset (Context r × ℕ) :=
  edges r 0 (w ++ List.replicate r 0)

def profile (r n : ℕ) : Multiset (Context r × ℕ) :=
  wordProfile r (Nat.digits 2 n)

theorem padded_swap (r g : ℕ) (h : r ≤ g) (u v : List ℕ) :
    wordProfile r (u ++ List.replicate g 0 ++ v) =
      wordProfile r (v ++ List.replicate g 0 ++ u) := by
  have hs (w : List ℕ) : state r 0 (w ++ List.replicate g 0) = 0 := by
    rw [state_append, state_reset r g h]
  have hfull :
      edges r 0 ((u ++ List.replicate g 0) ++ (v ++ List.replicate g 0)) =
      edges r 0 ((v ++ List.replicate g 0) ++ (u ++ List.replicate g 0)) := by
    rw [edges_append r 0 (u ++ List.replicate g 0) (v ++ List.replicate g 0),
      edges_append r 0 (v ++ List.replicate g 0) (u ++ List.replicate g 0), hs, hs,
      add_comm]
  obtain ⟨t, ht⟩ := Nat.exists_eq_add_of_le h
  have htail (w : List ℕ) :
      edges r 0 (w ++ List.replicate g 0) =
        wordProfile r w + edges r 0 (List.replicate t 0) := by
    rw [ht, List.replicate_add, ← List.append_assoc, edges_append]
    rw [state_append, state_reset r r le_rfl]
    rfl
  have hfull' :
      edges r 0 ((u ++ List.replicate g 0 ++ v) ++ List.replicate g 0) =
      edges r 0 ((v ++ List.replicate g 0 ++ u) ++ List.replicate g 0) := by
    simpa only [List.append_assoc] using hfull
  rw [htail, htail] at hfull'
  exact add_right_cancel hfull'

/- The gap is `r + 2`.  Choosing an arbitrary large totient multiple gives
arbitrary large binary length, while keeping the context width fixed. -/
theorem exists_core (r B : ℕ) :
    ∃ s A : ℕ, B + 3 ≤ s ∧
      (6 * 2 ^ r - 1) * A + 1 = 2 ^ (r + 2 + s) := by
  let D := 6 * 2 ^ r - 1
  have hp : 1 ≤ 2 ^ r := Nat.one_le_pow r 2 (by omega)
  have hD : 1 < D := by dsimp [D]; omega
  have hDa : D + 1 = 6 * 2 ^ r := by dsimp [D]; omega
  have hDo : Odd D := by rw [Nat.odd_iff]; omega
  let K := r + B + 5
  let L := D.totient * K
  have hφ : 1 ≤ D.totient := Nat.totient_pos.mpr (by omega)
  have hL : r + B + 5 ≤ L := by dsimp [L, K]; nlinarith
  have hmod : 2 ^ L % D = 1 := by
    have hh := (Nat.ModEq.pow_totient (Nat.coprime_two_left.mpr hDo)).pow K
    rw [← pow_mul, one_pow] at hh
    change 2 ^ L % D = 1 % D at hh
    simpa only [Nat.mod_eq_of_lt hD] using hh
  refine ⟨L - (r + 2), 2 ^ L / D, by omega, ?_⟩
  have he := Nat.div_add_mod (2 ^ L) D
  rw [hmod] at he
  have hindex : r + 2 + (L - (r + 2)) = L := by omega
  simpa only [hindex] using he

theorem core_bounds {r s A : ℕ} (hs : 3 ≤ s)
    (he : (6 * 2 ^ r - 1) * A + 1 = 2 ^ (r + 2 + s)) :
    2 ^ (s - 1) ≤ A ∧ A < 2 ^ s ∧ Odd A ∧
      (Nat.digits 2 A).length = s ∧ 1 < A := by
  let D := 6 * 2 ^ r - 1
  have hp : 1 ≤ 2 ^ r := Nat.one_le_pow r 2 (by omega)
  have hD : 1 < D := by dsimp [D]; omega
  have hDa : D + 1 = 6 * 2 ^ r := by dsimp [D]; omega
  have hD4 : 4 * 2 ^ r ≤ D := by omega
  have hD8 : D < 8 * 2 ^ r := by omega
  have hpow : 2 ^ (r + 2 + s) = 4 * 2 ^ r * 2 ^ s := by
    rw [pow_add, pow_add]
    norm_num
    ring
  have he' : D * A + 1 = 4 * 2 ^ r * 2 ^ s := by
    simpa only [hpow] using he
  have hupper : A < 2 ^ s := by
    by_contra h
    have hh := Nat.mul_le_mul hD4 (by omega : 2 ^ s ≤ A)
    nlinarith
  have hhalf : 2 ^ s = 2 * 2 ^ (s - 1) := by
    conv_lhs => rw [show s = (s - 1) + 1 by omega]
    rw [pow_succ]
    ring
  have hhalfpos : 0 < 2 ^ (s - 1) := by positivity
  have hlower : 2 ^ (s - 1) ≤ A := by
    by_contra h
    have hA : A + 1 ≤ 2 ^ (s - 1) := by omega
    have hmul := Nat.mul_le_mul_left D hA
    have hmul' := Nat.mul_lt_mul_of_pos_right hD8 hhalfpos
    rw [hhalf] at he'
    nlinarith
  have hodd : Odd A := by
    have hDmod : D % 2 = 1 := by omega
    have hm : (D * A + 1) % 2 = 0 := by
      rw [he', mul_assoc]
      omega
    rw [Nat.add_mod, Nat.mul_mod, hDmod] at hm
    norm_num at hm
    rw [Nat.odd_iff]
    omega
  have hlen : (Nat.digits 2 A).length = s := by
    have hu := (Nat.digits_length_le_iff (by decide : 1 < 2) A).mpr hupper
    have hl := (Nat.lt_digits_length_iff (by decide : 1 < 2) A).mpr hlower
    omega
  have hbig : 1 < A := by
    have hh : 2 ^ 2 ≤ 2 ^ (s - 1) := Nat.pow_le_pow_right (by decide) (by omega)
    norm_num at hh
    omega
  exact ⟨hlower, hupper, hodd, hlen, hbig⟩

theorem family_pair {r s A : ℕ} (hs : 3 ≤ s)
    (he : (6 * 2 ^ r - 1) * A + 1 = 2 ^ (r + 2 + s)) :
    let n := A * 2 ^ (r + 3) + 1
    let m := 2 ^ (r + 2 + s) + A
    1 < m ∧ m < n ∧ Odd n ∧ Odd m ∧ 3 * n + 1 = 4 * m ∧
      profile r n = profile r m := by
  let n := A * 2 ^ (r + 3) + 1
  let m := 2 ^ (r + 2 + s) + A
  obtain ⟨_, _, hodd, hlen, hbig⟩ := core_bounds hs he
  have hp : 1 ≤ 2 ^ r := Nat.one_le_pow r 2 (by omega)
  have hDa : (6 * 2 ^ r - 1) + 1 = 6 * 2 ^ r := by omega
  have hn : n = 8 * 2 ^ r * A + 1 := by
    dsimp [n]
    rw [pow_add]
    norm_num
    ring
  have hm : m = 6 * 2 ^ r * A + 1 := by
    dsimp [m]
    rw [← he]
    have hh := congrArg (fun z : ℕ => z * A) hDa
    nlinarith
  have hmpos : 1 < m := by rw [hm]; nlinarith
  have hmn : m < n := by rw [hn, hm]; nlinarith
  have hno : Odd n := by
    rw [hn, Nat.odd_iff, mul_assoc]
    omega
  have hmo : Odd m := by
    rw [hm, Nat.odd_iff, mul_assoc]
    omega
  have heq : 3 * n + 1 = 4 * m := by rw [hn, hm]; ring
  have hone : Nat.digits 2 1 = [1] := by decide
  have hnd : Nat.digits 2 n = [1] ++ List.replicate (r + 2) 0 ++ Nat.digits 2 A := by
    have hh := Nat.digits_append_zeroes_append_digits
      (b := 2) (k := r + 2) (n := 1) (m := A) (by decide) (by omega)
    rw [hone, List.length_singleton] at hh
    have hv : 1 + 2 ^ (1 + (r + 2)) * A = n := by
      dsimp [n]
      rw [show 1 + (r + 2) = r + 3 by omega]
      ring
    rw [hv] at hh
    exact hh.symm
  have hmd : Nat.digits 2 m = Nat.digits 2 A ++ List.replicate (r + 2) 0 ++ [1] := by
    have hh := Nat.digits_append_zeroes_append_digits
      (b := 2) (k := r + 2) (n := A) (m := 1) (by decide) (by decide)
    rw [hone, hlen, mul_one] at hh
    have hv : A + 2 ^ (s + (r + 2)) = m := by
      dsimp [m]
      rw [show s + (r + 2) = r + 2 + s by omega]
      omega
    rw [hv] at hh
    exact hh.symm
  refine ⟨hmpos, hmn, hno, hmo, heq, ?_⟩
  unfold profile
  rw [hnd, hmd]
  exact padded_swap r (r + 2) (by omega) [1] (Nat.digits 2 A)

theorem exists_arbitrarily_large_profile_collision (r B : ℕ) :
    ∃ n m : ℕ, B < n ∧ 1 < m ∧ m < n ∧ Odd n ∧ Odd m ∧
      3 * n + 1 = 4 * m ∧ profile r n = profile r m := by
  obtain ⟨s, A, hs, he⟩ := exists_core r B
  have hs' : 3 ≤ s := by omega
  obtain ⟨hlower, _, _, _, _⟩ := core_bounds hs' he
  have hBA : B < A := by
    have hh := Nat.lt_pow_self (n := s - 1) (by decide : 1 < 2)
    omega
  obtain ⟨hmpos, hmn, hno, hmo, heq, hprofile⟩ := family_pair hs' he
  refine ⟨A * 2 ^ (r + 3) + 1, 2 ^ (r + 2 + s) + A, ?_,
    hmpos, hmn, hno, hmo, heq, hprofile⟩
  omega

def step (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

theorem two_shortcut_steps {n m : ℕ} (hn : Odd n) (he : 3 * n + 1 = 4 * m) :
    step (step n) = m := by
  have hnmod := Nat.odd_iff.mp hn
  have hfirst : step n = 2 * m := by
    unfold step
    rw [ite_eq_right (by omega), he]
    omega
  rw [hfirst]
  unfold step
  rw [ite_eq_left (by omega : (2 * m) % 2 = 0)]
  omega

/-- This relation includes precisely positive odd-to-odd steps of `3*n+1`
with all factors of two removed.  `Odd m` ensures that the exponent is exact. -/
def OddStep (n m : ℕ) : Prop :=
  Odd n ∧ Odd m ∧ ∃ a : ℕ, 0 < a ∧ 3 * n + 1 = 2 ^ a * m

theorem no_strict_profile_rank (r B : ℕ) {α : Type*} [Preorder α]
    (rank : Multiset (Context r × ℕ) → α) :
    ¬ ∀ n m : ℕ, B < n → 1 < n → OddStep n m →
      rank (profile r m) < rank (profile r n) := by
  intro h
  obtain ⟨n, m, hBn, hm, hmn, hno, hmo, he, hp⟩ :=
    exists_arbitrarily_large_profile_collision r B
  have hstep : OddStep n m := ⟨hno, hmo, 2, by decide, by simpa using he⟩
  have hh := h n m hBn (by omega) hstep
  rw [hp] at hh
  exact lt_irrefl _ hh

#print axioms exists_arbitrarily_large_profile_collision
#print axioms no_strict_profile_rank

end LocalProfileObstruction
