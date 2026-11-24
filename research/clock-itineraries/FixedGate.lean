module

public import TernaryItinerary

public section
namespace Collatz.Itinerary.FixedGate

set_option autoImplicit false

/-- Remove at most the given number of factors of two. -/
private def peel : Nat → Nat → Nat × Nat
  | 0, x => (0,x)
  | k+1, x => if x%2=1 then (0,x) else
      let p := peel k (x/2)
      (p.1+1,p.2)

/-- The exact shortcut clock and odd endpoint of the next Syracuse step. -/
def next (a : Nat) : Nat × Nat := peel (3*a+1) (3*a+1)

def after : Nat → Nat → Nat
  | 0, a => a
  | n+1, a => after n (next a).2

def elapsed : Nat → Nat → Nat
  | 0, _ => 0
  | n+1, a => (next a).1 + elapsed n (next a).2

private theorem peel_spec {k x : Nat} (hx : 0<x) (hk : x≤k) :
    2^(peel k x).1*(peel k x).2=x ∧ (peel k x).2%2=1 := by
  induction k generalizing x with
  | zero => omega
  | succ k ih =>
    by_cases odd : x%2=1
    · simp [peel,odd]
    · have ⟨eqn,ho⟩ := ih (x:=x/2) (by omega) (by omega)
      simp only [peel,odd,if_false]
      refine ⟨?_,ho⟩
      rw [Nat.pow_succ,Nat.mul_right_comm,eqn]
      omega

private theorem next_gap {a : Nat} (ho : a%2=1) : Gap (next a).1 a (next a).2 := by
  have ⟨h₁,h₂⟩ := peel_spec (x:=3*a+1) (k:=3*a+1) (by omega) (by omega)
  change 2^(next a).1*(next a).2=3*a+1 at h₁
  change (next a).2%2=1 at h₂
  refine ⟨?_,ho,h₂,h₁⟩
  by_cases h : (next a).1=0
  · simp [h] at h₁; omega
  · omega

private theorem peel_unique {q e k : Nat} (ho : q%2=1) (he : e≤k) :
    peel k (2^e*q)=(e,q) := by
  induction e generalizing k with
  | zero =>
    cases k <;> simp [peel,ho]
  | succ e ih =>
    cases k with
    | zero => omega
    | succ k =>
      rw [Nat.pow_succ,Nat.mul_right_comm]
      simp [peel,ih (k:=k) (by omega)]

private theorem gap_next {a q e : Nat} (g : Gap e a q) : next a=(e,q) := by
  have hp := Nat.lt_two_pow_self (n:=e)
  have hq : 0<q := by have := g.oddTarget; omega
  have hc : 2^e≤2^e*q := by simpa using Nat.mul_le_mul_left (2^e) hq
  unfold next
  rw [←g.eqn]
  exact peel_unique g.oddTarget (by omega)

private theorem after_add (i j a : Nat) : after (i+j) a = after j (after i a) := by
  induction i generalizing a with
  | zero => simp [after]
  | succ i ih => simpa [Nat.succ_add,after] using ih (next a).2

private theorem snoc_clock (n a : Nat) :
    elapsed (n+1) a=elapsed n a+(next (after n a)).1 := by
  induction n generalizing a with
  | zero => simp [after,elapsed]
  | succ n ih =>
    change (next a).1+elapsed (n+1) (next a).2 =
      (next a).1+elapsed n (next a).2+(next (after n (next a).2)).1
    rw [ih (next a).2]
    omega

theorem route_read {a q s : Nat} {rs : List Bool} (r : Route q rs s a) :
    after rs.length a=q ∧ elapsed rs.length a=s := by
  induction r with
  | nil => exact ⟨rfl,rfl⟩
  | @cons q y x e s mark rs g _ _ ih =>
    have ⟨hy,ht⟩ := ih
    have he := gap_next g
    simp only [List.length_cons]
    rw [snoc_clock,after_add,hy,ht]
    simp [after,he,Nat.add_comm]

private theorem next_color {a : Nat} (ho : a%2=1) :
    ∃ c : Bool, (next a).2%3=digit c := by
  have g := next_gap ho
  have h : 2^(next a).1*(next a).2%3=1 := by rw [g.eqn]; omega
  rw [Nat.mul_mod] at h
  by_cases zero : (next a).2%3=0
  · simp [zero] at h
  · by_cases one : (next a).2%3=1
    · exact ⟨false,one⟩
    · exact ⟨true,by change (next a).2%3=2; omega⟩

