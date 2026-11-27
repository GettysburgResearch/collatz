import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Exact attained levels, integral parity decoding, and physical profile steering.
The archimedean counting and compression estimates are written mathematics. -/

namespace Collatz.AttainedClock

/-- An integer path can pass a level downwards by any amount, but if
the upward step is at most one it first reaches every intervening level. -/
theorem hits_level (L : ℕ → ℤ) (inc : ∀ i, L (i+1) ≤ L i + 1)
    (n : ℕ) (t : ℤ) (lower : L 0 ≤ t) (upper : t ≤ L n) :
    ∃ i ≤ n, L i = t := by
  induction n with
  | zero => exact ⟨0, by omega, by omega⟩
  | succ n ih =>
    by_cases h : t ≤ L n
    · obtain ⟨i,hi,he⟩ := ih h
      exact ⟨i,by omega,he⟩
    · have := inc n
      exact ⟨n+1,by omega,by omega⟩

/-- Source numerator coefficients of an earliest-bit-first physical word. -/
def slope : List Bool → ℤ
  | [] => 1
  | false :: w => slope w
  | true :: w => 3 * slope w

def scale : List Bool → ℤ
  | [] => 1
  | _ :: w => 2 * scale w

def offset : List Bool → ℤ
  | [] => 0
  | false :: w => 2 * offset w
  | true :: w => slope w + 2 * offset w

/-- Each integer edge equation forces its displayed physical parity. -/
def literal : List Bool → ℤ → ℤ → Prop
  | [], x, y => x = y
  | false :: w, x, y => ∃ z : ℤ, x = 2*z ∧ literal w z y
  | true :: w, x, y => ∃ z : ℤ, 3*x+1 = 2*z ∧ literal w z y

theorem slope_odd (w : List Bool) : slope w % 2 = 1 := by
  induction w with
  | nil => decide
  | cons b w ih => cases b <;> simp only [slope] <;> omega

private theorem cancel_half (s a b c : ℤ) (odd : s%2=1)
    (eqn : 2*a=s*b+2*c) : b=2*(b/2) ∧ a=s*(b/2)+c := by
  have hm : (s*b)%2=0 := by omega
  rw [Int.mul_emod,odd,one_mul,Int.emod_emod] at hm
  have even : b=2*(b/2) := by omega
  refine ⟨even,?_⟩
  rw [even] at eqn
  linarith only [eqn]

/-- The full affine equation alone decodes every physical step over the
integers. For a positive source all actual states stay positive. -/
theorem decode (w : List Bool) (x y : ℤ)
    (h : scale w*y = slope w*x + offset w) : literal w x y := by
  induction w generalizing x with
  | nil => simpa [literal,scale,slope,offset,eq_comm] using h
  | cons b w ih =>
    have oddSlope := slope_odd w
    cases b
    · simp only [scale,slope,offset] at h
      have he : 2*(scale w*y)=slope w*x+2*offset w := by linarith only [h]
      obtain ⟨even,next⟩ := cancel_half _ _ _ _ oddSlope he
      exact ⟨x/2,even,ih _ next⟩
    · simp only [scale,slope,offset] at h
      have he : 2*(scale w*y) = slope w*(3*x+1)+2*offset w := by linarith only [h]
      obtain ⟨even,next⟩ := cancel_half _ _ _ _ oddSlope he
      exact ⟨(3*x+1)/2,even,ih _ next⟩

/-- Each admitted literal word belongs to its unique phase class. -/
theorem phase_ledger (words phases : Finset ℕ) (phase : ℕ → ℕ)
    (maps : ∀ w ∈ words, phase w ∈ phases) :
    words.card = ∑ s ∈ phases, (words.filter (fun w => phase w = s)).card :=
  Finset.card_eq_sum_card_fiberwise maps

