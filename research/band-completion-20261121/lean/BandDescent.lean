module

public import SectionDynamics

@[expose] public section

/-!
# Exact transport of offset certificates

All statements concern the ordinary shortcut map from `ShellCover`.  The
transport theorem is valid only through the displayed binary depth.  The
family below shows that even an exponentially narrow leading interval does
not guarantee a stopping certificate within that depth.
-/

namespace CollatzShell.BandDescent

/-- Number of odd inputs among the first `k` ordinary shortcut steps. -/
def oddCount : Nat → Nat → Nat
  | 0, _ => 0
  | k+1, n => oddCount k (step n) + n % 2

private theorem step_shift (a b : Nat) :
    step (2*a+b) = 3^(b%2)*a + step b := by
  by_cases ev : b%2=0
  · simp [step,ev,show (2*a+b)%2=0 by omega]; omega
  · have odd : b%2=1 := by omega
    simp [step,odd]; omega

/-- Exact ordinary transport for every dyadic translate, not only a residue
    representative or a positive-probability collection of inputs. -/
theorem prefix_lift (k u h : Nat) :
    orbit k (2^k*h+u) = 3^(oddCount k u)*h+orbit k u := by
  induction k generalizing u h with
  | zero => simp [orbit,oddCount]
  | succ k ih =>
    rw [show 2^(k+1)*h+u=2*(2^k*h)+u by ring]
    simp only [orbit,oddCount,step_shift,pow_add]
    rw [show 3^(u%2)*(2^k*h)+step u=2^k*(3^(u%2)*h)+step u by ring,ih]
    ring

/-- The positive affine remainder cannot lower an orbit below its linear
    coefficient. -/
theorem coefficient_lower (k u : Nat) :
    3^(oddCount k u)*u ≤ 2^k*orbit k u := by
  induction k generalizing u with
  | zero => simp [oddCount,orbit]
  | succ k ih =>
    have one : 3^(u%2)*u ≤ 2*step u := by
      by_cases ev : u%2=0
      · simp [ev,step]; omega
      · have odd : u%2=1 := by omega
        simp [odd,step]; omega
    calc
      3^(oddCount (k+1) u)*u
          = 3^(oddCount k (step u))*(3^(u%2)*u) := by
              simp only [oddCount,pow_add]; ring
      _ ≤ 3^(oddCount k (step u))*(2*step u) := Nat.mul_le_mul_left _ one
      _ = 2*(3^(oddCount k (step u))*step u) := by ring
      _ ≤ 2*(2^k*orbit k (step u)) := Nat.mul_le_mul_left _ (ih (step u))
      _ = 2^(k+1)*orbit (k+1) u := by simp only [orbit,pow_succ]; ring

theorem descent_coefficient {k u : Nat} (drop : orbit k u<u) :
    3^(oddCount k u)<2^k := by
  have pos : 0<u := by omega
  by_contra! no
  have a := Nat.mul_le_mul_right u no
  have b := coefficient_lower k u
  have c := Nat.mul_lt_mul_of_pos_left drop (by positivity : 0<2^k)
  omega

/-- Any finite descent certificate lifts to every nonnegative dyadic
    translate that has the same certified parity prefix. -/
theorem descent_lift {k u : Nat} (drop : orbit k u<u) (h : Nat) :
    orbit k (2^k*h+u)<2^k*h+u := by
  rw [prefix_lift]
  have coeff := Nat.mul_le_mul_right h (descent_coefficient drop).le
  omega

/-- A non-strict endpoint certificate also lifts, provided its coefficient
    is strictly contracting and the upper dyadic block is nonzero.  This
    includes the two-clock certificate of the offset one. -/
theorem nonincrease_lift {k u h : Nat} (endpt : orbit k u≤u)
    (coeff : 3^(oddCount k u)<2^k) (hp : 0<h) :
    orbit k (2^k*h+u)<2^k*h+u := by
  rw [prefix_lift]
  have strict := Nat.mul_lt_mul_of_pos_right coeff hp
  omega

/-- Exactly `d` low bits are available for borrowing a certificate from the
    offset in `2^d+u`. -/
theorem offset_lift {d k : Nat} (u : Nat) (clock : k≤d) :
    orbit k (2^d+u) = 3^(oddCount k u)*2^(d-k)+orbit k u := by
  have split : 2^d=2^k*2^(d-k) := by
    rw [← pow_add, Nat.add_sub_of_le clock]
  rw [split,prefix_lift]

/-- At the first exhausted bit, the two ordinary orbits necessarily have
    opposite parities.  The shared-prefix certificate cannot simply be
    continued for one more step. -/
theorem offset_boundary_parity (d u : Nat) :
    orbit d (2^d+u)%2 ≠ orbit d u%2 := by
  have odd : 3^(oddCount d u)%2=1 := by simp [Nat.pow_mod]
  rw [offset_lift u le_rfl]
  simp only [Nat.sub_self,pow_zero,Nat.mul_one]
  omega

