import SevenPhaseOddMap

/-! Deterministic finite-time bounds for ternary proximity along each supplied ordinary orbit. -/
namespace TernaryAnchorEscape
open ReflectedCycleMinimum SevenPhaseMinimum SevenPhaseOddMap

/-- The seven calibrated odd phases, with the full positive ternary cofactor. -/
def Hit (R X : ℕ) : Prop := ∃ t a h z, (t,a,h)∈phases ∧ 0<z ∧ X+t=2*3^R*z

private theorem phase_facts : ∀ w ∈ phases, 17≤w.1 ∧ w.1%2=1 ∧
    w.2.1≤6 ∧ 11*w.2.1≤7*w.2.2+17 := by decide

private theorem odd_iter {n : ℕ} (odd : n%2=1) (j : ℕ) :
    (accelerated^[j] n)%2=1 := by
  cases j with
  | zero => exact odd
  | succ j =>
    rw [Function.iterate_succ_apply']
    have nd : ¬2∣accelerated (accelerated^[j] n) :=
      Nat.not_dvd_ordCompl Nat.prime_two (show 3*(accelerated^[j] n)+1≠0 by omega)
    omega

/-- A divisibility test on the supplied endpoint gives the exact positive cofactor. -/
theorem hit_of_dvd {t a h R X : ℕ} (row : (t,a,h)∈phases) (xo : X%2=1)
    (dv : 3^R∣X+t) : ∃ z, 0<z ∧ X+t=2*3^R*z := by
  obtain ⟨tmin,tover,_,_⟩ := phase_facts _ row
  change 17≤t at tmin
  change t%2=1 at tover
  obtain ⟨u,hu⟩ := dv
  have powodd (i : ℕ) : 3^i%2=1 := by
    induction i with
    | zero => decide
    | succ i ih => rw [pow_succ,Nat.mul_mod,ih]
  have modEq := congrArg (fun q : ℕ => q%2) hu
  change (X+t)%2=(3^R*u)%2 at modEq
  rw [Nat.add_mod X t 2,Nat.mul_mod (3^R) u 2,tover,xo,powodd] at modEq
  have even : u%2=0 := by omega
  have upos : 0<u := by
    by_contra zero
    have uz : u=0 := by omega
    rw [uz,Nat.mul_zero] at hu
    omega
  refine ⟨u/2,by omega,?_⟩
  have eq : u=2*(u/2) := by omega
  calc
    X+t=3^R*u := hu
    _=3^R*(2*(u/2)) := congrArg (fun v => 3^R*v) eq
    _=_ := by ring

private theorem growth_one {n : ℕ} (odd : n%2=1) : 2*(accelerated n+17)≤3*(n+17) := by
  let v := (3*n+1)/2
  have split : 3*n+1=2*v := by dsimp [v]; omega
  have core : accelerated n=oddPart v := by
    unfold accelerated
    rw [split]
    simpa only [pow_one,oddPart] using Nat.ordCompl_self_pow_mul v 1 Nat.prime_two
  have upper : oddPart v≤v := Nat.ordCompl_le _ _
  rw [core]
  omega

/-- Every unmarked interval uses only the actual forward one-step height bound. -/
theorem growth {n : ℕ} (odd : n%2=1) (j : ℕ) :
    2^j*(accelerated^[j] n+17)≤3^j*(n+17) := by
  induction j with
  | zero => simp
  | succ j ih =>
    have last := growth_one (odd_iter odd j)
    rw [Function.iterate_succ_apply',pow_succ,pow_succ]
    calc
      _=2^j*(2*(accelerated (accelerated^[j] n)+17)) := by ring
      _≤2^j*(3*(accelerated^[j] n+17)) := Nat.mul_le_mul_left _ last
      _=3*(2^j*(accelerated^[j] n+17)) := by ring
      _≤3*(3^j*(n+17)) := Nat.mul_le_mul_left 3 ih
      _=_ := by ring

private theorem minimum_power {t a h R z : ℕ} (row : (t,a,h)∈phases) (hr : 7≤R) :
    let k := (R-a)/7
    2^(11*R)*z^7≤2^10*(displacement (11*k+h) (7*k+a) R z)^7 := by
  let k := (R-a)/7
  let H := 11*k+h
  let p := 7*k+a
  change 2^(11*R)*z^7≤2^10*(displacement H p R z)^7
  obtain ⟨_,_,amax,phase⟩ := phase_facts _ row
  change a≤6 at amax
  change 11*a≤7*h+17 at phase
  have rank : p≤R := by dsimp [p,k]; omega
  have gap : 11*p≤7*H+17 := by dsimp [p,H]; omega
  have surplus : (2:ℕ)^(11*(R-p))≤3^(7*(R-p)) := by
    rw [pow_mul,pow_mul]
    exact Nat.pow_le_pow_left (by decide) _
  have main : (2:ℕ)^(11*R)≤2^(7*H+17)*3^(7*(R-p)) := calc
    _=2^(11*p)*2^(11*(R-p)) := by rw [←pow_add]; congr 1; omega
    _≤_ := Nat.mul_le_mul (Nat.pow_le_pow_right (by decide) gap) surplus
  calc
    _≤(2^(7*H+17)*3^(7*(R-p)))*z^7 := Nat.mul_le_mul_right _ main
    _=_ := by
      rw [pow_add 2 (7*H) 17,Nat.mul_comm 7 H,pow_mul,
        Nat.mul_comm 7 (R-p),pow_mul]
      unfold displacement
      simp only [Nat.mul_pow]
      ring

/-- A sharp absolute constant for every supplied positive ancestor of an anchored endpoint. -/
theorem source_guard {t a h R z n X : ℕ} (row : (t,a,h)∈phases)
    (hr : 7≤R) (hz : 0<z) (odd : n%2=1) (dest : accelerated^[R] n=X)
    (anchor : X+t=2*3^R*z) :
    2^(11*R)*z^7≤2^10*(n+17)^7 := by
  have Xeq : 2*3^R*z-t=X := by omega
  have min := (exact_accelerated_minimum row hr hz).2
    (show 0<n ∧ n%2=1 ∧ ∃ j≤R, accelerated^[j] n=2*3^R*z-t from
      ⟨by omega,odd,R,le_rfl,dest.trans Xeq.symm⟩)
  have gain := minimum_power (z:=z) row hr
  dsimp only at min gain
  have upper : displacement (11*((R-a)/7)+h) (7*((R-a)/7)+a) R z≤n+17 := by omega
  exact gain.trans (Nat.mul_le_mul_left _ (Nat.pow_le_pow_left upper 7))

/-- A marked interval has a much smaller allowed growth multiplier. -/
theorem marked_growth {t a h R z n X : ℕ} (row : (t,a,h)∈phases)
    (hr : 7≤R) (hz : 0<z) (odd : n%2=1) (dest : accelerated^[R] n=X)
    (anchor : X+t=2*3^R*z) :
    2^(11*R)*(X+t)^7≤2^17*3^(7*R)*(n+17)^7 := by
  have guard := source_guard row hr hz odd dest anchor
  rw [anchor,Nat.mul_comm 7 R,pow_mul 3 R 7]
  calc
    _=(2*3^R)^7*(2^(11*R)*z^7) := by rw [Nat.mul_pow]; ring
    _≤(2*3^R)^7*(2^10*(n+17)^7) := Nat.mul_le_mul_left _ guard
    _=_ := by rw [Nat.mul_pow]; ring

private theorem iter_append (n x y : ℕ) :
    accelerated^[x+y] n = accelerated^[y] (accelerated^[x] n) := by
  rw [Nat.add_comm,Function.iterate_add_apply]

/-- For any j and R≤j, including R equal to the actual ternary valuation,
this guard retains both the original fixed source and the full cofactor. -/
theorem suffix_escape {n j t a h R z : ℕ} (odd : n%2=1) (rj : R≤j)
    (row : (t,a,h)∈phases) (hr : 7≤R) (hz : 0<z)
    (hit : accelerated^[j] n+t=2*3^R*z) :
    2^(7*j+4*R)*z^7 ≤ 2^10*3^(7*(j-R))*(n+17)^7 := by
  let b := accelerated^[j-R] n
  have ends : accelerated^[R] b=accelerated^[j] n := by
    dsimp [b]; rw [←iter_append]; congr 1; omega
  have guard := source_guard row hr hz (odd_iter odd (j-R)) ends hit
  have base := Nat.pow_le_pow_left (growth odd (j-R)) 7
  rw [Nat.mul_pow,Nat.mul_pow] at base
  have link : 7*j+4*R=7*(j-R)+11*R := by omega
  rw [link,pow_add,Nat.mul_comm 7 (j-R),pow_mul,pow_mul 3 (j-R) 7]
  calc
    _=(2^(j-R))^7*(2^(11*R)*z^7) := by ring
    _≤(2^(j-R))^7*(2^10*(b+17)^7) := Nat.mul_le_mul_left _ guard
    _=2^10*((2^(j-R))^7*(b+17)^7) := by ring
    _≤2^10*((3^(j-R))^7*(n+17)^7) := Nat.mul_le_mul_left _ base
    _=_ := by ring

/-- Arbitrarily many disjoint marked intervals, separated by arbitrary unmarked gaps. -/
inductive Packing (n : ℕ) : ℕ → ℕ → ℕ → Prop
  | empty : Packing n 0 0 0
  | gap {N L s : ℕ} (before : Packing n N L s) (g : ℕ) : Packing n (N+g) L s
  | mark {N L s R : ℕ} (before : Packing n N L s) (hr : 7≤R)
      (hit : Hit R (accelerated^[N+R] n)) : Packing n (N+R) (L+R) (s+1)

private def Bound (x y N L s : ℕ) : Prop :=
  2^(7*N+4*L)*(y+17)^7≤2^(17*s)*3^(7*N)*(x+17)^7

private theorem compose {x y z N L s M K v : ℕ}
    (fst : Bound x y N L s) (snd : Bound y z M K v) :
    Bound x z (N+M) (L+K) (s+v) := by
  unfold Bound at *
  have A : 7*(N+M)+4*(L+K)=(7*N+4*L)+(7*M+4*K) := by omega
  have B : 17*(s+v)=17*s+17*v := by omega
  have C : 7*(N+M)=7*N+7*M := by omega
  rw [A,B,C,pow_add 2 (7*N+4*L) _,pow_add 2 (17*s) _,pow_add 3 (7*N) _]
  calc
    _=2^(7*N+4*L)*(2^(7*M+4*K)*(z+17)^7) := by ring
    _≤2^(7*N+4*L)*(2^(17*v)*3^(7*M)*(y+17)^7) := Nat.mul_le_mul_left _ snd
    _=(2^(17*v)*3^(7*M))*(2^(7*N+4*L)*(y+17)^7) := by ring
    _≤(2^(17*v)*3^(7*M))*(2^(17*s)*3^(7*N)*(x+17)^7) := Nat.mul_le_mul_left _ fst
    _=_ := by ring

/-- All-source occupancy bound. Overlaps are excluded exactly by the Packing constructor. -/
theorem packing_bound {n N L s : ℕ} (odd : n%2=1) (pack : Packing n N L s) :
    2^(7*N+4*L)*(accelerated^[N] n+17)^7≤2^(17*s)*3^(7*N)*(n+17)^7 := by
  change Bound n (accelerated^[N] n) N L s
  induction pack with
  | empty => simp [Bound]
  | @gap N L s before g ih =>
    have next : Bound (accelerated^[N] n) (accelerated^[N+g] n) g 0 0 := by
      have step := Nat.pow_le_pow_left (growth (odd_iter odd N) g) 7
      rw [Nat.mul_pow,Nat.mul_pow] at step
      simpa only [Bound,Nat.mul_zero,Nat.add_zero,pow_zero,one_mul,
        Nat.mul_comm 7 g,pow_mul,iter_append] using step
    simpa only [Nat.add_zero] using compose ih next
  | @mark N L s R before hr hit ih =>
    obtain ⟨t,a,h,z,row,hz,anchor⟩ := hit
    have start : accelerated^[R] (accelerated^[N] n)=accelerated^[N+R] n :=
      (iter_append _ _ _).symm
    have step := marked_growth row hr hz (odd_iter odd N) start anchor
    have tm := (phase_facts _ row).1
    change 17≤t at tm
    have next : Bound (accelerated^[N] n) (accelerated^[N+R] n) R R 1 := by
      unfold Bound
      rw [show 7*R+4*R=11*R by omega,Nat.mul_one]
      exact (Nat.mul_le_mul_left _ (Nat.pow_le_pow_left (Nat.add_le_add_left tm _) 7)).trans step
    exact compose ih next

/-- The full-rank anchor cannot be visited once the known source-size threshold is crossed. -/
theorem exclude_full_rank {n j t a h : ℕ} (odd : n%2=1) (row : (t,a,h)∈phases)
    (hr : 7≤j) (late : 2^10*(n+17)^7<2^(11*j)) : ¬3^j∣accelerated^[j] n+t := by
  intro dv
  obtain ⟨z,hz,anchor⟩ := hit_of_dvd row (odd_iter odd j) dv
  have guard := source_guard row hr hz odd rfl anchor
  have low : 2^(11*j)≤2^(11*j)*z^7 := by
    simpa only [Nat.mul_one] using Nat.mul_le_mul_left (2^(11*j)) (show 1≤z^7 from pow_pos hz 7)
  omega

end TernaryAnchorEscape


#print axioms TernaryAnchorEscape.phase_facts
#print axioms TernaryAnchorEscape.odd_iter
#print axioms TernaryAnchorEscape.hit_of_dvd
#print axioms TernaryAnchorEscape.growth_one
#print axioms TernaryAnchorEscape.growth
#print axioms TernaryAnchorEscape.minimum_power
#print axioms TernaryAnchorEscape.source_guard
#print axioms TernaryAnchorEscape.marked_growth
#print axioms TernaryAnchorEscape.iter_append
#print axioms TernaryAnchorEscape.suffix_escape
#print axioms TernaryAnchorEscape.compose
#print axioms TernaryAnchorEscape.packing_bound
#print axioms TernaryAnchorEscape.exclude_full_rank
