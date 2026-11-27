import Portal

/-! Synchronized root-chart contraction, using the physical shortcut already
defined in the sibling descent lane. -/

namespace Collatz.PairedGain

open Collatz.TernaryPortal

private theorem odd_run (k u : ℕ) (hu : 0 < u) :
    run k (2^k*u-1)=3^k*u-1 ∧ odds k (2^k*u-1)=k := by
  induction k generalizing u with
  | zero => simp [run, odds]
  | succ k ih =>
    have pp := Nat.mul_pos (Nat.two_pow_pos k) hu
    have form : 2^(k+1)*u=2*(2^k*u) := by ring
    have first : step (2^(k+1)*u-1)=2^k*(3*u)-1 := by
      rw [form, show 2^k*(3*u)=3*(2^k*u) by ring]
      unfold step
      split <;> omega
    have odd : (2^(k+1)*u-1)%2=1 := by rw [form]; omega
    obtain ⟨hr, ho⟩ := ih (3*u) (by omega)
    rw [run, odds, first, odd, hr, ho, pow_succ]
    constructor
    · congr 1
      ring
    · omega

/-- All positive lifts of one 15-clock suffix, including both actual arms. -/
theorem good_suffix {v X : ℕ} (link : 32768*X=6561*v+17569) :
    run 15 (9*v-1)=X ∧ odds 15 (9*v-1)=6 ∧
    run 15 (3*v-1)=3*X-1 ∧ odds 15 (3*v-1)=8 := by
  have hres : v%32768=13567 := by omega
  obtain ⟨t, hv, hX⟩ : ∃ t, v=13567+32768*t ∧ X=2717+6561*t :=
    ⟨v/32768, by omega, by omega⟩
  obtain ⟨lo, ol⟩ := prefix_lift 15 122102 (9*t)
  obtain ⟨hi, oh⟩ := prefix_lift 15 40700 (3*t)
  have low : run 15 122102=2717 ∧ odds 15 122102=6 := by decide
  have high : run 15 40700=8150 ∧ odds 15 40700=8 := by decide
  rw [low.1, low.2] at lo
  rw [low.2] at ol
  rw [high.1, high.2] at hi
  rw [high.2] at oh
  norm_num at lo ol hi oh
  have h1 : 9*v-1=122102+32768*(9*t) := by omega
  have h2 : 3*v-1=40700+32768*(3*t) := by omega
  rw [h1,h2]
  omega

/-- Legal ordinary transfer on the entire stated ternary class, at all odd
budgets k+8. No negative or rational point is substituted into the paths. -/
theorem ordinary_transfer {k u X : ℕ} (hu : 0<u)
    (link : 32768*X=3^(k+8)*u+17569) :
    let Y := 2^(k+2)*u-1
    run (k+17) Y=X ∧ odds (k+17) Y=k+8 ∧
    run (k+17) (3*Y-1)=3*X-1 ∧ odds (k+17) (3*Y-1)=k+8 := by
  dsimp only
  have hpow : 3^(k+8)*u=6561*(3^k*u) := by rw [pow_add]; ring
  obtain ⟨sl, sol, sh, soh⟩ := good_suffix (v:=3^k*u) (by simpa only [hpow] using link)
  have low := odd_run (k+2) u hu
  have lh : 3^(k+2)*u=9*(3^k*u) := by rw [pow_add]; ring
  rw [lh] at low
  have hh : 0<2^k*u := Nat.mul_pos (Nat.two_pow_pos k) hu
  have htwo : 2^(k+2)*u=4*(2^k*u) := by rw [pow_add]; ring
  have upper : 3*(2^(k+2)*u-1)-1=2^2*(2^k*(3*u)-1) := by
    rw [htwo,show 2^k*(3*u)=3*(2^k*u) by ring]
    omega
  have evens := halves 2 (2^k*(3*u)-1)
  have high := odd_run k (3*u) (by omega)
  rw [show 3^k*(3*u)=3*(3^k*u) by ring] at high
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [show k+17=k+2+15 by omega,run_add,low.1,sl]
  · rw [show k+17=k+2+15 by omega,odds_add,low.1,low.2,sol]
  · rw [upper,show k+17=2+(k+15) by omega,run_add,evens.1,run_add,high.1,sh]
  · rw [upper,show k+17=2+(k+15) by omega,odds_add,evens.1,evens.2,odds_add,high.1,high.2,soh]
    omega

/-- Every terminal in this positive root-chart cylinder is eight modulo nine. -/
theorem terminal_mod_nine {k u X : ℕ} (link : 32768*X=3^(k+8)*u+17569) :
    X%9=8 := by
  have hdiv : 3^(k+8)*u=9*(3^(k+6)*u) := by
    rw [show k+8=k+6+2 by omega, pow_add]; ring
  rw [hdiv] at link
  omega

private theorem lift_slope {k gain : ℕ} (base : 2^(k+17+gain)<3^(k+8)) :
    ∀ j, 2^(k+j+17+gain)<3^(k+j+8) := by
  intro j
  induction j with
  | zero => simpa using base
  | succ j ih =>
    rw [show k+(j+1)+17+gain=(k+j+17+gain)+1 by omega,
        show k+(j+1)+8=(k+j+8)+1 by omega, pow_succ, pow_succ]
    omega

/-- Uniform strictly positive height gain on every positive ordinary lift
in the high-precision terminal class. -/
theorem forty_bits {k u X : ℕ} (hk : 76 ≤ k) (hu : 0<u)
    (link : 32768*X=3^(k+8)*u+17569) : 2^40*(2^(k+2)*u-1)<X := by
  obtain ⟨j, hj⟩ := Nat.exists_eq_add_of_le hk
  have hs := lift_slope (k:=76) (gain:=40) (by decide) j
  rw [← hj] at hs
  have scaled := Nat.mul_lt_mul_of_pos_right hs hu
  have rearrange : 2^(k+17+40)*u=32768*(2^40*(2^(k+2)*u)) := by
    rw [show k+17+40=k+2+(15+40) by omega, pow_add]; ring
  rw [rearrange] at scaled
  omega

end Collatz.PairedGain

#print axioms Collatz.PairedGain.good_suffix
#print axioms Collatz.PairedGain.ordinary_transfer
#print axioms Collatz.PairedGain.terminal_mod_nine
#print axioms Collatz.PairedGain.forty_bits
