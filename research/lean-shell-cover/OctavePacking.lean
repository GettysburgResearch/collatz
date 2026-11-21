import OctaveCriterion
import Mathlib.Data.Nat.Factorization.Basic

/-! A bounded-multiplicity transfer of whole component populations into a single octave. -/

namespace CollatzShell.PeriodicWindow

private def sibling (tag : Bool) (m : Nat) := if tag then 4*m+1 else m
private def factor (tag : Bool) : Nat := if tag then 4 else 2

private structure Trace (n z : Nat) (s e : Bool) where
  a : Nat
  m : Nat
  j : Nat
  y : Nat
  mo : m%2=1
  yo : y%2=1
  input : n=2^a*m
  output : z=2^j*y
  bridge : 3*y+1=factor e*(2^a*sibling s m)

private theorem decode {n n' z : Nat} {s e : Bool} (t : Trace n z s e) (v : Trace n' z s e) : n=n' := by
  have yy := odd_core t.yo v.yo t.j v.j (t.output.symm.trans v.output)
  have fac : 0<factor e := by cases e <;> decide
  have key := Nat.eq_of_mul_eq_mul_left fac (t.bridge.symm.trans ((congrArg (fun y => 3*y+1) yy).trans v.bridge))
  have so (m : Nat) (h : m%2=1) : sibling s m%2=1 := by cases s <;> simp [sibling,h]; omega
  have same := odd_core (so _ t.mo) (so _ v.mo) t.a v.a key
  have mm : t.m=v.m := by cases s <;> simp [sibling] at same <;> omega
  rw [mm] at key
  have pos : 0<sibling s v.m := by have := so _ v.mo; omega
  have pw := Nat.eq_of_mul_eq_mul_right pos key
  rw [t.input,v.input,mm,pw]

private theorem powers_label {α : Type*} {f : Nat → α} (law : Laws f) (a m : Nat) : f (2^a*m)=f m := by
  induction a with
  | zero => simp
  | succ a ih => rw [show 2^(a+1)*m=2*(2^a*m) by ring,law.even,ih]

private theorem encode {α : Type*} {f : Nat → α} (law : Laws f) {n p : Nat} (hn : 0<n) (sz : 8*n≤p) :
    ∃ z s e, p≤z ∧ z≤2*p ∧ f z=f n ∧ Nonempty (Trace n z s e) := by
  obtain ⟨a,m,hm,num⟩ := Nat.exists_eq_two_pow_mul_odd hn.ne'
  have mo : m%2=1 := by obtain ⟨v,hv⟩ := hm; omega
  have mp : 0<m := by omega
  let s := decide (m%3=0)
  let Q := 2^a*sibling s m
  have su : sibling s m%3≠0 := by by_cases h : m%3=0 <;> simp [s,sibling,h]; omega
  have qu : Q%3≠0 := unit_pad _ _ su
  have sm : sibling s m≤5*m := by cases s <;> simp [sibling] <;> omega
  have qsz : Q≤5*n := by
    calc _ ≤ 2^a*(5*m) := Nat.mul_le_mul_left _ sm
         _ = _ := by rw [num]; ring
  have qlabel : f Q=f n := by
    change f (2^a*sibling s m)=f n
    rw [num,powers_label law,powers_label law]; cases s <;> simp only [sibling,Bool.false_eq_true,ite_false,ite_true]
    calc f (4*m+1) = f (2*(2*m)+1) := by congr 1; omega
         _ = f (3*(2*m)+2) := law.odd _
         _ = f (2*(3*m+1)) := by congr 1; omega
         _ = f (3*m+1) := law.even _
         _ = f m := plus_at_odd law _ mo
  let e := decide (Q%3=1)
  let y := (factor e*Q-1)/3
  have bridge : 3*y+1=factor e*Q := by by_cases h : Q%3=1 <;> simp [y,factor,e,h] <;> omega
  have yo : y%2=1 := by cases h : e <;> simp [factor,h] at bridge <;> omega
  have yp : 0<y := by omega
  have ybound : y≤p := by cases h : e <;> simp [factor,h] at bridge <;> omega
  have yl : f y=f n := by
    rw [← plus_at_odd law y yo,bridge]
    cases e <;> simp only [factor,Bool.false_eq_true,ite_false,ite_true]
    · exact (law.even Q).trans qlabel
    · exact (powers_label law 2 Q).trans qlabel
  obtain ⟨j,lo,hi⟩ := octave y p yp ybound
  let z := 2^(j+1)*y
  have ze : z=2*(2^j*y) := by dsimp [z]; ring
  exact ⟨z,s,e,by omega,by omega,(powers_label law _ _).trans yl,⟨⟨a,m,j+1,y,mo,yo,num,rfl,bridge⟩⟩⟩

/-- At most four inputs per output suffice to move a population below `p/8` into `[p,2p]`
    while preserving each input's ordinary component label. -/
