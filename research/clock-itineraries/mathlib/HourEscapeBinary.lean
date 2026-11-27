module
public import HourEscapeWindows
import all HourEscapePacking
import all HourEscapeSigned
import all HourEscapeLimits
import all HourEscapeBranching
import all HourCycleShadow
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.HourEscape
open Collatz.HourCycleShadow
set_option autoImplicit false

def ForwardShadow (d : ℕ) (e : ℕ → ℕ) (y : ℕ → ℤ) : Prop :=
  ∀ i,(2:ℤ)^(e i)*y (i+1)=3*y i+d

private theorem forward_drift {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} (dp : 0<d)
    (path : ForwardShadow d e y) (balanced : BoundedClock e) :
    (∃ C : ℕ, ∀ n,(y n).natAbs≤C*(n+1)) ∧
    (∀ A : ℤ, ∃ N,∀ j,N≤j → A<y j) := by
  obtain ⟨K,w,kp,strip⟩ := balanced
  let v := fun n => (y n:ℝ)/w n
  have kr : 0<(K:ℝ) := by exact_mod_cast kp
  have dr : 0<(d:ℝ) := by exact_mod_cast dp
  have wp (n : ℕ) : 0<w n := by nlinarith only [(strip n).1,kr]
  have inc (n : ℕ) : v (n+1)-v n=(d:ℝ)/(3*w n) := by
    have eqn : (2:ℝ)^(e n)*(y (n+1):ℝ)=3*(y n:ℝ)+d := by exact_mod_cast path n
    have scale := (strip n).2.2
    dsimp [v]
    field_simp [ne_of_gt (wp n),ne_of_gt (wp (n+1))]
    linear_combination (w (n+1))*eqn-(y (n+1):ℝ)*scale
  have bound (n : ℕ) :
      v 0+(n:ℝ)*((d:ℝ)/(3*K))≤v n ∧ v n≤v 0+(n:ℝ)*(d*K) := by
    induction n with
    | zero => simp
    | succ n ih =>
      have denominator : 0<3*w n := mul_pos (by norm_num) (wp n)
      have low : (d:ℝ)/(3*K)≤d/(3*w n) := by
        apply (div_le_div_iff₀ (by positivity : 0<(3:ℝ)*K) denominator).mpr
        exact mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_left (strip n).2.1 (by norm_num)) dr.le
      have high : (d:ℝ)/(3*w n)≤d*K := by
        apply (div_le_iff₀ denominator).mpr
        nlinarith only [mul_le_mul_of_nonneg_left (strip n).1 dr.le]
      have step := inc n
      push_cast
      constructor <;> linarith only [ih.1,ih.2,step,low,high]
  have value (n : ℕ) : (y n:ℝ)=w n*v n := by dsimp [v]; field_simp [ne_of_gt (wp n)]
  constructor
  · obtain ⟨C,large⟩ := exists_nat_ge ((K:ℝ)*(|v 0|+d*K+1))
    refine ⟨C,fun n => ?_⟩
    have h := bound n
    have vb : |v n|≤|v 0|+(n:ℝ)*(d*K) := by
      apply abs_le.mpr
      constructor <;> nlinarith only [h.1,h.2,neg_abs_le (v 0),le_abs_self (v 0),
        show 0≤(n:ℝ)*((d:ℝ)/(3*K)) by positivity,show 0≤(n:ℝ)*(d*K) by positivity]
    have yb : |(y n:ℝ)|≤(K:ℝ)*(|v 0|+(n:ℝ)*(d*K)) := by
      rw [value,abs_mul,abs_of_pos (wp n)]
      exact mul_le_mul (strip n).2.1 vb (abs_nonneg _) kr.le
    have target : |(y n:ℝ)|≤((C*(n+1):ℕ):ℝ) := by
      push_cast
      nlinarith only [yb,large,mul_le_mul_of_nonneg_right large (Nat.cast_nonneg n),
        show 0≤(n:ℝ)*K*|v 0| by positivity,show 0≤(n:ℝ)*K by positivity,
        show 0≤(d:ℝ)*K*K by positivity,kr]
    have zi : |y n|≤((C*(n+1):ℕ):ℤ) := by exact_mod_cast target
    rw [←Int.natCast_natAbs] at zi
    exact_mod_cast zi
  · intro A
    let h : ℝ := d/(3*K)
    have hp : 0<h := by dsimp [h]; positivity
    obtain ⟨N,large⟩ := exists_nat_gt (((K:ℝ)*|(A:ℝ)|-v 0)/h)
    have above := (div_lt_iff₀ hp).mp large
    refine ⟨N,fun j late => ?_⟩
    have jr : (N:ℝ)≤j := by exact_mod_cast late
    have high : (K:ℝ)*|(A:ℝ)|<v j := by
      have lb := (bound j).1
      change v 0+(j:ℝ)*h≤v j at lb
      nlinarith only [above,lb,mul_le_mul_of_nonneg_right jr hp.le]
    have comp := mul_lt_mul_of_pos_left high (wp j)
    have unit := mul_le_mul_of_nonneg_right (strip j).1 (abs_nonneg (A:ℝ))
    have finish : (A:ℝ)<(y j:ℝ) := by rw [value]; nlinarith only [comp,unit,le_abs_self (A:ℝ)]
    exact_mod_cast finish

