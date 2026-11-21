module

public import ForwardSection

@[expose] public section

/-!
# Exact transport from an offset to a high binary lift

The narrowing forward section suggests subtracting its leading power of two.
This file makes the useful transport statement public, then proves that the
section width alone does not supply the needed prefix length.  In fact a
polynomially thinner family has no descent during its entire binary horizon.
-/

namespace CollatzShell.OffsetDescent

def oddCount : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, n => oddCount k (step n) + n%2

theorem step_shift (a b : Nat) :
    step (2*a+b) = 3^(b%2)*a + step b := by
  by_cases ev : b%2=0
  · simp [step,ev,show (2*a+b)%2=0 by omega]; omega
  · have odd : b%2=1 := by omega
    simp [step,odd]; omega

/-- Exact affine transport along a shared binary prefix. -/
theorem orbit_shift (k b t : Nat) :
    orbit k (2^k*t+b)=3^(oddCount k b)*t+orbit k b := by
  induction k generalizing b t with
  | zero => simp [orbit,oddCount]
  | succ k ih =>
    rw [show 2^(k+1)*t+b=2*(2^k*t)+b by ring]
    simp only [orbit,oddCount,step_shift,pow_add]
    rw [show 3^(b%2)*(2^k*t)+step b=2^k*(3^(b%2)*t)+step b by ring,ih]
    ring

theorem binary_lift (r d t : Nat) (h : t≤d) :
    orbit t (2^d+r)=3^(oddCount t r)*2^(d-t)+orbit t r := by
  have eq : 2^d=2^t*2^(d-t) := by rw [← pow_add]; congr 1; omega
  rw [eq,orbit_shift]

/-- A contracting coefficient and a nonincreasing offset give a strict
descent of every high binary lift sharing that prefix. -/
theorem lift_descends {r d t : Nat} (h : t≤d)
    (coefficient : 3^(oddCount t r)<2^t) (offset : orbit t r≤r) :
    orbit t (2^d+r)<2^d+r := by
  rw [binary_lift r d t h]
  have strict := Nat.mul_lt_mul_of_pos_right coefficient (show 0<2^(d-t) by positivity)
  have eq : 2^t*2^(d-t)=2^d := by rw [← pow_add]; congr 1; omega
  rw [eq] at strict
  omega

/-- The lower affine bound is independent of any convergence assumption. -/
theorem coefficient_lower (r t : Nat) :
    3^(oddCount t r)*r ≤ 2^t*orbit t r := by
  induction t generalizing r with
  | zero => simp [orbit,oddCount]
  | succ t ih =>
    have one : 3^(r%2)*r≤2*step r := by
      by_cases ev : r%2=0
      · simp [step,ev]; omega
      · have odd : r%2=1 := by omega
        simp [step,odd]; omega
    have a := Nat.mul_le_mul_left (3^(oddCount t (step r))) one
    have b := Nat.mul_le_mul_left 2 (ih (step r))
    simp only [oddCount,orbit,pow_add,pow_succ]
    nlinarith

/-- A strict descent of the offset transports to every lift whose binary
horizon contains that certificate. -/
theorem offset_descent_transports {r d t : Nat} (h : t≤d)
    (offset : orbit t r<r) : orbit t (2^d+r)<2^d+r := by
  apply lift_descends h ?_ offset.le
  by_contra! bad
  have bound := coefficient_lower r t
  have a := Nat.mul_le_mul_right r bad
  have b := Nat.mul_lt_mul_of_pos_left offset (show 0<2^t by positivity)
  omega

/-- A hit of one also gives an explicit small endpoint, when the hit occurs
within the lift's binary horizon. -/
theorem offset_hit_endpoint {r d t : Nat} (h : t≤d) (hit : orbit t r=1) :
    r*(orbit t (2^d+r)-1)≤2^d := by
  have lower := coefficient_lower r t
  rw [hit,mul_one] at lower
  rw [binary_lift r d t h,hit,Nat.add_sub_cancel]
  have bound := Nat.mul_le_mul_right (2^(d-t)) lower
  have eq : 2^t*2^(d-t)=2^d := by rw [← pow_add]; congr 1; omega
  rw [eq] at bound
  simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using bound

