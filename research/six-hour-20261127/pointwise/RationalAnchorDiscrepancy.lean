import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Exact signed transitions for arbitrary bounded-height rational anchors.
The p-adic logarithm estimate is an external theorem in the written argument. -/
namespace RationalAnchorDiscrepancy

def defect (e : ℕ) (p q u v : ℤ) : ℤ := 2^e*q*u-v*(3*p-q)

/-- The discrepancy is a difference of the actual adjacent signed displacements. -/
theorem discrepancy_identity {e : ℕ} {x y : ℤ} (p q u v : ℤ)
    (physical : 2^e*y=3*x+1) :
    defect e p q u v=2^e*q*(v*y+u)-3*v*(q*x+p) := by
  unfold defect
  have scaled := congrArg (fun z : ℤ => q*v*z) physical
  linear_combination -scaled

/-- A common ternary precision divides the discrepancy, including the +1
in the incoming rank supplied by the odd departure. -/
theorem discrepancy_dvd {r e : ℕ} {x y p q u v : ℤ}
    (physical : 2^e*y=3*x+1)
    (start : (3:ℤ)^r∣3*(q*x+p)) (finish : (3:ℤ)^r∣v*y+u) :
    (3:ℤ)^r∣defect e p q u v := by
  obtain ⟨a,ha⟩ := start
  obtain ⟨b,hb⟩ := finish
  refine ⟨2^e*q*b-v*a,?_⟩
  rw [discrepancy_identity _ _ _ _ physical,hb]
  calc
    2^e*q*(3^r*b)-3*v*(q*x+p)=2^e*q*(3^r*b)-v*(3*(q*x+p)) := by ring
    _=_ := by rw [ha]; ring

def total (e : ℕ → ℕ) : ℕ → ℕ
  | 0 => 0
  | k+1 => total e k+e k

/-- The cross-denominator step stays integral even when individual
rational anchors have even numerators or denominators. -/
theorem exact_step {x y p q u v e : ℕ}
    (physical : 2^e*y=3*x+1) (matched : 2^e*q*u+q*v=3*p*v) :
    2^e*q*(v*y+u)=3*v*(q*x+p) := by
  have scale := congrArg (fun z : ℕ => q*v*z) physical
  calc
    2^e*q*(v*y+u) = q*v*(2^e*y)+2^e*q*u := by ring
    _=q*v*(3*x+1)+2^e*q*u := by rw [scale]
    _=3*v*(q*x)+(2^e*q*u+q*v) := by ring
    _=_ := by rw [matched]; ring

/-- Identically matching a supplied k-step ordinary word and a rational
negative word retains both endpoint denominators and their actual dyadic clock. -/
theorem run_transport (x p q e : ℕ → ℕ) (k : ℕ)
    (den : ∀ i, 0<q i)
    (physical : ∀ i<k, 2^(e i)*x (i+1)=3*x i+1)
    (matched : ∀ i<k, 2^(e i)*q i*p (i+1)+q i*q (i+1)=3*p i*q (i+1)) :
    2^(total e k)*q 0*(q k*x k+p k)=3^k*q k*(q 0*x 0+p 0) := by
  induction k with
  | zero => simp [total]
  | succ k ih =>
    have prev := ih (fun i hi => physical i (by omega)) (fun i hi => matched i (by omega))
    have step := exact_step (physical k (by omega)) (matched k (by omega))
    apply Nat.eq_of_mul_eq_mul_left (den k)
    rw [total,pow_add,pow_succ 3 k]
    calc
      q k*(2^total e k*2^e k*q 0*(q (k+1)*x (k+1)+p (k+1))) =
        2^total e k*q 0*(2^e k*q k*(q (k+1)*x (k+1)+p (k+1))) := by ring
      _=2^total e k*q 0*(3*q (k+1)*(q k*x k+p k)) := by rw [step]
      _=3*q (k+1)*(2^total e k*q 0*(q k*x k+p k)) := by ring
      _=_ := by rw [prev]; ring

private theorem count_le_total (e : ℕ → ℕ) (k : ℕ) (epos : ∀ i<k, 0<e i) :
    k≤total e k := by
  induction k with
  | zero => simp [total]
  | succ k ih =>
    have prev := ih (fun i hi => epos i (by omega))
    have today := epos k (by omega)
    rw [total]; omega

/-- A possibly even final denominator costs a single multiplicative factor.
All data are pointwise and the displacement belongs to the beginning of the run. -/
theorem dyadic_run_guard (x p q e : ℕ → ℕ) (k : ℕ)
    (den : ∀ i, 0<q i) (start : 0<q 0*x 0+p 0)
    (epos : ∀ i<k, 0<e i) (physical : ∀ i<k, 2^(e i)*x (i+1)=3*x i+1)
    (matched : ∀ i<k, 2^(e i)*q i*p (i+1)+q i*q (i+1)=3*p i*q (i+1)) :
    2^k ≤ q k*(q 0*x 0+p 0) := by
  have whole := run_transport x p q e k den physical matched
  have div : 2^(total e k)∣3^k*(q k*(q 0*x 0+p 0)) := by
    refine ⟨q 0*(q k*x k+p k),?_⟩
    simpa only [Nat.mul_assoc] using whole.symm
  have prime : Nat.Coprime (2^(total e k)) (3^k) :=
    ((show Nat.Coprime 2 3 by decide).pow_left _).pow_right _
  have endDiv := prime.dvd_of_dvd_mul_left div
  exact (Nat.pow_le_pow_right (by decide) (count_le_total e k epos)).trans
    (Nat.le_of_dvd (Nat.mul_pos (den k) start) endDiv)

