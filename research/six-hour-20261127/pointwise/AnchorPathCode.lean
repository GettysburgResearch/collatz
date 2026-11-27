import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! An exact signed anchor word has an injective binary carry code at a fixed length.
The rational endpoint fixes this code when the total division exponent is known. -/
namespace AnchorPathCode

def code : List ℕ → ℕ
  | [] => 1
  | a :: rest => 3 ^ rest.length + 2 ^ a * code rest

def Positive (w : List ℕ) : Prop := ∀ e ∈ w, 0 < e

def Follows (t : ℚ) : List ℕ → ℚ → Prop
  | [], u => u = t
  | e :: rest, u => ∃ v : ℚ, 2^e * v = 3*t-1 ∧ Follows v rest u

theorem positive_tail {e : ℕ} {w : List ℕ} (h : Positive (e :: w)) : Positive w :=
  fun i hi => h i (List.mem_cons_of_mem e hi)

theorem code_odd (w : List ℕ) (h : Positive w) : Odd (code w) := by
  cases w with
  | nil => simp [code]
  | cons a rest =>
    have ha := h a (by simp)
    have he : Even (2 ^ a : ℕ) := (even_two.pow_of_ne_zero ha.ne')
    have ho : Odd (3 ^ rest.length : ℕ) := (by decide : Odd (3:ℕ)).pow
    exact ho.add_even (he.mul_right (code rest))

private theorem unique_scale {i j a b : ℕ} (ha : Odd a) (hb : Odd b)
    (h : 2^i*a=2^j*b) : i=j ∧ a=b := by
  have strip {i j a b : ℕ} (hi : i<j) (hao : Odd a) (hh : 2^i*a=2^j*b) : False := by
    obtain ⟨d, hd⟩ := Nat.exists_eq_add_of_lt hi
    have hj : j = i+(d+1) := by omega
    rw [hj, pow_add, Nat.mul_assoc] at hh
    have eq := Nat.eq_of_mul_eq_mul_left (by positivity : 0 < 2 ^ i) hh
    have he : Even (2^(d+1):ℕ) := even_two.pow_of_ne_zero (by omega)
    have hboth : Even a := eq ▸ he.mul_right b
    obtain ⟨r,hr⟩ := hao
    obtain ⟨s,hs⟩ := hboth
    omega
  have ij : i=j := by
    rcases lt_trichotomy i j with lt | eq | gt
    · exact (strip lt ha h).elim
    · exact eq
    · exact (strip gt hb h.symm).elim
  subst j
  exact ⟨rfl, Nat.eq_of_mul_eq_mul_left (by positivity : 0 < 2 ^ i) h⟩

theorem injective_at_length {a b : List ℕ} (ha : Positive a) (hb : Positive b)
    (lengths : a.length=b.length) (codes : code a=code b) : a=b := by
  induction a generalizing b with
  | nil =>
    simpa using lengths.symm
  | cons e w ih =>
    cases b with
    | nil => simp at lengths
    | cons f u =>
      have l : w.length=u.length := by simpa using lengths
      simp only [code,l,Nat.add_left_cancel_iff] at codes
      obtain ⟨ef,wu⟩ := unique_scale (code_odd w (positive_tail ha))
        (code_odd u (positive_tail hb)) codes
      rw [ef,ih (positive_tail ha) (positive_tail hb) l wu]

theorem transport {t u : ℚ} {w : List ℕ} (h : Follows t w u) :
    (code w : ℚ) = 3^w.length*t + 2^w.sum*(1-u) := by
  induction w generalizing t with
  | nil =>
    change u=t at h
    simp [code,h]
  | cons e rest ih =>
    obtain ⟨v,hv,hu⟩ := h
    have prev := ih hu
    simp only [code, Nat.cast_add, Nat.cast_pow, Nat.cast_ofNat, Nat.cast_mul,
      List.length_cons, List.sum_cons, pow_add, pow_one]
    rw [prev]
    linear_combination (3:ℚ)^rest.length * hv

theorem endpoints_length_budget_unique {t u : ℚ} {a b : List ℕ}
    (ha : Positive a) (hb : Positive b) (pa : Follows t a u) (pb : Follows t b u)
    (lengths : a.length=b.length) (budgets : a.sum=b.sum) : a=b := by
  apply injective_at_length ha hb lengths
  have eq : (code a : ℚ) = (code b : ℚ) := by rw [transport pa,transport pb,lengths,budgets]
  exact_mod_cast eq

end AnchorPathCode

#print axioms AnchorPathCode.positive_tail
#print axioms AnchorPathCode.code_odd
#print axioms AnchorPathCode.unique_scale
#print axioms AnchorPathCode.injective_at_length
#print axioms AnchorPathCode.transport
#print axioms AnchorPathCode.endpoints_length_budget_unique
