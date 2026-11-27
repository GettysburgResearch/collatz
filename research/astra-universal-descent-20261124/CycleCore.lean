import Std

namespace CycleCore

/-- The endpoint form of the cycle-cut identity, with integral parameters. -/
theorem endpointDefect (U V D B u v : Int)
    (hD : U - V = D) (hF : U * v = V * u + B) :
    D * v - B = V * (u - v) := by
  subst D
  rw [Int.sub_mul, hF, Int.mul_sub]
  omega

/-- If the cut division succeeds with quotient t, the candidate at v is v−Vt. -/
theorem exactShadow (D V B u v t : Int)
    (h : D * v - B = V * (u - v)) (ht : u - v = D * t) :
    D * (v - V * t) = B := by
  rw [ht, ← Int.mul_assoc, Int.mul_comm V D, Int.mul_assoc] at h
  rw [Int.mul_sub]
  omega

/-- A positive integral fixed point with affine offset strictly below V and
    slope V/U < 2/3 must be 1. -/
theorem smallShadow (U V B y : Nat) (hs : 3 * V < 2 * U) (hb : B < V)
    (hy : 0 < y) (hfix : U * y = V * y + B) : y = 1 := by
  apply Classical.byContradiction
  intro hn
  have hy2 : 2 ≤ y := by omega
  have hUV : V ≤ U := by omega
  have hprod := Nat.mul_le_mul_left (U - V) hy2
  have hdiff : (U - V) * y = B := by
    rw [Nat.sub_mul, hfix]
    omega
  rw [hdiff] at hprod
  omega

/-- A cut with at least one exponent 1 before the exceptional exponent b
    cannot have candidate 1: its endpoint identity would identify an odd
    integer with an even one after cancelling a factor 2. -/
theorem excludeOneByParity (s t q : Nat) :
    2 * (2 * s + 1) ≠ 4 * t + 4 * q := by omega

/-- After deleting at least one leading exponent 1 the ratio drops by at
    least 2/3, expressed without division. -/
theorem dropLeadingOnes (U V U' V' : Nat) (hu : 0 < U')
    (hlt : V < U) (hr : 3 * V' * U ≤ 2 * V * U') :
    3 * V' < 2 * U' := by
  apply Classical.byContradiction
  intro hh
  have hh' : 2 * U' ≤ 3 * V' := by omega
  have h1 := Nat.mul_le_mul_right U hh'
  have h2 := Nat.mul_lt_mul_of_pos_right hlt hu
  have h3 := Nat.mul_lt_mul_of_pos_left h2 (by decide : 0 < 2)
  rw [← Nat.mul_assoc, ← Nat.mul_assoc] at h3
  have heq : 2 * U * U' = 2 * U' * U := by
    rw [Nat.mul_assoc, Nat.mul_comm U U', ← Nat.mul_assoc]
  omega

/-- Two ordered starts in one residue class are separated by at least the
    modulus. The parity-word argument supplies the quotient k. -/
theorem residueSpacing (m x y modulus k : Nat)
    (hx : m ≤ x) (hy : y < m + modulus) (hxy : x < y)
    (h : y = x + modulus * k) : False := by
  have hk : 0 < k := by
    cases k with
    | zero => simp at h; omega
    | succ k => omega
  have hgap := Nat.mul_le_mul_left modulus (show 1 ≤ k by omega)
  simp only [Nat.mul_one] at hgap
  omega

/-- A common shortcut word for scaled numerators. On the odd branch d is
    the shared denominator; the affine equations suffice for spacing. -/
inductive Shared (d : Nat) : Nat → Nat → Nat → Prop where
  | nil (x y : Nat) : Shared d 0 x y
  | even {k x y a b : Nat} (hx : x = 2*a) (hy : y = 2*b)
      (tail : Shared d k a b) : Shared d (k+1) x y
  | odd {k x y a b : Nat} (hx : 3*x+d = 2*a) (hy : 3*y+d = 2*b)
      (tail : Shared d k a b) : Shared d (k+1) x y

theorem sharedDvd {d k x y : Nat} (w : Shared d k x y) (hxy : x ≤ y) :
    2^k ∣ y-x := by
  induction w with
  | nil => simp
  | @even k x y a b hx hy tail ih =>
    obtain ⟨q,hq⟩ := ih (by omega)
    refine ⟨q, ?_⟩
    have h : y-x = (b-a)*2 := by omega
    rw [h, hq, Nat.pow_succ, Nat.mul_right_comm]
  | @odd k x y a b hx hy tail ih =>
    obtain ⟨q,hq⟩ := ih (by omega)
    have h : 3*(y-x) = (b-a)*2 := by omega
    have hd : 2^(k+1) ∣ 3*(y-x) := by
      refine ⟨q, ?_⟩
      rw [h, hq, Nat.pow_succ, Nat.mul_right_comm]
    exact ((Nat.Coprime.pow_left (k+1) (by decide : Nat.Coprime 2 3))).dvd_of_dvd_mul_left hd

/-- Finite packing comparison behind C5.1. The two alternatives are the
    rescaled backward and forward room above the numerator minimum. -/
theorem scaledWindowBound {d k x y e twoT backRoom forwardRoom : Nat}
    (w : Shared d k x y) (hxy : x < y) (he : e ≤ x)
    (hw : twoT * (y-e) ≤ max backRoom forwardRoom) :
    twoT * 2^k ≤ max backRoom forwardRoom := by
  obtain ⟨q,hq⟩ := sharedDvd w (by omega)
  have hqpos : 1 ≤ q := by
    cases q with
    | zero => simp at hq; omega
    | succ q => omega
  have hgap := Nat.mul_le_mul_left (2^k) hqpos
  simp only [Nat.mul_one] at hgap
  exact Nat.le_trans (Nat.mul_le_mul_left twoT (by omega : 2^k ≤ y-e)) hw

end CycleCore
