/-
No finite purely ordinary descent cover of the Collatz map exists.

Lean 4 core only: no Mathlib, no imports, no `sorry`.

Map: `T n = n/2` (n even), `(3n+1)/2` (n odd).  An ORDINARY WALK from `n` is a finite sequence
of moves, each either a forward step `w ↦ T w` or a backward step to some `w` with `T w` equal
to the current value (that is `w = 2v`, or `w = (2v-1)/3` when `v ≡ 2 mod 3`).

Main results
* `no_descent`: if `2^K ∣ n+1`, `3^J ∣ n`, `T^q w = T^p n`, `p ≤ K`, and the first `q` steps of
  `w` contain at most `p + J` odd steps, then `n ≤ w`.
* `no_short_walk_descent`: if `2^L ∣ n+1` and `3^L ∣ n`, every ordinary walk of length `L` from
  `n` ends at some `w ≥ n`.
* `unbounded_ordinary_descent_radius`: for all `L`, `N` there is `n > N` such that no ordinary
  walk of length `≤ L` from `n` ends below `n`.  Hence no finite family of ordinary descent
  certificates (each a walk of bounded length) can cover all large integers.

This is a statement about the 2-adic × 3-adic point (-1, 0); it says nothing about whether the
Collatz conjecture is true.
-/
namespace CoverObstruction

