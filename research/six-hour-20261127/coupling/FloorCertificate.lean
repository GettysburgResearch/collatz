import FloorCounting
import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Tactic.FieldSimp

/-! A second exact certificate for the high-floor reciprocal estimate.
It uses no restriction modulo three. -/
set_option autoImplicit false
set_option warningAsError true
set_option maxRecDepth 20000
set_option exponentiation.threshold 1000
namespace FloorCertificate
open CoreBranching FloorCounting
open scoped BigOperators

def cut (j : ℕ) : ℕ := 41*j/65

private theorem cut_pow (j : ℕ) : 3^cut j ≤ (2:ℕ)^j := by
  have rate : (3:ℕ)^41 ≤ 2^65 := by decide +kernel
  have fit : cut j*65≤41*j := Nat.div_mul_le_self _ _
  have w : ((3:ℕ)^cut j)^65 ≤ (2^j)^65 := calc
    _ = 3^(cut j*65) := (pow_mul ..).symm
    _ ≤ 3^(41*j) := Nat.pow_le_pow_right (by decide) fit
    _ = (3^41)^j := pow_mul ..
    _ ≤ (2^65)^j := Nat.pow_le_pow_left rate _
    _ = (2^j)^65 := by rw [←pow_mul,←pow_mul,Nat.mul_comm 65]
  exact le_of_not_gt (fun e => (not_lt_of_ge w) (Nat.pow_lt_pow_left e (by decide)))

private theorem ballots_choose (k F n p : ℕ) : ballots k F n p ≤ n.choose p := by
  induction n generalizing p with
  | zero => cases p <;> simp [ballots]
  | succ n ih =>
    unfold ballots
    split
    · cases p with
      | zero => simpa using ih 0
      | succ p =>
        simp only [Nat.add_one_ne_zero,ite_false,Nat.add_sub_cancel,Nat.choose_succ_succ]
        exact (Nat.add_le_add (ih (p+1)) (ih p)).trans_eq (Nat.add_comm ..)
    · exact Nat.zero_le _

def tail (n q : ℕ) := ∑ p ∈ Finset.range (n+1), if q<p then n.choose p else 0

theorem shell_count (x L F j : ℕ)
    (simple : ∀ a≤L, ∀ b≤L, run a x=run b x → a=b)
    (floor : ∀ t≤L, F≤run t x) :
    (visits x L (2^(j+1))).card ≤ (visits x L (2^j)).card+(j+1)+tail (j+1) (cut j) := by
  have h := visit_bound x L F (j+1) 0 (cut j) (2^j) simple floor (Or.inr rfl)
    (by simpa using cut_pow j)
  have c : (∑ p ∈ Finset.range (j+1+1), if cut j<p then ballots (j+1) F (j+1) p else 0)
      ≤tail (j+1) (cut j) := by
    apply Finset.sum_le_sum
    intro p _
    by_cases e : cut j<p
    · simpa [e] using ballots_choose (j+1) F (j+1) p
    · simp [e]
  simp only [Nat.add_zero,pow_zero,Nat.reduceDiv,Nat.sub_zero,one_mul] at h
  omega

private theorem tilted (n q : ℕ) : ((tail n q:ℕ):ℚ)*(5/3:ℚ)^(q+1)≤(1+5/3:ℚ)^n := by
  rw [tail,Nat.cast_sum,Finset.sum_mul,add_comm (1:ℚ),add_pow]
  apply Finset.sum_le_sum
  intro p _
  by_cases h : q<p
  · simp only [h,ite_true,one_pow,mul_one]
    rw [mul_comm (n.choose p : ℚ)]
    exact mul_le_mul_of_nonneg_right
      (pow_le_pow_right₀ (by norm_num) (show q+1≤p by omega)) (by positivity)
  · simp [h]; positivity

