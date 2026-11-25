module

public import TowerFrontierPrescribed
import all MixedBarrier
import all TernaryItinerary

public section

namespace Collatz.Itinerary.HourTower

set_option autoImplicit false

/-- Number of odd departures in a shortcut prefix. -/
@[expose] def count : Nat → Nat → Nat
  | 0, _ => 0
  | h+1, n => count h (step n) + n%2

theorem count_le (h n : Nat) : count h n≤h := by
  induction h generalizing n with
  | zero => simp [count]
  | succ h ih => have := ih (step n); simp only [count]; omega

theorem carry (h n : Nat) : ∃ c, 2^h*run h n=3^(count h n)*n+c ∧ c+2^h≤3^h := by
  induction h generalizing n with
  | zero => exact ⟨0,by simp [run,count]⟩
  | succ h ih =>
    obtain ⟨c,eq,le⟩ := ih (step n)
    have p := Nat.pow_le_pow_right (by decide : 0<3) (count_le h (step n))
    rw [run,count,Nat.pow_succ 2,Nat.pow_succ 3 h]
    by_cases even : n%2=0
    · rw [even,Nat.add_zero]
      have split : 2*step n=n := by simp only [step,even,↓reduceIte]; omega
      refine ⟨2*c,?_,by omega⟩
      calc
        2^h*2*run h (step n)=2*(2^h*run h (step n)) := by ac_rfl
        _ = 3^(count h (step n))*(2*step n)+2*c := by rw [eq,Nat.mul_add]; ac_rfl
        _ = 3^(count h (step n))*n+2*c := by rw [split]
    · have odd : n%2=1 := by omega
      rw [odd,Nat.pow_succ]
      have os : 2*step n=3*n+1 := by simp only [step,even,↓reduceIte]; omega
      refine ⟨3^(count h (step n))+2*c,?_,by omega⟩
      calc
        2^h*2*run h (step n)=2*(2^h*run h (step n)) := by ac_rfl
        _ = 3^(count h (step n))*(2*step n)+2*c := by rw [eq,Nat.mul_add]; ac_rfl
        _ = _ := by rw [os,Nat.mul_add,Nat.mul_one]; ac_rfl

/-- An upper bound that keeps track of the actual odd count, including near zero. -/
private theorem upper {h n t : Nat} (bound : n≤2^h*t) :
    run h n≤3^(count h n)*t := by
  induction h generalizing n t with
  | zero => simpa [run,count] using bound
  | succ h ih =>
    have sz : 2^(h+1)*t=2*(2^h*t) := by rw [Nat.pow_succ]; ac_rfl
    rw [sz] at bound
    rw [run,count]
    by_cases even : n%2=0
    · rw [even,Nat.add_zero]
      exact ih (by simp only [step,even,↓reduceIte]; omega)
    · have odd : n%2=1 := by omega
      rw [odd,Nat.pow_succ,Nat.mul_assoc]
      apply ih
      rw [show 2^h*(3*t)=3*(2^h*t) by ac_rfl]
      simp only [step,even,↓reduceIte]
      omega

private structure Base (H r w K : Nat) : Prop where
  large : 2<w
  unit : w%6=1
  bin : 2^(H+1) ∣ 3^r*w+1
  tern : 3^K ∣ w-1

