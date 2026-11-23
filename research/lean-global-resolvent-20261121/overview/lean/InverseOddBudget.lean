module
public import Mathlib.Data.Rat.Floor
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Ring
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.FieldSimp

@[expose] public section

namespace CollatzInverseOddBudget

/-- True is an odd inverse step; false is a halving inverse step. -/
def backStep (b : Bool) (x : ℚ) : ℚ := if b then (2*x-1)/3 else 2*x

/-- The list is in forward order, hence the tail is undone first. -/
def backRun : List Bool → ℚ → ℚ
  | [], x => x
  | b::w, x => backStep b (backRun w x)

def odds : List Bool → ℕ
  | [] => 0
  | b::w => odds w + if b then 1 else 0

def coeff (w : List Bool) : ℚ := 2^w.length / 3^(odds w)

def peak (j : ℕ) : ℚ := 2*(3/2:ℚ)^j-1

def endpoint (n j : ℕ) : ℚ := (n+1)*(3/2:ℚ)^j-1

/-- Every intermediate inverse value is an ordinary integer. -/
def IntegralRun : List Bool → ℚ → Prop
  | [], x => ∃ z : ℤ, x = z
  | b::w, x => IntegralRun w x ∧ ∃ z : ℤ, backRun (b::w) x = z

lemma coeff_nil : coeff [] = 1 := by norm_num [coeff, odds]
lemma coeff_cons (b : Bool) (w : List Bool) :
    coeff (b::w) = (if b then (2/3:ℚ) else 2) * coeff w := by
  cases b <;> simp [coeff, odds, pow_succ] <;> ring

lemma coeff_pos (w : List Bool) : 0 < coeff w := by
  dsimp [coeff]
  positivity

lemma run_diff (w : List Bool) (x y : ℚ) :
    backRun w x - backRun w y = coeff w * (x-y) := by
  induction w with
  | nil => simp [backRun, coeff_nil]
  | cons b w ih =>
    rw [backRun, backRun, coeff_cons]
    cases b <;> dsimp [backStep] <;> nlinarith [ih]

lemma peak_ge_one (j : ℕ) : 1 ≤ peak j := by
  have h : (1:ℚ) ≤ (3/2:ℚ)^j := one_le_pow₀ (by norm_num)
  dsimp [peak]
  linarith

lemma peak_succ (j : ℕ) : peak (j+1) = (3*peak j+1)/2 := by
  simp [peak, pow_succ]
  ring

lemma step_mono (b : Bool) {x y : ℚ} (h : x ≤ y) : backStep b x ≤ backStep b y := by
  cases b <;> dsimp [backStep] <;> linarith

lemma step_peak (b : Bool) (j : ℕ) : peak j ≤ backStep b (peak (j+1)) := by
  have h := peak_ge_one j
  rw [peak_succ]
  cases b <;> dsimp [backStep] <;> linarith

lemma run_peak_lower (w : List Bool) (k : ℕ) :
    peak k ≤ backRun w (peak (w.length+k)) := by
  induction w generalizing k with
  | nil => simp [backRun]
  | cons b w ih =>
    have h := ih (k+1)
    have h' := step_mono b h
    have hs := step_peak b k
    simpa [backRun, List.length_cons, Nat.add_assoc, Nat.add_left_comm, Nat.add_comm] using le_trans hs h'

lemma run_peak_short (w : List Bool) {j : ℕ} (h : w.length ≤ j) :
    1 ≤ backRun w (peak j) := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le h
  exact le_trans (peak_ge_one k) (run_peak_lower w k)

lemma run_neg_one (w : List Bool) : backRun w (-1) ≤ -1 := by
  induction w with
  | nil => simp [backRun]
  | cons b w ih => cases b <;> dsimp [backRun, backStep] <;> linarith

lemma run_peak_upper (w : List Bool) (j : ℕ) :
    backRun w (peak j) + 1 ≤ 2 * (coeff w * (3/2:ℚ)^j) := by
  have hd := run_diff w (peak j) (-1)
  have hn := run_neg_one w
  dsimp [peak] at hd ⊢
  nlinarith

