module

public import ForwardSection

@[expose] public section

/-!
# Exact rotation bookkeeping and descent from an early marked return

The dyadic band theorem supplies a marked return, but it does not bound the
integer part of the accumulated binary valuation.  This file keeps that
integer part explicit, and proves a positive descent certificate: sufficiently
early marked returns at sufficiently large height force an ordinary descent.

No claim of universal descent is made.
-/

namespace CollatzShell.BandRotation

open Real ForwardSection

/-- The actual total number of factors of two removed in `j` odd steps. -/
def valuationSum (n : Nat) : Nat → Nat
  | 0 => 0
  | j+1 => valuationSum n j + twos (3*oddOrbit n j+1)

/-- The exact positive logarithmic correction at an odd value. -/
noncomputable def phaseError (x : Nat) : ℝ := logb 2 (1+1/(3*(x:ℝ)))

noncomputable def errorSum (n : Nat) : Nat → ℝ
  | 0 => 0
  | j+1 => errorSum n j + phaseError (oddOrbit n j)

private theorem odd_orbit_positive {n : Nat} (hn : 0<n) (j : Nat) :
    0<oddOrbit n j := by
  cases j with
  | zero => exact hn
  | succ j =>
    exact Nat.ordCompl_pos 2 (by omega : 3*oddOrbit n j+1≠0)

theorem phase_error_bounds {x : Nat} (hx : 0<x) :
    0≤phaseError x ∧ phaseError x≤1/(x:ℝ) := by
  have xp : (0:ℝ)<x := by exact_mod_cast hx
  let d : ℝ := 1/(3*(x:ℝ))
  have dp : 0<d := by dsimp [d]; positivity
  have ep : 0≤logb 2 (1+d) := logb_nonneg (by norm_num) (by linarith)
  refine ⟨ep,?_⟩
  change log (1+d)/log 2≤_
  apply (div_le_iff₀ (log_pos (by norm_num))).mpr
  have up := log_le_sub_one_of_pos (show 0<1+d by linarith)
  have dl : d*x=1/3 := by dsimp [d]; field_simp
  rw [show 1/(x:ℝ)*log 2=log 2/x by ring]
  apply (le_div_iff₀ xp).mpr
  nlinarith [mul_le_mul_of_nonneg_right up xp.le,log_two_bounds.1]

