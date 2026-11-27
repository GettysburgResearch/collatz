import PeakRigidity
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-! Counting a simple native shortcut segment above a supplied floor.
Both the low-grade endpoint and the high-grade word belong to the
same starting site on the supplied segment. -/
set_option autoImplicit false
set_option warningAsError true
namespace FloorCounting
open CoreBranching PeakRigidity

private theorem run_last (j x : ℕ) : run (j+1) x = step (run j x) := by
  simpa [run] using run_add j 1 x

theorem sharp (d j x : ℕ) (hx : x<2^(j+d)) :
    run j x < 2^d * 3^(grade j x) := by
  induction j generalizing d with
  | zero => simpa [grade,run] using hx
  | succ j ih =>
    have a := ih (d+1) (by simpa [Nat.add_assoc,Nat.succ_add] using hx)
    rw [pow_succ,show 2^d*2*3^grade j x=2*(2^d*3^grade j x) by ring] at a
    rw [run_last,grade,pow_add]
    by_cases e : run j x%2=0
    · rw [e,pow_zero,mul_one]
      have st : 2*step (run j x)=run j x := by simp [step,e]; omega
      omega
    · have o : run j x%2=1 := by omega
      rw [o,pow_one]
      have st : 2*step (run j x)=3*run j x+1 := by simp [step,e]; omega
      rw [show 2^d*(3^grade j x*3)=3*(2^d*3^grade j x) by ring]
      omega

private theorem step_lift (y b : ℕ) :
    step (y+2*b)=step y+3^(y%2)*b := by
  have same : (y+2*b)%2=y%2 := by omega
  by_cases e : y%2=0
  · simp [step,same,e]; omega
  · have o : y%2=1 := by omega
    simp [step,same,o]; omega

theorem lift_prefix (j d r u : ℕ) :
    run j (r+2^(j+d)*u)=run j r+2^d*3^(grade j r)*u ∧
    grade j (r+2^(j+d)*u)=grade j r := by
  induction j generalizing d with
  | zero => simp [grade,run]
  | succ j ih =>
    have h := ih (d+1)
    rw [show j+1+d=j+(d+1) by omega,run_last,run_last,grade,grade,h.1,h.2,pow_succ]
    have a : 2^d*2*3^grade j r*u=2*(2^d*3^grade j r*u) := by ring
    rw [a,step_lift,pow_add]
    constructor
    · ring
    · omega

def mark (j x : ℕ) : ℕ := run j x%2

def bits : ℕ → ℕ → ℕ
  | 0, _ => 0
  | j+1, x => bits j x + 2^j*mark j x

theorem bits_lt (j x : ℕ) : bits j x<2^j := by
  induction j with
  | zero => simp [bits]
  | succ j ih =>
    have h : mark j x≤1 := by unfold mark; omega
    rcases Nat.le_one_iff_eq_zero_or_eq_one.mp h with h|h <;>
      simp [bits,h,pow_succ] <;> omega

private theorem periodic_bits (j d r u : ℕ) :
    bits j (r+2^(j+d)*u)=bits j r := by
  induction j generalizing d with
  | zero => rfl
  | succ j ih =>
    rw [show j+1+d=j+(d+1) by omega,bits,bits,ih,mark,mark,(lift_prefix j (d+1) r u).1,pow_succ]
    have a : 2^d*2*3^grade j r*u=2*(2^d*3^grade j r*u) := by ring
    rw [a,show (run j r+2*(2^d*3^grade j r*u))%2=run j r%2 by omega]

private theorem binary_cases (a b : ℕ) (ha : a<2) (hb : b<2) (ne : a≠b) :
    a=0 ∧ b=1 ∨ a=1 ∧ b=0 := by omega