/-- A reverse path into the offset endpoint converts the ternary difference
at the exhausted binary horizon back into a binary lift. -/
def rebase (r d u t : Nat) : Nat :=
  2^t*3^(oddCount d r-oddCount t u)+u

theorem rebase_hits {r d u t : Nat}
    (merge : orbit t u=orbit d r) (count : oddCount t u≤oddCount d r) :
    orbit t (rebase r d u t)=orbit d (2^d+r) := by
  unfold rebase
  rw [orbit_shift,binary_lift r d d le_rfl]
  simp only [Nat.sub_self,pow_zero,mul_one]
  rw [← pow_add,Nat.add_sub_of_le count,merge]

/-- Replacing the shadow's inverse history by an alternative history is a
genuine merger certificate for the original high-bit source. -/
theorem basin_of_rebase {r d u t : Nat}
    (merge : orbit t u=orbit d r) (count : oddCount t u≤oddCount d r)
    (certified : Basin (rebase r d u t)) : Basin (2^d+r) := by
  have common : Hits (rebase r d u t) (orbit d (2^d+r)) :=
    ⟨t,rebase_hits merge count⟩
  have downstream := (basin_at_hit common).mp certified
  exact (basin_at_hit (show Hits (2^d+r) (orbit d (2^d+r)) from ⟨d,rfl⟩)).mpr downstream

/-- A strictly cheaper inverse history closes an ordinary strong-induction
step. The existence of such a history is not assumed globally. -/
theorem basin_of_cheaper_rebase {r d u t : Nat}
    (merge : orbit t u=orbit d r) (count : oddCount t u≤oddCount d r)
    (cheaper : rebase r d u t<2^d+r)
    (smaller : ∀ x, 0<x → x<2^d+r → Basin x) : Basin (2^d+r) := by
  apply basin_of_rebase merge count
  apply smaller _ ?_ cheaper
  unfold rebase
  positivity

/-- Replaying the same shadow history cannot create an induction saving. -/
theorem rebase_original (r d : Nat) : rebase r d r d=2^d+r := by
  simp [rebase]

/-- Exact arithmetic form of the saving condition, with no divisions or
rounded comparisons.  It compares normalized inverse coefficients and the
two source offsets simultaneously. -/
theorem rebase_cheaper_iff {r d u t : Nat}
    (count : oddCount t u≤oddCount d r) :
    rebase r d u t<2^d+r ↔
      2^t*3^(oddCount d r)+3^(oddCount t u)*u <
        3^(oddCount t u)*(2^d+r) := by
  have eq : 3^(oddCount t u)*rebase r d u t=
      2^t*3^(oddCount d r)+3^(oddCount t u)*u := by
    unfold rebase
    rw [Nat.mul_add]
    congr 1
    rw [show 3^(oddCount t u)*(2^t*3^(oddCount d r-oddCount t u))=
      2^t*(3^(oddCount t u)*3^(oddCount d r-oddCount t u)) by ring]
    rw [← pow_add,Nat.add_sub_of_le count]
  rw [← eq]
  exact (Nat.mul_lt_mul_left (show 0<3^(oddCount t u) by positivity)).symm

/-- A smaller normalized inverse coefficient pays for the rebase whenever
its new source offset is no larger. -/
theorem rebase_cheaper_of_coefficient {r d u t : Nat}
    (count : oddCount t u≤oddCount d r) (source : u≤r)
    (coefficient : 2^t*3^(oddCount d r)<2^d*3^(oddCount t u)) :
    rebase r d u t<2^d+r := by
  rw [rebase_cheaper_iff count]
  have offsets := Nat.mul_le_mul_left (3^(oddCount t u)) source
  nlinarith

/-- A strict saving in the offset itself also suffices when the normalized
inverse coefficient does not increase. -/
theorem rebase_cheaper_of_offset {r d u t : Nat}
    (count : oddCount t u≤oddCount d r) (source : u<r)
    (coefficient : 2^t*3^(oddCount d r)≤2^d*3^(oddCount t u)) :
    rebase r d u t<2^d+r := by
  rw [rebase_cheaper_iff count]
  have offsets := Nat.mul_lt_mul_of_pos_left source (show 0<3^(oddCount t u) by positivity)
  nlinarith

