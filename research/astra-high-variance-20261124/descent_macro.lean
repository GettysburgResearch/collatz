import Std

namespace Collatz.ExpandingShadow

def step (x : Nat) := if x%2=0 then x/2 else (3*x+1)/2
def walk : Nat → Nat → Nat
  | 0,x => x
  | n+1,x => walk n (step x)
def odds : Nat → Nat → Nat
  | 0,_ => 0
  | n+1,x => x%2 + odds n (step x)
def Bad (x : Nat) := ∀ n, walk n x ≠ 1

private theorem walk_add (n m x : Nat) : walk (n+m) x=walk m (walk n x) := by
  induction n generalizing x with
  | zero => simp [walk]
  | succ n ih => rw [Nat.succ_add]; exact ih (step x)

private theorem lift_walk (n t b : Nat) :
    walk n (2^n*t+b)=3^(odds n b)*t+walk n b := by
  induction n generalizing t b with
  | zero => simp [walk, odds]
  | succ n ih =>
    rw [walk,walk,odds,Nat.pow_succ 2 n,Nat.pow_add 3]
    by_cases hb : b%2=0
    · have st : step (2^n*2*t+b)=2^n*t+step b := by
        rw [show 2^n*2*t=2*(2^n*t) by ac_rfl]
        simp only [step]; split <;> omega
      rw [st,ih,hb,Nat.pow_zero,Nat.one_mul]
    · have hbo : b%2=1 := by omega
      have st : step (2^n*2*t+b)=2^n*(3*t)+step b := by
        rw [show 2^n*2*t=2*(2^n*t) by ac_rfl,show 2^n*(3*t)=3*(2^n*t) by ac_rfl]
        simp only [step]; split <;> omega
      rw [st,ih,hbo,Nat.pow_one]
      ac_rfl

/-- A finite certificate for a whole residue class. The last two natural
constants clear a possibly negative affine intercept before using divisibility. -/
private theorem realize (A p C b e J H : Nat) (b_lt : b<2^A)
    (cu : Nat.Coprime (2^A) (3^p)) (bp : odds A b=p) (be : walk A b=e)
    (cert : 2^A*e=3^p*b+C) (pad : J+b=2^A) (adj : 3^p*J=C+2^A*H)
    {x y : Nat} (edge : 2^A*y=3^p*x+C) : walk A x=y := by
  have div : 2^A ∣ x+J := by
    apply cu.dvd_of_dvd_mul_left
    refine ⟨y+H,?_⟩
    rw [Nat.mul_add,Nat.mul_add (2^A),adj,edge]; omega
  obtain ⟨t,ht⟩ := div
  have hrem : x%2^A=b := by
    have hpos : 0<2^A := Nat.pow_pos (by decide)
    by_cases hz : t=0
    · subst t; simp at ht; omega
    · obtain ⟨w,hw⟩ : ∃ w,t=w+1 := ⟨t-1,by omega⟩
      rw [hw,Nat.mul_add,Nat.mul_one] at ht
      have ex : x=2^A*w+b := by omega
      rw [ex,Nat.mul_add_mod_self_left,Nat.mod_eq_of_lt b_lt]
  let t := x/2^A
  have xeq : x=2^A*t+b := by dsimp [t]; rw [←hrem]; exact (Nat.div_add_mod _ _).symm
  rw [xeq,lift_walk,bp,be]
  apply Nat.eq_of_mul_eq_mul_left (n:=2^A) (Nat.pow_pos (by decide))
  calc
    2^A*(3^p*t+e)=3^p*(2^A*t)+2^A*e := by rw [Nat.mul_add]; ac_rfl
    _=3^p*(2^A*t+b)+C := by rw [cert,Nat.mul_add]; omega
    _=2^A*y := by rw [←xeq,edge]

