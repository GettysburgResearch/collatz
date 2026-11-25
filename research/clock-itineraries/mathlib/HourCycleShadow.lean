module

public import Mathlib.Data.Fintype.Pi
public import Mathlib.Algebra.Order.AbsoluteValue.Basic
public import Mathlib.Data.Rat.Floor
public import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic

public section
namespace Collatz.HourCycleShadow

set_option autoImplicit false

/-- Signed numerator equations obtained by reading a gap word backwards.
The denominator is fixed and a ternary unit. -/
def Shadow (d : ℕ) (e : ℕ → ℕ) (y : ℕ → ℤ) : Prop :=
  ∀ i, 3*y (i+1)+(d:ℤ)=(2:ℤ)^(e i)*y i

def TwoGaps (e : ℕ → ℕ) : Prop := ∀ i, e i=1 ∨ e i=2

/-- The reciprocal accumulated clock products stay in a common compact
interval of positive reals. The multiplicative normalization is arbitrary. -/
def BoundedClock (e : ℕ → ℕ) : Prop :=
  ∃ (K : ℕ) (w : ℕ → ℝ), 0<K ∧
    ∀ i, 1≤(K:ℝ)*w i ∧ w i≤K ∧ (2:ℝ)^(e i)*w (i+1)=3*w i

private theorem next_unique {d : ℕ} (unit : d%3≠0) {x a b : ℤ} {e f : ℕ}
    (he : e=1 ∨ e=2) (hf : f=1 ∨ f=2)
    (one : 3*a+(d:ℤ)=(2:ℤ)^e*x) (two : 3*b+(d:ℤ)=(2:ℤ)^f*x) :
    a=b := by
  rcases he with rfl|rfl <;> rcases hf with rfl|rfl <;> norm_num at one two <;> omega

private theorem same_forward {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} (unit : d%3≠0)
    (bin : TwoGaps e) (path : Shadow d e y) {i j : ℕ} (eqn : y i=y j) (k : ℕ) :
    y (i+k)=y (j+k) := by
  induction k with
  | zero => simpa using eqn
  | succ k ih =>
    apply next_unique unit (bin (i+k)) (bin (j+k)) (path (i+k))
    simpa only [Nat.add_assoc,ih] using path (j+k)

private theorem injective_of_fall {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ}
    (unit : d%3≠0) (bin : TwoGaps e) (path : Shadow d e y)
    (fall : ∀ A : ℤ, ∃ N, ∀ j, N≤j → y j<A) : Function.Injective y := by
  have ordered {i j : ℕ} (lt : i<j) (eqn : y i=y j) : False := by
    let p := j-i
    have ret (r : ℕ) : y (i+r*p)=y i := by
      induction r with
      | zero => simp
      | succ r ih =>
        have h := same_forward unit bin path eqn (r*p)
        rw [show i+(r+1)*p=j+r*p by rw [Nat.add_mul,Nat.one_mul]; dsimp [p]; omega]
        exact h.symm.trans ih
    obtain ⟨N,cut⟩ := fall (y i)
    have le := Nat.mul_le_mul_left (N+1) (show 1≤p by dsimp [p]; omega)
    simp only [Nat.mul_one] at le
    have h := cut (i+(N+1)*p) (by omega)
    rw [ret] at h
    omega
  intro i j same
  rcases lt_trichotomy i j with hi|eqn|hj
  · exact False.elim (ordered hi same)
  · exact eqn
  · exact False.elim (ordered hj same.symm)

/-- Equal inverse words give equal signed terminal residues modulo 3^b. -/
theorem word_dvd {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} (path : Shadow d e y)
    (b i j : ℕ) (same : ∀ t, t<b → e (i+t)=e (j+t)) : (3:ℤ)^b ∣ y i-y j := by
  induction b generalizing i j with
  | zero => simp
  | succ b ih =>
    have head := same 0 (by omega)
    simp only [Nat.add_zero] at head
    obtain ⟨v,hv⟩ := ih (i+1) (j+1) (fun t ht => by
      simpa only [Nat.add_assoc] using same (1+t) (by omega))
    have h₁ := path i
    have h₂ := path j
    rw [←head] at h₂
    have scaled : (3:ℤ)^(b+1) ∣ 2^(e i)*(y i-y j) := by
      refine ⟨v,?_⟩
      rw [pow_succ]
      linear_combination h₂-h₁+3*hv
    have cop : IsCoprime (3:ℤ) 2 := ⟨1,-1,by norm_num⟩
    exact cop.pow.dvd_of_dvd_mul_left scaled

