import SectionDynamics

/-! Increasing first returns to the narrowing dyadic section. -/

namespace CollatzShell.ForwardSection

open Real

/-- The high bits give a small buffer above a power of two. The low bits force
    a run of increasing odd steps. -/
private def seed (d m : Nat) := 2^(d-m)*(d+8)-1

private theorem prefix_value {b j u : Nat} (hj : j≤b) (hu : 0<u) :
    orbit j (2^b*u-1)+1=3^j*(2^(b-j)*u) := by
  have decomp : 2^b*u=2^j*(2^(b-j)*u) := by rw [← mul_assoc,← pow_add]; congr 2; omega
  rw [decomp,(odd_run j _ (by positivity)).1]
  have pos : 0<3^j*(2^(b-j)*u) := by positivity
  omega

private theorem prefix_odd {d m j : Nat} (hj : j<d-m) : orbit j (seed d m)%2=1 := by
  have eq := prefix_value hj.le (by omega : 0<d+8)
  have e : ∃ c, d-m-j=c+1 := ⟨d-m-j-1,by omega⟩
  obtain ⟨c,h⟩ := e
  rw [h,show 3^j*(2^(c+1)*(d+8))=2*(3^j*(2^c*(d+8))) by ring] at eq
  unfold seed
  omega

private theorem buffer {d : Nat} {v : ℝ} (hd : 8≤d)
    (low : 1+7/(d:ℝ)≤v) (up : v≤1+8/(d:ℝ)) :
    2/(d:ℝ)≤logb 2 v ∧ logb 2 v≤16/(d:ℝ) := by
  have dr : (8:ℝ)≤d := by exact_mod_cast hd
  have dp : (0:ℝ)<d := by linarith
  have vp : 0<v := by linarith [show (0:ℝ)≤7/d by positivity]
  have v2 : v≤2 := by linarith [(div_le_one dp).mpr dr]
  have lo : 2/(d:ℝ) ≤ (v-1)/v := (le_div_iff₀ vp).mpr (by
    calc (2/(d:ℝ))*v ≤ (2/d)*2 := mul_le_mul_of_nonneg_left v2 (by positivity)
         _ ≤ 7/d := by rw [div_mul_eq_mul_div]; exact div_le_div_of_nonneg_right (by norm_num) dp.le
         _ ≤ v-1 := by linarith)
  have llog := one_sub_inv_le_log_of_pos vp
  have id : (v-1)/v=1-v⁻¹ := by rw [sub_div,div_self vp.ne',one_div]
  rw [id] at lo
  have ulog := log_le_sub_one_of_pos vp
  have lp : 0<log 2 := log_pos (by norm_num)
  constructor
  · apply (le_div_iff₀ lp).mpr
    calc (2/(d:ℝ))*log 2 ≤ (2/d)*1 := mul_le_mul_of_nonneg_left log_two_bounds.2 (by positivity)
         _ ≤ _ := by linarith
  · apply (div_le_iff₀ lp).mpr
    calc log v ≤ 8/d := by linarith
         _ = (16/d)*(1/2) := by ring
         _ ≤ _ := mul_le_mul_of_nonneg_left log_two_bounds.1 (by positivity)

/-- Uniformly on the rising prefix, the real height differs from the bare
    irrational rotation by a controlled positive amount. -/
private theorem prefix_phase {d m j : Nat} (hd : d=2^m) (dm : m≤d) (large : 8≤d)
    (hj : j≤d-m) : ∃ e : ℝ, 2/(d:ℝ)≤e ∧ e≤16/(d:ℝ) ∧
      height (orbit j (seed d m))=d+j*(alpha-1)+e := by
  let x := orbit j (seed d m)
  let F := (2:ℝ)^d*((3:ℝ)/2)^j
  have fp : 0<F := by dsimp [F]; positivity
  have dp : (0:ℝ)<d := by exact_mod_cast (show 0<d by omega)
  have rd : (d:ℝ)=(2:ℝ)^m := by exact_mod_cast hd
  have w : (2:ℝ)^j*2^(d-m-j)*(d:ℝ)=2^d := by
    rw [← pow_add,show j+(d-m-j)=d-m by omega,rd,← pow_add,show d-m+m=d by omega]
  have sx : (x:ℝ)+1=F*(1+8/d) := by
    calc (x:ℝ)+1 = (3:ℝ)^j*(2^(d-m-j)*(d+8)) := by exact_mod_cast prefix_value hj (by omega : 0<d+8)
         _ = _ := by dsimp only [F]; rw [← w,div_pow]; field_simp
  have fbig : (d:ℝ)≤F := by
    calc (d:ℝ) ≤ (2:ℝ)^d := by exact_mod_cast Nat.lt_two_pow_self.le
         _ ≤ F := le_mul_of_one_le_right (by positivity) (one_le_pow₀ (by norm_num : (1:ℝ)≤3/2))
  let v := (x:ℝ)/F
  have val : v=1+8/d-1/F := by
    dsimp [v]; rw [show (x:ℝ)=(1+8/d)*F-1 by linarith [mul_comm F (1+8/(d:ℝ))],sub_div,mul_div_cancel_right₀ _ fp.ne']
  have lo : 1+7/(d:ℝ)≤v := by rw [val]; linarith [one_div_le_one_div_of_le dp fbig,show 8/(d:ℝ)=7/d+1/d by ring]
  have up : v≤1+8/(d:ℝ) := by rw [val]; linarith [one_div_pos.mpr fp]
  have vp : 0<v := by linarith [show (0:ℝ)≤7/d by positivity]
  obtain ⟨el,eu⟩ := buffer large lo up
  refine ⟨logb 2 v,el,eu,?_⟩
  have xeq : (x:ℝ)=F*v := by dsimp only [v]; field_simp
  change logb 2 (x:ℝ)=_
  rw [xeq,logb_mul fp.ne' vp.ne']
  dsimp only [F]
  rw [logb_mul (by positivity) (by positivity),logb_pow,logb_pow,logb_div (by norm_num) (by norm_num),logb_two]
  unfold alpha
  ring

private theorem size_floor {d m j : Nat} (hd : d=2^m) (dm : m≤d) (hj : j≤d-m) :
    2^d ≤ orbit j (seed d m) := by
  have eq : 2^(d-m)*d=2^d := by
    conv_lhs => rhs; rw [hd]
    rw [← pow_add,show d-m+m=d by omega]
  have base : 2^d≤seed d m := by
    dsimp [seed]; rw [Nat.mul_add,eq]
    have pos : 0<2^(d-m) := by positivity
    omega
  exact base.trans ((odd_run (d-m) (d+8) (by omega)).2 _ hj)

private theorem marked_height {x : Nat} (m : Marked x) :
    height x-x.log2 ≤ 140/((x.log2:ℝ)+1) := by
  let P := 2^x.log2
  have xp : 0<x := by have := m.1; omega
  have xr : (0:ℝ)<x := by exact_mod_cast xp
  have pp : (0:ℝ)<P := by dsimp [P]; positivity
  have pl : P≤x := Nat.log2_self_le xp.ne'
  have bound := m.2
  change (x.log2+1)*(x-P)≤70*P at bound
  have br : ((x.log2:ℝ)+1)*((x:ℝ)-P)≤70*P := by
    simpa only [Nat.cast_add,Nat.cast_one,Nat.cast_mul,Nat.cast_ofNat,Nat.cast_sub pl] using
      (show (((x.log2+1)*(x-P):Nat):ℝ)≤((70*P:Nat):ℝ) by exact_mod_cast bound)
  let v := (x:ℝ)/P
  have vp : 0<v := div_pos xr pp
  have width : v-1≤70/((x.log2:ℝ)+1) := by
    apply (le_div_iff₀ (by positivity)).mpr
    rw [show (v-1)*((x.log2:ℝ)+1)=(((x.log2:ℝ)+1)*(x-P))/P by dsimp [v]; field_simp]
    exact (div_le_iff₀ pp).mpr br
  have id : logb 2 v=height x-(x.log2:ℝ) := by
    dsimp only [v,height,P]
    rw [logb_div xr.ne' pp.ne',Nat.cast_pow,Nat.cast_ofNat,logb_pow,logb_two,mul_one]
  rw [← id]
  apply (div_le_iff₀ (log_pos (by norm_num))).mpr
  calc log v ≤ v-1 := log_le_sub_one_of_pos vp
       _ ≤ _ := width
       _ = (140/((x.log2:ℝ)+1))*(1/2) := by ring
       _ ≤ _ := mul_le_mul_of_nonneg_left log_two_bounds.1 (by positivity)

private theorem mark_near {d m j : Nat} (hd : d=2^m) (dm : m≤d) (large : 16≤d)
    (half : 2*j≤d) (hj : j<d-m) {z : ℤ}
    (lo : 0≤height (orbit j (seed d m))-z)
    (hi : height (orbit j (seed d m))-z≤18/(d:ℝ)) : Marked (orbit j (seed d m)) := by
  let x := orbit j (seed d m)
  have odd := prefix_odd hj
  have xp : 0<x := by change x%2=1 at odd; omega
  have dr : (16:ℝ)≤d := by exact_mod_cast large
  have dp : (0:ℝ)<d := by linarith
  obtain ⟨e,_,eu,eq⟩ := prefix_phase hd dm (by omega) hj.le
  have half' : (2:ℝ)*j≤d := by exact_mod_cast half
  have upper : (x.log2:ℝ)+1 ≤ (7/4)*(d:ℝ) := by
    have h := Real.log2_le_logb x
    change (x.log2:ℝ)≤height x at h
    change height x=_ at eq
    linarith [mul_le_mul_of_nonneg_left (show alpha-1≤1 by linarith [rotation_bounds.2]) (show 0≤(j:ℝ) by positivity),
      (div_le_one dp).mpr dr]
  refine ⟨odd,section_of_phase xp lo ?_⟩
  calc _ ≤ (7/4*(d:ℝ))*(height x-z) := mul_le_mul_of_nonneg_right upper lo
       _ ≤ (7/4*(d:ℝ))*(18/d) := mul_le_mul_of_nonneg_left hi (by positivity)
       _ ≤ 35 := by field_simp; linarith

private theorem marked_pair {d m : Nat} (hd : d=2^m) (large : 16≤d) (room : m<d/2) :
    Marked (seed d m) ∧ ∃ q, 0<q ∧ q≤d/2 ∧ Marked (orbit q (seed d m)) := by
  have dm : m≤d := by omega
  have dr : (0:ℝ)<d := by exact_mod_cast (show 0<d by omega)
  obtain ⟨a,q,qp,qn,_,_,approx⟩ := rotation_grid (d/2) (by omega)
  have qj : q<d-m := by omega
  have appr : |(q:ℝ)*alpha-a|≤2/(d:ℝ) := approx.trans (by
    apply (div_le_div_iff₀ (by positivity) dr).mpr
    exact_mod_cast (show 1*d≤2*(d/2+1) by omega))
  constructor
  · obtain ⟨e,el,eu,eq⟩ := prefix_phase (j:=0) hd dm (by omega) (by omega)
    apply mark_near (j:=0) hd dm large (by omega) (by omega) (z:=(d:ℤ))
    · push_cast; simp only [Nat.cast_zero,zero_mul,add_zero] at eq
      linarith [show (0:ℝ)≤2/d by positivity]
    · push_cast; simp only [Nat.cast_zero,zero_mul,add_zero] at eq
      linarith [show 16/(d:ℝ)≤18/d from div_le_div_of_nonneg_right (by norm_num) dr.le]
  · obtain ⟨e,el,eu,eq⟩ := prefix_phase (j:=q) hd dm (by omega) qj.le
    refine ⟨q,qp,qn,mark_near hd dm large (by omega) qj (z:=(d:ℤ)+a-q) ?_ ?_⟩
    · push_cast; linarith [(abs_le.mp appr).1]
    · push_cast; linarith [(abs_le.mp appr).2,show 2/(d:ℝ)+16/d=18/d by ring]

private theorem late_mark {d m H j : Nat} (hd : d=2^m) (dm : m≤d) (large : 16≤d)
    (scale : 156*(4^H+1)≤d) (jp : 0<j) (hj : j≤d-m) (mark : Marked (orbit j (seed d m))) :
    H<j := by
  let x := orbit j (seed d m)
  have xp : 0<x := by have h : x%2=1 := mark.1; omega
  have dlow : d≤x.log2 := (Nat.le_log2 xp.ne').mpr (size_floor hd dm hj)
  have dr : (0:ℝ)<d := by exact_mod_cast (show 0<d by omega)
  have small := marked_height mark
  change height x-x.log2≤_ at small
  have hd' : (d:ℝ)≤(x.log2:ℝ)+1 := by exact_mod_cast (show d≤x.log2+1 by omega)
  have small' : height x-x.log2≤140/(d:ℝ) := by
    apply small.trans
    exact div_le_div_of_nonneg_left (by norm_num) dr hd'
  obtain ⟨e,el,eu,eq⟩ := prefix_phase hd dm (by omega) hj
  change height x=_ at eq
  let a := x.log2+j-d
  have ae : (a:ℝ)=x.log2+j-(d:ℝ) := by dsimp [a]; rw [Nat.cast_sub (by omega),Nat.cast_add]
  have near : |(j:ℝ)*alpha-a|≤156/(d:ℝ) := by
    rw [ae,abs_le]
    have stay : (x.log2:ℝ)≤height x := Real.log2_le_logb x
    constructor <;> linarith [show 0≤2/(d:ℝ) by positivity,
      show 0≤140/(d:ℝ) by positivity,show 156/(d:ℝ)=16/d+140/d by ring]
  have Kp : 0<(4:Nat)^H := by positivity
  have cmp : 156/(d:ℝ)≤1/(((4^H:Nat):ℝ)+1) := by
    apply (div_le_div_iff₀ dr (by positivity)).mpr
    exact_mod_cast (show 156*(4^H+1)≤1*d by omega)
  have b := grid_barrier Kp jp (near.trans cmp)
  by_contra! early
  have up := Nat.pow_le_pow_right (by decide : 0<4) early
  omega

private theorem gain {d m : Nat} (r : Nat) (bound : r≤d-m) :
    (r+2)*seed d m ≤ 2*orbit r (seed d m) := by
  induction r with
  | zero => simp [orbit]
  | succ j ih =>
    have i := ih (by omega)
    let x := orbit j (seed d m)
    have odd : x%2=1 := prefix_odd (by omega)
    have val : 2*step x=3*x+1 := by simp [step,show x%2≠0 by omega]; omega
    have mono : seed d m≤x := (odd_run _ (d+8) (by omega)).2 _ (by omega)
    rw [orbit_add j 1]
    change (j+1+2)*seed d m≤2*step x
    change (j+2)*seed d m≤2*x at i
    rw [val]; nlinarith only [i,mono]

/-- First positive section returns can increase by an arbitrarily large factor. -/
theorem arbitrarily_large_first_return (C : Nat) :
    ∃ n, 1<n ∧ Marked n ∧ C*n<next n := by
  let H := 2*C
  let m := 2*H+9
  let d := 2^m
  have eq : d=512*4^H := by dsimp [d,m]; rw [pow_add,pow_mul]; norm_num [mul_comm]
  have hp : 0<(4:Nat)^H := by positivity
  have large : 16≤d := by omega
  have room : m<d/2 := by
    have lower : ∀ h : Nat, h+1≤4^h := by
      intro h; induction h with
      | zero => decide
      | succ h ih => rw [pow_succ]; omega
    have := lower H
    dsimp [m]; omega
  obtain ⟨mn,q,qp,qh,mq⟩ := marked_pair (d:=d) (m:=m) rfl large room
  let n := seed d m
  have np : 1<n := by
    have bound : 2^d≤n := size_floor (j:=0) rfl (by omega) (by omega)
    have pw := Nat.lt_two_pow_self (n:=d)
    omega
  let r := returnTime n
  have rp : 0<r := by dsimp [r,returnTime]; omega
  have rq : r≤q := returnTime_min (by omega) qp mq
  have tooLate : H<r := late_mark (d:=d) (m:=m) rfl (by omega) large (by omega) rp (by omega) (next_marked n (by omega))
  have inc := gain (d:=d) (m:=m) r (by omega)
  change (r+2)*n≤2*next n at inc
  have factors : 2*C+1≤r+2 := by change 2*C<r at tooLate; omega
  have mult := Nat.mul_le_mul_right n factors
  refine ⟨n,np,mn,?_⟩
  nlinarith only [inc,mult,np]

#print axioms arbitrarily_large_first_return

end CollatzShell.ForwardSection
