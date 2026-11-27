import SourceDeletion
import Mathlib.Data.Finset.Max
import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Union

namespace Collatz.OriginalWindow

open Collatz.SourceDeletion

/-- Fixed intercept translations, including large stride-times-offset terms,
do not change the diameter of an inverse fibre. -/
theorem affine_diameter (p u v e x y : Nat)
    (hx : v ≤ p*x + u + e) (hy : p*y+u ≤ v+e) :
    p*(y-x) ≤ 2*e := by
  have key : p*y ≤ p*x + 2*e := by omega
  rw [Nat.mul_sub_left_distrib]
  omega

/-- An actual set of parents in an affine strip, counted in the ordinary
source variable and with no assumption on how they were selected. -/
theorem affine_fibre_card (s : Finset Nat) (p u v e : Nat) (hp : 0 < p)
    (hs : ∀ n ∈ s, v ≤ p*n+u+e ∧ p*n+u ≤ v+e) :
    s.card ≤ 2*e/p + 1 := by
  classical
  by_cases h : s.Nonempty
  · let lo := s.min' h
    have hlo : lo ∈ s := s.min'_mem h
    have hbound (n : Nat) (hn : n ∈ s) : n-lo ≤ 2*e/p := by
      apply (Nat.le_div_iff_mul_le hp).mpr
      rw [Nat.mul_comm]
      exact affine_diameter p u v e lo n (hs lo hlo).1 (hs n hn).2
    have hc := Finset.card_le_card_of_injOn (s := s) (t := Finset.range (2*e/p+1))
      (fun n => n-lo) (by
        intro n hn
        exact Finset.mem_range.mpr (Nat.lt_succ_of_le (hbound n hn))) (by
        intro x hx y hy he
        have h₁ := s.min'_le x hx
        have h₂ := s.min'_le y hy
        change x-lo=y-lo at he
        change lo ≤ x at h₁
        change lo ≤ y at h₂
        omega)
    simpa using hc
  · simp [Finset.not_nonempty_iff_eq_empty.mp h]

/-- The union bound over possible target values with a shared fibre cap. -/
theorem source_union_card (targets : Finset Nat) (parents : Nat → Finset Nat) (cap : Nat)
    (hcap : ∀ z ∈ targets, (parents z).card ≤ cap) :
    (targets.biUnion parents).card ≤ targets.card * cap := by
  induction targets using Finset.induction_on with
  | empty => simp
  | @insert z targets hz ih =>
    rw [Finset.biUnion_insert, Finset.card_insert_of_notMem hz, Nat.add_mul, Nat.one_mul]
    have hu := Finset.card_union_le (parents z) (targets.biUnion parents)
    have hzbound := hcap z (Finset.mem_insert_self z targets)
    have htbound := ih (fun x hx => hcap x (Finset.mem_insert_of_mem hx))
    omega

/-- At a fixed absolute clock the enlarged landing strip is narrower
than a multiplicative factor of three, so the cumulative grade is unique. -/
theorem unique_grade (n lo hi p q : Nat) (hnarrow : hi < 3*lo)
    (hp : lo ≤ 3^p*n) (hP : 3^p*n ≤ hi)
    (hq : lo ≤ 3^q*n) (hQ : 3^q*n ≤ hi) : p=q := by
  have impossible (i j : Nat) (hij : i < j) (hi₁ : lo ≤ 3^i*n)
      (hj₂ : 3^j*n ≤ hi) : False := by
    have hpow : 3^(i+1) ≤ 3^j := Nat.pow_le_pow_right (by decide) hij
    have hmul := Nat.mul_le_mul_right n hpow
    rw [pow_succ, Nat.mul_comm (3^i) 3, Nat.mul_assoc] at hmul
    omega
  rcases lt_trichotomy p q with hlt | heq | hgt
  · exact False.elim (impossible p q hlt hp hQ)
  · exact heq
  · exact False.elim (impossible q p hgt hq hP)

private def prefixSum (f : Nat → Nat) : Nat → Nat
  | 0 => 0
  | i+1 => prefixSum f i + f i

private theorem prefix_split (f : Nat → Nat) (b k : Nat) :
    prefixSum f (b+k) = prefixSum f b + prefixSum (fun i => f (b+i)) k := by
  induction k with
  | zero => simp [prefixSum]
  | succ k ih => simp [prefixSum, ih, Nat.add_assoc]

