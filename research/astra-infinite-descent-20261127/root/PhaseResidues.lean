import PhaseNet
import Mathlib.Data.Nat.ModEq
import Mathlib.Tactic.FieldSimp

/-! A finite multiplicative net with separately prescribed exponent classes. -/
set_option autoImplicit false
set_option warningAsError true

namespace PhaseNet

theorem pow_ratio_net_residues (Q M : ℕ) (Qp : 0<Q) (Mp : 0<M)
    (ε : ℝ) (ep : 0<ε) :
    ∃ D : ℕ, ∀ r c : ℕ, r<Q → c<M → ∀ u : ℝ, 1≤u →
      ∃ d m : ℕ, d≤D ∧ d ≡ r [MOD Q] ∧ m ≡ c [MOD M] ∧
        u<(2:ℝ)^m/3^d ∧ (2:ℝ)^m/3^d<(1+ε)*u := by
  have lp : 0<Real.log 2 := Real.log_pos (by norm_num)
  have ap : 0<Real.log 3 := Real.log_pos (by norm_num)
  have Qr : (0:ℝ)<Q := by exact_mod_cast Qp
  have Mr : (0:ℝ)<M := by exact_mod_cast Mp
  have ir : Irrational (((Q:ℝ)*Real.log 3)/((M:ℝ)*Real.log 2)) := by
    have h := (irrational_logs.natCast_mul (Nat.ne_of_gt Qp)).div_natCast (Nat.ne_of_gt Mp)
    convert h using 1
    field_simp
  obtain ⟨K,net⟩ := additive_net ((Q:ℝ)*Real.log 3) ((M:ℝ)*Real.log 2)
    (Real.log (1+ε)) (mul_pos Qr ap) (mul_pos Mr lp) ir (Real.log_pos (by linarith))
  refine ⟨Q*M+Q*K,?_⟩
  intro r c hr hc u hu
  let b := r+Q*c
  have cb : c≤b := by
    have h := Nat.le_mul_of_pos_left c Qp
    dsimp [b]
    omega
  have bb : b≤Q*M := by
    have h := Nat.mul_le_mul_left Q (show c+1≤M by omega)
    dsimp [b]
    nlinarith
  have logs : Real.log 2≤Real.log 3 := Real.log_le_log (by norm_num) (by norm_num)
  have offset : (c:ℝ)*Real.log 2≤(b:ℝ)*Real.log 3 := by
    calc
      (c:ℝ)*Real.log 2 ≤ (c:ℝ)*Real.log 3 := mul_le_mul_of_nonneg_left logs (by positivity)
      _ ≤ (b:ℝ)*Real.log 3 := mul_le_mul_of_nonneg_right (by exact_mod_cast cb) ap.le
  have target : 0≤Real.log u+(b:ℝ)*Real.log 3-(c:ℝ)*Real.log 2 := by
    have h := Real.log_nonneg hu
    linarith
  obtain ⟨j,k,jK,lo,hi⟩ := net _ target
  let d := b+Q*j
  let m := c+M*k
  have dD : d≤Q*M+Q*K := by
    have h := Nat.mul_le_mul_left Q jK
    dsimp [d]
    omega
  have dr : d ≡ r [MOD Q] := by
    dsimp [d,b]
    simp [Nat.ModEq,Nat.add_mod]
  have mc : m ≡ c [MOD M] := by
    dsimp [m]
    simp [Nat.ModEq]
  have low : Real.log u<(m:ℝ)*Real.log 2-(d:ℝ)*Real.log 3 := by
    dsimp [m,d]
    push_cast
    nlinarith only [lo]
  have high : (m:ℝ)*Real.log 2-(d:ℝ)*Real.log 3<Real.log u+Real.log (1+ε) := by
    dsimp [m,d]
    push_cast
    nlinarith only [hi]
  have up : 0<u := by linarith
  have id : Real.log ((2:ℝ)^m/3^d)=(m:ℝ)*Real.log 2-(d:ℝ)*Real.log 3 := by
    rw [Real.log_div (by positivity) (by positivity),Real.log_pow,Real.log_pow]
  refine ⟨d,m,dD,dr,mc,?_,?_⟩
  · exact (Real.log_lt_log_iff up (by positivity)).mp (by simpa only [id] using low)
  · have out : Real.log ((1+ε)*u)=Real.log u+Real.log (1+ε) := by
      rw [Real.log_mul (by positivity) (ne_of_gt up)]
      ring
    exact (Real.log_lt_log_iff (by positivity) (by positivity)).mp
      (by simpa only [id,out] using high)

#print axioms pow_ratio_net_residues
end PhaseNet
