import Std

namespace Collatz.RampMerger

def step (n : Nat) : Nat := if n%2=0 then n/2 else (3*n+1)/2
def iter (k n : Nat) : Nat := Nat.rec n (fun _ x => step x) k

private theorem iter_add (a b n : Nat) : iter (a+b) n = iter b (iter a n) := by
  induction b with
  | zero => rfl
  | succ b ih => change step (iter (a+b) n) = step (iter b (iter a n)); rw [ih]

private theorem odd_run (n v : Nat) (hv : 0<v) :
    iter n (2^n*v-1) = 3^n*v-1 := by
  induction n generalizing v with
  | zero => simp only [Nat.pow_zero, Nat.one_mul]; rfl
  | succ n ih =>
    have pos : 0<2^n*v := Nat.mul_pos (Nat.pow_pos (by decide)) hv
    have h : step (2^(n+1)*v-1) = 2^n*(3*v)-1 := by
      rw [Nat.pow_succ,show 2^n*2*v=2*(2^n*v) by ac_rfl,
        show 2^n*(3*v)=3*(2^n*v) by ac_rfl]
      unfold step; split <;> omega
    rw [show n+1=1+n by omega, iter_add]
    change iter n (step (2^(1+n)*v-1))=3^(1+n)*v-1
    rw [show 1+n=n+1 by omega,h, ih (3*v) (by omega), Nat.pow_succ, Nat.mul_assoc]

private theorem paid_three_light_target {y w : Nat} (h : 8192*w=243*y+3406) :
    iter 13 y=w := by
  have hh : 243*(y+250)=8192*(w+7) := by omega
  have div : 8192 ∣ y+250 :=
    (show Nat.Coprime 8192 243 by decide).dvd_of_dvd_mul_left ⟨_,hh⟩
  obtain ⟨t,ht⟩ := div
  cases t with
  | zero => omega
  | succ t =>
    have hy : y=8192*t+7942 := by omega
    have hw : w=243*t+236 := by omega
    rw [hy,hw]
    have e0 : step (8192*t+7942)=4096*t+3971 := by unfold step; split <;> omega
    have e1 : step (4096*t+3971)=6144*t+5957 := by unfold step; split <;> omega
    have e2 : step (6144*t+5957)=9216*t+8936 := by unfold step; split <;> omega
    have e3 : step (9216*t+8936)=4608*t+4468 := by unfold step; split <;> omega
    have e4 : step (4608*t+4468)=2304*t+2234 := by unfold step; split <;> omega
    have e5 : step (2304*t+2234)=1152*t+1117 := by unfold step; split <;> omega
    have e6 : step (1152*t+1117)=1728*t+1676 := by unfold step; split <;> omega
    have e7 : step (1728*t+1676)=864*t+838 := by unfold step; split <;> omega
    have e8 : step (864*t+838)=432*t+419 := by unfold step; split <;> omega
    have e9 : step (432*t+419)=648*t+629 := by unfold step; split <;> omega
    have e10 : step (648*t+629)=972*t+944 := by unfold step; split <;> omega
    have e11 : step (972*t+944)=486*t+472 := by unfold step; split <;> omega
    have e12 : step (486*t+472)=243*t+236 := by unfold step; split <;> omega
    change step (step (step (step (step (step (step (step (step (step (step (step (step (8192*t+7942)))))))))))))=243*t+236
    rw [e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12]

/-- The ramp endpoint merges across one paid block and three light blocks. -/
theorem paid_three_light_core {y q a b c w : Nat}
    (hy : 2*(y+1)=27*(q+7)) (hp : 32*a=9*q+5)
    (h1 : 8*b=9*a+7) (h2 : 8*c=9*b+7) (h3 : 8*w=9*c+7) :
    iter 13 y=w := by
  apply paid_three_light_target
  have h₁ : 256*b=81*q+269 := by
    calc
      256*b=32*(8*b) := by omega
      _=32*(9*a+7) := by rw [h1]
      _=9*(32*a)+224 := by omega
      _=81*q+269 := by rw [hp]; omega
  have h₂ : 2048*c=729*q+4213 := by
    calc
      2048*c=256*(8*c) := by omega
      _=256*(9*b+7) := by rw [h2]
      _=9*(256*b)+1792 := by omega
      _=729*q+4213 := by rw [h₁]; omega
  have h₃ : 16384*w=6561*q+52253 := by
    calc
      16384*w=2048*(8*w) := by omega
      _=2048*(9*c+7) := by rw [h3]
      _=9*(2048*c)+14336 := by omega
      _=6561*q+52253 := by rw [h₂]; omega
  clear hp h1 h2 h3 h₁ h₂
  omega

