import ConeBounds
import SignedEscape

namespace RampShadow.Postpeak

/-- The upper word starts at the chosen physical peak. -/
def PeakWord (w : Word) (H : ℕ) (v Y : ℤ) : Prop :=
  2^w.length*Y = 3^(H+weight w)*v + offset w

theorem peak_word_walk {w H v Y} (U : PeakWord w H v Y) :
    Walk w.length (weight w) (3^H*v-1) Y := by
  apply walk_of_word
  unfold PeakWord offset at U
  rw [pow_add] at U
  linarith only [U]

theorem peak_word_of_walk {t f H v Y} (U : Walk t f ((3:ℤ)^H*v-1) Y) :
    ∃ w : Word, w.length=t ∧ weight w=f ∧ PeakWord w H v Y := by
  obtain ⟨w,E,F,A⟩ := word_of_walk U
  refine ⟨w,E,F,?_⟩
  unfold PeakWord offset
  rw [E,F,pow_add]
  linarith only [A]

theorem small_state {u t : ℕ} {C A z : ℤ} (neg : -(3:ℤ)^t≤C)
    (pos : C<(3:ℤ)^t) (low : 0≤A) (high : A≤(3:ℤ)^t)
    (eq : (3:ℤ)^u*z+A=C) : |z|≤2*(3:ℤ)^t := by
  have P := one_le_pow₀ (show (1:ℤ)≤3 by norm_num) (n:=u)
  have T : (0:ℤ)≤3^t := by positivity
  by_cases Z : 0≤z
  · rw [abs_of_nonneg Z]
    have F := mul_le_mul_of_nonneg_right P Z
    linarith
  · rw [abs_of_nonpos (show z≤0 by omega)]
    have F := mul_le_mul_of_nonpos_right P (show z≤0 by omega)
    linarith

/-- The signed terminal shrinks by the full odd coefficient of its
    competing tail, so only the tail's even count enters its size. -/
theorem small_state_refined {u t : ℕ} {C A z : ℤ} (ut : u≤t)
    (neg : -(3:ℤ)^t≤C) (pos : C<(3:ℤ)^t) (low : 0≤A) (high : A≤(3:ℤ)^t)
    (eq : (3:ℤ)^u*z+A=C) : |z|≤2*(3:ℤ)^(t-u) := by
  have cap : |(3:ℤ)^u*z|≤2*3^t := by
    rw [abs_le]
    constructor <;> linarith
  rw [abs_mul,abs_of_nonneg (by positivity : (0:ℤ)≤3^u),
    show t=u+(t-u) by omega,pow_add] at cap
  apply le_of_mul_le_mul_left (a:=(3:ℤ)^u)
  · linarith only [cap]
  · positivity

private theorem strict_prefix_price {h p d H : ℕ} {m x v : ℤ}
    (vp : 0<v) (order : p≤h) (size : m<(2:ℤ)^H*v-1)
    (decomp : m=x+(2:ℤ)^h*3^d*v) (bound : |x|≤(2:ℤ)^(h-p)) :
    (2:ℤ)^p*3^d < 2^H := by
  let l := h-p
  have hl : h=l+p := by dsimp [l];omega
  have X : -(2:ℤ)^l≤x := le_trans (neg_le_neg bound) (neg_abs_le x)
  have nn : 0≤(2:ℤ)^H*v-1 := by
    have V : 1≤v := by omega
    have Q := mul_le_mul (one_le_pow₀ (show (1:ℤ)≤2 by norm_num) (n:=H)) V
      (by norm_num) (by positivity)
    omega
  by_contra! D
  have A := mul_le_mul_of_nonneg_right D (show 0≤v by omega)
  have B := mul_le_mul_of_nonneg_left A (show (0:ℤ)≤2^l by positivity)
  have C := mul_le_mul_of_nonneg_right (one_le_pow₀ (show (1:ℤ)≤2 by norm_num) (n:=l)) nn
  rw [hl,pow_add] at decomp
  nlinarith only [X,size,decomp,B,C]

private theorem grade_price {H p u d f : ℕ} (sum : p+u+d=H+f) :
    (2:ℤ)^p*3^d < 2^H ↔ (3:ℤ)^d*2^f < 2^(u+d) := by
  have poweq : (2:ℤ)^p*2^(u+d)=2^H*2^f := by
    rw [←pow_add,←pow_add,show p+(u+d)=H+f by omega]
  constructor
  · intro P
    have X := mul_lt_mul_of_pos_right P (show (0:ℤ)<2^(u+d) by positivity)
    apply lt_of_mul_lt_mul_left (a:=(2:ℤ)^H)
    · nlinarith only [X,congrArg (fun a : ℤ => a*3^d) poweq]
    · positivity
  · intro P
    have X := mul_lt_mul_of_pos_left P (show (0:ℤ)<2^H by positivity)
    apply lt_of_mul_lt_mul_right (a:=(2:ℤ)^(u+d))
    · nlinarith only [X,congrArg (fun a : ℤ => a*3^d) poweq]
    · positivity

