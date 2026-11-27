import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Algebra.Group.Nat.Defs
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Fixed odd-denominator shortcut dynamics and arithmetic interfaces of
the cleared-denominator source sector. -/
set_option autoImplicit false
set_option warningAsError true

namespace EscapeRationalSector

structure Frame where
  num : ℕ
  grade : ℕ
  intercept : ℕ

/-- Keep the initial odd denominator fixed throughout this integer recursion.
The represented value is num/q, even when the fraction is no longer reduced. -/
def frame (q a : ℕ) : ℕ → Frame
  | 0 => ⟨a,0,0⟩
  | n+1 =>
    let old := frame q a n
    if old.num%2=0 then ⟨old.num/2,old.grade,old.intercept⟩
    else ⟨(3*old.num+q)/2, old.grade+1, 3*old.intercept+2^n⟩

theorem exact_affine (q a : ℕ) (odd : q%2=1) (n : ℕ) :
    2^n*(frame q a n).num=3^(frame q a n).grade*a+q*(frame q a n).intercept := by
  induction n with
  | zero => simp [frame]
  | succ n ih =>
    let f := frame q a n
    change 2^n*f.num=3^f.grade*a+q*f.intercept at ih
    by_cases h : f.num%2=0
    · have eq : 2*(f.num/2)=f.num := by omega
      simp only [frame,show (frame q a n).num%2=0 from h,ite_true]
      change 2^(n+1)*(f.num/2) = 3^f.grade*a+q*f.intercept
      calc
        _ = 2^n*(2*(f.num/2)) := by rw [pow_succ]; ring
        _ = _ := by rw [eq,ih]
    · have eq : 2*((3*f.num+q)/2)=3*f.num+q := by omega
      simp only [frame,show ¬(frame q a n).num%2=0 from h,ite_false]
      change 2^(n+1)*((3*f.num+q)/2)=3^(f.grade+1)*a+q*(3*f.intercept+2^n)
      calc
        _ = 2^n*(2*((3*f.num+q)/2)) := by rw [pow_succ]; ring
        _ = 3*(2^n*f.num)+q*2^n := by rw [eq]; ring
        _ = _ := by rw [ih,pow_succ]; ring

/-- Every accepted gate-at-n source is an actual integer at the common clock. -/
theorem denominator_clears (h a n : ℕ)
    (enough : h≤(frame (3^h) a n).grade) : 3^h ∣ (frame (3^h) a n).num := by
  have odd : 3^h%2=1 := by simp [Nat.pow_mod]
  have h1 := exact_affine (3^h) a odd n
  have powDiv : 3^h ∣ 3^(frame (3^h) a n).grade := Nat.pow_dvd_pow 3 enough
  have div : 3^h ∣ 2^n*(frame (3^h) a n).num := by
    rw [h1]
    obtain ⟨c,hc⟩ := powDiv
    use c*a+(frame (3^h) a n).intercept
    rw [hc]
    ring
  exact (Nat.Coprime.pow h n (by decide : Nat.Coprime 3 2)).dvd_of_dvd_mul_left div

theorem shifted_floor_gate (y m u g H : ℕ) (hm : 0<m) (cap : y≤2^H*m)
    (floor : 2^(5*u)*m^5≤2^(8*g)*y^5) : 5*u≤8*g+5*H := by
  have up := Nat.pow_le_pow_left cap 5
  have bound : 2^(5*u)*m^5≤2^(8*g+5*H)*m^5 := calc
    _ ≤ 2^(8*g)*y^5 := floor
    _ ≤ 2^(8*g)*(2^H*m)^5 := Nat.mul_le_mul_left _ up
    _ = 2^(8*g+5*H)*m^5 := by rw [mul_pow,←pow_mul,pow_add]; ring_nf
  have mp : 0<m^5 := pow_pos hm _
  exact (Nat.pow_le_pow_iff_right (by decide : 1<(2:ℕ))).mp
    (Nat.le_of_mul_le_mul_right bound mp)

/-- Consecutive lifts by Q meet each residue modulo three once. -/
theorem triple_residues (Q a : ℕ) (unit : Q%3≠0) :
    a%3≠(a+Q)%3 ∧ a%3≠(a+2*Q)%3 ∧ (a+Q)%3≠(a+2*Q)%3 := by
  omega

theorem native_suffix_cost (p : ℚ) (hp : p≠0) (H k : ℕ) (hk : k≤H) :
    ((1-p)/p)^k * p^k * (1-p)^(H-k)=(1-p)^H := by
  rw [←mul_pow,div_mul_cancel₀ _ hp,←pow_add]
  congr 1
  omega

theorem numerical_floor : 319*4+13<25*13*4 ∧
    29*3^41<(2:ℕ)^71 ∧ (2:ℕ)^71<29*3^42 ∧ (3:ℕ)^17<2^27 := by norm_num

#print axioms exact_affine
#print axioms denominator_clears
#print axioms shifted_floor_gate
#print axioms triple_residues
#print axioms native_suffix_cost
#print axioms numerical_floor
end EscapeRationalSector