theorem geometric_tail (j : ℕ) :
    (tail (j+1) (cut j):ℚ)/(2:ℚ)^j ≤ (8/3:ℚ)*(31/32:ℚ)^j := by
  have w := tilted (j+1) (cut j)
  have ratio : (4/3:ℚ)^65*(3/5:ℚ)^41 ≤ (31/32:ℚ)^65 := by norm_num
  have ce : 41*j≤(cut j+1)*65 := by unfold cut; omega
  have ap : ((3/5:ℚ)^(cut j+1))^65 ≤ ((3/5:ℚ)^41)^j := by
    rw [←pow_mul,←pow_mul]
    exact pow_le_pow_of_le_one (by norm_num) (by norm_num) ce
  have scale : ((4/3:ℚ)^j*(3/5:ℚ)^(cut j+1))^65 ≤ ((31/32:ℚ)^j)^65 := calc
    _ = ((4/3:ℚ)^65)^j*((3/5:ℚ)^(cut j+1))^65 := by
      rw [mul_pow,←pow_mul, Nat.mul_comm j, pow_mul]
    _ ≤ ((4/3:ℚ)^65)^j*((3/5:ℚ)^41)^j :=
      mul_le_mul_of_nonneg_left ap (by positivity)
    _ = ((4/3:ℚ)^65*(3/5:ℚ)^41)^j := (mul_pow ..).symm
    _ ≤ ((31/32:ℚ)^65)^j := pow_le_pow_left₀ (by positivity) ratio _
    _ = _ := by rw [←pow_mul,←pow_mul,Nat.mul_comm 65]
  have s : (4/3:ℚ)^j*(3/5:ℚ)^(cut j+1)≤(31/32:ℚ)^j := by
    by_contra! no
    exact (not_lt_of_ge scale) (pow_lt_pow_left₀ no (by positivity) (by decide))
  have ww := mul_le_mul_of_nonneg_right w (by positivity : 0≤(3/5:ℚ)^(cut j+1))
  rw [mul_assoc,←mul_pow] at ww
  norm_num at ww
  have out := div_le_div_of_nonneg_right ww (by positivity : 0≤(2:ℚ)^j)
  calc
    _ ≤ _ := out
    _ = (8/3:ℚ)*((4/3:ℚ)^j*(3/5:ℚ)^(cut j+1)) := by
      rw [pow_succ]
      have b : (8/3:ℚ)^j=(2:ℚ)^j*(4/3:ℚ)^j := by rw [←mul_pow]; norm_num
      rw [b]; field_simp
    _ ≤ _ := mul_le_mul_of_nonneg_left s (by norm_num)

/-- Only the shorter complementary factorial is evaluated by the kernel. -/
private def fastCount (n q : ℕ) : ℕ → ℕ
  | 0 => 0
  | p+1 => fastCount n q p + if q<p then Nat.fast_choose n (n-p) else 0

private theorem fastCount_eq (n q b : ℕ) (hb : b≤n+1) :
    fastCount n q b = ∑ p ∈ Finset.range b, if q<p then n.choose p else 0 := by
  induction b with
  | zero => simp [fastCount]
  | succ b ih =>
    rw [fastCount,Finset.sum_range_succ,ih (by omega)]
    by_cases h : q<b
    · simp only [h,ite_true]
      rw [←Nat.choose_eq_fast_choose,Nat.choose_symm (show b≤n by omega)]
    · simp [h]

private def numerator : ℕ → ℕ
  | 0 => 0
  | j+1 => 2*numerator j+
      (if 71≤j then 2*(j+1+fastCount (j+1) (cut j) (j+2)) else 0)

set_option maxHeartbeats 0 in
private theorem finite_arithmetic : 1000*numerator 325 ≤ 993*2^325 := by decide +kernel

private def weight (j : ℕ) : ℚ :=
  if 71≤j then ((j+1:ℕ)+tail (j+1) (cut j))/(2:ℚ)^j else 0

private theorem weight_nonneg (j : ℕ) : 0≤weight j := by
  unfold weight
  split
  · exact div_nonneg (by positivity) (by norm_num)
  · rfl

private theorem numerator_sum (n : ℕ) :
    (numerator n:ℚ)/(2:ℚ)^n = ∑ j ∈ Finset.range n, weight j := by
  induction n with
  | zero => simp [numerator]
  | succ n ih =>
    rw [Finset.sum_range_succ,←ih,numerator,pow_succ]
    by_cases h : 71≤n
    · have fc := fastCount_eq (n+1) (cut n) (n+2) (by omega)
      simp only [weight,h,ite_true,fc]
      unfold tail
      push_cast
      ring
    · simp [weight,h]
      ring

private def reserve (j : ℕ) : ℚ :=
  (2*((j:ℚ)+2))/(2:ℚ)^j+(256/3:ℚ)*(31/32:ℚ)^j

private theorem reserve_pos (j : ℕ) : 0≤reserve j := by
  unfold reserve
  apply add_nonneg
  · exact div_nonneg (by positivity) (by norm_num)
  · exact mul_nonneg (by norm_num) (pow_nonneg (by norm_num) _)

