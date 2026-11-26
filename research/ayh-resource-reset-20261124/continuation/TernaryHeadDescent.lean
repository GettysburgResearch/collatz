import ShellCover
import Mathlib.Data.Nat.Log
import Mathlib.Tactic.IntervalCases

/-! Physical first hits of a fixed mixed-base blocked prefix and a source-bounded
four-trit partner. The ordinary merger with that partner remains open. -/
namespace CollatzShell.TernaryHead

def Head (x : Nat) : Prop := ∃ k, 4 ≤ k ∧ 7*3^k ≤ x ∧ x < 8*3^k

private theorem step_pos' {n : Nat} (hn : 0<n) : 0<step n := by
  unfold step
  split <;> omega

private theorem orbit_pos' (j : Nat) {n : Nat} (hn : 0<n) : 0<orbit j n := by
  induction j generalizing n with
  | zero => exact hn
  | succ j ih => exact ih (step_pos' hn)

private theorem oneStep (n : Nat) (hn : 600≤n) :
    ∃ p : Nat, 3^p*n ≤ 2*step n ∧ 1800*(2*step n) ≤ 1801*(3^p*n) := by
  by_cases h : n%2=0
  · refine ⟨0,?_,?_⟩ <;> simp [step,h] <;> omega
  · refine ⟨1,?_,?_⟩ <;> simp [step,h] <;> omega

private theorem physicalBounds (j n : Nat) (h : ∀ i<j, 600≤orbit i n) :
    ∃ p : Nat, 3^p*n ≤ 2^j*orbit j n ∧
      1800^j*(2^j*orbit j n) ≤ 1801^j*(3^p*n) := by
  induction j generalizing n with
  | zero => exact ⟨0,by simp [orbit],by simp [orbit]⟩
  | succ j ih =>
    obtain ⟨q,lo,hi⟩ := oneStep n (h 0 (by omega))
    obtain ⟨p,l,u⟩ := ih (step n) (fun i hi => h (i+1) (by omega))
    refine ⟨p+q,?_,?_⟩
    · calc
        3^(p+q)*n = 3^p*(3^q*n) := by ring
        _ ≤ 3^p*(2*step n) := Nat.mul_le_mul_left _ lo
        _ = 2*(3^p*step n) := by ring
        _ ≤ 2*(2^j*orbit j (step n)) := Nat.mul_le_mul_left _ l
        _ = 2^(j+1)*orbit (j+1) n := by simp only [orbit]; ring
    · calc
        1800^(j+1)*(2^(j+1)*orbit (j+1) n)
            = (1800*2)*(1800^j*(2^j*orbit j (step n))) := by simp only [orbit]; ring
        _ ≤ (1800*2)*(1801^j*(3^p*step n)) := Nat.mul_le_mul_left _ u
        _ = (1801^j*3^p)*(1800*(2*step n)) := by ring
        _ ≤ (1801^j*3^p)*(1801*(3^q*n)) := Nat.mul_le_mul_left _ hi
        _ = 1801^(j+1)*(3^(p+q)*n) := by ring

private theorem smallDistortion (j : Nat) (hj : j≤10) :
    64*1801^j ≤ 65*1800^j := by interval_cases j <;> decide

/-- A rational covering of one ternary shell by twelve images using clocks 0–10. -/
private theorem grid (n w : Nat) (hw : w≤n) (hn : n<3*w) :
    ∃ j p : Nat, j≤10 ∧ 7*2^j*w≤3^p*n ∧ 65*3^p*n < 512*2^j*w := by
  by_cases h0 : 15795*n < 16384*w
  · refine ⟨5,5,by decide,?_,?_⟩ <;> norm_num <;> omega
  by_cases h1 : 1755*n < 2048*w
  · refine ⟨2,3,by decide,?_,?_⟩ <;> norm_num <;> omega
  by_cases h2 : 426465*n < 524288*w
  · refine ⟨10,8,by decide,?_,?_⟩ <;> norm_num <;> omega
  by_cases h3 : 47385*n < 65536*w
  · refine ⟨7,6,by decide,?_,?_⟩ <;> norm_num <;> omega
  by_cases h4 : 5265*n < 8192*w
  · refine ⟨4,4,by decide,?_,?_⟩ <;> norm_num <;> omega
  by_cases h5 : 585*n < 1024*w
  · refine ⟨1,2,by decide,?_,?_⟩ <;> norm_num <;> omega
  by_cases h6 : 142155*n < 262144*w
  · refine ⟨9,7,by decide,?_,?_⟩ <;> norm_num <;> omega
  by_cases h7 : 15795*n < 32768*w
  · refine ⟨6,5,by decide,?_,?_⟩ <;> norm_num <;> omega
  by_cases h8 : 1755*n < 4096*w
  · refine ⟨3,3,by decide,?_,?_⟩ <;> norm_num <;> omega
  by_cases h9 : 195*n < 512*w
  · refine ⟨0,1,by decide,?_,?_⟩ <;> norm_num <;> omega
  by_cases h10 : 47385*n < 131072*w
  · refine ⟨8,6,by decide,?_,?_⟩ <;> norm_num <;> omega
  refine ⟨5,4,by decide,?_,?_⟩ <;> norm_num <;> omega

theorem head_or_small {n : Nat} (hn : 0<n) :
    ∃ j≤10, orbit j n<600 ∨ Head (orbit j n) := by
  by_cases hit : ∃ j≤10, orbit j n<600
  · obtain ⟨j,hj,h⟩ := hit
    exact ⟨j,hj,Or.inl h⟩
  push Not at hit
  let a := Nat.log 3 n
  have lo : 3^a≤n := Nat.pow_log_le_self _ (by omega)
  have up : n<3*3^a := by
    have := Nat.lt_pow_succ_log_self (by decide : 1<3) n
    simpa [a,pow_succ,Nat.mul_comm] using this
  obtain ⟨j,p,hj,gl,gu⟩ := grid n (3^a) lo up
  let x := orbit j n
  have hx : 600≤x := hit j hj
  obtain ⟨s,bl,bu⟩ := physicalBounds j n (fun i hi => hit i (by omega))
  change 3^s*n ≤ 2^j*x at bl
  change 1800^j*(2^j*x) ≤ 1801^j*(3^s*n) at bu
  have hratio : 64*(2^j*x) ≤ 65*(3^s*n) := by
    apply Nat.le_of_mul_le_mul_left (c:=1800^j) _ (by positivity)
    calc
      1800^j*(64*(2^j*x)) = 64*(1800^j*(2^j*x)) := by ring
      _ ≤ 64*(1801^j*(3^s*n)) := Nat.mul_le_mul_left _ bu
      _ = (64*1801^j)*(3^s*n) := by ring
      _ ≤ (65*1800^j)*(3^s*n) := Nat.mul_le_mul_right _ (smallDistortion j hj)
      _ = 1800^j*(65*(3^s*n)) := by ring
  have left : 7*3^(a+s)≤3^p*x := by
    apply Nat.le_of_mul_le_mul_left (c:=2^j) _ (by positivity)
    calc
      2^j*(7*3^(a+s)) = 3^s*(7*2^j*3^a) := by ring
      _ ≤ 3^s*(3^p*n) := Nat.mul_le_mul_left _ gl
      _ = 3^p*(3^s*n) := by ring
      _ ≤ 3^p*(2^j*x) := Nat.mul_le_mul_left _ bl
      _ = 2^j*(3^p*x) := by ring
  have right : 3^p*x<8*3^(a+s) := by
    apply Nat.lt_of_mul_lt_mul_left (a:=64*2^j)
    calc
      64*2^j*(3^p*x) = 3^p*(64*(2^j*x)) := by ring
      _ ≤ 3^p*(65*(3^s*n)) := Nat.mul_le_mul_left _ hratio
      _ = 3^s*(65*3^p*n) := by ring
      _ < 3^s*(512*2^j*3^a) := Nat.mul_lt_mul_of_pos_left gu (by positivity)
      _ = 64*2^j*(8*3^(a+s)) := by ring
  have hp : p≤a+s := by
    by_contra! not_le
    have pw : 3^(a+s)≤3^p := Nat.pow_le_pow_right (by decide) (by omega)
    have r : 3^p*x<3^p*8 := by omega
    exact (by omega : ¬x<8) (Nat.lt_of_mul_lt_mul_left r)
  obtain ⟨k,hk⟩ := Nat.exists_eq_add_of_le hp
  rw [hk,pow_add] at left right
  have l : 7*3^k≤x := Nat.le_of_mul_le_mul_left (by simpa only [Nat.mul_left_comm,Nat.mul_comm,Nat.mul_assoc] using left : 3^p*(7*3^k)≤3^p*x) (by positivity)
  have u : x<8*3^k := Nat.lt_of_mul_lt_mul_left (by simpa only [Nat.mul_left_comm,Nat.mul_comm,Nat.mul_assoc] using right : 3^p*x<3^p*(8*3^k))
  refine ⟨j,hj,Or.inr ⟨k,?_,l,u⟩⟩
  by_contra! h
  interval_cases k <;> norm_num at u <;> omega

private theorem growth (j n : Nat) : 2^j*(orbit j n+1) ≤ 3^j*(n+1) := by
  induction j generalizing n with
  | zero => simp [orbit]
  | succ j ih =>
    have l : 2*(step n+1)≤3*(n+1) := by unfold step; split <;> omega
    calc
      2^(j+1)*(orbit (j+1) n+1) = 2*(2^j*(orbit j (step n)+1)) := by simp only [orbit]; ring
      _ ≤ 2*(3^j*(step n+1)) := Nat.mul_le_mul_left _ (ih _)
      _ = 3^j*(2*(step n+1)) := by ring
      _ ≤ 3^j*(3*(n+1)) := Nat.mul_le_mul_left _ l
      _ = 3^(j+1)*(n+1) := by ring

theorem source_contraction {n j : Nat} (hn : 3≤n) (hj : j≤10) :
    orbit j n / 81 < n := by
  have h := growth j n
  apply (Nat.div_lt_iff_lt_mul (by decide : 0<81)).2
  interval_cases j <;> norm_num at h ⊢ <;> omega

/-- The all-odd envelope gives a uniform multiplicative saving, including its
integer rounding. On every source outside the certified finite base this in
particular saves strictly more than two sevenths. -/
theorem contraction_factor {n j : Nat} (hj : j≤10) :
    82944*(orbit j n / 81) + 1024 ≤ 59049*(n+1) := by
  have h := growth j n
  interval_cases j <;> norm_num at h ⊢ <;> omega

theorem contraction_seven_fifths {n j : Nat} (hn : 600≤n) (hj : j≤10) :
    7*(orbit j n / 81) < 5*n := by
  have := contraction_factor (n:=n) hj
  omega

private def checkBasin : Nat → Nat → Bool
  | 0,n => n == 1
  | k+1,n => n == 1 || checkBasin k (step n)

private theorem checkBasin_sound (k n : Nat) (h : checkBasin k n = true) :
    Basin n := by
  induction k generalizing n with
  | zero =>
    have : n=1 := by simpa [checkBasin] using h
    exact ⟨0,this⟩
  | succ k ih =>
    simp only [checkBasin,Bool.or_eq_true,beq_iff_eq] at h
    rcases h with h|h
    · exact ⟨0,h⟩
    · obtain ⟨b,hb⟩ := ih (step n) h
      exact ⟨b+1,hb⟩

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
private theorem low_table : ∀ i : Fin 600, i.val=0 ∨ checkBasin 160 i.val=true := by
  decide +kernel

theorem low_basin {n : Nat} (hn : 0<n) (h : n<600) : Basin n := by
  have t := low_table ⟨n,h⟩
  rcases t with bad|good
  · exact False.elim ((by omega : n≠0) bad)
  · exact checkBasin_sound 160 n good

def Meet (n m : Nat) : Prop := ∃ i j, orbit i n=orbit j m

/-- The four-trit deletion tests just single-block normal words with fixed
leading mixed prefix. Every successful test provides an actual lower source. -/
theorem universal_iff_truncate :
    Universal ↔ ∀ x, Head x → Meet x (x/81) := by
  constructor
  · intro all x hx
    obtain ⟨k,hk,l,_⟩ := hx
    have pw : 81≤3^k := by exact Nat.pow_le_pow_right (by decide : 0<3) hk
    obtain ⟨i,hi⟩ := all x (by omega)
    obtain ⟨j,hj⟩ := all (x/81) (by omega)
    exact ⟨i,j,hi.trans hj.symm⟩
  · intro cover n
    induction n using Nat.strong_induction_on with
    | h n ih =>
      intro hn
      by_cases small : n<600
      · exact low_basin hn small
      obtain ⟨h,hl,small'|head⟩ := head_or_small hn
      · exact (basin_at_hit ⟨h,rfl⟩).mpr (low_basin (orbit_pos' h hn) small')
      obtain ⟨a,b,meeting⟩ := cover _ head
      obtain ⟨k,hk,hbig,_⟩ := head
      have pw : 81≤3^k := by exact Nat.pow_le_pow_right (by decide : 0<3) hk
      have mp : 0<orbit h n/81 := by omega
      have mrest := ih _ (source_contraction (by omega) hl) mp
      have shared := (basin_at_hit ⟨b,rfl⟩).mp mrest
      rw [← meeting] at shared
      exact (basin_at_hit ⟨h,rfl⟩).mpr ((basin_at_hit ⟨a,rfl⟩).mpr shared)

end CollatzShell.TernaryHead
