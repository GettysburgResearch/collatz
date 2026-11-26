import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Basic.Real.Basic
import Mathlib.Data.Finset.Prod
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-! Exact finite bridges for quantitative spatial homogenization. All orbit
values use the ordinary shortcut function, extended at zero. -/
namespace CollatzPatchPairs

def step (n : Nat) := if n % 2 = 0 then n / 2 else (3*n+1)/2
def run : Nat → Nat → Nat
  | 0,n => n
  | k+1,n => step (run k n)
def odds : Nat → Nat → Nat
  | 0,_ => 0
  | k+1,n => odds k n + run k n % 2

private theorem intercept_bound (k n : Nat) :
    3*2^k*run k n + 3^odds k n ≤ 3^odds k n*(3*n+2^k) := by
  induction k with
  | zero => simp [run,odds]
  | succ k ih =>
    have pos : 1 ≤ 3^odds k n := Nat.one_le_pow _ _ (by decide)
    by_cases ev : run k n % 2 = 0
    · have half : 2*(run k n / 2) = run k n := by omega
      simp only [run,odds,ev,step,ite_true,Nat.add_zero,pow_succ]
      calc
        3*(2^k*2)*(run k n / 2)+3^odds k n =
          3*2^k*run k n+3^odds k n := by calc
            _ = 3*2^k*(2*(run k n / 2)) + 3^odds k n := by ring
            _ = _ := by rw [half]
        _ ≤ 3^odds k n*(3*n+2^k) := ih
        _ ≤ _ := by gcongr; omega
    · have odd : run k n % 2 = 1 := by omega
      have half : 2*((3*run k n+1)/2) = 3*run k n+1 := by omega
      simp only [run,odds,odd,step,pow_succ]
      have scaled := Nat.mul_le_mul_left 3 ih
      have extra := Nat.mul_le_mul_left (3*2^k) pos
      calc
        3*(2^k*2)*((3*run k n+1)/2)+3^odds k n*3 =
          3*2^k*(3*run k n+1)+3^odds k n*3 := by calc
            _ = 3*2^k*(2*((3*run k n+1)/2))+3^odds k n*3 := by ring
            _ = _ := by rw [half]
        _ ≤ _ := by nlinarith only [scaled,extra]

/-- In the affine lift of a binary offset h, the normalized endpoint is <4/3. -/
theorem binary_offset_normalization (k h : Nat) (hh : h < 2^k) :
    3 * run k h < 4 * 3^odds k h := by
  have main := intercept_bound k h
  have hp : 0 < 3^odds k h := by positivity
  have ht : 0 < 2^k := by positivity
  have hlt := Nat.mul_lt_mul_of_pos_left hh hp
  by_contra! bad
  have hmul := Nat.mul_le_mul_left (2^k) bad
  nlinarith only [main,hlt,hmul,hp]

private theorem one_lift (m h : Nat) :
    step (2*m+h) = 3^(h%2)*m + step h := by
  by_cases ev : h % 2 = 0
  · simp [step,ev,show (2*m+h)%2=0 by omega]; omega
  · have ho : h % 2 = 1 := by omega
    simp [step,ho]; omega

private theorem binary_lift (k h m : Nat) :
    run k (2^k*m+h) = 3^odds k h*m+run k h := by
  induction k generalizing m with
  | zero => simp [run,odds]
  | succ k ih =>
    rw [show 2^(k+1)*m+h=2^k*(2*m)+h by ring]
    simp only [run,odds,ih,pow_add]
    rw [show 3^odds k h*(2*m)+run k h=2*(3^odds k h*m)+run k h by ring,one_lift]
    ring

