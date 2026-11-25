import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! Ordinary asynchronous merger deadlines on the pure-power slice. -/
namespace TowerDeadline

def step (x : ℕ) := if x % 2 = 0 then x / 2 else (3*x+1)/2

def orbit : ℕ → ℕ → ℕ
  | 0, x => x
  | h+1, x => orbit h (step x)

def slope : ℕ → ℕ → ℕ
  | 0, _ => 1
  | h+1, x => (if x % 2 = 0 then 1 else 3) * slope h (step x)

def carry : ℕ → ℕ → ℕ
  | 0, _ => 0
  | h+1, x => 2*carry h (step x) + (x%2)*slope h (step x)

private theorem profile (h x : ℕ) :
    2^h*orbit h x = slope h x*x + carry h x := by
  induction h generalizing x with
  | zero => simp [orbit, slope, carry]
  | succ h ih =>
    have he := ih (step x)
    by_cases e : x%2=0
    · have hx : 2*step x=x := by simp [step,e]; omega
      simp only [orbit, slope, carry, e, ite_true, one_mul, zero_mul, add_zero, pow_succ]
      rw [show 2^h*2*orbit h (step x) = 2*(2^h*orbit h (step x)) by ring, he]
      have := congrArg (slope h (step x) * ·) hx
      nlinarith
    · have hx : 2*step x=3*x+1 := by simp [step,e]; omega
      have eo : x%2=1 := by omega
      simp only [orbit, slope, carry, eo, reduceCtorEq, ite_false, one_mul, pow_succ]
      rw [show 2^h*2*orbit h (step x) = 2*(2^h*orbit h (step x)) by ring, he]
      have := congrArg (slope h (step x) * ·) hx
      nlinarith

private theorem profile_bounds (h x : ℕ) :
    slope h x ≤ 3^h ∧ carry h x ≤ 3^h ∧ slope h x ≤ carry h x + 2^h := by
  induction h generalizing x with
  | zero => simp [slope, carry]
  | succ h ih =>
    obtain ⟨a,b,c⟩ := ih (step x)
    rcases (show x%2=0 ∨ x%2=1 by omega) with e|e <;>
      simp [slope, carry, e, pow_succ] <;> omega

private def Phase (c : ℕ) := c=5 ∨ c=7 ∨ c=10

private theorem negative_cycle (h x c : ℕ) (hc : Phase c) (hd : 2^h ∣ x+c) :
    carry h x + 5*2^h ≤ c*slope h x := by
  induction h generalizing x c with
  | zero => rcases hc with e|e|e <;> simp [carry, slope, e]
  | succ h ih =>
    obtain ⟨u,hu⟩ := hd
    rw [pow_succ, Nat.mul_right_comm] at hu
    rcases hc with rfl|rfl|rfl
    · have e : x%2=1 := by omega
      have nx : 2*(step x+7)=3*(x+5) := by simp [step,e]; omega
      have hd' : 2^h ∣ step x+7 := ⟨3*u, by nlinarith [hu,nx]⟩
      have := ih (step x) 7 (Or.inr (Or.inl rfl)) hd'
      simp [carry,slope,e,pow_succ]; omega
    · have e : x%2=1 := by omega
      have nx : 2*(step x+10)=3*(x+7) := by simp [step,e]; omega
      have hd' : 2^h ∣ step x+10 := ⟨3*u, by nlinarith [hu,nx]⟩
      have := ih (step x) 10 (Or.inr (Or.inr rfl)) hd'
      simp [carry,slope,e,pow_succ]; omega
    · have e : x%2=0 := by omega
      have nx : 2*(step x+5)=x+10 := by simp [step,e]; omega
      have hd' : 2^h ∣ step x+5 := ⟨u, by nlinarith [hu,nx]⟩
      have := ih (step x) 5 (Or.inl rfl) hd'
      simp [carry,slope,e,pow_succ]; omega

private theorem lower_one (h x : ℕ) (e : x%4=1) :
    5*slope h x ≤ 3*(carry h x+2*2^h) := by
  have ex : x%2=1 := by omega
  have ey : (step x)%2=0 := by simp [step,ex]; omega
  match h with
  | 0 => simp [slope, carry]
  | 1 => simp [slope, carry, ex]
  | k+2 =>
    have hb := (profile_bounds k (step (step x))).2.2
    simp only [slope,carry,ex,ey,reduceCtorEq,ite_false,ite_true,one_mul,zero_mul,add_zero,pow_succ]
    omega

