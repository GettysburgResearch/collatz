import Std

/- Std-only. Generic literal block traversal adapted from PR192
d2081d1cd2410e6004eaee9f9b13c5553afaf3f4, descent_Separated.lean. -/
set_option maxRecDepth 8000
set_option maxHeartbeats 2000000

namespace Collatz.MixedPaid

inductive Phase where
  | free | beginTile | two | oneSingle | onePair | pairLead | lastPaid
  deriving DecidableEq
open Phase

inductive Next : Phase → Phase → Prop
  | f0 : Next free free
  | fb : Next free beginTile
  | bt : Next beginTile two
  | ts : Next two oneSingle
  | tp : Next two onePair
  | sl : Next oneSingle lastPaid
  | pf : Next onePair pairLead
  | pl : Next pairLead lastPaid
  | lf : Next lastPaid free
  | lb : Next lastPaid beginTile

def width : Phase → Nat
  | pairLead | lastPaid => 32
  | _ => 8

def inputCarry : Phase → Nat
  | pairLead | lastPaid => 5
  | _ => 7

def mult : Phase → Nat
  | beginTile => 27
  | oneSingle | pairLead => 3
  | _ => 9

def carry : Phase → Nat
  | beginTile => 19
  | two | onePair => 10
  | oneSingle => 4
  | pairLead => 1
  | _ => 5

def numerator (s : Phase) (q : Nat) : Nat :=
  match s with
  | free | beginTile => 183*q+1
  | two => 549*q+131
  | oneSingle | onePair => 549*q-13
  | pairLead => 549*q-175
  | lastPaid => 183*q-37

def shadow (s : Phase) (q : Nat) := numerator s q / 256

structure Track (s : Nat → Phase) (q : Nat → Nat) : Prop where
  next : ∀ j, Next (s j) (s (j+1))
  edge : ∀ j, width (s j)*q (j+1)=9*q j+inputCarry (s j)
  odd : ∀ j, q j%2=1

private theorem large {s q} (h : Track s q) (j : Nat) : 17 ≤ q j := by
  have h0 := h.edge j
  have h1 := h.edge (j+1)
  have h2 := h.odd (j+1+1)
  cases hsj : s j <;> cases hsn : s (j+1) <;>
    simp [hsj, hsn, width, inputCarry] at h0 h1 <;> omega

private theorem numEdge {s t : Phase} {q r : Nat} (h : Next s t)
    (hq : 17 ≤ q) (hr : 17 ≤ r)
    (edge : width s*r=9*q+inputCarry s) :
    width s*numerator t r=mult s*numerator s q+256*carry s := by
  cases h <;> simp [width, inputCarry, mult, carry, numerator] at * <;> omega

