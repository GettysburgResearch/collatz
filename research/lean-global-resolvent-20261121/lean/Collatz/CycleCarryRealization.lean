import Collatz.CycleCarry
import Collatz.TerminalExponentLift

set_option autoImplicit false
set_option maxHeartbeats 2000000
set_option maxRecDepth 2000

namespace CollatzCycleCarryRealization

open CollatzCycleCarry CollatzTerminalExponentLift
open CollatzTerminalCarry CollatzTerminalCarryClosure
open CollatzReverseBasin CollatzClosure

/-- Recover the exact terminal congruence from every legal source identity,
not only from the constructed realizations. -/
theorem terminal_quotient {D h m : Nat}
    (ident : TerminalIdentity m (deficitWord D) h) :
    ∃ q, 3^(14*D+85)*q=2^h+122 ∧ m+41=2^(22*D+132)*q := by
  have corr := repeated_correction (2*D+12)
  rw [show 11*(2*D+12)=22*D+132 by omega,
    show 7*(2*D+12)=14*D+84 by omega] at corr
  change correction (deficitWord D)+41*2^(22*D+132)=41*3^(14*D+84) at corr
  unfold TerminalIdentity at ident
  rw [deficit_word_length,deficit_word_total] at ident
  rw [Nat.pow_add 2 (22*D+132) h] at ident
  have power : 3^(14*D+85)=3*3^(14*D+84) := by
    rw [show 14*D+85=(14*D+84)+1 by omega,Nat.pow_succ]
    omega
  have balance : 3^(14*D+85)*(m+41)=2^(22*D+132)*(2^h+122) := by
    rw [power] at ident ⊢
    grind
  have dv : 3^(14*D+85) ∣ 2^(22*D+132)*(2^h+122) := by
    rw [← balance]
    exact Nat.dvd_mul_right _ _
  have cp : Nat.Coprime (3^(14*D+85)) (2^(22*D+132)) :=
    Nat.Coprime.pow _ _ (by decide : Nat.Coprime 3 2)
  obtain ⟨q,hq⟩ := cp.dvd_of_dvd_mul_left dv
  refine ⟨q,hq.symm,?_⟩
  apply Nat.eq_of_mul_eq_mul_left (Nat.pow_pos (by decide) : 0<3^(14*D+85))
  rw [hq] at balance
  grind

theorem terminal_identity_iff_quotient {D h m : Nat} :
    TerminalIdentity m (deficitWord D) h ↔
      ∃ q, 3^(14*D+85)*q=2^h+122 ∧ m+41=2^(22*D+132)*q := by
  constructor
  · exact terminal_quotient
  · rintro ⟨q,hq,hm⟩
    exact cycle_source_identity hq hm

private theorem exponential_gap (D : Nat) :
    2^(22*D+134)+122<3^(14*D+85) := by
  induction D with
  | zero => decide
  | succ D ih =>
    rw [show 22*(D+1)+134=(22*D+134)+22 by omega,
      show 14*(D+1)+85=(14*D+85)+14 by omega,
      Nat.pow_add 2 (22*D+134) 22,Nat.pow_add 3 (14*D+85) 14]
    change 2^(22*D+134)*4194304+122<3^(14*D+85)*4782969
    omega

/-- Source legality forces more terminal binary precision than the whole
prefix clock, despite the unbounded compiler deficit. -/
theorem legal_terminal_bound {D h q : Nat}
    (congruence : 3^(14*D+85)*q=2^h+122) : 22*D+135≤h := by
  have positive : 0<q := by
    by_cases zero : q=0
    · simp only [zero,Nat.mul_zero] at congruence
      have impossible : (0:Nat)=2^h+122 := congruence
      exact Nat.noConfusion impossible
    · omega
  have lower := Nat.le_mul_of_pos_right (3^(14*D+85)) positive
  have gap := exponential_gap D
  by_cases done : 22*D+135≤h
  · exact done
  have small : h≤22*D+134 := by omega
  have bound := Nat.pow_le_pow_right (by decide : 0<2) small
  omega

