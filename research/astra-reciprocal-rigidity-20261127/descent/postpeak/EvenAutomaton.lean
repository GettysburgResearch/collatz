import PostWords

namespace RampShadow.Postpeak

def evens (w : Word) : ℕ := w.length-weight w

def carry (w : Word) : ℤ := offset w+2^w.length

def evenBit (o : Bool) : ℕ := if o then 0 else 1

def term (a : ℕ) (o : Bool) : ℤ := if o then 0 else 3^a

theorem evens_cons (o : Bool) (w : Word) : evens (o::w)=evenBit o+evens w := by
  have := weight_le w
  cases o <;> simp [evens,weight,evenBit]
  omega

theorem carry_cons (o : Bool) (w : Word) :
    carry (o::w)=2*carry w+term (weight w) o := by
  cases o <;> simp [carry,offset,intercept,weight,term,pow_succ] <;> ring

theorem carry_bounds (w : Word) : 0≤carry w ∧ 2*carry w≤3^w.length-3^weight w := by
  induction w with
  | nil => norm_num [carry,offset,intercept,weight]
  | cons o w IH =>
    have W : (3:ℤ)^weight w≤3^w.length := pow_le_pow_right₀ (by norm_num) (weight_le w)
    have P : (0:ℤ)≤3^weight w := by positivity
    rw [carry_cons]
    rcases IH with ⟨A,B⟩
    cases o <;> simp only [term,weight,List.length_cons,pow_succ,Bool.false_eq_true,ite_false,ite_true]
      <;> constructor <;> linarith

structure State where
  a : ℕ
  b : ℕ
  c : ℤ
  deriving DecidableEq, Repr

def change (δ : ℕ) (s : State) (up lo : Bool) : ℤ :=
  s.c+term s.a up-term (δ+s.b) lo

def advance (δ : ℕ) (s : State) (up lo : Bool) : State :=
  ⟨s.a+evenBit up,s.b+evenBit lo,3*(change δ s up lo/2)⟩

def valid (Q δ : ℕ) (s : State) : Prop :=
  s.a≤Q ∧ s.b+δ≤Q ∧ 3^s.a-(3:ℤ)^Q≤2*s.c ∧ 2*s.c≤3^Q-3^(δ+s.b)

instance (Q δ : ℕ) (s : State) : Decidable (valid Q δ s) := by
  unfold valid;infer_instance

def legal (Q δ : ℕ) (s : State) (up lo : Bool) : Prop :=
  change δ s up lo % 2 = 0 ∧ valid Q δ (advance δ s up lo)

instance (Q δ : ℕ) (s : State) (up lo : Bool) : Decidable (legal Q δ s up lo) := by
  unfold legal;infer_instance

/-- The exact future balance on named tails, with both total even counts. -/
structure Completes (Q δ : ℕ) (s : State) (w β : Word) : Prop where
  length : w.length=β.length
  upper : s.a+evens w=Q
  lower : s.b+evens β+δ=Q
  balance : (3:ℤ)^w.length*s.c=3^Q*(carry β-carry w)

private theorem exp_balance {Q a : ℕ} {w : Word} (h : a+evens w=Q) :
    (3:ℤ)^Q*3^weight w=3^w.length*3^a := by
  have E := weight_le w
  unfold evens at h
  rw [←pow_add,←pow_add,show Q+weight w=w.length+a by omega]

