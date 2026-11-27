import Portal

namespace Collatz.SignedCenter

open TernaryPortal (run step odds)

/-- The current signed value is a/3^k. The trace stops at the first integral state. -/
inductive Strip : Nat → Int → Nat → Int → Prop where
  | done (a : Int) : Strip 0 a 0 a
  | even {k t : Nat} {a b c : Int} (unit : a % 3 ≠ 0) (halve : a = 2*b)
      (tail : Strip (k+1) b t c) : Strip (k+1) a (t+1) c
  | odd {k t : Nat} {a b c : Int} (unit : a % 3 ≠ 0) (parity : a % 2 = 1)
      (next : a + 3^k = 2*b) (tail : Strip k b t c) : Strip (k+1) a (t+1) c

private theorem odd_three (k : Nat) : (3:Int)^k % 2 = 1 := by
  induction k with
  | zero => decide
  | succ k ih => rw [pow_succ,Int.mul_emod,ih]; decide

/-- Every nonintegral reduced state attains an integral state. -/
theorem strip_exists (k : Nat) (a : Int) (unit : 0 < k → a % 3 ≠ 0) :
    ∃ t c, Strip k a t c := by
  induction k generalizing a with
  | zero => exact ⟨0,a,.done a⟩
  | succ k ih =>
    have hu := unit (Nat.succ_pos k)
    clear unit
    generalize hm : a.natAbs = m
    induction m using Nat.strong_induction_on generalizing a with
    | h m inner =>
      by_cases even : a%2=0
      · let b := a/2
        have eq : a=2*b := by dsimp [b]; omega
        have ub : b%3≠0 := by omega
        have bn : b≠0 := by omega
        have positive := Int.natAbs_pos.mpr bn
        have sizes : a.natAbs=2*b.natAbs := by rw [eq,Int.natAbs_mul]; rfl
        obtain ⟨t,c,tail⟩ := inner b.natAbs (by omega) b ub rfl
        exact ⟨t+1,c,.even hu eq tail⟩
      · have odd : a%2=1 := by omega
        let b := (a+3^k)/2
        have par := odd_three k
        have eq : a+3^k=2*b := by dsimp [b]; omega
        have ub : 0<k → b%3≠0 := by
          intro pos
          obtain ⟨j,hj⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : k≠0)
          rw [hj,pow_succ] at eq
          omega
        obtain ⟨t,c,tail⟩ := ih b ub
        exact ⟨t+1,c,.odd hu odd eq tail⟩

def allowance : Nat → Nat
  | 0 => 1
  | k+1 => (1+3^k)*allowance k

/-- Time and absolute integral exit height obey a single computable bound. -/
theorem strip_budget {k t : Nat} {a c : Int} (tr : Strip k a t c) :
    2^t*max 1 c.natAbs ≤ max 1 a.natAbs*allowance k := by
  induction tr with
  | done => simp [allowance]
  | @even k t a b c unit eq tail ih =>
    have bn : b≠0 := by omega
    have bp := Int.natAbs_pos.mpr bn
    have sizes : a.natAbs=2*b.natAbs := by rw [eq,Int.natAbs_mul]; rfl
    have scaled := Nat.mul_le_mul_left 2 ih
    rw [show max 1 b.natAbs=b.natAbs from max_eq_right bp] at scaled
    rw [show max 1 a.natAbs=a.natAbs from max_eq_right (by omega),sizes,pow_succ]
    calc
      _ = 2*(2^t*max 1 c.natAbs) := by ring
      _ ≤ 2*(b.natAbs*allowance (k+1)) := scaled
      _ = _ := by ring
  | @odd k t a b c unit parity eq tail ih =>
    have ap := Int.natAbs_pos.mpr (by omega : a≠0)
    have pp : 0 < (3:Nat)^k := Nat.pow_pos (by decide)
    have sizes : 2*b.natAbs ≤ a.natAbs+3^k := by
      have h := Int.natAbs_add_le a (3^k)
      rw [eq,Int.natAbs_mul,Int.natAbs_pow] at h
      exact h
    have gap : 2*max 1 b.natAbs ≤ a.natAbs*(1+3^k) := by
      rw [Nat.mul_add,Nat.mul_one]
      have mult := Nat.mul_le_mul_right (3^k) (by omega : 1≤a.natAbs)
      simp only [one_mul] at mult
      omega
    have scaled := Nat.mul_le_mul_left 2 ih
    have paid := Nat.mul_le_mul_right (allowance k) gap
    rw [show max 1 a.natAbs=a.natAbs from max_eq_right ap,allowance,pow_succ]
    calc
      _ = 2*(2^t*max 1 c.natAbs) := by ring
      _ ≤ 2*(max 1 b.natAbs*allowance k) := scaled
      _ = (2*max 1 b.natAbs)*allowance k := by ring
      _ ≤ a.natAbs*(1+3^k)*allowance k := paid
      _ = _ := by ring