theorem bits_injective (j x y : ℕ) (hx : x<2^j) (hy : y<2^j)
    (eq : bits j x=bits j y) : x=y := by
  induction j generalizing x y with
  | zero => simp at hx hy; omega
  | succ j ih =>
    have p : 0<(2:ℕ)^j := by positivity
    let d := 2^j
    have repr (v : ℕ) : v=v%d+d*(v/d) := by exact (Nat.mod_add_div v d).symm
    have prev (v : ℕ) : bits j v=bits j (v%d) := by
      conv_lhs => rw [repr v]
      simpa [d] using periodic_bits j 0 (v%d) (v/d)
    have head (v : ℕ) : bits (j+1) v %d=bits j v := by
      have bound := bits_lt j v
      simp [bits,d,Nat.add_mod,Nat.mod_eq_of_lt bound]
    have b : bits j (x%d)=bits j (y%d) := by
      rw [←prev,←prev,←head,←head,eq]
    have same : x%d=y%d := ih _ _ (Nat.mod_lt _ p) (Nat.mod_lt _ p) b
    have mark_eq : mark j x=mark j y := by
      rw [bits,bits,prev x,prev y,same] at eq
      exact Nat.eq_of_mul_eq_mul_left p (Nat.add_left_cancel eq)
    have endv (v : ℕ) : run j v=run j (v%d)+3^(grade j (v%d))*(v/d) := by
      conv_lhs => rw [repr v]
      simpa [d] using (lift_prefix j 0 (v%d) (v/d)).1
    rw [pow_succ] at hx hy
    have xq : x/d<2 := (Nat.div_lt_iff_lt_mul p).2 (by simpa [d,Nat.mul_comm] using hx)
    have yq : y/d<2 := (Nat.div_lt_iff_lt_mul p).2 (by simpa [d,Nat.mul_comm] using hy)
    have odd : 3^(grade j (y%d))%2=1 := by simp [Nat.pow_mod]
    unfold mark at mark_eq
    rw [endv x,endv y,same] at mark_eq
    have sep : (run j (y%d)+3^(grade j (y%d)))%2 ≠ run j (y%d)%2 := by
      rw [Nat.add_mod,odd]
      omega
    have qeq : x/d=y/d := by
      by_contra non
      rcases binary_cases _ _ xq yq non with s|s
      · simp only [s.1,s.2,Nat.mul_zero,Nat.add_zero,Nat.mul_one] at mark_eq
        exact sep mark_eq.symm
      · simp only [s.1,s.2,Nat.mul_zero,Nat.add_zero,Nat.mul_one] at mark_eq
        exact sep mark_eq
    calc x = _ := repr x
         _ = _ := by rw [same,qeq]
         _ = y := (repr y).symm



/-- Packed words staying above the scale barrier at every positive prefix. -/
def words (k F : ℕ) : ℕ → ℕ → Finset ℕ
  | 0,p => if p=0 then {0} else ∅
  | j+1,p => if F<2^(k-(j+1))*3^p then
      words k F j p ∪ (if p=0 then ∅ else
        (words k F j (p-1)).image (fun w => w+2^j))
    else ∅

/-- The integer recurrence evaluated by the independent Python certificate. -/
def ballots (k F : ℕ) : ℕ → ℕ → ℕ
  | 0,p => if p=0 then 1 else 0
  | j+1,p => if F<2^(k-(j+1))*3^p then
      ballots k F j p+(if p=0 then 0 else ballots k F j (p-1))
    else 0

theorem words_card_le (k F h p : ℕ) : (words k F h p).card≤ballots k F h p := by
  induction h generalizing p with
  | zero => by_cases z : p=0 <;> simp [words,ballots,z]
  | succ j ih =>
    by_cases ok : F<2^(k-(j+1))*3^p
    · simp only [words,ballots,ok,ite_true]
      apply (Finset.card_union_le ..).trans
      apply Nat.add_le_add (ih p)
      by_cases z : p=0
      · simp [z]
      · simpa [z] using (Finset.card_image_le (s:=words k F j (p-1))
           (f:=fun w => w+2^j)).trans (ih _)
    · simp [words,ballots,ok]

theorem grade_le (h x : ℕ) : grade h x≤h := by
  induction h with
  | zero => rfl
  | succ h ih => simp only [grade]; omega

