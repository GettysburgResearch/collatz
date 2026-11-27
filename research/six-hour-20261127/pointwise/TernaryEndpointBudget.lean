import RationalAnchorDiscrepancy

/-! The terminal ternary precision alone bounds a synchronized ordinary run.
The terminal denominator may be even. -/
namespace TernaryEndpointBudget

open RationalAnchorDiscrepancy

theorem terminal_rank (q e : ℕ → ℕ) (u : ℕ → ℤ) (k r : ℕ)
    (den : ∀ i, 0<q i) (unit : Nat.Coprime 3 (q 0))
    (start : 3^r ∣ (u 0).natAbs)
    (pair : ∀ i<k, (2:ℤ)^(e i)*(q i:ℤ)*u (i+1)=3*(q (i+1):ℤ)*u i) :
    3^(k+r) ∣ (u k).natAbs := by
  have whole := congrArg Int.natAbs (signed_transport u q e k den pair)
  simp only [Int.natAbs_mul,Int.natAbs_pow,Int.natAbs_natCast] at whole
  have eq : 2^(total e k)*q 0*(u k).natAbs=3^k*q k*(u 0).natAbs := whole
  obtain ⟨a,ha⟩ := start
  have d : 3^(k+r) ∣ (2^(total e k)*q 0)*(u k).natAbs := by
    refine ⟨q k*a,?_⟩
    rw [eq,ha,pow_add]
    ring
  have cop : Nat.Coprime 3 (2^(total e k)*q 0) :=
    ((show Nat.Coprime 3 2 by decide).pow_right _).mul_right unit
  exact (cop.pow_left (k+r)).dvd_of_dvd_mul_left d

theorem growth (x e : ℕ → ℕ) (k : ℕ) (epos : ∀ i<k, 0<e i)
    (phys : ∀ i<k, 2^(e i)*x (i+1)=3*x i+1) :
    2^k*(x k+1)≤3^k*(x 0+1) := by
  induction k with
  | zero => simp
  | succ k ih =>
    have prev := ih (fun i hi=>epos i (by omega)) (fun i hi=>phys i (by omega))
    have two : 2 ≤ 2^(e k) := by
      simpa using Nat.pow_le_pow_right (by decide : 0<2) (show 1≤e k from epos k (by omega))
    have mul := Nat.mul_le_mul_right (x (k+1)) two
    rw [phys k (by omega)] at mul
    have step : 2*(x (k+1)+1)≤3*(x k+1) := by omega
    calc
      2^(k+1)*(x (k+1)+1)=2^k*(2*(x (k+1)+1)) := by ring
      _≤2^k*(3*(x k+1)) := Nat.mul_le_mul_left _ step
      _=3*(2^k*(x k+1)) := by ring
      _≤3*(3^k*(x 0+1)) := Nat.mul_le_mul_left _ prev
      _=3^(k+1)*(x 0+1) := by ring

theorem size_guard (x q e : ℕ → ℕ) (u : ℕ → ℤ) (k r s H : ℕ)
    (den : ∀ i, 0<q i) (unit : Nat.Coprime 3 (q 0)) (start : 3^r ∣ (u 0).natAbs)
    (pair : ∀ i<k, (2:ℤ)^(e i)*(q i:ℤ)*u (i+1)=3*(q (i+1):ℤ)*u i)
    (terminal_two : 2^s ∣ (u k).natAbs) (nonzero : 0<(u k).natAbs)
    (cap : (u k).natAbs≤H*(x k+1)) (epos : ∀ i<k, 0<e i)
    (phys : ∀ i<k, 2^(e i)*x (i+1)=3*x i+1) :
    2^(k+s)*3^r ≤ H*(x 0+1) := by
  have dv := terminal_rank q e u k r den unit start pair
  have cp : Nat.Coprime (3^(k+r)) (2^s) :=
    ((show Nat.Coprime 3 2 by decide).pow_left _).pow_right _
  have low := (Nat.le_of_dvd nonzero (cp.mul_dvd_of_dvd_of_dvd dv terminal_two)).trans cap
  have hi := growth x e k epos phys
  have full : 3^k*(2^(k+s)*3^r)≤3^k*(H*(x 0+1)) := calc
    3^k*(2^(k+s)*3^r)=2^k*(3^(k+r)*2^s) := by ring
    _≤2^k*(H*(x k+1)) := Nat.mul_le_mul_left _ low
    _=H*(2^k*(x k+1)) := by ring
    _≤H*(3^k*(x 0+1)) := Nat.mul_le_mul_left H hi
    _=3^k*(H*(x 0+1)) := by ring
  exact Nat.le_of_mul_le_mul_left full (by positivity)

end TernaryEndpointBudget

#print axioms TernaryEndpointBudget.terminal_rank
#print axioms TernaryEndpointBudget.growth
#print axioms TernaryEndpointBudget.size_guard
