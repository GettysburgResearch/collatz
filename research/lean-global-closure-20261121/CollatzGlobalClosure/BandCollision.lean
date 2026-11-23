import ForwardSection
import CollatzGlobalClosure.BandWord

/-! Analytic and arithmetic placement for cofinal equal-feature collisions.
No unproved assertion is imported as an axiom. -/

namespace CollatzBandCollision

open Real CollatzShell CollatzShell.ForwardSection

theorem ratio_of_log_close {A D u : ℝ} (Ap : 0<A) (Dp : 0<D) (hu : 2≤u)
    (close : |log D-log A|≤1/u) :
    (u-1)*A≤u*D ∧ u*D≤(u+2)*A := by
  let r := D/A
  have rp : 0<r := div_pos Dp Ap
  have up : 0<u := by linarith
  have eq : log r=log D-log A := log_div Dp.ne' Ap.ne'
  have lo : -(1/u)≤log r := by rw [eq]; exact (abs_le.mp close).1
  have hi : log r≤1/u := by rw [eq]; exact (abs_le.mp close).2
  have below := log_le_sub_one_of_pos rp
  have above := one_sub_inv_le_log_of_pos rp
  have low : u-1≤u*r := by
    have h := mul_le_mul_of_nonneg_left (lo.trans below) up.le
    field_simp at h
    nlinarith
  have high : (u-1)*r≤u := by
    have h := mul_le_mul_of_nonneg_right (above.trans hi) (mul_pos up rp).le
    field_simp at h
    nlinarith
  have r2 : r≤2 := by
    by_contra! h
    have prod := mul_nonneg (show 0≤u-2 by linarith) (show 0≤r-1 by linarith)
    nlinarith
  have high' : u*r≤u+2 := by nlinarith
  constructor
  · have h := mul_le_mul_of_nonneg_right low Ap.le
    dsimp [r] at h
    field_simp at h
    nlinarith
  · have h := mul_le_mul_of_nonneg_right high' Ap.le
    dsimp [r] at h
    field_simp at h
    nlinarith

theorem power_ratio_bounds {N p t : Nat} (hN : 1≤N)
    (close : |(p:ℝ)*alpha-t|≤1/((N:ℝ)+1)) :
    N*3^p≤(N+1)*2^t ∧ (N+1)*2^t≤(N+3)*3^p := by
  have lp : 0<log 2 := log_pos (by norm_num)
  have pn : 0<(N:ℝ)+1 := by positivity
  have id : log ((2:ℝ)^t)-log ((3:ℝ)^p)=((t:ℝ)-p*alpha)*log 2 := by
    rw [log_pow,log_pow]
    unfold alpha logb
    field_simp
  have lc : |log ((2:ℝ)^t)-log ((3:ℝ)^p)|≤1/((N:ℝ)+1) := by
    rw [id,abs_mul,abs_of_pos lp,abs_sub_comm]
    calc _ ≤ (1/((N:ℝ)+1))*log 2 := mul_le_mul_of_nonneg_right close lp.le
         _ ≤ _ := by nlinarith [log_two_bounds.2,show 0≤1/((N:ℝ)+1) by positivity]
  have h := ratio_of_log_close (A:=((3:ℝ)^p)) (D:=((2:ℝ)^t))
    (by positivity) (by positivity) (by exact_mod_cast (show 2≤N+1 by omega)) lc
  constructor
  · have l : (N:ℝ)*(3:ℝ)^p≤((N:ℝ)+1)*(2:ℝ)^t := by nlinarith [h.1]
    exact_mod_cast l
  · have u : ((N:ℝ)+1)*(2:ℝ)^t≤((N:ℝ)+3)*(3:ℝ)^p := by nlinarith [h.2]
    exact_mod_cast u

theorem rotation_three_halves : (3:ℝ)/2<alpha := by
  have h := logb_lt_logb (by norm_num : (1:ℝ)<2)
    (by norm_num : (0:ℝ)<8) (by norm_num : (8:ℝ)<9)
  have a : logb 2 (8:ℝ)=3 := by
    rw [show (8:ℝ)=2^3 by norm_num,logb_pow,logb_two]
    norm_num
  have b : logb 2 (9:ℝ)=2*alpha := by
    rw [show (9:ℝ)=3^2 by norm_num,logb_pow]
    rfl
  rw [a,b] at h
  linarith

