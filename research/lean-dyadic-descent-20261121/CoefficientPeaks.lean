import CoefficientCounting

/-!
# A finite escape certificate for ordinary coefficient strips

The coefficient after `t` shortcut steps is `3^(oddCount t n)/2^t`.
All statements below use exact natural-number inequalities, so no rounding or
independence assumption enters the coefficient comparisons.  The main theorem
gives an explicit finite clock at which an ordinary orbit must leave `[1,B]`.

The qualitative impossibility of a bounded supercritical coefficient sequence
already appears in the repository's coefficient-stopping and orbit-Mellin
programs.  This module supplies a finite integer proof with a displayed horizon,
using the exact parity-cylinder counting theorem in `CoefficientCounting`.
-/

namespace CollatzShell.CoefficientPeaks

open OffsetDescent CoefficientCounting

theorem orbit_next (t n : Nat) : orbit (t+1) n=step (orbit t n) := by
  rw [orbit_add]
  rfl

theorem oddCount_next (t n : Nat) :
    oddCount (t+1) n=oddCount t n+orbit t n%2 := by
  rw [oddCount_add]
  simp only [oddCount, add_zero]

theorem step_linear_exact (r : Nat) :
    2*step r=3^(r%2)*r+r%2 := by
  by_cases ev : r%2=0
  · simp [step,ev]; omega
  · have odd : r%2=1 := by omega
    simp [step,odd]; omega

/-- A supercritical prefix pays every affine correction at a cost of at most
one extra unit per clock in the normalized source. -/
theorem normalized_upper (n t : Nat) :
    (∀ i≤t, 2^i≤3^(oddCount i n)) →
    2^t*orbit t n≤3^(oddCount t n)*(n+t) := by
  induction t with
  | zero => intro _; simp [orbit,oddCount]
  | succ t ih =>
    intro lower
    have prev := ih (fun i hi => lower i (by omega))
    have coeff := lower t (by omega)
    have next := congrArg (fun z : Nat => 2^t*z) (step_linear_exact (orbit t n))
    simp only [orbit_next,oddCount_next,pow_add,pow_one]
    by_cases ev : orbit t n%2=0
    · simp only [ev,pow_zero,mul_one,add_zero] at next ⊢
      calc
        2^t*2*step (orbit t n)=2^t*orbit t n := by nlinarith only [next]
        _ ≤3^(oddCount t n)*(n+t) := prev
        _ ≤3^(oddCount t n)*(n+(t+1)) := Nat.mul_le_mul_left _ (by omega)
    · have odd : orbit t n%2=1 := by omega
      simp only [odd,pow_one] at next ⊢
      calc
        2^t*2*step (orbit t n)=3*(2^t*orbit t n)+2^t := by nlinarith only [next]
        _ ≤3*(3^(oddCount t n)*(n+t))+3^(oddCount t n) :=
          Nat.add_le_add (Nat.mul_le_mul_left 3 prev) coeff
        _ ≤3*(3^(oddCount t n)*(n+t))+3*3^(oddCount t n) := by omega
        _ =3^(oddCount t n)*3*(n+(t+1)) := by ring

/-- An upper coefficient bound pays each odd affine correction from below.
Keeping the full correction is what later excludes a repeated finite segment. -/
theorem normalized_lower (n B t : Nat) :
    (∀ i≤t, 3^(oddCount i n)≤B*2^i) →
    3^(oddCount t n)*((3*B)*n+oddCount t n)≤
      (3*B)*2^t*orbit t n := by
  induction t with
  | zero => intro _; simp [orbit,oddCount]
  | succ t ih =>
    intro upper
    have prev := ih (fun i hi => upper i (by omega))
    have coeff := upper t (by omega)
    have next := congrArg (fun z : Nat => (3*B)*2^t*z)
      (step_linear_exact (orbit t n))
    rw [orbit_next,oddCount_next,pow_add,pow_succ]
    by_cases ev : orbit t n%2=0
    · simp only [ev,pow_zero,mul_one,add_zero] at next ⊢
      nlinarith
    · have odd : orbit t n%2=1 := by omega
      simp only [odd,pow_one] at next ⊢
      nlinarith

/-- The finite coefficient strip at one specified ordinary source. -/
def CoefficientStrip (n B H : Nat) : Prop :=
  ∀ t≤H, 2^t≤3^(oddCount t n) ∧ 3^(oddCount t n)≤B*2^t

theorem strip_mono {n B H h : Nat} (strip : CoefficientStrip n B H)
    (hH : h≤H) : CoefficientStrip n B h :=
  fun t ht => strip t (ht.trans hH)

