import OffsetDescent
import SectionDynamics

/-!
# Certified descent from one marked point to another

A supplied certificate for the small offset is extended through the exact
`1,2` cycle.  The resulting high-bit orbit has an explicit endpoint.  Integer
inequalities certify both dyadic marks and a strict drop; `captures` then
places this endpoint in the actual first-return dynamics.

The arithmetic guards are hypotheses to check, not a claim that every marked
input satisfies them.  No convergence of an offset or a lifted input is
postulated as an axiom.
-/

namespace CollatzShell.MarkedOffsetReturn

open OffsetDescent ForwardSection

set_option exponentiation.threshold 2000
set_option maxRecDepth 4096

/-- A version of the mark test with a supplied, exact binary exponent. -/
theorem marked_of_bounds {x d : Nat} (odd : x%2=1)
    (lo : 2^d≤x) (hi : x<2^(d+1))
    (width : (d+1)*(x-2^d)≤70*2^d) : Marked x := by
  have xp : x≠0 := by omega
  have log : x.log2=d := (Nat.log2_eq_iff xp).mpr ⟨lo,hi⟩
  exact ⟨odd,by simpa [InSection,log] using width⟩

/-- The actual offset, rather than a real-valued approximation, certifies the
    initial marked point. -/
theorem marked_dyadic_offset {d r : Nat} (dp : 0<d) (odd : r%2=1)
    (small : r<2^d) (width : (d+1)*r≤70*2^d) : Marked (2^d+r) := by
  have even : 2^d%2=0 := by
    obtain ⟨e,rfl⟩ := Nat.exists_eq_succ_of_ne_zero dp.ne'
    rw [pow_succ]
    omega
  apply marked_of_bounds (d:=d) (by omega) (by omega)
  · rw [pow_succ]; omega
  · simpa using width

/-- Exact high-bit endpoint after the supplied offset certificate and `s`
    additional complete terminal cycles. -/
theorem padded_lift_endpoint {r t : Nat} (hit : orbit t r=1) (s e : Nat) :
    orbit (t+2*s) (2^(t+2*s+e)+r)=
      3^(oddCount t r+s)*2^e+1 := by
  obtain ⟨endpt,count⟩ := append_terminal_cycles hit s
  have lift := affine_lift (t+2*s) r (2^e)
  rw [← pow_add,endpt,count] at lift
  exact lift

/-- A coarse coefficient guard avoids constructing the gigantic factor
    `2^e` when checking the endpoint's dyadic band. -/
theorem endpoint_marked {q a e : Nat} (ep : 0<e)
    (lo : 2^a≤3^q) (hi : 3^q<2^(a+1))
    (width : (a+e+1)*(3^q-2^a+1)≤70*2^a) :
    Marked (3^q*2^e+1) := by
  have even : ∃ z, 2^e=2*z := by
    obtain ⟨b,rfl⟩ := Nat.exists_eq_succ_of_ne_zero ep.ne'
    exact ⟨2^b,by rw [pow_succ]; omega⟩
  obtain ⟨z,ez⟩ := even
  have odd : (3^q*2^e+1)%2=1 := by
    rw [ez,show 3^q*(2*z)+1=2*(3^q*z)+1 by ring]
    omega
  have ge : 2≤2^e := by
    have hp : 0<2^e := by positivity
    omega
  have lower : 2^(a+e)≤3^q*2^e+1 := by
    rw [pow_add]
    nlinarith
  have upper : 3^q*2^e+1<2^(a+e+1) := by
    have h := Nat.mul_le_mul_right (2^e) (show 3^q+1≤2^(a+1) by omega)
    have id : 2^(a+e+1)=2^(a+1)*2^e := by
      rw [← pow_add]; congr 1; omega
    rw [id]
    nlinarith
  apply marked_of_bounds odd lower upper
  have gap : 3^q=2^a+(3^q-2^a) := by omega
  have correction : 3^q*2^e+1-2^(a+e)=(3^q-2^a)*2^e+1 := by
    have id : 3^q*2^e+1=2^(a+e)+((3^q-2^a)*2^e+1) := by
      calc 3^q*2^e+1=(2^a+(3^q-2^a))*2^e+1 := by rw [← gap]
           _ = _ := by rw [pow_add]; ring
    rw [id]
    omega
  rw [correction,pow_add]
  have positive : 1≤2^e := by
    have hp : 0<2^e := by positivity
    omega
  calc
    (a+e+1)*((3^q-2^a)*2^e+1)
      ≤ (a+e+1)*((3^q-2^a+1)*2^e) := by
        apply Nat.mul_le_mul_left
        rw [Nat.add_mul]
        omega
    _ = ((a+e+1)*(3^q-2^a+1))*2^e := by ring
    _ ≤ (70*2^a)*2^e := Nat.mul_le_mul_right (2^e) width
    _ = 70*(2^a*2^e) := by ring