/-- A finite numerical census for actual signed shadows. At most 2^b
distinct values in an interval of width below 3^b can carry b further
one-or-two inverse gaps. -/
theorem finite_packing {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} (bin : TwoGaps e)
    (path : Shadow d e y) (N b X : ℕ)
    (size : ∀ i, i<N → (y i).natAbs≤X) (width : 2*X<3^b)
    (distinct : ∀ i j, i<N → j<N → y i=y j → i=j) : N≤2^b := by
  let code := fun (i : Fin N) (j : Fin b) => decide (e (i.val+j.val)=2)
  have inj : Function.Injective code := by
    intro i j eqn
    have words (t : ℕ) (ht : t<b) : e (i.val+t)=e (j.val+t) := by
      have compare := congrFun eqn (⟨t,ht⟩ : Fin b)
      change decide (e (i.val+t)=2)=decide (e (j.val+t)=2) at compare
      rcases bin (i.val+t) with h|h <;> rcases bin (j.val+t) with g|g <;> simp_all
    have dvd := Int.natAbs_dvd_natAbs.mpr (word_dvd path b i.val j.val words)
    simp only [Int.natAbs_pow] at dvd
    change 3^b ∣ (y i.val-y j.val).natAbs at dvd
    have bound := Int.natAbs_sub_le (y i.val) (y j.val)
    have left := size i.val i.isLt
    have right := size j.val j.isLt
    have short : (y i.val-y j.val).natAbs < 3^b := by omega
    have zero := Nat.eq_zero_of_dvd_of_lt dvd short
    have same : y i.val=y j.val := by omega
    exact Fin.ext (distinct _ _ i.isLt j.isLt same)
  simpa [Fintype.card_fun] using Fintype.card_le_of_injective code inj

private theorem power_room (C : ℕ) : ∃ b, 2*(C*(2^b+1))<3^b := by
  have growth (b : ℕ) : (b+2)*2^b≤2*3^b := by
    induction b with
    | zero => decide
    | succ b ih =>
      rw [pow_succ 2,pow_succ 3]
      nlinarith [Nat.zero_le (b*2^b)]
  let b := 8*C+2
  refine ⟨b,?_⟩
  have h := growth b
  have pos : 0<2^b := by positivity
  have room : (8*C+1)*2^b<(b+2)*2^b := Nat.mul_lt_mul_of_pos_right (by dsimp [b]; omega) pos
  nlinarith [Nat.mul_le_mul_left C (show 1≤2^b by omega)]

private theorem no_linear_fall {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} (unit : d%3≠0)
    (bin : TwoGaps e) (path : Shadow d e y)
    (size : ∃ C : ℕ, ∀ n, (y n).natAbs≤C*(n+1))
    (fall : ∀ A : ℤ, ∃ N, ∀ j, N≤j → y j<A) : False := by
  obtain ⟨C,linear⟩ := size
  obtain ⟨b,room⟩ := power_room C
  have inject := injective_of_fall unit bin path fall
  have count := finite_packing bin path (2^b+1) b (C*(2^b+1)) (fun i hi =>
    (linear i).trans (Nat.mul_le_mul_left C hi)) room (fun _ _ _ _ eqn => inject eqn)
  omega

