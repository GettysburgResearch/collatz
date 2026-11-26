import ShellCover

/-!
# Exact descent certificates for the offset above a power of two

The orbit and its normalization are those of PR173.  The affine lifting identity
is the public, counted version of `ShellCover`'s private `orbit_shift` lemma.
The new interface turns a checked finite offset prefix into an entire ordinary
arithmetic progression of strict descents, and gives its exact height threshold.
No conclusion here asserts convergence merely from a smaller endpoint.
-/

namespace CollatzShell.OffsetDescent

/-- Number of odd inputs in the first `t` shortcut steps, including an initial
    odd input and excluding the terminal value. -/
def oddCount : Nat → Nat → Nat
  | 0, _ => 0
  | t+1, r => r % 2 + oddCount t (step r)

theorem oddCount_add (a b r : Nat) :
    oddCount (a+b) r=oddCount a r+oddCount b (orbit a r) := by
  induction a generalizing r with
  | zero => simp [oddCount,orbit]
  | succ a ih => simp [Nat.succ_add,oddCount,orbit,ih,Nat.add_assoc]

theorem orbit_twice_one (s : Nat) : orbit (2*s) 1=1 := by
  induction s with
  | zero => rfl
  | succ s ih =>
    rw [show 2*(s+1)=2*s+2 by omega,orbit_add,ih]
    rfl

theorem oddCount_twice_one (s : Nat) : oddCount (2*s) 1=s := by
  induction s with
  | zero => rfl
  | succ s ih =>
    rw [show 2*(s+1)=2*s+2 by omega,oddCount_add,orbit_twice_one,ih]
    rfl

/-- Padding a supplied hit certificate with `s` copies of the actual `1→2→1`
    cycle adds exactly `2s` clocks and `s` odd inputs. -/
theorem append_terminal_cycles {h r : Nat} (hit : orbit h r=1) (s : Nat) :
    orbit (h+2*s) r=1 ∧ oddCount (h+2*s) r=oddCount h r+s := by
  constructor
  · rw [orbit_add,hit,orbit_twice_one]
  · rw [oddCount_add,hit,oddCount_twice_one]

theorem step_shift (q r : Nat) :
    step (2*q+r) = 3^(r%2)*q + step r := by
  by_cases ev : r%2=0
  · simp [step,ev,show (2*q+r)%2=0 by omega]; omega
  · have odd : r%2=1 := by omega
    simp [step,odd]; omega

/-- Exact ordinary high-bit transport.  There is no convergence assumption. -/
theorem affine_lift (t r q : Nat) :
    orbit t (2^t*q+r)=3^(oddCount t r)*q+orbit t r := by
  induction t generalizing r q with
  | zero => simp [orbit,oddCount]
  | succ t ih =>
    rw [show 2^(t+1)*q+r=2*(2^t*q)+r by ring]
    simp only [orbit,oddCount,step_shift,pow_add]
    rw [show 3^(r%2)*(2^t*q)+step r=2^t*(3^(r%2)*q)+step r by ring,ih]
    ring

theorem step_linear_lower (r : Nat) : 3^(r%2)*r ≤ 2*step r := by
  by_cases ev : r%2=0
  · simp [step,ev]; omega
  · have odd : r%2=1 := by omega
    simp [step,odd]; omega

/-- The affine correction is nonnegative, including the zero offset. -/
theorem linear_lower (t r : Nat) :
    3^(oddCount t r)*r ≤ 2^t*orbit t r := by
  induction t generalizing r with
  | zero => simp [oddCount,orbit]
  | succ t ih =>
    have h₁ := Nat.mul_le_mul_left (3^(oddCount t (step r))) (step_linear_lower r)
    have h₂ := Nat.mul_le_mul_left 2 (ih (step r))
    simp only [oddCount,pow_add,orbit]
    nlinarith

/-- Actual strict descent forces a strictly contracting affine coefficient. -/
theorem slope_lt_of_descent {t r : Nat} (drop : orbit t r<r) :
    3^(oddCount t r)<2^t := by
  have lower := linear_lower t r
  have dp : 0<2^t := by positivity
  nlinarith

/-- A descent of an offset certifies all its high-bit lifts at the same clock. -/
theorem lift_descent {t r : Nat} (drop : orbit t r<r) (q : Nat) :
    orbit t (2^t*q+r)<2^t*q+r := by
  rw [affine_lift]
  have coeff := Nat.mul_le_mul_right q (Nat.le_of_lt (slope_lt_of_descent drop))
  omega

/-- In particular, a prefix of length at most `d` certifies the actual point
    `2^d+r` above the power of two. -/
theorem dyadic_descent {t r d : Nat} (td : t≤d) (drop : orbit t r<r) :
    orbit t (2^d+r)<2^d+r := by
  have e : 2^t*2^(d-t)=2^d := by rw [← pow_add,Nat.add_sub_of_le td]
  simpa [e] using lift_descent drop (2^(d-t))

/-- Exact certificate inequality when the coefficient contracts.  It retains
    the affine correction instead of treating coefficient contraction alone as
    a stopping-time proof. -/
theorem descent_iff_guard {t r q : Nat}
    (contract : 3^(oddCount t r)<2^t) :
    orbit t (2^t*q+r)<2^t*q+r ↔
      orbit t r < r+(2^t-3^(oddCount t r))*q := by
  rw [affine_lift]
  have e : 2^t=3^(oddCount t r)+(2^t-3^(oddCount t r)) := by omega
  rw [e]
  simp only [Nat.add_mul,Nat.add_sub_cancel_left]
  omega

