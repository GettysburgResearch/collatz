import FrozenOffset
import ClockSeparation
import Mathlib.Tactic.LinearCombination

/-! A fixed signed carry turns the finite odd-count scan into an arbitrary-clock
exclusion for actual ordinary Mersenne peaks. This does not exclude an input
whose later carry changes, or an unequal-clock merger without paid grades. -/
namespace Collatz.FrozenPeakSeparation
open Collatz.SourceDeletion Collatz.RankTwoControl Collatz.FrozenOffset
open Collatz.SignedBudget Collatz.ShadowBarrier Collatz.PhysicalWindow

set_option maxRecDepth 30000
set_option maxHeartbeats 8000000
set_option exponentiation.threshold 4000

def signedCarry (h x : Nat) : Int :=
  (2:Int)^h*(run h x:Int) - (3:Int)^(odds h x)*((x:Int)+1)

private theorem odds_succ (h x : Nat) :
    odds (h+1) x=odds h x+(run h x)%2 := by
  simpa [odds] using (append h 1 x).2

private theorem run_succ (h x : Nat) : run (h+1) x=step (run h x) := by
  simpa [run] using (append h 1 x).1

theorem carry_succ (h x : Nat) :
    signedCarry (h+1) x =
      if (run h x)%2=0 then signedCarry h x else 3*signedCarry h x+2^h := by
  rw [signedCarry,run_succ,odds_succ]
  by_cases ev : (run h x)%2=0
  · have eqn : (2:Int)*(step (run h x):Int)=(run h x:Int) := by
      simp only [step,ev,ite_true]
      omega
    simp only [ev,ite_true,Nat.add_zero,pow_succ]
    unfold signedCarry
    linear_combination (2:Int)^h*eqn
  · have od : (run h x)%2=1 := by omega
    have eqn : (2:Int)*(step (run h x):Int)=3*(run h x:Int)+1 := by
      simp only [step,ev,ite_false]
      omega
    simp only [od,show ¬(1:Nat)=0 by decide,ite_false,pow_succ]
    unfold signedCarry
    linear_combination (2:Int)^h*eqn

private theorem initial_even (x : Nat) (ev : x%2=0) : signedCarry 1 x=-1 := by
  rw [carry_succ]
  simp [run,ev,signedCarry,odds]

theorem carry_lower (x h : Nat) (ev : x%2=0) (hp : 1≤h) : -1≤signedCarry h x := by
  induction h, hp using Nat.le_induction with
  | base => rw [initial_even x ev]
  | succ h hp ih =>
    rw [carry_succ]
    split
    · exact ih
    · have pow : (2:Int)≤(2:Int)^h := by
        exact_mod_cast (show (2:Nat)^1≤2^h from Nat.pow_le_pow_right (by decide) hp)
      omega

theorem carry_monotone (x i j : Nat) (ev : x%2=0) (ip : 1≤i) (le : i≤j) :
    signedCarry i x≤signedCarry j x := by
  induction j, le using Nat.le_induction with
  | base => rfl
  | succ j hj ih =>
    have low:=carry_lower x j ev (by omega)
    have pow : (2:Int)≤(2:Int)^j := by
      exact_mod_cast (show (2:Nat)^1≤2^j from Nat.pow_le_pow_right (by decide) (by omega))
    rw [carry_succ]
    split <;> omega

/-- Once the final carry is below `2^K-3`, every departure after position `K`
is even, regardless of the total clock. -/
theorem no_late_odds (x H K : Nat) (ev : x%2=0) (kp : 1≤K)
    (bound : signedCarry H x+3<(2:Int)^K) :
    ∀ i, K≤i → i<H → (run i x)%2=0 := by
  intro i ki ih
  by_contra ne
  have od : (run i x)%2=1 := by omega
  have low:=carry_lower x i ev (by omega)
  have mono:=carry_monotone x (i+1) H ev (by omega) (by omega)
  have pow : (2:Int)^K≤(2:Int)^i := by gcongr; norm_num
  simp only [carry_succ,ne,ite_false] at mono
  omega

theorem frozen_count (x H K : Nat) (ev : x%2=0) (kp : 1≤K) (kh : K≤H)
    (bound : signedCarry H x+3<(2:Int)^K) :
    odds H x=odds K x := by
  have even:=no_late_odds x H K ev kp bound
  have same : ∀ i, K≤i → i≤H → odds i x=odds K x := by
    intro i ki
    induction i,ki using Nat.le_induction with
    | base => intro _;rfl
    | succ i ki ih =>
      intro hi
      rw [odds_succ,even i ki (by omega),Nat.add_zero]
      exact ih (by omega)
  exact same H kh (by omega)

theorem odds_of_modEq (h x y : Nat) (con : x ≡ y [MOD 2^h]) : odds h x=odds h y := by
  obtain ⟨d,hd⟩:=con.dvd
  have eqn : (y:Int)=(x:Int)+(2:Int)^h*d := by
    push_cast at hd
    omega
  have q:=(signed_lift h (x:Int) d).2
  rw [←eqn,(physical h y).2,(physical h x).2] at q
  exact q.symm

