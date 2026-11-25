module

public import HourTower

public section

namespace Collatz.Itinerary.HourTower

set_option autoImplicit false
set_option maxRecDepth 8192
set_option maxHeartbeats 4000000
set_option exponentiation.threshold 8192

private structure Bounds where
  low : Nat
  high : Nat
  shift : Nat

private def Bounds.Covers (i : Bounds) (n : Nat) : Prop :=
  i.low*2^i.shift≤n ∧ n≤i.high*2^i.shift

/-- Remove a multiple of the target precision with a bounded number of integer
    comparisons. This keeps very large exponents out of the kernel computation. -/
private def dropBits (p hi : Nat) : Nat :=
  if 2^(4*p)≤hi then 3*p else if 2^(3*p)≤hi then 2*p
  else if 2^(2*p)≤hi then p else 0

private def trim (precision lo hi shift : Nat) : Bounds :=
  let drop := dropBits precision hi
  if drop=0 then ⟨lo,hi,shift⟩ else
    ⟨lo/2^drop,hi/2^drop+1,shift+drop⟩

private theorem trim_covers {precision lo hi shift n : Nat}
    (low : lo*2^shift≤n) (high : n≤hi*2^shift) :
    (trim precision lo hi shift).Covers n := by
  unfold trim
  dsimp only
  split
  · exact ⟨low,high⟩
  next _ =>
    let d := dropBits precision hi
    have lower := Nat.div_mul_le_self lo (2^d)
    have higher := Nat.lt_mul_div_succ hi (Nat.two_pow_pos d)
    change lo/2^d*2^(shift+d)≤n ∧ n≤(hi/2^d+1)*2^(shift+d)
    rw [Nat.pow_add]
    constructor
    · exact Nat.le_trans (by rw [show lo/2^d*(2^shift*2^d)=lo/2^d*2^d*2^shift by ac_rfl]
                             exact Nat.mul_le_mul_right _ lower) low
    · apply Nat.le_trans high
      rw [show (hi/2^d+1)*(2^shift*2^d)=(2^d*(hi/2^d+1))*2^shift by ac_rfl]
      exact Nat.mul_le_mul_right _ (Nat.le_of_lt higher)

private def square (precision c : Nat) : Bounds → Bounds
  | ⟨lo,hi,e⟩ => trim precision (c*lo*lo) (c*hi*hi) (e+e)

private theorem square_covers {i : Bounds} {n : Nat} (h : i.Covers n)
    (precision c : Nat) : (square precision c i).Covers (c*n*n) := by
  rcases i with ⟨lo,hi,e⟩
  obtain ⟨lower,upper⟩ := h
  apply trim_covers
  · calc
      c*lo*lo*2^(e+e) = (c*(lo*2^e))*(lo*2^e) := by rw [Nat.pow_add]; ac_rfl
      _ ≤ c*n*n := Nat.mul_le_mul (Nat.mul_le_mul_left _ lower) lower
  · calc
      c*n*n ≤ (c*(hi*2^e))*(hi*2^e) := Nat.mul_le_mul (Nat.mul_le_mul_left _ upper) upper
      _ = _ := by rw [Nat.pow_add]; ac_rfl

/-- Repeated squaring with outward rounding. The shift itself is unbounded. -/
private def bound3 : Nat → Nat → Nat → Bounds
  | 0, _, _ => ⟨1,1,0⟩
  | k+1, p, n => if n=0 then ⟨1,1,0⟩ else
      square p (3^(n%2)) (bound3 k p (n/2))

private theorem bound3_covers (k precision n : Nat) (bits : n<2^k) :
    (bound3 k precision n).Covers (3^n) := by
  induction k generalizing n with
  | zero =>
    have eq : n=0 := by simpa using bits
    subst n
    simp [bound3,Bounds.Covers]
  | succ k ih =>
    by_cases zero : n=0
    · subst n; simp [bound3,Bounds.Covers]
    · rw [bound3]; simp only [zero,↓reduceIte]
      have half : n/2<2^k := by rw [Nat.pow_succ] at bits; omega
      have s := square_covers (ih (n/2) half) precision (3^(n%2))
      have rep : n=n%2+n/2+n/2 := by omega
      have eqn : 3^n=3^(n%2)*3^(n/2)*3^(n/2) := by rw [←Nat.pow_add,←Nat.pow_add,←rep]
      rwa [eqn]

