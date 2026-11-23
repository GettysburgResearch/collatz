import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Tactic.Ring

/-!
Strong divisibility for homogeneous repunits, retaining the whole
ordinary integer factors.  No coprimality of the repunits is assumed:
it is derived from coprimality of the two bases and of the indices.
-/

namespace CollatzLiterature.HomogeneousRepunits

def repunit (P Q : ℕ) : ℕ → ℕ
  | 0 => 0
  | n + 1 => P * repunit P Q n + Q ^ n

@[simp] theorem repunit_zero (P Q : ℕ) : repunit P Q 0 = 0 := rfl

theorem repunit_succ (P Q n : ℕ) :
    repunit P Q (n + 1) = P * repunit P Q n + Q ^ n := rfl

@[simp] theorem repunit_one (P Q : ℕ) : repunit P Q 1 = 1 := by
  simp [repunit]

theorem repunit_eq_sum (P Q n : ℕ) :
    repunit P Q n = ∑ j ∈ Finset.range n, P ^ j * Q ^ (n - 1 - j) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [repunit_succ, ih, Finset.sum_range_succ']
    simp only [Nat.add_sub_cancel, pow_zero, one_mul]
    congr 1
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j hj
    have he : n - (j + 1) = n - 1 - j := by omega
    rw [he, pow_succ']
    exact (Nat.mul_assoc _ _ _).symm

theorem repunit_symm (P Q n : ℕ) : repunit P Q n = repunit Q P n := by
  rw [repunit_eq_sum, repunit_eq_sum]
  exact geom_sum₂_comm P Q n

theorem repunit_add (P Q m n : ℕ) :
    repunit P Q (m + n) = P ^ m * repunit P Q n + Q ^ n * repunit P Q m := by
  induction m with
  | zero => simp
  | succ m ih =>
    rw [show m + 1 + n = (m + n) + 1 by omega, repunit_succ, ih,
      repunit_succ, pow_succ, pow_add]
    ring

theorem coprime_base_left {P Q : ℕ} (hPQ : Nat.Coprime P Q)
    {n : ℕ} (hn : 0 < n) : Nat.Coprime P (repunit P Q n) := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt hn)
  rw [repunit_succ, Nat.coprime_mul_left_add_right]
  exact hPQ.pow_right k

theorem coprime_base_product {P Q : ℕ} (hPQ : Nat.Coprime P Q)
    {n : ℕ} (hn : 0 < n) : Nat.Coprime (repunit P Q n) (P * Q) := by
  apply Nat.coprime_mul_iff_right.mpr
  refine ⟨(coprime_base_left hPQ hn).symm, ?_⟩
  rw [repunit_symm]
  exact (coprime_base_left hPQ.symm hn).symm

theorem gcd_add_right {P Q : ℕ} (hPQ : Nat.Coprime P Q) (m n : ℕ) :
    Nat.gcd (repunit P Q m) (repunit P Q (m + n)) =
      Nat.gcd (repunit P Q m) (repunit P Q n) := by
  cases m with
  | zero => simp
  | succ m =>
    rw [repunit_add P Q (m + 1) n, Nat.gcd_add_mul_right_right]
    have h := (coprime_base_left hPQ (Nat.succ_pos m)).pow_left (m + 1)
    exact h.gcd_mul_left_cancel_right (repunit P Q n)

theorem gcd_mul_add_right {P Q : ℕ} (hPQ : Nat.Coprime P Q) (m n q : ℕ) :
    Nat.gcd (repunit P Q m) (repunit P Q (m * q + n)) =
      Nat.gcd (repunit P Q m) (repunit P Q n) := by
  induction q with
  | zero => simp
  | succ q ih =>
    rw [show m * (q + 1) + n = m + (m * q + n) by rw [Nat.mul_succ]; omega,
      gcd_add_right hPQ]
    exact ih

theorem gcd_repunit {P Q : ℕ} (hPQ : Nat.Coprime P Q) (m n : ℕ) :
    Nat.gcd (repunit P Q m) (repunit P Q n) = repunit P Q (Nat.gcd m n) := by
  induction m, n using Nat.gcd.induction with
  | H0 n => simp
  | H1 m n hm ih =>
    calc
      Nat.gcd (repunit P Q m) (repunit P Q n) =
          Nat.gcd (repunit P Q m) (repunit P Q (m * (n / m) + n % m)) := by
        rw [Nat.div_add_mod]
      _ = Nat.gcd (repunit P Q m) (repunit P Q (n % m)) :=
        gcd_mul_add_right hPQ m (n % m) (n / m)
      _ = repunit P Q (Nat.gcd (n % m) m) := by
        rw [Nat.gcd_comm]
        exact ih
      _ = repunit P Q (Nat.gcd m n) := by rw [Nat.gcd_rec m n]

theorem coprime_repunit {P Q m n : ℕ} (hPQ : Nat.Coprime P Q)
    (hmn : Nat.Coprime m n) : Nat.Coprime (repunit P Q m) (repunit P Q n) := by
  rw [Nat.coprime_iff_gcd_eq_one, gcd_repunit hPQ, hmn.gcd_eq_one, repunit_one]

theorem repunit_mul_sub {P Q : ℕ} (hQP : Q ≤ P) (n : ℕ) :
    repunit P Q n * (P - Q) = P ^ n - Q ^ n := by
  rw [repunit_eq_sum]
  exact geom_sum₂_mul_of_ge hQP n

theorem repunit_eq_div {P Q : ℕ} (hQP : Q < P) (n : ℕ) :
    repunit P Q n = (P ^ n - Q ^ n) / (P - Q) := by
  rw [← repunit_mul_sub (Nat.le_of_lt hQP)]
  exact (Nat.mul_div_cancel _ (Nat.sub_pos_of_lt hQP)).symm

theorem gcd_pow_sub_pow {P Q : ℕ} (hPQ : Nat.Coprime P Q)
    (hQP : Q ≤ P) (m n : ℕ) :
    Nat.gcd (P ^ m - Q ^ m) (P ^ n - Q ^ n) =
      P ^ Nat.gcd m n - Q ^ Nat.gcd m n := by
  rw [← repunit_mul_sub hQP m, ← repunit_mul_sub hQP n,
    Nat.gcd_mul_right, gcd_repunit hPQ, repunit_mul_sub hQP]

theorem coprime_powered_repunit {X Y m n : ℕ} (hXY : Nat.Coprime X Y)
    (r : ℕ) (hmn : Nat.Coprime m n) :
    Nat.Coprime (repunit (X ^ r) (Y ^ r) m) (repunit (X ^ r) (Y ^ r) n) :=
  coprime_repunit (hXY.pow r r) hmn

theorem powered_repunit_coprime_base {X Y r n : ℕ} (hXY : Nat.Coprime X Y)
    (hr : 0 < r) (hn : 0 < n) :
    Nat.Coprime (repunit (X ^ r) (Y ^ r) n) (X * Y) := by
  have h := coprime_base_product (hXY.pow r r) hn
  rw [← Nat.mul_pow] at h
  exact (Nat.coprime_pow_right_iff hr _ _).mp h

end CollatzLiterature.HomogeneousRepunits