private theorem weighted_estimates {d K : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} {w : ℕ → ℝ}
    (path : Shadow d e y) (strip : ∀ i,
      1≤(K:ℝ)*w i ∧ w i≤K ∧ (2:ℝ)^(e i)*w (i+1)=3*w i) (n : ℕ) :
    3*K*w n*y n ≤ 3*K*w 0*y 0-(n:ℝ)*d ∧
    3*w 0*y 0-(n:ℝ)*d*K ≤ 3*w n*y n := by
  have step (i : ℕ) :
      3*w (i+1)*(y (i+1):ℝ)+d*w (i+1)=3*w i*(y i:ℝ) := by
    have eqn : 3*(y (i+1):ℝ)+(d:ℝ)=(2:ℝ)^(e i)*(y i:ℝ) := by
      exact_mod_cast path i
    calc
      _ = w (i+1)*(3*(y (i+1):ℝ)+d) := by ring
      _ = ((2:ℝ)^(e i)*w (i+1))*(y i:ℝ) := by rw [eqn]; ring
      _ = _ := by rw [(strip i).2.2]
  induction n with
  | zero => simp
  | succ n ih =>
    obtain ⟨upper,lower⟩ := ih
    have exactStep := step n
    have scaled := congrArg ((K:ℝ)*·) exactStep
    have minCost := mul_le_mul_of_nonneg_left (strip (n+1)).1 (Nat.cast_nonneg d)
    have maxCost := mul_le_mul_of_nonneg_left (strip (n+1)).2.1 (Nat.cast_nonneg d)
    push_cast
    constructor <;> nlinarith only [upper,lower,scaled,exactStep,minCost,maxCost]

/-- Signed shadows of an inverse word in a bounded clock strip must
have at most linear size and must ultimately pass below every integer. -/
theorem linear_drift {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} (pos : 0<d)
    (path : Shadow d e y) (balanced : BoundedClock e) :
    (∃ C : ℕ, ∀ n, (y n).natAbs≤C*(n+1)) ∧
    (∀ A : ℤ, ∃ N, ∀ j, N≤j → y j<A) := by
  obtain ⟨K,w,kp,h⟩ := balanced
  have kr : 0<(K:ℝ) := by exact_mod_cast kp
  have dr : 1≤(d:ℝ) := by exact_mod_cast pos
  have wp (n : ℕ) : 0<w n := by nlinarith only [(h n).1,kr]
  let Y := w 0 * (y 0:ℝ)
  constructor
  · obtain ⟨F,f⟩ := exists_nat_ge (|Y|+(d:ℝ)*K+1)
    refine ⟨K*F,?_⟩
    intro n
    obtain ⟨up,low⟩ := weighted_estimates path h n
    have nu : w n*(y n:ℝ)≤Y := by
      apply le_of_mul_le_mul_left (a:=(3:ℝ)*K) _ (by positivity)
      dsimp [Y]
      nlinarith only [up,show 0≤(n:ℝ)*d by positivity]
    have bound : |w n*(y n:ℝ)|≤|Y|+(n:ℝ)*d*K := by
      apply abs_le.2
      dsimp [Y] at nu ⊢
      constructor <;> nlinarith only [nu,low,neg_abs_le (w 0*(y 0:ℝ)),
        le_abs_self (w 0*(y 0:ℝ)),show 0≤(n:ℝ)*d*K by positivity]
    have absorb : |Y|+(n:ℝ)*d*K ≤ F*((n:ℝ)+1) := by
      nlinarith only [f,mul_le_mul_of_nonneg_right f (Nat.cast_nonneg n),
        show 0≤ (n:ℝ)*|Y| by positivity,abs_nonneg Y,show 0≤(d:ℝ)*K by positivity]
    have small := mul_le_mul_of_nonneg_left (bound.trans absorb) kr.le
    rw [abs_mul,abs_of_pos (wp n)] at small
    have cp := mul_le_mul_of_nonneg_right (h n).1 (abs_nonneg (y n:ℝ))
    have finish : |(y n:ℝ)| ≤ ((K*F*(n+1):ℕ):ℝ) := by
      push_cast
      nlinarith only [small,cp]
    have zi : |y n|≤((K*F*(n+1):ℕ):ℤ) := by exact_mod_cast finish
    rw [←Int.natCast_natAbs] at zi
    exact_mod_cast zi
  · intro A
    obtain ⟨N,large⟩ := exists_nat_gt (3*K*Y+3*(K:ℝ)*K*|(A:ℝ)|)
    refine ⟨N,?_⟩
    intro j late
    by_contra! rev
    have ar : (A:ℝ)≤(y j:ℝ) := by exact_mod_cast rev
    have jr : (N:ℝ)≤j := by exact_mod_cast late
    have up := (weighted_estimates path h j).1
    have triv : -|(A:ℝ)|≤(y j:ℝ) := (neg_abs_le _).trans ar
    have front := mul_le_mul_of_nonneg_left triv (wp j).le
    have stretch := mul_le_mul_of_nonneg_right (h j).2.1 (abs_nonneg (A:ℝ))
    have lower : -(K:ℝ)*|(A:ℝ)| ≤ w j*(y j:ℝ) := by linarith
    have scale := mul_le_mul_of_nonneg_left lower (show 0≤3*(K:ℝ) by positivity)
    have count := mul_le_mul_of_nonneg_left dr (Nat.cast_nonneg j)
    dsimp [Y] at large
    nlinarith only [jr,up,scale,count,large]