/-- Every state in a finite strip has an elementary linear size bound. -/
theorem strip_height_bound {n B H t : Nat}
    (strip : CoefficientStrip n B H) (tH : t≤H) :
    orbit t n≤B*(n+t) := by
  have up := normalized_upper n t (fun i hi => (strip i (hi.trans tH)).1)
  have coeff := Nat.mul_le_mul_right (n+t) (strip t tH).2
  have total : 2^t*orbit t n≤2^t*(B*(n+t)) := by nlinarith
  exact Nat.le_of_mul_le_mul_left total (by positivity)

theorem supercritical_clock_bound {n t : Nat}
    (lower : 2^t≤3^(oddCount t n)) : t≤2*oddCount t n := by
  have base : 3^(oddCount t n)≤4^(oddCount t n) :=
    Nat.pow_le_pow_left (by decide : 3≤4) _
  have power : 4^(oddCount t n)=2^(2*oddCount t n) := by
    rw [pow_mul]
    rfl
  rw [power] at base
  exact (Nat.pow_le_pow_iff_right (by decide : 1<2)).mp (lower.trans base)

/-- A finite supercritical strip forces linear growth measured from its clock,
without assuming that the path is injective or aperiodic. -/
theorem strip_clock_bound {n B H t : Nat}
    (strip : CoefficientStrip n B H) (tH : t≤H) :
    t≤6*B*orbit t n := by
  have lo := normalized_lower n B t (fun i hi => (strip i (hi.trans tH)).2)
  have coeff := Nat.mul_le_mul_right ((3*B)*n+oddCount t n) (strip t tH).1
  have total : 2^t*((3*B)*n+oddCount t n)≤2^t*((3*B)*orbit t n) := by
    nlinarith
  have paid : (3*B)*n+oddCount t n≤(3*B)*orbit t n :=
    Nat.le_of_mul_le_mul_left total (by positivity)
  have clock := supercritical_clock_bound (strip t tH).1
  nlinarith

/-- Determinism alone turns any repeated finite pair into a bound on every
future state.  The proof reduces the clock by the repeated period. -/
theorem orbit_bound_of_repeat {n i j X : Nat} (ij : i<j)
    (same : orbit i n=orbit j n)
    (early : ∀ t<j, orbit t n≤X) (t : Nat) : orbit t n≤X := by
  induction t using Nat.strong_induction_on with
  | h t ih =>
    by_cases tj : t<j
    · exact early t tj
    · have jt : j≤t := by omega
      have small : i+(t-j)<t := by omega
      have reduce : orbit t n=orbit (i+(t-j)) n := by
        calc
          orbit t n=orbit (j+(t-j)) n := by rw [Nat.add_sub_of_le jt]
          _ =orbit (t-j) (orbit j n) := orbit_add _ _ _
          _ =orbit (t-j) (orbit i n) := by rw [same]
          _ =orbit (i+(t-j)) n := (orbit_add _ _ _).symm
      rw [reduce]
      exact ih _ small

/-- A long enough finite strip certifies distinctness of its first `N` states.
No global no-cycle or divergent-orbit premise is used. -/
theorem strip_prefix_injective {n B N H : Nat}
    (strip : CoefficientStrip n B H) (NH : N≤H)
    (long : 6*B^2*(n+N)<H) :
    Set.InjOn (fun t => orbit t n) (↑(Finset.range N) : Set Nat) := by
  have norepeat (i j : Nat) (iN : i<N) (jN : j<N) (ij : i<j)
      (same : orbit i n=orbit j n) : False := by
    have early : ∀ t<j, orbit t n≤B*(n+N) := by
      intro t tj
      have bound := strip_height_bound strip (show t≤H by omega)
      exact bound.trans (Nat.mul_le_mul_left B (by omega))
    have bound := orbit_bound_of_repeat ij same early H
    have clock := strip_clock_bound strip (Nat.le_refl H)
    have budget := Nat.mul_le_mul_left (6*B) bound
    nlinarith
  intro i hi j hj same
  have iN : i<N := Finset.mem_range.mp hi
  have jN : j<N := Finset.mem_range.mp hj
  rcases lt_trichotomy i j with ij | ij | ji
  · exact False.elim (norepeat i j iN jN ij same)
  · exact ij
  · exact False.elim (norepeat j i jN iN ji same.symm)

/-- Every permitted shifted block inherits a coefficient lower bound. -/
theorem strip_shifted_lower {n B H j k : Nat}
    (strip : CoefficientStrip n B H) (jkH : j+k≤H) :
    2^k≤B*3^(oddCount k (orbit j n)) := by
  have lower := (strip (j+k) jkH).1
  have upper := (strip j (by omega)).2
  rw [oddCount_add,pow_add,pow_add] at lower
  have mult := Nat.mul_le_mul_right (3^(oddCount k (orbit j n))) upper
  have total : 2^j*2^k≤2^j*(B*3^(oddCount k (orbit j n))) := by nlinarith
  exact Nat.le_of_mul_le_mul_left total (by positivity)