/-- The odd final denominator can be removed entirely. -/
theorem dyadic_odd_guard (x p q e : ℕ → ℕ) (k : ℕ)
    (den : ∀ i, 0<q i) (odd : Nat.Coprime 2 (q k)) (start : 0<q 0*x 0+p 0)
    (epos : ∀ i<k, 0<e i) (physical : ∀ i<k, 2^(e i)*x (i+1)=3*x i+1)
    (matched : ∀ i<k, 2^(e i)*q i*p (i+1)+q i*q (i+1)=3*p i*q (i+1)) :
    2^k ≤ q 0*x 0+p 0 := by
  have whole := run_transport x p q e k den physical matched
  have div : 2^(total e k)∣(3^k*q k)*(q 0*x 0+p 0) := by
    refine ⟨q 0*(q k*x k+p k),?_⟩
    simpa only [Nat.mul_assoc] using whole.symm
  have cop : Nat.Coprime 2 (3^k*q k) :=
    (((show Nat.Coprime 2 3 by decide).pow_right k).mul_right odd)
  have endDiv := (cop.pow_left (total e k)).dvd_of_dvd_mul_left div
  exact (Nat.pow_le_pow_right (by decide) (count_le_total e k epos)).trans
    (Nat.le_of_dvd start endDiv)

/-- At a closed ordinary lap even one complete circuit of exact
rational matching would force the powers of two and three to agree. -/
theorem closed_power {x p q e : ℕ → ℕ} {k : ℕ} (den : ∀ i, 0<q i)
    (start : 0<q 0*x 0+p 0)
    (physical : ∀ i<k, 2^(e i)*x (i+1)=3*x i+1)
    (matched : ∀ i<k, 2^(e i)*q i*p (i+1)+q i*q (i+1)=3*p i*q (i+1))
    (xc : x k=x 0) (pc : p k=p 0) (qc : q k=q 0) :
    2^(total e k)=3^k := by
  have whole := run_transport x p q e k den physical matched
  rw [xc,pc,qc] at whole
  exact Nat.eq_of_mul_eq_mul_right (den 0) (Nat.eq_of_mul_eq_mul_right start whole)

/-- The physical hypothesis in the preceding theorems is exactly the
ordinary accelerated Collatz step at its full division exponent. -/
theorem ordinary_edge (x : ℕ) :
    2^((3*x+1).factorization 2)*((3*x+1)/2^((3*x+1).factorization 2))=3*x+1 :=
  Nat.ordProj_mul_ordCompl_eq_self _ _

/-- A bounded-height family must make a real signed-transition discrepancy
in this actual finite window, independent of the number of allowed rationals. -/
theorem forced_discrepancy (x p q e : ℕ → ℕ) (k H : ℕ)
    (den : ∀ i, 0<q i) (start : 0<q 0*x 0+p 0)
    (epos : ∀ i<k, 0<e i) (physical : ∀ i<k, 2^(e i)*x (i+1)=3*x i+1)
    (pcap : p 0≤H) (qcap : q 0≤H) (endcap : q k≤H)
    (large : H^2*(x 0+1)<2^k) :
    ∃ i<k, 2^(e i)*q i*p (i+1)+q i*q (i+1)≠3*p i*q (i+1) := by
  by_contra! eq
  have run := dyadic_run_guard x p q e k den start epos physical eq
  have inside : q 0*x 0+p 0≤H*x 0+H := Nat.add_le_add (Nat.mul_le_mul_right _ qcap) pcap
  have upper := Nat.mul_le_mul endcap inside
  have cap : H*(H*x 0+H)=H^2*(x 0+1) := by ring
  omega

/-- The telescoping argument also accommodates signed displacements,
including comparisons to a positive rational phase. -/
theorem signed_transport (u : ℕ → ℤ) (q e : ℕ → ℕ) (k : ℕ)
    (den : ∀ i, 0<q i)
    (pair : ∀ i<k, (2:ℤ)^(e i)*(q i:ℤ)*u (i+1)=3*(q (i+1):ℤ)*u i) :
    (2:ℤ)^(total e k)*(q 0:ℤ)*u k=3^k*(q k:ℤ)*u 0 := by
  induction k with
  | zero => simp [total]
  | succ k ih =>
    have prev := ih (fun i hi => pair i (by omega))
    have nz : (q k:ℤ)≠0 := by exact_mod_cast (den k).ne'
    apply mul_left_cancel₀ nz
    rw [total,pow_add,pow_succ 3 k]
    calc
      _=2^total e k*(q 0:ℤ)*(2^e k*(q k:ℤ)*u (k+1)) := by ring
      _=2^total e k*(q 0:ℤ)*(3*(q (k+1):ℤ)*u k) := by rw [pair k (by omega)]
      _=3*(q (k+1):ℤ)*(2^total e k*(q 0:ℤ)*u k) := by ring
      _=_ := by rw [prev]; ring

end RationalAnchorDiscrepancy

#print axioms RationalAnchorDiscrepancy.discrepancy_identity
#print axioms RationalAnchorDiscrepancy.discrepancy_dvd
#print axioms RationalAnchorDiscrepancy.exact_step
#print axioms RationalAnchorDiscrepancy.run_transport
#print axioms RationalAnchorDiscrepancy.count_le_total
#print axioms RationalAnchorDiscrepancy.dyadic_run_guard
#print axioms RationalAnchorDiscrepancy.dyadic_odd_guard
#print axioms RationalAnchorDiscrepancy.closed_power
#print axioms RationalAnchorDiscrepancy.ordinary_edge
#print axioms RationalAnchorDiscrepancy.forced_discrepancy
#print axioms RationalAnchorDiscrepancy.signed_transport
