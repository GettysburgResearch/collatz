import BandCertificates

/-!
Deep ordinary descent can be converted to actual descent of PR173's marked
return map. The guard uses a finite upper bound on the next marked visit,
without any assumption that smaller unmarked integers converge.

The explicit family below has an even prefix followed by an endpoint much
smaller than its binary depth. Its first positive marked return is smaller.
-/

namespace CollatzBandBridge

open CollatzShell CollatzShell.ForwardSection

private theorem orbit_upper (t n : Nat) : orbit t n ≤ 2^t*n := by
  induction t generalizing n with
  | zero => simp [orbit]
  | succ t ih =>
    have bound : step n ≤ 2*n := by unfold step; split <;> omega
    calc
      orbit (t+1) n = orbit t (step n) := rfl
      _ ≤ 2^t*step n := ih _
      _ ≤ 2^t*(2*n) := Nat.mul_le_mul_left _ bound
      _ = 2^(t+1)*n := by rw [pow_succ]; ring

def visitBudget (m : Nat) : Nat := 4*m.sqrt+m.log2

private theorem visitBudget_le (m : Nat) : visitBudget m ≤ 5*m := by
  have hs := Nat.sqrt_le_self m
  have hl := Nat.log2_le_self m
  unfold visitBudget
  omega

private theorem small_endpoint_guard {n m d : Nat} (size : 2^d ≤ n)
    (small : 6*m < d) : 2^(visitBudget m)*m < n := by
  have mp : m ≤ 2^m := (Nat.lt_two_pow_self).le
  calc
    2^(visitBudget m)*m ≤ 2^(5*m)*2^m :=
      Nat.mul_le_mul (Nat.pow_le_pow_right (by decide) (visitBudget_le m)) mp
    _ = 2^(6*m) := by rw [← pow_add]; congr 1; omega
    _ < 2^d := (Nat.pow_lt_pow_iff_right (by decide : 1<2)).mpr small
    _ ≤ n := size

/-- An actual small ordinary endpoint, followed by its bounded marked visit,
gives descent after complete marked returns. No ordinary basin floor is used. -/
theorem return_descent_of_endpoint_guard {n m t : Nat} (hn : 0<n)
    (mp : 0<m) (hit : orbit t n=m)
    (guard : 2^(visitBudget m)*m < n) :
    ∃ k, 0<k ∧ returns n k<n := by
  obtain ⟨s,hs,mark⟩ := bounded_visit m mp
  have st : s ≤ visitBudget m := by unfold visitBudget; omega
  have drop : orbit s m < n :=
    (orbit_upper s m).trans_lt
      ((Nat.mul_le_mul_right m (Nat.pow_le_pow_right (by decide) st)).trans_lt guard)
  have hit' : orbit (t+s) n=orbit s m := by rw [orbit_add,hit]
  have mark' : Marked (orbit (t+s) n) := by rw [hit']; exact mark
  obtain ⟨k,hk⟩ := captures hn (t+s) mark'
  have kd : returns n k<n := by rw [hk,hit']; exact drop
  have kp : 0<k := by
    by_cases z : k=0
    · subst k
      simp only [returns] at kd
      omega
    · omega
  exact ⟨k,kp,kd⟩

/-- A conservative integer guard avoids asymptotic square-root estimates. -/
theorem return_descent_of_small_endpoint {n m t d : Nat} (hn : 0<n)
    (mp : 0<m) (hit : orbit t n=m) (size : 2^d ≤ n)
    (small : 6*m<d) : ∃ k, 0<k ∧ returns n k<n :=
  return_descent_of_endpoint_guard hn mp hit (small_endpoint_guard size small)

/-- If the prefix before the small endpoint has no positive marked point,
the first positive return itself lies under the guarded height bound. -/
theorem first_return_descent_of_even_prefix_guard {n m t : Nat} (hn : 0<n)
    (mp : 0<m) (tp : 0<t) (hit : orbit t n=m)
    (evenPrefix : ∀ j, 0<j → j<t → (orbit j n)%2=0)
    (guard : 2^(visitBudget m)*m<n) : next n<n := by
  obtain ⟨s,hs,mark⟩ := bounded_visit m mp
  have st : s ≤ visitBudget m := by unfold visitBudget; omega
  have hit' : orbit (t+s) n=orbit s m := by rw [orbit_add,hit]
  have mark' : Marked (orbit (t+s) n) := by rw [hit']; exact mark
  have upper := returnTime_min hn (show 0<t+s by omega) mark'
  have lower : t ≤ returnTime n := by
    by_contra bad
    have rp : 0<returnTime n := by unfold returnTime; omega
    have ev := evenPrefix (returnTime n) rp (by omega)
    have od := (next_marked n hn).1
    change (orbit (returnTime n) n)%2=1 at od
    omega
  have rem : returnTime n-t ≤ visitBudget m := by omega
  have e : next n=orbit (returnTime n-t) m := by
    unfold next
    have h := orbit_add t (returnTime n-t) n
    rw [show t+(returnTime n-t)=returnTime n by omega,hit] at h
    exact h
  rw [e]
  exact (orbit_upper _ _).trans_lt
    ((Nat.mul_le_mul_right m (Nat.pow_le_pow_right (by decide) rem)).trans_lt guard)