/-- No rational ternary unit has an infinite integral inverse history
with gaps one or two and bounded reciprocal clock products. -/
theorem no_rational_shadow {d : ℕ} {e : ℕ → ℕ} {y : ℕ → ℤ} (unit : d%3≠0)
    (bin : TwoGaps e) (path : Shadow d e y) (balanced : BoundedClock e) : False := by
  have pos : 0<d := by omega
  obtain ⟨size,fall⟩ := linear_drift pos path balanced
  exact no_linear_fall unit bin path size fall

private def gap (d : ℕ) (y : ℤ) : ℕ :=
  if (2*y-(d:ℤ))%3=0 then 1 else 2

private def previous (d : ℕ) (y : ℤ) : ℤ :=
  ((2:ℤ)^(gap d y)*y-d)/3

private def pull (d : ℕ) (A : ℤ) : ℕ → ℤ
  | 0 => A
  | n+1 => previous d (pull d A n)

private def letters (d : ℕ) (A : ℤ) (n : ℕ) := gap d (pull d A n)

private theorem read_edge {d : ℕ} {e : ℕ} {y v : ℤ} (unit : d%3≠0)
    (binary : e=1 ∨ e=2) (edge : 3*v+d=(2:ℤ)^e*y) :
    gap d y=e ∧ previous d y=v := by
  rcases binary with rfl|rfl
  · norm_num at edge
    have yes : (2*y-(d:ℤ))%3=0 := by omega
    simp [previous,gap,yes]
    omega
  · norm_num at edge
    have no : (2*y-(d:ℤ))%3≠0 := by omega
    norm_num [previous,gap,no]
    omega

private theorem lift_edge {d x z e t : ℕ} {y : ℤ} (unit : d%3≠0)
    (binary : e=1 ∨ e=2) (edge : 3*z+1=2^e*x)
    (congr : (3:ℤ)^(t+1)∣(d:ℤ)*x-y) :
    gap d y=e ∧ (3:ℤ)^(t) ∣ (d:ℤ)*z-previous d y ∧
      3*previous d y+(d:ℤ)=(2:ℤ)^e*y := by
  obtain ⟨h,div⟩ := congr
  let v : ℤ := (d:ℤ)*z-2^e*3^t*h
  have edgez : 3*(z:ℤ)+1=(2:ℤ)^e*x := by exact_mod_cast edge
  have exactEdge : 3*v+(d:ℤ)=(2:ℤ)^e*y := by
    dsimp [v]
    rw [pow_succ] at div
    linear_combination (d:ℤ)*edgez+(2:ℤ)^e*div
  obtain ⟨eg,pr⟩ := read_edge unit binary exactEdge
  refine ⟨eg,?_,by simpa only [pr] using exactEdge⟩
  rw [pr]
  exact ⟨2^e*h,by dsimp [v]; ring⟩

/-- An ordinary reversed window of N positive one-or-two gaps. The
floor may grow with the observation depth. The terminal is congruent
to the fixed signed rational numerator A over denominator d. -/
def OrdinaryWindow (d : ℕ) (A : ℤ) (K N : ℕ) : Prop :=
  ∃ (m : ℕ) (x g : ℕ → ℕ),
    0<m ∧ K*N≤m ∧
    (∀ i, i≤N → m≤x i ∧ x i≤K*m) ∧
    (∀ i, i<N → (g i=1 ∨ g i=2) ∧ 3*x (i+1)+1=2^(g i)*x i) ∧
    (3:ℤ)^N∣(d:ℤ)*x 0-A

