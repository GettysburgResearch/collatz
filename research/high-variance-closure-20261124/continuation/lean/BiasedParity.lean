import Mathlib
import QuarterShift

namespace BiasedParity

open QuarterShift

/-- Cleared cubed physical estimate on one finite actual high path. -/
theorem highPrefix (k n : ℕ)
    (hh : ∀ i, i < k → 20 ≤ endpoint i n) :
    2^(3*k) * (endpoint k n)^3 ≤ n^3 * 2^(5*oddCount k n) := by
  induction k generalizing n with
  | zero => simp [endpoint,oddCount]
  | succ k ih =>
    have hn : 20≤n := by simpa [endpoint] using hh 0 (by omega)
    have htail := ih (step n) (by
      intro i hi
      exact hh (i+1) (by omega))
    have hlocal : 8*(step n)^3 ≤ n^3*2^(5*(n%2)) := by
      have hm : n%2=0 ∨ n%2=1 := by omega
      rcases hm with h|h
      · rw [h]
        simp only [step,h,ite_true,Nat.mul_zero,pow_zero,Nat.mul_one]
        have he : 2*(n/2)=n := by omega
        calc 8*(n/2)^3=(2*(n/2))^3 := by ring
             _≤n^3 := by rw [he]
      · have he : 2*step n=3*n+1 := by simp [step,h]; omega
        have hr : 20*(2*step n)≤61*n := by rw [he];omega
        have hc := Nat.pow_le_pow_left hr 3
        have hs : 61^3 ≤ 32*20^3 := by decide
        have hb := Nat.mul_le_mul_right (n^3) hs
        rw [h]
        norm_num
        nlinarith only [hc,hb]
    calc
      2^(3*(k+1)) * (endpoint (k+1) n)^3 =
        8*(2^(3*k)*(endpoint k (step n))^3) := by
          rw [show 3*(k+1)=3*k+3 by omega,pow_add];simp [endpoint];ring
      _ ≤ 8*((step n)^3*2^(5*oddCount k (step n))) := Nat.mul_le_mul_left _ htail
      _ = (8*(step n)^3)*2^(5*oddCount k (step n)) := by ring
      _ ≤ (n^3*2^(5*(n%2)))*2^(5*oddCount k (step n)) := Nat.mul_le_mul_right _ hlocal
      _ = n^3*2^(5*oddCount (k+1) n) := by
        rw [oddCount,Nat.mul_add,pow_add];ring

/-- The fifth power of the k-th tilted summand has a strict geometric lower bound. -/
theorem geometricTerm (k n : ℕ)
    (hh : ∀ i, i < k → 20≤endpoint i n)
    (hp : 0<endpoint k n) :
    256^k * (3^k)^5 ≤ n^3 * (2^(k+oddCount k n))^5 * 243^k := by
  have h := highPrefix k n hh
  have hl : 2^(3*k) ≤ n^3*2^(5*oddCount k n) := by
    calc 2^(3*k) ≤ 2^(3*k)*(endpoint k n)^3 := Nat.le_mul_of_pos_right _ (by positivity)
         _ ≤ _ := h
  have hx := Nat.mul_le_mul_left (2^(5*k)*243^k) hl
  convert hx using 1 <;> simp only [pow_add,mul_pow,← pow_mul]
  · rw [show (256:ℕ)=2^8 by decide,show (243:ℕ)=3^5 by decide,← pow_mul,← pow_mul]
    ring_nf
  · ring_nf

noncomputable def term (n k : ℕ) : ℝ := (2:ℝ)^(k+oddCount k n) / 3^k

private theorem termNext (n k : ℕ) :
    term n (k+1)=((2:ℝ)^(1+n%2)/3)*term (step n) k := by
  unfold term
  rw [oddCount,show k+1+(n%2+oddCount k (step n))=
      (1+n%2)+(k+oddCount k (step n)) by omega,pow_add,pow_succ]
  ring

private theorem epAdd (a b n : ℕ) : endpoint (a+b) n=endpoint b (endpoint a n) := by
  induction a generalizing n with
  | zero => simp [endpoint]
  | succ a ih => simpa only [Nat.succ_add,endpoint] using ih (step n)

