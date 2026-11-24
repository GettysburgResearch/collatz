import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

/-! Exact arithmetic behind the entropy of ordinary residues. A letter `a`
represents the positive odd-step exponent `a+1`. -/
namespace Collatz.AuxiliaryResidues

/-- Complete binary clock. -/
def clock : List ℕ → ℕ
  | [] => 0
  | a :: w => a + 1 + clock w

/-- The affine carry plus `2^(clock w)`. The terminal one distinguishes the last gap. -/
def code : List ℕ → ℕ
  | [] => 1
  | a :: w => 3 ^ w.length + 2 ^ (a + 1) * code w

/-- Literal forward edges, with no change of source along the word. -/
inductive Path : ℕ → List ℕ → ℕ → Prop
  | nil (x : ℕ) : Path x [] x
  | cons {x y z a : ℕ} {w : List ℕ} :
      2 ^ (a + 1) * y = 3*x+1 → Path y w z → Path x (a :: w) z

/-- Exact observation from two ordinary endpoint values and the total clock. -/
theorem path_identity {x y : ℕ} {w : List ℕ} (h : Path x w y) :
    2 ^ clock w * (y+1) = 3 ^ w.length * x + code w := by
  induction h with
  | nil => simp [clock, code]
  | @cons x y z a w edge _ ih =>
    change 2^((a+1)+clock w) * (z+1) = 3^(w.length+1)*x + (3^w.length + 2^(a+1)*code w)
    rw [pow_add 2 (a+1) (clock w), Nat.mul_assoc, ih, pow_succ 3]
    calc
      _ = 3^w.length * (2^(a+1)*y) + 2^(a+1)*code w := by ring
      _ = _ := by rw [edge]; ring

private theorem code_odd (w : List ℕ) : Odd (code w) := by
  cases w with
  | nil => exact odd_one
  | cons a w =>
    have h : Even (2^(a+1) * code w) := by
      exact ((even_two.pow_of_ne_zero (by omega : a+1 ≠ 0))).mul_right _
    exact (show Odd (3:ℕ) by decide).pow.add_even h

private theorem recover_exponent {a b u v : ℕ} (hu : Odd u) (hv : Odd v)
    (h : 2^a*u = 2^b*v) : a=b := by
  have hu0 : u ≠ 0 := by rintro rfl; exact Nat.not_odd_zero hu
  have hv0 : v ≠ 0 := by rintro rfl; exact Nat.not_odd_zero hv
  have hu2 : u.factorization 2 = 0 := Nat.factorization_eq_zero_of_not_dvd
    (fun d => (Nat.not_even_iff_odd.mpr hu) ((even_iff_two_dvd).mpr d))
  have hv2 : v.factorization 2 = 0 := Nat.factorization_eq_zero_of_not_dvd
    (fun d => (Nat.not_even_iff_odd.mpr hv) ((even_iff_two_dvd).mpr d))
  have eqn := congrArg (fun z : ℕ => z.factorization 2) h
  simpa [Nat.factorization_mul (by positivity : (2:ℕ)^a ≠ 0) hu0,
    Nat.factorization_mul (by positivity : (2:ℕ)^b ≠ 0) hv0,
    Nat.Prime.factorization_pow Nat.prime_two, hu2, hv2] using eqn