private theorem size_bounds (h x : ℕ) : x ≤ 2^h*orbit h x ∧ orbit h x ≤ 2^h*x := by
  induction h generalizing x with
  | zero => simp [orbit]
  | succ h ih =>
    obtain ⟨l,u⟩ := ih (step x)
    have first : x ≤ 2*step x ∧ step x ≤ 2*x := by
      by_cases e : x%2=0 <;> simp [step,e] <;> omega
    constructor
    · exact first.1.trans ((Nat.mul_le_mul_left 2 l).trans_eq (by simp [orbit, pow_succ]; ring))
    · exact u.trans ((Nat.mul_le_mul_left _ first.2).trans_eq (by simp [pow_succ]; ring))

/-- The clocks may differ. The integer `r` is the larger exponent and
`s` is any smaller nonnegative exponent, including zero. -/
theorem no_earlier_power (H r : ℕ) (depth : 2 ≤ H) (large : 24^H < 3^r)
    (shadow : 2^H ∣ 3^r+5) (s i l : ℕ) (hs : s<r) (hi : i≤H) (hl : l≤H) :
    orbit i (3^r) ≠ orbit l (3^s) := by
  intro meet
  obtain ⟨d,rd⟩ := Nat.exists_eq_add_of_lt hs
  have eqr : r=s+(d+1) := by omega
  let k := 3^(d+1)
  let m := 3^s
  have source : 3^r=k*m := by dsimp [k,m]; rw [eqr,pow_add,Nat.mul_comm]
  let a := 2^l*slope i (3^r)
  let b := 2^i*slope l m
  let e := 2^l*carry i (3^r)
  let f := 2^i*carry l m
  have twoI := Nat.pow_le_pow_right (by decide : 0<2) hi
  have twoL := Nat.pow_le_pow_right (by decide : 0<2) hl
  have hU := (size_bounds i (3^r)).1
  have hL := (size_bounds l m).2
  rw [meet] at hU
  have sz : 3^r ≤ 4^H*m := calc
    _ ≤ 2^i*(2^l*m) := hU.trans (Nat.mul_le_mul_left _ hL)
    _ ≤ 2^H*2^H*m := by rw [←Nat.mul_assoc]; exact Nat.mul_le_mul_right _ (Nat.mul_le_mul twoI twoL)
    _ = _ := by rw [←Nat.mul_pow]
  have big : 6^H < m := by
    by_contra! h
    have le := sz.trans (Nat.mul_le_mul_left (4^H) h)
    rw [←Nat.mul_pow] at le
    exact (Nat.not_lt_of_ge le) large
  have carr {n t : ℕ} (ht : t≤H) : carry t n ≤ 3^H :=
    (profile_bounds t n).2.1.trans (Nat.pow_le_pow_right (by decide) ht)
  have es : e<m := by
    apply Nat.lt_of_le_of_lt (Nat.mul_le_mul twoL (carr hi)) _
    rwa [←Nat.mul_pow]
  have fs : f<m := by
    apply Nat.lt_of_le_of_lt (Nat.mul_le_mul twoI (carr hl)) _
    rwa [←Nat.mul_pow]
  have same : (a*k)*m+e=b*m+f := by
    have pu := congrArg (2^l * ·) (profile i (3^r))
    have pl := congrArg (2^i * ·) (profile l m)
    have mt : orbit i (3^r)=orbit l m := meet
    dsimp [a,b,e,f]
    rw [mt] at pu
    rw [source] at pu ⊢
    nlinarith only [pu,pl]
  have ef : e=f := by
    have q := congrArg (· % m) same
    simpa [Nat.add_mod, Nat.mod_eq_of_lt es, Nat.mod_eq_of_lt fs] using q
  have ak : a*k=b := Nat.eq_of_mul_eq_mul_right (by omega : 0<m)
    (by rw [ef] at same; omega)
  have shI : 2^i ∣ 3^r+5 := (Nat.pow_dvd_pow 2 hi).trans shadow
  have up := Nat.mul_le_mul_left (2^l) (negative_cycle i (3^r) 5 (Or.inl rfl) shI)
  have low : 5*slope l m ≤ k*(carry l m+2*2^l) := by
    cases d with
    | zero =>
      have hh : 4 ∣ 3^r+5 := (Nat.pow_dvd_pow 2 depth).trans shadow
      obtain ⟨u,hu⟩ := hh
      change 3^r=3*m at source
      have em : m%4=1 := by omega
      exact lower_one l m em
    | succ d =>
      have sk : 5≤k := by
        change 5 ≤ 3^(d+1+1)
        exact Nat.le_trans (by decide : 5≤3^2)
          (Nat.pow_le_pow_right (by decide) (by omega))
      have bb := (profile_bounds l m).2.2
      exact (Nat.mul_le_mul_left 5 bb).trans (Nat.mul_le_mul sk (by omega))
  have dn := Nat.mul_le_mul_left (2^i) low
  have un : e+5*(2^i*2^l) ≤ 5*a := by dsimp [e,a]; nlinarith only [up]
  have ln : 5*b ≤ k*(f+2*(2^i*2^l)) := by dsimp [b,f]; nlinarith only [dn]
  rw [←ak, ←ef] at ln
  have fin := (Nat.mul_le_mul_right k un).trans (by simpa [Nat.mul_assoc] using ln)
  have kp : 0<k := by dsimp [k]; positivity
  have pp : 0 < 2^i*2^l := by positivity
  nlinarith only [fin, Nat.mul_pos pp kp]

