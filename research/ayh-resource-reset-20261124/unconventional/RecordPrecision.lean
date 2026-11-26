import NonunitExit
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Data.Int.GCD

/-! Exact finite arithmetic for two observations on a single ordinary shortcut path.
The analytic Diophantine estimates are separate written results. -/
namespace Collatz.RecordPrecision

open NonunitExit
set_option autoImplicit false

/-- The numerator added along the actual `n` branches from `x`. -/
def carry : ℕ → ℕ → ℕ
  | 0, _ => 0
  | n+1, x =>
    let next := stepD 1 x
    3^(gradeD 1 n next)*(x%2) + 2*carry n next

private theorem one_step (x : ℕ) :
    2*stepD 1 x = 3^(x%2)*x+x%2 := by
  unfold stepD
  by_cases h : x%2=0
  · simp [h]; omega
  · have hx : x%2=1 := by omega
    simp [hx]; omega

theorem ordinary_row (n x : ℕ) :
    2^n*iterD 1 n x = 3^(gradeD 1 n x)*x+carry n x := by
  induction n generalizing x with
  | zero => simp [iterD,gradeD,carry]
  | succ n ih =>
    let z := stepD 1 x
    change 2^(n+1)*iterD 1 n z =
      3^(gradeD 1 n z+x%2)*x+(3^(gradeD 1 n z)*(x%2)+2*carry n z)
    calc
      _ = 2*(2^n*iterD 1 n z) := by rw [pow_succ]; ring
      _ = 3^(gradeD 1 n z)*(2*z)+2*carry n z := by rw [ih]; ring
      _ = _ := by rw [show 2*z=3^(x%2)*x+x%2 from one_step x,pow_add]; ring

theorem grade_le_clock (n x : ℕ) : gradeD 1 n x ≤ n := by
  induction n generalizing x with
  | zero => simp [gradeD]
  | succ n ih =>
    have h := ih (stepD 1 x)
    simp only [gradeD]
    omega

theorem carry_le (n x : ℕ) : carry n x ≤ 3^n := by
  induction n generalizing x with
  | zero => simp [carry]
  | succ n ih =>
    let z := stepD 1 x
    have h₁ : 3^(gradeD 1 n z) ≤ 3^n := Nat.pow_le_pow_right (by decide) (grade_le_clock n z)
    have h₂ : 3^(gradeD 1 n z)*(x%2) ≤ 3^n := calc
      _ ≤ 3^(gradeD 1 n z)*1 := Nat.mul_le_mul_left _ (by omega)
      _ ≤ 3^n := by simpa only [mul_one] using h₁
    have h₃ := ih z
    change 3^(gradeD 1 n z)*(x%2)+2*carry n z ≤ 3^(n+1)
    rw [pow_succ]; omega

/-- Sharp carry envelope at fixed bit count and odd count.  Equality holds
for a block of all its zero bits followed by all its one bits. -/
theorem carry_plus_clock_le (n x : ℕ) :
    carry n x + 2^n ≤ 2^(n-gradeD 1 n x)*3^(gradeD 1 n x) := by
  induction n generalizing x with
  | zero => simp [carry,gradeD]
  | succ n ih =>
    let z := stepD 1 x
    let g := gradeD 1 n z
    have hg : g ≤ n := grade_le_clock n z
    have ht : carry n z + 2^n ≤ 2^(n-g)*3^g := ih z
    change 3^g*(x%2)+2*carry n z + 2^(n+1) ≤
      2^(n+1-(g+x%2))*3^(g+x%2)
    by_cases he : x%2=0
    · rw [he,add_zero,mul_zero,zero_add,show n+1-g=(n-g)+1 by omega,
          pow_succ,pow_succ]
      calc
        _ = 2*(carry n z + 2^n) := by ring
        _ ≤ 2*(2^(n-g)*3^g) := Nat.mul_le_mul_left _ ht
        _ = _ := by ring
    · have ho : x%2=1 := by omega
      rw [ho,mul_one,show n+1-(g+1)=n-g by omega,pow_succ,pow_succ]
      have ha : 3^g ≤ 2^(n-g)*3^g :=
        Nat.le_mul_of_pos_left _ (Nat.pow_pos (by decide))
      calc
        _ = 3^g+2*(carry n z + 2^n) := by ring
        _ ≤ 2^(n-g)*3^g+2*(2^(n-g)*3^g) :=
          Nat.add_le_add ha (Nat.mul_le_mul_left _ ht)
        _ = _ := by ring

