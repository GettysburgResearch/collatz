import Std

namespace Collatz.TriplePaid

def step (n : Nat) : Nat := if n%2=0 then n/2 else (3*n+1)/2
def iter (k n : Nat) : Nat := Nat.rec n (fun _ x => step x) k

private theorem iter_add (a b n : Nat) : iter (a+b) n = iter b (iter a n) := by
  induction b with
  | zero => rfl
  | succ b ih => change step (iter (a+b) n) = step (iter b (iter a n)); rw [ih]

def half (q : Nat) : Nat := (q-7)/2

private theorem Lword {x r : Nat} (h : 8*r=9*x+7) : iter 3 x=r := by
  have hx : x%2=1 := by omega
  have hc : ((3*x+1)/2)%2=0 := by omega
  have hd : (((3*x+1)/2)/2)%2=1 := by omega
  change step (step (step x))=r
  simp [step, show x%2 ≠ 0 by omega, hc, show (((3*x+1)/2)/2)%2≠0 by omega]
  omega

private theorem Pword {x r : Nat} (h : 32*r=9*x+5) : iter 5 x=r := by
  have hx : x%2=1 := by omega
  have ho : ((3*x+1)/2)%2=1 := by omega
  have e0 : step x=(3*x+1)/2 := by simp [step, show x%2≠0 by omega]
  have e1 : step ((3*x+1)/2)=8*r := by simp [step, show ((3*x+1)/2)%2≠0 by omega]; omega
  have ev (v : Nat) : step (2*v)=v := by simp [step]
  change step (step (step (step (step x))))=r
  rw [e0,e1, show 8*r=2*(4*r) by omega, ev, show 4*r=2*(2*r) by omega, ev, ev]

private theorem triple_target {z r : Nat} (h : 16384*r=729*z+6034) : iter 14 z=r := by
  have hh : 729*(z+13538)=16384*(r+602) := by omega
  have div : 16384 ∣ z+13538 :=
    (show Nat.Coprime 16384 729 by decide).dvd_of_dvd_mul_left ⟨_, hh⟩
  obtain ⟨t,ht⟩ := div
  cases t with
  | zero => omega
  | succ t =>
    have hz : z=16384*t+2846 := by omega
    have hr : r=729*t+127 := by omega
    rw [hz,hr]
    have e0 : step (16384*t+2846)=8192*t+1423 := by unfold step; split <;> omega
    have e1 : step (8192*t+1423)=12288*t+2135 := by unfold step; split <;> omega
    have e2 : step (12288*t+2135)=18432*t+3203 := by unfold step; split <;> omega
    have e3 : step (18432*t+3203)=27648*t+4805 := by unfold step; split <;> omega
    have e4 : step (27648*t+4805)=41472*t+7208 := by unfold step; split <;> omega
    have e5 : step (41472*t+7208)=20736*t+3604 := by unfold step; split <;> omega
    have e6 : step (20736*t+3604)=10368*t+1802 := by unfold step; split <;> omega
    have e7 : step (10368*t+1802)=5184*t+901 := by unfold step; split <;> omega
    have e8 : step (5184*t+901)=7776*t+1352 := by unfold step; split <;> omega
    have e9 : step (7776*t+1352)=3888*t+676 := by unfold step; split <;> omega
    have e10 : step (3888*t+676)=1944*t+338 := by unfold step; split <;> omega
    have e11 : step (1944*t+338)=972*t+169 := by unfold step; split <;> omega
    have e12 : step (972*t+169)=1458*t+254 := by unfold step; split <;> omega
    have e13 : step (1458*t+254)=729*t+127 := by unfold step; split <;> omega
    change step (step (step (step (step (step (step (step (step (step (step (step (step (step (16384*t+2846))))))))))))))=729*t+127
    rw [e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13]

