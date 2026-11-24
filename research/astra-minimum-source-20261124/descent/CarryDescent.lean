import Std

set_option maxRecDepth 100000

namespace Collatz.CarryDescent

def T (n : Nat) : Nat := if n%2=0 then n/2 else (3*n+1)/2

def orbit (j n : Nat) : Nat :=
  match j with
  | 0 => n
  | j+1 => orbit j (T n)

def odds (j n : Nat) : Nat :=
  match j with
  | 0 => 0
  | j+1 => n%2 + odds j (T n)

theorem edge_lift (z b : Nat) : T (2*z+b) = 3^(b%2)*z+T b := by
  by_cases h : b%2 = 0
  · have h' : (2*z+b)%2=0 := by omega
    simp [T, h, h']; omega
  · have h' : (2*z+b)%2 ≠ 0 := by omega
    have h1 : b%2=1 := by omega
    simp [T, h1]; omega

theorem lift (h b t : Nat) :
    orbit h (2^h*t+b) = 3^(odds h b)*t+orbit h b := by
  induction h generalizing b t with
  | zero => simp [orbit, odds]
  | succ h ih =>
    have H : T (2^(h+1)*t+b) = 2^h*(3^(b%2)*t)+T b := by
      rw [Nat.pow_succ]
      have he : 2^h*2*t = 2*(2^h*t) := by ac_rfl
      rw [he, edge_lift]
      ac_rfl
    rw [orbit, H, ih, odds, orbit, Nat.pow_add]
    ac_rfl

theorem precondition (t : Nat) :
    orbit 26 (2537983+67108864*t) = T (9767881+258280326*t) ∧
    orbit 26 (3*(2537983+67108864*t)) = T (3*(9767881+258280326*t)) := by
  have first := lift 26 2537983 t
  have second := lift 26 (3*2537983) (3*t)
  have a : odds 26 2537983 = 18 := by decide
  have b : odds 26 (3*2537983) = 18 := by decide
  have c : orbit 26 2537983 = 14651822 := by decide
  have d : orbit 26 (3*2537983) = 43955465 := by decide
  rw [a,c] at first
  rw [b,d] at second
  change orbit 26 (67108864*t+2537983) = 387420489*t+14651822 at first
  change orbit 26 (67108864*(3*t)+7613949) = 387420489*(3*t)+43955465 at second
  have aa : 2537983+67108864*t=67108864*t+2537983 := by omega
  have bb : 3*(2537983+67108864*t)=67108864*(3*t)+7613949 := by omega
  constructor
  · rw [aa,first]; unfold T; split <;> omega
  · rw [bb,second]; unfold T; split <;> omega

theorem stable (s y : Nat) (hy : 3*y=2*(8*s+7)-1) :
    T y = 8*s+7 ∧ orbit 4 (3*y) = orbit 3 (3*(8*s+7)) ∧
    y%8=7 ∧ 3*(y+1)=2*((8*s+7)+1) := by
  refine ⟨?_,?_,?_,?_⟩
  · unfold T; split <;> omega
  · rw [hy]
    have a := lift 4 13 s
    have b := lift 3 21 (3*s)
    change orbit 4 (16*s+13) = 9*s+8 at a
    change orbit 3 (8*(3*s)+21) = 3*(3*s)+8 at b
    have h1 : 2*(8*s+7)-1=16*s+13 := by omega
    have h2 : 3*(8*s+7)=8*(3*s)+21 := by omega
    rw [h1,h2,a,b]; omega
  · omega
  · omega

theorem orbit_add (i j n : Nat) : orbit (i+j) n = orbit j (orbit i n) := by
  induction i generalizing n with
  | zero => simp [orbit]
  | succ i ih => rw [Nat.succ_add, orbit, orbit, ih]

/-- A dyadic perturbation contracts about any reference reaching the standard cycle. -/
theorem cycle_scale (h a k : Nat) (ha : orbit h a = 1) :
    orbit h (2^h*(3*k)+a) = orbit (h+2) (2^h*(4*k)+a) := by
  rw [orbit_add, lift, lift, ha]
  have H : 3^(odds h a)*(4*k)+1 = 2^2*(3^(odds h a)*k)+1 := by
    change _ = 4*(_*k)+1
    ac_rfl
  rw [H, lift]
  change _ = 3*(3^(odds h a)*k)+1
  ac_rfl

/-- The two arms of q = 8192t+8171 and the smaller unit share actual futures. -/
theorem negative_twenty_one (t : Nat) :
    orbit 5 (8192*t+8171)=6912*t+6895 ∧
    orbit 8 (3*(6912*t+6895))=orbit 13 (3*(8192*t+8171)) ∧
    6912*t+6895 < 8192*t+8171 := by
  have a := lift 5 8171 (256*t)
  have b := lift 8 (3*6895) (81*t)
  have c := lift 13 (3*8171) (3*t)
  change orbit 5 (32*(256*t)+8171)=27*(256*t)+6895 at a
  change orbit 8 (256*(81*t)+20685)=27*(81*t)+2182 at b
  change orbit 13 (8192*(3*t)+24513)=729*(3*t)+2182 at c
  have h1 : 8192*t+8171=32*(256*t)+8171 := by omega
  have h2 : 3*(6912*t+6895)=256*(81*t)+20685 := by omega
  have h3 : 3*(8192*t+8171)=8192*(3*t)+24513 := by omega
  refine ⟨?_,?_,?_⟩
  · rw [h1,a]; omega
  · rw [h2,h3,b,c]; omega
  · omega

theorem all_odd (j w : Nat) (hw : 0<w) :
    orbit j (2^j*w-1) = 3^j*w-1 := by
  induction j generalizing w with
  | zero => simp [orbit]
  | succ j ih =>
    have hpos : 0 < 2^j*w := Nat.mul_pos (Nat.pow_pos (by decide)) hw
    have edge (x : Nat) (hx : 0 < x) : T (2*x-1)=3*x-1 := by
      unfold T; split <;> omega
    have hs : 2^(j+1)*w = 2*(2^j*w) := by rw [Nat.pow_succ]; grind
    have hr : 3*(2^j*w)=2^j*(3*w) := by grind
    rw [hs, orbit, edge _ hpos, hr, ih (3*w) (by omega), Nat.pow_succ]
    grind

theorem fixed_ratio (k : Nat) : 3*2^(k+3) < 3^(k+3) := by
  induction k with
  | zero => decide
  | succ k ih =>
    have a : 2^(k+1+3)=2^(k+3)*2 := by rw [← Nat.pow_succ]
    have b : 3^(k+1+3)=3^(k+3)*3 := by rw [← Nat.pow_succ]
    rw [a,b]; omega

theorem adjacent (s : Nat) : orbit 2 ((4*s+3)-1) = orbit 2 (3*(4*s+3)-1) := by
  have a := lift 2 2 s
  have b := lift 2 8 (3*s)
  change orbit 2 (4*s+2)=3*s+2 at a
  change orbit 2 (4*(3*s)+8)=1*(3*s)+2 at b
  have hc : 3*(4*s+3)-1=4*(3*s)+8 := by omega
  rw [hc]
  exact a.trans (by simpa using b.symm)

/-- An adaptive common future for n and n-1 on the downward side. -/
theorem adaptive_down (m a s : Nat) (ha : 0<a) (h : 3^m*a=4*s+3) :
    orbit ((m+1)+2) (2^(m+1)*a-1) =
    orbit ((m+1)+2) ((2^(m+1)*a-1)-1) := by
  have pos : 0<2^m*a := Nat.mul_pos (Nat.pow_pos (by decide)) ha
  have e : T ((2^(m+1)*a-1)-1)=2^m*a-1 := by
    have f : 2^(m+1)*a=2*(2^m*a) := by rw [Nat.pow_succ]; ac_rfl
    rw [f]; unfold T; split <;> omega
  have e' : orbit (m+1) ((2^(m+1)*a-1)-1)=3^m*a-1 := by
    rw [orbit,e,all_odd _ _ ha]
  have f : 3^(m+1)*a=3*(3^m*a) := by rw [Nat.pow_succ]; ac_rfl
  simp only [orbit_add (m+1) 2, all_odd (m+1) a ha, e', f, h]
  exact (adjacent s).symm

#print axioms edge_lift
#print axioms orbit_add
#print axioms adjacent
#print axioms adaptive_down
#print axioms fixed_ratio
#print axioms all_odd
#print axioms negative_twenty_one
#print axioms cycle_scale
#print axioms lift
#print axioms precondition
#print axioms stable

end Collatz.CarryDescent