private theorem posAt (k n : ℕ) (hn : 0<n) : 0<endpoint k n := by
  induction k generalizing n with
  | zero => simpa [endpoint] using hn
  | succ k ih =>
    apply ih
    unfold step
    split <;> omega

private theorem oneTwo (k : ℕ) : term 1 (k+2)=(8/9:ℝ)*term 1 k := by
  rw [termNext,termNext]
  norm_num [step]
  ring

private theorem oneBound (k : ℕ) : term 1 k ≤ 2*(19/20:ℝ)^k := by
  induction k using Nat.twoStepInduction with
  | zero => norm_num [term,oddCount]
  | one => norm_num [term,oddCount]
  | more k hk _ =>
    rw [oneTwo,pow_add]
    have hpos : 0≤(19/20:ℝ)^k := by positivity
    nlinarith

theorem summableOfHits (n j : ℕ) (hit : endpoint j n=1) : Summable (term n) := by
  induction j generalizing n with
  | zero =>
    have h : n=1 := hit
    rw [h]
    exact Summable.of_nonneg_of_le (fun k => by unfold term; positivity) oneBound
      ((summable_geometric_of_lt_one (by norm_num : (0:ℝ)≤19/20) (by norm_num)).mul_left 2)
  | succ j ih =>
    apply (summable_nat_add_iff 1).mp
    simpa only [termNext] using (ih (step n) hit).mul_left ((2:ℝ)^(1+n%2)/3)

theorem boundedIffHits (n : ℕ) (hn : 0<n) :
    BddAbove (Set.range (term n)) ↔ ∃ j, endpoint j n=1 := by
  constructor
  · rintro ⟨M,hM⟩
    by_contra hno
    have hhigh (i : ℕ) : 20≤endpoint i n := by
      by_contra hlow
      let m : Fin 20 := ⟨endpoint i n, by omega⟩
      obtain ⟨j,hj⟩ := below_twenty m (posAt i n hn)
      exact hno ⟨i+j, (epAdd i j n).trans hj⟩
    have hM0 : 0≤M := by
      have hm := hM (Set.mem_range_self (f:=term n) 0)
      norm_num [term,oddCount] at hm
      linarith
    have ev := (tendsto_pow_atTop_atTop_of_one_lt (by norm_num : (1:ℝ)<256/243)).eventually_gt_atTop
        ((n:ℝ)^3*M^5)
    obtain ⟨k,hk⟩ := ev.exists
    have hraw := geometricTerm k n (fun i _ => hhigh i) (posAt k n hn)
    have hreal : (256:ℝ)^k*(3^k:ℝ)^5 ≤ (n:ℝ)^3*((2:ℝ)^(k+oddCount k n))^5*243^k := by
      exact_mod_cast hraw
    have hrat : (256/243:ℝ)^k ≤ (n:ℝ)^3*(term n k)^5 := by
      unfold term
      rw [div_pow,div_pow]
      apply (div_le_iff₀ (by positivity : (0:ℝ)<243^k)).mpr
      rw [mul_div_assoc',div_mul_eq_mul_div]
      apply (le_div_iff₀ (by positivity : (0:ℝ)<(3^k:ℝ)^5)).mpr
      exact hreal
    have hterm := hM (Set.mem_range_self (f:=term n) k)
    have hle : (term n k)^5≤M^5 := by
      gcongr
      unfold term
      positivity
    exact (not_lt_of_ge (hrat.trans (mul_le_mul_of_nonneg_left hle (by positivity)))) hk
  · rintro ⟨j,hj⟩
    exact (summableOfHits n j hj).tendsto_atTop_zero.bddAbove_range

theorem summableIffHits (n : ℕ) (hn : 0<n) :
    Summable (term n) ↔ ∃ j, endpoint j n=1 := by
  constructor
  · intro hs
    exact (boundedIffHits n hn).mp hs.tendsto_atTop_zero.bddAbove_range
  · rintro ⟨j,hj⟩
    exact summableOfHits n j hj

#print axioms highPrefix
#print axioms geometricTerm
#print axioms summableOfHits
#print axioms boundedIffHits
#print axioms summableIffHits
end BiasedParity
