import Std

namespace Collatz.SeparatedDescent

inductive Phase where
  | far | six | five | four | three | two | one | paid
  deriving DecidableEq

open Phase

inductive Next : Phase → Phase → Prop
  | ff : Next far far
  | fs : Next far six
  | s5 : Next six five
  | s4 : Next five four
  | s3 : Next four three
  | s2 : Next three two
  | s1 : Next two one
  | s0 : Next one paid
  | pf : Next paid far
  | ps : Next paid six

def width : Phase → Nat
  | paid => 32
  | _ => 8

def inputCarry : Phase → Nat
  | paid => 5
  | _ => 7

def outputCarry : Phase → Nat
  | six | two | one => 5
  | _ => 7

def debit : Phase → Nat
  | far | six => 75565
  | five => 141101
  | four => 149293
  | three => 158509
  | two => 168877
  | one => 246077
  | paid => 332927

def numerator (s : Phase) (q : Nat) : Nat := 251349*q - debit s

def shadow (s : Phase) (q : Nat) : Nat := numerator s q / 262144

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
    width s*numerator t r=9*numerator s q+262144*outputCarry s := by
  cases h <;> simp [width, inputCarry, outputCarry, numerator, debit] at * <;> omega

/-- Every formal dyadic numerator along the one actual path is integral after
division by 2^18. Each of its next six real edges contributes at least 2^3. -/
theorem integral {s q} (h : Track s q) (j : Nat) : 262144 ∣ numerator (s j) (q j) := by
  let N := fun i => numerator (s i) (q i)
  have lift (i d : Nat) (hd : d ∣ N (i+1)) (hb : 8*d ∣ 262144)
      (hc : Nat.Coprime (8*d) 9) : 8*d ∣ N i := by
    have hw : 8 ∣ width (s i) := by cases s i <;> decide
    have he := numEdge (h.next i) (large h i) (large h (i+1)) (h.edge i)
    change width (s i)*N (i+1)=9*N i+262144*outputCarry (s i) at he
    have hv := Nat.mul_dvd_mul hw hd
    rw [he] at hv
    exact hc.dvd_of_dvd_mul_left ((Nat.dvd_add_iff_left
      (Nat.dvd_trans hb (Nat.dvd_mul_right 262144 _))).mpr hv)
  have d1 (i) : 8 ∣ N i := lift i 1 (Nat.one_dvd _) (by decide) (by decide)
  have d2 (i) : 64 ∣ N i := lift i 8 (d1 _) (by decide) (by decide)
  have d3 (i) : 512 ∣ N i := lift i 64 (d2 _) (by decide) (by decide)
  have d4 (i) : 4096 ∣ N i := lift i 512 (d3 _) (by decide) (by decide)
  have d5 (i) : 32768 ∣ N i := lift i 4096 (d4 _) (by decide) (by decide)
  exact lift j 32768 (d5 _) (by decide) (by decide)

theorem shadow_edge {s q} (h : Track s q) (j : Nat) :
    width (s j)*shadow (s (j+1)) (q (j+1)) =
      9*shadow (s j) (q j) + outputCarry (s j) := by
  have he := numEdge (h.next j) (large h j) (large h (j+1)) (h.edge j)
  have h0 := Nat.mul_div_cancel' (integral h j)
  have h1 := Nat.mul_div_cancel' (integral h (j+1))
  change 262144*shadow (s j) (q j) = _ at h0
  change 262144*shadow (s (j+1)) (q (j+1)) = _ at h1
  rw [← h0, ← h1] at he
  apply Nat.mul_left_cancel (n := 262144) (by decide)
  simpa only [Nat.mul_add, Nat.mul_left_comm] using he

private theorem shadow_size {s q} (h : Track s q) (j : Nat) :
    2 < shadow (s j) (q j) ∧ shadow (s j) (q j) < q j := by
  have hj := large h j
  cases hs : s j <;> simp [shadow, numerator, debit] <;> omega

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
    (edge : 8*r=9*x+5 ∨ 8*r=9*x+7 ∨ 32*r=9*x+5 ∨ 32*r=9*x+7) :
    ∃ k : Nat, 1 ≤ k ∧ iter k x=r := by
  rcases edge with h|h|h|h
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

private theorem inputBad {s q} (h : Track s q) (j : Nat) : Bad (q j) := by
  apply bad_of_blocks q (fun i => by have := large h i; omega) _ j
  intro i
  apply literalBlock _ _ (h.odd i) (h.odd (i+1))
  have he := h.edge i
  cases hs : s i <;> simp [hs, width, inputCarry] at he <;> omega

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

private def down : Phase → Phase
  | six => five | five => four | four => three | three => two
  | two => one | one => paid | _ => far

private theorem deterministic {s t : Phase} (h : Next s t) (hf : s ≠ far)
    (hp : s ≠ paid) : t = down s := by cases h <;> simp_all [down]

