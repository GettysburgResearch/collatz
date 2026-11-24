import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Integer reconstruction of the two-block fixed-clock ratio-five family.
The Fourier and Haar results are in the companion written proof. -/
set_option autoImplicit false
namespace Collatz.MarkedRouter

def step (x : ℤ) : ℤ := if x % 2 = 0 then x/2 else (3*x+1)/2

def tick (z : ℤ × ℕ) : ℤ × ℕ :=
  (step z.1, z.2 + (if z.1 % 2 = 0 then 0 else 1))

def trace : ℕ → ℤ → ℤ × ℕ
  | 0, x => (x,0)
  | n+1, x => tick (trace n x)

theorem trace_add (n m : ℕ) (x : ℤ) :
    trace (n+m) x = ((trace m (trace n x).1).1,
                     (trace n x).2 + (trace m (trace n x).1).2) := by
  induction m with
  | zero => simp [trace]
  | succ m ih => simp [trace, ih, tick, Nat.add_assoc]

private theorem trace_evenStart (m : ℕ) (x : ℤ) :
    trace (m+1) (2*x) = trace m x := by
  rw [Nat.add_comm, trace_add]
  simp [trace, tick, step]

private theorem trace_halves (m : ℕ) (x : ℤ) :
    trace m ((2:ℤ)^m*x) = (x,0) := by
  induction m with
  | zero => simp [trace]
  | succ m ih =>
    convert trace_evenStart m ((2:ℤ)^m*x) |>.trans ih using 2
    ring

/-- The five positive clocks before the first return are decided on the
entire binary cylinder, including the affine first-return endpoint. -/
theorem first_return_six (s : ℤ) :
    trace 6 (64*s+49) = (9*s+7,2) ∧
    trace 6 (5*(64*s+49)) = (5*(9*s+7),2) ∧
    ∀ h : ℕ, 0 < h → h < 6 →
      ¬ ((trace h (64*s+49)).2 = (trace h (5*(64*s+49))).2 ∧
         5*(trace h (64*s+49)).1 = (trace h (5*(64*s+49))).1) := by
  have ev (a b : ℤ) (j : ℕ) (h : a=2*b) : tick (a,j)=(b,j) := by
    subst a; simp [tick,step]
  have od (a b : ℤ) (j : ℕ) (mod : a%2≠0) (h : 3*a+1=2*b) :
      tick (a,j)=(b,j+1) := by
    simp [tick,step,mod]; omega
  have l1 : trace 1 (64*s+49) = (96*s+74,1) := by
    change tick (64*s+49,0) = _
    apply od <;> omega
  have l2 : trace 2 (64*s+49) = (48*s+37,1) := by
    change tick (trace 1 _) = _
    rw [l1]
    apply ev
    omega
  have l3 : trace 3 (64*s+49) = (72*s+56,2) := by
    change tick (trace 2 _) = _
    rw [l2]
    apply od <;> omega
  have l4 : trace 4 (64*s+49) = (36*s+28,2) := by
    change tick (trace 3 _) = _
    rw [l3]
    apply ev
    omega
  have l5 : trace 5 (64*s+49) = (18*s+14,2) := by
    change tick (trace 4 _) = _
    rw [l4]
    apply ev
    omega
  have l6 : trace 6 (64*s+49) = (9*s+7,2) := by
    change tick (trace 5 _) = _
    rw [l5]
    apply ev
    omega
  have r1 : trace 1 (5*(64*s+49)) = (480*s+368,1) := by
    change tick (5*(64*s+49),0) = _
    apply od <;> omega
  have r2 : trace 2 (5*(64*s+49)) = (240*s+184,1) := by
    change tick (trace 1 _) = _
    rw [r1]
    apply ev
    omega
  have r3 : trace 3 (5*(64*s+49)) = (120*s+92,1) := by
    change tick (trace 2 _) = _
    rw [r2]
    apply ev
    omega
  have r4 : trace 4 (5*(64*s+49)) = (60*s+46,1) := by
    change tick (trace 3 _) = _
    rw [r3]
    apply ev
    omega
  have r5 : trace 5 (5*(64*s+49)) = (30*s+23,1) := by
    change tick (trace 4 _) = _
    rw [r4]
    apply ev
    omega
  have r6 : trace 6 (5*(64*s+49)) = (5*(9*s+7),2) := by
    change tick (trace 5 _) = _
    rw [r5]
    apply od <;> omega
  refine ⟨l6,r6,?_⟩
  intro h lo hi
  interval_cases h
  · simp only [l1,r1]; omega
  · simp only [l2,r2]; omega
  · simp only [l3,r3]; omega
  · simp only [l4,r4]; omega
  · simp only [l5,r5]; omega

