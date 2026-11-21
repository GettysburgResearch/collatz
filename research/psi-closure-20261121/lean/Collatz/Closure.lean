/-
The ψ-closure route. Lean core only; builds on the PR #146 reverse criterion
(`Collatz/ReverseBasin146.lean`).

Normalization: `shortcut n = n/2` for even `n`, `(3n+1)/2` for odd `n`;
`Basin n` means some iterate of `shortcut` from `n` equals 1.
`ψ(m) = 2m - 1`, and `shortcut (ψ m) = 3m - 1`.

Nothing here proves the Collatz conjecture. `OpenLemma` is a hypothesis.
-/
import Collatz.ReverseBasin146

open CollatzReverseBasin

namespace CollatzClosure

/-! ## Ordinary moves -/

theorem basin_step (n : Nat) : Basin (shortcut n) ↔ Basin n := by
  constructor
  · rintro ⟨k, h⟩
    exact ⟨k+1, h⟩
  · rintro ⟨k, h⟩
    cases k with
    | zero => change n = 1 at h; subst n; exact ⟨1, rfl⟩
    | succ k => exact ⟨k, h⟩

theorem basin_twice (n : Nat) : Basin (2*n) ↔ Basin n := by
  have e : shortcut (2*n) = n := by simp [shortcut]
  simpa only [e] using (basin_step (2*n)).symm

theorem basin_odd (n : Nat) (hn : n % 2 = 1) : Basin (3*n+1) ↔ Basin n := by
  have e : 3*n+1 = 2 * shortcut n := by unfold shortcut; split <;> omega
  rw [e]
  exact (basin_twice _).trans (basin_step n)

/-- `4t+1` and `3t+1` are two ordinary steps apart. -/
theorem basin_exch (a b t : Nat) (ha : a = 4*t+1) (hb : b = 3*t+1) : Basin a ↔ Basin b := by
  subst ha; subst hb
  have h1 := basin_odd (4*t+1) (by omega)
  have e : 3*(4*t+1)+1 = 2*(2*(3*t+1)) := by omega
  rw [e] at h1
  exact h1.symm.trans ((basin_twice _).trans (basin_twice _))

/-- `ψ(m) = 2m-1` is one ordinary step above `3m-1`. -/
theorem basin_psi (m : Nat) (hm : 0 < m) : Basin (2*m-1) ↔ Basin (3*m-1) := by
  have h1 := basin_odd (2*m-1) (by omega)
  have e : 3*(2*m-1)+1 = 2*(3*m-1) := by omega
  rw [e] at h1
  exact h1.symm.trans (basin_twice _)

/-! ## The frame: Collatz is closure of the basin under ψ -/

/-- Unrestricted forward form. Elementary: every `n > 1` is `2m` or `2m-1` with `m < n`. -/
theorem collatz_iff_psi_forward :
    (∀ n : Nat, 0 < n → Basin n) ↔ (∀ m : Nat, 0 < m → Basin m → Basin (2*m-1)) := by
  constructor
  · intro all m hm _
    exact all _ (by omega)
  · intro H n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro hn
      by_cases h1 : n = 1
      · subst h1; exact ⟨0, rfl⟩
      by_cases he : n % 2 = 0
      · have small : Basin (n/2) := ih (n/2) (by omega) (by omega)
        have e : n = 2*(n/2) := by omega
        rw [e]
        exact (basin_twice _).mpr small
      · have small : Basin ((n+1)/2) := ih ((n+1)/2) (by omega) (by omega)
        have big := H ((n+1)/2) (by omega) small
        have e : 2*((n+1)/2) - 1 = n := by omega
        rwa [e] at big