theorem first_return_descent_of_even_prefix_small {n m t d : Nat} (hn : 0<n)
    (mp : 0<m) (tp : 0<t) (hit : orbit t n=m)
    (evenPrefix : ∀ j, 0<j → j<t → (orbit j n)%2=0)
    (size : 2^d ≤ n) (small : 6*m<d) : next n<n :=
  first_return_descent_of_even_prefix_guard hn mp tp hit evenPrefix
    (small_endpoint_guard size small)

/-- When the first odd step produces a prescribed power of two times `m`,
all the remaining prefix clocks are exact halvings. -/
theorem power_source_prefix {n m t : Nat} (odd : n%2=1) (tp : 0<t)
    (source : 3*n+1=2^t*m) :
    ∀ j, 0<j → j≤t → orbit j n=2^(t-j)*m := by
  have first : step n=2^(t-1)*m := by
    have e : 2^t*m=2*(2^(t-1)*m) := by
      have h := pow_succ (2 : Nat) (t-1)
      rw [show t-1+1=t by omega] at h
      rw [h]
      ring
    unfold step
    split
    · omega
    · rw [source,e]
      omega
  intro j jp jt
  cases j with
  | zero => omega
  | succ j =>
    simp only [orbit]
    rw [first,show t-1=j+(t-(j+1)) by omega,pow_add,Nat.mul_assoc,orbit_pad]

/- The source has one odd step followed by a long even prefix. The index
is unrestricted; all large quantities are symbolic powers. -/

def familyHalf (r : Nat) : Nat := 128*4^r-(r+1)
def familyDepth (r : Nat) : Nat := 256*4^r
def familyClock (r : Nat) : Nat := 2*familyHalf r
def familyOffset (r : Nat) : Nat := (4^(familyHalf r)-1)/3
def familyInput (r : Nat) : Nat := 2^(familyDepth r)+familyOffset r
def familyEndpoint (r : Nat) : Nat := 12*4^r+1

private theorem index_below_power (r : Nat) : r+1 ≤ 4^r := by
  have h := Nat.lt_two_pow_self (n := r)
  have p := Nat.pow_le_pow_left (by decide : 2≤4) r
  omega

theorem familyHalf_positive (r : Nat) : 0<familyHalf r := by
  have h := index_below_power r
  have p : 0<4^r := by positivity
  unfold familyHalf
  omega

theorem family_depth_split (r : Nat) :
    familyClock r+(2*r+2)=familyDepth r := by
  have h := index_below_power r
  unfold familyClock familyHalf familyDepth
  omega

theorem family_offset_identity (r : Nat) :
    3*familyOffset r+1=4^(familyHalf r) := by
  have mod : (4^(familyHalf r))%3=1 := by simp [Nat.pow_mod]
  have positive : 0<4^(familyHalf r) := by positivity
  unfold familyOffset
  omega

private theorem family_four_power (r : Nat) :
    2^(familyClock r)=4^(familyHalf r) := by
  unfold familyClock
  rw [pow_mul]
  norm_num

theorem family_high_power (r : Nat) :
    2^(familyDepth r)=4^(familyHalf r)*(4*4^r) := by
  rw [← family_depth_split, pow_add, family_four_power]
  congr 1
  rw [show 2*r+2=2*(r+1) by omega,pow_mul,pow_succ]
  norm_num
  ring

