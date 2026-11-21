import ShellCover
import Mathlib.Analysis.SpecialFunctions.Log.Base
import Mathlib.NumberTheory.DiophantineApproximation.Basic
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.Int.ModEq

/-! A forced narrow section of the actual forward Collatz orbit. -/

namespace CollatzShell.ForwardSection

open Real

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

private theorem orbit_odd {n : Nat} (hn : n%2=1) (j : Nat) : oddOrbit n j%2=1 := by
  cases j with
  | zero => exact hn
  | succ i => exact part_odd (by omega : 0<3*oddOrbit n i+1)

private theorem odd_step_hit {n : Nat} (hn : n%2=1) : Hits n (oddStep n) := by
  let a := twos (3*n+1)
  have eq : 2^a*oddStep n=3*n+1 := split_twos _
  have ho := part_odd (by omega : 0<3*n+1)
  change oddStep n%2=1 at ho
  cases ha : a with
  | zero => rw [ha,pow_zero,one_mul] at eq; omega
  | succ b =>
    rw [ha,show 2^(b+1)*oddStep n=2*(2^b*oddStep n) by ring] at eq
    have st : step n=2^b*oddStep n := by simp [step,hn]; omega
    exact ⟨b+1,by simp only [orbit,st,orbit_pad]⟩

theorem odd_orbit_hit {n : Nat} (hn : n%2=1) (j : Nat) : Hits n (oddOrbit n j) := by
  induction j with
  | zero => exact ⟨0,rfl⟩
  | succ j ih => exact ih.trans (odd_step_hit (orbit_odd hn j))

private theorem size_step {n : Nat} (hn : n%2=1) : oddStep n≤2*n := by
  have eq := split_twos (3*n+1)
  change 2^(twos (3*n+1))*oddStep n=3*n+1 at eq
  have odd := part_odd (by omega : 0<3*n+1)
  change oddStep n%2=1 at odd
  cases ha : twos (3*n+1) with
  | zero => rw [ha,pow_zero,one_mul] at eq; omega
  | succ a =>
    have ge : 2≤2^(a+1) := Nat.le_self_pow (by omega) 2
    have h := Nat.mul_le_mul_right (oddStep n) ge
    rw [ha] at eq; omega

private theorem size_orbit {n : Nat} (hn : n%2=1) (j : Nat) : oddOrbit n j≤2^j*n := by
  induction j with
  | zero => simp [oddOrbit]
  | succ j ih => exact (size_step (orbit_odd hn j)).trans (by rw [show 2^(j+1)*n=2*(2^j*n) by ring]; omega)

private noncomputable def alpha := logb 2 3
private noncomputable def height (n : Nat) := logb 2 n

private theorem log_two_bounds : 1/2 ≤ log 2 ∧ log 2 ≤ 1 := by
  constructor
  · have := one_sub_inv_le_log_of_pos (by norm_num : (0:ℝ)<2); linarith
  · have := log_le_sub_one_of_pos (by norm_num : (0:ℝ)<2); linarith

