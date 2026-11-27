module

public import PassageGatePacking
import all PassageGatePacking
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.PassageGate

open Finset
set_option autoImplicit false

private theorem binomial_moment (h : ℕ) :
    (∑ d ∈ range (h+1), h.choose d*2^d)=3^h := by
  have eqn := add_pow (2:ℕ) 1 h
  simpa only [one_pow,mul_one,Nat.reduceAdd,Nat.cast_id,Nat.mul_comm] using eqn.symm

private theorem block_tail {h k : ℕ} (lo : 8*k<h) (hi : h≤8*(k+1)) :
    tail h (cutoff (h-1))≤6561*206^k := by
  have mark : 5*k≤Nat.log 3 (2^(h-1)) := by
    apply Nat.le_log_of_pow_le (by decide)
    calc
      3^(5*k)=(3^5)^k := pow_mul ..
      _ ≤ (2^8)^k := Nat.pow_le_pow_left (by decide) k
      _ = 2^(8*k) := (pow_mul ..).symm
      _ ≤ 2^(h-1) := Nat.pow_le_pow_right (by decide) (by omega)
  have bound : 2^(5*k)*tail h (cutoff (h-1))≤3^h := by
    rw [tail,mul_sum,←binomial_moment]
    calc
      _ ≤ ∑ d ∈ Icc (cutoff (h-1)) h, h.choose d*2^d := by
        apply sum_le_sum
        intro d hd
        have kd := (mem_Icc.mp hd).1
        unfold cutoff at kd
        rw [Nat.mul_comm (2^(5*k))]
        exact Nat.mul_le_mul_left _ (Nat.pow_le_pow_right (by decide) (by omega))
      _ ≤ _ := by
        apply sum_le_sum_of_subset_of_nonneg
        · intro d hd
          exact mem_range.mpr (by have := (mem_Icc.mp hd).2; omega)
        · intro _ _ _
          omega
  have cap : 3^h≤2^(5*k)*(6561*206^k) := by
    calc
      3^h ≤ 3^(8*(k+1)) := Nat.pow_le_pow_right (by decide) hi
      _ = (3^8)^k*6561 := by rw [pow_mul,pow_succ]; norm_num
      _ ≤ (2^5*206)^k*6561 := Nat.mul_le_mul_right 6561 (Nat.pow_le_pow_left (by decide) k)
      _ = 2^(5*k)*(6561*206^k) := by rw [mul_pow,pow_mul]; ring
  exact Nat.le_of_mul_le_mul_left (bound.trans cap) (Nat.two_pow_pos _)

/-- A fully numerical, sublinear simple-orbit packing bound at every
dyadic scale with exponent divisible by eight. -/
theorem explicit_budget (k : ℕ) : budget (8*k)≤300*206^k := by
  induction k with
  | zero => decide
  | succ k ih =>
    have inc (j : ℕ) (cap : j≤8) :
        budget (8*k+j) ≤ budget (8*k)+j*(8*(k+1)+6561*206^k) := by
      induction j with
      | zero => simp
      | succ j prev =>
        have term := block_tail (h:=8*k+(j+1)) (k:=k) (by omega) (by omega)
        have prev' := prev (by omega)
        rw [Nat.add_succ,budget,Nat.succ_mul j]
        rw [show 8*k+(j+1)-1=8*k+j by omega] at term
        rw [←Nat.add_assoc] at term
        omega
    have e := inc 8 (by decide)
    have small : k+1≤206^k := (Nat.lt_two_pow_self (n:=k)).trans_le
      (Nat.pow_le_pow_left (by decide) k)
    rw [Nat.mul_succ,pow_succ]
    omega

theorem explicit_simple_visits {x n : ℕ} (k : ℕ) (positive : 0<x)
    (simple : (Set.Iio n).InjOn (fun i => run i x)) :
    (visitSet x n (8*k)).card≤300*206^k :=
  (simple_visits x n (8*k) positive simple).trans (explicit_budget k)