theorem usable_rotation (N : Nat) (hN : 64≤N) :
    ∃ p t : Nat, 4≤p ∧ p≤N ∧ p+2≤t ∧ t≤2*N ∧
      N*3^p≤(N+1)*2^t ∧ (N+1)*2^t≤(N+3)*3^p := by
  obtain ⟨t,p,pp,pN,_,barrier,close⟩ := rotation_grid N (by omega)
  have p4 : 4≤p := by
    by_contra! h
    have bound := Nat.pow_le_pow_right (by decide : 0<4) (show p≤3 by omega)
    norm_num at bound
    omega
  have nr : (0:ℝ)<N+1 := by positivity
  have small : 1/((N:ℝ)+1)<1 := (div_lt_one nr).mpr (by exact_mod_cast (show 1<N+1 by omega))
  have pr : (4:ℝ)≤p := by exact_mod_cast p4
  have pl : (0:ℝ)<p := by exact_mod_cast pp
  have low : (p:ℝ)+1<t := by
    have bound := mul_lt_mul_of_pos_left rotation_three_halves pl
    linarith [(abs_le.mp close).2]
  have high : (t:ℝ)<2*p+1 := by
    have bound := mul_lt_mul_of_pos_left rotation_bounds.2 pl
    linarith [(abs_le.mp close).1]
  have tl : p+2≤t := by
    have : p+1<t := by exact_mod_cast low
    omega
  have tu : t≤2*N := by
    have : t<2*p+1 := by exact_mod_cast high
    omega
  exact ⟨p,t,p4,pN,tl,tu,power_ratio_bounds (by omega) close⟩

theorem octave_padding (N p : Nat) (hN : 64≤N) (hp : p≤N) :
    N+1≤2^(8*N)/(N+1) ∧ 8*3^p≤2^(8*N)/(N+1) := by
  have up : 0<N+1 := by omega
  have u : N+1≤2^N := Nat.lt_two_pow_self
  have sq : (N+1)*(N+1)≤2^(8*N) := by
    calc _ ≤ 2^N*2^N := Nat.mul_le_mul u u
         _ = 2^(2*N) := by rw [←pow_add]; congr 1; omega
         _ ≤ _ := Nat.pow_le_pow_right (by decide) (by omega)
  have eight : 8≤2^N := by
    have h := Nat.pow_le_pow_right (by decide : 0<2) (show 3≤N by omega)
    norm_num at h
    exact h
  have three : 3^p≤2^(2*N) := by
    calc _ ≤ 3^N := Nat.pow_le_pow_right (by decide) hp
         _ ≤ 4^N := Nat.pow_le_pow_left (by decide) _
         _ = _ := by rw [pow_mul]; norm_num
  have stride : (8*3^p)*(N+1)≤2^(8*N) := by
    calc _ ≤ (2^N*2^(2*N))*2^N := Nat.mul_le_mul (Nat.mul_le_mul eight three) u
         _ = 2^(4*N) := by rw [←pow_add,←pow_add]; congr 1; omega
         _ ≤ _ := Nat.pow_le_pow_right (by decide) (by omega)
  exact ⟨(Nat.le_div_iff_mul_le up).mpr sq,(Nat.le_div_iff_mul_le up).mpr stride⟩

