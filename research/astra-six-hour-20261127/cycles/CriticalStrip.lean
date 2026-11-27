import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Int.ModEq
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp

/-! Signed numerator orbits in a fixed denominator lattice. -/
namespace CriticalStrip

/-- A restricted accelerated edge has one of the two binary divisors. -/
def divisor (a : Bool) : ℤ := if a then 4 else 2

private theorem divisor_coprime (a : Bool) : IsCoprime (3 : ℤ) (divisor a) := by
  cases a
  · exact ⟨1,-1,by decide⟩
  · exact ⟨-1,1,by decide⟩

/-- Agreement of native words forces agreement at three at the terminal. -/
theorem terminal_dvd {d : ℤ} {x : ℕ → ℤ} {a : ℕ → Bool}
    (edge : ∀ n, divisor (a n)*x (n+1)=3*x n+d) (i j k : ℕ)
    (word : ∀ t<k, a (i+t)=a (j+t)) : (3:ℤ)^k ∣ x (i+k)-x (j+k) := by
  induction k with
  | zero => simp
  | succ k ih =>
    have w := word k (by omega)
    have c := (divisor_coprime (a (i+k))).pow_left (m := k+1)
    apply c.dvd_of_dvd_mul_left
    obtain ⟨z,hz⟩ := ih (fun t ht => word t (by omega))
    refine ⟨z,?_⟩
    have h₁ := edge (i+k)
    have h₂ := edge (j+k)
    rw [← w] at h₂
    rw [pow_succ]
    linear_combination h₁ - h₂ + 3*hz

private theorem grow_power (n : ℕ) : 2^n*(n+2) ≤ 2*3^n := by
  induction n with
  | zero => decide
  | succ n ih =>
    rw [pow_succ, pow_succ]
    nlinarith [Nat.zero_le ((2:ℕ)^n*n)]

private theorem eventually_injective {d : ℤ} {x : ℕ → ℤ} {a : ℕ → Bool}
    (edge : ∀ n, divisor (a n)*x (n+1)=3*x n+d) (od : ∀ n, Odd (x n))
    (escape : ∀ b : ℤ, ∃ N, ∀ n≥N, b<x n) : Function.Injective x := by
  have next : ∀ i j, x i=x j → x (i+1)=x (j+1) := by
    intro i j h
    have h₁ := edge i
    have h₂ := edge j
    rw [← h] at h₂
    obtain ⟨u,hu⟩ := od (i+1)
    obtain ⟨v,hv⟩ := od (j+1)
    cases e : a i <;> cases f : a j <;> simp [divisor,e,f] at h₁ h₂ <;> omega
  have same : ∀ i j, x i=x j → ∀ k, x (i+k)=x (j+k) := by
    intro i j h k
    induction k with
    | zero => simpa using h
    | succ k ih => exact next _ _ ih
  have norep : ∀ i k, 0<k → x i≠x (i+k) := by
    intro i k hk eq
    obtain ⟨N,hN⟩ := escape (x i)
    have laps : ∀ m, x i=x (i+k*m) := by
      intro m
      induction m with
      | zero => simp
      | succ m ih =>
        have hh := same i (i+k) eq (k*m)
        rw [Nat.mul_succ]
        convert ih.trans hh using 2
        omega
    have big : N ≤ i+k*N := by nlinarith [Nat.mul_le_mul_right N (show 1≤k by omega)]
    exact (ne_of_lt (hN _ big)) (laps N)
  intro i j eq
  rcases lt_trichotomy i j with h|h|h
  · exact False.elim (norep i (j-i) (by omega) (by simpa [Nat.add_sub_of_le h.le] using eq))
  · exact h
  · exact False.elim (norep j (i-j) (by omega) (by simpa [Nat.add_sub_of_le h.le] using eq.symm))

/-- Native words of length `L` give at most `2^L` terminal classes modulo `3^L`.
    This excludes an injective positive tail of at most linear height. -/
