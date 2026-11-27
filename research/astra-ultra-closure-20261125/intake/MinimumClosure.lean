import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Logic.Function.Iterate

/-! Repaired intake of PR200 at 81ea4c1754d73c98d1451447527e6b2ba56977cc.
The original six public statements are preserved. Two helpers replace a
noncompiling forward-convergence argument; all assumptions remain explicit. -/

set_option autoImplicit false

namespace MinimumClosure

def T (n : ℕ) : ℕ :=
  if n % 2 = 0 then n / 2 else (3*n+1)/2

def Good (n : ℕ) : Prop := ∃ k : ℕ, (T^[k]) n = 1

/-- A literal ordinary path transfers the actual basin backwards. -/
theorem good_of_path (x y k : ℕ) (h : (T^[k]) x = y)
    (hy : Good y) : Good x := by
  obtain ⟨j, hj⟩ := hy
  refine ⟨j+k, ?_⟩
  rw [Function.iterate_add_apply, h, hj]

/-- Relative carry recurrence for the two exact inverse arms. -/
theorem relative_carry (x z x' z' c : ℚ) (e f d d' : ℕ)
    (hx : 3*x' = (2:ℚ)^e*x-1)
    (hz : 3*z' = (2:ℚ)^f*z-1)
    (hr : z = (2:ℚ)^d*x+c)
    (hg : (2:ℚ)^d'*(2:ℚ)^e = (2:ℚ)^f*(2:ℚ)^d) :
    3*(z'-(2:ℚ)^d'*x') = (2:ℚ)^d'+(2:ℚ)^f*c-1 := by
  calc
    3*(z'-(2:ℚ)^d'*x') =
        3*z'-(2:ℚ)^d'*(3*x') := by ring
    _ = (2:ℚ)^f*z-1-(2:ℚ)^d'*((2:ℚ)^e*x-1) := by rw [hx, hz]
    _ = (2:ℚ)^f*c-1+(2:ℚ)^d' := by
      rw [hr]
      have hm := congrArg (fun v : ℚ => v*x) hg
      nlinarith only [hm]
    _ = _ := by ring

/-- The only first crossing of a nonnegative relative exponent. -/
theorem negative_crossing (d e f : ℕ) (he : e ≤ 2) (hf : 1 ≤ f)
    (h : (d:ℤ)+(f:ℤ)-(e:ℤ) < 0) :
    d = 0 ∧ e = 2 ∧ f = 1 := by omega

theorem relative_floor (s x z : ℚ) (d c : ℕ)
    (hs : 0 ≤ s) (hx : s ≤ x) (hd : 1 ≤ d) (hc : 1 ≤ c)
    (hz : z = (2:ℚ)^d*x+(c:ℚ)) :
    2*s+1 ≤ z := by
  have hp : (2:ℚ) ≤ (2:ℚ)^d := by
    obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hd
    rw [pow_add]
    have hpow : (1:ℚ) ≤ (2:ℚ)^k := one_le_pow₀ (by norm_num : (1:ℚ) ≤ 2)
    nlinarith
  have hc' : (1:ℚ) ≤ (c:ℚ) := by exact_mod_cast hc
  have hx0 : 0 ≤ x := le_trans hs hx
  rw [hz]
  nlinarith [mul_nonneg (sub_nonneg.mpr hp) hx0]

/-- Convergence is preserved by one actual step, including the 1,2 cycle. -/
theorem good_step (n : ℕ) (hn : Good n) : Good (T n) := by
  obtain ⟨k, hk⟩ := hn
  cases k with
  | zero =>
      have heq : n = 1 := hk
      subst n
      exact ⟨1, by decide⟩
  | succ k =>
      exact ⟨k, by simpa only [Function.iterate_succ_apply] using hk⟩

/-- Convergence is preserved at every finite position of the same orbit. -/
theorem good_iterate (n i : ℕ) (hn : Good n) : Good ((T^[i]) n) := by
  induction i with
  | zero => exact hn
  | succ i ih =>
      rw [Function.iterate_succ_apply']
      exact good_step _ ih

/-- A smaller multiple in the *same* bad component contradicts minimality. -/
theorem smaller_multiple_contradiction (n x y i j : ℕ)
    (hmin : ∀ m, 0 < m → m < n → 3 ∣ m → Good m)
    (hbad : ¬ Good y)
    (hx : 0 < x) (hlt : x < n) (hthree : 3 ∣ x)
    (hxy : (T^[i]) x = (T^[j]) y) :
    False := by
  have hstep := good_iterate x i (hmin x hx hlt hthree)
  rw [hxy] at hstep
  exact hbad (good_of_path y ((T^[j]) y) j rfl hstep)

/-- Full-proof consumer: neither premise is proved in this new module.
    The first premise is PR192's actual minimum theorem, while the second
    is the universal closure obligation. -/
theorem collatz_of_minimum_and_descent
    (minimum : (∃ z : ℕ, 0 < z ∧ ¬ Good z) →
      ∃ n : ℕ, 0 < n ∧ 3 ∣ n ∧ ¬ Good n ∧
        (∀ x : ℕ, 0 < x → x < n → 3 ∣ x → Good x))
    (descent : ∀ n : ℕ, 0 < n → 3 ∣ n → ¬ Good n →
      (∀ x : ℕ, 0 < x → x < n → 3 ∣ x → Good x) →
      ∃ x i j : ℕ, 0 < x ∧ x < n ∧ 3 ∣ x ∧
        (T^[i]) x = (T^[j]) n) :
    ∀ z : ℕ, 0 < z → Good z := by
  intro z hz
  by_contra hn
  obtain ⟨n, hp, ht, hb, hm⟩ := minimum ⟨z, hz, hn⟩
  obtain ⟨x, i, j, hx, hl, h3, heq⟩ := descent n hp ht hb hm
  exact smaller_multiple_contradiction n x n i j hm hb hx hl h3 heq

#print axioms good_of_path
#print axioms relative_carry
#print axioms negative_crossing
#print axioms relative_floor
#print axioms good_step
#print axioms good_iterate
#print axioms smaller_multiple_contradiction
#print axioms collatz_of_minimum_and_descent

end MinimumClosure