private theorem choose_base (H r L K : Nat) (hk : 0<K) :
    ∃ w>L, Base H r w K := by
  let A := 3^r
  let M := 3^(r+K)
  obtain ⟨t,ht⟩ := MixedBarrier.three_odd (r+K)
  obtain ⟨v,z,ep⟩ := MixedBarrier.inverse_two (H+1) M t ht
  let q := 2^(H+1)
  let D := z*(A+1)+q*(L+3)
  let u := v*(A+1)+M*(L+3)
  let w := 1+3^K*D
  have id : q*u=A*w+1 := by
    change q*v=1+M*z at ep
    dsimp [u,w,D]
    rw [Nat.mul_add,←Nat.mul_assoc,ep,show M=A*3^K from Nat.pow_add ..]
    grind
  have size : L+3≤q*(L+3) := Nat.le_mul_of_pos_left _ (Nat.two_pow_pos _)
  have sizeD : L+3≤D := by dsimp [D]; omega
  have big : D≤3^K*D := Nat.le_mul_of_pos_left _ (Nat.pow_pos (by decide))
  have par : w%2=1 := by
    have ev : q*u%2=0 := by dsimp [q]; rw [Nat.pow_succ,Nat.mul_right_comm]; omega
    rw [id,Nat.add_mod,Nat.mul_mod,show A%2=1 by simp [A,Nat.pow_mod]] at ev
    omega
  have m3 : w%3=1 := by
    obtain ⟨i,ei⟩ := Nat.exists_eq_succ_of_ne_zero (show K≠0 by omega)
    dsimp [w]; rw [ei,Nat.pow_succ,Nat.mul_right_comm]; omega
  exact ⟨w,by dsimp [w]; omega,by dsimp [w]; omega,by omega,⟨u,id.symm⟩,
    ⟨D,by simp [w]⟩⟩

private theorem converging_base (H r L K : Nat) (hk : 0<K) :
    ∃ w>L, Base H r w K ∧ ReachesOne (3^r*w) := by
  obtain ⟨b,bl,base⟩ := choose_base H r L K hk
  obtain ⟨u,eq⟩ := base.bin
  have up : 0<u := by cases u <;> simp_all
  let q := 2*(3^H*u)-1
  have pu := Nat.mul_pos (Nat.pow_pos (n:=H) (by decide : 0<3)) up
  have odd : q%2=1 := by dsimp [q]; omega
  obtain ⟨e,d,_,_,exit⟩ := Shadow.one_gap_cylinder (t:=1) odd (by decide) (by decide) (H+r+K)
  let w := b+2^(H+1)*(3^K*d)
  let U := u+3^r*(3^K*d)
  have ident : 3^r*w+1=2^(H+1)*U := by
    dsimp [w,U]
    calc
      _ = (3^r*b+1) + 2^(H+1)*(3^r*(3^K*d)) := by rw [Nat.mul_add]; ac_rfl
      _ = _ := by rw [eq,Nat.mul_add]
  have big := base.large
  have bw : b≤w := Nat.le_add_right _ _
  have dw : w-1=(b-1)+3^K*(2^(H+1)*d) := by
    dsimp [w]; rw [show 2^(H+1)*(3^K*d)=3^K*(2^(H+1)*d) by ac_rfl]; omega
  have tern : 3^K∣w-1 := by rw [dw]; exact Nat.dvd_add base.tern ⟨_,rfl⟩
  have three : 3∣w-1 := Nat.dvd_trans (Nat.pow_dvd_pow 3 (show 1≤K by omega)) tern
  have wodd : w%2=1 := by
    have even : 2^(H+1)*U%2=0 := by rw [Nat.pow_succ,Nat.mul_right_comm]; omega
    rw [←ident,Nat.add_mod,Nat.mul_mod,show 3^r%2=1 by simp [Nat.pow_mod]] at even
    omega
  refine ⟨w,by omega,⟨by omega,by omega,⟨U,ident⟩,tern⟩,H+e,?_⟩
  have UP : 0<U := by dsimp [U]; omega
  have arg : 3^r*w=2^H*(2*U)-1 := by
    rw [Nat.pow_succ,Nat.mul_assoc] at ident; omega
  rw [run_add,arg,TowerFrontier.odd_steps _ _ (by omega : 0<2*U)]
  have target : 3^H*(2*U)-1=q+2*(3^(H+r+K)*d) := by
    dsimp [q,U]
    rw [Nat.mul_add,Nat.mul_add,Nat.pow_add 3 (H+r),Nat.pow_add 3 H]
    have left : 3^H*(2*u)=2*(3^H*u) := by ac_rfl
    have right : 3^H*(2*(3^r*(3^K*d)))=2*(3^H*3^r*3^K*d) := by ac_rfl
    rw [left,right]
    omega
  rw [target,exit.follow]

