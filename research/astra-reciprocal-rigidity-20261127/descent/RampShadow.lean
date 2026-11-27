import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.LinearCombination

/-! Physical two-sided descent barriers along an initial all-odd ramp.
    Negative integers are used only to translate a finite prefix. -/
namespace RampShadow

/-- Number of shortcut steps, odd inputs, source and terminal. Each edge
    equation forces its physical parity, including on signed integers. -/
inductive Walk : ℕ → ℕ → ℤ → ℤ → Prop
  | nil (x : ℤ) : Walk 0 0 x x
  | even {h p : ℕ} {x y : ℤ} : Walk h p x y → Walk (h+1) p (2*x) y
  | odd {h p : ℕ} {x y z : ℤ} : 3*x+1=2*y → Walk h p y z → Walk (h+1) (p+1) x z

theorem count_le {h p x y} (w : Walk h p x y) : p ≤ h := by
  induction w <;> omega

theorem affine {h p x y} (w : Walk h p x y) :
    ∃ A : ℤ, 0≤A ∧ A≤3^h-2^h ∧ 2^h*y=3^p*x+A := by
  induction w with
  | nil x => exact ⟨0, by norm_num, by norm_num, by simp⟩
  | @even h p x y w ih =>
    obtain ⟨A,hA,hB,eq⟩ := ih
    refine ⟨2*A,by omega,?_,?_⟩
    · have pos : (0:ℤ)≤3^h := by positivity
      simp only [pow_succ]; linarith
    · simp only [pow_succ]; linear_combination 2*eq
  | @odd h p x y z xy w ih =>
    obtain ⟨A,hA,hB,eq⟩ := ih
    have pq : (3:ℤ)^p≤3^h := pow_le_pow_right₀ (by norm_num) (count_le w)
    have pos : (0:ℤ)≤3^p := by positivity
    refine ⟨3^p+2*A,by omega,?_,?_⟩
    · simp only [pow_succ]; linarith
    · simp only [pow_succ]; linear_combination 2*eq - (3:ℤ)^p*xy

theorem lift {h p x y} (w : Walk h p x y) (a : ℤ) :
    Walk h p (x+2^h*a) (y+3^p*a) := by
  induction w generalizing a with
  | nil x => simpa using Walk.nil (x+a)
  | @even h p x y w ih =>
    rw [show 2*x+2^(h+1)*a=2*(x+2^h*a) by rw [pow_succ]; ring]
    exact Walk.even (ih a)
  | @odd h p x y z eq w ih =>
    rw [show z+3^(p+1)*a=z+3^p*(3*a) by rw [pow_succ]; ring]
    apply Walk.odd (y:=y+2^h*(3*a)) _ (ih _)
    rw [pow_succ]; linear_combination eq

theorem nonneg_of_terminal {h p x y} (w : Walk h p x y) : 0≤y → 0≤x := by
  induction w <;> omega

theorem zero_origin {h p x y} (w : Walk h p x y) : x=0 → p=0 ∧ y=0 := by
  induction w <;> omega

theorem cycle_origin {h p x y} (w : Walk h p x y) : x=1 ∨ x=2 → y=1 ∨ y=2 := by
  induction w <;> omega

theorem all_odd {h p x y} (w : Walk h p x y) (hp : p=h) :
    2^h*(y+1)=3^h*(x+1) := by
  induction w with
  | nil => simp
  | @even h p x y w ih => have := count_le w; omega
  | @odd h p x y z xy w ih =>
    have ph : p=h := by omega
    have eq := ih ph
    simp only [pow_succ]; linear_combination 2*eq - (3:ℤ)^h*xy

theorem split {d j k x y} (w : Walk (d+j) k x y) :
    ∃ p u z, Walk d p x z ∧ Walk j u z y ∧ k=p+u := by
  induction d generalizing k x with
  | zero => exact ⟨0,k,x,.nil x,by simpa using w,by simp⟩
  | succ d ih =>
    rw [show d+1+j=(d+j)+1 by omega] at w
    cases w with
    | even v =>
      obtain ⟨p,u,z,l,r,h⟩ := ih v
      exact ⟨p,u,z,.even l,r,h⟩
    | odd eq v =>
      obtain ⟨p,u,z,l,r,h⟩ := ih v
      exact ⟨p+1,u,z,.odd eq l,r,by omega⟩

/-- Any physical path from a smaller positive start needs at least j shortcuts
    to meet the all-odd maximum at time j. -/