theorem native_word (k F h x : ℕ) (hk : h≤k) (hx : x<2^k)
    (floor : ∀ j≤h, F≤run j x) :
    bits h x ∈ words k F h (grade h x) := by
  induction h with
  | zero => simp [bits,grade,words]
  | succ h ih =>
    have prev := ih (by omega) (fun j jh => floor j (by omega))
    have scale := sharp (k-(h+1)) (h+1) x (by simpa [show h+1+(k-(h+1))=k by omega] using hx)
    have ok := (floor (h+1) le_rfl).trans_lt scale
    simp only [words,ok,ite_true]
    by_cases z : mark h x=0
    · have z' : run h x%2=0 := z
      simp only [bits,z,mul_zero,add_zero,grade,z']
      exact Finset.mem_union_left _ prev
    · have o : mark h x=1 := by unfold mark at *; omega
      have o' : run h x%2=1 := o
      simp only [bits,o,mul_one,grade,o',Nat.add_one_ne_zero,ite_false,Nat.add_sub_cancel]
      exact Finset.mem_union_right _ (Finset.mem_image_of_mem _ prev)

def highWords (k F h q : ℕ) : Finset ℕ :=
  (Finset.range (h+1)).biUnion (fun p => if q<p then words k F h p else ∅)

theorem high_card (k F h q : ℕ) : (highWords k F h q).card ≤
    ∑ p ∈ Finset.range (h+1), if q<p then ballots k F h p else 0 := by
  apply Finset.card_biUnion_le.trans
  apply Finset.sum_le_sum
  intro p _
  by_cases z : q<p
  · simpa [z] using words_card_le k F h p
  · simp [z]

private theorem pow_two_mod_three (h : ℕ) : 2^h%3=1 ∨ 2^h%3=2 := by
  induction h with
  | zero => decide
  | succ h ih => rcases ih with a|a <;> simp [pow_succ,Nat.mul_mod,a]

/-- One of the three lift indices always produces a multiple of three. -/
private def omitted (r h : ℕ) : ℕ :=
  if r%3=0 then 0 else if (r+2^h)%3=0 then 1 else 2

private theorem omitted_lt (r h : ℕ) : omitted r h<3 := by
  unfold omitted
  split <;> (try split) <;> decide

private theorem excludes (r h j : ℕ) (unit : (r+2^h*j)%3≠0) :
    j%3≠omitted r h := by
  intro a
  unfold omitted at a
  have modj : j%3<3 := Nat.mod_lt _ (by decide)
  have modr : r%3<3 := Nat.mod_lt _ (by decide)
  have one := pow_two_mod_three h
  rw [Nat.add_mod,Nat.mul_mod] at unit
  rw [Nat.add_mod] at a
  split at a <;> (try split at a) <;> rcases one with e|e <;>
    interval_cases s : r%3 <;> simp_all

private def compress (t j : ℕ) : ℕ :=
  2*(j/3)+(j%3-(if t<j%3 then 1 else 0))

private theorem compress_lt (t j D : ℕ) (ht : t<3) (hj : j<D) (ok : j%3≠t) :
    compress t j < D-D/3 := by
  unfold compress
  split <;> omega

private theorem compress_inj (t j l : ℕ) (ht : t<3) (hj : j%3≠t) (hl : l%3≠t)
    (eq : compress t j=compress t l) : j=l := by
  unfold compress at eq
  split at eq <;> split at eq <;> omega

theorem cap_injective (h x y : ℕ) (ux : x%3≠0) (uy : y%3≠0)
    (w : bits h x=bits h y)
    (v : compress (omitted (x%2^h) h) (x/2^h)=
         compress (omitted (y%2^h) h) (y/2^h)) : x=y := by
  let d := 2^h
  have pos : 0<d := by dsimp [d]; positivity
  have repr (z : ℕ) : z=z%d+d*(z/d) := (Nat.mod_add_div z d).symm
  have prev (z : ℕ) : bits h z=bits h (z%d) := by
    conv_lhs => rw [repr z]
    simpa [d] using periodic_bits h 0 (z%d) (z/d)
  have r : x%d=y%d := bits_injective h _ _ (Nat.mod_lt _ pos) (Nat.mod_lt _ pos)
    ((prev x).symm.trans (w.trans (prev y)))
  have a := excludes (x%d) h (x/d) (by change (x%d+d*(x/d))%3≠0; rw [←repr x]; exact ux)
  have b := excludes (y%d) h (y/d) (by change (y%d+d*(y/d))%3≠0; rw [←repr y]; exact uy)
  change compress (omitted (x%d) h) (x/d)=compress (omitted (y%d) h) (y/d) at v
  rw [r] at a v
  have q := compress_inj _ _ _ (omitted_lt _ _) a b v
  calc x = _ := repr x
       _ = _ := by rw [r,q]
       _ = y := (repr y).symm



def visits (x L B : ℕ) : Finset ℕ :=
  (Finset.range (L+1)).filter (fun t => run t x<B)

private theorem mem_visits (x L B t : ℕ) :
    t ∈ visits x L B ↔ t≤L ∧ run t x<B := by
  simp [visits,Nat.lt_succ_iff]

private def address (h x : ℕ) : ℕ × ℕ :=
  (bits h x,compress (omitted (x%2^h) h) (x/2^h))

/-- The height-floor, ternary-unit, and simple-path recurrence.
The left side counts actual native visits, including the terminal site. -/
theorem visit_bound (x L F h d q B : ℕ)
    (simple : ∀ a≤L, ∀ b≤L, run a x=run b x → a=b)
    (floor : ∀ t≤L, F≤run t x) (unit : (∀ t≤L, run t x%3≠0) ∨ d=0)
    (cap : 2^d*3^q≤B) :
    (visits x L (2^(h+d))).card ≤ h+(visits x L B).card+
      (2^d-2^d/3)*(∑ p ∈ Finset.range (h+1), if q<p then ballots (h+d) F h p else 0) := by
  let I := visits x L (2^(h+d))
  let live := I.filter (fun t => t+h≤L)
  let short := I.filter (fun t => ¬t+h≤L)
  let low := live.filter (fun t => grade h (run t x)≤q)
  let high := live.filter (fun t => ¬grade h (run t x)≤q)
  have cut : live.card + short.card = I.card :=
    Finset.card_filter_add_card_filter_not (s:=I) _
  have cut' : low.card + high.card = live.card :=
    Finset.card_filter_add_card_filter_not (s:=live) _
  have loc {t : ℕ} (ht : t∈live) : t≤L ∧ run t x<2^(h+d) ∧ t+h≤L := by
    obtain ⟨hi,hroom⟩ := Finset.mem_filter.mp ht
    obtain ⟨htl, bound⟩ := (mem_visits ..).mp hi
    exact ⟨htl,bound,hroom⟩
  have shortBound : short.card≤h := by
    calc
      _ ≤ (Finset.range h).card := by
        apply Finset.card_le_card_of_injOn (fun t => L-t)
        · intro t ht
          obtain ⟨e,s⟩ := Finset.mem_filter.mp ht
          obtain ⟨w,_⟩ := (mem_visits ..).mp e
          exact Finset.mem_range.mpr (show L-t<h by omega)
        · intro t ht v hv eq
          have a := ((mem_visits ..).mp (Finset.mem_filter.mp ht).1).1
          have b := ((mem_visits ..).mp (Finset.mem_filter.mp hv).1).1
          change L-t=L-v at eq
          omega
      _ = h := Finset.card_range h
  have lowBound : low.card≤(visits x L B).card := by
    apply Finset.card_le_card_of_injOn (fun t => t+h)
    · intro t ht
      obtain ⟨lt,gr⟩ := Finset.mem_filter.mp ht
      obtain ⟨_,bound,room⟩ := loc lt
      refine (mem_visits ..).mpr ⟨room,?_⟩
      rw [run_add]
      exact (sharp d h _ bound).trans_le ((Nat.mul_le_mul_left (2^d)
        (Nat.pow_le_pow_right (by decide) gr)).trans cap)
    · intro a _ b _ eq
      exact Nat.add_right_cancel eq
  let D := 2^d
  let W := highWords (h+d) F h q
  have highBound : high.card ≤ W.card*(D-D/3) := by
    calc
      _ ≤ (W ×ˢ Finset.range (D-D/3)).card := by
        apply Finset.card_le_card_of_injOn (fun t => address h (run t x))
        · intro t ht
          obtain ⟨lt,gr⟩ := Finset.mem_filter.mp ht
          obtain ⟨tl,bound,room⟩ := loc lt
          let y := run t x
          have g : q<grade h y := Nat.lt_of_not_ge gr
          have good : bits h y ∈ words (h+d) F h (grade h y) := by
            apply native_word _ _ _ _ (by omega) bound
            intro j jh
            rw [←run_add]
            exact floor _ (by omega)
          have a : bits h y∈W := by
            apply Finset.mem_biUnion.mpr
            refine ⟨grade h y,Finset.mem_range.mpr (Nat.lt_succ_of_le (grade_le ..)),?_⟩
            simpa [g] using good
          have yd : y/2^h<D := by
            apply (Nat.div_lt_iff_lt_mul (by positivity)).2
            simpa [D,pow_add,Nat.mul_comm] using bound
          apply Finset.mem_product.mpr
          refine ⟨a,Finset.mem_range.mpr ?_⟩
          rcases unit with units|dz
          · have exc : y/2^h%3≠omitted (y%2^h) h := by
              apply excludes
              rw [Nat.mod_add_div]
              exact units t tl
            exact compress_lt _ _ _ (omitted_lt ..) yd exc
          · have one : D=1 := by simp [D,dz]
            have zer : y/2^h=0 := Nat.lt_one_iff.mp (one ▸ yd)
            change compress _ (y/2^h)<D-D/3
            simp [zer,compress,one]
        · intro a ha b hb eq
          have al := (loc (Finset.mem_filter.mp ha).1).1
          have bl := (loc (Finset.mem_filter.mp hb).1).1
          apply simple a al b bl
          rcases unit with units|dz
          · exact cap_injective _ _ _ (units a al) (units b bl)
              (congrArg Prod.fst eq) (congrArg Prod.snd eq)
          · have get {t : ℕ} (ht : t∈high) : run t x<2^h := by
              simpa [dz] using (loc (Finset.mem_filter.mp ht).1).2.1
            exact bits_injective _ _ _ (get ha) (get hb) (congrArg Prod.fst eq)
      _ = W.card*(D-D/3) := by simp
  have highFinal := highBound.trans (Nat.mul_le_mul_right (D-D/3) (high_card (h+d) F h q))
  rw [Nat.mul_comm] at highFinal
  change I.card ≤ h+(visits x L B).card+(D-D/3)*_
  omega

#print axioms sharp
#print axioms bits_injective
#print axioms native_word
#print axioms visit_bound
end FloorCounting
