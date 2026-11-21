import SectionDynamics

/-!
# Cofinal expanding section returns with a trailing-depth reset

The logarithmic estimates `buffer` and `marked_height` are reproduced from
PR 173, fa0c9e2a2851e6324391e39c17afcb5913185aec,
research/lean-shell-cover/RisingReturns.lean. The reset seed, ordinary prefix,
shifted phase, and simultaneous coordinate increase are new here.
-/

namespace CollatzShell.ForwardSection.Reset

open Real

private def start (d h : Nat) := (2^(d-h)*(3*d+23)-5)/3
private def base (d h : Nat) := 2^(d-h-2)*(3*d+23)-1
private def value (d h j : Nat) := orbit (j-1) (base d h)

private theorem four_linear (h : Nat) (hh : 5≤h) : 4*(h+1)≤2^h := by
  induction h,hh using Nat.le_induction with
  | base => decide
  | succ h hh ih => rw [pow_succ]; omega

private theorem double_linear (d : Nat) (hd : 2≤d) : 2*d≤2^d := by
  induction d,hd using Nat.le_induction with
  | base => decide
  | succ d hd ih => rw [pow_succ]; omega

private theorem power_decomp {d h : Nat} (hd : d=2^h) (room : h+2≤d) :
    2^(d-h)*d=2^d ∧ 4*2^(d-h-2)=2^(d-h) := by
  constructor
  · rw [hd,←pow_add]; congr 1; omega
  · calc 4*2^(d-h-2)=2^((d-h-2)+2) := by rw [pow_add]; norm_num; ring
         _ = 2^(d-h) := by congr 1; omega

private theorem start_exact {d h : Nat} (hd : d=2^h) (he : h%2=0)
    (hp : 0<h) (room : h+2≤d) :
    3*start d h+5=2^(d-h)*(3*d+23) := by
  have de : d%2=0 := by
    obtain ⟨i,hi⟩ := Nat.exists_eq_succ_of_ne_zero hp.ne'
    rw [hd,hi,pow_succ]; omega
  have e : (d-h)%2=0 := by omega
  have expo : d-h=2*((d-h)/2) := by omega
  have pmod : 2^(d-h)%3=1 := by rw [expo,pow_mul]; norm_num [Nat.pow_mod]
  have pos : 5≤2^(d-h)*(3*d+23) := by
    have pw : 1≤2^(d-h) := Nat.one_le_pow _ _ (by decide)
    nlinarith
  have rem : (2^(d-h)*(3*d+23)-5)%3=0 := by
    have : (2^(d-h)*(3*d+23))%3=2 := by simp [Nat.mul_mod,Nat.add_mod,pmod]
    omega
  have dv := Nat.mod_add_div (2^(d-h)*(3*d+23)-5) 3
  dsimp [start]; omega

private theorem start_bounds {d h : Nat} (hd : d=2^h) (he : h%2=0)
    (hp : 0<h) (room : h+2≤d) (large : 16≤d) :
    2^d≤start d h ∧ start d h<2^(d+1) := by
  have eq := start_exact hd he hp room
  have pd := (power_decomp hd room).1
  have pp : 0<2^(d-h) := by positivity
  constructor
  · nlinarith only [eq,pd,pp]
  · rw [pow_succ]; nlinarith only [eq,pd,pp,large]