theorem exact_height_step {x : Nat} (hx : 0<x) :
    height (oddStep x)=height x+alpha-(twos (3*x+1):ℝ)+phaseError x := by
  have xp : (0:ℝ)<x := by exact_mod_cast hx
  let d : ℝ := 1/(3*(x:ℝ))
  have dp : 0<d := by dsimp [d]; positivity
  have num : (2:ℝ)^twos (3*x+1)*(oddStep x:ℝ)=(3*x)*(1+d) := by
    have h : (2:ℝ)^twos (3*x+1)*(oddStep x:ℝ)=3*(x:ℝ)+1 := by
      exact_mod_cast Nat.ordProj_mul_ordCompl_eq_self (3*x+1) 2
    rw [h]; dsimp [d]; field_simp
  have base := congrArg (logb 2) num
  have op : 0<oddStep x := Nat.ordCompl_pos 2 (by omega : 3*x+1≠0)
  have op' : (oddStep x:ℝ)≠0 := by positivity
  simp only [logb_mul (by positivity : (2:ℝ)^twos (3*x+1)≠0) op',
    logb_pow,logb_two,mul_one,
    logb_mul (by positivity : 3*(x:ℝ)≠0) (by linarith : 1+d≠0),
    logb_mul (by norm_num : (3:ℝ)≠0) xp.ne'] at base
  dsimp only [height,alpha,phaseError]
  dsimp only [d] at base
  linarith

/-- The exact height identity retains the actual valuation sum, rather than an
    existential integer that might conceal the unresolved drift. -/
theorem exact_height {n : Nat} (hn : 0<n) (j : Nat) :
    height (oddOrbit n j)=height n+j*alpha-(valuationSum n j:ℝ)+errorSum n j := by
  induction j with
  | zero => simp [oddOrbit,valuationSum,errorSum]
  | succ j ih =>
    rw [oddOrbit,exact_height_step (odd_orbit_positive hn j),ih,valuationSum,errorSum]
    push_cast
    ring

/-- An actual lower floor bounds the accumulated correction. -/
theorem error_sum_bounds {n m : Nat} (hn : 0<n) (hm : 0<m) (j : Nat)
    (floor : ∀ i<j, m≤oddOrbit n i) :
    0≤errorSum n j ∧ errorSum n j≤j/(m:ℝ) := by
  induction j with
  | zero => simp [errorSum]
  | succ j ih =>
    obtain ⟨el,eu⟩ := ih (fun i hi => floor i (by omega))
    obtain ⟨dl,du⟩ := phase_error_bounds (odd_orbit_positive hn j)
    have cmp : (1:ℝ)/oddOrbit n j≤1/m :=
      one_div_le_one_div_of_le (by exact_mod_cast hm)
        (by exact_mod_cast floor j (by omega))
    constructor
    · simp only [errorSum]; linarith
    · simp only [errorSum,Nat.cast_add,Nat.cast_one,add_div]; linarith

/-- Both ends of the marked phase window are one-sided. -/
theorem marked_height_window {x : Nat} (mark : Marked x) :
    0≤height x-x.log2 ∧ height x-x.log2≤140/((x.log2:ℝ)+1) := by
  let P := 2^x.log2
  have xp : 0<x := by have := mark.1; omega
  have xr : (0:ℝ)<x := by exact_mod_cast xp
  have pp : (0:ℝ)<P := by dsimp [P]; positivity
  have pl : P≤x := Nat.log2_self_le xp.ne'
  have br : ((x.log2:ℝ)+1)*((x:ℝ)-P)≤70*P := by
    have bound := mark.2
    change (x.log2+1)*(x-P)≤70*P at bound
    simpa only [Nat.cast_add,Nat.cast_one,Nat.cast_mul,Nat.cast_ofNat,Nat.cast_sub pl] using
      (show (((x.log2+1)*(x-P):Nat):ℝ)≤((70*P:Nat):ℝ) by exact_mod_cast bound)
  let v := (x:ℝ)/P
  have vp : 0<v := div_pos xr pp
  have width : v-1≤70/((x.log2:ℝ)+1) := by
    apply (le_div_iff₀ (by positivity)).mpr
    rw [show (v-1)*((x.log2:ℝ)+1)=(((x.log2:ℝ)+1)*(x-P))/P by
      dsimp [v]; field_simp]
    exact (div_le_iff₀ pp).mpr br
  have id : logb 2 v=height x-(x.log2:ℝ) := by
    dsimp only [v,height,P]
    rw [logb_div xr.ne' pp.ne',Nat.cast_pow,Nat.cast_ofNat,
      logb_pow,logb_two,mul_one]
  refine ⟨sub_nonneg.mpr (Real.log2_le_logb x),?_⟩
  rw [←id]
  apply (div_le_iff₀ (log_pos (by norm_num))).mpr
  calc log v ≤ v-1 := log_le_sub_one_of_pos vp
       _ ≤ 70/((x.log2:ℝ)+1) := width
       _ = (140/((x.log2:ℝ)+1))*(1/2) := by ring
       _ ≤ _ := mul_le_mul_of_nonneg_left log_two_bounds.1 (by positivity)

/-- Every non-descending marked return supplies this explicit rational
    approximation. The constant is 140, rather than a sum of two widths,
    because the endpoint phase offsets are both nonnegative. -/
theorem marked_return_approx {n j : Nat} (start : Marked n)
    (finish : Marked (oddOrbit n j))
    (floor : ∀ i≤j, n≤oddOrbit n i) :
    ∃ a : Nat, |(j:ℝ)*alpha-a|≤140/((n.log2:ℝ)+1)+j/(n:ℝ) := by
  have np : 0<n := by have := start.1; omega
  let y := oddOrbit n j
  have yp : 0<y := odd_orbit_positive np j
  have nd : n.log2≤y.log2 := (Nat.le_log2 yp.ne').mpr
    ((Nat.log2_self_le np.ne').trans (floor j le_rfl))
  have nd' : (n.log2:ℝ)+1≤(y.log2:ℝ)+1 := by
    exact_mod_cast Nat.add_le_add_right nd 1
  obtain ⟨xl,xu⟩ := marked_height_window start
  obtain ⟨yl,yu⟩ := marked_height_window finish
  change 0≤height y-y.log2 at yl
  change height y-y.log2≤140/((y.log2:ℝ)+1) at yu
  have yu' : height y-y.log2≤140/((n.log2:ℝ)+1) :=
    yu.trans (div_le_div_of_nonneg_left (by norm_num) (by positivity) nd')
  obtain ⟨el,eu⟩ := error_sum_bounds np np j (fun i hi => floor i hi.le)
  have h := exact_height np j
  change height y=_ at h
  let a := valuationSum n j+y.log2-n.log2
  have ar : (a:ℝ)=(valuationSum n j:ℝ)+y.log2-n.log2 := by
    dsimp only [a]
    rw [Nat.cast_sub (by omega),Nat.cast_add]
  refine ⟨a,?_⟩
  rw [ar,abs_le]
  constructor <;> linarith [show (0:ℝ)≤j/(n:ℝ) by positivity]

/-- At large enough binary height, a marked return without an intervening
    descent cannot occur in the first `H` odd clocks. -/
theorem nondecreasing_marked_return_late {n j H : Nat}
    (start : Marked n) (finish : Marked (oddOrbit n j))
    (floor : ∀ i≤j, n≤oddOrbit n i) (jp : 0<j)
    (error_budget : (n.log2+1)*H≤n)
    (height_budget : 141*(4^H+1)≤n.log2+1) : H<j := by
  have np : 0<n := by have := start.1; omega
  by_contra! early
  obtain ⟨a,approx⟩ := marked_return_approx start finish floor
  have jp' : (0:ℝ)<n := by exact_mod_cast np
  have dp : (0:ℝ)<(n.log2:ℝ)+1 := by positivity
  have mult : ((n.log2:ℝ)+1)*(j:ℝ)≤n := by
    exact_mod_cast (Nat.mul_le_mul_left (n.log2+1) early).trans error_budget
  have tiny : (j:ℝ)/n≤1/((n.log2:ℝ)+1) :=
    (div_le_div_iff₀ jp' dp).mpr (by nlinarith only [mult])
  have scale : (141:ℝ)*(((4^H:Nat):ℝ)+1)≤(n.log2:ℝ)+1 := by
    exact_mod_cast height_budget
  have small : |(j:ℝ)*alpha-a|≤1/(((4^H:Nat):ℝ)+1) := by
    calc _ ≤ 140/((n.log2:ℝ)+1)+j/(n:ℝ) := approx
         _ ≤ 141/((n.log2:ℝ)+1) := by
           rw [show (141:ℝ)/((n.log2:ℝ)+1)=140/((n.log2:ℝ)+1)+1/((n.log2:ℝ)+1) by ring]
           exact add_le_add le_rfl tiny
         _ ≤ _ := (div_le_div_iff₀ dp (by positivity)).mpr (by nlinarith only [scale])
  have sep := grid_barrier (N:=4^H) (by positivity) jp small
  have up := Nat.pow_le_pow_right (by decide : 0<4) early
  omega

/-- A short marked return is an actual descent certificate. This result has no
    no-descent hypothesis: its conclusion gives a smaller ordinary orbit value. -/
theorem early_marked_return_forces_descent {n j H : Nat}
    (start : Marked n) (finish : Marked (oddOrbit n j))
    (jp : 0<j) (early : j≤H)
    (error_budget : (n.log2+1)*H≤n)
    (height_budget : 141*(4^H+1)≤n.log2+1) :
    ∃ y<n, Hits n y := by
  by_cases floor : ∀ i≤j, n≤oddOrbit n i
  · have := nondecreasing_marked_return_late start finish floor jp error_budget height_budget
    omega
  · push Not at floor
    obtain ⟨i,_,drop⟩ := floor
    exact ⟨oddOrbit n i,drop,odd_orbit_hit start.1 i⟩

/-- A small positive leading gap and a long suffix of binary ones. -/
def risingSeed (d m : Nat) : Nat := 2^(d-m)*(d+1)-1

private theorem rising_seed_spec {d m : Nat} (hd : d=2^m) (hm : m<d) :
    (risingSeed d m).log2=d ∧ Marked (risingSeed d m) ∧ 2^d≤risingSeed d m := by
  let Q := 2^(d-m)
  have qp : 0<Q := by dsimp [Q]; positivity
  have main : Q*d=2^d := by
    dsimp [Q]
    conv_lhs => rhs; rw [hd]
    rw [←pow_add,show d-m+m=d by omega]
  have qq : Q≤2^d := Nat.pow_le_pow_right (by decide) (by omega)
  have value : risingSeed d m=2^d+Q-1 := by
    dsimp only [risingSeed]
    rw [Nat.mul_add,Nat.mul_one]
    change Q*d+Q-1=_
    rw [main]
  have lo : 2^d≤risingSeed d m := by rw [value]; omega
  have hi : risingSeed d m<2^(d+1) := by rw [value,pow_succ]; omega
  have np : 0<risingSeed d m := lt_of_lt_of_le (by positivity) lo
  have len : (risingSeed d m).log2=d := by
    have := (Nat.le_log2 np.ne').mpr lo
    have := (Nat.log2_lt np.ne').mpr hi
    omega
  have evenQ : Q%2=0 := by
    obtain ⟨b,hb⟩ : ∃ b, d-m=b+1 := ⟨d-m-1,by omega⟩
    dsimp [Q]
    rw [hb,pow_succ]
    omega
  have odd : risingSeed d m%2=1 := by
    have productpos : 0<Q*(d+1) := by positivity
    have eq : risingSeed d m+1=Q*(d+1) := by
      change Q*(d+1)-1+1=Q*(d+1)
      omega
    have : (Q*(d+1))%2=0 := by rw [Nat.mul_mod,evenQ]; simp
    omega
  refine ⟨len,⟨odd,?_⟩,lo⟩
  unfold InSection
  rw [len]
  have gap : risingSeed d m-2^d=Q-1 := by rw [value]; omega
  rw [gap]
  have qdec : Q-1+1=Q := by omega
  have bound : (d+1)*(Q-1)≤2*2^d := by nlinarith [main,qq,qdec]
  omega

private theorem rising_prefix_value {d m j : Nat} (hj : j≤d-m) :
    orbit j (risingSeed d m)+1=3^j*(2^(d-m-j)*(d+1)) := by
  have decomp : 2^(d-m)*(d+1)=2^j*(2^(d-m-j)*(d+1)) := by
    rw [←mul_assoc,←pow_add]
    congr 2
    omega
  dsimp only [risingSeed]
  rw [decomp,(odd_run j _ (by positivity)).1]
  have pos : 0<3^j*(2^(d-m-j)*(d+1)) := by positivity
  omega

private theorem rising_prefix_odd {d m j : Nat} (hj : j<d-m) :
    orbit j (risingSeed d m)%2=1 := by
  have eq := rising_prefix_value hj.le
  obtain ⟨b,hb⟩ : ∃ b, d-m-j=b+1 := ⟨d-m-j-1,by omega⟩
  rw [hb,show 3^j*(2^(b+1)*(d+1))=2*(3^j*(2^b*(d+1))) by ring] at eq
  omega

private theorem odd_step_eq_step {x : Nat} (hx : x%2=1) (hs : step x%2=1) :
    oddStep x=step x := by
  have eq : 3*x+1=2*step x := by simp [step,hx]; omega
  have undiv : ¬2∣step x := by omega
  dsimp only [oddStep,oddPart,twos]
  rw [eq]
  simpa only [pow_one] using Nat.ordCompl_pow_mul_of_not_dvd 1 Nat.prime_two undiv

private theorem rising_odd_prefix {d m H : Nat} (room : H<d-m) :
    ∀ j≤H, oddOrbit (risingSeed d m) j=orbit j (risingSeed d m) := by
  intro j hj
  induction j with
  | zero => rfl
  | succ j ih =>
    have prev := ih (by omega)
    rw [oddOrbit,prev,orbit_add j 1]
    exact odd_step_eq_step (rising_prefix_odd (by omega)) (by
      change orbit 1 (orbit j (risingSeed d m))%2=1
      rw [←orbit_add]
      exact rising_prefix_odd (by omega))

private theorem three_mul_le_two_pow {m : Nat} (hm : 4≤m) : 3*m≤2^m := by
  induction m,hm using Nat.le_induction with
  | base => norm_num
  | succ m hm ih =>
    rw [pow_succ]
    have hp : 3≤2^m := by omega
    omega

/-- The early-return descent certificate cannot be paired with an unconditional
    assertion that such a return always occurs.  For every window `H`, this
    explicit ordinary family satisfies both numerical certificate budgets,
    rises throughout the window, and has no positive marked visit in it. -/
theorem short_return_window_can_be_empty (H : Nat) :
    ∃ n : Nat, Marked n ∧
      (n.log2+1)*H≤n ∧ 141*(4^H+1)≤n.log2+1 ∧
      (∀ j≤H, n≤oddOrbit n j) ∧
      (∀ j, 0<j → j≤H → ¬Marked (oddOrbit n j)) := by
  let m := 2*H+10
  let d := 2^m
  let n := risingSeed d m
  have hm : 4≤m := by dsimp [m]; omega
  have md : 3*m≤d := three_mul_le_two_pow hm
  have hd : d=2^m := rfl
  have ml : m<d := by omega
  obtain ⟨len,mark,lo⟩ := rising_seed_spec hd ml
  change n.log2=d at len
  change Marked n at mark
  change 2^d≤n at lo
  have hp : 0<d := by dsimp [d]; positivity
  have hH : H≤m := by dsimp [m]; omega
  have square : (d+1)*H≤d*d := by
    nlinarith [Nat.mul_le_mul_right (d+1) hH,Nat.mul_le_mul_right d md,
      Nat.mul_le_mul_left m hp]
  have exponential : d*d≤2^d := by
    calc d*d = 2^(m+m) := (pow_add (2:Nat) m m).symm
         _ ≤ 2^d := Nat.pow_le_pow_right (by decide) (by omega)
  have budget : (n.log2+1)*H≤n := by rw [len]; exact square.trans (exponential.trans lo)
  have shape : d=1024*4^H := by
    dsimp [d,m]
    rw [pow_add,pow_mul]
    norm_num
    ring
  have scale : 141*(4^H+1)≤n.log2+1 := by
    rw [len,shape]
    have positive : 0<(4:Nat)^H := by positivity
    omega
  have room : H<d-m := by omega
  have rising : ∀ j≤H, n≤oddOrbit n j := by
    intro j hj
    rw [rising_odd_prefix room j hj]
    exact (odd_run (d-m) (d+1) (by omega)).2 j (by omega)
  refine ⟨n,mark,budget,scale,rising,?_⟩
  intro j jp jH finish
  have late := nondecreasing_marked_return_late mark finish
    (fun i hi => rising i (hi.trans jH)) jp budget scale
  omega

#print axioms exact_height
#print axioms marked_return_approx
#print axioms nondecreasing_marked_return_late
#print axioms early_marked_return_forces_descent
#print axioms short_return_window_can_be_empty

end CollatzShell.BandRotation