private def belowTwo (k p a b : Nat) : Bool :=
  let i := bound3 k p a
  i.shift ≤ b && i.high < 2^(b-i.shift)

private def margin (k p a b r : Nat) : Bool :=
  let i := bound3 k p a
  i.shift ≤ b && (3^r+1)*2^(b-i.shift) ≤ 3^r*i.low

private theorem belowTwo_sound {k p a b : Nat} (bits : a<2^k)
    (check : belowTwo k p a b=true) : 3^a<2^b := by
  let i := bound3 k p a
  have both : i.shift≤b ∧ i.high<2^(b-i.shift) := by simpa [belowTwo,i] using check
  have data := (bound3_covers k p a bits).2
  have hi := Nat.mul_lt_mul_of_pos_right both.2 (Nat.two_pow_pos i.shift)
  rw [←Nat.pow_add,Nat.sub_add_cancel both.1] at hi
  exact Nat.lt_of_le_of_lt data hi

private theorem margin_sound {k p a b r : Nat} (bits : a<2^k)
    (check : margin k p a b r=true) : (3^r+1)*2^b ≤ 3^r*3^a := by
  let i := bound3 k p a
  have both : i.shift≤b ∧ (3^r+1)*2^(b-i.shift)≤3^r*i.low := by simpa [margin,i] using check
  have data := (bound3_covers k p a bits).1
  have compare := Nat.mul_le_mul_right (2^i.shift) both.2
  rw [Nat.mul_assoc,Nat.mul_assoc,←Nat.pow_add,Nat.sub_add_cancel both.1] at compare
  exact Nat.le_trans compare (Nat.mul_le_mul_left _ data)

private theorem det_pos {g Q d P : Nat} (qpos : 0<Q) (lower : 3^P<2^Q)
    (above : 2^d<3^g) : d*P<g*Q := by
  have h : 3^(d*P)<3^(g*Q) := by
    calc
      3^(d*P) = (3^P)^d := by rw [Nat.mul_comm d P,Nat.pow_mul]
      _ ≤ (2^Q)^d := Nat.pow_le_pow_left (Nat.le_of_lt lower) _
      _ = (2^d)^Q := by rw [←Nat.pow_mul,←Nat.pow_mul,Nat.mul_comm Q d]
      _ < (3^g)^Q := Nat.pow_lt_pow_left above (by omega)
      _ = _ := (Nat.pow_mul ..).symm
  by_cases le : g*Q≤d*P
  · have opp := Nat.pow_le_pow_right (by decide : 0<3) le
    omega
  · omega

private theorem compare_ratios {x y z t u : Nat} (xy : y≤x) (up : 0<u)
    (ypos : 0<y) (hi : t*x^u ≤ z*y^u) : t*x≤z*y := by
  obtain ⟨j,hj⟩ := Nat.exists_eq_succ_of_ne_zero (show u≠0 by omega)
  rw [hj,Nat.pow_succ x,Nat.pow_succ y] at hi
  have order : x^j*(t*x)≤x^j*(z*y) := by
    calc
      _ = t*(x^j*x) := by ac_rfl
      _ ≤ _ := hi
      _ = y^j*(z*y) := by ac_rfl
      _ ≤ _ := Nat.mul_le_mul_right _ (Nat.pow_le_pow_left xy _)
  exact Nat.le_of_mul_le_mul_left order (Nat.pow_pos (Nat.lt_of_lt_of_le ypos xy))

/-- A determinant-one bracket bounds every earlier approximation on its upper
    side. All comparisons are between ordinary integer powers. -/