/-- Every cheap all-clock merger supplies a same-offset tail word with
    sufficient grade. There is no restriction on the smaller start's clock. -/
theorem collision_necessary {w H v m Y e k d} (U : PeakWord w H v Y)
    (tall : 21*(w.length-weight w)+3≤H) (vp : 0<v) (mp : 0<m)
    (lt : m<(2:ℤ)^H*v-1) (W : Walk e k m Y) (grade : k+d=H+weight w) :
    ∃ b : Word, b.length=w.length ∧ offset b=offset w ∧
      (3:ℤ)^d*2^weight w < 2^(weight b+d) := by
  let t := w.length
  let f := weight w
  have hU := peak_word_walk U
  have bud := actual_even_budget (weight_le w) (cheap_budget vp mp lt hU W grade)
  have ke := count_le W
  have fc := weight_le w
  change e-k+d<2*(t-f) at bud
  change 21*(t-f)+3≤H at tall
  change k+d=H+f at grade
  change f≤t at fc
  let h := e-t
  have eh : e=h+t := by dsimp [h]; omega
  have W' : Walk (h+t) k m Y := eh ▸ W
  obtain ⟨p,u,z,L,R,ku⟩ := split W'
  have uh := count_le R
  have ph := count_le L
  have price : p+u+d=H+f := by omega
  let a := (3:ℤ)^d*v
  let x₀ := m-2^h*a
  let z₀ := z-3^p*a
  have S : Walk h p x₀ z₀ := by
    simpa only [x₀,z₀,sub_eq_add_neg,mul_neg] using lift L (-a)
  have upperEq : (2:ℤ)^t*Y=3^(H+f)*v+offset w := U
  have poweq : (3:ℤ)^(H+f)=3^u*3^p*3^d := by
    rw [←pow_add,←pow_add,show u+p+d=H+f by omega]
  rw [poweq] at upperEq
  obtain ⟨b,bl,bw,beq⟩ := word_of_walk R
  have trans : 3^u*z₀+intercept b=offset w := by
    dsimp [z₀,a]
    nlinarith only [upperEq,beq]
  have OB := offset_bounds w
  have BB := intercept_bounds b
  rw [bl] at BB
  have two : (0:ℤ)≤2^t := by positivity
  have tiny := small_state_refined uh OB.1 OB.2 BB.1 (by linarith [BB.2]) trans
  have tailEven : t-u≤2*(t-f) := by omega
  have Z := pow_le_pow_right₀ (show (1:ℤ)≤3 by norm_num) tailEven
  have small : |z₀|≤2*(3:ℤ)^(2*(t-f)) := by linarith only [tiny,Z]
  have high : 9*(2*(t-f))+3≤p := by omega
  have low : h-p≤2*(2*(t-f)) := by omega
  have hit := signed_trap S high low small
  have cap := origin_magnitude S
  rw [hit] at cap
  norm_num at cap
  have decom : m=x₀+(2:ℤ)^h*3^d*v := by dsimp [x₀,a];ring
  have P := strict_prefix_price vp ph lt decom cap
  refine ⟨b,bl,?_,?_⟩
  · change intercept b-3^weight b=offset w
    rw [bw]
    rw [hit] at trans
    linarith only [trans]
  · rw [bw]
    exact (grade_price price).mp P

private theorem integer_budget {u d f : ℕ} (G : (3:ℤ)^d*2^f < 2^(u+d)) : d<2*u := by
  by_contra! L
  obtain ⟨a,eq⟩ := Nat.exists_eq_add_of_le L
  have A := pow_le_pow_left₀ (by norm_num : (0:ℤ)≤8) (by norm_num : (8:ℤ)≤9) u
  have B := pow_le_pow_left₀ (by norm_num : (0:ℤ)≤2) (by norm_num : (2:ℤ)≤3) a
  have C := mul_le_mul A B (by positivity) (by positivity)
  have F := mul_le_mul_of_nonneg_left (one_le_pow₀ (show (1:ℤ)≤2 by norm_num) (n:=f))
    (show (0:ℤ)≤3^d by positivity)
  have left : (2:ℤ)^(u+d)=8^u*2^a := by
    rw [show u+d=3*u+a by omega,pow_add,pow_mul];norm_num
  have right : (3:ℤ)^d=9^u*3^a := by rw [eq,pow_add,pow_mul];norm_num
  linarith only [G,F,left,right,C]

