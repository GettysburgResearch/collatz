import SignedCenter
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

namespace Collatz.SignedCenter

open TernaryPortal (run step odds)

private theorem pos_step' {z : Nat} (hz : 0<z) : 0<step z := by
  unfold step
  split <;> omega

private theorem run_pos (z h : Nat) (hz : 0<z) : 0<run h z := by
  induction h generalizing z with
  | zero => exact hz
  | succ h ih => exact ih _ (pos_step' hz)

private theorem ordinary_lower (z h : Nat) :
    (3:ℚ)^(odds h z)*z ≤ 2^h*(run h z:ℚ) := by
  induction h generalizing z with
  | zero => simp [odds,run]
  | succ h ih =>
    have tail := ih (step z)
    rw [run,odds,pow_succ,pow_add]
    by_cases e : z%2=0
    · have s : 2*step z=z := by simp [step,e]; omega
      have s' : 2*(step z:ℚ)=z := by exact_mod_cast s
      rw [e,pow_zero,one_mul,←s']
      linear_combination 2*tail
    · have o : z%2=1 := by omega
      have s : 2*step z=3*z+1 := by simp [step,o]; omega
      have s' : 2*(step z:ℚ)=3*z+1 := by exact_mod_cast s
      rw [o,pow_one]
      have p : 0≤(3:ℚ)^odds h (step z) := by positivity
      linear_combination 2*tail - (3:ℚ)^odds h (step z)*s' + p

private theorem ordinary_upper (z h : Nat) (hz : 0<z)
    (nohit : ∀ i, i<h → run i z ≠ 1) :
    (2:ℚ)^h*(run h z:ℚ) ≤ (10/3:ℚ)^(odds h z)*z := by
  induction h generalizing z with
  | zero => simp [odds,run]
  | succ h ih =>
    have tail := ih (step z) (pos_step' hz)
      (fun i hi => nohit (i+1) (by omega))
    rw [run,odds,pow_succ,pow_add]
    by_cases e : z%2=0
    · have s : 2*step z=z := by simp [step,e]; omega
      have s' : 2*(step z:ℚ)=z := by exact_mod_cast s
      rw [e,pow_zero,one_mul,←s']
      linear_combination 2*tail
    · have o : z%2=1 := by omega
      have no := nohit 0 (by omega)
      change z≠1 at no
      have s : 3*(2*step z)≤10*z := by simp [step,o]; omega
      have s' : 3*(2*(step z:ℚ))≤10*z := by exact_mod_cast s
      rw [o,pow_one]
      have pp : 0≤(10/3:ℚ)^odds h (step z) := by positivity
      have cost := mul_le_mul_of_nonneg_left s' pp
      linear_combination 2*tail + cost/3

/-- Padding a supplied upper hit with one genuine 1-cycle lap per existing odd
departure supplies enough binary clocks for every lower ternary cancellation,
unless that same positive lower has already reached one. -/
theorem paid_grade {z H : Nat} (positive : 0<z) (upper : run H (3*z)=1) :
    let r := odds H (3*z)
    (∃ i, i<H+2*r ∧ run i z=1) ∨ 2*r+1≤odds (H+2*r) z := by
  dsimp only
  let r := odds H (3*z)
  change (∃ i, i<H+2*r ∧ run i z=1) ∨ 2*r+1≤odds (H+2*r) z
  by_cases done : ∃ i, i<H+2*r ∧ run i z=1
  · exact Or.inl done
  apply Or.inr
  by_contra wrong
  have grade : odds (H+2*r) z ≤ 2*r := by omega
  have u := ordinary_lower (3*z) H
  rw [upper] at u
  push_cast at u
  change (3:ℚ)^r*(3*z)≤2^H*1 at u
  have v := ordinary_upper z (H+2*r) positive (fun i hi h => done ⟨i,hi,h⟩)
  have rz : (0:ℚ)<z := by exact_mod_cast positive
  have n := run_pos z (H+2*r) positive
  have large : (1:ℚ)≤run (H+2*r) z := by exact_mod_cast n
  have last := mul_le_mul_of_nonneg_left large (by positivity : (0:ℚ)≤2^(H+2*r))
  rw [mul_one] at last
  have gp := pow_le_pow_right₀ (by norm_num : (1:ℚ)≤10/3) grade
  have cr := pow_le_pow_left₀ (by norm_num : (0:ℚ)≤(10/3)^2)
    (by norm_num : (10/3:ℚ)^2≤12) r
  have rel : (2:ℚ)^(H+2*r)=2^H*4^r := by
    rw [pow_add,pow_mul]; norm_num
  have a : (2:ℚ)^(H+2*r) ≤ 12^r*z := by
    calc
      _ ≤ _ := last.trans v
      _ ≤ (10/3:ℚ)^(2*r)*z := mul_le_mul_of_nonneg_right gp rz.le
      _ ≤ 12^r*z := by rw [pow_mul]; exact mul_le_mul_of_nonneg_right cr rz.le
  have b : (12:ℚ)^r*z < 2^(H+2*r) := by
    rw [rel,show (12:ℚ)=3*4 by norm_num,mul_pow]
    have du := mul_le_mul_of_nonneg_right u (by positivity : (0:ℚ)≤4^r)
    have pos : 0<(3:ℚ)^r*4^r*z := by positivity
    nlinarith only [du,pos]
  exact (not_lt_of_ge a) b

private theorem two_unit (h : Nat) : (2:Int)^h%3=1 ∨ (2:Int)^h%3=2 := by
  induction h with
  | zero => decide
  | succ h ih =>
    rcases ih with one|two
    · rw [pow_succ,Int.mul_emod,one]; decide
    · rw [pow_succ,Int.mul_emod,two]; decide

private theorem laps (k : Nat) : run (2*k) 1=1 ∧ odds (2*k) 1=k := by
  induction k with
  | zero => decide
  | succ k ih =>
    rw [Nat.mul_succ,TernaryPortal.run_add,TernaryPortal.odds_add,ih.1,ih.2]
    exact ⟨by decide,by rfl⟩

/-- A complete real upper certificate gives a strictly positive physical lower
exit from its full padded signed center at every odd rank. -/
theorem paid_full_lift {z H : Nat} (positive : 0<z) (upper : run H (3*z)=1) :
    let r := odds H (3*z)
    let L := H+2*r
    let k := 2*r+1
    let a := (3:Int)^k*z-2^L
    (∃ i, i<L ∧ run i z=1) ∨
    (run L (3*z)=1 ∧ odds L (3*z)=2*r ∧
      ∃ t c, Strip k a t c ∧ t≤L ∧ 0<run t z ∧
        (run t z:Int)=2^(L-t)+c ∧ odds t z=k) := by
  dsimp only
  let r := odds H (3*z)
  let L := H+2*r
  let k := 2*r+1
  let a := (3:Int)^k*z-2^L
  change (∃ i, i<L ∧ run i z=1) ∨
    (run L (3*z)=1 ∧ odds L (3*z)=2*r ∧ ∃ t c, Strip k a t c ∧ t≤L ∧ 0<run t z ∧
      (run t z:Int)=2^(L-t)+c ∧ odds t z=k)
  obtain cleared|enough := paid_grade positive upper
  · exact Or.inl cleared
  have uword : run L (3*z)=1 ∧ odds L (3*z)=2*r := by
    dsimp only [L]
    rw [TernaryPortal.run_add,TernaryPortal.odds_add,upper,(laps r).1,(laps r).2]
    change 1=1 ∧ r+r=2*r
    omega
  have unit : a%3≠0 := by
    have res := two_unit L
    dsimp only [a,k]
    rw [pow_succ,show (3:Int)^(2*r)*3*z=3*(3^(2*r)*z) by ring]
    omega
  have link : (3:Int)^k*z=2^L*1+a := by dsimp only [a]; ring
  obtain ⟨t,c,tr,ht⟩ := strip_by_grade (fun _ => unit) link enough
  have split : t+(L-t)=L := by omega
  obtain ⟨pos,endpt,grade⟩ := strip_lift (d:=L-t) (q:=1) tr positive (by simpa [split] using link)
  exact Or.inr ⟨uword.1,uword.2,t,c,tr,ht,pos,by simpa using endpt,grade⟩

#print axioms paid_full_lift
#print axioms paid_grade

end Collatz.SignedCenter