private theorem farey {P Q G D g d : Nat} (qpos : 0<Q) (det : G*Q=P*D+1)
    (lower : 3^P<2^Q) (upper : 2^D≤3^G) (above : 2^d<3^g) (cap : d<D+Q) :
    2^d*3^G ≤ 3^g*2^D := by
  have dp := det_pos qpos lower above
  let u := g*Q-d*P
  have ud : g*Q=d*P+u := by dsimp [u]; omega
  have up : 0<u := by dsimp [u]; omega
  have nonneg : d*G≤g*D := by
    by_cases h : d*G≤g*D
    · exact h
    let v := d*G-g*D
    have vd : d*G=g*D+v := by dsimp [v]; omega
    have vp : 0<v := by dsimp [v]; omega
    have eq : d=u*D+v*Q := by grind
    have du := Nat.le_mul_of_pos_left D up
    have qv := Nat.le_mul_of_pos_left Q vp
    omega
  let v := g*D-d*G
  have vd : g*D=d*G+v := by dsimp [v]; omega
  have dc : D*u=d+Q*v := by grind
  have gc : G*u=g+P*v := by grind
  apply compare_ratios upper up (Nat.two_pow_pos D)
  calc
    2^d*(3^G)^u = 2^d*(3^g*(3^P)^v) := by rw [←Nat.pow_mul,gc,Nat.pow_add,Nat.pow_mul]
    _ ≤ 2^d*(3^g*(2^Q)^v) := Nat.mul_le_mul_left _ (Nat.mul_le_mul_left _
      (Nat.pow_le_pow_left (Nat.le_of_lt lower) _))
    _ = 3^g*(2^D)^u := by rw [←Nat.pow_mul 2 D,dc,Nat.pow_add,Nat.pow_mul]; ac_rfl

private theorem relative_gap {P Q G D g d r : Nat} (qpos : 0<Q)
    (det : G*Q=P*D+1) (lower : 3^P<2^Q) (wide : (3^r+1)*2^D≤3^r*3^G)
    (above : 2^d<3^g) (limit : d<D+Q) : 2^d≤3^r*(3^g-2^d) := by
  have lim : 3^r*2^D≤3^r*3^G := Nat.le_trans
    (Nat.mul_le_mul_right _ (Nat.le_succ _)) wide
  have upper := Nat.le_of_mul_le_mul_left lim (Nat.pow_pos (by decide : 0<3))
  have raw := farey qpos det lower upper above limit
  have scaled : 2^D*((3^r+1)*2^d) ≤ 2^D*(3^r*3^g) := by
    calc
      _ = (3^r+1)*2^D*2^d := by ac_rfl
      _ ≤ (3^r*3^G)*2^d := Nat.mul_le_mul_right _ wide
      _ = 3^r*(2^d*3^G) := by ac_rfl
      _ ≤ 3^r*(3^g*2^D) := Nat.mul_le_mul_left _ raw
      _ = _ := by ac_rfl
  have er := Nat.le_of_mul_le_mul_left scaled (Nat.two_pow_pos D)
  rw [Nat.add_mul,Nat.one_mul] at er
  rw [Nat.mul_sub]
  omega

private def pack (base : Nat) (i : Bounds) : Option Nat :=
  if i.low<base ∧ i.high<base then some ((i.shift*base+i.high)*base+i.low) else none

private def unpack (base a : Nat) : Bounds :=
  ⟨a%base,a/base%base,a/base/base⟩

private theorem pack_sound {base a : Nat} {i : Bounds} (pos : 0<base)
    (ok : pack base i=some a) : unpack base a=i := by
  rcases i with ⟨lo,hi,e⟩
  simp only [pack] at ok
  split at ok <;> rename_i bounds
  · have ⟨hlo,hhi⟩ := bounds
    cases ok
    simp [unpack,Nat.add_comm,Nat.mod_eq_of_lt hlo,
      Nat.mod_eq_of_lt hhi,Nat.add_mul_div_right, Nat.div_eq_of_lt hlo,Nat.div_eq_of_lt hhi,pos]
  · contradiction

private def next (p c base : Nat) : Nat → Option Nat
  | 0 => none
  | v+1 => pack base (square p c (unpack base (v+1)))

private def packed3 : Nat → Nat → Nat → Nat → Option Nat
  | 0, _, b, _ => pack b ⟨1,1,0⟩
  | k+1, p, b, n => if n=0 then pack b ⟨1,1,0⟩ else
      (packed3 k p b (n/2)).bind (next p (3^(n%2)) b)

private theorem packed_sound {k p b n a : Nat} (bp : 0<b)
    (ok : packed3 k p b n=some a) : unpack b a=bound3 k p n := by
  induction k generalizing n a with
  | zero => exact pack_sound bp ok
  | succ k ih =>
    by_cases z : n=0
    · subst n; simpa only [packed3,bound3,↓reduceIte] using (pack_sound bp ok)
    · simp only [packed3,z,↓reduceIte] at ok
      rw [bound3]; simp only [z,↓reduceIte]
      cases prev : packed3 k p b (n/2) with
      | none => simp [prev] at ok
      | some v =>
        simp only [prev,Option.bind_some] at ok
        cases v with
        | zero => simp [next] at ok
        | succ v =>
          have h := pack_sound bp ok
          rw [←ih prev]
          exact h