/-- Full ordinary positive realization at one padded word, including its
source parity and both actual endpoints and odd counts. -/
theorem padded (b : ℕ) (x q : ℤ) (hq : 0 < q)
    (row : (2:ℤ)^(6+b)*q=9*x+7) :
    0 < x ∧ x%2=1 ∧ trace (6+b) x = (q,2) ∧
      trace (6+b) (5*x) = (5*q,2) := by
  rw [pow_add] at row
  norm_num at row
  have eqn : 64*((2:ℤ)^b*q)=9*x+7 := by linarith only [row]
  let s := (x-49)/64
  have hx : x=64*s+49 := by dsimp [s]; omega
  have y : 9*s+7=(2:ℤ)^b*q := by omega
  have hy : 0 < (2:ℤ)^b*q := by positivity
  obtain ⟨left, right, _⟩ := first_return_six s
  rw [← hx, y] at left right
  have yp : 5*((2:ℤ)^b*q)=(2:ℤ)^b*(5*q) := by ring
  refine ⟨by omega, by omega, ?_, ?_⟩
  · rw [trace_add, left]
    simp [trace_halves]
  · rw [trace_add, right]
    simp [yp,trace_halves]

/-- The final single congruence reconstructs an integral middle unit. This
justifies applying the physical padded-word theorem twice without guessing
its high ternary digits. -/
theorem pair_split (u v : ℕ) (x q : ℤ)
    (row : (2:ℤ)^(u+v)*q=81*x+7*(2:ℤ)^v+63) :
    ∃ y : ℤ, (2:ℤ)^u*q=9*y+7 ∧ (2:ℤ)^v*y=9*x+7 ∧ ¬3∣y := by
  rw [pow_add] at row
  have mul : (2:ℤ)^v*((2:ℤ)^u*q-7)=9*(9*x+7) := by nlinarith only [row]
  have co : IsCoprime (9:ℤ) 2 := ⟨1,-4,by norm_num⟩
  obtain ⟨y,hy⟩ := (co.pow_right (n:=v)).dvd_of_dvd_mul_left
    (show (9:ℤ) ∣ 2^v*(2^u*q-7) from ⟨9*x+7,mul⟩)
  have h' : (2:ℤ)^v*y=9*x+7 := by rw [hy] at mul; linarith [mul]
  refine ⟨y, by linarith, h', ?_⟩
  rintro ⟨w,hw⟩
  rw [hw] at h'
  have eq3 : 3*((2:ℤ)^v*w)=9*x+7 := by linarith only [h']
  omega

/-- The common total gives a true two-arm path at the supplied ordinary q. -/
theorem physical_pair (s t : ℕ) (x q : ℤ) (hq : 0 < q)
    (row : (2:ℤ)^((6+s)+(6+t))*q = 81*x+7*(2:ℤ)^(6+t)+63) :
    0 < x ∧ x%2=1 ∧ trace ((6+s)+(6+t)) x = (q,4) ∧
      trace ((6+s)+(6+t)) (5*x) = (5*q,4) := by
  obtain ⟨y,hy,hx,_⟩ := pair_split (6+s) (6+t) x q row
  obtain ⟨pos,_,ly,ry⟩ := padded s y q hq hy
  obtain ⟨xpos,odd,lx,rx⟩ := padded t x y pos hx
  refine ⟨xpos,odd,?_,?_⟩
  · rw [Nat.add_comm (6+s),trace_add,lx]; simp [ly]
  · rw [Nat.add_comm (6+s),trace_add,rx]; simp [ry]

/-- Outward order. The head is the pair closest to the supplied root. -/
def clock : List (ℕ × ℕ) → ℕ
  | [] => 0
  | (s,t)::w => ((6+s)+(6+t)) + clock w

def carry : List (ℕ × ℕ) → ℤ
  | [] => 0
  | (_,t)::w => 2^clock w*(7*(2:ℤ)^(6+t)+63)+81*carry w

/-- One whole affine equality decodes every pair and both ordinary paths. -/
theorem physical_chain (w : List (ℕ × ℕ)) (x q : ℤ) (hq : 0 < q)
    (row : (2:ℤ)^clock w*q=81^w.length*x+carry w) :
    0 < x ∧ trace (clock w) x=(q,4*w.length) ∧
      trace (clock w) (5*x)=(5*q,4*w.length) := by
  induction w generalizing q with
  | nil => simp [clock,carry] at row; subst q; simp [clock,trace,hq]
  | cons pair w ih =>
    obtain ⟨s,t⟩ := pair
    simp only [clock,carry,List.length_cons,pow_add (2:ℤ) ((6+s)+(6+t)) (clock w),
      pow_succ (81:ℤ)] at row
    let T := (6+s)+(6+t)
    let c : ℤ := 7*2^(6+t)+63
    have mul : (2:ℤ)^clock w*(2^T*q-c)=81*(81^w.length*x+carry w) := by
      dsimp [T,c]
      nlinarith only [row]
    have co : IsCoprime (81:ℤ) 2 := ⟨1,-40,by norm_num⟩
    obtain ⟨y,hy⟩ := (co.pow_right (n:=clock w)).dvd_of_dvd_mul_left
      (show (81:ℤ) ∣ 2^clock w*(2^T*q-c) from ⟨_,mul⟩)
    have first : (2:ℤ)^T*q=81*y+c := by omega
    have tail : (2:ℤ)^clock w*y=81^w.length*x+carry w := by
      rw [hy] at mul
      nlinarith only [mul]
    obtain ⟨yp,_,ly,ry⟩ := physical_pair s t y q hq
      (by simpa only [T,c,add_assoc] using first)
    obtain ⟨xp,lx,rx⟩ := ih y yp tail
    refine ⟨xp,?_,?_⟩
    · change trace (T+clock w) x=_
      rw [Nat.add_comm T,trace_add,lx]; simp [T,ly,Nat.mul_add]
    · change trace (T+clock w) (5*x)=_
      rw [Nat.add_comm T,trace_add,rx]; simp [T,ry,Nat.mul_add]

/-- The extra ternary digits impose an actual ordinary source residue. -/
theorem realize_residue (w : List (ℕ × ℕ)) (q a : ℤ) (m : ℕ) (hq : 0 < q)
    (h : (81:ℤ)^w.length*3^m ∣
      (2:ℤ)^clock w*q-carry w-81^w.length*a) :
    ∃ x : ℤ, 0 < x ∧ (3:ℤ)^m ∣ x-a ∧
      trace (clock w) x=(q,4*w.length) ∧
      trace (clock w) (5*x)=(5*q,4*w.length) := by
  obtain ⟨z,hz⟩ := h
  let x : ℤ := a+3^m*z
  have row : (2:ℤ)^clock w*q=81^w.length*x+carry w := by
    dsimp [x]; nlinarith only [hz]
  obtain ⟨pos,l,r⟩ := physical_chain w x q hq row
  exact ⟨x,pos,⟨z,by dsimp [x]; ring⟩,l,r⟩

#print axioms trace_add
#print axioms first_return_six
#print axioms padded
#print axioms pair_split
#print axioms physical_pair
#print axioms physical_chain
#print axioms realize_residue
end Collatz.MarkedRouter