theorem placed_source_bounds {N P Q A D C E n m : Nat}
    (hN : 64≤N) (hq : N+1≤Q) (hP : P≤(N+2)*Q) (Ap : 0<A)
    (ratioLo : N*A≤(N+1)*D) (ratioHi : (N+1)*D≤(N+3)*A)
    (eq : A*n+C=D*m+E) (c : C≤5*A) (e : E≤2*A)
    (ml : P+4*Q≤m) (mu : m≤P+5*Q) :
    P≤n ∧ n≤P+8*Q := by
  have low : N*m≤(N+1)*n+5*(N+1) := by
    apply Nat.le_of_mul_le_mul_left (c:=A) ?_ Ap
    have h1 := Nat.mul_le_mul_right m ratioLo
    have h2 := Nat.mul_le_mul_left (N+1) c
    have h3 := congrArg ((N+1)*·) eq
    nlinarith only [h1,h2,h3]
  have high : (N+1)*n≤(N+3)*m+2*(N+1) := by
    apply Nat.le_of_mul_le_mul_left (c:=A) ?_ Ap
    have h1 := Nat.mul_le_mul_right m ratioHi
    have h2 := Nat.mul_le_mul_left (N+1) e
    have h3 := congrArg ((N+1)*·) eq
    nlinarith only [h1,h2,h3]
  have n2 : N+2≤2*N := by omega
  have hP2 : P≤2*N*Q := hP.trans (Nat.mul_le_mul_right Q n2)
  have six : 5*(N+1)≤2*N*Q := by
    have h := Nat.mul_le_mul_right Q (show 5≤2*N by omega)
    omega
  have big : P+5*(N+1)≤4*N*Q := by nlinarith only [hP2,six]
  constructor
  · have h := Nat.mul_le_mul_left N ml
    apply Nat.le_of_mul_le_mul_left (c:=N+1) ?_ (by omega)
    nlinarith only [h,low,big]
  · have h := Nat.mul_le_mul_left (N+3) mu
    have margin := Nat.mul_le_mul_right Q (show 14≤N+1 by omega)
    apply Nat.le_of_mul_le_mul_left (c:=N+1) ?_ (by omega)
    nlinarith only [h,high,hP,hq,margin]