/-- Sharp reverse form: it suffices that `ψ(m) ∈ Basin → m ∈ Basin` on `m = 27k+1`, `4 ∤ k`.
This is PR #146's `collatz_iff_deep_reverse_binary` moved to ψ-coordinates. -/
theorem collatz_iff_psi_reverse :
    (∀ n : Nat, 0 < n → Basin n) ↔
      (∀ k : Nat, k % 4 ≠ 0 → Basin (2*(27*k+1)-1) → Basin (27*k+1)) := by
  rw [collatz_iff_deep_reverse_binary]
  have up (k : Nat) : Basin (128*k+1) ↔ Basin (2*(27*k+1)-1) :=
    ((basin_exch (128*k+1) (96*k+1) (32*k) (by omega) (by omega)).trans
      (basin_exch (96*k+1) (72*k+1) (24*k) (by omega) (by omega))).trans
      (basin_exch (72*k+1) (2*(27*k+1)-1) (18*k) (by omega) (by omega))
  have lo (k : Nat) : Basin (64*k+1) ↔ Basin (27*k+1) :=
    ((basin_exch (64*k+1) (48*k+1) (16*k) (by omega) (by omega)).trans
      (basin_exch (48*k+1) (36*k+1) (12*k) (by omega) (by omega))).trans
      (basin_exch (36*k+1) (27*k+1) (9*k) (by omega) (by omega))
  exact ⟨fun h k hk hy => (lo k).mp (h k hk ((up k).mpr hy)),
         fun h k hk hy => (lo k).mpr (h k hk ((up k).mp hy))⟩

/-- The single open statement of this route. -/
def OpenLemma : Prop :=
  ∀ k : Nat, k % 4 ≠ 0 → Basin (3*(27*k+1)-1) → Basin (27*k+1)

theorem collatz_iff_open_lemma : (∀ n : Nat, 0 < n → Basin n) ↔ OpenLemma := by
  unfold OpenLemma
  rw [collatz_iff_psi_reverse]
  have key (k : Nat) := basin_psi (27*k+1) (by omega)
  exact ⟨fun h k hk hy => h k hk ((key k).mpr hy), fun h k hk hy => h k hk ((key k).mp hy)⟩

/-- The whole conjecture from the one open lemma. -/
theorem collatz_of_open_lemma (H : OpenLemma) : ∀ n : Nat, 0 < n → Basin n :=
  collatz_iff_open_lemma.mpr H

/-! ## Exponent-parametrized families (schema induction, no bounded certificate) -/

/-- `2^k q - 1` and `3^k q - 1` are in the same component, for every `k`. -/
theorem basin_pow_two_pred (k : Nat) :
    ∀ q : Nat, 0 < q → (Basin (2^k*q - 1) ↔ Basin (3^k*q - 1)) := by
  induction k with
  | zero => intro q _; simp
  | succ k ih =>
    intro q hq
    have hpos : 0 < 2^k*q := Nat.mul_pos (Nat.pow_pos (by omega)) hq
    have h1 := basin_psi (2^k*q) hpos
    have e1 : 2^(k+1)*q = 2*(2^k*q) := by grind
    have e2 : 3*(2^k*q) = 2^k*(3*q) := by grind
    have e3 : 3^(k+1)*q = 3^k*(3*q) := by grind
    rw [e1, e3]
    rw [e2] at h1
    exact h1.trans (ih (3*q) (by omega))

/-- `4^i v + 1` and `3^i v + 1` are in the same component, for every `i`. -/
theorem basin_pow_four_succ (i : Nat) :
    ∀ v : Nat, (Basin (4^i*v + 1) ↔ Basin (3^i*v + 1)) := by
  induction i with
  | zero => intro v; simp
  | succ i ih =>
    intro v
    have e1 : 4^(i+1)*v = 4*(4^i*v) := by grind
    have e2 : 3*(4^i*v) = 4^i*(3*v) := by grind
    have e3 : 3^(i+1)*v = 3^i*(3*v) := by grind
    have h1 := basin_exch (4*(4^i*v)+1) (3*(4^i*v)+1) (4^i*v) rfl rfl
    rw [e1, e3]
    rw [e2] at h1
    exact h1.trans (ih (3*v))

theorem three_pow_odd (i : Nat) : 3^i % 2 = 1 := by
  induction i with
  | zero => rfl
  | succ i ih => rw [Nat.pow_succ]; omega

theorem four_pow_mod_three (j : Nat) : 4^j % 3 = 1 := by
  induction j with
  | zero => rfl
  | succ j ih => rw [Nat.pow_succ]; omega

