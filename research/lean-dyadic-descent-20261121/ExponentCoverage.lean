import InfiniteDescent

/-!
# Simultaneous blocks of prescribed dyadic exponents

PR182's unbounded-family theorem chooses one exponent after choosing an
offset certificate. Here one positive approximation produces a whole
interval of exponents, and the
same interval works simultaneously for every supplied offset certificate
within an arbitrary clock budget.  This is an unconditional
existence theorem for arbitrarily large blocks; it is not a cover of every
dyadic exponent or of every marked ordinary orbit.
-/

namespace CollatzShell.ExponentCoverage

open ForwardSection OffsetDescent MarkedOffsetReturn
open ForwardSection.InfiniteDescent

theorem oddCount_le_clock (t r : Nat) : oddCount t r≤t := by
  induction t generalizing r with
  | zero => simp [oddCount]
  | succ t ih =>
    simp only [oddCount]
    have h := ih (step r)
    have parity := Nat.mod_lt r (by decide : 0<2)
    omega

/-- A supplied ordinary hit certificate itself bounds its source; no separate
    offset-size budget is needed. -/
theorem certificate_source_bound {h r : Nat} (hit : orbit h r=1) : r≤2^h := by
  have lower := linear_lower h r
  rw [hit,Nat.mul_one] at lower
  have positive : 1≤3^(oddCount h r) := by
    have hp : 0<3^(oddCount h r) := by positivity
    omega
  nlinarith only [lower,positive,Nat.zero_le r]

theorem twice_le_three_pow (q : Nat) : 2*q≤3^q := by
  induction q with
  | zero => simp
  | succ q ih =>
    rw [pow_succ]
    have pos : 0<3^q := by positivity
    nlinarith only [ih,pos]

/-- A single positive rational approximation marks all the endpoints in an
    exponent window of length proportional to its denominator.  The additive
    one is retained, including its contribution to the logarithmic phase. -/
theorem endpoint_marked_phase_window {q a e : Nat} (qp : 0<q)
    (ep : 0<e) (eqbound : e≤10*q)
    (lower : 0<(q:ℝ)*alpha-a)
    (upper : (q:ℝ)*((q:ℝ)*alpha-a)≤2) :
    Marked (3^q*2^e+1) := by
  let P : ℝ := (3:ℝ)^q
  let B : ℝ := (2:ℝ)^e
  have pp : 0<P := by dsimp [P]; positivity
  have bp : 0<B := by dsimp [B]; positivity
  have btwo : (2:ℝ)≤B := by
    dsimp [B]
    exact_mod_cast (Nat.pow_le_pow_right (by decide : 0<2) (show 1≤e by omega))
  have qr : (0:ℝ)<q := by exact_mod_cast qp
  have qone : (1:ℝ)≤q := by exact_mod_cast qp
  have qP : 2*(q:ℝ)≤P := by
    dsimp [P]
    exact_mod_cast twice_le_three_pow q
  let u : ℝ := 1/(P*B)
  have up : 0<u := by dsimp [u]; positivity
  let error : ℝ := Real.logb 2 (1+u)
  have nonneg : 0≤error := Real.logb_nonneg (by norm_num) (by linarith)
  have small : error≤1/P := by
    change Real.log (1+u)/Real.log 2≤_
    apply (div_le_iff₀ (Real.log_pos (by norm_num))).mpr
    calc Real.log (1+u) ≤ u := by
           have h := Real.log_le_sub_one_of_pos (by linarith : 0<1+u)
           linarith
         _ ≤ (1/P)*(1/2) := by
           dsimp [u]
           rw [← one_div_mul_one_div]
           exact mul_le_mul_of_nonneg_left
             (one_div_le_one_div_of_le (by norm_num) btwo) (by positivity)
         _ ≤ (1/P)*Real.log 2 :=
           mul_le_mul_of_nonneg_left log_two_bounds.1 (by positivity)
  have charged : 2*(q:ℝ)*error≤1 := by
    calc 2*(q:ℝ)*error ≤ P*error := mul_le_mul_of_nonneg_right qP nonneg
         _ ≤ P*(1/P) := mul_le_mul_of_nonneg_left small pp.le
         _ = 1 := by field_simp
  have one : error≤1 := by nlinarith only [qone,charged,nonneg]
  have factor : ((3^q*2^e+1:Nat):ℝ)=P*B*(1+u) := by
    push_cast
    dsimp [P,B,u]
    field_simp
  have logval : height (3^q*2^e+1)=(e:ℝ)+(q:ℝ)*alpha+error := by
    unfold height
    rw [factor,Real.logb_mul (by positivity : P*B≠0) (by linarith : 1+u≠0),
      Real.logb_mul pp.ne' bp.ne']
    dsimp [P,B,error,alpha]
    rw [Real.logb_pow,Real.logb_pow,logb_two]
    ring
  have bound : ((3^q*2^e+1).log2:ℝ)+1≤14*(q:ℝ) := by
    have h := Real.log2_le_logb (3^q*2^e+1)
    change ((3^q*2^e+1).log2:ℝ)≤height (3^q*2^e+1) at h
    rw [logval] at h
    have rot := mul_lt_mul_of_pos_left rotation_bounds.2 qr
    have eb : (e:ℝ)≤10*(q:ℝ) := by exact_mod_cast eqbound
    nlinarith only [h,rot,eb,qone,one]
  let phase : ℝ := (q:ℝ)*alpha-a+error
  have positive : 0≤phase := by dsimp [phase]; linarith only [lower,nonneg]
  have charge : 2*(q:ℝ)*phase≤5 := by
    dsimp [phase]
    nlinarith only [upper,charged]
  have close : (((3^q*2^e+1).log2:ℝ)+1)*phase≤35 := by
    calc _ ≤ (14*(q:ℝ))*phase := mul_le_mul_of_nonneg_right bound positive
         _ ≤ 35 := by nlinarith only [charge]
  have even : 2^e%2=0 := by
    obtain ⟨v,rfl⟩ := Nat.exists_eq_succ_of_ne_zero ep.ne'
    rw [pow_succ]
    omega
  have odd : (3^q*2^e+1)%2=1 := by
    rw [Nat.add_mod,Nat.mul_mod,even]
    simp
  refine ⟨odd,section_of_phase (by positivity) (z:=(a:ℤ)+e) ?_ ?_⟩
  · rw [logval]
    push_cast
    dsimp [phase] at positive
    linarith
  · rw [logval]
    push_cast
    convert close using 1
    dsimp [phase]
    ring

