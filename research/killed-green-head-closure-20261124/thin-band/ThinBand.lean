import Mathlib

/-! Proposed finite core and concrete cofinal-row consumer.
    No compilation or axiom audit in the authoring session. -/
namespace ThinBand

def countOdd : List Bool → ℕ
  | [] => 0
  | e :: w => (if e then 1 else 0) + countOdd w

def carry : List Bool → ℚ → ℚ
  | [], c => c
  | e :: w, c => carry w (if e then (3*c+1)/2 else c/2)

theorem carry_bound (w : List Bool) (c : ℚ) (hc : 0 ≤ c) :
    carry w c + 1 ≤ (3/2 : ℚ)^countOdd w * (c+1) := by
  induction w generalizing c with
  | nil => simp [carry, countOdd]
  | cons e w ih =>
    cases e
    · simp only [carry, countOdd, Bool.false_eq_true, if_false, zero_add]
      have hp : 0 ≤ c/2 := by linarith
      calc
        carry w (c/2)+1 ≤ (3/2 : ℚ)^countOdd w*(c/2+1) := ih _ hp
        _ ≤ (3/2 : ℚ)^countOdd w*(c+1) :=
          mul_le_mul_of_nonneg_left (by linarith) (by positivity)
    · simp only [carry, countOdd, if_true]
      have hp : 0 ≤ (3*c+1)/2 := by linarith
      calc
        carry w ((3*c+1)/2)+1 ≤
            (3/2 : ℚ)^countOdd w*((3*c+1)/2+1) := ih _ hp
        _ = (3/2 : ℚ)^(1+countOdd w)*(c+1) := by
          rw [pow_add, pow_one]
          ring

/-- One long pad cancels from the real source-window width. -/
theorem padded_width (m s : ℕ) (Z x c : ℚ)
    (hc : c+1 ≤ (3/2 : ℚ)^m)
    (he : Z-x = ((2:ℚ)^s/3^(m+1))*(3*c+1)) :
    Z-x ≤ (2:ℚ)^s/2^m := by
  have hb : 3*c+1 ≤ 3*(3/2 : ℚ)^m := by linarith
  calc
    Z-x = ((2:ℚ)^s/3^(m+1))*(3*c+1) := he
    _ ≤ ((2:ℚ)^s/3^(m+1))*(3*(3/2 : ℚ)^m) :=
      mul_le_mul_of_nonneg_left hb (by positivity)
    _ = (2:ℚ)^s/2^m := by
      rw [pow_succ, div_pow]
      field_simp
      <;> ring

theorem scaled_integer_separation (A B : ℤ) (g : ℚ)
    (hab : A ≠ B) (hg : 0 < g) :
    g ≤ |g*(A:ℚ)-g*(B:ℚ)| := by
  have hi : (1:ℚ) ≤ |(A:ℚ)-(B:ℚ)| := by
    rcases lt_or_gt_of_ne hab with h | h
    · have hc : (1:ℚ) ≤ (B:ℚ)-(A:ℚ) := by
        exact_mod_cast (show 1 ≤ B-A by omega)
      rw [abs_of_nonpos (by linarith)]
      linarith
    · have hc : (1:ℚ) ≤ (A:ℚ)-(B:ℚ) := by
        exact_mod_cast (show 1 ≤ A-B by omega)
      rw [abs_of_nonneg (by linarith)]
      exact hc
  rw [← mul_sub, abs_mul, abs_of_pos hg]
  calc
    g = g*1 := by ring
    _ ≤ g*|(A:ℚ)-(B:ℚ)| := mul_le_mul_of_nonneg_left hi hg.le

def step (n : ℕ) : ℕ := if n%2=0 then n/2 else (3*n+1)/2

def run : ℕ → ℕ → ℕ
  | 0, n => n
  | t+1, n => step (run t n)

def oddCount : ℕ → ℕ → ℕ
  | 0, _ => 0
  | t+1, n => oddCount t n + run t n % 2

def Unit (n : ℕ) : Prop := 0<n ∧ n%2=1 ∧ n%3≠0
def K (b : ℕ) : ℕ := Nat.log2 b+1
def SmallDepth (k h : ℕ) : Prop :=
  1≤h ∧ 3^(2*(h+1))≤k ∧ k<3^(2*(h+2))

def InBand (g s k x : ℕ) : Prop :=
  3^k*x < 2^s*g ∧ 2^s*g ≤ 3^k*(x+2^(8*k))

def Repeated (b x : ℕ) : Prop :=
  ∃ i j : ℕ, i<j ∧ j≤2*b ∧ run i x=run j x

def Row (b num den x q : ℕ) : Prop :=
  Unit x ∧ Unit q ∧ 1<q ∧ run (2*b) x=q ∧ oddCount (2*b) x=b ∧
  den*3^b*x ≤ (den-num)*4^b*q ∧ (K b<q ∨ Repeated b x)

def BandWitness (b num den : ℕ) : Prop :=
  ∃ k h g s q : ℕ,
    K b≤k ∧ k≤2*K b ∧ SmallDepth k h ∧ Unit g ∧ g≤K b ∧ s≤2*b ∧
    Unit q ∧ 1<q ∧
    ∀ r v : ℕ, r<2^h → r%2=1 → (v=1 ∨ v=2) →
      ∃ A : Finset ℕ, 2^(k-h-3)≤A.card ∧
        ∀ x∈A, InBand g s k x ∧ x%2^h=r ∧ x%3=v ∧ Row b num den x q

def UniversalConvergence : Prop := ∀ n : ℕ, 0<n → ∃ t, run t n=1

/-- Consumer only. The written lower amplification must still be
formalized, and the cofinal absence hypothesis is the OPEN problem. -/
theorem collatz_of_cofinal_absence
    (amplifies : ¬UniversalConvergence →
      ∃ num den : ℕ, 0<num ∧ num<den ∧
        ∃ B : ℕ, ∀ b, B≤b → BandWitness b num den)
    (absence : ∀ num den : ℕ, 0<num → num<den →
      ∀ B : ℕ, ∃ b, B≤b ∧ ¬BandWitness b num den) :
    UniversalConvergence := by
  by_contra h
  obtain ⟨num,den,hn,hd,B,hB⟩ := amplifies h
  obtain ⟨b,hb,hnoband⟩ := absence num den hn hd B
  exact hnoband (hB b hb)

end ThinBand

#print axioms ThinBand.carry_bound
#print axioms ThinBand.padded_width
#print axioms ThinBand.scaled_integer_separation
#print axioms ThinBand.collatz_of_cofinal_absence