private theorem input_parity {k : Nat} {z : Nat} {q a : Int}
    (eq : (3:Int)^k*z=2*q+a) : (z:Int)%2=a%2 := by
  have coeff := odd_three k
  have split : (3:Int)^k=2*(3^k/2)+1 := by omega
  rw [split,add_mul,mul_assoc,one_mul] at eq
  omega

private theorem pos_step {z : Nat} (hz : 0<z) : 0<step z := by
  unfold step
  split <;> omega

/-- An adequate binary reserve lifts the whole signed trace at the supplied positive
ordinary source. It records the actual lower endpoint, strict positivity, and odd grade. -/
theorem strip_lift {k t d z : Nat} {a c q : Int} (tr : Strip k a t c) (hz : 0<z)
    (interval : (3:Int)^k*z=2^(t+d)*q+a) :
    0<run t z ∧ (run t z:Int)=2^d*q+c ∧ odds t z=k := by
  induction tr generalizing z with
  | done => simpa [run,odds] using And.intro hz interval
  | @even k t a b c unit eq tail ih =>
    have power : (2:Int)^(t+1+d)=2*2^(t+d) := by rw [show t+1+d=(t+d)+1 by omega,pow_succ]; ring
    rw [power,mul_assoc] at interval
    have parity := input_parity interval
    rw [eq] at parity interval
    have e : z%2=0 := by omega
    have next : (z:Int)=2*(step z:Int) := by simp [step,e]; omega
    have link : (3:Int)^(k+1)*(step z:Int)=2^(t+d)*q+b := by
      rw [next] at interval
      have double : 2*((3:Int)^(k+1)*(step z:Int))=2*(2^(t+d)*q+b) := by
        linear_combination interval
      omega
    obtain ⟨positive,endpoint,grade⟩ := ih (pos_step hz) link
    simpa [run,odds,e,grade] using And.intro positive endpoint
  | @odd k t a b c unit odd eq tail ih =>
    have power : (2:Int)^(t+1+d)=2*2^(t+d) := by rw [show t+1+d=(t+d)+1 by omega,pow_succ]; ring
    rw [power,mul_assoc] at interval
    have parity := input_parity interval
    have o : z%2=1 := by omega
    have next : 2*(step z:Int)=3*z+1 := by simp [step,o]; omega
    have link : (3:Int)^k*(step z:Int)=2^(t+d)*q+b := by
      rw [pow_succ] at interval
      have double : 2*(3^k*(step z:Int))=2*(2^(t+d)*q+b) := by
        linear_combination interval + (3:Int)^k*next + eq
      omega
    obtain ⟨positive,endpoint,grade⟩ := ih (pos_step hz) link
    exact ⟨positive,endpoint,by simp only [odds,o,grade]; omega⟩

/-- A negative exit implies that the entire trace stayed strictly negative.
The binary reserve then pays for every clock without an odd-step allowance. -/
theorem negative_exit {k t : Nat} {a c : Int} (tr : Strip k a t c) (hc : c<0) :
    (2:Int)^t*(-c) ≤ -a := by
  induction tr with
  | done => simp
  | @even k t a b c _ eq _ ih =>
    rw [eq,pow_succ]
    have h := mul_le_mul_of_nonneg_left (ih hc) (by decide : (0:Int)≤2)
    linear_combination h
  | @odd k t a b c _ _ eq _ ih =>
    rw [pow_succ]
    have h := mul_le_mul_of_nonneg_left (ih hc) (by decide : (0:Int)≤2)
    have p := pow_nonneg (by decide : (0:Int)≤3) k
    linear_combination h + p + eq

