import ActualScalar

namespace Collatz.ActualThreeRun

/-- The ordinary odd endpoints and carry clocks imply a one-step contraction
for the normalized height of a synchronized digit three. -/
private theorem height_step (q r a c d : ℕ)
    (edge : 2^a*r=3*q+1) (clock : a+d=3+3*c) :
    8 * (5 * ((r:ℚ)/2^d) - 1) ≤ 3 * (5 * ((q:ℚ)/2^c) - 1) := by
  have he : (2:ℚ)^a*(r:ℚ)=3*(q:ℚ)+1 := by exact_mod_cast edge
  have hp : (2:ℚ)^a*2^d = 8*(2:ℚ)^c*(2:ℚ)^c*(2:ℚ)^c := by
    rw [← pow_add, clock, pow_add, Nat.mul_comm 3 c, pow_mul]
    ring
  have hge : (1:ℚ) ≤ 2^c := one_le_pow₀ (by norm_num)
  have htwo : (0:ℚ) < 2^d := by positivity
  have heq : 8*(2:ℚ)^c*(2:ℚ)^c*(2:ℚ)^c*((r:ℚ)/2^d)=3*(q:ℚ)+1 := by
    rw [← hp, mul_assoc, mul_div_cancel₀ _ (ne_of_gt htwo), he]
  have hv : 0 ≤ (2:ℚ)^c*((r:ℚ)/2^d) := by positivity
  have hsq : (1:ℚ) ≤ 2^c*2^c := one_le_mul_of_one_le_of_one_le hge hge
  have hb := mul_le_mul_of_nonneg_right hsq hv
  have hs : 8*((r:ℚ)/2^d) * 2^c ≤ 3*(q:ℚ)+1 := by
    linarith only [hb, heq]
  have hn : 8*((r:ℚ)/2^d) ≤ 3*((q:ℚ)/2^c)+1 := by
    have hs' := (le_div_iff₀ (by positivity : (0:ℚ)<2^c)).2 hs
    calc
      _ ≤ (3*(q:ℚ)+1)/2^c := hs'
      _ ≤ _ := by
        rw [add_div,mul_div_assoc]
        have := (div_le_one (by positivity : (0:ℚ)<2^c)).2 hge
        linarith only [this]
  linarith only [hn]

/-- Finite ordinary-source obstruction for an arbitrarily placed run of
synchronized threes. The input floor is needed only at the final endpoint. -/
theorem three_run_bound (q a c : ℕ → ℕ) (L : ℕ)
    (edges : ∀ i < L, 2^(a i)*q (i+1)=3*q i+1)
    (clocks : ∀ i < L, a i+c (i+1)=3+3*c i)
    (floorEnd : 2^(c L) ≤ q L) :
    4*8^L ≤ 3^L*(5*q 0-1) := by
  let H (i : ℕ) : ℚ := 5*((q i:ℚ)/2^(c i))-1
  have iter (i : ℕ) (hi : i ≤ L) :
      (8:ℚ)^i * H i ≤ (3:ℚ)^i * H 0 := by
    induction i with
    | zero => simp
    | succ i ih =>
      have hs := height_step _ _ _ _ _ (edges i (by omega)) (clocks i (by omega))
      change 8*H (i+1) ≤ 3*H i at hs
      have p := mul_le_mul_of_nonneg_left hs (show (0:ℚ) ≤ 8^i by positivity)
      have r := mul_le_mul_of_nonneg_left (ih (by omega)) (show (0:ℚ) ≤ 3 by norm_num)
      rw [pow_succ, pow_succ]
      linarith only [p,r]
  have hEnd : (4:ℚ) ≤ H L := by
    have f : (2:ℚ)^(c L) ≤ q L := by exact_mod_cast floorEnd
    have g := (one_le_div (show (0:ℚ) < 2^(c L) by positivity)).2 f
    dsimp [H]; linarith only [g]
  have hStart : H 0 ≤ 5*(q 0:ℚ)-1 := by
    have g : (q 0:ℚ)/2^(c 0) ≤ q 0 :=
      div_le_self (by positivity) (one_le_pow₀ (by norm_num))
    dsimp [H]; linarith only [g]
  have hl := mul_le_mul_of_nonneg_left hEnd (show (0:ℚ) ≤ 8^L by positivity)
  have hr := mul_le_mul_of_nonneg_left hStart (show (0:ℚ) ≤ 3^L by positivity)
  have final : (4:ℚ)*8^L + 3^L ≤ 3^L*(5*(q 0:ℚ)) := by
    have h := iter L (by omega)
    linarith only [hl, hr, h]
  have hh : 4*8^L+3^L ≤ 3^L*(5*q 0) := by exact_mod_cast final
  rw [Nat.mul_sub, Nat.mul_one]
  omega

#print axioms three_run_bound

open Collatz.CarryTowerRoundTen.ActualScalar

/-- Right-closed centered fractional representative of the actual discounted gap sum. -/
noncomputable def carry (q : ℕ) : ℕ := ⌈scalar q - 1/2⌉₊ - 1

noncomputable def phase (q : ℕ) : ℝ := scalar q - carry q

noncomputable def digit (q : ℕ) : ℝ := 3 * phase q - phase (oddMap q)

theorem carry_lt (q : ℕ) (hq : 0 < q) (ho : Odd q) :
    (carry q : ℝ) < scalar q - 1/2 := by
  have hh := scalar_strict_lower q hq ho
  have hp : 0 < ⌈scalar q - 1/2⌉₊ := Nat.ceil_pos.mpr (by linarith)
  apply Nat.lt_ceil.mp
  unfold carry
  omega

theorem actual_floor (q : ℕ) (hq : 0 < q) (ho : Odd q) : 2^(carry q) ≤ q := by
  by_cases h : carry q = 0
  · simpa [h] using hq
  have hc : (1:ℝ) ≤ carry q := by exact_mod_cast (show 1 ≤ carry q by omega)
  have hu := scalar_upper q hq
  have hl := carry_lt q hq ho
  have hb : (carry q:ℝ) ≤ logTwo q := by linarith
  have htwo := Real.log_pos (by norm_num : (1:ℝ)<2)
  have hlog := (le_div_iff₀ htwo).mp hb
  have hqR : (0:ℝ) < q := by exact_mod_cast hq
  have hp : (2:ℝ)^(carry q) ≤ q := by
    apply (Real.log_le_log_iff (by positivity) hqR).mp
    rwa [Real.log_pow]
  exact_mod_cast hp

theorem actual_clock (q : ℕ) (hq : 0 < q) (b : ℕ) (hd : digit q = b) :
    gap q + carry (oddMap q) = b + 3*carry q := by
  obtain h := scalar_recurrence q hq
  unfold digit phase at hd
  have he : (gap q:ℝ) + (carry (oddMap q):ℝ) = (b:ℝ)+3*(carry q:ℝ) := by linarith
  exact_mod_cast he

/-- A run is tested on the actual scalar of one fixed ordinary source. -/
theorem actual_three_run (q L : ℕ) (hq : 0 < q) (ho : Odd q)
    (run : ∀ i < L, digit (orbit q i)=3) :
    4*8^L ≤ 3^L*(5*q-1) := by
  apply three_run_bound (orbit q) (fun i => gap (orbit q i))
    (fun i => carry (orbit q i)) L
  · intro i _; exact complete_step _
  · intro i hi
    exact actual_clock _ (orbit_pos q i hq) 3 (by simpa using run i hi)
  · exact actual_floor _ (orbit_pos q L hq) (orbit_odd q L ho)

#print axioms actual_floor
#print axioms actual_three_run

end Collatz.ActualThreeRun
