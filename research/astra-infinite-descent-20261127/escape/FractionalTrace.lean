import OriginalLoss

/-! The finite incoming-word algebra of the marked PR193 row difference.
All sums are cut at a supplied total number of initial halving exponents. -/
set_option autoImplicit false
set_option warningAsError true
namespace FractionalTrace
open Finset

noncomputable def bit (a t : ℝ) : ℝ := if a≤t then 1 else 0
noncomputable def selector (n : ℕ) : ℝ := (n%3:ℕ)
noncomputable def term (e n : ℕ) (h t : ℝ) : ℝ :=
  if (2^e*n)%3=1 then 3/(2:ℝ)^e*selector ((2^e*n-1)/3)*bit (((n:ℝ)-1/(2:ℝ)^e)*h) t
  else 0
noncomputable def raw (E n : ℕ) (h t : ℝ) : ℝ :=
  (∑i∈range E,term (i+1) n h t)-selector n*bit ((n:ℝ)*h) t

theorem cancel_long (e n : ℕ) (h t : ℝ) :
    term (e+1) n h t=term e (2*n) (h/2) t/2 := by
  have power : 2^(e+1)*n=2^e*(2*n) := by rw [pow_succ]; ring
  have pos : (2:ℝ)^e≠0 := by positivity
  have loc : ((n:ℝ)-1/(2:ℝ)^(e+1))*h=(((2*n:ℕ):ℝ)-1/(2:ℝ)^e)*(h/2) := by
    push_cast
    rw [pow_succ]
    field_simp
  unfold term
  rw [power,loc]
  split
  · rw [pow_succ]
    field_simp
  · norm_num

theorem exact_remainder (E n : ℕ) (h t : ℝ) :
    raw (E+1) n h t-raw E (2*n) (h/2) t/2 =
      term 1 n h t+(selector (2*n)/2-selector n)*bit ((n:ℝ)*h) t := by
  have loc : ((2*n:ℕ):ℝ)*(h/2)=(n:ℝ)*h := by push_cast; ring
  have sum : (∑i∈range E,term (i+1+1) n h t)=
      (∑i∈range E,term (i+1) (2*n) (h/2) t)/2 := by
    simp_rw [cancel_long (n:=n)]
    rw [Finset.sum_div]
  unfold raw
  rw [sum_range_succ',sum,loc]
  simp only [Nat.zero_add]
  ring

/-- The residual at the three supported classes. The negative class has
zero incoming birth. The positive classes have one and two births. -/
theorem three_classes (k E : ℕ) (h t : ℝ) :
    (∀ r∈({2,5,8}:Finset ℕ),
      raw (E+1) (9*k+r) h t-raw E (2*(9*k+r)) (h/2) t/2 =
      (3:ℝ)/2*(selector ((2*(9*k+r)-1)/3)*bit (((9*k+r:ℕ):ℝ)*h-h/2) t
                        -bit (((9*k+r:ℕ):ℝ)*h) t)) ∧
    selector ((2*(9*k+2)-1)/3)=1 ∧ selector ((2*(9*k+5)-1)/3)=0 ∧
      selector ((2*(9*k+8)-1)/3)=2 := by
  constructor
  · intro r hr
    have two : r=2 ∨ r=5 ∨ r=8 := by simpa using hr
    have rem : (9*k+r)%3=2 := by omega
    have dbl : (2*(9*k+r))%3=1 := by omega
    have loc : (((9*k+r:ℕ):ℝ)-1/2)*h=((9*k+r:ℕ):ℝ)*h-h/2 := by ring
    rw [exact_remainder]
    simp only [term,pow_one,dbl,ite_true,loc,selector,rem,Nat.cast_one,Nat.cast_ofNat]
    ring
  · unfold selector
    norm_cast
    omega

theorem silent_classes (E n : ℕ) (h t : ℝ) (other : n%3≠2) :
    raw (E+1) n h t-raw E (2*n) (h/2) t/2=0 := by
  have gone : (2*n)%3≠1 := by omega
  have eq : (2*n)%3=2*(n%3) := by omega
  rw [exact_remainder]
  have zero : term 1 n h t=0 := by simp only [term,pow_one,gone,ite_false]
  rw [zero]
  simp only [selector,eq,Nat.cast_mul,Nat.cast_ofNat]
  ring

theorem synced_sign (k : ℕ) (h t v : ℝ) (hp : 0≤h) (vp : 0≤v) :
    v*bit ((((9*k+8:ℕ):ℝ)-1/2)*h) t-v*bit (((9*k+5:ℕ):ℝ)*h) t≤0 := by
  have earlier : ((9*k+5:ℕ):ℝ)*h≤(((9*k+8:ℕ):ℝ)-1/2)*h := by
    push_cast
    linarith
  unfold bit
  split
  · rename_i positive
    rw [ite_eq_left (earlier.trans positive)]
    simp
  · split <;> linarith

#print axioms cancel_long
#print axioms exact_remainder
#print axioms three_classes
#print axioms silent_classes
#print axioms synced_sign
end FractionalTrace
