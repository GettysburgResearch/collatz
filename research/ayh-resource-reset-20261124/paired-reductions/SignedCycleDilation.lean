import TwoOddCertificate

/-! A signed reference orbit supplies identities between positive lifts.
The argument uses exactly the displayed finite periods of the two arms. -/

namespace SignedCycleDilation
open CollatzReverseBasin CollatzTwoOdd

def step (x : Int) : Int := if x % 2 = 0 then x / 2 else (3*x+1)/2

def orbit : Nat → Int → Int
  | 0, x => x
  | h+1, x => orbit h (step x)

def count : Nat → Int → Nat
  | 0, _ => 0
  | h+1, x => (if x % 2 = 0 then 0 else 1) + count h (step x)

private theorem first_lift (x k : Int) :
    step (2*k+x) = (3:Int)^(if x%2=0 then 0 else 1 : Nat)*k+step x := by
  have same : (2*k+x)%2 = x%2 := by omega
  by_cases he : x%2=0
  · simp only [step,same,he,ite_true,pow_zero,one_mul]
    omega
  · simp only [step,same,he,ite_false,pow_one]
    omega

theorem lift (h : Nat) (x k : Int) :
    orbit h (2^h*k+x) = 3^(count h x)*k+orbit h x := by
  induction h generalizing x k with
  | zero => simp [orbit,count]
  | succ h ih =>
    rw [show (2:Int)^(h+1)*k=2*(2^h*k) by rw [pow_succ]; ring]
    simp only [orbit,count,first_lift]
    rw [show (3:Int)^(if x%2=0 then 0 else 1 : Nat)*(2^h*k)=
      2^h*(3^(if x%2=0 then 0 else 1 : Nat)*k) by ring, ih,pow_add]
    ring

private theorem comp (h k : Nat) (x : Int) :
    orbit (h+k) x=orbit k (orbit h x) := by
  induction h generalizing x with
  | zero => simp [orbit]
  | succ h ih => simpa [Nat.succ_add,orbit] using ih (step x)

/-- The starting vertex may be a negative integer. The two translated
orbits meet at the specified clocks whenever the anchor returns at clock k. -/
theorem cycle_lifts (h k p : Nat) (a t : Int)
    (hp : orbit k (orbit h a)=orbit h a) (hc : count k (orbit h a)=p) :
    orbit (h+k) (a+2^h*2^k*t) = orbit h (a+2^h*3^p*t) := by
  rw [comp,show a+2^h*2^k*t=2^h*(2^k*t)+a by ring,lift]
  rw [show (3:Int)^(count h a)*(2^k*t)+orbit h a=
    2^k*(3^(count h a)*t)+orbit h a by ring,lift,hp,hc]
  rw [show a+2^h*3^p*t=2^h*(3^p*t)+a by ring,lift]
  ring

private theorem nat_step (n : Nat) : step (n:Int)=(shortcut n:Int) := by
  by_cases he : n%2=0
  · have hi : (n:Int)%2=0 := by omega
    simp only [step,hi,shortcut,he,ite_true]
    omega
  · have hi : (n:Int)%2≠0 := by omega
    simp only [step,hi,shortcut,he,ite_false]
    omega

theorem nat_orbit (h n : Nat) : orbit h (n:Int)=(value h n:Int) := by
  induction h generalizing n with
  | zero => rfl
  | succ h ih => simp only [orbit,value,nat_step,ih]

private theorem basin_step (n : Nat) : Basin (shortcut n) ↔ Basin n := by
  constructor
  · rintro ⟨k,h⟩; exact ⟨k+1,h⟩
  · rintro ⟨k,h⟩
    cases k with
    | zero => change n=1 at h; subst n; exact ⟨1,rfl⟩
    | succ k => exact ⟨k,h⟩

theorem basin_value (h n : Nat) : Basin (value h n) ↔ Basin n := by
  induction h generalizing n with
  | zero => rfl
  | succ h ih => exact (ih (shortcut n)).trans (basin_step n)