theorem actual_terminal_bound {D h m : Nat}
    (ident : TerminalIdentity m (deficitWord D) h) :
    total (deficitWord D)+3≤h := by
  obtain ⟨q,hq,_⟩ := terminal_quotient ident
  have bound := legal_terminal_bound hq
  rw [deficit_word_total]
  omega

/-- Every deficit is realized by arbitrarily large actual positive complete
source words, with exactly the displayed ordinary target endpoint. -/
theorem arbitrarily_large_complete_sources (D H : Nat) :
    ∃ h m, H<h ∧ 0<m ∧ Follows m (deficitWord D++[h]) ∧
      Basin m ∧ TerminalIdentity m (deficitWord D) h ∧
      total (deficitWord D)=(21*D+132)+D ∧
      (iterate (2*m+1) (21*D+132):Int)=
        (2:Int)^(h+D+1)+244*(2:Int)^D-5 := by
  obtain ⟨h,q,large,eq⟩ := arbitrarily_large_exponents
    (by decide : 122%3=2) (14*D+84) H
  have congruence : 3^(14*D+85)*q=2^h+122 := by
    simpa only [show 14*D+84+1=14*D+85 by omega] using eq
  have qpos : 0<q := by
    by_cases zero : q=0
    · simp only [zero,Nat.mul_zero] at congruence
      have impossible : (0:Nat)=2^h+122 := congruence
      exact Nat.noConfusion impossible
    · omega
  have powerbound := Nat.pow_le_pow_right (by decide : 0<2)
    (by omega : 6≤22*D+132)
  change 64≤2^(22*D+132) at powerbound
  have productbound := Nat.le_mul_of_pos_right (2^(22*D+132)) qpos
  let m := 2^(22*D+132)*q-41
  have source : m+41=2^(22*D+132)*q := by dsimp [m]; omega
  have positive : 0<m := by dsimp [m]; omega
  have full := cycle_source_full_word (by omega : 0<h) congruence source
  have ident := cycle_source_identity congruence source
  exact ⟨h,m,large,positive,full,follows_basin full,ident,
    unbounded_deficit D,cycle_ordinary_endpoint ident⟩

/-- A fixed signed pin cannot support arbitrary carry -1 debt: its distance
from -1 has to be divisible by the entire unpaid binary power. -/
theorem minus_one_pin_divisibility {K c : Int} {D : Nat}
    (eq : K*(2:Int)^D+c=(-1:Int)) : (2:Int)^D ∣ c+1 := by
  refine ⟨-K,?_⟩
  grind

theorem minus_five_pin_exact {K : Int} {D : Nat}
    (eq : K*(2:Int)^D-5=(-1:Int)) :
    (D=0 ∧ K=4) ∨ (D=1 ∧ K=2) ∨ (D=2 ∧ K=1) := by
  have ppos : 0<(2:Int)^D := Int.pow_pos (by decide)
  have kpos : 0<K := by
    by_cases done : 0<K
    · exact done
    have nonpos : K≤0 := by omega
    have product := Int.mul_nonpos_of_nonpos_of_nonneg nonpos (by omega : 0≤(2:Int)^D)
    omega
  have upper : (2:Int)^D≤4 := by
    have mult := Int.mul_le_mul_of_nonneg_right (by omega : (1:Int)≤K)
      (by omega : 0≤(2:Int)^D)
    omega
  have bound : D≤2 := by
    by_cases done : D≤2
    · exact done
    have lower := Nat.pow_le_pow_right (by decide : 0<2) (by omega : 3≤D)
    have lower' : (8:Int)≤(2:Int)^D := by
      have lc : ((2^3:Nat):Int)≤((2^D:Nat):Int) := by omega
      rw [Int.natCast_pow,Int.natCast_pow] at lc
      exact lc
    omega
  have cases : D=0 ∨ D=1 ∨ D=2 := by omega
  rcases cases with h | h | h
  · subst D; simp at eq; exact Or.inl ⟨rfl,by omega⟩
  · subst D; simp at eq; exact Or.inr (Or.inl ⟨rfl,by omega⟩)
  · subst D; simp at eq; exact Or.inr (Or.inr ⟨rfl,by omega⟩)

end CollatzCycleCarryRealization