/-- Equal-grade, odd-discrepancy repair with the intermediate odd
part c'. Parities are enforced by the integral edge equations. -/
theorem equal_grade_repair (x y x₁ y₁ x₂ y₂ x₃ y₃ d c f c' : ℤ)
    (start : y=x+d) (ex : x=2*x₁) (oy : 3*y+1=2*y₁)
    (cc : 2*c=3*d+1) (divide : c=f*c')
    (factor : f≠0) (hx : x₁=f*x₂) (hy : y₁=f*y₂)
    (ox : 3*x₂+1=2*x₃) (ey : y₂=2*y₃) :
    2*(y₃-x₃)=c'-1 := by
  have h₁ : y₁=3*x₁+c := by linarith
  have hz : f*(y₂-3*x₂-c')=0 := by
    calc
      _ = f*y₂-3*(f*x₂)-f*c' := by ring
      _ = 0 := by rw [← hy,← hx,← divide,h₁]; ring
  have h₂ := (mul_eq_zero.mp hz).resolve_left factor
  linarith

theorem repair_contracts (d d' f : ℕ) (hf : 1 ≤ f)
    (law : f*(4*d'+2)=3*d+1) : 4*d' < 3*d := by
  have hm := Nat.mul_le_mul_right (4*d'+2) hf
  omega

/-- One physical step of a positive-grade drop. -/
theorem grade_drop (x y x' y' p d : ℤ)
    (disparity : y=3*p*x+d) (oddx : 3*x+1=2*x') (eveny : y=2*y') :
    2*(y'-p*x')=d-p := by
  calc
    _ = 2*y'-p*(2*x') := by ring
    _ = d-p := by rw [← eveny,← oddx,disparity]; ring

/-- All m shortcut inputs are odd. The last state itself may be even. -/
theorem odd_climb (m : ℕ) (u : ℤ) :
    literal (List.replicate m true) (2^m*u-1) (3^m*u-1) := by
  induction m generalizing u with
  | zero => simp [literal]
  | succ m ih =>
    rw [List.replicate_succ]
    refine ⟨2^m*(3*u)-1,?_,?_⟩
    · rw [pow_succ]
      ring
    · simpa only [pow_succ,mul_assoc] using ih (3*u)

theorem even_descent (d : ℕ) (u : ℤ) :
    literal (List.replicate d false) (2^d*u) u := by
  induction d with
  | zero => simp [literal]
  | succ d ih =>
    rw [List.replicate_succ]
    exact ⟨2^d*u, by rw [pow_succ]; ring, ih⟩

/-- An exact finite convergent witness by concatenating two physical legs. -/
theorem convergent_climb_control (m d : ℕ) (u : ℤ) (paid : 3^m*u=2^d+1) :
    literal (List.replicate m true) (2^m*u-1) (2^d) ∧
    literal (List.replicate d false) (2^d) 1 := by
  constructor
  · simpa only [paid,add_sub_cancel_right] using odd_climb m u
  · simpa only [mul_one] using even_descent d 1

/-- Comparable sources reaching one gate at the same lag force periodicity. -/
theorem packet_antichain {α : Type*} (f : α → α) (s d : ℕ) (x a : α)
    (first : f^[s] x = a) (second : f^[s] (f^[d] x) = a) : f^[d] a = a := by
  rw [← first, ← Function.iterate_add_apply, Nat.add_comm, Function.iterate_add_apply,
      second, first]

/-- Exact new binary digit flipped by each doubling of the exponent of
3^162. The odd multiplier is exhibited, not merely bounded below. -/
theorem principal_order (j : ℕ) :
    ∃ v : ℕ, (3^162 : ℕ)^(2^j)=1+2^(j+3)*(2*v+1) := by
  induction j with
  | zero => exact ⟨(3^162-9)/16, by decide +kernel⟩
  | succ j ih =>
    obtain ⟨v,hv⟩ := ih
    refine ⟨v+2^(j+1)*(2*v+1)^2,?_⟩
    rw [pow_succ 2 j,pow_mul,hv]
    simp only [pow_succ]
    ring

def physical (x : ℕ) : ℕ := if x%2=0 then x/2 else (3*x+1)/2

def path : ℕ → ℕ → ℕ
  | 0,x => x
  | n+1,x => path n (physical x)

def odds : ℕ → ℕ → ℕ
  | 0,_ => 0
  | n+1,x => x%2 + odds n (physical x)

def shiftedFactor (x : ℕ) : ℚ := if x%2=0 then (x+2:ℚ)/(x+1) else 1

def shiftedProduct : ℕ → ℕ → ℚ
  | 0,_ => 1
  | n+1,x => shiftedFactor x * shiftedProduct n (physical x)

private theorem shifted_step (x : ℕ) :
    2*((physical x:ℚ)+1)=(3:ℚ)^(x%2)*(x+1)*shiftedFactor x := by
  by_cases e : x%2=0
  · have hc : (x:ℚ)=2*(↑(x/2):ℚ) := by exact_mod_cast (show x=2*(x/2) by omega)
    have hm := div_mul_cancel₀ ((x:ℚ)+2) (show (x:ℚ)+1 ≠ 0 by positivity)
    simp [physical,shiftedFactor,e]
    linarith only [hc,hm]
  · have eo : x%2=1 := by omega
    have hc : 3*(x:ℚ)+1=2*(↑((3*x+1)/2):ℚ) := by
      exact_mod_cast (show 3*x+1=2*((3*x+1)/2) by omega)
    simp [physical,shiftedFactor,eo]
    linarith only [hc]

/-- Shift by one before recording the distortion: the correction factor now
belongs precisely to the even physical departures. -/
theorem shifted_product (h x : ℕ) :
    (2:ℚ)^h*((path h x:ℚ)+1)=(3:ℚ)^(odds h x)*(x+1)*shiftedProduct h x := by
  induction h generalizing x with
  | zero => simp [path,odds,shiftedProduct]
  | succ n ih =>
    simp only [path,odds,shiftedProduct,pow_succ,pow_add]
    calc
      _ = 2*((2:ℚ)^n*((path n (physical x):ℚ)+1)) := by ring
      _ = 2*((3:ℚ)^(odds n (physical x))*((physical x:ℚ)+1)*shiftedProduct n (physical x)) := by rw [ih]
      _ = (3:ℚ)^(odds n (physical x))*(2*((physical x:ℚ)+1))*shiftedProduct n (physical x) := by ring
      _ = _ := by rw [shifted_step]; ring

#print axioms hits_level
#print axioms slope_odd
#print axioms decode
#print axioms phase_ledger
#print axioms equal_grade_repair
#print axioms repair_contracts
#print axioms grade_drop
#print axioms odd_climb
#print axioms even_descent
#print axioms convergent_climb_control
#print axioms packet_antichain
#print axioms principal_order
#print axioms shifted_product

end Collatz.AttainedClock