theorem lift_value (h a b q : Nat) (ha : 2^h*(a/2^h)=a) :
    value h (a*q+b) = (3^(count h (b:Int))*(a/2^h))*q + value h b := by
  have hl := lift h (b:Int) (((a/2^h)*q:Nat):Int)
  have hv := nat_orbit h (a*q+b)
  have hb := nat_orbit h b
  have he : ((a*q+b:Nat):Int)=2^h*((((a/2^h)*q):Nat):Int)+(b:Int) := by
    exact_mod_cast (show a*q+b=2^h*((a/2^h)*q)+b by rw [←Nat.mul_assoc,ha])
  rw [he,hl,hb] at hv
  exact_mod_cast (show ((value h (a*q+b):Nat):Int)=
    (3^(count h (b:Int))*((a/2^h:Nat):Int))*(q:Int)+((value h b:Nat):Int) by
    rw [←hv]; push_cast; ring)

private theorem meet (h k x y : Nat) (hh : orbit h (x:Int)=orbit k (y:Int)) :
    Basin x ↔ Basin y := by
  rw [nat_orbit,nat_orbit] at hh
  have hv : value h x=value k y := by omega
  exact (basin_value h x).symm.trans (hv ▸ basin_value k y)

def CommonCycle (h k p : Nat) (a : Int) : Prop :=
  (orbit k (orbit h a)=orbit h a ∧ count k (orbit h a)=p) ∧
  (orbit k (orbit h (3*a))=orbit h (3*a) ∧ count k (orbit h (3*a))=p)

/-- The labels on both positive arms agree. Unequal cycle periods are
allowed whenever their positive multiples give the same clock and count. -/
theorem paired (h k p x y : Nat) (a t : Int)
    (hc : CommonCycle h k p a)
    (hx : (x:Int)=a+2^h*2^k*t) (hy : (y:Int)=a+2^h*3^p*t) :
    (Basin x ↔ Basin y) ∧ (Basin (3*x) ↔ Basin (3*y)) := by
  have m := cycle_lifts h k p a t hc.1.1 hc.1.2
  have m3 := cycle_lifts h k p (3*a) (3*t) hc.2.1 hc.2.2
  constructor
  · apply meet (h+k) h
    rwa [hx,hy]
  · apply meet (h+k) h
    have hx3 : ((3*x:Nat):Int)=3*a+2^h*2^k*(3*t) := by push_cast; rw [hx]; ring
    have hy3 : ((3*y:Nat):Int)=3*a+2^h*3^p*(3*t) := by push_cast; rw [hy]; ring
    rwa [hx3,hy3]

theorem no_least_of_pair (z w : Nat) (hz : ReverseDefect z)
    (least : ∀ v, ReverseDefect v → z≤v)
    (hw : w%48=17) (ltz : w<z) (lower : Basin w ↔ Basin z)
    (upper : Basin (3*w) ↔ Basin (3*z)) : False := by
  have h := least w ⟨hw,upper.mpr hz.2.1,fun h => hz.2.2 (lower.mp h)⟩
  omega

/-- A source-dependent contraction can be used even when its two signed
arms never occupy the same cycle vertex at a common clock. -/
theorem minus1183 (t w z : Nat)
    (hw : w+1183=6442450944*t) (hz : z+1183=7247757312*t) :
    w%48=17 ∧ w<z ∧ (Basin w ↔ Basin z) ∧ (Basin (3*w) ↔ Basin (3*z)) := by
  have hc : CommonCycle 28 3 2 (-1183) := by unfold CommonCycle; decide
  obtain ⟨lo,hi⟩ := paired 28 3 2 w z (-1183) (3*(t:Int)) hc
    (by norm_num; omega) (by norm_num; omega)
  exact ⟨by omega, by omega, lo, hi⟩

theorem least_not_minus1183 (t w z : Nat)
    (hw : w+1183=6442450944*t) (hz : z+1183=7247757312*t)
    (hd : ReverseDefect z) (least : ∀ v, ReverseDefect v → z≤v) : False := by
  obtain ⟨hr,hl,lo,hi⟩ := minus1183 t w z hw hz
  exact no_least_of_pair z w hd least hr hl lo hi

#print axioms cycle_lifts
#print axioms paired
#print axioms minus1183
#print axioms least_not_minus1183
end SignedCycleDilation