lemma integralRun_last {w : List Bool} {x : ℚ} (h : IntegralRun w x) :
    ∃ z : ℤ, backRun w x = z := by
  cases w with
  | nil => exact h
  | cons b w => exact h.2

lemma integral_difference (w : List Bool) {n j L : ℕ}
    (hn : 1 ≤ n) (hd : 3^L ∣ n-1)
    (hj : j ≤ w.length) (ho : odds w ≤ L+j) :
    ∃ z : ℤ, coeff w * (3/2:ℚ)^j * (n-1) = z := by
  obtain ⟨h, hh⟩ := hd
  have hnat : n = 1 + 3^L*h := by omega
  obtain ⟨d, hlen⟩ := Nat.exists_eq_add_of_le hj
  obtain ⟨e, he⟩ := Nat.exists_eq_add_of_le ho
  refine ⟨(2^d * 3^e * h : ℕ), ?_⟩
  have hp3 : (3:ℚ)^L * 3^j = (3:ℚ)^(odds w) * 3^e := by
    rw [← pow_add, ← pow_add, he]
  have hp2 : (2:ℚ)^w.length = (2:ℚ)^j * 2^d := by rw [hlen, pow_add]
  have hnq : (n:ℚ)-1 = 3^L*(h:ℚ) := by exact_mod_cast (by omega : n-1 = 3^L*h)
  rw [hnq]
  push_cast
  dsimp [coeff]
  rw [div_pow, hp2]
  field_simp
  nlinarith [hp3]

lemma virtual_integral (w : List Bool) {n j L : ℕ}
    (hn : 1 ≤ n) (hd : 3^L ∣ n-1)
    (hj : j ≤ w.length) (ho : odds w ≤ L+j)
    (hi : IntegralRun w (endpoint n j)) :
    ∃ z : ℤ, backRun w (peak j) = z := by
  obtain ⟨a, ha⟩ := integralRun_last hi
  obtain ⟨b, hb⟩ := integral_difference w hn hd hj ho
  refine ⟨a-b, ?_⟩
  have hdiff := run_diff w (endpoint n j) (peak j)
  have he : endpoint n j - peak j = (3/2:ℚ)^j * ((n:ℚ)-1) := by
    dsimp [endpoint, peak]
    ring
  rw [he] at hdiff
  rw [← mul_assoc, hb, ha] at hdiff
  push_cast
  linarith

lemma virtual_positive (w : List Bool) {n j L : ℕ}
    (hn : 1 ≤ n) (hd : 3^L ∣ n-1) (ho : odds w ≤ L+j)
    (hi : IntegralRun w (endpoint n j)) :
    1 ≤ backRun w (peak j) := by
  induction w with
  | nil => exact peak_ge_one j
  | cons b w ih =>
    by_cases hs : (b::w).length ≤ j
    · exact run_peak_short (b::w) hs
    have hshort : odds w ≤ L+j := by
      cases b <;> simp [odds] at ho ⊢ <;> omega
    have hv := ih hshort hi.1
    obtain ⟨z, hz⟩ := virtual_integral (b::w) hn hd (by omega) ho hi
    have hp : 0 < backRun (b::w) (peak j) := by
      cases b <;> dsimp [backRun, backStep] <;> linarith
    have hzpos : (0:ℚ) < (z:ℚ) := by simpa [hz] using hp
    have hzi : (1:ℤ) ≤ z := by exact_mod_cast hzpos
    have hzq : (1:ℚ) ≤ (z:ℚ) := by exact_mod_cast hzi
    simpa [hz] using hzq