private theorem window_edges {d N : ℕ} {A : ℤ} {x g : ℕ → ℕ} (unit : d%3≠0)
    (steps : ∀ i, i<N → (g i=1 ∨ g i=2) ∧ 3*x (i+1)+1=2^(g i)*x i)
    (root : (3:ℤ)^N∣(d:ℤ)*x 0-A) :
    ∀ i, i<N → letters d A i=g i ∧
      3*pull d A (i+1)+(d:ℤ)=(2:ℤ)^(letters d A i)*pull d A i := by
  have agree (i : ℕ) (hi : i≤N) : (3:ℤ)^(N-i)∣(d:ℤ)*x i-pull d A i := by
    induction i with
    | zero => simpa [pull] using root
    | succ i ih =>
      obtain ⟨choice,edge⟩ := steps i (by omega)
      have old := ih (by omega)
      rw [show N-i=(N-(i+1))+1 by omega] at old
      exact (lift_edge unit choice edge old).2.1
  intro i hi
  have old := agree i hi.le
  rw [show N-i=(N-(i+1))+1 by omega] at old
  obtain ⟨choice,edge⟩ := steps i hi
  obtain ⟨letter,_,valid⟩ := lift_edge unit choice edge old
  exact ⟨letter,by change 3*previous d (pull d A i)+(d:ℤ)=(2:ℤ)^(gap d (pull d A i))*_; rw [letter]; exact valid⟩

private noncomputable def weight (e : ℕ → ℕ) : ℕ → ℝ
  | 0 => 1
  | n+1 => 3*weight e n/(2:ℝ)^(e n)

private theorem weight_pos (e : ℕ → ℕ) (n : ℕ) : 0<weight e n := by
  induction n with
  | zero => simp [weight]
  | succ n ih => rw [weight]; positivity

private theorem weight_step (e : ℕ → ℕ) (n : ℕ) :
    (2:ℝ)^(e n)*weight e (n+1)=3*weight e n := by rw [weight]; field_simp

private theorem window_strip {e x : ℕ → ℕ} {m K N : ℕ}
    (positive : 0<m) (budget : K*N≤m)
    (bounds : ∀ i, i≤N → m≤x i ∧ x i≤K*m)
    (edge : ∀ i, i<N → 3*x (i+1)+1=2^(e i)*x i) :
    1≤(2*K:ℕ)*weight e N ∧ weight e N≤(K:ℝ) := by
  let w := weight e
  have gains (i : ℕ) (hi : i<N) :
      3*w (i+1)*(x (i+1):ℝ)+w (i+1)=3*w i*(x i:ℝ) := by
    have physical : 3*(x (i+1):ℝ)+1=(2:ℝ)^(e i)*(x i:ℝ) := by exact_mod_cast edge i hi
    calc
      _ = w (i+1)*(3*(x (i+1):ℝ)+1) := by ring
      _ = ((2:ℝ)^(e i)*w (i+1))*(x i:ℝ) := by rw [physical]; ring
      _ = _ := by rw [weight_step]
  have upper (i : ℕ) (hi : i≤N) : w i*(x i:ℝ)≤x 0 := by
    induction i with
    | zero => simp [w,weight]
    | succ i ih => linarith only [ih (by omega), gains i (by omega), weight_pos e (i+1)]
  have small (i : ℕ) (hi : i≤N) : w i≤(K:ℝ) := by
    have u := upper i hi
    have xl : (m:ℝ)≤x i := by exact_mod_cast (bounds i hi).1
    have xh : (x 0:ℝ)≤(K:ℝ)*m := by exact_mod_cast (bounds 0 (by omega)).2
    have mpos : 0<(m:ℝ) := by exact_mod_cast positive
    exact le_of_mul_le_mul_right (a:=(m:ℝ)) (by
      nlinarith only [u,xh,mul_le_mul_of_nonneg_left xl (weight_pos e i).le]) mpos
  have lower (i : ℕ) (hi : i≤N) : 3*(x 0:ℝ)-(i:ℝ)*K≤3*w i*(x i:ℝ) := by
    induction i with
    | zero => simp [w,weight]
    | succ i ih =>
      have prev := ih (by omega)
      have extra := small (i+1) hi
      push_cast
      nlinarith only [prev,extra,gains i (by omega)]
  have ln := lower N (by omega)
  have x₀ : (m:ℝ)≤x 0 := by exact_mod_cast (bounds 0 (by omega)).1
  have xN : (x N:ℝ)≤(K:ℝ)*m := by exact_mod_cast (bounds N (by omega)).2
  have room : (K:ℝ)*N≤m := by exact_mod_cast budget
  have mpos : 0<(m:ℝ) := by exact_mod_cast positive
  refine ⟨?_,small N (by omega)⟩
  apply le_of_mul_le_mul_right (a:=(m:ℝ)) _ mpos
  push_cast
  nlinarith only [ln,x₀,room,mul_le_mul_of_nonneg_left xN (weight_pos e N).le,mpos]

