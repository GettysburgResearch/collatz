import RankTwoControl
import MinimumFailure
import Mathlib.Tactic.IntervalCases

/-! The upper certificate always belongs to the same ordinary reverse
disagreement. Lexicographic payment counts its even departures first. -/
namespace Collatz.EvenMinimum
open Collatz.SourceDeletion Collatz.MinimumFailure Collatz.RankTwoControl

set_option maxHeartbeats 1500000

def First (H n : Nat) : Prop :=
  run H n=1 ∧ ∀ t, t<H → run t n≠1

def ReverseAt (x H : Nat) : Prop := 0<x ∧ ¬Good x ∧ First H (3*x)

def evenCount (H n : Nat) : Nat := H-odds H n

theorem odds_le_clock (H n : Nat) : odds H n≤H := by
  induction H generalizing n with
  | zero => rfl
  | succ H ih =>
    simpa only [odds] using (show odds H (step n)+n%2≤H+1 by
      have := ih (step n); omega)

/-- A true minimum simultaneously attains both coordinates. -/
theorem exists_minimum (someRev : ∃ x H, ReverseAt x H) :
    ∃ x H, ReverseAt x H ∧ ∀ y K, ReverseAt y K →
      evenCount H (3*x)≤evenCount K (3*y) ∧
      (evenCount H (3*x)=evenCount K (3*y) → x≤y) := by
  classical
  have e : ∃ E, ∃ x H, ReverseAt x H ∧ evenCount H (3*x)=E := by
    obtain ⟨x,H,h⟩ := someRev
    exact ⟨_,x,H,h,rfl⟩
  have m : ∃ x, ∃ H, ReverseAt x H ∧ evenCount H (3*x)=Nat.find e := Nat.find_spec e
  obtain ⟨H,hx,eq⟩:=Nat.find_spec m
  refine ⟨Nat.find m,H,hx,?_⟩
  intro y K hy
  refine ⟨?_,?_⟩
  · rw [eq]
    exact Nat.find_min' e ⟨y,K,hy,rfl⟩
  intro tie
  exact Nat.find_min' m ⟨K,hy,tie.symm.trans eq⟩

/-- Along every ordinary prefix the affine correction is nonnegative. -/
theorem lower_product (H n : Nat) : 3^(odds H n)*n≤2^H*run H n := by
  induction H generalizing n with
  | zero => simp [run,odds]
  | succ H ih =>
    have edge : 3^(n%2)*n≤2*step n := by
      unfold step
      split
      · rename_i hn; rw [hn,pow_zero]; omega
      · have hn : n%2=1 := by omega
        rw [hn,pow_one]; omega
    simp only [odds,run,pow_add,pow_succ]
    calc
      _ = 3^(odds H (step n))*(3^(n%2)*n) := by ring
      _ ≤ 3^(odds H (step n))*(2*step n) := Nat.mul_le_mul_left _ edge
      _ = 2*(3^(odds H (step n))*step n) := by ring
      _ ≤ 2*(2^H*run H (step n)) := Nat.mul_le_mul_left _ (ih _)
      _ = _ := by ring

/-- Every odd input before the first hit at one is at least three. -/
theorem upper_product (H n : Nat) (pos : 0<n) (noOne : ∀ t, t<H → run t n≠1) :
    3^(odds H n)*(2^H*run H n)≤10^(odds H n)*n := by
  induction H generalizing n with
  | zero => simp [run,odds]
  | succ H ih =>
    have ne : n≠1 := noOne 0 (by omega)
    have stepPos : 0<step n := by unfold step; split <;> omega
    have later (t : Nat) (ht : t<H) : run t (step n)≠1 := noOne (t+1) (by omega)
    have edge : 3^(n%2)*(2*step n)≤10^(n%2)*n := by
      unfold step
      split
      · rename_i hn; rw [hn]; simp;omega
      · have hn : n%2=1 := by omega
        rw [hn,pow_one,pow_one];omega
    have tail := ih (step n) stepPos later
    simp only [odds,run,pow_add,pow_succ]
    calc
      _ = (3^(n%2)*2)*(3^(odds H (step n))*(2^H*run H (step n))) := by ring
      _ ≤ (3^(n%2)*2)*(10^(odds H (step n))*step n) := Nat.mul_le_mul_left _ tail
      _ = 10^(odds H (step n))*(3^(n%2)*(2*step n)) := by ring
      _ ≤ 10^(odds H (step n))*(10^(n%2)*n) := Nat.mul_le_mul_left _ edge
      _ = _ := by ring