private theorem prefix_bound (f : Nat → Nat) (k cap : Nat)
    (h : ∀ i < k, f i ≤ cap) : prefixSum f k ≤ k*cap := by
  induction k with
  | zero => simp [prefixSum]
  | succ k ih =>
    have ha := ih (fun i hi => h i (by omega))
    have hb := h k (by omega)
    simp only [prefixSum, Nat.succ_mul]
    omega

private theorem block_sum (f : Nat → Nat) (b k : Nat)
    (half : ∀ i < k, 2*f (b+i) ≤ f i) :
    2*prefixSum (fun i => f (b+i)) k ≤ prefixSum f k := by
  induction k with
  | zero => simp [prefixSum]
  | succ k ih =>
    have ha := ih (fun i hi => half i (by omega))
    have hb := half k (by omega)
    simp only [prefixSum]
    omega

/-- Denominator-cleared bound for accumulated affine corrections at first
passage. Each reversed suffix multiplier is at most the common denominator
and its weight halves across a full contracting block. -/
theorem suffix_budget (f : Nat → Nat) (b h den err : Nat)
    (prefix_cap : ∀ i < h, f i ≤ den)
    (block_half : ∀ i, b+i < h → 2*f (b+i) ≤ f i)
    (affine_sum : 2*err ≤ (List.range h).foldl (fun s i => s+f i) 0) :
    err ≤ b*den := by
  have eq_sum (k : Nat) : (List.range k).foldl (fun s i => s+f i) 0 = prefixSum f k := by
    induction k with
    | zero => rfl
    | succ k ih => simp [List.range_succ, List.foldl_append, ih, prefixSum]
  rw [eq_sum] at affine_sum
  by_cases hb : h ≤ b
  · have hcost := prefix_bound f h den prefix_cap
    have hmul := Nat.mul_le_mul_right den hb
    omega
  · let k := h-b
    have hh : b+k=h := by dsimp [k]; omega
    have base := prefix_bound f b den (fun i hi => prefix_cap i (by omega))
    have half := block_sum f b k (fun i hi => block_half i (by omega))
    have hs := prefix_split f b k
    rw [hh] at hs
    have hmono : prefixSum f k ≤ prefixSum f h := by
      rw [← hh, Nat.add_comm b k, prefix_split f k b]
      omega
    omega

/-- Twice the weight of a possible odd affine impulse, in reverse order,
with common denominator 2^h. Only indices below h are used. -/
def weight : Nat → Nat → Nat → Nat
  | 0, _, _ => 0
  | h+1, x, j => if j<h then 2*weight h (step x) j else 2*3^(odds h (step x))

private def carry : Nat → Nat → Nat
  | 0, _ => 0
  | h+1, x => 2*carry h (step x) + x%2 * 3^(odds h (step x))

private theorem exact_affine (h x : Nat) :
    2^h*run h x = 3^(odds h x)*x+carry h x := by
  induction h generalizing x with
  | zero => simp [run, odds, carry]
  | succ h ih =>
    have one : 2*step x = 3^(x%2)*x+x%2 := by
      by_cases he : x%2=0
      · simp [step, he]; omega
      · have ho : x%2=1 := by omega
        simp [step, ho]; omega
    rw [run, odds, carry, pow_succ, pow_add]
    calc
      2^h * 2 * run h (step x) = 2*(2^h * run h (step x)) := by ring
      _ = 3^(odds h (step x)) * (2*step x)+2*carry h (step x) := by rw [ih]; ring
      _ = _ := by rw [one]; ring

private theorem old_weights (h x k : Nat) (hk : k ≤ h) :
    prefixSum (weight (h+1) x) k = 2*prefixSum (weight h (step x)) k := by
  induction k with
  | zero => simp [prefixSum]
  | succ k ih =>
    have hlt : k<h := by omega
    rw [prefixSum, prefixSum, ih (by omega), Nat.mul_add]
    congr 1
    simp [weight, hlt]