private theorem extendL {v u x r z : Nat} (a : v*(r+7)=u*(x+7))
    (b : 8*z=9*r+7) : (v*8)*(z+7)=(u*9)*(x+7) := by
  have he : 8*(z+7)=9*(r+7) := by omega
  calc
    (v*8)*(z+7) = v*(8*(z+7)) := Nat.mul_assoc _ _ _
    _ = v*(9*(r+7)) := by rw [he]
    _ = 9*(v*(r+7)) := by ac_rfl
    _ = 9*(u*(x+7)) := by rw [a]
    _ = (u*9)*(x+7) := by ac_rfl

private theorem finishP {v u x r z : Nat} (a : v*(r+7)=u*(x+7))
    (b : 32*z=9*r+5) : v*(32*z+58)=(9*u)*(x+7) := by
  have he : 32*z+58=9*(r+7) := by omega
  calc
    v*(32*z+58) = v*(9*(r+7)) := by rw [he]
    _ = 9*(v*(r+7)) := by ac_rfl
    _ = 9*(u*(x+7)) := by rw [a]
    _ = (9*u)*(x+7) := by ac_rfl

private theorem drop1 {x z : Nat} (h : 17≤x) (eq : 8*(32*z+58)=81*(x+7)) :
    z < (3*x+1)/4 := by omega

private theorem drop2 {x z : Nat} (h : 17≤x) (eq : 64*(32*z+58)=729*(x+7)) :
    z < (3*x+1)/4 := by omega

private theorem drop6 {x z : Nat} (h : 17≤x) (eq : 262144*(32*z+58)=4782969*(x+7)) :
    z < (3*x+1)/4 := by omega

private theorem short_drop {s q} (h : Track s q) (j : Nat)
    (hs : s j=one ∨ s j=two ∨ s j=six) : ∃ k, q k < (3*q j+1)/4 := by
  have forward {i : Nat} {a : Phase} (hh : s i=a) (hf : a≠far) (hp : a≠paid) :
      s (i+1)=down a ∧ 8*q (i+1)=9*q i+7 := by
    have he := h.edge i
    rw [hh] at he
    refine ⟨?_, ?_⟩
    · rw [← hh]
      exact deterministic (h.next i) (hh ▸ hf) (hh ▸ hp)
    · cases a <;> simp_all [width, inputCarry]
  have terminal {i : Nat} (hh : s i=paid) : 32*q (i+1)=9*q i+5 := by
    simpa [hh, width, inputCarry] using h.edge i
  have lower := large h j
  rcases hs with hh|hh|hh
  · obtain ⟨h1, e1⟩ := forward hh (by decide) (by decide)
    have a0 : 1*(q j+7)=1*(q j+7) := rfl
    have a1 := extendL a0 e1
    have last := finishP a1 (terminal h1)
    refine ⟨j+1+1, ?_⟩
    exact drop1 lower last
  · obtain ⟨h1, e1⟩ := forward hh (by decide) (by decide)
    obtain ⟨h2, e2⟩ := forward h1 (by decide) (by decide)
    have a0 : 1*(q j+7)=1*(q j+7) := rfl
    have a1 := extendL a0 e1
    have a2 := extendL a1 e2
    have last := finishP a2 (terminal h2)
    refine ⟨j+1+1+1, ?_⟩
    exact drop2 lower last
  · obtain ⟨h1, e1⟩ := forward hh (by decide) (by decide)
    obtain ⟨h2, e2⟩ := forward h1 (by decide) (by decide)
    obtain ⟨h3, e3⟩ := forward h2 (by decide) (by decide)
    obtain ⟨h4, e4⟩ := forward h3 (by decide) (by decide)
    obtain ⟨h5, e5⟩ := forward h4 (by decide) (by decide)
    obtain ⟨h6, e6⟩ := forward h5 (by decide) (by decide)
    have a0 : 1*(q j+7)=1*(q j+7) := rfl
    have a1 := extendL a0 e1
    have a2 := extendL a1 e2
    have a3 := extendL a2 e3
    have a4 := extendL a3 e4
    have a5 := extendL a4 e5
    have a6 := extendL a5 e6
    have last := finishP a6 (terminal h6)
    refine ⟨j+1+1+1+1+1+1+1, ?_⟩
    exact drop6 lower last

def intermediate (s : Phase) (q : Nat) : Nat :=
  if s=paid then (3*q+1)/2 else (3*q+1)/4

private theorem quarter_lt {x y : Nat} (h : x+2≤y) : (3*x+1)/4 < (3*y+1)/4 := by omega

