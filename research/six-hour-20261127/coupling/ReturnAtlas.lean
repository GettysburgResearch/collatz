import EarlierOffsets

/-! A checker for complete mixed-radix ordinary descent words. Only a
directed move at 1 modulo 16 consumes the original cofactor budget. -/
set_option autoImplicit false
set_option warningAsError true
set_option maxHeartbeats 500000
namespace ReturnAtlas
open CoreBranching
open EarlierOffsets (Good good_run)

structure Row where
  a : ℕ
  b : ℕ
deriving DecidableEq, Repr

def value (r : Row) (t : ℕ) := r.a*t+r.b
def sub (r : Row) (m i : ℕ) : Row := ⟨r.a*m,r.a*i+r.b⟩

inductive Move where
  | forward (e : ℕ)
  | backward (e : ℕ)
  | charge
deriving DecidableEq, Repr

def next (r : Row) : Move → Row
  | .forward e => ⟨3*r.a/2^e,(3*r.b+1)/2^e⟩
  | .backward e => ⟨2^e*r.a/3,(2^e*r.b-1)/3⟩
  | .charge => ⟨3*r.a,3*r.b⟩

def Realizes (e : ℕ) (r s : Row) : Prop :=
  0<e ∧ r.a%2=0 ∧ r.b%2=1 ∧ 2^e*s.a=3*r.a ∧ 2^e*s.b=3*r.b+1

instance (e : ℕ) (r s : Row) : Decidable (Realizes e r s) := by unfold Realizes; infer_instance

def Legal (K : ℕ) (root r : Row) : Move → Prop
  | .forward e => Realizes e r (next r (.forward e))
  | .backward e => Realizes e (next r (.backward e)) r
  | .charge => r.a%16=0 ∧ r.b%16=1 ∧ r.a≤K*root.a ∧ r.b≤K*root.b

instance (K : ℕ) (root r : Row) (m : Move) : Decidable (Legal K root r m) := by
  cases m <;> unfold Legal <;> infer_instance

private theorem halves (n x : ℕ) : run n (2^n*x)=x := by
  induction n with
  | zero => simp [run]
  | succ n ih => rw [pow_succ,show 2^n*2*x=2*(2^n*x) by ring,run,step_double,ih]

/-- A checked directed physical odd block may end at an even integer. -/
theorem realizes_run (e : ℕ) (r s : Row) (h : Realizes e r s) (t : ℕ) :
    run e (value r t)=value s t := by
  obtain ⟨ep,ae,bo,sa,sb⟩:=h
  have parity : value r t%2=1 := by
    rw [value,Nat.add_mod,Nat.mul_mod,ae,bo]; simp
  have eq : 2^e*value s t=3*value r t+1 := by
    unfold value
    rw [Nat.mul_add,←mul_assoc,sa,sb]
    ring
  cases e with
  | zero => omega
  | succ e =>
    have st : step (value r t)=2^e*value s t := by
      have odd : value r t%2≠0 := by omega
      simp only [step,odd,ite_false] ; rw [←eq,pow_succ]
      rw [show 2^e*2*value s t=2*(2^e*value s t) by ring]
      omega
    rw [run,st,halves]

def Charged (K n : ℕ) : Prop := ∀ w, w%16=1 → w≤K*n → Good (3*w) → Good w

private theorem move_good (K : ℕ) (root r : Row) (m : Move) (t : ℕ)
    (ok : Legal K root r m) (hyp : Charged K (value root t)) :
    Good (value (next r m) t) → Good (value r t) := by
  cases m with
  | forward e =>
    have eq:=realizes_run e r _ ok t
    rw [←eq]; exact (good_run _ _).mp
  | backward e =>
    have eq:=realizes_run e _ r ok t
    rw [←eq]; exact (good_run _ _).mpr
  | charge =>
    rcases ok with ⟨ma,mb,ca,cb⟩
    have same : value (next r .charge) t=3*value r t := by simp [next,value]; ring
    have modW : value r t%16=1 := by rw [value,Nat.add_mod,Nat.mul_mod,ma,mb]; simp
    have le := Nat.add_le_add (Nat.mul_le_mul_right t ca) cb
    rw [same]
    apply hyp _ modW
    unfold value
    simpa only [Nat.mul_add,mul_assoc] using le

def Finish (root cur : Row) : Prop := 0<cur.b ∧ cur.a≤root.a ∧ cur.b<root.b

instance (r s : Row) : Decidable (Finish r s) := by unfold Finish; infer_instance

def checkWord (K : ℕ) (root : Row) : Row → List Move → Bool
  | cur,[] => decide (Finish root cur)
  | cur,m::rest => decide (Legal K root cur m) && checkWord K root (next cur m) rest