theorem marked_of_octave_window {N x : Nat} (hN : 64≤N) (odd : x%4=1)
    (low : 2^(8*N)≤x) (high : x≤2^(8*N)+8*(2^(8*N)/(N+1))) :
    Marked x ∧ x.log2=8*N := by
  let P := 2^(8*N)
  let Q := P/(N+1)
  have pq : (N+1)*Q≤P := Nat.mul_div_le P (N+1)
  have qpos : 0<Q := by
    have h := (octave_padding N 0 hN (by omega)).1
    change N+1≤Q at h
    omega
  have gap : 8*Q<P := by nlinarith [Nat.mul_le_mul_right Q (show 9≤N+1 by omega)]
  have xp : 0<x := by have p := Nat.two_pow_pos (8*N); omega
  have hi : x<2^(8*N+1) := by
    rw [pow_succ]
    change x≤P+8*Q at high
    omega
  have lg : x.log2=8*N := (Nat.log2_eq_iff xp.ne').mpr ⟨low,hi⟩
  refine ⟨⟨by omega,?_⟩,lg⟩
  unfold InSection
  rw [lg]
  have off : x-P≤8*Q := by change x≤P+8*Q at high; omega
  change (8*N+1)*(x-P)≤70*P
  calc _ ≤ (8*N+1)*(8*Q) := Nat.mul_le_mul_left _ off
       _ ≤ (8*(N+1))*(8*Q) := Nat.mul_le_mul_right _ (by omega)
       _ = 64*((N+1)*Q) := by ring
       _ ≤ 64*P := Nat.mul_le_mul_left _ pq
       _ ≤ 70*P := by omega

set_option maxRecDepth 4096

/-- Above every cutoff there is an actual nonconstant path between marks with
the same binary exponent and trailing-one depth one.  The extra source bound
keeps every intermediate ordinary state strictly above the cutoff. -/
theorem cofinal_equal_features (B : Nat) :
    ∃ n m t : Nat, B<n ∧ B<m ∧ 1<n ∧ Marked n ∧ Marked m ∧
      n.log2=m.log2 ∧ n%4=1 ∧ m%4=1 ∧ 0<t ∧ orbit t n=m ∧ n≠m ∧
      (B+1)*2^t≤n := by
  let N := B+64
  let P := 2^(8*N)
  let Q := P/(N+1)
  have hN : 64≤N := by dsimp [N]; omega
  obtain ⟨p,t,p4,pN,pt,tN,rl,ru⟩ := usable_rotation N hN
  obtain ⟨hq,hs⟩ := octave_padding N p hN pN
  change N+1≤Q at hq
  change 8*3^p≤Q at hs
  have qP : Q≤P := Nat.div_le_self _ _
  have large : 5*3^p≤P+4*Q := by omega
  obtain ⟨n,m,ml',mu',m4,n4,hit,eq⟩ :=
    CollatzShell.BandWord.section_word_in_interval p t (P+4*Q) (by omega) pt large
  have ml : P+4*Q≤m := ml'.le
  have mu : m≤P+5*Q := by omega
  have rem := Nat.mod_lt P (by omega : 0<N+1)
  have div := Nat.div_add_mod P (N+1)
  change (N+1)*Q+P%(N+1)=P at div
  have Pq : P≤(N+2)*Q := by nlinarith only [div,rem,hq]
  have Ap : 0<(3:Nat)^p := by positivity
  have cb : 5*3^(p-1)≤5*3^p := Nat.mul_le_mul_left 5
    (Nat.pow_le_pow_right (by decide) (by omega))
  have eb : 2^(p+1)≤2*3^p := by
    rw [pow_succ]
    have h := Nat.pow_le_pow_left (by decide : (2:Nat)≤3) p
    omega
  obtain ⟨nl,nu⟩ := placed_source_bounds hN hq Pq Ap rl ru eq cb eb ml mu
  obtain ⟨nm,nlog⟩ := marked_of_octave_window hN n4 nl nu
  obtain ⟨mm,mlog⟩ := marked_of_octave_window hN m4 (by omega : P≤m)
    (by omega : m≤P+8*Q)
  have above : B<P := by
    have h := Nat.lt_two_pow_self (n:=8*N)
    dsimp [P,N] at *
    omega
  have np : 1<n := by
    have h := Nat.lt_two_pow_self (n:=8*N)
    change 8*N<P at h
    omega
  have tp : 0<t := by omega
  have oddA : (3^p)%2=1 := by simp [Nat.pow_mod]
  have evenD : (2^t)%2=0 := by simp [Nat.pow_mod,zero_pow tp.ne']
  have different : (3:Nat)^p≠2^t := by intro h; rw [h] at oddA; omega
  have csmall : 5*3^(p-1)<n := by omega
  have esmall : 2^(p+1)<n := by omega
  have ne : n≠m := by
    intro same
    rw [←same] at eq
    rcases lt_or_gt_of_ne different with lt|gt
    · have h := Nat.mul_le_mul_right n (show 3^p+1≤2^t by omega)
      simp only [Nat.add_mul,Nat.one_mul] at h
      have h' : 3^p*n+n≤3^p*n+5*3^(p-1) := by
        calc _ ≤ 2^t*n := h
             _ ≤ 2^t*n+2^(p+1) := Nat.le_add_right _ _
             _ = _ := eq.symm
      exact (Nat.not_le_of_lt csmall) (Nat.le_of_add_le_add_left h')
    · have h := Nat.mul_le_mul_right n (show 2^t+1≤3^p by omega)
      simp only [Nat.add_mul,Nat.one_mul] at h
      have h' : 2^t*n+n≤2^t*n+2^(p+1) := by
        calc _ ≤ 3^p*n := h
             _ ≤ 3^p*n+5*3^(p-1) := Nat.le_add_right _ _
             _ = _ := eq
      exact (Nat.not_le_of_lt esmall) (Nat.le_of_add_le_add_left h')
  have floor : (B+1)*2^t≤n := by
    have small : B+1≤2^N := by
      have h := Nat.lt_two_pow_self (n:=N)
      dsimp [N] at *
      omega
    calc _ ≤ 2^N*2^(2*N) := Nat.mul_le_mul small
              (Nat.pow_le_pow_right (by decide) tN)
         _ = 2^(3*N) := by rw [←pow_add,show N+2*N=3*N by omega]
         _ ≤ P := Nat.pow_le_pow_right (by decide) (by omega)
         _ ≤ n := nl
  exact ⟨n,m,t,by omega,by omega,np,nm,mm,nlog.trans mlog.symm,n4,m4,tp,hit,ne,floor⟩

end CollatzBandCollision

#print axioms CollatzBandCollision.ratio_of_log_close
#print axioms CollatzBandCollision.power_ratio_bounds
#print axioms CollatzBandCollision.usable_rotation
#print axioms CollatzBandCollision.octave_padding
#print axioms CollatzBandCollision.placed_source_bounds
#print axioms CollatzBandCollision.marked_of_octave_window
#print axioms CollatzBandCollision.cofinal_equal_features