theorem completion_valid {Q δ s w β} (F : Completes Q δ s w β) : valid Q δ s := by
  have U := carry_bounds w
  have V := carry_bounds β
  have W := exp_balance F.upper
  have B := exp_balance (a:=δ+s.b) (w:=β) (Q:=Q) (by have h := F.lower;omega)
  have EL := F.length
  rw [←EL] at B V
  have U' := mul_le_mul_of_nonneg_left U.2 (show (0:ℤ)≤3^Q by positivity)
  have V' := mul_le_mul_of_nonneg_left V.2 (show (0:ℤ)≤3^Q by positivity)
  have P := mul_nonneg (show (0:ℤ)≤3^Q by positivity) U.1
  have P' := mul_nonneg (show (0:ℤ)≤3^Q by positivity) V.1
  have bal := F.balance
  unfold valid
  refine ⟨by have h := F.upper;omega,by have h := F.lower;omega,?_,?_⟩
  · apply le_of_mul_le_mul_left (a:=(3:ℤ)^w.length)
    · nlinarith only [U',P',bal,W]
    · positivity
  · apply le_of_mul_le_mul_left (a:=(3:ℤ)^w.length)
    · nlinarith only [V',P,bal,B]
    · positivity

private theorem scale_carry {Q a : ℕ} {w : Word} {o : Bool} (H : a+evens (o::w)=Q) :
    (3:ℤ)^Q*carry (o::w)=2*3^Q*carry w+3^(w.length+1)*term a o := by
  rw [carry_cons]
  cases o with
  | false =>
    have E := weight_le w
    change a+(w.length+1-weight w)=Q at H
    have exp : (3:ℤ)^Q*3^weight w=3^(w.length+1)*3^a := by
      rw [←pow_add,←pow_add,show Q+weight w=w.length+1+a by omega]
    simp only [term,Bool.false_eq_true,ite_false]
    linarith only [exp]
  | true => simp [term];ring

private theorem pow_odd (p : ℕ) : (3:ℤ)^p%2=1 := by
  induction p with
  | zero => decide
  | succ p ih => rw [pow_succ,Int.mul_emod,ih];decide

/-- Every potentially successful step follows the finite integer automaton. -/
theorem completion_step {Q δ s up lo w β} (F : Completes Q δ s (up::w) (lo::β)) :
    legal Q δ s up lo ∧ Completes Q δ (advance δ s up lo) w β := by
  have EL : w.length=β.length := by simpa using F.length
  have U := scale_carry F.upper
  have V := scale_carry (Q:=Q) (a:=δ+s.b) (w:=β) (o:=lo) (by have h := F.lower;omega)
  rw [←EL] at V
  have bal := F.balance
  change (3:ℤ)^(w.length+1)*s.c=3^Q*(carry (lo::β)-carry (up::w)) at bal
  have raw : 3^(w.length+1)*change δ s up lo=2*(3^Q*(carry β-carry w)) := by
    unfold change
    linear_combination bal + V - U
  have par : 3^(w.length+1)*change δ s up lo%2=0 := by rw [raw];omega
  rw [Int.mul_emod,pow_odd] at par
  have even : change δ s up lo%2 = 0 := by omega
  have half : 2*(change δ s up lo/2)=change δ s up lo := by omega
  have FF : Completes Q δ (advance δ s up lo) w β := by
    constructor
    · exact EL
    · have H := F.upper
      rw [evens_cons] at H
      change s.a+evenBit up+evens w=Q
      omega
    · have H := F.lower
      rw [evens_cons] at H
      change s.b+evenBit lo+evens β+δ=Q
      omega
    · change (3:ℤ)^w.length*(3*(change δ s up lo/2))=3^Q*(carry β-carry w)
      rw [pow_succ] at raw
      nlinarith only [raw,congrArg (fun z : ℤ => (3:ℤ)^w.length*3*z) half]
  exact ⟨⟨even,completion_valid FF⟩,FF⟩

def initial : State := ⟨0,0,0⟩

theorem completion_initial {w β : Word} {Q δ : ℕ} (L : w.length=β.length)
    (EQ : evens w=Q) (EQ' : evens β+δ=Q) (same : offset w=offset β) :
    Completes Q δ initial w β := by
  refine ⟨L,by simpa [initial] using EQ,by simpa [initial] using EQ',?_⟩
  simp [initial,carry,L,same]

end RampShadow.Postpeak