theorem clocks_order {e k j : ℕ} {m n y : ℤ} (w : Walk e k m y)
    (hm : 0≤m) (hlt : m<n) (ramp : 2^j*(y+1)=3^j*(n+1)) : j≤e := by
  obtain ⟨A,_,bound,eq⟩ := affine w
  have pq : (3:ℤ)^k≤3^e := pow_le_pow_right₀ (by norm_num) (count_le w)
  have le : 2^e*(y+1) ≤ 3^e*(m+1) := by nlinarith [mul_le_mul_of_nonneg_right pq hm]
  by_contra! h
  obtain ⟨a,ha⟩ := Nat.exists_eq_add_of_le (Nat.le_of_lt h)
  rw [ha, pow_add, pow_add] at ramp
  have dd : (2:ℤ)^a ≤ 3^a := pow_le_pow_left₀ (by norm_num) (by norm_num) _
  have npos : 0≤3^e*(m+1) := by positivity
  have G := mul_le_mul_of_nonneg_right dd npos
  have F := mul_le_mul_of_nonneg_right le (show 0≤(2:ℤ)^a by positivity)
  have H := mul_lt_mul_of_pos_left (show m+1<n+1 by omega)
    (show (0:ℤ)<3^e*3^a by positivity)
  nlinarith only [F,G,H,ramp]

/-- A contracted diagram near residue 0 or 1 forces an actual small signed
    origin and an actual prefix. The remaining j steps are used only affinely. -/
theorem translated_origin {d j k : ℕ} {m n y a s : ℤ}
    (w : Walk (d+j) k m y) (ha : 3^k*a=3^j*(n-s))
    (ramp : 2^j*(y+1)=3^j*(n+1)) (hs : 0≤s) :
    ∃ p u z m₀ z₀ A, k=p+u ∧ u≤j ∧
      m=m₀+2^d*a ∧ z=z₀+3^p*a ∧ Walk d p m₀ z₀ ∧ Walk j u z y ∧
      0≤m₀ ∧ (s=1 → 1≤m₀) ∧
      3^k*m₀ < 2^d*3^j*(s+1) ∧
      3^u*z₀+A=3^j*(s+1)-2^j := by
  obtain ⟨p,u,z,P,Q,ku⟩ := split w
  obtain ⟨A,hA,bA,eA⟩ := affine Q
  obtain ⟨B,hB,_,eB⟩ := affine w
  let m₀ := m-2^d*a
  let z₀ := z-3^p*a
  have L : Walk d p m₀ z₀ := by simpa [m₀,z₀,sub_eq_add_neg] using lift P (-a)
  have prod : (3:ℤ)^u*3^p*a=3^j*(n-s) := by
    rw [← pow_add, Nat.add_comm u p, ← ku]; exact ha
  have tailEq : 3^u*z₀+A=3^j*(s+1)-2^j := by
    dsimp [z₀]; linear_combination eA.symm + ramp - prod
  have pos : (0:ℤ)<3^u := by positivity
  have zj : 0≤z₀ := by
    by_contra! hh
    have H := mul_neg_of_pos_of_neg pos hh
    nlinarith [mul_nonneg (show (0:ℤ)≤3^j by positivity) hs]
  have pos₀ : 0≤m₀ := nonneg_of_terminal L zj
  have strict : s=1 → 1≤m₀ := by
    rintro rfl
    have pj : (0:ℤ)<3^j := by positivity
    by_contra! hh
    have h0 := (zero_origin L (by omega)).2
    rw [h0] at tailEq
    nlinarith
  have whole : 3^k*m₀+B=2^d*(3^j*(s+1)-2^j) := by
    dsimp [m₀]; rw [pow_add] at eB
    linear_combination -eB + (2:ℤ)^d*ramp - (2:ℤ)^d*ha
  have posPow : (0:ℤ)<2^d*2^j := by positivity
  exact ⟨p,u,z,m₀,z₀,A,ku,count_le Q,by dsimp [m₀]; ring,
    by dsimp [z₀]; ring,L,Q,pos₀,strict,by nlinarith only [whole,hB,posPow],tailEq⟩

/-- Excludes every smaller ordinary merging partner, at an unrestricted
    lower clock, whenever its odd-count cost is at most K+j. -/