private theorem carry_le_weights (h x : Nat) :
    2*carry h x ≤ prefixSum (weight h x) h := by
  induction h generalizing x with
  | zero => simp [carry, prefixSum]
  | succ h ih =>
    have hi := ih (step x)
    have hp : x%2 ≤ 1 := by omega
    have hm := Nat.mul_le_mul_right (3^(odds h (step x))) hp
    simp only [Nat.one_mul] at hm
    rw [prefixSum, old_weights h x h (le_refl h),
      show weight (h+1) x h = 2*3^(odds h (step x)) by simp [weight], carry]
    omega

/-- The actual shortcut ordinate, rather than a free additive error,
satisfies the integer first-passage budget when its suffix weights obey
the two deterministic bounds. -/
theorem landing_carry (b h x : Nat)
    (hcap : ∀ i < h, weight h x i ≤ 2^h)
    (half : ∀ i, b+i < h → 2*weight h x (b+i) ≤ weight h x i) :
    2^h*run h x ≤ 3^(odds h x)*x+b*2^h := by
  have he := carry_le_weights h x
  have hl (k : Nat) :
      (List.range k).foldl (fun s i => s+weight h x i) 0 = prefixSum (weight h x) k := by
    induction k with
    | zero => rfl
    | succ k ih => simp [List.range_succ, List.foldl_append, ih, prefixSum]
  have hc := suffix_budget (weight h x) b h (2^h) (carry h x) hcap half (by rwa [hl])
  rw [exact_affine]
  omega

private theorem run_add (i j x : Nat) : run (i+j) x = run j (run i x) := by
  induction i generalizing x with
  | zero => simp [run]
  | succ i ih => simpa [Nat.succ_add, run] using ih (step x)

private theorem odds_add (i j x : Nat) : odds (i+j) x = odds i x + odds j (run i x) := by
  induction i generalizing x with
  | zero => simp [run, odds]
  | succ i ih => rw [Nat.succ_add]; simp only [odds, run, ih]; omega