/-- Every original odd phase has a strictly smaller positive odd nonconverger,
including intermediates in the switched L blocks. -/
theorem descent_all_phases {s q} (h : Track s q) (j x : Nat)
    (hx : x=q j ∨ x=intermediate (s j) (q j)) :
    ∃ y, y%2=1 ∧ 0<y ∧ y<x ∧ Bad y := by
  let y := shadow (s j) (q j)
  obtain ⟨positive, small, bad⟩ := smaller_boundary h j
  have yodd := shadowOdd h j
  have lower := large h j
  rcases hx with hx|hx
  · subst x
    exact ⟨y, yodd, by omega, small, bad⟩
  subst x
  by_cases hp : s j=paid
  · exact ⟨y, yodd, by omega, by simp [intermediate, hp]; omega, bad⟩
  simp [intermediate, hp]
  by_cases hs : s j=one ∨ s j=two ∨ s j=six
  · obtain ⟨k,hk⟩ := short_drop h j hs
    exact ⟨q k, h.odd k, by have := large h k; omega, hk, inputBad h k⟩
  have he := shadow_edge h j
  have fixed : width (s j)=8 ∧ outputCarry (s j)=7 := by
    cases e : s j <;> simp_all [width, outputCarry]
  rw [fixed.1,fixed.2] at he
  change 8*shadow (s (j+1)) (q (j+1))=9*y+7 at he
  have yr := shadowOdd h (j+1)
  change y%2=1 at yodd
  change 2<y at positive
  change y<q j at small
  let z := (3*y+1)/4
  have ez : 4*z=3*y+1 := by dsimp [z]; omega
  have eo : z%2=1 := by dsimp [z]; omega
  have ezstep := gap y z 1 yodd ez
  refine ⟨z, eo, by omega, ?_, ?_⟩
  · have qo := h.odd j
    have margin : y+2 ≤ q j := by omega
    exact quarter_lt margin
  · intro k hit
    apply bad (2+k)
    rw [iter_add, ezstep, hit]


/-- Unmarked input language: true means P, false means L. -/
def SixSeparated (p : Nat → Bool) : Prop :=
  ∀ j, p j=true → ∀ k, 1≤k → k≤6 → p (j+k)=false

def classify (p : Nat → Bool) (j : Nat) : Phase :=
  if p j then paid else if p (j+1) then one else if p (j+2) then two else
  if p (j+3) then three else if p (j+4) then four else if p (j+5) then five else
  if p (j+6) then six else far

private theorem classify_next {p} (sep : SixSeparated p) (j : Nat) :
    Next (classify p j) (classify p (j+1)) := by
  by_cases h0 : p j=true
  · have h1 := sep j h0 1 (by decide) (by decide)
    have h2 := sep j h0 2 (by decide) (by decide)
    have h3 := sep j h0 3 (by decide) (by decide)
    have h4 := sep j h0 4 (by decide) (by decide)
    have h5 := sep j h0 5 (by decide) (by decide)
    have h6 := sep j h0 6 (by decide) (by decide)
    cases h7 : p (j+7) <;> simp [classify, Nat.add_assoc, *] <;> constructor
  by_cases h1 : p (j+1)=true
  · simp [classify, *]; constructor
  by_cases h2 : p (j+2)=true
  · simp [classify, Nat.add_assoc, *]; constructor
  by_cases h3 : p (j+3)=true
  · simp [classify, Nat.add_assoc, *]; constructor
  by_cases h4 : p (j+4)=true
  · simp [classify, Nat.add_assoc, *]; constructor
  by_cases h5 : p (j+5)=true
  · simp [classify, Nat.add_assoc, *]; constructor
  by_cases h6 : p (j+6)=true
  · simp [classify, Nat.add_assoc, *]; constructor
  cases h7 : p (j+7) <;> simp [classify, Nat.add_assoc, *] <;> constructor

/-- No supplied annotation, integrality guard, or presumed convergence status.
The starting odd state may be a block boundary or its first odd successor. -/
theorem separated_descent {p : Nat → Bool} {q : Nat → Nat} (sep : SixSeparated p)
    (odd : ∀ j, q j%2=1)
    (edges : ∀ j, if p j then 32*q (j+1)=9*q j+5 else 8*q (j+1)=9*q j+7)
    (j x : Nat) (hx : x=q j ∨ x=(if p j then (3*q j+1)/2 else (3*q j+1)/4)) :
    ∃ y, y%2=1 ∧ 0<y ∧ y<x ∧ Bad y := by
  have htrack : Track (classify p) q := {
    next := classify_next sep
    odd := odd
    edge := by
      intro i
      have hi := edges i
      cases v : p i
      · simp [v] at hi
        simp [classify, v]
        repeat' split
        all_goals exact hi
      · simpa [classify, v, width, inputCarry] using hi }
  apply descent_all_phases htrack j x
  rcases hx with a|a
  · exact Or.inl a
  apply Or.inr
  cases v : p j
  · have hn : classify p j ≠ paid := by
      simp [classify, v]
      repeat' split
      all_goals decide
    simpa [intermediate, hn, v] using a
  · simpa [intermediate, classify, v] using a

#print axioms separated_descent

#print axioms integral
#print axioms shadow_edge
#print axioms smaller_boundary
#print axioms descent_all_phases
end Collatz.SeparatedDescent