/-- At a complete upper hit of one the offset is strictly smaller than the
full binary scale. Therefore a negative integral exit always lifts at the
actual original source, even without a long final run of halvings. -/
theorem full_negative_lift {k t H z : Nat} {a c : Int} (tr : Strip k a t c)
    (hc : c<0) (hz : 0<z) (full : (3:Int)^k*z=2^H+a) :
    t<H ∧ 0<run t z ∧ (run t z:Int)=2^(H-t)+c ∧ odds t z=k := by
  have neg := negative_exit tr hc
  have p := mul_pos (pow_pos (by decide : (0:Int)<3) k) (show 0 < (z:Int) by exact_mod_cast hz)
  have p2 := pow_nonneg (by decide : (0:Int)≤2) t
  have one := mul_le_mul_of_nonneg_left (by omega : (1:Int) ≤ -c) p2
  rw [mul_one] at one
  have lt : (2:Int)^t < 2^H := by omega
  have clk : t<H := (pow_lt_pow_iff_right₀ (by decide : (1:Int)<2)).mp lt
  have split : t+(H-t)=H := by omega
  have lift := strip_lift (d:=H-t) (q:=1) tr hz (by simpa [split] using full)
  simpa using And.intro clk lift

/-- Reaching k odd departures within the physical budget forces the full signed
reduction to finish within that budget at the very same source. -/
theorem strip_by_grade {k H z : Nat} {a q : Int}
    (unit : 0<k → a%3≠0) (eq : (3:Int)^k*z=2^H*q+a)
    (grade : k≤odds H z) : ∃ t c, Strip k a t c ∧ t≤H := by
  induction H generalizing k z a with
  | zero =>
    change k≤0 at grade
    obtain rfl : k=0 := by omega
    exact ⟨0,a,.done a,Nat.le_refl _⟩
  | succ H ih =>
    cases k with
    | zero => exact ⟨0,a,.done a,Nat.zero_le _⟩
    | succ k =>
      have hu := unit (Nat.succ_pos k)
      rw [show (2:Int)^(H+1)=2*2^H by ring,mul_assoc] at eq
      have same := input_parity eq
      rw [odds] at grade
      by_cases e : z%2=0
      · let b := a/2
        have even : a=2*b := by dsimp [b]; omega
        have ub : b%3≠0 := by omega
        have next : (z:Int)=2*(step z:Int) := by simp [step,e]; omega
        rw [next,even] at eq
        have double : 2*((3:Int)^(k+1)*(step z:Int))=2*(2^H*q+b) := by
          linear_combination eq
        obtain ⟨t,c,tail,bound⟩ := ih (k:=k+1) (a:=b) (z:=step z)
          (fun _ => ub) (by omega) (by omega)
        exact ⟨t+1,c,.even hu even tail,by omega⟩
      · let b := (a+3^k)/2
        have o : z%2=1 := by omega
        have odd : a%2=1 := by omega
        have three := odd_three k
        have succ : a+3^k=2*b := by dsimp [b]; omega
        have ub : 0<k → b%3≠0 := by
          intro pos
          obtain ⟨j,hj⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : k≠0)
          rw [hj,pow_succ] at succ
          omega
        have next : 2*(step z:Int)=3*z+1 := by simp [step,o]; omega
        rw [pow_succ] at eq
        have double : 2*((3:Int)^k*(step z:Int))=2*(2^H*q+b) := by
          linear_combination eq + (3:Int)^k*next + succ
        obtain ⟨t,c,tail,bound⟩ := ih (k:=k) (a:=b) (z:=step z)
          ub (by omega) (by omega)
        exact ⟨t+1,c,.odd hu odd succ tail,by omega⟩

#print axioms strip_by_grade
#print axioms negative_exit
#print axioms full_negative_lift
#print axioms strip_exists
#print axioms strip_budget
#print axioms strip_lift

end Collatz.SignedCenter