/-- A genuine descent in the actual marked return process, with an optional
    prescribed relative saving.  The endpoint need not be the first return. -/
def Success (C r d : Nat) : Prop :=
  Marked (2^d+r) ∧ ∃ y k : Nat, Marked y ∧ y<2^d+r ∧
    C*y<2^d+r ∧ 0<k ∧ returns (2^d+r) k=y ∧
    (Basin (2^d+r) ↔ Basin y)

/-- A reusable arithmetic interface for a common exponent block.  The
    approximation, additive-one budget, and coefficient guard are shared by
    all the supplied offset certificates. The following theorems discharge
    these guards unconditionally, including an exponential saving factor. -/
theorem simultaneous_block_of_coefficient {q a H C : Nat}
    (qp : 0<q) (Hq : H≤q)
    (lower : 0<(q:ℝ)*alpha-a)
    (upper : (q:ℝ)*((q:ℝ)*alpha-a)≤2)
    (saving : C<3^q)
    (coefficient : ∀ h p : Nat, h≤H → p≤h →
      (C+1)*3^q<2^(h+2*(q-p))) :
    ∀ r h d : Nat, r%2=1 → h≤H → orbit h r=1 →
      2*q+H+1≤d → d+H≤12*q → Success C r d := by
  intro r h d odd hH hit left right
  let p := oddCount h r
  have ph : p≤h := oddCount_le_clock h r
  let s := q-p
  let e := d-(h+2*s)
  have pq : p+s=q := by dsimp [s]; omega
  have decomp : h+2*s+e=d := by dsimp [e,s]; omega
  have ep : 0<e := by dsimp [e,s]; omega
  have eqbound : e≤10*q := by dsimp [e,s]; omega
  let n := 2^d+r
  let y := 3^q*2^e+1
  have rp : 0<r := by omega
  have source : r≤2^H :=
    (certificate_source_bound hit).trans (Nat.pow_le_pow_right (by decide) hH)
  have small : r<2^d :=
    source.trans_lt (Nat.pow_lt_pow_right (by decide) (by omega : H<d))
  have price : 12*q+1≤70*2^(2*q) := by
    have power := Nat.lt_two_pow_self (n:=2*q)
    omega
  have width : (d+1)*r≤70*2^d := by
    calc (d+1)*r ≤ (12*q+1)*2^H :=
           Nat.mul_le_mul (by omega) source
         _ ≤ (70*2^(2*q))*2^H := Nat.mul_le_mul_right _ price
         _ = 70*2^(2*q+H) := by rw [pow_add]; ring
         _ ≤ 70*2^d := Nat.mul_le_mul_left _
           (Nat.pow_le_pow_right (by decide) (by omega : 2*q+H≤d))
  have initial : Marked n := marked_dyadic_offset (by omega) odd small width
  have target : Marked y := endpoint_marked_phase_window qp ep eqbound lower upper
  have endpoint : orbit (h+2*s) n=y := by
    have lift := padded_lift_endpoint hit s e
    rw [decomp] at lift
    change orbit (h+2*s) (2^d+r)=3^(p+s)*2^e+1 at lift
    rw [pq] at lift
    exact lift
  have guard : (C+1)*3^q<2^(h+2*s) := coefficient h p hH ph
  have contract : 3^q<2^(h+2*s) := by
    calc 3^q = 1*3^q := by omega
         _ ≤ (C+1)*3^q := Nat.mul_le_mul_right _ (by omega)
         _ < _ := guard
  have decrease : y<n := by
    have scaled := Nat.mul_lt_mul_of_pos_right contract (by positivity : 0<2^e)
    rw [← pow_add,decomp] at scaled
    dsimp [n,y]
    omega
  have strong : C*y<n := by
    have scaled := Nat.mul_lt_mul_of_pos_right guard (by positivity : 0<2^e)
    rw [← pow_add,decomp] at scaled
    have atLeastOne : 1≤2^e := by
      have hp : 0<2^e := by positivity
      omega
    have ample : C<3^q*2^e := saving.trans_le
      (by simpa only [Nat.mul_one] using Nat.mul_le_mul_left (3^q) atLeastOne)
    dsimp [y,n]
    nlinarith only [scaled,ample,Nat.zero_le r]
  have np : 0<n := by dsimp [n]; positivity
  obtain ⟨k,cap⟩ := captures np (h+2*s) (endpoint ▸ target)
  have visited : returns n k=y := cap.trans endpoint
  have kp : 0<k := by
    cases k with
    | zero => simp only [returns] at visited; omega
    | succ k => omega
  exact ⟨initial,y,k,target,decrease,strong,kp,visited,basin_at_hit ⟨_,endpoint⟩⟩