private theorem start_marked {d h : Nat} (hd : d=2^h) (he : h%2=0)
    (hp : 0<h) (room : h+2≤d) (large : 16≤d) : Marked (start d h) := by
  have eq := start_exact hd he hp room
  obtain ⟨lo,hi⟩ := start_bounds hd he hp room large
  have np : 0<start d h := lt_of_lt_of_le (by positivity) lo
  have lg : (start d h).log2=d := (Nat.log2_eq_iff np.ne').mpr ⟨lo,hi⟩
  have pd := power_decomp hd room
  have nm : start d h%4=1 := by
    have eq4 := eq
    rw [←pd.2,Nat.mul_assoc] at eq4
    omega
  refine ⟨by omega,?_⟩
  unfold InSection
  rw [lg]
  have gap := Nat.sub_add_cancel lo
  have pd1 := pd.1
  have diff : 3*(start d h-2^d)+5=23*2^(d-h) := by nlinarith only [eq,pd1,gap]
  have small : start d h-2^d≤8*2^(d-h) := by omega
  have limit := Nat.mul_le_mul_right (2^(d-h)) (by omega : d+1≤2*d)
  calc (d+1)*(start d h-2^d) ≤ (d+1)*(8*2^(d-h)) := Nat.mul_le_mul_left _ small
       _ = 8*((d+1)*2^(d-h)) := by ring
       _ ≤ 8*(2*2^d) := Nat.mul_le_mul_left _ (by nlinarith only [limit,pd1])
       _ ≤ 70*2^d := by omega

private theorem first_steps {d h : Nat} (hd : d=2^h) (he : h%2=0)
    (hp : 0<h) (room : h+2≤d) :
    start d h%4=1 ∧ step (start d h)=2*base d h ∧ orbit 2 (start d h)=base d h := by
  have eq := start_exact hd he hp room
  have pd := (power_decomp hd room).2
  have pos : 0<2^(d-h-2)*(3*d+23) := by positivity
  rw [←pd,Nat.mul_assoc] at eq
  have nm : start d h%4=1 := by omega
  have stepEq : step (start d h)=2*base d h := by
    simp only [step,show start d h%2≠0 by omega,ite_false]
    dsimp [base]; omega
  exact ⟨nm,stepEq,by simp only [orbit,stepEq,step_double]⟩

private theorem value_exact {d h j : Nat} (jp : 0<j) (bound : j≤d-h-1) :
    value d h j+1=3^(j-1)*(2^(d-h-2-(j-1))*(3*d+23)) := by
  have hj : j-1≤d-h-2 := by omega
  have decomp : 2^(d-h-2)*(3*d+23)=2^(j-1)*(2^(d-h-2-(j-1))*(3*d+23)) := by
    rw [←mul_assoc,←pow_add]; congr 2; omega
  dsimp [value,base]
  rw [decomp,(odd_run (j-1) _ (by positivity)).1]
  have pos : 0<3^(j-1)*(2^(d-h-2-(j-1))*(3*d+23)) := by positivity
  omega

private theorem value_odd {d h j : Nat} (jp : 0<j) (bound : j<d-h-1) :
    value d h j%2=1 := by
  have ex := value_exact jp bound.le
  have e : d-h-2-(j-1)=(d-h-2-(j-1)-1)+1 := by omega
  have rhs : 3^(j-1)*(2^(d-h-2-(j-1))*(3*d+23)) =
      2*(3^(j-1)*(2^(d-h-2-(j-1)-1)*(3*d+23))) := by
    conv_lhs => rw [e,pow_succ]
    ring
  rw [rhs] at ex
  omega

private theorem value_hit {d h j : Nat} (hd : d=2^h) (he : h%2=0)
    (hp : 0<h) (room : h+2≤d) (jp : 0<j) :
    orbit (j+1) (start d h)=value d h j := by
  rw [show j+1=2+(j-1) by omega,orbit_add,(first_steps hd he hp room).2.2]
  rfl

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


private theorem prefix_phase {d h j : Nat} (hd : d=2^h) (room : h+2≤d)
    (large : 16≤d) (jp : 0<j) (bound : j≤d-h-1) :
    ∃ e : ℝ, 2/(d:ℝ)≤e ∧ e≤16/(d:ℝ) ∧
      height (value d h j)=(d:ℝ)-1+j*(alpha-1)+e := by
  let x := value d h j
  let t := j-1
  let F := (2:ℝ)^d*(3/4)*((3:ℝ)/2)^t
  have fp : 0<F := by dsimp [F]; positivity
  have dp : (0:ℝ)<d := by exact_mod_cast (show 0<d by omega)
  have rd : (d:ℝ)=(2:ℝ)^h := by exact_mod_cast hd
  have et : t≤d-h-2 := by dsimp [t]; omega
  have w : 4*(2:ℝ)^t*2^(d-h-2-t)*(d:ℝ)=2^d := by
    rw [rd,show (4:ℝ)=2^2 by norm_num,←pow_add,←pow_add,←pow_add]
    congr 1
    omega
  have sx : (x:ℝ)+1=F*(1+23/(3*d)) := by
    calc (x:ℝ)+1 = (3:ℝ)^t*(2^(d-h-2-t)*(3*d+23)) := by
           exact_mod_cast value_exact jp bound
         _ = _ := by dsimp only [F]; rw [←w,div_pow]; field_simp
  have fbig : 3*(d:ℝ)≤2*F := by
    have two : 2*(d:ℝ)≤(2:ℝ)^d := by exact_mod_cast double_linear d (by omega)
    have inc : (1:ℝ)≤(3/2:ℝ)^t := one_le_pow₀ (by norm_num)
    dsimp only [F]
    nlinarith [mul_le_mul_of_nonneg_left inc (show 0≤(2:ℝ)^d*(3/4) by positivity)]
  let v := (x:ℝ)/F
  have val : v=1+23/(3*d)-1/F := by
    dsimp [v]
    rw [show (x:ℝ)=(1+23/(3*d))*F-1 by linarith [mul_comm F (1+23/(3*(d:ℝ)))],sub_div,mul_div_cancel_right₀ _ fp.ne']
  have inv : 1/F≤2/(3*(d:ℝ)) := (div_le_div_iff₀ fp (by positivity)).mpr (by linarith)
  have lo : 1+7/(d:ℝ)≤v := by
    rw [val]
    have id : 23/(3*(d:ℝ))-2/(3*d)=7/d := by field_simp; ring
    linarith
  have up : v≤1+8/(d:ℝ) := by
    rw [val]
    have small : 23/(3*(d:ℝ))≤8/d := by apply (div_le_div_iff₀ (by positivity) dp).mpr; nlinarith
    linarith [one_div_pos.mpr fp]
  have vp : 0<v := by linarith [show (0:ℝ)≤7/d by positivity]
  obtain ⟨el,eu⟩ := buffer (by omega) lo up
  refine ⟨logb 2 v,el,eu,?_⟩
  have xeq : (x:ℝ)=F*v := by dsimp only [v]; field_simp
  change logb 2 (x:ℝ)=_
  rw [xeq,logb_mul fp.ne' vp.ne']
  dsimp only [F]
  rw [logb_mul (by positivity) (by positivity),logb_mul (by positivity) (by positivity),
    logb_pow,logb_pow,logb_div (by norm_num) (by norm_num),
    logb_div (by norm_num) (by norm_num),logb_two]
  have four : logb 2 (4:ℝ)=2 := by rw [show (4:ℝ)=2^2 by norm_num,logb_pow,logb_two]; norm_num
  rw [four]
  have tj : (t:ℝ)=(j:ℝ)-1 := by dsimp [t]; rw [Nat.cast_sub (by omega),Nat.cast_one]
  rw [tj]
  unfold alpha
  ring

private theorem size_floor {d h j : Nat} (hd : d=2^h) (he : h%2=0)
    (hp : 0<h) (room : h+2≤d) (large : 16≤d) (jp : 0<j) (bound : j≤d-h-1) :
    2^(d-1)≤value d h j := by
  have st := (first_steps hd he hp room).2.1
  have eq := start_exact hd he hp room
  have dec := (power_decomp hd room).2
  have lo := (start_bounds hd he hp room large).1
  have pos : 0<2^(d-h-2)*(3*d+23) := by positivity
  have bs : 4*base d h=3*start d h+1 := by dsimp [base]; rw [←dec,Nat.mul_assoc] at eq; omega
  have pw : 2^d=2*2^(d-1) := by
    calc 2^d=2^((d-1)+1) := by congr 1; omega
         _ = 2*2^(d-1) := by rw [pow_succ]; ring
  have startLow : 2^(d-1)≤base d h := by omega
  exact startLow.trans ((odd_run (d-h-2) (3*d+23) (by omega)).2 _ (by omega))

private theorem mark_near {d h j : Nat} (hd : d=2^h) (room : h+2≤d)
    (large : 16≤d) (jp : 0<j) (half : 2*j≤d) (bound : j<d-h-1) {z : ℤ}
    (lo : 0≤height (value d h j)-z) (hi : height (value d h j)-z≤18/(d:ℝ)) :
    Marked (value d h j) := by
  let x := value d h j
  have odd := value_odd jp bound
  have xp : 0<x := by change x%2=1 at odd; omega
  have dr : (16:ℝ)≤d := by exact_mod_cast large
  have dp : (0:ℝ)<d := by linarith
  obtain ⟨e,_,eu,eq⟩ := prefix_phase hd room large jp bound.le
  have half' : (2:ℝ)*j≤d := by exact_mod_cast half
  have upper : (x.log2:ℝ)+1≤(7/4)*(d:ℝ) := by
    have hlog := Real.log2_le_logb x
    change (x.log2:ℝ)≤height x at hlog
    change height x=_ at eq
    linarith [mul_le_mul_of_nonneg_left (show alpha-1≤1 by linarith [rotation_bounds.2]) (show 0≤(j:ℝ) by positivity),
      (div_le_one dp).mpr dr]
  refine ⟨odd,section_of_phase xp lo ?_⟩
  calc _ ≤ (7/4*(d:ℝ))*(height x-z) := mul_le_mul_of_nonneg_right upper lo
       _ ≤ (7/4*(d:ℝ))*(18/d) := mul_le_mul_of_nonneg_left hi (by positivity)
       _ ≤ 35 := by field_simp; linarith

private theorem marked_endpoint {d h : Nat} (hd : d=2^h) (large : 16≤d)
    (room : h+2<d/2) : ∃ q, 0<q ∧ q≤d/2 ∧ Marked (value d h q) := by
  obtain ⟨a,q,qp,qn,_,_,approx⟩ := rotation_grid (d/2) (by omega)
  have qr : q<d-h-1 := by omega
  have dp : (0:ℝ)<d := by exact_mod_cast (show 0<d by omega)
  have appr : |(q:ℝ)*alpha-a|≤2/(d:ℝ) := approx.trans (by
    apply (div_le_div_iff₀ (by positivity) dp).mpr
    exact_mod_cast (show 1*d≤2*(d/2+1) by omega))
  obtain ⟨e,el,eu,eq⟩ := prefix_phase (j:=q) hd (by omega) large qp qr.le
  refine ⟨q,qp,qn,mark_near hd (by omega) large qp (by omega) qr
    (z:=(d:ℤ)-1+a-q) ?_ ?_⟩
  · push_cast; linarith [(abs_le.mp appr).1]
  · push_cast; linarith [(abs_le.mp appr).2,show 2/(d:ℝ)+16/d=18/d by ring]

private theorem late_mark {d h H j : Nat} (hd : d=2^h) (he : h%2=0) (hp : 0<h)
    (room : h+2≤d) (large : 16≤d) (scale : 156*(4^H+1)≤d)
    (jp : 0<j) (bound : j≤d-h-1) (mark : Marked (value d h j)) : H<j := by
  let x := value d h j
  have xp : 0<x := by have m : x%2=1 := mark.1; omega
  have dlow : d-1≤x.log2 := (Nat.le_log2 xp.ne').mpr (size_floor hd he hp room large jp bound)
  have dr : (0:ℝ)<d := by exact_mod_cast (show 0<d by omega)
  have small := marked_height mark
  change height x-x.log2≤_ at small
  have hd' : (d:ℝ)≤(x.log2:ℝ)+1 := by exact_mod_cast (show d≤x.log2+1 by omega)
  have small' : height x-x.log2≤140/(d:ℝ) :=
    small.trans (div_le_div_of_nonneg_left (by norm_num) dr hd')
  obtain ⟨e,el,eu,eq⟩ := prefix_phase hd room large jp bound
  change height x=_ at eq
  let a := x.log2+j+1-d
  have ae : (a:ℝ)=x.log2+j+1-(d:ℝ) := by
    dsimp [a]; rw [Nat.cast_sub (by omega),Nat.cast_add,Nat.cast_add,Nat.cast_one]
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

private theorem rising_gain (b u t : Nat) (up : 0<u) (bound : t≤b) :
    (t+2)*(2^b*u-1)≤2*orbit t (2^b*u-1) := by
  induction t with
  | zero => simp [orbit]
  | succ t ih =>
    have it := ih (by omega)
    let x := orbit t (2^b*u-1)
    have decomp : 2^b*u=2^t*(2^(b-t)*u) := by rw [←mul_assoc,←pow_add]; congr 2; omega
    have eq : x+1=3^t*(2^(b-t)*u) := by
      dsimp [x]
      rw [decomp,(odd_run t _ (by positivity)).1]
      have pos : 0<3^t*(2^(b-t)*u) := by positivity
      omega
    have ex : b-t=(b-t-1)+1 := by omega
    have rhs : 3^t*(2^(b-t)*u)=2*(3^t*(2^(b-t-1)*u)) := by
      conv_lhs => rw [ex,pow_succ]
      ring
    rw [rhs] at eq
    have odd : x%2=1 := by omega
    have val : 2*step x=3*x+1 := by simp [step,show x%2≠0 by omega]; omega
    have mono : 2^b*u-1≤x := (odd_run b u up).2 _ (by omega)
    rw [orbit_add t 1]
    change (t+1+2)*(2^b*u-1)≤2*step x
    change (t+2)*(2^b*u-1)≤2*x at it
    rw [val]
    nlinarith only [it,mono]

private theorem reset_gain {d h j : Nat} (hd : d=2^h) (he : h%2=0) (hp : 0<h)
    (room : h+2≤d) (jp : 0<j) (bound : j≤d-h-1) :
    (j+1)*start d h≤4*value d h j := by
  have eq := start_exact hd he hp room
  have dc := (power_decomp hd room).2
  rw [←dc,Nat.mul_assoc] at eq
  have pos : 0<2^(d-h-2)*(3*d+23) := by positivity
  have bs : 2*base d h≥start d h := by dsimp [base]; omega
  have inc := rising_gain (d-h-2) (3*d+23) (j-1) (by omega) (by omega)
  have mult := Nat.mul_le_mul_left (j+1) bs
  have je : j-1+2=j+1 := by omega
  rw [je] at inc
  change (j+1)*base d h≤2*value d h j at inc
  nlinarith only [inc,mult]

private theorem source_depth {d h : Nat} (hd : d=2^h) (he : h%2=0) (hp : 0<h)
    (room : h+2≤d) : twos (start d h+1)=1 := by
  have mod := (first_steps hd he hp room).1
  have nz : start d h+1≠0 := by omega
  have lower : 1≤twos (start d h+1) :=
    (Nat.prime_two.pow_dvd_iff_le_factorization nz).mp (by norm_num; omega)
  have upper : ¬2≤twos (start d h+1) := by
    intro too
    have := (Nat.prime_two.pow_dvd_iff_le_factorization nz).mpr too
    norm_num at this
    omega
  omega

/-- The next section return can grow arbitrarily in both ordinary size and
trailing-one depth, even when the supplied marked start has depth exactly one. -/
theorem cofinal_expanding_reset (C L : Nat) : ∃ n, L<n ∧ 1<n ∧ Marked n ∧
    twos (n+1)=1 ∧ C*n<next n ∧ C<twos (next n+1) := by
  let H := 4*C+4
  let h := 2*H+2*L+10
  let d := 2^h
  have hp : 0<h := by dsimp [h]; omega
  have he : h%2=0 := by dsimp [h]; omega
  have fl := four_linear h (by dsimp [h]; omega)
  change 4*(h+1)≤d at fl
  have large : 16≤d := by omega
  have room : h+2<d/2 := by omega
  have scale : 156*(4^H+1)≤d := by
    have eq : d=1024*4^H*4^L := by dsimp [d,h]; rw [pow_add,pow_add,pow_mul,pow_mul]; norm_num; ring
    have pH : 0<(4:Nat)^H := by positivity
    have pL : 0<(4:Nat)^L := by positivity
    rw [eq]
    nlinarith
  let n := start d h
  have nm : Marked n := start_marked rfl he hp (by omega) large
  have np : 1<n := by
    have lo : 2^d≤n := (start_bounds rfl he hp (by omega) large).1
    have := Nat.lt_two_pow_self (n:=d)
    omega
  have nL : L<n := by
    have lo : 2^d≤n := (start_bounds rfl he hp (by omega) large).1
    have := Nat.lt_two_pow_self (n:=d)
    dsimp [h] at fl
    omega
  obtain ⟨q,qp,qh,mq⟩ := marked_endpoint (d:=d) (h:=h) rfl large room
  have hitq := value_hit (d:=d) (h:=h) (j:=q) rfl he hp (by omega) qp
  let r := returnTime n
  have rq : r≤q+1 := returnTime_min (by omega) (by omega) (hitq ▸ mq)
  have rp : 0<r := by dsimp [r,returnTime]; omega
  have nr : Marked (next n) := next_marked n (by omega)
  have rtwo : 2≤r := by
    by_contra! small
    have re : r=1 := by omega
    have eq : next n=step n := by change orbit r n=step n; rw [re]; rfl
    have st := (first_steps (d:=d) (h:=h) rfl he hp (by omega)).2.1
    have odd := nr.1
    rw [eq] at odd
    change step (start d h)%2=1 at odd
    rw [st] at odd
    omega
  let j := r-1
  have jp : 0<j := by dsimp [j]; omega
  have jh : j≤d/2 := by dsimp [j]; omega
  have bound : j<d-h-1 := by omega
  have endpt : next n=value d h j := by
    change orbit r (start d h)=_
    rw [show r=j+1 by dsimp [j]; omega]
    exact value_hit rfl he hp (by omega) jp
  have mj : Marked (value d h j) := endpt ▸ nr
  have late : H<j := late_mark rfl he hp (by omega) large scale jp bound.le mj
  have gain := reset_gain (d:=d) (h:=h) (j:=j) rfl he hp (by omega) jp bound.le
  have growth : C*n<next n := by
    rw [endpt]
    change (j+1)*n≤4*value d h j at gain
    dsimp [H] at late
    nlinarith only [gain,late,np]
  have ex := value_exact jp bound.le
  have divisible : 2^(d-h-2-(j-1))∣value d h j+1 := by
    rw [ex]
    exact ⟨3^(j-1)*(3*d+23),by ring⟩
  have depth : d-h-2-(j-1)≤twos (value d h j+1) :=
    (Nat.prime_two.pow_dvd_iff_le_factorization (by omega)).mp divisible
  have high : C<twos (next n+1) := by
    rw [endpt]
    dsimp [h,H] at fl
    omega
  exact ⟨n,nL,np,nm,source_depth rfl he hp (by omega),growth,high⟩

/-- No finite cutoff makes a coordinatewise increasing function of ordinary
size and trailing-one depth strictly decrease at every marked return.
The codomain may be any preorder, and the function need not be linear. -/
theorem no_eventual_coordinate_rank {α : Type*} [Preorder α]
    (F : Nat × Nat → α) (hF : Monotone F) (L : Nat) :
    ¬ ∀ n, L<n → 1<n → Marked n →
      F (next n,twos (next n+1)) < F (n,twos (n+1)) := by
  intro drop
  obtain ⟨n,nL,np,nm,depth,grow,tail⟩ := cofinal_expanding_reset 1 L
  have size_le : n≤next n := by omega
  have tail_le : twos (n+1)≤twos (next n+1) := by omega
  exact not_lt_of_ge (hF ⟨size_le,tail_le⟩) (drop n nL np nm)

#print axioms cofinal_expanding_reset
#print axioms no_eventual_coordinate_rank

end CollatzShell.ForwardSection.Reset