private theorem source_word {H r w K h : Nat} (base : Base H r w K) (within : h≤H) :
    2^h*(run h (3^r*w)+1)=3^h*(3^r*w+1) := by
  obtain ⟨v,hv⟩ := Nat.dvd_trans (Nat.pow_dvd_pow 2 (show h≤H+1 by omega)) base.bin
  have nv : 3^r*w=2^h*v-1 := by omega
  have vp : 0<v := by
    cases v with
    | zero => simp at hv
    | succ v => omega
  rw [nv,TowerFrontier.odd_steps _ _ vp]
  have pv := Nat.mul_pos (Nat.two_pow_pos h) vp
  have qv := Nat.mul_pos (Nat.pow_pos (n:=h) (by decide : 0<3)) vp
  rw [show 3^h*v-1+1=3^h*v by omega,show 2^h*v-1+1=2^h*v by omega]
  ac_rfl

private theorem strip_dvd {s j f b v : Nat} (eq : 3^s*b=3^j*f+v)
    (pos : 0<v) (small : v<3^j) : 3^s∣v := by
  have dv (n : Nat) (ns : n≤s) (nj : n≤j) : 3^n∣v := by
    have lhs : 3^n∣3^s*b := Nat.dvd_trans (Nat.pow_dvd_pow 3 ns) ⟨b,rfl⟩
    rw [eq] at lhs
    apply (Nat.dvd_add_iff_right (Nat.dvd_trans (Nat.pow_dvd_pow 3 nj) ⟨f,rfl⟩)).mpr lhs
  by_cases sj : s≤j
  · exact dv s (by omega) sj
  · have := Nat.le_of_dvd pos (dv j (by omega) (by omega))
    omega

private theorem small_virtual {d h H r j v : Nat} (clock : d+h≤H)
    (budget : H+r+1≤j) (le : v<2^d*3^h*(3^r+1)) : v<3^j := by
  have last : 3^r+1≤3^(r+1) := by
    rw [Nat.pow_succ]; have := Nat.pow_pos (n:=r) (by decide : 0<3); omega
  calc
    v < 2^d*3^h*(3^r+1) := le
    _ ≤ 3^d*3^h*3^(r+1) := Nat.mul_le_mul
      (Nat.mul_le_mul_right _ (Nat.pow_le_pow_left (by decide : 2≤3) _)) last
    _ = 3^(d+h+(r+1)) := by rw [Nat.pow_add 3 (d+h) (r+1), Nat.pow_add 3 d h]
    _ ≤ 3^j := Nat.pow_le_pow_right (by decide) (by omega)