/-- Signed displacement of two independently supplied rational labels with a common
integer denominator. This identity keeps the actual source and actual terminal. -/
theorem shifted_row (n x : ℕ) (d a b : ℤ) :
    (2:ℤ)^n*(d*(iterD 1 n x:ℤ)-b) - (3:ℤ)^(gradeD 1 n x)*(d*(x:ℤ)-a) =
      d*(carry n x:ℤ)+(3:ℤ)^(gradeD 1 n x)*a-(2:ℤ)^n*b := by
  have h : (2:ℤ)^n*(iterD 1 n x:ℤ) =
      (3:ℤ)^(gradeD 1 n x)*(x:ℤ)+(carry n x:ℤ) := by
    exact_mod_cast ordinary_row n x
  calc
    _ = d*((2:ℤ)^n*(iterD 1 n x:ℤ)) -
        d*((3:ℤ)^(gradeD 1 n x)*(x:ℤ)) +
        (3:ℤ)^(gradeD 1 n x)*a-(2:ℤ)^n*b := by ring
    _ = _ := by rw [h]; ring

/-- The two endpoint displacements on an exact rational arc are obtained
from one ordinary integer. No sign or divisibility of the labels is assumed. -/
theorem zero_shift_parameter (m s : ℕ) (A B : ℤ)
    (row : (2:ℤ)^s*B=(3:ℤ)^m*A) :
    ∃ w : ℤ, A=(2:ℤ)^s*w ∧ B=(3:ℤ)^m*w := by
  have cp : IsCoprime (2:ℤ) 3 := ⟨-1,1,by decide⟩
  have divides : (2:ℤ)^s ∣ A :=
    cp.pow.dvd_of_dvd_mul_left ⟨B, row.symm⟩
  obtain ⟨w,hw⟩ := divides
  refine ⟨w,hw,?_⟩
  apply mul_left_cancel₀ (show (2:ℤ)^s ≠ 0 by positivity)
  rw [row,hw]; ring

/-- A rational fixed point of the observed block has binary agreement
with the source and ternary agreement with the terminal. -/
theorem closing_matches (n x : ℕ) (d a : ℤ)
    (hfix : ((2:ℤ)^n-(3:ℤ)^(gradeD 1 n x))*a=d*(carry n x:ℤ)) :
    (2:ℤ)^n ∣ d*(x:ℤ)-a ∧
    (3:ℤ)^(gradeD 1 n x) ∣ d*(iterD 1 n x:ℤ)-a := by
  have hr := shifted_row n x d a a
  rw [← hfix] at hr
  have hzero : ((2:ℤ)^n-(3:ℤ)^(gradeD 1 n x))*a +
      (3:ℤ)^(gradeD 1 n x)*a-(2:ℤ)^n*a=0 := by ring
  rw [hzero,sub_eq_zero] at hr
  obtain ⟨w,hs,ht⟩ := zero_shift_parameter (gradeD 1 n x) n _ _ hr
  exact ⟨⟨w,hs⟩,⟨w,ht⟩⟩

/-- At two distinct primes, the valuations charged to the same parameter
are paid only once. This also covers signed parameters. -/
theorem disjoint_powers (w : ℤ) (h k : ℕ) (hw : w≠0)
    (h₂ : (2:ℤ)^h ∣ w) (h₃ : (3:ℤ)^k ∣ w) :
    2^h*3^k ≤ w.natAbs := by
  have cp : IsCoprime (2:ℤ) 3 := ⟨-1,1,by decide⟩
  have hd := Int.natAbs_dvd_natAbs.mpr (cp.pow.mul_dvd h₂ h₃)
  have hpos : 0<w.natAbs := Int.natAbs_pos.mpr hw
  have hcast : ((2:ℤ)^h*3^k).natAbs = 2^h*3^k := by
    simp [Int.natAbs_mul, Int.natAbs_pow]
  rw [hcast] at hd
  exact Nat.le_of_dvd hpos hd

/-- Every prime-two and prime-three monomial is coprime to a mixed raw
clock difference with both exponents positive. -/
theorem clock_difference_coprime (s m h k : ℕ) :
    IsCoprime ((2:ℤ)^(s+1)-3^(m+1)) (2^h*3^k) := by
  have cp : IsCoprime (2:ℤ) 3 := ⟨-1,1,by decide⟩
  obtain ⟨a,b,hab⟩ := cp.pow (m := s+1) (n := m+1)
  let X : ℤ := 2^(s+1)
  let Y : ℤ := 3^(m+1)
  change a*X+b*Y=1 at hab
  have hx : IsCoprime (X-Y) X := ⟨-b,a+b,by calc
    _ = a*X+b*Y := by ring
    _ = 1 := hab⟩
  have hy : IsCoprime (X-Y) Y := ⟨a,a+b,by calc
    _ = a*X+b*Y := by ring
    _ = 1 := hab⟩
  have hd2 : IsCoprime (X-Y) 2 := by
    exact (show IsCoprime (X-Y) ((2:ℤ)^s*2) by simpa [X,pow_succ] using hx).of_mul_right_right
  have hd3 : IsCoprime (X-Y) 3 := by
    exact (show IsCoprime (X-Y) ((3:ℤ)^m*3) by simpa [Y,pow_succ] using hy).of_mul_right_right
  exact hd2.pow_right.mul_right hd3.pow_right