private theorem spend (j : ℕ) : weight j+reserve (j+1)≤reserve j := by
  have e := geometric_tail j
  have h : ((j:ℚ)+1)/(2:ℚ)^j + (8/3:ℚ)*(31/32:ℚ)^j + reserve (j+1) = reserve j := by
    unfold reserve
    push_cast
    rw [pow_succ,pow_succ]
    ring
  rw [←h]
  apply add_le_add_left
  by_cases w : 71≤j
  · simp only [weight,w,ite_true,Nat.cast_add,Nat.cast_one,add_div]
    exact add_le_add_right e _
  · simp only [weight,w,ite_false]
    apply add_nonneg
    · exact div_nonneg (by positivity) (by norm_num)
    · exact mul_nonneg (by norm_num) (pow_nonneg (by norm_num) _)

private theorem spend_all (j n : ℕ) :
    (∑ i ∈ Finset.range n, weight (j+i)) + reserve (j+n) ≤ reserve j := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ,←Nat.add_assoc,add_assoc]
    exact (add_le_add_right (spend (j+n)) _).trans ih

private theorem total_budget (n : ℕ) : (∑ j ∈ Finset.range n, weight j) < 249/250 := by
  have f := finite_arithmetic
  have f' : (∑ j ∈ Finset.range 325, weight j) ≤ 993/1000 := by
    rw [←numerator_sum]
    have ff : (1000:ℚ)*(numerator 325:ℚ)≤993*(2:ℚ)^325 := by exact_mod_cast f
    apply (div_le_iff₀ (by positivity)).2
    linarith only [ff]
  by_cases le : n≤325
  · have small := Finset.sum_le_sum_of_subset_of_nonneg (Finset.range_mono le)
        (fun i _ _ => weight_nonneg i)
    linarith
  · obtain ⟨d,hd⟩ := Nat.exists_eq_add_of_le (show 325≤n by omega)
    rw [hd,Finset.sum_range_add]
    have s := spend_all 325 d
    have sp := reserve_pos (325+d)
    have bound : reserve 325 < 3/1000 := by norm_num [reserve]
    linarith

private theorem sliced (x L n : ℕ)
    (simple : ∀ a≤L, ∀ b≤L, run a x=run b x → a=b)
    (floor : ∀ t≤L, 2^71≤run t x) :
    (∑ t ∈ visits x L (2^n), 1/(run t x:ℚ)) ≤ ∑ j ∈ Finset.range n, weight j := by
  have mem (B t : ℕ) : t∈visits x L B ↔ t≤L ∧ run t x<B := by
    simp [visits]
  induction n with
  | zero =>
    have emp : visits x L 1=∅ := by
      apply Finset.eq_empty_iff_forall_notMem.mpr
      intro t ht
      obtain ⟨a,b⟩ := (mem 1 t).mp ht
      have := floor t a
      omega
    simp [emp]
  | succ n ih =>
    have incl : visits x L (2^n) ⊆ visits x L (2^(n+1)) := by
      intro t ht
      obtain ⟨a,b⟩ := (mem _ _).mp ht
      exact (mem _ _).mpr ⟨a,b.trans_le (Nat.pow_le_pow_right (by decide) (by omega))⟩
    rw [←Finset.sum_sdiff incl,Finset.sum_range_succ,add_comm (∑ _ ∈ _ \ _, _)]
    apply add_le_add ih
    let C := visits x L (2^(n+1)) \ visits x L (2^n)
    change (∑ t ∈ C, 1/(run t x:ℚ)) ≤ weight n
    by_cases h : 71≤n
    · have size : C.card≤ n+1+tail (n+1) (cut n) := by
        have bound := shell_count x L (2^71) n simple floor
        rw [show C.card=(visits x L (2^(n+1))).card-(visits x L (2^n)).card by
          simp [C,Finset.card_sdiff,Finset.inter_eq_left.mpr incl]]
        omega
      calc
        _ ≤ ∑ _ ∈ C, 1/(2:ℚ)^n := by
          apply Finset.sum_le_sum
          intro t ht
          obtain ⟨t1,t0⟩ := Finset.mem_sdiff.mp ht
          have htL := ((mem _ _).mp t1).1
          have htB : 2^n≤run t x := by
            by_contra! no
            exact t0 ((mem _ _).mpr ⟨htL,no⟩)
          exact div_le_div_of_nonneg_left (by norm_num) (by positivity) (by exact_mod_cast htB)
        _ = (C.card:ℚ)/(2:ℚ)^n := by simp [div_eq_mul_inv]
        _ ≤ weight n := by
          simp only [weight,h,ite_true]
          exact div_le_div_of_nonneg_right (by exact_mod_cast size) (by positivity)
    · have emp : C=∅ := by
        apply Finset.eq_empty_iff_forall_notMem.mpr
        intro t ht
        obtain ⟨tl,hn⟩ := (mem _ _).mp (Finset.mem_sdiff.mp ht).1
        have u := floor t tl
        have v : (2:ℕ)^(n+1)≤2^71 := Nat.pow_le_pow_right (by decide) (by omega)
        omega
      simp [emp,weight,h]

