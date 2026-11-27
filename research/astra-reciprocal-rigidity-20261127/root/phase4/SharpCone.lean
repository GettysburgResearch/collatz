import MirrorEnergy
import PostSelector
import ScaledPrepaid

/-! Stronger cones from the corrected signed energy. The ordinary affine,
source, and word arguments below reuse CollisionCone, ProtectedCone, and
PostSelector, replacing only their signed trap and the sufficient heights.
All older declarations and source files remain unchanged. -/

namespace RampShadow.Postpeak.Sharp

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
    (tall : 6*(w.length-weight w)+3≤H) (vp : 0<v) (mp : 0<m)
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
  change 6*(t-f)+3≤H at tall
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
  have hit := MirrorEnergy.sharp_trap S (by omega) tiny
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

theorem collision_sufficient {w b H v Y k d} (U : PeakWord w H v Y)
    (tall : 6*(w.length-weight w)+3≤H) (vp : 0<v)
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
    (tall : 6*(w.length-weight w)+3≤H) (vp : 0<v) (grade : k+d=H+weight w) :
    (∃ m e, 0<m ∧ m<(2:ℤ)^H*v-1 ∧ Walk e k m Y) ↔
    ∃ b : Word, b.length=w.length ∧ offset b=offset w ∧
      (3:ℤ)^d*2^weight w < 2^(weight b+d) := by
  constructor
  · rintro ⟨m,e,mp,lt,W⟩
    exact collision_necessary U tall vp mp lt W grade
  · rintro ⟨b,bl,bc,price⟩
    exact collision_sufficient U tall vp grade bl bc price

theorem paid_peak {w H v m Y e k b} (U : PeakWord w H v Y)
    (tall : 6*(w.length-weight w)+3*b+3≤H) (vp : 0<v) (mp : 0<m)
    (lt : m<(2:ℤ)^H*v-1) (W : Walk e k m Y) (grade : k=H+weight w+b) :
    ∃ β : Word, ∃ a : ℕ, β.length=w.length ∧ offset β=offset w ∧
      Walk a (k-weight β) m (3^(H+weight w-weight β)*v-1) := by
  let t := w.length
  let f := weight w
  let q := t-f
  have ft : f≤t := weight_le w
  have bud := overflow_even_count vp mp lt (peak_word_walk U) W grade
  change e-k≤2*q+b at bud
  change 6*q+3*b+3≤H at tall
  change k=H+f+b at grade
  obtain ⟨a0,a1,m1,e01,F,G⟩ := split_odds W b (H+f) (by omega)
  have a0k := count_le F
  have a1k := count_le G
  have qe : t=q+f := by dsimp [q];omega
  let h := a1-t
  have splitTime : a1=h+t := by dsimp [h];omega
  have G' : Walk (h+t) (H+f) m1 Y := splitTime ▸ G
  obtain ⟨p,u,z,L,R,price⟩ := split G'
  have uh := count_le R
  have ph := count_le L
  let x₀ := m1-2^h*v
  let z₀ := z-3^p*v
  have S : Walk h p x₀ z₀ := by
    simpa only [x₀,z₀,sub_eq_add_neg,mul_neg] using lift L (-v)
  have upperEq : (2:ℤ)^t*Y=3^(H+f)*v+offset w := U
  rw [price,pow_add] at upperEq
  obtain ⟨β,bl,bw,beq⟩ := word_of_walk R
  have trans : 3^u*z₀+intercept β=offset w := by
    dsimp [z₀]
    nlinarith only [upperEq,beq]
  have OB := offset_bounds w
  have BB := intercept_bounds β
  rw [bl] at BB
  have two : (0:ℤ)≤2^t := by positivity
  have tiny := small_state_refined uh OB.1 OB.2 BB.1 (by linarith [BB.2]) trans
  have hit := MirrorEnergy.sharp_trap S (by omega) tiny
  have zz : z=3^p*v-1 := by dsimp [z₀] at hit;omega
  refine ⟨β,a0+h,bl,?_,?_⟩
  · change intercept β-3^weight β=offset w
    rw [bw]
    rw [hit] at trans
    linarith only [trans]
  · rw [bw,show k-u=b+p by omega]
    change Walk (a0+h) (b+p) m (3^(H+f-u)*v-1)
    rw [show H+f-u=p by omega,←zz]
    exact append F L