/-- Every prescribed exponent in this block works for every offset certificate
    within the fixed clock budget, with any fixed desired saving factor. -/
theorem simultaneous_block_of_approximant {q a H C : Nat}
    (large : 5*(H+C+1)<q)
    (lower : 0<(q:ℝ)*alpha-a)
    (upper : (q:ℝ)*((q:ℝ)*alpha-a)≤2) :
    ∀ r h d : Nat, r%2=1 → h≤H → orbit h r=1 →
      2*q+H+1≤d → d+H≤12*q → Success C r d := by
  have saving : C<3^q := (show C<q by omega).trans
    ((Nat.lt_two_pow_self (n:=q)).trans_le (Nat.pow_le_pow_left (by decide : 2≤3) q))
  apply simultaneous_block_of_coefficient (by omega) (by omega) lower upper saving
  intro h p hH ph
  exact padded_coefficient_contract_scaled (by omega)

/-- Arbitrarily large common exponent blocks exist without any assumption
    about the complete collection of ordinary Collatz inputs. -/
theorem arbitrarily_large_simultaneous_blocks (C H N : Nat) :
    ∃ q : Nat, N<q ∧ 5*(H+C+1)<q ∧
      ∀ r h d : Nat, r%2=1 → h≤H → orbit h r=1 →
        2*q+H+1≤d → d+H≤12*q → Success C r d := by
  obtain ⟨q,a,large,lower,upper⟩ :=
    arbitrarily_large_positive_approximants (N+5*(H+C+1))
  exact ⟨q,by omega,by omega,
    simultaneous_block_of_approximant (by omega) lower upper.le⟩