private theorem forward_dvd {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} (path : ForwardShadow d e y)
    (b i j : ℕ) (same : ∀ t,t<b → e (i+t)=e (j+t)) : (3:ℤ)^b∣y (i+b)-y (j+b) := by
  induction b with
  | zero => simp
  | succ b ih =>
    obtain ⟨v,hv⟩ := ih (fun t ht => same t (by omega))
    have eqn := same b (by omega)
    have left := path (i+b)
    have right := path (j+b)
    rw [←eqn] at right
    have scaled : (3:ℤ)^(b+1)∣2^(e (i+b))*(y (i+(b+1))-y (j+(b+1))) := by
      refine ⟨v,?_⟩
      rw [pow_succ]
      linear_combination left-right+3*hv
    have cop : IsCoprime (3:ℤ) 2 := ⟨1,-1,by norm_num⟩
    exact cop.pow.dvd_of_dvd_mul_left scaled

private theorem words_nonempty (s b : ℕ) (room : b≤s) : 0<(gapWords s b).length := by
  have mem : List.replicate b 1∈gapWords s b :=
    gapWords_mem (by simp) (by intro i hi; have eq := List.eq_of_mem_replicate hi; omega)
      (by simpa using room)
  exact List.length_pos_of_mem mem

private theorem words_enough (s b : ℕ) (room : b<s) : b+1≤(gapWords s b).length := by
  induction b generalizing s with
  | zero => exact words_nonempty s 0 (by omega)
  | succ b ih =>
    cases s with
    | zero => omega
    | succ s =>
      have a := words_nonempty s (b+1) (by omega)
      have c := ih s (by omega)
      simp only [gapWords,List.length_append,List.length_map]; omega

private theorem forward_unique {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} (odd : d%2=1)
    (pos : ∀ n,0<e n) (path : ForwardShadow d e y)
    (rises : ∀ A : ℤ,∃ N,∀ j,N≤j → A<y j) : Function.Injective y := by
  have oddY (i : ℕ) : y i%2=1 := by
    obtain ⟨r,eqn⟩ := Nat.exists_eq_add_of_le (show 1≤e i from pos i)
    have rr := path i
    rw [eqn,pow_add] at rr
    have h : 2*(2^r*y (i+1))=3*y i+d := by simpa only [pow_one,mul_assoc] using rr
    have dc : (d:ℤ)%2=1 := by exact_mod_cast odd
    omega
  have advance {i j : ℕ} (same : y i=y j) : y (i+1)=y (j+1) := by
    have l := path i
    rw [same] at l
    exact odd_part_unique (oddY _) (oddY _) (l.trans (path j).symm)
  have shift {i j : ℕ} (same : y i=y j) (r : ℕ) : y (i+r)=y (j+r) := by
    induction r with
    | zero => simpa using same
    | succ r ih => exact advance ih
  have ordered {i j : ℕ} (lt : i<j) (eqn : y i=y j) : False := by
    let p := j-i
    have per (r : ℕ) : y (i+r*p)=y i := by
      induction r with
      | zero => simp
      | succ r ih =>
        have h := shift eqn (r*p)
        rw [Nat.succ_mul,show i+(r*p+p)=j+r*p by dsimp [p]; omega]
        exact h.symm.trans ih
    obtain ⟨N,large⟩ := rises (y i)
    have room := Nat.le_mul_of_pos_right N (by dsimp [p]; omega : 0<p)
    have high := large (i+N*p) (by omega)
    rw [per] at high
    omega
  intro i j eqn
  rcases lt_trichotomy i j with hi|same|hj
  · exact False.elim (ordered hi eqn)
  · exact same
  · exact False.elim (ordered hj eqn.symm)