theorem ramp_barrier {K j e k : ℕ} {s m n y : ℤ}
    (seed : s=0 ∨ s=1) (hn : s<n) (hm : 0<m) (hlt : m<n)
    (precision : (3:ℤ)^K ∣ n-s)
    (ramp : 2^j*(y+1)=3^j*(n+1))
    (w : Walk e k m y) : K+j<k := by
  by_contra! cap
  obtain ⟨d,ed⟩ := Nat.exists_eq_add_of_le (clocks_order w (by omega) hlt ramp)
  rw [show e=d+j by omega] at w
  obtain ⟨v,hv⟩ := precision
  obtain ⟨f,hf⟩ := Nat.exists_eq_add_of_le cap
  let a : ℤ := 3^f*v
  have ha : 3^k*a=3^j*(n-s) := by
    dsimp [a]; rw [hv]
    rw [← mul_assoc, ← pow_add, ← hf, Nat.add_comm K j, pow_add]; ring
  obtain ⟨p,u,z,m₀,z₀,A,ku,uj,em,ez,L,Q,mnon,mpos,small,tEq⟩ :=
    translated_origin w ha ramp (by omega)
  have ms : s≤m₀ := by rcases seed with hh|hh <;> simp_all
  have prod : (2^d*3^j)*(n-s) < 3^k*(n-s) := by
    have inequality : 2^d*a < n-s := by omega
    have h := mul_lt_mul_of_pos_left inequality (show (0:ℤ)<3^k by positivity)
    calc
      _ = 2^d*(3^k*a) := by rw [ha]; ring
      _ = 3^k*(2^d*a) := by ring
      _ < _ := h
  have slope : (2:ℤ)^d*3^j < 3^k := lt_of_mul_lt_mul_right prod (by omega)
  rcases seed with rfl|rfl
  · have eq0 : m₀=0 := by
      by_contra! hz
      have := mul_le_mul_of_nonneg_left (show 1≤m₀ by omega)
        (show (0:ℤ)≤3^k by positivity)
      nlinarith only [this,small,slope]
    have p0 := (zero_origin L eq0).1
    have pk : (3:ℤ)^k≤3^j := pow_le_pow_right₀ (by norm_num) (by omega)
    have one : (1:ℤ)≤2^d := one_le_pow₀ (by norm_num)
    nlinarith [mul_le_mul_of_nonneg_right one (show (0:ℤ)≤3^j by positivity)]
  · have eq1 : m₀=1 := by
      by_contra! hz
      have := mul_le_mul_of_nonneg_left (show 2≤m₀ by omega)
        (show (0:ℤ)≤3^k by positivity)
      nlinarith only [this,small,slope]
    obtain ⟨B,hB,_,pEq⟩ := affine L
    rw [eq1] at pEq
    have cyc := cycle_origin L (Or.inl eq1)
    rw [ku,pow_add] at slope
    have powu : (3:ℤ)^u≤3^j := pow_le_pow_right₀ (by norm_num) uj
    rcases cyc with z1|z2
    · rw [z1] at pEq
      have pBound : (3:ℤ)^p≤2^d := by linarith
      nlinarith only [slope,mul_le_mul pBound powu (by positivity) (by positivity)]
    · have ud : u<j := by
        by_contra! ge
        have eqU : u=j := by omega
        have eqQ := all_odd Q eqU
        have G : (3:ℤ)^j*(z+1)=3^j*(n+1) := eqQ.symm.trans ramp
        have zn : z=n := by
          have pos : (0:ℤ)<3^j := by positivity
          nlinarith [mul_eq_zero.mp (show (3:ℤ)^j*(z-n)=0 by linarith)]
        rw [z2,zn] at ez
        have fromA : (3:ℤ)^j*(3^p*a)=3^j*(n-1) := by
          rw [← mul_assoc, ← pow_add, show j+p=k by omega]; exact ha
        have Z : (3:ℤ)^j=0 := by linear_combination -(3:ℤ)^j*ez - fromA
        exact (ne_of_gt (by positivity : (0:ℤ)<3^j)) Z
      have qBound : (3:ℤ)^u*3≤3^j := by
        rw [← pow_succ]; exact pow_le_pow_right₀ (by norm_num) ud
      rw [z2] at pEq
      have pBound : (3:ℤ)^p≤2^d*2 := by linarith
      have qBound' : (3:ℤ)^u*2≤3^j := by linarith [show (0:ℤ)≤3^u by positivity]
      have X := mul_le_mul_of_nonneg_right pBound (show (0:ℤ)≤3^u by positivity)
      have Y := mul_le_mul_of_nonneg_left qBound' (show (0:ℤ)≤2^d by positivity)
      nlinarith only [slope,X,Y]


def step (x : ℤ) : ℤ := if x%2=0 then x/2 else (3*x+1)/2

def run : ℕ → ℤ → ℤ
  | 0,x => x
  | h+1,x => run h (step x)

def odds : ℕ → ℤ → ℕ
  | 0,_ => 0
  | h+1,x => (if x%2=0 then 0 else 1) + odds h (step x)