/-- A mixed power of two and three leaves extra ternary divisibility at the
end of the binary prefix.  No upper bound on the residual offset is needed. -/
def reservedSource (r h s v : Nat) : Nat := 2^h*3^s*v+r

def reservedRebase (r h s v u t : Nat) : Nat :=
  2^t*3^(oddCount h r+s-oddCount t u)*v+u

theorem reservedSource_endpoint (r h s v : Nat) :
    orbit h (reservedSource r h s v)=3^(oddCount h r+s)*v+orbit h r := by
  unfold reservedSource
  rw [Nat.mul_assoc,orbit_shift,pow_add]
  ring

/-- The reserved ternary exponent permits inverse histories with more odd
steps than the original offset prefix. -/
theorem reservedRebase_hits {r h s v u t : Nat}
    (merge : orbit t u=orbit h r) (count : oddCount t u≤oddCount h r+s) :
    orbit t (reservedRebase r h s v u t)=orbit h (reservedSource r h s v) := by
  unfold reservedRebase
  rw [Nat.mul_assoc,orbit_shift,reservedSource_endpoint]
  rw [show 3^(oddCount t u)*(3^(oddCount h r+s-oddCount t u)*v)=
    (3^(oddCount t u)*3^(oddCount h r+s-oddCount t u))*v by ring]
  rw [← pow_add,Nat.add_sub_of_le count,merge]

theorem basin_of_reservedRebase {r h s v u t : Nat}
    (merge : orbit t u=orbit h r) (count : oddCount t u≤oddCount h r+s)
    (certified : Basin (reservedRebase r h s v u t)) : Basin (reservedSource r h s v) := by
  have common : Hits (reservedRebase r h s v u t) (orbit h (reservedSource r h s v)) :=
    ⟨t,reservedRebase_hits merge count⟩
  have downstream := (basin_at_hit common).mp certified
  exact (basin_at_hit (show Hits (reservedSource r h s v) (orbit h (reservedSource r h s v)) from
    ⟨h,rfl⟩)).mpr downstream

theorem reservedRebase_cheaper_iff {r h s v u t : Nat}
    (count : oddCount t u≤oddCount h r+s) :
    reservedRebase r h s v u t<reservedSource r h s v ↔
      2^t*3^(oddCount h r+s)*v+3^(oddCount t u)*u <
        3^(oddCount t u)*reservedSource r h s v := by
  have eq : 3^(oddCount t u)*reservedRebase r h s v u t=
      2^t*3^(oddCount h r+s)*v+3^(oddCount t u)*u := by
    unfold reservedRebase
    rw [Nat.mul_add]
    congr 1
    rw [show 3^(oddCount t u)*(2^t*3^(oddCount h r+s-oddCount t u)*v)=
      2^t*(3^(oddCount t u)*3^(oddCount h r+s-oddCount t u))*v by ring]
    rw [← pow_add,Nat.add_sub_of_le count]
  rw [← eq]
  exact (Nat.mul_lt_mul_left (show 0<3^(oddCount t u) by positivity)).symm

theorem basin_of_cheaper_reservedRebase {r h s v u t : Nat} (hv : 0<v)
    (merge : orbit t u=orbit h r) (count : oddCount t u≤oddCount h r+s)
    (cheaper : reservedRebase r h s v u t<reservedSource r h s v)
    (smaller : ∀ x, 0<x → x<reservedSource r h s v → Basin x) :
    Basin (reservedSource r h s v) := by
  apply basin_of_reservedRebase merge count
  apply smaller _ ?_ cheaper
  unfold reservedRebase
  positivity

theorem ordinary_rebase_is_reserved (r d u t : Nat) :
    rebase r d u t=reservedRebase r d 0 1 u t := by simp [rebase,reservedRebase]


end CollatzShell.OffsetDescent

#print axioms CollatzShell.OffsetDescent.binary_lift
#print axioms CollatzShell.OffsetDescent.offset_descent_transports
#print axioms CollatzShell.OffsetDescent.basin_of_cheaper_rebase
#print axioms CollatzShell.OffsetDescent.rebase_cheaper_iff
#print axioms CollatzShell.OffsetDescent.reservedRebase_hits
#print axioms CollatzShell.OffsetDescent.basin_of_cheaper_reservedRebase
#print axioms CollatzShell.OffsetDescent.reservedRebase_cheaper_iff