/-- A rational dyadic coordinate, whose reduced denominator is odd, cannot
have an infinite signed forward history in a bounded clock strip. -/
theorem no_rational_forward_balanced {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} (odd : d%2=1)
    (pos : ∀ i,0<e i) (path : ForwardShadow d e y) (balanced : BoundedClock e) : False := by
  obtain ⟨⟨C,linear⟩,rises⟩ := forward_drift (by omega) path balanced
  have inject := forward_unique odd pos path rises
  obtain ⟨K,w,_,strip⟩ := balanced
  let H := K*K
  obtain ⟨r,rp,room⟩ := strip_packing_room (2*C) 0 H
  let b := 5*r
  let words := gapWords (8*r+H) b
  let N := words.length+1
  let enc := fun i : Fin N => window e b i.val
  have member (i : Fin N) : enc i∈words := by
    apply strip_words_of_window pos
    have scale := window_factor (fun n => (strip n).2.2) i.val b
    have first := mul_le_mul_of_nonneg_left (strip (i.val+b)).1
      (show 0≤(2:ℝ)^(window e b i.val).sum by positivity)
    have last := mul_le_mul_of_nonneg_left (strip i.val).2.1 (show 0≤(3:ℝ)^b by positivity)
    have bound : (2:ℝ)^(window e b i.val).sum≤(K:ℝ)*K*3^b := by
      calc
        _ ≤ 2^(window e b i.val).sum*((K:ℝ)*w (i.val+b)) := by simpa using first
        _ = (K:ℝ)*(3^b*w i.val) := by rw [←scale]; ring
        _ ≤ (K:ℝ)*(3^b*K) := mul_le_mul_of_nonneg_left last (Nat.cast_nonneg K)
        _ = _ := by ring
    exact_mod_cast bound
  have many : b+1≤words.length := words_enough _ _ (by dsimp [b]; omega)
  have inj : Function.Injective enc := by
    intro i j eqn
    have hist : ∀ s,s<b → e (i.val+s)=e (j.val+s) := fun _ hs => window_agree eqn hs
    have dvd := Int.natAbs_dvd_natAbs.mpr (forward_dvd path b i.val j.val hist)
    simp only [Int.natAbs_pow] at dvd
    change 3^b∣(y (i.val+b)-y (j.val+b)).natAbs at dvd
    have size (i : Fin N) : (y (i.val+b)).natAbs≤(2*C)*(words.length+1) := by
      have le : i.val+b+1≤2*(words.length+1) := by have := i.isLt; dsimp [N] at this; omega
      simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using
        (linear (i.val+b)).trans (Nat.mul_le_mul_left C le)
    have capI := size i
    have capJ := size j
    have dist := Int.natAbs_sub_le (y (i.val+b)) (y (j.val+b))
    change 2*((2*C)*(words.length+0+1))<3^b at room
    simp only [Nat.add_zero] at room
    have short : (y (i.val+b)-y (j.val+b)).natAbs<3^b := by omega
    have zero := Nat.eq_zero_of_dvd_of_lt dvd short
    have nq : y (i.val+b)=y (j.val+b) := by omega
    have equal := inject nq
    apply Fin.ext
    omega
  have sub : List.ofFn enc⊆words := by
    intro x hx; obtain ⟨i,rfl⟩ := List.mem_ofFn.mp hx; exact member i
  have count := (List.nodup_ofFn_ofInjective inj).length_le_of_subset sub
  simp only [List.length_ofFn] at count
  dsimp [N] at count
  omega

#print axioms no_rational_forward_balanced
end Collatz.Itinerary.HourEscape
