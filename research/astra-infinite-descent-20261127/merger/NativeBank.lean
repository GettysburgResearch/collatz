import FiveRouting
import FloorCounting

/-! A finite-duration bank of physical ratio-five returns has a power
saving in ordinary source count at every supplied target. Pure common
halvings have arbitrary length and the final physical clock may vary. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.NativeBank
open TwoGapRouting FiveRouting

/-- A finite succession of actual dual records of duration at most H,
allowing unbounded common-halving padding between records. -/
inductive Parsed (H : ℕ) : ℕ → ℕ → Prop where
  | nil (x) : Parsed H 0 x
  | even {k x} (zero : x%2=0) (tail : Parsed H k (step x)) : Parsed H (1+k) x
  | record {h g k x y} (pos : 0<h) (short : h≤H) (route : Dual h g x y)
      (tail : Parsed H k y) : Parsed H (h+k) x

private theorem runs (h x : ℕ) : CoreBranching.run h x=run h x := by
  induction h generalizing x with
  | zero => rfl
  | succ h ih => exact ih (step x)

private theorem odds_le (h x : ℕ) : odds h x≤h := by
  induction h generalizing x with
  | zero => simp [odds]
  | succ h ih => have := ih (step x); simp only [odds]; omega

private theorem full_odd (h x : ℕ) (hh : odds h x=h) :
    2^h*(run h x+1)=3^h*(x+1) := by
  induction h generalizing x with
  | zero => simp [run]
  | succ h ih =>
    have oh := odds_le h (step x)
    change x%2+odds h (step x)=h+1 at hh
    have odd : x%2=1 := by omega
    have r:=ih (step x) (by omega)
    have eq : 2*(step x+1)=3*(x+1) := by unfold step; split <;> omega
    change 2^(h+1)*(run h (step x)+1)=3^(h+1)*(x+1)
    rw [pow_succ,pow_succ]
    nlinarith only [r,congrArg (fun z : ℕ => 3^h*z) eq]

private theorem missing_even (h x : ℕ) (below : odds h x<h) :
    ∃j<h, run j x%2=0 := by
  induction h generalizing x with
  | zero => simp [odds] at below
  | succ h ih =>
    by_cases ev : x%2=0
    · exact ⟨0,by omega,ev⟩
    have bit : x%2=1 := by omega
    change x%2+odds h (step x)<h+1 at below
    obtain ⟨j,jl,jz⟩:=ih (step x) (by omega)
    exact ⟨j+1,by omega,jz⟩

/-- Every positive-clock native equal-ratio/equal-grade return has an
actual even departure on its first arm. -/
theorem even_in_record {h g x y : ℕ} (hp : 0<h) (route : Dual h g x y) :
    ∃j<h, run j x%2=0 := by
  obtain ⟨hit,count,other,otherCount⟩:=route
  apply missing_even
  by_contra bad
  have hh : odds h x=h := by have := odds_le h x; omega
  have first:=full_odd h x hh
  have second:=full_odd h (5*x) (by omega)
  rw [hit] at first
  rw [other] at second
  have lt : (2:ℕ)^h<3^h := Nat.pow_lt_pow_left (by decide) (by omega)
  nlinarith only [first,second,lt]

private theorem early_even {H D x : ℕ} (hp : 0<H) (path : Parsed H D x) (hl : H≤D) :
    ∃j<H, run j x%2=0 := by
  cases path with
  | nil x => omega
  | even zero _ => exact ⟨0,hp,zero⟩
  | record pos short route _ =>
    obtain ⟨j,jl,jz⟩:=even_in_record pos route
    exact ⟨j,by omega,jz⟩

/-- Every length-2H subword of a completed bank path has an even bit. -/
theorem window_even {H D x : ℕ} (hp : 0<H) (path : Parsed H D x) (i : ℕ)
    (room : i+2*H≤D) : ∃j, i≤j ∧ j<i+2*H ∧ run j x%2=0 := by
  induction path generalizing i with
  | nil => omega
  | @even k x zero tail ih =>
    by_cases first : i=0
    · subst i; exact ⟨0,by omega,by omega,zero⟩
    obtain ⟨j,lo,hi,ev⟩:=ih (i-1) (by omega)
    exact ⟨j+1,by omega,by omega,ev⟩
  | @record h g k x y pos short route tail ih =>
    obtain ⟨hit,_,_,_⟩:=route
    by_cases before : i<h
    · obtain ⟨j,b,ev⟩:=early_even hp tail (by omega)
      exact ⟨h+j,by omega,by omega,by rw [(append h j x).1,hit]; exact ev⟩
    · obtain ⟨j,lo,hi,ev⟩:=ih (i-h) (by omega)
      exact ⟨h+j,by omega,by omega,by rw [(append h j x).1,hit]; exact ev⟩