private theorem bigP {x y z : Nat} (p : 32*y=9*x+5) (p' : 32*z=9*y+5) :
    9≤x := by
  by_cases hx : 9≤x
  · exact hx
  · have hy : y≤2 := by omega
    have hz : z=0 := by omega
    omega

private theorem bigL {x r : Nat} (eq : 8*r=9*x+7) (ho : r%2=1) : 9≤x := by omega

private theorem composition {x y z w : Nat} (a : 32*y=9*x+5) (b : 32*z=9*y+5)
    (c : 32*w=9*z+5) : 32768*w=729*x+6965 := by
  calc
    32768*w = 1024*(32*w) := by omega
    _ = 1024*(9*z+5) := by rw [c]
    _ = 288*(32*z)+5120 := by omega
    _ = 288*(9*y+5)+5120 := by rw [b]
    _ = 81*(32*y)+6560 := by omega
    _ = 729*x+6965 := by rw [a]; omega

private theorem halfSpec {x : Nat} (h : 9≤x) (o : x%2=1) :
    2*half x+7=x := by unfold half; omega

private theorem small {x : Nat} (h : 9≤x) :
    0<half x ∧ half x < x ∧ half x < (3*x+1)/4 := by unfold half; omega

private theorem halfComposite {q w : Nat} (h : 32768*w=729*q+6965)
    (hs : 2*half q+7=q) : 16384*w=729*half q+6034 := by omega

/-- Physical merger after an arbitrarily long L prefix and a triple P; the
competitor starts at (q₀−7)/2 and uses one fewer shortcut clock. -/
theorem triple_paid_merger (q : Nat → Nat) (n : Nat) (odd : ∀ i, q i%2=1)
    (ls : ∀ i, i<n → 8*q (i+1)=9*q i+7)
    (ps : ∀ i, i<3 → 32*q (n+i+1)=9*q (n+i)+5) :
    0 < half (q 0) ∧ half (q 0)<q 0 ∧ half (q 0)<(3*q 0+1)/4 ∧
    iter (3*n+14) (half (q 0))=iter (3*n+15) (q 0) := by
  have p0 : 32*q (n+1)=9*q n+5 := ps 0 (by decide)
  have p1 : 32*q (n+1+1)=9*q (n+1)+5 := ps 1 (by decide)
  have p2 : 32*q (n+1+1+1)=9*q (n+1+1)+5 := ps 2 (by decide)
  have big (i) (hi : i≤n) : 9≤q i := by
    by_cases z : i=n
    · subst i
      exact bigP p0 p1
    · exact bigL (ls i (by omega)) (odd (i+1))
  have f (i) (hi : i≤n) :
      iter (3*i) (q 0)=q i ∧ iter (3*i) (half (q 0))=half (q i) := by
    induction i with
    | zero => exact ⟨rfl,rfl⟩
    | succ i ih =>
      obtain ⟨f0,f1⟩ := ih (by omega)
      have l := ls i (by omega)
      have h0 := big i (by omega)
      have h1 := big (i+1) hi
      have qo := odd i
      have ro := odd (i+1)
      have lh : 8*half (q (i+1))=9*half (q i)+7 := by simp only [half]; omega
      rw [show 3*(i+1)=3*i+3 by omega]
      exact ⟨by rw [iter_add, f0, Lword l], by rw [iter_add, f1, Lword lh]⟩
  have last : 16384*q (n+1+1+1)=729*half (q n)+6034 := by
    have h0 := big n (by omega)
    have qo := odd n
    have numer := composition p0 p1 p2
    exact halfComposite numer (halfSpec h0 qo)
  have base := big 0 (by omega)
  obtain ⟨hp,hx,hm⟩ := small base
  refine ⟨hp,hx,hm,?_⟩
  obtain ⟨u,v⟩ := f n (by omega)
  rw [iter_add, iter_add, v, u, triple_target last]
  rw [show 15=5+(5+5) by decide, iter_add, Pword p0, iter_add, Pword p1, Pword p2]

#print axioms triple_paid_merger
end Collatz.TriplePaid