theorem family_odd (r : Nat) : (familyInput r)%2=1 := by
  have half := familyHalf_positive r
  have ae : (4^(familyHalf r))%2=0 := by
    obtain ⟨j,hj⟩ := Nat.exists_eq_succ_of_ne_zero half.ne'
    rw [hj,pow_succ]
    omega
  have eq := family_offset_identity r
  have ao : (familyOffset r)%2=1 := by omega
  have ip : (2^(familyDepth r))%2=0 := by
    rw [family_high_power]
    simp [Nat.mul_mod]
  unfold familyInput
  omega

theorem family_log2 (r : Nat) : (familyInput r).log2=familyDepth r := by
  have p : 0<4^r := by positivity
  have a := family_offset_identity r
  have op : familyOffset r<2^(familyDepth r) := by
    rw [family_high_power]
    nlinarith
  have low : 2^(familyDepth r) ≤ familyInput r := by unfold familyInput; omega
  have high : familyInput r<2^(familyDepth r+1) := by
    unfold familyInput
    rw [pow_succ]
    omega
  have ip : 0<familyInput r := by unfold familyInput; positivity
  have lo := (Nat.le_log2 ip.ne').mpr low
  have hi := (Nat.log2_lt ip.ne').mpr high
  omega

theorem family_marked (r : Nat) : Marked (familyInput r) := by
  refine ⟨family_odd r, ?_⟩
  unfold InSection
  rw [family_log2]
  have sub : familyInput r-2^(familyDepth r)=familyOffset r := by
    unfold familyInput
    omega
  rw [sub,family_high_power]
  have identity := family_offset_identity r
  have p : 1≤4^r := by exact Nat.one_le_pow _ _ (by decide)
  unfold familyDepth
  nlinarith

theorem family_power_source (r : Nat) :
    3*familyInput r+1=2^(familyClock r)*familyEndpoint r := by
  unfold familyInput familyEndpoint
  rw [family_high_power,family_four_power]
  have identity := family_offset_identity r
  nlinarith

theorem family_endpoint (r : Nat) :
    orbit (familyClock r) (familyInput r)=familyEndpoint r := by
  have tp : 0<familyClock r := by
    have h := familyHalf_positive r
    unfold familyClock
    omega
  have h := power_source_prefix (family_odd r) tp (family_power_source r)
    (familyClock r) tp (by rfl)
  simpa using h

theorem family_even_prefix (r j : Nat) (jp : 0<j) (jt : j<familyClock r) :
    (orbit j (familyInput r))%2=0 := by
  have tp : 0<familyClock r := by omega
  rw [power_source_prefix (family_odd r) tp (family_power_source r) j jp jt.le]
  have ex : 0<familyClock r-j := by omega
  obtain ⟨e,he⟩ := Nat.exists_eq_succ_of_ne_zero ex.ne'
  rw [he,pow_succ]
  simp [Nat.mul_mod]

theorem family_endpoint_small (r : Nat) :
    6*familyEndpoint r<familyDepth r := by
  have p : 0<4^r := by positivity
  unfold familyEndpoint familyDepth
  omega

/-- This closes the actual first-return descent obligation for every member
of the explicit marked family. It has no basin or ordinary-floor premise. -/
theorem family_first_return_descent (r : Nat) : next (familyInput r)<familyInput r := by
  have hn : 0<familyInput r := by unfold familyInput; positivity
  have mp : 0<familyEndpoint r := by unfold familyEndpoint; omega
  have tp : 0<familyClock r := by
    have h := familyHalf_positive r
    unfold familyClock
    omega
  have size : 2^(familyDepth r) ≤ familyInput r := by unfold familyInput; omega
  exact first_return_descent_of_even_prefix_small hn mp tp (family_endpoint r)
    (family_even_prefix r) size (family_endpoint_small r)

/-- An unbounded family of marks with a proved descending first return. -/
theorem unbounded_descending_first_returns (B : Nat) :
    ∃ n, B<n ∧ Marked n ∧ next n<n := by
  have base := index_below_power B
  have depth : B≤familyDepth B := by unfold familyDepth; omega
  have power : familyDepth B<2^(familyDepth B) := Nat.lt_two_pow_self
  have size : 2^(familyDepth B) ≤ familyInput B := by unfold familyInput; omega
  exact ⟨familyInput B, depth.trans_lt (power.trans_le size),
    family_marked B, family_first_return_descent B⟩

end CollatzBandBridge