/-- The certificate budget may grow with the selected block: every supplied
    certificate of length at most `q/10` is covered simultaneously. The
    clock budget and source-size upper bound have no fixed ceiling. -/
theorem growing_certificate_blocks (C N : Nat) :
    ∃ q : Nat, N<q ∧ 5*(q/10+C+1)<q ∧
      ∀ r h d : Nat, r%2=1 → h≤q/10 → orbit h r=1 →
        2*q+q/10+1≤d → d+q/10≤12*q → Success C r d := by
  obtain ⟨q,a,large,lower,upper⟩ :=
    arbitrarily_large_positive_approximants (N+10*(C+1))
  have budget : 5*(q/10+C+1)<q := by
    have divided := Nat.div_mul_le_self q 10
    omega
  exact ⟨q,by omega,budget,simultaneous_block_of_approximant budget lower upper.le⟩

/-- The growing certificate budget leaves an exponential coefficient reserve.
    The proof uses only the integer inequalities `3^10 < 2^16` and
    `3^9 < 2^15`; the one-sided approximation is unchanged. -/
theorem exponential_padded_coefficient {q h p : Nat} (large : 100≤q)
    (ph : p≤h) (hH : h≤q/10) :
    (2^(q/10+1)+1)*3^q<2^(h+2*(q-p)) := by
  let H := q/10
  let v := q%10
  have vp : v≤9 := by dsimp [v]; omega
  have decomp : q=10*H+v := by
    have eq := Nat.mod_add_div q 10
    dsimp [H,v]
    omega
  have hp : 10≤H := by dsimp [H]; omega
  have coefficient : 3^q≤2^(16*H+15) := by
    calc
      3^q = (3^10)^H*3^v := by rw [decomp,pow_add,pow_mul]
      _ ≤ (2^16)^H*2^15 := Nat.mul_le_mul
        (Nat.pow_le_pow_left (by decide : 3^10≤2^16) H)
        ((Nat.pow_le_pow_right (by decide : 0<3) vp).trans (by decide : 3^9≤2^15))
      _ = 2^(16*H+15) := by rw [← pow_mul,← pow_add]
  have multiplier : 2^(H+1)+1≤2^(H+2) := by
    have one : 1≤2^H := by
      have hp : 0<2^H := by positivity
      omega
    simp only [pow_add,pow_one,show (2:Nat)^2=4 by decide]
    omega
  have exponent : 17*H+17<h+2*(q-p) := by
    change h≤H at hH
    omega
  change (2^(H+1)+1)*3^q<_
  calc
    _ ≤ 2^(H+2)*2^(16*H+15) := Nat.mul_le_mul multiplier coefficient
    _ = 2^(17*H+17) := by rw [← pow_add]; congr 1; omega
    _ < _ := Nat.pow_lt_pow_right (by decide) exponent

/-- A fixed integer-power saving, stated without real-power conventions. -/
def PowerSuccess (r d : Nat) : Prop :=
  Marked (2^d+r) ∧ ∃ y k : Nat, Marked y ∧ y<2^d+r ∧
    y^120<(2^d+r)^119 ∧ 0<k ∧ returns (2^d+r) k=y ∧
    (Basin (2^d+r) ↔ Basin y)

theorem power_success_of_scale {C r d : Nat} (scale : 2^d+r≤C^120)
    (success : Success C r d) : PowerSuccess r d := by
  obtain ⟨initial,y,k,target,drop,strong,kp,visit,basin⟩ := success
  have powered := Nat.pow_lt_pow_left strong (by decide : 120≠0)
  rw [mul_pow] at powered
  have bound := (Nat.mul_le_mul_right (y^120) scale).trans_lt powered
  have form : (2^d+r)^120=(2^d+r)*(2^d+r)^119 := by
    rw [pow_succ]
    ring
  rw [form] at bound
  exact ⟨initial,y,k,target,drop,Nat.lt_of_mul_lt_mul_left bound,kp,visit,basin⟩

/-- At the common source scales, the exponential saving coefficient controls
    a fixed positive power of the original source itself. -/