private theorem bits_deficit {h x : ℕ} (miss : ∃j<h,run j x%2=0) :
    FloorCounting.bits h x<2^h-1 := by
  induction h with
  | zero => simp at miss
  | succ h ih =>
    obtain ⟨j,jl,ev⟩:=miss
    have last : FloorCounting.mark h x=run h x%2 := by unfold FloorCounting.mark; rw [runs]
    have prev:=FloorCounting.bits_lt h x
    have pow : 0<(2:ℕ)^h := by positivity
    rw [FloorCounting.bits,last,pow_succ]
    by_cases eq : j=h
    · subst j; rw [ev]; omega
    · have b:=ih ⟨j,by omega,ev⟩
      rcases (show run h x%2=0 ∨ run h x%2=1 by omega) with p|p <;> rw [p] <;> omega

private def Holes (C k x : ℕ) : Prop :=
  ∀ i<k, FloorCounting.bits C (run (C*i) x)<2^C-1

private theorem holes_tail {C k x : ℕ} (good : Holes C (k+1) x) : Holes C k (run C x) := by
  intro i hi
  have r:=good (i+1) (by omega)
  rwa [Nat.mul_succ,Nat.add_comm (C*i) C,(append C (C*i) x).1] at r

private theorem actual_holes {H D x : ℕ} (hp : 0<H) (p : Parsed H D x) (k : ℕ)
    (long : 2*H*k≤D) : Holes (2*H) k x := by
  intro i hi
  have le : 2*H*(i+1)≤2*H*k := Nat.mul_le_mul_left _ hi
  rw [Nat.mul_succ] at le
  obtain ⟨j,lo,hi',ev⟩:=window_even hp p (2*H*i) (by omega)
  apply bits_deficit
  refine ⟨j-2*H*i,by omega,?_⟩
  rw [←(append (2*H*i) (j-2*H*i) x).1,Nat.add_sub_of_le lo]
  exact ev

private def compressed (C : ℕ) : ℕ → ℕ → ℕ
  | 0, _ => 0
  | k+1, x => FloorCounting.bits C x+(2^C-1)*compressed C k (run C x)

private theorem compressed_lt {C k x : ℕ} (good : Holes C k x) :
    compressed C k x<(2^C-1)^k := by
  induction k generalizing x with
  | zero => simp [compressed]
  | succ k ih =>
    have head:=good 0 (by omega)
    simp only [Nat.mul_zero,run] at head
    have tail:=ih (holes_tail good)
    change FloorCounting.bits C x+(2^C-1)*compressed C k (run C x)<(2^C-1)^(k+1)
    have prod:=Nat.mul_le_mul_left (2^C-1) (Nat.succ_le_of_lt tail)
    rw [Nat.mul_succ] at prod
    rw [pow_succ,Nat.mul_comm ((2^C-1)^k)]
    omega

private theorem bits_append (h k x : ℕ) :
    FloorCounting.bits (h+k) x=FloorCounting.bits h x+2^h*FloorCounting.bits k (run h x) := by
  induction k with
  | zero => simp [FloorCounting.bits]
  | succ k ih =>
    have m : FloorCounting.mark (h+k) x=FloorCounting.mark k (run h x) := by
      unfold FloorCounting.mark; rw [runs,runs,(append h k x).1]
    rw [Nat.add_succ,FloorCounting.bits,ih,FloorCounting.bits,m,pow_add]; ring

private theorem decode {C k x y : ℕ} (left : Holes C k x) (right : Holes C k y)
    (eq : compressed C k x=compressed C k y) :
    FloorCounting.bits (C*k) x=FloorCounting.bits (C*k) y := by
  induction k generalizing x y with
  | zero => simp [FloorCounting.bits]
  | succ k ih =>
    have a:=left 0 (by omega)
    have b:=right 0 (by omega)
    simp only [Nat.mul_zero,run] at a b
    let B:=2^C-1
    change FloorCounting.bits C x+B*compressed C k (run C x)=
      FloorCounting.bits C y+B*compressed C k (run C y) at eq
    have hd:=congrArg (fun n : ℕ => n%B) eq
    simp only [Nat.add_mul_mod_self_left] at hd
    rw [Nat.mod_eq_of_lt (show FloorCounting.bits C x<B from a),
      Nat.mod_eq_of_lt (show FloorCounting.bits C y<B from b)] at hd
    have pos : 0<B := by dsimp [B]; omega
    have tl : compressed C k (run C x)=compressed C k (run C y) := by
      exact Nat.eq_of_mul_eq_mul_left pos (Nat.add_left_cancel (hd ▸ eq))
    rw [Nat.mul_succ,Nat.add_comm (C*k) C,bits_append,bits_append,hd,ih (holes_tail left) (holes_tail right) tl]