/-- Shortcut Collatz map. -/
def T (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

/-- `iter k n = T^k n`. -/
def iter : Nat → Nat → Nat
  | 0, n => n
  | k + 1, n => iter k (T n)

/-- Number of odd terms among `n, T n, …, T^(k-1) n`. -/
def odds : Nat → Nat → Nat
  | 0, _ => 0
  | k + 1, n => n % 2 + odds k (T n)

/-! ### Elementary facts about powers -/

theorem pow2_pos : ∀ k : Nat, 0 < 2 ^ k
  | 0 => by decide
  | k + 1 => by have := pow2_pos k; rw [Nat.pow_succ]; omega

theorem pow3_pos : ∀ k : Nat, 0 < 3 ^ k
  | 0 => by decide
  | k + 1 => by have := pow3_pos k; rw [Nat.pow_succ]; omega

theorem pow2_le_pow3 : ∀ k : Nat, 2 ^ k ≤ 3 ^ k
  | 0 => by decide
  | k + 1 => by have := pow2_le_pow3 k; rw [Nat.pow_succ, Nat.pow_succ]; omega

theorem three_pow_odd : ∀ k : Nat, 3 ^ k % 2 = 1
  | 0 => by decide
  | k + 1 => by have := three_pow_odd k; rw [Nat.pow_succ]; omega

theorem three_dvd_cancel (a X : Nat) (h : 3 ∣ 2 ^ a * X) : 3 ∣ X := by
  induction a with
  | zero => simpa using h
  | succ a ih =>
    apply ih
    have e : 2 ^ (a + 1) * X = 2 * (2 ^ a * X) := by
      rw [Nat.pow_succ, Nat.mul_comm (2 ^ a) 2, Nat.mul_assoc]
    rw [e] at h
    omega

/-! ### Forward part: `n ≡ -1 (mod 2^K)` climbs for `K` steps -/

theorem T_of_dvd {K n : Nat} (h : 2 ^ (K + 1) ∣ n + 1) :
    2 * (T n + 1) = 3 * (n + 1) ∧ 2 ^ K ∣ T n + 1 := by
  obtain ⟨m, hm⟩ := h
  have hm' : n + 1 = 2 * (2 ^ K * m) := by
    rw [hm, Nat.pow_succ, Nat.mul_comm (2 ^ K) 2, Nat.mul_assoc]
  have hne : ¬ (n % 2 = 0) := by omega
  have hT : T n = (3 * n + 1) / 2 := by unfold T; split <;> omega
  have hT1 : T n + 1 = 3 * (2 ^ K * m) := by omega
  refine ⟨by omega, ⟨3 * m, ?_⟩⟩
  rw [hT1]
  exact Nat.mul_left_comm _ _ _

theorem forward : ∀ (p K n : Nat), p ≤ K → 2 ^ K ∣ n + 1 →
    2 ^ p * (iter p n + 1) = 3 ^ p * (n + 1)
  | 0, _, n, _, _ => by simp [iter]
  | p + 1, 0, _, h, _ => by omega
  | p + 1, K + 1, n, h, hd => by
    obtain ⟨h1, h2⟩ := T_of_dvd hd
    have ih := forward p K (T n) (by omega) h2
    show 2 ^ (p + 1) * (iter p (T n) + 1) = 3 ^ (p + 1) * (n + 1)
    have e1 : 2 ^ (p + 1) * (iter p (T n) + 1) = 2 * (2 ^ p * (iter p (T n) + 1)) := by
      rw [Nat.pow_succ, Nat.mul_comm (2 ^ p) 2, Nat.mul_assoc]
    have e2 : 3 ^ (p + 1) * (n + 1) = 3 ^ p * (3 * (n + 1)) := by
      rw [Nat.pow_succ, Nat.mul_assoc]
    have e3 : 3 ^ p * (2 * (T n + 1)) = 2 * (3 ^ p * (T n + 1)) := Nat.mul_left_comm _ _ _
    rw [e1, e2, ← h1, e3, ih]

/-! ### The invariant

`Inv n p w q o` describes a node `w` with `T^q w = T^p n` whose first `q` steps contain `o`
odd steps.  Writing the path as `w = α·(n+1) − X = α·n + y` with multiplier
`α = 2^(q-p)·3^(p-o)`:

* first disjunct (`o ≤ p`): `X = B` is an integer with `1 ≤ B ≤ 2^j`, `j = q − o`;
* second disjunct (`o ≥ p`): `y` is a natural number and `y + 1 ≤ α`.

In both cases `X ≥ 1` and `y ≥ 0`, so `α = X + y ≥ 1` and `w = α n + y ≥ n`. -/
def Inv (n p w q o : Nat) : Prop :=
  (∃ a j B, o + a = p ∧ o + j = q ∧ 1 ≤ B ∧ B ≤ 2 ^ j ∧
      2 ^ a * (w + B) = 2 ^ j * 3 ^ a * (n + 1)) ∨
  (∃ e d y, o = p + e ∧ q = p + d ∧
      3 ^ e * w = 2 ^ d * n + 3 ^ e * y ∧ 3 ^ e * (y + 1) ≤ 2 ^ d)

theorem inv_le {n p w q o : Nat} (h : Inv n p w q o) : n ≤ w := by
  unfold Inv at h
  rcases h with ⟨a, j, B, _, _, hB1, hB2, hE⟩ | ⟨e, d, y, _, _, hE, hb⟩
  · have h32 := pow2_le_pow3 a
    have s1 : 2 ^ a * (2 ^ j * (n + 1)) ≤ 3 ^ a * (2 ^ j * (n + 1)) :=
      Nat.mul_le_mul_right _ h32
    have s2 : 3 ^ a * (2 ^ j * (n + 1)) = 2 ^ j * 3 ^ a * (n + 1) := by
      rw [← Nat.mul_assoc, Nat.mul_comm (3 ^ a) (2 ^ j)]
    have h1 : 2 ^ a * (2 ^ j * (n + 1)) ≤ 2 ^ a * (w + B) := by omega
    have h2 : 2 ^ j * (n + 1) ≤ w + B := Nat.le_of_mul_le_mul_left h1 (pow2_pos a)
    have h3 : B * (n + 1) ≤ 2 ^ j * (n + 1) := Nat.mul_le_mul_right _ hB2
    have h4 : B * (n + 1) = B * n + B := Nat.mul_succ B n
    have h5 : 1 * n ≤ B * n := Nat.mul_le_mul_right _ hB1
    omega
  · have h3e := pow3_pos e
    have h1 : 3 ^ e * 1 ≤ 3 ^ e * (y + 1) := Nat.mul_le_mul_left _ (by omega)
    have h2 : 3 ^ e ≤ 2 ^ d := by omega
    have h3 : 3 ^ e * n ≤ 2 ^ d * n := Nat.mul_le_mul_right _ h2
    have h4 : 3 ^ e * n ≤ 3 ^ e * w := by omega
    exact Nat.le_of_mul_le_mul_left h4 h3e

/-- Backward doubling `w1 ↦ 2·w1` preserves the invariant. -/
theorem step_even {n p w1 q o : Nat} (h : Inv n p w1 q o) :
    Inv n p (2 * w1) (q + 1) o := by
  unfold Inv at h ⊢
  rcases h with ⟨a, j, B, hoa, hoj, hB1, hB2, hE⟩ | ⟨e, d, y, ho, hq, hE, hb⟩
  · refine Or.inl ⟨a, j + 1, 2 * B, hoa, by omega, by omega, ?_, ?_⟩
    · rw [Nat.pow_succ]; omega
    · have e1 : 2 ^ a * (2 * w1 + 2 * B) = 2 * (2 ^ a * (w1 + B)) := by
        rw [← Nat.mul_add]; exact Nat.mul_left_comm _ _ _
      have e2 : 2 ^ (j + 1) * 3 ^ a * (n + 1) = 2 * (2 ^ j * 3 ^ a * (n + 1)) := by
        rw [Nat.pow_succ]; ac_rfl
      omega
  · refine Or.inr ⟨e, d + 1, 2 * y, ho, by omega, ?_, ?_⟩
    · have e1 : 3 ^ e * (2 * w1) = 2 * (3 ^ e * w1) := Nat.mul_left_comm _ _ _
      have e2 : 2 ^ (d + 1) * n = 2 * (2 ^ d * n) := by
        rw [Nat.pow_succ]; ac_rfl
      have e3 : 3 ^ e * (2 * y) = 2 * (3 ^ e * y) := Nat.mul_left_comm _ _ _
      omega
    · have e1 : 3 ^ e * (2 * y + 1) ≤ 3 ^ e * (2 * (y + 1)) :=
        Nat.mul_le_mul_left _ (by omega)
      have e2 : 3 ^ e * (2 * (y + 1)) = 2 * (3 ^ e * (y + 1)) := Nat.mul_left_comm _ _ _
      rw [Nat.pow_succ]; omega

/-- Backward odd step in the second regime; this is where `3^J ∣ n` is used. -/
theorem odd_step2 {n J w w1 e d y : Nat} (hJ : 3 ^ J ∣ n) (heJ : e + 1 ≤ J)
    (hE : 3 ^ e * w1 = 2 ^ d * n + 3 ^ e * y) (hb : 3 ^ e * (y + 1) ≤ 2 ^ d)
    (hw : 2 * w1 = 3 * w + 1) :
    ∃ y', 3 ^ (e + 1) * w = 2 ^ (d + 1) * n + 3 ^ (e + 1) * y' ∧
      3 ^ (e + 1) * (y' + 1) ≤ 2 ^ (d + 1) := by
  obtain ⟨m, hm⟩ := Nat.dvd_trans (Nat.pow_dvd_pow 3 heJ) hJ
  have h3e := pow3_pos e
  have hn : n = 3 ^ e * (3 * m) := by
    rw [hm, Nat.pow_succ, Nat.mul_assoc]
  have e1 : 2 ^ d * n = 3 ^ e * (3 * (2 ^ d * m)) := by
    rw [hn]; ac_rfl
  have hw1 : w1 = 3 * (2 ^ d * m) + y := by
    apply Nat.eq_of_mul_eq_mul_left h3e
    rw [Nat.mul_add, ← e1]; exact hE
  obtain ⟨y', hy⟩ : ∃ y', y = 3 * y' + 2 := ⟨y / 3, by omega⟩
  have hwv : w = 2 * (2 ^ d * m) + (2 * y' + 1) := by omega
  refine ⟨2 * y' + 1, ?_, ?_⟩
  · have e2 : 2 ^ (d + 1) * n = 3 ^ (e + 1) * (2 * (2 ^ d * m)) := by
      rw [hm, Nat.pow_succ 2 d]; ac_rfl
    rw [e2, ← Nat.mul_add, hwv]
  · have e3 : 3 ^ (e + 1) * (2 * y' + 1 + 1) = 2 * (3 ^ e * (y + 1)) := by
      have e4 : 3 * (2 * y' + 1 + 1) = 2 * (y + 1) := by omega
      rw [Nat.pow_succ, Nat.mul_assoc, e4]; exact Nat.mul_left_comm _ _ _
    rw [e3, Nat.pow_succ]; omega

/-- Backward odd step `w1 ↦ w` with `3w + 1 = 2·w1` preserves the invariant, as long as the
number of odd backward steps stays `≤ p + J`. -/
theorem step_odd {n p J w w1 q o : Nat} (hJ : 3 ^ J ∣ n) (h : Inv n p w1 q o)
    (hw : 2 * w1 = 3 * w + 1) (hoJ : o + 1 ≤ p + J) : Inv n p w (q + 1) (o + 1) := by
  unfold Inv at h ⊢
  rcases h with ⟨a, j, B, hoa, hoj, hB1, hB2, hE⟩ | ⟨e, d, y, ho, hq, hE, hb⟩
  · cases a with
    | zero =>
      -- hand-over from the first regime to the second: y = 2^j − B ≥ 0
      have hE' : w1 + B = 2 ^ j * (n + 1) := by simpa using hE
      have hmul : 2 ^ j * (n + 1) = 2 ^ j * n + 2 ^ j := Nat.mul_succ _ _
      have hEq : 3 ^ 0 * w1 = 2 ^ j * n + 3 ^ 0 * (2 ^ j - B) := by
        rw [Nat.pow_zero, Nat.one_mul, Nat.one_mul]; omega
      have hbd : 3 ^ 0 * (2 ^ j - B + 1) ≤ 2 ^ j := by
        rw [Nat.pow_zero, Nat.one_mul]; omega
      obtain ⟨y', h1, h2⟩ := odd_step2 hJ (by omega) hEq hbd hw
      exact Or.inr ⟨0 + 1, j + 1, y', by omega, by omega, h1, h2⟩
    | succ a' =>
      have hpos := pow2_pos j
      have e1 : 2 ^ (a' + 1) * (w1 + B) = 2 ^ a' * (3 * w + (2 * B + 1)) := by
        have e0 : 3 * w + (2 * B + 1) = 2 * (w1 + B) := by omega
        rw [e0, Nat.pow_succ, Nat.mul_assoc]
      have e2 : 2 ^ j * 3 ^ (a' + 1) * (n + 1) = 3 * (2 ^ j * 3 ^ a' * (n + 1)) := by
        rw [Nat.pow_succ]; ac_rfl
      have key : 2 ^ a' * (3 * w + (2 * B + 1)) = 3 * (2 ^ j * 3 ^ a' * (n + 1)) := by
        rw [← e1, ← e2]; exact hE
      have hd : 3 ∣ 3 * w + (2 * B + 1) := three_dvd_cancel a' _ ⟨_, key⟩
      obtain ⟨B', hB'⟩ : ∃ B', 2 * B + 1 = 3 * B' := ⟨(2 * B + 1) / 3, by omega⟩
      refine Or.inl ⟨a', j, B', by omega, by omega, by omega, by omega, ?_⟩
      have e3 : 2 ^ a' * (3 * w + (2 * B + 1)) = 3 * (2 ^ a' * (w + B')) := by
        rw [hB', ← Nat.mul_add]; exact Nat.mul_left_comm _ _ _
      omega
  · obtain ⟨y', h1, h2⟩ := odd_step2 hJ (by omega) hE hb hw
    exact Or.inr ⟨e + 1, d + 1, y', by omega, by omega, h1, h2⟩

theorem inv_of_meet {K J n p : Nat} (hK : 2 ^ K ∣ n + 1) (hJ : 3 ^ J ∣ n) (hp : p ≤ K) :
    ∀ (q w : Nat), iter q w = iter p n → odds q w ≤ p + J → Inv n p w q (odds q w)
  | 0, w, hm, _ => by
    have hf := forward p K n hp hK
    have hw : w = iter p n := hm
    subst hw
    unfold Inv
    refine Or.inl ⟨p, 0, 1, by simp [odds], by simp [odds], Nat.le_refl 1, by decide, ?_⟩
    rw [Nat.pow_zero, Nat.one_mul]; exact hf
  | q + 1, w, hm, ho => by
    have hm' : iter q (T w) = iter p n := hm
    have ho' : w % 2 + odds q (T w) ≤ p + J := ho
    have ih := inv_of_meet hK hJ hp q (T w) hm' (by omega)
    show Inv n p w (q + 1) (w % 2 + odds q (T w))
    have hpar : w % 2 = 0 ∨ w % 2 = 1 := by omega
    rcases hpar with h0 | h1
    · have hT : T w = w / 2 := by unfold T; split <;> omega
      have hw : 2 * T w = w := by omega
      have h := step_even ih
      rw [hw] at h
      rw [h0, Nat.zero_add]; exact h
    · have hne : ¬ (w % 2 = 0) := by omega
      have hT : T w = (3 * w + 1) / 2 := by unfold T; split <;> omega
      have hw : 2 * T w = 3 * w + 1 := by omega
      have h := step_odd hJ ih hw (by omega)
      rw [h1, Nat.add_comm 1 (odds q (T w))]; exact h

/-! ### Main theorems -/

/-- **Meet form.**  Let `n ≡ -1 (mod 2^K)` and `n ≡ 0 (mod 3^J)`.  If `w` merges with `n`
(`T^q w = T^p n`) after `p ≤ K` forward steps of `n`, and the `q` steps of `w` contain at most
`p + J` odd steps, then `w ≥ n`. -/
theorem no_descent {K J n p q w : Nat} (hK : 2 ^ K ∣ n + 1) (hJ : 3 ^ J ∣ n) (hp : p ≤ K)
    (hm : iter q w = iter p n) (ho : odds q w ≤ p + J) : n ≤ w :=
  inv_le (inv_of_meet hK hJ hp q w hm ho)

theorem odds_le : ∀ (q w : Nat), odds q w ≤ q
  | 0, _ => Nat.le_refl 0
  | q + 1, w => by
    have h1 := odds_le q (T w)
    have h2 : w % 2 < 2 := Nat.mod_lt w (by decide)
    show w % 2 + odds q (T w) ≤ q + 1
    omega

theorem iter_succ' : ∀ (k n : Nat), iter (k + 1) n = T (iter k n)
  | 0, _ => rfl
  | k + 1, n => iter_succ' k (T n)

/-- `Walk n L w`: `w` is reached from `n` by `L` ordinary moves, each a forward `T`-step or a
backward `T`-step (to any `T`-preimage of the current value). -/
inductive Walk (n : Nat) : Nat → Nat → Prop
  | refl : Walk n 0 n
  | fwd {L w : Nat} : Walk n L w → Walk n (L + 1) (T w)
  | bwd {L w : Nat} : Walk n L (T w) → Walk n (L + 1) w

/-- A walk with `p` forward and `q` backward moves ends at `w` with `T^q w = T^p n`. -/
theorem walk_meet {n L w : Nat} (h : Walk n L w) :
    ∃ p q, p + q = L ∧ iter q w = iter p n := by
  induction h with
  | refl => exact ⟨0, 0, rfl, rfl⟩
  | @fwd L w _ ih =>
    obtain ⟨p, q, hL, hm⟩ := ih
    refine ⟨p + 1, q, by omega, ?_⟩
    calc iter q (T w) = iter (q + 1) w := rfl
      _ = T (iter q w) := iter_succ' q w
      _ = T (iter p n) := by rw [hm]
      _ = iter (p + 1) n := (iter_succ' p n).symm
  | @bwd L w _ ih =>
    obtain ⟨p, q, hL, hm⟩ := ih
    exact ⟨p, q + 1, by omega, hm⟩

/-- **Walk form.**  If `n ≡ -1 (mod 2^L)` and `n ≡ 0 (mod 3^L)`, no ordinary walk of length
`L` from `n` ends below `n`. -/
theorem no_short_walk_descent {L n w : Nat} (h2 : 2 ^ L ∣ n + 1) (h3 : 3 ^ L ∣ n)
    (h : Walk n L w) : n ≤ w := by
  obtain ⟨p, q, hL, hm⟩ := walk_meet h
  have hq := odds_le q w
  exact no_descent h2 h3 (by omega) hm (by omega)

theorem no_walk_descent_le {L L' n w : Nat} (hL : L' ≤ L) (h2 : 2 ^ L ∣ n + 1)
    (h3 : 3 ^ L ∣ n) (h : Walk n L' w) : n ≤ w :=
  no_short_walk_descent (Nat.dvd_trans (Nat.pow_dvd_pow 2 hL) h2)
    (Nat.dvd_trans (Nat.pow_dvd_pow 3 hL) h3) h

/-! ### The class is infinite -/

theorem exists_class (c : Nat) (hc : c % 2 = 1) : ∀ K : Nat, ∃ m, 2 ^ K ∣ c * m + 1
  | 0 => ⟨0, by simp⟩
  | K + 1 => by
    obtain ⟨m, a, ha⟩ := exists_class c hc K
    have hpar : a % 2 = 0 ∨ a % 2 = 1 := by omega
    rcases hpar with h0 | h1
    · refine ⟨m, a / 2, ?_⟩
      have e0 : 2 * (a / 2) = a := by omega
      rw [ha, Nat.pow_succ, Nat.mul_assoc, e0]
    · refine ⟨m + 2 ^ K, (a + c) / 2, ?_⟩
      have e0 : 2 * ((a + c) / 2) = a + c := by omega
      rw [Nat.pow_succ, Nat.mul_assoc, e0, Nat.mul_add c m (2 ^ K), Nat.mul_add (2 ^ K) a c,
        ← ha, Nat.mul_comm (2 ^ K) c]
      omega

theorem exists_obstructed (L N : Nat) : ∃ n, N < n ∧ 2 ^ L ∣ n + 1 ∧ 3 ^ L ∣ n := by
  obtain ⟨m, a, ha⟩ := exists_class (3 ^ L) (three_pow_odd L) L
  refine ⟨3 ^ L * (m + 2 ^ L * (N + 1)), ?_, ⟨a + 3 ^ L * (N + 1), ?_⟩, ⟨_, rfl⟩⟩
  · have h1 : 1 * (N + 1) ≤ 2 ^ L * (N + 1) := Nat.mul_le_mul_right _ (pow2_pos L)
    have h2 : 1 * (m + 2 ^ L * (N + 1)) ≤ 3 ^ L * (m + 2 ^ L * (N + 1)) :=
      Nat.mul_le_mul_right _ (pow3_pos L)
    omega
  · rw [Nat.mul_add (3 ^ L) m (2 ^ L * (N + 1)), Nat.mul_add (2 ^ L) a (3 ^ L * (N + 1)),
      ← ha, Nat.mul_left_comm (3 ^ L) (2 ^ L) (N + 1)]
    omega

/-- **No finite ordinary cover.**  For every bound `L` on the walk length and every `N` there
is `n > N` such that every ordinary walk of length `≤ L` from `n` ends at some `w ≥ n`.
Consequently no finite family of ordinary descent certificates covers all large integers. -/
theorem unbounded_ordinary_descent_radius (L N : Nat) :
    ∃ n, N < n ∧ ∀ L' w, L' ≤ L → Walk n L' w → n ≤ w := by
  obtain ⟨n, hN, h2, h3⟩ := exists_obstructed L N
  exact ⟨n, hN, fun _ _ hL h => no_walk_descent_le hL h2 h3 h⟩

end CoverObstruction

#print axioms CoverObstruction.no_descent
#print axioms CoverObstruction.no_short_walk_descent
#print axioms CoverObstruction.unbounded_ordinary_descent_radius
#check @CoverObstruction.no_descent
#check @CoverObstruction.no_short_walk_descent
#check @CoverObstruction.unbounded_ordinary_descent_radius
