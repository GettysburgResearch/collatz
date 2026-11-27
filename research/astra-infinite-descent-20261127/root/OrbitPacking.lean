import BinaryCylinder
import FirstArrival
import Mathlib.Order.Interval.Finset.Nat

/-! Elementary finite packing of an actual simple shortcut path.
The proof uses the exact binary grade moment and injectivity of forward
images away from the final finite clock. No density or trace input occurs. -/
set_option autoImplicit false
set_option warningAsError true

namespace OrbitPacking
open CoreBranching PeakRigidity
open scoped BigOperators

private theorem runs (h n : ℕ) : CoreBranching.run h n=Collatz.TwoGapRouting.run h n := by
  induction h generalizing n with
  | zero => rfl
  | succ h ih => exact ih (step n)

private theorem grades (h n : ℕ) : grade h n=Collatz.TwoGapRouting.odds h n := by
  induction h with
  | zero => rfl
  | succ h ih =>
    change grade h n+CoreBranching.run h n%2=Collatz.TwoGapRouting.odds (h+1) n
    rw [ih,runs,(Collatz.TwoGapRouting.append h 1 n).2]
    simp [Collatz.TwoGapRouting.odds]

/-- A finite Chernoff bound, obtained from the exact positive grade moment. -/
theorem grade_tail_card (h a : ℕ) :
    ((Finset.range (2^h)).filter (fun x => a≤grade h x)).card*2^a≤3^h := by
  let S := (Finset.range (2^h)).filter (fun x => a≤grade h x)
  calc
    S.card*2^a = ∑ _x ∈ S, 2^a := by simp
    _ ≤ ∑ x ∈ S, 2^(grade h x) := by
      apply Finset.sum_le_sum
      intro x hx
      exact Nat.pow_le_pow_right (by decide) (Finset.mem_filter.mp hx).2
    _ ≤ ∑ x ∈ Finset.range (2^h), 2^(grade h x) :=
      Finset.sum_le_sum_of_subset_of_nonneg (Finset.filter_subset _ _) (by intros; positivity)
    _ = 3^h := BinaryCylinder.grade_power_sum h

private theorem low_image {h a x : ℕ} (hx : x<2^h) (hg : grade h x≤a) :
    run h x<2*3^a := by
  have upper := Collatz.FirstArrival.affine_upper h x
  rw [←runs,←grades] at upper
  have pow : 3^(grade h x)≤3^a := Nat.pow_le_pow_right (by decide) hg
  have strict : 2^h*run h x<2^h*(2*3^a) := by
    calc
      2^h*run h x ≤ 3^(grade h x)*(x+2^h) := upper
      _ < 3^(grade h x)*(2^h+2^h) :=
        Nat.mul_lt_mul_of_pos_left (Nat.add_lt_add_right hx _) (by positivity)
      _ ≤ 3^a*(2^h+2^h) := Nat.mul_le_mul_right _ pow
      _ = 2^h*(2*3^a) := by ring
  exact Nat.lt_of_mul_lt_mul_left strict

/-- A collection inside one binary interval whose forward images are
all distinct has a small cardinality, after the high-grade tail is paid. -/
theorem injective_card (S : Finset ℕ) (h a : ℕ)
    (bounded : ∀x∈S, x<2^h)
    (inj : Set.InjOn (run h) (S : Set ℕ)) :
    S.card*2^a≤(2*3^a)*2^a+3^h := by
  classical
  let lo := S.filter (fun x => grade h x<a)
  let hi := S.filter (fun x => a≤grade h x)
  have parts : lo.card+hi.card=S.card := by
    simpa only [lo,hi,not_lt] using
      (Finset.card_filter_add_card_filter_not (s:=S) (fun x => grade h x<a))
  have linj : Set.InjOn (run h) (lo : Set ℕ) := by
    intro x hx y hy eq
    exact inj (Finset.mem_filter.mp hx).1 (Finset.mem_filter.mp hy).1 eq
  have lc : lo.card≤2*3^a := by
    calc
      lo.card = (lo.image (run h)).card := (Finset.card_image_of_injOn linj).symm
      _ ≤ (Finset.range (2*3^a)).card := by
        apply Finset.card_le_card
        intro y hy
        obtain ⟨x,hx,rfl⟩ := Finset.mem_image.mp hy
        obtain ⟨xs,xg⟩ := Finset.mem_filter.mp hx
        exact Finset.mem_range.mpr (low_image (bounded x xs) xg.le)
      _ = 2*3^a := Finset.card_range _
  have hc : hi.card*2^a≤3^h := by
    have sub : hi⊆(Finset.range (2^h)).filter (fun x => a≤grade h x) := by
      intro x hx
      obtain ⟨xs,xg⟩ := Finset.mem_filter.mp hx
      exact Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (bounded x xs),xg⟩
    exact (Nat.mul_le_mul_right (2^a) (Finset.card_le_card sub)).trans (grade_tail_card h a)
  have lm := Nat.mul_le_mul_right (2^a) lc
  rw [←parts,Nat.add_mul]
  exact Nat.add_le_add lm hc