theorem basin_four_pow (j : Nat) : Basin (4^j) := by
  induction j with
  | zero => exact ⟨0, rfl⟩
  | succ j ih =>
    have e : 4^(j+1) = 2*(2*4^j) := by grind
    rw [e]
    exact (basin_twice _).mpr ((basin_twice _).mpr ih)

/-- `4^(i+1) + 1` converges exactly when `3^i` does. -/
theorem basin_four_pow_succ_iff_three_pow (i : Nat) : Basin (4^(i+1) + 1) ↔ Basin (3^i) := by
  have h1 := basin_pow_four_succ (i+1) 1
  have h2 := basin_odd (3^i) (three_pow_odd i)
  have e1 : 4^(i+1)*1 + 1 = 4^(i+1) + 1 := by omega
  have e2 : 3^(i+1)*1 + 1 = 3*3^i + 1 := by grind
  rw [e1, e2] at h1
  exact h1.trans h2

/-- The Jacobsthal number `(2·4^(i+1)+1)/3` converges exactly when `3^i` does. -/
theorem basin_jacobsthal (i m : Nat) (h : 3*m = 2*4^(i+1) + 1) : Basin m ↔ Basin (3^i) := by
  have hs : shortcut m = 4^(i+1) + 1 := by
    unfold shortcut
    generalize 4^(i+1) = X at h ⊢
    split <;> omega
  have h1 := basin_step m
  rw [hs] at h1
  exact h1.symm.trans (basin_four_pow_succ_iff_three_pow i)

/-- The weakest layer of the closure statement — the member arm `3m-1` is a power of two —
is exactly convergence of every power of three. -/
theorem first_layer_iff_pow_three :
    (∀ i m : Nat, 3*m = 2*4^(i+1) + 1 → Basin (3*m-1) → Basin m) ↔ (∀ i : Nat, Basin (3^i)) := by
  constructor
  · intro H i
    have hmod := four_pow_mod_three (i+1)
    have hm : 3*((2*4^(i+1)+1)/3) = 2*4^(i+1) + 1 := by
      generalize 4^(i+1) = X at hmod ⊢
      omega
    have arm : Basin (3*((2*4^(i+1)+1)/3) - 1) := by
      have e : 3*((2*4^(i+1)+1)/3) - 1 = 2*4^(i+1) := by omega
      rw [e]
      exact (basin_twice _).mpr (basin_four_pow (i+1))
    exact (basin_jacobsthal i _ hm).mp (H i _ hm arm)
  · intro P i m hm _
    exact (basin_jacobsthal i m hm).mpr (P i)

/-! ## Relation calculus: transport of a closure failure

`Fail a b x` says: `x` is outside the basin while `a·x - b` is inside. The open lemma is
`∀ k, 4 ∤ k → ¬ Fail 3 1 (27k+1)`. The four lemmas below move a `Fail 3 1` at `m` to the
next relation, by ordinary steps on both arms, according to `m mod 4`. -/

def Fail (a b x : Nat) : Prop := ¬ Basin x ∧ Basin (a*x - b)

theorem open_lemma_iff_no_fail : OpenLemma ↔ ∀ k : Nat, k % 4 ≠ 0 → ¬ Fail 3 1 (27*k+1) := by
  unfold OpenLemma Fail
  constructor
  · intro H k hk hf
    exact hf.1 (H k hk hf.2)
  · intro H k hk hy
    exact Classical.byContradiction (fun hn => H k hk ⟨hn, hy⟩)

/-- `m = 4t+1`: the pair moves to the smaller point `3t+1` with the same relation. -/
theorem fail_mod4_one (t : Nat) : Fail 3 1 (4*t+1) ↔ Fail 3 1 (3*t+1) := by
  have a := basin_exch (4*t+1) (3*t+1) t rfl rfl
  have b : Basin (3*(4*t+1)-1) ↔ Basin (3*(3*t+1)-1) := by
    have h1 := basin_twice (6*t+1)
    have h2 := basin_odd (6*t+1) (by omega)
    have h3 := basin_twice (9*t+2)
    have e1 : 3*(4*t+1)-1 = 2*(6*t+1) := by omega
    have e2 : 3*(6*t+1)+1 = 2*(9*t+2) := by omega
    have e3 : 3*(3*t+1)-1 = 9*t+2 := by omega
    rw [e1, e3]
    rw [e2] at h2
    exact h1.trans (h2.symm.trans h3)
  unfold Fail
  rw [a, b]