theorem walk_run (h : ℕ) (x : ℤ) : Walk h (odds h x) x (run h x) := by
  induction h generalizing x with
  | zero => exact .nil x
  | succ h ih =>
    by_cases hx : x%2=0
    · simp only [odds,run,step,hx,ite_true,Nat.zero_add]
      have W := Walk.even (ih (x/2))
      rwa [show 2*(x/2)=x by omega] at W
    · simp only [odds,run,step,hx,ite_false,Nat.add_comm 1]
      exact Walk.odd (by omega) (ih _)

theorem readout {h p x y} (w : Walk h p x y) : run h x=y ∧ odds h x=p := by
  induction w with
  | nil => simp [run,odds]
  | @even h p x y w ih =>
    have he : (2*x)%2=0 := by omega
    have hv : 2*x/2=x := by omega
    simpa [run,odds,step,he,hv] using ih
  | @odd h p x y z eq w ih =>
    have ho : x%2≠0 := by omega
    have hv : (3*x+1)/2=y := by omega
    simpa [run,odds,step,ho,hv,Nat.add_comm 1] using ih

/-- Exact physical all-odd ramp, even if its last displayed state is even. -/
theorem ramp_walk (j : ℕ) (v : ℤ) :
    Walk j j (2^j*v-1) (3^j*v-1) := by
  induction j generalizing v with
  | zero => simp [Walk.nil]
  | succ j ih =>
    have W := ih (3*v)
    rw [show 3^j*(3*v)-1=3^(j+1)*v-1 by rw [pow_succ]; ring] at W
    apply Walk.odd (y:=2^j*(3*v)-1) _ W
    rw [pow_succ]; ring

/-- Barrier stated on the actual shortcut iterator and its own native odd clock. -/
theorem native_barrier {K j e : ℕ} {s m n : ℤ}
    (seed : s=0 ∨ s=1) (hn : s<n) (hm : 0<m) (hlt : m<n)
    (precision : (3:ℤ)^K ∣ n-s) (rise : (2:ℤ)^j ∣ n+1)
    (meet : run e m=run j n) : K+j<odds e m := by
  obtain ⟨v,hv⟩ := rise
  have rn : n=2^j*v-1 := by omega
  have R := ramp_walk j v
  rw [←rn] at R
  have Y := (readout R).1
  apply ramp_barrier seed hn hm hlt precision _ (walk_run e m)
  rw [meet,Y]; linear_combination (3:ℤ)^j*(-rn)

theorem append {d j p u x y z} (l : Walk d p x y) (r : Walk j u y z) :
    Walk (d+j) (p+u) x z := by
  induction l with
  | nil => simpa using r
  | even w ih => simpa [Nat.succ_add] using Walk.even (ih r)
  | odd eq w ih => simpa [Nat.succ_add] using Walk.odd eq (ih r)

/-- Reverse K traversals of the trivial two-step word, transplanted to
    a positive ternary fibre. -/
theorem lifted_twos (K : ℕ) (v : ℤ) :
    Walk (2*K) K (1+4^K*v) (1+3^K*v) := by
  induction K generalizing v with
  | zero => simp [Walk.nil]
  | succ K ih =>
    have W := ih (3*v)
    rw [show 1+3^K*(3*v)=1+3^(K+1)*v by rw [pow_succ]; ring] at W
    rw [show 2*(K+1)=2*K+1+1 by omega]
    apply Walk.odd (y:=2*(1+4^K*(3*v))) _ (Walk.even W)
    rw [pow_succ]; ring

/-- An all-precision certificate. Its two starts, clocks, inequality and
    every subsequent joint ramp vertex are physical. -/
theorem post_barrier_witness {K b j : ℕ} {v t c : ℤ}
    (positive : 0<v) (tpos : 0<t) (bpos : 0<b)
    (bridge : 2+4^K*v=3^b*t)
    (winning : (2:ℤ)^b*4^K < 3^b*3^K)
    (rising : 1+3^K*v=2^j*c-1) :
    0<2^b*t-1 ∧ 2^b*t-1 < 1+3^K*v ∧
    Walk (b+2*K+j) (b+K+j) (2^b*t-1) (3^j*c-1) := by
  have A := ramp_walk b t
  rw [show 3^b*t-1=1+4^K*v by omega] at A
  have B := lifted_twos K v
  have C := ramp_walk j c
  rw [←rising] at C
  have d1 : (2:ℤ)^1 ≤2^b := pow_le_pow_right₀ (by norm_num) bpos
  have d2 : (2:ℤ)^b≤3^b := pow_le_pow_left₀ (by norm_num) (by norm_num) _
  have budget := mul_lt_mul_of_pos_right winning positive
  have D : (3:ℤ)^b*(2^b*t-1) < 3^b*(1+3^K*v) := by
    have E := congrArg (fun x : ℤ => 2^b*x) bridge
    nlinarith only [E,budget,d2]
  refine ⟨?_,lt_of_mul_lt_mul_left D (by positivity),append (append A B) C⟩
  norm_num at d1
  nlinarith [mul_nonneg (show (0:ℤ)≤2^b-2 by omega) (show 0≤t-1 by omega)]