/-- Simultaneous control of the actual physical lift and its intercept on
one individual dyadic-ternary residue progression. -/
theorem mixed_progression_lift (k a m t h : Nat) (ht : t < 3^a) (hh : h < 2^k) :
    run k (2^k*3^a*m+(2^k*t+h)) =
      3^(a+odds k h)*m + (3^odds k h*t+run k h) ∧
    3*(3^odds k h*t+run k h) < 7*3^(a+odds k h) := by
  constructor
  · rw [show 2^k*3^a*m+(2^k*t+h)=2^k*(3^a*m+t)+h by ring,binary_lift,pow_add]
    ring
  · rw [pow_add]
    have hb := binary_offset_normalization k h hh
    have hp : 0 < 3^odds k h := by positivity
    have ha : 1 ≤ 3^a := Nat.one_le_pow _ _ (by decide)
    have h1 := Nat.mul_lt_mul_of_pos_left ht hp
    have h2 := Nat.mul_le_mul_left (3^odds k h) ha
    nlinarith only [hb,h1,h2]

/-- A color respected by every certified meeting forces all cross-color pairs
into the failed set, with both orientations counted. -/
theorem cross_pairs_le_failed {α : Type*} [DecidableEq α]
    (S : Finset α) (color : α → Bool) (meet : α → α → Prop)
    [DecidableRel meet] (same : ∀ x y, meet x y → color x = color y) :
    2 * (S.filter (fun x => color x = true)).card *
      (S.filter (fun x => color x = false)).card ≤
      ((S ×ˢ S).filter (fun p => ¬ meet p.1 p.2)).card := by
  let A := S.filter (fun x => color x = true)
  let B := S.filter (fun x => color x = false)
  have disj : Disjoint (A ×ˢ B) (B ×ˢ A) := by
    rw [Finset.disjoint_left]
    intro p hp hq
    have left := (Finset.mem_product.mp hp).1
    have right := (Finset.mem_product.mp hq).1
    simp only [A,B,Finset.mem_filter] at left right
    simp_all
  have sub : A ×ˢ B ∪ B ×ˢ A ⊆ (S ×ˢ S).filter (fun p => ¬ meet p.1 p.2) := by
    intro p hp
    simp only [Finset.mem_union,Finset.mem_product,Finset.mem_filter,A,B] at hp ⊢
    rcases hp with ⟨⟨ha,hx⟩,hb,hy⟩ | ⟨⟨ha,hx⟩,hb,hy⟩ <;>
      exact ⟨⟨ha,hb⟩, by intro hm; simpa [hx,hy] using same _ _ hm⟩
  have hcard := Finset.card_le_card sub
  rw [Finset.card_union_of_disjoint disj,Finset.card_product,Finset.card_product] at hcard
  change 2*A.card*B.card ≤ _
  nlinarith only [hcard]

open scoped BigOperators

/-- Unnormalized rotation-averaging step. Each rotated integral is close
to the unrotated one; discrepancy bounds the sum of the rotated integrals. -/
theorem rotation_average_bridge (q : Nat) (I target E D : ℝ) (u : ℕ → ℝ)
    (rotation : ∀ k ∈ Finset.range q, |I - u k| ≤ E)
    (grid : |(∑ k ∈ Finset.range q, u k) - q*target| ≤ D) :
    q * |I-target| ≤ q*E + D := by
  have first : |(q:ℝ)*I - ∑ k ∈ Finset.range q, u k| ≤ q*E := by
    calc
      _ = |∑ k ∈ Finset.range q, (I-u k)| := by simp [Finset.sum_sub_distrib]
      _ ≤ ∑ k ∈ Finset.range q, |I-u k| := Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ _k ∈ Finset.range q, E := Finset.sum_le_sum rotation
      _ = _ := by simp
  calc
    _ = |(q:ℝ)*I - q*target| := by rw [← mul_sub,abs_mul,abs_of_nonneg (Nat.cast_nonneg q : (0:ℝ) ≤ (q:ℝ))]
    _ ≤ |(q:ℝ)*I - ∑ k ∈ Finset.range q, u k| + |(∑ k ∈ Finset.range q, u k)-q*target| := abs_sub_le _ _ _
    _ ≤ _ := add_le_add first grid

#print axioms binary_offset_normalization
#print axioms mixed_progression_lift
#print axioms cross_pairs_le_failed
#print axioms rotation_average_bridge

end CollatzPatchPairs