theorem integral {s q} (h : Track s q) (j : Nat) : 256 ∣ numerator (s j) (q j) := by
  let N := fun i => numerator (s i) (q i)
  have lift (i d e : Nat) (hd : d ∣ N (i+1)) (hb : e ∣ 256) (hd' : e ∣ 8*d)
      (hc : ∀ a : Phase, Nat.Coprime e (mult a)) : e ∣ N i := by
    have hw : 8 ∣ width (s i) := by cases s i <;> decide
    have he := numEdge (h.next i) (large h i) (large h (i+1)) (h.edge i)
    change width (s i)*N (i+1)=mult (s i)*N i+256*carry (s i) at he
    have hv := Nat.dvd_trans hd' (Nat.mul_dvd_mul hw hd)
    rw [he] at hv
    exact (hc _).dvd_of_dvd_mul_left ((Nat.dvd_add_iff_left
      (Nat.dvd_trans hb (Nat.dvd_mul_right 256 _))).mpr hv)
  have d1 (i) : 8 ∣ N i := lift i 1 8 (Nat.one_dvd _) (by decide) (by decide)
    (fun a => by cases a <;> decide)
  have d2 (i) : 64 ∣ N i := lift i 8 64 (d1 _) (by decide) (by decide)
    (fun a => by cases a <;> decide)
  exact lift j 64 256 (d2 _) (by decide) (by decide) (fun a => by cases a <;> decide)

theorem shadow_edge {s q} (h : Track s q) (j : Nat) :
    width (s j)*shadow (s (j+1)) (q (j+1)) =
      mult (s j)*shadow (s j) (q j) + carry (s j) := by
  have he := numEdge (h.next j) (large h j) (large h (j+1)) (h.edge j)
  have h0 := Nat.mul_div_cancel' (integral h j)
  have h1 := Nat.mul_div_cancel' (integral h (j+1))
  change 256*shadow (s j) (q j) = _ at h0
  change 256*shadow (s (j+1)) (q (j+1)) = _ at h1
  rw [← h0, ← h1] at he
  apply Nat.mul_left_cancel (n := 256) (by decide)
  simpa only [Nat.mul_add, Nat.mul_left_comm] using he

def step (n : Nat) : Nat := if n%2=0 then n/2 else (3*n+1)/2
def iter (k n : Nat) : Nat := Nat.rec n (fun _ v => step v) k
def Bad (n : Nat) : Prop := ∀ k, iter k n ≠ 1

private theorem iter_add (a b n : Nat) : iter (a+b) n = iter b (iter a n) := by
  induction b with
  | zero => rfl
  | succ b ih => change step (iter (a+b) n) = step (iter b (iter a n)); rw [ih]

private theorem trap (k n : Nat) (h : n=1 ∨ n=2) : iter k n=1 ∨ iter k n=2 := by
  induction k with
  | zero => exact h
  | succ k ih =>
    change step (iter k n)=1 ∨ step (iter k n)=2
    rcases ih with e|e <;> rw [e] <;> decide

private theorem bad_of_blocks (x : Nat → Nat) (above : ∀ j, 2 < x j)
    (edge : ∀ j, ∃ k : Nat, 1 ≤ k ∧ iter k (x j)=x (j+1)) (j : Nat) : Bad (x j) := by
  have visits (i : Nat) : ∃ k, i ≤ k ∧ iter k (x j)=x (j+i) := by
    induction i with
    | zero => exact ⟨0, by decide, rfl⟩
    | succ i ih =>
      obtain ⟨k,hk,he⟩ := ih
      obtain ⟨u,hu,hit⟩ := edge (j+i)
      exact ⟨k+u, by omega, by rw [iter_add,he]; exact hit⟩
  intro t ht
  obtain ⟨k,hk,he⟩ := visits t
  have eq : k=t+(k-t) := by omega
  rw [eq, iter_add, ht] at he
  have hc := trap (k-t) 1 (Or.inl rfl)
  have hq := above (j+t)
  omega

private theorem halve (x : Nat) : step (2*x)=x := by simp [step]

private theorem halving (n x : Nat) : iter n (2^n*x)=x := by
  induction n with
  | zero => simp only [Nat.pow_zero, Nat.one_mul]; rfl
  | succ n ih =>
    rw [show n+1=1+n by omega, iter_add]
    change iter n (step (2^(1+n)*x))=x
    rw [Nat.pow_add, Nat.pow_one, Nat.mul_assoc, halve, ih]

private theorem gap (x r k : Nat) (hx : x%2=1) (he : 2^(k+1)*r=3*x+1) :
    iter (k+1) x=r := by
  have hstep : step x = 2^k*r := by
    simp [step, show x%2≠0 by omega, ← he, Nat.pow_succ, Nat.mul_right_comm]
  rw [show k+1=1+k by omega, iter_add]
  change iter k (step x)=r
  rw [hstep, halving]

private theorem literalBlock (x r : Nat) (hx : x%2=1) (hr : r%2=1)
    (edge : 8*r=9*x+5 ∨ 8*r=9*x+7 ∨ 32*r=9*x+5 ∨ 32*r=9*x+7 ∨ 32*r=9*x+11) :
    ∃ k : Nat, 1 ≤ k ∧ iter k x=r := by
  rcases edge with h|h|h|h|h
  · let z := (3*x+1)/2
    have e := gap x z 0 hx (by dsimp [z]; omega)
    have f := gap z r 1 (by dsimp [z]; omega) (by dsimp [z]; omega)
    exact ⟨1+2, by decide, by rw [iter_add, e, f]⟩
  · let z := (3*x+1)/4
    have e := gap x z 1 hx (by dsimp [z]; omega)
    have f := gap z r 0 (by dsimp [z]; omega) (by dsimp [z]; omega)
    exact ⟨2+1, by decide, by rw [iter_add, e, f]⟩
  · let z := (3*x+1)/2
    have e := gap x z 0 hx (by dsimp [z]; omega)
    have f := gap z r 3 (by dsimp [z]; omega) (by dsimp [z]; omega)
    exact ⟨1+4, by decide, by rw [iter_add, e, f]⟩
  · let z := (3*x+1)/4
    have e := gap x z 1 hx (by dsimp [z]; omega)
    have f := gap z r 2 (by dsimp [z]; omega) (by dsimp [z]; omega)
    exact ⟨2+3, by decide, by rw [iter_add, e, f]⟩

  · let z := (3*x+1)/8
    have e := gap x z 2 hx (by dsimp [z]; omega)
    have f := gap z r 1 (by dsimp [z]; omega) (by dsimp [z]; omega)
    exact ⟨3+2, by decide, by rw [iter_add, e, f]⟩

private theorem inputBad {s q} (h : Track s q) (j : Nat) : Bad (q j) := by
  apply bad_of_blocks q (fun i => by have := large h i; omega) _ j
  intro i
  apply literalBlock _ _ (h.odd i) (h.odd (i+1))
  have he := h.edge i
  cases hs : s i <;> simp [hs, width, inputCarry] at he <;> omega

private theorem literalTarget (s : Phase) (x r : Nat)
    (eq : width s*r=mult s*x+carry s) :
    ∃ k : Nat, 1≤k ∧ iter k x=r := by
  cases s <;> simp [width,mult,carry] at eq
  · have hh : x%8=3 := by omega
    let v := x/8
    have hx : x=8*v+3 := by dsimp [v]; omega
    have e0 : step (8*v+3)=12*v+5 := by unfold step; split <;> omega
    have e1 : step (12*v+5)=18*v+8 := by unfold step; split <;> omega
    have e2 : step (18*v+8)=9*v+4 := by unfold step; split <;> omega
    refine ⟨3, by decide, ?_⟩
    change step (step (step (x)))=r
    rw [hx, e0, e1, e2]
    omega
  · have hh : x%8=7 := by omega
    let v := x/8
    have hx : x=8*v+7 := by dsimp [v]; omega
    have e0 : step (8*v+7)=12*v+11 := by unfold step; split <;> omega
    have e1 : step (12*v+11)=18*v+17 := by unfold step; split <;> omega
    have e2 : step (18*v+17)=27*v+26 := by unfold step; split <;> omega
    refine ⟨3, by decide, ?_⟩
    change step (step (step (x)))=r
    rw [hx, e0, e1, e2]
    omega
  · have hh : x%8=6 := by omega
    let v := x/8
    have hx : x=8*v+6 := by dsimp [v]; omega
    have e0 : step (8*v+6)=4*v+3 := by unfold step; split <;> omega
    have e1 : step (4*v+3)=6*v+5 := by unfold step; split <;> omega
    have e2 : step (6*v+5)=9*v+8 := by unfold step; split <;> omega
    refine ⟨3, by decide, ?_⟩
    change step (step (step (x)))=r
    rw [hx, e0, e1, e2]
    omega
  · have hh : x%8=4 := by omega
    let v := x/8
    have hx : x=8*v+4 := by dsimp [v]; omega
    have e0 : step (8*v+4)=4*v+2 := by unfold step; split <;> omega
    have e1 : step (4*v+2)=2*v+1 := by unfold step; split <;> omega
    have e2 : step (2*v+1)=3*v+2 := by unfold step; split <;> omega
    refine ⟨3, by decide, ?_⟩
    change step (step (step (x)))=r
    rw [hx, e0, e1, e2]
    omega
  · have hh : x%8=6 := by omega
    let v := x/8
    have hx : x=8*v+6 := by dsimp [v]; omega
    have e0 : step (8*v+6)=4*v+3 := by unfold step; split <;> omega
    have e1 : step (4*v+3)=6*v+5 := by unfold step; split <;> omega
    have e2 : step (6*v+5)=9*v+8 := by unfold step; split <;> omega
    refine ⟨3, by decide, ?_⟩
    change step (step (step (x)))=r
    rw [hx, e0, e1, e2]
    omega
  · have hh : x%32=21 := by omega
    let v := x/32
    have hx : x=32*v+21 := by dsimp [v]; omega
    have e0 : step (32*v+21)=48*v+32 := by unfold step; split <;> omega
    have e1 : step (48*v+32)=24*v+16 := by unfold step; split <;> omega
    have e2 : step (24*v+16)=12*v+8 := by unfold step; split <;> omega
    have e3 : step (12*v+8)=6*v+4 := by unfold step; split <;> omega
    have e4 : step (6*v+4)=3*v+2 := by unfold step; split <;> omega
    refine ⟨5, by decide, ?_⟩
    change step (step (step (step (step (x)))))=r
    rw [hx, e0, e1, e2, e3, e4]
    omega
  · have hh : x%32=3 := by omega
    let v := x/32
    have hx : x=32*v+3 := by dsimp [v]; omega
    have e0 : step (32*v+3)=48*v+5 := by unfold step; split <;> omega
    have e1 : step (48*v+5)=72*v+8 := by unfold step; split <;> omega
    have e2 : step (72*v+8)=36*v+4 := by unfold step; split <;> omega
    have e3 : step (36*v+4)=18*v+2 := by unfold step; split <;> omega
    have e4 : step (18*v+2)=9*v+1 := by unfold step; split <;> omega
    refine ⟨5, by decide, ?_⟩
    change step (step (step (step (step (x)))))=r
    rw [hx, e0, e1, e2, e3, e4]
    omega
private theorem shadowBad {s q} (h : Track s q) (j : Nat) : Bad (shadow (s j) (q j)) := by
  let y := fun i => shadow (s i) (q i)
  apply bad_of_blocks y _ _ j
  · intro i
    have hl := large h i
    dsimp [y,shadow]
    cases s i <;> simp [numerator] <;> omega
  · intro i
    apply literalTarget
    exact shadow_edge h i

private theorem drop1 {x y z : Nat} (hx : 17≤x) (h0 : 8*y=9*x+7)
    (h1 : 32*z=9*y+5) : z<x ∧ z<(3*x+1)/4 := by
  have a : 256*z=81*x+103 := by omega
  constructor <;> omega

private theorem drop2 {x y z w : Nat} (hx : 17≤x) (h0 : 8*y=9*x+7)
    (h1 : 8*z=9*y+7) (h2 : 32*w=9*z+5) : w<x ∧ w<(3*x+1)/4 := by
  have e : 64*z=81*x+119 := by omega
  have f : 2048*w=729*x+1391 := by omega
  constructor <;> omega

private theorem mark_floor {s q} (h : Track s q) (j : Nat) :
    ∃ m : Nat, 0<m ∧ m%2=1 ∧ m<q j ∧
      m<(3*q j+1)/(if width (s j)=8 then 4 else 2) ∧ Bad m := by
  have hi := large h j
  have eq0 := h.edge j
  have eq1 := h.edge (j+1)
  have eq2 := h.edge (j+2)
  have freeCase (hf : s j=free ∨ s j=beginTile) :
      ∃ m : Nat, 0<m ∧ m%2=1 ∧ m<q j ∧ m<(3*q j+1)/4 ∧ Bad m := by
    let m := shadow (s j) (q j)
    have sel := shadow_edge h j
    have ho : m%2=1 := by
      change width (s j)*_=mult (s j)*m+carry (s j) at sel
      rcases hf with h0|h0 <;> simp [h0,width,mult,carry] at sel <;> omega
    refine ⟨m, ?_, ho, ?_, ?_, shadowBad h j⟩ <;>
      rcases hf with h0|h0 <;> dsimp [m,shadow] <;> simp [h0,numerator] <;> omega
  have pDrop {i} (_eq : 32*q (i+1)=9*q i+5) (r : Nat) (hr : q (i+1)<r) (hm : q (i+1)<q j) :
      ∃ m : Nat, 0<m ∧ m%2=1 ∧ m<q j ∧ m<r ∧ Bad m :=
    ⟨q (i+1), by have := large h (i+1); omega, h.odd _, hm, hr, inputBad h _⟩
  cases hj : s j <;> simp [hj,width,inputCarry] at eq0 ⊢
  · exact freeCase (Or.inl hj)
  · exact freeCase (Or.inr hj)
  · have f1 : s (j+1)=oneSingle ∨ s (j+1)=onePair := by
      have e := h.next j
      rw [hj] at e
      generalize s (j+1)=v at e ⊢
      cases e <;> simp
    have f2 : s (j+2)=lastPaid ∨ s (j+2)=pairLead := by
      have e := h.next (j+1)
      rcases f1 with a|a <;> rw [a] at e <;>
        generalize s (j+2)=v at e ⊢ <;> cases e <;> simp
    have a : 8*q (j+2)=9*q (j+1)+7 := by rcases f1 with z|z <;> simpa [z,width,inputCarry] using eq1
    have b : 32*q (j+3)=9*q (j+2)+5 := by rcases f2 with z|z <;> simpa [z,width,inputCarry] using eq2
    have dd := drop2 hi eq0 a b
    exact pDrop b _ dd.2 dd.1
  · have f : s (j+1)=lastPaid := by
      have e := h.next j
      rw [hj] at e
      generalize s (j+1)=v at e ⊢
      cases e
      rfl
    have a : 32*q (j+2)=9*q (j+1)+5 := by simpa [f,width,inputCarry] using eq1
    have dd := drop1 hi eq0 a
    exact pDrop a _ dd.2 dd.1
  · have f : s (j+1)=pairLead := by
      have e := h.next j
      rw [hj] at e
      generalize s (j+1)=v at e ⊢
      cases e
      rfl
    have a : 32*q (j+2)=9*q (j+1)+5 := by simpa [f,width,inputCarry] using eq1
    have dd := drop1 hi eq0 a
    exact pDrop a _ dd.2 dd.1
  · exact pDrop eq0 _ (by omega) (by omega)
  · exact pDrop eq0 _ (by omega) (by omega)

def mark (a b c d : Bool) : Phase :=
  if a then (if b then pairLead else lastPaid) else
  if b then (if c then onePair else oneSingle) else
  if c then two else if d then beginTile else free

private theorem mark_next (a b c d e : Bool)
    (endPair : a=true → b=true → c=false)
    (apart : a=true → b=false → c=false ∧ d=false) :
    Next (mark a b c d) (mark b c d e) := by
  cases a <;> cases b <;> cases c <;> cases d <;> cases e <;>
    simp_all [mark] <;> constructor

private theorem mark_width (a b c d : Bool) :
    width (mark a b c d) = (if a then 32 else 8) ∧
    inputCarry (mark a b c d) = (if a then 5 else 7) := by
  cases a <;> cases b <;> cases c <;> cases d <;> decide

/-- Singletons and pairs can be intermingled arbitrarily, with at least three
light blocks between clusters. Every actual odd phase has a smaller bad source. -/
theorem mixed_descent (p : Nat → Bool) (q : Nat → Nat)
    (endPair : ∀ i, p i=true → p (i+1)=true → p (i+2)=false)
    (apart : ∀ i, p i=true → p (i+1)=false → p (i+2)=false ∧ p (i+3)=false)
    (edge : ∀ i, (if p i then 32 else 8)*q (i+1)=9*q i+(if p i then 5 else 7))
    (odd : ∀ i, q i%2=1) (j : Nat) :
    ∃ m : Nat, 0<m ∧ m%2=1 ∧ m<q j ∧
      m<(3*q j+1)/(if p j then 2 else 4) ∧ Bad m := by
  let s := fun i => mark (p i) (p (i+1)) (p (i+2)) (p (i+3))
  have tr : Track s q := {
    next := fun i => mark_next _ _ _ _ _ (endPair i) (apart i)
    edge := fun i => by
      dsimp [s]
      rw [(mark_width _ _ _ _).1, (mark_width _ _ _ _).2]
      exact edge i
    odd := odd }
  have result := mark_floor tr j
  have w := (mark_width (p j) (p (j+1)) (p (j+2)) (p (j+3))).1
  change width (s j) = _ at w
  rw [w] at result
  cases h : p j <;> simpa [h] using result

#print axioms mixed_descent
end Collatz.MixedPaid