private theorem numerator_edge (w s M B D c k q q' : Nat)
    (source : w*q'=s*q+c) (carry : M*c+w*B=s*B+D*k) :
    w*(M*q'+B)=s*(M*q+B)+D*k := by
  calc
    w*(M*q'+B)=M*(w*q')+w*B := by rw [Nat.mul_add]; ac_rfl
    _=M*(s*q)+(M*c+w*B) := by rw [source,Nat.mul_add]; omega
    _=s*(M*q+B)+D*k := by rw [carry,Nat.mul_add]; ac_rfl

inductive Profile where | low | high deriving DecidableEq
inductive Block where | light | single | pair | shortPair | spacedPair deriving DecidableEq
inductive Header where | ppLLL | pLLpL | pLLpp deriving DecidableEq

def mul : Profile → Nat | .low => 5583 | .high => 72873
def depth : Profile → Nat | .low => 12 | .high => 16
def D (f : Profile) := 2^(depth f)
def bias (f : Profile) := 7*(mul f-D f)
def N (f : Profile) (x : Nat) := mul f*x+bias f
def Y (f : Profile) (x : Nat) := N f x / D f
def profile : Header → Profile | .ppLLL | .pLLpL => .low | .pLLpp => .high
def debt : Header → Nat | .ppLLL | .pLLpL => 6 | .pLLpp => 9

def clock : Block → Nat
  | .light => 3
  | .single => 23
  | .pair => 28
  | .shortPair => 31
  | .spacedPair => 34

def count : Block → Nat
  | .light => 2
  | .single => 14
  | .pair => 16
  | .shortPair => 18
  | .spacedPair => 20

def carry : Block → Nat
  | .light => 7
  | .single => 18276431
  | .pair => 206430919
  | .shortPair => 2344417535
  | .spacedPair => 24992071927

def hClock : Header → Nat
  | .ppLLL => 19
  | .pLLpL => 19
  | .pLLpp => 21

def hCount : Header → Nat
  | .ppLLL => 10
  | .pLLpL => 10
  | .pLLpp => 10

def hCarry : Header → Nat
  | .ppLLL => 1704901
  | .pLLpL => 892165
  | .pLLpp => 761093

def target : Profile → Block → Nat
  | .low, .light => 7
  | .low, .single => 34074319
  | .low, .pair => 854144327
  | .low, .shortPair => 7668305791
  | .low, .spacedPair => 68862806903
  | .high, .light => 7
  | .high, .single => 23148199
  | .high, .pair => 406173407
  | .high, .shortPair => 3986203351
  | .high, .spacedPair => 38520971663

def ent : Header → Nat
  | .ppLLL => 6377087774
  | .pLLpL => 4108335230
  | .pLLpp => 67686869126

private theorem literal_resets (f b) {x y : Nat}
    (he : 2^(clock b)*y=3^(count b)*x+target f b) : walk (clock b) x=y := by
  cases f <;> cases b
  · exact realize 3 2 7 1 2 7 7 (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) he
  · exact realize 23 14 34074319 4234617 2414474 4153991 2368495 (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) he
  · exact realize 28 16 854144327 197315961 31641893 71119495 11404828 (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) he
  · exact realize 31 18 7668305791 212213113 38284676 1935270535 349135813 (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) he
  · exact realize 34 20 68862806903 10008436089 2031287813 7171433095 1455496588 (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) he
  · exact realize 3 2 7 1 2 7 7 (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) he
  · exact realize 23 14 23148199 1238241 706016 7150367 4076953 (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) he
  · exact realize 28 16 406173407 222812641 35730578 45622815 7316143 (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) he
  · exact realize 31 18 3986203351 1779911905 321108077 367571743 66312412 (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) he
  · exact realize 34 20 38520971663 2448172257 496875080 14731696927 2989909321 (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) he

private theorem literal_entrances (h) {x y : Nat}
    (he : 2^(hClock h+depth (profile h)-1)*y=3^(hCount h+debt h)*x+ent h) :
    walk (hClock h+depth (profile h)-1) x=y := by
  cases h
  · exact realize 30 16 6377087774 427521634 17139512 646220190 25907209 (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) he
  · exact realize 30 16 4108335230 629725442 25245938 444016382 17800783 (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) he
  · exact realize 36 19 67686869126 2091646094 35376284 66627830642 1126885183 (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) (by decide) he

structure Tail (b : Nat → Block) (q : Nat → Nat) : Prop where
  height : ∀ j, 3≤q j
  edge : ∀ j, 2^(clock (b j))*q (j+1)=3^(count (b j))*q j+carry (b j)

private theorem nedge {b q} (h : Tail b q) (f : Profile) (j : Nat) :
    2^(clock (b j))*N f (q (j+1))=3^(count (b j))*N f (q j)+D f*target f (b j) := by
  apply numerator_edge _ _ _ _ _ _ _ _ _ (h.edge j)
  cases f <;> cases b j <;> decide

/-- Infinite integrality is forced by future edges of one fixed path. -/
theorem tail_integral {b q} (h : Tail b q) (f : Profile) (j : Nat) : D f ∣ N f (q j) := by
  have lift (k i : Nat) (hk : k≤depth f) : 2^k ∣ N f (q i) := by
    induction k generalizing i with
    | zero => simp
    | succ k ih =>
      have low := ih (i+1) (by omega)
      have hw : 2 ∣ 2^(clock (b i)) := by cases b i <;> decide
      have both := Nat.mul_dvd_mul hw low
      rw [nedge h f i] at both
      have fk : 2*2^k ∣ D f := by rw [Nat.mul_comm,←Nat.pow_succ]; exact Nat.pow_dvd_pow 2 hk
      have add := Nat.dvd_trans fk (Nat.dvd_mul_right (D f) (target f (b i)))
      have prod := (Nat.dvd_add_iff_left add).mpr both
      rw [Nat.mul_comm 2 (2^k),←Nat.pow_succ] at prod
      exact (((show Nat.Coprime 2 3 by decide).pow_left (k+1)).pow_right _).dvd_of_dvd_mul_left prod
  exact lift (depth f) j (Nat.le_refl _)

private theorem yedge {b q} (h : Tail b q) (f : Profile) (j : Nat) :
    2^(clock (b j))*Y f (q (j+1))=3^(count (b j))*Y f (q j)+target f (b j) := by
  have hz (i) : D f*Y f (q i)=N f (q i) := Nat.mul_div_cancel' (tail_integral h f i)
  apply Nat.eq_of_mul_eq_mul_left (n:=D f) (Nat.pow_pos (by decide))
  calc
    D f*(2^(clock (b j))*Y f (q (j+1)))=2^(clock (b j))*(D f*Y f (q (j+1))) := by ac_rfl
    _=3^(count (b j))*N f (q j)+D f*target f (b j) := by rw [hz,nedge h f j]
    _=D f*(3^(count (b j))*Y f (q j)+target f (b j)) := by rw [←hz,Nat.mul_add]; ac_rfl

private theorem trap (k n : Nat) (hn : n=1 ∨ n=2) : walk k n=1 ∨ walk k n=2 := by
  induction k generalizing n with
  | zero => exact hn
  | succ k ih =>
    apply ih (step n)
    rcases hn with e|e <;> rw [e] <;> decide

private theorem bad_of_link {x y : Nat} (h : Bad y) (k) (link : walk k x=y) : Bad x := by
  intro t ht
  by_cases early : t≤k
  · have hs : walk (k-t) (walk t x)=y := by rw [←walk_add,show t+(k-t)=k by omega,link]
    rw [ht] at hs
    have tr := trap (k-t) 1 (Or.inl rfl)
    rw [hs] at tr
    rcases tr with a|a
    · exact h 0 a
    · apply h 1; rw [a]; decide
  · apply h (t-k)
    rw [←link,←walk_add,show k+(t-k)=t by omega,ht]

/-- A literal, positive, nonconvergent orbit exists at each macro boundary. -/
theorem tail_bad {b q} (h : Tail b q) (f : Profile) (j : Nat) : Bad (Y f (q j)) := by
  have visit (i) : ∃ k, i≤k ∧ walk k (Y f (q j))=Y f (q (j+i)) := by
    induction i with
    | zero => exact ⟨0,by decide,rfl⟩
    | succ i ih =>
      obtain ⟨k,hk,eq⟩ := ih
      have pos : 0<clock (b (j+i)) := by cases b (j+i) <;> decide
      refine ⟨k+clock (b (j+i)),by omega,?_⟩
      rw [walk_add,eq]
      exact literal_resets _ _ (yedge h f (j+i))
  intro t ht
  obtain ⟨k,hk,eq⟩ := visit t
  rw [show k=t+(k-t) by omega,walk_add,ht] at eq
  have tr := trap (k-t) 1 (Or.inl rfl)
  rw [eq] at tr
  have height := h.height (j+t)
  cases f <;> simp [Y,N,D,mul,depth,bias] at tr <;> omega

private theorem entrance_algebra (W D M n R Z U b C K q q' z y : Nat)
    (size : 2*Z=W*D) (sc : U=n*R) (kc : M*C+W*b+2*U=7*M*n+2*K)
    (source : W*q'=n*q+C) (shadow : D*y=M*q'+b)
    (ramp : 2*R*(z+1)=M*(q+7)) : Z*y=U*z+K := by
  have g1 : 2*(Z*y)=M*(n*q)+(M*C+W*b) := by
    calc
      2*(Z*y)=W*(D*y) := by rw [←Nat.mul_assoc,size]; ac_rfl
      _=M*(W*q')+W*b := by rw [shadow,Nat.mul_add]; ac_rfl
      _=M*(n*q)+(M*C+W*b) := by rw [source,Nat.mul_add]; omega
  have g2 : 2*(U*z)+2*U=M*(n*q)+7*M*n := by
    calc
      2*(U*z)+2*U=n*(2*R*(z+1)) := by rw [sc]; simp only [Nat.mul_add,Nat.mul_one]; ac_rfl
      _=M*(n*q)+7*M*n := by rw [ramp]; simp only [Nat.mul_add]; ac_rfl
  omega

private theorem enter {b q} (tail : Tail b q) (h : Header) (qP z : Nat)
    (source : 2^(hClock h)*q 0=3^(hCount h)*qP+hCarry h)
    (ramp : 2*3^(debt h)*(z+1)=mul (profile h)*(qP+7)) :
    walk (hClock h+depth (profile h)-1) z=Y (profile h) (q 0) := by
  apply literal_entrances
  have hz : D (profile h)*Y (profile h) (q 0)=N (profile h) (q 0) :=
    Nat.mul_div_cancel' (tail_integral tail _ 0)
  exact entrance_algebra _ _ _ _ _ _ _ _ _ _ _ _ _ _
    (by cases h <;> decide) (by cases h <;> decide) (by cases h <;> decide)
    source hz ramp

/-- All three asynchronous entrances into the nonconvergent ordinary tail. -/
theorem entrance_bad {b q} (tail : Tail b q) (h : Header) (qP z : Nat)
    (source : 2^(hClock h)*q 0=3^(hCount h)*qP+hCarry h)
    (ramp : 2*3^(debt h)*(z+1)=mul (profile h)*(qP+7)) : Bad z :=
  bad_of_link (tail_bad tail (profile h) 0) _ (enter tail h qP z source ramp)

private theorem odd_run (a v : Nat) (hv : 0<v) :
    walk a (2^a*v-1)=3^a*v-1 := by
  induction a generalizing v with
  | zero => simp [walk]
  | succ a ih =>
    rw [walk,Nat.pow_succ 2 a,show 2^a*2*v=2*(2^a*v) by ac_rfl]
    have pos := Nat.mul_pos (Nat.pow_pos (a:=2) (n:=a) (by decide)) hv
    have st : step (2*(2^a*v)-1)=2^a*(3*v)-1 := by
      rw [show 2^a*(3*v)=3*(2^a*v) by ac_rfl]; unfold step; split <;> omega
    rw [st,ih (3*v) (by omega),Nat.pow_succ,Nat.mul_assoc]

private theorem cofactor (q : Nat → Nat) (r : Nat)
    (ls : ∀ i, i<r → 8*q (i+1)=9*q i+7) (ho : q r%2=1) :
    ∃ v, 0<v ∧ q 0+7=2^(3*r+1)*v ∧ q r+7=2*9^r*v := by
  have h (i : Nat) (hi : i≤r) : 8^i*(q i+7)=9^i*(q 0+7) := by
    induction i with
    | zero => simp
    | succ i ih =>
      have hprev := ih (by omega)
      have e := ls i (by omega)
      have ec : 8*(q (i+1)+7)=9*(q i+7) := by omega
      calc
        8^(i+1)*(q (i+1)+7)=8^i*(8*(q (i+1)+7)) := by rw [Nat.pow_succ]; ac_rfl
        _=8^i*(9*(q i+7)) := by rw [ec]
        _=9*(8^i*(q i+7)) := by ac_rfl
        _=9^(i+1)*(q 0+7) := by rw [hprev,Nat.pow_succ]; ac_rfl
  have pair := h r (Nat.le_refl _)
  let t := (q r+7)/2
  have ht : q r+7=2*t := by dsimp [t]; omega
  have div : 2^(3*r+1) ∣ 9^r*(q 0+7) := by
    refine ⟨t,?_⟩
    rw [←pair,ht,Nat.pow_succ 2 (3*r),Nat.pow_mul]
    change 8^r*(2*t)=8^r*2*t
    ac_rfl
  have cop := ((show Nat.Coprime 2 9 by decide).pow_left (3*r+1)).pow_right r
  obtain ⟨v,hv⟩ := cop.dvd_of_dvd_mul_left div
  refine ⟨v, ?_,hv,?_⟩
  · by_cases hz : v=0
    · simp [hz] at hv
    · omega
  · apply Nat.eq_of_mul_eq_mul_left (n:=8^r) (Nat.pow_pos (by decide))
    rw [pair,hv,Nat.pow_succ 2 (3*r),Nat.pow_mul]
    change 9^r*(8^r*2*v)=8^r*(2*9^r*v)
    ac_rfl

private theorem ramp_floor (h : Header) (r v q₀ : Nat) (hr : 7≤r) (hv : 0<v)
    (hs : q₀+7=2^(3*r+1)*v) :
    let X := 2^(2*r-debt h)*(mul (profile h)*v)
    0<X-1 ∧ (X-1)%2=1 ∧ X-1<(3*q₀+1)/4 ∧ X-1<q₀ := by
  let a := 2*r-debt h
  let M := mul (profile h)
  have de : debt h≤9 := by cases h <;> decide
  have pos : 0<a := by dsimp [a]; omega
  have bound : 8*M≤5*2^(7+debt h+1) := by cases h <;> decide
  have factor : 8*M≤5*2^(r+debt h+1) := Nat.le_trans bound
    (Nat.mul_le_mul_left 5 (Nat.pow_le_pow_right (n:=2) (by decide) (by omega)))
  have cost : 8*(2^a*(M*v))≤5*(q₀+7) := by
    rw [hs,show 3*r+1=(r+debt h+1)+a by dsimp [a]; omega,Nat.pow_add]
    calc
      8*(2^a*(M*v))=(8*M)*(2^a*v) := by ac_rfl
      _≤(5*2^(r+debt h+1))*(2^a*v) := Nat.mul_le_mul_right _ factor
      _=_ := by ac_rfl
  have qbound : 64≤q₀+7 := by
    rw [hs]
    exact Nat.le_trans (Nat.pow_le_pow_right (n:=2) (by decide) (show 6≤3*r+1 by omega))
      (Nat.le_mul_of_pos_right _ hv)
  obtain ⟨i,hi⟩ : ∃ i,a=i+1 := ⟨a-1,by omega⟩
  have evenX : 2^a*(M*v)=2*(2^i*(M*v)) := by rw [hi,Nat.pow_succ]; ac_rfl
  have mv := Nat.mul_pos (show 0<M by cases h <;> decide) hv
  have ipos := Nat.mul_pos (Nat.pow_pos (a:=2) (n:=i) (by decide)) mv
  change 0<2^a*(M*v)-1 ∧ (2^a*(M*v)-1)%2=1 ∧
    2^a*(M*v)-1<(3*q₀+1)/4 ∧ 2^a*(M*v)-1<q₀
  omega

/-- Descent below both initial floors for a long initial light run, all
three residual headers and an infinite tail of the declared five macros. -/
theorem original_floor_descent {b q} (tail : Tail b q) (h : Header)
    (z : Nat → Nat) (r : Nat) (hr : 7≤r) (ho : z r%2=1)
    (ls : ∀ i, i<r → 8*z (i+1)=9*z i+7)
    (header : 2^(hClock h)*q 0=3^(hCount h)*z r+hCarry h) :
    ∃ m, 0<m ∧ m%2=1 ∧ m<(3*z 0+1)/4 ∧ m<z 0 ∧ Bad m := by
  obtain ⟨v,hv,hs,he⟩ := cofactor z r ls ho
  let a := 2*r-debt h
  let M := mul (profile h)
  have mv := Nat.mul_pos (show 0<M by cases h <;> decide) hv
  have vp : 0<3^a*(M*v) := Nat.mul_pos (Nat.pow_pos (by decide)) mv
  have dr : debt h+a=2*r := by
    have de : debt h≤9 := by cases h <;> decide
    dsimp [a]; omega
  have ramp : 2*3^(debt h)*(3^a*(M*v)-1+1)=M*(z r+7) := by
    rw [Nat.sub_add_cancel vp,he]
    calc
      2*3^(debt h)*(3^a*(M*v))=(3^(debt h)*3^a)*(2*(M*v)) := by ac_rfl
      _=M*(2*9^r*v) := by rw [←Nat.pow_add,dr,Nat.pow_mul]; change 9^r*(2*(M*v))=_; ac_rfl
  have bad := entrance_bad tail h (z r) _ header ramp
  obtain ⟨hp,hod,h₁,h₂⟩ := ramp_floor h r v (z 0) hr hv hs
  exact ⟨_,hp,hod,h₁,h₂,bad_of_link bad a (odd_run a (M*v) mv)⟩

/-- For every short initial light run the ordinary paid endpoint wins directly. -/
theorem short_paid_drop (r q y : Nat) (hr : r≤6) (hq : 17≤q)
    (edge : 32*8^r*y+58*8^r=9^(r+1)*(q+7)) :
    y<(3*q+1)/4 ∧ y<q := by
  let W := 32*8^r
  let C := 58*8^r
  let A := 9^(r+1)
  have ranges : r=0 ∨ r=1 ∨ r=2 ∨ r=3 ∨ r=4 ∨ r=5 ∨ r=6 := by omega
  have rates : 4*A≤3*W ∧ 96*A+3*W≤51*W+4*C := by
    rcases ranges with e|e|e|e|e|e|e <;> subst r <;> decide
  let u := q-17
  have qeq : q=u+17 := by dsimp [u]; omega
  change W*y+C=A*(q+7) at edge
  rw [qeq,show u+17+7=u+24 by omega,Nat.mul_add] at edge
  have scaled : 4*(W*y)+4*C=(4*A)*u+96*A := by
    calc
      _=4*(W*y+C) := by rw [Nat.mul_add]
      _=4*(A*u+A*24) := by rw [edge]
      _=_ := by rw [Nat.mul_add,show 96=4*24 by decide]; ac_rfl
  have slope := Nat.mul_le_mul_right u rates.1
  have base := rates.2
  have whole : W*(4*y+3)≤W*(3*q) := by
    rw [qeq,show W*(4*y+3)=4*(W*y)+3*W by rw [Nat.mul_add]; ac_rfl,
      show W*(3*(u+17))=(3*W)*u+51*W by rw [Nat.mul_add,Nat.mul_add,show 51=3*17 by decide]; ac_rfl]
    omega
  have result := Nat.le_of_mul_le_mul_left whole (show 0<W from Nat.mul_pos (by decide) (Nat.pow_pos (by decide)))
  omega

#print axioms original_floor_descent
#print axioms short_paid_drop

#print axioms tail_integral
#print axioms tail_bad
#print axioms entrance_bad
end Collatz.ExpandingShadow