/-- One fixed coefficient inequality certifies every exponent in a whole
    window.  Its verification never evaluates `2^e` for the variable exponent. -/
theorem endpoint_marked_window {q a b e : Nat} (ep : 0<e) (eb : e≤b)
    (lo : 2^a≤3^q) (hi : 3^q<2^(a+1))
    (budget : (a+b+1)*(3^q-2^a+1)≤70*2^a) :
    Marked (3^q*2^e+1) := by
  apply endpoint_marked ep lo hi
  exact (Nat.mul_le_mul_right _ (by omega : a+e+1≤a+b+1)).trans budget

/-- A one-sided rational approximation to `log₂ 3` marks the ordinary integer
    `2*3^j+1`.  The small additive `+1` is retained in the logarithmic estimate.
    The scaled approximation hypothesis is convenient for exact grid proofs. -/
theorem endpoint_marked_of_phase {j a : Nat} (jp : 0<j)
    (lower : 0<(j:ℝ)*alpha-a)
    (upper : (j:ℝ)*((j:ℝ)*alpha-a)≤2) : Marked (2*3^j+1) := by
  let P : ℝ := (3:ℝ)^j
  have pp : 0<P := by dsimp [P]; positivity
  have jr : (0:ℝ)<j := by exact_mod_cast jp
  have jone : (1:ℝ)≤j := by exact_mod_cast jp
  have jP : (j:ℝ)≤P := by
    dsimp [P]
    exact_mod_cast (Nat.lt_two_pow_self (n:=j)).le.trans
      (Nat.pow_le_pow_left (by decide : 2≤3) j)
  let u : ℝ := 1/(2*P)
  have up : 0<u := by dsimp [u]; positivity
  let error : ℝ := Real.logb 2 (1+u)
  have nonneg : 0≤error := Real.logb_nonneg (by norm_num) (by linarith)
  have small : error≤1/P := by
    change Real.log (1+u)/Real.log 2≤_
    apply (div_le_iff₀ (Real.log_pos (by norm_num))).mpr
    calc Real.log (1+u) ≤ u := by
           have h := Real.log_le_sub_one_of_pos (by linarith : 0<1+u)
           linarith
         _ = (1/P)*(1/2) := by dsimp [u]; ring
         _ ≤ (1/P)*Real.log 2 :=
           mul_le_mul_of_nonneg_left log_two_bounds.1 (by positivity)
  have charged : (j:ℝ)*error≤1 := by
    calc (j:ℝ)*error ≤ P*error := mul_le_mul_of_nonneg_right jP nonneg
         _ ≤ P*(1/P) := mul_le_mul_of_nonneg_left small pp.le
         _ = 1 := by field_simp
  have one : error≤1 := by nlinarith
  have factor : ((2*3^j+1:Nat):ℝ)=2*P*(1+u) := by
    push_cast
    dsimp [P,u]
    field_simp
  have logval : height (2*3^j+1)=1+(j:ℝ)*alpha+error := by
    unfold height
    rw [factor,Real.logb_mul (by positivity : 2*P≠0) (by linarith : 1+u≠0),
      Real.logb_mul (by norm_num : (2:ℝ)≠0) pp.ne',logb_two]
    dsimp [P,error,alpha]
    rw [Real.logb_pow]
  have bound : ((2*3^j+1).log2:ℝ)+1≤2*(j:ℝ)+3 := by
    have h := Real.log2_le_logb (2*3^j+1)
    change ((2*3^j+1).log2:ℝ)≤height (2*3^j+1) at h
    rw [logval] at h
    have rot := mul_lt_mul_of_pos_left rotation_bounds.2 jr
    linarith
  let phase : ℝ := (j:ℝ)*alpha-a+error
  have positive : 0≤phase := by dsimp [phase]; linarith
  have charge : (j:ℝ)*phase≤3 := by dsimp [phase]; nlinarith
  have phaseBound : phase≤3 := by nlinarith
  have close : (((2*3^j+1).log2:ℝ)+1)*phase≤35 := by
    calc _ ≤ (2*(j:ℝ)+3)*phase := mul_le_mul_of_nonneg_right bound positive
         _ ≤ 15 := by nlinarith
         _ ≤ 35 := by norm_num
  refine ⟨by omega,section_of_phase (by positivity) (z:=(a:ℤ)+1) ?_ ?_⟩
  · rw [logval]
    push_cast
    dsimp [phase] at positive
    linarith
  · rw [logval]
    push_cast
    convert close using 1
    dsimp [phase]
    ring

/-- A finite offset witness plus integer coefficient and band guards gives an
    actual strict descent in the induced marked-return dynamics. -/
theorem marked_to_marked_descent {r t s a e : Nat}
    (hit : orbit t r=1) (odd : r%2=1) (ep : 0<e)
    (small : r<2^(t+2*s+e))
    (sourceWidth : (t+2*s+e+1)*r≤70*2^(t+2*s+e))
    (lo : 2^a≤3^(oddCount t r+s))
    (hi : 3^(oddCount t r+s)<2^(a+1))
    (targetWidth : (a+e+1)*(3^(oddCount t r+s)-2^a+1)≤70*2^a)
    (contract : 3^(oddCount t r+s)<2^(t+2*s)) :
    let n := 2^(t+2*s+e)+r
    let y := 3^(oddCount t r+s)*2^e+1
    Marked n ∧ Marked y ∧ y<n ∧
      (∃ k, 0<k ∧ returns n k=y) ∧ (Basin n ↔ Basin y) := by
  dsimp only
  let n := 2^(t+2*s+e)+r
  let y := 3^(oddCount t r+s)*2^e+1
  have initial : Marked n := marked_dyadic_offset (by omega) odd small sourceWidth
  have target : Marked y := endpoint_marked ep lo hi targetWidth
  have endpoint : orbit (t+2*s) n=y := padded_lift_endpoint hit s e
  have decrease : y<n := by
    have h := Nat.mul_lt_mul_of_pos_right contract (by positivity : 0<2^e)
    rw [← pow_add] at h
    dsimp [n,y]
    omega
  have np : 0<n := by have := initial.1; omega
  obtain ⟨k,visited⟩ := captures np (t+2*s) (endpoint ▸ target)
  have exactVisit : returns n k=y := visited.trans endpoint
  have kp : 0<k := by
    cases k with
    | zero => simp only [returns] at exactVisit; omega
    | succ k => omega
  exact ⟨initial,target,decrease,⟨k,kp,exactVisit⟩,basin_at_hit ⟨_,endpoint⟩⟩

/-- A finite coefficient certificate supplies an entire window above the
    offset one.  Its four arithmetic hypotheses depend only on `q,a,b`. -/
theorem power_plus_one_certificate_window {q a b e : Nat}
    (lo : 2^a≤3^q) (hi : 3^q<2^(a+1)) (contract : 3^q<2^(2*q))
    (budget : (a+b+1)*(3^q-2^a+1)≤70*2^a)
    (ep : 0<e) (eb : e≤b) :
    let n := 2^(2*q+e)+1
    let y := 3^q*2^e+1
    Marked n ∧ Marked y ∧ y<n ∧
      (∃ k, 0<k ∧ returns n k=y) ∧ (Basin n ↔ Basin y) := by
  have small : 1<2^(0+2*q+e) := by
    have h := Nat.lt_two_pow_self (n:=0+2*q+e)
    omega
  have source : (0+2*q+e+1)*1≤70*2^(0+2*q+e) := by
    have h := Nat.lt_two_pow_self (n:=0+2*q+e)
    omega
  have width : (a+e+1)*(3^(oddCount 0 1+q)-2^a+1)≤70*2^a := by
    simp only [oddCount,zero_add]
    exact (Nat.mul_le_mul_right _ (by omega : a+e+1≤a+b+1)).trans budget
  simpa only [oddCount,zero_add] using
      (marked_to_marked_descent (r:=1) (t:=0) (s:=q) (a:=a) (e:=e)
        rfl (by decide) ep small source (by simpa [oddCount] using lo)
        (by simpa [oddCount] using hi) width (by simpa [oddCount] using contract))

/-- The pair `(q,a)=(12,19)` supplies 5,110 distinct binary exponents at once.
    The marked endpoint occurs at 24 ordinary clocks.  Its first-return index
    is not asserted to be one. -/
theorem power_plus_one_window {e : Nat} (ep : 0<e) (eb : e≤5110) :
    let n := 2^(24+e)+1
    let y := 531441*2^e+1
    Marked n ∧ Marked y ∧ y<n ∧
      (∃ k, 0<k ∧ returns n k=y) ∧ (Basin n ↔ Basin y) := by
  simpa only [show 2*12=24 by decide,show 3^12=531441 by decide] using
    (power_plus_one_certificate_window (q:=12) (a:=19) (b:=5110)
      (by decide) (by decide) (by decide) (by decide) ep eb)

/-- A second kernel-checked coefficient pair extends the window by more than
    a million binary exponents.  This is a bounded-exponent theorem; the
    arbitrary-exponent assertion remains separate. -/
theorem power_plus_one_large_window {e : Nat} (ep : 0<e) (eb : e≤1602424) :
    let n := 2^(1330+e)+1
    let y := 3^665*2^e+1
    Marked n ∧ Marked y ∧ y<n ∧
      (∃ k, 0<k ∧ returns n k=y) ∧ (Basin n ↔ Basin y) := by
  simpa only [show 2*665=1330 by decide] using
    (power_plus_one_certificate_window (q:=665) (a:=1054) (b:=1602424)
      (by decide) (by decide) (by decide) (by decide) ep eb)

/-- Three coefficient certificates overlap.  They prove strict descent in
    the marked-return dynamics for every `2^d+1` in this exponent interval.
    This statement is not convergence of those endpoints. -/
theorem power_plus_one_overlapping_windows {d : Nat} (lo : 3≤d) (hi : d≤1603754) :
    Marked (2^d+1) ∧ ∃ k, 0<k ∧ Marked (returns (2^d+1) k) ∧
      returns (2^d+1) k<2^d+1 := by
  by_cases first : d≤70
  · have cert := power_plus_one_certificate_window (q:=1) (a:=1) (b:=68)
      (e:=d-2) (by decide) (by decide) (by decide) (by decide) (by omega) (by omega)
    have decomp : 2*1+(d-2)=d := by omega
    dsimp only at cert
    rw [decomp] at cert
    obtain ⟨mark,target,drop,⟨k,kp,visit⟩,_⟩ := cert
    refine ⟨mark,k,kp,?_,?_⟩
    · rw [visit]; exact target
    · rw [visit]; exact drop
  · by_cases second : d≤5134
    · have cert := power_plus_one_window (e:=d-24) (by omega) (by omega)
      have decomp : 24+(d-24)=d := by omega
      dsimp only at cert
      rw [decomp] at cert
      obtain ⟨mark,target,drop,⟨k,kp,visit⟩,_⟩ := cert
      refine ⟨mark,k,kp,?_,?_⟩
      · rw [visit]; exact target
      · rw [visit]; exact drop
    · have cert := power_plus_one_large_window (e:=d-1330) (by omega) (by omega)
      have decomp : 1330+(d-1330)=d := by omega
      dsimp only at cert
      rw [decomp] at cert
      obtain ⟨mark,target,drop,⟨k,kp,visit⟩,_⟩ := cert
      refine ⟨mark,k,kp,?_,?_⟩
      · rw [visit]; exact target
      · rw [visit]; exact drop

#print axioms padded_lift_endpoint
#print axioms endpoint_marked
#print axioms endpoint_marked_of_phase
#print axioms marked_to_marked_descent
#print axioms power_plus_one_window
#print axioms power_plus_one_large_window
#print axioms power_plus_one_overlapping_windows

end CollatzShell.MarkedOffsetReturn