theorem word_sound (K : ℕ) (root cur : Row) (word : List Move) (t : ℕ)
    (ok : checkWord K root cur word=true) (hyp : Charged K (value root t)) :
    ∃ y, 0<y ∧ y<value root t ∧ (Good y → Good (value cur t)) := by
  induction word generalizing cur with
  | nil =>
    have fin : Finish root cur := of_decide_eq_true ok
    obtain ⟨p,a,b⟩:=fin
    exact ⟨value cur t,by unfold value; omega,
      Nat.add_lt_add_of_le_of_lt (Nat.mul_le_mul_right t a) b,id⟩
  | cons m rest ih =>
    simp only [checkWord,Bool.and_eq_true,decide_eq_true_eq] at ok
    obtain ⟨y,yp,yl,meet⟩:=ih _ ok.2
    exact ⟨y,yp,yl,(move_good K root cur m t ok.1 hyp).comp meet⟩

inductive Tree where
  | leaf (word : List Move)
  | two (left right : Tree)
  | three (zero one two : Tree)

def check (K : ℕ) : Tree → Row → Bool
  | .leaf w,r => checkWord K r r w
  | .two a b,r => check K a (sub r 2 0) && check K b (sub r 2 1)
  | .three a b c,r => check K a (sub r 3 0) && check K b (sub r 3 1) && check K c (sub r 3 2)

private theorem split (r : Row) (t k i : ℕ) (e : t%k=i) :
    value r t=value (sub r k i) (t/k) := by
  have eq := Nat.mod_add_div t k
  rw [e] at eq
  unfold value sub
  dsimp only
  nth_rw 1 [←eq]
  ring

theorem tree_sound (K : ℕ) (tree : Tree) (r : Row) (t : ℕ) (ok : check K tree r=true) :
    Charged K (value r t) →
    ∃ y, 0<y ∧ y<value r t ∧ (Good y → Good (value r t)) := by
  induction tree generalizing r t with
  | leaf w => exact word_sound K r r w t ok
  | two a b ia ib =>
    simp only [check,Bool.and_eq_true] at ok
    rcases (show t%2=0 ∨ t%2=1 by omega) with e|e
    · rw [split r t 2 0 e]; exact ia _ _ ok.1
    · rw [split r t 2 1 e]; exact ib _ _ ok.2
  | three a b c ia ib ic =>
    simp only [check,Bool.and_eq_true] at ok
    rcases (show t%3=0 ∨ t%3=1 ∨ t%3=2 by omega) with e|e|e
    · rw [split r t 3 0 e]; exact ia _ _ ok.1.1
    · rw [split r t 3 1 e]; exact ib _ _ ok.1.2
    · rw [split r t 3 2 e]; exact ic _ _ ok.2

/-- A generic checked return tree yields an actual ordered disagreement in
the prescribed binary class at an original-source-relative height. -/
theorem bounded_return (K : ℕ) (tree : Tree) (ok : check K tree ⟨2,3⟩=true)
    (n : ℕ) (positive : 0<n) (bad : ¬Good n) :
    ∃ w, 0<w ∧ w%16=1 ∧ w≤K*n ∧ ¬Good w ∧ Good (3*w) := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases one : n=1
    · subst n; exact (bad ⟨0,rfl⟩).elim
    by_cases ev : n%2=0
    · have e : n=2*(n/2) := by omega
      have bn : ¬Good (n/2) := by
        intro small
        apply bad
        apply (good_run 1 n).mp
        change Good (step n)
        rw [e,step_double]
        simpa only [Nat.mul_div_cancel_left _ (by decide : 0<2)] using small
      obtain ⟨w,wp,wm,wl,b,g⟩:=ih (n/2) (by omega) (by omega) bn
      exact ⟨w,wp,wm,wl.trans (Nat.mul_le_mul_left _ (Nat.div_le_self _ _)),b,g⟩
    · let t := (n-3)/2
      have eq : value ⟨2,3⟩ t=n := by dsimp [value,t]; omega
      by_cases hc : Charged K n
      · have ch := tree_sound K tree ⟨2,3⟩ t ok
        rw [eq] at ch
        obtain ⟨y,yp,yl,back⟩:=ch hc
        obtain ⟨w,wp,wm,wl,b,g⟩:=ih y yl yp (fun gy => bad (back gy))
        exact ⟨w,wp,wm,wl.trans (Nat.mul_le_mul_left _ yl.le),b,g⟩
      · unfold Charged at hc
        push Not at hc
        obtain ⟨w,wm,wl,g,b⟩:=hc
        exact ⟨w,by omega,wm,wl,b,g⟩

#print axioms realizes_run
#print axioms word_sound
#print axioms tree_sound
#print axioms bounded_return
end ReturnAtlas