theorem pack_population {α : Type*} {f : Nat → α} (law : Laws f) (p : Nat) (A S : Finset Nat)
    (small : ∀ n∈A, 0<n ∧ 8*n≤p)
    (cover : ∀ n∈A, ∀ z, p≤z → z≤2*p → f z=f n → z∈S) : A.card≤4*S.card := by
  classical
  have get (n : A) := encode law (small n n.property).1 (small n n.property).2
  choose z s e zl zu lab trace using get
  let g (n : A) : S × (Bool × Bool) := ⟨⟨z n,cover n n.property _ (zl n) (zu n) (lab n)⟩,s n,e n⟩
  have inj : Function.Injective g := by
    intro n m eq
    have zz : z n=z m := congrArg (fun c : S × (Bool × Bool) => c.1.val) eq
    have ss : s n=s m := congrArg (fun c : S × (Bool × Bool) => c.2.1) eq
    have ee : e n=e m := congrArg (fun c : S × (Bool × Bool) => c.2.2) eq
    obtain ⟨tn⟩ := trace n
    obtain ⟨tm⟩ := trace m
    rw [zz,ss,ee] at tn
    exact Subtype.ext (decode tn tm)
  have cnt := Fintype.card_le_of_injective g inj
  simpa [Nat.mul_comm] using cnt

/-- Any two monochromatic populations large enough to survive the four-to-one transfer
    have the same label whenever the ordinary annulus admits the indicated fit. -/
theorem population_rigidity {α : Type*} [DecidableEq α] {f g : Nat → α} (k : Nat)
    (law : Laws f) (per : Period g (2^k)) (E : Finset Nat)
    (fit : ∀ x, 2^k≤x → x<6*2^k → x∉E → f x=g x) :
    ∃ c, ∀ (A : Finset Nat) (v : α), (∀ n∈A, 0<n ∧ 8*n≤2^k ∧ f n=v) →
      4*((4*k+1)*E.card+1)<A.card → v=c := by
  obtain ⟨c,S,size,flat⟩ := octave_rigidity k law per E fit
  refine ⟨c,?_⟩
  intro A v h large
  by_contra different
  have count := pack_population law (2^k) A S (fun n hn => ⟨(h _ hn).1,(h _ hn).2.1⟩) (by
    intro n hn z zl zu same
    by_contra clear
    exact different (((h n hn).2.2).symm.trans (same.symm.trans (flat _ zl zu clear))))
  have cap := Nat.mul_le_mul_left 4 size
  omega

/-- Theorem 6.1 of Krasikov and Lagarias restricted to `X=2^(25h)`.
    This published counting input is an explicit hypothesis, not a Lean axiom. -/
def Population84 : Prop := ∀ q : Nat, q%3≠0 → ∃ H, ∀ h≥H,
    ∃ A : Finset Nat, 2^(21*h)≤A.card ∧ ∀ n∈A, 0<n ∧ n≤2^(25*h) ∧ Hits n q

/-- With the published population input, one can allow errors of order `p^0.84/log p`. -/
theorem collatz_iff_population_comparisons (base : Population84) : Universal ↔
    ∀ K : Nat, ∃ h≥K, ∃ t, 4*((4*(25*h+3)+1)*(unmatched (2^(25*h+3)) t).card+1)<2^(21*h) := by
  classical
  constructor
  · intro all K
    let h := K+1
    obtain ⟨t,clear⟩ := empty_unmatched all (p:=2^(25*h+3)) (by positivity)
    refine ⟨h,by dsimp [h]; omega,t,?_⟩
    simp only [clear,Finset.card_empty,Nat.mul_zero,Nat.zero_add,Nat.mul_one]
    exact lt_of_lt_of_le (by decide : 4<2^3) (Nat.pow_le_pow_right (by decide) (by dsimp [h]; omega))
  · intro tests
    apply universal_of_units
    intro q hu
    obtain ⟨H,atq⟩ := base q hu
    obtain ⟨J,at1⟩ := base 1 (by decide)
    obtain ⟨h,big,t,ok⟩ := tests (max H J)
    let k := 25*h+3
    let p := 2^k
    obtain ⟨c,rigid⟩ := population_rigidity k basin_laws (reference_period p) (unmatched p t) (reference_fit p t)
    have label (y : Nat) (A : Finset Nat) (cnt : 2^(21*h)≤A.card)
        (mem : ∀ n∈A, 0<n ∧ n≤2^(25*h) ∧ Hits n y) : Basin y=c := by
      apply rigid A _ _ (ok.trans_le cnt)
      intro n hn
      obtain ⟨lo,hi,hit⟩ := mem n hn
      refine ⟨lo,?_,propext (basin_at_hit hit)⟩
      calc 8*n ≤ 8*2^(25*h) := Nat.mul_le_mul_left _ hi
           _ = 2^k := by dsimp [k]; rw [pow_add]; ring
    obtain ⟨A,ca,ma⟩ := atq h (le_trans (le_max_left H J) big)
    obtain ⟨B,cb,mb⟩ := at1 h (le_trans (le_max_right H J) big)
    exact ((label q A ca ma).trans (label 1 B cb mb).symm).mpr ⟨0,rfl⟩

#print axioms population_rigidity
#print axioms collatz_iff_population_comparisons

end CollatzShell.PeriodicWindow
