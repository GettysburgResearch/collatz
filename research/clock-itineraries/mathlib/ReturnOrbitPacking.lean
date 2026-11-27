module
public import HourEscapeBinaryWindows
public import ReturnOrbitCensus
import all HourEscapeBinary
import all HourEscapeLimits
import all HourEscapePacking
import all HourEscapeSigned
import all HourCycleShadow
import Mathlib.Tactic

public section
namespace Collatz.Itinerary.HourEscape
open Collatz.HourCycleShadow
set_option autoImplicit false

/-- A multiplicative strip incurs only this many additional binary digits
in the budget for the gaps in a short block. -/
def stripPadding (K : ℕ) := (K*K).log2+1

theorem padding_cost {K : ℕ} (kp : 0<K) : 19^(stripPadding K)≤19*K^10 := by
  let s := (K*K).log2
  have l : 2^s≤K*K := Nat.log2_self_le (ne_of_gt (Nat.mul_pos kp kp))
  have c : 19^s≤32^s := Nat.pow_le_pow_left (by decide) _
  have eqn : (32:ℕ)^s=(2^s)^5 := by
    change ((2:ℕ)^5)^s=_
    rw [←Nat.pow_mul,←Nat.pow_mul,Nat.mul_comm]
  rw [eqn] at c
  have powered := c.trans (Nat.pow_le_pow_left l 5)
  change 19^(s+1)≤_
  rw [Nat.pow_succ]
  calc
    _ ≤ (K*K)^5*19 := Nat.mul_le_mul_right 19 powered
    _ = _ := by ring

set_option exponentiation.threshold 1000 in
private theorem padded_strip_words {u : ℕ → ℕ} {K : ℕ} (pos : ∀ i,0<u i)
    (r i : ℕ) (reduced : 2^(window u (200*r) i).sum≤(K*K)*3^(200*r)) :
    window u (200*r) i∈gapWords (317*r+stripPadding K) (200*r) := by
  apply gapWords_mem (win_length u (200*r) i) (win_positive pos (200*r) i)
  have left : 3^(200*r)≤2^(317*r) := by
    rw [Nat.pow_mul,Nat.pow_mul]; exact Nat.pow_le_pow_left (by decide) r
  have right : K*K≤2^(stripPadding K) := Nat.lt_log2_self.le
  have goal := reduced.trans (Nat.mul_le_mul right left)
  rw [←Nat.pow_add,Nat.add_comm (stripPadding K)] at goal
  exact (Nat.pow_le_pow_iff_right (by decide : 1<2)).mp goal

/-- Choose a short gap block whose ternary modulus exceeds the possible signed
diameter, but whose word census fits in the requested sample. -/
theorem finite_packing_scale {H D n : ℕ} (dp : 0<D) (np : 0<n)
    (big : ((19^H)*4)^20*((3^200)*D)^19<n) :
    ∃ r, 0<r ∧ D*n<3^(200*r) ∧ 200*r+(gapWords (317*r+H) (200*r)).length+1≤n := by
  have ex : ∃ r, D*n<(3^200)^r := ⟨D*n, by
    have l := Nat.lt_two_pow_self (n:=D*n)
    exact l.trans_le (Nat.pow_le_pow_left (by decide) _)⟩
  let r := Nat.find ex
  have lower : D*n<(3^200)^r := Nat.find_spec ex
  have rp : 0<r := by
    by_contra! hz
    have eq : r=0 := by omega
    rw [eq,pow_zero] at lower
    have := Nat.mul_pos dp np
    omega
  have prior : (3^200)^(r-1)≤D*n := by
    simpa only [not_lt] using Nat.find_min ex (m:=r-1) (by omega : r-1<r)
  have upper : (3^200)^r≤((3^200)*D)*n := by
    have id : r-1+1=r := by omega
    calc
      _ = (3^200)^((r-1)+1) := congrArg (fun j : ℕ => (3^200:ℕ)^j) id.symm
      _ = (3^200)^(r-1)*(3^200) := Nat.pow_succ _ _
      _ ≤ (D*n)*(3^200) := Nat.mul_le_mul_right _ prior
      _ = _ := (Nat.mul_comm _ _).trans (Nat.mul_assoc _ _ _).symm
  let W := (gapWords (317*r+H) (200*r)).length
  have powW : W^20≤(19^H)^20*((3^200)^r)^19 := by
    simpa only [Nat.pow_mul] using sharp_census_power r H
  have cap := powW.trans (Nat.mul_le_mul_left _ (Nat.pow_le_pow_left upper 19))
  have strict : (4*W)^20<n^20 := by
    rw [mul_pow]
    calc
      _ ≤ 4^20*((19^H)^20*(((3^200)*D)*n)^19) := Nat.mul_le_mul_left _ cap
      _ = (((19^H)*4)^20*((3^200)*D)^19)*n^19 := by ring
      _ < n*n^19 := Nat.mul_lt_mul_of_pos_right big (by positivity)
      _ = n^20 := by ring
  have sw : 4*W<n := by
    by_contra! h
    exact (Nat.not_le_of_lt strict) (Nat.pow_le_pow_left h 20)
  have many : 200*r+1≤W := words_enough _ _ (by omega)
  refine ⟨r,rp,?_,by omega⟩
  simpa only [Nat.pow_mul] using lower