private def total (e : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | n+1 => total e n + e n

private theorem weight_formula (e : ℕ → ℕ) (n : ℕ) :
    weight e n=(3:ℝ)^n/(2:ℝ)^(total e n) := by
  induction n with
  | zero => simp [weight,total]
  | succ n ih =>
    simp only [weight,total,ih,pow_add]
    field_simp

/-- Check the rational root's forced backward gaps and the two integer
clock bounds through N. A false result excludes an ordinary window. -/
def passes (d : ℕ) (A : ℤ) (K N : ℕ) : Bool :=
  let e := letters d A
  let y := pull d A
  ((List.range N).all fun i => decide (3*y (i+1)+(d:ℤ)=(2:ℤ)^(e i)*y i)) &&
    ((List.range (N+1)).all fun i => decide
      (2^(total e i)≤2*K*3^i ∧ 3^i≤K*2^(total e i)))

private theorem pass_spec (d : ℕ) (A : ℤ) (K N : ℕ) :
    passes d A K N=true ↔
    (∀ i, i<N → 3*pull d A (i+1)+(d:ℤ)=(2:ℤ)^(letters d A i)*pull d A i) ∧
    ∀ i, i≤N → 2^(total (letters d A) i)≤2*K*3^i ∧ 3^i≤K*2^(total (letters d A) i) := by
  simp [passes,List.all_eq_true]

private theorem natural_strip (e : ℕ → ℕ) (K n : ℕ) :
    (1≤((2*K:ℕ):ℝ)*weight e n ∧ weight e n≤(K:ℝ)) ↔
    2^(total e n)≤2*K*3^n ∧ 3^n≤K*2^(total e n) := by
  rw [weight_formula,←mul_div_assoc,le_div_iff₀ (by positivity),div_le_iff₀ (by positivity)]
  simp only [one_mul]
  norm_cast

theorem ordinary_passes {d K N : ℕ} {A : ℤ} (unit : d%3≠0)
    (window : OrdinaryWindow d A K N) : passes d A K N=true := by
  obtain ⟨m,x,g,mp,room,band,steps,modulus⟩ := window
  have native := window_edges unit steps modulus
  refine (pass_spec ..).mpr ⟨fun i hi => (native i hi).2,?_⟩
  intro i hi
  apply (natural_strip ..).mp
  apply window_strip mp (Nat.le_trans (Nat.mul_le_mul_left K hi) room)
    (fun j hj => band j (hj.trans hi))
  intro j hj
  have lt := hj.trans_le hi
  rw [(native j lt).1]
  exact (steps j lt).2

/-- At every fixed rational unit a finite failed test exists and all later
tests fail. Searching for the first failure is therefore total. -/
theorem eventually_fails (d K : ℕ) (A : ℤ) (unit : d%3≠0) (positive : 0<K) :
    ∃ N, ∀ n, N≤n → passes d A K n=false := by
  by_contra! frequent
  let e := letters d A
  let y := pull d A
  have good (L : ℕ) : ∃ n, L≤n ∧ passes d A K n=true := by simpa using frequent L
  have edge : Shadow d e y := by
    intro i
    obtain ⟨n,late,accept⟩ := good (i+1)
    exact ((pass_spec ..).mp accept).1 i (by omega)
  have bin : TwoGaps e := by intro i; dsimp [e,letters,gap]; split <;> simp
  apply no_rational_shadow unit bin edge
  refine ⟨2*K,weight e,by omega,?_⟩
  intro i
  obtain ⟨n,late,accept⟩ := good i
  have bound := (natural_strip e K i).mpr (((pass_spec ..).mp accept).2 i late)
  refine ⟨bound.1,?_,weight_step e i⟩
  push_cast
  linarith only [bound.2,show 0≤(K:ℝ) by positivity]

/-- Every fixed signed rational ternary integer is excluded, at a finite
depth, from all sufficiently high ordinary one-or-two-gap windows. -/
theorem ordinary_rational_exclusion (d K : ℕ) (A : ℤ) (unit : d%3≠0) (positive : 0<K) :
    ∃ N, ¬OrdinaryWindow d A K N := by
  obtain ⟨N,fail⟩ := eventually_fails d K A unit positive
  exact ⟨N, fun win => by simpa [ordinary_passes unit win] using fail N (by omega)⟩

private theorem some_failure (d K : ℕ) (A : ℤ) (unit : d%3≠0) (positive : 0<K) :
    ∃ N, passes d A K N=false := by
  obtain ⟨N,fail⟩ := eventually_fails d K A unit positive
  exact ⟨N,fail N (by omega)⟩

/-- The executable least depth of the excluded rational residue class. -/
def firstFailure (d K : ℕ) (A : ℤ) (unit : d%3≠0) (positive : 0<K) : ℕ :=
  Nat.find (some_failure d K A unit positive)

theorem firstFailure_spec (d K : ℕ) (A : ℤ) (unit : d%3≠0) (positive : 0<K) :
    let N := firstFailure d K A unit positive
    passes d A K N=false ∧ (∀ n, n<N → passes d A K n=true) ∧ ¬OrdinaryWindow d A K N := by
  let H := some_failure d K A unit positive
  have failed := Nat.find_spec H
  refine ⟨failed,fun n hn => ?_,fun win => ?_⟩
  · exact Bool.eq_true_of_not_eq_false (Nat.find_min H hn)
  · exact Bool.noConfusion ((ordinary_passes unit win).symm.trans failed)

/-- A failed test excludes that residue class at every phase of an
ordinary bounded-width cycle, uniformly in its period. -/
theorem cycle_phase_exclusion {d K N : ℕ} {A : ℤ} (unit : d%3≠0)
    (fail : passes d A K N=false) {x g : ℕ → ℕ} {m p : ℕ}
    (per : 0<p) (pos : 0<m) (room : K*N≤m)
    (band : ∀ j, m≤x j ∧ x j≤K*m)
    (step : ∀ j, (g j=1 ∨ g j=2) ∧ 3*x j+1=2^(g j)*x (j+1))
    (periodic : ∀ j, x (j+p)=x j) (t : ℕ) :
    ¬(3:ℤ)^N∣(d:ℤ)*x t-A := by
  intro congr
  have laps (n : ℕ) : x (t+n*p)=x t := by
    induction n with
    | zero => simp
    | succ n ih => rw [Nat.succ_mul,←Nat.add_assoc,periodic,ih]
  let back := fun j => t+N*p-j
  have big : N≤N*p := by simpa using Nat.mul_le_mul_left N per
  have win : OrdinaryWindow d A K N := by
    refine ⟨m,fun j => x (back j),fun j => g (back (j+1)),pos,room,fun j _ => band _,?_,?_⟩
    · intro j hj
      have nxt : back (j+1)+1=back j := by dsimp [back]; omega
      obtain ⟨choice,edge⟩ := step (back (j+1))
      exact ⟨choice,by simpa only [nxt] using edge⟩
    · simpa [back,laps] using congr
  simp [ordinary_passes unit win] at fail

set_option maxRecDepth 10000 in
set_option maxHeartbeats 1500000 in
set_option exponentiation.threshold 1000 in
theorem rational_controls :
    passes 1 (-1) 6 4=true ∧ passes 1 (-1) 6 5=false ∧
    passes 1 1 6 8=true ∧ passes 1 1 6 9=false ∧
    passes 1631 10865 6 44=true ∧ passes 1631 10865 6 45=false ∧
    passes 13 283 6 162=true ∧ passes 13 283 6 163=false := by decide

#print axioms finite_packing
#print axioms linear_drift
#print axioms no_rational_shadow
#print axioms ordinary_rational_exclusion
#print axioms ordinary_passes
#print axioms eventually_fails
#print axioms firstFailure_spec
#print axioms cycle_phase_exclusion
#print axioms rational_controls
end Collatz.HourCycleShadow