/-- Ternary protection on the original ordinary source survives every
    maximal postpeak word in the upper-even-count cone. -/
theorem protected_barrier {w H K v m Y e k s} (U : PeakWord w H v Y)
    (maximal : Maximal w) (tall : 6*(w.length-weight w)+3*K+3≤H)
    (vp : 0<v) (seed : s=0 ∨ s=1) (prec : (3:ℤ)^K ∣ (2:ℤ)^H*v-1-s)
    (mp : 0<m) (lt : m<(2:ℤ)^H*v-1) (W : Walk e k m Y) :
    H+weight w+K < k := by
  by_contra! low
  by_cases discount : k≤H+weight w
  · obtain ⟨d,D⟩ := Nat.exists_eq_add_of_le discount
    obtain ⟨β,bl,bc,gain⟩ := collision_necessary U (by omega) vp mp lt W D.symm
    have more := (gain_width gain).1
    have less := maximal β bl bc
    omega
  · let b := k-(H+weight w)
    have grade : k=H+weight w+b := by dsimp [b];omega
    have cap : b≤K := by omega
    obtain ⟨β,a,bl,bc,V⟩ := paid_peak U (by omega) vp mp lt W grade
    let δ := weight w-weight β
    have free := maximal β bl bc
    have fd : H+weight w-weight β=H+δ := by dsimp [δ];omega
    rw [fd] at V
    have spos : s<(2:ℤ)^H*v-1 := by rcases seed with S|S <;> omega
    have rise : (2:ℤ)^(H+δ)*(3^(H+δ)*v-1+1) =
        3^(H+δ)*2^δ*(2^H*v-1+1) := by rw [pow_add (2:ℤ)];ring
    have pay := scaled_ramp seed spos mp lt
      (one_le_pow₀ (by norm_num : (1:ℤ)≤2) (n:=δ)) prec rise V
    omega

theorem maximal_selector_iff {w H K v Y} (upper : PeakWord w H v Y)
    (maximal : Maximal w) (tall : 6*(w.length-weight w)+3*K+3≤H)
    (vp : 0<v) (np : 0<(2:ℤ)^H*v-1)
    (height : (K:ℤ)*(1+3^K)≤2*(2^H*v-1)) :
    (∃ (e k : ℕ) (m : ℤ), 0<m ∧ m<(2:ℤ)^H*v-1 ∧ k≤H+weight w+K ∧ Walk e k m Y)
      ↔ ∃ β : Word, β.length=w.length ∧ offset β=offset w ∧
        ScaleRow (2^H*v-1) (H+(weight w-weight β)) (weight w-weight β) K := by
  let n := (2:ℤ)^H*v-1
  have rise (δ : ℕ) : (2:ℤ)^(H+δ)*v=2^δ*(n+1) := by dsimp [n];rw [pow_add];ring
  constructor
  · rintro ⟨e,k,m,mp,lt,cap,W⟩
    have expensive : H+weight w<k := by
      by_contra! low
      obtain ⟨d,D⟩ := Nat.exists_eq_add_of_le low
      obtain ⟨β,L,C,G⟩ := collision_necessary upper (by omega) vp mp lt W D.symm
      have A := (gain_width G).1
      have B := maximal β L C
      omega
    let b := k-(H+weight w)
    have cost : k=H+weight w+b := by dsimp [b];omega
    obtain ⟨β,a,L,C,P⟩ := paid_peak upper (by omega) vp mp lt W cost
    have F := maximal β L C
    let δ := weight w-weight β
    have ee : H+weight w-weight β=H+δ := by dsimp [δ];omega
    rw [ee] at P
    refine ⟨β,L,C,(scaled_selector_iff np (rise δ) height).mp ?_⟩
    exact ⟨a,k-weight β,m,mp,lt,by dsimp [δ];omega,P⟩
  · rintro ⟨β,L,C,R⟩
    let δ := weight w-weight β
    have F := maximal β L C
    obtain ⟨a,b,m,mp,lt,budget,P⟩ := (scaled_selector_iff np (rise δ) height).mpr R
    have eq : (2:ℤ)^β.length*Y=3^weight β*(3^(H+δ)*v-1)+intercept β := by
      rw [L]
      have U : (2:ℤ)^w.length*Y=3^(H+weight w)*v+offset w := upper
      rw [←C,offset] at U
      rw [show H+weight w=weight β+(H+δ) by dsimp [δ];omega,pow_add] at U
      nlinarith only [U]
    exact ⟨_,_,m,mp,lt,by dsimp [δ] at budget;omega,append P (walk_of_word β _ _ eq)⟩