/-- An unbounded backward word with at most `j+L` odd steps cannot
produce a source smaller than `n` from its initial all-odd endpoint. -/
theorem no_smaller_inverse_word (w : List Bool) {n j L : ℕ}
    (hn : 1 ≤ n) (hd : 3^L ∣ n-1) (ho : odds w ≤ L+j)
    (hi : IntegralRun w (endpoint n j)) :
    (n:ℚ) ≤ backRun w (endpoint n j) := by
  have hv := virtual_positive w hn hd ho hi
  have hu := run_peak_upper w j
  have hc : (1:ℚ) ≤ coeff w * (3/2:ℚ)^j := by linarith
  have hnq : (1:ℚ) ≤ (n:ℚ) := by exact_mod_cast hn
  have hdif := run_diff w (endpoint n j) (peak j)
  have he : endpoint n j - peak j = (3/2:ℚ)^j * ((n:ℚ)-1) := by
    dsimp [endpoint, peak]
    ring
  rw [he, ← mul_assoc] at hdif
  nlinarith

/-- The ordinary shortcut Collatz map. -/
def T (n : ℕ) : ℕ := if n % 2 = 0 then n/2 else (3*n+1)/2

def iterate : ℕ → ℕ → ℕ
  | 0, n => n
  | q+1, n => iterate q (T n)

def bit (n : ℕ) : Bool := decide (n % 2 = 1)

def trace : ℕ → ℕ → List Bool
  | 0, _ => []
  | q+1, n => bit n :: trace q (T n)

def oddCount (q n : ℕ) : ℕ := odds (trace q n)

lemma step_cancel (n : ℕ) : backStep (bit n) (T n) = n := by
  by_cases he : n % 2 = 0
  · have h : 2*(n/2) = n := by omega
    simp [bit, backStep, T, he]
    exact_mod_cast h
  · have ho : n % 2 = 1 := by omega
    have h : 2*((3*n+1)/2) = 3*n+1 := by omega
    have hq : (2:ℚ)*((3*n+1)/2 : ℕ) = 3*(n:ℚ)+1 := by exact_mod_cast h
    simp [bit, ho, backStep, T]
    linarith

lemma run_trace (q n : ℕ) : backRun (trace q n) (iterate q n) = n := by
  induction q generalizing n with
  | zero => simp [trace, iterate, backRun]
  | succ q ih => simpa [trace, iterate, backRun, ih] using step_cancel n

lemma integral_trace (q n : ℕ) : IntegralRun (trace q n) (iterate q n) := by
  induction q generalizing n with
  | zero => exact ⟨n, by simp [iterate]⟩
  | succ q ih =>
    change IntegralRun (trace q (T n)) (iterate q (T n)) ∧ _
    refine ⟨ih (T n), n, ?_⟩
    simpa [trace] using run_trace (q+1) n

lemma rising_endpoint {n j : ℕ} (hj : 2^j ∣ n+1) :
    (iterate j n : ℚ) = endpoint n j := by
  induction j generalizing n with
  | zero => simp [iterate, endpoint]
  | succ j ih =>
    obtain ⟨u, hu⟩ := hj
    have heven : 2 ∣ n+1 := by
      refine ⟨2^j*u, ?_⟩
      rw [hu, pow_succ]
      ring
    have hodd : n % 2 = 1 := by omega
    have hT : 2*(T n+1) = 3*(n+1) := by
      simp [T, hodd]
      omega
    have hT' : T n+1 = 2^j*(3*u) := by
      rw [hu, pow_succ] at hT
      nlinarith
    have hd : 2^j ∣ T n+1 := ⟨3*u, hT'⟩
    have hTq : (T n : ℚ)+1 = (3/2:ℚ)*((n:ℚ)+1) := by
      have hc : (2:ℚ)*((T n:ℚ)+1) = 3*((n:ℚ)+1) := by exact_mod_cast hT
      linarith
    rw [iterate, ih hd]
    dsimp [endpoint]
    rw [hTq, pow_succ]
    ring