theorem gain_width {u d f : ℕ} (G : (3:ℤ)^d*2^f < 2^(u+d)) : f<u ∧ d<2*(u-f) := by
  have U : f<u := by
    by_contra! H
    have A := pow_le_pow_right₀ (show (1:ℤ)≤2 by norm_num) H
    have B := pow_le_pow_left₀ (by norm_num : (0:ℤ)≤2) (by norm_num : (2:ℤ)≤3) d
    have C := mul_le_mul A B (by positivity) (by positivity)
    rw [pow_add] at G
    linarith only [G,C]
  refine ⟨U,integer_budget (u:=u-f) (d:=d) (f:=0) ?_⟩
  simp only [pow_zero,mul_one]
  apply lt_of_mul_lt_mul_right (a:=(2:ℤ)^f)
  · rw [←pow_add,show u-f+d+f=u+d by omega];exact G
  · positivity

/-- Each sufficiently heavy same-offset word gives an explicit smaller
    positive source. Its prefix consists entirely of physical odd edges. -/
theorem collision_sufficient {w b H v Y k d} (U : PeakWord w H v Y)
    (tall : 21*(w.length-weight w)+3≤H) (vp : 0<v)
    (grade : k+d=H+weight w) (bl : b.length=w.length) (matchC : offset b=offset w)
    (cheap : (3:ℤ)^d*2^weight w < 2^(weight b+d)) :
    ∃ m e, 0<m ∧ m<(2:ℤ)^H*v-1 ∧ Walk e k m Y := by
  let u := weight b
  let p := k-u
  have ut : u≤w.length := by simpa only [u,bl] using weight_le b
  have B := (gain_width cheap).2
  change d<2*(u-weight w) at B
  have uf := (gain_width cheap).1
  change weight w<u at uf
  have fl := weight_le w
  have pk : p+u=k := by dsimp [p];omega
  have P : 1≤p := by dsimp [p];omega
  have price : p+u+d=H+weight w := by omega
  have gain := (grade_price price).mpr cheap
  let a := (3:ℤ)^d*v
  let m := (2:ℤ)^p*a-1
  have ap : 1≤a := by
    dsimp [a]
    have A := mul_le_mul (one_le_pow₀ (show (1:ℤ)≤3 by norm_num) (n:=d))
      (show 1≤v by omega) (by norm_num) (by positivity)
    simpa using A
  have M : 0<m := by
    have G : (2:ℤ)^1≤2^p := pow_le_pow_right₀ (by norm_num) P
    have A := mul_le_mul G ap (by norm_num) (by positivity)
    dsimp [m];norm_num at A;omega
  have MM : m<(2:ℤ)^H*v-1 := by
    have G := mul_lt_mul_of_pos_right gain vp
    dsimp [m,a]
    linarith only [G]
  have r := ramp_walk p a
  have tail : Walk b.length u (3^p*a-1) Y := by
    apply walk_of_word
    have eq := U
    unfold PeakWord at eq
    unfold offset at matchC
    have PP : (3:ℤ)^(H+weight w)=3^u*3^p*3^d := by
      rw [←pow_add,←pow_add,show u+p+d=H+weight w by omega]
    rw [PP] at eq
    rw [bl]
    dsimp [a]
    change (2:ℤ)^w.length*Y = 3^u*(3^p*(3^d*v)-1)+intercept b
    change intercept b-3^u=offset w at matchC
    nlinarith only [eq,matchC]
  refine ⟨m,p+b.length,M,MM,?_⟩
  rw [←pk]
  exact append r tail

/-- An exact finite word criterion for existence of smaller ordinary visitors
    with a prescribed near-optimal odd grade, even at unbounded lower clocks. -/
theorem cone_iff {w H v Y k d} (U : PeakWord w H v Y)
    (tall : 21*(w.length-weight w)+3≤H) (vp : 0<v) (grade : k+d=H+weight w) :
    (∃ m e, 0<m ∧ m<(2:ℤ)^H*v-1 ∧ Walk e k m Y) ↔
    ∃ b : Word, b.length=w.length ∧ offset b=offset w ∧
      (3:ℤ)^d*2^weight w < 2^(weight b+d) := by
  constructor
  · rintro ⟨m,e,mp,lt,W⟩
    exact collision_necessary U tall vp mp lt W grade
  · rintro ⟨b,bl,bc,price⟩
    exact collision_sufficient U tall vp grade bl bc price

end RampShadow.Postpeak

#print axioms RampShadow.Postpeak.cone_iff