private theorem logb_two : logb 2 2=1 := by simp [logb,(log_pos (by norm_num : (1:ℝ)<2)).ne']

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

private theorem rotation_bounds : 1<alpha ∧ alpha<2 := by
  constructor
  · rw [← logb_two]; exact logb_lt_logb (by norm_num) (by norm_num) (by norm_num)
  · have h := logb_lt_logb (b:=2) (x:=3) (y:=2^2) (by norm_num) (by norm_num) (by norm_num)
    simpa [alpha,logb_pow,logb_two] using h

private theorem separated_logs {X Y K : Nat} (xp : 0<X) (lt : X<Y)
    (small : (K:ℝ)*|log Y-log X|≤1) : K≤Y := by
  have xr : (0:ℝ)<X := by exact_mod_cast xp
  have yr : (0:ℝ)<Y := by exact_mod_cast (by omega : 0<Y)
  have diff : (X:ℝ)+1≤Y := by exact_mod_cast lt
  have frac := one_sub_inv_le_log_of_pos (div_pos yr xr)
  rw [inv_div, log_div yr.ne' xr.ne'] at frac
  have gap : 1/(Y:ℝ)≤log Y-log X := by
    calc 1/(Y:ℝ) ≤ 1-(X:ℝ)/Y := by apply (le_sub_iff_add_le).mpr; rw [← add_div]; exact (div_le_one yr).mpr (by linarith)
         _ ≤ _ := frac
  have ma := mul_le_mul_of_nonneg_left gap (by positivity : 0≤(K:ℝ))
  have endpt : (K:ℝ)/Y≤1 := by
    rw [← mul_one_div]; exact ma.trans ((mul_le_mul_of_nonneg_left (le_abs_self _) (by positivity)).trans small)
  exact_mod_cast (div_le_one yr).mp endpt

/-- One rational grid supplies both the precision and a lower bound on the number of turns.
    Separation of the integer powers of two and three controls the grid denominator. -/
private theorem rotation_grid (N : Nat) (hN : 0<N) : ∃ a q : Nat,
    0<q ∧ q≤N ∧ a.Coprime q ∧ N+1≤4^q ∧ |q*alpha-a|≤1/((N:ℝ)+1) := by
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
  have aa : a≤2*q := by
    have h := mul_lt_mul_of_pos_left rotation_bounds.2 qr
    have val : (a:ℝ)<2*(q:ℝ)+1 := by rw [ar]; nlinarith
    exact Nat.le_of_lt_succ (by exact_mod_cast val)
  have ae : 0<a := by exact_mod_cast (show (0:ℤ)<a by rwa [ai])
  have distinct : (3:Nat)^q≠2^a := by
    have odd (k : Nat) : 3^k%2=1 := by induction k with | zero => rfl | succ k ih => rw [pow_succ]; omega
    obtain ⟨b,ab⟩ := Nat.exists_eq_succ_of_ne_zero ae.ne'
    rw [ab,pow_succ]; have := odd q; omega
  have magnitude : ((N+1:Nat):ℝ)*|log ((3^q:Nat):ℝ)-log ((2^a:Nat):ℝ)|≤1 := by
    have L : 0<log 2 := log_pos (by norm_num)
    have id : log ((3^q:Nat):ℝ)-log ((2^a:Nat):ℝ)=(q*alpha-r.num)*log 2 := by
      push_cast; rw [log_pow,log_pow,← ar]; unfold alpha logb; field_simp
    rw [id,abs_mul,abs_of_pos L,Nat.cast_add,Nat.cast_one,← mul_assoc]
    have u := (le_div_iff₀ nr).mp err
    have w : ((N:ℝ)+1)*|q*alpha-r.num|≤1 := by linarith [mul_comm ((N:ℝ)+1) |q*alpha-r.num|]
    exact (mul_le_mul_of_nonneg_right w L.le).trans (by simpa using log_two_bounds.2)
  have sep : N+1≤4^q := by
    rcases lt_or_gt_of_ne distinct with h | h
    · have h' : ((N+1:Nat):ℝ)*|log ((2^a:Nat):ℝ)-log ((3^q:Nat):ℝ)|≤1 := by rwa [abs_sub_comm]
      have le := separated_logs (K:=N+1) (by positivity) h h'
      exact le.trans (by simpa only [pow_mul,show (2:Nat)^2=4 by decide] using (Nat.pow_le_pow_right (by decide : 0<2) aa))
    · exact (separated_logs (by positivity) h magnitude).trans (Nat.pow_le_pow_left (by decide) _)
  exact ⟨a,q,qpos,den,r.reduced,sep,by rwa [ar]⟩

private theorem grid_point {a q : Nat} (qp : 0<q) (cop : a.Coprime q) (y : ℝ) :
    ∃ j : Nat, j<q ∧ ∃ z : ℤ,
      1≤q*(y+j*((a:ℝ)/q)-z) ∧ q*(y+j*((a:ℝ)/q)-z)≤2 := by
  let F := ⌊(q:ℝ)*y⌋
  let R := 1-F
  obtain ⟨u,hu⟩ := Int.mod_coprime cop
  let J := (u*R)%(q:ℤ)
  have qz : (0:ℤ)<q := by exact_mod_cast qp
  have jl : 0≤J := Int.emod_nonneg _ qz.ne'
  have ju : J<q := Int.emod_lt_of_pos _ qz
  let j := J.toNat
  have je : (j:ℤ)=J := Int.toNat_of_nonneg jl
  have modj : (a:ℤ)*j ≡ R [ZMOD ↑q] := by
    rw [je]
    calc (a:ℤ)*J ≡ a*(u*R) [ZMOD ↑q] := (Int.mod_modEq _ _).mul_left _
         _ ≡ R [ZMOD ↑q] := by simpa [mul_assoc] using hu.mul_right R
  obtain ⟨z,hz⟩ := Int.modEq_iff_dvd.mp modj.symm
  have eq : (a:ℝ)*j-(1-(F:ℝ))=q*(z:ℝ) := by exact_mod_cast hz
  have fl : (F:ℝ)≤q*y := Int.floor_le _
  have fu : (q:ℝ)*y<F+1 := Int.lt_floor_add_one _
  have qr : (q:ℝ)≠0 := by positivity
  have alg : (q:ℝ)*(y+j*((a:ℝ)/q)-z)=q*y+(a:ℝ)*j-q*z := by field_simp
  exact ⟨j,by exact_mod_cast (je.trans_lt ju),z,by rw [alg]; linarith,by rw [alg]; linarith⟩

/-- On one ordinary forward orbit, a drop or a visit to any prescribed leading phase
    occurs within the indicated odd-step budget. The target may depend on the source. -/
theorem steer (n : Nat) (hn : n%2=1) (theta : ℝ) :
    ∃ j<n.sqrt, 4*oddOrbit n j<n ∨ ∃ z : ℤ,
      0≤logb 2 (oddOrbit n j)-(theta+z) ∧
      ((oddOrbit n j).log2+1:ℝ)*(logb 2 (oddOrbit n j)-(theta+z))≤35 := by
  have np : 0<n := by omega
  let N := n.sqrt
  obtain ⟨a,q,qp,qn,cop,sep,approx⟩ := rotation_grid N (Nat.sqrt_pos.mpr np)
  let m := (n+3)/4
  have mp : 0<m := by dsimp [m]; omega
  have nm : n≤4*m := by dsimp [m]; omega
  by_cases floor : ∀ i<q, n≤4*oddOrbit n i
  · obtain ⟨j,jq,z,gl,gu⟩ := grid_point qp cop (height n-theta)
    obtain ⟨A,e,el,eu,eq⟩ := phase_orbit np mp j (fun i hi => by have := floor i (by omega); dsimp [m]; omega)
    let x := oddOrbit n j
    have qr : (0:ℝ)<q := by exact_mod_cast qp
    have jr : (0:ℝ)≤j := by positivity
    have mr : (0:ℝ)<m := by exact_mod_cast mp
    have qsq : q*q≤n := (Nat.mul_le_mul qn qn).trans (Nat.sqrt_le n)
    have elt : (q:ℝ)*e≤4 := by
      calc (q:ℝ)*e ≤ q*(j/m) := mul_le_mul_of_nonneg_left eu qr.le
           _ = (q*j)/m := by ring
           _ ≤ 4 := (div_le_iff₀ mr).mpr (by exact_mod_cast (Nat.mul_le_mul_left q jq.le).trans (qsq.trans nm))
    have al : |(j:ℝ)*(q*alpha-a)|≤1 := by
      rw [abs_mul,abs_of_nonneg jr]
      calc (j:ℝ)*|q*alpha-a| ≤ j*(1/((N:ℝ)+1)) := mul_le_mul_of_nonneg_left approx jr
           _ = j/((N:ℝ)+1) := by ring
           _ ≤ 1 := (div_le_one (by positivity)).mpr (by exact_mod_cast (by omega : j≤N+1))
    have algebra : (q:ℝ)*(height x-(theta+((z-(A:ℤ):ℤ):ℝ))) =
        q*((height n-theta)+j*((a:ℝ)/q)-z)+j*(q*alpha-a)+q*e := by
      dsimp only [x]; rw [eq]; push_cast; field_simp; ring
    have lo : 0≤height x-(theta+((z-(A:ℤ):ℤ):ℝ)) := by
      apply nonneg_of_mul_nonneg_right (a:= (q:ℝ)) _ qr
      rw [algebra]; linarith [(abs_le.mp al).1,mul_nonneg qr.le el]
    have hi : (q:ℝ)*(height x-(theta+((z-(A:ℤ):ℤ):ℝ)))≤7 := by rw [algebra]; linarith [(abs_le.mp al).2]
    have boundN : n<2^(4*q) := by
      calc n < (N+1)*(N+1) := Nat.lt_succ_sqrt n
           _ ≤ 4^q*4^q := Nat.mul_le_mul sep sep
           _ = 2^(4*q) := by rw [show 4*q=2*q+2*q by omega,pow_add,pow_mul]; norm_num
    have powx : x<2^(5*q) := by
      calc x ≤ 2^j*n := size_orbit hn j
           _ < 2^j*2^(4*q) := Nat.mul_lt_mul_of_pos_left boundN (by positivity)
           _ ≤ 2^(5*q) := by rw [← pow_add]; apply Nat.pow_le_pow_right (by decide); omega
    have dl := (Nat.log2_lt (orbit_pos np j).ne').mpr powx
    change x.log2<5*q at dl
    have du : (x.log2:ℝ)+1≤5*q := by exact_mod_cast (show x.log2+1≤5*q by omega)
    refine ⟨j,jq.trans_le qn,Or.inr ⟨z-(A:ℤ),lo,?_⟩⟩
    calc _ ≤ (5*q)*(height x-(theta+((z-(A:ℤ):ℤ):ℝ))) := mul_le_mul_of_nonneg_right du lo
         _ ≤ 35 := by linarith [mul_assoc (5:ℝ) (q:ℝ) (height x-(theta+((z-(A:ℤ):ℤ):ℝ)))]
  · push Not at floor
    obtain ⟨j,jq,drop⟩ := floor
    exact ⟨j,jq.trans_le qn,Or.inl drop⟩

/-- An integer test involving only the length and leading digits of its argument. -/
def InSection (x : Nat) : Prop :=
  (x.log2+1)*(x-2^x.log2) ≤ 70*2^x.log2

instance (x : Nat) : Decidable (InSection x) := inferInstanceAs (Decidable (_ ≤ _))

private theorem section_of_phase {x : Nat} (xp : 0<x) {z : ℤ}
    (lo : 0≤height x-z) (close : ((x.log2:ℝ)+1)*(height x-z)≤35) : InSection x := by
  let d := x.log2
  let P := 2^d
  have pl : P≤x := Nat.log2_self_le xp.ne'
  have xu : x<2*P := by simpa [P,d,pow_succ,Nat.mul_comm] using (Nat.lt_log2_self (n:=x))
  have pr : (0:ℝ)<P := by dsimp [P]; positivity
  have xr : (0:ℝ)<x := by exact_mod_cast xp
  have hp2 : logb 2 (P:ℝ)=(d:ℝ) := by dsimp [P]; push_cast; rw [logb_pow,logb_two,mul_one]
  have hhi : height x < (d:ℝ)+1 := by
    have u : (x:ℝ)<2*(P:ℝ) := by exact_mod_cast xu
    have h := logb_lt_logb (by norm_num : (1:ℝ)<2) xr u
    rw [logb_mul (by norm_num) pr.ne',logb_two,hp2] at h
    dsimp only [height]; linarith
  have zd : z≤(d:ℤ) := by
    have hr : (z:ℝ)<(d:ℝ)+1 := by linarith
    have zi : z<(d:ℤ)+1 := by exact_mod_cast hr
    omega
  have zd' : (z:ℝ)≤d := by exact_mod_cast zd
  have dd : (d:ℝ)+1≥0 := by positivity
  have upper : ((d:ℝ)+1)*(height x-d)≤35 := (mul_le_mul_of_nonneg_left (by linarith) dd).trans close
  have frac := one_sub_inv_le_log_of_pos (div_pos xr pr)
  rw [inv_div, log_div xr.ne' pr.ne'] at frac
  have lp : 0<log 2 := log_pos (by norm_num)
  have H : log x-log P = (height x-d)*log 2 := by
    change log (P:ℝ)/log 2=(d:ℝ) at hp2
    unfold height logb; field_simp at hp2 ⊢; linarith
  have hd : 0≤height x-d := by exact sub_nonneg.mpr (by exact Real.log2_le_logb x)
  have diff : (x:ℝ)-P ≤ x*(height x-d) := by
    have estimate : 1-(P:ℝ)/x ≤ height x-d := by
      rw [H] at frac
      exact frac.trans (by simpa using mul_le_mul_of_nonneg_left log_two_bounds.2 hd)
    have h := mul_le_mul_of_nonneg_left estimate xr.le
    rwa [mul_sub,mul_one,mul_div_cancel₀ _ xr.ne'] at h
  unfold InSection
  have cap : ((d:ℝ)+1)*((x:ℝ)-P) ≤ 70*(P:ℝ) := by
    calc _ ≤ ((d:ℝ)+1)*(x*(height x-d)) := mul_le_mul_of_nonneg_left diff dd
         _ = x*(((d:ℝ)+1)*(height x-d)) := by ring
         _ ≤ x*35 := mul_le_mul_of_nonneg_left upper xr.le
         _ ≤ _ := by
           have u : (x:ℝ)<2*(P:ℝ) := by exact_mod_cast xu
           linarith
  exact_mod_cast (by simpa only [Nat.cast_sub pl] using cap : ((d:ℝ)+1)*((x-P:Nat):ℝ)≤70*P)

/-- A finite positive computation always produces either descent or a section hit. -/
theorem descent_or_section (n : Nat) (hn : n%2=1) :
    ∃ j<n.sqrt, 4*oddOrbit n j<n ∨ InSection (oddOrbit n j) := by
  obtain ⟨j,bound,drop | ⟨z,lo,hi⟩⟩ := steer n hn 0
  · exact ⟨j,bound,Or.inl drop⟩
  · exact ⟨j,bound,Or.inr (section_of_phase (orbit_pos (by omega) j) (by simpa [height] using lo) (by simpa [height] using hi))⟩

/-- Every individual positive forward orbit visits the section. -/
theorem hits_section (n : Nat) (hn : 0<n) : ∃ x, 0<x ∧ InSection x ∧ Hits n x := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases even : n%2=0
    · obtain ⟨x,xp,sec,hit⟩ := ih (n/2) (by omega) (by omega)
      exact ⟨x,xp,sec,Hits.trans (y:=n/2) ⟨1,by simp [orbit,step,even]⟩ hit⟩
    have odd : n%2=1 := by omega
    obtain ⟨j,_,drop | sec⟩ := descent_or_section n odd
    · obtain ⟨x,xp,sec,hit⟩ := ih (oddOrbit n j) (by omega) (orbit_pos hn j)
      exact ⟨x,xp,sec,(odd_orbit_hit odd j).trans hit⟩
    · exact ⟨_,orbit_pos hn j,sec,odd_orbit_hit odd j⟩

theorem collatz_iff_section : Universal ↔ ∀ n, 0<n → InSection n → Basin n := by
  constructor
  · exact fun all n hp _ => all n hp
  · intro cover n hn
    obtain ⟨x,xp,sec,hit⟩ := hits_section n hn
    exact hit.trans (cover x xp sec)

end CollatzShell.ForwardSection