private theorem route_exists (n a : Nat) {c : Bool} (ho : a%2=1) (hc : a%3=digit c) :
    ∃ rs, rs.length=n ∧ Route (after n a) rs (elapsed n a) a ∧
      after n a%2=1 ∧ ∃ d : Bool, after n a%3=digit d := by
  induction n with
  | zero => exact ⟨[],rfl,.nil a,ho,c,hc⟩
  | succ n ih =>
    obtain ⟨rs,hl,r,hy,d,hd⟩ := ih
    have g := next_gap hy
    obtain ⟨f,hf⟩ := next_color hy
    rw [after_add,snoc_clock]
    change ∃ rs', rs'.length=n+1 ∧
      Route (next (after n a)).2 rs' (elapsed n a+(next (after n a)).1) a ∧ _
    exact ⟨d::rs,by simp [hl],Nat.add_comm _ _ ▸ Route.cons g hd r,g.oddTarget,f,hf⟩

private theorem after_one (n : Nat) : after n 1=1 := by
  induction n with
  | zero => rfl
  | succ n ih => exact ih

set_option maxRecDepth 10000 in
set_option maxHeartbeats 12000000 in
private theorem small_hit : ∀ a : Fin 32, a.val%2=1 → after 41 a.val=1 := by decide

set_option maxRecDepth 10000 in
set_option maxHeartbeats 12000000 in
set_option exponentiation.threshold 1000 in
private theorem small_table : ∀ (a : Fin 32) (n : Fin 41), a.val%2=1 → 2<after n.val a.val →
    59049*(2^(5*elapsed n.val a.val)*(after n.val a.val)^5) ≤
      100000*(2^(8*n.val)*a.val^5) := by decide

private theorem small_rate {a n : Nat} (ha : a<32) (ho : a%2=1) (hq : 2<after n a) :
    59049*(2^(5*elapsed n a)*(after n a)^5) ≤ 100000*(2^(8*n)*a^5) := by
  by_cases h : n<41
  · exact small_table ⟨a,ha⟩ ⟨n,h⟩ ho hq
  · have splitN : n=41+(n-41) := by omega
    rw [splitN,after_add,small_hit ⟨a,ha⟩ ho,after_one] at hq
    omega

private theorem large_rate {a : Nat} (ha : 32≤a) (ho : a%2=1) :
    2^(5*(next a).1)*(next a).2^5≤2^8*a^5 := by
  have g := next_gap ho
  rw [Nat.mul_comm 5 _,Nat.pow_mul,←Nat.mul_pow,g.eqn]
  have p := Nat.pow_le_pow_left (show 32*(3*a+1)≤97*a by omega) 5
  rw [Nat.mul_pow,Nat.mul_pow] at p
  omega

/-- Sharp uniform finite-path distortion at rate eight fifths, up to the
last odd state above two. Equality is attained from nine at depth five. -/
theorem distortion {n a : Nat} (ho : a%2=1) (hq : 2<after n a) :
    59049*(2^(5*elapsed n a)*(after n a)^5) ≤ 100000*(2^(8*n)*a^5) := by
  induction n generalizing a with
  | zero =>
    simp only [elapsed,after,Nat.mul_zero,Nat.pow_zero,Nat.one_mul]
    exact Nat.mul_le_mul_right _ (by decide)
  | succ n ih =>
    by_cases ha : a<32
    · exact small_rate ha ho hq
    · have localBound := large_rate (by omega : 32≤a) ho
      have tail := ih (next_gap ho).oddTarget hq
      simp only [elapsed,after,Nat.mul_add,Nat.pow_add,Nat.mul_one]
      calc
        _ = 2^(5*(next a).1)*(59049*(2^(5*elapsed n (next a).2)*(after n (next a).2)^5)) := by ac_rfl
        _ ≤ 2^(5*(next a).1)*(100000*(2^(8*n)*(next a).2^5)) := Nat.mul_le_mul_left _ tail
        _ = (100000*2^(8*n))*(2^(5*(next a).1)*(next a).2^5) := by ac_rfl
        _ ≤ (100000*2^(8*n))*(2^8*a^5) := Nat.mul_le_mul_left _ localBound
        _ = _ := by ac_rfl

