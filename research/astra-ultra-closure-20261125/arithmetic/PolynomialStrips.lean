import PhysicalEcho
import Mathlib.Analysis.SpecialFunctions.Log.Base
import Mathlib.NumberTheory.DiophantineApproximation.Basic
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.Int.ModEq

/-!
The odd-map logarithmic identity and reduced Dirichlet witness below are adapted
from PR 173 at fa0c9e2a2851e6324391e39c17afcb5913185aec, ForwardSection.lean.
The full-block permutation and its perturbation estimates are proved here.
-/
namespace Collatz.PolynomialStrips
open Real
set_option autoImplicit false

def twos (n : Nat) := n.factorization 2
def oddPart (n : Nat) := n / 2^(twos n)

private theorem split_twos (n : Nat) : 2^(twos n)*oddPart n=n := Nat.ordProj_mul_ordCompl_eq_self n 2
private theorem part_pos {n : Nat} (hn : 0<n) : 0<oddPart n := Nat.ordCompl_pos 2 hn.ne'
private theorem part_odd {n : Nat} (hn : 0<n) : oddPart n%2=1 := by
  have h : ¬ 2∣oddPart n := Nat.not_dvd_ordCompl Nat.prime_two hn.ne'
  omega

/-- One odd-only step, with the powers of two removed. -/
def oddStep (n : Nat) := oddPart (3*n+1)

def oddOrbit (n : Nat) : Nat → Nat
  | 0 => n
  | j+1 => oddStep (oddOrbit n j)

private theorem orbit_pos {n : Nat} (hn : 0<n) (j : Nat) : 0<oddOrbit n j := by
  cases j with
  | zero => exact hn
  | succ i => exact part_pos (by omega : 0<3*oddOrbit n i+1)

noncomputable def alpha := logb 2 3
noncomputable def height (n : Nat) := logb 2 n

theorem log_two_bounds : 1/2 ≤ log 2 ∧ log 2 ≤ 1 := by
  constructor
  · have := one_sub_inv_le_log_of_pos (by norm_num : (0:ℝ)<2); linarith
  · have := log_le_sub_one_of_pos (by norm_num : (0:ℝ)<2); linarith

