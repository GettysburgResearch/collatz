import PinClock
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! The physical duration of an exact power word on distinct ordinary states. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.PowerTreeArithmetic
open CoreBranching PinClock

def copies (w : List Bool) : ℕ→List Bool
  | 0 => []
  | n+1 => w++copies w n

@[simp] theorem copies_length (w : List Bool) (n : ℕ) : (copies w n).length=n*w.length := by
  induction n with
  | zero => simp [copies]
  | succ n ih => simp only [copies,List.length_append,ih,Nat.succ_mul];omega

private theorem copies_snoc (w : List Bool) (n : ℕ) : copies w (n+1)=copies w n++w := by
  induction n with
  | zero => simp [copies]
  | succ n ih =>
    change w++copies w (n+1)=(w++copies w n)++w
    rw [ih,List.append_assoc]

@[simp] theorem parity_length (k x : ℕ) : (parityPrefix k x).length=k := by
  induction k generalizing x with
  | zero => rfl
  | succ k ih => simp only [parityPrefix,List.length_cons,ih]

theorem parity_append (a b x : ℕ) :
    parityPrefix (a+b) x=parityPrefix a x++parityPrefix b (run a x) := by
  induction a generalizing x with
  | zero => simp [parityPrefix,run]
  | succ a ih =>
    rw [Nat.succ_add]
    simp only [parityPrefix,run,List.cons_append,ih]

/-- Matching parity bits force the corresponding full dyadic divisibility. -/
theorem shared_prefix_dvd (k x y : ℕ) (h : parityPrefix k x=parityPrefix k y) : 2^k∣x-y := by
  let w := parityPrefix k y
  have hx : code w x=2^k*(run k x+1) := by change code (parityPrefix k y) x=_;rw [←h,actual_code]
  have hy : code w y=2^k*(run k y+1) := actual_code k y
  have hd : den w*(x-y)=code w x-code w y := by simp only [code,Nat.add_sub_add_right,Nat.mul_sub]
  have hdiv : 2^k∣den w*(x-y) := by
    rw [hd,hx,hy,←Nat.mul_sub]
    exact Nat.dvd_mul_right _ _
  have ho : Odd (den w) := Nat.odd_iff.mpr (den_odd w)
  exact (ho.coprime_two_left.pow_left k).dvd_of_dvd_mul_left hdiv

private theorem run_growth (p x : ℕ) : 2^p*(run p x+1)≤3^p*(x+1) := by
  induction p generalizing x with
  | zero => simp [run]
  | succ p ih =>
    have he : 2*(step x+1)≤3*(x+1) := by
      unfold step
      split <;> omega
    calc
      2^(p+1)*(run (p+1) x+1)=2*(2^p*(run p (step x)+1)) := by simp only [run,pow_succ];ring
      _≤2*(3^p*(step x+1)) := Nat.mul_le_mul_left _ (ih _)
      _=3^p*(2*(step x+1)) := by ring
      _≤3^p*(3*(x+1)) := Nat.mul_le_mul_left _ he
      _=3^(p+1)*(x+1) := by ring

/-- The exact integer size estimate when a repeated prefix is observed at two distinct states. -/
theorem shared_run_bound (p a x : ℕ) (hn : x≠run p x)
    (h : parityPrefix a x=parityPrefix a (run p x)) : 2^(a+p)≤3^p*(x+1) := by
  have ha : 2^a≤max (x+1) (run p x+1) := by
    rcases lt_or_gt_of_ne hn with hlt|hgt
    · have hd := Nat.le_of_dvd (Nat.sub_pos_of_lt hlt) (shared_prefix_dvd a _ _ h.symm)
      exact hd.trans ((Nat.sub_le _ _).trans (by omega))
    · have hd := Nat.le_of_dvd (Nat.sub_pos_of_lt hgt) (shared_prefix_dvd a _ _ h)
      exact hd.trans ((Nat.sub_le _ _).trans (by omega))
  rw [pow_add,Nat.mul_comm]
  apply (Nat.mul_le_mul_left (2^p) ha).trans
  rcases le_total (x+1) (run p x+1) with hu|hd
  · rw [max_eq_right hu];exact run_growth p x
  · rw [max_eq_left hd];exact Nat.mul_le_mul_right _ (Nat.pow_le_pow_left (by decide) p)

/-- A literal power of any observed word gives the matching prefixes used by the height bound. -/
theorem power_bound (w : List Bool) (j x : ℕ) (hn : x≠run w.length x)
    (hw : parityPrefix ((j+2)*w.length) x=copies w (j+2)) :
    2^((j+2)*w.length)≤3^w.length*(x+1) := by
  let p := w.length
  let a := (j+1)*p
  have hpa : (j+2)*w.length=p+a := by dsimp only [p,a];ring
  have hap : (j+2)*w.length=a+p := by dsimp only [p,a];ring
  have hr : parityPrefix a (run p x)=copies w (j+1) := by
    have he := hw
    rw [hpa,parity_append,copies] at he
    have hd := congrArg (List.drop p) he
    have hl : (parityPrefix p x).length=p := parity_length p x
    have h1 : (parityPrefix p x).drop p=[] := List.drop_eq_nil_of_le (by omega)
    have h2 : w.drop p=[] := List.drop_eq_nil_of_le (by rfl)
    simpa only [List.drop_append_of_le_length,hl,le_refl,h1,h2,
      List.nil_append,show w.length=p from rfl] using hd
  have hl : parityPrefix a x=copies w (j+1) := by
    have he := hw
    rw [hap,parity_append,copies_snoc] at he
    have ht := congrArg (List.take a) he
    have len : (copies w (j+1)).length=a := copies_length w (j+1)
    have h1 : (parityPrefix a x).take a=parityPrefix a x := List.take_of_length_le (by rw [parity_length])
    have h2 : (copies w (j+1)).take a=copies w (j+1) := List.take_of_length_le (by rw [len])
    simpa only [List.take_append_of_le_length,parity_length,len,le_refl,h1,h2] using ht
  rw [hap]
  exact shared_run_bound p a x hn (hl.trans hr.symm)

/-- An absolute duration bound with no logarithms or transcendental constants. -/
theorem power_bit_bound (w : List Bool) (j x : ℕ) (hn : x≠run w.length x)
    (hw : parityPrefix ((j+2)*w.length) x=copies w (j+2)) :
    2^((j+2)*w.length)≤(x+1)^5 := by
  let L := (j+2)*w.length
  have hp := pow_le_pow_left' (power_bound w j x hn hw) 5
  rw [←pow_mul,mul_pow,←pow_mul] at hp
  have hv : 3^(w.length*5)≤2^(4*L) := by
    calc
      _ = (3^5)^w.length := by rw [←pow_mul,Nat.mul_comm]
      _ ≤ (2^8)^w.length := Nat.pow_le_pow_left (by decide) _
      _ = 2^(8*w.length) := (pow_mul _ _ _).symm
      _ ≤ _ := Nat.pow_le_pow_right (by decide) (by dsimp [L];nlinarith)
  have hc : 2^(4*L)*2^L≤2^(4*L)*(x+1)^5 := by
    calc
      _ = 2^(L*5) := by rw [←pow_add];congr 1;omega
      _ ≤ _ := hp.trans (Nat.mul_le_mul_right _ hv)
  exact Nat.le_of_mul_le_mul_left hc (by positivity)

end Collatz.PowerTreeArithmetic
