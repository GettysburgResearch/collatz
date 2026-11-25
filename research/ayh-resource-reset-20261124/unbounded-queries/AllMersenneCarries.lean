import MersenneParity
import Mathlib.Tactic.Linarith

set_option autoImplicit false
set_option warningAsError true

namespace CollatzAllMersenneCarries
open CollatzReverseBasin CollatzMersenneParity

/-- Numerator of an arbitrary affine word applied to -1, with its clock and odd count. -/
inductive Carry : ℕ → ℕ → ℤ → Prop
  | start : Carry 0 0 (-1)
  | even {t p c} : Carry t p c → Carry (t+1) p c
  | odd {t p c} : Carry t p c → Carry (t+1) (p+1) (3*c+2^t)

private theorem clockLast (t n : ℕ) : atClock (t+1) n=shortcut (atClock t n) := by
  induction t generalizing n with
  | zero => rfl
  | succ t ih => exact ih (shortcut n)

private theorem twoUnit (t : ℕ) : ((2:ℤ)^t)%3=1 ∨ ((2:ℤ)^t)%3=2 := by
  induction t with
  | zero => decide
  | succ t ih =>
    rw [pow_succ, Int.mul_emod]
    rcases ih with h|h <;> rw [h] <;> decide

private theorem cancelAtThree (t : ℕ) (x : ℤ) (h : 3 ∣ 2^t*x) : 3 ∣ x := by
  have m := Int.emod_eq_zero_of_dvd h
  rw [Int.mul_emod] at m
  rcases twoUnit t with a|a <;> rw [a] at m <;> omega