theorem sparse_not_linear {d : ℤ} {x : ℕ → ℤ} {a : ℕ → Bool}
    (edge : ∀ n, divisor (a n)*x (n+1)=3*x n+d) (inj : Function.Injective x)
    (S B : ℕ) (pos : ∀ n≥S, 0≤x n) (size : ∀ n, x n≤(B:ℤ)*(n+1)) : False := by
  let L := 4*B+1
  let E := S+L+1
  let N := 3^L*E
  have hE : 0<E := by dsimp [E]; omega
  have hN : 0<N := by dsimp [N]; positivity
  have range_bound (i : Fin N) : (x (S+i+L)).toNat < 3^L*(2*B*E+1) := by
    have hu := size (S+i+L)
    have hz := pos (S+i+L) (by omega)
    have hn : (i:ℕ)<3^L*E := i.isLt
    have hpe : E ≤ 3^L*E := Nat.le_mul_of_pos_left _ (by positivity)
    have ht : S+i+L+1 ≤ 2*(3^L*E) := by dsimp [E] at hn hpe ⊢; omega
    have hb := Nat.mul_le_mul_left B ht
    have hcast : (x (S+i+L)).toNat ≤ B*(S+i+L+1) := by
      apply Int.toNat_le.mpr
      push_cast
      exact hu
    nlinarith [show 0<(3:ℕ)^L by positivity]
  let enc (i : Fin N) : (Fin L → Bool) × Fin (2*B*E+1) :=
    (fun t => a (S+i+t), ⟨(x (S+i+L)).toNat / 3^L,
      (Nat.div_lt_iff_lt_mul (by positivity)).mpr (by simpa [Nat.mul_comm] using range_bound i)⟩)
  have einj : Function.Injective enc := by
    intro i j eq
    have e₁ := congrArg Prod.fst eq
    have e₂ := congrArg (fun p : (Fin L → Bool) × Fin (2*B*E+1) => p.2.val) eq
    dsimp [enc] at e₁ e₂
    have dv := terminal_dvd edge (S+i) (S+j) L (fun t ht => congrFun e₁ ⟨t,ht⟩)
    have hm := Int.modEq_iff_dvd.mpr dv
    have zi := pos (S+i+L) (by omega)
    have zj := pos (S+j+L) (by omega)
    have eme : (x (S+j+L)).toNat % 3^L = (x (S+i+L)).toNat % 3^L := by
      exact_mod_cast (show ((x (S+j+L)).toNat:ℤ) % ↑((3:ℕ)^L) = ((x (S+i+L)).toNat:ℤ) % ↑((3:ℕ)^L) by simpa [Int.toNat_of_nonneg zi, Int.toNat_of_nonneg zj, Int.ModEq] using hm)
    have ee : (x (S+i+L)).toNat=(x (S+j+L)).toNat := by
      have ii := Nat.mod_add_div (x (S+i+L)).toNat (3^L)
      have jj := Nat.mod_add_div (x (S+j+L)).toNat (3^L)
      rw [eme,← e₂] at jj
      exact ii.symm.trans jj
    have h := inj (show x (S+i+L)=x (S+j+L) by omega)
    exact Fin.ext (by omega)
  have bound := Fintype.card_le_of_injective enc einj
  simp only [Fintype.card_fin, Fintype.card_prod, Fintype.card_fun, Fintype.card_bool] at bound
  have step1 : (2*B+1)*2^L < 3^L := by
    have h := grow_power L
    dsimp [L] at h ⊢
    nlinarith [show 0<(2:ℕ)^(4*B+1) by positivity]
  have step2 : 2^L*(2*B*E+1) < N := by
    dsimp [N]
    nlinarith [Nat.mul_lt_mul_of_pos_right step1 hE, Nat.mul_le_mul_left (2^L) (show 1≤E by omega)]
  exact (not_lt_of_ge bound) step2

/-- No signed rational source on a fixed odd-denominator lattice can maintain
    both uniform coefficient bounds indefinitely on restricted odd edges. The
    displayed coefficient is the ordinary product of its edge multipliers. -/