/-- Every smaller ordinary merger into the initial all-odd ascent must
pay more than the full ternary reserve in additional odd inputs. -/
theorem smaller_merger_odd_surplus {n x j q L : ℕ}
    (hn : 1 ≤ n) (h2 : 2^j ∣ n+1) (h3 : 3^L ∣ n-1)
    (hx : x < n) (hm : iterate q x = iterate j n) :
    j+L < oddCount q x := by
  by_contra hnot
  have ho : odds (trace q x) ≤ L+j := by dsimp [oddCount] at hnot; omega
  have he : (iterate q x : ℚ) = endpoint n j := by rw [hm, rising_endpoint h2]
  have hi := integral_trace q x
  rw [he] at hi
  have hb := no_smaller_inverse_word (trace q x) hn h3 ho hi
  rw [← he, run_trace] at hb
  have hl : (x:ℚ) < (n:ℚ) := by exact_mod_cast hx
  linarith

/-- A fully explicit ternary lifting identity. -/
lemma lift_three (H : ℕ) : ∃ c : ℕ, 4^(3^H) = 1 + 3^(H+1)*c := by
  induction H with
  | zero => exact ⟨1, by norm_num⟩
  | succ H ih =>
    obtain ⟨c, hc⟩ := ih
    refine ⟨c + 3*(3^H)*c^2 + 3*(3^H)^2*c^3, ?_⟩
    calc
      4^(3^(H+1)) = (4^(3^H))^3 := by rw [pow_succ, pow_mul]
      _ = (1 + 3^(H+1)*c)^3 := by rw [hc]
      _ = 1 + 3^((H+1)+1)*(c + 3*(3^H)*c^2 + 3*(3^H)^2*c^3) := by
        simp only [pow_succ]
        ring

def ascentLength (H : ℕ) : ℕ := 2*3^H+1

def mersenne (H : ℕ) : ℕ := 2^(ascentLength H)-1

lemma mersenne_center_one (H : ℕ) : ∃ c : ℕ, mersenne H = 1 + 2*3^(H+1)*c := by
  obtain ⟨c, hc⟩ := lift_three H
  refine ⟨c, ?_⟩
  have hp : 2^(ascentLength H) = 2 + 2*3^(H+1)*c := by
    dsimp [ascentLength]
    rw [pow_succ, pow_mul]
    norm_num only [Nat.reducePow]
    rw [hc]
    ring
  dsimp [mersenne]
  omega

lemma mersenne_positive (H : ℕ) : 1 ≤ mersenne H := by
  obtain ⟨c, hc⟩ := mersenne_center_one H
  omega

lemma mersenne_ternary (H : ℕ) : 3^(H+1) ∣ mersenne H-1 := by
  obtain ⟨c, hc⟩ := mersenne_center_one H
  refine ⟨2*c, ?_⟩
  rw [hc]
  simp only [Nat.add_sub_cancel_left]
  ring

lemma mersenne_add_one (H : ℕ) : mersenne H+1 = 2^(ascentLength H) := by
  have hp : 0 < 2^(ascentLength H) := by positivity
  dsimp [mersenne]
  omega

/-- Throughout each entire initial Mersenne ascent, every smaller merger
requires an arbitrarily large excess of odd inputs. -/
theorem mersenne_merger_odd_budget {H j q x : ℕ}
    (hj : j ≤ ascentLength H) (hx : x < mersenne H)
    (hm : iterate q x = iterate j (mersenne H)) :
    j+H+2 ≤ oddCount q x := by
  have h2 : 2^j ∣ mersenne H+1 := by
    rw [mersenne_add_one]
    exact Nat.pow_dvd_pow 2 hj
  have hb := smaller_merger_odd_surplus (mersenne_positive H) h2 (mersenne_ternary H) hx hm
  omega

/-- The strict threshold is attained: the smaller source 27 merges into
31 using exactly two odd inputs, while v₃(31−1)=1. -/
theorem sharp_small_example :
    27 < 31 ∧ 3 ∣ 31-1 ∧ ¬ 9 ∣ 31-1 ∧ iterate 3 27 = 31 ∧ oddCount 3 27 = 2 := by
  norm_num [iterate, T, oddCount, trace, odds, bit]

#print axioms no_smaller_inverse_word
#print axioms smaller_merger_odd_surplus
#print axioms mersenne_merger_odd_budget

end CollatzInverseOddBudget