theorem finite_sublevel (H x E : Nat) (hit : run H (3*x)=1)
    (score : evenCount H (3*x)≤E) : 3*x≤2^E := by
  let p := odds H (3*x)
  have le : p≤H := odds_le_clock _ _
  have hh : H=(H-p)+p := by omega
  have eqn : 2^H=2^(H-p)*2^p := by rw [←pow_add,←hh]
  have lower := lower_product H (3*x)
  change 3^p*(3*x)≤2^H*run H (3*x) at lower
  rw [hit,Nat.mul_one,eqn] at lower
  have small : (2:Nat)^p≤3^p := Nat.pow_le_pow_left (by decide) _
  have lf : (3*x)*2^p≤3^p*(3*x) := by
    rw [Nat.mul_comm (3*x)]
    exact Nat.mul_le_mul_right _ small
  have cmp := lf.trans lower
  exact (Nat.le_of_mul_le_mul_right cmp (Nat.two_pow_pos _)).trans
    (Nat.pow_le_pow_right (by decide) score)

/-- The upper rank of every such physical source is at most six. -/
theorem floor_sparse (j H x : Nat) (hit : run H (3*x)=1)
    (cost : evenCount H (3*x)≤j+4) (floor : 3*2^j≤8*x) :
    odds H (3*x)≤6 := by
  let p:=odds H (3*x)
  have le : p≤H := odds_le_clock _ _
  have hclock : H≤j+4+p := by unfold evenCount at cost;dsimp [p] at *;omega
  have lower := lower_product H (3*x)
  change 3^p*(3*x)≤2^H*run H (3*x) at lower
  rw [hit,Nat.mul_one] at lower
  have hp := Nat.pow_le_pow_right (by decide : 0<(2:Nat)) hclock
  rw [pow_add,pow_add] at hp
  have bound : 2^j*(9*3^p)≤2^j*(128*2^p) := by
    have lf := Nat.mul_le_mul_left (3*3^p) floor
    nlinarith only [lf, lower, hp]
  have can := Nat.le_of_mul_le_mul_left bound (Nat.two_pow_pos j)
  change p≤6
  by_contra! high
  obtain ⟨k,hk⟩:=Nat.exists_eq_add_of_le (show 7≤p by omega)
  rw [hk,pow_add,pow_add] at can
  have ratio : (2:Nat)^k≤3^k := Nat.pow_le_pow_left (by decide) _
  have pos := Nat.two_pow_pos k
  norm_num at can
  omega

theorem d_four_high (j x H : Nat) (first : First H (3*x)) (pos : 0<x)
    (cost : evenCount H (3*x)=j+4) (tieHeight : 243*x≤256*2^j) :
    4≤odds H (3*x) := by
  let p:=odds H (3*x)
  have le : p≤H := odds_le_clock _ _
  have hh : H=(j+4)+p := by unfold evenCount at cost;dsimp [p] at *;omega
  have bound := upper_product H (3*x) (by omega) first.2
  change 3^p*(2^H*run H (3*x))≤10^p*(3*x) at bound
  rw [first.1,Nat.mul_one,hh,pow_add,pow_add] at bound
  change 4≤p
  by_contra! small
  interval_cases p <;> norm_num at bound <;> have := Nat.two_pow_pos j <;> omega

theorem sparse_rows (d p : Nat) (dmax : d≤4) (pmax : p≤6)
    (pmin : 0<p) (budget : 9*3^p≤8*2^d*2^p)
    (high : d=4 → 4≤p) :
    (d=1 ∧ p=1) ∨ (d=2 ∧ p≤3) ∨ (d=3 ∧ p≤4) ∨ (d=4 ∧ 4≤p) := by
  interval_cases d <;> interval_cases p <;> norm_num at *

/-- The two legitimate 16-clock physical prefixes overlap across all lifts. -/
theorem long_second_drop (x N : Nat) (_large : 2048≤N) (cap : 27*x≤32*N)
    (div : 65536∣9*x+1) : 8*run 16 x<3*N := by
  obtain ⟨k,hk⟩:=div
  have src : x=29127+65536*(x/65536) := by omega
  have h:=lift 16 29127 (x/65536)
  change run 16 (29127+65536*(x/65536))=8749+19683*(x/65536) at h
  conv_lhs => rw [src,h]
  omega

theorem short_two_drop (x N : Nat) (large : 2048≤N) (cap : 27*x≤32*N)
    (div : 65536∣27*x+7) : 8*run 16 x<3*N := by
  obtain ⟨k,hk⟩:=div
  have src : x=2427+65536*(x/65536) := by omega
  have h:=lift 16 2427 (x/65536)
  change run 16 (2427+65536*(x/65536))=730+19683*(x/65536) at h
  conv_lhs => rw [src,h]
  omega

#print axioms exists_minimum
#print axioms lower_product
#print axioms upper_product
#print axioms finite_sublevel
#print axioms floor_sparse
#print axioms d_four_high
#print axioms sparse_rows
#print axioms long_second_drop
#print axioms short_two_drop
end Collatz.EvenMinimum