theorem no_rational_strip {d : ℤ} (hd : 0<d) {x : ℕ → ℤ} {a : ℕ → Bool}
    (edge : ∀ n, divisor (a n)*x (n+1)=3*x n+d) (od : ∀ n, Odd (x n))
    (c : ℕ → ℚ) (initial : c 0=1)
    (clock : ∀ n, c (n+1)*(divisor (a n):ℚ)=3*c n)
    (strip : ∀ n, 1/6≤c n ∧ c n≤6) : False := by
  have hc (n : ℕ) : 0<c n := by linarith [(strip n).1]
  have inc (n : ℕ) : (x (n+1):ℚ)/c (n+1)=(x n:ℚ)/c n + (d:ℚ)/(3*c n) := by
    have he : (divisor (a n):ℚ)*(x (n+1):ℚ)=3*(x n:ℚ)+d := by exact_mod_cast edge n
    have hclock := clock n
    field_simp [ne_of_gt (hc n), ne_of_gt (hc (n+1))]
    linear_combination c (n+1)*he - (x (n+1):ℚ)*hclock
  have terms (n : ℕ) : (d:ℚ)/18≤(d:ℚ)/(3*c n) ∧ (d:ℚ)/(3*c n)≤2*d := by
    have cpos := hc n
    constructor
    · apply (le_div_iff₀ (by positivity)).mpr
      nlinarith [mul_le_mul_of_nonneg_left (strip n).2 (show (0:ℚ)≤d by exact_mod_cast hd.le)]
    · apply (div_le_iff₀ (by positivity)).mpr
      nlinarith [mul_le_mul_of_nonneg_left (strip n).1 (show (0:ℚ)≤d by exact_mod_cast hd.le)]
  have bounds (n : ℕ) :
      (x 0:ℚ)+(n:ℚ)*(d:ℚ)/18 ≤ (x n:ℚ)/c n ∧
      (x n:ℚ)/c n ≤ (x 0:ℚ)+2*(d:ℚ)*n := by
    induction n with
    | zero => simp [initial]
    | succ n ih =>
      rw [inc]
      push_cast
      constructor <;> linarith [(terms n).1, (terms n).2, ih.1, ih.2]
  have grow (b : ℤ) : ∃ N, ∀ n≥N, b<x n := by
    let N := 18*((x 0).natAbs+6*b.natAbs+1)
    refine ⟨N, fun n hn => ?_⟩
    have hN : (18:ℚ)*((x 0).natAbs+6*b.natAbs+1)≤n := by exact_mod_cast hn
    have hb : (x 0:ℚ) ≥ -((x 0).natAbs:ℚ) := by exact_mod_cast (show -((x 0).natAbs:ℤ)≤x 0 by omega)
    have h1 : (1:ℚ)≤d := by exact_mod_cast (show 1≤d by omega)
    have high : 6*(b.natAbs:ℚ)<(x n:ℚ)/c n := by
      nlinarith [(bounds n).1, mul_le_mul_of_nonneg_right h1 (Nat.cast_nonneg (α:=ℚ) n)]
    have hprod := (lt_div_iff₀ (hc n)).mp high
    have hbn : (b:ℚ)≤(b.natAbs:ℚ) := by
      have hh : (b:ℚ)≤((b.natAbs:ℤ):ℚ) := Int.cast_le.mpr (@Int.le_natAbs b)
      simpa only [Int.cast_natCast] using hh
    have hp := mul_le_mul_of_nonneg_left (strip n).1 (Nat.cast_nonneg (α:=ℚ) b.natAbs)
    exact_mod_cast (show (b:ℚ)<x n by nlinarith)
  obtain ⟨S,hS⟩ := grow 0
  let B := 6*(x 0).natAbs+12*d.natAbs
  apply sparse_not_linear edge (eventually_injective edge od grow) S B (fun n hn => (hS n hn).le)
  intro n
  have hi := (div_le_iff₀ (hc n)).mp (bounds n).2
  have x0 : (x 0:ℚ)≤((x 0).natAbs:ℚ) := by
    have hh : ((x 0):ℚ)≤(((x 0).natAbs:ℤ):ℚ) := Int.cast_le.mpr (@Int.le_natAbs (x 0))
    simpa only [Int.cast_natCast] using hh
  have dn : (d:ℚ)≤(d.natAbs:ℚ) := by
    have hh : (d:ℚ)≤((d.natAbs:ℤ):ℚ) := Int.cast_le.mpr (@Int.le_natAbs d)
    simpa only [Int.cast_natCast] using hh
  have hu : (x 0:ℚ)+2*(d:ℚ)*n ≤ ((x 0).natAbs:ℚ)+2*(d.natAbs:ℚ)*n := by
    nlinarith [mul_le_mul_of_nonneg_right dn (Nat.cast_nonneg (α:=ℚ) n)]
  have hp := mul_le_mul_of_nonneg_right hu (hc n).le
  have hq := mul_le_mul_of_nonneg_left (strip n).2 (show (0:ℚ)≤((x 0).natAbs:ℚ)+2*(d.natAbs:ℚ)*n by positivity)
  have hz : (x n:ℚ)≤(B:ℚ)*(n+1) := by
    dsimp [B]
    push_cast
    nlinarith [mul_nonneg (Nat.cast_nonneg (α:=ℚ) (x 0).natAbs) (Nat.cast_nonneg (α:=ℚ) n)]
  exact_mod_cast hz

#print axioms terminal_dvd
#print axioms sparse_not_linear
#print axioms no_rational_strip

end CriticalStrip