theorem logb_two : logb 2 2=1 := by simp [logb,(log_pos (by norm_num : (1:ℝ)<2)).ne']

private theorem phase_step (x : Nat) (hx : 0<x) :
    ∃ e : ℝ, 0≤e ∧ e≤1/(x:ℝ) ∧
      height (oddStep x) = height x+alpha-(twos (3*x+1):ℝ)+e := by
  have xp : (0:ℝ)<x := by exact_mod_cast hx
  let d : ℝ := 1/(3*(x:ℝ))
  have dp : 0<d := by dsimp [d]; positivity
  let e := logb 2 (1+d)
  have ep : 0≤e := logb_nonneg (by norm_num) (by linarith)
  have small : e≤1/(x:ℝ) := by
    change log (1+d)/log 2 ≤ _
    apply (div_le_iff₀ (log_pos (by norm_num))).mpr
    have up := log_le_sub_one_of_pos (show 0<1+d by linarith)
    have dl : d*x=1/3 := by dsimp [d]; field_simp
    rw [show 1/(x:ℝ)*log 2=log 2/x by ring]
    apply (le_div_iff₀ xp).mpr
    nlinarith [mul_le_mul_of_nonneg_right up xp.le,log_two_bounds.1]
  have num : (2:ℝ)^(twos (3*x+1))*(oddStep x:ℝ)= (3*x)*(1+d) := by
    have h : (2:ℝ)^(twos (3*x+1))*(oddStep x:ℝ)=3*(x:ℝ)+1 := by exact_mod_cast split_twos (3*x+1)
    rw [h]; dsimp [d]; field_simp
  have base := congrArg (logb 2) num
  have op : 0<oddStep x := part_pos (by omega : 0<3*x+1)
  have op' : (oddStep x:ℝ)≠0 := by positivity
  simp only [logb_mul (by positivity : (2:ℝ)^twos (3*x+1)≠0) op',logb_pow,logb_two,mul_one,
    logb_mul (by positivity : 3*(x:ℝ)≠0) (by linarith : 1+d≠0),logb_mul (by norm_num : (3:ℝ)≠0) xp.ne'] at base
  refine ⟨e,ep,small,?_⟩
  dsimp only [height,alpha,e] at *; linarith

/-- The accumulated phase error is one-sided and is controlled by the actual floor. -/
private theorem phase_orbit {n m : Nat} (hn : 0<n) (hm : 0<m) (j : Nat)
    (floor : ∀ i<j, m≤oddOrbit n i) : ∃ (A : Nat) (e : ℝ), 0≤e ∧ e≤j/(m:ℝ) ∧
      height (oddOrbit n j)=height n+j*alpha-(A:ℝ)+e := by
  induction j with
  | zero => exact ⟨0,0,by simp [oddOrbit]⟩
  | succ j ih =>
    obtain ⟨a,e,el,eu,eq⟩ := ih (fun i hi => floor i (by omega))
    obtain ⟨d,dl,du,step⟩ := phase_step _ (orbit_pos hn j)
    have comp : (1:ℝ)/oddOrbit n j≤1/m := one_div_le_one_div_of_le (by exact_mod_cast hm) (by exact_mod_cast floor j (by omega))
    refine ⟨a+twos (3*oddOrbit n j+1),e+d,by linarith,?_,?_⟩
    · push_cast; rw [add_div]; linarith
    · change height (oddStep (oddOrbit n j))=_
      rw [step,eq]; push_cast; ring

theorem rotation_bounds : 1<alpha ∧ alpha<2 := by
  constructor
  · rw [← logb_two]; exact logb_lt_logb (by norm_num) (by norm_num) (by norm_num)
  · have h := logb_lt_logb (b:=2) (x:=3) (y:=2^2) (by norm_num) (by norm_num) (by norm_num)
    simpa [alpha,logb_pow,logb_two] using h

theorem rotation_grid (N : Nat) (hN : 0<N) : ∃ a q : Nat,
    0<q ∧ q≤N ∧ a.Coprime q ∧ |q*alpha-a|≤1/((N:ℝ)+1) := by
  obtain ⟨r,approx,den⟩ := exists_rat_abs_sub_le_and_den_le alpha hN
  let q := r.den
  have qpos : 0<q := r.pos
  have qr : (0:ℝ)<q := by exact_mod_cast qpos
  have nr : (0:ℝ)<N+1 := by positivity
  have err : |(q:ℝ)*alpha-(r.num:ℝ)|≤1/((N:ℝ)+1) := by
    rw [Rat.cast_def] at approx
    change |alpha-(r.num:ℝ)/q| ≤ 1/(((N:ℝ)+1)*q) at approx
    rw [show (q:ℝ)*alpha-r.num=q*(alpha-r.num/q) by field_simp,abs_mul,abs_of_pos qr]
    calc _ ≤ q*(1/(((N:ℝ)+1)*q)) := mul_le_mul_of_nonneg_left approx qr.le
         _ = _ := by field_simp
  have lt1 : 1/((N:ℝ)+1)<1 := (div_lt_one nr).mpr (by exact_mod_cast (by omega : 1<N+1))
  have lo := (abs_le.mp err).1
  have hi := (abs_le.mp err).2
  have ap : 0<r.num := by
    have qone : (1:ℝ)≤q := by exact_mod_cast qpos
    have z := mul_lt_mul_of_pos_left rotation_bounds.1 qr
    exact_mod_cast (show (0:ℝ)<r.num by nlinarith)
  let a := r.num.natAbs
  have ai : (a:ℤ)=r.num := by rw [show (a:ℤ)=|r.num| from Int.natCast_natAbs _,abs_of_pos ap]
  have ar : (a:ℝ)=(r.num:ℝ) := by exact_mod_cast ai
  have near : |q*alpha-a|≤1/((N:ℝ)+1) := by rwa [ar]
  exact ⟨a,q,qpos,den,r.reduced,near⟩



private theorem match_index {a q : ℕ} (qp : 0<q) (cop : a.Coprime q)
    (b : ℤ) (r : Fin q) :
    ∃ j : Fin q, ∃ z : ℤ, (a:ℤ)*(j.val:ℤ) + b = (r.val:ℤ)+1+q*z := by
  obtain ⟨u,hu⟩ := Int.mod_coprime cop
  let R : ℤ := r.val+1-b
  let J := (u*R)%(q:ℤ)
  have qz : (0:ℤ)<q := by exact_mod_cast qp
  have jl : 0≤J := Int.emod_nonneg _ qz.ne'
  have ju : J<q := Int.emod_lt_of_pos _ qz
  have je : (J.toNat:ℤ)=J := Int.toNat_of_nonneg jl
  let j : Fin q := ⟨J.toNat,by exact_mod_cast (je.trans_lt ju)⟩
  have modj : (a:ℤ)*j.val ≡ R [ZMOD ↑q] := by
    change (a:ℤ)*J.toNat ≡ R [ZMOD ↑q]
    rw [je]
    calc (a:ℤ)*J ≡ a*(u*R) [ZMOD ↑q] := (Int.mod_modEq _ _).mul_left _
         _ ≡ R [ZMOD ↑q] := by simpa [mul_assoc] using hu.mul_right R
  obtain ⟨z,hz⟩ := Int.modEq_iff_dvd.mp modj.symm
  exact ⟨j,z,by dsimp [R] at hz; omega⟩

/-- A whole ordinary orbit block matches the rational rotation grid, with
different grid points assigned different observation times. The floor is
imposed only on the actual block used. -/
theorem phase_permutation {n m N a q : ℕ} (hn : 0<n) (hm : 0<m)
    (qp : 0<q) (qn : q≤N) (cop : a.Coprime q)
    (near : |(q:ℝ)*alpha-a|≤1/((N:ℝ)+1))
    (floor : ∀ i<q, m≤oddOrbit n i) (θ : ℝ) :
    ∃ f : Fin q → Fin q, Function.Injective f ∧ ∀ r, ∃ z : ℤ,
      0 ≤ height (oddOrbit n (f r).val) - (θ + z + (r.val:ℝ)/q) ∧
      height (oddOrbit n (f r).val) - (θ + z + (r.val:ℝ)/q) ≤ 3/(q:ℝ)+q/m := by
  let y := height n - θ
  let b := ⌊(q:ℝ)*y⌋
  choose f z grid using match_index qp cop b
  have inj : Function.Injective f := by
    intro r s eqn
    have h₁ := grid r
    have h₂ := grid s
    rw [eqn] at h₁
    have modq : (r.val:ℤ) ≡ (s.val:ℤ) [ZMOD ↑q] := by
      apply Int.modEq_iff_dvd.mpr
      exact ⟨z r-z s,by linear_combination h₁-h₂⟩
    have rr : (r.val:ℤ) % q = r.val := Int.emod_eq_of_lt (by positivity) (by exact_mod_cast r.isLt)
    have ss : (s.val:ℤ) % q = s.val := Int.emod_eq_of_lt (by positivity) (by exact_mod_cast s.isLt)
    apply Fin.ext
    change (r.val:ℤ)%q = (s.val:ℤ)%q at modq
    exact_mod_cast (rr.symm.trans (modq.trans ss))
  refine ⟨f,inj,?_⟩
  intro r
  let j := (f r).val
  have jq : j < q := (f r).isLt
  have qr : (0:ℝ)<q := by exact_mod_cast qp
  have mr : (0:ℝ)<m := by exact_mod_cast hm
  have jr : (0:ℝ)≤j := by positivity
  obtain ⟨A,e,el,eu,phase⟩ := phase_orbit hn hm j (fun i hi => floor i (hi.trans jq))
  have eg : ((a:ℝ)*j + (b:ℝ)) = (r.val:ℝ)+1+q*(z r:ℝ) := by exact_mod_cast grid r
  have b₁ : (b:ℝ) ≤ q*y := Int.floor_le _
  have b₂ : (q:ℝ)*y < b+1 := Int.lt_floor_add_one _
  have ae : |(j:ℝ)*(q*alpha-a)|≤1 := by
    rw [abs_mul,abs_of_nonneg jr]
    calc (j:ℝ)*|q*alpha-a| ≤ j*(1/((N:ℝ)+1)) := mul_le_mul_of_nonneg_left near jr
         _ = j/((N:ℝ)+1) := by ring
         _ ≤ 1 := (div_le_one (by positivity)).mpr (by exact_mod_cast (by omega : j≤N+1))
  have eu' : e ≤ (q:ℝ)/m := eu.trans (div_le_div_of_nonneg_right (by exact_mod_cast jq.le) mr.le)
  have identity : (q:ℝ)*(height (oddOrbit n j)-(θ+((z r-(A:ℤ):ℤ):ℝ)+(r.val:ℝ)/q)) =
        (q*y-(b:ℝ)+1) + j*(q*alpha-a) + q*e := by
    rw [phase]; dsimp only [y] at *; push_cast
    field_simp
    linear_combination eg
  refine ⟨z r-(A:ℤ),?_,?_⟩
  · apply nonneg_of_mul_nonneg_right (a:=(q:ℝ)) _ qr
    rw [identity]
    linarith [(abs_le.mp ae).1,mul_nonneg qr.le el]
  · change height (oddOrbit n j)-(θ+((z r-(A:ℤ):ℤ):ℝ)+(r.val:ℝ)/q) ≤ _
    apply le_of_mul_le_mul_left (a:=(q:ℝ)) _ qr
    rw [identity,mul_add,show (q:ℝ)*(3/q)=3 by field_simp]
    linarith [(abs_le.mp ae).2,mul_le_mul_of_nonneg_left eu' qr.le]

/-- A denominator chosen before the starting phase works for every rotation
of the grid. A premature exit supplies an actual dropped ordinary iterate. -/
theorem drop_or_grid {m n N : ℕ} (hm : 0<m) (hn : 0<n) (hN : 0<N) :
    ∃ a q : ℕ, 0<q ∧ q≤N ∧ a.Coprime q ∧ |(q:ℝ)*alpha-a|≤1/((N:ℝ)+1) ∧
    ((∃ i<q, oddOrbit n i<m) ∨ ∀ θ : ℝ, ∃ f : Fin q → Fin q,
      Function.Injective f ∧ ∀ r, ∃ z : ℤ,
        0 ≤ height (oddOrbit n (f r).val) - (θ + z + (r.val:ℝ)/q) ∧
        height (oddOrbit n (f r).val) - (θ + z + (r.val:ℝ)/q) ≤ 3/(q:ℝ)+q/m) := by
  obtain ⟨a,q,qp,qn,cop,near⟩ := rotation_grid N hN
  refine ⟨a,q,qp,qn,cop,near,?_⟩
  by_cases fl : ∀ i<q, m≤oddOrbit n i
  · exact Or.inr (phase_permutation hn hm qp qn cop near fl)
  · push Not at fl
    exact Or.inl fl

private theorem orbit_odd {n : ℕ} (hn : n%2=1) (j : ℕ) : oddOrbit n j%2=1 := by
  cases j with
  | zero => exact hn
  | succ j => exact part_odd (by omega : 0<3*oddOrbit n j+1)

private theorem strip_twos (a x : ℕ) : PhysicalEcho.orbit a (2^a*x)=x := by
  induction a with
  | zero => simp [PhysicalEcho.orbit]
  | succ a ih =>
    rw [pow_succ',Nat.mul_assoc,PhysicalEcho.orbit]
    simpa [PhysicalEcho.step] using ih

private theorem actual_odd_step {x : ℕ} (hx : x%2=1) :
    PhysicalEcho.orbit (twos (3*x+1)) x=oddStep x := by
  let a := twos (3*x+1)
  have eq : 2^a*oddStep x=3*x+1 := split_twos _
  have ho := part_odd (by omega : 0<3*x+1)
  change oddStep x%2=1 at ho
  cases ha : a with
  | zero => rw [ha,pow_zero,one_mul] at eq; omega
  | succ b =>
    rw [ha,show 2^(b+1)*oddStep x=2*(2^b*oddStep x) by ring] at eq
    have step : PhysicalEcho.step x=2^b*oddStep x := by simp [PhysicalEcho.step,hx]; omega
    change PhysicalEcho.orbit a x=oddStep x
    rw [ha,PhysicalEcho.orbit,step,strip_twos]

def clock (n : ℕ) : ℕ → ℕ
  | 0 => 0
  | j+1 => clock n j + twos (3*oddOrbit n j+1)

/-- Attachment to the same positive shortcut map as the other modules. -/
theorem actual_odd_orbit {n : ℕ} (odd : n%2=1) (j : ℕ) :
    PhysicalEcho.orbit (clock n j) n=oddOrbit n j := by
  induction j with
  | zero => rfl
  | succ j ih => rw [clock,PhysicalEcho.orbit_add,ih]; exact actual_odd_step (orbit_odd odd j)

/-- The powered bounds use a finite lower-denominator statement for the
chosen search scale. The analytic theorem supplying such bounds is external. -/
theorem polynomial_grid_physical {n m t s h C : ℕ} (odd : n%2=1) (ht : 0<t)
    (floorSize : t^(s+h)≤m)
    (separation : ∀ a q : ℕ, 0<q → q≤t^s → a.Coprime q →
      |(q:ℝ)*alpha-a|≤1/(((t^s:ℕ):ℝ) + 1) → t^h≤C*q) :
    ∃ q : ℕ, 0<q ∧ q≤t^s ∧ t^h≤C*q ∧
    ((∃ i<q, PhysicalEcho.orbit (clock n i) n<m) ∨ ∀ θ : ℝ,
      ∃ f : Fin q → Fin q, Function.Injective f ∧ ∀ r, ∃ z : ℤ,
      0 ≤ height (PhysicalEcho.orbit (clock n (f r).val) n)-(θ+z+(r.val:ℝ)/q) ∧
      height (PhysicalEcho.orbit (clock n (f r).val) n)-(θ+z+(r.val:ℝ)/q)
        ≤ ((3:ℝ)*C+1)/(t^h:ℕ)) := by
  have hp : 0<n := by omega
  have hm : 0<m := lt_of_lt_of_le (Nat.pow_pos ht) floorSize
  obtain ⟨a,q,qp,qn,cop,near,drop | covered⟩ := drop_or_grid hm hp (Nat.pow_pos ht (n:=s))
  · exact ⟨q,qp,qn,separation a q qp qn cop near,Or.inl (by simpa only [actual_odd_orbit odd] using drop)⟩
  · have bound := separation a q qp qn cop near
    refine ⟨q,qp,qn,bound,Or.inr ?_⟩
    intro θ
    obtain ⟨f,inj,grid⟩ := covered θ
    refine ⟨f,inj,?_⟩
    intro r
    obtain ⟨z,lower,upper⟩ := grid r
    rw [actual_odd_orbit odd]
    refine ⟨z,lower,upper.trans ?_⟩
    have qr : (0:ℝ)<q := by exact_mod_cast qp
    have mr : (0:ℝ)<m := by exact_mod_cast hm
    have hr : (0:ℝ)<(t^h:ℕ) := by exact_mod_cast Nat.pow_pos ht
    have lowerQ : ((t^h:ℕ):ℝ)≤C*(q:ℝ) := by exact_mod_cast bound
    have upperQ : (q:ℝ)*(t^h:ℕ)≤m := by
      exact_mod_cast (Nat.mul_le_mul_right (t^h) qn).trans ((Nat.pow_add t s h).ge.trans floorSize)
    have one : (q:ℝ)/m ≤ 1/(t^h:ℕ) :=
      (div_le_div_iff₀ mr hr).mpr (by simpa using upperQ)
    have three : (3:ℝ)/q ≤ (3*C)/(t^h:ℕ) :=
      (div_le_div_iff₀ qr hr).mpr (by linarith)
    rw [add_div]
    exact add_le_add three one

/-- Identical literal gap words preserve the entire affine carry. -/
private theorem common_affine (x y k : ℕ)
    (same : ∀ i<k, twos (3*oddOrbit x i+1)=twos (3*oddOrbit y i+1)) :
    ∃ C : ℕ, 2^(clock x k)*oddOrbit x k=3^k*x+C ∧
      2^(clock x k)*oddOrbit y k=3^k*y+C := by
  induction k with
  | zero => exact ⟨0,by simp [clock,oddOrbit],by simp [clock,oddOrbit]⟩
  | succ k ih =>
    obtain ⟨C,hx,hy⟩ := ih (fun i hi => same i (by omega))
    have one (z : ℕ) (h : twos (3*oddOrbit x k+1)=twos (3*oddOrbit z k+1))
        (hz : 2^(clock x k)*oddOrbit z k=3^k*z+C) :
        2^(clock x (k+1))*oddOrbit z (k+1)=3^(k+1)*z+(3*C+2^(clock x k)) := by
      calc
        _ = 2^(clock x k)*(2^(twos (3*oddOrbit z k+1))*oddStep (oddOrbit z k)) := by
          rw [clock,pow_add,h,oddOrbit,Nat.mul_assoc]
        _ = 2^(clock x k)*(3*oddOrbit z k+1) := by rw [oddStep,split_twos]
        _ = 3*(2^(clock x k)*oddOrbit z k)+2^(clock x k) := by ring
        _ = _ := by rw [hz,pow_succ]; ring
    exact ⟨_,one x rfl hx,one y (same k (by omega)) hy⟩

/-- In a terminal interval shorter than 3^k, one clock word gives at most
one distinct integer endpoint, even if its input contains a wrapped lap. -/
theorem band_terminal_unique {x y k : ℕ}
    (same : ∀ i<k, twos (3*oddOrbit x i+1)=twos (3*oddOrbit y i+1))
    (small : |(oddOrbit y k:ℤ)-(oddOrbit x k:ℤ)| < (3:ℤ)^k) :
    oddOrbit x k=oddOrbit y k := by
  obtain ⟨C,hx,hy⟩ := common_affine x y k same
  have eqn : 2^(clock x k)*oddOrbit x k ≡ 2^(clock x k)*oddOrbit y k [MOD 3^k] := by
    rw [hx,hy]
    simp [Nat.ModEq, Nat.add_mod]
  have cop : Nat.Coprime (3^k) (2^(clock x k)) :=
    ((by decide : Nat.Coprime 3 2).pow_left k).pow_right _
  exact (Nat.ModEq.cancel_left_of_coprime cop eqn).eq_of_abs_lt (by exact_mod_cast small)

#print axioms band_terminal_unique
#print axioms phase_permutation
#print axioms drop_or_grid
#print axioms actual_odd_orbit
#print axioms polynomial_grid_physical
end Collatz.PolynomialStrips
