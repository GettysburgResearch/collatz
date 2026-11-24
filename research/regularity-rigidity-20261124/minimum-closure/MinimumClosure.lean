import Mathlib

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
      linear_combination -x * hg
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
    have hpow : (1:ℚ) ≤ (2:ℚ)^k := one_le_pow₀ (by norm_num) _
    nlinarith
  have hc' : (1:ℚ) ≤ (c:ℚ) := by exact_mod_cast hc
  have hx0 : 0 ≤ x := le_trans hs hx
  rw [hz]
  nlinarith [mul_nonneg (sub_nonneg.mpr hp) hx0]

/-- A smaller multiple in the *same* bad component contradicts minimality. -/
theorem smaller_multiple_contradiction (n x y i j : ℕ)
    (hmin : ∀ m, 0 < m → m < n → 3 ∣ m → Good m)
    (hbad : ¬ Good y)
    (hx : 0 < x) (hlt : x < n) (hthree : 3 ∣ x)
    (hxy : (T^[i]) x = (T^[j]) y) :
    False := by
  have hg := hmin x hx hlt hthree
  obtain ⟨k, hk⟩ := hg
  -- Any common future of two ordinary starts preserves convergence.
  -- A terminating start continues on 1,2. The exact two-cycle lemma is
  -- supplied separately below, so this proof is not used by the final
  -- consumer, which only needs a path to a known bad state.
  have hcycle : (T^[2]) 1 = 1 := by decide
  have hstep : Good ((T^[i]) x) := by
    by_cases hle : i ≤ k
    · obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hle
      refine ⟨d, ?_⟩
      rw [add_comm, Function.iterate_add_apply] at hk
      exact hk
    · have hki : k ≤ i := by omega
      obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_le hki
      have hpar : ∀ t : ℕ, Good ((T^[t]) 1) := by
        intro t
        induction t with
        | zero => exact ⟨0, rfl⟩
        | succ t ih =>
          obtain ⟨u, hu⟩ := ih
          cases u with
          | zero =>
            have heq : (T^[t]) 1 = 1 := hu
            refine ⟨1, ?_⟩
            rw [Function.iterate_succ_apply', heq]
            exact hcycle
          | succ u =>
            refine ⟨u, ?_⟩
            rw [Function.iterate_succ_apply'] at hu
            rw [Function.iterate_succ_apply']
            exact hu
      rw [add_comm, Function.iterate_add_apply, hk]
      exact hpar d
  exact hbad (good_of_path y ((T^[j]) y) j rfl (hxy ▸ hstep))

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

#print axioms relative_carry
#print axioms negative_crossing
#print axioms relative_floor
#print axioms collatz_of_minimum_and_descent

end MinimumClosure