/-- Length and the integer observation recover every ordered positive gap. -/
theorem code_injective {u v : List ℕ} (len : u.length = v.length)
    (obs : code u = code v) : u = v := by
  induction u generalizing v with
  | nil => simpa using len.symm
  | cons a u ih =>
    cases v with
    | nil => simp at len
    | cons b v =>
      have len' : u.length = v.length := by simpa using len
      simp only [code, len', Nat.add_right_inj] at obs
      have eq := recover_exponent (code_odd u) (code_odd v) obs
      have ab : a=b := by omega
      subst b
      have tail := Nat.eq_of_mul_eq_mul_left (by positivity : 0 < (2:ℕ)^(a+1)) obs
      rw [ih len' tail]

/-- For any modulus, two endpoint residues and a common total recover the
whole ordered word whenever its integer observation is below the modulus. -/
theorem residue_decoder {x y x' y' M : ℕ} {u v : List ℕ}
    (pu : Path x u y) (pv : Path x' v y') (len : u.length = v.length)
    (tot : clock u = clock v) (src : x ≡ x' [MOD M]) (dst : y ≡ y' [MOD M])
    (bu : code u < M) (bv : code v < M) : u = v := by
  have h := (dst.add_right 1).mul_left (2 ^ clock u)
  rw [path_identity pu, tot, path_identity pv, len] at h
  have hcode := Nat.ModEq.add_left_cancel (src.mul_left (3^v.length)) h
  apply code_injective len
  simpa [Nat.ModEq, Nat.mod_eq_of_lt bu, Nat.mod_eq_of_lt bv] using hcode

/-- Two different modular words of equal clock and length can land together
only at moduli dividing their nonzero observation difference. There is no
ordinary common-source legality assumption in this modular statement. -/
theorem collision_codes {x y y' M : ℕ} {u v : List ℕ}
    (hu : 2^clock u * (y+1) ≡ 3^u.length*x + code u [MOD M])
    (hv : 2^clock v * (y'+1) ≡ 3^v.length*x + code v [MOD M])
    (len : u.length = v.length) (tot : clock u = clock v)
    (same : y ≡ y' [MOD M]) (diff : u ≠ v) :
    code u ≡ code v [MOD M] ∧ code u ≠ code v := by
  have hs := (same.add_right 1).mul_left (2^clock u)
  rw [tot] at hs hu
  rw [len] at hu
  exact ⟨(hu.symm.trans (hs.trans hv)).add_left_cancel' _, fun e => diff (code_injective len e)⟩

/-- Uniform integer height of the observation for actual gaps in {1,2,3}. -/
theorem code_bound {w : List ℕ} (small : ∀ a ∈ w, a < 3) :
    code w ≤ 16^w.length := by
  induction w with
  | nil => simp [code]
  | cons a w ih =>
    have ha : a < 3 := small a (by simp)
    have ht := ih (fun b hb => small b (by simp [hb]))
    have hm : (2:ℕ)^(a+1) ≤ 8 := by
      exact Nat.pow_le_pow_right (by decide : 0 < 2) (by omega : a+1 ≤ 3)
    have h3 : (3:ℕ)^w.length ≤ 16^w.length := Nat.pow_le_pow_left (by decide) _
    simp only [code, List.length_cons, pow_succ (16:ℕ)]
    have hb := Nat.mul_le_mul hm ht
    omega

/-- The equal-clock words with raw gaps (1,2) and (2,1) differ by a
quarter translation. Exact invariance under both forces invariance under
translation by one. This works over composite moduli prime to six. -/
theorem swap_translation {R X : Type*} [CommRing R] (f : R → X)
    (u t : R) (invNine : 9*u=1) (invFour : 4*t=1)
    (first : ∀ x y : R, 8*y=9*x+5 → f y=f x)
    (second : ∀ x y : R, 8*y=9*x+7 → f y=f x) (y : R) : f (y+1)=f y := by
  have quarter (z : R) : f (z+t)=f z := by
    let x := u*(8*z-5)
    have hx : 9*x=8*z-5 := by dsimp [x]; rw [← mul_assoc, invNine, one_mul]
    have a : 8*z=9*x+5 := by rw [hx]; ring
    have b : 8*(z+t)=9*x+7 := by rw [hx]; linear_combination 2*invFour
    exact (second x (z+t) b).trans (first x z a).symm
  have h : y+1 = (((y+t)+t)+t)+t := by linear_combination -invFour
  rw [h, quarter, quarter, quarter, quarter]

/-- An actual return to a residue gives the signed center congruence, even
when the slope difference and modulus are not coprime. -/
theorem return_congruence {x y : ℕ} {M r : ℤ} {w : List ℕ} (hw : Path x w y)
    (hx : M ∣ (x:ℤ)-r) (hy : M ∣ (y:ℤ)-r) :
    M ∣ ((2:ℤ)^clock w-3^w.length)*r-((code w:ℤ)-2^clock w) := by
  have obs : (2:ℤ)^clock w*((y:ℤ)+1)=3^w.length*(x:ℤ)+(code w:ℤ) := by
    exact_mod_cast path_identity hw
  have eqn : ((2:ℤ)^clock w-3^w.length)*r-((code w:ℤ)-2^clock w) =
      3^w.length*((x:ℤ)-r)-2^clock w*((y:ℤ)-r) := by nlinarith only [obs]
  rw [eqn]
  exact dvd_sub (dvd_mul_of_dvd_right hx _) (dvd_mul_of_dvd_right hy _)

/-- Two short returns to one residue have identical rational centers if the
nonzero modulus exceeds their signed cross determinant in absolute value. -/
theorem return_center_equal {M r d e c f : ℤ}
    (h1 : M ∣ d*r-c) (h2 : M ∣ e*r-f)
    (small : (d*f-e*c).natAbs < M.natAbs) : d*f=e*c := by
  have h : M ∣ e*(d*r-c)-d*(e*r-f) :=
    dvd_sub (dvd_mul_of_dvd_right h1 _) (dvd_mul_of_dvd_right h2 _)
  have eqn : e*(d*r-c)-d*(e*r-f)=d*f-e*c := by ring
  rw [eqn] at h
  exact sub_eq_zero.mp (Int.eq_zero_of_dvd_of_natAbs_lt_natAbs h small)

#print axioms path_identity
#print axioms code_injective
#print axioms residue_decoder
#print axioms collision_codes
#print axioms code_bound
#print axioms swap_translation
#print axioms return_congruence
#print axioms return_center_equal
end Collatz.AuxiliaryResidues