private def fastBelow (k p a b : Nat) : Bool :=
  let B := 2^(2*p+2)
  match packed3 k p B a with
  | none => false
  | some z =>
    let i := unpack B z
    i.shift ≤ b && i.high < 2^(b-i.shift)

private def fastMargin (k p a b r : Nat) : Bool :=
  let B := 2^(2*p+2)
  match packed3 k p B a with
  | none => false
  | some z =>
    let i := unpack B z
    i.shift ≤ b && (3^r+1)*2^(b-i.shift) ≤ 3^r*i.low

private theorem fastBelow_sound {k p a b : Nat} (h : fastBelow k p a b=true) :
    belowTwo k p a b=true := by
  unfold fastBelow at h
  cases hit : packed3 k p (2^(2*p+2)) a with
  | none => simp [hit] at h
  | some z => simpa [belowTwo,hit,packed_sound (Nat.two_pow_pos _) hit] using h

private theorem fastMargin_sound {k p a b r : Nat} (h : fastMargin k p a b r=true) :
    margin k p a b r=true := by
  unfold fastMargin at h
  cases hit : packed3 k p (2^(2*p+2)) a with
  | none => simp [hit] at h
  | some z => simpa [margin,hit,packed_sound (Nat.two_pow_pos _) hit] using h

private def upperGrade : Nat := 1376177782736040975000286955931525296944730308945228325169622273123166212572335007809183882438989155005519282539853299350095766243346217967497567090351617639547841599735839189578975340817252462948526291626017358703064246849575414039741994751333
private def upperTime : Nat := 2181190179962211458638288808804442479969472570561036138500224583507028652303338306922713620681749175151538169612941666606054661178685422537309275677481626108132740927703875597287550819560452817499890861596700928539842420490554244836994111828499
private def lowerGrade : Nat := 1621983786702298834957816186315911286623650363172266440162374760418178460975673910782073348966461654862162665572078938891667747081334245759929067086250596699033621195295692976879994220219584331439778272298717833085104197405402274810795735776590
private def lowerTime : Nat := 2570783478700845951199933359421442098669891815205204471622551386125200491301323320746859778248852150758092613684317787986851659248694570400377890591976614150808502415064914118061694027814415869667043819212040195174775765789564789881668253702767

private theorem lower_check : belowTwo 1024 2048 lowerGrade lowerTime=true :=
  fastBelow_sound (by decide +kernel)
private theorem upper_check : margin 1024 2048 upperGrade upperTime 512=true :=
  fastMargin_sound (by decide +kernel)

/-- A uniform finite check on all lags, using the two fractions whose
    determinant is one. -/
theorem rank512_gap {d g : Nat} (cap : d≤10^243) (above : 2^d<3^g) :
    2^d≤3^512*(3^g-2^d) := by
  have low := belowTwo_sound (by decide : lowerGrade<2^1024) lower_check
  have wide := margin_sound (by decide : upperGrade<2^1024) upper_check
  have big : 10^243 < upperTime+lowerTime := by decide
  exact relative_gap (by decide : 0<lowerTime)
    (by decide : upperGrade*lowerTime=lowerGrade*upperTime+1)
    low wide above (Nat.lt_of_le_of_lt cap big)

/-- Arbitrarily large converging inputs at rank 512 miss every lower-cone
    merger with both ordinary clocks bounded by 10^243. -/
theorem rank512_delayed_merger (L : Nat) :
    ∃ w>L, w%6=1 ∧ ReachesOne (3^512*w) ∧ ∀ h ≤ 10^243, ∀ k ≤ 10^243, ∀ a s b,
      Lower w 512 b s → run h (3^512*w)≠run k (2^a*(3^s*b)) := by
  obtain ⟨w,large,unit,good,barrier⟩ := prescribed_cone_resonance 512 (10^243) L
  refine ⟨w,large,unit,good,?_⟩
  intro h hh k hk a s b low hit
  obtain ⟨d,g,time,above,close,_,_⟩ := barrier h hh k hk a s b low hit
  exact (Nat.not_lt_of_ge (rank512_gap (by omega) above)) close

#print axioms rank512_gap
#print axioms rank512_delayed_merger
end Collatz.Itinerary.HourTower