theorem source_exponential_scale {q h r d : Nat}
    (hit : orbit h r=1) (hH : h≤q/10)
    (left : q/10<d) (right : d≤12*q) :
    2^d+r≤(2^(q/10+1))^120 := by
  let H := q/10
  have remainder := Nat.mod_lt q (by decide : 0<10)
  have division := Nat.mod_add_div q 10
  have digits : d+1≤120*(H+1) := by dsimp [H]; omega
  have source : r≤2^H :=
    (certificate_source_bound hit).trans (Nat.pow_le_pow_right (by decide) hH)
  have small : r<2^d := source.trans_lt
    (Nat.pow_lt_pow_right (by decide) (by dsimp [H]; omega : H<d))
  calc
    2^d+r ≤ 2^d+2^d := Nat.add_le_add_left small.le _
    _ = 2^(d+1) := by rw [pow_succ]; ring
    _ ≤ 2^(120*(H+1)) := Nat.pow_le_pow_right (by decide) digits
    _ = (2^(H+1))^120 := by rw [← pow_mul]; congr 1; omega


/-- A growing certificate budget and an exponentially growing saving factor
    hold simultaneously on the same arbitrarily large exponent blocks. -/
theorem exponential_simultaneous_blocks (N : Nat) :
    ∃ q : Nat, N<q ∧ 100≤q ∧
      ∀ r h d : Nat, r%2=1 → h≤q/10 → orbit h r=1 →
        2*q+q/10+1≤d → d+q/10≤12*q → Success (2^(q/10+1)) r d := by
  obtain ⟨q,a,large,lower,upper⟩ :=
    arbitrarily_large_positive_approximants (N+100)
  have qlarge : 100≤q := by omega
  have saving : 2^(q/10+1)<3^q :=
    (Nat.pow_le_pow_right (by decide : 0<2) (by omega : q/10+1≤q)).trans_lt
      (Nat.pow_lt_pow_left (by decide : 2<3) (by omega : q≠0))
  refine ⟨q,by omega,qlarge,?_⟩
  apply simultaneous_block_of_coefficient (by omega) (Nat.div_le_self q 10)
    lower upper.le saving
  intro h p hH ph
  exact exponential_padded_coefficient qlarge ph hH

/-- The same common blocks have a fixed power saving in the original source:
    the actual smaller marked endpoint satisfies `y^120 < n^119`. -/
theorem power_saving_simultaneous_blocks (N : Nat) :
    ∃ q : Nat, N<q ∧ 100≤q ∧
      ∀ r h d : Nat, r%2=1 → h≤q/10 → orbit h r=1 →
        2*q+q/10+1≤d → d+q/10≤12*q → PowerSuccess r d := by
  obtain ⟨q,high,large,block⟩ := exponential_simultaneous_blocks N
  refine ⟨q,high,large,?_⟩
  intro r h d odd hH hit left right
  apply power_success_of_scale (C:=2^(q/10+1))
    (source_exponential_scale hit hH (by omega) (by omega))
  exact block r h d odd hH hit left right

/-- Unconditional coverage of whole multiplicatively long exponent blocks on
    the offset-one ray.  Every exponent in `[2q+1,12q]` is certified. -/
theorem power_plus_one_blocks (C N : Nat) :
    ∃ q : Nat, N<q ∧ ∀ d : Nat, 2*q+1≤d → d≤12*q → Success C 1 d := by
  obtain ⟨q,high,_large,block⟩ := arbitrarily_large_simultaneous_blocks C 0 N
  refine ⟨q,high,?_⟩
  intro d left right
  exact block 1 0 d (by decide) (by omega) rfl (by omega) (by omega)

/-- The entire offset-one block has the same fixed power saving, with no
    offset convergence hypothesis: its certificate is the zero-clock hit. -/