theorem distortion_sharp :
    after 5 9=5 ∧ elapsed 5 9=9 ∧
    59049*(2^(5*elapsed 5 9)*(after 5 9)^5) = 100000*(2^(8*5)*9^5) := by decide

/-- Rounded binary heights cost no extra clock bit, since the sharp
distortion constant is strictly below two. -/
theorem height_clock {n a H Q : Nat} (ho : a%2=1) (hq : 2<after n a)
    (upper : a≤2^H) (lower : 2^Q≤after n a) :
    5*elapsed n a+5*Q≤8*n+5*H := by
  have low := Nat.mul_le_mul_left (2^(5*elapsed n a)) (Nat.pow_le_pow_left lower 5)
  have high := Nat.mul_le_mul_left (2^(8*n)) (Nat.pow_le_pow_left upper 5)
  have bound := Nat.le_trans (Nat.mul_le_mul_left 59049 low)
    (Nat.le_trans (distortion ho hq) (Nat.mul_le_mul_left 100000 high))
  rw [←Nat.pow_mul,←Nat.pow_mul,Nat.mul_comm Q 5,Nat.mul_comm H 5,←Nat.pow_add,←Nat.pow_add] at bound
  have strict : 2^(5*elapsed n a+5*Q)<2^(8*n+5*H+1) := by
    rw [Nat.pow_succ]
    have := Nat.two_pow_pos (8*n+5*H)
    omega
  have := (Nat.pow_lt_pow_iff_right (by decide : 1<2)).1 strict
  omega

/-- Once the prefix has its guaranteed clock, every missing word is
equivalent to the deterministic suffix having entered the cycle. -/
theorem full_iff_after_of_clock {a b m : Nat} {c : Bool} (ho : a%2=1) (hc : a%3=digit c)
    (hm : 2≤m) (budget : elapsed (b-m) a+6*m+7≤2*b) :
    FullRow a b m ↔ 2<after (b-m) a := by
  constructor
  · rintro ⟨q,rs,u,v,hq,hl,r,_,_⟩
    rw [←hl,(route_read r).1]
    exact hq
  · intro hq
    obtain ⟨rs,hl,r,_,_⟩ := route_exists (b-m) a ho hc
    refine ⟨after (b-m) a,rs,2*b-elapsed (b-m) a,elapsed (b-m) a,hq,hl,r,by omega,?_⟩
    intro w hw
    apply free_marks ho hc w <;> omega

/-- Pointwise saturation on the original b/11 scale, uniformly over
converging and nonconverging gates. Q may be any lower endpoint height. -/
theorem full_iff_after {a b m H Q : Nat} {c : Bool} (ho : a%2=1) (hc : a%3=digit c)
    (hm : 2≤m) (mb : m≤b) (upper : a≤2^H)
    (lower : 2^Q≤after (b-m) a) (budget : 22*m+5*H+35≤2*b+5*Q) :
    FullRow a b m ↔ 2<after (b-m) a := by
  constructor
  · rintro ⟨q,rs,u,v,hq,hl,r,_,_⟩
    rw [←hl,(route_read r).1]
    exact hq
  · intro hq
    have := height_clock ho hq upper lower
    exact (full_iff_after_of_clock ho hc hm (by omega)).2 hq

/-- At depth floor(b/12), the canonical ordinary hitting certificate has
the same truth value as the missing-row test. The threshold depends only
logarithmically on the gate. -/
theorem missing_iff_hits {a b : Nat} {c : Bool} (ho : a%2=1) (hc : a%3=digit c)
    (hb : 30*(a.log2+1)+210≤b) :
    ¬FullRow a b (b/12) ↔ run (elapsed (b-b/12) a) a=1 := by
  have ⟨rs,_,r,odd,_⟩ := route_exists (b-b/12) a ho hc
  have pos : 2^0≤after (b-b/12) a := by simp; omega
  have iff := full_iff_after (b:=b) (m:=b/12) ho hc (by omega) (by omega)
    (Nat.le_of_lt (Nat.lt_log2_self (n:=a))) pos (by omega)
  rw [iff,r.follow]
  omega

#print axioms route_read
#print axioms distortion
#print axioms distortion_sharp
#print axioms height_clock
#print axioms full_iff_after_of_clock
#print axioms full_iff_after
#print axioms missing_iff_hits

end Collatz.Itinerary.FixedGate