theorem protected_prepaid_barrier {w : Word} {H K b L e k : ℕ} {v m Y s : ℤ}
    (U : PeakWord w H v Y) (maximal : Maximal w)
    (tall : 6*(w.length-weight w)+3*(K+b)+3≤H)
    (vp : 0<v) (seed : s=0 ∨ s=1)
    (prec : (3:ℤ)^K ∣ (2:ℤ)^H*v-1-s)
    (mp : 0<m) (lt : m<(2:ℤ)^H*v-1) (W : Walk e k m Y)
    (room : b≤K) (budget : SmallPrefixBound b L)
    (margin : (3:ℤ)^(K+1-b)*2^(L+1)*3^b ≤ 4^(K+1-b)*2^b) :
    H+weight w+K+b < k := by
  by_contra! low
  by_cases discount : k≤H+weight w
  · obtain ⟨d,D⟩ := Nat.exists_eq_add_of_le discount
    obtain ⟨β,bl,bc,gain⟩ := collision_necessary U (by omega) vp mp lt W D.symm
    have more := (gain_width gain).1
    have less := maximal β bl bc
    omega
  · let surplus := k-(H+weight w)
    have grade : k=H+weight w+surplus := by dsimp [surplus]; omega
    have cap : surplus≤K+b := by omega
    obtain ⟨β,a,bl,bc,V⟩ := paid_peak U (by omega) vp mp lt W grade
    let δ := weight w-weight β
    have free := maximal β bl bc
    have fd : H+weight w-weight β=H+δ := by dsimp [δ]; omega
    rw [fd] at V
    have spos : s<(2:ℤ)^H*v-1 := by rcases seed with S|S <;> omega
    have rise : (2:ℤ)^(H+δ)*(3^(H+δ)*v-1+1) =
        3^(H+δ)*2^δ*(2^H*v-1+1) := by
      rw [pow_add (2:ℤ)]; ring
    have pay := scaled_prepaid_ramp seed spos mp lt
      (one_le_pow₀ (by norm_num : (1:ℤ)≤2) (n:=δ)) prec rise V
      room budget margin
    omega

#print axioms cone_iff
#print axioms paid_peak
#print axioms protected_barrier
#print axioms maximal_selector_iff
#print axioms protected_prepaid_barrier

end RampShadow.Postpeak.Sharp

namespace CertifiedRamp.Sharp
open RampShadow RampShadow.Postpeak

/-- The original finite 648-source certificate in the stronger energy cone. -/
theorem twelve_extra_postpeak_odds {w : Word} {H K e k : ℕ} {v m Y s : ℤ}
    (hK : 84≤K) (U : PeakWord w H v Y) (maximal : Maximal w)
    (tall : 6*(w.length-weight w)+3*(K+12)+3≤H)
    (vp : 0<v) (seed : s=0 ∨ s=1)
    (prec : (3:ℤ)^K ∣ (2:ℤ)^H*v-1-s)
    (mp : 0<m) (lt : m<(2:ℤ)^H*v-1) (W : Walk e k m Y) :
    H+weight w+K+12 < k := by
  exact RampShadow.Postpeak.Sharp.protected_prepaid_barrier U maximal tall vp seed prec mp lt W
    (by omega) finite_budget (margin K hK)

#print axioms twelve_extra_postpeak_odds
end CertifiedRamp.Sharp