theorem power_plus_one_power_saving_blocks (N : Nat) :
    ∃ q : Nat, N<q ∧ ∀ d : Nat, 2*q+1≤d → d≤12*q → PowerSuccess 1 d := by
  obtain ⟨q,a,large,lower,upper⟩ :=
    arbitrarily_large_positive_approximants (N+100)
  have qlarge : 100≤q := by omega
  have saving : 2^(q/10+1)<3^q :=
    (Nat.pow_le_pow_right (by decide : 0<2) (by omega : q/10+1≤q)).trans_lt
      (Nat.pow_lt_pow_left (by decide : 2<3) (by omega : q≠0))
  have shared := simultaneous_block_of_coefficient (H:=0)
    (by omega : 0<q) (by omega : 0≤q) lower upper.le saving
    (by
      intro h p hH ph
      exact exponential_padded_coefficient qlarge ph (by omega))
  refine ⟨q,by omega,?_⟩
  intro d left right
  apply power_success_of_scale (C:=2^(q/10+1))
    (source_exponential_scale (h:=0) (r:=1) rfl (by omega)
      (by have := Nat.div_le_self q 10; omega) right)
  exact shared 1 0 d (by decide) (by omega) rfl (by omega) (by omega)

/-- Number of positive dyadic exponents at most `M` possessing the specified
    marked-return contraction.  The predicate is mathematical, not a claim
    that this noncomputable count is a total termination algorithm. -/
noncomputable def successCount (C M : Nat) : Nat := by
  classical
  exact ((Finset.Icc 1 M).filter (Success C 1)).card

/-- Number of positive exponents having the fixed power saving in the actual
    marked return process. This is a mathematical count, not an algorithm. -/
noncomputable def powerSuccessCount (M : Nat) : Nat := by
  classical
  exact ((Finset.Icc 1 M).filter (PowerSuccess 1)).card

/-- Exact finite inequalities witnessing upper natural density at least `5/6`
    among the dyadic exponents, for every fixed contraction factor.  This is
    not a density assertion about all positive integer starting values. -/
theorem power_plus_one_upper_density (C N : Nat) :
    ∃ M : Nat, N<M ∧ 5*M≤6*successCount C M := by
  classical
  obtain ⟨q,high,block⟩ := power_plus_one_blocks C N
  have qp : 0<q := by omega
  have cover : Finset.Icc (2*q+1) (12*q) ⊆
      (Finset.Icc 1 (12*q)).filter (Success C 1) := by
    intro d member
    obtain ⟨left,right⟩ := Finset.mem_Icc.mp member
    exact Finset.mem_filter.mpr ⟨Finset.mem_Icc.mpr ⟨by omega,right⟩,block d left right⟩
  have size := Finset.card_le_card cover
  have length : (Finset.Icc (2*q+1) (12*q)).card=10*q := by
    rw [Nat.card_Icc]
    omega
  rw [length] at size
  refine ⟨12*q,by omega,?_⟩
  change 5*(12*q)≤6*((Finset.Icc 1 (12*q)).filter (Success C 1)).card
  omega

/-- Exact upper-density witnesses for a uniform power saving. At least `5/6`
    of the exponents along arbitrarily large cutoffs have a positive actual
    marked return with `y^120 < (2^d+1)^119`. -/
theorem power_plus_one_power_saving_density (N : Nat) :
    ∃ M : Nat, N<M ∧ 5*M≤6*powerSuccessCount M := by
  classical
  obtain ⟨q,high,block⟩ := power_plus_one_power_saving_blocks N
  have cover : Finset.Icc (2*q+1) (12*q) ⊆
      (Finset.Icc 1 (12*q)).filter (PowerSuccess 1) := by
    intro d member
    obtain ⟨left,right⟩ := Finset.mem_Icc.mp member
    exact Finset.mem_filter.mpr ⟨Finset.mem_Icc.mpr ⟨by omega,right⟩,block d left right⟩
  have size := Finset.card_le_card cover
  have length : (Finset.Icc (2*q+1) (12*q)).card=10*q := by
    rw [Nat.card_Icc]
    omega
  rw [length] at size
  refine ⟨12*q,by omega,?_⟩
  change 5*(12*q)≤6*((Finset.Icc 1 (12*q)).filter (PowerSuccess 1)).card
  omega

#print axioms endpoint_marked_phase_window
#print axioms simultaneous_block_of_approximant
#print axioms arbitrarily_large_simultaneous_blocks
#print axioms growing_certificate_blocks
#print axioms exponential_padded_coefficient
#print axioms exponential_simultaneous_blocks
#print axioms power_saving_simultaneous_blocks
#print axioms power_plus_one_blocks
#print axioms power_plus_one_upper_density
#print axioms power_plus_one_power_saving_blocks
#print axioms power_plus_one_power_saving_density

end CollatzShell.ExponentCoverage