theorem offset_descent {d k u : Nat} (clock : k≤d)
    (drop : orbit k u<u) : orbit k (2^d+u)<2^d+u := by
  have split : 2^d=2^k*2^(d-k) := by
    rw [← pow_add, Nat.add_sub_of_le clock]
  rw [split]
  exact descent_lift drop _

/-- A convergent offset larger than one eventually supplies a uniform
    certificate for every sufficiently high dyadic translate.  The threshold
    depends on the actual convergence clock, not just on offset size. -/
theorem convergent_offset_eventually_lifts {u : Nat} (up : 1<u) (basin : Basin u) :
    ∃ k, ∀ d≥k, orbit k (2^d+u)<2^d+u := by
  obtain ⟨k,hk⟩ := basin
  exact ⟨k,fun _ clock => offset_descent clock (by simpa [hk] using up)⟩

private theorem orbit_upper (j n : Nat) : orbit j n≤2^j*n := by
  induction j generalizing n with
  | zero => simp [orbit]
  | succ j ih =>
    have one : step n≤2*n := by unfold step; split <;> omega
    calc
      orbit (j+1) n = orbit j (step n) := rfl
      _ ≤ 2^j*step n := ih _
      _ ≤ 2^j*(2*n) := Nat.mul_le_mul_left _ one
      _ = 2^(j+1)*n := by rw [pow_succ]; ring

/-- A sufficiently small ordinary endpoint produces a *lower marked
    endpoint*.  This retains the distinction between ordinary descent and
    descent of the induced section dynamics. -/
theorem return_descent_of_small_hit {x d k y : Nat} (base : 2^d≤x)
    (yp : 0<y) (hit : orbit k x=y) (room : 4*y.sqrt+2*y.log2≤d) :
    ∃ j, ForwardSection.returns x j<x := by
  obtain ⟨t,clock,mark⟩ := ForwardSection.bounded_visit y yp
  have bound : orbit t y<2^d := calc
    orbit t y ≤ 2^t*y := orbit_upper _ _
    _ < 2^t*2^(y.log2+1) := Nat.mul_lt_mul_of_pos_left Nat.lt_log2_self (by positivity)
    _ = 2^(t+y.log2+1) := by rw [← pow_add,Nat.add_assoc]
    _ ≤ 2^d := Nat.pow_le_pow_right (by decide) (by omega)
  have xp : 0<x := (by positivity : 0<2^d).trans_le base
  have m : ForwardSection.Marked (orbit (k+t) x) := by rw [orbit_add,hit]; exact mark
  obtain ⟨j,hj⟩ := ForwardSection.captures xp (k+t) m
  refine ⟨j,?_⟩
  rw [hj,orbit_add,hit]
  exact bound.trans_le base

/-- A complete offset certificate produces an endpoint at most
    `1 + 2^d / u`, a stronger fact than its mere descent. -/
theorem offset_endpoint_bound {u d k : Nat} (up : 0<u)
    (clock : k≤d) (hit : orbit k u=1) :
    orbit k (2^d+u)≤2^d/u+1 := by
  have coeff := coefficient_lower k u
  rw [hit,Nat.mul_one] at coeff
  have product : (3^(oddCount k u)*2^(d-k))*u≤2^d := calc
    _ = (3^(oddCount k u)*u)*2^(d-k) := by ring
    _ ≤ 2^k*2^(d-k) := Nat.mul_le_mul_right _ coeff
    _ = 2^d := by rw [← pow_add,Nat.add_sub_of_le clock]
  have quotient := (Nat.le_div_iff_mul_le up).mpr product
  rw [offset_lift u clock,hit]
  omega

/-- A certified offset whose complete clock fits the low bits, and whose
    resulting quotient leaves enough room for the quantitative section visit,
    yields the exact induced-return descent needed by SectionDynamics.  All
    guards are explicit ordinary integer inequalities. -/
