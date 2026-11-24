import Std

/- The generic parity and block traversal lemmas are adapted from PR192,
d2081d1cd2410e6004eaee9f9b13c5553afaf3f4, descent_Separated.lean. -/
namespace Collatz.PaidPairs

inductive Phase where
  | free | four | three | two | one | first | second
  deriving DecidableEq
open Phase

inductive Next : Phase → Phase → Prop
  | ff : Next free free
  | f4 : Next free four
  | n3 : Next four three
  | n2 : Next three two
  | n1 : Next two one
  | np : Next one first
  | pp : Next first second
  | pf : Next second free
  | p4 : Next second four

def width : Phase → Nat
  | first | second => 32
  | _ => 8

def inputCarry : Phase → Nat
  | first | second => 5
  | _ => 7

def outputCarry : Phase → Nat
  | four | three | two => 7
  | second => 11
  | _ => 5

def offset : Phase → Nat
  | free | four => 1381
  | three => 2405
  | two => 3557
  | one => 4853
  | first => 5287
  | second => 1639

def numerator (s : Phase) (q : Nat) := 3123*q + offset s
def shadow (s : Phase) (q : Nat) := numerator s q / 4096

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
    (_hq : 17 ≤ q) (_hr : 17 ≤ r)
    (edge : width s*r=9*q+inputCarry s) :
    width s*numerator t r=9*numerator s q+4096*outputCarry s := by
  cases h <;> simp [width, inputCarry, outputCarry, numerator, offset] at * <;> omega

/-- Every formal dyadic numerator along the one actual path is integral after
division by 2^12. Each of its next four real edges contributes at least 2^3. -/
theorem integral {s q} (h : Track s q) (j : Nat) : 4096 ∣ numerator (s j) (q j) := by
  let N := fun i => numerator (s i) (q i)
  have lift (i d : Nat) (hd : d ∣ N (i+1)) (hb : 8*d ∣ 4096)
      (hc : Nat.Coprime (8*d) 9) : 8*d ∣ N i := by
    have hw : 8 ∣ width (s i) := by cases s i <;> decide
    have he := numEdge (h.next i) (large h i) (large h (i+1)) (h.edge i)
    change width (s i)*N (i+1)=9*N i+4096*outputCarry (s i) at he
    have hv := Nat.mul_dvd_mul hw hd
    rw [he] at hv
    exact hc.dvd_of_dvd_mul_left ((Nat.dvd_add_iff_left
      (Nat.dvd_trans hb (Nat.dvd_mul_right 4096 _))).mpr hv)
  have d1 (i) : 8 ∣ N i := lift i 1 (Nat.one_dvd _) (by decide) (by decide)
  have d2 (i) : 64 ∣ N i := lift i 8 (d1 _) (by decide) (by decide)
  have d3 (i) : 512 ∣ N i := lift i 64 (d2 _) (by decide) (by decide)
  have d4 (i) : 4096 ∣ N i := lift i 512 (d3 _) (by decide) (by decide)
  exact d4 j

theorem shadow_edge {s q} (h : Track s q) (j : Nat) :
    width (s j)*shadow (s (j+1)) (q (j+1)) =
      9*shadow (s j) (q j) + outputCarry (s j) := by
  have he := numEdge (h.next j) (large h j) (large h (j+1)) (h.edge j)
  have h0 := Nat.mul_div_cancel' (integral h j)
  have h1 := Nat.mul_div_cancel' (integral h (j+1))
  change 4096*shadow (s j) (q j) = _ at h0
  change 4096*shadow (s (j+1)) (q (j+1)) = _ at h1
  rw [← h0, ← h1] at he
  apply Nat.mul_left_cancel (n := 4096) (by decide)
  simpa only [Nat.mul_add, Nat.mul_left_comm] using he

private theorem shadow_size {s q} (h : Track s q) (j : Nat) :
    2 < shadow (s j) (q j) ∧ shadow (s j) (q j) < q j := by
  have hj := large h j
  cases hs : s j <;> simp [shadow, numerator, offset] <;> omega

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

theorem smaller_boundary {s q} (h : Track s q) (j : Nat) :
    2 < shadow (s j) (q j) ∧ shadow (s j) (q j) < q j ∧ Bad (shadow (s j) (q j)) := by
  let y := fun i => shadow (s i) (q i)
  have odd (i) : y i%2=1 := by
    have he := shadow_edge h i
    change width (s i)*y (i+1)=9*y i+outputCarry (s i) at he
    cases hs : s i <;> simp [hs, width, outputCarry] at he <;> omega
  refine ⟨(shadow_size h j).1, (shadow_size h j).2,
    bad_of_blocks y (fun i => (shadow_size h i).1) ?_ j⟩
  intro i
  apply literalBlock _ _ (odd i) (odd (i+1))
  have he := shadow_edge h i
  change width (s i)*y (i+1)=9*y i+outputCarry (s i) at he
  cases hs : s i <;> simp [hs, width, outputCarry] at he <;> omega

private theorem shadowOdd {s q} (h : Track s q) (j : Nat) : shadow (s j) (q j)%2=1 := by
  let y := fun i => shadow (s i) (q i)
  change y j%2=1
  have he := shadow_edge h j
  change width (s j)*y (j+1)=9*y j+outputCarry (s j) at he
  cases hs : s j <;> simp [hs, width, outputCarry] at he <;> omega