/-- In the translated fixed-phase equation for a word with one zero, every
integer denominator is a multiple of the entire raw clock difference. -/
theorem one_zero_denominator_dvd (s m h k : ℕ) (d z : ℤ)
    (fixedRow : d*((2:ℤ)^h*3^k)=((2:ℤ)^(s+1)-3^(m+1))*z) :
    (2:ℤ)^(s+1)-3^(m+1) ∣ d :=
  (clock_difference_coprime s m h k).dvd_of_dvd_mul_right ⟨z,fixedRow⟩

/-- Beyond an explicit dyadic-size threshold, a rational plane meeting an
actual prefix vector must evaluate at one fixed terminal. -/
theorem fixed_plane_late (n x : ℕ) (r t w : ℤ)
    (late : (r-w*(x:ℤ)).natAbs < 2^n)
    (plane : r*(3:ℤ)^(gradeD 1 n x)+t*(2:ℤ)^n+w*(carry n x:ℤ)=0) :
    r=w*(x:ℤ) ∧ t= -w*(iterD 1 n x:ℤ) := by
  let X : ℤ := 3^(gradeD 1 n x)
  let Y : ℤ := 2^n
  let v : ℤ := iterD 1 n x
  have hr : Y*v=X*(x:ℤ)+(carry n x:ℤ) := by
    dsimp only [X,Y,v]
    exact_mod_cast ordinary_row n x
  change r*X+t*Y+w*(carry n x:ℤ)=0 at plane
  have hc : (carry n x:ℤ)=Y*v-X*(x:ℤ) := by omega
  rw [hc] at plane
  have he : X*(r-w*(x:ℤ))=Y*(-(t+w*v)) := by
    ring_nf at plane ⊢
    omega
  have cp : IsCoprime (2:ℤ) 3 := ⟨-1,1,by decide⟩
  have hd : (2:ℤ)^n ∣ r-w*(x:ℤ) :=
    cp.pow.dvd_of_dvd_mul_left ⟨-(t+w*v),he⟩
  have hz : r-w*(x:ℤ)=0 := by
    by_contra hne
    have hh := Int.natAbs_dvd_natAbs.mpr hd
    have hpos := Int.natAbs_pos.mpr hne
    have hle := Nat.le_of_dvd hpos hh
    simp [Int.natAbs_pow] at hle
    omega
  rw [hz,mul_zero] at he
  have hy : Y≠0 := by dsimp [Y]; positivity
  have ht := (mul_eq_zero.mp he.symm).resolve_left hy
  constructor
  · omega
  · change t= -w*v
    rw [neg_mul]
    omega

/-- On one injective ordinary path, at most one sufficiently late prefix
vector can lie in a fixed nonzero integral plane. -/
theorem fixed_plane_unique_late (x i j : ℕ) (r t w : ℤ)
    (hinj : Function.Injective (fun n => iterD 1 n x))
    (nontrivial : r≠0 ∨ t≠0 ∨ w≠0)
    (hi : (r-w*(x:ℤ)).natAbs < 2^i)
    (hj : (r-w*(x:ℤ)).natAbs < 2^j)
    (pi : r*(3:ℤ)^(gradeD 1 i x)+t*(2:ℤ)^i+w*(carry i x:ℤ)=0)
    (pj : r*(3:ℤ)^(gradeD 1 j x)+t*(2:ℤ)^j+w*(carry j x:ℤ)=0) :
    i=j := by
  obtain ⟨hr,hti⟩ := fixed_plane_late i x r t w hi pi
  obtain ⟨_,htj⟩ := fixed_plane_late j x r t w hj pj
  have hw : -w≠0 := by
    intro hn
    have hwz : w=0 := by omega
    simp [hwz] at hr hti nontrivial
    tauto
  have hv := mul_left_cancel₀ hw (hti.symm.trans htj)
  apply hinj
  exact_mod_cast hv

#print axioms ordinary_row
#print axioms grade_le_clock
#print axioms carry_le
#print axioms carry_plus_clock_le
#print axioms shifted_row
#print axioms zero_shift_parameter
#print axioms closing_matches
#print axioms disjoint_powers
#print axioms clock_difference_coprime
#print axioms one_zero_denominator_dvd
#print axioms fixed_plane_late
#print axioms fixed_plane_unique_late
end Collatz.RecordPrecision