private theorem near_power {H r w d h s b : Nat} (base : Base H r w (2*H+r+3))
    (clock : d+h≤H) (hit : run h (3^r*w)=run (d+h) (3^s*b))
    (lower : b<w ∨ b=w ∧ s<r) :
    ∃ g : Nat, 2^d < 3^g ∧ 3^r*(3^g-2^d) < 2^d ∧
      3^g*(b-1)=2^d*(w-1) ∧ 3^r*(w-1)<(3^r+1)*(b-1) := by
  let y := 3^s*b
  let z := run d y
  let l := count d y
  let p := count h z
  let n := p+l
  let A := 3^(h+r)
  let J := 2*H+r+3-n
  have nl : n≤H := by
    dsimp [n,p,l]; have := count_le h z; have := count_le d y; omega
  have jsize : H+r+1≤J := by dsimp [J]; omega
  obtain ⟨D,hD⟩ := base.tern
  have ww : w=1+3^n*(3^J*D) := by
    have group : 3^n*(3^J*D)=3^(2*H+r+3)*D := by
      rw [←Nat.mul_assoc,←Nat.pow_add,show n+J=2*H+r+3 by dsimp [J]; omega]
    rw [group,←hD]; have := base.large; omega
  let U := A*(3^J*D)
  have wp : A+3^n*U=A*w := by
    calc
      A+3^n*U = A*(1+3^n*(3^J*D)) := by dsimp [U]; rw [Nat.mul_add,Nat.mul_one]; ac_rfl
      _ = A*w := by rw [←ww]
  obtain ⟨c,ec,lc⟩ := carry h z
  obtain ⟨e,ee,_⟩ := carry d y
  change 2^h*run h z=3^p*z+c at ec
  change 2^d*z=3^l*y+e at ee
  have rr : run h (3^r*w)=run h z := by simpa [run_add,z,y] using hit
  have source := source_word base (show h≤H by omega)
  rw [rr,Nat.mul_add,Nat.mul_one,ec] at source
  have key : 3^p*z+c+2^h=3^n*U+(A+3^h) := by
    calc
      _ = 3^h*(3^r*w+1) := source
      _ = A*w+3^h := by dsimp [A]; rw [Nat.mul_add,Nat.mul_one,Nat.pow_add,Nat.mul_assoc]
      _ = _ := by rw [←wp]; omega
  have posShift : 2^d*U<y := by
    by_cases small : y≤2^d*U
    · have bound : z≤3^l*U := upper small
      have bad := Nat.mul_le_mul_left (3^p) bound
      rw [←Nat.mul_assoc,←Nat.pow_add] at bad
      change 3^p*z≤3^n*U at bad
      have ap : 0<A := Nat.pow_pos (by decide)
      omega
    · omega
  let v := y-2^d*U
  have vpos : 0<v := by dsimp [v]; omega
  have yrep : y=2^d*U+v := by dsimp [v]; omega
  have id : 3^n*v+3^p*e+2^d*(c+2^h)=2^d*(A+3^h) := by
    have flat : 3^p*(2^d*z)+2^d*(c+2^h)
        = 3^n*(2^d*U)+2^d*(A+3^h) := by
      calc
        _ = 2^d*(3^p*z+c+2^h) := by rw [Nat.mul_add,Nat.mul_add,Nat.mul_add]; ac_rfl
        _ = _ := by rw [key,Nat.mul_add]; ac_rfl
    rw [ee,Nat.mul_add,←Nat.mul_assoc,←Nat.pow_add] at flat
    change 3^n*y+3^p*e+2^d*(c+2^h)=3^n*(2^d*U)+2^d*(A+3^h) at flat
    rw [yrep,Nat.mul_add] at flat
    omega
  have ah : A+3^h=3^h*(3^r+1) := by dsimp [A]; rw [Nat.pow_add,Nat.mul_add,Nat.mul_one]
  have strict : 3^n*v < 2^d*3^h*(3^r+1) := by
    have pos := Nat.mul_pos (Nat.two_pow_pos d) (show 0<c+2^h by have := Nat.two_pow_pos h; omega)
    rw [ah,←Nat.mul_assoc] at id
    omega
  have vsmall := small_virtual (v:=v) clock jsize (Nat.lt_of_le_of_lt
    (Nat.le_mul_of_pos_left _ (Nat.pow_pos (by decide : 0<3))) strict)
  have sh : 3^s*b=3^J*(2^d*A*D)+v := by
    change y=_; rw [yrep]; dsimp [U]; ac_rfl
  have vd := strip_dvd sh vpos vsmall
  have sv := Nat.le_of_dvd vpos vd
  let B := 3^(n+s)
  have whole : B*b=2^d*A*(w-1)+3^n*v := by
    have act : B*b=3^n*y := by dsimp [B,y]; rw [Nat.pow_add,Nat.mul_assoc]
    rw [act,yrep,Nat.mul_add]
    have conv : 3^n*U=A*(w-1) := by rw [ww]; simp only [Nat.add_sub_cancel_left,U]; ac_rfl
    rw [show 3^n*(2^d*U)=2^d*(3^n*U) by ac_rfl,conv,Nat.mul_assoc]
  have bet : B≤3^n*v := by dsimp [B]; rw [Nat.pow_add]; exact Nat.mul_le_mul_left _ sv
  have neq : 2^d*A<B := by
    by_cases lt : 2^d*A<B
    · exact lt
    have rhs : B*w≤2^d*A*(w-1)+3^n*v := by
      calc
        _ = B*(w-1)+B := by rw [←Nat.mul_succ,show (w-1).succ=w by have := base.large; omega]
        _ ≤ _ := Nat.add_le_add (Nat.mul_le_mul_right _ (by omega)) bet
    have bw : w≤b := Nat.le_of_mul_le_mul_left (by rwa [whole]) (Nat.pow_pos (by decide))
    obtain ⟨beq,sr⟩ : b=w ∧ s<r := lower.elim (fun x => False.elim (by omega)) (fun x => x)
    have eq : 2^d*A=B := by
      by_cases hi : B<2^d*A
      · have more := Nat.mul_lt_mul_of_pos_right hi (show 0<w-1 by have := base.large; omega)
        have lift := Nat.add_lt_add_of_lt_of_le more bet
        rw [←Nat.mul_succ,show (w-1).succ=w by have := base.large; omega,←whole,beq] at lift
        omega
      · omega
    cases d with
    | zero =>
      have er : 3^(h+r)=3^(n+s) := by simpa [A,B] using eq
      have lowerExp : n+s<h+r := by
        have : n≤h := by simpa [n,l,count] using count_le h z
        omega
      exact False.elim ((Nat.ne_of_lt (Nat.pow_lt_pow_right (by decide : 1<3) lowerExp)) er.symm)
    | succ d =>
      have even : (2^(d+1)*A)%2=0 := by rw [Nat.pow_succ,Nat.mul_right_comm]; omega
      have odd : B%2=1 := by simp [B,Nat.pow_mod]
      omega
  have Bsmall : B<2^d*3^h*(3^r+1) := Nat.lt_of_le_of_lt bet strict
  have ab : A<B := Nat.lt_of_le_of_lt (Nat.le_mul_of_pos_left _ (Nat.two_pow_pos d)) neq
  have ex : h+r<n+s := by
    by_cases hh : n+s≤h+r
    · have bad := Nat.pow_le_pow_right (by decide : 0<3) hh
      exact False.elim (Nat.not_le_of_gt ab bad)
    · omega
  let g := n+s-(h+r)
  have Bg : B=3^g*A := by dsimp [B,A]; rw [←Nat.pow_add,show g+(h+r)=n+s by dsimp [g]; omega]
  rw [Bg] at neq Bsmall
  have dl : 2^d<3^g := Nat.lt_of_mul_lt_mul_right neq
  have star : 3^h*(3^g*3^r) < 3^h*(2^d*(3^r+1)) := by
    simpa only [A,Nat.pow_add,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using Bsmall
  have cut := Nat.lt_of_mul_lt_mul_left star
  have cut' : 3^r*(3^g-2^d)<2^d := by
    have dp := Nat.two_pow_pos d
    rw [Nat.mul_sub]
    rw [Nat.mul_add,Nat.mul_one] at cut
    rw [Nat.mul_comm (3^g),Nat.mul_comm (2^d)] at cut
    omega
  obtain ⟨β,ev⟩ := vd
  have vb : 3^n*v=B*β := by rw [ev,show B=3^n*3^s from Nat.pow_add ..,Nat.mul_assoc]
  have one : β=1 := by
    have room : 3^r+1≤2*3^r := by have := Nat.pow_pos (n:=r) (by decide : 0<3); omega
    have ext := Nat.mul_le_mul_left (2^d*3^h) room
    have bound : 3^n*v<2*(2^d*A) := Nat.lt_of_lt_of_le strict
      (by simpa only [A,Nat.pow_add,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using ext)
    have strictBase : 2^d*A<B := by rwa [Bg]
    by_cases hi : 2≤β
    · have lo := Nat.mul_le_mul_left B hi
      rw [←vb] at lo
      omega
    · by_cases zero : β=0
      · simp [zero] at ev; omega
      · omega
  have bp : 0<b := by
    by_cases no : b=0
    · simp [no] at whole; have := Nat.pow_pos (n:=n) (by decide : 0<3)
      have := Nat.mul_pos this vpos; omega
    · omega
  have law : 3^g*(b-1)=2^d*(w-1) := by
    have eq : B*(b-1)=2^d*A*(w-1) := by
      rw [vb,one,Nat.mul_one] at whole
      rw [Nat.mul_sub,Nat.mul_one]; omega
    apply Nat.eq_of_mul_eq_mul_left (show 0<A from Nat.pow_pos (by decide))
    simpa only [Bg,Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using eq
  have posB : 0<b-1 := by
    have p0 := Nat.mul_pos (Nat.two_pow_pos d) (show 0<w-1 by have := base.large; omega)
    by_cases z : b-1=0
    · simp [z] at law; omega
    · omega
  have tight : 3^r*(w-1)<(3^r+1)*(b-1) := by
    have sieve : 3^r*3^g < 2^d*(3^r+1) := by
      rw [Nat.mul_comm (3^r)]; exact cut
    have order := Nat.mul_lt_mul_of_pos_right sieve posB
    rw [Nat.mul_assoc,law] at order
    apply Nat.lt_of_mul_lt_mul_left (a:=2^d)
    simpa only [Nat.mul_assoc,Nat.mul_comm,Nat.mul_left_comm] using order
  exact ⟨g,dl,cut',law,tight⟩

/-- If the first arm follows the odd branch for longer than the entire second
    prefix, the ternary-free portion of the second start exceeds the first start. -/
theorem shorter_arm {x h k s b : Nat} (short : k<h)
    (word : 2^h*(run h x+1)=3^h*(x+1))
    (hit : run h x=run k (3^s*b)) : x<b := by
  let d := h-k
  have hd : 0<d := by dsimp [d]; omega
  have hrep : h=d+k := by dsimp [d]; omega
  let p := count k (3^s*b)
  obtain ⟨c,eq,bc⟩ := carry k (3^s*b)
  change 2^k*run k (3^s*b)=3^p*(3^s*b)+c at eq
  have full : 2^d*(3^(p+s)*b+(c+2^k))=3^h*(x+1) := by
    calc
      _ = 2^d*(2^k*(run k (3^s*b)+1)) := by rw [Nat.mul_add (2^k),Nat.mul_one,eq,Nat.pow_add]; ac_rfl
      _ = 2^h*(run h x+1) := by rw [hit,←Nat.mul_assoc,←Nat.pow_add,←hrep]
      _ = _ := word
  have summed : p+s≤k := by
    by_cases g : p+s≤k
    · exact g
    have dv : 3^(k+1)∣3^h*(x+1) := Nat.dvd_trans (Nat.pow_dvd_pow 3 short) ⟨_,rfl⟩
    rw [←full] at dv
    have cop := ((show Nat.Coprime 3 2 by decide).pow_left (k+1)).pow_right d
    have whole := cop.dvd_of_dvd_mul_left dv
    have lhs : 3^(k+1)∣3^(p+s)*b := Nat.dvd_trans (Nat.pow_dvd_pow 3 (by omega)) ⟨_,rfl⟩
    have off := (Nat.dvd_add_iff_right lhs).mpr whole
    have pos : 0<c+2^k := by have := Nat.two_pow_pos k; omega
    have high := Nat.le_of_dvd pos off
    have larger := Nat.pow_lt_pow_right (by decide : 1<3) (show k<k+1 by omega)
    omega
  have bounded : 3^(p+s)*b+(c+2^k) ≤ 3^k*(b+1) := by
    rw [Nat.mul_add,Nat.mul_one]
    exact Nat.add_le_add (Nat.mul_le_mul_right _ (Nat.pow_le_pow_right (by decide) summed)) bc
  have scale : 3^k*(3^d*(x+1)) ≤ 3^k*(2^d*(b+1)) := by
    calc
      _ = 3^h*(x+1) := by rw [hrep,Nat.pow_add]; ac_rfl
      _ = _ := full.symm
      _ ≤ 2^d*(3^k*(b+1)) := Nat.mul_le_mul_left _ bounded
      _ = _ := by ac_rfl
  have cut := Nat.le_of_mul_le_mul_left scale (Nat.pow_pos (by decide : 0<3))
  have gt := Nat.mul_lt_mul_of_pos_right (Nat.pow_lt_pow_left (by decide : 2<3)
    (show d≠0 by omega)) (show 0<x+1 by omega)
  have imp := Nat.lt_of_mul_lt_mul_left (Nat.lt_of_lt_of_le gt cut)
  omega

/-- A candidate can be a smooth multiple of any strictly smaller positive
    base, or a lower ternary rank at the original base. -/
@[expose] def Lower (w r b s : Nat) : Prop := b<w ∨ b=w ∧ s<r

/-- Every merger from the supplied rank to the entire lower cone, even with
    independent clocks and arbitrary competitor dyadic and ternary powers,
    needs a strictly positive effective clock lead near a power of three. -/
theorem prescribed_cone_resonance (r H L : Nat) :
    ∃ w>L, w%6=1 ∧ ReachesOne (3^r*w) ∧ ∀ h ≤ H, ∀ k ≤ H, ∀ a s b,
      Lower w r b s → run h (3^r*w)=run k (2^a*(3^s*b)) →
      ∃ d g : Nat, k=a+h+d ∧ 2^d<3^g ∧ 3^r*(3^g-2^d)<2^d ∧
        3^g*(b-1)=2^d*(w-1) ∧ 3^r*(w-1)<(3^r+1)*(b-1) := by
  obtain ⟨w,wl,base,good⟩ := converging_base H r L (2*H+r+3) (by omega)
  refine ⟨w,wl,base.unit,good,?_⟩
  intro h hh k hk a s b low hit
  have shortHalf : a≤k := by
    by_cases enough : a≤k
    · exact enough
    let f := a-k
    have fp : 0<f := by dsimp [f]; omega
    have fac : a=k+f := by dsimp [f]; omega
    have evenTerm : run k (2^a*(3^s*b))%2=0 := by
      rw [fac,Nat.pow_add,Nat.mul_assoc,halve]
      obtain ⟨j,hj⟩ := Nat.exists_eq_succ_of_ne_zero (show f≠0 by omega)
      rw [hj,Nat.pow_succ,Nat.mul_right_comm]; omega
    obtain ⟨v,hv⟩ := Nat.dvd_trans (Nat.pow_dvd_pow 2 (show h+1≤H+1 by omega)) base.bin
    have vp : 0<v := by cases v <;> simp_all
    have factor : 2^(h+1)*v=2^h*(2*v) := by rw [Nat.pow_succ,Nat.mul_assoc]
    have oddTerm : run h (3^r*w)%2=1 := by
      rw [factor] at hv
      rw [show 3^r*w=2^h*(2*v)-1 by omega,TowerFrontier.odd_steps _ _ (by omega)]
      rw [show 3^h*(2*v)=2*(3^h*v) by ac_rfl]
      have := Nat.mul_pos (Nat.pow_pos (n:=h) (by decide : 0<3)) vp
      omega
    rw [hit] at oddTerm
    omega
  let j := k-a
  have jr : k=a+j := by dsimp [j]; omega
  have actual : run h (3^r*w)=run j (3^s*b) := by simpa only [jr,run_add,halve] using hit
  have after : h≤j := by
    by_cases ok : h≤j
    · exact ok
    have early := shorter_arm (by omega : j<h) (source_word base hh) actual
    have large := Nat.le_mul_of_pos_left w (Nat.pow_pos (n:=r) (by decide : 0<3))
    rcases low with lt|⟨same,_⟩ <;> omega
  let d := j-h
  have shift : j=d+h := by dsimp [d]; omega
  obtain ⟨g,above,narrow,law,tight⟩ := near_power base (by omega : d+h≤H) (by rwa [←shift]) low
  exact ⟨d,g,by omega,above,narrow,law,tight⟩

/-- A whole finite-clock lower-cone search fails at infinitely many ordinary
    bases at any relatively high supplied rank. -/
theorem no_lower_cone (r H L : Nat) (range : 2^H≤3^r) :
    ∃ w>L, w%6=1 ∧ ReachesOne (3^r*w) ∧ ∀ h ≤ H, ∀ k ≤ H, ∀ a s b,
      Lower w r b s → run h (3^r*w)≠run k (2^a*(3^s*b)) := by
  obtain ⟨w,large,unit,good,barrier⟩ := prescribed_cone_resonance r H L
  refine ⟨w,large,unit,good,?_⟩
  intro h hh k hk a s b low hit
  obtain ⟨d,g,time,less,gap,_,_⟩ := barrier h hh k hk a s b low hit
  have pos : 0<3^g-2^d := by omega
  have cost := Nat.le_mul_of_pos_right (3^r) pos
  have hw := Nat.pow_le_pow_right (by decide : 0<2) (show d≤H by omega)
  omega

#print axioms shorter_arm
#print axioms prescribed_cone_resonance
#print axioms no_lower_cone

end Collatz.Itinerary.HourTower