/-- Least safe positive quotient for a contracting prefix.  Quotient zero is
    deliberately outside this interface because it is the unlifted offset. -/
def positiveThreshold (t r : Nat) : Nat :=
  (orbit t r-r)/(2^t-3^(oddCount t r))+1

/-- The threshold is exact among positive ordinary quotients. -/
theorem descent_iff_threshold {t r q : Nat}
    (contract : 3^(oddCount t r)<2^t) (qp : 0<q) :
    orbit t (2^t*q+r)<2^t*q+r ↔ positiveThreshold t r≤q := by
  rw [descent_iff_guard contract]
  have gap : 0<2^t-3^(oddCount t r) := by omega
  have prod : 0<(2^t-3^(oddCount t r))*q := Nat.mul_pos gap qp
  have div := Nat.div_lt_iff_lt_mul (x:=orbit t r-r) (y:=q) gap
  dsimp [positiveThreshold]
  rw [Nat.mul_comm q] at div
  omega

/-- A transparent finite evaluator.  Its output is a certificate about an
    entire affine cylinder, not a heuristic parity statistic. -/
def accepts (t r q : Nat) : Bool :=
  decide (3^(oddCount t r)<2^t ∧ positiveThreshold t r≤q)

theorem accepts_sound {t r q : Nat} (qp : 0<q) (h : accepts t r q=true) :
    orbit t (2^t*q+r)<2^t*q+r := by
  have cert : 3^(oddCount t r)<2^t ∧ positiveThreshold t r≤q := by
    simpa [accepts] using h
  exact (descent_iff_threshold cert.1 qp).mpr cert.2

/-- The finite evaluator is complete at its stated positive-quotient domain. -/
theorem accepts_iff_descent {t r q : Nat} (qp : 0<q) :
    accepts t r q=true ↔ orbit t (2^t*q+r)<2^t*q+r := by
  constructor
  · exact accepts_sound qp
  · intro h
    have contract : 3^(oddCount t r)<2^t := by
      by_contra hc
      have ge : 2^t≤3^(oddCount t r) := by omega
      have prod := Nat.mul_le_mul_right q ge
      rw [affine_lift] at h
      have drop : orbit t r<r := by omega
      exact (Nat.not_lt_of_ge ge) (slope_lt_of_descent drop)
    have thresh := (descent_iff_threshold contract qp).mp h
    simpa [accepts] using And.intro contract thresh

/-- An exact finite-prefix decision at a point above a power of two. -/
theorem dyadic_accepts_iff {t r d : Nat} (td : t≤d) :
    accepts t r (2^(d-t))=true ↔ orbit t (2^d+r)<2^d+r := by
  have e : 2^t*2^(d-t)=2^d := by rw [← pow_add,Nat.add_sub_of_le td]
  simpa only [e] using accepts_iff_descent (t:=t) (r:=r) (by positivity : 0<2^(d-t))

/-- Accepting a finite quotient certifies every larger quotient. -/
theorem accepts_upper_ray {t r q : Nat} (qp : 0<q) (h : accepts t r q=true)
    {v : Nat} (qv : q≤v) : orbit t (2^t*v+r)<2^t*v+r := by
  have cert : 3^(oddCount t r)<2^t ∧ positiveThreshold t r≤q := by
    simpa [accepts] using h
  exact (descent_iff_threshold cert.1 (by omega)).mpr (cert.2.trans qv)

/-- The proof of convergence of a fixed offset, if supplied, gives an entire
    unbounded dyadic ray of strict descents.  It does not prove those lifted
    inputs converge without an induction hypothesis at their smaller values. -/
theorem eventually_dyadic_descent {r : Nat} (rp : 0<r) (known : Basin r) :
    ∃ t, 0<t ∧ ∀ d, t≤d → orbit t (2^d+r)<2^d+r := by
  by_cases one : r=1
  · subst r
    refine ⟨2,by omega,?_⟩
    intro d hd
    have cert : accepts 2 1 1=true := by decide
    have e : 2^2*2^(d-2)=2^d := by rw [← pow_add,Nat.add_sub_of_le hd]
    have pos : 0<2^(d-2) := by positivity
    have h := accepts_upper_ray (by omega : 0<1) cert (by omega : 1≤2^(d-2))
    rw [e] at h
    exact h
  · obtain ⟨t,hit⟩ := known
    have drop : orbit t r<r := by rw [hit]; omega
    have tp : 0<t := by cases t with
      | zero => simp [orbit] at drop
      | succ t => omega
    exact ⟨t,tp,fun _ hd => dyadic_descent hd drop⟩

/-- A single explicitly checked offset certificate has an infinite ordinary
    domain.  For `n=16q+3`, four shortcut steps give `9q+2<n` for every `q≥1`. -/
theorem cylinder_three_mod_sixteen (q : Nat) (qp : 0<q) :
    orbit 4 (16*q+3)=9*q+2 ∧ orbit 4 (16*q+3)<16*q+3 := by
  constructor
  · exact affine_lift 4 3 q
  · exact accepts_upper_ray (by omega : 0<1) (by decide : accepts 4 3 1=true) (by omega)

#print axioms affine_lift
#print axioms dyadic_descent
#print axioms descent_iff_threshold
#print axioms accepts_upper_ray
#print axioms eventually_dyadic_descent

end CollatzShell.OffsetDescent