/-- All sites, including the endpoint, on the supplied ordinary simple path. -/
theorem reciprocal_floor (x L : ℕ)
    (simple : ∀ a≤L, ∀ b≤L, run a x=run b x → a=b)
    (floor : ∀ t≤L, 2^71≤run t x) :
    (∑ t ∈ Finset.range (L+1), 1/(run t x:ℚ)) < 249/250 := by
  let n := (Finset.range (L+1)).sup (fun t => run t x)
  have allV : visits x L (2^n)=Finset.range (L+1) := by
    apply Finset.filter_true_of_mem
    intro t ht
    exact (Finset.le_sup (f:=fun i => run i x) ht).trans_lt (Nat.lt_two_pow_self (n:=n))
  rw [←allV]
  exact (sliced x L n simple floor).trans_lt (total_budget n)

def evenCorrection (y : ℕ) : ℚ := if y%2=0 then 1/((y:ℚ)+1) else 0

private theorem local_balance (y : ℕ) (hy : 10000≤y) :
    (3999/1000:ℚ)*evenCorrection y ≤
      1/(y:ℚ) + 3*(1/((step y:ℚ)+1)-1/((y:ℚ)+1)) := by
  have yp : (0:ℚ)<y := by exact_mod_cast (by omega : 0<y)
  have yl : (10000:ℚ)≤y := by exact_mod_cast hy
  by_cases e : y%2=0
  · have a : 2*step y=y := by simp [step,e]; omega
    have b : (step y:ℚ)=(y:ℚ)/2 := by
      have c : (2:ℚ)*(step y:ℚ)=(y:ℚ) := by exact_mod_cast a
      linarith
    simp only [evenCorrection,e,ite_true,b]
    field_simp
    nlinarith [mul_nonneg (sub_nonneg.mpr yl) yp.le]
  · have a : 2*step y=3*y+1 := by simp [step,e]; omega
    have b : (step y:ℚ)=(3*(y:ℚ)+1)/2 := by
      have c : (2:ℚ)*(step y:ℚ)=3*(y:ℚ)+1 := by exact_mod_cast a
      linarith
    simp only [evenCorrection,e,ite_false,b]
    field_simp
    nlinarith

/-- The sum is over even departures only. Simplicity and the floor refer
to the actual path, including its endpoint. No congruence restriction. -/
theorem even_reciprocal_floor (x L : ℕ)
    (simple : ∀ a≤L, ∀ b≤L, run a x=run b x → a=b)
    (floor : ∀ t≤L, 2^71≤run t x) :
    (∑ t ∈ Finset.range L, evenCorrection (run t x)) < 1/4 := by
  let f := fun t => 1/((run t x:ℚ)+1)
  have b : ∀ t<L, (3999/1000:ℚ)*evenCorrection (run t x) ≤
      1/(run t x:ℚ)+3*(f (t+1)-f t) := by
    intro t ht
    have u := floor t (by omega)
    have h := local_balance (run t x) (by omega)
    have next : run (t+1) x=step (run t x) := by simpa [run] using run_add t 1 x
    simpa only [f,next] using h
  have sums := Finset.sum_le_sum (s:=Finset.range L) (fun t ht => b t (Finset.mem_range.mp ht))
  rw [←Finset.mul_sum,Finset.sum_add_distrib,←Finset.mul_sum,Finset.sum_range_sub] at sums
  have full := reciprocal_floor x L simple floor
  rw [Finset.sum_range_succ] at full
  have pos : (0:ℚ)≤1/(run L x:ℚ) := div_nonneg (by norm_num) (by positivity)
  have start : 0≤f 0 := div_nonneg (by norm_num) (by positivity)
  have finalBound : f L≤1/10000 := by
    have d := floor L le_rfl
    apply div_le_div_of_nonneg_left (by norm_num) (by norm_num)
    have dl : (9999:ℚ)≤(run L x:ℚ) := by exact_mod_cast (by omega : 9999≤run L x)
    linarith
  linarith

#print axioms shell_count
#print axioms geometric_tail
#print axioms reciprocal_floor
#print axioms even_reciprocal_floor
end FloorCertificate