theorem bad_preimage {m y k : Nat} (hy : Bad y) (hk : iter k m=y) : Bad m := by
  intro t ht
  have e : iter t y = iter k 1 := by
    rw [← hk, ← iter_add, Nat.add_comm k t, iter_add, ht]
  have trapAt := trap k 1 (Or.inl rfl)
  rcases trapAt with h | h
  · exact hy t (e.trans h)
  · apply hy (t+1)
    change step (iter t y)=1
    rw [e,h]
    decide

set_option maxHeartbeats 2000000 in
/-- A single fixed positive odd partner lies below both odd input floors. -/
theorem smaller_both {s q} (h : Track s q) (j : Nat) :
    ∃ m : Nat, 0 < m ∧ m%2=1 ∧ m < q j ∧
      m < (3*q j+1)/(if width (s j)=8 then 4 else 2) ∧ Bad m := by
  let y := shadow (s j) (q j)
  obtain ⟨hy2, hsmall, hbad⟩ := smaller_boundary h j
  have ho : y%2=1 := shadowOdd h j
  have hnum := Nat.mul_div_cancel' (integral h j)
  change 4096*y = 3123*q j + offset (s j) at hnum
  have hlarge := large h j
  have case4 (hz : y%9=4) (hsz : (8*y-5)/9 < (3*q j+1)/4) :
      ∃ m : Nat, 0<m ∧ m%2=1 ∧ m<q j ∧ m<(3*q j+1)/4 ∧ Bad m := by
    let m := (8*y-5)/9
    have h1 : step m=(4*y-1)/3 := by simp [step, m]; split <;> omega
    have h2 : step ((4*y-1)/3)=2*y := by simp [step]; split <;> omega
    have he : iter 3 m=y := by change step (step (step m))=y; rw [h1,h2,halve]
    exact ⟨m, by dsimp [m]; omega, by dsimp [m]; omega, by dsimp [m]; omega,
      hsz, bad_preimage hbad he⟩
  have case2 (hz : y%3=2) (hsz : (2*y-1)/3 < (3*q j+1)/4) :
      ∃ m : Nat, 0<m ∧ m%2=1 ∧ m<q j ∧ m<(3*q j+1)/4 ∧ Bad m := by
    let m := (2*y-1)/3
    have he : iter 1 m=y := by change step m=y; simp [step,m]; split <;> omega
    exact ⟨m, by dsimp [m]; omega, by dsimp [m]; omega, by dsimp [m]; omega,
      hsz, bad_preimage hbad he⟩
  cases hs : s j <;> simp [hs,width,offset] at hnum ⊢
  · exact case4 (by omega) (by omega)
  · exact case4 (by omega) (by omega)
  · exact case2 (by omega) (by omega)
  · exact case2 (by omega) (by omega)
  · exact case2 (by omega) (by omega)
  · exact ⟨y, by change 2<y at hy2; omega,ho,hsmall,by omega,hbad⟩
  · exact ⟨y, by change 2<y at hy2; omega,ho,hsmall,by omega,hbad⟩

/-- Four letters of lookahead also classify an initial partial pair or light run. -/
def mark (a b c d e : Bool) : Phase :=
  if a then (if b then first else second) else
  if b then one else if c then two else if d then three else if e then four else free

private theorem mark_next (a b c d e f : Bool)
    (join : a=false → b=true → c=true)
    (endPair : a=true → b=true → c=false)
    (apart : a=true → b=false → c=false ∧ d=false ∧ e=false) :
    Next (mark a b c d e) (mark b c d e f) := by
  cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> cases f <;>
    simp_all [mark] <;> constructor

private theorem mark_width (a b c d e : Bool) :
    width (mark a b c d e) = (if a then 32 else 8) ∧
    inputCarry (mark a b c d e) = (if a then 5 else 7) := by
  cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> decide

/-- Ordinary, unannotated input: paid runs are pairs with at least four
light letters between pairs. At time zero a suffix can start mid-pair. -/
theorem paired_descent (p : Nat → Bool) (q : Nat → Nat)
    (join : ∀ i, p i=false → p (i+1)=true → p (i+2)=true)
    (endPair : ∀ i, p i=true → p (i+1)=true → p (i+2)=false)
    (apart : ∀ i, p i=true → p (i+1)=false →
       p (i+2)=false ∧ p (i+3)=false ∧ p (i+4)=false)
    (edge : ∀ i, (if p i then 32 else 8)*q (i+1)=9*q i+(if p i then 5 else 7))
    (odd : ∀ i, q i%2=1) (j : Nat) :
    ∃ m : Nat, 0<m ∧ m%2=1 ∧ m<q j ∧
      m<(3*q j+1)/(if p j then 2 else 4) ∧ Bad m := by
  let s := fun i => mark (p i) (p (i+1)) (p (i+2)) (p (i+3)) (p (i+4))
  have tr : Track s q := {
    next := fun i => mark_next _ _ _ _ _ _ (join i) (endPair i) (apart i)
    edge := fun i => by
      dsimp [s]
      rw [(mark_width _ _ _ _ _).1, (mark_width _ _ _ _ _).2]
      exact edge i
    odd := odd }
  have result := smaller_both tr j
  have w := (mark_width (p j) (p (j+1)) (p (j+2)) (p (j+3)) (p (j+4))).1
  change width (s j) = _ at w
  rw [w] at result
  cases h : p j <;> simpa [h] using result

#print axioms paired_descent
#print axioms integral
#print axioms shadow_edge
#print axioms smaller_both
end Collatz.PaidPairs