private theorem weight_eq (h x j : Nat) (hj : j<h) :
    weight h x j = 2^(h-j)*3^(odds j (run (h-j) x)) := by
  induction h generalizing x j with
  | zero => omega
  | succ h ih =>
    by_cases hj' : j<h
    · rw [show h+1-j=(h-j)+1 by omega, pow_succ, run]
      rw [show weight (h+1) x j = 2*weight h (step x) j by simp [weight, hj'], ih (step x) j hj']
      ring
    · have je : j=h := by omega
      subst j
      simp [weight, run]

/-- A positive record landing with contracting full blocks has additive
affine error at most one block length at its actual clock. -/
theorem record_landing_carry (b h x : Nat)
    (record : ∀ i ≤ h, 0 < run i x ∧ run h x ≤ run i x)
    (blocks : ∀ i, i+b ≤ h → 2*3^(odds b (run i x)) ≤ 2^b) :
    2^h*run h x ≤ 3^(odds h x)*x+b*2^h := by
  apply landing_carry
  · intro j hj
    let v := run (h-j) x
    have hv := record (h-j) (by omega)
    have endeq : run j v = run h x := by
      dsimp [v]; rw [← run_add, show h-j+j=h by omega]
    have ha := exact_affine j v
    rw [endeq] at ha
    have hm : 3^(odds j v)*v ≤ 2^j*v := by
      calc
        _ ≤ 2^j*run h x := by omega
        _ ≤ _ := Nat.mul_le_mul_left _ hv.2
    have hh : 3^(odds j v) ≤ 2^j := Nat.le_of_mul_le_mul_right hm hv.1
    rw [weight_eq h x j hj, ← show (h-j)+j=h by omega, pow_add]
    simpa only [Nat.add_sub_cancel] using Nat.mul_le_mul_left (2^(h-j)) hh
  · intro j hj
    let u := h-(b+j)
    have et : u+b=h-j := by dsimp [u]; omega
    have ball := blocks u (by dsimp [u]; omega)
    rw [weight_eq h x (b+j) hj, weight_eq h x j (by omega), odds_add, pow_add]
    change 2*(2^u*(3^(odds b (run u x))*3^(odds j (run b (run u x))))) ≤ _
    rw [← run_add, ← et, pow_add]
    calc
      _ = (2^u*3^(odds j (run (u+b) x))) * (2*3^(odds b (run u x))) := by ring
      _ ≤ (2^u*3^(odds j (run (u+b) x))) * 2^b := Nat.mul_le_mul_left _ ball
      _ = _ := by ring

def Meet (h x y : Nat) : Prop :=
  ∃ i ≤ h, ∃ j ≤ h, run i x = run j y

/-- A certified meeting of two landing gates lifts to their source sites. -/
theorem lift_gate_meet (h l a b x y : Nat) (ha : a ≤ l) (hb : b ≤ l)
    (hm : Meet h (run a x) (run b y)) : Meet (h+l) x y := by
  obtain ⟨i,hi,j,hj,he⟩ := hm
  exact ⟨a+i, by omega, b+j, by omega, by simpa [run_add] using he⟩

/-- A meeting of the sources remains detectable at their possibly different
landing times. The two arms use the same continuation after their meeting. -/
theorem descend_source_meet (h l a b x y : Nat) (ha : a ≤ l) (hb : b ≤ l)
    (hm : Meet h x y) : Meet (h+l) (run a x) (run b y) := by
  obtain ⟨i,hi,j,hj,he⟩ := hm
  let k := max (a-i) (b-j)
  have hk : k ≤ l := by dsimp [k]; omega
  have h₁ : a ≤ i+k := by dsimp [k]; omega
  have h₂ : b ≤ j+k := by dsimp [k]; omega
  refine ⟨i+k-a, by omega, j+k-b, by omega, ?_⟩
  rw [← run_add, ← run_add, show a+(i+k-a)=i+k by omega,
    show b+(j+k-b)=j+k by omega, run_add i k, run_add j k, he]

private theorem double_color (f : Nat → Nat) (inv : ∀ n, f (step n)=f n)
    (x : Nat) : f (2*x)=f x := by
  rw [← inv (2*x)]
  simp [step]

private theorem odd_color (f : Nat → Nat) (inv : ∀ n, f (step n)=f n)
    (x : Nat) (ho : x%2=1) : f (3*x+1)=f x := by
  have e : 3*x+1=2*((3*x+1)/2) := by omega
  calc
    f (3*x+1) = f (2*((3*x+1)/2)) := congrArg f e
    _ = f ((3*x+1)/2) := double_color f inv _
    _ = f x := by simpa [step, ho] using inv x

/-- If local adjacent comparisons around x and 3x all agree, tripling
also preserves the color, on both parities of x. -/
theorem tripling_via_adjacent (f : Nat → Nat) (inv : ∀ n, f (step n)=f n)
    (x : Nat) (low : f (x+1)=f x) (high : ∀ i ≤ 4, f (3*x+i)=f (3*x)) :
    f (3*x)=f x := by
  by_cases ho : x%2=1
  · exact (high 1 (by decide)).symm.trans (odd_color f inv x ho)
  · have hu := odd_color f inv (x+1) (by omega)
    rw [show 3*(x+1)+1=3*x+4 by omega] at hu
    exact (high 4 (by decide)).symm.trans (hu.trans low)

/-- An adjacent color split produces a literal four-trit edge at the
current level or persists precisely across a base-81 column boundary. -/
theorem head_or_boundary (f : Nat → Nat) (x : Nat) (split : f x ≠ f (x+1)) :
    f x ≠ f (x/81) ∨ f (x+1) ≠ f ((x+1)/81) ∨
      ((x+1)%81=0 ∧ f (x/81) ≠ f (x/81+1)) := by
  by_cases hl : f x = f (x/81)
  · by_cases hu : f (x+1) = f ((x+1)/81)
    · right; right
      have ne : x/81 ≠ (x+1)/81 := by
        intro he
        exact split (hl.trans ((congrArg f he).trans hu.symm))
      have hd : (x+1)/81=x/81+1 := by omega
      exact ⟨by omega, by simpa [hl, hu, hd] using split⟩
    · exact Or.inr (Or.inl hu)
  · exact Or.inl hl

#print axioms affine_diameter
#print axioms affine_fibre_card
#print axioms source_union_card
#print axioms unique_grade
#print axioms suffix_budget
#print axioms landing_carry
#print axioms record_landing_carry
#print axioms lift_gate_meet
#print axioms descend_source_meet
#print axioms tripling_via_adjacent
#print axioms head_or_boundary

end Collatz.OriginalWindow