/-- Every formal carry whose affine endpoint is an ordinary integer is physically
realized on the indicated earlier ternary peak. No parity admissibility premise. -/
theorem realize {t p : ℕ} {c : ℤ} (w : Carry t p c) (n y : ℕ)
    (h : (2:ℤ)^t*y=3^(n+p)+c) : atClock t (3^n-1)=y := by
  induction w generalizing y with
  | start =>
    simp at h
    have hp : 0 < (3:ℕ)^n := by positivity
    rw [atClock]
    apply Int.ofNat_inj.mp
    rw [Nat.cast_sub (by omega : 1≤(3:ℕ)^n)]
    push_cast
    omega
  | @even t p c w ih =>
    rw [clockLast, ih (2*y) (by push_cast; rw [pow_succ] at h; nlinarith only [h])]
    unfold shortcut
    split <;> omega
  | @odd t p c w ih =>
    have eqn : (2:ℤ)^t*(2*y-1)=3*(3^(n+p)+c) := by
      rw [pow_succ, ←Nat.add_assoc, pow_succ] at h
      nlinarith only [h]
    obtain ⟨x,hx⟩ := cancelAtThree t (2*y-1) ⟨_,eqn⟩
    have hy : 0≤x := by omega
    have hx' : (↑x.toNat : ℤ) = x := Int.toNat_of_nonneg hy
    have prev : (2:ℤ)^t*x.toNat=3^(n+p)+c := by
      rw [hx']
      rw [hx] at eqn
      nlinarith only [eqn]
    rw [clockLast, ih x.toNat prev]
    unfold shortcut
    split <;> omega

/-- Each physical word from a ternary peak supplies exactly such a signed carry. -/
theorem physical (n t : ℕ) :
    ∃ p c, Carry t p c ∧ (2:ℤ)^t*(atClock t (3^n-1))=3^(n+p)+c := by
  induction t with
  | zero =>
    refine ⟨0,-1,.start,?_⟩
    have hp : 0<(3:ℕ)^n := by positivity
    simp [atClock, Nat.cast_sub (by omega : 1≤(3:ℕ)^n), sub_eq_add_neg]
  | succ t ih =>
    obtain ⟨p,c,w,l⟩:=ih
    let x:=atClock t (3^n-1)
    change (2:ℤ)^t*x = _ at l
    by_cases ev : x%2=0
    · refine ⟨p,c,.even w,?_⟩
      rw [clockLast]
      have eqn : (2:ℤ)*(shortcut x)=x := by
        unfold shortcut
        simp only [ev,ite_true]
        omega
      change (2:ℤ)^(t+1)*(shortcut x)=_
      rw [pow_succ,mul_assoc,eqn,l]
    · refine ⟨p+1,3*c+2^t,.odd w,?_⟩
      rw [clockLast]
      have eqn : (2:ℤ)*(shortcut x)=3*x+1 := by
        unfold shortcut
        simp only [ev,ite_false]
        omega
      change (2:ℤ)^(t+1)*(shortcut x)=_
      rw [pow_succ,mul_assoc,eqn,←Nat.add_assoc,pow_succ]
      nlinarith only [l]

theorem oddCount_le {t p : ℕ} {c : ℤ} (w : Carry t p c) : p≤t := by
  induction w <;> omega

/-- At a negative endpoint the entire numerator is a negative power of two. -/
theorem negativeShape {t p : ℕ} {c : ℤ} (w : Carry t p c) (neg : c<0) :
    ∃ i : ℕ, i≤t ∧ c= -(2:ℤ)^i := by
  induction w with
  | start => exact ⟨0,by decide,by decide⟩
  | @even t p c w ih =>
    obtain ⟨i,hi,eqn⟩:=ih neg
    exact ⟨i,by omega,eqn⟩
  | @odd t p c w ih =>
    have hp : 0<(2:ℤ)^t := by positivity
    obtain ⟨i,hi,eqn⟩:=ih (by omega)
    subst c
    by_cases same : i=t
    · subst i
      refine ⟨t+1,by omega,?_⟩
      rw [pow_succ]; ring
    · by_cases next : i+1=t
      · subst t
        refine ⟨i,by omega,?_⟩
        rw [pow_succ]; ring
      · have ord : i+2≤t := by omega
        have big : (2:ℤ)^(i+2)≤2^t := pow_le_pow_right₀ (by decide) ord
        rw [pow_add] at big
        norm_num at big
        omega

/-- An odd negative carry can only be -1. -/
theorem negativeOdd {t p : ℕ} {c : ℤ} (w : Carry t p c)
    (neg : c<0) (odd : c%2=1) : c= -1 := by
  obtain ⟨i,_,e⟩:=negativeShape w neg
  cases i with
  | zero => simpa using e
  | succ i => rw [pow_succ] at e; omega

private theorem minusOne (t : ℕ) : Carry t 0 (-1) := by
  induction t with
  | zero => exact .start
  | succ t ih => exact .even ih

/-- A signed numerator -1 directly gives an ordinary meeting with the Mersenne
input indexed by N, including all its initial ascending steps. -/
theorem rescueMinusOne (N t y : ℕ) (h : (2:ℤ)^t*y=3^N-1) :
    atClock (N+t) (2^N-1)=y := by
  have cat (a b x : ℕ) : atClock (a+b) x=atClock b (atClock a x) := by
    induction a generalizing x with
    | zero => simp [atClock]
    | succ a ih => simpa [Nat.succ_add,atClock] using ih (shortcut x)
  have peak := ascent N 1 (by decide)
  simp only [Nat.mul_one] at peak
  rw [cat,peak]
  exact realize (minusOne t) N y (by simpa [sub_eq_add_neg] using h)

/-- A carry certificate selects an actual earlier exponent directly. -/
theorem selectEarlier {t p : ℕ} {c : ℤ} (w : Carry t p c)
    (N y j : ℕ) (lo : t<N) (hi : N<j)
    (value : (2:ℤ)^t*y=3^N+c) :
    ∃ n : ℕ, 0<n ∧ n<j ∧ atClock t (3^n-1)=y := by
  have cnt:=oddCount_le w
  refine ⟨N-p,by omega,by omega,realize w _ _ ?_⟩
  rwa [show N-p+p=N by omega]

/-- Any odd positive carry can be recognized at its last odd step. Its binary
clock coefficient is at most c+3, uniformly in the originally supplied clock. -/
theorem positiveDeadline {t p : ℕ} {c : ℤ} (w : Carry t p c)
    (pos : 0<c) (odd : c%2=1) :
    ∃ i q : ℕ, i+1≤t ∧ (2:ℤ)^i≤c+3 ∧ Carry (i+1) q c := by
  induction w with
  | start => omega
  | @even t p c w ih =>
    obtain ⟨i,q,l,b,s⟩:=ih pos odd
    exact ⟨i,q,by omega,b,s⟩
  | @odd t p c w ih =>
    refine ⟨t,p+1,by omega,?_,.odd w⟩
    cases t with
    | zero => simp at *; omega
    | succ t =>
      have prev : c%2=1 := by rw [pow_succ] at odd; omega
      by_cases neg : c<0
      · rw [negativeOdd w neg prev]; omega
      · omega

/-- Signed affine numerator starting from an arbitrary numerator c and denominator m. -/
def signedNumerator : List Bool → ℤ → ℤ → ℤ
  | [],_,c => c
  | bit::rest,m,c =>
    signedNumerator rest (2*m) (if bit then 3*c+m else c)

/-- Uniform sign obstruction for all supplied branch words. The denominator
after the word is m times 2^length. -/
theorem negativePrefix (word : List Bool) (m c : ℤ) (hm : 0<m)
    (deep : c ≤ -(m*2^word.length)) :
    signedNumerator word m c ≤ c := by
  induction word generalizing m c with
  | nil => exact le_refl _
  | cons bit rest ih =>
    simp only [List.length_cons, pow_succ] at deep
    have power : 1≤(2:ℤ)^rest.length := by
      exact one_le_pow₀ (by decide)
    have small : 3*c+m≤c := by nlinarith only [deep,hm,power,mul_nonneg (le_of_lt hm) (sub_nonneg.mpr power)]
    have base : c ≤ -(2*m*2^rest.length) := by nlinarith only [deep]
    cases bit with
    | false => exact ih _ _ (by omega) base
    | true => exact (ih _ _ (by omega) (small.trans base)).trans small

#print axioms negativePrefix
#print axioms selectEarlier
#print axioms positiveDeadline
#print axioms realize
#print axioms physical
#print axioms negativeShape
#print axioms negativeOdd
#print axioms rescueMinusOne

end CollatzAllMersenneCarries