theorem offset_certificate_return_descent {u d k : Nat} (up : 0<u)
    (clock : k≤d) (hit : orbit k u=1)
    (room : 4*(2^d/u+1).sqrt+2*(2^d/u+1).log2≤d) :
    ∃ j, ForwardSection.returns (2^d+u) j<2^d+u := by
  let y := orbit k (2^d+u)
  let B := 2^d/u+1
  have bound : y≤B := offset_endpoint_bound up clock hit
  have yp : 0<y := by dsimp [y]; rw [offset_lift u clock,hit]; omega
  have bp : 0<B := yp.trans_le bound
  have roots : y.sqrt≤B.sqrt := Nat.sqrt_le_sqrt bound
  have logs : y.log2≤B.log2 := (Nat.le_log2 bp.ne').mpr
    ((Nat.log2_self_le yp.ne').trans bound)
  exact return_descent_of_small_hit (d:=d) (k:=k) (y:=y) (by omega) yp rfl
    (by change 4*B.sqrt+2*B.log2≤d at room; omega)

private theorem max_halving (j n : Nat) : n≤2^j*orbit j n := by
  induction j generalizing n with
  | zero => simp [orbit]
  | succ j ih =>
    have a : n≤2*step n := by unfold step; split <;> omega
    have b := Nat.mul_le_mul_left 2 (ih (step n))
    simpa only [orbit,pow_succ,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using a.trans b

/-- A run of `b` odd steps can force survival for another `r` clocks,
    independently of the later parities. -/
theorem rising_survival {b r v : Nat} (vp : 0<v)
    (height : 2^r*(2^b*v-1) ≤ 3^b*v-1) :
    ∀ j≤b+r, 2^b*v-1≤orbit j (2^b*v-1) := by
  intro j hj
  obtain ⟨endpt,before⟩ := odd_run b v vp
  by_cases early : j≤b
  · exact before j early
  · obtain ⟨l,eq⟩ := Nat.exists_eq_add_of_le (show b≤j by omega)
    have lr : l≤r := by omega
    rw [eq,orbit_add,endpt]
    have lower := max_halving l (3^b*v-1)
    have mono := Nat.mul_le_mul_left (2^b*v-1)
      (Nat.pow_le_pow_right (by decide : 0<2) lr)
    rw [Nat.mul_comm (2^b*v-1) (2^l),Nat.mul_comm (2^b*v-1) (2^r)] at mono
    exact Nat.le_of_mul_le_mul_left (mono.trans (height.trans lower)) (by positivity)

/-- An exact coefficient inequality certifies survival throughout the
    complete binary depth, for every positive multiplier. -/
theorem survival_of_power_gap {b d : Nat} (bd : b≤d)
    (ratio : 2^d≤3^b) (v : Nat) (vp : 0<v) :
    ∀ j≤d, 2^b*v-1≤orbit j (2^b*v-1) := by
  have height : 2^(d-b)*(2^b*v-1)≤3^b*v-1 := by
    have source : 0<2^b*v := by positivity
    have dest : 0<3^b*v := by positivity
    have one : 1≤2^(d-b) := Nat.one_le_pow _ 2 (by decide)
    have bound := Nat.mul_le_mul_right v ratio
    have split : 2^d=2^(d-b)*2^b := by rw [← pow_add,Nat.sub_add_cancel bd]
    rw [split] at bound
    have consumed : 2^(d-b)*(2^b*v-1)+2^(d-b)=(2^(d-b)*2^b)*v := by
      calc
        _ = 2^(d-b)*((2^b*v-1)+1) := by ring
        _ = _ := by rw [Nat.sub_add_cancel (by omega : 1≤2^b*v)]; ring
    omega
  simpa only [Nat.add_sub_of_le bd] using rising_survival vp height

/-- Both an offset and its dyadic translate survive whenever their shared
    odd prefix creates enough height to cover the remaining bit budget. -/
theorem offset_pair_no_descent {b d : Nat} (bd : b≤d) (ratio : 2^d≤3^b) :
    (∀ j≤d, 2^b-1≤orbit j (2^b-1)) ∧
    (∀ j≤d, 2^d+(2^b-1)≤orbit j (2^d+(2^b-1))) := by
  constructor
  · simpa using survival_of_power_gap bd ratio 1 (by decide)
  · have form : 2^d+(2^b-1)=2^b*(2^(d-b)+1)-1 := by
      have pos : 0<2^b := by positivity
      have base : 0<2^d := by positivity
      rw [Nat.mul_add,Nat.mul_one,← pow_add,Nat.add_sub_of_le bd]
      omega
    rw [form]
    exact survival_of_power_gap bd ratio _ (by positivity)

/-- The narrow-band obstruction family. -/
def thinStart (a : Nat) := 2^(3*a)+(2^(2*a)-1)
def thinOffset (a : Nat) := 2^(2*a)-1

theorem thin_depth (a : Nat) : (thinStart a).log2=3*a := by
  have pos : 0<thinStart a := by unfold thinStart; positivity
  have low : 2^(3*a)≤thinStart a := by unfold thinStart; omega
  have small : 2^(2*a)-1<2^(3*a) := by
    have p : 0<2^(2*a) := by positivity
    have inc := Nat.pow_le_pow_right (by decide : 0<2) (show 2*a≤3*a by omega)
    omega
  have high : thinStart a<2^(3*a+1) := by
    unfold thinStart
    rw [pow_succ]
    omega
  have lo := (Nat.le_log2 pos.ne').mpr low
  have hi := (Nat.log2_lt pos.ne').mpr high
  omega

/-- These starts belong to the exact marked section from PR 173. -/
theorem thin_marked {a : Nat} (ap : 0<a) : ForwardSection.Marked (thinStart a) := by
  have powpos : 0<2^(2*a) := by positivity
  have form : thinStart a=2^(2*a)*(2^a+1)-1 := by
    have base : 0<2^(3*a) := by positivity
    unfold thinStart
    rw [Nat.mul_add,Nat.mul_one,← pow_add,show 2*a+a=3*a by omega]
    omega
  have pform : 2^(2*a)=2*2^(2*a-1) := by
    rw [← pow_succ']; congr 1; omega
  have odd : thinStart a%2=1 := by
    rw [form,pform,show 2*2^(2*a-1)*(2^a+1)=2*(2^(2*a-1)*(2^a+1)) by ring]
    have pos : 0<2^(2*a-1)*(2^a+1) := by positivity
    omega
  refine ⟨odd,?_⟩
  unfold ForwardSection.InSection
  rw [thin_depth]
  have gap : thinStart a-2^(3*a)=2^(2*a)-1 := by unfold thinStart; omega
  rw [gap]
  have bound : 3*a+1≤70*2^a := by
    have h := Nat.lt_two_pow_self (n:=a)
    omega
  calc
    (3*a+1)*(2^(2*a)-1) ≤ (70*2^a)*2^(2*a) :=
      Nat.mul_le_mul bound (Nat.sub_le _ _)
    _ = 70*2^(3*a) := by rw [Nat.mul_assoc,← pow_add]; congr 2; omega

/-- Its relative offset is strictly less than `2^(-a)`, exponentially
    narrower than the marked interval's inverse-depth width. -/
theorem thin_relative_offset (a : Nat) :
    2^a*(thinStart a-2^((thinStart a).log2))<2^((thinStart a).log2) := by
  rw [thin_depth]
  have gap : thinStart a-2^(3*a)=2^(2*a)-1 := by unfold thinStart; omega
  rw [gap]
  have small : 2^(2*a)-1<2^(2*a) := by
    have : 0<2^(2*a) := by positivity
    omega
  calc
    2^a*(2^(2*a)-1) < 2^a*2^(2*a) := Nat.mul_lt_mul_of_pos_left small (by positivity)
    _ = 2^(3*a) := by rw [← pow_add]; congr 1; omega

private theorem thin_survival (a v : Nat) (vp : 0<v) :
    ∀ j≤3*a, 2^(2*a)*v-1≤orbit j (2^(2*a)*v-1) := by
  have ratio : 2^(3*a)≤3^(2*a) := by
    rw [pow_mul,pow_mul]
    exact Nat.pow_le_pow_left (by decide) a
  exact survival_of_power_gap (by omega) ratio v vp

/-- The offset has no strict descent during the entire available low-bit
    clock, at every scale of this infinite family. -/
theorem thin_offset_no_descent (a : Nat) :
    ∀ j≤3*a, thinOffset a≤orbit j (thinOffset a) := by
  simpa [thinOffset] using thin_survival a 1 (by decide)

/-- The marked start itself also has no strict descent during that clock. -/
theorem thin_start_no_descent (a : Nat) :
    ∀ j≤3*a, thinStart a≤orbit j (thinStart a) := by
  have form : thinStart a=2^(2*a)*(2^a+1)-1 := by
    have pos : 0<2^(2*a) := by positivity
    have base : 0<2^(3*a) := by positivity
    unfold thinStart
    rw [Nat.mul_add,Nat.mul_one,← pow_add,show 2*a+a=3*a by omega]
    omega
  rw [form]
  exact thin_survival a (2^a+1) (by positivity)

/-- Every positive scale of the thin family is an ordinary, marked
    counterexample to the proposed universal quick-offset certificate rule. -/
theorem thin_no_quick_certificate {a : Nat} (ap : 0<a) :
    ∀ k≤(thinStart a).log2,
      orbit k (thinStart a-2^((thinStart a).log2))≠1 := by
  have low : 2^2≤2^(2*a) := Nat.pow_le_pow_right (by decide) (by omega)
  have up : 1<thinOffset a := by unfold thinOffset; norm_num at low; omega
  intro k clock hit
  rw [thin_depth] at clock hit
  have gap : thinStart a-2^(3*a)=thinOffset a := by unfold thinStart thinOffset; omega
  rw [gap] at hit
  have bound := thin_offset_no_descent a k clock
  omega

#print axioms prefix_lift
#print axioms offset_boundary_parity
#print axioms offset_descent
#print axioms convergent_offset_eventually_lifts
#print axioms offset_certificate_return_descent
#print axioms offset_pair_no_descent
#print axioms thin_marked
#print axioms thin_relative_offset
#print axioms thin_offset_no_descent
#print axioms thin_start_no_descent
#print axioms thin_no_quick_certificate

end CollatzShell.BandDescent