private theorem peak_even (j : Nat) : (3^j-1)%2=0 := by
  have pos : 1≤(3:Nat)^j := Nat.pow_pos (by decide)
  have od : (3:Nat)^j%2=1 := by simp [Nat.pow_mod]
  omega

private theorem peak_carry (h j : Nat) :
    (2:Int)^h*(run h (3^j-1):Int) =
      (3:Int)^(j+odds h (3^j-1))+signedCarry h (3^j-1) := by
  have pos : 1≤(3:Nat)^j := Nat.pow_pos (by decide)
  have e : ((3^j-1:Nat):Int)+1=(3:Int)^j := by
    rw [Nat.cast_sub pos]
    push_cast
    ring
  unfold signedCarry
  rw [e,pow_add]
  ring

private theorem cancel_three (d a b : Nat) (con : 3^d*a ≡ 3^d*b [MOD 2^498]) :
    a ≡ b [MOD 2^498] := by
  apply con.cancel_left_of_coprime
  exact Nat.Coprime.pow 498 d (by decide : Nat.Coprime 2 3)

private theorem residue_positive (d : Nat) : 1≤residue d := by
  have con:=(residue_spec d).2.of_dvd (show (2:Nat)∣2^498 by exact dvd_pow_self 2 (by decide))
  have od : residue d%2=1 := by
    simpa [Nat.ModEq,Nat.mul_mod,Nat.pow_mod] using con
  omega

theorem frozen_peak_residue (H j : Nat) (long : 498≤H)
    (count : odds H (3^j-1)=240) (fixed : signedCarry H (3^j-1)=frozenC) :
    3^j ≡ 3^173 [MOD 2^498] := by
  have e:=peak_carry H j
  rw [count,fixed] at e
  have en : 2^H*run H (3^j-1)=3^(j+240)+frozenC := by exact_mod_cast e
  have da : (2:Nat)^498∣3^(j+240)+frozenC := by
    rw [←en]
    exact dvd_mul_of_dvd_left (pow_dvd_pow 2 long) _
  have db : (2:Nat)^498∣3^(173+240)+frozenC := by
    rw [←native498.2.1]
    exact dvd_mul_right _ _
  have con : 3^(j+240) ≡ 3^(173+240) [MOD 2^498] :=
    ((Nat.modEq_zero_iff_dvd.mpr da).trans (Nat.modEq_zero_iff_dvd.mpr db).symm).add_right_cancel' frozenC
  apply cancel_three 240
  simpa [pow_add,Nat.mul_comm] using con

/-- The finite 257-entry scan excludes every earlier peak at any synchronized
paid clock while the native ordinary source has the frozen grades and carry. -/
theorem no_earlier_paid_peak (H j t : Nat) (long : 498≤H) (earlier : t<j)
    (count : odds H (3^j-1)=240) (fixed : signedCarry H (3^j-1)=frozenC)
    (same : run H (3^j-1)=run H (3^t-1))
    (paid : j+odds H (3^j-1)=t+odds H (3^t-1)) : False := by
  let d:=j-t
  have dp : 1≤d := by dsimp [d];omega
  have jt : j=t+d := by dsimp [d];omega
  have grade : odds H (3^t-1)=240+d := by rw [count] at paid;omega
  have other_fixed : signedCarry H (3^t-1)=frozenC := by
    have a:=peak_carry H j
    have b:=peak_carry H t
    rw [same,paid,fixed] at a
    omega
  have bound : signedCarry H (3^t-1)+3<(2:Int)^497 := by
    rw [other_fixed]
    exact_mod_cast native498.2.2
  have all_count:=frozen_count (3^t-1) H 497 (peak_even t) (by decide) (by omega) bound
  have maxq:=odd_le 497 (3^t-1)
  have small : d≤257 := by omega
  have at498 : odds 498 (3^t-1)=240+d := by
    have c:=carry_monotone (3^t-1) 498 H (peak_even t) (by decide) long
    have b498 : signedCarry 498 (3^t-1)+3<(2:Int)^497 := by omega
    have f:=frozen_count (3^t-1) 498 497 (peak_even t) (by decide) (by decide) b498
    omega
  have native:=frozen_peak_residue H j long count fixed
  have leading : 3^t ≡ residue d [MOD 2^498] := by
    apply cancel_three d
    have e : 3^d*3^t=3^j := by rw [←pow_add,jt,Nat.add_comm]
    rw [e]
    exact native.trans (residue_spec d).2.symm
  have sub : 3^t-1 ≡ residue d-1 [MOD 2^498] :=
    leading.sub_right (Nat.pow_pos (by decide)) (residue_positive d)
  have eqcount:=odds_of_modEq 498 (3^t-1) (residue d-1) sub
  have blocked:=finite_scan ⟨d-1,by omega⟩
  change odds 498 (residue ((d-1)+1)-1)≠240+((d-1)+1) at blocked
  rw [Nat.sub_add_cancel dp] at blocked
  exact blocked (eqcount.symm.trans at498)

#print axioms carry_succ
#print axioms carry_lower
#print axioms carry_monotone
#print axioms no_late_odds
#print axioms frozen_count
#print axioms odds_of_modEq
#print axioms frozen_peak_residue
#print axioms no_earlier_paid_peak
end Collatz.FrozenPeakSeparation