/-- `m = 4t+2`: the pair moves to the smaller point `3t+2`, relation `3x-2`. -/
theorem fail_mod4_two (t : Nat) : Fail 3 1 (4*t+2) ↔ Fail 3 2 (3*t+2) := by
  have a : Basin (4*t+2) ↔ Basin (3*t+2) := by
    have h1 := basin_twice (2*t+1)
    have h2 := basin_odd (2*t+1) (by omega)
    have h3 := basin_twice (3*t+2)
    have e1 : 4*t+2 = 2*(2*t+1) := by omega
    have e2 : 3*(2*t+1)+1 = 2*(3*t+2) := by omega
    rw [e1]
    rw [e2] at h2
    exact h1.trans (h2.symm.trans h3)
  have b : Basin (3*(4*t+2)-1) ↔ Basin (3*(3*t+2)-2) := by
    have h2 := basin_odd (12*t+5) (by omega)
    have h3 := basin_twice (2*(9*t+4))
    have h4 := basin_twice (9*t+4)
    have e1 : 3*(4*t+2)-1 = 12*t+5 := by omega
    have e2 : 3*(12*t+5)+1 = 2*(2*(9*t+4)) := by omega
    have e3 : 3*(3*t+2)-2 = 9*t+4 := by omega
    rw [e1, e3]
    rw [e2] at h2
    exact h2.symm.trans (h3.trans h4)
  unfold Fail
  rw [a, b]

/-- `m = 4t+3`: the pair moves to the larger point `6t+5`, relation `x-1` (adjacent pair). -/
theorem fail_mod4_three (t : Nat) : Fail 3 1 (4*t+3) ↔ Fail 1 1 (6*t+5) := by
  have a : Basin (4*t+3) ↔ Basin (6*t+5) := by
    have h2 := basin_odd (4*t+3) (by omega)
    have h3 := basin_twice (6*t+5)
    have e2 : 3*(4*t+3)+1 = 2*(6*t+5) := by omega
    rw [e2] at h2
    exact h2.symm.trans h3
  have b : Basin (3*(4*t+3)-1) ↔ Basin (1*(6*t+5)-1) := by
    have h1 := basin_twice (6*t+4)
    have e1 : 3*(4*t+3)-1 = 2*(6*t+4) := by omega
    have e3 : 1*(6*t+5)-1 = 6*t+4 := by omega
    rw [e1, e3]
    exact h1
  unfold Fail
  rw [a, b]

/-- `m = 4t`: the pair moves to the smaller point `t`, relation `27x-1`. -/
theorem fail_mod4_zero (t : Nat) (ht : 0 < t) : Fail 3 1 (4*t) ↔ Fail 27 1 t := by
  have a : Basin (4*t) ↔ Basin t := by
    have h1 := basin_twice (2*t)
    have h2 := basin_twice t
    have e1 : 4*t = 2*(2*t) := by omega
    rw [e1]
    exact h1.trans h2
  have b : Basin (3*(4*t)-1) ↔ Basin (27*t-1) := by
    have h1 := basin_odd (12*t-1) (by omega)
    have h2 := basin_twice (18*t-1)
    have h3 := basin_odd (18*t-1) (by omega)
    have h4 := basin_twice (27*t-1)
    have e0 : 3*(4*t)-1 = 12*t-1 := by omega
    have e1 : 3*(12*t-1)+1 = 2*(18*t-1) := by omega
    have e2 : 3*(18*t-1)+1 = 2*(27*t-1) := by omega
    rw [e0]
    rw [e1] at h1
    rw [e2] at h3
    exact h1.symm.trans (h2.trans (h3.symm.trans h4))
  unfold Fail
  rw [a, b]

end CollatzClosure