private theorem periodic_bits (j d r u : ℕ) :
    FloorCounting.bits j (r+2^(j+d)*u)=FloorCounting.bits j r := by
  induction j generalizing d with
  | zero => rfl
  | succ j ih =>
    rw [show j+1+d=j+(d+1) by omega,FloorCounting.bits,FloorCounting.bits,ih,
      FloorCounting.mark,FloorCounting.mark,(FloorCounting.lift_prefix j (d+1) r u).1,pow_succ]
    have a : 2^d*2*3^(PeakRigidity.grade j r)*u=2*(2^d*3^(PeakRigidity.grade j r)*u) := by ring
    rw [a,show (CoreBranching.run j r+2*(2^d*3^(PeakRigidity.grade j r)*u))%2=
      CoreBranching.run j r%2 by omega]

private theorem bits_mod (h x : ℕ) : FloorCounting.bits h x=FloorCounting.bits h (x%2^h) := by
  conv_lhs => rw [←Nat.mod_add_div x (2^h)]
  simpa using periodic_bits h 0 (x%2^h) (x/2^h)

/-- A pointwise octave count. The clocks and grades of different starts
may be entirely different, and every supplied positive target is allowed. -/
theorem fixed_target_count (H k q : ℕ) (hp : 0<H) (qp : 0<q) (S : Finset ℕ)
    (shell : ∀x∈S, q*2^(2*H*k)≤x ∧ x<2*q*2^(2*H*k))
    (physical : ∀x∈S, ∃D, Parsed H D x ∧ run D x=q) :
    S.card≤2*q*(2^(2*H)-1)^k := by
  classical
  let C:=2*H
  let L:=C*k
  let A:=2^L
  have ap : 0<A := by dsimp [A]; positivity
  have good (x : ℕ) (hx : x∈S) : Holes C k x := by
    obtain ⟨D,p,hit⟩:=physical x hx
    have f:=MergerThreshold.forward_lower D x
    rw [hit] at f
    have one : 1≤(3:ℕ)^(odds D x) := Nat.one_le_pow _ _ (by decide)
    have ll:=Nat.mul_le_mul_right x one
    have low:=(shell x hx).1
    have dl : L≤D := by
      by_contra no
      have po : (2:ℕ)^D<2^L := Nat.pow_lt_pow_right (by decide) (by omega)
      have less:=Nat.mul_lt_mul_of_pos_right po qp
      change q*2^L≤x at low
      rw [Nat.mul_comm q] at low
      omega
    exact actual_holes hp p k dl
  let enc (x : ℕ) := (x/A,compressed C k x)
  let out := (Finset.range (2*q)).product (Finset.range ((2^C-1)^k))
  have inc (x : ℕ) (hx : x∈S) : enc x∈out := by
    apply Finset.mem_product.mpr
    exact ⟨Finset.mem_range.mpr ((Nat.div_lt_iff_lt_mul ap).2 (shell x hx).2),
      Finset.mem_range.mpr (compressed_lt (good x hx))⟩
  have ct:=Finset.card_le_card_of_injOn (s:=S) (t:=out) enc inc (by
    intro x hx y hy eq
    have qeq : x/A=y/A:=congrArg Prod.fst eq
    have de:=decode (good x hx) (good y hy) (congrArg Prod.snd eq)
    rw [bits_mod L x,bits_mod L y] at de
    have re:=FloorCounting.bits_injective L (x%A) (y%A) (Nat.mod_lt _ ap) (Nat.mod_lt _ ap) de
    have xx:=Nat.mod_add_div x A
    have yy:=Nat.mod_add_div y A
    rw [qeq,re] at xx
    omega)
  simpa [out,C] using ct

#print axioms even_in_record
#print axioms window_even
#print axioms fixed_target_count
end Collatz.NativeBank
