module
public import PassageOrbitAllTimes
import all PassageOrbitDenominator
import all PassageOrbitHeights
public section

namespace Collatz.Itinerary.PassageOrbit

/-- Remove the whole primary part for every entry in a finite list.
Repeated entries and entries that are not prime have no effect. -/
def outside : List ℕ → ℕ → ℕ
  | [], n => n
  | p::ps, n => outside ps (ordCompl[p] n)

theorem outside_mul (ps : List ℕ) (x y : ℕ) : outside ps (x*y)=outside ps x*outside ps y := by
  induction ps generalizing x y with
  | nil => rfl
  | cons p ps ih => simp only [outside,Nat.ordCompl_mul,ih]

theorem outside_le (ps : List ℕ) (n : ℕ) : outside ps n≤n := by
  induction ps generalizing n with
  | nil => exact Nat.le_refl _
  | cons p ps ih => exact (ih _).trans (Nat.ordCompl_le ..)

theorem outside_pos (ps : List ℕ) {n : ℕ} (np : 0<n) : 0<outside ps n := by
  induction ps generalizing n with
  | nil => exact np
  | cons p ps ih => exact ih (Nat.ordCompl_pos p np.ne')

theorem outside_one (ps : List ℕ) : outside ps 1=1 := by
  have a := outside_pos ps (by decide : 0<1)
  have b := outside_le ps 1
  omega

theorem outside_valuation (ps : List ℕ) (n q : ℕ) : (outside ps n).factorization q=
    if q∈ps then 0 else n.factorization q := by
  induction ps generalizing n with
  | nil => simp [outside]
  | cons p ps ih =>
    rw [outside,ih,Nat.factorization_ordCompl]
    by_cases same : q=p
    · subst q; simp
    · simp [same,Finsupp.erase_ne same]

theorem outside_one_iff (ps : List ℕ) {n : ℕ} (np : 0<n) :
    outside ps n=1 ↔ ∀q, q.Prime → q ∣ n → q∈ps := by
  constructor
  · intro h q qp qd
    by_contra hn
    have eq := outside_valuation ps n q
    rw [h] at eq
    have nz := qp.factorization_pos_of_dvd np.ne' qd
    simp [hn] at eq
    omega
  · intro supported
    apply Nat.eq_of_factorization_eq (outside_pos ps np).ne' (by decide)
    intro q
    rw [outside_valuation]
    by_cases inside : q∈ps
    · simp [inside]
    · rw [ite_eq_right_iff.mpr (fun h => False.elim (inside h))]
      simp only [Nat.factorization_one,Finsupp.zero_apply]
      rw [Nat.factorization_eq_zero_iff]
      by_cases prime : q.Prime
      · exact Or.inr (Or.inl (fun qd => inside (supported q prime qd)))
      · exact Or.inl prime

theorem return_denominator {a t : ℕ} (tp : 0<t) (ret : run t a=a) : denominator a t=1 := by
  unfold denominator
  rw [ret]
  simp only [Nat.dist,Nat.sub_self,Nat.add_zero,Nat.gcd_zero_right]
  exact Nat.div_self (determinant_pos tp)

/-- Finite elementary transfer from the prime-to-S determinant to the
prime-to-S part of the actual reduced denominator of a nonreturn. -/
theorem rough_denominator {a t : ℕ} (ps : List ℕ) (nr : run t a≠a)
    (outsideBound : 2^(7*t)≤(outside ps (determinant a t))^8) :
    2^t≤((a+1)*outside ps (denominator a t))^4 := by
  let g := (determinant a t).gcd (Nat.dist (run t a) a)
  let d := denominator a t
  let b := (a+1)*outside ps d
  have recov : g*d=determinant a t := Nat.mul_div_cancel' (Nat.gcd_dvd_left ..)
  have up : 2^t*outside ps (determinant a t) ≤ 3^t*b := calc
    _ = (2^t*outside ps g)*outside ps d := by rw [←recov,outside_mul]; ring
    _ ≤ (2^t*g)*outside ps d := by gcongr; exact outside_le ..
    _ ≤ (3^t*(a+1))*outside ps d := Nat.mul_le_mul_right _ (gcd_height nr)
    _ = _ := by dsimp [b]; ring
  have calc₁ : 4^t*3^(8*t)≤2^(15*t) := by
    rw [pow_mul,pow_mul,←mul_pow]
    exact Nat.pow_le_pow_left (by decide : 4*3^8≤2^15) t
  have calc₂ : 2^(15*t)≤(3^t*b)^8 := calc
    _ = (2^t)^8*2^(7*t) := by rw [←pow_mul,←pow_add]; congr 1; ring
    _ ≤ (2^t)^8*(outside ps (determinant a t))^8 := Nat.mul_le_mul_left _ outsideBound
    _ = (2^t*outside ps (determinant a t))^8 := (mul_pow ..).symm
    _ ≤ _ := Nat.pow_le_pow_left up _
  have cancel := calc₁.trans calc₂
  rw [mul_pow,←pow_mul,Nat.mul_comm t 8,Nat.mul_comm (3^(8*t))] at cancel
  have squared := Nat.le_of_mul_le_mul_right cancel (by positivity)
  have form : (2^t)^2≤(b^4)^2 := by
    rw [←pow_mul,←pow_mul,Nat.mul_comm t 2,pow_mul]
    exact squared
  exact (Nat.pow_le_pow_iff_left (by decide : 2≠0)).mp form

/-- Rational slopes of finitely many exceptional lines can be written
mX=nY with positive n bounded by B for lines meeting the positive quadrant.
The written proof obtains such a cover from the p-adic Subspace Theorem. -/
def ExceptionalLineCover (ps : List ℕ) (B : ℕ) : Prop :=
  ∀t u : ℕ, 0<t → 0<u → (outside ps (Nat.dist (2^t) (3^u)))^8 < 2^(7*t) →
    ∃m n : ℕ, 0<n ∧ n≤B ∧ m*2^t=n*3^u

theorem outside_bound_of_lines {ps : List ℕ} {B t u : ℕ} (cover : ExceptionalLineCover ps B)
    (tp : 0<t) (up : 0<u) (large : B<2^t) :
    2^(7*t)≤(outside ps (Nat.dist (2^t) (3^u)))^8 := by
  by_contra! bad
  obtain ⟨m,n,np,nb,line⟩ := cover t u tp up bad
  have cop : (2^t).Coprime (3^u) := ((by decide : Nat.Coprime 2 3).pow_left t).pow_right u
  have dv : 2^t ∣ n*3^u := line ▸ Nat.dvd_mul_left _ _
  have small := Nat.le_of_dvd np (cop.dvd_of_dvd_mul_right dv)
  omega

private theorem zero_carry {a t : ℕ} (h : oddCount a t=0) : carry a t=0 := by
  induction t with
  | zero => rfl
  | succ t ih =>
    rw [oddCount] at h
    have old : oddCount a t=0 := by omega
    have even : run t a%2=0 := by omega
    simp [carry,even,ih old]

theorem positive_odd_count {a t : ℕ} (ap : 0<a) (big : a<2^t) : 0<oddCount a t := by
  by_contra! z
  have zz : oddCount a t=0 := by omega
  have aff := affine_identity a t
  rw [zz,zero_carry zz] at aff
  simp at aff
  have dv : 2^t ∣ a := ⟨run t a,aff.symm⟩
  exact (Nat.not_le_of_gt big) (Nat.le_of_dvd ap dv)

/-- The finite-line input is explicit. All other steps in the eventual
prime-support equivalence are kernel-checked. -/
theorem eventual_supported_iff {a : ℕ} (ap : 0<a) (ps : List ℕ)
    (lines : ∃B, ExceptionalLineCover ps B) :
    ∃T, ∀t≥T, (∀q, q.Prime → q ∣ denominator a t → q∈ps) ↔ run t a=a := by
  obtain ⟨B,cover⟩ := lines
  refine ⟨B+(a+1)^4+a+1,fun t late => ?_⟩
  have tp : 0<t := by omega
  have power := Nat.lt_two_pow_self (n:=t)
  have up := positive_odd_count ap (by omega : a<2^t)
  have obs := outside_bound_of_lines cover tp up (by omega : B<2^t)
  rw [←outside_one_iff _ (denominator_pos (a:=a) tp)]
  constructor
  · intro supp
    by_contra nr
    have heavy := rough_denominator ps nr obs
    rw [supp,Nat.mul_one] at heavy
    omega
  · intro ret
    rw [return_denominator tp ret,outside_one]

#print axioms eventual_supported_iff
end Collatz.Itinerary.PassageOrbit