/-- Number of distinct values required for the residue-packing contradiction. -/
def sampleCount (n B : Nat) : Nat := n+2^(blockClock B)+1

/-- A completely explicit finite observation time. -/
def escapeClock (n B : Nat) : Nat := 6*B^2*(n+sampleCount n B)+1

/-- The logarithmic block clock gives a polynomial bound in the proposed
coefficient ceiling, with a fixed explicit (deliberately coarse) constant. -/
theorem escapeClock_polynomial (n B : Nat) (Bp : 0<B) :
    escapeClock n B≤12*B^2*n+6*2^210*B^72+6*B^2+1 := by
  have logbound : 2^B.log2≤B := Nat.log2_self_le Bp.ne'
  have power := Nat.pow_le_pow_left logbound 70
  have block : 2^(blockClock B)≤2^210*B^70 := by
    calc
      2^(blockClock B)=2^210*(2^B.log2)^70 := by
        change 2^(70*(B.log2+3))=2^210*(2^B.log2)^70
        rw [← pow_mul,← pow_add]
        congr 1
        omega
      _ ≤2^210*B^70 := Nat.mul_le_mul_left _ power
  have product := Nat.mul_le_mul_left (6*B^2) block
  dsimp [escapeClock,sampleCount]
  have powers : B^2*B^70=B^72 := by rw [← pow_add]
  nlinarith

/-- No positive integer coefficient strip can contain this entire finite
ordinary orbit prefix.  Both the coefficient bounds and the observation clock
are exact natural-number expressions. -/
theorem finite_strip_impossible (n B : Nat) (Bp : 0<B) :
    ¬ CoefficientStrip n B (escapeClock n B) := by
  intro strip
  let N := sampleCount n B
  let H := escapeClock n B
  let M := 2^(blockClock B)
  have B1 : 1≤B := Bp
  have BB : 1≤B^2 := by nlinarith
  have Mp : 0<M := by dsimp [M]; positivity
  have MN : M<N := by dsimp [N,sampleCount,M]; omega
  have clock : blockClock B<M := Nat.lt_two_pow_self
  have large : 6*N≤H := by dsimp [H,escapeClock,N]; nlinarith
  have NH : N≤H := by omega
  have long : 6*B^2*(n+N)<H := by dsimp [H,escapeClock,N]; omega
  have distinct := strip_prefix_injective strip NH long
  have bounded : ∀ j<N, orbit j n≤B*(n+N) := by
    intro j jN
    have bound := strip_height_bound strip (show j≤H by omega)
    exact bound.trans (Nat.mul_le_mul_left B (by omega))
  have resistant : ∀ j<N,
      2^(blockClock B)≤B*3^(oddCount (blockClock B) (orbit j n)) := by
    intro j jN
    exact strip_shifted_lower strip (by omega)
  have packed := packing Bp (fun j => orbit j n) distinct bounded resistant
  have small : B*n+M<B*N := by
    have mprod : M≤B*M := by nlinarith
    dsimp [N,sampleCount,M] at *
    nlinarith
  change 4*B*N≤B*(n+N)+M at packed
  nlinarith

/-- Every ordinary source either obtains a contracting coefficient or exceeds
the proposed upper coefficient bound by this explicit finite clock. -/
theorem finite_coefficient_exit (n B : Nat) (Bp : 0<B) :
    ∃ t≤escapeClock n B,
      3^(oddCount t n)<2^t ∨ B*2^t<3^(oddCount t n) := by
  by_contra h
  apply finite_strip_impossible n B Bp
  intro t ht
  have noexit : ¬ (3^(oddCount t n)<2^t ∨ B*2^t<3^(oddCount t n)) := by
    intro exit
    exact h ⟨t,ht,exit⟩
  omega

/-- On any supplied all-supercritical ordinary path, arbitrarily high
coefficient peaks have an explicit finite witness bound.  This theorem does
not exclude the all-supercritical alternative. -/
theorem supercritical_peak (n B : Nat) (Bp : 0<B)
    (supercritical : ∀ t, 2^t≤3^(oddCount t n)) :
    ∃ t≤escapeClock n B, B*2^t<3^(oddCount t n) := by
  obtain ⟨t,ht,exit⟩ := finite_coefficient_exit n B Bp
  refine ⟨t,ht,?_⟩
  rcases exit with below | above
  · exact False.elim ((Nat.not_lt_of_ge (supercritical t)) below)
  · exact above

#print axioms normalized_upper
#print axioms normalized_lower
#print axioms strip_clock_bound
#print axioms strip_prefix_injective
#print axioms escapeClock_polynomial
#print axioms finite_strip_impossible
#print axioms finite_coefficient_exit
#print axioms supercritical_peak

end CollatzShell.CoefficientPeaks
