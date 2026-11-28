import PadeObserved

/-! Physical window bounds and normalization of an arbitrary initial odd run. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.PadeWindow
open CoreBranching PinClock PinCriterion
open Collatz.PadeArithmetic Collatz.PadeNative Collatz.PadeObserved

theorem normalize_clock (e n : ℕ) :
    clock e n=twos (n+1)+clock e (run (twos (n+1)) n) := by
  have he := first_even n
  have ht := even_twos he
  cases e with
  | zero => simp only [clock,ht,add_zero]
  | succ e =>
    simp only [clock,ht,zero_add,afterEven,run]
    omega

theorem initial_even_height (n : ℕ) :
    run (twos (n+1)) n+1≤(n+1)^2 := by
  let a := twos (n+1)
  have ha : 2^a≤n+1 := by
    apply Nat.le_of_dvd (by omega)
    exact (Nat.prime_two.pow_dvd_iff_le_factorization (by omega)).mpr le_rfl
  have h := first_odd_shift a n rfl
  have h34 : (3:ℕ)^a≤4^a := Nat.pow_le_pow_left (by decide) a
  have h4 : (4:ℕ)^a=2^a*2^a := by
    rw [←mul_pow]
    norm_num
  have hb : 2^a*(run a n+1)≤2^a*(n+1)^2 := by
    calc
      _ = 3^a*(n+1) := h
      _ ≤ 4^a*(n+1) := Nat.mul_le_mul_right _ h34
      _ = 2^a*(2^a*(n+1)) := by rw [h4]; ring
      _ ≤ 2^a*((n+1)*(n+1)) := Nat.mul_le_mul_left _ (Nat.mul_le_mul_right _ ha)
      _ = _ := by ring
  have hp : 0<2^a := by positivity
  change run a n+1≤(n+1)^2
  nlinarith

theorem initial_even_bit_bound (n B : ℕ) (hB : (n:ℤ)+1≤(2:ℤ)^B) :
    ((run (twos (n+1)) n:ℕ):ℤ)+2≤(2:ℤ)^(2*B+1) := by
  have hn : ((run (twos (n+1)) n:ℕ):ℤ)+1≤((n:ℤ)+1)^2 := by
    exact_mod_cast initial_even_height n
  have hb := pow_le_pow_left₀ (by positivity : 0≤(n:ℤ)+1) hB 2
  have hz : (1:ℤ)≤((n:ℤ)+1)^2 := by nlinarith
  calc
    _ ≤ 2*((n:ℤ)+1)^2 := by omega
    _ ≤ 2*((2:ℤ)^B)^2 := mul_le_mul_of_nonneg_left hb (by decide)
    _ = _ := by rw [←pow_mul,pow_succ,Nat.mul_comm 2 B]; ring

theorem schedule_mono (b h : ℕ) {j k : ℕ} (hjk : j≤k) :
    schedule b h j≤schedule b h k := by
  exact Nat.add_le_add (Nat.mul_le_mul_right _ hjk)
    (Nat.mul_le_mul_left h (tri_mono hjk))

/-- The generous coefficient 17 pays for the last incomplete odd run. -/
theorem schedule_cost_bound (b h s K : ℕ) (hh : 0<h) (hs : 0<s) (hK : K+1≤9*s) :
    schedule b h (K+1)≤17*(3*h*s*s+4*b*s) := by
  have hm := schedule_mono b h hK
  have ht := twice_tri (9*s)
  have htri : tri (9*s)≤41*s*s := by nlinarith
  have hmult := Nat.mul_le_mul_left h htri
  have hcurv : s≤h*s*s := by
    have h1 : 1≤h := by omega
    have h2 : 1≤s := by omega
    nlinarith [Nat.mul_le_mul h1 h2]
  unfold schedule at hm ⊢
  nlinarith

theorem interpolation_index (K : ℕ) (hK : 12≤K) :
    let s := (K-2)/5
    2≤s ∧ 5*s+2≤K ∧ K+1≤9*s := by
  dsimp
  omega

/-- Every long observed positive-curvature window is bounded by the source bit budget.
`L` may cut the final odd run at any point before its next prescribed even input. -/
theorem long_window_bound (n a b h K L B : ℕ) (hh : 0<h) (hK : 12≤K)
    (hc : ∀ j≤K,clock j n=a+schedule b h j)
    (hL : L≤a+schedule b h (K+1))
    (hB : (n:ℤ)+1≤(2:ℤ)^B) :
    L≤579*B+289 := by
  have ha : twos (n+1)=a := by
    simpa only [clock,schedule,zero_mul,tri_zero,mul_zero,add_zero] using hc 0 (by omega)
  have haB : a≤B := by
    rw [←ha]
    exact Nat.factorization_le_of_le_pow (by exact_mod_cast hB)
  let u := run (twos (n+1)) n
  let s := (K-2)/5
  have hi := interpolation_index K hK
  change 2≤s ∧ 5*s+2≤K ∧ K+1≤9*s at hi
  have hobs : ∀ j≤5*s+2,clock j u=schedule b h j := by
    intro j hj
    have hn := normalize_clock j n
    have hp := hc j (by omega)
    change clock j n=twos (n+1)+clock j u at hn
    omega
  have hcost := actual_clock_exponent_bound b h s u (2*B+1) hh hobs
    (initial_even_bit_bound n B hB)
  have htime := schedule_cost_bound b h s K hh (by omega) hi.2.2
  omega

theorem long_window_linear_bound (n a b h K L B : ℕ) (hh : 0<h) (hK : 12≤K)
    (hc : ∀ j≤K,clock j n=a+schedule b h j)
    (hL : L≤a+schedule b h (K+1))
    (hB : (n:ℤ)+1≤(2:ℤ)^B) (hBpos : 0<B) :
    L≤868*B := by
  have h := long_window_bound n a b h K L B hh hK hc hL hB
  omega

end Collatz.PadeWindow