private theorem toggle (k : ℕ) :
    ∃ u, 3^(6*2^k)=1+2^(k+3)*(2*u+1) := by
  induction k with
  | zero => exact ⟨45, by decide⟩
  | succ k ih =>
    obtain ⟨u,hu⟩ := ih
    refine ⟨u+2^(k+1)*(2*u+1)^2, ?_⟩
    rw [Nat.pow_succ 2 k, ←Nat.mul_assoc, Nat.pow_mul, hu]
    simp only [pow_succ]
    ring

private theorem odd_power (r : ℕ) : ∃ z, 3^r=2*z+1 := by
  induction r with
  | zero => exact ⟨0, rfl⟩
  | succ r ih =>
    obtain ⟨z,hz⟩ := ih
    exact ⟨3*z+1, by rw [pow_succ,hz]; omega⟩

theorem lift_class (k L offset : ℕ) (initial : offset % 8=5) : ∃ r,
    6*L+1 ≤ r ∧ r ≤ 6*L+1+6*(2^k-1) ∧ r%3=1 ∧ 2^(k+3) ∣ 3^r+offset := by
  induction k with
  | zero =>
    refine ⟨6*L+1, by omega, by simp, by omega, ?_⟩
    have modpow : 729^L%8=1 := by
      induction L with
      | zero => decide
      | succ L ih => rw [pow_succ, Nat.mul_mod, ih]
    rw [Nat.pow_succ 3 (6*L), Nat.pow_mul]
    apply Nat.dvd_of_mod_eq_zero
    change (729^L*3+offset)%8=0
    rw [Nat.add_mod,Nat.mul_mod,modpow,initial]
  | succ k ih =>
    obtain ⟨r,rl,ru,rm,u,hu⟩ := ih
    have pos : 0 < (2:ℕ)^k := by positivity
    obtain ⟨v,hv⟩ := toggle k
    have evenSplit : u%2=0 ∨ u%2=1 := by omega
    rcases evenSplit with even|odd
    · refine ⟨r,rl,by rw [pow_succ]; omega,rm,u/2,?_⟩
      rw [show k+1+3=k+3+1 by omega,pow_succ,hu]
      have de : u=2*(u/2) := by omega
      nlinarith only [congrArg (2^(k+3)*·) de]
    · refine ⟨r+6*2^k, by omega, by rw [pow_succ]; omega, by omega, ?_⟩
      obtain ⟨z,hz⟩ := odd_power r
      refine ⟨u/2 + 3^r*v + z+1, ?_⟩
      have du : u=2*(u/2)+1 := by omega
      rw [show k+1+3=k+3+1 by omega,pow_succ,pow_add,hv]
      have addu := congrArg (2^(k+3)*·) du
      have addz := congrArg (2^(k+3)*·) hz
      nlinarith only [hu, addu, addz]

/-- Cofinal, actual exponents in the rank-one slice, with arbitrary lower
bound and a two-arm deadline that applies to every earlier exponent. -/
theorem deadline_window (H L : ℕ) :
    ∃ r, 6*(H+L+3)+1 ≤ r ∧ r ≤ 6*(H+L+3)+1+6*(2^H-1) ∧ r%3=1 ∧
      ∀ s i l, s<r → i≤H → l≤H → orbit i (3^r) ≠ orbit l (3^s) := by
  obtain ⟨r, lo, up, modr, sh⟩ := lift_class H (H+L+3) 5 (by decide)
  refine ⟨r, lo, up, modr, ?_⟩
  have bound : 24^(H+3) < 3^r := calc
    _ ≤ 27^(H+3) := Nat.pow_le_pow_left (by decide) _
    _ = 3^(3*(H+3)) := by rw [Nat.pow_mul]
    _ < _ := Nat.pow_lt_pow_right (by decide) (by omega)
  intro s i l hs hi hl
  exact no_earlier_power (H+3) r (by omega) bound sh s i l hs (by omega) (by omega)

theorem cofinal_deadline (H L : ℕ) :
    ∃ r, L≤r ∧ r%3=1 ∧
      ∀ s i l, s<r → i≤H → l≤H → orbit i (3^r) ≠ orbit l (3^s) := by
  obtain ⟨r, lo, _, modr, pr⟩ := deadline_window H L
  exact ⟨r, by omega, modr, pr⟩

#print axioms no_earlier_power
#print axioms lift_class
#print axioms deadline_window
#print axioms cofinal_deadline
end TowerDeadline