private theorem finite_forward_dvd {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ}
    {T b i j : ℕ} (path : ∀ k,k<T → (2:ℤ)^(e k)*y (k+1)=3*y k+d)
    (hi : i+b≤T) (hj : j+b≤T) (same : ∀ t,t<b → e (i+t)=e (j+t)) :
    (3:ℤ)^b∣y (i+b)-y (j+b) := by
  induction b with
  | zero => simp
  | succ b ih =>
    obtain ⟨v,hv⟩ := ih (by omega) (by omega) (fun t ht => same t (by omega))
    have eqn := same b (by omega)
    have left := path (i+b) (by omega)
    have right := path (j+b) (by omega)
    rw [←eqn] at right
    have scaled : (3:ℤ)^(b+1)∣2^(e (i+b))*(y (i+(b+1))-y (j+(b+1))) := by
      refine ⟨v,?_⟩
      rw [pow_succ]
      linear_combination left-right+3*hv
    have cop : IsCoprime (3:ℤ) 2 := ⟨1,-1,by norm_num⟩
    exact cop.pow.dvd_of_dvd_mul_left scaled

/-- Determinism up to a finite horizon suffices for injection before a new
extreme. A prior repeat traps all the subsequent states in the old block. -/
theorem distinct_before_extreme {α : Type} {y : ℕ → α} {n T : ℕ}
    (advance : ∀ i j, i<T → j<T → y i=y j → y (i+1)=y (j+1))
    (away : ∀ i,i≤n → y i≠y T) (_room : n≤T) :
    ∀ i j, i≤n → j≤n → y i=y j → i=j := by
  have solve {i j : ℕ} (lt : i<j) (hj : j≤n) (eqn : y i=y j) : False := by
    have shift (s : ℕ) (fits : j+s≤T) : y (i+s)=y (j+s) := by
      induction s with
      | zero => simpa using eqn
      | succ s ih => exact advance (i+s) (j+s) (by omega) (by omega) (ih (by omega))
    have wrap (k : ℕ) (ht : k≤T) : ∃ a, a≤n ∧ y a=y k := by
      induction k using Nat.strong_induction_on with
      | h k ih =>
        by_cases small : k≤j
        · exact ⟨k,by omega,rfl⟩
        · have h := shift (k-j) (by omega)
          rw [show j+(k-j)=k by omega] at h
          obtain ⟨a,ha,hv⟩ := ih (i+(k-j)) (by omega) (by omega)
          exact ⟨a,ha,hv.trans h⟩
    obtain ⟨a,ha,hv⟩ := wrap T (by omega)
    exact away a ha hv
  intro i j hi hj eqn
  rcases lt_trichotomy i j with l|s|r
  · exact False.elim (solve l hj eqn)
  · exact s
  · exact False.elim (solve r hi eqn.symm)

/-- Equal short scripts force equal ternary residues at their two endpoints.
The census can therefore contain every tested source only if a large signed
distance or an actual repetition occurs. -/
theorem finite_forward_packing {d K n T r : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ}
    (path : ∀ k,k<T → (2:ℤ)^(e k)*y (k+1)=3*y k+d)
    (room : n≤T) (cap : 200*r+(gapWords (317*r+stripPadding K) (200*r)).length+1≤n)
    (pos : ∀ i,0<e i)
    (strip : ∀ i, i+200*r≤n → 2^(window e (200*r) i).sum≤(K*K)*3^(200*r))
    (short : ∀ i j,i≤n → j≤n → (y i-y j).natAbs<3^(200*r))
    (distinct : ∀ i j,i≤n → j≤n → y i=y j → i=j) : False := by
  let b := 200*r
  let words := gapWords (317*r+stripPadding K) b
  let N := words.length+1
  let enc := fun i : Fin N => window e b i.val
  have fits (i : Fin N) : i.val+b≤n := by have := i.isLt; dsimp [N,words,b] at *; omega
  have member (i : Fin N) : enc i∈words := padded_strip_words pos r i.val (strip i.val (fits i))
  have inj : Function.Injective enc := by
    intro i j eqn
    have hist : ∀ s,s<b → e (i.val+s)=e (j.val+s) := fun _ hs => window_agree eqn hs
    have dvd := Int.natAbs_dvd_natAbs.mpr
      (finite_forward_dvd path ((fits i).trans room) ((fits j).trans room) hist)
    simp only [Int.natAbs_pow] at dvd
    change 3^b∣(y (i.val+b)-y (j.val+b)).natAbs at dvd
    have zero := Nat.eq_zero_of_dvd_of_lt dvd (short _ _ (fits i) (fits j))
    have equal := distinct _ _ (fits i) (fits j) (by omega)
    apply Fin.ext; omega
  have sub : List.ofFn enc⊆words := by
    intro x hx; obtain ⟨i,rfl⟩ := List.mem_ofFn.mp hx; exact member i
  have count := (List.nodup_ofFn_ofInjective inj).length_le_of_subset sub
  simp only [List.length_ofFn] at count
  dsimp [N] at count
  omega

#print axioms finite_packing_scale
#print axioms finite_forward_packing
end Collatz.Itinerary.HourEscape