/-- For arbitrary leading length r, the parameter v is the half-cofactor at
the end of the light run: q_start+7=2^(3*r+1)*v and q_paid+7=2*9^r*v. -/
theorem ramp_merger (r v q₀ q a b c w : Nat) (hr : 3≤r) (hv : 0<v)
    (hs : q₀+7=2^(3*r+1)*v) (he : q+7=2*9^r*v)
    (hp : 32*a=9*q+5) (h1 : 8*b=9*a+7) (h2 : 8*c=9*b+7)
    (h3 : 8*w=9*c+7) :
    ∃ m, 0<m ∧ m%2=1 ∧ m<(3*q₀+1)/4 ∧ m<q₀ ∧ iter (2*r+3+13) m=w := by
  let X := 2^(2*r+3)*v
  have hn : 2*r+3+1≤3*r+1 := by omega
  have pw := Nat.pow_le_pow_right (n:=2) (by decide) hn
  have twice : 2*X ≤ q₀+7 := by
    rw [hs]; dsimp [X]
    rw [show 2*(2^(2*r+3)*v)=2^(2*r+3+1)*v by rw [Nat.pow_succ 2 (2*r+3)]; ac_rfl]
    exact Nat.mul_le_mul_right v pw
  have pw8 : 16 ≤ 2^(2*r+3) := Nat.pow_le_pow_right (n:=2) (by decide) (show 4≤2*r+3 by omega)
  have big : 16≤X := Nat.le_trans pw8 (Nat.le_mul_of_pos_right _ hv)
  have small : 0<X-1 ∧ X-1<(3*q₀+1)/4 ∧ X-1<q₀ := by
    clear hp h1 h2 h3 he hs; omega
  have evenX : X=2*(2^(2*r+2)*v) := by
    dsimp [X]; rw [Nat.pow_succ 2 (2*r+2)]; ac_rfl
  have odd : (X-1)%2=1 := by clear hp h1 h2 h3 he hs; omega
  refine ⟨X-1, small.1, odd, small.2.1, small.2.2, ?_⟩
  rw [iter_add,show iter (2*r+3) (X-1)=3^(2*r+3)*v-1 from odd_run _ _ hv]
  apply paid_three_light_core _ hp h1 h2 h3
  rw [he,Nat.pow_add,Nat.pow_mul]
  change 2*(9^r*27*v-1+1)=27*(2*9^r*v)
  have nz : 0<9^r*27*v := Nat.mul_pos (Nat.mul_pos (Nat.pow_pos (by decide)) (by decide)) hv
  rw [Nat.sub_add_cancel (show 1≤9^r*27*v from nz)]
  ac_rfl


/-- The half-cofactor used by the ramp is forced by the raw light boundary equations. -/
private theorem cofactor (q : Nat → Nat) (r : Nat)
    (ls : ∀ i, i<r → 8*q (i+1)=9*q i+7) (ho : q r%2=1) :
    ∃ v, 0<v ∧ q 0+7=2^(3*r+1)*v ∧ q r+7=2*9^r*v := by
  have h (i : Nat) (hi : i≤r) : 8^i*(q i+7)=9^i*(q 0+7) := by
    induction i with
    | zero => simp
    | succ i ih =>
      have hprev := ih (by omega)
      have e := ls i (by omega)
      have ec : 8*(q (i+1)+7)=9*(q i+7) := by omega
      calc
        8^(i+1)*(q (i+1)+7)=8^i*(8*(q (i+1)+7)) := by rw [Nat.pow_succ]; ac_rfl
        _=8^i*(9*(q i+7)) := by rw [ec]
        _=9*(8^i*(q i+7)) := by ac_rfl
        _=9^(i+1)*(q 0+7) := by rw [hprev,Nat.pow_succ]; ac_rfl
  have pair := h r (Nat.le_refl _)
  let t := (q r+7)/2
  have ht : q r+7=2*t := by dsimp [t]; omega
  have div : 2^(3*r+1) ∣ 9^r*(q 0+7) := by
    refine ⟨t,?_⟩
    rw [←pair,ht,Nat.pow_succ 2 (3*r),Nat.pow_mul]
    change 8^r*(2*t)=8^r*2*t
    ac_rfl
  have cop := ((show Nat.Coprime 2 9 by decide).pow_left (3*r+1)).pow_right r
  obtain ⟨v,hv⟩ := cop.dvd_of_dvd_mul_left div
  refine ⟨v, ?_,hv,?_⟩
  · by_cases hz : v=0
    · simp [hz] at hv
    · omega
  · apply Nat.eq_of_mul_eq_mul_left (n:=8^r) (Nat.pow_pos (by decide))
    rw [pair,hv,Nat.pow_succ 2 (3*r),Nat.pow_mul]
    change 9^r*(8^r*2*v)=8^r*(2*9^r*v)
    ac_rfl

/-- Raw unmarked finite source path: r light blocks, paid, light, light,
light. Its end belongs to the literal trajectory of a smaller positive source. -/
theorem light_paid_merger (q : Nat → Nat) (r : Nat) (hr : 3≤r)
    (ho : q r%2=1) (ls : ∀ i, i<r → 8*q (i+1)=9*q i+7)
    (p : 32*q (r+1)=9*q r+5)
    (a : 8*q (r+2)=9*q (r+1)+7) (b : 8*q (r+3)=9*q (r+2)+7)
    (c : 8*q (r+4)=9*q (r+3)+7) :
    ∃ m, 0<m ∧ m%2=1 ∧ m<(3*q 0+1)/4 ∧ m<q 0 ∧ iter (2*r+3+13) m=q (r+4) := by
  obtain ⟨v,hv,hs,he⟩ := cofactor q r ls ho
  exact ramp_merger r v (q 0) (q r) _ _ _ _ hr hv hs he p a b c

#print axioms light_paid_merger

#print axioms paid_three_light_core
#print axioms ramp_merger
end Collatz.RampMerger