/-- Existing PR197 (1,2) witness, now optimal against *every* smaller start
    at *every* native clock on the chosen ramp. -/
theorem sharp_at_one {j : ℕ} {v c : ℤ} (hv : 0≤v) (rise : 9*v+4=2^j*c-1) :
    0<8*v+3 ∧ 8*v+3<9*v+4 ∧
    Walk (3+j) (2+j) (8*v+3) (3^j*c-1) ∧
    ∀ (m : ℤ) (e : ℕ), 0<m → m<9*v+4 →
      run e m=3^j*c-1 → 2+j≤odds e m := by
  have W : Walk 3 2 (8*v+3) (9*v+4) := by
    apply Walk.odd (y:=12*v+5) (by ring)
    apply Walk.odd (y:=2*(9*v+4)) (by ring)
    exact Walk.even (Walk.nil _)
  have R := ramp_walk j c
  rw [←rise] at R
  refine ⟨by omega,by omega,append W R,?_⟩
  intro m e hm lt meet
  have precision : (3:ℤ)^1 ∣ (9*v+4)-1 := ⟨3*v+1,by ring⟩
  have proof := native_barrier (K:=1) (j:=j) (e:=e) (s:=1) (n:=9*v+4)
    (Or.inr rfl) (by omega) hm lt precision ⟨c,by omega⟩
    (meet.trans (readout R).1.symm)
  omega

/-- Cut immediately after the first b odd inputs, with arbitrary native even
    steps on either side. The last K odd inputs remain in the right walk. -/
theorem split_odds {e k x y} (w : Walk e k x y) (b K : ℕ) (hk : k=b+K) :
    ∃ d f z, e=d+f ∧ Walk d b x z ∧ Walk f K z y := by
  induction w generalizing b with
  | nil x =>
    have hb : b=0 := by omega
    have hK : K=0 := by omega
    subst b; subst K
    exact ⟨0,0,x,rfl,.nil x,.nil x⟩
  | @even h p x y w ih =>
    obtain ⟨d,f,z,eq,P,Q⟩ := ih b hk
    exact ⟨d+1,f,z,by omega,.even P,Q⟩
  | @odd h p x y z eq w ih =>
    cases b with
    | zero =>
      have hr : p+1=K := by omega
      subst K
      exact ⟨0,h+1,x,by omega,.nil x,.odd eq w⟩
    | succ b =>
      obtain ⟨d,f,v,eqD,P,Q⟩ := ih b (by omega)
      exact ⟨d+1,f,v,by omega,.odd eq P,Q⟩

/-- At precision K, every proposed clock with K+b odd inputs pays the
    complete inverse price at the ordinary target 1, plus b other steps. -/
theorem one_fibre_price {K b e E : ℕ} {x n : ℤ}
    (optimal : ∀ (f : ℕ) (u : ℤ), Walk f K u 1 → E≤f)
    (hn : (3:ℤ)^K ∣ n-1)
    (walk : Walk e (b+K) x n) : E+b≤e := by
  obtain ⟨v,hv⟩ := hn
  obtain ⟨d,f,z,eq,P,Q⟩ := split_odds walk b K rfl
  have shadow := lift Q (-v)
  rw [show n+3^K*(-v)=1 by linarith] at shadow
  have := optimal f _ shadow
  have := count_le P
  omega

/-- Any physical K-odd history at 1 can be lifted and prefixed by b
    actual all-odd steps on the congruence in the hypothesis. -/
theorem decode_one_fibre {K E b : ℕ} {u v t : ℤ}
    (base : Walk E K u 1) (congr : u+2^E*v+1=3^b*t) :
    Walk (b+E) (b+K) (2^b*t-1) (1+3^K*v) := by
  have head := ramp_walk b t
  rw [show 3^b*t-1=u+2^E*v by omega] at head
  exact append head (lift base v)

#print axioms ramp_barrier
#print axioms native_barrier
#print axioms post_barrier_witness
#print axioms sharp_at_one
#print axioms one_fibre_price
#print axioms decode_one_fibre
end RampShadow
