/- Exact paired inverse return: a smaller source for one full ternary class.
New finite word, not a proof of universal closure. Core Lean only.
-/
import Collatz.Closure
open CollatzReverseBasin CollatzClosure
namespace CollatzInverseReturn

def run : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => run k (shortcut n)

theorem basin_run (k n : Nat) : Basin (run k n) ↔ Basin n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih => exact (ih (shortcut n)).trans (basin_step n)

theorem source_run (t : Nat) : run 17 (131072*t+127657) = 177147*t+172534 := by
  have h0 : shortcut (131072*t+127657) = 196608*t+191486 := by
    unfold shortcut
    split <;> omega
  have h1 : shortcut (196608*t+191486) = 98304*t+95743 := by
    unfold shortcut
    split <;> omega
  have h2 : shortcut (98304*t+95743) = 147456*t+143615 := by
    unfold shortcut
    split <;> omega
  have h3 : shortcut (147456*t+143615) = 221184*t+215423 := by
    unfold shortcut
    split <;> omega
  have h4 : shortcut (221184*t+215423) = 331776*t+323135 := by
    unfold shortcut
    split <;> omega
  have h5 : shortcut (331776*t+323135) = 497664*t+484703 := by
    unfold shortcut
    split <;> omega
  have h6 : shortcut (497664*t+484703) = 746496*t+727055 := by
    unfold shortcut
    split <;> omega
  have h7 : shortcut (746496*t+727055) = 1119744*t+1090583 := by
    unfold shortcut
    split <;> omega
  have h8 : shortcut (1119744*t+1090583) = 1679616*t+1635875 := by
    unfold shortcut
    split <;> omega
  have h9 : shortcut (1679616*t+1635875) = 2519424*t+2453813 := by
    unfold shortcut
    split <;> omega
  have h10 : shortcut (2519424*t+2453813) = 3779136*t+3680720 := by
    unfold shortcut
    split <;> omega
  have h11 : shortcut (3779136*t+3680720) = 1889568*t+1840360 := by
    unfold shortcut
    split <;> omega
  have h12 : shortcut (1889568*t+1840360) = 944784*t+920180 := by
    unfold shortcut
    split <;> omega
  have h13 : shortcut (944784*t+920180) = 472392*t+460090 := by
    unfold shortcut
    split <;> omega
  have h14 : shortcut (472392*t+460090) = 236196*t+230045 := by
    unfold shortcut
    split <;> omega
  have h15 : shortcut (236196*t+230045) = 354294*t+345068 := by
    unfold shortcut
    split <;> omega
  have h16 : shortcut (354294*t+345068) = 177147*t+172534 := by
    unfold shortcut
    split <;> omega
  simp only [run, h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16]

theorem companion_run (t : Nat) : run 17 (655360*t+638285) = 885735*t+862670 := by
  have h0 : shortcut (655360*t+638285) = 983040*t+957428 := by
    unfold shortcut
    split <;> omega
  have h1 : shortcut (983040*t+957428) = 491520*t+478714 := by
    unfold shortcut
    split <;> omega
  have h2 : shortcut (491520*t+478714) = 245760*t+239357 := by
    unfold shortcut
    split <;> omega
  have h3 : shortcut (245760*t+239357) = 368640*t+359036 := by
    unfold shortcut
    split <;> omega
  have h4 : shortcut (368640*t+359036) = 184320*t+179518 := by
    unfold shortcut
    split <;> omega
  have h5 : shortcut (184320*t+179518) = 92160*t+89759 := by
    unfold shortcut
    split <;> omega
  have h6 : shortcut (92160*t+89759) = 138240*t+134639 := by
    unfold shortcut
    split <;> omega
  have h7 : shortcut (138240*t+134639) = 207360*t+201959 := by
    unfold shortcut
    split <;> omega
  have h8 : shortcut (207360*t+201959) = 311040*t+302939 := by
    unfold shortcut
    split <;> omega
  have h9 : shortcut (311040*t+302939) = 466560*t+454409 := by
    unfold shortcut
    split <;> omega
  have h10 : shortcut (466560*t+454409) = 699840*t+681614 := by
    unfold shortcut
    split <;> omega
  have h11 : shortcut (699840*t+681614) = 349920*t+340807 := by
    unfold shortcut
    split <;> omega
  have h12 : shortcut (349920*t+340807) = 524880*t+511211 := by
    unfold shortcut
    split <;> omega
  have h13 : shortcut (524880*t+511211) = 787320*t+766817 := by
    unfold shortcut
    split <;> omega
  have h14 : shortcut (787320*t+766817) = 1180980*t+1150226 := by
    unfold shortcut
    split <;> omega
  have h15 : shortcut (1180980*t+1150226) = 590490*t+575113 := by
    unfold shortcut
    split <;> omega
  have h16 : shortcut (590490*t+575113) = 885735*t+862670 := by
    unfold shortcut
    split <;> omega
  simp only [run, h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16]

theorem source_basin (t : Nat) :
    Basin (131072*t+127657) ↔ Basin (177147*t+172534) := by
  simpa only [source_run] using (basin_run 17 (131072*t+127657)).symm

theorem companion_basin (t : Nat) :
    Basin (5*(131072*t+127657)) ↔ Basin (5*(177147*t+172534)) := by
  have h := (basin_run 17 (655360*t+638285)).symm
  rw [companion_run] at h
  rw [show 5*(131072*t+127657) = 655360*t+638285 by omega,
      show 5*(177147*t+172534) = 885735*t+862670 by omega]
  exact h

def FiveFail (n : Nat) : Prop := Basin n ∧ ¬ Basin (5*n)

theorem inverse_failure (t : Nat) :
    FiveFail (177147*t+172534) ↔ FiveFail (131072*t+127657) := by
  unfold FiveFail
  rw [source_basin, companion_basin]

theorem inverse_smaller (t : Nat) : 131072*t+127657 < 177147*t+172534 := by omega

theorem excludes_least_failure (t : Nat)
    (h : ∀ x, x < 177147*t+172534 → ¬ FiveFail x) :
    ¬ FiveFail (177147*t+172534) := by
  intro hf
  exact h _ (inverse_smaller t) ((inverse_failure t).mp hf)

end CollatzInverseReturn
