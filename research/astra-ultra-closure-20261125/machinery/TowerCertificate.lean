import BinomialTower
import Mathlib.Data.Nat.Choose.Basic

set_option exponentiation.threshold 2048

namespace TowerCertificate
open scoped BigOperators
open TowerDescent PhysicalEcho

/-- Sum a rank indicator across consecutive powers of three. -/
private def ranks : ℕ → ℕ → ℕ → ℕ → ℕ
  | 0, _, _, _ => 0
  | r+1, H, b, v => (if H ≤ b*(v+1) then 1 else 0) + ranks r H b (v*3)

private theorem ranks_eq (R H b v : ℕ) :
    ranks R H b v = ∑ j ∈ Finset.range R, if H ≤ b*(v*3^j+1) then 1 else 0 := by
  induction R generalizing v with
  | zero => simp [ranks]
  | succ R ih =>
    rw [ranks, ih, Finset.sum_range_succ']
    simp only [pow_zero, mul_one]
    simp_rw [pow_succ' 3, Nat.mul_assoc]
    omega

/-- Accumulate by word weight. The successively updated coefficient c is an
    exact binomial coefficient, by the consecutive-binomial relation. -/
private def sweep : ℕ → ℕ → ℕ → ℕ → ℕ → ℕ → ℕ → ℕ
  | 0, _, _, _, _, _, _ => 0
  | len+1, h, R, H, p, c, b =>
    c * ranks R H b 1 +
      sweep len h R H (p+1) (c*(h-p)/(p+1)) (b*3)

private theorem sweep_eq (len h R H p v : ℕ) :
    sweep len h R H p (Nat.choose h p) (v*3^p) =
      ∑ j ∈ Finset.range len, Nat.choose h (p+j) *
        (∑ r ∈ Finset.range R, if H ≤ v*3^(p+j)*(3^r+1) then 1 else 0) := by
  induction len generalizing p with
  | zero => simp [sweep]
  | succ len ih =>
    have coeff : Nat.choose h p*(h-p)/(p+1) = Nat.choose h (p+1) := by
      rw [← Nat.choose_succ_right_eq, Nat.mul_div_cancel _ (by omega : 0<p+1)]
    rw [sweep, coeff, show v*3^p*3=v*3^(p+1) by rw [pow_succ, Nat.mul_assoc], ih, ranks_eq, Finset.sum_range_succ']
    simp only [Nat.one_mul, Nat.add_zero]
    rw [Nat.add_comm]
    congr 1
    apply Finset.sum_congr rfl
    intro j _
    rw [show p+1+j=p+(j+1) by omega]

private theorem total_eq_sweep (h R : ℕ) :
    (∑ r ∈ Finset.range R, tailCount h r) =
      sweep (h+1) h R (2^h) 0 1 1 := by
  have he := sweep_eq (h+1) h R (2^h) 0 1
  simp only [Nat.choose_zero_right,pow_zero,Nat.zero_add,Nat.one_mul] at he
  rw [he]
  simp only [tailCount, possibleCounts, Finset.sum_filter]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro j _
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro r _
  by_cases hk : 2^h ≤ 3^j*(3^r+1) <;> simp [hk]

private theorem ray_eq_sweep (l R : ℕ) :
    (∑ r ∈ Finset.range R, rayTail l r) =
      sweep (l+1) l R (2^(l+1)) 0 1 3 := by
  have he := sweep_eq (l+1) l R (2^(l+1)) 0 3
  simp only [Nat.choose_zero_right,pow_zero,Nat.zero_add,Nat.mul_one] at he
  rw [he]
  simp only [rayTail, Finset.sum_filter, pow_succ' 3]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro j _
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro r _
  by_cases hk : 2^(l+1) ≤ 3*3^j*(3^r+1) <;> simp [hk]

set_option maxRecDepth 200000 in
set_option maxHeartbeats 100000000 in
theorem numerical_116 :
    10^6*(∑ r ∈ Finset.range 116, tailCount 1024 r) < 919766*2^1024 := by
  rw [total_eq_sweep]
  decide +kernel

set_option maxRecDepth 200000 in
set_option maxHeartbeats 100000000 in
theorem odd_numerical_116 :
    10^6*(∑ r ∈ Finset.range 116, rayTail 1023 r) < 978462*2^1023 := by
  rw [ray_eq_sweep]
  decide +kernel

/-- For the same 116 exponents, the 1024-step ordinary endpoint is below
    one common base chosen from any qualifying block. -/
theorem full_block_116 (a : ℕ) (ha : 2^1024 ≤ a) :
    ∃ i : Fin (2^1024), ∀ r ≤ 115, ∃ b : ℕ, 0<b ∧ b<a+i.val ∧
      orbit 1024 (3^r*(a+i.val))=orbit 0 (3^0*b) := by
  apply exists_of_tail ha
  change (∑ r ∈ Finset.range 116, tailCount 1024 r) < 2^1024
  exact Nat.lt_of_mul_lt_mul_left (numerical_116.trans_le
    (Nat.mul_le_mul_right _ (by decide : 919766≤10^6)))

/-- The same conclusion is available within each eligible odd progression
    of step six, preserving the class modulo six. -/
theorem odd_ray_116 (a : ℕ) (ha : 2^1024 ≤ a) (odd : a%2=1) :
    ∃ i : Fin (2^1023), ∀ r ≤ 115,
      0<orbit 1024 (3^r*(a+6*i.val)) ∧ orbit 1024 (3^r*(a+6*i.val))<a+6*i.val := by
  apply ray_exists_of_tail (l:=1023) ha odd
  change (∑ r ∈ Finset.range 116, rayTail 1023 r) < 2^1023
  exact Nat.lt_of_mul_lt_mul_left (odd_numerical_116.trans_le
    (Nat.mul_le_mul_right _ (by decide : 978462≤10^6)))

#print axioms numerical_116
#print axioms odd_numerical_116
#print axioms full_block_116
#print axioms odd_ray_116

private theorem twice_step (n : ℕ) :
    2 * step n = 3^(n%2)*n+n%2 := by
  by_cases hz : n%2=0
  · simp [step,hz]; omega
  · have ho : n%2=1 := by omega
    simp [step,ho]; omega

/-- A uniform bound for the additive affine correction, independent of the
    input n. It keeps the linear term exact. -/
theorem affine_sandwich (h n : ℕ) :
    3^(odds h n)*n ≤ 2^h*orbit h n ∧
    2^h*orbit h n ≤ 3^(odds h n)*n+3^h := by
  induction h generalizing n with
  | zero => simp [orbit, odds]
  | succ h ih =>
    obtain ⟨lo,hi⟩ := ih (step n)
    have ep : odds (h+1) n = n%2 + odds h (step n) := by
      change (if n%2=0 then 0 else 1)+_ = _
      split <;> omega
    have hp : 3^(odds h (step n)) ≤ (3:ℕ)^h :=
      Nat.pow_le_pow_right (by decide) (odds_le h _)
    have cap : 3^(odds h (step n))*(n%2) ≤ 3^h := by
      have hz : n%2 ≤ 1 := by omega
      exact (Nat.mul_le_mul_right _ hp).trans ((Nat.mul_le_mul_left _ hz).trans_eq (Nat.mul_one _))
    have eq := congrArg (fun z => 3^(odds h (step n))*z) (twice_step n)
    simp only [ep,pow_add,Nat.pow_one,orbit] at *
    constructor <;> nlinarith [Nat.zero_le (3^(odds h (step n))*(n%2))]

/-- At clock 1024 the lower-base test is exact on every ordinary input in
    the full-sized region w≥2^1024, for every ternary exponent r. -/
theorem exact_clock_1024 (w r : ℕ) (base : 2^1024 ≤ w) :
    orbit 1024 (3^r*w) < w ↔ odds 1024 (3^r*w)+r ≤ 646 := by
  let q := odds 1024 (3^r*w)
  obtain ⟨lo,hi⟩ := affine_sandwich 1024 (3^r*w)
  change 3^q*(3^r*w) ≤ _ at lo
  change _ ≤ 3^q*(3^r*w)+_ at hi
  rw [←Nat.mul_assoc, ←pow_add] at lo hi
  change _ ↔ q+r≤646
  constructor
  · intro below
    by_contra! high
    have power : 2^1024 ≤ (3:ℕ)^(q+r) :=
      (by decide : 2^1024 ≤ (3:ℕ)^647).trans
        (Nat.pow_le_pow_right (by decide) (by omega))
    have left := (Nat.mul_le_mul_right w power).trans lo
    exact (Nat.not_le_of_lt (Nat.mul_lt_mul_of_pos_left below (by positivity))) left
  · intro low
    have gap : 3^1024 < (2^1024-3^646)*w :=
      (by decide : 3^1024 < (2^1024-3^646)*2^1024).trans_le
        (Nat.mul_le_mul_left _ base)
    have hpow : (3:ℕ)^(q+r) ≤ 3^646 := Nat.pow_le_pow_right (by decide) low
    have scale := Nat.mul_le_mul_right w hpow
    have split : (2^1024-3^646)*w+3^646*w=2^1024*w := by
      rw [← Nat.add_mul, Nat.sub_add_cancel (by decide : 3^646≤2^1024)]
    apply Nat.lt_of_mul_lt_mul_left (a:=2^1024)
    omega

#print axioms affine_sandwich
#print axioms exact_clock_1024

end TowerCertificate