/-- Count the actual visited states below a binary cutoff. The final h
positions are discarded before applying forward injectivity; no claim
of injectivity after a possible later cycle is used. -/
theorem simple_prefix_card (n L h a : ℕ)
    (simple : ∀ i≤L, ∀ j≤L, run i n=run j n → i=j) :
    ((Finset.range (L+1)).filter (fun i => run i n<2^h)).card*2^a≤
      (h+2*3^a)*2^a+3^h := by
  classical
  let S := (Finset.range (L+1)).filter (fun i => run i n<2^h)
  let J := S.filter (fun i => i+h≤L)
  let tail := S.filter (fun i => ¬i+h≤L)
  have parts : J.card+tail.card=S.card :=
    Finset.card_filter_add_card_filter_not (s:=S) (fun i => i+h≤L)
  have sub : tail⊆Finset.Icc (L+1-h) L := by
    intro i hi
    obtain ⟨is,late⟩ := Finset.mem_filter.mp hi
    have il := Finset.mem_range.mp (Finset.mem_filter.mp is).1
    exact Finset.mem_Icc.mpr ⟨by omega,by omega⟩
  have tc : tail.card≤h := by
    have b := Finset.card_le_card sub
    rw [Nat.card_Icc] at b
    omega
  let A := J.image (fun i => run i n)
  have member {i : ℕ} (hi : i∈J) : i≤L ∧ run i n<2^h ∧ i+h≤L := by
    obtain ⟨is,clock⟩ := Finset.mem_filter.mp hi
    obtain ⟨ir,small⟩ := Finset.mem_filter.mp is
    have il := Finset.mem_range.mp ir
    exact ⟨by omega,small,clock⟩
  have ac : A.card=J.card := by
    apply Finset.card_image_of_injOn
    intro i hi j hj eq
    exact simple i (member hi).1 j (member hj).1 eq
  have bound : ∀x∈A, x<2^h := by
    intro x hx
    obtain ⟨i,hi,rfl⟩ := Finset.mem_image.mp hx
    exact (member hi).2.1
  have ainj : Set.InjOn (run h) (A : Set ℕ) := by
    intro x hx y hy eq
    obtain ⟨i,hi,rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨j,hj,rfl⟩ := Finset.mem_image.mp hy
    have shifted : run (i+h) n=run (j+h) n := by simpa only [run_add] using eq
    have ij := simple (i+h) (member hi).2.2 (j+h) (member hj).2.2 shifted
    have ij' : i=j := by omega
    rw [ij']
  have packed := injective_card A h a bound ainj
  rw [ac] at packed
  have tm := Nat.mul_le_mul_right (2^a) tc
  change S.card*2^a≤(h+2*3^a)*2^a+3^h
  rw [←parts,Nat.add_mul]
  calc
    J.card*2^a+tail.card*2^a ≤ (2*3^a*2^a+3^h)+h*2^a := Nat.add_le_add packed tm
    _ = (h+2*3^a)*2^a+3^h := by ring

private theorem thirteen_le (k : ℕ) : 13*k≤3^(8*k) := by
  induction k with
  | zero => norm_num
  | succ k ih =>
    rw [Nat.mul_succ,Nat.mul_succ,pow_add]
    norm_num
    have positive : 0<(3:ℕ)^(8*k) := by positivity
    omega

/-- Exact geometric packing at the 8192-adic cutoffs. Both bases and
constants are integers, for direct use in a summable reciprocal-tail proof. -/
theorem simple_block_card (n L k : ℕ)
    (simple : ∀ i≤L, ∀ j≤L, run i n=run j n → i=j) :
    ((Finset.range (L+1)).filter (fun i => run i n<8192^k)).card≤4*6561^k := by
  have bound := simple_prefix_card n L (13*k) (8*k) simple
  have powers : (3:ℕ)^(13*k)≤3^(8*k)*2^(8*k) := by
    have base : (3:ℕ)^5≤2^8 := by norm_num
    have grown := pow_le_pow_left' base k
    simp only [←pow_mul] at grown
    calc
      (3:ℕ)^(13*k) = 3^(8*k)*3^(5*k) := by rw [←pow_add]; congr 1; omega
      _ ≤ 3^(8*k)*2^(8*k) := Nat.mul_le_mul_left _ grown
  have hsmall := thirteen_le k
  have packed : ((Finset.range (L+1)).filter (fun i => run i n<2^(13*k))).card≤
      4*3^(8*k) := by
    have pos : 0<(2:ℕ)^(8*k) := by positivity
    apply Nat.le_of_mul_le_mul_right (hc:=pos)
    nlinarith only [bound,powers,Nat.mul_le_mul_right (2^(8*k)) hsmall]
  simpa only [pow_mul,show (2:ℕ)^13=8192 by norm_num,
    show (3:ℕ)^8=6561 by norm_num] using packed

#print axioms grade_tail_card
#print axioms injective_card
#print axioms simple_prefix_card
#print axioms simple_block_card
end OrbitPacking