/-- The prescribed fixed ordinary nonrepeating orbit has exceeded
256^k by the specified native date. -/
theorem explicit_escape_exit {x : ℕ} (k : ℕ) (positive : 0<x)
    (injective : Function.Injective (fun i => run i x)) :
    ∃ i≤300*206^k, 256^k<run i x := by
  obtain ⟨i,early,high⟩ := escape_exits_by_budget x (8*k) positive injective
  exact ⟨i,early.trans (explicit_budget k),by simpa only [pow_mul,show (2:ℕ)^8=256 by decide] using high⟩

/-- Count any positive forward-invariant set on which each native clock
is injective. In particular this counts all periodic points together. -/
theorem invariant_visits (S : Set ℕ)
    (forward : ∀ h x, x∈S → run h x∈S)
    (injective : ∀ h, Set.InjOn (run h) S) (h : ℕ) : (sites S h).card≤budget h := by
  classical
  induction h with
  | zero =>
    apply card_le_one.mpr
    intro x hx y hy
    obtain ⟨xp,xl,_⟩ := in_sites.mp hx
    obtain ⟨yp,yl,_⟩ := in_sites.mp hy
    simp only [pow_zero] at xl yl
    omega
  | succ h ih =>
    have one (y : ℕ) : ((sites S (h+1)).filter (fun x => run (h+1) x=y)).card≤1 := by
      apply card_le_one.mpr
      intro x hx z hz
      obtain ⟨xs,ex⟩ := mem_filter.mp hx
      obtain ⟨zs,ez⟩ := mem_filter.mp hz
      exact injective (h+1) (in_sites.mp xs).2.2 (in_sites.mp zs).2.2 (ex.trans ez.symm)
    have le := packet_bound S (h+1) h 1 (forward _) one
    simp only [one_mul] at le
    change (sites S (h+1)).card≤tail (h+1) (cutoff h)+(sites S h).card at le
    rw [budget]
    omega

def periodicSite (x : ℕ) : Prop := ∃ p, 0<p ∧ run p x=x

private theorem multiply_period {x p : ℕ} (ret : run p x=x) (j : ℕ) : run (p*j) x=x := by
  induction j with
  | zero => simp [run]
  | succ j ih => rw [Nat.mul_succ,run_add,ih,ret]

private theorem periodic_forward (h x : ℕ) (px : periodicSite x) : periodicSite (run h x) := by
  obtain ⟨p,pos,ret⟩ := px
  refine ⟨p,pos,?_⟩
  rw [←run_add,Nat.add_comm,run_add,ret]

private theorem periodic_injective (h : ℕ) : Set.InjOn (run h) {x | periodicSite x} := by
  intro x px y py eqn
  obtain ⟨p,pp,xp⟩ := px
  obtain ⟨q,qp,yq⟩ := py
  let L := p*q*(h+1)
  have size : h≤L := by
    have lb := Nat.le_mul_of_pos_left (h+1) (Nat.mul_pos pp qp)
    dsimp only [L]
    omega
  have xr : run L x=x := by
    simpa only [L,Nat.mul_assoc] using multiply_period xp (q*(h+1))
  have yr : run L y=y := by
    simpa only [L,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using multiply_period yq (p*(h+1))
  have endEq := congrArg (run (L-h)) eqn
  rwa [←run_add,←run_add,Nat.add_sub_of_le size,xr,yr] at endEq

/-- The union of all positive periodic sites, across all possible
primitive cycles, obeys one common sublinear count. -/
theorem all_periodic_sites (k : ℕ) :
    (sites {x | periodicSite x} (8*k)).card≤300*206^k :=
  (invariant_visits {x | periodicSite x} periodic_forward periodic_injective (8*k)).trans
    (explicit_budget k)

#print axioms all_periodic_sites
#print axioms explicit_budget
#print axioms explicit_simple_visits
#print axioms explicit_escape_exit
end Collatz.Itinerary.PassageGate
